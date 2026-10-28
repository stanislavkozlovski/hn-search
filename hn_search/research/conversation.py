"""Approve exactly the table, question, and normalized keywords on screen."""

import copy
from dataclasses import dataclass, field

from .ai import DEFAULT_SETTINGS, run_stage
from .prompts import PROMPTS
from .search import normalize_keywords


def agree_settings(client, cwd, ask, progress):
    screen = copy.deepcopy(DEFAULT_SETTINGS)
    exchange = []
    while True:
        progress.event("Model settings:\n" + "\n".join(
            f"  {stage.replace('_', ' '):16} {value['model']:14} {value['effort']}" for stage, value in screen.items()))
        reply = progress.ask(ask)
        exchange.append({"screen": screen, "reply": reply})
        with progress.busy("settings", "model settings · gpt-6-luna medium"):
            result = run_stage(client, "settings", PROMPTS["settings"].render(
                table=screen, exchange=exchange, reply=reply),
                cwd=cwd, model="gpt-6-luna", effort="medium").output
        revised = {stage: result[stage] for stage in DEFAULT_SETTINGS}
        exchange.append({"result": result})
        if result["note"]:
            progress.event(result["note"])
        if result["approved"] and revised == screen:
            return screen
        screen = revised


@dataclass
class Keywords:
    question: str
    keywords: list
    exchange: list = field(default_factory=list)


def agree_keywords(client, cwd, settings, ask, progress, *, state=None, question=None,
                   first_reply=None, gate=None):
    if state is None:
        state = Keywords(question, [])
    exchange = list(state.exchange)
    screen = Keywords(state.question, list(state.keywords), exchange)
    reply = first_reply
    if gate is not None:
        exchange.append({"gate": gate})
    while True:
        if screen.keywords and reply is None:
            progress.event("Question: " + screen.question + "\nKeywords: " + ", ".join(screen.keywords))
            reply = progress.ask(ask)
        exchange.append({"question": screen.question, "keywords": screen.keywords, "reply": reply})
        prompt = PROMPTS["keywords"].render(question=screen.question, keywords=screen.keywords,
                                           exchange=exchange, reply=reply)
        model, effort = settings["keywords"]["model"], settings["keywords"]["effort"]
        with progress.busy("keywords", f"keywords · {model} {effort}"):
            result = run_stage(client, "keywords", prompt, cwd=cwd, model=model, effort=effort).output
        if not result["question"].strip():
            raise ValueError("keyword reply returned an empty question")
        keywords = normalize_keywords(result["keywords"])
        if not keywords:
            raise ValueError("keyword reply returned no searchable keywords")
        exchange.append({"result": result})
        if result["note"]:
            progress.event(result["note"])
        unchanged = result["question"] == screen.question and keywords == screen.keywords
        if result["approved"] and unchanged:
            return Keywords(screen.question, screen.keywords, exchange)
        screen = Keywords(result["question"], keywords, exchange)
        reply = None
