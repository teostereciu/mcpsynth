from typing import Any, Dict, List, Optional

from .common import client


def get_users(
    client_gravatar: Optional[bool] = None,
    include_custom_profile_fields: Optional[bool] = None,
    user_ids: Optional[List[int]] = None,
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


def get_own_user() -> Dict[str, Any]:
    return client.request("GET", "/users/me")


def get_user(
    user_id: int,
    client_gravatar: Optional[bool] = None,
    include_custom_profile_fields: Optional[bool] = None,
) -> Dict[str, Any]:
    return client.request(
        "GET",
        f"/users/{user_id}",
        params={
            "client_gravatar": client_gravatar,
            "include_custom_profile_fields": include_custom_profile_fields,
        },
    )


def get_user_by_email(
    email: str,
    client_gravatar: Optional[bool] = None,
    include_custom_profile_fields: Optional[bool] = None,
) -> Dict[str, Any]:
    return client.request(
        "GET",
        f"/users/{email}",
        params={
            "client_gravatar": client_gravatar,
            "include_custom_profile_fields": include_custom_profile_fields,
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
    profile_data: Optional[List[Dict[str, Any]]] = None,
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


def deactivate_user(
    user_id: int,
    actions: Optional[Dict[str, Any]] = None,
    deactivation_notification_comment: Optional[str] = None,
) -> Dict[str, Any]:
    return client.request(
        "DELETE",
        f"/users/{user_id}",
        data={
            "actions": actions,
            "deactivation_notification_comment": deactivation_notification_comment,
        },
    )


def reactivate_user(user_id: int) -> Dict[str, Any]:
    return client.request("POST", f"/users/{user_id}/reactivate")
