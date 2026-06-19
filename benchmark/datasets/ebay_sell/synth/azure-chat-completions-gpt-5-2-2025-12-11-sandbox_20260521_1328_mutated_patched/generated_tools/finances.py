from typing import Any, Dict, Optional

from .client import EbayClient


def get_transactions(
    *,
    marketplace_id: str = "EBAY_US",
    filter: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    sort_by: Optional[str] = None,
    client: Optional[EbayClient] = None,
) -> Dict[str, Any]:
    """GET /transaction

    Retrieve monetary transactions (Finances API). Note: EU/UK sellers may require digital signatures.
    """
    c = client or EbayClient()
    params: Dict[str, Any] = {}
    if filter is not None:
        params["filter"] = filter
    if limit is not None:
        params["limit"] = str(limit)
    if offset is not None:
        params["offset"] = str(offset)
    if sort_by is not None:
        params["sort"] = sort_by

    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    return c.request(
        "GET",
        "/sell/finances/v1/transaction",
        params=params or None,
        headers=headers,
    )
