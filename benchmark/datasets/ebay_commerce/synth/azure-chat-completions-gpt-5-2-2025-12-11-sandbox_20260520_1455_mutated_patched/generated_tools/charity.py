from __future__ import annotations

from typing import Any, Dict

from .ebay_client import EbayClient


def search_charity_orgs(
    marketplace_id: str,
    query: str | None = None,
    registration_ids: str | None = None,
    page_size: int | None = None,
    offset: int | None = None,
) -> Dict[str, Any]:
    """GET /charity_org

    Provide either `query` OR `registration_ids` (comma-separated), not both.

    OAuth scope: https://api.ebay.com/oauth/api_scope (app token)
    """
    client = EbayClient.for_standard_api(user_scoped=False)
    params: Dict[str, Any] = {}
    if query is not None:
        params["q"] = query
    if registration_ids is not None:
        params["registration_ids"] = registration_ids
    if page_size is not None:
        params["limit"] = page_size
    if offset is not None:
        params["offset"] = offset

    return client.request(
        "GET",
        "/commerce/charity/v1/charity_org",
        headers={"X-EBAY-C-MARKETPLACE-ID": marketplace_id},
        params=params,
    )


def get_charity_org(charity_org_id: str, marketplace_id: str) -> Dict[str, Any]:
    """GET /charity_org/{charity_org_id}

    OAuth scope: https://api.ebay.com/oauth/api_scope (app token)
    """
    client = EbayClient.for_standard_api(user_scoped=False)
    return client.request(
        "GET",
        f"/commerce/charity/v1/charity_org/{charity_org_id}",
        headers={"X-EBAY-C-MARKETPLACE-ID": marketplace_id},
    )
