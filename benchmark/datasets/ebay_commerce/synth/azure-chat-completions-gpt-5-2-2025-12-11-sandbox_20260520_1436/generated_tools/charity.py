from typing import Any, Dict, Optional

from .ebay_client import EbayClient


APP_SCOPE = "https://api.ebay.com/oauth/api_scope"


def get_charity_org(charity_org_id: str, marketplace_id: str) -> Any:
    """GET /commerce/charity/v1/charity_org/{charity_org_id}

    Doc: docs/api_commerce_charity_resources_charity_org_methods_getCharityOrg.md
    """
    client = EbayClient()
    return client.request(
        "GET",
        f"/commerce/charity/v1/charity_org/{charity_org_id}",
        marketplace_id=marketplace_id,
        user_scope=None,
    )


def get_charity_orgs(
    marketplace_id: str,
    q: Optional[str] = None,
    registration_ids: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
) -> Any:
    """GET /commerce/charity/v1/charity_org

    Doc: docs/api_commerce_charity_resources_charity_org_methods_getCharityOrgs.md
    """
    client = EbayClient()
    params: Dict[str, Any] = {}
    if q is not None:
        params["q"] = q
    if registration_ids is not None:
        params["registration_ids"] = registration_ids
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset

    return client.request(
        "GET",
        "/commerce/charity/v1/charity_org",
        params=params or None,
        marketplace_id=marketplace_id,
        user_scope=None,
    )
