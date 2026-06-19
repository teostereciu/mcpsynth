#!/usr/bin/env python3
"""
MCP Server for Stripe API
Provides tools for interacting with Stripe's REST API
"""

import os
import json
import requests
from typing import Any, Optional
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
server = FastMCP("stripe-api")

# Configuration
STRIPE_API_KEY = os.getenv("STRIPE_API_KEY", "")
BASE_URL = "https://api.stripe.com/v1"

def make_request(
    method: str,
    endpoint: str,
    params: Optional[dict] = None,
    data: Optional[dict] = None,
) -> dict:
    """Make an authenticated request to the Stripe API."""
    url = f"{BASE_URL}{endpoint}"
    headers = {
        "Authorization": f"Bearer {STRIPE_API_KEY}",
    }
    
    try:
        if method == "GET":
            response = requests.get(url, headers=headers, params=params, timeout=30)
        elif method == "POST":
            response = requests.post(url, headers=headers, data=data, timeout=30)
        elif method == "DELETE":
            response = requests.delete(url, headers=headers, timeout=30)
        else:
            return {"error": f"Unsupported HTTP method: {method}"}
        
        if response.status_code >= 400:
            try:
                error_data = response.json()
                return {"error": error_data.get("error", {}).get("message", response.text)}
            except:
                return {"error": f"HTTP {response.status_code}: {response.text}"}
        
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}
    except Exception as e:
        return {"error": f"Unexpected error: {str(e)}"}


# ============================================================================
# CUSTOMERS
# ============================================================================

@server.tool()
def create_customer(
    email: Optional[str] = None,
    name: Optional[str] = None,
    description: Optional[str] = None,
    phone: Optional[str] = None,
    metadata: Optional[dict] = None,
) -> dict:
    """Create a new customer."""
    data = {}
    if email:
        data["email"] = email
    if name:
        data["name"] = name
    if description:
        data["description"] = description
    if phone:
        data["phone"] = phone
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return make_request("POST", "/customers", data=data)


@server.tool()
def get_customer(customer_id: str) -> dict:
    """Retrieve a customer by ID."""
    return make_request("GET", f"/customers/{customer_id}")


@server.tool()
def update_customer(
    customer_id: str,
    email: Optional[str] = None,
    name: Optional[str] = None,
    description: Optional[str] = None,
    phone: Optional[str] = None,
    metadata: Optional[dict] = None,
) -> dict:
    """Update a customer."""
    data = {}
    if email is not None:
        data["email"] = email
    if name is not None:
        data["name"] = name
    if description is not None:
        data["description"] = description
    if phone is not None:
        data["phone"] = phone
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return make_request("POST", f"/customers/{customer_id}", data=data)


@server.tool()
def list_customers(limit: int = 10) -> dict:
    """List customers."""
    return make_request("GET", "/customers", params={"limit": limit})


@server.tool()
def delete_customer(customer_id: str) -> dict:
    """Delete a customer."""
    return make_request("DELETE", f"/customers/{customer_id}")


# ============================================================================
# PAYMENT INTENTS
# ============================================================================

@server.tool()
def create_payment_intent(
    amount: int,
    currency: str,
    customer: Optional[str] = None,
    description: Optional[str] = None,
    payment_method: Optional[str] = None,
    confirm: bool = False,
    metadata: Optional[dict] = None,
) -> dict:
    """Create a payment intent."""
    data = {
        "amount": amount,
        "currency": currency,
    }
    if customer:
        data["customer"] = customer
    if description:
        data["description"] = description
    if payment_method:
        data["payment_method"] = payment_method
    if confirm:
        data["confirm"] = "true"
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return make_request("POST", "/payment_intents", data=data)


@server.tool()
def get_payment_intent(payment_intent_id: str) -> dict:
    """Retrieve a payment intent."""
    return make_request("GET", f"/payment_intents/{payment_intent_id}")


@server.tool()
def confirm_payment_intent(
    payment_intent_id: str,
    payment_method: Optional[str] = None,
) -> dict:
    """Confirm a payment intent."""
    data = {}
    if payment_method:
        data["payment_method"] = payment_method
    
    return make_request("POST", f"/payment_intents/{payment_intent_id}/confirm", data=data)


@server.tool()
def cancel_payment_intent(payment_intent_id: str) -> dict:
    """Cancel a payment intent."""
    return make_request("POST", f"/payment_intents/{payment_intent_id}/cancel", data={})


