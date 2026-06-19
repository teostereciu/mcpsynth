from typing import Any, Optional

from generated_tools.ebay_common import client


def get_inventory_item(sku: str) -> Any:
    return client.request("GET", f"/inventory_item/{sku}", api_group="inventory")


def create_or_replace_inventory_item(sku: str, body: dict, content_language: str = "en-US") -> Any:
    return client.request(
        "PUT",
        f"/inventory_item/{sku}",
        api_group="inventory",
        json_body=body,
        headers={
            "Content-Type": "application/json",
            "Content-Language": content_language,
        },
    )


def get_offers(sku: str, format: Optional[str] = None, limit: Optional[str] = None, marketplace_id: Optional[str] = None, offset: Optional[str] = None) -> Any:
    return client.request(
        "GET",
        "/offer",
        api_group="inventory",
        params={
            "sku": sku,
            "format": format,
            "limit": limit,
            "marketplace_id": marketplace_id,
            "offset": offset,
        },
    )


def create_offer(body: dict, content_language: str = "en-US") -> Any:
    return client.request(
        "POST",
        "/offer",
        api_group="inventory",
        json_body=body,
        headers={
            "Content-Type": "application/json",
            "Content-Language": content_language,
        },
    )
