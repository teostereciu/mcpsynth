from typing import Any, Dict

from .client import ShopifyClient


def list_webhooks(limit: int = 250) -> Dict[str, Any]:
    """GET /webhooks.json"""
    return ShopifyClient().request("GET", "/webhooks.json", params={"limit": limit})


def get_webhook(webhook_id: int) -> Dict[str, Any]:
    """GET /webhooks/{id}.json"""
    return ShopifyClient().request("GET", f"/webhooks/{webhook_id}.json")


def create_webhook(webhook: Dict[str, Any]) -> Dict[str, Any]:
    """POST /webhooks.json"""
    return ShopifyClient().request("POST", "/webhooks.json", json={"webhook": webhook})


def update_webhook(webhook_id: int, webhook: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /webhooks/{id}.json"""
    return ShopifyClient().request("PUT", f"/webhooks/{webhook_id}.json", json={"webhook": webhook})


def delete_webhook(webhook_id: int) -> Dict[str, Any]:
    """DELETE /webhooks/{id}.json"""
    return ShopifyClient().request("DELETE", f"/webhooks/{webhook_id}.json")
