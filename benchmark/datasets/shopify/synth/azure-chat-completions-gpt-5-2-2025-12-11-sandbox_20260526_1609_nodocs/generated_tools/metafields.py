from typing import Any, Dict, Optional

from .client import ShopifyClient


def list_metafields(owner_resource: str, owner_id: int, limit: int = 50) -> Dict[str, Any]:
    """GET /{owner_resource}/{owner_id}/metafields.json"""
    return ShopifyClient().request("GET", f"/{owner_resource}/{owner_id}/metafields.json", params={"limit": limit})


def get_metafield(metafield_id: int) -> Dict[str, Any]:
    """GET /metafields/{id}.json"""
    return ShopifyClient().request("GET", f"/metafields/{metafield_id}.json")


def create_metafield(owner_resource: str, owner_id: int, metafield: Dict[str, Any]) -> Dict[str, Any]:
    """POST /{owner_resource}/{owner_id}/metafields.json"""
    return ShopifyClient().request("POST", f"/{owner_resource}/{owner_id}/metafields.json", json={"metafield": metafield})


def update_metafield(metafield_id: int, metafield: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /metafields/{id}.json"""
    return ShopifyClient().request("PUT", f"/metafields/{metafield_id}.json", json={"metafield": metafield})


def delete_metafield(metafield_id: int) -> Dict[str, Any]:
    """DELETE /metafields/{id}.json"""
    return ShopifyClient().request("DELETE", f"/metafields/{metafield_id}.json")


def list_shop_metafields(limit: int = 50) -> Dict[str, Any]:
    """GET /metafields.json"""
    return ShopifyClient().request("GET", "/metafields.json", params={"limit": limit})


def count_metafields(owner_resource: Optional[str] = None, owner_id: Optional[int] = None) -> Dict[str, Any]:
    """GET /metafields/count.json or /{owner_resource}/{owner_id}/metafields/count.json"""
    if owner_resource and owner_id is not None:
        return ShopifyClient().request("GET", f"/{owner_resource}/{owner_id}/metafields/count.json")
    return ShopifyClient().request("GET", "/metafields/count.json")
