"""Tools for interacting with scheduled messages in Zulip."""

import os
import requests
from typing import Optional, List

ZULIP_EMAIL = os.environ.get("ZULIP_EMAIL")
ZULIP_API_KEY = os.environ.get("ZULIP_API_KEY")
ZULIP_SITE = os.environ.get("ZULIP_SITE")

def schedule_message(to: str, content: str, scheduled_delivery_timestamp: int, type: str = "stream", topic: Optional[str] = None) -> dict:
    """Schedules a message."""
    data = {
        "type": type,
        "to": to,
        "content": content,
        "scheduled_delivery_timestamp": scheduled_delivery_timestamp,
    }
    if topic:
        data["topic"] = topic
    response = requests.post(
        f"{ZULIP_SITE}/api/v1/scheduled_messages",
        auth=(ZULIP_EMAIL, ZULIP_API_KEY),
        data=data,
    )
    return response.json()
