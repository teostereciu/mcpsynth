"""eBay Commerce Catalog API tools."""
from mcp.server.fastmcp import FastMCP
from .auth import get_app_token, get_base_url

def register(mcp: FastMCP):

    @mcp.tool()
    def get_product(epid: str, marketplace_id: str = "EBAY_US") -> dict:
        """Retrieve full details of a catalog product by its eBay product identifier (ePID).

        Args:
            epid: The eBay product identifier (ePID) of the product.
            marketplace_id: eBay marketplace ID (default: EBAY_US).
        """
        import requests
        token = get_app_token()
        if "error" in token:
            return token
        url = f"{get_base_url()}/commerce/catalog/v1_beta/product/{epid}"
        headers = {
            "Authorization": f"Bearer {token['access_token']}",
            "X-EBAY-C-MARKETPLACE-ID": marketplace_id,
        }
        try:
            resp = requests.get(url, headers=headers, timeout=30)
            if resp.status_code == 200:
                return resp.json()
            return {"error": resp.text, "status_code": resp.status_code}
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def search_products(
        q: str = "",
        gtin: str = "",
        mpn: str = "",
        category_ids: str = "",
        aspect_filter: str = "",
        fieldgroups: str = "",
        limit: str = "50",
        offset: str = "",
        marketplace_id: str = "EBAY_US",
    ) -> dict:
        """Search for product summaries in the eBay catalog.

        Args:
            q: Keyword search string (cannot be combined with gtin or mpn).
            gtin: Comma-separated GTINs (EAN, ISBN, UPC) to search for.
            mpn: Comma-separated Manufacturer Part Numbers to search for.
            category_ids: Comma-separated category IDs to narrow results.
            aspect_filter: Aspect filter string e.g. 'categoryId:9355,Color:{Black|White}'.
            fieldgroups: ASPECT_REFINEMENTS, MATCHING_PRODUCTS, or FULL.
            limit: Number of results to return (max 200, default 50).
            offset: Number of results to skip.
            marketplace_id: eBay marketplace ID (default: EBAY_US).
        """
        import requests
        token = get_app_token()
        if "error" in token:
            return token
        url = f"{get_base_url()}/commerce/catalog/v1_beta/product_summary/search"
        headers = {
            "Authorization": f"Bearer {token['access_token']}",
            "X-EBAY-C-MARKETPLACE-ID": marketplace_id,
        }
        params = {}
        if q:
            params["q"] = q
        if gtin:
            params["gtin"] = gtin
        if mpn:
            params["mpn"] = mpn
        if category_ids:
            params["category_ids"] = category_ids
        if aspect_filter:
            params["aspect_filter"] = aspect_filter
        if fieldgroups:
            params["fieldgroups"] = fieldgroups
        if limit:
            params["limit"] = limit
        if offset:
            params["offset"] = offset
        try:
            resp = requests.get(url, headers=headers, params=params, timeout=30)
            if resp.status_code == 200:
                return resp.json()
            return {"error": resp.text, "status_code": resp.status_code}
        except Exception as e:
            return {"error": str(e)}
