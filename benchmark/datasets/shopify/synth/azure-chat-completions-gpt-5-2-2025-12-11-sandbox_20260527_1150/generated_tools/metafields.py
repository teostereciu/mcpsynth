from typing import Any, Dict, Optional

from .http_client import ShopifyAdminClient


# Metafields are exposed on many resource-specific endpoints. We implement a commonly-used subset
# for products, variants, orders, customers, and shop.


def create_product_metafield(product_id: int, metafield: Dict[str, Any], *, api_version: str = "2026-01") -> Dict[str, Any]:
    """POST /admin/api/2026-01/products/{product_id}/metafields.json"""
    client = ShopifyAdminClient(api_version=api_version)
    return client.request("POST", f"/products/{product_id}/metafields.json", json_body={"metafield": metafield})


def list_product_metafields(product_id: int, *, api_version: str = "2026-01", namespace: Optional[str] = None, key: Optional[str] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/products/{product_id}/metafields.json"""
    client = ShopifyAdminClient(api_version=api_version)
    params: Dict[str, Any] = {}
    if namespace is not None:
        params["namespace"] = namespace
    if key is not None:
        params["key"] = key
    return client.request("GET", f"/products/{product_id}/metafields.json", params=params or None)


def get_product_metafield(product_id: int, metafield_id: int, *, api_version: str = "2026-01") -> Dict[str, Any]:
    """GET /admin/api/2026-01/products/{product_id}/metafields/{metafield_id}.json"""
    client = ShopifyAdminClient(api_version=api_version)
    return client.request("GET", f"/products/{product_id}/metafields/{metafield_id}.json")


def update_product_metafield(product_id: int, metafield_id: int, metafield: Dict[str, Any], *, api_version: str = "2026-01") -> Dict[str, Any]:
    """PUT /admin/api/2026-01/products/{product_id}/metafields/{metafield_id}.json"""
    client = ShopifyAdminClient(api_version=api_version)
    body = {"metafield": {**metafield, "id": metafield_id}}
    return client.request("PUT", f"/products/{product_id}/metafields/{metafield_id}.json", json_body=body)


def delete_product_metafield(product_id: int, metafield_id: int, *, api_version: str = "2026-01") -> Dict[str, Any]:
    """DELETE /admin/api/2026-01/products/{product_id}/metafields/{metafield_id}.json"""
    client = ShopifyAdminClient(api_version=api_version)
    return client.request("DELETE", f"/products/{product_id}/metafields/{metafield_id}.json")


def create_variant_metafield(variant_id: int, metafield: Dict[str, Any], *, api_version: str = "2026-01") -> Dict[str, Any]:
    """POST /admin/api/2026-01/variants/{variant_id}/metafields.json"""
    client = ShopifyAdminClient(api_version=api_version)
    return client.request("POST", f"/variants/{variant_id}/metafields.json", json_body={"metafield": metafield})


def list_variant_metafields(variant_id: int, *, api_version: str = "2026-01", namespace: Optional[str] = None, key: Optional[str] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/variants/{variant_id}/metafields.json"""
    client = ShopifyAdminClient(api_version=api_version)
    params: Dict[str, Any] = {}
    if namespace is not None:
        params["namespace"] = namespace
    if key is not None:
        params["key"] = key
    return client.request("GET", f"/variants/{variant_id}/metafields.json", params=params or None)


def create_order_metafield(order_id: int, metafield: Dict[str, Any], *, api_version: str = "2026-01") -> Dict[str, Any]:
    """POST /admin/api/2026-01/orders/{order_id}/metafields.json"""
    client = ShopifyAdminClient(api_version=api_version)
    return client.request("POST", f"/orders/{order_id}/metafields.json", json_body={"metafield": metafield})


def list_order_metafields(order_id: int, *, api_version: str = "2026-01", namespace: Optional[str] = None, key: Optional[str] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/orders/{order_id}/metafields.json"""
    client = ShopifyAdminClient(api_version=api_version)
    params: Dict[str, Any] = {}
    if namespace is not None:
        params["namespace"] = namespace
    if key is not None:
        params["key"] = key
    return client.request("GET", f"/orders/{order_id}/metafields.json", params=params or None)


def create_customer_metafield(customer_id: int, metafield: Dict[str, Any], *, api_version: str = "2026-01") -> Dict[str, Any]:
    """POST /admin/api/2026-01/customers/{customer_id}/metafields.json"""
    client = ShopifyAdminClient(api_version=api_version)
    return client.request("POST", f"/customers/{customer_id}/metafields.json", json_body={"metafield": metafield})


def list_customer_metafields(customer_id: int, *, api_version: str = "2026-01", namespace: Optional[str] = None, key: Optional[str] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/customers/{customer_id}/metafields.json"""
    client = ShopifyAdminClient(api_version=api_version)
    params: Dict[str, Any] = {}
    if namespace is not None:
        params["namespace"] = namespace
    if key is not None:
        params["key"] = key
    return client.request("GET", f"/customers/{customer_id}/metafields.json", params=params or None)


def list_shop_metafields(*, api_version: str = "2026-01", namespace: Optional[str] = None, key: Optional[str] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/metafields.json"""
    client = ShopifyAdminClient(api_version=api_version)
    params: Dict[str, Any] = {}
    if namespace is not None:
        params["namespace"] = namespace
    if key is not None:
        params["key"] = key
    return client.request("GET", "/metafields.json", params=params or None)