@server.tool()
def list_payment_intents(limit: int = 10) -> dict:
    """List payment intents."""
    return make_request("GET", "/payment_intents", params={"limit": limit})


# ============================================================================
# CHARGES
# ============================================================================

@server.tool()
def create_charge(
    amount: int,
    currency: str,
    customer: Optional[str] = None,
    source: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[dict] = None,
) -> dict:
    """Create a charge (deprecated - use Payment Intents instead)."""
    data = {
        "amount": amount,
        "currency": currency,
    }
    if customer:
        data["customer"] = customer
    if source:
        data["source"] = source
    if description:
        data["description"] = description
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return make_request("POST", "/charges", data=data)


@server.tool()
def get_charge(charge_id: str) -> dict:
    """Retrieve a charge."""
    return make_request("GET", f"/charges/{charge_id}")


@server.tool()
def update_charge(
    charge_id: str,
    description: Optional[str] = None,
    metadata: Optional[dict] = None,
) -> dict:
    """Update a charge."""
    data = {}
    if description is not None:
        data["description"] = description
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return make_request("POST", f"/charges/{charge_id}", data=data)


@server.tool()
def list_charges(limit: int = 10) -> dict:
    """List charges."""
    return make_request("GET", "/charges", params={"limit": limit})


# ============================================================================
# REFUNDS
# ============================================================================

@server.tool()
def create_refund(
    charge: Optional[str] = None,
    payment_intent: Optional[str] = None,
    amount: Optional[int] = None,
    reason: Optional[str] = None,
    metadata: Optional[dict] = None,
) -> dict:
    """Create a refund."""
    data = {}
    if charge:
        data["charge"] = charge
    if payment_intent:
        data["payment_intent"] = payment_intent
    if amount is not None:
        data["amount"] = amount
    if reason:
        data["reason"] = reason
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return make_request("POST", "/refunds", data=data)


@server.tool()
def get_refund(refund_id: str) -> dict:
    """Retrieve a refund."""
    return make_request("GET", f"/refunds/{refund_id}")


@server.tool()
def update_refund(
    refund_id: str,
    metadata: Optional[dict] = None,
) -> dict:
    """Update a refund."""
    data = {}
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return make_request("POST", f"/refunds/{refund_id}", data=data)


@server.tool()
def list_refunds(limit: int = 10) -> dict:
    """List refunds."""
    return make_request("GET", "/refunds", params={"limit": limit})


# ============================================================================
# PRODUCTS
# ============================================================================

@server.tool()
def create_product(
    name: str,
    description: Optional[str] = None,
    active: bool = True,
    metadata: Optional[dict] = None,
) -> dict:
    """Create a product."""
    data = {
        "name": name,
        "active": "true" if active else "false",
    }
    if description:
        data["description"] = description
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return make_request("POST", "/products", data=data)


@server.tool()
def get_product(product_id: str) -> dict:
    """Retrieve a product."""
    return make_request("GET", f"/products/{product_id}")


@server.tool()
def update_product(
    product_id: str,
    name: Optional[str] = None,
    description: Optional[str] = None,
    active: Optional[bool] = None,
    metadata: Optional[dict] = None,
) -> dict:
    """Update a product."""
    data = {}
    if name is not None:
        data["name"] = name
    if description is not None:
        data["description"] = description
    if active is not None:
        data["active"] = "true" if active else "false"
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return make_request("POST", f"/products/{product_id}", data=data)


@server.tool()
def list_products(limit: int = 10) -> dict:
    """List products."""
    return make_request("GET", "/products", params={"limit": limit})


# ============================================================================
# PRICES
# ============================================================================

@server.tool()
def create_price(
    currency: str,
    product: Optional[str] = None,
    unit_amount: Optional[int] = None,
    recurring: Optional[dict] = None,
    active: bool = True,
    metadata: Optional[dict] = None,
) -> dict:
    """Create a price."""
    data = {
        "currency": currency,
        "active": "true" if active else "false",
    }
    if product:
        data["product"] = product
    if unit_amount is not None:
        data["unit_amount"] = unit_amount
    if recurring:
        for key, value in recurring.items():
            data[f"recurring[{key}]"] = value
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return make_request("POST", "/prices", data=data)


@server.tool()
def get_price(price_id: str) -> dict:
    """Retrieve a price."""
    return make_request("GET", f"/prices/{price_id}")


@server.tool()
def update_price(
    price_id: str,
    active: Optional[bool] = None,
    metadata: Optional[dict] = None,
) -> dict:
    """Update a price."""
    data = {}
    if active is not None:
        data["active"] = "true" if active else "false"
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return make_request("POST", f"/prices/{price_id}", data=data)


