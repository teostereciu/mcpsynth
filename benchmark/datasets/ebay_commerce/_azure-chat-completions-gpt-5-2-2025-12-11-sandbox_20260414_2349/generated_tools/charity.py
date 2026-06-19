from __future__ import annotations

from typing import Any, Dict, Optional

from .http import commerce_base_url, request_json


API_SCOPE = "https://api.ebay.com/oauth/api_scope"


def search_charity_orgs(
    *,
    marketplace_id: str = "EBAY_US",
    q: Optional[str] = None,
    registration_ids: Optional[str] = None,
    limit: int = 20,
    offset: int = 0,
) -> Dict[str, Any]:
    """GET /commerce/charity/v1/charity_org

    Provide either q or registration_ids (comma-separated).
    Requires X-EBAY-C-MARKETPLACE-ID header.
    """
    params: Dict[str, Any] = {"limit": limit, "offset": offset}
    if q is not None:
        params["q"] = q
    if registration_ids is not None:
        params["registration_ids"] = registration_ids

    return request_json(
        "GET",
        commerce_base_url(),
        "/commerce/charity/v1/charity_org/",
        params=params,
        user_auth=False,
        scope=API_SCOPE,
        extra_headers={"X-EBAY-C-MARKETPLACE-ID": marketplace_id},
    )


def get_charity_org(charity_org_id: str, *, marketplace_id: str = "EBAY_US") -> Dict[str, Any]:
    """GET /commerce/charity/v1/charity_org/{charity_org_id}"""
    return request_json(
        "GET",
        commerce_base_url(),
        f"/commerce/charity/v1/charity_org/{charity_org_id}",
        user_auth=False,
        scope=API_SCOPE,
        extra_headers={"X-EBAY-C-MARKETPLACE-ID": marketplace_id},
    )
