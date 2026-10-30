"""A one-second terminal ticker, with plain event lines for pipes."""

import threading
from contextlib import contextmanager


STAGES = ("search", "download", "classify", "analyze", "report")
SPINNER = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"


class Progress:
    def __init__(self, stream, clock):
        self.stream, self.clock = stream, clock
        self.terminal = bool(getattr(stream, "isatty", lambda: False)())
        self.lock = threading.RLock()
        self.summaries = {}
        self.finished = set()
        self.checklist = False
        self.active = None
        self.label = ""
        self.started = 0
        self.drawn = 0
        self.frame = 0
        self.closed = False

    def _clear(self):
        if self.drawn:
            self.stream.write(f"\x1b[{self.drawn}A\r\x1b[J")
            self.drawn = 0

    def _draw(self):
        if not self.terminal:
            return
        with self.lock:
            if self.closed:
                return
            self._clear()
            spinner = SPINNER[self.frame % len(SPINNER)]
            self.frame += 1
            elapsed = max(0, int(self.clock() - self.started))
            if self.checklist:
                lines = []
                for stage in STAGES:
                    mark = "✓" if stage in self.finished else spinner if stage == self.active else "·"
                    lines.append(f"{mark} {stage:8} {self.summaries.get(stage, '')}")
                if self.active:
                    lines.append(f"  {self.label} · {elapsed // 60}m {elapsed % 60:02}s")
            elif self.active:
                lines = [f"{spinner} {self.label} · {elapsed // 60}m {elapsed % 60:02}s"]
            else:
                lines = []
            if lines:
                self.stream.write("\n".join(lines) + "\n")
            self.drawn = len(lines)
            self.stream.flush()

    def event(self, text):
        with self.lock:
            self._clear()
            print(text, file=self.stream, flush=True)

    def update(self, stage, summary, *, done=False):
        self.summaries[stage] = summary
        if done:
            self.finished.add(stage)
        self._draw()

    @contextmanager
    def busy(self, stage, label):
        self.active, self.label, self.started = stage, label, self.clock()
        stop = threading.Event()

        def tick():
            while not stop.wait(1):
                self._draw()

        ticker = threading.Thread(target=tick, daemon=True) if self.terminal else None
        self._draw()
        if ticker:
            ticker.start()
        try:
            yield
        finally:
            stop.set()
            if ticker:
                ticker.join()
            self.active = None
            self._draw()

    def ask(self, ask, prompt="> "):
        # Every ticker has joined before a conversation reaches this method.
        with self.lock:
            self._clear()
        return ask(prompt)

    def close(self):
        # An AI failure may finalize the display before busy() stops its ticker.
        with self.lock:
            if self.closed:
                return
            self.active = None
            self._draw()
            self.drawn = 0
            self.closed = True
