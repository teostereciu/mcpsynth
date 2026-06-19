from typing import Any, Dict, Optional

from .http_client import ShopifyClient


def webhook_create(webhook: Dict[str, Any]) -> Dict[str, Any]:
    """POST /admin/api/2026-01/webhooks.json"""
    client = ShopifyClient()
    return client.request("POST", "/webhooks.json", json_body={"webhook": webhook})


def webhooks_list(*, limit: Optional[int] = None, since_id: Optional[int] = None, topic: Optional[str] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/webhooks.json"""
    client = ShopifyClient()
    params: Dict[str, Any] = {}
    for k, v in {"limit": limit, "since_id": since_id, "topic": topic}.items():
        if v is not None:
            params[k] = v
    return client.request("GET", "/webhooks.json", params=params if params else None)


def webhook_get(webhook_id: int) -> Dict[str, Any]:
    """GET /admin/api/2026-01/webhooks/{webhook_id}.json"""
    client = ShopifyClient()
    return client.request("GET", f"/webhooks/{webhook_id}.json")


def webhooks_count(*, topic: Optional[str] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/webhooks/count.json"""
    client = ShopifyClient()
    params = {"topic": topic} if topic else None
    return client.request("GET", "/webhooks/count.json", params=params)


def webhook_update(webhook_id: int, webhook: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /admin/api/2026-01/webhooks/{webhook_id}.json"""
    client = ShopifyClient()
    body = {"webhook": {**webhook, "id": webhook_id}}
    return client.request("PUT", f"/webhooks/{webhook_id}.json", json_body=body)


def webhook_delete(webhook_id: int) -> Dict[str, Any]:
    """DELETE /admin/api/2026-01/webhooks/{webhook_id}.json"""
    client = ShopifyClient()
    return client.request("DELETE", f"/webhooks/{webhook_id}.json")
