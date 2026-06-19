from typing import Any, Optional

from .common import client

API_PATH = "/sell/inventory/v1"


def get_inventory_item(sku: str) -> Any:
    return client.request(API_PATH, "GET", f"/inventory_item/{sku}")


def create_or_replace_inventory_item(
    sku: str,
    body: dict,
    content_language: str = "en-US",
) -> Any:
    return client.request(
        API_PATH,
        "PUT",
        f"/inventory_item/{sku}",
        json_body=body,
        headers={
            "Content-Type": "application/json",
            "Content-Language": content_language,
        },
    )


def get_inventory_items(limit: Optional[int] = None, offset: Optional[int] = None) -> Any:
    return client.request(API_PATH, "GET", "/inventory_item", params={"limit": limit, "offset": offset})


def create_offer(body: dict, content_language: str = "en-US") -> Any:
    return client.request(
        API_PATH,
        "POST",
        "/offer",
        json_body=body,
        headers={
            "Content-Type": "application/json",
            "Content-Language": content_language,
        },
    )


def get_offer(offer_id: str) -> Any:
    return client.request(API_PATH, "GET", f"/offer/{offer_id}")


def publish_offer(offer_id: str) -> Any:
    return client.request(API_PATH, "POST", f"/offer/{offer_id}/publish")
