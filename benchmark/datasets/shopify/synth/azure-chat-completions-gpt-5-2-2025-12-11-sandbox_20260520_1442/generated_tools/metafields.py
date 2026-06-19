from typing import Any, Dict, Optional

from .client import ShopifyClient


def create_metafield(owner_resource: str, owner_id: int, metafield: Dict[str, Any], *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """POST /admin/api/2026-01/{owner_resource}/{owner_id}/metafields.json

    Note: Metafields are created via the owning resource endpoint (product, order, customer, etc.).
    """
    client = client or ShopifyClient()
    return client.request("POST", f"/{owner_resource}/{owner_id}/metafields.json", json_body={"metafield": metafield})


def list_metafields(
    owner_resource: str,
    owner_id: int,
    *,
    namespace: Optional[str] = None,
    key: Optional[str] = None,
    limit: Optional[int] = None,
    since_id: Optional[int] = None,
    client: Optional[ShopifyClient] = None,
) -> Dict[str, Any]:
    """GET /admin/api/2026-01/{owner_resource}/{owner_id}/metafields.json"""
    client = client or ShopifyClient()
    params: Dict[str, Any] = {}
    for k, v in {"namespace": namespace, "key": key, "limit": limit, "since_id": since_id}.items():
        if v is not None:
            params[k] = v
    return client.request("GET", f"/{owner_resource}/{owner_id}/metafields.json", params=params)


def get_metafield(owner_resource: str, owner_id: int, metafield_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/{owner_resource}/{owner_id}/metafields/{metafield_id}.json"""
    client = client or ShopifyClient()
    return client.request("GET", f"/{owner_resource}/{owner_id}/metafields/{metafield_id}.json")


def count_metafields(owner_resource: str, owner_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/{owner_resource}/{owner_id}/metafields/count.json"""
    client = client or ShopifyClient()
    return client.request("GET", f"/{owner_resource}/{owner_id}/metafields/count.json")


def update_metafield(
    owner_resource: str,
    owner_id: int,
    metafield_id: int,
    metafield: Dict[str, Any],
    *,
    client: Optional[ShopifyClient] = None,
) -> Dict[str, Any]:
    """PUT /admin/api/2026-01/{owner_resource}/{owner_id}/metafields/{metafield_id}.json"""
    client = client or ShopifyClient()
    return client.request(
        "PUT",
        f"/{owner_resource}/{owner_id}/metafields/{metafield_id}.json",
        json_body={"metafield": metafield},
    )


def delete_metafield(owner_resource: str, owner_id: int, metafield_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """DELETE /admin/api/2026-01/{owner_resource}/{owner_id}/metafields/{metafield_id}.json"""
    client = client or ShopifyClient()
    return client.request("DELETE", f"/{owner_resource}/{owner_id}/metafields/{metafield_id}.json")
