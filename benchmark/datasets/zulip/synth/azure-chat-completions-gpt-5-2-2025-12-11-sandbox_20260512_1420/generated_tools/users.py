import json
from typing import Any, Dict, List, Optional, Union

from .client import ZulipClient


def get_own_user() -> Dict[str, Any]:
    """GET /users/me"""
    return ZulipClient().request("GET", "/users/me")


def get_user(user_id: int, client_gravatar: Optional[bool] = None) -> Dict[str, Any]:
    """GET /users/{user_id}"""
    params: Dict[str, Any] = {}
    if client_gravatar is not None:
        params["client_gravatar"] = json.dumps(client_gravatar)
    return ZulipClient().request("GET", f"/users/{user_id}", params=params)


def get_user_by_email(email: str) -> Dict[str, Any]:
    """GET /users/{email}"""
    return ZulipClient().request("GET", f"/users/{email}")


def get_users(client_gravatar: Optional[bool] = None, include_custom_profile_fields: Optional[bool] = None) -> Dict[str, Any]:
    """GET /users"""
    params: Dict[str, Any] = {}
    if client_gravatar is not None:
        params["client_gravatar"] = json.dumps(client_gravatar)
    if include_custom_profile_fields is not None:
        params["include_custom_profile_fields"] = json.dumps(include_custom_profile_fields)
    return ZulipClient().request("GET", "/users", params=params)


def update_status(text: Optional[str] = None, emoji_name: Optional[str] = None, emoji_code: Optional[str] = None, reaction_type: Optional[str] = None) -> Dict[str, Any]:
    """POST /users/me/status"""
    data: Dict[str, Any] = {}
    if text is not None:
        data["status_text"] = text
    if emoji_name is not None:
        data["emoji_name"] = emoji_name
    if emoji_code is not None:
        data["emoji_code"] = emoji_code
    if reaction_type is not None:
        data["reaction_type"] = reaction_type
    return ZulipClient().request("POST", "/users/me/status", data=data)


def get_user_presence(user_id_or_email: Union[int, str]) -> Dict[str, Any]:
    """GET /users/{user_id_or_email}/presence"""
    return ZulipClient().request("GET", f"/users/{user_id_or_email}/presence")


def get_presence() -> Dict[str, Any]:
    """GET /realm/presence"""
    return ZulipClient().request("GET", "/realm/presence")


def update_presence(status: str, ping_only: Optional[bool] = None, new_user_input: Optional[bool] = None) -> Dict[str, Any]:
    """POST /users/me/presence"""
    data: Dict[str, Any] = {"status": status}
    if ping_only is not None:
        data["ping_only"] = json.dumps(ping_only)
    if new_user_input is not None:
        data["new_user_input"] = json.dumps(new_user_input)
    return ZulipClient().request("POST", "/users/me/presence", data=data)


def mute_user(user_id: int) -> Dict[str, Any]:
    """POST /users/me/muted_users/{user_id}"""
    return ZulipClient().request("POST", f"/users/me/muted_users/{user_id}")


def unmute_user(user_id: int) -> Dict[str, Any]:
    """DELETE /users/me/muted_users/{user_id}"""
    return ZulipClient().request("DELETE", f"/users/me/muted_users/{user_id}")


def get_alert_words() -> Dict[str, Any]:
    """GET /users/me/alert_words"""
    return ZulipClient().request("GET", "/users/me/alert_words")


def add_alert_words(words: List[str]) -> Dict[str, Any]:
    """POST /users/me/alert_words"""
    return ZulipClient().request("POST", "/users/me/alert_words", data={"alert_words": json.dumps(words)})


def remove_alert_words(words: List[str]) -> Dict[str, Any]:
    """DELETE /users/me/alert_words"""
    return ZulipClient().request("DELETE", "/users/me/alert_words", data={"alert_words": json.dumps(words)})
