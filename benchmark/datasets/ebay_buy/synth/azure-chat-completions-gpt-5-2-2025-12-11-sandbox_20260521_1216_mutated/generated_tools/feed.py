from typing import Any, Dict, Optional

from .ebay_client import EbayClient


class FeedTools:
    def __init__(self, client: Optional[EbayClient] = None):
        self.client = client or EbayClient()

    def get_item_feed(
        self,
        *,
        feed_scope: str,
        category_id: Optional[str] = None,
        date: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> Dict[str, Any]:
        params: Dict[str, Any] = {"feed_scope": feed_scope}
        if category_id is not None:
            params["category_id"] = category_id
        if date is not None:
            params["date"] = date
        if limit is not None:
            params["limit"] = int(limit)
        if offset is not None:
            params["offset"] = int(offset)
        return self.client.request(
            "GET",
            "/buy/feed/v1/item",
            params=params,
            scope="https://api.ebay.com/oauth/api_scope/buy.item.feed",
        )

    def get_item_group_feed(
        self,
        *,
        feed_scope: str,
        category_id: Optional[str] = None,
        date: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> Dict[str, Any]:
        params: Dict[str, Any] = {"feed_scope": feed_scope}
        if category_id is not None:
            params["category_id"] = category_id
        if date is not None:
            params["date"] = date
        if limit is not None:
            params["limit"] = int(limit)
        if offset is not None:
            params["offset"] = int(offset)
        return self.client.request(
            "GET",
            "/buy/feed/v1/item_group",
            params=params,
            scope="https://api.ebay.com/oauth/api_scope/buy.item.feed",
        )

    def get_item_group_feed_by_item(
        self,
        *,
        feed_scope: str,
        category_id: Optional[str] = None,
        date: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> Dict[str, Any]:
        params: Dict[str, Any] = {"feed_scope": feed_scope}
        if category_id is not None:
            params["category_id"] = category_id
        if date is not None:
            params["date"] = date
        if limit is not None:
            params["limit"] = int(limit)
        if offset is not None:
            params["offset"] = int(offset)
        return self.client.request(
            "GET",
            "/buy/feed/v1/item/item_group",
            params=params,
            scope="https://api.ebay.com/oauth/api_scope/buy.item.feed",
        )

    def get_item_priority_feed(
        self,
        *,
        feed_scope: str,
        category_id: Optional[str] = None,
        date: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> Dict[str, Any]:
        params: Dict[str, Any] = {"feed_scope": feed_scope}
        if category_id is not None:
            params["category_id"] = category_id
        if date is not None:
            params["date"] = date
        if limit is not None:
            params["limit"] = int(limit)
        if offset is not None:
            params["offset"] = int(offset)
        return self.client.request(
            "GET",
            "/buy/feed/v1/item_priority",
            params=params,
            scope="https://api.ebay.com/oauth/api_scope/buy.item.feed",
        )

    def get_item_snapshot_feed(
        self,
        *,
        feed_scope: str,
        category_id: Optional[str] = None,
        date: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> Dict[str, Any]:
        params: Dict[str, Any] = {"feed_scope": feed_scope}
        if category_id is not None:
            params["category_id"] = category_id
        if date is not None:
            params["date"] = date
        if limit is not None:
            params["limit"] = int(limit)
        if offset is not None:
            params["offset"] = int(offset)
        return self.client.request(
            "GET",
            "/buy/feed/v1/item_snapshot",
            params=params,
            scope="https://api.ebay.com/oauth/api_scope/buy.item.feed",
        )
