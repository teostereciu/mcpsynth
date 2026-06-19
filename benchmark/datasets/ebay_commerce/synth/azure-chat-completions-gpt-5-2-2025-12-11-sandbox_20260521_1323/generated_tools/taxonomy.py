from typing import Any, Dict, Optional

from .http_client import EbayClient


TAXONOMY_SCOPE = "https://api.ebay.com/oauth/api_scope"


def get_default_category_tree_id(marketplace_id: str) -> Dict[str, Any]:
    """GET /commerce/taxonomy/v1/get_default_category_tree_id

    Doc: docs/api_commerce_taxonomy_resources_category_tree_methods_getDefaultCategoryTreeId.md
    """
    client = EbayClient()
    return client.request(
        "GET",
        "/commerce/taxonomy/v1/get_default_category_tree_id",
        params={"marketplace_id": marketplace_id},
        scope=TAXONOMY_SCOPE,
    )


def get_category_tree(category_tree_id: str) -> Dict[str, Any]:
    """GET /commerce/taxonomy/v1/category_tree/{category_tree_id}

    Doc: docs/api_commerce_taxonomy_resources_category_tree_methods_getCategoryTree.md
    """
    client = EbayClient()
    return client.request(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}",
        scope=TAXONOMY_SCOPE,
    )


def get_category_subtree(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    """GET /commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_subtree

    Doc: docs/api_commerce_taxonomy_resources_category_tree_methods_getCategorySubtree.md
    """
    client = EbayClient()
    return client.request(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_subtree",
        params={"category_id": category_id},
        scope=TAXONOMY_SCOPE,
    )


def get_category_suggestions(category_tree_id: str, q: str) -> Dict[str, Any]:
    """GET /commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_suggestions

    Doc: docs/api_commerce_taxonomy_resources_category_tree_methods_getCategorySuggestions.md
    """
    client = EbayClient()
    return client.request(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_suggestions",
        params={"q": q},
        scope=TAXONOMY_SCOPE,
    )


def get_item_aspects_for_category(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    """GET /commerce/taxonomy/v1/category_tree/{category_tree_id}/get_item_aspects_for_category

    Doc: docs/api_commerce_taxonomy_resources_category_tree_methods_getItemAspectsForCategory.md
    """
    client = EbayClient()
    return client.request(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_item_aspects_for_category",
        params={"category_id": category_id},
        scope=TAXONOMY_SCOPE,
    )


def fetch_item_aspects(category_tree_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    """POST /commerce/taxonomy/v1/category_tree/{category_tree_id}/fetch_item_aspects

    Doc: docs/api_commerce_taxonomy_resources_category_tree_methods_fetchItemAspects.md
    """
    client = EbayClient()
    return client.request(
        "POST",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/fetch_item_aspects",
        json_body=payload,
        scope=TAXONOMY_SCOPE,
    )


def get_compatibility_properties(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    """GET /commerce/taxonomy/v1/category_tree/{category_tree_id}/get_compatibility_properties

    Doc: docs/api_commerce_taxonomy_resources_category_tree_methods_getCompatibilityProperties.md
    """
    client = EbayClient()
    return client.request(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_compatibility_properties",
        params={"category_id": category_id},
        scope=TAXONOMY_SCOPE,
    )


def get_compatibility_property_values(
    category_tree_id: str,
    category_id: str,
    compatibility_property: str,
    filter: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /commerce/taxonomy/v1/category_tree/{category_tree_id}/get_compatibility_property_values

    Doc: docs/api_commerce_taxonomy_resources_category_tree_methods_getCompatibilityPropertyValues.md
    """
    params: Dict[str, Any] = {"category_id": category_id, "compatibility_property": compatibility_property}
    if filter is not None:
        params["filter"] = filter
    client = EbayClient()
    return client.request(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_compatibility_property_values",
        params=params,
        scope=TAXONOMY_SCOPE,
    )


def get_expired_categories(category_tree_id: str) -> Dict[str, Any]:
    """GET /commerce/taxonomy/v1/category_tree/{category_tree_id}/get_expired_categories

    Doc: docs/api_commerce_taxonomy_resources_category_tree_methods_getExpiredCategories.md
    """
    client = EbayClient()
    return client.request(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_expired_categories",
        scope=TAXONOMY_SCOPE,
    )
