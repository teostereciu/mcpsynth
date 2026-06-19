"""User tools."""

from __future__ import annotations

from typing import Any, Dict, List, Optional, Sequence

from .http import zulip_request


JsonDict = Dict[str, Any]


def get_user(*, user_id: int, client_gravatar: Optional[bool] = None, include_custom_profile_fields: Optional[bool] = None) -> JsonDict:
    """GET /users/{user_id}"""
    params: Dict[str, Any] = {
        "client_gravatar": client_gravatar,
        "include_custom_profile_fields": include_custom_profile_fields,
    }
    return zulip_request("GET", f"/users/{user_id}", params=params)


def get_user_by_email(*, email: str, client_gravatar: Optional[bool] = None, include_custom_profile_fields: Optional[bool] = None) -> JsonDict:
    """GET /users/{email}"""
    params: Dict[str, Any] = {
        "client_gravatar": client_gravatar,
        "include_custom_profile_fields": include_custom_profile_fields,
    }
    return zulip_request("GET", f"/users/{email}", params=params)


def get_users(
    *,
    client_gravatar: Optional[bool] = None,
    include_custom_profile_fields: Optional[bool] = None,
    user_ids: Optional[Sequence[int]] = None,
) -> JsonDict:
    """GET /users"""
    params: Dict[str, Any] = {
        "client_gravatar": client_gravatar,
        "include_custom_profile_fields": include_custom_profile_fields,
        "user_ids": list(user_ids) if user_ids is not None else None,
    }
    return zulip_request("GET", "/users", params=params)


def get_own_user() -> JsonDict:
    """GET /users/me"""
    return zulip_request("GET", "/users/me")
