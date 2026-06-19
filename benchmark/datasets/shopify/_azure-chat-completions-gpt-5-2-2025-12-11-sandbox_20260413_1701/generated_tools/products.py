from __future__ import annotations

from typing import Any, Dict, List, Optional, Union

from . import mcp, client


@mcp.tool()
def list_products(
    limit: int = 50,
    status: Optional[str] = None,
    ids: Optional[str] = None,
    fields: Optional[str] = None,
    since_id: Optional[Union[int, str]] = None,
    title: Optional[str] = None,
    vendor: Optional[str] = None,
    product_type: Optional[str] = None,
    handle: Optional[str] = None,
    created_at_min: Optional[str] = None,
    created_at_max: Optional[str] = None,
    updated_at_min: Optional[str] = None,
    updated_at_max: Optional[str] = None,
    published_at_min: Optional[str] = None,
    published_at_max: Optional[str] = None,
) -> List[Dict[str, Any]]:
    """Retrieve a list of products."""
    params: Dict[str, Any] = {"limit": limit}
    for k, v in {
        "status": status,
        "ids": ids,
        "fields": fields,
        "since_id": since_id,
        "title": title,
        "vendor": vendor,
        "product_type": product_type,
        "handle": handle,
        "created_at_min": created_at_min,
        "created_at_max": created_at_max,
        "updated_at_min": updated_at_min,
        "updated_at_max": updated_at_max,
        "published_at_min": published_at_min,
        "published_at_max": published_at_max,
    }.items():
        if v is not None:
            params[k] = v
    return client.request("GET", "/products.json", params=params)


@mcp.tool()
def get_product(product_id: Union[int, str], fields: Optional[str] = None) -> Dict[str, Any]:
    """Retrieve a single product by ID."""
    params = {"fields": fields} if fields else None
    return client.request("GET", f"/products/{product_id}.json", params=params)


@mcp.tool()
def count_products(
    status: Optional[str] = None,
    vendor: Optional[str] = None,
    product_type: Optional[str] = None,
    collection_id: Optional[Union[int, str]] = None,
    created_at_min: Optional[str] = None,
    created_at_max: Optional[str] = None,
    updated_at_min: Optional[str] = None,
    updated_at_max: Optional[str] = None,
    published_at_min: Optional[str] = None,
    published_at_max: Optional[str] = None,
) -> Dict[str, Any]:
    """Retrieve a count of products."""
    params: Dict[str, Any] = {}
    for k, v in {
        "status": status,
        "vendor": vendor,
        "product_type": product_type,
        "collection_id": collection_id,
        "created_at_min": created_at_min,
        "created_at_max": created_at_max,
        "updated_at_min": updated_at_min,
        "updated_at_max": updated_at_max,
        "published_at_min": published_at_min,
        "published_at_max": published_at_max,
    }.items():
        if v is not None:
            params[k] = v
    return client.request("GET", "/products/count.json", params=params)


@mcp.tool()
def create_product(product: Dict[str, Any]) -> Dict[str, Any]:
    """Create a new product.

    Args:
        product: Product payload (fields per Shopify Product resource).

    Returns:
        Created product.
    """
    return client.request("POST", "/products.json", body={"product": product})


@mcp.tool()
def update_product(product_id: Union[int, str], product: Dict[str, Any]) -> Dict[str, Any]:
    """Update an existing product."""
    payload = dict(product)
    payload["id"] = int(product_id) if str(product_id).isdigit() else product_id
    return client.request("PUT", f"/products/{product_id}.json", body={"product": payload})


@mcp.tool()
def delete_product(product_id: Union[int, str]) -> Dict[str, Any]:
    """Delete a product."""
    return client.request("DELETE", f"/products/{product_id}.json", unwrap=False)
