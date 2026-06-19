from typing import Any, Dict, Optional

from .ebay_client import EbayClient


class FulfillmentTools:
    def __init__(self, client: Optional[EbayClient] = None):
        self.client = client or EbayClient()

    def get_orders(self, filter: Optional[str] = None, limit: int = 50, offset: int = 0, sort: Optional[str] = None) -> Dict[str, Any]:
        params: Dict[str, Any] = {"limit": limit, "offset": offset}
        if filter:
            params["filter"] = filter
        if sort:
            params["sort"] = sort
        return self.client.request("GET", "/sell/fulfillment/v1/order", params=params)

    def get_order(self, order_id: str) -> Dict[str, Any]:
        return self.client.request("GET", f"/sell/fulfillment/v1/order/{order_id}")

    def get_shipping_fulfillments(self, order_id: str) -> Dict[str, Any]:
        return self.client.request("GET", f"/sell/fulfillment/v1/order/{order_id}/shipping_fulfillment")

    def create_shipping_fulfillment(self, order_id: str, fulfillment: Dict[str, Any]) -> Dict[str, Any]:
        return self.client.request(
            "POST",
            f"/sell/fulfillment/v1/order/{order_id}/shipping_fulfillment",
            json=fulfillment,
        )
