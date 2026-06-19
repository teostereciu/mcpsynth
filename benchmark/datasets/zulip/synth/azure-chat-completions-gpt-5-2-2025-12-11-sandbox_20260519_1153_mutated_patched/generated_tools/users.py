from typing import Any, Dict, List, Optional

from .client import ZulipClient, _maybe_json_dumps


def get_own_user() -> Dict[str, Any]:
    """GET /users/me"""
    client = ZulipClient()
    return client.request("GET", "/users/me")


def get_users(
    *,
    client_gravatar: Optional[bool] = None,
    include_custom_profile_fields: Optional[bool] = None,
    user_ids: Optional[List[int]] = None,
) -> Dict[str, Any]:
    """GET /users"""
    client = ZulipClient()
    params: Dict[str, Any] = {}
    if client_gravatar is not None:
        params["client_gravatar"] = "true" if client_gravatar else "false"
    if include_custom_profile_fields is not None:
        params["include_custom_profile_fields"] = "true" if include_custom_profile_fields else "false"
    if user_ids is not None:
        params["user_ids"] = _maybe_json_dumps(user_ids)
    return client.request("GET", "/users", params=params)


def get_user_presence(*, user_id_or_email: str) -> Dict[str, Any]:
    """GET /users/{user_id_or_email}/presence"""
    client = ZulipClient()
    return client.request("GET", f"/users/{user_id_or_email}/presence")


def get_realm_presence() -> Dict[str, Any]:
    """GET /realm/presence"""
    client = ZulipClient()
    return client.request("GET", "/realm/presence")
