from typing import Any, Dict, Optional

from ._client import get_client


# Metafields are exposed on many resource-specific endpoints. This module provides
# helpers for the most common ones used in workflows.


def create_product_metafield(product_id: int, metafield: Dict[str, Any]) -> Dict[str, Any]:
    """POST /products/{product_id}/metafields.json

    Doc: docs/api_metafield.md
    Body wrapper: {"metafield": {...}}
    """
    client = get_client()
    return client.request(
        "POST", f"/products/{product_id}/metafields.json", json={"metafield": metafield}
    )


def list_product_metafields(
    product_id: int,
    *,
    limit: Optional[int] = None,
    since_id: Optional[int] = None,
) -> Dict[str, Any]:
    """GET /products/{product_id}/metafields.json

    Doc: docs/api_metafield.md
    """
    client = get_client()
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if since_id is not None:
        params["since_id"] = since_id
    return client.request("GET", f"/products/{product_id}/metafields.json", params=params or None)


def get_product_metafield(product_id: int, metafield_id: int) -> Dict[str, Any]:
    """GET /products/{product_id}/metafields/{metafield_id}.json

    Doc: docs/api_metafield.md
    """
    client = get_client()
    return client.request("GET", f"/products/{product_id}/metafields/{metafield_id}.json")


def count_product_metafields(product_id: int) -> Dict[str, Any]:
    """GET /products/{product_id}/metafields/count.json

    Doc: docs/api_metafield.md
    """
    client = get_client()
    return client.request("GET", f"/products/{product_id}/metafields/count.json")


def update_product_metafield(product_id: int, metafield_id: int, metafield: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /products/{product_id}/metafields/{metafield_id}.json

    Doc: docs/api_metafield.md
    Body wrapper: {"metafield": {..., "id": metafield_id}}
    """
    client = get_client()
    body = dict(metafield)
    body.setdefault("id", metafield_id)
    return client.request(
        "PUT",
        f"/products/{product_id}/metafields/{metafield_id}.json",
        json={"metafield": body},
    )


def delete_product_metafield(product_id: int, metafield_id: int) -> Dict[str, Any]:
    """DELETE /products/{product_id}/metafields/{metafield_id}.json

    Doc: docs/api_metafield.md
    """
    client = get_client()
    return client.request("DELETE", f"/products/{product_id}/metafields/{metafield_id}.json")


def create_order_metafield(order_id: int, metafield: Dict[str, Any]) -> Dict[str, Any]:
    """POST /orders/{order_id}/metafields.json

    Doc: docs/api_metafield.md
    """
    client = get_client()
    return client.request(
        "POST", f"/orders/{order_id}/metafields.json", json={"metafield": metafield}
    )


def list_order_metafields(order_id: int, *, limit: Optional[int] = None, since_id: Optional[int] = None) -> Dict[str, Any]:
    """GET /orders/{order_id}/metafields.json

    Doc: docs/api_metafield.md
    """
    client = get_client()
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if since_id is not None:
        params["since_id"] = since_id
    return client.request("GET", f"/orders/{order_id}/metafields.json", params=params or None)
