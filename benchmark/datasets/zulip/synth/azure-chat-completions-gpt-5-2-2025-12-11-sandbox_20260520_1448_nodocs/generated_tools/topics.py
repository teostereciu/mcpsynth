from __future__ import annotations

from typing import Any, Optional

from zulip_client import ZulipClient


def get_topics(client: ZulipClient, *, stream_id: int) -> dict:
    return client.request("GET", f"/users/me/{stream_id}/topics")


def update_topic(client: ZulipClient, *, stream_id: int, topic: str, new_topic: str, propagate_mode: Optional[str] = None) -> dict:
    data: dict[str, Any] = {"topic": topic, "new_topic": new_topic}
    if propagate_mode is not None:
        data["propagate_mode"] = propagate_mode
    return client.request("POST", f"/streams/{stream_id}/topics", data=data)
