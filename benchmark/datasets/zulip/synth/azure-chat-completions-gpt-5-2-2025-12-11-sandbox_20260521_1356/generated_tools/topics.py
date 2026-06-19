from typing import Any, Dict, Optional

from .client import ZulipClient


def get_stream_topics(
    client: ZulipClient,
    stream_id: int,
    allow_empty_topic_name: Optional[bool] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if allow_empty_topic_name is not None:
        params["allow_empty_topic_name"] = "true" if allow_empty_topic_name else "false"
    return client.request("GET", f"/users/me/{stream_id}/topics", params)


def delete_topic(client: ZulipClient, stream_id: int, topic_name: str) -> Dict[str, Any]:
    params: Dict[str, Any] = {"topic_name": topic_name}
    return client.request("POST", f"/streams/{stream_id}/delete_topic", params)


def update_user_topic_visibility(
    client: ZulipClient,
    stream_id: int,
    topic: str,
    visibility_policy: int,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "stream_id": stream_id,
        "topic": topic,
        "visibility_policy": visibility_policy,
    }
    return client.request("POST", "/user_topics", params)


def mute_topic_legacy(
    client: ZulipClient,
    topic: str,
    op: str,
    stream: str | None = None,
    stream_id: int | None = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"topic": topic, "op": op}
    if stream is not None:
        params["stream"] = stream
    if stream_id is not None:
        params["stream_id"] = stream_id
    return client.request("PATCH", "/users/me/subscriptions/muted_topics", params)
