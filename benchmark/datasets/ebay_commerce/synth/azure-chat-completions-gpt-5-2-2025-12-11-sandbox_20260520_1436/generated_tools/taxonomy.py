from typing import Any, Dict, Optional

from .ebay_client import EbayClient


APP_SCOPE = "https://api.ebay.com/oauth/api_scope"


def get_default_category_tree_id(marketplace_id: str) -> Any:
    """GET /commerce/taxonomy/v1/get_default_category_tree_id

    Doc: docs/api_commerce_taxonomy_resources_category_tree_methods_getDefaultCategoryTreeId.md
    """
    client = EbayClient()
    return client.request(
        "GET",
        "/commerce/taxonomy/v1/get_default_category_tree_id",
        params={"marketplace_id": marketplace_id},
    )


def get_category_tree(category_tree_id: str) -> Any:
    """GET /commerce/taxonomy/v1/category_tree/{category_tree_id}

    Doc: docs/api_commerce_taxonomy_resources_category_tree_methods_getCategoryTree.md
    """
    client = EbayClient()
    return client.request("GET", f"/commerce/taxonomy/v1/category_tree/{category_tree_id}")


def get_category_subtree(category_tree_id: str, category_id: str) -> Any:
    """GET /commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_subtree

    Doc: docs/api_commerce_taxonomy_resources_category_tree_methods_getCategorySubtree.md
    """
    client = EbayClient()
    return client.request(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_subtree",
        params={"category_id": category_id},
    )


def get_category_suggestions(category_tree_id: str, q: str) -> Any:
    """GET /commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_suggestions

    Doc: docs/api_commerce_taxonomy_resources_category_tree_methods_getCategorySuggestions.md
    """
    client = EbayClient()
    return client.request(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_suggestions",
        params={"q": q},
    )


def get_item_aspects_for_category(category_tree_id: str, category_id: str) -> Any:
    """GET /commerce/taxonomy/v1/category_tree/{category_tree_id}/get_item_aspects_for_category

    Doc: docs/api_commerce_taxonomy_resources_category_tree_methods_getItemAspectsForCategory.md
    """
    client = EbayClient()
    return client.request(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_item_aspects_for_category",
        params={"category_id": category_id},
    )


def fetch_item_aspects(category_tree_id: str, payload: Dict[str, Any]) -> Any:
    """POST /commerce/taxonomy/v1/category_tree/{category_tree_id}/fetch_item_aspects

    Doc: docs/api_commerce_taxonomy_resources_category_tree_methods_fetchItemAspects.md
    """
    client = EbayClient()
    return client.request(
        "POST",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/fetch_item_aspects",
        json_body=payload,
    )


def get_expired_categories(category_tree_id: str, date: Optional[str] = None) -> Any:
    """GET /commerce/taxonomy/v1/category_tree/{category_tree_id}/get_expired_categories

    Doc: docs/api_commerce_taxonomy_resources_category_tree_methods_getExpiredCategories.md
    """
    client = EbayClient()
    params = {"date": date} if date else None
    return client.request(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_expired_categories",
        params=params,
    )


def get_compatibility_properties(category_tree_id: str, category_id: str) -> Any:
    """GET /commerce/taxonomy/v1/category_tree/{category_tree_id}/get_compatibility_properties

    Doc: docs/api_commerce_taxonomy_resources_category_tree_methods_getCompatibilityProperties.md
    """
    client = EbayClient()
    return client.request(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_compatibility_properties",
        params={"category_id": category_id},
    )


def get_compatibility_property_values(
    category_tree_id: str,
    category_id: str,
    compatibility_property: str,
) -> Any:
    """GET /commerce/taxonomy/v1/category_tree/{category_tree_id}/get_compatibility_property_values

    Doc: docs/api_commerce_taxonomy_resources_category_tree_methods_getCompatibilityPropertyValues.md
    """
    client = EbayClient()
    return client.request(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_compatibility_property_values",
        params={"category_id": category_id, "compatibility_property": compatibility_property},
    )
