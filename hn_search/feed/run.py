"""Commit each step, continue delivery after classifier failure, then exit."""

from contextlib import closing
import os

from stan_ai_client import CodexClient

from hn_search.feed import algolia, classify, lenses, store, telegram


def _log(event, settings, **values):
    fields = " ".join(f"{key}={telegram.safe_error(value, settings.tokens)}" for key, value in values.items())
    print(f"feed {event} {fields}".rstrip(), flush=True)


def run_feed(conn, settings, client, *, opener, clock):
    now = int(clock())
    stories = algolia.fetch_window(now, opener=opener)
    new = store.save_window(conn, settings.lenses, stories, now)
    _log(f"window=[{now - algolia.LOOKBACK_SECONDS},{now})", settings, stories=len(stories), new=new)
    failures, sends, edits = 0, 0, 0
    batches = list(store.batches_to_judge(conn, settings.lenses, stories))
    for number, batch in enumerate(batches, 1):
        try:
            decisions = classify.classify_batch(client, batch)
        except Exception as error:
            _log("classify-failed", settings, error=error)
            failures += 1
            break
        store.save_decisions(conn, decisions, now)
        _log("classify", settings, batch=f"{number}/{len(batches)}", stories=len(batch.stories),
             lenses=len(batch.lenses), matched=sum(bool(decision.categories) for decision in decisions))
    for message in telegram.pack(store.pending_lines(conn, settings, stories)):
        try:
            message_id = telegram.send_message(message, settings.tokens, opener=opener)
        except telegram.TelegramError as error:
            _log("send-failed", settings, chat=message.chat_id, error=error)
            failures += 1
            continue
        store.record_message(conn, message, message_id, now)
        sends += 1
        _log("send", settings, lens=",".join(dict.fromkeys(line.lens for line in message.lines)),
             chat=message.chat_id, lines=len(message.lines), message_id=message_id)
    for message in store.messages_to_edit(conn, settings, stories):
        try:
            telegram.edit_message(message, settings.tokens, opener=opener)
        except telegram.TelegramError as error:
            _log("edit-failed", settings, chat=message.chat_id, message_id=message.telegram_message_id, error=error)
            continue
        store.record_edit(conn, message)
        edits += 1
        _log("edit", settings, chat=message.chat_id, message_id=message.telegram_message_id)
    _log("done", settings, sends=sends, edits=edits, failures=failures)
    if failures:
        raise SystemExit(1)


def feed_command(path, config, *, opener, clock):
    settings = lenses.load_settings(config, os.environ)
    client = CodexClient(default_model=settings.model, default_reasoning_effort=settings.effort,
                         default_permission_mode="default", default_timeout_seconds=300)
    with closing(store.open_feed(path)) as conn:
        run_feed(conn, settings, client, opener=opener, clock=clock)
