from __future__ import annotations

from typing import Any, Dict, List, Optional

from . import mcp
from .http import SlackAPIError, slack_api_call


@mcp.tool(name="conversations_list")
def conversations_list(
    limit: Optional[int] = None,
    cursor: Optional[str] = None,
    exclude_archived: Optional[bool] = None,
    types: Optional[str] = None,
    team_id: Optional[str] = None,
) -> Dict[str, Any]:
    """Lists all channels in a Slack team (conversations.list)."""

    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if cursor is not None:
        params["cursor"] = cursor
    if exclude_archived is not None:
        params["exclude_archived"] = exclude_archived
    if types is not None:
        params["types"] = types
    if team_id is not None:
        params["team_id"] = team_id

    try:
        return slack_api_call("conversations.list", http_method="GET", params=params)
    except SlackAPIError as e:
        return {"ok": False, "error": "http_error", "detail": e.message, "status_code": e.status_code}


@mcp.tool(name="conversations_info")
def conversations_info(
    channel: str,
    include_locale: Optional[bool] = None,
    include_num_members: Optional[bool] = None,
) -> Dict[str, Any]:
    """Gets information about a conversation (conversations.info)."""

    params: Dict[str, Any] = {"channel": channel}
    if include_locale is not None:
        params["include_locale"] = include_locale
    if include_num_members is not None:
        params["include_num_members"] = include_num_members

    try:
        return slack_api_call("conversations.info", http_method="GET", params=params)
    except SlackAPIError as e:
        return {"ok": False, "error": "http_error", "detail": e.message, "status_code": e.status_code}


@mcp.tool(name="conversations_history")
def conversations_history(
    channel: str,
    limit: Optional[int] = None,
    cursor: Optional[str] = None,
    latest: Optional[str] = None,
    oldest: Optional[str] = None,
    inclusive: Optional[bool] = None,
    include_all_metadata: Optional[bool] = None,
) -> Dict[str, Any]:
    """Fetches conversation history (conversations.history)."""

    params: Dict[str, Any] = {"channel": channel}
    if limit is not None:
        params["limit"] = limit
    if cursor is not None:
        params["cursor"] = cursor
    if latest is not None:
        params["latest"] = latest
    if oldest is not None:
        params["oldest"] = oldest
    if inclusive is not None:
        params["inclusive"] = inclusive
    if include_all_metadata is not None:
        params["include_all_metadata"] = include_all_metadata

    try:
        return slack_api_call("conversations.history", http_method="GET", params=params)
    except SlackAPIError as e:
        return {"ok": False, "error": "http_error", "detail": e.message, "status_code": e.status_code}


@mcp.tool(name="conversations_replies")
def conversations_replies(
    channel: str,
    ts: str,
    limit: Optional[int] = None,
    cursor: Optional[str] = None,
    latest: Optional[str] = None,
    oldest: Optional[str] = None,
    inclusive: Optional[bool] = None,
) -> Dict[str, Any]:
    """Retrieve a thread of messages posted to a conversation (conversations.replies)."""

    params: Dict[str, Any] = {"channel": channel, "ts": ts}
    if limit is not None:
        params["limit"] = limit
    if cursor is not None:
        params["cursor"] = cursor
    if latest is not None:
        params["latest"] = latest
    if oldest is not None:
        params["oldest"] = oldest
    if inclusive is not None:
        params["inclusive"] = inclusive

    try:
        return slack_api_call("conversations.replies", http_method="GET", params=params)
    except SlackAPIError as e:
        return {"ok": False, "error": "http_error", "detail": e.message, "status_code": e.status_code}


@mcp.tool(name="conversations_members")
def conversations_members(
    channel: str,
    limit: Optional[int] = None,
    cursor: Optional[str] = None,
) -> Dict[str, Any]:
    """Retrieve members of a conversation (conversations.members)."""

    params: Dict[str, Any] = {"channel": channel}
    if limit is not None:
        params["limit"] = limit
    if cursor is not None:
        params["cursor"] = cursor

    try:
        return slack_api_call("conversations.members", http_method="GET", params=params)
    except SlackAPIError as e:
        return {"ok": False, "error": "http_error", "detail": e.message, "status_code": e.status_code}


