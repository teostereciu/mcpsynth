from typing import Any, Dict, Optional

from .ebay_client import EbayClient


def get_category_policies(
    marketplace_id: str,
    category_id: str,
) -> Dict[str, Any]:
    """GET /category_tree/{category_tree_id}/get_category_policies

    Note: This wrapper uses the category_tree_id as marketplace_id for convenience only if docs differ.
    Prefer using get_item_condition_policies etc. if needed.
    """
    client = EbayClient()
    return client.request(
        "GET",
        f"/sell/metadata/v1/category_tree/{marketplace_id}/get_category_policies",
        params={"category_id": category_id},
    )


def get_currencies() -> Dict[str, Any]:
    """GET /currency"""
    client = EbayClient()
    return client.request("GET", "/sell/metadata/v1/currency")


def get_item_condition_policies(marketplace_id: str, category_id: str) -> Dict[str, Any]:
    """GET /marketplace/{marketplace_id}/get_item_condition_policies"""
    client = EbayClient()
    return client.request(
        "GET",
        f"/sell/metadata/v1/marketplace/{marketplace_id}/get_item_condition_policies",
        params={"category_id": category_id},
    )
