from typing import Any, Dict, Optional

from ._client import get_client


def _resource_metafields_path(resource: str, resource_id: int) -> str:
    # resource should be plural endpoint segment, e.g. 'products', 'orders', 'customers', 'draft_orders', 'locations'
    return f"/{resource}/{resource_id}/metafields"


def create_metafield(resource: str, resource_id: int, metafield: Dict[str, Any]) -> Dict[str, Any]:
    """POST /{resource}/{resource_id}/metafields.json

    Doc: docs/api_metafield.md
    """
    return get_client().request("POST", _resource_metafields_path(resource, resource_id) + ".json", json_body={"metafield": metafield})


def list_metafields(
    resource: str,
    resource_id: int,
    *,
    limit: Optional[int] = None,
    since_id: Optional[int] = None,
    namespace: Optional[str] = None,
    key: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /{resource}/{resource_id}/metafields.json

    Doc: docs/api_metafield.md
    """
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if since_id is not None:
        params["since_id"] = since_id
    if namespace is not None:
        params["namespace"] = namespace
    if key is not None:
        params["key"] = key
    return get_client().request("GET", _resource_metafields_path(resource, resource_id) + ".json", params=params)


def get_metafield(resource: str, resource_id: int, metafield_id: int) -> Dict[str, Any]:
    """GET /{resource}/{resource_id}/metafields/{metafield_id}.json

    Doc: docs/api_metafield.md
    """
    return get_client().request("GET", _resource_metafields_path(resource, resource_id) + f"/{metafield_id}.json")


def count_metafields(resource: str, resource_id: int) -> Dict[str, Any]:
    """GET /{resource}/{resource_id}/metafields/count.json

    Doc: docs/api_metafield.md
    """
    return get_client().request("GET", _resource_metafields_path(resource, resource_id) + "/count.json")


def update_metafield(resource: str, resource_id: int, metafield_id: int, metafield: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /{resource}/{resource_id}/metafields/{metafield_id}.json

    Doc: docs/api_metafield.md
    """
    return get_client().request(
        "PUT",
        _resource_metafields_path(resource, resource_id) + f"/{metafield_id}.json",
        json_body={"metafield": {**metafield, "id": metafield_id}},
    )


def delete_metafield(resource: str, resource_id: int, metafield_id: int) -> Dict[str, Any]:
    """DELETE /{resource}/{resource_id}/metafields/{metafield_id}.json

    Doc: docs/api_metafield.md
    """
    return get_client().request("DELETE", _resource_metafields_path(resource, resource_id) + f"/{metafield_id}.json")
