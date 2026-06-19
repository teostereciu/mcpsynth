from typing import Any, Dict, List, Optional, Union

from .client import ZulipClient, _maybe_json_loads


def get_messages(
    anchor: Optional[str] = None,
    num_before: Optional[int] = None,
    num_after: Optional[int] = None,
    narrow: Optional[Union[str, List[Dict[str, Any]]]] = None,
    include_anchor: Optional[bool] = None,
    client_gravatar: Optional[bool] = None,
    apply_markdown: Optional[bool] = None,
    message_ids: Optional[Union[str, List[int]]] = None,
    allow_empty_topic_name: Optional[bool] = None,
    use_first_unread_anchor: Optional[bool] = None,
    anchor_date: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /messages

    Doc: docs/api_get-messages.md
    """
    client = ZulipClient()
    params: Dict[str, Any] = {}
    if anchor is not None:
        params["anchor"] = anchor
    if num_before is not None:
        params["num_before"] = num_before
    if num_after is not None:
        params["num_after"] = num_after
    if include_anchor is not None:
        params["include_anchor"] = include_anchor
    if client_gravatar is not None:
        params["client_gravatar"] = client_gravatar
    if apply_markdown is not None:
        params["apply_markdown"] = apply_markdown
    if allow_empty_topic_name is not None:
        params["allow_empty_topic_name"] = allow_empty_topic_name
    if use_first_unread_anchor is not None:
        params["use_first_unread_anchor"] = use_first_unread_anchor
    if anchor_date is not None:
        params["anchor_date"] = anchor_date

    if narrow is not None:
        narrow_val = _maybe_json_loads(narrow)
        if isinstance(narrow_val, (list, dict)):
            import json as _json

            params["narrow"] = _json.dumps(narrow_val)
        else:
            params["narrow"] = narrow_val

    if message_ids is not None:
        mids = _maybe_json_loads(message_ids)
        if isinstance(mids, (list, dict)):
            import json as _json

            params["message_ids"] = _json.dumps(mids)
        else:
            params["message_ids"] = mids

    return client.request("GET", "/messages", params=params)



def send_message(
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
    params: Dict[str, Any] = {
        "type": type,
        "to": to,
        "content": content,
    }
    if topic is not None:
        params["topic"] = topic
    if queue_id is not None:
        params["queue_id"] = queue_id
    if local_id is not None:
        params["local_id"] = local_id
    if read_by_sender is not None:
        params["read_by_sender"] = read_by_sender

    # Zulip expects some complex params as JSON-encoded strings in form data.
    params["to"] = _maybe_json_loads(params["to"])
    if isinstance(params["to"], (list, dict)):
        import json as _json

        params["to"] = _json.dumps(params["to"])

    return client.request("POST", "/messages", params=params)
