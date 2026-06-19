from typing import Any, Dict, Optional

from .ebay_client import EbayClient


def get_events(
    client: EbayClient,
    *,
    marketplace_id: str,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset

    headers: Dict[str, str] = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx

    return client.request("GET", "/buy/deal/v1/event", params=params, headers=headers)
