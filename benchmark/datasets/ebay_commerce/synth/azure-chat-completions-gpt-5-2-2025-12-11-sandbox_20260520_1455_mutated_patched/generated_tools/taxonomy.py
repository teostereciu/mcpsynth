from __future__ import annotations

from typing import Any, Dict, Optional

from .ebay_client import EbayClient


def get_default_category_tree_id(marketplace_id: str) -> Dict[str, Any]:
    """GET /get_default_category_tree_id

    OAuth scope: https://api.ebay.com/oauth/api_scope (app token)
    """
    client = EbayClient.for_standard_api(user_scoped=False)
    return client.request(
        "GET",
        "/commerce/taxonomy/v1/get_default_category_tree_id",
        params={"marketplace_id": marketplace_id},
    )


def get_category_tree(category_tree_id: str) -> Dict[str, Any]:
    """GET /category_tree/{category_tree_id}

    OAuth scope: https://api.ebay.com/oauth/api_scope (app token)
    """
    client = EbayClient.for_standard_api(user_scoped=False)
    return client.request("GET", f"/commerce/taxonomy/v1/category_tree/{category_tree_id}")


def get_category_subtree(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    """GET /category_tree/{category_tree_id}/get_category_subtree

    OAuth scope: https://api.ebay.com/oauth/api_scope (app token)
    """
    client = EbayClient.for_standard_api(user_scoped=False)
    return client.request(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_subtree",
        params={"category_ids": category_id},
    )


def get_category_suggestions(category_tree_id: str, query: str) -> Dict[str, Any]:
    """GET /category_tree/{category_tree_id}/get_category_suggestions

    OAuth scope: https://api.ebay.com/oauth/api_scope (app token)
    """
    client = EbayClient.for_standard_api(user_scoped=False)
    return client.request(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_suggestions",
        params={"q": query},
    )


def get_item_aspects_for_category(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    """GET /category_tree/{category_tree_id}/get_item_aspects_for_category

    OAuth scope: https://api.ebay.com/oauth/api_scope (app token)
    """
    client = EbayClient.for_standard_api(user_scoped=False)
    return client.request(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_item_aspects_for_category",
        params={"category_ids": category_id},
    )


def fetch_item_aspects(category_tree_id: str, item: Dict[str, Any]) -> Dict[str, Any]:
    """GET /category_tree/{category_tree_id}/fetch_item_aspects

    Note: eBay expects an `item` query parameter containing a JSON object.

    OAuth scope: https://api.ebay.com/oauth/api_scope (app token)
    """
    client = EbayClient.for_standard_api(user_scoped=False)
    return client.request(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/fetch_item_aspects",
        params={"item": item},
    )


def get_compatibility_properties(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    """GET /category_tree/{category_tree_id}/get_compatibility_properties

    OAuth scope: https://api.ebay.com/oauth/api_scope (app token)
    """
    client = EbayClient.for_standard_api(user_scoped=False)
    return client.request(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_compatibility_properties",
        params={"category_ids": category_id},
    )


def get_compatibility_property_values(
    category_tree_id: str,
    category_id: str,
    compatibility_property: str,
    filter: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /category_tree/{category_tree_id}/get_compatibility_property_values

    `filter` is a comma-separated list of name:value pairs (URL encoding may be required).

    OAuth scope: https://api.ebay.com/oauth/api_scope (app token)
    """
    client = EbayClient.for_standard_api(user_scoped=False)
    params: Dict[str, Any] = {
        "category_ids": category_id,
        "compatibility_property": compatibility_property,
    }
    if filter is not None:
        params["filter"] = filter
    return client.request(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_compatibility_property_values",
        params=params,
    )


def get_expired_categories(category_tree_id: str, category_version: Optional[str] = None) -> Dict[str, Any]:
    """GET /category_tree/{category_tree_id}/get_expired_categories

    OAuth scope: https://api.ebay.com/oauth/api_scope (app token)
    """
    client = EbayClient.for_standard_api(user_scoped=False)
    params: Dict[str, Any] = {}
    if category_version is not None:
        params["category_version"] = category_version
    return client.request(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_expired_categories",
        params=params,
    )
