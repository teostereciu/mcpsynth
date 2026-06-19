from typing import Any, Dict

from .client import EbayClient


def create_or_replace_inventory_item(
    seller_sku: str,
    inventory_item: Dict[str, Any],
    *,
    content_language: str = "en-US",
) -> Dict[str, Any]:
    """PUT /inventory_item/{seller_sku}

    Creates a new inventory item record or replaces an existing one.
    """

    client = EbayClient()
    return client.request(
        "PUT",
        f"/sell/inventory/v1/inventory_item/{seller_sku}",
        json=inventory_item,
        content_language=content_language,
    )


def get_inventory_item(seller_sku: str) -> Dict[str, Any]:
    """GET /inventory_item/{seller_sku}

    Retrieves the inventory item record for a given SKU.
    """

    client = EbayClient()
    return client.request("GET", f"/sell/inventory/v1/inventory_item/{seller_sku}")
