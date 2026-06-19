from typing import Any, Dict, List, Optional, Union

from .http_client import ZulipClient, dumps_if_needed


def get_messages(
    *,
    anchor: Optional[Union[int, str]] = None,
    include_anchor: Optional[bool] = None,
    anchor_date: Optional[str] = None,
    num_before: Optional[int] = None,
    num_after: Optional[int] = None,
    filter_spec: Optional[List[Dict[str, Any]]] = None,
    client_gravatar: Optional[bool] = None,
    apply_markdown: Optional[bool] = None,
    message_ids: Optional[List[int]] = None,
    allow_empty_topic_name: Optional[bool] = None,
) -> Dict[str, Any]:
    """GET /messages

    Doc: docs/api_get-messages.md
    """
    client = ZulipClient()
    params: Dict[str, Any] = {}
    if anchor is not None:
        params["anchor"] = anchor
    if include_anchor is not None:
        params["include_anchor"] = include_anchor
    if anchor_date is not None:
        params["anchor_date"] = anchor_date
    if num_before is not None:
        params["num_before"] = num_before
    if num_after is not None:
        params["num_after"] = num_after
    if filter_spec is not None:
        params["narrow"] = dumps_if_needed(filter_spec)
    if client_gravatar is not None:
        params["client_gravatar"] = client_gravatar
    if apply_markdown is not None:
        params["apply_markdown"] = apply_markdown
    if message_ids is not None:
        params["message_ids"] = dumps_if_needed(message_ids)
    if allow_empty_topic_name is not None:
        params["allow_empty_topic_name"] = allow_empty_topic_name

    return client.request("GET", "/messages", params=params)


def upload_file(*, file_path: str) -> Dict[str, Any]:
    """POST /user_uploads

    Doc: docs/api_upload-file.md
    """
    client = ZulipClient()
    try:
        with open(file_path, "rb") as f:
            files = {"filename": f}
            return client.request("POST", "/user_uploads", files=files)
    except OSError as e:
        return {"error": str(e)}


def send_message(
    *,
    type: str,
    to: Union[str, int, List[Union[str, int]]],
    content: str,
    topic: Optional[str] = None,
    queue_id: Optional[str] = None,
    local_id: Optional[str] = None,
    read_by_sender: Optional[bool] = None,
) -> Dict[str, Any]:
    """POST /messages

    Doc: docs/api_send-message.md
    """
    client = ZulipClient()
    data: Dict[str, Any] = {
        "type": type,
        "to": dumps_if_needed(to),
        "content": content,
    }
    if topic is not None:
        data["topic"] = topic
    if queue_id is not None:
        data["queue_id"] = queue_id
    if local_id is not None:
        data["local_id"] = local_id
    if read_by_sender is not None:
        data["read_by_sender"] = read_by_sender

    return client.request("POST", "/messages", data=data)
