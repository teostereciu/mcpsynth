from typing import Any, Dict, List, Optional, Sequence

from .ebay_client import EbayClient


class BrowseTools:
    def __init__(self, client: Optional[EbayClient] = None):
        self.client = client or EbayClient()

    def get_item(self, listing_id: str, *, fieldgroups: Optional[List[str]] = None) -> Dict[str, Any]:
        params: Dict[str, Any] = {}
        if fieldgroups:
            params["fieldgroups"] = ",".join(fieldgroups)
        return self.client.request("GET", f"/buy/browse/v1/item/{listing_id}", params=params)

    def search_item_summaries(
        self,
        *,
        q: Optional[str] = None,
        category_ids: Optional[str] = None,
        charity_ids: Optional[str] = None,
        epid: Optional[str] = None,
        gtin: Optional[str] = None,
        filter: Optional[str] = None,
        aspect_filter: Optional[str] = None,
        compatibility_filter: Optional[str] = None,
        fieldgroups: Optional[List[str]] = None,
        sort: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> Dict[str, Any]:
        params: Dict[str, Any] = {}
        if q is not None:
            params["q"] = q
        if category_ids is not None:
            params["category_ids"] = category_ids
        if charity_ids is not None:
            params["charity_ids"] = charity_ids
        if epid is not None:
            params["epid"] = epid
        if gtin is not None:
            params["gtin"] = gtin
        if filter is not None:
            params["filter"] = filter
        if aspect_filter is not None:
            params["aspect_filter"] = aspect_filter
        if compatibility_filter is not None:
            params["compatibility_filter"] = compatibility_filter
        if fieldgroups:
            params["fieldgroups"] = ",".join(fieldgroups)
        if sort is not None:
            params["sort"] = sort
        if limit is not None:
            params["limit"] = int(limit)
        if offset is not None:
            params["offset"] = int(offset)
        return self.client.request("GET", "/buy/browse/v1/item_summary/search", params=params)

    def search_item_summaries_by_image(
        self,
        image_base64: str,
        *,
        category_ids: Optional[str] = None,
        charity_ids: Optional[str] = None,
        filter: Optional[str] = None,
        aspect_filter: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> Dict[str, Any]:
        params: Dict[str, Any] = {}
        if category_ids is not None:
            params["category_ids"] = category_ids
        if charity_ids is not None:
            params["charity_ids"] = charity_ids
        if filter is not None:
            params["filter"] = filter
        if aspect_filter is not None:
            params["aspect_filter"] = aspect_filter
        if limit is not None:
            params["limit"] = int(limit)
        if offset is not None:
            params["offset"] = int(offset)
        payload = {"image": image_base64}
        return self.client.request(
            "POST",
            "/buy/browse/v1/item_summary/search_by_image",
            params=params,
            json=payload,
        )

    def get_item_by_legacy_id(
        self,
        legacy_item_id: str,
        *,
        legacy_variation_id: Optional[str] = None,
        fieldgroups: Optional[List[str]] = None,
    ) -> Dict[str, Any]:
        params: Dict[str, Any] = {"legacy_item_id": legacy_item_id}
        if legacy_variation_id is not None:
            params["legacy_variation_id"] = legacy_variation_id
        if fieldgroups:
            params["fieldgroups"] = ",".join(fieldgroups)
        return self.client.request("GET", "/buy/browse/v1/item/get_item_by_legacy_id", params=params)

    def get_items(
        self,
        *,
        item_ids: Optional[Sequence[str]] = None,
        item_group_ids: Optional[Sequence[str]] = None,
    ) -> Dict[str, Any]:
        params: Dict[str, Any] = {}
        if item_ids:
            params["item_ids"] = ",".join(item_ids)
        if item_group_ids:
            params["item_group_ids"] = ",".join(item_group_ids)
        # This endpoint uses a different scope
        return self.client.request(
            "GET",
            "/buy/browse/v1/item/",
            params=params,
            scope="https://api.ebay.com/oauth/api_scope/buy.item.bulk",
        )

    def check_compatibility(
        self,
        listing_id: str,
        compatibility_properties: List[Dict[str, str]],
        *,
        marketplace_id: Optional[str] = None,
        accept_language: Optional[str] = None,
    ) -> Dict[str, Any]:
        headers: Dict[str, str] = {"Content-Type": "application/json"}
        if marketplace_id:
            headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
        if accept_language:
            headers["Accept-Language"] = accept_language
        payload = {"compatibilityProperties": compatibility_properties}
        return self.client.request(
            "POST",
            f"/buy/browse/v1/item/{listing_id}/check_compatibility",
            json=payload,
            headers=headers,
        )

    def get_items_by_item_group(
        self,
        item_group_id: str,
        *,
        fieldgroups: Optional[List[str]] = None,
    ) -> Dict[str, Any]:
        params: Dict[str, Any] = {}
        if fieldgroups:
            params["fieldgroups"] = ",".join(fieldgroups)
        return self.client.request(
            "GET",
            "/buy/browse/v1/item/get_items_by_item_group",
            params={**params, "item_group_id": item_group_id},
        )
