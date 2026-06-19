from typing import Any, Dict, Optional
from urllib.parse import quote

from generated_tools.common import clean_params, client


def get_inventory_item(seller_sku: str) -> Any:
    return client.request("GET", f"/sell/inventory/v1/inventory_item/{quote(seller_sku, safe='')}")


def create_or_replace_inventory_item(
    seller_sku: str,
    body: Dict[str, Any],
    content_language: str = "en-US",
) -> Any:
    return client.request(
        "PUT",
        f"/sell/inventory/v1/inventory_item/{quote(seller_sku, safe='')}",
        json_body=body,
        headers={"Content-Type": "application/json", "Content-Language": content_language},
    )


def get_inventory_items(limit: Optional[int] = None, offset: Optional[int] = None) -> Any:
    return client.request("GET", "/sell/inventory/v1/inventory_item", params=clean_params(limit=limit, offset=offset))


def create_offer(body: Dict[str, Any], content_language: str = "en-US") -> Any:
    return client.request(
        "POST",
        "/sell/inventory/v1/offer",
        json_body=body,
        headers={"Content-Type": "application/json", "Content-Language": content_language},
    )
