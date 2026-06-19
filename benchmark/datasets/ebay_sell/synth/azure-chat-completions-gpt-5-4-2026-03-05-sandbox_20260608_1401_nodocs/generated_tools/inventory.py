from typing import Any, Dict, Optional

from generated_tools.common import client


def get_inventory_item(sku: str) -> Dict[str, Any]:
    return client.request("GET", f"/sell/inventory/v1/inventory_item/{sku}")


def create_or_replace_inventory_item(
    sku: str,
    availability: Optional[Dict[str, Any]] = None,
    condition: Optional[str] = None,
    product: Optional[Dict[str, Any]] = None,
    package_weight_and_size: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    body: Dict[str, Any] = {}
    if availability is not None:
        body["availability"] = availability
    if condition is not None:
        body["condition"] = condition
    if product is not None:
        body["product"] = product
    if package_weight_and_size is not None:
        body["packageWeightAndSize"] = package_weight_and_size
    return client.request("PUT", f"/sell/inventory/v1/inventory_item/{sku}", json_body=body)


def delete_inventory_item(sku: str) -> Dict[str, Any]:
    return client.request("DELETE", f"/sell/inventory/v1/inventory_item/{sku}")


def bulk_get_inventory_item(skus: list[str]) -> Dict[str, Any]:
    return client.request("GET", "/sell/inventory/v1/bulk_get_inventory_item", params={"sku": ",".join(skus)})


def get_inventory_items(limit: int = 50, offset: int = 0) -> Dict[str, Any]:
    return client.request("GET", "/sell/inventory/v1/inventory_item", params={"limit": limit, "offset": offset})


def create_offer(
    sku: str,
    marketplace_id: str,
    format: str,
    available_quantity: int,
    category_id: str,
    listing_description: str,
    pricing_summary: Dict[str, Any],
    merchant_location_key: str,
    listing_policies: Dict[str, Any],
) -> Dict[str, Any]:
    return client.request(
        "POST",
        "/sell/inventory/v1/offer",
        json_body={
            "sku": sku,
            "marketplaceId": marketplace_id,
            "format": format,
            "availableQuantity": available_quantity,
            "categoryId": category_id,
            "listingDescription": listing_description,
            "pricingSummary": pricing_summary,
            "merchantLocationKey": merchant_location_key,
            "listingPolicies": listing_policies,
        },
    )


def get_offer(offer_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/sell/inventory/v1/offer/{offer_id}")


def update_offer(offer_id: str, offer_payload: Dict[str, Any]) -> Dict[str, Any]:
    return client.request("PUT", f"/sell/inventory/v1/offer/{offer_id}", json_body=offer_payload)


def delete_offer(offer_id: str) -> Dict[str, Any]:
    return client.request("DELETE", f"/sell/inventory/v1/offer/{offer_id}")


def publish_offer(offer_id: str) -> Dict[str, Any]:
    return client.request("POST", f"/sell/inventory/v1/offer/{offer_id}/publish")


def withdraw_offer(offer_id: str) -> Dict[str, Any]:
    return client.request("POST", f"/sell/inventory/v1/offer/{offer_id}/withdraw")


def get_offers(sku: Optional[str] = None, marketplace_id: Optional[str] = None, limit: int = 50, offset: int = 0) -> Dict[str, Any]:
    params: Dict[str, Any] = {"limit": limit, "offset": offset}
    if sku is not None:
        params["sku"] = sku
    if marketplace_id is not None:
        params["marketplace_id"] = marketplace_id
    return client.request("GET", "/sell/inventory/v1/offer", params=params)


def create_inventory_location(merchant_location_key: str, location_payload: Dict[str, Any]) -> Dict[str, Any]:
    return client.request("POST", f"/sell/inventory/v1/location/{merchant_location_key}", json_body=location_payload)


def get_inventory_location(merchant_location_key: str) -> Dict[str, Any]:
    return client.request("GET", f"/sell/inventory/v1/location/{merchant_location_key}")


def update_inventory_location(merchant_location_key: str, location_payload: Dict[str, Any]) -> Dict[str, Any]:
    return client.request("POST", f"/sell/inventory/v1/location/{merchant_location_key}/update_location_details", json_body=location_payload)


def delete_inventory_location(merchant_location_key: str) -> Dict[str, Any]:
    return client.request("DELETE", f"/sell/inventory/v1/location/{merchant_location_key}")


def get_inventory_locations(limit: int = 50, offset: int = 0) -> Dict[str, Any]:
    return client.request("GET", "/sell/inventory/v1/location", params={"limit": limit, "offset": offset})
