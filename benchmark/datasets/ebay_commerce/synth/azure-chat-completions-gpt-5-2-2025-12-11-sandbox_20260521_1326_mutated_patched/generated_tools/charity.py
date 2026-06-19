from typing import Any, Dict

from .http import EbayAuth, request_json


AUTH = EbayAuth()


def get_charity_org(charity_org_id: str, marketplace_id: str) -> Dict[str, Any]:
    """GET /commerce/charity/v1/charity_org/{charity_org_id}"""
    token = AUTH.get_app_token("https://api.ebay.com/oauth/api_scope")
    if token.startswith("{"):
        return {"error": "oauth_error", "details": token}

    return request_json(
        method="GET",
        path=f"/commerce/charity/v1/charity_org/{charity_org_id}",
        headers={"X-EBAY-C-MARKETPLACE-ID": marketplace_id},
        access_token=token,
    )


def get_charity_orgs(
    *,
    marketplace_id: str,
    q: str | None = None,
    registration_ids: str | None = None,
    limit: int | None = None,
    offset: int | None = None,
) -> Dict[str, Any]:
    """GET /commerce/charity/v1/charity_org"""
    token = AUTH.get_app_token("https://api.ebay.com/oauth/api_scope")
    if token.startswith("{"):
        return {"error": "oauth_error", "details": token}

    query: Dict[str, Any] = {}
    if q is not None:
        query["q"] = q
    if registration_ids is not None:
        query["registration_ids"] = registration_ids
    if limit is not None:
        query["limit"] = limit
    if offset is not None:
        query["offset"] = offset

    return request_json(
        method="GET",
        path="/commerce/charity/v1/charity_org",
        query=query or None,
        headers={"X-EBAY-C-MARKETPLACE-ID": marketplace_id},
        access_token=token,
    )
