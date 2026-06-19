from typing import Any, Dict, Optional

from generated_tools.common import shopify_request

RESOURCE_PATHS = {
    "article": "/articles/{owner_id}",
    "blog": "/blogs/{owner_id}",
    "collection": "/collections/{owner_id}",
    "smart_collection": "/smart_collections/{owner_id}",
    "custom_collection": "/custom_collections/{owner_id}",
    "customer": "/customers/{owner_id}",
    "draft_order": "/draft_orders/{owner_id}",
    "location": "/locations/{owner_id}",
    "order": "/orders/{owner_id}",
    "page": "/pages/{owner_id}",
    "product": "/products/{owner_id}",
    "product_image": "/products/{parent_id}/images/{owner_id}",
    "variant": "/variants/{owner_id}",
    "shop": "",
}


def _resource_base(resource_type: str, owner_id: Optional[int] = None, parent_id: Optional[int] = None) -> str:
    template = RESOURCE_PATHS[resource_type]
    return template.format(owner_id=owner_id, parent_id=parent_id)


def create_metafield(resource_type: str, metafield: Dict[str, Any], owner_id: Optional[int] = None, parent_id: Optional[int] = None) -> Any:
    return shopify_request("POST", f"{_resource_base(resource_type, owner_id, parent_id)}/metafields.json", json_body={"metafield": metafield})


def list_metafields(resource_type: str, owner_id: Optional[int] = None, parent_id: Optional[int] = None, limit: Optional[int] = None, since_id: Optional[int] = None) -> Any:
    params = {k: v for k, v in {"limit": limit, "since_id": since_id}.items() if v is not None}
    return shopify_request("GET", f"{_resource_base(resource_type, owner_id, parent_id)}/metafields.json", params=params)


def get_metafield(resource_type: str, metafield_id: int, owner_id: Optional[int] = None, parent_id: Optional[int] = None) -> Any:
    return shopify_request("GET", f"{_resource_base(resource_type, owner_id, parent_id)}/metafields/{metafield_id}.json")


def count_metafields(resource_type: str, owner_id: Optional[int] = None, parent_id: Optional[int] = None) -> Any:
    return shopify_request("GET", f"{_resource_base(resource_type, owner_id, parent_id)}/metafields/count.json")


def update_metafield(resource_type: str, metafield_id: int, metafield: Dict[str, Any], owner_id: Optional[int] = None, parent_id: Optional[int] = None) -> Any:
    payload = dict(metafield)
    payload.setdefault("id", metafield_id)
    return shopify_request("PUT", f"{_resource_base(resource_type, owner_id, parent_id)}/metafields/{metafield_id}.json", json_body={"metafield": payload})


def delete_metafield(resource_type: str, metafield_id: int, owner_id: Optional[int] = None, parent_id: Optional[int] = None) -> Any:
    return shopify_request("DELETE", f"{_resource_base(resource_type, owner_id, parent_id)}/metafields/{metafield_id}.json")
