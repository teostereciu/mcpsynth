from typing import Any, Dict, List, Optional, Union

from .http_client import ZulipClient, clean_params


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
    """POST /messages"""
    data: Dict[str, Any] = {
        "type": type,
        "to": to,
        "content": content,
        "topic": topic,
        "queue_id": queue_id,
        "local_id": local_id,
        "read_by_sender": read_by_sender,
    }
    return client.request("POST", "/messages", data=clean_params(data))


def get_messages(
    client: ZulipClient,
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
    """GET /messages"""
    params: Dict[str, Any] = {
        "anchor": anchor,
        "include_anchor": include_anchor,
        "anchor_date": anchor_date,
        "num_before": num_before,
        "num_after": num_after,
        "filter_spec": filter_spec,
        "client_gravatar": client_gravatar,
        "apply_markdown": apply_markdown,
        "message_ids": message_ids,
        "allow_empty_topic_name": allow_empty_topic_name,
    }
    return client.request("GET", "/messages", params=clean_params(params))
