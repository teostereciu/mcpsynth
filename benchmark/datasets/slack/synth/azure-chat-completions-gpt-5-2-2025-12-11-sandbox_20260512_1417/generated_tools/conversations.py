from typing import Any, Dict, Optional

from .slack_client import get_client


def conversations_list(
    cursor: Optional[str] = None,
    exclude_archived: Optional[bool] = None,
    limit: Optional[int] = None,
    team_id: Optional[str] = None,
    types: Optional[str] = None,
) -> Dict[str, Any]:
    payload: Dict[str, Any] = {}
    if cursor is not None:
        payload["cursor"] = cursor
    if exclude_archived is not None:
        payload["exclude_archived"] = exclude_archived
    if limit is not None:
        payload["limit"] = limit
    if team_id is not None:
        payload["team_id"] = team_id
    if types is not None:
        payload["types"] = types
    return get_client().request("GET", "/conversations.list", json=payload)


def conversations_history(
    channel: str,
    cursor: Optional[str] = None,
    include_all_metadata: Optional[bool] = None,
    inclusive: Optional[bool] = None,
    latest: Optional[str] = None,
    limit: Optional[int] = None,
    oldest: Optional[str] = None,
) -> Dict[str, Any]:
    payload: Dict[str, Any] = {"channel": channel}
    if cursor is not None:
        payload["cursor"] = cursor
    if include_all_metadata is not None:
        payload["include_all_metadata"] = include_all_metadata
    if inclusive is not None:
        payload["inclusive"] = inclusive
    if latest is not None:
        payload["latest"] = latest
    if limit is not None:
        payload["limit"] = limit
    if oldest is not None:
        payload["oldest"] = oldest
    return get_client().request("GET", "/conversations.history", json=payload)


def conversations_replies(
    channel: str,
    ts: str,
    cursor: Optional[str] = None,
    include_all_metadata: Optional[bool] = None,
    inclusive: Optional[bool] = None,
    latest: Optional[str] = None,
    limit: Optional[int] = None,
    oldest: Optional[str] = None,
) -> Dict[str, Any]:
    payload: Dict[str, Any] = {"channel": channel, "ts": ts}
    if cursor is not None:
        payload["cursor"] = cursor
    if include_all_metadata is not None:
        payload["include_all_metadata"] = include_all_metadata
    if inclusive is not None:
        payload["inclusive"] = inclusive
    if latest is not None:
        payload["latest"] = latest
    if limit is not None:
        payload["limit"] = limit
    if oldest is not None:
        payload["oldest"] = oldest
    return get_client().request("GET", "/conversations.replies", json=payload)


def conversations_members(
    channel: str,
    cursor: Optional[str] = None,
    limit: Optional[int] = None,
) -> Dict[str, Any]:
    payload: Dict[str, Any] = {"channel": channel}
    if cursor is not None:
        payload["cursor"] = cursor
    if limit is not None:
        payload["limit"] = limit
    return get_client().request("GET", "/conversations.members", json=payload)
