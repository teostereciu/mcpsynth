import os
from typing import Any, Dict, Optional

from mcp.server.fastmcp import FastMCP

from stripe_client import StripeClient


mcp = FastMCP("stripe-mcp")
client = StripeClient()


def _ok_or_error(status: int, payload: Dict[str, Any]) -> Dict[str, Any]:
    if status == 0:
        return payload
    if status >= 400:
        return {"error": payload.get("error", payload), "status": status}
    return payload


# -------------------- Customers --------------------

@mcp.tool()
def create_customer(
    email: Optional[str] = None,
    name: Optional[str] = None,
    phone: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """POST /v1/customers"""
    status, payload = client.request(
        "POST",
        "/v1/customers",
        {k: v for k, v in {
            "email": email,
            "name": name,
            "phone": phone,
            "description": description,
            "metadata": metadata,
        }.items() if v is not None},
    )
    return _ok_or_error(status, payload)


@mcp.tool()
def get_customer(customer_id: str) -> Dict[str, Any]:
    """GET /v1/customers/{customer}"""
    status, payload = client.request("GET", f"/v1/customers/{customer_id}")
    return _ok_or_error(status, payload)


@mcp.tool()
def update_customer(customer_id: str, updates: Dict[str, Any]) -> Dict[str, Any]:
    """POST /v1/customers/{customer}"""
    status, payload = client.request("POST", f"/v1/customers/{customer_id}", updates)
    return _ok_or_error(status, payload)


@mcp.tool()
def delete_customer(customer_id: str) -> Dict[str, Any]:
    """DELETE /v1/customers/{customer}"""
    status, payload = client.request("DELETE", f"/v1/customers/{customer_id}")
    return _ok_or_error(status, payload)


@mcp.tool()
def list_customers(limit: int = 10, starting_after: Optional[str] = None, email: Optional[str] = None) -> Dict[str, Any]:
    """GET /v1/customers"""
    params = {"limit": limit}
    if starting_after:
        params["starting_after"] = starting_after
    if email:
        params["email"] = email
    status, payload = client.request("GET", "/v1/customers", params)
    return _ok_or_error(status, payload)


# -------------------- Products & Prices --------------------

@mcp.tool()
def create_product(name: str, description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None, active: Optional[bool] = None) -> Dict[str, Any]:
    """POST /v1/products"""
    params = {"name": name}
    if description is not None:
        params["description"] = description
    if metadata is not None:
        params["metadata"] = metadata
    if active is not None:
        params["active"] = active
    status, payload = client.request("POST", "/v1/products", params)
    return _ok_or_error(status, payload)


@mcp.tool()
def get_product(product_id: str) -> Dict[str, Any]:
    """GET /v1/products/{id}"""
    status, payload = client.request("GET", f"/v1/products/{product_id}")
    return _ok_or_error(status, payload)


@mcp.tool()
def update_product(product_id: str, updates: Dict[str, Any]) -> Dict[str, Any]:
    """POST /v1/products/{id}"""
    status, payload = client.request("POST", f"/v1/products/{product_id}", updates)
    return _ok_or_error(status, payload)


@mcp.tool()
def list_products(limit: int = 10, starting_after: Optional[str] = None, active: Optional[bool] = None) -> Dict[str, Any]:
    """GET /v1/products"""
    params: Dict[str, Any] = {"limit": limit}
    if starting_after:
        params["starting_after"] = starting_after
    if active is not None:
        params["active"] = active
    status, payload = client.request("GET", "/v1/products", params)
    return _ok_or_error(status, payload)


@mcp.tool()
def create_price(
    unit_amount: int,
    currency: str,
    product: str,
    recurring: Optional[Dict[str, Any]] = None,
    nickname: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """POST /v1/prices"""
    params: Dict[str, Any] = {
        "unit_amount": unit_amount,
        "currency": currency,
        "product": product,
    }
    if recurring is not None:
        params["recurring"] = recurring
    if nickname is not None:
        params["nickname"] = nickname
    if metadata is not None:
        params["metadata"] = metadata
    status, payload = client.request("POST", "/v1/prices", params)
    return _ok_or_error(status, payload)


@mcp.tool()
def get_price(price_id: str) -> Dict[str, Any]:
    """GET /v1/prices/{id}"""
    status, payload = client.request("GET", f"/v1/prices/{price_id}")
    return _ok_or_error(status, payload)


@mcp.tool()
def list_prices(limit: int = 10, starting_after: Optional[str] = None, product: Optional[str] = None, active: Optional[bool] = None) -> Dict[str, Any]:
    """GET /v1/prices"""
    params: Dict[str, Any] = {"limit": limit}
    if starting_after:
        params["starting_after"] = starting_after
    if product:
        params["product"] = product
    if active is not None:
        params["active"] = active
    status, payload = client.request("GET", "/v1/prices", params)
    return _ok_or_error(status, payload)


# -------------------- Payment Intents --------------------

@mcp.tool()
def create_payment_intent(
    amount: int,
    currency: str,
    customer: Optional[str] = None,
    payment_method: Optional[str] = None,
    confirm: Optional[bool] = None,
    off_session: Optional[bool] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    receipt_email: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/payment_intents"""
    params: Dict[str, Any] = {"amount": amount, "currency": currency}
    if customer is not None:
        params["customer"] = customer
    if payment_method is not None:
        params["payment_method"] = payment_method
    if confirm is not None:
        params["confirm"] = confirm
    if off_session is not None:
        params["off_session"] = off_session
    if description is not None:
        params["description"] = description
    if metadata is not None:
        params["metadata"] = metadata
    if receipt_email is not None:
        params["receipt_email"] = receipt_email
    status, payload = client.request("POST", "/v1/payment_intents", params)
    return _ok_or_error(status, payload)


@mcp.tool()
def get_payment_intent(payment_intent_id: str) -> Dict[str, Any]:
    """GET /v1/payment_intents/{intent}"""
    status, payload = client.request("GET", f"/v1/payment_intents/{payment_intent_id}")
    return _ok_or_error(status, payload)


@mcp.tool()
def update_payment_intent(payment_intent_id: str, updates: Dict[str, Any]) -> Dict[str, Any]:
    """POST /v1/payment_intents/{intent}"""
    status, payload = client.request("POST", f"/v1/payment_intents/{payment_intent_id}", updates)
    return _ok_or_error(status, payload)


@mcp.tool()
def confirm_payment_intent(payment_intent_id: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """POST /v1/payment_intents/{intent}/confirm"""
    status, payload = client.request("POST", f"/v1/payment_intents/{payment_intent_id}/confirm", params or {})
    return _ok_or_error(status, payload)


@mcp.tool()
def cancel_payment_intent(payment_intent_id: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """POST /v1/payment_intents/{intent}/cancel"""
    status, payload = client.request("POST", f"/v1/payment_intents/{payment_intent_id}/cancel", params or {})
    return _ok_or_error(status, payload)


@mcp.tool()
def list_payment_intents(limit: int = 10, customer: Optional[str] = None, starting_after: Optional[str] = None) -> Dict[str, Any]:
    """GET /v1/payment_intents"""
    params: Dict[str, Any] = {"limit": limit}
    if customer:
        params["customer"] = customer
    if starting_after:
        params["starting_after"] = starting_after
    status, payload = client.request("GET", "/v1/payment_intents", params)
    return _ok_or_error(status, payload)


# -------------------- Charges & Refunds --------------------

@mcp.tool()
def get_charge(charge_id: str) -> Dict[str, Any]:
    """GET /v1/charges/{charge}"""
    status, payload = client.request("GET", f"/v1/charges/{charge_id}")
    return _ok_or_error(status, payload)


@mcp.tool()
def list_charges(limit: int = 10, customer: Optional[str] = None, payment_intent: Optional[str] = None, starting_after: Optional[str] = None) -> Dict[str, Any]:
    """GET /v1/charges"""
    params: Dict[str, Any] = {"limit": limit}
    if customer:
        params["customer"] = customer
    if payment_intent:
        params["payment_intent"] = payment_intent
    if starting_after:
        params["starting_after"] = starting_after
    status, payload = client.request("GET", "/v1/charges", params)
    return _ok_or_error(status, payload)


@mcp.tool()
def create_refund(
    charge: Optional[str] = None,
    payment_intent: Optional[str] = None,
    amount: Optional[int] = None,
    reason: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """POST /v1/refunds"""
    params: Dict[str, Any] = {}
    if charge is not None:
        params["charge"] = charge
    if payment_intent is not None:
        params["payment_intent"] = payment_intent
    if amount is not None:
        params["amount"] = amount
    if reason is not None:
        params["reason"] = reason
    if metadata is not None:
        params["metadata"] = metadata
    status, payload = client.request("POST", "/v1/refunds", params)
    return _ok_or_error(status, payload)


@mcp.tool()
def get_refund(refund_id: str) -> Dict[str, Any]:
    """GET /v1/refunds/{refund}"""
    status, payload = client.request("GET", f"/v1/refunds/{refund_id}")
    return _ok_or_error(status, payload)


@mcp.tool()
def update_refund(refund_id: str, updates: Dict[str, Any]) -> Dict[str, Any]:
    """POST /v1/refunds/{refund}"""
    status, payload = client.request("POST", f"/v1/refunds/{refund_id}", updates)
    return _ok_or_error(status, payload)


@mcp.tool()
def list_refunds(limit: int = 10, charge: Optional[str] = None, payment_intent: Optional[str] = None, starting_after: Optional[str] = None) -> Dict[str, Any]:
    """GET /v1/refunds"""
    params: Dict[str, Any] = {"limit": limit}
    if charge:
        params["charge"] = charge
    if payment_intent:
        params["payment_intent"] = payment_intent
    if starting_after:
        params["starting_after"] = starting_after
    status, payload = client.request("GET", "/v1/refunds", params)
    return _ok_or_error(status, payload)


# -------------------- Subscriptions & Invoices --------------------

@mcp.tool()
def create_subscription(
    customer: str,
    items: list,
    default_payment_method: Optional[str] = None,
    trial_period_days: Optional[int] = None,
    metadata: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """POST /v1/subscriptions"""
    params: Dict[str, Any] = {"customer": customer, "items": items}
    if default_payment_method is not None:
        params["default_payment_method"] = default_payment_method
    if trial_period_days is not None:
        params["trial_period_days"] = trial_period_days
    if metadata is not None:
        params["metadata"] = metadata
    status, payload = client.request("POST", "/v1/subscriptions", params)
    return _ok_or_error(status, payload)


@mcp.tool()
def get_subscription(subscription_id: str) -> Dict[str, Any]:
    """GET /v1/subscriptions/{subscription_exposed_id}"""
    status, payload = client.request("GET", f"/v1/subscriptions/{subscription_id}")
    return _ok_or_error(status, payload)


@mcp.tool()
def update_subscription(subscription_id: str, updates: Dict[str, Any]) -> Dict[str, Any]:
    """POST /v1/subscriptions/{subscription_exposed_id}"""
    status, payload = client.request("POST", f"/v1/subscriptions/{subscription_id}", updates)
    return _ok_or_error(status, payload)


@mcp.tool()
def cancel_subscription(subscription_id: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """DELETE /v1/subscriptions/{subscription_exposed_id}"""
    status, payload = client.request("DELETE", f"/v1/subscriptions/{subscription_id}", params or {})
    return _ok_or_error(status, payload)


@mcp.tool()
def list_subscriptions(limit: int = 10, customer: Optional[str] = None, status_filter: Optional[str] = None, starting_after: Optional[str] = None) -> Dict[str, Any]:
    """GET /v1/subscriptions"""
    params: Dict[str, Any] = {"limit": limit}
    if customer:
        params["customer"] = customer
    if status_filter:
        params["status"] = status_filter
    if starting_after:
        params["starting_after"] = starting_after
    status, payload = client.request("GET", "/v1/subscriptions", params)
    return _ok_or_error(status, payload)


@mcp.tool()
def create_invoice(customer: str, auto_advance: Optional[bool] = None, metadata: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """POST /v1/invoices"""
    params: Dict[str, Any] = {"customer": customer}
    if auto_advance is not None:
        params["auto_advance"] = auto_advance
    if metadata is not None:
        params["metadata"] = metadata
    status, payload = client.request("POST", "/v1/invoices", params)
    return _ok_or_error(status, payload)


@mcp.tool()
def get_invoice(invoice_id: str) -> Dict[str, Any]:
    """GET /v1/invoices/{invoice}"""
    status, payload = client.request("GET", f"/v1/invoices/{invoice_id}")
    return _ok_or_error(status, payload)


@mcp.tool()
def update_invoice(invoice_id: str, updates: Dict[str, Any]) -> Dict[str, Any]:
    """POST /v1/invoices/{invoice}"""
    status, payload = client.request("POST", f"/v1/invoices/{invoice_id}", updates)
    return _ok_or_error(status, payload)


@mcp.tool()
def finalize_invoice(invoice_id: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """POST /v1/invoices/{invoice}/finalize"""
    status, payload = client.request("POST", f"/v1/invoices/{invoice_id}/finalize", params or {})
    return _ok_or_error(status, payload)


@mcp.tool()
def pay_invoice(invoice_id: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """POST /v1/invoices/{invoice}/pay"""
    status, payload = client.request("POST", f"/v1/invoices/{invoice_id}/pay", params or {})
    return _ok_or_error(status, payload)


@mcp.tool()
def void_invoice(invoice_id: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """POST /v1/invoices/{invoice}/void"""
    status, payload = client.request("POST", f"/v1/invoices/{invoice_id}/void", params or {})
    return _ok_or_error(status, payload)


@mcp.tool()
def list_invoices(limit: int = 10, customer: Optional[str] = None, status_filter: Optional[str] = None, starting_after: Optional[str] = None) -> Dict[str, Any]:
    """GET /v1/invoices"""
    params: Dict[str, Any] = {"limit": limit}
    if customer:
        params["customer"] = customer
    if status_filter:
        params["status"] = status_filter
    if starting_after:
        params["starting_after"] = starting_after
    status, payload = client.request("GET", "/v1/invoices", params)
    return _ok_or_error(status, payload)


# -------------------- Checkout Sessions & Payment Links --------------------

@mcp.tool()
def create_checkout_session(
    mode: str,
    success_url: str,
    cancel_url: str,
    line_items: list,
    customer: Optional[str] = None,
    customer_email: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """POST /v1/checkout/sessions"""
    params: Dict[str, Any] = {
        "mode": mode,
        "success_url": success_url,
        "cancel_url": cancel_url,
        "line_items": line_items,
    }
    if customer is not None:
        params["customer"] = customer
    if customer_email is not None:
        params["customer_email"] = customer_email
    if metadata is not None:
        params["metadata"] = metadata
    status, payload = client.request("POST", "/v1/checkout/sessions", params)
    return _ok_or_error(status, payload)


@mcp.tool()
def get_checkout_session(session_id: str) -> Dict[str, Any]:
    """GET /v1/checkout/sessions/{id}"""
    status, payload = client.request("GET", f"/v1/checkout/sessions/{session_id}")
    return _ok_or_error(status, payload)


@mcp.tool()
def list_checkout_sessions(limit: int = 10, starting_after: Optional[str] = None) -> Dict[str, Any]:
    """GET /v1/checkout/sessions"""
    params: Dict[str, Any] = {"limit": limit}
    if starting_after:
        params["starting_after"] = starting_after
    status, payload = client.request("GET", "/v1/checkout/sessions", params)
    return _ok_or_error(status, payload)


@mcp.tool()
def create_payment_link(line_items: list, after_completion: Optional[Dict[str, Any]] = None, metadata: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """POST /v1/payment_links"""
    params: Dict[str, Any] = {"line_items": line_items}
    if after_completion is not None:
        params["after_completion"] = after_completion
    if metadata is not None:
        params["metadata"] = metadata
    status, payload = client.request("POST", "/v1/payment_links", params)
    return _ok_or_error(status, payload)


@mcp.tool()
def get_payment_link(payment_link_id: str) -> Dict[str, Any]:
    """GET /v1/payment_links/{payment_link}"""
    status, payload = client.request("GET", f"/v1/payment_links/{payment_link_id}")
    return _ok_or_error(status, payload)


@mcp.tool()
def list_payment_links(limit: int = 10, starting_after: Optional[str] = None, active: Optional[bool] = None) -> Dict[str, Any]:
    """GET /v1/payment_links"""
    params: Dict[str, Any] = {"limit": limit}
    if starting_after:
        params["starting_after"] = starting_after
    if active is not None:
        params["active"] = active
    status, payload = client.request("GET", "/v1/payment_links", params)
    return _ok_or_error(status, payload)


# -------------------- Setup Intents --------------------

@mcp.tool()
def create_setup_intent(customer: Optional[str] = None, payment_method_types: Optional[list] = None, usage: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """POST /v1/setup_intents"""
    params: Dict[str, Any] = {}
    if customer is not None:
        params["customer"] = customer
    if payment_method_types is not None:
        params["payment_method_types"] = payment_method_types
    if usage is not None:
        params["usage"] = usage
    if metadata is not None:
        params["metadata"] = metadata
    status, payload = client.request("POST", "/v1/setup_intents", params)
    return _ok_or_error(status, payload)


@mcp.tool()
def get_setup_intent(setup_intent_id: str) -> Dict[str, Any]:
    """GET /v1/setup_intents/{intent}"""
    status, payload = client.request("GET", f"/v1/setup_intents/{setup_intent_id}")
    return _ok_or_error(status, payload)


@mcp.tool()
def confirm_setup_intent(setup_intent_id: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """POST /v1/setup_intents/{intent}/confirm"""
    status, payload = client.request("POST", f"/v1/setup_intents/{setup_intent_id}/confirm", params or {})
    return _ok_or_error(status, payload)


# -------------------- Coupons & Promotion Codes --------------------

@mcp.tool()
def create_coupon(
    duration: str,
    percent_off: Optional[float] = None,
    amount_off: Optional[int] = None,
    currency: Optional[str] = None,
    name: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """POST /v1/coupons"""
    params: Dict[str, Any] = {"duration": duration}
    if percent_off is not None:
        params["percent_off"] = percent_off
    if amount_off is not None:
        params["amount_off"] = amount_off
    if currency is not None:
        params["currency"] = currency
    if name is not None:
        params["name"] = name
    if metadata is not None:
        params["metadata"] = metadata
    status, payload = client.request("POST", "/v1/coupons", params)
    return _ok_or_error(status, payload)


@mcp.tool()
def get_coupon(coupon_id: str) -> Dict[str, Any]:
    """GET /v1/coupons/{coupon}"""
    status, payload = client.request("GET", f"/v1/coupons/{coupon_id}")
    return _ok_or_error(status, payload)


@mcp.tool()
def list_coupons(limit: int = 10, starting_after: Optional[str] = None) -> Dict[str, Any]:
    """GET /v1/coupons"""
    params: Dict[str, Any] = {"limit": limit}
    if starting_after:
        params["starting_after"] = starting_after
    status, payload = client.request("GET", "/v1/coupons", params)
    return _ok_or_error(status, payload)


@mcp.tool()
def create_promotion_code(
    coupon: str,
    code: Optional[str] = None,
    max_redemptions: Optional[int] = None,
    expires_at: Optional[int] = None,
    metadata: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """POST /v1/promotion_codes"""
    params: Dict[str, Any] = {"coupon": coupon}
    if code is not None:
        params["code"] = code
    if max_redemptions is not None:
        params["max_redemptions"] = max_redemptions
    if expires_at is not None:
        params["expires_at"] = expires_at
    if metadata is not None:
        params["metadata"] = metadata
    status, payload = client.request("POST", "/v1/promotion_codes", params)
    return _ok_or_error(status, payload)


@mcp.tool()
def get_promotion_code(promotion_code_id: str) -> Dict[str, Any]:
    """GET /v1/promotion_codes/{promotion_code}"""
    status, payload = client.request("GET", f"/v1/promotion_codes/{promotion_code_id}")
    return _ok_or_error(status, payload)


@mcp.tool()
def list_promotion_codes(limit: int = 10, coupon: Optional[str] = None, code: Optional[str] = None, starting_after: Optional[str] = None) -> Dict[str, Any]:
    """GET /v1/promotion_codes"""
    params: Dict[str, Any] = {"limit": limit}
    if coupon:
        params["coupon"] = coupon
    if code:
        params["code"] = code
    if starting_after:
        params["starting_after"] = starting_after
    status, payload = client.request("GET", "/v1/promotion_codes", params)
    return _ok_or_error(status, payload)


# -------------------- Connect: Accounts, Transfers, Payouts --------------------

@mcp.tool()
def create_account(type: str = "express", country: Optional[str] = None, email: Optional[str] = None, capabilities: Optional[Dict[str, Any]] = None, metadata: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """POST /v1/accounts"""
    params: Dict[str, Any] = {"type": type}
    if country is not None:
        params["country"] = country
    if email is not None:
        params["email"] = email
    if capabilities is not None:
        params["capabilities"] = capabilities
    if metadata is not None:
        params["metadata"] = metadata
    status, payload = client.request("POST", "/v1/accounts", params)
    return _ok_or_error(status, payload)


@mcp.tool()
def get_account(account_id: str) -> Dict[str, Any]:
    """GET /v1/accounts/{account}"""
    status, payload = client.request("GET", f"/v1/accounts/{account_id}")
    return _ok_or_error(status, payload)


@mcp.tool()
def update_account(account_id: str, updates: Dict[str, Any]) -> Dict[str, Any]:
    """POST /v1/accounts/{account}"""
    status, payload = client.request("POST", f"/v1/accounts/{account_id}", updates)
    return _ok_or_error(status, payload)


@mcp.tool()
def create_transfer(amount: int, currency: str, destination: str, source_transaction: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """POST /v1/transfers"""
    params: Dict[str, Any] = {"amount": amount, "currency": currency, "destination": destination}
    if source_transaction is not None:
        params["source_transaction"] = source_transaction
    if metadata is not None:
        params["metadata"] = metadata
    status, payload = client.request("POST", "/v1/transfers", params)
    return _ok_or_error(status, payload)


@mcp.tool()
def get_transfer(transfer_id: str) -> Dict[str, Any]:
    """GET /v1/transfers/{transfer}"""
    status, payload = client.request("GET", f"/v1/transfers/{transfer_id}")
    return _ok_or_error(status, payload)


@mcp.tool()
def list_transfers(limit: int = 10, destination: Optional[str] = None, starting_after: Optional[str] = None) -> Dict[str, Any]:
    """GET /v1/transfers"""
    params: Dict[str, Any] = {"limit": limit}
    if destination:
        params["destination"] = destination
    if starting_after:
        params["starting_after"] = starting_after
    status, payload = client.request("GET", "/v1/transfers", params)
    return _ok_or_error(status, payload)


@mcp.tool()
def create_payout(amount: int, currency: str, destination: Optional[str] = None, method: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    """POST /v1/payouts"""
    params: Dict[str, Any] = {"amount": amount, "currency": currency}
    if destination is not None:
        params["destination"] = destination
    if method is not None:
        params["method"] = method
    if metadata is not None:
        params["metadata"] = metadata
    status, payload = client.request("POST", "/v1/payouts", params, stripe_account=stripe_account)
    return _ok_or_error(status, payload)


@mcp.tool()
def get_payout(payout_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    """GET /v1/payouts/{payout}"""
    status, payload = client.request("GET", f"/v1/payouts/{payout_id}", stripe_account=stripe_account)
    return _ok_or_error(status, payload)


@mcp.tool()
def list_payouts(limit: int = 10, starting_after: Optional[str] = None, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    """GET /v1/payouts"""
    params: Dict[str, Any] = {"limit": limit}
    if starting_after:
        params["starting_after"] = starting_after
    status, payload = client.request("GET", "/v1/payouts", params, stripe_account=stripe_account)
    return _ok_or_error(status, payload)


def main():
    # FastMCP uses stdio by default when run as a script.
    mcp.run()


if __name__ == "__main__":
    main()
