#!/usr/bin/env python3
"""
Stripe MCP Server - Comprehensive Stripe API integration for autonomous agents.
Provides tools for managing customers, payments, subscriptions, products, and more.
"""

import os
import json
import requests
from typing import Any, Optional
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
server = FastMCP("stripe-mcp")

# Configuration
STRIPE_API_KEY = os.getenv("STRIPE_API_KEY", "")
BASE_URL = "https://api.stripe.com/v1"

# Helper function to make authenticated API requests
def stripe_request(
    method: str,
    endpoint: str,
    params: Optional[dict] = None,
    data: Optional[dict] = None,
) -> dict:
    """Make an authenticated request to the Stripe API."""
    if not STRIPE_API_KEY:
        return {"error": "STRIPE_API_KEY environment variable not set"}
    
    url = f"{BASE_URL}{endpoint}"
    headers = {
        "Authorization": f"Bearer {STRIPE_API_KEY}",
    }
    
    try:
        if method == "GET":
            response = requests.get(url, headers=headers, params=params, timeout=30)
        elif method == "POST":
            headers["Content-Type"] = "application/x-www-form-urlencoded"
            response = requests.post(url, headers=headers, data=data, timeout=30)
        elif method == "DELETE":
            response = requests.delete(url, headers=headers, params=params, timeout=30)
        else:
            return {"error": f"Unsupported HTTP method: {method}"}
        
        if response.status_code >= 400:
            return {
                "error": f"API error {response.status_code}",
                "details": response.text
            }
        
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}
    except json.JSONDecodeError:
        return {"error": "Invalid JSON response from API"}


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
    
    return stripe_request("POST", "/customers", data=data)


@server.tool()
def get_customer(customer_id: str) -> dict:
    """Retrieve a customer by ID."""
    return stripe_request("GET", f"/customers/{customer_id}")


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
    
    return stripe_request("POST", f"/customers/{customer_id}", data=data)


@server.tool()
def delete_customer(customer_id: str) -> dict:
    """Delete a customer."""
    return stripe_request("DELETE", f"/customers/{customer_id}")


@server.tool()
def list_customers(limit: int = 10) -> dict:
    """List customers."""
    return stripe_request("GET", "/customers", params={"limit": limit})


# ============================================================================
# PAYMENT INTENTS
# ============================================================================

