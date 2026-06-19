from typing import Any, Dict, Optional

from .client import shopify_request


def list_metafields(*, owner_resource: str, owner_id: int, limit: int = 50) -> Dict[str, Any]:
    # owner_resource examples: products, orders, customers, collections
    return shopify_request("GET", f"/{owner_resource}/{owner_id}/metafields.json", params={"limit": limit})


def get_metafield(*, metafield_id: int) -> Dict[str, Any]:
    return shopify_request("GET", f"/metafields/{metafield_id}.json")


def create_metafield(*, owner_resource: str, owner_id: int, metafield: Dict[str, Any]) -> Dict[str, Any]:
    return shopify_request(
        "POST",
        f"/{owner_resource}/{owner_id}/metafields.json",
        json_body={"metafield": metafield},
    )


def update_metafield(*, metafield_id: int, metafield: Dict[str, Any]) -> Dict[str, Any]:
    body = {"metafield": {**metafield, "id": metafield_id}}
    return shopify_request("PUT", f"/metafields/{metafield_id}.json", json_body=body)


def delete_metafield(*, metafield_id: int) -> Dict[str, Any]:
    return shopify_request("DELETE", f"/metafields/{metafield_id}.json")
