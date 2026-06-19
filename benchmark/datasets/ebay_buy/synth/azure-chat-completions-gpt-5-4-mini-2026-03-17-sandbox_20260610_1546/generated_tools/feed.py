from .common import request


def get_item_feed(feed_type=None, marketplace_id=None):
    params = {k: v for k, v in {'feed_type': feed_type, 'marketplace_id': marketplace_id}.items() if v is not None}
    return request('GET', '/buy/feed/v1/item/feed', params=params)


def get_item_group_feed(feed_type=None, marketplace_id=None):
    params = {k: v for k, v in {'feed_type': feed_type, 'marketplace_id': marketplace_id}.items() if v is not None}
    return request('GET', '/buy/feed/v1/item_group/feed', params=params)


def get_item_priority_feed(feed_type=None, marketplace_id=None):
    params = {k: v for k, v in {'feed_type': feed_type, 'marketplace_id': marketplace_id}.items() if v is not None}
    return request('GET', '/buy/feed/v1/item_priority/feed', params=params)


def get_item_snapshot_feed(feed_type=None, marketplace_id=None):
    params = {k: v for k, v in {'feed_type': feed_type, 'marketplace_id': marketplace_id}.items() if v is not None}
    return request('GET', '/buy/feed/v1/item_snapshot/feed', params=params)
