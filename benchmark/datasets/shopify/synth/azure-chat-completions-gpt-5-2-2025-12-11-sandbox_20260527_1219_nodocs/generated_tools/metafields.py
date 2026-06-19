from typing import Any, Dict, Optional

from shopify_client import ShopifyClient, build_pagination_params


def list_metafields(
    *,
    owner_resource: Optional[str] = None,
    owner_id: Optional[int] = None,
    limit: Optional[int] = 50,
    page_info: Optional[str] = None,
    since_id: Optional[int] = None,
    namespace: Optional[str] = None,
    key: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /metafields.json or nested /{resource}/{id}/metafields.json"""
    c = ShopifyClient()
    params = build_pagination_params(limit=limit, page_info=page_info, since_id=since_id)
    if namespace is not None:
        params["namespace"] = namespace
    if key is not None:
        params["key"] = key

    if owner_resource and owner_id:
        return c.request("GET", f"/{owner_resource}/{owner_id}/metafields.json", params=params)
    return c.request("GET", "/metafields.json", params=params)


def get_metafield(*, metafield_id: int) -> Dict[str, Any]:
    """GET /metafields/{metafield_id}.json"""
    c = ShopifyClient()
    return c.request("GET", f"/metafields/{metafield_id}.json")


def create_metafield(*, metafield: Dict[str, Any], owner_resource: Optional[str] = None, owner_id: Optional[int] = None) -> Dict[str, Any]:
    """POST /metafields.json or nested /{resource}/{id}/metafields.json"""
    c = ShopifyClient()
    if owner_resource and owner_id:
        return c.request("POST", f"/{owner_resource}/{owner_id}/metafields.json", json={"metafield": metafield})
    return c.request("POST", "/metafields.json", json={"metafield": metafield})


def update_metafield(*, metafield_id: int, metafield: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /metafields/{metafield_id}.json"""
    c = ShopifyClient()
    body = {"metafield": {**metafield, "id": metafield_id}}
    return c.request("PUT", f"/metafields/{metafield_id}.json", json=body)


def delete_metafield(*, metafield_id: int) -> Dict[str, Any]:
    """DELETE /metafields/{metafield_id}.json"""
    c = ShopifyClient()
    return c.request("DELETE", f"/metafields/{metafield_id}.json")
