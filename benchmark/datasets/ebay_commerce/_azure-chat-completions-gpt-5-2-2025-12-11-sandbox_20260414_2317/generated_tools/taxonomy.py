"""Tools for eBay Commerce Taxonomy API."""

from __future__ import annotations

from typing import Any, Dict, Optional

from .http import request_json


def get_default_category_tree_id(marketplace_id: str) -> Dict[str, Any]:
    """Get the default category tree ID for a marketplace.

    Docs: GET /commerce/taxonomy/v1/get_default_category_tree_id?marketplace_id=...
    Auth: Application token
    """

    status, data, _ = request_json(
        "GET",
        "/commerce/taxonomy/v1/get_default_category_tree_id",
        params={"marketplace_id": marketplace_id},
        user_auth=False,
        media=False,
    )
    return data if status < 400 else data


def get_category_tree(category_tree_id: str) -> Dict[str, Any]:
    """Get a full category tree.

    Docs: GET /commerce/taxonomy/v1/category_tree/{category_tree_id}
    Auth: Application token
    """

    status, data, _ = request_json(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}",
        user_auth=False,
        media=False,
    )
    return data


def get_category_subtree(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    """Get a subtree of a category tree.

    Docs: GET /commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_subtree?category_id=...
    Auth: Application token
    """

    status, data, _ = request_json(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_subtree",
        params={"category_id": category_id},
        user_auth=False,
        media=False,
    )
    return data


def get_category_suggestions(category_tree_id: str, q: str) -> Dict[str, Any]:
    """Get category suggestions for a query.

    Docs: GET /commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_suggestions?q=...
    Auth: Application token
    """

    status, data, _ = request_json(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_suggestions",
        params={"q": q},
        user_auth=False,
        media=False,
    )
    return data


def get_item_aspects_for_category(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    """Get required/recommended item aspects for a category.

    Docs: GET /commerce/taxonomy/v1/category_tree/{category_tree_id}/get_item_aspects_for_category?category_id=...
    Auth: Application token
    """

    status, data, _ = request_json(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_item_aspects_for_category",
        params={"category_id": category_id},
        user_auth=False,
        media=False,
    )
    return data


def get_compatibility_properties(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    """Get compatibility properties for a category.

    Docs: GET /commerce/taxonomy/v1/category_tree/{category_tree_id}/get_compatibility_properties?category_id=...
    Auth: Application token
    """

    status, data, _ = request_json(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_compatibility_properties",
        params={"category_id": category_id},
        user_auth=False,
        media=False,
    )
    return data


def get_compatibility_property_values(
    category_tree_id: str,
    category_id: str,
    compatibility_property: str,
    *,
    filter: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
) -> Dict[str, Any]:
    """Get compatibility property values.

    Docs: GET /commerce/taxonomy/v1/category_tree/{category_tree_id}/get_compatibility_property_values
    Auth: Application token
    """

    params: Dict[str, Any] = {"category_id": category_id, "compatibility_property": compatibility_property}
    if filter is not None:
        params["filter"] = filter
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset

    status, data, _ = request_json(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_compatibility_property_values",
        params=params,
        user_auth=False,
        media=False,
    )
    return data


def get_expired_categories(category_tree_id: str, *, category_ids: Optional[str] = None) -> Dict[str, Any]:
    """Get expired categories in a category tree.

    Docs: GET /commerce/taxonomy/v1/category_tree/{category_tree_id}/get_expired_categories
    Auth: Application token
    """

    params: Dict[str, Any] = {}
    if category_ids is not None:
        params["category_ids"] = category_ids

    status, data, _ = request_json(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_expired_categories",
        params=params or None,
        user_auth=False,
        media=False,
    )
    return data


def fetch_item_aspects(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    """(Legacy) Fetch item aspects for a category.

    Docs: GET /commerce/taxonomy/v1/category_tree/{category_tree_id}/fetch_item_aspects?category_id=...
    Auth: Application token
    """

    status, data, _ = request_json(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/fetch_item_aspects",
        params={"category_id": category_id},
        user_auth=False,
        media=False,
    )
    return data
