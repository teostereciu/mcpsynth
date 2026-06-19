from typing import Any, Dict, Optional

from .slack_client import SlackWebAPIClient, _clean_dict


def users_list(
    cursor: Optional[str] = None,
    include_locale: Optional[bool] = None,
    limit: Optional[int] = None,
    team_id: Optional[str] = None,
    client: Optional[SlackWebAPIClient] = None,
) -> Dict[str, Any]:
    client = client or SlackWebAPIClient()
    params = _clean_dict(
        {
            "cursor": cursor,
            "include_locale": include_locale,
            "limit": limit,
            "team_id": team_id,
        }
    )
    return client.get("users.list", params)


def users_get_presence(
    user: Optional[str] = None,
    client: Optional[SlackWebAPIClient] = None,
) -> Dict[str, Any]:
    client = client or SlackWebAPIClient()
    params = _clean_dict({"user": user})
    return client.get("users.getPresence", params)


def users_lookup_by_email(
    email: str,
    client: Optional[SlackWebAPIClient] = None,
) -> Dict[str, Any]:
    client = client or SlackWebAPIClient()
    params = _clean_dict({"email": email})
    return client.get("users.lookupByEmail", params)
