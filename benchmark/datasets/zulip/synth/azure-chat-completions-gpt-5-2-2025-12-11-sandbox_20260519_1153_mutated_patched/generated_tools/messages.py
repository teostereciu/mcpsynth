from typing import Any, Dict, List, Optional, Union

from .client import ZulipClient, _maybe_json_dumps


def send_message(
    *,
    type: str,
    to: Union[str, int, List[str], List[int]],
    content: str,
    topic: Optional[str] = None,
    queue_id: Optional[str] = None,
    local_id: Optional[str] = None,
    read_by_sender: Optional[bool] = None,
) -> Dict[str, Any]:
    """POST /messages

    Send a channel or direct message.

    Args:
      type: One of direct/channel/channel_name/private.
      to: Channel name/id for channel messages; list of user ids/emails for direct.
      content: Message content.
      topic: Topic for channel messages.
      queue_id/local_id: For local echo.
      read_by_sender: Mark read by sender.
    """
    client = ZulipClient()
    data: Dict[str, Any] = {
        "type": type,
        "to": _maybe_json_dumps(to),
        "content": content,
    }
    if topic is not None:
        data["topic"] = topic
    if queue_id is not None:
        data["queue_id"] = queue_id
    if local_id is not None:
        data["local_id"] = local_id
    if read_by_sender is not None:
        data["read_by_sender"] = "true" if read_by_sender else "false"

    return client.request("POST", "/messages", data=data)


def update_message(
    *,
    message_id: int,
    content: Optional[str] = None,
    topic: Optional[str] = None,
    propagate_mode: Optional[str] = None,
    send_notification_to_old_thread: Optional[bool] = None,
    send_notification_to_new_thread: Optional[bool] = None,
    prev_content_sha256: Optional[str] = None,
    stream_id: Optional[int] = None,
) -> Dict[str, Any]:
    """PATCH /messages/{message_id}

    Edit message content and/or move between topics/channels.
    """
    client = ZulipClient()
    data: Dict[str, Any] = {}
    if content is not None:
        data["content"] = content
    if topic is not None:
        data["topic"] = topic
    if propagate_mode is not None:
        data["propagate_mode"] = propagate_mode
    if send_notification_to_old_thread is not None:
        data["send_notification_to_old_thread"] = "true" if send_notification_to_old_thread else "false"
    if send_notification_to_new_thread is not None:
        data["send_notification_to_new_thread"] = "true" if send_notification_to_new_thread else "false"
    if prev_content_sha256 is not None:
        data["prev_content_sha256"] = prev_content_sha256
    if stream_id is not None:
        data["stream_id"] = str(stream_id)

    return client.request("PATCH", f"/messages/{message_id}", data=data)


def get_messages(
    *,
    anchor: Optional[str] = None,
    num_before: Optional[int] = None,
    num_after: Optional[int] = None,
    filter_spec: Optional[List[Dict[str, Any]]] = None,
    include_anchor: Optional[bool] = None,
    client_gravatar: Optional[bool] = None,
    apply_markdown: Optional[bool] = None,
    message_ids: Optional[List[int]] = None,
    allow_empty_topic_name: Optional[bool] = None,
) -> Dict[str, Any]:
    """GET /messages

    Fetch messages matching a narrow (filter_spec) around an anchor.
    """
    client = ZulipClient()
    params: Dict[str, Any] = {}
    if anchor is not None:
        params["anchor"] = anchor
    if num_before is not None:
        params["num_before"] = str(num_before)
    if num_after is not None:
        params["num_after"] = str(num_after)
    if filter_spec is not None:
        params["narrow"] = _maybe_json_dumps(filter_spec)
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

    return client.request("GET", "/messages", params=params)


def get_message(
    *,
    message_id: int,
    apply_markdown: Optional[bool] = None,
    allow_empty_topic_name: Optional[bool] = None,
) -> Dict[str, Any]:
    """GET /messages/{message_id}"""
    client = ZulipClient()
    params: Dict[str, Any] = {}
    if apply_markdown is not None:
        params["apply_markdown"] = "true" if apply_markdown else "false"
    if allow_empty_topic_name is not None:
        params["allow_empty_topic_name"] = "true" if allow_empty_topic_name else "false"
    return client.request("GET", f"/messages/{message_id}", params=params)


def add_reaction(
    *,
    message_id: int,
    emoji_name: str,
    emoji_code: Optional[str] = None,
    reaction_type: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /messages/{message_id}/reactions"""
    client = ZulipClient()
    data: Dict[str, Any] = {"emoji_name": emoji_name}
    if emoji_code is not None:
        data["emoji_code"] = emoji_code
    if reaction_type is not None:
        data["reaction_type"] = reaction_type
    return client.request("POST", f"/messages/{message_id}/reactions", data=data)


def remove_reaction(
    *,
    message_id: int,
    emoji_name: Optional[str] = None,
    emoji_code: Optional[str] = None,
    reaction_type: Optional[str] = None,
) -> Dict[str, Any]:
    """DELETE /messages/{message_id}/reactions"""
    client = ZulipClient()
    params: Dict[str, Any] = {}
    if emoji_name is not None:
        params["emoji_name"] = emoji_name
    if emoji_code is not None:
        params["emoji_code"] = emoji_code
    if reaction_type is not None:
        params["reaction_type"] = reaction_type
    return client.request("DELETE", f"/messages/{message_id}/reactions", params=params)


def delete_message(*, message_id: int) -> Dict[str, Any]:
    """DELETE /messages/{message_id}"""
    client = ZulipClient()
    return client.request("DELETE", f"/messages/{message_id}")
