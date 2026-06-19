from __future__ import annotations

from typing import Any, Dict, Optional

from . import mcp
from .http import SlackAPIError, slack_api_call


@mcp.tool(name="views_open")
def views_open(trigger_id: str, view: Dict[str, Any]) -> Dict[str, Any]:
    """Opens a modal view (views.open)."""

    try:
        return slack_api_call("views.open", http_method="POST", json={"trigger_id": trigger_id, "view": view})
    except SlackAPIError as e:
        return {"ok": False, "error": "http_error", "detail": e.message, "status_code": e.status_code}


@mcp.tool(name="views_push")
def views_push(trigger_id: str, view: Dict[str, Any]) -> Dict[str, Any]:
    """Pushes a view onto the modal stack (views.push)."""

    try:
        return slack_api_call("views.push", http_method="POST", json={"trigger_id": trigger_id, "view": view})
    except SlackAPIError as e:
        return {"ok": False, "error": "http_error", "detail": e.message, "status_code": e.status_code}


@mcp.tool(name="views_update")
def views_update(
    view: Dict[str, Any],
    view_id: Optional[str] = None,
    external_id: Optional[str] = None,
    hash: Optional[str] = None,
) -> Dict[str, Any]:
    """Updates an existing view (views.update)."""

    payload: Dict[str, Any] = {"view": view}
    if view_id is not None:
        payload["view_id"] = view_id
    if external_id is not None:
        payload["external_id"] = external_id
    if hash is not None:
        payload["hash"] = hash

    try:
        return slack_api_call("views.update", http_method="POST", json=payload)
    except SlackAPIError as e:
        return {"ok": False, "error": "http_error", "detail": e.message, "status_code": e.status_code}


@mcp.tool(name="views_publish")
def views_publish(user_id: str, view: Dict[str, Any], hash: Optional[str] = None) -> Dict[str, Any]:
    """Publishes a static view for a User's App Home (views.publish)."""

    payload: Dict[str, Any] = {"user_id": user_id, "view": view}
    if hash is not None:
        payload["hash"] = hash

    try:
        return slack_api_call("views.publish", http_method="POST", json=payload)
    except SlackAPIError as e:
        return {"ok": False, "error": "http_error", "detail": e.message, "status_code": e.status_code}
