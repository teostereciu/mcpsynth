from typing import Any, Dict, Optional

from .http_client import EbayHttpClient


class CatalogTools:
    def __init__(self, client: Optional[EbayHttpClient] = None):
        self.client = client or EbayHttpClient()

    def get_product(self, epid: str, *, marketplace_id: Optional[str] = None) -> Dict[str, Any]:
        headers = {}
        if marketplace_id:
            headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
        return self.client.request(
            "GET",
            f"/commerce/catalog/v1_beta/product/{epid}",
            token_type="user",
            scope="https://api.ebay.com/oauth/api_scope/commerce.catalog.readonly",
            headers=headers,
        )

    def search_product_summaries(
        self,
        *,
        q: Optional[str] = None,
        gtin: Optional[str] = None,
        mpn: Optional[str] = None,
        category_ids: Optional[str] = None,
        aspect_filter: Optional[str] = None,
        fieldgroups: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        marketplace_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        params: Dict[str, Any] = {}
        if q is not None:
            params["q"] = q
        if gtin is not None:
            params["gtin"] = gtin
        if mpn is not None:
            params["mpn"] = mpn
        if category_ids is not None:
            params["category_ids"] = category_ids
        if aspect_filter is not None:
            params["aspect_filter"] = aspect_filter
        if fieldgroups is not None:
            params["fieldgroups"] = fieldgroups
        if limit is not None:
            params["limit"] = int(limit)
        if offset is not None:
            params["offset"] = int(offset)

        headers = {}
        if marketplace_id:
            headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id

        return self.client.request(
            "GET",
            "/commerce/catalog/v1_beta/product_summary/search",
            token_type="user",
            scope="https://api.ebay.com/oauth/api_scope/commerce.catalog.readonly",
            params=params,
            headers=headers,
        )
