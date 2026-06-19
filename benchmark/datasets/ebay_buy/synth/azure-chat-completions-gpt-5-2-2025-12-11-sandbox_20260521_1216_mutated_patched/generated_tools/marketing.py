from typing import Any, Dict, Optional

from .ebay_client import EbayClient


class MarketingTools:
    def __init__(self, client: Optional[EbayClient] = None):
        self.client = client or EbayClient()

    def get_merchandised_products(
        self,
        *,
        category_id: str,
        metric_name: str = "BEST_SELLING",
        max_results: Optional[int] = None,
        aspect_filter: Optional[str] = None,
    ) -> Dict[str, Any]:
        params: Dict[str, Any] = {
            "category_id": category_id,
            "metric_name": metric_name,
        }
        if max_results is not None:
            params["limit"] = int(max_results)
        if aspect_filter is not None:
            params["aspect_filter"] = aspect_filter
        return self.client.request(
            "GET",
            "/buy/marketing/v1/merchandised_product",
            params=params,
            scope="https://api.ebay.com/oauth/api_scope/buy.marketing",
        )
