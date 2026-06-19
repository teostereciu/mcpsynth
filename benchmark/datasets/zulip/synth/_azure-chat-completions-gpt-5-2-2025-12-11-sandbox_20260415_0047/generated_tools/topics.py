"""Topic management tools."""

from __future__ import annotations

from typing import Any, Dict

from .http import zulip_request


JsonDict = Dict[str, Any]


def delete_topic(*, stream_id: int, topic_name: str) -> JsonDict:
    """POST /streams/{stream_id}/delete_topic

    Requires organization administrator.
    """
    return zulip_request("POST", f"/streams/{stream_id}/delete_topic", data={"topic_name": topic_name})