@server.tool()
def list_prices(limit: int = 10) -> dict:
    """List prices."""
    return make_request("GET", "/prices", params={"limit": limit})


# ============================================================================
# SUBSCRIPTIONS
# ============================================================================

@server.tool()
def create_subscription(
    customer: str,
    items: list,
    currency: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[dict] = None,
) -> dict:
    """Create a subscription."""
    data = {
        "customer": customer,
    }
    if currency:
        data["currency"] = currency
    if description:
        data["description"] = description
    
    # Add items
    for i, item in enumerate(items):
        if "price" in item:
            data[f"items[{i}][price]"] = item["price"]
        if "quantity" in item:
            data[f"items[{i}][quantity]"] = item["quantity"]
    
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return make_request("POST", "/subscriptions", data=data)


@server.tool()
def get_subscription(subscription_id: str) -> dict:
    """Retrieve a subscription."""
    return make_request("GET", f"/subscriptions/{subscription_id}")


@server.tool()
def update_subscription(
    subscription_id: str,
    description: Optional[str] = None,
    metadata: Optional[dict] = None,
) -> dict:
    """Update a subscription."""
    data = {}
    if description is not None:
        data["description"] = description
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return make_request("POST", f"/subscriptions/{subscription_id}", data=data)


@server.tool()
def cancel_subscription(subscription_id: str) -> dict:
    """Cancel a subscription."""
    return make_request("DELETE", f"/subscriptions/{subscription_id}")


@server.tool()
def list_subscriptions(limit: int = 10) -> dict:
    """List subscriptions."""
    return make_request("GET", "/subscriptions", params={"limit": limit})


# ============================================================================
# INVOICES
# ============================================================================

@server.tool()
def create_invoice(
    customer: str,
    description: Optional[str] = None,
    metadata: Optional[dict] = None,
) -> dict:
    """Create an invoice."""
    data = {
        "customer": customer,
    }
    if description:
        data["description"] = description
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return make_request("POST", "/invoices", data=data)


@server.tool()
def get_invoice(invoice_id: str) -> dict:
    """Retrieve an invoice."""
    return make_request("GET", f"/invoices/{invoice_id}")


@server.tool()
def finalize_invoice(invoice_id: str) -> dict:
    """Finalize an invoice."""
    return make_request("POST", f"/invoices/{invoice_id}/finalize", data={})


@server.tool()
def pay_invoice(invoice_id: str) -> dict:
    """Pay an invoice."""
    return make_request("POST", f"/invoices/{invoice_id}/pay", data={})


@server.tool()
def list_invoices(limit: int = 10) -> dict:
    """List invoices."""
    return make_request("GET", "/invoices", params={"limit": limit})


# ============================================================================
# PAYMENT METHODS
# ============================================================================

@server.tool()
def create_payment_method(
    type: str,
    card: Optional[dict] = None,
    billing_details: Optional[dict] = None,
    metadata: Optional[dict] = None,
) -> dict:
    """Create a payment method."""
    data = {
        "type": type,
    }
    if card:
        for key, value in card.items():
            data[f"card[{key}]"] = value
    if billing_details:
        for key, value in billing_details.items():
            data[f"billing_details[{key}]"] = value
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return make_request("POST", "/payment_methods", data=data)


@server.tool()
def get_payment_method(payment_method_id: str) -> dict:
    """Retrieve a payment method."""
    return make_request("GET", f"/payment_methods/{payment_method_id}")


@server.tool()
def attach_payment_method(
    payment_method_id: str,
    customer: str,
) -> dict:
    """Attach a payment method to a customer."""
    data = {
        "customer": customer,
    }
    return make_request("POST", f"/payment_methods/{payment_method_id}/attach", data=data)


@server.tool()
def detach_payment_method(payment_method_id: str) -> dict:
    """Detach a payment method."""
    return make_request("POST", f"/payment_methods/{payment_method_id}/detach", data={})


@server.tool()
def list_payment_methods(customer: str, type: str = "card") -> dict:
    """List payment methods for a customer."""
    return make_request("GET", f"/customers/{customer}/payment_methods", params={"type": type})


# ============================================================================
# COUPONS
# ============================================================================

