from typing import Any, Dict, Optional

from .ebay_client import EbayClient, omit_none


client = EbayClient()


def inventory_get_inventory_item(sku: str) -> Dict[str, Any]:
    return client.request("GET", f"/sell/inventory/v1/inventory_item/{sku}")


def inventory_create_or_replace_inventory_item(sku: str, inventory_item: Dict[str, Any]) -> Dict[str, Any]:
    return client.request("PUT", f"/sell/inventory/v1/inventory_item/{sku}", json_body=inventory_item)


def inventory_delete_inventory_item(sku: str) -> Dict[str, Any]:
    return client.request("DELETE", f"/sell/inventory/v1/inventory_item/{sku}")


def inventory_bulk_create_or_replace_inventory_item(request_body: Dict[str, Any]) -> Dict[str, Any]:
    return client.request("POST", "/sell/inventory/v1/bulk_create_or_replace_inventory_item", json_body=request_body)


def inventory_get_offers(
    sku: Optional[str] = None,
    marketplace_id: Optional[str] = None,
    format: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
) -> Dict[str, Any]:
    params = omit_none({"sku": sku, "marketplace_id": marketplace_id, "format": format, "limit": limit, "offset": offset})
    return client.request("GET", "/sell/inventory/v1/offer", params=params)


def inventory_get_offer(offer_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/sell/inventory/v1/offer/{offer_id}")


def inventory_create_offer(offer: Dict[str, Any]) -> Dict[str, Any]:
    return client.request("POST", "/sell/inventory/v1/offer", json_body=offer)


def inventory_update_offer(offer_id: str, offer: Dict[str, Any]) -> Dict[str, Any]:
    return client.request("PUT", f"/sell/inventory/v1/offer/{offer_id}", json_body=offer)


def inventory_delete_offer(offer_id: str) -> Dict[str, Any]:
    return client.request("DELETE", f"/sell/inventory/v1/offer/{offer_id}")


def inventory_publish_offer(offer_id: str) -> Dict[str, Any]:
    return client.request("POST", f"/sell/inventory/v1/offer/{offer_id}/publish")


def inventory_withdraw_offer(offer_id: str) -> Dict[str, Any]:
    return client.request("POST", f"/sell/inventory/v1/offer/{offer_id}/withdraw")


def inventory_get_locations(limit: Optional[int] = None, offset: Optional[int] = None) -> Dict[str, Any]:
    params = omit_none({"limit": limit, "offset": offset})
    return client.request("GET", "/sell/inventory/v1/location", params=params)


def inventory_get_location(merchant_location_key: str) -> Dict[str, Any]:
    return client.request("GET", f"/sell/inventory/v1/location/{merchant_location_key}")


def inventory_create_or_replace_location(merchant_location_key: str, location: Dict[str, Any]) -> Dict[str, Any]:
    return client.request("PUT", f"/sell/inventory/v1/location/{merchant_location_key}", json_body=location)


def inventory_delete_location(merchant_location_key: str) -> Dict[str, Any]:
    return client.request("DELETE", f"/sell/inventory/v1/location/{merchant_location_key}")
