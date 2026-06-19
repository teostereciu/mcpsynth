from typing import Any, Dict, Optional

from .client import ShopifyClient, clean_params


def create_webhook(webhook: Dict[str, Any], *, client: Optional[ShopifyClient] = None) -> Any:
    """POST /webhooks.json"""
    client = client or ShopifyClient()
    return client.request("POST", "/webhooks.json", json={"webhook": webhook})


def list_webhooks(*, limit: Optional[int] = None, since_id: Optional[int] = None, client: Optional[ShopifyClient] = None) -> Any:
    """GET /webhooks.json"""
    client = client or ShopifyClient()
    params = clean_params({"limit": limit, "since_id": since_id})
    return client.request("GET", "/webhooks.json", params=params)


def get_webhook(webhook_id: int, *, client: Optional[ShopifyClient] = None) -> Any:
    """GET /webhooks/{webhook_id}.json"""
    client = client or ShopifyClient()
    return client.request("GET", f"/webhooks/{webhook_id}.json")


def count_webhooks(*, topic: Optional[str] = None, address: Optional[str] = None, client: Optional[ShopifyClient] = None) -> Any:
    """GET /webhooks/count.json"""
    client = client or ShopifyClient()
    params = clean_params({"topic": topic, "address": address})
    return client.request("GET", "/webhooks/count.json", params=params)


def update_webhook(webhook_id: int, webhook: Dict[str, Any], *, client: Optional[ShopifyClient] = None) -> Any:
    """PUT /webhooks/{webhook_id}.json"""
    client = client or ShopifyClient()
    body = {"webhook": {**webhook, "id": webhook_id}}
    return client.request("PUT", f"/webhooks/{webhook_id}.json", json=body)


def delete_webhook(webhook_id: int, *, client: Optional[ShopifyClient] = None) -> Any:
    """DELETE /webhooks/{webhook_id}.json"""
    client = client or ShopifyClient()
    return client.request("DELETE", f"/webhooks/{webhook_id}.json")
