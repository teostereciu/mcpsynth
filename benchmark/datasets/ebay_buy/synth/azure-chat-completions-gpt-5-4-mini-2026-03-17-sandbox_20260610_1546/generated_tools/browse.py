from .common import request


def search(q=None, category_ids=None, limit=None, offset=None, sort=None, fieldgroups=None, filter=None, aspect_filter=None, compatibility_filter=None, gtin=None, epid=None, charity_ids=None):
    params = {k: v for k, v in {
        'q': q, 'category_ids': category_ids, 'limit': limit, 'offset': offset, 'sort': sort,
        'fieldgroups': fieldgroups, 'filter': filter, 'aspect_filter': aspect_filter,
        'compatibility_filter': compatibility_filter, 'gtin': gtin, 'epid': epid, 'charity_ids': charity_ids,
    }.items() if v is not None}
    return request('GET', '/buy/browse/v1/item_summary/search', params=params)


def search_by_image(image_url=None, limit=None, offset=None):
    params = {k: v for k, v in {'image_url': image_url, 'limit': limit, 'offset': offset}.items() if v is not None}
    return request('GET', '/buy/browse/v1/item_summary/search_by_image', params=params)


def get_item(item_id, fieldgroups=None):
    params = {k: v for k, v in {'fieldgroups': fieldgroups}.items() if v is not None}
    return request('GET', f'/buy/browse/v1/item/{item_id}', params=params)


def get_item_by_legacy_id(legacy_item_id, legacy_variation_id=None, legacy_sku=None, fieldgroups=None):
    params = {k: v for k, v in {'legacy_item_id': legacy_item_id, 'legacy_variation_id': legacy_variation_id, 'legacy_sku': legacy_sku, 'fieldgroups': fieldgroups}.items() if v is not None}
    return request('GET', '/buy/browse/v1/item/get_item_by_legacy_id', params=params)


def get_items(item_ids=None, item_group_ids=None, fieldgroups=None):
    params = {k: v for k, v in {'item_ids': item_ids, 'item_group_ids': item_group_ids, 'fieldgroups': fieldgroups}.items() if v is not None}
    return request('GET', '/buy/browse/v1/item/get_items', params=params)


def get_items_by_item_group(item_group_id, fieldgroups=None):
    params = {k: v for k, v in {'fieldgroups': fieldgroups}.items() if v is not None}
    return request('GET', f'/buy/browse/v1/item/get_items_by_item_group/{item_group_id}', params=params)


def check_compatibility(item_id, compatibility_filter=None):
    params = {k: v for k, v in {'compatibility_filter': compatibility_filter}.items() if v is not None}
    return request('POST', f'/buy/browse/v1/item/{item_id}/check_compatibility', params=params)
