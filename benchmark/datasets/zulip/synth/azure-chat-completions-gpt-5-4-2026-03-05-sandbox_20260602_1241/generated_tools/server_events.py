from typing import Any, Dict, List, Optional

from generated_tools.common import client


def get_server_settings() -> Dict[str, Any]:
    return client.request("GET", "/server_settings")


def register_queue(
    event_types: Optional[List[str]] = None,
    fetch_event_types: Optional[List[str]] = None,
    narrow: Optional[List[List[str]]] = None,
    all_public_streams: Optional[bool] = None,
    apply_markdown: Optional[bool] = None,
    client_gravatar: Optional[bool] = None,
    include_subscribers: Optional[str] = None,
    slim_presence: Optional[bool] = None,
    presence_history_limit_days: Optional[int] = None,
    client_capabilities: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    return client.request(
        "POST",
        "/register",
        data={
            "event_types": event_types,
            "fetch_event_types": fetch_event_types,
            "narrow": narrow,
            "all_public_streams": all_public_streams,
            "apply_markdown": apply_markdown,
            "client_gravatar": client_gravatar,
            "include_subscribers": include_subscribers,
            "slim_presence": slim_presence,
            "presence_history_limit_days": presence_history_limit_days,
            "client_capabilities": client_capabilities,
        },
    )


def get_events(queue_id: str, last_event_id: Optional[int] = None, dont_block: Optional[bool] = None) -> Dict[str, Any]:
    return client.request(
        "GET",
        "/events",
        params={"queue_id": queue_id, "last_event_id": last_event_id, "dont_block": dont_block},
    )


def delete_queue(queue_id: str) -> Dict[str, Any]:
    return client.request("DELETE", "/events", data={"queue_id": queue_id})
