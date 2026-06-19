from typing import Any, Dict, Optional

from .ebay_client import EbayClient


TAXONOMY_SCOPE_APP = "https://api.ebay.com/oauth/api_scope"


def get_default_category_tree_id(marketplace_id: str) -> Dict[str, Any]:
    """Get the default category tree ID for a marketplace.

    GET /commerce/taxonomy/v1/get_default_category_tree_id?marketplace_id=...
    OAuth: app token
    """
    client = EbayClient()
    return client.request(
        "GET",
        "/commerce/taxonomy/v1/get_default_category_tree_id",
        params={"marketplace_id": marketplace_id},
        scope=TAXONOMY_SCOPE_APP,
        user=False,
        is_media=False,
    )


def get_category_tree(category_tree_id: str) -> Dict[str, Any]:
    """Get a full category tree.

    GET /commerce/taxonomy/v1/category_tree/{category_tree_id}
    """
    client = EbayClient()
    return client.request(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}",
        scope=TAXONOMY_SCOPE_APP,
        user=False,
        is_media=False,
    )


def get_category_subtree(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    """Get a category subtree.

    GET /commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_subtree?category_id=...
    """
    client = EbayClient()
    return client.request(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_subtree",
        params={"category_id": category_id},
        scope=TAXONOMY_SCOPE_APP,
        user=False,
        is_media=False,
    )


def get_category_suggestions(category_tree_id: str, q: str) -> Dict[str, Any]:
    """Get category suggestions for a query.

    GET /commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_suggestions?q=...
    """
    client = EbayClient()
    return client.request(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_suggestions",
        params={"q": q},
        scope=TAXONOMY_SCOPE_APP,
        user=False,
        is_media=False,
    )


def get_item_aspects_for_category(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    """Get item aspects for a category.

    GET /commerce/taxonomy/v1/category_tree/{category_tree_id}/get_item_aspects_for_category?category_id=...
    """
    client = EbayClient()
    return client.request(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_item_aspects_for_category",
        params={"category_id": category_id},
        scope=TAXONOMY_SCOPE_APP,
        user=False,
        is_media=False,
    )


def fetch_item_aspects(category_tree_id: str, category_id: str, *, additional_params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Fetch item aspects (bulk) for a category.

    GET /commerce/taxonomy/v1/category_tree/{category_tree_id}/fetch_item_aspects?category_id=...
    """
    params: Dict[str, Any] = {"category_id": category_id}
    if additional_params:
        params.update(additional_params)
    client = EbayClient()
    return client.request(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/fetch_item_aspects",
        params=params,
        scope=TAXONOMY_SCOPE_APP,
        user=False,
        is_media=False,
    )


def get_compatibility_properties(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    """Get compatibility properties for a category.

    GET /commerce/taxonomy/v1/category_tree/{category_tree_id}/get_compatibility_properties?category_id=...
    """
    client = EbayClient()
    return client.request(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_compatibility_properties",
        params={"category_id": category_id},
        scope=TAXONOMY_SCOPE_APP,
        user=False,
        is_media=False,
    )


def get_compatibility_property_values(
    category_tree_id: str,
    category_id: str,
    compatibility_property: str,
    *,
    filter: Optional[str] = None,
) -> Dict[str, Any]:
    """Get compatibility property values.

    GET /commerce/taxonomy/v1/category_tree/{category_tree_id}/get_compatibility_property_values
    """
    params: Dict[str, Any] = {"category_id": category_id, "compatibility_property": compatibility_property}
    if filter is not None:
        params["filter"] = filter
    client = EbayClient()
    return client.request(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_compatibility_property_values",
        params=params,
        scope=TAXONOMY_SCOPE_APP,
        user=False,
        is_media=False,
    )


def get_expired_categories(category_tree_id: str) -> Dict[str, Any]:
    """Get expired categories for a category tree.

    GET /commerce/taxonomy/v1/category_tree/{category_tree_id}/get_expired_categories
    """
    client = EbayClient()
    return client.request(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_expired_categories",
        scope=TAXONOMY_SCOPE_APP,
        user=False,
        is_media=False,
    )
