from typing import Any, Optional

from generated_tools.common import client, compact_kwargs, parse_json_body


API_BASE = "/sell/inventory/v1"


def get_inventory_item(seller_sku: str) -> Any:
    try:
        return client.request(API_BASE, "GET", f"/inventory_item/{seller_sku}")
    except Exception as e:
        return {"error": str(e)}


def get_inventory_items(limit: Optional[int] = None, offset: Optional[int] = None) -> Any:
    try:
        return client.request(API_BASE, "GET", "/inventory_item", params=compact_kwargs(limit=limit, offset=offset))
    except Exception as e:
        return {"error": str(e)}


def create_or_replace_inventory_item(seller_sku: str, body: str) -> Any:
    try:
        return client.request(API_BASE, "PUT", f"/inventory_item/{seller_sku}", json_body=parse_json_body(body))
    except Exception as e:
        return {"error": str(e)}


def delete_inventory_item(seller_sku: str) -> Any:
    try:
        return client.request(API_BASE, "DELETE", f"/inventory_item/{seller_sku}")
    except Exception as e:
        return {"error": str(e)}


def bulk_get_inventory_item(body: str) -> Any:
    try:
        return client.request(API_BASE, "POST", "/bulk_get_inventory_item", json_body=parse_json_body(body))
    except Exception as e:
        return {"error": str(e)}


def bulk_create_or_replace_inventory_item(body: str) -> Any:
    try:
        return client.request(API_BASE, "POST", "/bulk_create_or_replace_inventory_item", json_body=parse_json_body(body))
    except Exception as e:
        return {"error": str(e)}


def create_offer(body: str, content_language: str) -> Any:
    try:
        return client.request(API_BASE, "POST", "/offer", json_body=parse_json_body(body), headers={"Content-Language": content_language})
    except Exception as e:
        return {"error": str(e)}


def get_offer(offer_id: str) -> Any:
    try:
        return client.request(API_BASE, "GET", f"/offer/{offer_id}")
    except Exception as e:
        return {"error": str(e)}


def get_offers(sku: Optional[str] = None, marketplace_id: Optional[str] = None, format: Optional[str] = None, limit: Optional[int] = None, offset: Optional[int] = None) -> Any:
    try:
        return client.request(API_BASE, "GET", "/offer", params=compact_kwargs(sku=sku, marketplace_id=marketplace_id, format=format, limit=limit, offset=offset))
    except Exception as e:
        return {"error": str(e)}


def update_offer(offer_id: str, body: str, content_language: Optional[str] = None) -> Any:
    try:
        headers = {"Content-Language": content_language} if content_language else None
        return client.request(API_BASE, "PUT", f"/offer/{offer_id}", json_body=parse_json_body(body), headers=headers)
    except Exception as e:
        return {"error": str(e)}


def delete_offer(offer_id: str) -> Any:
    try:
        return client.request(API_BASE, "DELETE", f"/offer/{offer_id}")
    except Exception as e:
        return {"error": str(e)}


def publish_offer(offer_id: str) -> Any:
    try:
        return client.request(API_BASE, "POST", f"/offer/{offer_id}/publish")
    except Exception as e:
        return {"error": str(e)}


def withdraw_offer(offer_id: str, body: Optional[str] = None) -> Any:
    try:
        return client.request(API_BASE, "POST", f"/offer/{offer_id}/withdraw", json_body=parse_json_body(body) if body else None)
    except Exception as e:
        return {"error": str(e)}


def bulk_create_offer(body: str, content_language: str) -> Any:
    try:
        return client.request(API_BASE, "POST", "/bulk_create_offer", json_body=parse_json_body(body), headers={"Content-Language": content_language})
    except Exception as e:
        return {"error": str(e)}


def bulk_publish_offer(body: str) -> Any:
    try:
        return client.request(API_BASE, "POST", "/bulk_publish_offer", json_body=parse_json_body(body))
    except Exception as e:
        return {"error": str(e)}


def bulk_update_price_quantity(body: str) -> Any:
    try:
        return client.request(API_BASE, "POST", "/bulk_update_price_quantity", json_body=parse_json_body(body))
    except Exception as e:
        return {"error": str(e)}


def get_listing_fees(body: str) -> Any:
    try:
        return client.request(API_BASE, "POST", "/offer/get_listing_fees", json_body=parse_json_body(body))
    except Exception as e:
        return {"error": str(e)}


def create_inventory_location(merchant_location_key: str, body: str) -> Any:
    try:
        return client.request(API_BASE, "POST", f"/location/{merchant_location_key}", json_body=parse_json_body(body))
    except Exception as e:
        return {"error": str(e)}


def get_inventory_location(merchant_location_key: str) -> Any:
    try:
        return client.request(API_BASE, "GET", f"/location/{merchant_location_key}")
    except Exception as e:
        return {"error": str(e)}


def get_inventory_locations(limit: Optional[int] = None, offset: Optional[int] = None) -> Any:
    try:
        return client.request(API_BASE, "GET", "/location", params=compact_kwargs(limit=limit, offset=offset))
    except Exception as e:
        return {"error": str(e)}


def update_inventory_location(merchant_location_key: str, body: str) -> Any:
    try:
        return client.request(API_BASE, "POST", f"/location/{merchant_location_key}/update_location_details", json_body=parse_json_body(body))
    except Exception as e:
        return {"error": str(e)}


def enable_inventory_location(merchant_location_key: str) -> Any:
    try:
        return client.request(API_BASE, "POST", f"/location/{merchant_location_key}/enable")
    except Exception as e:
        return {"error": str(e)}


def disable_inventory_location(merchant_location_key: str) -> Any:
    try:
        return client.request(API_BASE, "POST", f"/location/{merchant_location_key}/disable")
    except Exception as e:
        return {"error": str(e)}


def delete_inventory_location(merchant_location_key: str) -> Any:
    try:
        return client.request(API_BASE, "DELETE", f"/location/{merchant_location_key}")
    except Exception as e:
        return {"error": str(e)}


def create_or_replace_inventory_item_group(inventory_item_group_key: str, body: str) -> Any:
    try:
        return client.request(API_BASE, "PUT", f"/inventory_item_group/{inventory_item_group_key}", json_body=parse_json_body(body))
    except Exception as e:
        return {"error": str(e)}


def get_inventory_item_group(inventory_item_group_key: str) -> Any:
    try:
        return client.request(API_BASE, "GET", f"/inventory_item_group/{inventory_item_group_key}")
    except Exception as e:
        return {"error": str(e)}


def delete_inventory_item_group(inventory_item_group_key: str) -> Any:
    try:
        return client.request(API_BASE, "DELETE", f"/inventory_item_group/{inventory_item_group_key}")
    except Exception as e:
        return {"error": str(e)}


def publish_offer_by_inventory_item_group(body: str) -> Any:
    try:
        return client.request(API_BASE, "POST", "/offer/publish_by_inventory_item_group", json_body=parse_json_body(body))
    except Exception as e:
        return {"error": str(e)}


def withdraw_offer_by_inventory_item_group(body: str) -> Any:
    try:
        return client.request(API_BASE, "POST", "/offer/withdraw_by_inventory_item_group", json_body=parse_json_body(body))
    except Exception as e:
        return {"error": str(e)}
