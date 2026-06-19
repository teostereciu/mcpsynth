from typing import Any, Dict, Optional

from .slack_client import get_client


def users_list(
    cursor: Optional[str] = None,
    include_locale: Optional[bool] = None,
    limit: Optional[int] = None,
    team_id: Optional[str] = None,
) -> Dict[str, Any]:
    payload: Dict[str, Any] = {}
    if cursor is not None:
        payload["cursor"] = cursor
    if include_locale is not None:
        payload["include_locale"] = include_locale
    if limit is not None:
        payload["limit"] = limit
    if team_id is not None:
        payload["team_id"] = team_id
    return get_client().request("GET", "/users.list", json=payload)


def users_lookup_by_email(email: str) -> Dict[str, Any]:
    payload: Dict[str, Any] = {"email": email}
    return get_client().request("GET", "/users.lookupByEmail", json=payload)


def users_get_presence(user: Optional[str] = None) -> Dict[str, Any]:
    payload: Dict[str, Any] = {}
    if user is not None:
        payload["user"] = user
    return get_client().request("GET", "/users.getPresence", json=payload)


def users_info(user: str, include_locale: Optional[bool] = None) -> Dict[str, Any]:
    payload: Dict[str, Any] = {"user": user}
    if include_locale is not None:
        payload["include_locale"] = include_locale
    return get_client().request("GET", "/users.info", json=payload)
