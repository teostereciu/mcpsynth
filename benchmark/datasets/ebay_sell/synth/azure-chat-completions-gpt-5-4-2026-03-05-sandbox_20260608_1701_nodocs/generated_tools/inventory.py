from typing import Any, Dict, Optional

from .common import client


def list_inventory_items(limit: int = 50, offset: int = 0, sku: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"limit": limit, "offset": offset}
    if sku:
        params["sku"] = sku
    return client.request("GET", "/sell/inventory/v1/inventory_item", params=params)


def get_inventory_item(sku: str) -> Dict[str, Any]:
    return client.request("GET", f"/sell/inventory/v1/inventory_item/{sku}")


def create_or_replace_inventory_item(sku: str, data: Dict[str, Any]) -> Dict[str, Any]:
    return client.request("PUT", f"/sell/inventory/v1/inventory_item/{sku}", json_body=data)


def delete_inventory_item(sku: str) -> Dict[str, Any]:
    return client.request("DELETE", f"/sell/inventory/v1/inventory_item/{sku}")


def bulk_create_or_replace_inventory_item(items: Dict[str, Any]) -> Dict[str, Any]:
    return client.request("POST", "/sell/inventory/v1/bulk_create_or_replace_inventory_item", json_body=items)


def bulk_get_inventory_item(skus: list[str]) -> Dict[str, Any]:
    return client.request("POST", "/sell/inventory/v1/bulk_get_inventory_item", json_body={"requests": [{"sku": s} for s in skus]})


def create_offer(data: Dict[str, Any]) -> Dict[str, Any]:
    return client.request("POST", "/sell/inventory/v1/offer", json_body=data)


def get_offer(offer_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/sell/inventory/v1/offer/{offer_id}")


def update_offer(offer_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
    return client.request("PUT", f"/sell/inventory/v1/offer/{offer_id}", json_body=data)


def delete_offer(offer_id: str) -> Dict[str, Any]:
    return client.request("DELETE", f"/sell/inventory/v1/offer/{offer_id}")


def publish_offer(offer_id: str) -> Dict[str, Any]:
    return client.request("POST", f"/sell/inventory/v1/offer/{offer_id}/publish")


def withdraw_offer(offer_id: str) -> Dict[str, Any]:
    return client.request("POST", f"/sell/inventory/v1/offer/{offer_id}/withdraw")


def list_offers(limit: int = 50, offset: int = 0, sku: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"limit": limit, "offset": offset}
    if sku:
        params["sku"] = sku
    return client.request("GET", "/sell/inventory/v1/offer", params=params)


def get_inventory_item_group(inventory_item_group_key: str) -> Dict[str, Any]:
    return client.request("GET", f"/sell/inventory/v1/inventory_item_group/{inventory_item_group_key}")


def create_or_replace_inventory_item_group(inventory_item_group_key: str, data: Dict[str, Any]) -> Dict[str, Any]:
    return client.request("PUT", f"/sell/inventory/v1/inventory_item_group/{inventory_item_group_key}", json_body=data)


def delete_inventory_item_group(inventory_item_group_key: str) -> Dict[str, Any]:
    return client.request("DELETE", f"/sell/inventory/v1/inventory_item_group/{inventory_item_group_key}")


def create_inventory_location(merchant_location_key: str, data: Dict[str, Any]) -> Dict[str, Any]:
    return client.request("POST", f"/sell/inventory/v1/location/{merchant_location_key}", json_body=data)


def get_inventory_location(merchant_location_key: str) -> Dict[str, Any]:
    return client.request("GET", f"/sell/inventory/v1/location/{merchant_location_key}")


def update_inventory_location(merchant_location_key: str, data: Dict[str, Any]) -> Dict[str, Any]:
    return client.request("POST", f"/sell/inventory/v1/location/{merchant_location_key}/update_location_details", json_body=data)


def delete_inventory_location(merchant_location_key: str) -> Dict[str, Any]:
    return client.request("DELETE", f"/sell/inventory/v1/location/{merchant_location_key}")


def list_inventory_locations(limit: int = 50, offset: int = 0) -> Dict[str, Any]:
    return client.request("GET", "/sell/inventory/v1/location", params={"limit": limit, "offset": offset})