@server.tool()
def create_coupon(
    percent_off: Optional[int] = None,
    amount_off: Optional[int] = None,
    currency: Optional[str] = None,
    duration: str = "once",
    metadata: Optional[dict] = None,
) -> dict:
    """Create a coupon."""
    data = {
        "duration": duration,
    }
    if percent_off is not None:
        data["percent_off"] = percent_off
    if amount_off is not None:
        data["amount_off"] = amount_off
    if currency:
        data["currency"] = currency
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return make_request("POST", "/coupons", data=data)


@server.tool()
def get_coupon(coupon_id: str) -> dict:
    """Retrieve a coupon."""
    return make_request("GET", f"/coupons/{coupon_id}")


@server.tool()
def delete_coupon(coupon_id: str) -> dict:
    """Delete a coupon."""
    return make_request("DELETE", f"/coupons/{coupon_id}")


@server.tool()
def list_coupons(limit: int = 10) -> dict:
    """List coupons."""
    return make_request("GET", "/coupons", params={"limit": limit})


# ============================================================================
# PROMOTION CODES
# ============================================================================

@server.tool()
def create_promotion_code(
    coupon: str,
    code: Optional[str] = None,
    active: bool = True,
    metadata: Optional[dict] = None,
) -> dict:
    """Create a promotion code."""
    data = {
        "coupon": coupon,
        "active": "true" if active else "false",
    }
    if code:
        data["code"] = code
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return make_request("POST", "/promotion_codes", data=data)


@server.tool()
def get_promotion_code(promotion_code_id: str) -> dict:
    """Retrieve a promotion code."""
    return make_request("GET", f"/promotion_codes/{promotion_code_id}")


@server.tool()
def update_promotion_code(
    promotion_code_id: str,
    active: Optional[bool] = None,
    metadata: Optional[dict] = None,
) -> dict:
    """Update a promotion code."""
    data = {}
    if active is not None:
        data["active"] = "true" if active else "false"
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return make_request("POST", f"/promotion_codes/{promotion_code_id}", data=data)


@server.tool()
def list_promotion_codes(limit: int = 10) -> dict:
    """List promotion codes."""
    return make_request("GET", "/promotion_codes", params={"limit": limit})


# ============================================================================
# SETUP INTENTS
# ============================================================================

@server.tool()
def create_setup_intent(
    customer: Optional[str] = None,
    payment_method: Optional[str] = None,
    confirm: bool = False,
    metadata: Optional[dict] = None,
) -> dict:
    """Create a setup intent."""
    data = {}
    if customer:
        data["customer"] = customer
    if payment_method:
        data["payment_method"] = payment_method
    if confirm:
        data["confirm"] = "true"
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return make_request("POST", "/setup_intents", data=data)


@server.tool()
def get_setup_intent(setup_intent_id: str) -> dict:
    """Retrieve a setup intent."""
    return make_request("GET", f"/setup_intents/{setup_intent_id}")


@server.tool()
def confirm_setup_intent(
    setup_intent_id: str,
    payment_method: Optional[str] = None,
) -> dict:
    """Confirm a setup intent."""
    data = {}
    if payment_method:
        data["payment_method"] = payment_method
    
    return make_request("POST", f"/setup_intents/{setup_intent_id}/confirm", data=data)


@server.tool()
def list_setup_intents(limit: int = 10) -> dict:
    """List setup intents."""
    return make_request("GET", "/setup_intents", params={"limit": limit})


# ============================================================================
# CHECKOUT SESSIONS
# ============================================================================

@server.tool()
def create_checkout_session(
    payment_method_types: list,
    line_items: list,
    mode: str = "payment",
    success_url: Optional[str] = None,
    cancel_url: Optional[str] = None,
    customer: Optional[str] = None,
    metadata: Optional[dict] = None,
) -> dict:
    """Create a checkout session."""
    data = {
        "mode": mode,
    }
    
    # Add payment method types
    for i, pmt_type in enumerate(payment_method_types):
        data[f"payment_method_types[{i}]"] = pmt_type
    
    # Add line items
    for i, item in enumerate(line_items):
        if "price" in item:
            data[f"line_items[{i}][price]"] = item["price"]
        if "quantity" in item:
            data[f"line_items[{i}][quantity]"] = item["quantity"]
    
    if success_url:
        data["success_url"] = success_url
    if cancel_url:
        data["cancel_url"] = cancel_url
    if customer:
        data["customer"] = customer
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return make_request("POST", "/checkout/sessions", data=data)


@server.tool()
def get_checkout_session(session_id: str) -> dict:
    """Retrieve a checkout session."""
    return make_request("GET", f"/checkout/sessions/{session_id}")


