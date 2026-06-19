from typing import Any, Dict, Optional

from .ebay_client import EbayClient


def search_items(
    client: EbayClient,
    *,
    q: Optional[str] = None,
    category_ids: Optional[str] = None,
    charity_ids: Optional[str] = None,
    epid: Optional[str] = None,
    gtin: Optional[str] = None,
    filter: Optional[str] = None,
    aspect_filter: Optional[str] = None,
    compatibility_filter: Optional[str] = None,
    fieldgroups: Optional[str] = None,
    sort: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    marketplace_id: Optional[str] = None,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    for k, v in {
        "q": q,
        "category_ids": category_ids,
        "charity_ids": charity_ids,
        "epid": epid,
        "gtin": gtin,
        "filter": filter,
        "aspect_filter": aspect_filter,
        "compatibility_filter": compatibility_filter,
        "fieldgroups": fieldgroups,
        "sort": sort,
        "limit": limit,
        "offset": offset,
    }.items():
        if v is not None:
            params[k] = v

    headers: Dict[str, str] = {}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx

    return client.request("GET", "/buy/browse/v1/item_summary/search", params=params, headers=headers)


def get_item(
    client: EbayClient,
    *,
    item_id: str,
    fieldgroups: Optional[str] = None,
    marketplace_id: Optional[str] = None,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if fieldgroups is not None:
        params["fieldgroups"] = fieldgroups

    headers: Dict[str, str] = {}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx

    return client.request("GET", f"/buy/browse/v1/item/{item_id}", params=params, headers=headers)
