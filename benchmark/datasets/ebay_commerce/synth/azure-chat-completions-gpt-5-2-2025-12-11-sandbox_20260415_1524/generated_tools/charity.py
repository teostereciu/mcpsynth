from typing import Any, Dict

from .ebay_client import EbayClient


CHARITY_SCOPE_APP = "https://api.ebay.com/oauth/api_scope"


def get_charity_org(charity_org_id: str, marketplace_id: str) -> Dict[str, Any]:
    """Get details for a supported charitable organization.

    GET /commerce/charity/v1/charity_org/{charity_org_id}
    Requires X-EBAY-C-MARKETPLACE-ID (EBAY_US or EBAY_GB)
    OAuth: app token (client credentials) with https://api.ebay.com/oauth/api_scope
    """
    client = EbayClient()
    return client.request(
        "GET",
        f"/commerce/charity/v1/charity_org/{charity_org_id}",
        headers={"X-EBAY-C-MARKETPLACE-ID": marketplace_id},
        scope=CHARITY_SCOPE_APP,
        user=False,
        is_media=False,
    )


def search_charity_orgs(
    *,
    marketplace_id: str,
    q: str | None = None,
    registration_ids: str | None = None,
    limit: int | None = None,
    offset: int | None = None,
) -> Dict[str, Any]:
    """Search supported charitable organizations.

    GET /commerce/charity/v1/charity_org
    Requires X-EBAY-C-MARKETPLACE-ID.
    Provide either q or registration_ids (comma-separated), but not both.
    """
    client = EbayClient()
    params: Dict[str, Any] = {}
    if q is not None:
        params["q"] = q
    if registration_ids is not None:
        params["registration_ids"] = registration_ids
    if limit is not None:
        params["limit"] = str(limit)
    if offset is not None:
        params["offset"] = str(offset)

    return client.request(
        "GET",
        "/commerce/charity/v1/charity_org",
        params=params,
        headers={"X-EBAY-C-MARKETPLACE-ID": marketplace_id},
        scope=CHARITY_SCOPE_APP,
        user=False,
        is_media=False,
    )