@server.tool()
def list_checkout_sessions(limit: int = 10) -> dict:
    """List checkout sessions."""
    return make_request("GET", "/checkout/sessions", params={"limit": limit})


# ============================================================================
# PAYMENT LINKS
# ============================================================================

@server.tool()
def create_payment_link(
    line_items: list,
    metadata: Optional[dict] = None,
) -> dict:
    """Create a payment link."""
    data = {}
    
    # Add line items
    for i, item in enumerate(line_items):
        if "price" in item:
            data[f"line_items[{i}][price]"] = item["price"]
        if "quantity" in item:
            data[f"line_items[{i}][quantity]"] = item["quantity"]
    
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return make_request("POST", "/payment_links", data=data)


@server.tool()
def get_payment_link(payment_link_id: str) -> dict:
    """Retrieve a payment link."""
    return make_request("GET", f"/payment_links/{payment_link_id}")


@server.tool()
def update_payment_link(
    payment_link_id: str,
    active: Optional[bool] = None,
    metadata: Optional[dict] = None,
) -> dict:
    """Update a payment link."""
    data = {}
    if active is not None:
        data["active"] = "true" if active else "false"
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return make_request("POST", f"/payment_links/{payment_link_id}", data=data)


@server.tool()
def list_payment_links(limit: int = 10) -> dict:
    """List payment links."""
    return make_request("GET", "/payment_links", params={"limit": limit})


# ============================================================================
# TRANSFERS (Connect)
# ============================================================================

@server.tool()
def create_transfer(
    amount: int,
    currency: str,
    destination: str,
    description: Optional[str] = None,
    metadata: Optional[dict] = None,
) -> dict:
    """Create a transfer to a connected account."""
    data = {
        "amount": amount,
        "currency": currency,
        "destination": destination,
    }
    if description:
        data["description"] = description
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return make_request("POST", "/transfers", data=data)


@server.tool()
def get_transfer(transfer_id: str) -> dict:
    """Retrieve a transfer."""
    return make_request("GET", f"/transfers/{transfer_id}")


@server.tool()
def update_transfer(
    transfer_id: str,
    description: Optional[str] = None,
    metadata: Optional[dict] = None,
) -> dict:
    """Update a transfer."""
    data = {}
    if description is not None:
        data["description"] = description
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return make_request("POST", f"/transfers/{transfer_id}", data=data)


@server.tool()
def list_transfers(limit: int = 10) -> dict:
    """List transfers."""
    return make_request("GET", "/transfers", params={"limit": limit})


# ============================================================================
# PAYOUTS
# ============================================================================

@server.tool()
def create_payout(
    amount: int,
    currency: str,
    method: str = "standard",
    description: Optional[str] = None,
    metadata: Optional[dict] = None,
) -> dict:
    """Create a payout."""
    data = {
        "amount": amount,
        "currency": currency,
        "method": method,
    }
    if description:
        data["description"] = description
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return make_request("POST", "/payouts", data=data)


@server.tool()
def get_payout(payout_id: str) -> dict:
    """Retrieve a payout."""
    return make_request("GET", f"/payouts/{payout_id}")


@server.tool()
def cancel_payout(payout_id: str) -> dict:
    """Cancel a payout."""
    return make_request("POST", f"/payouts/{payout_id}/cancel", data={})


@server.tool()
def list_payouts(limit: int = 10) -> dict:
    """List payouts."""
    return make_request("GET", "/payouts", params={"limit": limit})


# ============================================================================
# ACCOUNTS (Connect)
# ============================================================================

@server.tool()
def create_connected_account(
    type: str,
    country: str,
    email: str,
    metadata: Optional[dict] = None,
) -> dict:
    """Create a connected account."""
    data = {
        "type": type,
        "country": country,
        "email": email,
    }
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return make_request("POST", "/accounts", data=data)


@server.tool()
def get_account(account_id: str) -> dict:
    """Retrieve an account."""
    return make_request("GET", f"/accounts/{account_id}")


@server.tool()
def update_account(
    account_id: str,
    metadata: Optional[dict] = None,
) -> dict:
    """Update an account."""
    data = {}
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return make_request("POST", f"/accounts/{account_id}", data=data)


# ============================================================================
# DISPUTES
# ============================================================================

@server.tool()
def get_dispute(dispute_id: str) -> dict:
    """Retrieve a dispute."""
    return make_request("GET", f"/disputes/{dispute_id}")


