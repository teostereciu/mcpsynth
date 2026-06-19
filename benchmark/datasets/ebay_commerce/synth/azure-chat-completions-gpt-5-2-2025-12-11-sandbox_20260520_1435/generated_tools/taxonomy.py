from typing import Any, Dict, Optional

from .http_client import EbayHTTP


TAXONOMY_SCOPE_APP = "https://api.ebay.com/oauth/api_scope"


def get_default_category_tree_id(marketplace_id: str) -> Dict[str, Any]:
    """GET /commerce/taxonomy/v1/get_default_category_tree_id

    Doc: docs/api_commerce_taxonomy_resources_category_tree_methods_getDefaultCategoryTreeId.md
    """
    http = EbayHTTP()
    return http.request(
        "GET",
        http.oauth.api_base,
        "/commerce/taxonomy/v1/get_default_category_tree_id",
        scope=TAXONOMY_SCOPE_APP,
        params={"marketplace_id": marketplace_id},
    )


def get_category_tree(category_tree_id: str) -> Dict[str, Any]:
    """GET /commerce/taxonomy/v1/category_tree/{category_tree_id}

    Doc: docs/api_commerce_taxonomy_resources_category_tree_methods_getCategoryTree.md
    """
    http = EbayHTTP()
    return http.request(
        "GET",
        http.oauth.api_base,
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}",
        scope=TAXONOMY_SCOPE_APP,
    )


def get_category_subtree(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    """GET /commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_subtree

    Doc: docs/api_commerce_taxonomy_resources_category_tree_methods_getCategorySubtree.md
    """
    http = EbayHTTP()
    return http.request(
        "GET",
        http.oauth.api_base,
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_subtree",
        scope=TAXONOMY_SCOPE_APP,
        params={"category_id": category_id},
    )


def get_category_suggestions(category_tree_id: str, q: str) -> Dict[str, Any]:
    """GET /commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_suggestions

    Doc: docs/api_commerce_taxonomy_resources_category_tree_methods_getCategorySuggestions.md
    """
    http = EbayHTTP()
    return http.request(
        "GET",
        http.oauth.api_base,
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_suggestions",
        scope=TAXONOMY_SCOPE_APP,
        params={"q": q},
    )


def get_item_aspects_for_category(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    """GET /commerce/taxonomy/v1/category_tree/{category_tree_id}/get_item_aspects_for_category

    Doc: docs/api_commerce_taxonomy_resources_category_tree_methods_getItemAspectsForCategory.md
    """
    http = EbayHTTP()
    return http.request(
        "GET",
        http.oauth.api_base,
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_item_aspects_for_category",
        scope=TAXONOMY_SCOPE_APP,
        params={"category_id": category_id},
    )


def fetch_item_aspects(category_tree_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    """POST /commerce/taxonomy/v1/category_tree/{category_tree_id}/fetch_item_aspects

    Doc: docs/api_commerce_taxonomy_resources_category_tree_methods_fetchItemAspects.md
    """
    http = EbayHTTP()
    return http.request(
        "POST",
        http.oauth.api_base,
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/fetch_item_aspects",
        scope=TAXONOMY_SCOPE_APP,
        json=payload,
        headers={"Content-Type": "application/json"},
    )


def get_expired_categories(category_tree_id: str) -> Dict[str, Any]:
    """GET /commerce/taxonomy/v1/category_tree/{category_tree_id}/get_expired_categories

    Doc: docs/api_commerce_taxonomy_resources_category_tree_methods_getExpiredCategories.md
    """
    http = EbayHTTP()
    return http.request(
        "GET",
        http.oauth.api_base,
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_expired_categories",
        scope=TAXONOMY_SCOPE_APP,
    )


def get_compatibility_properties(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    """GET /commerce/taxonomy/v1/category_tree/{category_tree_id}/get_compatibility_properties

    Doc: docs/api_commerce_taxonomy_resources_category_tree_methods_getCompatibilityProperties.md
    """
    http = EbayHTTP()
    return http.request(
        "GET",
        http.oauth.api_base,
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_compatibility_properties",
        scope=TAXONOMY_SCOPE_APP,
        params={"category_id": category_id},
    )


def get_compatibility_property_values(
    category_tree_id: str,
    category_id: str,
    compatibility_property: str,
    *,
    filter: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /commerce/taxonomy/v1/category_tree/{category_tree_id}/get_compatibility_property_values

    Doc: docs/api_commerce_taxonomy_resources_category_tree_methods_getCompatibilityPropertyValues.md
    """
    http = EbayHTTP()
    params: Dict[str, Any] = {"category_id": category_id, "compatibility_property": compatibility_property}
    if filter is not None:
        params["filter"] = filter
    return http.request(
        "GET",
        http.oauth.api_base,
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_compatibility_property_values",
        scope=TAXONOMY_SCOPE_APP,
        params=params,
    )
