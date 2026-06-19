from typing import Any, Dict, Optional

from .ebay_client import EbayClient, omit_none


client = EbayClient()


def fulfillment_get_orders(
    filter: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    order_ids: Optional[str] = None,
    field_groups: Optional[str] = None,
) -> Dict[str, Any]:
    params = omit_none({"filter": filter, "limit": limit, "offset": offset, "orderIds": order_ids, "fieldGroups": field_groups})
    return client.request("GET", "/sell/fulfillment/v1/order", params=params)


def fulfillment_get_order(order_id: str, field_groups: Optional[str] = None) -> Dict[str, Any]:
    params = omit_none({"fieldGroups": field_groups})
    return client.request("GET", f"/sell/fulfillment/v1/order/{order_id}", params=params)


def fulfillment_get_shipping_fulfillments(order_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/sell/fulfillment/v1/order/{order_id}/shipping_fulfillment")


def fulfillment_create_shipping_fulfillment(order_id: str, fulfillment: Dict[str, Any]) -> Dict[str, Any]:
    return client.request("POST", f"/sell/fulfillment/v1/order/{order_id}/shipping_fulfillment", json_body=fulfillment)