@server.tool()
def update_dispute(
    dispute_id: str,
    evidence: Optional[dict] = None,
    metadata: Optional[dict] = None,
) -> dict:
    """Update a dispute."""
    data = {}
    if evidence:
        for key, value in evidence.items():
            data[f"evidence[{key}]"] = value
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return make_request("POST", f"/disputes/{dispute_id}", data=data)


@server.tool()
def close_dispute(dispute_id: str) -> dict:
    """Close a dispute."""
    return make_request("POST", f"/disputes/{dispute_id}/close", data={})


@server.tool()
def list_disputes(limit: int = 10) -> dict:
    """List disputes."""
    return make_request("GET", "/disputes", params={"limit": limit})


# ============================================================================
# BALANCE
# ============================================================================

@server.tool()
def get_balance() -> dict:
    """Retrieve account balance."""
    return make_request("GET", "/balance")


@server.tool()
def list_balance_transactions(limit: int = 10) -> dict:
    """List balance transactions."""
    return make_request("GET", "/balance_transactions", params={"limit": limit})


# ============================================================================
# EVENTS
# ============================================================================

@server.tool()
def get_event(event_id: str) -> dict:
    """Retrieve an event."""
    return make_request("GET", f"/events/{event_id}")


@server.tool()
def list_events(limit: int = 10) -> dict:
    """List events."""
    return make_request("GET", "/events", params={"limit": limit})


# ============================================================================
# SUBSCRIPTION ITEMS
# ============================================================================

@server.tool()
def create_subscription_item(
    subscription: str,
    price: Optional[str] = None,
    quantity: Optional[int] = None,
    metadata: Optional[dict] = None,
) -> dict:
    """Create a subscription item."""
    data = {
        "subscription": subscription,
    }
    if price:
        data["price"] = price
    if quantity is not None:
        data["quantity"] = quantity
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return make_request("POST", "/subscription_items", data=data)


@server.tool()
def get_subscription_item(subscription_item_id: str) -> dict:
    """Retrieve a subscription item."""
    return make_request("GET", f"/subscription_items/{subscription_item_id}")


@server.tool()
def update_subscription_item(
    subscription_item_id: str,
    price: Optional[str] = None,
    quantity: Optional[int] = None,
    metadata: Optional[dict] = None,
) -> dict:
    """Update a subscription item."""
    data = {}
    if price:
        data["price"] = price
    if quantity is not None:
        data["quantity"] = quantity
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return make_request("POST", f"/subscription_items/{subscription_item_id}", data=data)


@server.tool()
def delete_subscription_item(subscription_item_id: str) -> dict:
    """Delete a subscription item."""
    return make_request("DELETE", f"/subscription_items/{subscription_item_id}")


@server.tool()
def list_subscription_items(subscription: str, limit: int = 10) -> dict:
    """List subscription items for a subscription."""
    return make_request("GET", "/subscription_items", params={"subscription": subscription, "limit": limit})


# ============================================================================
# TAX CODES
# ============================================================================

@server.tool()
def get_tax_code(tax_code_id: str) -> dict:
    """Retrieve a tax code."""
    return make_request("GET", f"/tax_codes/{tax_code_id}")


@server.tool()
def list_tax_codes(limit: int = 10) -> dict:
    """List tax codes."""
    return make_request("GET", "/tax_codes", params={"limit": limit})


# ============================================================================
# TAX RATES
# ============================================================================

@server.tool()
def create_tax_rate(
    display_name: str,
    percentage: float,
    jurisdiction: Optional[str] = None,
    inclusive: bool = False,
    metadata: Optional[dict] = None,
) -> dict:
    """Create a tax rate."""
    data = {
        "display_name": display_name,
        "percentage": percentage,
        "inclusive": "true" if inclusive else "false",
    }
    if jurisdiction:
        data["jurisdiction"] = jurisdiction
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return make_request("POST", "/tax_rates", data=data)


@server.tool()
def get_tax_rate(tax_rate_id: str) -> dict:
    """Retrieve a tax rate."""
    return make_request("GET", f"/tax_rates/{tax_rate_id}")


@server.tool()
def update_tax_rate(
    tax_rate_id: str,
    display_name: Optional[str] = None,
    metadata: Optional[dict] = None,
) -> dict:
    """Update a tax rate."""
    data = {}
    if display_name is not None:
        data["display_name"] = display_name
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return make_request("POST", f"/tax_rates/{tax_rate_id}", data=data)


@server.tool()
def list_tax_rates(limit: int = 10) -> dict:
    """List tax rates."""
    return make_request("GET", "/tax_rates", params={"limit": limit})


# ============================================================================
# CREDIT NOTES
# ============================================================================

