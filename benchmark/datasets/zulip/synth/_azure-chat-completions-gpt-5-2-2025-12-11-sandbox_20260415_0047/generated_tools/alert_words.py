"""Alert words tools."""

from __future__ import annotations

from typing import Any, Dict, List, Sequence

from .http import zulip_request


JsonDict = Dict[str, Any]


def get_alert_words() -> JsonDict:
    """GET /users/me/alert_words"""
    return zulip_request("GET", "/users/me/alert_words")


def add_alert_words(*, alert_words: Sequence[str]) -> JsonDict:
    """POST /users/me/alert_words"""
    return zulip_request("POST", "/users/me/alert_words", data={"alert_words": list(alert_words)})


def remove_alert_words(*, alert_words: Sequence[str]) -> JsonDict:
    """DELETE /users/me/alert_words"""
    return zulip_request("DELETE", "/users/me/alert_words", data={"alert_words": list(alert_words)})
