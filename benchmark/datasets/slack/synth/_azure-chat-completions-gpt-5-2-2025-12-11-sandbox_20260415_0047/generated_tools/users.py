from __future__ import annotations

from typing import Any, Dict, Optional

from . import mcp
from .http import SlackAPIError, slack_api_call


@mcp.tool(name="users_list")
def users_list(
    limit: Optional[int] = None,
    cursor: Optional[str] = None,
    include_locale: Optional[bool] = None,
    team_id: Optional[str] = None,
) -> Dict[str, Any]:
    """Lists all users in a Slack team (users.list)."""

    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if cursor is not None:
        params["cursor"] = cursor
    if include_locale is not None:
        params["include_locale"] = include_locale
    if team_id is not None:
        params["team_id"] = team_id

    try:
        return slack_api_call("users.list", http_method="GET", params=params)
    except SlackAPIError as e:
        return {"ok": False, "error": "http_error", "detail": e.message, "status_code": e.status_code}


@mcp.tool(name="users_info")
def users_info(user: str, include_locale: Optional[bool] = None) -> Dict[str, Any]:
    """Gets information about a user (users.info)."""

    params: Dict[str, Any] = {"user": user}
    if include_locale is not None:
        params["include_locale"] = include_locale

    try:
        return slack_api_call("users.info", http_method="GET", params=params)
    except SlackAPIError as e:
        return {"ok": False, "error": "http_error", "detail": e.message, "status_code": e.status_code}


@mcp.tool(name="users_lookup_by_email")
def users_lookup_by_email(email: str) -> Dict[str, Any]:
    """Finds a user by email address (users.lookupByEmail)."""

    try:
        return slack_api_call("users.lookupByEmail", http_method="GET", params={"email": email})
    except SlackAPIError as e:
        return {"ok": False, "error": "http_error", "detail": e.message, "status_code": e.status_code}


@mcp.tool(name="users_get_presence")
def users_get_presence(user: str) -> Dict[str, Any]:
    """Gets user presence information (users.getPresence)."""

    try:
        return slack_api_call("users.getPresence", http_method="GET", params={"user": user})
    except SlackAPIError as e:
        return {"ok": False, "error": "http_error", "detail": e.message, "status_code": e.status_code}


@mcp.tool(name="users_profile_get")
def users_profile_get(user: Optional[str] = None, include_labels: Optional[bool] = None) -> Dict[str, Any]:
    """Retrieves a user's profile information (users.profile.get)."""

    params: Dict[str, Any] = {}
    if user is not None:
        params["user"] = user
    if include_labels is not None:
        params["include_labels"] = include_labels

    try:
        return slack_api_call("users.profile.get", http_method="GET", params=params)
    except SlackAPIError as e:
        return {"ok": False, "error": "http_error", "detail": e.message, "status_code": e.status_code}
