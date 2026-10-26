"""Hourly title-and-URL feed, independent of the research catalog."""

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Story:
    id: int
    title: str
    url: str | None
    created_at: int
    points: int


@dataclass(frozen=True)
class Lens:
    name: str
    bot_token_env: str
    chat_id: int
    categories: dict[str, str]
    categories_digest: str


@dataclass(frozen=True)
class Settings:
    lenses: tuple[Lens, ...]
    tokens: dict[str, str] = field(repr=False)
    model: str = "gpt-6-luna"
    effort: str = "high"


@dataclass(frozen=True)
class Batch:
    stories: tuple[Story, ...]
    lenses: tuple[Lens, ...]
    needed: frozenset[tuple[str, int]]


@dataclass(frozen=True)
class Decision:
    lens: str
    story: Story
    categories_digest: str
    categories: tuple[str, ...]


@dataclass(frozen=True)
class Line:
    lens: str
    story_id: int
    tags: tuple[str, ...]
    title: str
    url: str | None
    shown_points: tuple[int, ...]


@dataclass(frozen=True)
class Message:
    bot_token_env: str
    chat_id: int
    lines: tuple[Line, ...]
    telegram_message_id: int | None = None
    id: int | None = None
