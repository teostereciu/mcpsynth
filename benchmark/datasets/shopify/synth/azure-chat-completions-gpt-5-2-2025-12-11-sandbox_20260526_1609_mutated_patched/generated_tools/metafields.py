from typing import Any, Dict, Optional

from .http import ShopifyClient


# Metafields are created/listed via the owning resource endpoint.
# This module provides helpers for common owners (products, orders, customers).


def list_product_metafields(*, product_id: int, limit: int = 50) -> Dict[str, Any]:
    """GET /admin/api/2026-01/products/{product_id}/metafields.json"""
    return ShopifyClient().request(
        "GET",
        f"/products/{product_id}/metafields.json",
        params={"limit": limit},
    )


def create_product_metafield(*, product_id: int, metafield: Dict[str, Any]) -> Dict[str, Any]:
    """POST /admin/api/2026-01/products/{product_id}/metafields.json"""
    return ShopifyClient().request(
        "POST",
        f"/products/{product_id}/metafields.json",
        json={"metafield": metafield},
    )


def list_order_metafields(*, order_id: int, limit: int = 50) -> Dict[str, Any]:
    """GET /admin/api/2026-01/orders/{order_id}/metafields.json"""
    return ShopifyClient().request(
        "GET",
        f"/orders/{order_id}/metafields.json",
        params={"limit": limit},
    )


def create_order_metafield(*, order_id: int, metafield: Dict[str, Any]) -> Dict[str, Any]:
    """POST /admin/api/2026-01/orders/{order_id}/metafields.json"""
    return ShopifyClient().request(
        "POST",
        f"/orders/{order_id}/metafields.json",
        json={"metafield": metafield},
    )


def list_customer_metafields(*, customer_id: int, limit: int = 50) -> Dict[str, Any]:
    """GET /admin/api/2026-01/customers/{customer_id}/metafields.json"""
    return ShopifyClient().request(
        "GET",
        f"/customers/{customer_id}/metafields.json",
        params={"limit": limit},
    )


def create_customer_metafield(*, customer_id: int, metafield: Dict[str, Any]) -> Dict[str, Any]:
    """POST /admin/api/2026-01/customers/{customer_id}/metafields.json"""
    return ShopifyClient().request(
        "POST",
        f"/customers/{customer_id}/metafields.json",
        json={"metafield": metafield},
    )


def get_metafield(*, metafield_id: int) -> Dict[str, Any]:
    """GET /admin/api/2026-01/metafields/{metafield_id}.json

    Note: Shopify supports a global metafield endpoint for direct access by ID.
    """
    return ShopifyClient().request("GET", f"/metafields/{metafield_id}.json")


def update_metafield(*, metafield_id: int, metafield: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /admin/api/2026-01/metafields/{metafield_id}.json"""
    body = {"metafield": {**metafield, "id": metafield_id}}
    return ShopifyClient().request("PUT", f"/metafields/{metafield_id}.json", json=body)


def delete_metafield(*, metafield_id: int) -> Dict[str, Any]:
    """DELETE /admin/api/2026-01/metafields/{metafield_id}.json"""
    return ShopifyClient().request("DELETE", f"/metafields/{metafield_id}.json")