@server.tool()
def create_payment_intent(
    amount: int,
    currency: str,
    customer: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[dict] = None,
    confirm: bool = False,
    payment_method: Optional[str] = None,
    off_session: Optional[bool] = None,
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
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    if confirm:
        data["confirm"] = "true"
    if payment_method:
        data["payment_method"] = payment_method
    if off_session is not None:
        data["off_session"] = "true" if off_session else "false"
    
    return stripe_request("POST", "/payment_intents", data=data)


@server.tool()
def get_payment_intent(payment_intent_id: str) -> dict:
    """Retrieve a payment intent."""
    return stripe_request("GET", f"/payment_intents/{payment_intent_id}")


@server.tool()
def confirm_payment_intent(
    payment_intent_id: str,
    payment_method: Optional[str] = None,
) -> dict:
    """Confirm a payment intent."""
    data = {}
    if payment_method:
        data["payment_method"] = payment_method
    
    return stripe_request("POST", f"/payment_intents/{payment_intent_id}/confirm", data=data)


@server.tool()
def cancel_payment_intent(payment_intent_id: str) -> dict:
    """Cancel a payment intent."""
    return stripe_request("POST", f"/payment_intents/{payment_intent_id}/cancel", data={})


@server.tool()
def list_payment_intents(limit: int = 10) -> dict:
    """List payment intents."""
    return stripe_request("GET", "/payment_intents", params={"limit": limit})


# ============================================================================
# CHARGES
# ============================================================================

@server.tool()
def get_charge(charge_id: str) -> dict:
    """Retrieve a charge."""
    return stripe_request("GET", f"/charges/{charge_id}")


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
    
    return stripe_request("POST", f"/charges/{charge_id}", data=data)


@server.tool()
def list_charges(limit: int = 10) -> dict:
    """List charges."""
    return stripe_request("GET", "/charges", params={"limit": limit})


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
    
    return stripe_request("POST", "/refunds", data=data)


@server.tool()
def get_refund(refund_id: str) -> dict:
    """Retrieve a refund."""
    return stripe_request("GET", f"/refunds/{refund_id}")


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
    
    return stripe_request("POST", f"/refunds/{refund_id}", data=data)


@server.tool()
def list_refunds(limit: int = 10) -> dict:
    """List refunds."""
    return stripe_request("GET", "/refunds", params={"limit": limit})


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
    
    return stripe_request("POST", "/products", data=data)


@server.tool()
def get_product(product_id: str) -> dict:
    """Retrieve a product."""
    return stripe_request("GET", f"/products/{product_id}")


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
    
    return stripe_request("POST", f"/products/{product_id}", data=data)


@server.tool()
def list_products(limit: int = 10) -> dict:
    """List products."""
    return stripe_request("GET", "/products", params={"limit": limit})


# ============================================================================
# PRICES
# ============================================================================

@server.tool()
def create_price(
    currency: str,
    product: str,
    unit_amount: int,
    recurring_interval: Optional[str] = None,
    nickname: Optional[str] = None,
    metadata: Optional[dict] = None,
) -> dict:
    """Create a price."""
    data = {
        "currency": currency,
        "product": product,
        "unit_amount": unit_amount,
    }
    if recurring_interval:
        data["recurring[interval]"] = recurring_interval
    if nickname:
        data["nickname"] = nickname
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return stripe_request("POST", "/prices", data=data)


@server.tool()
def get_price(price_id: str) -> dict:
    """Retrieve a price."""
    return stripe_request("GET", f"/prices/{price_id}")


@server.tool()
def update_price(
    price_id: str,
    active: Optional[bool] = None,
    nickname: Optional[str] = None,
    metadata: Optional[dict] = None,
) -> dict:
    """Update a price."""
    data = {}
    if active is not None:
        data["active"] = "true" if active else "false"
    if nickname is not None:
        data["nickname"] = nickname
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return stripe_request("POST", f"/prices/{price_id}", data=data)


@server.tool()
def list_prices(limit: int = 10) -> dict:
    """List prices."""
    return stripe_request("GET", "/prices", params={"limit": limit})


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
    trial_period_days: Optional[int] = None,
) -> dict:
    """Create a subscription.
    
    items should be a list of dicts with 'price' key, e.g.:
    [{"price": "price_1234567890"}]
    """
    data = {
        "customer": customer,
    }
    if currency:
        data["currency"] = currency
    if description:
        data["description"] = description
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    if trial_period_days is not None:
        data["trial_period_days"] = trial_period_days
    
    # Add items
    for i, item in enumerate(items):
        if "price" in item:
            data[f"items[{i}][price]"] = item["price"]
        if "quantity" in item:
            data[f"items[{i}][quantity]"] = item["quantity"]
    
    return stripe_request("POST", "/subscriptions", data=data)


@server.tool()
def get_subscription(subscription_id: str) -> dict:
    """Retrieve a subscription."""
    return stripe_request("GET", f"/subscriptions/{subscription_id}")


@server.tool()
def update_subscription(
    subscription_id: str,
    description: Optional[str] = None,
    metadata: Optional[dict] = None,
    cancel_at_period_end: Optional[bool] = None,
) -> dict:
    """Update a subscription."""
    data = {}
    if description is not None:
        data["description"] = description
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    if cancel_at_period_end is not None:
        data["cancel_at_period_end"] = "true" if cancel_at_period_end else "false"
    
    return stripe_request("POST", f"/subscriptions/{subscription_id}", data=data)


