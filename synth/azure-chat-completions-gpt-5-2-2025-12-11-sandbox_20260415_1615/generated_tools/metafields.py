from typing import Any, Dict, Optional

from .http_client import get_client


def metafield_create(resource_path: str, resource_id: int, metafield: Dict[str, Any]) -> Dict[str, Any]:
    """Create a metafield on a resource.

    Shopify REST uses resource-scoped endpoints, e.g.:
      POST /products/{id}/metafields.json
      POST /orders/{id}/metafields.json

    Args:
        resource_path: plural resource path segment, e.g. "products", "orders", "customers".
        resource_id: owner resource id.
        metafield: metafield payload (wrapped under {"metafield": ...} by this tool).
    """
    return get_client().request(
        "POST",
        f"/{resource_path}/{resource_id}/metafields.json",
        json_body={"metafield": metafield},
    )


def metafields_list(
    resource_path: str,
    resource_id: int,
    *,
    namespace: Optional[str] = None,
    key: Optional[str] = None,
    limit: Optional[int] = None,
) -> Dict[str, Any]:
    """List metafields for a resource: GET /{resource_path}/{id}/metafields.json"""
    params: Dict[str, Any] = {}
    for k, v in {"namespace": namespace, "key": key, "limit": limit}.items():
        if v is not None:
            params[k] = v
    return get_client().request(
        "GET",
        f"/{resource_path}/{resource_id}/metafields.json",
        params=params or None,
    )


def metafield_get(resource_path: str, resource_id: int, metafield_id: int) -> Dict[str, Any]:
    """Get a metafield: GET /{resource_path}/{id}/metafields/{metafield_id}.json"""
    return get_client().request(
        "GET",
        f"/{resource_path}/{resource_id}/metafields/{metafield_id}.json",
    )


def metafields_count(resource_path: str, resource_id: int) -> Dict[str, Any]:
    """Count metafields: GET /{resource_path}/{id}/metafields/count.json"""
    return get_client().request(
        "GET",
        f"/{resource_path}/{resource_id}/metafields/count.json",
    )


def metafield_update(resource_path: str, resource_id: int, metafield_id: int, metafield: Dict[str, Any]) -> Dict[str, Any]:
    """Update a metafield: PUT /{resource_path}/{id}/metafields/{metafield_id}.json"""
    body = {"metafield": {**metafield, "id": metafield_id}}
    return get_client().request(
        "PUT",
        f"/{resource_path}/{resource_id}/metafields/{metafield_id}.json",
        json_body=body,
    )


def metafield_delete(resource_path: str, resource_id: int, metafield_id: int) -> Dict[str, Any]:
    """Delete a metafield: DELETE /{resource_path}/{id}/metafields/{metafield_id}.json"""
    return get_client().request(
        "DELETE",
        f"/{resource_path}/{resource_id}/metafields/{metafield_id}.json",
    )
