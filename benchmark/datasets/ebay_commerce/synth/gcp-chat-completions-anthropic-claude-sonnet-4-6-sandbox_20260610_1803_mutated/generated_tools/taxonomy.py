"""
eBay Commerce Taxonomy API tools.
Base URL: https://api.sandbox.ebay.com/commerce/taxonomy/v1
Auth: App token (client_credentials)
"""

import requests
from .auth import app_headers, _base_url


def _taxonomy_url(path: str) -> str:
    return f"{_base_url()}/commerce/taxonomy/v1{path}"


def get_default_category_tree_id(marketplace_id: str) -> dict:
    """
    Retrieve the default category tree ID and version for a given eBay marketplace.
    marketplace_id: e.g. 'EBAY_US', 'EBAY_GB', 'EBAY_DE', 'EBAY_AU', etc.
    Returns categoryTreeId and categoryTreeVersion.
    """
    try:
        resp = requests.get(
            _taxonomy_url("/get_default_category_tree_id"),
            headers=app_headers(),
            params={"marketplace_id": marketplace_id},
            timeout=30,
        )
        if resp.status_code == 200:
            return resp.json()
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


def get_category_tree(category_tree_id: str) -> dict:
    """
    Retrieve the complete category tree for the given category tree ID.
    WARNING: This can return a very large payload (up to ~20,000 categories).
    Use get_category_subtree for a smaller subset.
    Returns the full tree with applicableMarketplaceIds, categoryTreeId,
    categoryTreeVersion, and rootCategoryNode.
    """
    try:
        resp = requests.get(
            _taxonomy_url(f"/category_tree/{category_tree_id}"),
            headers={**app_headers(), "Accept-Encoding": "gzip"},
            timeout=120,
        )
        if resp.status_code == 200:
            return resp.json()
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


def get_category_subtree(category_tree_id: str, category_id: str) -> dict:
    """
    Retrieve the subtree of a category tree rooted at the specified category.
    category_tree_id: use get_default_category_tree_id to find this.
    category_id: the category at the top of the desired subtree.
    Returns categorySubtreeNode, categoryTreeId, categoryTreeVersion.
    """
    try:
        resp = requests.get(
            _taxonomy_url(f"/category_tree/{category_tree_id}/get_category_subtree"),
            headers={**app_headers(), "Accept-Encoding": "gzip"},
            params={"category_id": category_id},
            timeout=60,
        )
        if resp.status_code == 200:
            return resp.json()
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


def get_category_suggestions(category_tree_id: str, query: str) -> dict:
    """
    Get suggested leaf categories for a product based on a keyword query.
    category_tree_id: use get_default_category_tree_id to find this.
    query: free-form text describing the product (e.g. 'iphone', 'drone').
    Returns categorySuggestions array sorted by relevance, plus categoryTreeId/Version.
    Note: Not supported in Sandbox (returns boilerplate text).
    """
    try:
        resp = requests.get(
            _taxonomy_url(f"/category_tree/{category_tree_id}/get_category_suggestions"),
            headers=app_headers(),
            params={"q": query},
            timeout=30,
        )
        if resp.status_code == 200:
            return resp.json()
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


def get_item_aspects_for_category(category_tree_id: str, category_id: str) -> dict:
    """
    Retrieve all item aspects (attributes) for a specific leaf category.
    category_tree_id: use get_default_category_tree_id to find this.
    category_id: must be a leaf category ID.
    Returns aspects array with constraints, allowed values, and requirement info.
    """
    try:
        resp = requests.get(
            _taxonomy_url(f"/category_tree/{category_tree_id}/get_item_aspects_for_category"),
            headers=app_headers(),
            params={"category_id": category_id},
            timeout=30,
        )
        if resp.status_code == 200:
            return resp.json()
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


def fetch_item_aspects(category_tree_id: str) -> dict:
    """
    Fetch all item aspects for all leaf categories in a marketplace (bulk download).
    Returns a gzipped JSON file as binary — this method returns the parsed JSON.
    WARNING: Response can be over 100 MB compressed. Use sparingly.
    category_tree_id: use get_default_category_tree_id to find this.
    """
    try:
        resp = requests.get(
            _taxonomy_url(f"/category_tree/{category_tree_id}/fetch_item_aspects"),
            headers=app_headers(),
            timeout=300,
            stream=True,
        )
        if resp.status_code == 200:
            # Response is gzip-compressed JSON
            import gzip
            import json
            content = resp.content
            try:
                decompressed = gzip.decompress(content)
                return json.loads(decompressed)
            except Exception:
                return {"raw_bytes_length": len(content), "note": "Response is gzip-compressed JSON"}
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


def get_compatibility_properties(category_tree_id: str, category_id: str) -> dict:
    """
    Retrieve compatible vehicle aspects (Make, Model, Year, Engine, Trim, etc.)
    for a parts-compatibility-enabled category.
    category_tree_id: e.g. '0' (US), '100' (US Motors), '3' (UK), '77' (Germany).
    category_id: must be a category that supports parts compatibility.
    Returns compatibilityProperties array with name and localizedName.
    """
    try:
        resp = requests.get(
            _taxonomy_url(f"/category_tree/{category_tree_id}/get_compatibility_properties"),
            headers=app_headers(),
            params={"category_id": category_id},
            timeout=30,
        )
        if resp.status_code == 200:
            return resp.json()
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


def get_compatibility_property_values(
    category_tree_id: str,
    category_id: str,
    compatibility_property: str,
    filter: str | None = None,
) -> dict:
    """
    Retrieve valid values for a specific vehicle compatibility property.
    category_tree_id: e.g. '100' for US Motors.
    category_id: parts-compatible category ID.
    compatibility_property: e.g. 'Make', 'Model', 'Year', 'Trim', 'Engine'.
    filter: optional comma-separated name:value pairs, e.g. 'Year:2018,Make:Honda'.
    Returns compatibilityPropertyValues array.
    """
    try:
        params: dict = {
            "category_id": category_id,
            "compatibility_property": compatibility_property,
        }
        if filter:
            params["filter"] = filter
        resp = requests.get(
            _taxonomy_url(f"/category_tree/{category_tree_id}/get_compatibility_property_values"),
            headers=app_headers(),
            params=params,
            timeout=30,
        )
        if resp.status_code == 200:
            return resp.json()
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


def get_expired_categories(category_tree_id: str) -> dict:
    """
    Retrieve mappings of expired leaf categories to their active replacements.
    category_tree_id: use get_default_category_tree_id to find this.
    Returns expiredCategories array with fromCategoryId and toCategoryId.
    """
    try:
        resp = requests.get(
            _taxonomy_url(f"/category_tree/{category_tree_id}/get_expired_categories"),
            headers=app_headers(),
            timeout=30,
        )
        if resp.status_code == 200:
            return resp.json()
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}
