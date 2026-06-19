from typing import Any, Dict, Optional

from generated_tools.catalog import client


def get_charity_org(charity_org_id: str, marketplace_id: str) -> Dict[str, Any]:
    return client.request(
        "GET",
        f"/commerce/charity/v1/charity_org/{charity_org_id}",
        token_type="app",
        headers={"X-EBAY-C-MARKETPLACE-ID": marketplace_id},
    )


def search_charity_orgs(
    marketplace_id: str,
    q: Optional[str] = None,
    registration_ids: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    for key, value in {
        "q": q,
        "registration_ids": registration_ids,
        "limit": limit,
        "offset": offset,
    }.items():
        if value is not None:
            params[key] = value
    return client.request(
        "GET",
        "/commerce/charity/v1/charity_org",
        token_type="app",
        params=params,
        headers={"X-EBAY-C-MARKETPLACE-ID": marketplace_id},
    )
