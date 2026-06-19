from typing import Any, Dict, Optional

from .ebay_client import EbayClient


class DealTools:
    def __init__(self, client: Optional[EbayClient] = None):
        self.client = client or EbayClient()

    def get_deal_items(
        self,
        *,
        category_ids: Optional[str] = None,
        commissionable: Optional[bool] = None,
        delivery_country: Optional[str] = None,
        max_results: Optional[int] = None,
        skip: Optional[int] = None,
        marketplace_id: Optional[str] = None,
        enduserctx: Optional[str] = None,
    ) -> Dict[str, Any]:
        params: Dict[str, Any] = {}
        if category_ids is not None:
            params["category_ids"] = category_ids
        if commissionable is not None:
            params["commissionable"] = str(bool(commissionable)).lower()
        if delivery_country is not None:
            params["delivery_country"] = delivery_country
        if max_results is not None:
            params["max_results"] = int(max_results)
        if skip is not None:
            params["skip"] = int(skip)

        headers: Dict[str, str] = {}
        if marketplace_id is not None:
            headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
        if enduserctx is not None:
            headers["X-EBAY-C-ENDUSERCTX"] = enduserctx

        return self.client.request(
            "GET",
            "/buy/deal/v1/deal_item",
            params=params,
            headers=headers,
            scope="https://api.ebay.com/oauth/api_scope/buy.deal",
        )

    def get_events(
        self,
        *,
        max_results: Optional[int] = None,
        skip: Optional[int] = None,
        marketplace_id: Optional[str] = None,
        enduserctx: Optional[str] = None,
    ) -> Dict[str, Any]:
        params: Dict[str, Any] = {}
        if max_results is not None:
            params["max_results"] = int(max_results)
        if skip is not None:
            params["skip"] = int(skip)

        headers: Dict[str, str] = {}
        if marketplace_id is not None:
            headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
        if enduserctx is not None:
            headers["X-EBAY-C-ENDUSERCTX"] = enduserctx

        return self.client.request(
            "GET",
            "/buy/deal/v1/event",
            params=params,
            headers=headers,
            scope="https://api.ebay.com/oauth/api_scope/buy.deal",
        )

    def get_event(
        self,
        event_id: str,
        *,
        marketplace_id: Optional[str] = None,
        enduserctx: Optional[str] = None,
    ) -> Dict[str, Any]:
        headers: Dict[str, str] = {}
        if marketplace_id is not None:
            headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
        if enduserctx is not None:
            headers["X-EBAY-C-ENDUSERCTX"] = enduserctx
        return self.client.request(
            "GET",
            f"/buy/deal/v1/event/{event_id}",
            headers=headers,
            scope="https://api.ebay.com/oauth/api_scope/buy.deal",
        )

    def get_event_items(
        self,
        *,
        event_ids: str,
        category_ids: Optional[str] = None,
        delivery_country: Optional[str] = None,
        max_results: Optional[int] = None,
        skip: Optional[int] = None,
        marketplace_id: Optional[str] = None,
        enduserctx: Optional[str] = None,
    ) -> Dict[str, Any]:
        params: Dict[str, Any] = {"event_ids": event_ids}
        if category_ids is not None:
            params["category_ids"] = category_ids
        if delivery_country is not None:
            params["delivery_country"] = delivery_country
        if max_results is not None:
            params["max_results"] = int(max_results)
        if skip is not None:
            params["skip"] = int(skip)

        headers: Dict[str, str] = {}
        if marketplace_id is not None:
            headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
        if enduserctx is not None:
            headers["X-EBAY-C-ENDUSERCTX"] = enduserctx

        return self.client.request(
            "GET",
            "/buy/deal/v1/event_item",
            params=params,
            headers=headers,
            scope="https://api.ebay.com/oauth/api_scope/buy.deal",
        )
