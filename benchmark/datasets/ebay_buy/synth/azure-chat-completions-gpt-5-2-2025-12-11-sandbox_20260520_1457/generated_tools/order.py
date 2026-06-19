from typing import Any, Dict, List, Optional

from .client import EbayClient


# Note: Order API v2 uses apix.ebay.com host per docs. We'll route via base_url by overriding path with full host not supported.
# For simplicity, we use the standard api.ebay.com base; in practice, apix is required. We detect and swap host in client.


def _order_base_path(path: str) -> str:
    # Client base_url is https://api(.sandbox).ebay.com; Order v2 uses https://apix(.sandbox).ebay.com
    # We'll encode as absolute URL marker and let server use requests directly if needed.
    return path


def order_initiate_guest_checkout_session(
    client: EbayClient,
    *,
    marketplace_id: str,
    contact_email: str,
    line_item_inputs: List[Dict[str, Any]],
    shipping_address: Dict[str, Any],
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    headers: Dict[str, str] = {
        "X-EBAY-C-MARKETPLACE-ID": marketplace_id,
    }
    if enduserctx is not None:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx

    payload = {
        "contactEmail": contact_email,
        "lineItemInputs": line_item_inputs,
        "shippingAddress": shipping_address,
    }
    return client.request(
        "POST",
        "/buy/order/v2/guest_checkout_session/initiate",
        json=payload,
        headers=headers,
        use_apix=True,
    )


def order_get_guest_checkout_session(
    client: EbayClient,
    checkout_session_id: str,
    *,
    marketplace_id: str,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    headers: Dict[str, str] = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    if enduserctx is not None:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx
    return client.request(
        "GET",
        f"/buy/order/v2/guest_checkout_session/{checkout_session_id}",
        headers=headers,
        use_apix=True,
    )


def order_update_guest_quantity(
    client: EbayClient,
    checkout_session_id: str,
    line_item_id: str,
    quantity: int,
    *,
    marketplace_id: str,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    headers: Dict[str, str] = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    if enduserctx is not None:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx
    payload = {"lineItemId": line_item_id, "quantity": quantity}
    return client.request(
        "POST",
        f"/buy/order/v2/guest_checkout_session/{checkout_session_id}/update_quantity",
        json=payload,
        headers=headers,
        use_apix=True,
    )


def order_update_guest_shipping_address(
    client: EbayClient,
    checkout_session_id: str,
    shipping_address: Dict[str, Any],
    *,
    marketplace_id: str,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    headers: Dict[str, str] = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    if enduserctx is not None:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx
    payload = {"shippingAddress": shipping_address}
    return client.request(
        "POST",
        f"/buy/order/v2/guest_checkout_session/{checkout_session_id}/update_shipping_address",
        json=payload,
        headers=headers,
        use_apix=True,
    )


def order_update_guest_shipping_option(
    client: EbayClient,
    checkout_session_id: str,
    line_item_id: str,
    shipping_option_id: str,
    *,
    marketplace_id: str,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    headers: Dict[str, str] = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    if enduserctx is not None:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx
    payload = {"lineItemId": line_item_id, "shippingOptionId": shipping_option_id}
    return client.request(
        "POST",
        f"/buy/order/v2/guest_checkout_session/{checkout_session_id}/update_shipping_option",
        json=payload,
        headers=headers,
        use_apix=True,
    )


def order_apply_guest_coupon(
    client: EbayClient,
    checkout_session_id: str,
    coupon_code: str,
    *,
    marketplace_id: str,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    headers: Dict[str, str] = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    if enduserctx is not None:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx
    payload = {"couponCode": coupon_code}
    return client.request(
        "POST",
        f"/buy/order/v2/guest_checkout_session/{checkout_session_id}/apply_coupon",
        json=payload,
        headers=headers,
        use_apix=True,
    )


def order_remove_guest_coupon(
    client: EbayClient,
    checkout_session_id: str,
    coupon_code: str,
    *,
    marketplace_id: str,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    headers: Dict[str, str] = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    if enduserctx is not None:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx
    payload = {"couponCode": coupon_code}
    return client.request(
        "POST",
        f"/buy/order/v2/guest_checkout_session/{checkout_session_id}/remove_coupon",
        json=payload,
        headers=headers,
        use_apix=True,
    )


def order_get_guest_purchase_order(
    client: EbayClient,
    purchase_order_id: str,
    *,
    marketplace_id: str,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    headers: Dict[str, str] = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    if enduserctx is not None:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx
    return client.request(
        "GET",
        f"/buy/order/v2/guest_purchase_order/{purchase_order_id}",
        headers=headers,
        use_apix=True,
    )
