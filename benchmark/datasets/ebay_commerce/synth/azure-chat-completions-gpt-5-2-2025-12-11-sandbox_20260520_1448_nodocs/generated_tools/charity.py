from typing import Any, Dict, Optional

from .ebay_http import EbayClient, compact


APP_SCOPE = "https://api.ebay.com/oauth/api_scope"


def get_charity_org(charity_org_id: str, *, marketplace_id: Optional[str] = None) -> Dict[str, Any]:
    """GET /commerce/charity/v1/charity_org/{charityOrgId}"""
    c = EbayClient()
    headers = c.build_headers(marketplace_id=marketplace_id)
    return c.request(
        "GET",
        f"/commerce/charity/v1/charity_org/{charity_org_id}",
        headers=headers,
        app_scope=APP_SCOPE,
    )


def search_charity_orgs(
    *,
    q: Optional[str] = None,
    registration_ids: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    marketplace_id: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /commerce/charity/v1/charity_org"""
    c = EbayClient()
    headers = c.build_headers(marketplace_id=marketplace_id)
    params = compact({"q": q, "registration_ids": registration_ids, "limit": limit, "offset": offset})
    return c.request(
        "GET",
        "/commerce/charity/v1/charity_org",
        params=params,
        headers=headers,
        app_scope=APP_SCOPE,
    )
