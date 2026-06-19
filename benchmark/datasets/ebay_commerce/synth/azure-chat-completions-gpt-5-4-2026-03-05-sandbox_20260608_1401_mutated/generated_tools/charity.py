from typing import Any, Dict, Optional

from .ebay_common import client


def get_charity_org(charity_org_id: str, marketplace_id: str) -> Dict[str, Any]:
    return client.request(
        "GET",
        f"/commerce/charity/v1/charity_org/{charity_org_id}",
        token_type="app",
        headers={"X-EBAY-C-MARKETPLACE-ID": marketplace_id},
    )


def search_charity_orgs(
    marketplace_id: str,
    query: Optional[str] = None,
    registration_ids: Optional[str] = None,
    page_size: Optional[int] = None,
    offset: Optional[int] = None,
) -> Dict[str, Any]:
    return client.request(
        "GET",
        "/commerce/charity/v1/charity_org",
        token_type="app",
        headers={"X-EBAY-C-MARKETPLACE-ID": marketplace_id},
        params={
            "query": query,
            "registration_ids": registration_ids,
            "page_size": page_size,
            "offset": offset,
        },
    )
