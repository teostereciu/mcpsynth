from typing import Any, Dict

from .http_client import EbayHTTP


CHARITY_SCOPE_APP = "https://api.ebay.com/oauth/api_scope"


def get_charity_org(charity_org_id: str, *, marketplace_id: str) -> Dict[str, Any]:
    """GET /commerce/charity/v1/charity_org/{charity_org_id}

    Doc: docs/api_commerce_charity_resources_charity_org_methods_getCharityOrg.md
    """
    http = EbayHTTP()
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    return http.request(
        "GET",
        http.oauth.api_base,
        f"/commerce/charity/v1/charity_org/{charity_org_id}",
        scope=CHARITY_SCOPE_APP,
        headers=headers,
    )


def search_charity_orgs(
    *,
    marketplace_id: str,
    q: str | None = None,
    registration_ids: str | None = None,
    limit: int | None = None,
    offset: int | None = None,
) -> Dict[str, Any]:
    """GET /commerce/charity/v1/charity_org

    Doc: docs/api_commerce_charity_resources_charity_org_methods_getCharityOrgs.md
    """
    http = EbayHTTP()
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    params: Dict[str, Any] = {}
    if q is not None:
        params["q"] = q
    if registration_ids is not None:
        params["registration_ids"] = registration_ids
    if limit is not None:
        params["limit"] = str(limit)
    if offset is not None:
        params["offset"] = str(offset)

    return http.request(
        "GET",
        http.oauth.api_base,
        "/commerce/charity/v1/charity_org",
        scope=CHARITY_SCOPE_APP,
        headers=headers,
        params=params,
    )
