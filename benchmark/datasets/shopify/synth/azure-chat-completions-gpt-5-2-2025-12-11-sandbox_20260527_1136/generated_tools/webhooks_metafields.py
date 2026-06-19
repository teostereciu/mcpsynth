from typing import Any, Dict, Optional

from .http_client import ShopifyClient


# Webhooks

def create_webhook(webhook: Dict[str, Any], *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """POST /webhooks.json"""
    client = client or ShopifyClient()
    return client.request("POST", "/webhooks.json", json_body={"webhook": webhook})


def list_webhooks(*, client: Optional[ShopifyClient] = None, limit: Optional[int] = None, since_id: Optional[int] = None, topic: Optional[str] = None) -> Dict[str, Any]:
    """GET /webhooks.json"""
    client = client or ShopifyClient()
    params: Dict[str, Any] = {}
    for k, v in {"limit": limit, "since_id": since_id, "topic": topic}.items():
        if v is not None:
            params[k] = v
    return client.request("GET", "/webhooks.json", params=params or None)


def get_webhook(webhook_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """GET /webhooks/{webhook_id}.json"""
    client = client or ShopifyClient()
    return client.request("GET", f"/webhooks/{webhook_id}.json")


def count_webhooks(*, client: Optional[ShopifyClient] = None, topic: Optional[str] = None) -> Dict[str, Any]:
    """GET /webhooks/count.json"""
    client = client or ShopifyClient()
    params = {"topic": topic} if topic else None
    return client.request("GET", "/webhooks/count.json", params=params)


def update_webhook(webhook_id: int, webhook: Dict[str, Any], *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """PUT /webhooks/{webhook_id}.json"""
    client = client or ShopifyClient()
    body = {"webhook": {**webhook, "id": webhook_id}}
    return client.request("PUT", f"/webhooks/{webhook_id}.json", json_body=body)


def delete_webhook(webhook_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """DELETE /webhooks/{webhook_id}.json"""
    client = client or ShopifyClient()
    return client.request("DELETE", f"/webhooks/{webhook_id}.json")


# Metafields (generic helper: provide resource path prefix)

def create_metafield(resource_path_prefix: str, resource_id: int, metafield: Dict[str, Any], *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """POST /{resource_path_prefix}/{resource_id}/metafields.json (e.g. /products/{id}/metafields.json)"""
    client = client or ShopifyClient()
    return client.request("POST", f"/{resource_path_prefix}/{resource_id}/metafields.json", json_body={"metafield": metafield})


def list_metafields(resource_path_prefix: str, resource_id: int, *, client: Optional[ShopifyClient] = None, limit: Optional[int] = None, since_id: Optional[int] = None) -> Dict[str, Any]:
    """GET /{resource_path_prefix}/{resource_id}/metafields.json"""
    client = client or ShopifyClient()
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if since_id is not None:
        params["since_id"] = since_id
    return client.request("GET", f"/{resource_path_prefix}/{resource_id}/metafields.json", params=params or None)


def get_metafield(resource_path_prefix: str, resource_id: int, metafield_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """GET /{resource_path_prefix}/{resource_id}/metafields/{metafield_id}.json"""
    client = client or ShopifyClient()
    return client.request("GET", f"/{resource_path_prefix}/{resource_id}/metafields/{metafield_id}.json")


def count_metafields(resource_path_prefix: str, resource_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """GET /{resource_path_prefix}/{resource_id}/metafields/count.json"""
    client = client or ShopifyClient()
    return client.request("GET", f"/{resource_path_prefix}/{resource_id}/metafields/count.json")


def update_metafield(resource_path_prefix: str, resource_id: int, metafield_id: int, metafield: Dict[str, Any], *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """PUT /{resource_path_prefix}/{resource_id}/metafields/{metafield_id}.json"""
    client = client or ShopifyClient()
    body = {"metafield": {**metafield, "id": metafield_id}}
    return client.request("PUT", f"/{resource_path_prefix}/{resource_id}/metafields/{metafield_id}.json", json_body=body)


def delete_metafield(resource_path_prefix: str, resource_id: int, metafield_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """DELETE /{resource_path_prefix}/{resource_id}/metafields/{metafield_id}.json"""
    client = client or ShopifyClient()
    return client.request("DELETE", f"/{resource_path_prefix}/{resource_id}/metafields/{metafield_id}.json")