@server.tool()
def create_credit_note(
    invoice: str,
    lines: Optional[list] = None,
    amount: Optional[int] = None,
    reason: Optional[str] = None,
    metadata: Optional[dict] = None,
) -> dict:
    """Create a credit note."""
    data = {
        "invoice": invoice,
    }
    if lines:
        for i, line in enumerate(lines):
            if "invoice_line_item" in line:
                data[f"lines[{i}][invoice_line_item]"] = line["invoice_line_item"]
            if "quantity" in line:
                data[f"lines[{i}][quantity]"] = line["quantity"]
    if amount is not None:
        data["amount"] = amount
    if reason:
        data["reason"] = reason
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return make_request("POST", "/credit_notes", data=data)


@server.tool()
def get_credit_note(credit_note_id: str) -> dict:
    """Retrieve a credit note."""
    return make_request("GET", f"/credit_notes/{credit_note_id}")


@server.tool()
def list_credit_notes(limit: int = 10) -> dict:
    """List credit notes."""
    return make_request("GET", "/credit_notes", params={"limit": limit})


# ============================================================================
# DISCOUNTS
# ============================================================================

@server.tool()
def create_discount(
    coupon: Optional[str] = None,
    promotion_code: Optional[str] = None,
    customer: Optional[str] = None,
    subscription: Optional[str] = None,
    invoice: Optional[str] = None,
) -> dict:
    """Create a discount."""
    data = {}
    if coupon:
        data["coupon"] = coupon
    if promotion_code:
        data["promotion_code"] = promotion_code
    if customer:
        data["customer"] = customer
    if subscription:
        data["subscription"] = subscription
    if invoice:
        data["invoice"] = invoice
    
    return make_request("POST", "/discounts", data=data)


@server.tool()
def delete_discount(discount_id: str) -> dict:
    """Delete a discount."""
    return make_request("DELETE", f"/discounts/{discount_id}")


# ============================================================================
# INVOICE ITEMS
# ============================================================================

@server.tool()
def create_invoice_item(
    customer: str,
    amount: Optional[int] = None,
    currency: Optional[str] = None,
    description: Optional[str] = None,
    invoice: Optional[str] = None,
    price: Optional[str] = None,
    quantity: Optional[int] = None,
    metadata: Optional[dict] = None,
) -> dict:
    """Create an invoice item."""
    data = {
        "customer": customer,
    }
    if amount is not None:
        data["amount"] = amount
    if currency:
        data["currency"] = currency
    if description:
        data["description"] = description
    if invoice:
        data["invoice"] = invoice
    if price:
        data["price"] = price
    if quantity is not None:
        data["quantity"] = quantity
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return make_request("POST", "/invoiceitems", data=data)


@server.tool()
def get_invoice_item(invoice_item_id: str) -> dict:
    """Retrieve an invoice item."""
    return make_request("GET", f"/invoiceitems/{invoice_item_id}")


@server.tool()
def update_invoice_item(
    invoice_item_id: str,
    amount: Optional[int] = None,
    description: Optional[str] = None,
    metadata: Optional[dict] = None,
) -> dict:
    """Update an invoice item."""
    data = {}
    if amount is not None:
        data["amount"] = amount
    if description is not None:
        data["description"] = description
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return make_request("POST", f"/invoiceitems/{invoice_item_id}", data=data)


@server.tool()
def delete_invoice_item(invoice_item_id: str) -> dict:
    """Delete an invoice item."""
    return make_request("DELETE", f"/invoiceitems/{invoice_item_id}")


@server.tool()
def list_invoice_items(limit: int = 10) -> dict:
    """List invoice items."""
    return make_request("GET", "/invoiceitems", params={"limit": limit})


# ============================================================================
# CUSTOMER BANK ACCOUNTS
# ============================================================================

@server.tool()
def create_customer_bank_account(
    customer: str,
    source: str,
) -> dict:
    """Create a bank account for a customer."""
    data = {
        "source": source,
    }
    return make_request("POST", f"/customers/{customer}/sources", data=data)


@server.tool()
def get_customer_bank_account(customer: str, bank_account_id: str) -> dict:
    """Retrieve a customer's bank account."""
    return make_request("GET", f"/customers/{customer}/sources/{bank_account_id}")


@server.tool()
def delete_customer_bank_account(customer: str, bank_account_id: str) -> dict:
    """Delete a customer's bank account."""
    return make_request("DELETE", f"/customers/{customer}/sources/{bank_account_id}")


