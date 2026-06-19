from typing import Any, Dict, Optional

from .client import EbayClient


def get_transactions(
    *,
    marketplace_id: str = "EBAY_US",
    filter: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    sort: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /transaction

    Retrieves monetary transactions (Finances API).

    Note: EU/UK sellers may require Digital Signatures; this client does not implement that.

    Doc: docs/api_finances_get-transactions.md
    """

    params: Dict[str, Any] = {}
    if filter is not None:
        params["filter"] = filter
    if limit is not None:
        params["limit"] = str(limit)
    if offset is not None:
        params["offset"] = str(offset)
    if sort is not None:
        params["sort"] = sort

    client = EbayClient()
    return client.request_json(
        "GET",
        "/sell/finances/v1/transaction",
        params=params or None,
        headers={"X-EBAY-C-MARKETPLACE-ID": marketplace_id},
    )