@server.tool()
def cancel_subscription(subscription_id: str) -> dict:
    """Cancel a subscription."""
    return stripe_request("DELETE", f"/subscriptions/{subscription_id}")


@server.tool()
def list_subscriptions(limit: int = 10) -> dict:
    """List subscriptions."""
    return stripe_request("GET", "/subscriptions", params={"limit": limit})


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
    
    return stripe_request("POST", "/invoices", data=data)


@server.tool()
def get_invoice(invoice_id: str) -> dict:
    """Retrieve an invoice."""
    return stripe_request("GET", f"/invoices/{invoice_id}")


@server.tool()
def finalize_invoice(invoice_id: str) -> dict:
    """Finalize an invoice."""
    return stripe_request("POST", f"/invoices/{invoice_id}/finalize", data={})


@server.tool()
def pay_invoice(invoice_id: str) -> dict:
    """Pay an invoice."""
    return stripe_request("POST", f"/invoices/{invoice_id}/pay", data={})


@server.tool()
def void_invoice(invoice_id: str) -> dict:
    """Void an invoice."""
    return stripe_request("POST", f"/invoices/{invoice_id}/void", data={})


@server.tool()
def list_invoices(limit: int = 10) -> dict:
    """List invoices."""
    return stripe_request("GET", "/invoices", params={"limit": limit})


# ============================================================================
# CHECKOUT SESSIONS
# ============================================================================

@server.tool()
def create_checkout_session(
    mode: str,
    line_items: list,
    success_url: str,
    cancel_url: Optional[str] = None,
    customer: Optional[str] = None,
    customer_email: Optional[str] = None,
    metadata: Optional[dict] = None,
) -> dict:
    """Create a checkout session.
    
    mode should be 'payment', 'setup', or 'subscription'
    line_items should be a list of dicts with 'price' and 'quantity' keys
    """
    data = {
        "mode": mode,
        "success_url": success_url,
    }
    if cancel_url:
        data["cancel_url"] = cancel_url
    if customer:
        data["customer"] = customer
    if customer_email:
        data["customer_email"] = customer_email
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    # Add line items
    for i, item in enumerate(line_items):
        if "price" in item:
            data[f"line_items[{i}][price]"] = item["price"]
        if "quantity" in item:
            data[f"line_items[{i}][quantity]"] = item["quantity"]
    
    return stripe_request("POST", "/checkout/sessions", data=data)


@server.tool()
def get_checkout_session(session_id: str) -> dict:
    """Retrieve a checkout session."""
    return stripe_request("GET", f"/checkout/sessions/{session_id}")


@server.tool()
def list_checkout_sessions(limit: int = 10) -> dict:
    """List checkout sessions."""
    return stripe_request("GET", "/checkout/sessions", params={"limit": limit})


# ============================================================================
# PAYMENT METHODS
# ============================================================================

@server.tool()
def get_payment_method(payment_method_id: str) -> dict:
    """Retrieve a payment method."""
    return stripe_request("GET", f"/payment_methods/{payment_method_id}")


@server.tool()
def list_payment_methods(customer: str, limit: int = 10) -> dict:
    """List payment methods for a customer."""
    return stripe_request("GET", "/payment_methods", params={
        "customer": customer,
        "limit": limit,
    })


@server.tool()
def detach_payment_method(payment_method_id: str) -> dict:
    """Detach a payment method from a customer."""
    return stripe_request("POST", f"/payment_methods/{payment_method_id}/detach", data={})


# ============================================================================
# COUPONS
# ============================================================================

