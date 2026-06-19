from typing import Any, Dict, Optional

from .shopify_client import ShopifyClient, build_params


def create_webhook(webhook: Dict[str, Any], *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """POST /admin/api/2026-01/webhooks.json"""
    client = client or ShopifyClient()
    return client.request("POST", "/webhooks.json", json={"webhook": webhook})


def list_webhooks(
    *,
    address: Optional[str] = None,
    topic: Optional[str] = None,
    fields: Optional[str] = None,
    client: Optional[ShopifyClient] = None,
) -> Dict[str, Any]:
    """GET /admin/api/2026-01/webhooks.json"""
    client = client or ShopifyClient()
    params = build_params(address=address, topic=topic, fields=fields)
    return client.request("GET", "/webhooks.json", params=params)


def get_webhook(webhook_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/webhooks/{webhook_id}.json"""
    client = client or ShopifyClient()
    return client.request("GET", f"/webhooks/{webhook_id}.json")


def count_webhooks(*, topic: Optional[str] = None, address: Optional[str] = None, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/webhooks/count.json"""
    client = client or ShopifyClient()
    params = build_params(topic=topic, address=address)
    return client.request("GET", "/webhooks/count.json", params=params)


def update_webhook(webhook_id: int, webhook: Dict[str, Any], *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """PUT /admin/api/2026-01/webhooks/{webhook_id}.json"""
    client = client or ShopifyClient()
    return client.request("PUT", f"/webhooks/{webhook_id}.json", json={"webhook": webhook})


def delete_webhook(webhook_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """DELETE /admin/api/2026-01/webhooks/{webhook_id}.json"""
    client = client or ShopifyClient()
    return client.request("DELETE", f"/webhooks/{webhook_id}.json")
