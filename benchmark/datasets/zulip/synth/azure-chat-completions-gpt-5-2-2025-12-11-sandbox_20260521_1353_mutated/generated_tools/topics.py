from typing import Any, Dict, Optional

from .http_client import ZulipClient


def update_user_topic(*, stream_id: int, topic: str, visibility_policy: Optional[int] = None) -> Dict[str, Any]:
    """PATCH /users/me/{stream_id}/topics

    Doc: docs/api_update-user-topic.md
    """
    client = ZulipClient()
    data: Dict[str, Any] = {"topic": topic}
    if visibility_policy is not None:
        data["visibility_policy"] = visibility_policy
    return client.request("PATCH", f"/users/me/{stream_id}/topics", data=data)


def delete_topic(*, stream_id: int, topic_name: str) -> Dict[str, Any]:
    """POST /streams/{stream_id}/delete_topic

    Doc: docs/api_delete-topic.md
    """
    client = ZulipClient()
    return client.request("POST", f"/streams/{stream_id}/delete_topic", data={"topic_name": topic_name})
