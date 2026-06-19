from typing import Any, Dict

from .ebay_client import EbayClient


CHARITY_SCOPE = "https://api.ebay.com/oauth/api_scope"


def get_charity_org(charity_org_id: str, marketplace_id: str) -> Dict[str, Any]:
    """GET /commerce/charity/v1/charity_org/{charity_org_id}"""
    client = EbayClient()
    return client.request(
        "GET",
        client.api_base,
        f"/commerce/charity/v1/charity_org/{charity_org_id}",
        headers={"X-EBAY-C-MARKETPLACE-ID": marketplace_id},
        auth="app",
        scope=CHARITY_SCOPE,
    )


def search_charity_orgs(
    *,
    marketplace_id: str,
    query: str | None = None,
    registration_ids: str | None = None,
    page_size: int | None = None,
    offset: int | None = None,
) -> Dict[str, Any]:
    """GET /commerce/charity/v1/charity_org"""
    client = EbayClient()
    params: Dict[str, Any] = {}
    if query is not None:
        params["query"] = query
    if registration_ids is not None:
        params["registration_ids"] = registration_ids
    if page_size is not None:
        params["page_size"] = page_size
    if offset is not None:
        params["offset"] = offset

    return client.request(
        "GET",
        client.api_base,
        "/commerce/charity/v1/charity_org",
        params=params,
        headers={"X-EBAY-C-MARKETPLACE-ID": marketplace_id},
        auth="app",
        scope=CHARITY_SCOPE,
    )
