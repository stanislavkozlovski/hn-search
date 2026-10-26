"""Strict TOML configuration; tokens are resolved before opening SQLite."""

import hashlib
import json
from pathlib import Path
import re
import tomllib
from typing import get_args

from stan_ai_client import CodexReasoningEffort

from hn_search.feed import Lens, Settings


def _keys(value, allowed, context):
    if not isinstance(value, dict):
        raise ValueError(f"{context} must be a table")
    unknown = value.keys() - allowed
    if unknown:
        raise ValueError(f"Unknown {context} key: {sorted(unknown)[0]}")


def _text(value, name):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{name} must be a nonempty string")
    return value


def _name(value, context):
    if not isinstance(value, str) or not re.fullmatch(r"[a-z0-9-]+", value):
        raise ValueError(f"{context} must use lowercase letters, digits, and hyphens")
    return value


def load_settings(path, environ):
    with Path(path).open("rb") as source:
        data = tomllib.load(source)
    _keys(data, {"classifier", "lens"}, "config")
    classifier = data.get("classifier", {})
    _keys(classifier, {"model", "effort"}, "classifier")
    model = _text(classifier.get("model", "gpt-6-luna"), "classifier.model")
    effort = classifier.get("effort", "high")
    if effort not in get_args(CodexReasoningEffort):
        raise ValueError("Unknown classifier.effort")
    raw_lenses = data.get("lens")
    if not isinstance(raw_lenses, list) or not raw_lenses:
        raise ValueError("config needs at least one [[lens]]")
    lenses, tokens, names = [], {}, set()
    for raw in raw_lenses:
        _keys(raw, {"name", "bot_token_env", "chat_id", "categories"}, "lens")
        name = _name(raw.get("name"), "lens.name")
        if name in names:
            raise ValueError(f"Repeated lens name: {name}")
        names.add(name)
        token_env = _text(raw.get("bot_token_env"), "lens.bot_token_env")
        if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", token_env):
            raise ValueError("lens.bot_token_env must name an environment variable")
        token = environ.get(token_env)
        if not token:
            raise ValueError(f"Unset bot token environment variable: {token_env}")
        chat_id = raw.get("chat_id")
        if type(chat_id) is not int or not -(2**63) <= chat_id < 2**63:
            raise ValueError("lens.chat_id must be an integer fitting SQLite")
        categories = raw.get("categories")
        if not isinstance(categories, dict) or not categories:
            raise ValueError(f"Lens {name} needs categories")
        for category, description in categories.items():
            _name(category, "category name")
            _text(description, f"category {category}")
        digest = hashlib.sha256(json.dumps(categories, sort_keys=True).encode()).hexdigest()
        lenses.append(Lens(name, token_env, chat_id, categories, digest))
        tokens[token_env] = token
    return Settings(tuple(lenses), tokens, model, effort)
