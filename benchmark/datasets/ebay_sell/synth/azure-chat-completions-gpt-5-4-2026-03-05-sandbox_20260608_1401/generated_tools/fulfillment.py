from typing import Any, Optional

from .common import client

API_PATH = "/sell/fulfillment/v1"


def get_orders(
    field_groups: Optional[str] = None,
    filter: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    order_ids: Optional[str] = None,
) -> Any:
    return client.request(
        API_PATH,
        "GET",
        "/order",
        params={
            "fieldGroups": field_groups,
            "filter": filter,
            "limit": limit,
            "offset": offset,
            "orderIds": order_ids,
        },
    )


def get_order(order_id: str, field_groups: Optional[str] = None) -> Any:
    return client.request(API_PATH, "GET", f"/order/{order_id}", params={"fieldGroups": field_groups})


def create_shipping_fulfillment(order_id: str, body: dict) -> Any:
    return client.request(
        API_PATH,
        "POST",
        f"/order/{order_id}/shipping_fulfillment",
        json_body=body,
        headers={"Content-Type": "application/json"},
    )


def get_shipping_fulfillments(order_id: str) -> Any:
    return client.request(API_PATH, "GET", f"/order/{order_id}/shipping_fulfillment")
