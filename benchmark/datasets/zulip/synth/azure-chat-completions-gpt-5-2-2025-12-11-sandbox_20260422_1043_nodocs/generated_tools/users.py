from typing import Any, Dict, Optional

from .client import ZulipClient


def get_users(client_gravatar: Optional[bool] = None, include_custom_profile_fields: Optional[bool] = None) -> Dict[str, Any]:
    c = ZulipClient()
    params: Dict[str, Any] = {}
    if client_gravatar is not None:
        params["client_gravatar"] = "true" if client_gravatar else "false"
    if include_custom_profile_fields is not None:
        params["include_custom_profile_fields"] = "true" if include_custom_profile_fields else "false"
    return c.request("GET", "/users", params=params)


def get_user(user_id: int, client_gravatar: Optional[bool] = None) -> Dict[str, Any]:
    c = ZulipClient()
    params: Dict[str, Any] = {}
    if client_gravatar is not None:
        params["client_gravatar"] = "true" if client_gravatar else "false"
    return c.request("GET", f"/users/{user_id}", params=params)


def get_own_profile() -> Dict[str, Any]:
    c = ZulipClient()
    return c.request("GET", "/users/me")


def update_own_profile(full_name: Optional[str] = None) -> Dict[str, Any]:
    c = ZulipClient()
    data: Dict[str, Any] = {}
    if full_name is not None:
        data["full_name"] = full_name
    return c.request("PATCH", "/settings", data=data)


def get_presence(user_id_or_email: str) -> Dict[str, Any]:
    c = ZulipClient()
    return c.request("GET", f"/users/{user_id_or_email}/presence")
