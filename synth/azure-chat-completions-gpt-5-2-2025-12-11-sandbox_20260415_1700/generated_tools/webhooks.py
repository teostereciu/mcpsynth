from typing import Any, Dict, Optional

from .client import request_json


def webhook_create(webhook: Dict[str, Any]) -> Any:
    """POST /webhooks.json"""
    return request_json("POST", "/webhooks.json", json_body={"webhook": webhook})


def webhooks_list(*, limit: Optional[int] = None, since_id: Optional[int] = None, topic: Optional[str] = None, address: Optional[str] = None) -> Any:
    """GET /webhooks.json"""
    params: Dict[str, Any] = {}
    for k, v in {"limit": limit, "since_id": since_id, "topic": topic, "address": address}.items():
        if v is not None:
            params[k] = v
    return request_json("GET", "/webhooks.json", params=params or None)


def webhook_get(webhook_id: int) -> Any:
    """GET /webhooks/{webhook_id}.json"""
    return request_json("GET", f"/webhooks/{webhook_id}.json")


def webhooks_count(*, topic: Optional[str] = None, address: Optional[str] = None) -> Any:
    """GET /webhooks/count.json"""
    params: Dict[str, Any] = {}
    for k, v in {"topic": topic, "address": address}.items():
        if v is not None:
            params[k] = v
    return request_json("GET", "/webhooks/count.json", params=params or None)


def webhook_update(webhook_id: int, webhook: Dict[str, Any]) -> Any:
    """PUT /webhooks/{webhook_id}.json"""
    body = {"webhook": {**webhook, "id": webhook_id}}
    return request_json("PUT", f"/webhooks/{webhook_id}.json", json_body=body)


def webhook_delete(webhook_id: int) -> Any:
    """DELETE /webhooks/{webhook_id}.json"""
    return request_json("DELETE", f"/webhooks/{webhook_id}.json")
