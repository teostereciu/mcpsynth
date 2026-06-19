from typing import Any, Dict, Optional

from generated_tools.common import client


def get_own_user() -> Dict[str, Any]:
    return client.request("GET", "/users/me")


def get_user_by_id(user_id: int) -> Dict[str, Any]:
    return client.request("GET", f"/users/{user_id}")


def get_user_by_email(email: str) -> Dict[str, Any]:
    return client.request("GET", f"/users/{email}")


def get_users() -> Dict[str, Any]:
    return client.request("GET", "/users")


def get_presence(user_id_or_email: str) -> Dict[str, Any]:
    return client.request("GET", f"/users/{user_id_or_email}/presence")


def update_status_text(status_text: Optional[str] = None, away: Optional[bool] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if status_text is not None:
        params["status_text"] = status_text
    if away is not None:
        params["away"] = str(away).lower()
    return client.request("POST", "/users/me/status", params=params)
