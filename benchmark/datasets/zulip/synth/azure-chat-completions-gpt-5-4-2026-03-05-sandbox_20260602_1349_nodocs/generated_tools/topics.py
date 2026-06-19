from typing import Any, Dict, Optional

from generated_tools.common import client


def rename_topic(stream_id: int, topic_name: str, new_topic: str, propagate_mode: str = "change_all") -> Dict[str, Any]:
    params = {
        "stream_id": stream_id,
        "topic_name": topic_name,
        "op": "change_topic",
        "new_topic": new_topic,
        "propagate_mode": propagate_mode,
    }
    return client.request("POST", "/messages/topic", params=params)


def resolve_topic(stream_id: int, topic_name: str) -> Dict[str, Any]:
    params = {
        "stream_id": stream_id,
        "topic_name": topic_name,
        "op": "change_status",
        "status": "resolved",
    }
    return client.request("POST", "/messages/topic", params=params)


def unresolve_topic(stream_id: int, topic_name: str) -> Dict[str, Any]:
    params = {
        "stream_id": stream_id,
        "topic_name": topic_name,
        "op": "change_status",
        "status": "unresolved",
    }
    return client.request("POST", "/messages/topic", params=params)


def delete_topic(stream_id: int, topic_name: str) -> Dict[str, Any]:
    params = {"stream_id": stream_id, "topic_name": topic_name}
    return client.request("DELETE", "/messages/topic", params=params)


def get_topic_history(stream_id: Optional[int] = None) -> Dict[str, Any]:
    params = {}
    if stream_id is not None:
        params["stream_id"] = stream_id
    return client.request("GET", "/users/me/topics", params=params)
