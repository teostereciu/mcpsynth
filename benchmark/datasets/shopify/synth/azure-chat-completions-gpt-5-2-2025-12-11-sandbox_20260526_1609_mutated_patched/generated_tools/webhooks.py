from typing import Any, Dict, Optional

from .http import ShopifyClient


def list_webhooks(*, limit: int = 50, since_id: Optional[int] = None, topic: Optional[str] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/webhooks.json"""
    params: Dict[str, Any] = {"limit": limit}
    if since_id is not None:
        params["since_id"] = since_id
    if topic:
        params["topic"] = topic
    return ShopifyClient().request("GET", "/webhooks.json", params=params)


def get_webhook(*, webhook_id: int) -> Dict[str, Any]:
    """GET /admin/api/2026-01/webhooks/{webhook_id}.json"""
    return ShopifyClient().request("GET", f"/webhooks/{webhook_id}.json")


def count_webhooks(*, topic: Optional[str] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/webhooks/count.json"""
    params: Dict[str, Any] = {}
    if topic:
        params["topic"] = topic
    return ShopifyClient().request("GET", "/webhooks/count.json", params=params)


def create_webhook(*, webhook: Dict[str, Any]) -> Dict[str, Any]:
    """POST /admin/api/2026-01/webhooks.json"""
    return ShopifyClient().request("POST", "/webhooks.json", json={"webhook": webhook})


def update_webhook(*, webhook_id: int, webhook: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /admin/api/2026-01/webhooks/{webhook_id}.json"""
    body = {"webhook": {**webhook, "id": webhook_id}}
    return ShopifyClient().request("PUT", f"/webhooks/{webhook_id}.json", json=body)


def delete_webhook(*, webhook_id: int) -> Dict[str, Any]:
    """DELETE /admin/api/2026-01/webhooks/{webhook_id}.json"""
    return ShopifyClient().request("DELETE", f"/webhooks/{webhook_id}.json")
