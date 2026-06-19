from .common import request


def initiate_guest_checkout_session(payload):
    return request('POST', '/buy/order/v2/guest_checkout_session/initiate', json_body=payload)


def get_guest_checkout_session(checkout_session_id):
    return request('GET', f'/buy/order/v2/guest_checkout_session/{checkout_session_id}')


def apply_guest_coupon(checkout_session_id, payload):
    return request('POST', f'/buy/order/v2/guest_checkout_session/{checkout_session_id}/apply_coupon', json_body=payload)


def remove_guest_coupon(checkout_session_id, payload):
    return request('POST', f'/buy/order/v2/guest_checkout_session/{checkout_session_id}/remove_coupon', json_body=payload)


def update_guest_quantity(checkout_session_id, payload):
    return request('POST', f'/buy/order/v2/guest_checkout_session/{checkout_session_id}/update_quantity', json_body=payload)


def update_guest_shipping_address(checkout_session_id, payload):
    return request('POST', f'/buy/order/v2/guest_checkout_session/{checkout_session_id}/update_shipping_address', json_body=payload)


def update_guest_shipping_option(checkout_session_id, payload):
    return request('POST', f'/buy/order/v2/guest_checkout_session/{checkout_session_id}/update_shipping_option', json_body=payload)


def get_guest_purchase_order(purchase_order_id):
    return request('GET', f'/buy/order/v2/guest_purchase_order/{purchase_order_id}')
