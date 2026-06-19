from typing import Any, Dict, List, Optional, Union

from .client import ZulipClient, _maybe_json_dumps


def send_message(
    client: ZulipClient,
    type: str,
    to: Union[str, int, List[Union[str, int]]],
    content: str,
    topic: Optional[str] = None,
    queue_id: Optional[str] = None,
    local_id: Optional[str] = None,
    read_by_sender: Optional[bool] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "type": type,
        "to": _maybe_json_dumps(to),
        "content": content,
    }
    if topic is not None:
        params["topic"] = topic
    if queue_id is not None:
        params["queue_id"] = queue_id
    if local_id is not None:
        params["local_id"] = local_id
    if read_by_sender is not None:
        params["read_by_sender"] = "true" if read_by_sender else "false"

    return client.request("POST", "/messages", params)


def update_message(
    client: ZulipClient,
    message_id: int,
    content: Optional[str] = None,
    topic: Optional[str] = None,
    propagate_mode: Optional[str] = None,
    send_notification_to_old_thread: Optional[bool] = None,
    send_notification_to_new_thread: Optional[bool] = None,
    prev_content_sha256: Optional[str] = None,
    stream_id: Optional[int] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if content is not None:
        params["content"] = content
    if topic is not None:
        params["topic"] = topic
    if propagate_mode is not None:
        params["propagate_mode"] = propagate_mode
    if send_notification_to_old_thread is not None:
        params["send_notification_to_old_thread"] = "true" if send_notification_to_old_thread else "false"
    if send_notification_to_new_thread is not None:
        params["send_notification_to_new_thread"] = "true" if send_notification_to_new_thread else "false"
    if prev_content_sha256 is not None:
        params["prev_content_sha256"] = prev_content_sha256
    if stream_id is not None:
        params["stream_id"] = stream_id

    return client.request("PATCH", f"/messages/{message_id}", params)


def delete_message(client: ZulipClient, message_id: int) -> Dict[str, Any]:
    return client.request("DELETE", f"/messages/{message_id}")


def get_messages(
    client: ZulipClient,
    anchor: Optional[str] = None,
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
    params: Dict[str, Any] = {}
    if anchor is not None:
        params["anchor"] = anchor
    if num_before is not None:
        params["num_before"] = num_before
    if num_after is not None:
        params["num_after"] = num_after
    if narrow is not None:
        params["narrow"] = _maybe_json_dumps(narrow)
    if include_anchor is not None:
        params["include_anchor"] = "true" if include_anchor else "false"
    if client_gravatar is not None:
        params["client_gravatar"] = "true" if client_gravatar else "false"
    if apply_markdown is not None:
        params["apply_markdown"] = "true" if apply_markdown else "false"
    if message_ids is not None:
        params["message_ids"] = _maybe_json_dumps(message_ids)
    if allow_empty_topic_name is not None:
        params["allow_empty_topic_name"] = "true" if allow_empty_topic_name else "false"
    if anchor_date is not None:
        params["anchor_date"] = anchor_date

    return client.request("GET", "/messages", params)


def get_message(
    client: ZulipClient,
    message_id: int,
    apply_markdown: Optional[bool] = None,
    allow_empty_topic_name: Optional[bool] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if apply_markdown is not None:
        params["apply_markdown"] = "true" if apply_markdown else "false"
    if allow_empty_topic_name is not None:
        params["allow_empty_topic_name"] = "true" if allow_empty_topic_name else "false"
    return client.request("GET", f"/messages/{message_id}", params)
