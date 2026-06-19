from typing import Any, Dict, Optional

from shopify_api import shopify_request


def create_resource_metafield(resource_path: str, resource_id: int, metafield: Dict[str, Any]) -> Any:
    return shopify_request("POST", f"/{resource_path}/{resource_id}/metafields.json", json_body={"metafield": metafield})


def list_resource_metafields(resource_path: str, resource_id: int, limit: Optional[int] = None) -> Any:
    return shopify_request("GET", f"/{resource_path}/{resource_id}/metafields.json", params={"limit": limit})


def get_resource_metafield(resource_path: str, resource_id: int, metafield_id: int) -> Any:
    return shopify_request("GET", f"/{resource_path}/{resource_id}/metafields/{metafield_id}.json")


def count_resource_metafields(resource_path: str, resource_id: int) -> Any:
    return shopify_request("GET", f"/{resource_path}/{resource_id}/metafields/count.json")


def update_resource_metafield(resource_path: str, resource_id: int, metafield_id: int, metafield: Dict[str, Any]) -> Any:
    payload = dict(metafield)
    payload["id"] = metafield_id
    return shopify_request("PUT", f"/{resource_path}/{resource_id}/metafields/{metafield_id}.json", json_body={"metafield": payload})


def delete_resource_metafield(resource_path: str, resource_id: int, metafield_id: int) -> Any:
    return shopify_request("DELETE", f"/{resource_path}/{resource_id}/metafields/{metafield_id}.json")


def create_webhook(webhook: Dict[str, Any]) -> Any:
    return shopify_request("POST", "/webhooks.json", json_body={"webhook": webhook})


def list_webhooks(topic: Optional[str] = None, address: Optional[str] = None, limit: Optional[int] = None) -> Any:
    return shopify_request("GET", "/webhooks.json", params={"topic": topic, "address": address, "limit": limit})


def get_webhook(webhook_id: int) -> Any:
    return shopify_request("GET", f"/webhooks/{webhook_id}.json")


def count_webhooks(topic: Optional[str] = None) -> Any:
    return shopify_request("GET", "/webhooks/count.json", params={"topic": topic})


def update_webhook(webhook_id: int, webhook: Dict[str, Any]) -> Any:
    payload = dict(webhook)
    payload["id"] = webhook_id
    return shopify_request("PUT", f"/webhooks/{webhook_id}.json", json_body={"webhook": payload})


def delete_webhook(webhook_id: int) -> Any:
    return shopify_request("DELETE", f"/webhooks/{webhook_id}.json")
