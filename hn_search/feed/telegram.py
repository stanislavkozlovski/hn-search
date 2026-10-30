"""HTML messages with room for score edits and one request per attempt."""

from dataclasses import replace
from html import escape
from http.client import HTTPException
import json
import re
from urllib.error import HTTPError, URLError
from urllib.request import Request

from hn_search.feed import MAX_SHOWN_POINTS

LIMIT = 4096


class TelegramError(Exception):
    """A sanitized error that is safe to put in the journal."""


def utf16_units(text):
    return len(text.encode("utf-16-le")) // 2


def render(message, *, worst_case=False, markup=True):
    lenses = ", ".join(dict.fromkeys(line.lens for line in message.lines))
    count = len(message.lines)
    parts = [f"{lenses} · {count} new {'match' if count == 1 else 'matches'}"]
    text = (lambda value: escape(value, quote=False)) if markup else (lambda value: value)
    for line in message.lines:
        points = line.shown_points
        if worst_case:
            points = (max(99999, *points),) * MAX_SHOWN_POINTS
        history = [f"{value} points" for value in points]
        if markup:
            history = [f"<s>{value}</s>" for value in history[:-1]] + history[-1:]
        links = [f"https://news.ycombinator.com/item?id={line.story_id}"]
        if line.url:
            links.insert(0, line.url)
        parts.append(f"[{', '.join(line.tags)}] {text(line.title)}\n"
                     + " ".join(history) + " · " + " · ".join(text(url) for url in links))
    return parts[0] + "\n\n" + "\n\n--------------------\n\n".join(parts[1:])


def pack(messages):
    for message in messages:
        lines = []
        for line in message.lines:
            candidate = replace(message, lines=tuple([*lines, line]))
            if utf16_units(render(candidate, worst_case=True, markup=False)) > LIMIT:
                if lines:
                    yield replace(message, lines=tuple(lines))
                candidate = replace(message, lines=(line,))
                if utf16_units(render(candidate, worst_case=True, markup=False)) > LIMIT:
                    raise TelegramError(f"{message.bot_token_env}: story {line.story_id} exceeds Telegram's text limit")
                lines = []
            lines.append(line)
        if lines:
            yield replace(message, lines=tuple(lines))


def safe_error(error, tokens):
    message = str(error)
    for token in tokens.values():
        message = message.replace(token, "[redacted]")
    return re.sub(r"https?://api\.telegram\.org/[^\s\"']+", "[Telegram request]", message)


def _request(message, method, tokens, *, opener):
    payload = {"chat_id": message.chat_id}
    if method != "deleteMessage":
        if utf16_units(render(message, markup=False)) > LIMIT:
            raise TelegramError(f"{message.bot_token_env}: message exceeds Telegram's text limit")
        payload.update(text=render(message), parse_mode="HTML", link_preview_options={"is_disabled": True})
    if method != "sendMessage":
        payload["message_id"] = message.telegram_message_id
    token = tokens[message.bot_token_env]
    request = Request(f"https://api.telegram.org/bot{token}/{method}",
                      data=json.dumps(payload).encode(), headers={"Content-Type": "application/json"})
    http_status = None
    try:
        try:
            response = opener(request, timeout=30)
        except HTTPError as error:
            http_status = error.code
            response = error
        with response:
            body = json.load(response)
    except (HTTPException, URLError, OSError, ValueError, UnicodeError) as error:
        # Transport exceptions can contain the complete secret-bearing request URL.
        raise TelegramError(f"{message.bot_token_env}: Telegram request failed ({type(error).__name__})") from None
    if not isinstance(body, dict):
        raise TelegramError(f"{message.bot_token_env}: Invalid Telegram response")
    description = body.get("description", "Invalid Telegram response")
    if (method == "editMessageText" and (http_status or body.get("error_code")) == 400
            and isinstance(description, str) and description.startswith("Bad Request: message is not modified")):
        return None
    if (method == "deleteMessage" and (http_status or body.get("error_code")) == 400
            and description == "Bad Request: message to delete not found"):
        return True
    if http_status is not None or body.get("ok") is not True:
        description = safe_error(description, tokens)
        raise TelegramError(f"{message.bot_token_env}: {description}") from None
    return body.get("result")


def send_message(message, tokens, *, opener):
    result = _request(message, "sendMessage", tokens, opener=opener)
    message_id = result.get("message_id") if isinstance(result, dict) else None
    if type(message_id) is not int or not 0 < message_id < 2**63:
        raise TelegramError(f"{message.bot_token_env}: Invalid Telegram message_id")
    return message_id


def edit_message(message, tokens, *, opener):
    _request(message, "editMessageText", tokens, opener=opener)


def delete_message(message, tokens, *, opener):
    if _request(message, "deleteMessage", tokens, opener=opener) is not True:
        raise TelegramError(f"{message.bot_token_env}: Invalid Telegram delete response")
