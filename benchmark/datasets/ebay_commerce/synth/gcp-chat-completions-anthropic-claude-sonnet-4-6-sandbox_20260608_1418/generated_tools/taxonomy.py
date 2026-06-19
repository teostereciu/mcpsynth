"""eBay Commerce Taxonomy API tools (category trees, aspects, compatibility)."""
from mcp.server.fastmcp import FastMCP
from .auth import get_app_token, get_base_url

def register(mcp: FastMCP):

    def _headers(token: dict) -> dict:
        return {"Authorization": f"Bearer {token['access_token']}"}

    @mcp.tool()
    def get_default_category_tree_id(marketplace_id: str) -> dict:
        """Retrieve the default category tree ID for an eBay marketplace.

        Args:
            marketplace_id: eBay marketplace ID, e.g. EBAY_US, EBAY_GB, EBAY_DE, EBAY_AU, etc.
        """
        import requests
        token = get_app_token()
        if "error" in token:
            return token
        url = f"{get_base_url()}/commerce/taxonomy/v1/get_default_category_tree_id"
        try:
            resp = requests.get(url, headers=_headers(token),
                                params={"marketplace_id": marketplace_id}, timeout=30)
            if resp.status_code == 200:
                return resp.json()
            return {"error": resp.text, "status_code": resp.status_code}
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_category_tree(category_tree_id: str) -> dict:
        """Retrieve the complete category tree for an eBay marketplace.

        Note: This can return a very large payload. Consider using get_category_subtree
        for a specific branch instead.

        Args:
            category_tree_id: The unique identifier of the eBay category tree
                              (from get_default_category_tree_id).
        """
        import requests
        token = get_app_token()
        if "error" in token:
            return token
        url = f"{get_base_url()}/commerce/taxonomy/v1/category_tree/{category_tree_id}"
        headers = {**_headers(token), "Accept-Encoding": "gzip"}
        try:
            resp = requests.get(url, headers=headers, timeout=60)
            if resp.status_code == 200:
                return resp.json()
            return {"error": resp.text, "status_code": resp.status_code}
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_category_subtree(category_tree_id: str, category_id: str) -> dict:
        """Retrieve the category subtree rooted at a specific category.

        Args:
            category_tree_id: The unique identifier of the eBay category tree.
            category_id: The unique identifier of the category at the top of the subtree.
        """
        import requests
        token = get_app_token()
        if "error" in token:
            return token
        url = (f"{get_base_url()}/commerce/taxonomy/v1/category_tree"
               f"/{category_tree_id}/get_category_subtree")
        headers = {**_headers(token), "Accept-Encoding": "gzip"}
        try:
            resp = requests.get(url, headers=headers,
                                params={"category_id": category_id}, timeout=60)
            if resp.status_code == 200:
                return resp.json()
            return {"error": resp.text, "status_code": resp.status_code}
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_category_suggestions(category_tree_id: str, q: str) -> dict:
        """Get suggested leaf categories for a product based on keywords.

        Note: Not supported in Sandbox (returns boilerplate text).

        Args:
            category_tree_id: The unique identifier of the eBay category tree.
            q: Free-form search string describing the product (e.g. 'iPhone 14 Pro').
        """
        import requests
        token = get_app_token()
        if "error" in token:
            return token
        url = (f"{get_base_url()}/commerce/taxonomy/v1/category_tree"
               f"/{category_tree_id}/get_category_suggestions")
        try:
            resp = requests.get(url, headers=_headers(token),
                                params={"q": q}, timeout=30)
            if resp.status_code == 200:
                return resp.json()
            return {"error": resp.text, "status_code": resp.status_code}
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_item_aspects_for_category(category_tree_id: str, category_id: str) -> dict:
        """Retrieve aspects (item attributes) for a specific leaf category.

        Returns required and optional aspects, their data types, allowed values,
        and whether they can be used for item variations.

        Args:
            category_tree_id: The unique identifier of the eBay category tree.
            category_id: The unique identifier of the leaf category.
        """
        import requests
        token = get_app_token()
        if "error" in token:
            return token
        url = (f"{get_base_url()}/commerce/taxonomy/v1/category_tree"
               f"/{category_tree_id}/get_item_aspects_for_category")
        try:
            resp = requests.get(url, headers=_headers(token),
                                params={"category_id": category_id}, timeout=30)
            if resp.status_code == 200:
                return resp.json()
            return {"error": resp.text, "status_code": resp.status_code}
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def fetch_item_aspects(category_tree_id: str) -> dict:
        """Fetch all item aspects for all leaf categories in a marketplace (bulk download).

        Returns a gzipped JSON payload. This can be a very large response (100+ MB compressed).

        Args:
            category_tree_id: The unique identifier of the eBay category tree.
        """
        import requests
        token = get_app_token()
        if "error" in token:
            return token
        url = (f"{get_base_url()}/commerce/taxonomy/v1/category_tree"
               f"/{category_tree_id}/fetch_item_aspects")
        try:
            resp = requests.get(url, headers=_headers(token), timeout=120)
            if resp.status_code == 200:
                # Response is gzipped binary; try to parse as JSON
                try:
                    return resp.json()
                except Exception:
                    return {"status": "success", "content_type": resp.headers.get("Content-Type"),
                            "content_length": len(resp.content)}
            return {"error": resp.text, "status_code": resp.status_code}
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_expired_categories(category_tree_id: str) -> dict:
        """Retrieve mappings of expired leaf categories to their active replacements.

        Args:
            category_tree_id: The unique identifier of the eBay category tree.
        """
        import requests
        token = get_app_token()
        if "error" in token:
            return token
        url = (f"{get_base_url()}/commerce/taxonomy/v1/category_tree"
               f"/{category_tree_id}/get_expired_categories")
        try:
            resp = requests.get(url, headers=_headers(token), timeout=30)
            if resp.status_code == 200:
                return resp.json()
            return {"error": resp.text, "status_code": resp.status_code}
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_compatibility_properties(category_tree_id: str, category_id: str) -> dict:
        """Retrieve compatible vehicle properties (Make, Model, Year, etc.) for a parts category.

        Args:
            category_tree_id: Category tree ID (e.g. 100 for eBay Motors US, 0 for eBay US).
            category_id: eBay category ID that supports parts compatibility.
        """
        import requests
        token = get_app_token()
        if "error" in token:
            return token
        url = (f"{get_base_url()}/commerce/taxonomy/v1/category_tree"
               f"/{category_tree_id}/get_compatibility_properties")
        try:
            resp = requests.get(url, headers=_headers(token),
                                params={"category_id": category_id}, timeout=30)
            if resp.status_code == 200:
                return resp.json()
            return {"error": resp.text, "status_code": resp.status_code}
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_compatibility_property_values(
        category_tree_id: str,
        category_id: str,
        compatibility_property: str,
        filter: str = "",
    ) -> dict:
        """Retrieve valid values for a compatible vehicle property.

        Example: Get all 2018 Honda models by setting compatibility_property='Model'
        and filter='Year:2018,Make:Honda'.

        Args:
            category_tree_id: Category tree ID (e.g. 100 for eBay Motors US).
            category_id: eBay category ID that supports parts compatibility.
            compatibility_property: The vehicle property to retrieve values for
                                    (e.g. 'Make', 'Model', 'Year', 'Trim', 'Engine').
            filter: Comma-separated name:value pairs to narrow results
                    (e.g. 'Year:2018,Make:Honda').
        """
        import requests
        token = get_app_token()
        if "error" in token:
            return token
        url = (f"{get_base_url()}/commerce/taxonomy/v1/category_tree"
               f"/{category_tree_id}/get_compatibility_property_values")
        params = {
            "category_id": category_id,
            "compatibility_property": compatibility_property,
        }
        if filter:
            params["filter"] = filter
        try:
            resp = requests.get(url, headers=_headers(token), params=params, timeout=30)
            if resp.status_code == 200:
                return resp.json()
            return {"error": resp.text, "status_code": resp.status_code}
        except Exception as e:
            return {"error": str(e)}
