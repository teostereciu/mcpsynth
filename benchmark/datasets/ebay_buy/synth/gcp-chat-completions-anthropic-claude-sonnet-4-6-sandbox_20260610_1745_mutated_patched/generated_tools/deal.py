"""
eBay Buy Deal API tools.
Covers: deal items, events, event items.
"""

from typing import Optional
from mcp.server.fastmcp import FastMCP
from .auth import get_auth_headers, get_base_url


def register_deal_tools(mcp: FastMCP) -> None:

    @mcp.tool()
    def get_deal_items(
        category_ids: Optional[str] = None,
        commissionable: Optional[bool] = None,
        delivery_country: Optional[str] = None,
        max_results: Optional[int] = None,
        skip: Optional[int] = None,
        marketplace_id: str = "EBAY_US",
    ) -> dict:
        """Retrieve a paginated set of eBay deal items for a marketplace.
        Deal items are discounted listings with special pricing.

        Args:
            category_ids: Comma-separated category IDs to filter deals.
            commissionable: If True, return only commissionable items (US only).
            delivery_country: 2-letter ISO country code for shipping filter.
            max_results: Max items per page (default 20, max 100).
            skip: Number of items to skip for pagination.
            marketplace_id: eBay marketplace ID (default EBAY_US).
        """
        import requests
        params = {}
        if category_ids:
            params["category_ids"] = category_ids
        if commissionable is not None:
            params["commissionable"] = str(commissionable).lower()
        if delivery_country:
            params["delivery_country"] = delivery_country
        if max_results is not None:
            params["limit"] = max_results
        if skip is not None:
            params["offset"] = skip

        url = f"{get_base_url()}/buy/deal/v1/deal_item"
        try:
            resp = requests.get(
                url,
                params=params,
                headers={**get_auth_headers(), "X-EBAY-C-MARKETPLACE-ID": marketplace_id},
                timeout=30,
            )
            if resp.status_code == 200:
                return resp.json()
            return {"error": resp.text, "status_code": resp.status_code}
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_events(
        max_results: Optional[int] = None,
        skip: Optional[int] = None,
        marketplace_id: str = "EBAY_US",
    ) -> dict:
        """Retrieve all eBay sale events for a marketplace (paginated).
        Events are time-limited promotional sales with curated items.

        Args:
            max_results: Max events per page (default 20, max 100).
            skip: Number of events to skip for pagination.
            marketplace_id: eBay marketplace ID (default EBAY_US).
        """
        import requests
        params = {}
        if max_results is not None:
            params["limit"] = max_results
        if skip is not None:
            params["offset"] = skip

        url = f"{get_base_url()}/buy/deal/v1/event"
        try:
            resp = requests.get(
                url,
                params=params,
                headers={**get_auth_headers(), "X-EBAY-C-MARKETPLACE-ID": marketplace_id},
                timeout=30,
            )
            if resp.status_code == 200:
                return resp.json()
            return {"error": resp.text, "status_code": resp.status_code}
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_event(
        event_id: str,
        marketplace_id: str = "EBAY_US",
    ) -> dict:
        """Retrieve details for a specific eBay sale event by its ID.
        Returns event title, description, dates, coupons, and terms.

        Args:
            event_id: The unique event identifier (use get_events to find IDs).
            marketplace_id: eBay marketplace ID (default EBAY_US).
        """
        import requests
        url = f"{get_base_url()}/buy/deal/v1/event/{event_id}"
        try:
            resp = requests.get(
                url,
                headers={**get_auth_headers(), "X-EBAY-C-MARKETPLACE-ID": marketplace_id},
                timeout=30,
            )
            if resp.status_code == 200:
                return resp.json()
            return {"error": resp.text, "status_code": resp.status_code}
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_event_items(
        event_ids: str,
        category_ids: Optional[str] = None,
        delivery_country: Optional[str] = None,
        max_results: Optional[int] = None,
        skip: Optional[int] = None,
        marketplace_id: str = "EBAY_US",
    ) -> dict:
        """Retrieve items associated with a specific eBay sale event.
        Returns discounted items with pricing, images, and shipping info.

        Args:
            event_ids: The event ID to retrieve items for (one at a time).
            category_ids: Category ID to filter event items (max 1).
            delivery_country: 2-letter ISO country code for shipping filter.
            max_results: Max items per page (default 20, max 100).
            skip: Number of items to skip for pagination.
            marketplace_id: eBay marketplace ID (default EBAY_US).
        """
        import requests
        params = {"event_ids": event_ids}
        if category_ids:
            params["category_ids"] = category_ids
        if delivery_country:
            params["delivery_country"] = delivery_country
        if max_results is not None:
            params["limit"] = max_results
        if skip is not None:
            params["offset"] = skip

        url = f"{get_base_url()}/buy/deal/v1/event_item"
        try:
            resp = requests.get(
                url,
                params=params,
                headers={**get_auth_headers(), "X-EBAY-C-MARKETPLACE-ID": marketplace_id},
                timeout=30,
            )
            if resp.status_code == 200:
                return resp.json()
            return {"error": resp.text, "status_code": resp.status_code}
        except Exception as e:
            return {"error": str(e)}
