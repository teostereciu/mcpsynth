"""Core Twilio Account tools."""

from __future__ import annotations

from typing import Any, Dict

from .http import core_get


def account_fetch() -> Dict[str, Any]:
    """Fetch the authenticated account details."""
    return core_get(".json")
