"""Emoji reaction tools."""

from __future__ import annotations

from typing import Any, Dict, Optional

from .http import zulip_request


JsonDict = Dict[str, Any]


def add_reaction(
    *,
    message_id: int,
    emoji_name: str,
    emoji_code: Optional[str] = None,
    reaction_type: Optional[str] = None,
) -> JsonDict:
    """POST /messages/{message_id}/reactions"""
    data: Dict[str, Any] = {"emoji_name": emoji_name, "emoji_code": emoji_code, "reaction_type": reaction_type}
    return zulip_request("POST", f"/messages/{message_id}/reactions", data=data)


def remove_reaction(
    *,
    message_id: int,
    emoji_name: Optional[str] = None,
    emoji_code: Optional[str] = None,
    reaction_type: Optional[str] = None,
) -> JsonDict:
    """DELETE /messages/{message_id}/reactions"""
    data: Dict[str, Any] = {"emoji_name": emoji_name, "emoji_code": emoji_code, "reaction_type": reaction_type}
    return zulip_request("DELETE", f"/messages/{message_id}/reactions", data=data)
