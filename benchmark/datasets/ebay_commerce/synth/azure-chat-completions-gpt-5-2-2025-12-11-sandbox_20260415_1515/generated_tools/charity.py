from typing import Any, Dict, Optional

from .http_client import EbayHttpClient


class CharityTools:
    def __init__(self, client: Optional[EbayHttpClient] = None):
        self.client = client or EbayHttpClient()

    def get_charity_orgs(
        self,
        *,
        marketplace_id: str,
        q: Optional[str] = None,
        registration_ids: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> Dict[str, Any]:
        params: Dict[str, Any] = {}
        if q is not None:
            params["q"] = q
        if registration_ids is not None:
            params["registration_ids"] = registration_ids
        if limit is not None:
            params["limit"] = int(limit)
        if offset is not None:
            params["offset"] = int(offset)

        return self.client.request(
            "GET",
            "/commerce/charity/v1/charity_org",
            token_type="app",
            scope="https://api.ebay.com/oauth/api_scope",
            params=params,
            headers={"X-EBAY-C-MARKETPLACE-ID": marketplace_id},
        )

    def get_charity_org(self, charity_org_id: str, *, marketplace_id: str) -> Dict[str, Any]:
        return self.client.request(
            "GET",
            f"/commerce/charity/v1/charity_org/{charity_org_id}",
            token_type="app",
            scope="https://api.ebay.com/oauth/api_scope",
            headers={"X-EBAY-C-MARKETPLACE-ID": marketplace_id},
        )
