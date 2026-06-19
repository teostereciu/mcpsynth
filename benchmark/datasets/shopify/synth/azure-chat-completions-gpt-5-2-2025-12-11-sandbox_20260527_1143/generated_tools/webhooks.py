from typing import Any, Dict, Optional

from .http import request_json


def create_webhook(webhook: Dict[str, Any]) -> Dict[str, Any]:
    """POST /webhooks.json"""
    return request_json("POST", "/webhooks.json", json_body={"webhook": webhook})


def list_webhooks(*, limit: Optional[int] = None, since_id: Optional[int] = None, topic: Optional[str] = None, address: Optional[str] = None) -> Dict[str, Any]:
    """GET /webhooks.json"""
    params: Dict[str, Any] = {}
    for k, v in {"limit": limit, "since_id": since_id, "topic": topic, "address": address}.items():
        if v is not None:
            params[k] = v
    return request_json("GET", "/webhooks.json", params=params)


def get_webhook(webhook_id: int) -> Dict[str, Any]:
    """GET /webhooks/{webhook_id}.json"""
    return request_json("GET", f"/webhooks/{webhook_id}.json")


def count_webhooks(*, topic: Optional[str] = None, address: Optional[str] = None) -> Dict[str, Any]:
    """GET /webhooks/count.json"""
    params: Dict[str, Any] = {}
    for k, v in {"topic": topic, "address": address}.items():
        if v is not None:
            params[k] = v
    return request_json("GET", "/webhooks/count.json", params=params if params else None)


def update_webhook(webhook_id: int, webhook: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /webhooks/{webhook_id}.json"""
    return request_json("PUT", f"/webhooks/{webhook_id}.json", json_body={"webhook": webhook})


def delete_webhook(webhook_id: int) -> Dict[str, Any]:
    """DELETE /webhooks/{webhook_id}.json"""
    return request_json("DELETE", f"/webhooks/{webhook_id}.json")
