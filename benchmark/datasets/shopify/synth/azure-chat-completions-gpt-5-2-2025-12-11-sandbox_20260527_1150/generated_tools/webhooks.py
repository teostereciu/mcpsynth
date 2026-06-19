from typing import Any, Dict, Optional

from .http_client import ShopifyAdminClient


def create_webhook(webhook: Dict[str, Any], *, api_version: str = "2026-01") -> Dict[str, Any]:
    """POST /admin/api/2026-01/webhooks.json"""
    client = ShopifyAdminClient(api_version=api_version)
    return client.request("POST", "/webhooks.json", json_body={"webhook": webhook})


def list_webhooks(*, api_version: str = "2026-01", address: Optional[str] = None, topic: Optional[str] = None, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/webhooks.json"""
    client = ShopifyAdminClient(api_version=api_version)
    params: Dict[str, Any] = {}
    for k, v in {"address": address, "topic": topic, "fields": fields}.items():
        if v is not None:
            params[k] = v
    return client.request("GET", "/webhooks.json", params=params or None)


def get_webhook(webhook_id: int, *, api_version: str = "2026-01", fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/webhooks/{webhook_id}.json"""
    client = ShopifyAdminClient(api_version=api_version)
    params = {"fields": fields} if fields else None
    return client.request("GET", f"/webhooks/{webhook_id}.json", params=params)


def count_webhooks(*, api_version: str = "2026-01", topic: Optional[str] = None, address: Optional[str] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/webhooks/count.json"""
    client = ShopifyAdminClient(api_version=api_version)
    params: Dict[str, Any] = {}
    for k, v in {"topic": topic, "address": address}.items():
        if v is not None:
            params[k] = v
    return client.request("GET", "/webhooks/count.json", params=params or None)


def update_webhook(webhook_id: int, webhook: Dict[str, Any], *, api_version: str = "2026-01") -> Dict[str, Any]:
    """PUT /admin/api/2026-01/webhooks/{webhook_id}.json"""
    client = ShopifyAdminClient(api_version=api_version)
    body = {"webhook": {**webhook, "id": webhook_id}}
    return client.request("PUT", f"/webhooks/{webhook_id}.json", json_body=body)


def delete_webhook(webhook_id: int, *, api_version: str = "2026-01") -> Dict[str, Any]:
    """DELETE /admin/api/2026-01/webhooks/{webhook_id}.json"""
    client = ShopifyAdminClient(api_version=api_version)
    return client.request("DELETE", f"/webhooks/{webhook_id}.json")
