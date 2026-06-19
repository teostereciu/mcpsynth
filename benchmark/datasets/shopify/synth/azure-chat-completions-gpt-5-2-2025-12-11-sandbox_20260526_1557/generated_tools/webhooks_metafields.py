from typing import Any, Dict, Optional

from .http import ShopifyClient


# Webhooks

def list_webhooks(*, limit: Optional[int] = 50, since_id: Optional[int] = None, topic: Optional[str] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/webhooks.json"""
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if since_id is not None:
        params["since_id"] = since_id
    if topic is not None:
        params["topic"] = topic
    return ShopifyClient().request("GET", "/webhooks.json", params=params or None)


def get_webhook(*, webhook_id: int) -> Dict[str, Any]:
    """GET /admin/api/2026-01/webhooks/{webhook_id}.json"""
    return ShopifyClient().request("GET", f"/webhooks/{webhook_id}.json")


def count_webhooks(*, topic: Optional[str] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/webhooks/count.json"""
    params: Dict[str, Any] = {}
    if topic is not None:
        params["topic"] = topic
    return ShopifyClient().request("GET", "/webhooks/count.json", params=params or None)


def create_webhook(*, webhook: Dict[str, Any]) -> Dict[str, Any]:
    """POST /admin/api/2026-01/webhooks.json"""
    return ShopifyClient().request("POST", "/webhooks.json", json_body={"webhook": webhook})


def update_webhook(*, webhook_id: int, webhook: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /admin/api/2026-01/webhooks/{webhook_id}.json"""
    body = {"webhook": {**webhook, "id": webhook_id}}
    return ShopifyClient().request("PUT", f"/webhooks/{webhook_id}.json", json_body=body)


def delete_webhook(*, webhook_id: int) -> Dict[str, Any]:
    """DELETE /admin/api/2026-01/webhooks/{webhook_id}.json"""
    return ShopifyClient().request("DELETE", f"/webhooks/{webhook_id}.json")


# Metafields (generic helper for any owner resource)

def list_metafields(*, owner_resource: str, owner_id: int, limit: Optional[int] = 50) -> Dict[str, Any]:
    """GET /admin/api/2026-01/{owner_resource}/{owner_id}/metafields.json"""
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    return ShopifyClient().request("GET", f"/{owner_resource}/{owner_id}/metafields.json", params=params or None)


def get_metafield(*, owner_resource: str, owner_id: int, metafield_id: int) -> Dict[str, Any]:
    """GET /admin/api/2026-01/{owner_resource}/{owner_id}/metafields/{metafield_id}.json"""
    return ShopifyClient().request("GET", f"/{owner_resource}/{owner_id}/metafields/{metafield_id}.json")


def count_metafields(*, owner_resource: str, owner_id: int) -> Dict[str, Any]:
    """GET /admin/api/2026-01/{owner_resource}/{owner_id}/metafields/count.json"""
    return ShopifyClient().request("GET", f"/{owner_resource}/{owner_id}/metafields/count.json")


def create_metafield(*, owner_resource: str, owner_id: int, metafield: Dict[str, Any]) -> Dict[str, Any]:
    """POST /admin/api/2026-01/{owner_resource}/{owner_id}/metafields.json"""
    return ShopifyClient().request("POST", f"/{owner_resource}/{owner_id}/metafields.json", json_body={"metafield": metafield})


def update_metafield(*, owner_resource: str, owner_id: int, metafield_id: int, metafield: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /admin/api/2026-01/{owner_resource}/{owner_id}/metafields/{metafield_id}.json"""
    body = {"metafield": {**metafield, "id": metafield_id}}
    return ShopifyClient().request("PUT", f"/{owner_resource}/{owner_id}/metafields/{metafield_id}.json", json_body=body)


def delete_metafield(*, owner_resource: str, owner_id: int, metafield_id: int) -> Dict[str, Any]:
    """DELETE /admin/api/2026-01/{owner_resource}/{owner_id}/metafields/{metafield_id}.json"""
    return ShopifyClient().request("DELETE", f"/{owner_resource}/{owner_id}/metafields/{metafield_id}.json")
