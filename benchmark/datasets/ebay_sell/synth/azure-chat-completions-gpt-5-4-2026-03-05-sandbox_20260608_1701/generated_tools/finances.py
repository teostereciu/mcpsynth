from typing import Any, Optional

from generated_tools.ebay_common import client


def get_transactions(
    marketplace_id: str,
    filter: Optional[str] = None,
    limit: Optional[str] = None,
    offset: Optional[str] = None,
    sort: Optional[str] = None,
) -> Any:
    return client.request(
        "GET",
        "/transaction",
        api_group="finances",
        params={"filter": filter, "limit": limit, "offset": offset, "sort": sort},
        headers={"X-EBAY-C-MARKETPLACE-ID": marketplace_id},
    )


def get_payouts(
    marketplace_id: str,
    filter: Optional[str] = None,
    limit: Optional[str] = None,
    offset: Optional[str] = None,
    sort: Optional[str] = None,
) -> Any:
    return client.request(
        "GET",
        "/payout",
        api_group="finances",
        params={"filter": filter, "limit": limit, "offset": offset, "sort": sort},
        headers={"X-EBAY-C-MARKETPLACE-ID": marketplace_id},
    )
