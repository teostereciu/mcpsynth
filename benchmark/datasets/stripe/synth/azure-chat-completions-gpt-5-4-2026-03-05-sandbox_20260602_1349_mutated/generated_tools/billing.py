from typing import Any, Dict

from generated_tools.common import stripe_request


def create_subscription(customer: str, items: list[dict], **kwargs: Any) -> Dict[str, Any]:
    return stripe_request("POST", "/v1/subscriptions", data={"customer": customer, "items": items, **kwargs})


def update_subscription(subscription: str, **kwargs: Any) -> Dict[str, Any]:
    return stripe_request("POST", f"/v1/subscriptions/{subscription}", data=kwargs)


def retrieve_subscription(subscription: str, **query: Any) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/subscriptions/{subscription}", query=query)


def create_invoice_preview(**kwargs: Any) -> Dict[str, Any]:
    return stripe_request("POST", "/v1/invoices/create_preview", data=kwargs)


def create_invoice(**kwargs: Any) -> Dict[str, Any]:
    return stripe_request("POST", "/v1/invoices", data=kwargs)


def update_invoice(invoice: str, **kwargs: Any) -> Dict[str, Any]:
    return stripe_request("POST", f"/v1/invoices/{invoice}", data=kwargs)


def retrieve_invoice(invoice: str, **query: Any) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/invoices/{invoice}", query=query)


def create_coupon(duration: str = "once", **kwargs: Any) -> Dict[str, Any]:
    return stripe_request("POST", "/v1/coupons", data={"duration": duration, **kwargs})


def update_coupon(coupon: str, **kwargs: Any) -> Dict[str, Any]:
    return stripe_request("POST", f"/v1/coupons/{coupon}", data=kwargs)


def retrieve_coupon(coupon: str, **query: Any) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/coupons/{coupon}", query=query)


def create_promotion_code(promotion: dict, **kwargs: Any) -> Dict[str, Any]:
    return stripe_request("POST", "/v1/promotion_codes", data={"promotion": promotion, **kwargs})


def update_promotion_code(promotion_code: str, **kwargs: Any) -> Dict[str, Any]:
    return stripe_request("POST", f"/v1/promotion_codes/{promotion_code}", data=kwargs)


def retrieve_promotion_code(promotion_code: str, **query: Any) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/promotion_codes/{promotion_code}", query=query)
