from typing import Any, Optional

from .common import client

API_PATH = "/sell/finances/v1"


def get_transactions(
    marketplace_id: str = "EBAY_US",
    filter: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    sort: Optional[str] = None,
) -> Any:
    return client.request(
        API_PATH,
        "GET",
        "/transaction",
        params={"filter": filter, "limit": limit, "offset": offset, "sort": sort},
        headers={"X-EBAY-C-MARKETPLACE-ID": marketplace_id},
    )


def get_payouts(
    marketplace_id: str = "EBAY_US",
    filter: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    sort: Optional[str] = None,
) -> Any:
    return client.request(
        API_PATH,
        "GET",
        "/payout",
        params={"filter": filter, "limit": limit, "offset": offset, "sort": sort},
        headers={"X-EBAY-C-MARKETPLACE-ID": marketplace_id},
    )
