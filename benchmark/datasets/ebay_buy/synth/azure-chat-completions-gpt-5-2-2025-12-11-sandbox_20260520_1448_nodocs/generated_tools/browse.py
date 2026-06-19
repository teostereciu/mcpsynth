from typing import Any, Dict, Optional

from .client import EbayBuyApiClient


BROWSE_SCOPE = "https://api.ebay.com/oauth/api_scope"


def search_items(
    client: EbayBuyApiClient,
    *,
    q: Optional[str] = None,
    category_ids: Optional[str] = None,
    aspect_filter: Optional[str] = None,
    filter: Optional[str] = None,
    sort: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    fieldgroups: Optional[str] = None,
    compatibility_filter: Optional[str] = None,
    auto_correct: Optional[bool] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if q is not None:
        params["q"] = q
    if category_ids is not None:
        params["category_ids"] = category_ids
    if aspect_filter is not None:
        params["aspect_filter"] = aspect_filter
    if filter is not None:
        params["filter"] = filter
    if sort is not None:
        params["sort"] = sort
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    if fieldgroups is not None:
        params["fieldgroups"] = fieldgroups
    if compatibility_filter is not None:
        params["compatibility_filter"] = compatibility_filter
    if auto_correct is not None:
        params["auto_correct"] = str(auto_correct).lower()

    return client.request("GET", "/buy/browse/v1/item_summary/search", scope=BROWSE_SCOPE, params=params)


def get_item(client: EbayBuyApiClient, *, item_id: str, fieldgroups: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if fieldgroups is not None:
        params["fieldgroups"] = fieldgroups
    return client.request("GET", f"/buy/browse/v1/item/{item_id}", scope=BROWSE_SCOPE, params=params)


def get_item_group(client: EbayBuyApiClient, *, item_group_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/buy/browse/v1/item_group/{item_group_id}", scope=BROWSE_SCOPE)


def get_items_by_item_group(client: EbayBuyApiClient, *, item_group_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/buy/browse/v1/item_group/{item_group_id}/get_items", scope=BROWSE_SCOPE)


def get_item_by_legacy_id(client: EbayBuyApiClient, *, legacy_item_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/buy/browse/v1/item/get_item_by_legacy_id", scope=BROWSE_SCOPE, params={"legacy_item_id": legacy_item_id})


def get_item_by_epid(client: EbayBuyApiClient, *, epid: str) -> Dict[str, Any]:
    return client.request("GET", f"/buy/browse/v1/item/get_item_by_epid", scope=BROWSE_SCOPE, params={"epid": epid})


def get_item_by_gtin(client: EbayBuyApiClient, *, gtin: str) -> Dict[str, Any]:
    return client.request("GET", f"/buy/browse/v1/item/get_item_by_gtin", scope=BROWSE_SCOPE, params={"gtin": gtin})


def get_item_by_isbn(client: EbayBuyApiClient, *, isbn: str) -> Dict[str, Any]:
    return client.request("GET", f"/buy/browse/v1/item/get_item_by_isbn", scope=BROWSE_SCOPE, params={"isbn": isbn})


def get_item_by_upc(client: EbayBuyApiClient, *, upc: str) -> Dict[str, Any]:
    return client.request("GET", f"/buy/browse/v1/item/get_item_by_upc", scope=BROWSE_SCOPE, params={"upc": upc})


def get_item_by_product(client: EbayBuyApiClient, *, product_id: str, product_id_type: str) -> Dict[str, Any]:
    return client.request(
        "GET",
        "/buy/browse/v1/item/get_item_by_product",
        scope=BROWSE_SCOPE,
        params={"product_id": product_id, "product_id_type": product_id_type},
    )


def check_item_compatibility(client: EbayBuyApiClient, *, item_id: str, compatibility_properties: str) -> Dict[str, Any]:
    return client.request(
        "GET",
        f"/buy/browse/v1/item/{item_id}/check_compatibility",
        scope=BROWSE_SCOPE,
        params={"compatibility_properties": compatibility_properties},
    )


def get_item_compatibility(client: EbayBuyApiClient, *, item_id: str, compatibility_properties: str) -> Dict[str, Any]:
    return client.request(
        "GET",
        f"/buy/browse/v1/item/{item_id}/get_compatibility",
        scope=BROWSE_SCOPE,
        params={"compatibility_properties": compatibility_properties},
    )


def get_item_compatibility_properties(client: EbayBuyApiClient, *, category_id: str) -> Dict[str, Any]:
    return client.request(
        "GET",
        f"/buy/browse/v1/item/get_compatibility_properties",
        scope=BROWSE_SCOPE,
        params={"category_id": category_id},
    )


def get_merchandised_products(client: EbayBuyApiClient, *, category_id: str, metric_name: Optional[str] = None, limit: Optional[int] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"category_id": category_id}
    if metric_name is not None:
        params["metric_name"] = metric_name
    if limit is not None:
        params["limit"] = limit
    return client.request("GET", "/buy/browse/v1/item/get_merchandised_products", scope=BROWSE_SCOPE, params=params)


def get_category_tree(client: EbayBuyApiClient, *, category_tree_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/buy/browse/v1/category_tree/{category_tree_id}", scope=BROWSE_SCOPE)


def get_category_subtree(client: EbayBuyApiClient, *, category_tree_id: str, category_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/buy/browse/v1/category_tree/{category_tree_id}/get_category_subtree", scope=BROWSE_SCOPE, params={"category_id": category_id})


def get_category_suggestions(client: EbayBuyApiClient, *, category_tree_id: str, q: str) -> Dict[str, Any]:
    return client.request("GET", f"/buy/browse/v1/category_tree/{category_tree_id}/get_category_suggestions", scope=BROWSE_SCOPE, params={"q": q})


def get_default_category_tree_id(client: EbayBuyApiClient, *, marketplace_id: str) -> Dict[str, Any]:
    return client.request("GET", "/buy/browse/v1/get_default_category_tree_id", scope=BROWSE_SCOPE, params={"marketplace_id": marketplace_id})


def get_item_aspects_for_category(client: EbayBuyApiClient, *, category_tree_id: str, category_id: str) -> Dict[str, Any]:
    return client.request(
        "GET",
        f"/buy/browse/v1/category_tree/{category_tree_id}/get_item_aspects_for_category",
        scope=BROWSE_SCOPE,
        params={"category_id": category_id},
    )
