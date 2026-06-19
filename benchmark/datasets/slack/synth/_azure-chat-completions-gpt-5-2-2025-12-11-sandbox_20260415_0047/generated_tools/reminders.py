from __future__ import annotations

from typing import Any, Dict, Optional

from . import mcp
from .http import SlackAPIError, slack_api_call


@mcp.tool(name="reminders_add")
def reminders_add(text: str, time: str, user: Optional[str] = None) -> Dict[str, Any]:
    """Creates a reminder (reminders.add)."""

    payload: Dict[str, Any] = {"text": text, "time": time}
    if user is not None:
        payload["user"] = user

    try:
        return slack_api_call("reminders.add", http_method="POST", json=payload)
    except SlackAPIError as e:
        return {"ok": False, "error": "http_error", "detail": e.message, "status_code": e.status_code}


@mcp.tool(name="reminders_list")
def reminders_list() -> Dict[str, Any]:
    """Lists reminders created by or for the calling user (reminders.list)."""

    try:
        return slack_api_call("reminders.list", http_method="GET", params={})
    except SlackAPIError as e:
        return {"ok": False, "error": "http_error", "detail": e.message, "status_code": e.status_code}


@mcp.tool(name="reminders_info")
def reminders_info(reminder: str) -> Dict[str, Any]:
    """Gets information about a reminder (reminders.info)."""

    try:
        return slack_api_call("reminders.info", http_method="GET", params={"reminder": reminder})
    except SlackAPIError as e:
        return {"ok": False, "error": "http_error", "detail": e.message, "status_code": e.status_code}


@mcp.tool(name="reminders_complete")
def reminders_complete(reminder: str) -> Dict[str, Any]:
    """Marks a reminder as complete (reminders.complete)."""

    try:
        return slack_api_call("reminders.complete", http_method="POST", json={"reminder": reminder})
    except SlackAPIError as e:
        return {"ok": False, "error": "http_error", "detail": e.message, "status_code": e.status_code}


@mcp.tool(name="reminders_delete")
def reminders_delete(reminder: str) -> Dict[str, Any]:
    """Deletes a reminder (reminders.delete)."""

    try:
        return slack_api_call("reminders.delete", http_method="POST", json={"reminder": reminder})
    except SlackAPIError as e:
        return {"ok": False, "error": "http_error", "detail": e.message, "status_code": e.status_code}
