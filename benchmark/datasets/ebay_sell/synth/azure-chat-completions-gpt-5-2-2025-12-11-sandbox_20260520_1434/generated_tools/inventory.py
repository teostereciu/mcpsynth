from typing import Any, Dict

from .client import EbaySellClient


def create_or_replace_inventory_item(
    sku: str,
    inventory_item: Dict[str, Any],
    *,
    content_language: str = "en-US",
) -> Dict[str, Any]:
    """PUT /inventory_item/{sku}

    Creates a new inventory item record or replaces an existing one.
    """
    client = EbaySellClient()
    return client.request(
        "PUT",
        f"/sell/inventory/v1/inventory_item/{sku}",
        json=inventory_item,
        headers={
            "Content-Language": content_language,
            "Content-Type": "application/json",
        },
    )


def get_inventory_item(sku: str) -> Dict[str, Any]:
    """GET /inventory_item/{sku}

    Retrieves the inventory item record for a given SKU.
    """
    client = EbaySellClient()
    return client.request("GET", f"/sell/inventory/v1/inventory_item/{sku}")


def get_inventory_items(*, limit: int = 25, offset: int = 0) -> Dict[str, Any]:
    """GET /inventory_item

    Retrieves all inventory item records for the seller account (paged).
    """
    client = EbaySellClient()
    return client.request(
        "GET",
        "/sell/inventory/v1/inventory_item",
        params={"limit": str(limit), "offset": str(offset)},
    )
