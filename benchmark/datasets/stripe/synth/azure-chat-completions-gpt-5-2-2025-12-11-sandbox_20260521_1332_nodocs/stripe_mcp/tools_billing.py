from typing import Any, Dict, Optional

from .http import stripe_request


def _ok(x: Any) -> Any:
    return x


def _err(e: Dict[str, Any]) -> Dict[str, Any]:
    return e


# Products
async def create_product(*, name: str, description: Optional[str] = None, active: Optional[bool] = None, metadata: Optional[Dict[str, str]] = None) -> Any:
    data = {"name": name, "description": description, "active": active, "metadata": metadata}
    res, err = stripe_request("POST", "/v1/products", data=data)
    return _ok(res) if not err else _err(err)


async def get_product(*, product_id: str) -> Any:
    res, err = stripe_request("GET", f"/v1/products/{product_id}")
    return _ok(res) if not err else _err(err)


async def update_product(*, product_id: str, name: Optional[str] = None, description: Optional[str] = None, active: Optional[bool] = None, metadata: Optional[Dict[str, str]] = None) -> Any:
    data = {"name": name, "description": description, "active": active, "metadata": metadata}
    res, err = stripe_request("POST", f"/v1/products/{product_id}", data=data)
    return _ok(res) if not err else _err(err)


async def list_products(*, active: Optional[bool] = None, limit: int = 10) -> Any:
    query = {"active": active, "limit": limit}
    res, err = stripe_request("GET", "/v1/products", query=query)
    return _ok(res) if not err else _err(err)


# Prices
async def create_price(
    *,
    currency: str,
    unit_amount: Optional[int] = None,
    unit_amount_decimal: Optional[str] = None,
    product: Optional[str] = None,
    recurring: Optional[Dict[str, Any]] = None,
    nickname: Optional[str] = None,
    active: Optional[bool] = None,
    metadata: Optional[Dict[str, str]] = None,
) -> Any:
    data = {
        "currency": currency,
        "unit_amount": unit_amount,
        "unit_amount_decimal": unit_amount_decimal,
        "product": product,
        "recurring": recurring,
        "nickname": nickname,
        "active": active,
        "metadata": metadata,
    }
    res, err = stripe_request("POST", "/v1/prices", data=data)
    return _ok(res) if not err else _err(err)


async def get_price(*, price_id: str) -> Any:
    res, err = stripe_request("GET", f"/v1/prices/{price_id}")
    return _ok(res) if not err else _err(err)


async def update_price(*, price_id: str, active: Optional[bool] = None, nickname: Optional[str] = None, metadata: Optional[Dict[str, str]] = None) -> Any:
    data = {"active": active, "nickname": nickname, "metadata": metadata}
    res, err = stripe_request("POST", f"/v1/prices/{price_id}", data=data)
    return _ok(res) if not err else _err(err)


async def list_prices(*, product: Optional[str] = None, active: Optional[bool] = None, limit: int = 10) -> Any:
    query = {"product": product, "active": active, "limit": limit}
    res, err = stripe_request("GET", "/v1/prices", query=query)
    return _ok(res) if not err else _err(err)


# Subscriptions
async def create_subscription(
    *,
    customer: str,
    items: list,
    default_payment_method: Optional[str] = None,
    trial_period_days: Optional[int] = None,
    coupon: Optional[str] = None,
    promotion_code: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
) -> Any:
    data = {
        "customer": customer,
        "items": items,
        "default_payment_method": default_payment_method,
        "trial_period_days": trial_period_days,
        "coupon": coupon,
        "promotion_code": promotion_code,
        "metadata": metadata,
    }
    res, err = stripe_request("POST", "/v1/subscriptions", data=data)
    return _ok(res) if not err else _err(err)


async def get_subscription(*, subscription_id: str) -> Any:
    res, err = stripe_request("GET", f"/v1/subscriptions/{subscription_id}")
    return _ok(res) if not err else _err(err)


async def update_subscription(
    *,
    subscription_id: str,
    cancel_at_period_end: Optional[bool] = None,
    items: Optional[list] = None,
    proration_behavior: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
) -> Any:
    data = {
        "cancel_at_period_end": cancel_at_period_end,
        "items": items,
        "proration_behavior": proration_behavior,
        "metadata": metadata,
    }
    res, err = stripe_request("POST", f"/v1/subscriptions/{subscription_id}", data=data)
    return _ok(res) if not err else _err(err)


async def cancel_subscription(*, subscription_id: str, invoice_now: Optional[bool] = None, prorate: Optional[bool] = None) -> Any:
    data = {"invoice_now": invoice_now, "prorate": prorate}
    res, err = stripe_request("DELETE", f"/v1/subscriptions/{subscription_id}", data=data)
    return _ok(res) if not err else _err(err)


async def list_subscriptions(*, customer: Optional[str] = None, status: Optional[str] = None, limit: int = 10) -> Any:
    query = {"customer": customer, "status": status, "limit": limit}
    res, err = stripe_request("GET", "/v1/subscriptions", query=query)
    return _ok(res) if not err else _err(err)


# Invoices
async def create_invoice(*, customer: str, auto_advance: Optional[bool] = None, collection_method: Optional[str] = None, days_until_due: Optional[int] = None, metadata: Optional[Dict[str, str]] = None) -> Any:
    data = {
        "customer": customer,
        "auto_advance": auto_advance,
        "collection_method": collection_method,
        "days_until_due": days_until_due,
        "metadata": metadata,
    }
    res, err = stripe_request("POST", "/v1/invoices", data=data)
    return _ok(res) if not err else _err(err)


async def get_invoice(*, invoice_id: str) -> Any:
    res, err = stripe_request("GET", f"/v1/invoices/{invoice_id}")
    return _ok(res) if not err else _err(err)


async def finalize_invoice(*, invoice_id: str) -> Any:
    res, err = stripe_request("POST", f"/v1/invoices/{invoice_id}/finalize")
    return _ok(res) if not err else _err(err)


async def pay_invoice(*, invoice_id: str, paid_out_of_band: Optional[bool] = None) -> Any:
    data = {"paid_out_of_band": paid_out_of_band}
    res, err = stripe_request("POST", f"/v1/invoices/{invoice_id}/pay", data=data)
    return _ok(res) if not err else _err(err)


async def void_invoice(*, invoice_id: str) -> Any:
    res, err = stripe_request("POST", f"/v1/invoices/{invoice_id}/void")
    return _ok(res) if not err else _err(err)


async def list_invoices(*, customer: Optional[str] = None, status: Optional[str] = None, limit: int = 10) -> Any:
    query = {"customer": customer, "status": status, "limit": limit}
    res, err = stripe_request("GET", "/v1/invoices", query=query)
    return _ok(res) if not err else _err(err)
