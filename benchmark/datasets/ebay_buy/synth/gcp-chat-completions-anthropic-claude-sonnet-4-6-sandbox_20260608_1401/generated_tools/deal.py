"""
eBay Buy Deal API tools.
Covers: deal items, events, event items.
"""
from typing import Optional
from . import _client as client


def get_deal_items(
    category_ids: Optional[str] = None,
    commissionable: Optional[str] = None,
    delivery_country: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    marketplace_id: str = "EBAY_US",
) -> dict:
    """Retrieve a paginated set of eBay deal items for a marketplace.

    Args:
        category_ids: Comma-separated category IDs to filter deal items.
        commissionable: Filter by commissionable status ('true' or 'false').
            Only supported for US marketplace.
        delivery_country: 2-digit ISO country code to filter by shippable country.
        limit: Max items per page (default 20, max 100).
        offset: Number of items to skip for pagination (default 0).
        marketplace_id: eBay marketplace ID (required, e.g. 'EBAY_US').
    """
    params = {}
    if category_ids is not None:
        params["category_ids"] = category_ids
    if commissionable is not None:
        params["commissionable"] = commissionable
    if delivery_country is not None:
        params["delivery_country"] = delivery_country
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset

    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    return client.get(
        "/buy/deal/v1/deal_item",
        params=params,
        extra_headers=headers,
    )


def get_event(
    event_id: str,
    marketplace_id: str = "EBAY_US",
) -> dict:
    """Retrieve details for a specific eBay deal event by event ID.

    Args:
        event_id: The unique identifier of the eBay event.
        marketplace_id: eBay marketplace ID (required, e.g. 'EBAY_US').
    """
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    return client.get(
        f"/buy/deal/v1/event/{event_id}",
        extra_headers=headers,
    )


def get_events(
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    marketplace_id: str = "EBAY_US",
) -> dict:
    """Retrieve a paginated list of all eBay deal events for a marketplace.

    Args:
        limit: Max events per page (default 20, max 100).
        offset: Number of events to skip for pagination (default 0).
        marketplace_id: eBay marketplace ID (required, e.g. 'EBAY_US').
    """
    params = {}
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset

    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    return client.get(
        "/buy/deal/v1/event",
        params=params,
        extra_headers=headers,
    )


def get_event_items(
    event_ids: str,
    category_ids: Optional[str] = None,
    delivery_country: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    marketplace_id: str = "EBAY_US",
) -> dict:
    """Retrieve a paginated set of items associated with a specific eBay deal event.

    Args:
        event_ids: The unique identifier of the event (maximum 1 event ID).
        category_ids: Category ID to filter event items (maximum 1).
        delivery_country: 2-digit ISO country code to filter by shippable country.
        limit: Max items per page (default 20).
        offset: Number of items to skip for pagination (default 0).
        marketplace_id: eBay marketplace ID (required, e.g. 'EBAY_US').
    """
    params = {"event_ids": event_ids}
    if category_ids is not None:
        params["category_ids"] = category_ids
    if delivery_country is not None:
        params["delivery_country"] = delivery_country
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset

    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    return client.get(
        "/buy/deal/v1/event_item",
        params=params,
        extra_headers=headers,
    )
