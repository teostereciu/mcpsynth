from typing import Any, Dict, Optional

from .client import ShopifyClient


def create_webhook(webhook: Dict[str, Any], *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """POST /admin/api/2026-01/webhooks.json"""
    client = client or ShopifyClient()
    return client.request("POST", "/webhooks.json", json_body={"webhook": webhook})


def list_webhooks(
    *,
    address: Optional[str] = None,
    topic: Optional[str] = None,
    fields: Optional[str] = None,
    limit: Optional[int] = None,
    since_id: Optional[int] = None,
    client: Optional[ShopifyClient] = None,
) -> Dict[str, Any]:
    """GET /admin/api/2026-01/webhooks.json"""
    client = client or ShopifyClient()
    params: Dict[str, Any] = {}
    for k, v in {"address": address, "topic": topic, "fields": fields, "limit": limit, "since_id": since_id}.items():
        if v is not None:
            params[k] = v
    return client.request("GET", "/webhooks.json", params=params)


def get_webhook(webhook_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/webhooks/{webhook_id}.json"""
    client = client or ShopifyClient()
    return client.request("GET", f"/webhooks/{webhook_id}.json")


def count_webhooks(*, topic: Optional[str] = None, address: Optional[str] = None, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/webhooks/count.json"""
    client = client or ShopifyClient()
    params: Dict[str, Any] = {}
    if topic is not None:
        params["topic"] = topic
    if address is not None:
        params["address"] = address
    return client.request("GET", "/webhooks/count.json", params=params)


def update_webhook(webhook_id: int, webhook: Dict[str, Any], *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """PUT /admin/api/2026-01/webhooks/{webhook_id}.json"""
    client = client or ShopifyClient()
    return client.request("PUT", f"/webhooks/{webhook_id}.json", json_body={"webhook": webhook})


def delete_webhook(webhook_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """DELETE /admin/api/2026-01/webhooks/{webhook_id}.json"""
    client = client or ShopifyClient()
    return client.request("DELETE", f"/webhooks/{webhook_id}.json")
