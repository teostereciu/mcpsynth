from typing import Any, Dict, Optional

from .http import shopify_request


def create_webhook(webhook: Dict[str, Any]) -> Dict[str, Any]:
    """POST /webhooks.json"""
    return shopify_request("POST", "/webhooks.json", json={"webhook": webhook})


def list_webhooks(*, address: Optional[str] = None, topic: Optional[str] = None, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /webhooks.json"""
    params: Dict[str, Any] = {}
    for k, v in {"address": address, "topic": topic, "fields": fields}.items():
        if v is not None:
            params[k] = v
    return shopify_request("GET", "/webhooks.json", params=params or None)


def get_webhook(webhook_id: int, *, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /webhooks/{webhook_id}.json"""
    params = {"fields": fields} if fields else None
    return shopify_request("GET", f"/webhooks/{webhook_id}.json", params=params)


def count_webhooks(*, topic: Optional[str] = None, address: Optional[str] = None) -> Dict[str, Any]:
    """GET /webhooks/count.json"""
    params: Dict[str, Any] = {}
    for k, v in {"topic": topic, "address": address}.items():
        if v is not None:
            params[k] = v
    return shopify_request("GET", "/webhooks/count.json", params=params or None)


def update_webhook(webhook_id: int, webhook: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /webhooks/{webhook_id}.json"""
    payload = dict(webhook)
    payload.setdefault("id", webhook_id)
    return shopify_request("PUT", f"/webhooks/{webhook_id}.json", json={"webhook": payload})


def delete_webhook(webhook_id: int) -> Dict[str, Any]:
    """DELETE /webhooks/{webhook_id}.json"""
    return shopify_request("DELETE", f"/webhooks/{webhook_id}.json")
