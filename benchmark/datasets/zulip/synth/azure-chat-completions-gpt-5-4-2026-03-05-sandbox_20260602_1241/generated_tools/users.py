from typing import Any, Dict, Optional
from urllib.parse import quote

from generated_tools.common import client


def get_own_user() -> Dict[str, Any]:
    return client.request("GET", "/users/me")


def get_user(user_id: int, client_gravatar: Optional[bool] = None, include_custom_profile_fields: Optional[bool] = None) -> Dict[str, Any]:
    return client.request(
        "GET",
        f"/users/{user_id}",
        params={
            "client_gravatar": client_gravatar,
            "include_custom_profile_fields": include_custom_profile_fields,
        },
    )


def get_user_by_email(email: str, client_gravatar: Optional[bool] = None, include_custom_profile_fields: Optional[bool] = None) -> Dict[str, Any]:
    return client.request(
        "GET",
        f"/users/{quote(email, safe='')}",
        params={
            "client_gravatar": client_gravatar,
            "include_custom_profile_fields": include_custom_profile_fields,
        },
    )


def get_users(
    client_gravatar: Optional[bool] = None,
    include_custom_profile_fields: Optional[bool] = None,
    user_ids: Optional[list[int]] = None,
) -> Dict[str, Any]:
    return client.request(
        "GET",
        "/users",
        params={
            "client_gravatar": client_gravatar,
            "include_custom_profile_fields": include_custom_profile_fields,
            "user_ids": user_ids,
        },
    )


def create_user(email: str, password: str, full_name: str) -> Dict[str, Any]:
    return client.request(
        "POST",
        "/users",
        data={"email": email, "password": password, "full_name": full_name},
    )


def update_user(
    user_id: int,
    full_name: Optional[str] = None,
    role: Optional[int] = None,
    profile_data: Optional[list[dict[str, Any]]] = None,
    new_email: Optional[str] = None,
) -> Dict[str, Any]:
    return client.request(
        "PATCH",
        f"/users/{user_id}",
        data={
            "full_name": full_name,
            "role": role,
            "profile_data": profile_data,
            "new_email": new_email,
        },
    )


def update_status(
    status_text: Optional[str] = None,
    emoji_name: Optional[str] = None,
    emoji_code: Optional[str] = None,
    reaction_type: Optional[str] = None,
    away: Optional[bool] = None,
) -> Dict[str, Any]:
    return client.request(
        "POST",
        "/users/me/status",
        data={
            "status_text": status_text,
            "emoji_name": emoji_name,
            "emoji_code": emoji_code,
            "reaction_type": reaction_type,
            "away": away,
        },
    )


def get_presence() -> Dict[str, Any]:
    return client.request("GET", "/realm/presence")


def get_user_presence(user_id_or_email: str) -> Dict[str, Any]:
    return client.request("GET", f"/users/{quote(str(user_id_or_email), safe='')}/presence")


def update_presence(
    status: str,
    last_update_id: Optional[int] = None,
    history_limit_days: Optional[int] = None,
    new_user_input: Optional[bool] = None,
    ping_only: Optional[bool] = None,
    slim_presence: Optional[bool] = None,
) -> Dict[str, Any]:
    return client.request(
        "POST",
        "/users/me/presence",
        data={
            "status": status,
            "last_update_id": last_update_id,
            "history_limit_days": history_limit_days,
            "new_user_input": new_user_input,
            "ping_only": ping_only,
            "slim_presence": slim_presence,
        },
    )
