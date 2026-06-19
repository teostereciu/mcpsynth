from typing import Any, Optional

from generated_tools.ebay_common import client


def get_orders(
    field_groups: Optional[str] = None,
    filter: Optional[str] = None,
    limit: Optional[str] = None,
    offset: Optional[str] = None,
    order_ids: Optional[str] = None,
) -> Any:
    return client.request(
        "GET",
        "/order",
        api_group="fulfillment",
        params={
            "fieldGroups": field_groups,
            "filter": filter,
            "limit": limit,
            "offset": offset,
            "orderIds": order_ids,
        },
    )


def get_order(order_id: str, field_groups: Optional[str] = None) -> Any:
    return client.request(
        "GET",
        f"/order/{order_id}",
        api_group="fulfillment",
        params={"fieldGroups": field_groups},
    )
