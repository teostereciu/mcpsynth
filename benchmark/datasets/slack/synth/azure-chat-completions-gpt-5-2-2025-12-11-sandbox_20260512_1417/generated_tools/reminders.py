from typing import Any, Dict, Optional

from .slack_client import get_client


def reminders_add(
    text: str,
    time: str,
    team_id: Optional[str] = None,
    recurrence: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    payload: Dict[str, Any] = {"text": text, "time": time}
    if team_id is not None:
        payload["team_id"] = team_id
    if recurrence is not None:
        payload["recurrence"] = recurrence
    return get_client().request("POST", "/reminders.add", json=payload)


def reminders_list(team_id: Optional[str] = None) -> Dict[str, Any]:
    payload: Dict[str, Any] = {}
    if team_id is not None:
        payload["team_id"] = team_id
    return get_client().request("GET", "/reminders.list", json=payload)
