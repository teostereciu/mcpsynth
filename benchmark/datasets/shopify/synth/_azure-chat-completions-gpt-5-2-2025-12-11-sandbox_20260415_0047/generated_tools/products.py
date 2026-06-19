from typing import Any, Dict, List, Optional, Union

from . import mcp
from .http import ShopifyClient, unwrap_envelope


@mcp.tool()
def list_products(
    limit: int = 50,
    status: Optional[str] = None,
    vendor: Optional[str] = None,
    product_type: Optional[str] = None,
    title: Optional[str] = None,
    ids: Optional[str] = None,
    fields: Optional[str] = None,
    since_id: Optional[Union[int, str]] = None,
) -> List[Dict[str, Any]]:
    """List products.

    Mirrors GET /products.json.
    """
    client = ShopifyClient()
    params: Dict[str, Any] = {"limit": limit}
    if status:
        params["status"] = status
    if vendor:
        params["vendor"] = vendor
    if product_type:
        params["product_type"] = product_type
    if title:
        params["title"] = title
    if ids:
        params["ids"] = ids
    if fields:
        params["fields"] = fields
    if since_id is not None:
        params["since_id"] = since_id
    data = client.request("GET", "/products.json", params=params)
    return unwrap_envelope(data)


@mcp.tool()
def get_product(product_id: Union[int, str], fields: Optional[str] = None) -> Dict[str, Any]:
    """Get a single product by id."""
    client = ShopifyClient()
    params = {"fields": fields} if fields else None
    data = client.request("GET", f"/products/{product_id}.json", params=params)
    return unwrap_envelope(data)


@mcp.tool()
def create_product(product: Dict[str, Any]) -> Dict[str, Any]:
    """Create a product.

    Args:
        product: Product payload (will be wrapped in {"product": ...}).
    """
    client = ShopifyClient()
    data = client.request("POST", "/products.json", body={"product": product})
    return unwrap_envelope(data)


@mcp.tool()
def update_product(product_id: Union[int, str], product: Dict[str, Any]) -> Dict[str, Any]:
    """Update a product."""
    client = ShopifyClient()
    payload = dict(product)
    payload["id"] = int(product_id) if str(product_id).isdigit() else product_id
    data = client.request("PUT", f"/products/{product_id}.json", body={"product": payload})
    return unwrap_envelope(data)


@mcp.tool()
def delete_product(product_id: Union[int, str]) -> Dict[str, Any]:
    """Delete a product."""
    client = ShopifyClient()
    return client.request("DELETE", f"/products/{product_id}.json")
