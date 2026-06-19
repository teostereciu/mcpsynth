from typing import Any, Dict, Optional

from .client import ZulipClient


def get_topics(stream_id: int) -> Dict[str, Any]:
    c = ZulipClient()
    return c.request("GET", f"/users/me/{stream_id}/topics")


def update_topic(stream_id: int, topic: str, new_topic: str, propagate_mode: Optional[str] = None) -> Dict[str, Any]:
    c = ZulipClient()
    data: Dict[str, Any] = {"topic": topic, "new_topic": new_topic}
    if propagate_mode is not None:
        data["propagate_mode"] = propagate_mode
    return c.request("PATCH", f"/streams/{stream_id}/topics", data=data)
