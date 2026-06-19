from typing import Any, Optional
from urllib.parse import quote

from generated_tools.common import clean_params, client


def get_orders(
    fieldGroups: Optional[str] = None,
    filter: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    orderIds: Optional[str] = None,
) -> Any:
    return client.request(
        "GET",
        "/sell/fulfillment/v1/order",
        params=clean_params(fieldGroups=fieldGroups, filter=filter, limit=limit, offset=offset, orderIds=orderIds),
    )


def get_order(orderId: str, fieldGroups: Optional[str] = None) -> Any:
    return client.request(
        "GET",
        f"/sell/fulfillment/v1/order/{quote(orderId, safe='')}",
        params=clean_params(fieldGroups=fieldGroups),
    )
