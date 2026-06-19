from typing import Any, Dict, Optional

from .http_client import request_json


def _resource_metafields_path(resource: str, resource_id: int) -> str:
    # Shopify REST uses pluralized resource paths for metafields.
    # Supported examples include: products, orders, customers, collections, smart_collections,
    # custom_collections, blogs, articles, pages, locations, product_images, variants.
    return f"/{resource}/{resource_id}/metafields.json"


def _resource_metafield_path(resource: str, resource_id: int, metafield_id: int) -> str:
    return f"/{resource}/{resource_id}/metafields/{metafield_id}.json"


def _resource_metafields_count_path(resource: str, resource_id: int) -> str:
    return f"/{resource}/{resource_id}/metafields/count.json"


def create_metafield(resource: str, resource_id: int, metafield: Dict[str, Any]) -> Dict[str, Any]:
    """POST /{resource}/{resource_id}/metafields.json

    Doc: docs/api_metafield.md
    Body wrapper: {"metafield": {...}}

    resource: plural resource path segment, e.g. "products", "orders", "customers".
    """
    return request_json("POST", _resource_metafields_path(resource, resource_id), json_body={"metafield": metafield})


def list_metafields(
    resource: str,
    resource_id: int,
    *,
    namespace: Optional[str] = None,
    key: Optional[str] = None,
    limit: Optional[int] = None,
    since_id: Optional[int] = None,
) -> Dict[str, Any]:
    """GET /{resource}/{resource_id}/metafields.json

    Doc: docs/api_metafield.md
    """
    params: Dict[str, Any] = {}
    if namespace is not None:
        params["namespace"] = namespace
    if key is not None:
        params["key"] = key
    if limit is not None:
        params["limit"] = limit
    if since_id is not None:
        params["since_id"] = since_id
    return request_json("GET", _resource_metafields_path(resource, resource_id), params=params)


def get_metafield(resource: str, resource_id: int, metafield_id: int) -> Dict[str, Any]:
    """GET /{resource}/{resource_id}/metafields/{metafield_id}.json

    Doc: docs/api_metafield.md
    """
    return request_json("GET", _resource_metafield_path(resource, resource_id, metafield_id))


def count_metafields(resource: str, resource_id: int) -> Dict[str, Any]:
    """GET /{resource}/{resource_id}/metafields/count.json

    Doc: docs/api_metafield.md
    """
    return request_json("GET", _resource_metafields_count_path(resource, resource_id))


def update_metafield(resource: str, resource_id: int, metafield_id: int, metafield: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /{resource}/{resource_id}/metafields/{metafield_id}.json

    Doc: docs/api_metafield.md
    Body wrapper: {"metafield": {...}}
    """
    return request_json(
        "PUT",
        _resource_metafield_path(resource, resource_id, metafield_id),
        json_body={"metafield": metafield},
    )


def delete_metafield(resource: str, resource_id: int, metafield_id: int) -> Dict[str, Any]:
    """DELETE /{resource}/{resource_id}/metafields/{metafield_id}.json

    Doc: docs/api_metafield.md
    """
    return request_json("DELETE", _resource_metafield_path(resource, resource_id, metafield_id))