@server.tool()
def list_customer_bank_accounts(customer: str, limit: int = 10) -> dict:
    """List a customer's bank accounts."""
    return make_request("GET", f"/customers/{customer}/sources", params={"limit": limit, "object": "bank_account"})


# ============================================================================
# CUSTOMER SOURCES
# ============================================================================

@server.tool()
def create_customer_source(
    customer: str,
    source: str,
    metadata: Optional[dict] = None,
) -> dict:
    """Create a source for a customer."""
    data = {
        "source": source,
    }
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return make_request("POST", f"/customers/{customer}/sources", data=data)


@server.tool()
def get_customer_source(customer: str, source_id: str) -> dict:
    """Retrieve a customer's source."""
    return make_request("GET", f"/customers/{customer}/sources/{source_id}")


@server.tool()
def update_customer_source(
    customer: str,
    source_id: str,
    metadata: Optional[dict] = None,
) -> dict:
    """Update a customer's source."""
    data = {}
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return make_request("POST", f"/customers/{customer}/sources/{source_id}", data=data)


@server.tool()
def delete_customer_source(customer: str, source_id: str) -> dict:
    """Delete a customer's source."""
    return make_request("DELETE", f"/customers/{customer}/sources/{source_id}")


@server.tool()
def list_customer_sources(customer: str, limit: int = 10) -> dict:
    """List a customer's sources."""
    return make_request("GET", f"/customers/{customer}/sources", params={"limit": limit})


# ============================================================================
# MANDATES
# ============================================================================

@server.tool()
def get_mandate(mandate_id: str) -> dict:
    """Retrieve a mandate."""
    return make_request("GET", f"/mandates/{mandate_id}")


@server.tool()
def list_mandates(limit: int = 10) -> dict:
    """List mandates."""
    return make_request("GET", "/mandates", params={"limit": limit})


# ============================================================================
# SHIPPING RATES
# ============================================================================

@server.tool()
def create_shipping_rate(
    display_name: str,
    type: str,
    fixed_amount: Optional[dict] = None,
    metadata: Optional[dict] = None,
) -> dict:
    """Create a shipping rate."""
    data = {
        "display_name": display_name,
        "type": type,
    }
    if fixed_amount:
        for key, value in fixed_amount.items():
            data[f"fixed_amount[{key}]"] = value
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return make_request("POST", "/shipping_rates", data=data)


@server.tool()
def get_shipping_rate(shipping_rate_id: str) -> dict:
    """Retrieve a shipping rate."""
    return make_request("GET", f"/shipping_rates/{shipping_rate_id}")


@server.tool()
def update_shipping_rate(
    shipping_rate_id: str,
    display_name: Optional[str] = None,
    metadata: Optional[dict] = None,
) -> dict:
    """Update a shipping rate."""
    data = {}
    if display_name is not None:
        data["display_name"] = display_name
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return make_request("POST", f"/shipping_rates/{shipping_rate_id}", data=data)


@server.tool()
def list_shipping_rates(limit: int = 10) -> dict:
    """List shipping rates."""
    return make_request("GET", "/shipping_rates", params={"limit": limit})


# ============================================================================
# PLANS (Legacy - use Prices instead)
# ============================================================================

@server.tool()
def create_plan(
    amount: int,
    currency: str,
    interval: str,
    product: Optional[str] = None,
    nickname: Optional[str] = None,
    metadata: Optional[dict] = None,
) -> dict:
    """Create a plan (legacy - use prices instead)."""
    data = {
        "amount": amount,
        "currency": currency,
        "interval": interval,
    }
    if product:
        data["product"] = product
    if nickname:
        data["nickname"] = nickname
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return make_request("POST", "/plans", data=data)


@server.tool()
def get_plan(plan_id: str) -> dict:
    """Retrieve a plan."""
    return make_request("GET", f"/plans/{plan_id}")


@server.tool()
def update_plan(
    plan_id: str,
    nickname: Optional[str] = None,
    metadata: Optional[dict] = None,
) -> dict:
    """Update a plan."""
    data = {}
    if nickname is not None:
        data["nickname"] = nickname
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return make_request("POST", f"/plans/{plan_id}", data=data)


@server.tool()
def delete_plan(plan_id: str) -> dict:
    """Delete a plan."""
    return make_request("DELETE", f"/plans/{plan_id}")


@server.tool()
def list_plans(limit: int = 10) -> dict:
    """List plans."""
    return make_request("GET", "/plans", params={"limit": limit})


if __name__ == "__main__":
    server.run()

