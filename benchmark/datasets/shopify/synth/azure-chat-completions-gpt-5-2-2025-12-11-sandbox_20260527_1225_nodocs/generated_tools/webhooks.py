from typing import Any, Dict, Optional

from .client import ShopifyClient


def list_webhooks(limit: int = 50, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /webhooks.json"""
    client = ShopifyClient()
    params: Dict[str, Any] = {"limit": limit}
    if fields:
        params["fields"] = fields
    return client.request("GET", "/webhooks.json", params=params)


def get_webhook(webhook_id: int) -> Dict[str, Any]:
    """GET /webhooks/{webhook_id}.json"""
    client = ShopifyClient()
    return client.request("GET", f"/webhooks/{webhook_id}.json")


def create_webhook(webhook: Dict[str, Any]) -> Dict[str, Any]:
    """POST /webhooks.json"""
    client = ShopifyClient()
    return client.request("POST", "/webhooks.json", json_body={"webhook": webhook})


def update_webhook(webhook_id: int, webhook: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /webhooks/{webhook_id}.json"""
    client = ShopifyClient()
    body = {"webhook": {**webhook, "id": webhook_id}}
    return client.request("PUT", f"/webhooks/{webhook_id}.json", json_body=body)


def delete_webhook(webhook_id: int) -> Dict[str, Any]:
    """DELETE /webhooks/{webhook_id}.json"""
    client = ShopifyClient()
    return client.request("DELETE", f"/webhooks/{webhook_id}.json")
