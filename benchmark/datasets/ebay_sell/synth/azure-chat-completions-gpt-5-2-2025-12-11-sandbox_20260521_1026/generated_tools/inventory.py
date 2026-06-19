from __future__ import annotations

from typing import Any, Dict, Optional

from .client import EbayClient


def create_offer(
    offer: Dict[str, Any],
    *,
    content_language: str = "en-US",
    client: Optional[EbayClient] = None,
) -> Any:
    """POST /offer

    Doc: docs/api_inventory_create-offer.md
    """
    c = client or EbayClient()
    status, body, headers = c.request(
        "POST",
        "/offer",
        json=offer,
        headers={"Content-Language": content_language},
        content_type="application/json",
    )
    return c.ok_or_error(status, body, headers)



def get_offer(
    offer_id: str,
    *,
    client: Optional[EbayClient] = None,
) -> Any:
    """GET /offer/{offerId}

    Doc: docs/api_inventory_get-offer.md
    """
    c = client or EbayClient()
    status, body, headers = c.request("GET", f"/offer/{offer_id}")
    return c.ok_or_error(status, body, headers)


def get_inventory_item(
    sku: str,
    *,
    client: Optional[EbayClient] = None,
) -> Any:
    """GET /inventory_item/{sku}

    Doc: docs/api_inventory_get-inventory-item.md
    """
    c = client or EbayClient()
    status, body, headers = c.request("GET", f"/inventory_item/{sku}")
    return c.ok_or_error(status, body, headers)


def update_offer(
    offer_id: str,
    offer: Dict[str, Any],
    *,
    content_language: str = "en-US",
    client: Optional[EbayClient] = None,
) -> Any:
    """PUT /offer/{offerId}

    Doc: docs/api_inventory_update-offer.md
    """
    c = client or EbayClient()
    status, body, headers = c.request(
        "PUT",
        f"/offer/{offer_id}",
        json=offer,
        headers={"Content-Language": content_language},
        content_type="application/json",
    )
    return c.ok_or_error(status, body, headers)


def get_inventory_items(
    *,
    limit: int = 25,
    offset: int = 0,
    client: Optional[EbayClient] = None,
) -> Any:
    """GET /inventory_item

    Doc: docs/api_inventory_get-inventory-items.md
    """
    c = client or EbayClient()
    params = {"limit": str(limit), "offset": str(offset)}
    status, body, headers = c.request("GET", "/inventory_item", params=params)
    return c.ok_or_error(status, body, headers)


def publish_offer(
    offer_id: str,
    *,
    client: Optional[EbayClient] = None,
) -> Any:
    """POST /offer/{offerId}/publish

    Doc: docs/api_inventory_publish-offer.md
    """
    c = client or EbayClient()
    status, body, headers = c.request("POST", f"/offer/{offer_id}/publish")
    return c.ok_or_error(status, body, headers)


def delete_inventory_item(
    sku: str,
    *,
    client: Optional[EbayClient] = None,
) -> Any:
    """DELETE /inventory_item/{sku}

    Doc: docs/api_inventory_delete-inventory-item.md
    """
    c = client or EbayClient()
    status, body, headers = c.request("DELETE", f"/inventory_item/{sku}")
    return c.ok_or_error(status, body, headers)


def create_or_replace_inventory_item(
    sku: str,
    inventory_item: Dict[str, Any],
    *,
    content_language: str = "en-US",
    client: Optional[EbayClient] = None,
) -> Any:
    """PUT /inventory_item/{sku}

    Doc: docs/api_inventory_create-or-replace-inventory-item.md
    """
    c = client or EbayClient()
    status, body, headers = c.request(
        "PUT",
        f"/inventory_item/{sku}",
        json=inventory_item,
        headers={"Content-Language": content_language},
        content_type="application/json",
    )
    return c.ok_or_error(status, body, headers)
