from .common import request_json


def get_subscriptions(page_size=None, continuation_token=None):
    params = {}
    if page_size is not None:
        params['page_size'] = page_size
    if continuation_token is not None:
        params['continuation_token'] = continuation_token
    return request_json('GET', '/commerce/notification/v1/subscription', token_type='user', params=params)
