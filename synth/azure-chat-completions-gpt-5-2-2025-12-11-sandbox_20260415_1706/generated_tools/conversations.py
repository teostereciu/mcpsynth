from typing import Any, Dict, Optional

from .slack_client import SlackWebAPIClient, _clean_dict


def conversations_list(
    cursor: Optional[str] = None,
    exclude_archived: Optional[bool] = None,
    limit: Optional[int] = None,
    team_id: Optional[str] = None,
    types: Optional[str] = None,
    client: Optional[SlackWebAPIClient] = None,
) -> Dict[str, Any]:
    client = client or SlackWebAPIClient()
    params = _clean_dict(
        {
            "cursor": cursor,
            "exclude_archived": exclude_archived,
            "limit": limit,
            "team_id": team_id,
            "types": types,
        }
    )
    return client.get("conversations.list", params)


def conversations_members(
    channel: str,
    cursor: Optional[str] = None,
    limit: Optional[int] = None,
    client: Optional[SlackWebAPIClient] = None,
) -> Dict[str, Any]:
    client = client or SlackWebAPIClient()
    params = _clean_dict({"channel": channel, "cursor": cursor, "limit": limit})
    return client.get("conversations.members", params)


def conversations_replies(
    channel: str,
    ts: str,
    cursor: Optional[str] = None,
    include_all_metadata: Optional[bool] = None,
    inclusive: Optional[bool] = None,
    latest: Optional[str] = None,
    limit: Optional[int] = None,
    oldest: Optional[str] = None,
    client: Optional[SlackWebAPIClient] = None,
) -> Dict[str, Any]:
    client = client or SlackWebAPIClient()
    params = _clean_dict(
        {
            "channel": channel,
            "ts": ts,
            "cursor": cursor,
            "include_all_metadata": include_all_metadata,
            "inclusive": inclusive,
            "latest": latest,
            "limit": limit,
            "oldest": oldest,
        }
    )
    return client.get("conversations.replies", params)


def conversations_create(
    name: str,
    is_private: Optional[bool] = None,
    team_id: Optional[str] = None,
    client: Optional[SlackWebAPIClient] = None,
) -> Dict[str, Any]:
    client = client or SlackWebAPIClient()
    payload = _clean_dict({"name": name, "is_private": is_private, "team_id": team_id})
    return client.post("conversations.create", payload)


def conversations_open(
    channel: Optional[str] = None,
    users: Optional[str] = None,
    return_im: Optional[bool] = None,
    prevent_creation: Optional[bool] = None,
    client: Optional[SlackWebAPIClient] = None,
) -> Dict[str, Any]:
    client = client or SlackWebAPIClient()
    payload = _clean_dict(
        {
            "channel": channel,
            "users": users,
            "return_im": return_im,
            "prevent_creation": prevent_creation,
        }
    )
    return client.post("conversations.open", payload)


def conversations_invite(
    channel: str,
    users: str,
    force: Optional[bool] = None,
    client: Optional[SlackWebAPIClient] = None,
) -> Dict[str, Any]:
    client = client or SlackWebAPIClient()
    payload = _clean_dict({"channel": channel, "users": users, "force": force})
    return client.post("conversations.invite", payload)


def conversations_join(
    channel: str,
    client: Optional[SlackWebAPIClient] = None,
) -> Dict[str, Any]:
    client = client or SlackWebAPIClient()
    payload = _clean_dict({"channel": channel})
    return client.post("conversations.join", payload)


def conversations_history(
    channel: str,
    cursor: Optional[str] = None,
    include_all_metadata: Optional[bool] = None,
    inclusive: Optional[bool] = None,
    latest: Optional[str] = None,
    limit: Optional[int] = None,
    oldest: Optional[str] = None,
    client: Optional[SlackWebAPIClient] = None,
) -> Dict[str, Any]:
    client = client or SlackWebAPIClient()
    params = _clean_dict(
        {
            "channel": channel,
            "cursor": cursor,
            "include_all_metadata": include_all_metadata,
            "inclusive": inclusive,
            "latest": latest,
            "limit": limit,
            "oldest": oldest,
        }
    )
    return client.get("conversations.history", params)
