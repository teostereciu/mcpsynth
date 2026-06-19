"""
eBay Buy Deal API tools.
Covers: deal items, events, event items.
"""

from __future__ import annotations
from typing import Optional
from .auth import get_auth_header, get_base_url


def get_deal_items(
    category_ids: Optional[str] = None,
    commissionable: Optional[str] = None,
    delivery_country: Optional[str] = None,
    max_results: Optional[int] = None,
    skip: Optional[int] = None,
    marketplace_id: str = "EBAY_US",
) -> dict:
    """
    Retrieve a paginated set of eBay deal items for the specified marketplace.

    Args:
        category_ids: Comma-separated eBay category IDs to filter results.
        commissionable: Filter by commissionable items ('true' or 'false').
            Only supported for the US marketplace.
        delivery_country: 2-digit ISO country code to filter by shippable country.
        max_results: Maximum number of items per page (max 100, default 20).
        skip: Number of items to skip for pagination (default 0).
        marketplace_id: eBay marketplace ID (default EBAY_US).
    """
    import requests
    params = {}
    if category_ids:
        params["category_ids"] = category_ids
    if commissionable is not None:
        params["commissionable"] = commissionable
    if delivery_country:
        params["delivery_country"] = delivery_country
    if max_results is not None:
        params["max_results"] = max_results
    if skip is not None:
        params["skip"] = skip

    url = f"{get_base_url()}/buy/deal/v1/deal_item"
    headers = get_auth_header()
    headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    try:
        resp = requests.get(url, headers=headers, params=params, timeout=30)
        if resp.status_code == 200:
            return resp.json()
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


def get_event(
    event_id: str,
    marketplace_id: str = "EBAY_US",
) -> dict:
    """
    Retrieve details for a specific eBay deal event by event ID.

    Args:
        event_id: The unique identifier of the eBay event.
        marketplace_id: eBay marketplace ID (default EBAY_US).
    """
    import requests
    url = f"{get_base_url()}/buy/deal/v1/event/{event_id}"
    headers = get_auth_header()
    headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    try:
        resp = requests.get(url, headers=headers, timeout=30)
        if resp.status_code == 200:
            return resp.json()
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


def get_events(
    max_results: Optional[int] = None,
    skip: Optional[int] = None,
    marketplace_id: str = "EBAY_US",
) -> dict:
    """
    Retrieve a paginated list of all eBay deal events for the specified marketplace.

    Args:
        max_results: Maximum number of events per page (max 100, default 20).
        skip: Number of events to skip for pagination (default 0).
        marketplace_id: eBay marketplace ID (default EBAY_US).
    """
    import requests
    params = {}
    if max_results is not None:
        params["max_results"] = max_results
    if skip is not None:
        params["skip"] = skip

    url = f"{get_base_url()}/buy/deal/v1/event"
    headers = get_auth_header()
    headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    try:
        resp = requests.get(url, headers=headers, params=params, timeout=30)
        if resp.status_code == 200:
            return resp.json()
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


def get_event_items(
    event_ids: str,
    category_ids: Optional[str] = None,
    delivery_country: Optional[str] = None,
    max_results: Optional[int] = None,
    skip: Optional[int] = None,
    marketplace_id: str = "EBAY_US",
) -> dict:
    """
    Retrieve a paginated set of items associated with a specific eBay deal event.

    Args:
        event_ids: The unique identifier of the event (only one event ID supported).
        category_ids: A single eBay category ID to filter results.
        delivery_country: 2-digit ISO country code to filter by shippable country.
        max_results: Maximum number of items per page (max 100, default 20).
        skip: Number of items to skip for pagination (default 0).
        marketplace_id: eBay marketplace ID (default EBAY_US).
    """
    import requests
    params = {"event_ids": event_ids}
    if category_ids:
        params["category_ids"] = category_ids
    if delivery_country:
        params["delivery_country"] = delivery_country
    if max_results is not None:
        params["max_results"] = max_results
    if skip is not None:
        params["skip"] = skip

    url = f"{get_base_url()}/buy/deal/v1/event_item"
    headers = get_auth_header()
    headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    try:
        resp = requests.get(url, headers=headers, params=params, timeout=30)
        if resp.status_code == 200:
            return resp.json()
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}
