from typing import Any, Optional

from generated_tools.common import clean_params, client


def get_payouts(
    marketplace_id: str,
    filter: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    sort_by: Optional[str] = None,
) -> Any:
    return client.request(
        "GET",
        "/sell/finances/v1/payout",
        params=clean_params(filter=filter, limit=limit, offset=offset, sort_by=sort_by),
        headers={"X-EBAY-C-MARKETPLACE-ID": marketplace_id},
    )


def get_transactions(
    marketplace_id: str,
    filter: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    sort_by: Optional[str] = None,
) -> Any:
    return client.request(
        "GET",
        "/sell/finances/v1/transaction",
        params=clean_params(filter=filter, limit=limit, offset=offset, sort_by=sort_by),
        headers={"X-EBAY-C-MARKETPLACE-ID": marketplace_id},
    )


def get_transaction_summary(marketplace_id: str, filter: str) -> Any:
    return client.request(
        "GET",
        "/sell/finances/v1/transaction_summary",
        params=clean_params(filter=filter),
        headers={"X-EBAY-C-MARKETPLACE-ID": marketplace_id},
    )
