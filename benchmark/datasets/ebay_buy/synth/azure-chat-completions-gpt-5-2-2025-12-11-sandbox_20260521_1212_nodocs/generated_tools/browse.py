from typing import Any, Dict, Optional

from .ebay_client import EbayClient


def search_items(
    client: EbayClient,
    *,
    q: Optional[str] = None,
    category_ids: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    sort: Optional[str] = None,
    filter: Optional[str] = None,
    fieldgroups: Optional[str] = None,
    aspect_filter: Optional[str] = None,
    epn_category_id: Optional[str] = None,
    charity_ids: Optional[str] = None,
    auto_correct: Optional[bool] = None,
    compatibility_filter: Optional[str] = None,
    buyer_postal_code: Optional[str] = None,
    x_ebay_c_marketplace_id: str = "EBAY_US",
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if q is not None:
        params["q"] = q
    if category_ids is not None:
        params["category_ids"] = category_ids
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    if sort is not None:
        params["sort"] = sort
    if filter is not None:
        params["filter"] = filter
    if fieldgroups is not None:
        params["fieldgroups"] = fieldgroups
    if aspect_filter is not None:
        params["aspect_filter"] = aspect_filter
    if epn_category_id is not None:
        params["epn_category_id"] = epn_category_id
    if charity_ids is not None:
        params["charity_ids"] = charity_ids
    if auto_correct is not None:
        params["auto_correct"] = str(auto_correct).lower()
    if compatibility_filter is not None:
        params["compatibility_filter"] = compatibility_filter
    if buyer_postal_code is not None:
        params["buyerPostalCode"] = buyer_postal_code

    headers = {"X-EBAY-C-MARKETPLACE-ID": x_ebay_c_marketplace_id}
    return client.request("GET", "/buy/browse/v1/item_summary/search", params=params, headers=headers)


def get_item(
    client: EbayClient,
    item_id: str,
    *,
    fieldgroups: Optional[str] = None,
    x_ebay_c_marketplace_id: str = "EBAY_US",
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if fieldgroups is not None:
        params["fieldgroups"] = fieldgroups
    headers = {"X-EBAY-C-MARKETPLACE-ID": x_ebay_c_marketplace_id}
    return client.request("GET", f"/buy/browse/v1/item/{item_id}", params=params, headers=headers)


def get_item_by_legacy_id(
    client: EbayClient,
    legacy_item_id: str,
    *,
    x_ebay_c_marketplace_id: str = "EBAY_US",
) -> Dict[str, Any]:
    headers = {"X-EBAY-C-MARKETPLACE-ID": x_ebay_c_marketplace_id}
    return client.request("GET", f"/buy/browse/v1/item/get_item_by_legacy_id", params={"legacy_item_id": legacy_item_id}, headers=headers)


def get_item_group(
    client: EbayClient,
    item_group_id: str,
    *,
    x_ebay_c_marketplace_id: str = "EBAY_US",
) -> Dict[str, Any]:
    headers = {"X-EBAY-C-MARKETPLACE-ID": x_ebay_c_marketplace_id}
    return client.request("GET", f"/buy/browse/v1/item_group/{item_group_id}", headers=headers)


def get_items_by_item_group(
    client: EbayClient,
    item_group_id: str,
    *,
    x__ebay_c_marketplace_id: str = "EBAY_US",
) -> Dict[str, Any]:
    headers = {"X-EBAY-C-MARKETPLACE-ID": x__ebay_c_marketplace_id}
    return client.request("GET", f"/buy/browse/v1/item_group/{item_group_id}/get_items_by_item_group", headers=headers)


def get_item_snapshot(
    client: EbayClient,
    item_id: str,
    *,
    snapshot_id: Optional[str] = None,
    x_ebay_c_marketplace_id: str = "EBAY_US",
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if snapshot_id is not None:
        params["snapshot_id"] = snapshot_id
    headers = {"X-EBAY-C-MARKETPLACE-ID": x_ebay_c_marketplace_id}
    return client.request("GET", f"/buy/browse/v1/item/{item_id}/get_item_snapshot", params=params, headers=headers)


def check_compatibility(
    client: EbayClient,
    item_id: str,
    *,
    compatibility_filter: str,
    x_ebay_c_marketplace_id: str = "EBAY_US",
) -> Dict[str, Any]:
    headers = {"X-EBAY-C-MARKETPLACE-ID": x_ebay_c_marketplace_id}
    params = {"compatibility_filter": compatibility_filter}
    return client.request("GET", f"/buy/browse/v1/item/{item_id}/check_compatibility", params=params, headers=headers)


def get_merchandised_products(
    client: EbayClient,
    *,
    category_id: Optional[str] = None,
    metric_name: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    filter: Optional[str] = None,
    x_ebay_c_marketplace_id: str = "EBAY_US",
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if category_id is not None:
        params["category_id"] = category_id
    if metric_name is not None:
        params["metric_name"] = metric_name
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    if filter is not None:
        params["filter"] = filter
    headers = {"X-EBAY-C-MARKETPLACE-ID": x_ebay_c_marketplace_id}
    return client.request("GET", "/buy/browse/v1/item/get_merchandised_products", params=params, headers=headers)


def get_item_summary_by_gtin(
    client: EbayClient,
    gtin: str,
    *,
    x_ebay_c_marketplace_id: str = "EBAY_US",
) -> Dict[str, Any]:
    headers = {"X-EBAY-C-MARKETPLACE-ID": x_ebay_c_marketplace_id}
    return client.request("GET", "/buy/browse/v1/item_summary/get_by_gtin", params={"gtin": gtin}, headers=headers)


def get_item_summary_by_epid(
    client: EbayClient,
    epid: str,
    *,
    x_ebay_c_marketplace_id: str = "EBAY_US",
) -> Dict[str, Any]:
    headers = {"X-EBAY-C-MARKETPLACE-ID": x_ebay_c_marketplace_id}
    return client.request("GET", "/buy/browse/v1/item_summary/get_by_epid", params={"epid": epid}, headers=headers)


def get_item_summary_by_product(
    client: EbayClient,
    *,
    gtin: Optional[str] = None,
    epid: Optional[str] = None,
    mpn: Optional[str] = None,
    brand: Optional[str] = None,
    x_ebay_c_marketplace_id: str = "EBAY_US",
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if gtin is not None:
        params["gtin"] = gtin
    if epid is not None:
        params["epid"] = epid
    if mpn is not None:
        params["mpn"] = mpn
    if brand is not None:
        params["brand"] = brand
    headers = {"X-EBAY-C-MARKETPLACE-ID": x_ebay_c_marketplace_id}
    return client.request("GET", "/buy/browse/v1/item_summary/get_by_product", params=params, headers=headers)


def get_item_summary_by_category(
    client: EbayClient,
    category_id: str,
    *,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    filter: Optional[str] = None,
    sort: Optional[str] = None,
    x_ebay_c_marketplace_id: str = "EBAY_US",
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"category_id": category_id}
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    if filter is not None:
        params["filter"] = filter
    if sort is not None:
        params["sort"] = sort
    headers = {"X-EBAY-C-MARKETPLACE-ID": x_ebay_c_marketplace_id}
    return client.request("GET", "/buy/browse/v1/item_summary/search", params=params, headers=headers)
