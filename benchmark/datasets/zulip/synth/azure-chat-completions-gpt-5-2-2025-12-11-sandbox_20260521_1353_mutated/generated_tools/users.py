from typing import Any, Dict, Optional

from .http_client import ZulipClient, dumps_if_needed


def get_own_user() -> Dict[str, Any]:
    """GET /users/me

    Doc: docs/api_get-own-user.md
    """
    client = ZulipClient()
    return client.request("GET", "/users/me")


def get_user(*, user_id: int) -> Dict[str, Any]:
    """GET /users/{user_id}

    Doc: docs/api_get-user.md
    """
    client = ZulipClient()
    return client.request("GET", f"/users/{user_id}")


def get_user_by_email(*, email: str) -> Dict[str, Any]:
    """GET /users/{email}

    Doc: docs/api_get-user-by-email.md
    """
    client = ZulipClient()
    return client.request("GET", f"/users/{email}")


def get_users(*, client_gravatar: Optional[bool] = None, include_custom_profile_fields: Optional[bool] = None) -> Dict[str, Any]:
    """GET /users

    Doc: docs/api_get-users.md
    """
    client = ZulipClient()
    params: Dict[str, Any] = {}
    if client_gravatar is not None:
        params["client_gravatar"] = client_gravatar
    if include_custom_profile_fields is not None:
        params["include_custom_profile_fields"] = include_custom_profile_fields
    return client.request("GET", "/users", params=params)


def get_user_presence(*, user_id_or_email: str) -> Dict[str, Any]:
    """GET /users/{user_id_or_email}/presence

    Doc: docs/api_get-user-presence.md
    """
    client = ZulipClient()
    return client.request("GET", f"/users/{user_id_or_email}/presence")


def get_presence() -> Dict[str, Any]:
    """GET /realm/presence

    Doc: docs/api_get-presence.md
    """
    client = ZulipClient()
    return client.request("GET", "/realm/presence")


def update_presence(*, status: str, ping_only: Optional[bool] = None, new_user_input: Optional[bool] = None) -> Dict[str, Any]:
    """POST /users/me/presence

    Doc: docs/api_update-presence.md
    """
    client = ZulipClient()
    data: Dict[str, Any] = {"status": status}
    if ping_only is not None:
        data["ping_only"] = ping_only
    if new_user_input is not None:
        data["new_user_input"] = new_user_input
    return client.request("POST", "/users/me/presence", data=data)


def update_status(*, status_text: Optional[str] = None, emoji_name: Optional[str] = None, emoji_code: Optional[str] = None, reaction_type: Optional[str] = None, away: Optional[bool] = None) -> Dict[str, Any]:
    """POST /users/me/status

    Doc: docs/api_update-status.md
    """
    client = ZulipClient()
    data: Dict[str, Any] = {}
    if status_text is not None:
        data["status_text"] = status_text
    if emoji_name is not None:
        data["emoji_name"] = emoji_name
    if emoji_code is not None:
        data["emoji_code"] = emoji_code
    if reaction_type is not None:
        data["reaction_type"] = reaction_type
    if away is not None:
        data["away"] = away
    return client.request("POST", "/users/me/status", data=data)


def get_user_status(*, user_id: int) -> Dict[str, Any]:
    """GET /users/{user_id}/status

    Doc: docs/api_get-user-status.md
    """
    client = ZulipClient()
    return client.request("GET", f"/users/{user_id}/status")


def mute_user(*, muted_user_id: int) -> Dict[str, Any]:
    """POST /users/me/muted_users/{muted_user_id}

    Doc: docs/api_mute-user.md
    """
    client = ZulipClient()
    return client.request("POST", f"/users/me/muted_users/{muted_user_id}")


def unmute_user(*, muted_user_id: int) -> Dict[str, Any]:
    """DELETE /users/me/muted_users/{muted_user_id}

    Doc: docs/api_unmute-user.md
    """
    client = ZulipClient()
    return client.request("DELETE", f"/users/me/muted_users/{muted_user_id}")


def get_alert_words() -> Dict[str, Any]:
    """GET /users/me/alert_words

    Doc: docs/api_get-alert-words.md
    """
    client = ZulipClient()
    return client.request("GET", "/users/me/alert_words")


def add_alert_words(*, words: list[str]) -> Dict[str, Any]:
    """POST /users/me/alert_words

    Doc: docs/api_add-alert-words.md
    """
    client = ZulipClient()
    return client.request("POST", "/users/me/alert_words", data={"words": dumps_if_needed(words)})


def remove_alert_words(*, words: list[str]) -> Dict[str, Any]:
    """DELETE /users/me/alert_words

    Doc: docs/api_remove-alert-words.md
    """
    client = ZulipClient()
    return client.request("DELETE", "/users/me/alert_words", data={"words": dumps_if_needed(words)})
