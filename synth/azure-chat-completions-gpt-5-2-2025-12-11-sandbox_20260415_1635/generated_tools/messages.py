from typing import Any, Dict, List, Optional, Union

from ._client import ZulipClient, dumps_narrow


def update_message(
    message_id: int,
    content: Optional[str] = None,
    topic: Optional[str] = None,
    propagate_mode: Optional[str] = None,
    send_notification_to_old_thread: Optional[bool] = None,
    send_notification_to_new_thread: Optional[bool] = None,
    prev_content_sha256: Optional[str] = None,
    stream_id: Optional[int] = None,
) -> Dict[str, Any]:
    """PATCH /messages/{message_id}"""
    data: Dict[str, Any] = {}
    if content is not None:
        data["content"] = content
    if topic is not None:
        data["topic"] = topic
    if propagate_mode is not None:
        data["propagate_mode"] = propagate_mode
    if send_notification_to_old_thread is not None:
        data["send_notification_to_old_thread"] = send_notification_to_old_thread
    if send_notification_to_new_thread is not None:
        data["send_notification_to_new_thread"] = send_notification_to_new_thread
    if prev_content_sha256 is not None:
        data["prev_content_sha256"] = prev_content_sha256
    if stream_id is not None:
        data["stream_id"] = stream_id
    return ZulipClient().request("PATCH", f"/messages/{message_id}", data=data)


def delete_message(message_id: int) -> Dict[str, Any]:
    """DELETE /messages/{message_id}"""
    return ZulipClient().request("DELETE", f"/messages/{message_id}")


def send_message(
    type: str,
    to: Union[str, int, List[Union[str, int]]],
    content: str,
    topic: Optional[str] = None,
    queue_id: Optional[str] = None,
    local_id: Optional[str] = None,
    read_by_sender: Optional[bool] = None,
) -> Dict[str, Any]:
    """POST /messages"""
    data: Dict[str, Any] = {"type": type, "to": to, "content": content}
    if topic is not None:
        data["topic"] = topic
    if queue_id is not None:
        data["queue_id"] = queue_id
    if local_id is not None:
        data["local_id"] = local_id
    if read_by_sender is not None:
        data["read_by_sender"] = read_by_sender
    return ZulipClient().request("POST", "/messages", data=data)


def get_messages(
    anchor: Optional[Union[int, str]] = None,
    num_before: Optional[int] = None,
    num_after: Optional[int] = None,
    narrow: Optional[List[Dict[str, Any]]] = None,
    include_anchor: Optional[bool] = None,
    client_gravatar: Optional[bool] = None,
    apply_markdown: Optional[bool] = None,
    message_ids: Optional[List[int]] = None,
    allow_empty_topic_name: Optional[bool] = None,
    anchor_date: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /messages"""
    params: Dict[str, Any] = {}
    if anchor is not None:
        params["anchor"] = anchor
    if num_before is not None:
        params["num_before"] = num_before
    if num_after is not None:
        params["num_after"] = num_after
    if narrow is not None:
        params["narrow"] = dumps_narrow(narrow)
    if include_anchor is not None:
        params["include_anchor"] = include_anchor
    if client_gravatar is not None:
        params["client_gravatar"] = client_gravatar
    if apply_markdown is not None:
        params["apply_markdown"] = apply_markdown
    if message_ids is not None:
        params["message_ids"] = dumps_narrow(message_ids)
    if allow_empty_topic_name is not None:
        params["allow_empty_topic_name"] = allow_empty_topic_name
    if anchor_date is not None:
        params["anchor_date"] = anchor_date
    return ZulipClient().request("GET", "/messages", params=params)
