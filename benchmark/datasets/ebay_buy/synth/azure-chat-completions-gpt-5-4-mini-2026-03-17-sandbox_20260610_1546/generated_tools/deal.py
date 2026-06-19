from .common import request


def get_deal_items(markets=None, limit=None, offset=None):
    params = {k: v for k, v in {'marketplace_id': markets, 'limit': limit, 'offset': offset}.items() if v is not None}
    return request('GET', '/buy/deal/v1/deal_item', params=params)


def get_events(markets=None, limit=None, offset=None):
    params = {k: v for k, v in {'marketplace_id': markets, 'limit': limit, 'offset': offset}.items() if v is not None}
    return request('GET', '/buy/deal/v1/event', params=params)


def get_event(event_id):
    return request('GET', f'/buy/deal/v1/event/{event_id}')


def get_event_items(event_id, limit=None, offset=None):
    params = {k: v for k, v in {'limit': limit, 'offset': offset}.items() if v is not None}
    return request('GET', f'/buy/deal/v1/event/{event_id}/item', params=params)