@server.tool()
def create_coupon(
    percent_off: Optional[int] = None,
    amount_off: Optional[int] = None,
    currency: Optional[str] = None,
    duration: str = "once",
    duration_in_months: Optional[int] = None,
    max_redemptions: Optional[int] = None,
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
    if duration_in_months is not None:
        data["duration_in_months"] = duration_in_months
    if max_redemptions is not None:
        data["max_redemptions"] = max_redemptions
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return stripe_request("POST", "/coupons", data=data)


@server.tool()
def get_coupon(coupon_id: str) -> dict:
    """Retrieve a coupon."""
    return stripe_request("GET", f"/coupons/{coupon_id}")


@server.tool()
def delete_coupon(coupon_id: str) -> dict:
    """Delete a coupon."""
    return stripe_request("DELETE", f"/coupons/{coupon_id}")


@server.tool()
def list_coupons(limit: int = 10) -> dict:
    """List coupons."""
    return stripe_request("GET", "/coupons", params={"limit": limit})


# ============================================================================
# PROMOTION CODES
# ============================================================================

@server.tool()
def create_promotion_code(
    coupon: str,
    code: str,
    active: bool = True,
    max_redemptions: Optional[int] = None,
    metadata: Optional[dict] = None,
) -> dict:
    """Create a promotion code."""
    data = {
        "coupon": coupon,
        "code": code,
        "active": "true" if active else "false",
    }
    if max_redemptions is not None:
        data["max_redemptions"] = max_redemptions
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return stripe_request("POST", "/promotion_codes", data=data)


@server.tool()
def get_promotion_code(promotion_code_id: str) -> dict:
    """Retrieve a promotion code."""
    return stripe_request("GET", f"/promotion_codes/{promotion_code_id}")


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
    
    return stripe_request("POST", f"/promotion_codes/{promotion_code_id}", data=data)


@server.tool()
def list_promotion_codes(limit: int = 10) -> dict:
    """List promotion codes."""
    return stripe_request("GET", "/promotion_codes", params={"limit": limit})


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
    
    return stripe_request("POST", "/setup_intents", data=data)


@server.tool()
def get_setup_intent(setup_intent_id: str) -> dict:
    """Retrieve a setup intent."""
    return stripe_request("GET", f"/setup_intents/{setup_intent_id}")


@server.tool()
def confirm_setup_intent(
    setup_intent_id: str,
    payment_method: Optional[str] = None,
) -> dict:
    """Confirm a setup intent."""
    data = {}
    if payment_method:
        data["payment_method"] = payment_method
    
    return stripe_request("POST", f"/setup_intents/{setup_intent_id}/confirm", data=data)


@server.tool()
def list_setup_intents(limit: int = 10) -> dict:
    """List setup intents."""
    return stripe_request("GET", "/setup_intents", params={"limit": limit})


# ============================================================================
# BALANCE
# ============================================================================

@server.tool()
def get_balance() -> dict:
    """Retrieve account balance."""
    return stripe_request("GET", "/balance")


@server.tool()
def list_balance_transactions(limit: int = 10) -> dict:
    """List balance transactions."""
    return stripe_request("GET", "/balance_transactions", params={"limit": limit})


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
    
    return stripe_request("POST", "/transfers", data=data)


@server.tool()
def get_transfer(transfer_id: str) -> dict:
    """Retrieve a transfer."""
    return stripe_request("GET", f"/transfers/{transfer_id}")


@server.tool()
def update_transfer(
    transfer_id: str,
    metadata: Optional[dict] = None,
) -> dict:
    """Update a transfer."""
    data = {}
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return stripe_request("POST", f"/transfers/{transfer_id}", data=data)


@server.tool()
def list_transfers(limit: int = 10) -> dict:
    """List transfers."""
    return stripe_request("GET", "/transfers", params={"limit": limit})


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
    
    return stripe_request("POST", "/payouts", data=data)


@server.tool()
def get_payout(payout_id: str) -> dict:
    """Retrieve a payout."""
    return stripe_request("GET", f"/payouts/{payout_id}")


@server.tool()
def cancel_payout(payout_id: str) -> dict:
    """Cancel a payout."""
    return stripe_request("POST", f"/payouts/{payout_id}/cancel", data={})


@server.tool()
def list_payouts(limit: int = 10) -> dict:
    """List payouts."""
    return stripe_request("GET", "/payouts", params={"limit": limit})


# ============================================================================
# DISPUTES
# ============================================================================

@server.tool()
def get_dispute(dispute_id: str) -> dict:
    """Retrieve a dispute."""
    return stripe_request("GET", f"/disputes/{dispute_id}")


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
    
    return stripe_request("POST", f"/disputes/{dispute_id}", data=data)


@server.tool()
def close_dispute(dispute_id: str) -> dict:
    """Close a dispute."""
    return stripe_request("POST", f"/disputes/{dispute_id}/close", data={})


@server.tool()
def list_disputes(limit: int = 10) -> dict:
    """List disputes."""
    return stripe_request("GET", "/disputes", params={"limit": limit})


# ============================================================================
# EVENTS
# ============================================================================

@server.tool()
def get_event(event_id: str) -> dict:
    """Retrieve an event."""
    return stripe_request("GET", f"/events/{event_id}")


@server.tool()
def list_events(limit: int = 10) -> dict:
    """List events."""
    return stripe_request("GET", "/events", params={"limit": limit})


# ============================================================================
# ACCOUNTS (Connect)
# ============================================================================

@server.tool()
def get_account(account_id: Optional[str] = None) -> dict:
    """Retrieve an account. If no account_id provided, retrieves the current account."""
    if account_id:
        return stripe_request("GET", f"/accounts/{account_id}")
    else:
        return stripe_request("GET", "/account")


@server.tool()
def list_accounts(limit: int = 10) -> dict:
    """List connected accounts."""
    return stripe_request("GET", "/accounts", params={"limit": limit})


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
    if amount is not None:
        data["amount"] = amount
    if reason:
        data["reason"] = reason
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    if lines:
        for i, line in enumerate(lines):
            if "invoice_line_item" in line:
                data[f"lines[{i}][invoice_line_item]"] = line["invoice_line_item"]
            if "quantity" in line:
                data[f"lines[{i}][quantity]"] = line["quantity"]
    
    return stripe_request("POST", "/credit_notes", data=data)


@server.tool()
def get_credit_note(credit_note_id: str) -> dict:
    """Retrieve a credit note."""
    return stripe_request("GET", f"/credit_notes/{credit_note_id}")


@server.tool()
def list_credit_notes(limit: int = 10) -> dict:
    """List credit notes."""
    return stripe_request("GET", "/credit_notes", params={"limit": limit})


# ============================================================================
# TAX RATES
# ============================================================================

@server.tool()
def create_tax_rate(
    display_name: str,
    percentage: float,
    inclusive: bool = False,
    jurisdiction: Optional[str] = None,
    description: Optional[str] = None,
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
    if description:
        data["description"] = description
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return stripe_request("POST", "/tax_rates", data=data)


@server.tool()
def get_tax_rate(tax_rate_id: str) -> dict:
    """Retrieve a tax rate."""
    return stripe_request("GET", f"/tax_rates/{tax_rate_id}")


@server.tool()
def update_tax_rate(
    tax_rate_id: str,
    display_name: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[dict] = None,
) -> dict:
    """Update a tax rate."""
    data = {}
    if display_name is not None:
        data["display_name"] = display_name
    if description is not None:
        data["description"] = description
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return stripe_request("POST", f"/tax_rates/{tax_rate_id}", data=data)


@server.tool()
def list_tax_rates(limit: int = 10) -> dict:
    """List tax rates."""
    return stripe_request("GET", "/tax_rates", params={"limit": limit})


# ============================================================================
# PLANS (Legacy - use Prices instead)
# ============================================================================

@server.tool()
def create_plan(
    currency: str,
    interval: str,
    product: str,
    amount: int,
    nickname: Optional[str] = None,
    active: bool = True,
    metadata: Optional[dict] = None,
) -> dict:
    """Create a plan (legacy - use Prices API instead)."""
    data = {
        "currency": currency,
        "interval": interval,
        "product": product,
        "amount": amount,
        "active": "true" if active else "false",
    }
    if nickname:
        data["nickname"] = nickname
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return stripe_request("POST", "/plans", data=data)


@server.tool()
def get_plan(plan_id: str) -> dict:
    """Retrieve a plan."""
    return stripe_request("GET", f"/plans/{plan_id}")


@server.tool()
def update_plan(
    plan_id: str,
    nickname: Optional[str] = None,
    active: Optional[bool] = None,
    metadata: Optional[dict] = None,
) -> dict:
    """Update a plan."""
    data = {}
    if nickname is not None:
        data["nickname"] = nickname
    if active is not None:
        data["active"] = "true" if active else "false"
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return stripe_request("POST", f"/plans/{plan_id}", data=data)


@server.tool()
def delete_plan(plan_id: str) -> dict:
    """Delete a plan."""
    return stripe_request("DELETE", f"/plans/{plan_id}")


@server.tool()
def list_plans(limit: int = 10) -> dict:
    """List plans."""
    return stripe_request("GET", "/plans", params={"limit": limit})


# ============================================================================
# QUOTES
# ============================================================================

@server.tool()
def create_quote(
    customer: str,
    line_items: list,
    description: Optional[str] = None,
    metadata: Optional[dict] = None,
) -> dict:
    """Create a quote.
    
    line_items should be a list of dicts with 'price' and 'quantity' keys
    """
    data = {
        "customer": customer,
    }
    if description:
        data["description"] = description
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    # Add line items
    for i, item in enumerate(line_items):
        if "price" in item:
            data[f"line_items[{i}][price]"] = item["price"]
        if "quantity" in item:
            data[f"line_items[{i}][quantity]"] = item["quantity"]
    
    return stripe_request("POST", "/quotes", data=data)


@server.tool()
def get_quote(quote_id: str) -> dict:
    """Retrieve a quote."""
    return stripe_request("GET", f"/quotes/{quote_id}")


@server.tool()
def update_quote(
    quote_id: str,
    description: Optional[str] = None,
    metadata: Optional[dict] = None,
) -> dict:
    """Update a quote."""
    data = {}
    if description is not None:
        data["description"] = description
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return stripe_request("POST", f"/quotes/{quote_id}", data=data)


@server.tool()
def accept_quote(quote_id: str) -> dict:
    """Accept a quote."""
    return stripe_request("POST", f"/quotes/{quote_id}/accept", data={})


@server.tool()
def cancel_quote(quote_id: str) -> dict:
    """Cancel a quote."""
    return stripe_request("POST", f"/quotes/{quote_id}/cancel", data={})


@server.tool()
def finalize_quote(quote_id: str) -> dict:
    """Finalize a quote."""
    return stripe_request("POST", f"/quotes/{quote_id}/finalize", data={})


@server.tool()
def list_quotes(limit: int = 10) -> dict:
    """List quotes."""
    return stripe_request("GET", "/quotes", params={"limit": limit})


# ============================================================================
# PAYMENT LINKS
# ============================================================================

@server.tool()
def create_payment_link(
    line_items: list,
    metadata: Optional[dict] = None,
    active: bool = True,
) -> dict:
    """Create a payment link.
    
    line_items should be a list of dicts with 'price' and 'quantity' keys
    """
    data = {
        "active": "true" if active else "false",
    }
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    # Add line items
    for i, item in enumerate(line_items):
        if "price" in item:
            data[f"line_items[{i}][price]"] = item["price"]
        if "quantity" in item:
            data[f"line_items[{i}][quantity]"] = item["quantity"]
    
    return stripe_request("POST", "/payment_links", data=data)


@server.tool()
def get_payment_link(payment_link_id: str) -> dict:
    """Retrieve a payment link."""
    return stripe_request("GET", f"/payment_links/{payment_link_id}")


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
    
    return stripe_request("POST", f"/payment_links/{payment_link_id}", data=data)


@server.tool()
def list_payment_links(limit: int = 10) -> dict:
    """List payment links."""
    return stripe_request("GET", "/payment_links", params={"limit": limit})


# ============================================================================
# MANDATES
# ============================================================================

@server.tool()
def get_mandate(mandate_id: str) -> dict:
    """Retrieve a mandate."""
    return stripe_request("GET", f"/mandates/{mandate_id}")


# ============================================================================
# SUBSCRIPTION ITEMS
# ============================================================================

@server.tool()
def create_subscription_item(
    subscription: str,
    price: str,
    quantity: int = 1,
    metadata: Optional[dict] = None,
) -> dict:
    """Create a subscription item."""
    data = {
        "subscription": subscription,
        "price": price,
        "quantity": quantity,
    }
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return stripe_request("POST", "/subscription_items", data=data)


@server.tool()
def get_subscription_item(subscription_item_id: str) -> dict:
    """Retrieve a subscription item."""
    return stripe_request("GET", f"/subscription_items/{subscription_item_id}")


@server.tool()
def update_subscription_item(
    subscription_item_id: str,
    quantity: Optional[int] = None,
    metadata: Optional[dict] = None,
) -> dict:
    """Update a subscription item."""
    data = {}
    if quantity is not None:
        data["quantity"] = quantity
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return stripe_request("POST", f"/subscription_items/{subscription_item_id}", data=data)


@server.tool()
def delete_subscription_item(subscription_item_id: str) -> dict:
    """Delete a subscription item."""
    return stripe_request("DELETE", f"/subscription_items/{subscription_item_id}")


@server.tool()
def list_subscription_items(subscription: str, limit: int = 10) -> dict:
    """List subscription items for a subscription."""
    return stripe_request("GET", "/subscription_items", params={
        "subscription": subscription,
        "limit": limit,
    })


# ============================================================================
# DISCOUNTS
# ============================================================================

@server.tool()
def create_discount(
    coupon: str,
    customer: Optional[str] = None,
    subscription: Optional[str] = None,
) -> dict:
    """Create a discount."""
    data = {
        "coupon": coupon,
    }
    if customer:
        data["customer"] = customer
    if subscription:
        data["subscription"] = subscription
    
    return stripe_request("POST", "/discounts", data=data)


@server.tool()
def delete_discount(discount_id: str) -> dict:
    """Delete a discount."""
    return stripe_request("DELETE", f"/discounts/{discount_id}")


# ============================================================================
# INVOICE ITEMS
# ============================================================================

@server.tool()
def create_invoice_item(
    customer: str,
    amount: int,
    currency: str,
    description: Optional[str] = None,
    invoice: Optional[str] = None,
    metadata: Optional[dict] = None,
) -> dict:
    """Create an invoice item."""
    data = {
        "customer": customer,
        "amount": amount,
        "currency": currency,
    }
    if description:
        data["description"] = description
    if invoice:
        data["invoice"] = invoice
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return stripe_request("POST", "/invoiceitems", data=data)


@server.tool()
def get_invoice_item(invoice_item_id: str) -> dict:
    """Retrieve an invoice item."""
    return stripe_request("GET", f"/invoiceitems/{invoice_item_id}")


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
    
    return stripe_request("POST", f"/invoiceitems/{invoice_item_id}", data=data)


@server.tool()
def delete_invoice_item(invoice_item_id: str) -> dict:
    """Delete an invoice item."""
    return stripe_request("DELETE", f"/invoiceitems/{invoice_item_id}")


@server.tool()
def list_invoice_items(limit: int = 10) -> dict:
    """List invoice items."""
    return stripe_request("GET", "/invoiceitems", params={"limit": limit})


if __name__ == "__main__":
    server.run()
