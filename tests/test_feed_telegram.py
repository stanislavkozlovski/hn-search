from dataclasses import replace
from http.client import IncompleteRead, InvalidURL
from io import BytesIO
import json
from urllib.error import HTTPError, URLError

from hn_search.feed import Line, Message
from hn_search.feed import telegram
from tests.feed_helpers import TOKEN, FeedCase, RecordingOpener, sent


class TelegramTests(FeedCase):
    def message(self, **changes):
        line = Line("ai-agents", 1, ("agents",), "C++ <templates> & you 🙂", "https://example.com/?a=1&b=2", (6, 19, 31))
        return replace(Message("HN_FEED_TEST_TOKEN", 123, (line,)), **changes)

    def test_html_escaping_history_and_utf16_count(self):
        rendered = telegram.render(self.message())
        self.assertIn("C++ &lt;templates&gt; &amp; you 🙂", rendered)
        self.assertIn("a=1&amp;b=2", rendered)
        self.assertIn("<s>6 points</s> <s>19 points</s> 31 points", rendered)
        self.assertEqual(telegram.utf16_units("🙂"), 2)

    def test_40_long_lines_pack_for_ten_values_and_shared_lens_header(self):
        line = self.message().lines[0]
        lines = tuple(replace(line, story_id=i + 1, title="🙂" * 80, url="https://example.com/" + "x" * 400,
                              lens="databases" if i % 2 else line.lens) for i in range(40))
        messages = list(telegram.pack([self.message(lines=lines)]))
        self.assertGreater(len(messages), 1)
        self.assertEqual(sum(len(message.lines) for message in messages), 40)
        for message in messages:
            self.assertLessEqual(telegram.utf16_units(telegram.render(message, worst_case=True, markup=False)), 4096)
            future = replace(message, lines=tuple(replace(line, shown_points=(99999,) * 10) for line in message.lines))
            self.assertLessEqual(telegram.utf16_units(telegram.render(future, markup=False)), 4096)
        self.assertTrue(telegram.render(messages[0]).startswith("ai-agents, databases"))
        with self.assertRaises(telegram.TelegramError):
            list(telegram.pack([self.message(lines=(replace(line, title="x" * 4096),))]))

    def test_send_payload_and_not_modified_http_400_count_as_success(self):
        opener = RecordingOpener(sent())
        self.assertEqual(telegram.send_message(self.message(), self.settings().tokens, opener=opener), 812)
        self.assertEqual(opener.requests[0]["payload"], {"chat_id": 123, "text": telegram.render(self.message()), "parse_mode": "HTML"})
        self.assertEqual(opener.requests[0]["timeout"], 30)
        body = {"ok": False, "error_code": 400, "description": "Bad Request: message is not modified: unchanged"}
        error = HTTPError(f"https://api.telegram.org/bot{TOKEN}/editMessageText", 400, "bad", {}, BytesIO(json.dumps(body).encode()))
        opener = RecordingOpener(error)
        telegram.edit_message(self.message(telegram_message_id=812), self.settings().tokens, opener=opener)
        self.assertEqual(opener.requests[0]["payload"]["message_id"], 812)

    def test_api_and_transport_errors_never_expose_token_or_request_url(self):
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        cases = [URLError(url), TimeoutError(url), IncompleteRead(b'{"ok":', 10), InvalidURL(url),
                 {"ok": False, "error_code": 403, "description": f"Forbidden {url} {TOKEN}"},
                 HTTPError(url, 403, url, {}, BytesIO(b'{"ok":false,"description":"Forbidden"}')),
                 {"ok": True, "result": {"message_id": True}}]
        for response in cases:
            with self.subTest(response=type(response).__name__), self.assertRaises(telegram.TelegramError) as raised:
                telegram.send_message(self.message(), self.settings().tokens, opener=RecordingOpener(response))
            self.assertIn("HN_FEED_TEST_TOKEN", str(raised.exception))
            self.assertNotIn(TOKEN, str(raised.exception))
            self.assertNotIn("api.telegram.org", str(raised.exception))
