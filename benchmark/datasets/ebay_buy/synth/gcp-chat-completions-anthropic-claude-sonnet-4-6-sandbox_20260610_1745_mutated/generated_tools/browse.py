"""
eBay Buy Browse API tools.
Covers: item search, item details, item groups, compatibility checks.
"""

from typing import Optional
from mcp.server.fastmcp import FastMCP
from .auth import get_auth_headers, get_base_url


def register_browse_tools(mcp: FastMCP) -> None:

    @mcp.tool()
    def search_items(
        q: Optional[str] = None,
        category_ids: Optional[str] = None,
        filter: Optional[str] = None,
        sort: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        fieldgroups: Optional[str] = None,
        aspect_filter: Optional[str] = None,
        epid: Optional[str] = None,
        gtin: Optional[str] = None,
        charity_ids: Optional[str] = None,
        compatibility_filter: Optional[str] = None,
        marketplace_id: str = "EBAY_US",
    ) -> dict:
        """Search for eBay items by keyword, category, ePID, GTIN, or charity.
        Supports filtering, sorting, pagination, and aspect refinements.

        Args:
            q: Keyword search string (e.g. 'drone', 'nike shoes').
            category_ids: Comma-separated category IDs to restrict search.
            filter: Filter expressions (e.g. 'price:[10..50],conditions:{NEW}').
            sort: Sort order (e.g. 'price', '-price', 'newlyListed', 'distance').
            limit: Max number of items to return per page (default 50, max 200).
            offset: Number of items to skip for pagination.
            fieldgroups: Additional field groups to return (e.g. 'EXTENDED').
            aspect_filter: Filter by item aspects (e.g. 'categoryId:9355,Color:{Red}').
            epid: eBay product ID to search within.
            gtin: Global Trade Item Number (UPC, EAN, ISBN).
            charity_ids: Comma-separated charity registration IDs.
            compatibility_filter: Filter by vehicle compatibility attributes.
            marketplace_id: eBay marketplace ID (default EBAY_US).
        """
        import requests
        params = {}
        if q:
            params["q"] = q
        if category_ids:
            params["category_ids"] = category_ids
        if filter:
            params["filter"] = filter
        if sort:
            params["sort"] = sort
        if limit is not None:
            params["limit"] = limit
        if offset is not None:
            params["offset"] = offset
        if fieldgroups:
            params["fieldgroups"] = fieldgroups
        if aspect_filter:
            params["aspect_filter"] = aspect_filter
        if epid:
            params["epid"] = epid
        if gtin:
            params["gtin"] = gtin
        if charity_ids:
            params["charity_ids"] = charity_ids
        if compatibility_filter:
            params["compatibility_filter"] = compatibility_filter

        url = f"{get_base_url()}/buy/browse/v1/item_summary/search"
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
    def search_items_by_image(
        image_base64: str,
        category_ids: Optional[str] = None,
        filter: Optional[str] = None,
        sort: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        aspect_filter: Optional[str] = None,
        marketplace_id: str = "EBAY_US",
    ) -> dict:
        """Search for eBay items using a Base64-encoded image.
        Returns item summaries visually similar to the provided image.

        Args:
            image_base64: Base64-encoded image string.
            category_ids: Comma-separated category IDs to restrict search.
            filter: Filter expressions (e.g. 'price:[10..50]').
            sort: Sort order (e.g. 'price', '-price').
            limit: Max number of items to return.
            offset: Number of items to skip for pagination.
            aspect_filter: Filter by item aspects.
            marketplace_id: eBay marketplace ID (default EBAY_US).
        """
        import requests
        params = {}
        if category_ids:
            params["category_ids"] = category_ids
        if filter:
            params["filter"] = filter
        if sort:
            params["sort"] = sort
        if limit is not None:
            params["limit"] = limit
        if offset is not None:
            params["offset"] = offset
        if aspect_filter:
            params["aspect_filter"] = aspect_filter

        url = f"{get_base_url()}/buy/browse/v1/item_summary/search_by_image"
        try:
            resp = requests.post(
                url,
                params=params,
                json={"image": image_base64},
                headers={
                    **get_auth_headers(),
                    "X-EBAY-C-MARKETPLACE-ID": marketplace_id,
                    "Content-Type": "application/json",
                },
                timeout=30,
            )
            if resp.status_code == 200:
                return resp.json()
            return {"error": resp.text, "status_code": resp.status_code}
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_item(
        item_id: str,
        fieldgroups: Optional[str] = None,
        marketplace_id: str = "EBAY_US",
    ) -> dict:
        """Retrieve full details of a specific eBay item by its RESTful item ID.
        Returns price, description, condition, shipping, seller info, and more.

        Args:
            item_id: RESTful item ID (e.g. 'v1|123456789|0').
            fieldgroups: Optional field groups: PRODUCT, COMPACT,
                         ADDITIONAL_SELLER_DETAILS, CHARITY_DETAILS.
            marketplace_id: eBay marketplace ID (default EBAY_US).
        """
        import requests
        params = {}
        if fieldgroups:
            params["fieldgroups"] = fieldgroups

        url = f"{get_base_url()}/buy/browse/v1/item/{item_id}"
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
    def get_item_by_legacy_id(
        legacy_item_id: str,
        legacy_variation_id: Optional[str] = None,
        legacy_variation_sku: Optional[str] = None,
        fieldgroups: Optional[str] = None,
        marketplace_id: str = "EBAY_US",
    ) -> dict:
        """Retrieve item details using a legacy eBay item ID (from Shopping/Finding APIs).
        Also returns the RESTful item_id for use with other Buy API methods.

        Args:
            legacy_item_id: The legacy item ID (e.g. '281726208046').
            legacy_variation_id: Legacy variation ID for multi-SKU items.
            legacy_variation_sku: SKU of the variation.
            fieldgroups: Optional field groups: PRODUCT, ADDITIONAL_SELLER_DETAILS,
                         CHARITY_DETAILS.
            marketplace_id: eBay marketplace ID (default EBAY_US).
        """
        import requests
        params = {"legacy_item_id": legacy_item_id}
        if legacy_variation_id:
            params["legacy_variation_id"] = legacy_variation_id
        if legacy_variation_sku:
            params["legacy_variation_sku"] = legacy_variation_sku
        if fieldgroups:
            params["fieldgroups"] = fieldgroups

        url = f"{get_base_url()}/buy/browse/v1/item/get_item_by_legacy_id"
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
    def get_items(
        item_ids: Optional[str] = None,
        item_group_ids: Optional[str] = None,
        marketplace_id: str = "EBAY_US",
    ) -> dict:
        """Retrieve details for multiple eBay items in a single call.
        Pass either a list of item IDs or item group IDs (not both).

        Args:
            item_ids: Comma-separated RESTful item IDs
                      (e.g. 'v1|123|0,v1|456|0'). Max 20.
            item_group_ids: Comma-separated item group IDs. Max 10.
            marketplace_id: eBay marketplace ID (default EBAY_US).
        """
        import requests
        params = {}
        if item_ids:
            params["item_ids"] = item_ids
        if item_group_ids:
            params["item_group_ids"] = item_group_ids

        url = f"{get_base_url()}/buy/browse/v1/item"
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
    def get_items_by_item_group(
        item_group_id: str,
        fieldgroups: Optional[str] = None,
        marketplace_id: str = "EBAY_US",
    ) -> dict:
        """Retrieve all item variations within an item group (e.g. different sizes/colors).
        Returns individual item details plus shared descriptions.

        Args:
            item_group_id: The item group ID (e.g. '351825690866').
            fieldgroups: Optional field groups: ADDITIONAL_SELLER_DETAILS,
                         CHARITY_DETAILS.
            marketplace_id: eBay marketplace ID (default EBAY_US).
        """
        import requests
        params = {"item_group_id": item_group_id}
        if fieldgroups:
            params["fieldgroups"] = fieldgroups

        url = f"{get_base_url()}/buy/browse/v1/item/get_items_by_item_group"
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
    def check_item_compatibility(
        item_id: str,
        compatibility_properties: list,
        marketplace_id: str = "EBAY_US",
    ) -> dict:
        """Check if a part/item is compatible with a specific vehicle or product.
        Returns COMPATIBLE, NOT_COMPATIBLE, or UNDETERMINED.

        Args:
            item_id: RESTful item ID of the part to check (e.g. 'v1|123456789|0').
            compatibility_properties: List of dicts with 'name' and 'value' keys
                defining the product (e.g. [{'name': 'Year', 'value': '2019'},
                {'name': 'Make', 'value': 'Honda'}, {'name': 'Model', 'value': 'Civic'}]).
            marketplace_id: eBay marketplace ID (default EBAY_US).
        """
        import requests
        url = f"{get_base_url()}/buy/browse/v1/item/{item_id}/check_compatibility"
        payload = {"compatibilityProperties": compatibility_properties}
        try:
            resp = requests.post(
                url,
                json=payload,
                headers={
                    **get_auth_headers(),
                    "X-EBAY-C-MARKETPLACE-ID": marketplace_id,
                    "Content-Type": "application/json",
                },
                timeout=30,
            )
            if resp.status_code == 200:
                return resp.json()
            return {"error": resp.text, "status_code": resp.status_code}
        except Exception as e:
            return {"error": str(e)}
