from typing import Any, Dict, Optional

from .slack_client import SlackWebAPIClient, _clean_dict


def reminders_add(
    text: str,
    time: str,
    team_id: Optional[str] = None,
    recurrence: Optional[Any] = None,
    user: Optional[str] = None,
    client: Optional[SlackWebAPIClient] = None,
) -> Dict[str, Any]:
    client = client or SlackWebAPIClient()
    payload = _clean_dict(
        {
            "text": text,
            "time": time,
            "team_id": team_id,
            "recurrence": recurrence,
            "user": user,
        }
    )
    return client.post("reminders.add", payload)


def reminders_list(
    team_id: Optional[str] = None,
    client: Optional[SlackWebAPIClient] = None,
) -> Dict[str, Any]:
    client = client or SlackWebAPIClient()
    params = _clean_dict({"team_id": team_id})
    return client.get("reminders.list", params)


def reminders_complete(
    reminder: str,
    client: Optional[SlackWebAPIClient] = None,
) -> Dict[str, Any]:
    client = client or SlackWebAPIClient()
    payload = _clean_dict({"reminder": reminder})
    return client.post("reminders.complete", payload)


def reminders_delete(
    reminder: str,
    client: Optional[SlackWebAPIClient] = None,
) -> Dict[str, Any]:
    client = client or SlackWebAPIClient()
    payload = _clean_dict({"reminder": reminder})
    return client.post("reminders.delete", payload)