@mcp.tool(name="conversations_create")
def conversations_create(
    name: str,
    is_private: Optional[bool] = None,
    team_id: Optional[str] = None,
) -> Dict[str, Any]:
    """Creates a new conversation (conversations.create)."""

    payload: Dict[str, Any] = {"name": name}
    if is_private is not None:
        payload["is_private"] = is_private
    if team_id is not None:
        payload["team_id"] = team_id

    try:
        return slack_api_call("conversations.create", http_method="POST", json=payload)
    except SlackAPIError as e:
        return {"ok": False, "error": "http_error", "detail": e.message, "status_code": e.status_code}


@mcp.tool(name="conversations_join")
def conversations_join(channel: str) -> Dict[str, Any]:
    """Joins an existing conversation (conversations.join)."""

    try:
        return slack_api_call("conversations.join", http_method="POST", json={"channel": channel})
    except SlackAPIError as e:
        return {"ok": False, "error": "http_error", "detail": e.message, "status_code": e.status_code}


@mcp.tool(name="conversations_open")
def conversations_open(
    users: Optional[List[str]] = None,
    channel: Optional[str] = None,
    return_im: Optional[bool] = None,
) -> Dict[str, Any]:
    """Opens or resumes a direct message or multi-person direct message (conversations.open)."""

    payload: Dict[str, Any] = {}
    if users is not None:
        payload["users"] = ",".join(users)
    if channel is not None:
        payload["channel"] = channel
    if return_im is not None:
        payload["return_im"] = return_im

    try:
        return slack_api_call("conversations.open", http_method="POST", json=payload)
    except SlackAPIError as e:
        return {"ok": False, "error": "http_error", "detail": e.message, "status_code": e.status_code}


@mcp.tool(name="conversations_invite")
def conversations_invite(channel: str, users: List[str]) -> Dict[str, Any]:
    """Invites users to a channel (conversations.invite)."""

    try:
        return slack_api_call(
            "conversations.invite",
            http_method="POST",
            json={"channel": channel, "users": ",".join(users)},
        )
    except SlackAPIError as e:
        return {"ok": False, "error": "http_error", "detail": e.message, "status_code": e.status_code}


@mcp.tool(name="conversations_archive")
def conversations_archive(channel: str) -> Dict[str, Any]:
    """Archives a conversation (conversations.archive)."""

    try:
        return slack_api_call("conversations.archive", http_method="POST", json={"channel": channel})
    except SlackAPIError as e:
        return {"ok": False, "error": "http_error", "detail": e.message, "status_code": e.status_code}


@mcp.tool(name="conversations_unarchive")
def conversations_unarchive(channel: str) -> Dict[str, Any]:
    """Unarchives a conversation (conversations.unarchive)."""

    try:
        return slack_api_call("conversations.unarchive", http_method="POST", json={"channel": channel})
    except SlackAPIError as e:
        return {"ok": False, "error": "http_error", "detail": e.message, "status_code": e.status_code}


@mcp.tool(name="conversations_set_topic")
def conversations_set_topic(channel: str, topic: str) -> Dict[str, Any]:
    """Sets the topic for a conversation (conversations.setTopic)."""

    try:
        return slack_api_call("conversations.setTopic", http_method="POST", json={"channel": channel, "topic": topic})
    except SlackAPIError as e:
        return {"ok": False, "error": "http_error", "detail": e.message, "status_code": e.status_code}


@mcp.tool(name="conversations_set_purpose")
def conversations_set_purpose(channel: str, purpose: str) -> Dict[str, Any]:
    """Sets the purpose for a conversation (conversations.setPurpose)."""

    try:
        return slack_api_call(
            "conversations.setPurpose", http_method="POST", json={"channel": channel, "purpose": purpose}
        )
    except SlackAPIError as e:
        return {"ok": False, "error": "http_error", "detail": e.message, "status_code": e.status_code}
