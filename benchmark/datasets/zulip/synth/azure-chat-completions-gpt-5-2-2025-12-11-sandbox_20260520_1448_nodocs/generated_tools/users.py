from __future__ import annotations

from typing import Any, Optional

from zulip_client import ZulipClient


def get_own_profile(client: ZulipClient) -> dict:
    return client.request("GET", "/users/me")


def get_user(client: ZulipClient, *, user_id: int) -> dict:
    return client.request("GET", f"/users/{user_id}")


def get_users(client: ZulipClient, *, client_gravatar: Optional[bool] = None, include_custom_profile_fields: Optional[bool] = None) -> dict:
    params: dict[str, Any] = {}
    if client_gravatar is not None:
        params["client_gravatar"] = client_gravatar
    if include_custom_profile_fields is not None:
        params["include_custom_profile_fields"] = include_custom_profile_fields
    return client.request("GET", "/users", params=params)


def get_presence(client: ZulipClient, *, user_id_or_email: str) -> dict:
    return client.request("GET", f"/users/{user_id_or_email}/presence")


def update_own_status(client: ZulipClient, *, status_text: Optional[str] = None, away: Optional[bool] = None, emoji_name: Optional[str] = None, emoji_code: Optional[str] = None, reaction_type: Optional[str] = None) -> dict:
    data: dict[str, Any] = {}
    if status_text is not None:
        data["status_text"] = status_text
    if away is not None:
        data["away"] = away
    if emoji_name is not None:
        data["emoji_name"] = emoji_name
    if emoji_code is not None:
        data["emoji_code"] = emoji_code
    if reaction_type is not None:
        data["reaction_type"] = reaction_type
    return client.request("POST", "/users/me/status", data=data)
