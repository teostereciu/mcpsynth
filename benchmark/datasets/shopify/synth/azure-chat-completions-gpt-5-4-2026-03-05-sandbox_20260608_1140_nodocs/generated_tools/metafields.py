from typing import Any, Dict, Optional

from generated_tools.common import clean_params, shopify_request


def list_metafields(owner_resource: str, owner_id: int, limit: Optional[int] = None, namespace: Optional[str] = None) -> Any:
    params = clean_params(limit=limit, namespace=namespace)
    return shopify_request("GET", f"/{owner_resource}/{owner_id}/metafields.json", params=params)


def get_metafield(metafield_id: int) -> Any:
    return shopify_request("GET", f"/metafields/{metafield_id}.json")


def create_metafield(owner_resource: str, owner_id: int, metafield: Dict[str, Any]) -> Any:
    return shopify_request("POST", f"/{owner_resource}/{owner_id}/metafields.json", json_body={"metafield": metafield})


def update_metafield(metafield_id: int, metafield: Dict[str, Any]) -> Any:
    body = {"metafield": {"id": metafield_id, **metafield}}
    return shopify_request("PUT", f"/metafields/{metafield_id}.json", json_body=body)


def delete_metafield(metafield_id: int) -> Any:
    return shopify_request("DELETE", f"/metafields/{metafield_id}.json")
