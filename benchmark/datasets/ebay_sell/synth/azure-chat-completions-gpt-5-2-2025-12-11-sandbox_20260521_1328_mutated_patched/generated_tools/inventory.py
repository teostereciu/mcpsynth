from typing import Any, Dict, Optional

from .client import EbayClient


def create_or_replace_inventory_item(
    seller_sku: str,
    inventory_item: Dict[str, Any],
    *,
    content_language: str = "en-US",
    client: Optional[EbayClient] = None,
) -> Dict[str, Any]:
    """PUT /inventory_item/{seller_sku}

    Creates a new inventory item record or replaces an existing one.
    """
    c = client or EbayClient()
    return c.request(
        "PUT",
        f"/sell/inventory/v1/inventory_item/{seller_sku}",
        json=inventory_item,
        content_language=content_language,
    )


def get_inventory_item(
    seller_sku: str,
    *,
    client: Optional[EbayClient] = None,
) -> Dict[str, Any]:
    """GET /inventory_item/{seller_sku}

    Retrieves the inventory item record for a given SKU.
    """
    c = client or EbayClient()
    return c.request("GET", f"/sell/inventory/v1/inventory_item/{seller_sku}")


def get_inventory_items(
    *,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    client: Optional[EbayClient] = None,
) -> Dict[str, Any]:
    """GET /inventory_item

    Retrieves all inventory item records for the seller (paginated).
    """
    c = client or EbayClient()
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = str(limit)
    if offset is not None:
        params["offset"] = str(offset)
    return c.request("GET", "/sell/inventory/v1/inventory_item", params=params or None)


def create_offer(
    offer: Dict[str, Any],
    *,
    content_language: str = "en-US",
    client: Optional[EbayClient] = None,
) -> Dict[str, Any]:
    """POST /offer

    Creates an offer for an inventory item on a marketplace.
    """
    c = client or EbayClient()
    return c.request(
        "POST",
        "/sell/inventory/v1/offer",
        json=offer,
        content_language=content_language,
    )


def publish_offer(
    offer_id: str,
    *,
    client: Optional[EbayClient] = None,
) -> Dict[str, Any]:
    """POST /offer/{offerId}/publish

    Publishes an unpublished offer to create a live listing.
    """
    c = client or EbayClient()
    return c.request("POST", f"/sell/inventory/v1/offer/{offer_id}/publish")
