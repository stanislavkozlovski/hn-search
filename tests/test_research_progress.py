import io
import time
import unittest

from hn_search.research.progress import Progress


class Terminal(io.StringIO):
    def isatty(self):
        return True


class ProgressTests(unittest.TestCase):
    def test_terminal_ticks_then_stops_while_a_prompt_waits(self):
        stream = Terminal()
        progress = Progress(stream, time.monotonic)
        progress.checklist = True
        with progress.busy("classify", "verdict call 1/2"):
            time.sleep(1.05)
        progress.event("relevant 1")

        def ask(prompt):
            value = stream.getvalue()
            time.sleep(0.03)
            self.assertEqual(stream.getvalue(), value)
            return "proceed"

        self.assertEqual(progress.ask(ask), "proceed")
        self.assertIn("\x1b[", stream.getvalue())
        self.assertIn("\x1b[J", stream.getvalue())
        self.assertIn("verdict call 1/2", stream.getvalue())

    def test_pipe_has_only_plain_event_lines(self):
        stream = io.StringIO()
        progress = Progress(stream, time.monotonic)
        with progress.busy("classify", "verdict"):
            progress.event("description 1 complete")
        progress.update("classify", "1/1", done=True)
        progress.event("relevant 1")
        progress.close()
        self.assertEqual(stream.getvalue(), "description 1 complete\nrelevant 1\n")
