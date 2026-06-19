from typing import Any, Dict, Optional

from .http_client import EbayClient


CHARITY_SCOPE = "https://api.ebay.com/oauth/api_scope"


def get_charity_org(charity_org_id: str, marketplace_id: str) -> Dict[str, Any]:
    """GET /commerce/charity/v1/charity_org/{charity_org_id}

    Doc: docs/api_commerce_charity_resources_charity_org_methods_getCharityOrg.md
    """
    client = EbayClient()
    return client.request(
        "GET",
        f"/commerce/charity/v1/charity_org/{charity_org_id}",
        marketplace_id=marketplace_id,
        scope=CHARITY_SCOPE,
        user_token=False,
    )


def get_charity_orgs(
    marketplace_id: str,
    q: Optional[str] = None,
    registration_ids: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
) -> Dict[str, Any]:
    """GET /commerce/charity/v1/charity_org

    Doc: docs/api_commerce_charity_resources_charity_org_methods_getCharityOrgs.md
    """
    params: Dict[str, Any] = {}
    if q is not None:
        params["q"] = q
    if registration_ids is not None:
        params["registration_ids"] = registration_ids
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset

    client = EbayClient()
    return client.request(
        "GET",
        "/commerce/charity/v1/charity_org",
        params=params or None,
        marketplace_id=marketplace_id,
        scope=CHARITY_SCOPE,
        user_token=False,
    )
