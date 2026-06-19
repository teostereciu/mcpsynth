from typing import Any, Dict, Optional

from .client import EbayClient


def create_offer(offer: Dict[str, Any], *, content_language: str = "en-US") -> Dict[str, Any]:
    """POST /offer

    Creates an offer (staged for publishing).

    Doc: docs/api_inventory_create-offer.md
    """

    client = EbayClient()
    return client.request_json(
        "POST",
        "/sell/inventory/v1/offer",
        json=offer,
        content_language=content_language,
        content_type="application/json",
    )


def update_offer(offer_id: str, offer: Dict[str, Any], *, content_language: str = "en-US") -> Dict[str, Any]:
    """PUT /offer/{offerId}

    Replaces an existing offer.

    Doc: docs/api_inventory_update-offer.md
    """

    client = EbayClient()
    return client.request_json(
        "PUT",
        f"/sell/inventory/v1/offer/{offer_id}",
        json=offer,
        content_language=content_language,
        content_type="application/json",
    )


def publish_offer(offer_id: str) -> Dict[str, Any]:
    """POST /offer/{offerId}/publish

    Publishes an offer (creates/revises live listing).

    Doc: docs/api_inventory_publish-offer.md
    """

    client = EbayClient()
    return client.request_json("POST", f"/sell/inventory/v1/offer/{offer_id}/publish")


def withdraw_offer(offer_id: str) -> Dict[str, Any]:
    """POST /offer/{offerId}/withdraw

    Withdraws (ends) the listing associated with an offer.

    Doc: docs/api_inventory_withdraw-offer.md
    """

    client = EbayClient()
    return client.request_json("POST", f"/sell/inventory/v1/offer/{offer_id}/withdraw")


def get_offer(offer_id: str) -> Dict[str, Any]:
    """GET /offer/{offerId}

    Retrieves a specific offer by offerId.

    Doc: docs/api_inventory_get-offer.md
    """

    client = EbayClient()
    return client.request_json("GET", f"/sell/inventory/v1/offer/{offer_id}")


def get_inventory_item(sku: str) -> Dict[str, Any]:
    """GET /inventory_item/{sku}

    Retrieves the inventory item record for a given SKU.

    Doc: docs/api_inventory_get-inventory-item.md
    """

    client = EbayClient()
    return client.request_json("GET", f"/sell/inventory/v1/inventory_item/{sku}")


def get_offers(
    *,
    sku: Optional[str] = None,
    marketplace_id: Optional[str] = None,
    format: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
) -> Dict[str, Any]:
    """GET /offer

    Retrieves offers, typically filtered by sku.

    Doc: docs/api_inventory_get-offers.md
    """

    params: Dict[str, Any] = {}
    if sku is not None:
        params["sku"] = sku
    if marketplace_id is not None:
        params["marketplace_id"] = marketplace_id
    if format is not None:
        params["format"] = format
    if limit is not None:
        params["limit"] = str(limit)
    if offset is not None:
        params["offset"] = str(offset)

    client = EbayClient()
    return client.request_json("GET", "/sell/inventory/v1/offer", params=params or None)


def get_inventory_items(*, limit: Optional[int] = None, offset: Optional[int] = None) -> Dict[str, Any]:
    """GET /inventory_item

    Retrieves all inventory item records for the seller account (paged).

    Doc: docs/api_inventory_get-inventory-items.md
    """

    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = str(limit)
    if offset is not None:
        params["offset"] = str(offset)

    client = EbayClient()
    return client.request_json("GET", "/sell/inventory/v1/inventory_item", params=params or None)


def delete_inventory_item(sku: str) -> Dict[str, Any]:
    """DELETE /inventory_item/{sku}

    Deletes an inventory item record for a given SKU.

    Doc: docs/api_inventory_delete-inventory-item.md
    """

    client = EbayClient()
    return client.request_json("DELETE", f"/sell/inventory/v1/inventory_item/{sku}")


def create_or_replace_inventory_item(
    sku: str,
    inventory_item: Dict[str, Any],
    *,
    content_language: str = "en-US",
) -> Dict[str, Any]:
    """PUT /inventory_item/{sku}

    Creates a new inventory item record or replaces an existing one.

    Doc: docs/api_inventory_create-or-replace-inventory-item.md
    """

    client = EbayClient()
    return client.request_json(
        "PUT",
        f"/sell/inventory/v1/inventory_item/{sku}",
        json=inventory_item,
        content_language=content_language,
        content_type="application/json",
    )
