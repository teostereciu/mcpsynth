"""Tools for eBay Commerce Taxonomy API."""

from __future__ import annotations

from typing import Any, Dict, Optional

from .http import EbayApiError, error_dict, get_api_base_url, request_json


def get_default_category_tree_id(marketplace_id: str) -> Dict[str, Any]:
    """Get the default category tree ID for a marketplace.

    Args:
        marketplace_id: e.g. "EBAY_US"
    """
    try:
        return request_json(
            method="GET",
            base_url=get_api_base_url(),
            path="/commerce/taxonomy/v1/get_default_category_tree_id",
            params={"marketplace_id": marketplace_id},
            user_auth=False,
        )
    except EbayApiError as e:
        return error_dict(e)


def get_category_tree(category_tree_id: str, accept_encoding: Optional[str] = "gzip") -> Dict[str, Any]:
    """Retrieve the complete category tree."""
    try:
        headers = {"Accept-Encoding": accept_encoding} if accept_encoding else None
        return request_json(
            method="GET",
            base_url=get_api_base_url(),
            path=f"/commerce/taxonomy/v1/category_tree/{category_tree_id}",
            headers=headers,
            user_auth=False,
        )
    except EbayApiError as e:
        return error_dict(e)


def get_category_subtree(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    """Get a subtree below a category."""
    try:
        return request_json(
            method="GET",
            base_url=get_api_base_url(),
            path=f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_subtree",
            params={"category_id": category_id},
            user_auth=False,
        )
    except EbayApiError as e:
        return error_dict(e)


def get_category_suggestions(category_tree_id: str, q: str) -> Dict[str, Any]:
    """Get category suggestions for a query string."""
    try:
        return request_json(
            method="GET",
            base_url=get_api_base_url(),
            path=f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_suggestions",
            params={"q": q},
            user_auth=False,
        )
    except EbayApiError as e:
        return error_dict(e)


def get_item_aspects_for_category(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    """Get required/recommended aspects for a category."""
    try:
        return request_json(
            method="GET",
            base_url=get_api_base_url(),
            path=f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_item_aspects_for_category",
            params={"category_id": category_id},
            user_auth=False,
        )
    except EbayApiError as e:
        return error_dict(e)


def get_compatibility_properties(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    """Get compatibility properties for a category."""
    try:
        return request_json(
            method="GET",
            base_url=get_api_base_url(),
            path=f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_compatibility_properties",
            params={"category_id": category_id},
            user_auth=False,
        )
    except EbayApiError as e:
        return error_dict(e)


def get_compatibility_property_values(
    category_tree_id: str,
    category_id: str,
    compatibility_property: str,
    filter: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
) -> Dict[str, Any]:
    """Get compatibility property values for a property (e.g., Make, Model)."""
    try:
        params: Dict[str, Any] = {"category_id": category_id, "compatibility_property": compatibility_property}
        if filter:
            params["filter"] = filter
        if limit is not None:
            params["limit"] = limit
        if offset is not None:
            params["offset"] = offset
        return request_json(
            method="GET",
            base_url=get_api_base_url(),
            path=f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_compatibility_property_values",
            params=params,
            user_auth=False,
        )
    except EbayApiError as e:
        return error_dict(e)


def get_expired_categories(category_tree_id: str, category_ids: str) -> Dict[str, Any]:
    """Get expired categories for a category tree.

    Args:
        category_ids: comma-separated list of category IDs
    """
    try:
        return request_json(
            method="GET",
            base_url=get_api_base_url(),
            path=f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_expired_categories",
            params={"category_ids": category_ids},
            user_auth=False,
        )
    except EbayApiError as e:
        return error_dict(e)


def fetch_item_aspects(category_tree_id: str, category_ids: str) -> Dict[str, Any]:
    """Bulk fetch item aspects for multiple categories.

    Args:
        category_ids: comma-separated list of category IDs
    """
    try:
        return request_json(
            method="GET",
            base_url=get_api_base_url(),
            path=f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/fetch_item_aspects",
            params={"category_ids": category_ids},
            user_auth=False,
        )
    except EbayApiError as e:
        return error_dict(e)
