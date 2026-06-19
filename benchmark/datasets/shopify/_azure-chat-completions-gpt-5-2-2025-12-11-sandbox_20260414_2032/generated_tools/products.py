from __future__ import annotations

from typing import Any, Dict, List, Optional, Union

from . import mcp
from .http import shopify_request, unwrap_envelope


@mcp.tool()
def list_products(
    limit: int = 50,
    status: Optional[str] = None,
    vendor: Optional[str] = None,
    product_type: Optional[str] = None,
    ids: Optional[str] = None,
    fields: Optional[str] = None,
    since_id: Optional[Union[int, str]] = None,
) -> Union[List[Dict[str, Any]], Dict[str, Any]]:
    """List products.

    Args:
        limit: Max number of products.
        status: active|archived|draft.
        vendor: Filter by vendor.
        product_type: Filter by product_type.
        ids: Comma-separated product IDs.
        fields: Comma-separated fields.
        since_id: Return products after this ID.

    Returns:
        List of products or error dict.
    """

    params: Dict[str, Any] = {"limit": limit}
    if status:
        params["status"] = status
    if vendor:
        params["vendor"] = vendor
    if product_type:
        params["product_type"] = product_type
    if ids:
        params["ids"] = ids
    if fields:
        params["fields"] = fields
    if since_id is not None:
        params["since_id"] = since_id

    data = shopify_request("GET", "/products.json", params=params)
    if "error" in data:
        return data
    return unwrap_envelope(data)


@mcp.tool()
def get_product(product_id: Union[int, str], fields: Optional[str] = None) -> Union[Dict[str, Any], Dict[str, Any]]:
    """Get a single product by ID."""

    params = {"fields": fields} if fields else None
    data = shopify_request("GET", f"/products/{product_id}.json", params=params)
    if "error" in data:
        return {"error": f"Product {product_id} not found or could not be retrieved", **data}
    return unwrap_envelope(data)


@mcp.tool()
def create_product(product: Dict[str, Any]) -> Union[Dict[str, Any], Dict[str, Any]]:
    """Create a product.

    Args:
        product: Product payload (fields per Shopify Product resource).

    Returns:
        Created product dict or error dict.
    """

    data = shopify_request("POST", "/products.json", body={"product": product})
    if "error" in data:
        return data
    return unwrap_envelope(data)


@mcp.tool()
def update_product(product_id: Union[int, str], product: Dict[str, Any]) -> Union[Dict[str, Any], Dict[str, Any]]:
    """Update a product by ID."""

    payload = dict(product)
    payload["id"] = int(product_id) if str(product_id).isdigit() else product_id
    data = shopify_request("PUT", f"/products/{product_id}.json", body={"product": payload})
    if "error" in data:
        return data
    return unwrap_envelope(data)


@mcp.tool()
def delete_product(product_id: Union[int, str]) -> Dict[str, Any]:
    """Delete a product by ID."""

    data = shopify_request("DELETE", f"/products/{product_id}.json")
    if "error" in data:
        return data
    return {"ok": True}


@mcp.tool()
def count_products(
    status: Optional[str] = None,
    vendor: Optional[str] = None,
    product_type: Optional[str] = None,
) -> Union[int, Dict[str, Any]]:
    """Count products."""

    params: Dict[str, Any] = {}
    if status:
        params["status"] = status
    if vendor:
        params["vendor"] = vendor
    if product_type:
        params["product_type"] = product_type

    data = shopify_request("GET", "/products/count.json", params=params or None)
    if "error" in data:
        return data
    unwrapped = unwrap_envelope(data)
    if isinstance(unwrapped, dict) and "count" in unwrapped:
        return int(unwrapped["count"])
    return unwrapped
