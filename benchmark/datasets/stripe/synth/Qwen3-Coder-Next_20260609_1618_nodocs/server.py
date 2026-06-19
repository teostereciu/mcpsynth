#!/usr/bin/env python3
"""Stripe MCP Server - MCP server for Stripe API operations."""

import json
import os
import requests
from typing import Any, Dict, List, Optional

from fastmcp import FastMCP


mcp = FastMCP("stripe")


def get_stripe_api_key() -> str:
    """Get the Stripe API key from environment variables."""
    api_key = os.environ.get("STRIPE_API_KEY")
    if not api_key:
        raise ValueError("STRIPE_API_KEY environment variable is not set")
    return api_key


def stripe_request(
    method: str,
    path: str,
    params: Optional[Dict[str, Any]] = None,
    data: Optional[Dict[str, Any]] = None,
    api_key: Optional[str] = None,
) -> Dict[str, Any]:
    """Make a request to the Stripe API."""
    api_key = api_key or get_stripe_api_key()
    
    url = f"https://api.stripe.com{path}"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Stripe-Version": "2024-12-18.acacia",
    }
    
    try:
        if method.upper() == "GET":
            response = requests.get(url, headers=headers, params=params)
        elif method.upper() == "POST":
            response = requests.post(url, headers=headers, params=params, data=data)
        elif method.upper() == "PUT":
            response = requests.put(url, headers=headers, json=data)
        elif method.upper() == "DELETE":
            response = requests.delete(url, headers=headers, params=params)
        else:
            return {"error": f"Unsupported HTTP method: {method}"}
        
        if response.status_code >= 200 and response.status_code < 300:
            try:
                return response.json()
            except json.JSONDecodeError:
                return {"raw": response.text}
        else:
            error_msg = f"Stripe API error: {response.status_code} - {response.text}"
            return {"error": error_msg}
    
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}


# Payment Intents

@mcp.tool()
def get_payment_intent(payment_intent_id: str) -> Dict[str, Any]:
    """Retrieve a payment intent by ID."""
    return stripe_request("GET", f"/v1/payment_intents/{payment_intent_id}")


@mcp.tool()
def list_payment_intents(
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    customer: Optional[str] = None,
    status: Optional[str] = None,
) -> Dict[str, Any]:
    """List payment intents with optional filtering."""
    params = {"limit": limit}
    if starting_after:
        params["starting_after"] = starting_after
    if ending_before:
        params["ending_before"] = ending_before
    if customer:
        params["customer"] = customer
    if status:
        params["status"] = status
    return stripe_request("GET", "/v1/payment_intents", params=params)


@mcp.tool()
def create_payment_intent(
    amount: int,
    currency: str,
    description: Optional[str] = None,
    customer: Optional[str] = None,
    payment_method: Optional[str] = None,
    confirm: bool = False,
    return_url: Optional[str] = None,
    receipt_email: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    """Create a new payment intent."""
    data = {
        "amount": amount,
        "currency": currency,
    }
    if description:
        data["description"] = description
    if customer:
        data["customer"] = customer
    if payment_method:
        data["payment_method"] = payment_method
    if confirm:
        data["confirm"] = "true"
    if return_url:
        data["return_url"] = return_url
    if receipt_email:
        data["receipt_email"] = receipt_email
    if metadata:
        data["metadata"] = metadata
    return stripe_request("POST", "/v1/payment_intents", data=data)


@mcp.tool()
def confirm_payment_intent(
    payment_intent_id: str,
    payment_method: Optional[str] = None,
    return_url: Optional[str] = None,
) -> Dict[str, Any]:
    """Confirm a payment intent."""
    data = {}
    if payment_method:
        data["payment_method"] = payment_method
    if return_url:
        data["return_url"] = return_url
    return stripe_request("POST", f"/v1/payment_intents/{payment_intent_id}/confirm", data=data)


@mcp.tool()
def cancel_payment_intent(payment_intent_id: str, reason: Optional[str] = None) -> Dict[str, Any]:
    """Cancel a payment intent."""
    data = {}
    if reason:
        data["reason"] = reason
    return stripe_request("POST", f"/v1/payment_intents/{payment_intent_id}/cancel", data=data)


@mcp.tool()
def capture_payment_intent(payment_intent_id: str, amount_to_capture: Optional[int] = None) -> Dict[str, Any]:
    """Capture a payment intent."""
    data = {}
    if amount_to_capture:
        data["amount_to_capture"] = amount_to_capture
    return stripe_request("POST", f"/v1/payment_intents/{payment_intent_id}/capture", data=data)


@mcp.tool()
def update_payment_intent(
    payment_intent_id: str,
    description: Optional[str] = None,
    receipt_email: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    """Update a payment intent."""
    data = {}
    if description:
        data["description"] = description
    if receipt_email:
        data["receipt_email"] = receipt_email
    if metadata:
        data["metadata"] = metadata
    return stripe_request("POST", f"/v1/payment_intents/{payment_intent_id}", data=data)


# Charges

@mcp.tool()
def get_charge(charge_id: str) -> Dict[str, Any]:
    """Retrieve a charge by ID."""
    return stripe_request("GET", f"/v1/charges/{charge_id}")


@mcp.tool()
def list_charges(
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    customer: Optional[str] = None,
    status: Optional[str] = None,
) -> Dict[str, Any]:
    """List charges with optional filtering."""
    params = {"limit": limit}
    if starting_after:
        params["starting_after"] = starting_after
    if ending_before:
        params["ending_before"] = ending_before
    if customer:
        params["customer"] = customer
    if status:
        params["status"] = status
    return stripe_request("GET", "/v1/charges", params=params)


@mcp.tool()
def create_charge(
    amount: int,
    currency: str,
    source: Optional[str] = None,
    customer: Optional[str] = None,
    description: Optional[str] = None,
    receipt_email: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    """Create a new charge."""
    data = {
        "amount": amount,
        "currency": currency,
    }
    if source:
        data["source"] = source
    if customer:
        data["customer"] = customer
    if description:
        data["description"] = description
    if receipt_email:
        data["receipt_email"] = receipt_email
    if metadata:
        data["metadata"] = metadata
    return stripe_request("POST", "/v1/charges", data=data)


@mcp.tool()
def capture_charge(charge_id: str, amount_to_capture: Optional[int] = None) -> Dict[str, Any]:
    """Capture a charge."""
    data = {}
    if amount_to_capture:
        data["amount_to_capture"] = amount_to_capture
    return stripe_request("POST", f"/v1/charges/{charge_id}/capture", data=data)


@mcp.tool()
def refund_charge(charge_id: str, amount: Optional[int] = None, reason: Optional[str] = None) -> Dict[str, Any]:
    """Create a refund for a charge."""
    data = {}
    if amount:
        data["amount"] = amount
    if reason:
        data["reason"] = reason
    return stripe_request("POST", f"/v1/charges/{charge_id}/refunds", data=data)


@mcp.tool()
def list_charge_refunds(charge_id: str, limit: int = 10) -> Dict[str, Any]:
    """List refunds for a charge."""
    params = {"limit": limit}
    return stripe_request("GET", f"/v1/charges/{charge_id}/refunds", params=params)


# Customers

@mcp.tool()
def get_customer(customer_id: str) -> Dict[str, Any]:
    """Retrieve a customer by ID."""
    return stripe_request("GET", f"/v1/customers/{customer_id}")


@mcp.tool()
def list_customers(
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    email: Optional[str] = None,
) -> Dict[str, Any]:
    """List customers with optional filtering."""
    params = {"limit": limit}
    if starting_after:
        params["starting_after"] = starting_after
    if ending_before:
        params["ending_before"] = ending_before
    if email:
        params["email"] = email
    return stripe_request("GET", "/v1/customers", params=params)


@mcp.tool()
def create_customer(
    email: Optional[str] = None,
    name: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    """Create a new customer."""
    data = {}
    if email:
        data["email"] = email
    if name:
        data["name"] = name
    if description:
        data["description"] = description
    if metadata:
        data["metadata"] = metadata
    return stripe_request("POST", "/v1/customers", data=data)


@mcp.tool()
def update_customer(
    customer_id: str,
    email: Optional[str] = None,
    name: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    """Update a customer."""
    data = {}
    if email is not None:
        data["email"] = email
    if name is not None:
        data["name"] = name
    if description is not None:
        data["description"] = description
    if metadata is not None:
        data["metadata"] = metadata
    return stripe_request("POST", f"/v1/customers/{customer_id}", data=data)


@mcp.tool()
def delete_customer(customer_id: str) -> Dict[str, Any]:
    """Delete a customer."""
    return stripe_request("DELETE", f"/v1/customers/{customer_id}")


# Products

@mcp.tool()
def get_product(product_id: str) -> Dict[str, Any]:
    """Retrieve a product by ID."""
    return stripe_request("GET", f"/v1/products/{product_id}")


@mcp.tool()
def list_products(
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
) -> Dict[str, Any]:
    """List products."""
    params = {"limit": limit}
    if starting_after:
        params["starting_after"] = starting_after
    if ending_before:
        params["ending_before"] = ending_before
    return stripe_request("GET", "/v1/products", params=params)


@mcp.tool()
def create_product(
    name: str,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    """Create a new product."""
    data = {"name": name}
    if description:
        data["description"] = description
    if metadata:
        data["metadata"] = metadata
    return stripe_request("POST", "/v1/products", data=data)


@mcp.tool()
def update_product(
    product_id: str,
    name: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    """Update a product."""
    data = {}
    if name is not None:
        data["name"] = name
    if description is not None:
        data["description"] = description
    if metadata is not None:
        data["metadata"] = metadata
    return stripe_request("POST", f"/v1/products/{product_id}", data=data)


@mcp.tool()
def delete_product(product_id: str) -> Dict[str, Any]:
    """Delete a product."""
    return stripe_request("DELETE", f"/v1/products/{product_id}")


# Prices

@mcp.tool()
def get_price(price_id: str) -> Dict[str, Any]:
    """Retrieve a price by ID."""
    return stripe_request("GET", f"/v1/prices/{price_id}")


@mcp.tool()
def list_prices(
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    product: Optional[str] = None,
    active: Optional[bool] = None,
) -> Dict[str, Any]:
    """List prices with optional filtering."""
    params = {"limit": limit}
    if starting_after:
        params["starting_after"] = starting_after
    if ending_before:
        params["ending_before"] = ending_before
    if product:
        params["product"] = product
    if active is not None:
        params["active"] = str(active).lower()
    return stripe_request("GET", "/v1/prices", params=params)


@mcp.tool()
def create_price(
    product: Optional[str] = None,
    unit_amount: Optional[int] = None,
    currency: str = "usd",
    recurring: Optional[Dict[str, Any]] = None,
    nickname: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    """Create a new price."""
    data = {"currency": currency}
    if product:
        data["product"] = product
    if unit_amount is not None:
        data["unit_amount"] = unit_amount
    if recurring:
        data["recurring"] = json.dumps(recurring)
    if nickname:
        data["nickname"] = nickname
    if metadata:
        data["metadata"] = metadata
    return stripe_request("POST", "/v1/prices", data=data)


@mcp.tool()
def update_price(price_id: str, metadata: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
    """Update a price."""
    data = {}
    if metadata:
        data["metadata"] = metadata
    return stripe_request("POST", f"/v1/prices/{price_id}", data=data)


# Subscriptions

@mcp.tool()
def get_subscription(subscription_id: str) -> Dict[str, Any]:
    """Retrieve a subscription by ID."""
    return stripe_request("GET", f"/v1/subscriptions/{subscription_id}")


@mcp.tool()
def list_subscriptions(
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    customer: Optional[str] = None,
    status: Optional[str] = None,
) -> Dict[str, Any]:
    """List subscriptions with optional filtering."""
    params = {"limit": limit}
    if starting_after:
        params["starting_after"] = starting_after
    if ending_before:
        params["ending_before"] = ending_before
    if customer:
        params["customer"] = customer
    if status:
        params["status"] = status
    return stripe_request("GET", "/v1/subscriptions", params=params)


@mcp.tool()
def create_subscription(
    customer: str,
    items: List[Dict[str, Any]],
    trial_period_days: Optional[int] = None,
    metadata: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    """Create a new subscription."""
    data = {
        "customer": customer,
    }
    for i, item in enumerate(items):
        for key, value in item.items():
            data[f"items[{i}][{key}]"] = value
    if trial_period_days:
        data["trial_period_days"] = trial_period_days
    if metadata:
        data["metadata"] = metadata
    return stripe_request("POST", "/v1/subscriptions", data=data)


@mcp.tool()
def update_subscription(
    subscription_id: str,
    items: Optional[List[Dict[str, Any]]] = None,
    metadata: Optional[Dict[str, str]] = None,
    cancel_at_period_end: Optional[bool] = None,
) -> Dict[str, Any]:
    """Update a subscription."""
    data = {}
    if items:
        for i, item in enumerate(items):
            for key, value in item.items():
                data[f"items[{i}][{key}]"] = value
    if metadata:
        data["metadata"] = metadata
    if cancel_at_period_end is not None:
        data["cancel_at_period_end"] = str(cancel_at_period_end).lower()
    return stripe_request("POST", f"/v1/subscriptions/{subscription_id}", data=data)


@mcp.tool()
def delete_subscription(subscription_id: str) -> Dict[str, Any]:
    """Cancel a subscription."""
    return stripe_request("DELETE", f"/v1/subscriptions/{subscription_id}")


@mcp.tool()
def cancel_subscription(
    subscription_id: str,
    at_period_end: bool = False,
) -> Dict[str, Any]:
    """Cancel a subscription."""
    data = {"at_period_end": str(at_period_end).lower()}
    return stripe_request("POST", f"/v1/subscriptions/{subscription_id}/cancel", data=data)


# Invoices

@mcp.tool()
def get_invoice(invoice_id: str) -> Dict[str, Any]:
    """Retrieve an invoice by ID."""
    return stripe_request("GET", f"/v1/invoices/{invoice_id}")


@mcp.tool()
def list_invoices(
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    customer: Optional[str] = None,
    status: Optional[str] = None,
) -> Dict[str, Any]:
    """List invoices with optional filtering."""
    params = {"limit": limit}
    if starting_after:
        params["starting_after"] = starting_after
    if ending_before:
        params["ending_before"] = ending_before
    if customer:
        params["customer"] = customer
    if status:
        params["status"] = status
    return stripe_request("GET", "/v1/invoices", params=params)


@mcp.tool()
def create_invoice(
    customer: str,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    """Create a new invoice."""
    data = {"customer": customer}
    if description:
        data["description"] = description
    if metadata:
        data["metadata"] = metadata
    return stripe_request("POST", "/v1/invoices", data=data)


@mcp.tool()
def update_invoice(invoice_id: str, description: Optional[str] = None, metadata: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
    """Update an invoice."""
    data = {}
    if description:
        data["description"] = description
    if metadata:
        data["metadata"] = metadata
    return stripe_request("POST", f"/v1/invoices/{invoice_id}", data=data)


@mcp.tool()
def pay_invoice(invoice_id: str, out_of_band: bool = False) -> Dict[str, Any]:
    """Pay an invoice."""
    data = {"out_of_band": str(out_of_band).lower()}
    return stripe_request("POST", f"/v1/invoices/{invoice_id}/pay", data=data)


# Refunds

@mcp.tool()
def get_refund(refund_id: str) -> Dict[str, Any]:
    """Retrieve a refund by ID."""
    return stripe_request("GET", f"/v1/refunds/{refund_id}")


@mcp.tool()
def list_refunds(
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    charge: Optional[str] = None,
) -> Dict[str, Any]:
    """List refunds with optional filtering."""
    params = {"limit": limit}
    if starting_after:
        params["starting_after"] = starting_after
    if ending_before:
        params["ending_before"] = ending_before
    if charge:
        params["charge"] = charge
    return stripe_request("GET", "/v1/refunds", params=params)


@mcp.tool()
def create_refund(
    charge: str,
    amount: Optional[int] = None,
    reason: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    """Create a new refund."""
    data = {"charge": charge}
    if amount:
        data["amount"] = amount
    if reason:
        data["reason"] = reason
    if metadata:
        data["metadata"] = metadata
    return stripe_request("POST", "/v1/refunds", data=data)


@mcp.tool()
def update_refund(refund_id: str, metadata: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
    """Update a refund."""
    data = {}
    if metadata:
        data["metadata"] = metadata
    return stripe_request("POST", f"/v1/refunds/{refund_id}", data=data)


# Payment Methods

@mcp.tool()
def get_payment_method(payment_method_id: str) -> Dict[str, Any]:
    """Retrieve a payment method by ID."""
    return stripe_request("GET", f"/v1/payment_methods/{payment_method_id}")


@mcp.tool()
def list_payment_methods(
    customer: str,
    limit: int = 10,
    type: Optional[str] = None,
) -> Dict[str, Any]:
    """List payment methods for a customer."""
    params = {"customer": customer, "limit": limit}
    if type:
        params["type"] = type
    return stripe_request("GET", "/v1/payment_methods", params=params)


@mcp.tool()
def create_payment_method(
    type: str,
    card: Optional[Dict[str, Any]] = None,
    billing_details: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    """Create a new payment method."""
    data = {"type": type}
    if card:
        data["card"] = json.dumps(card)
    if billing_details:
        data["billing_details"] = json.dumps(billing_details)
    if metadata:
        data["metadata"] = metadata
    return stripe_request("POST", "/v1/payment_methods", data=data)


@mcp.tool()
def attach_payment_method(payment_method_id: str, customer: str) -> Dict[str, Any]:
    """Attach a payment method to a customer."""
    data = {"customer": customer}
    return stripe_request("POST", f"/v1/payment_methods/{payment_method_id}/attach", data=data)


@mcp.tool()
def detach_payment_method(payment_method_id: str) -> Dict[str, Any]:
    """Detach a payment method."""
    return stripe_request("POST", f"/v1/payment_methods/{payment_method_id}/detach")


@mcp.tool()
def update_payment_method(
    payment_method_id: str,
    card: Optional[Dict[str, Any]] = None,
    billing_details: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    """Update a payment method."""
    data = {}
    if card:
        data["card"] = json.dumps(card)
    if billing_details:
        data["billing_details"] = json.dumps(billing_details)
    if metadata:
        data["metadata"] = metadata
    return stripe_request("POST", f"/v1/payment_methods/{payment_method_id}", data=data)


# Setup Intents

@mcp.tool()
def get_setup_intent(setup_intent_id: str) -> Dict[str, Any]:
    """Retrieve a setup intent by ID."""
    return stripe_request("GET", f"/v1/setup_intents/{setup_intent_id}")


@mcp.tool()
def list_setup_intents(
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    customer: Optional[str] = None,
) -> Dict[str, Any]:
    """List setup intents with optional filtering."""
    params = {"limit": limit}
    if starting_after:
        params["starting_after"] = starting_after
    if ending_before:
        params["ending_before"] = ending_before
    if customer:
        params["customer"] = customer
    return stripe_request("GET", "/v1/setup_intents", params=params)


@mcp.tool()
def create_setup_intent(
    customer: Optional[str] = None,
    payment_method_types: Optional[List[str]] = None,
    return_url: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    """Create a new setup intent."""
    data = {}
    if customer:
        data["customer"] = customer
    if payment_method_types:
        for i, pmt in enumerate(payment_method_types):
            data[f"payment_method_types[{i}]"] = pmt
    if return_url:
        data["return_url"] = return_url
    if metadata:
        data["metadata"] = metadata
    return stripe_request("POST", "/v1/setup_intents", data=data)


@mcp.tool()
def confirm_setup_intent(
    setup_intent_id: str,
    payment_method: Optional[str] = None,
    return_url: Optional[str] = None,
) -> Dict[str, Any]:
    """Confirm a setup intent."""
    data = {}
    if payment_method:
        data["payment_method"] = payment_method
    if return_url:
        data["return_url"] = return_url
    return stripe_request("POST", f"/v1/setup_intents/{setup_intent_id}/confirm", data=data)


@mcp.tool()
def cancel_setup_intent(setup_intent_id: str) -> Dict[str, Any]:
    """Cancel a setup intent."""
    return stripe_request("POST", f"/v1/setup_intents/{setup_intent_id}/cancel")


# Coupons

@mcp.tool()
def get_coupon(coupon_id: str) -> Dict[str, Any]:
    """Retrieve a coupon by ID."""
    return stripe_request("GET", f"/v1/coupons/{coupon_id}")


@mcp.tool()
def list_coupons(
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
) -> Dict[str, Any]:
    """List coupons."""
    params = {"limit": limit}
    if starting_after:
        params["starting_after"] = starting_after
    if ending_before:
        params["ending_before"] = ending_before
    return stripe_request("GET", "/v1/coupons", params=params)


@mcp.tool()
def create_coupon(
    percent_off: Optional[int] = None,
    amount_off: Optional[int] = None,
    currency: str = "usd",
    duration: str = "repeating",
    duration_in_months: Optional[int] = None,
    max_redemptions: Optional[int] = None,
    metadata: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    """Create a new coupon."""
    data = {"currency": currency, "duration": duration}
    if percent_off is not None:
        data["percent_off"] = percent_off
    if amount_off is not None:
        data["amount_off"] = amount_off
    if duration_in_months:
        data["duration_in_months"] = duration_in_months
    if max_redemptions:
        data["max_redemptions"] = max_redemptions
    if metadata:
        data["metadata"] = metadata
    return stripe_request("POST", "/v1/coupons", data=data)


@mcp.tool()
def delete_coupon(coupon_id: str) -> Dict[str, Any]:
    """Delete a coupon."""
    return stripe_request("DELETE", f"/v1/coupons/{coupon_id}")


@mcp.tool()
def update_coupon(
    coupon_id: str,
    max_redemptions: Optional[int] = None,
    metadata: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    """Update a coupon."""
    data = {}
    if max_redemptions is not None:
        data["max_redemptions"] = max_redemptions
    if metadata:
        data["metadata"] = metadata
    return stripe_request("POST", f"/v1/coupons/{coupon_id}", data=data)


# Promotion Codes

@mcp.tool()
def get_promotion_code(promotion_code_id: str) -> Dict[str, Any]:
    """Retrieve a promotion code by ID."""
    return stripe_request("GET", f"/v1/promotion_codes/{promotion_code_id}")


@mcp.tool()
def list_promotion_codes(
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    coupon: Optional[str] = None,
    active: Optional[bool] = None,
) -> Dict[str, Any]:
    """List promotion codes with optional filtering."""
    params = {"limit": limit}
    if starting_after:
        params["starting_after"] = starting_after
    if ending_before:
        params["ending_before"] = ending_before
    if coupon:
        params["coupon"] = coupon
    if active is not None:
        params["active"] = str(active).lower()
    return stripe_request("GET", "/v1/promotion_codes", params=params)


@mcp.tool()
def create_promotion_code(
    coupon: str,
    code: Optional[str] = None,
    max_redemptions: Optional[int] = None,
    metadata: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    """Create a new promotion code."""
    data = {"coupon": coupon}
    if code:
        data["code"] = code
    if max_redemptions:
        data["max_redemptions"] = max_redemptions
    if metadata:
        data["metadata"] = metadata
    return stripe_request("POST", "/v1/promotion_codes", data=data)


@mcp.tool()
def update_promotion_code(
    promotion_code_id: str,
    max_redemptions: Optional[int] = None,
    metadata: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    """Update a promotion code."""
    data = {}
    if max_redemptions is not None:
        data["max_redemptions"] = max_redemptions
    if metadata:
        data["metadata"] = metadata
    return stripe_request("POST", f"/v1/promotion_codes/{promotion_code_id}", data=data)


# Checkout Sessions

@mcp.tool()
def get_checkout_session(session_id: str) -> Dict[str, Any]:
    """Retrieve a checkout session by ID."""
    return stripe_request("GET", f"/v1/checkout/sessions/{session_id}")


@mcp.tool()
def create_checkout_session(
    line_items: List[Dict[str, Any]],
    mode: str = "payment",
    success_url: Optional[str] = None,
    cancel_url: Optional[str] = None,
    customer_email: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    """Create a new checkout session."""
    data = {"mode": mode}
    for i, item in enumerate(line_items):
        for key, value in item.items():
            data[f"line_items[{i}][{key}]"] = value
    if success_url:
        data["success_url"] = success_url
    if cancel_url:
        data["cancel_url"] = cancel_url
    if customer_email:
        data["customer_email"] = customer_email
    if metadata:
        data["metadata"] = metadata
    return stripe_request("POST", "/v1/checkout/sessions", data=data)


# Payment Links

@mcp.tool()
def get_payment_link(payment_link_id: str) -> Dict[str, Any]:
    """Retrieve a payment link by ID."""
    return stripe_request("GET", f"/v1/payment_links/{payment_link_id}")


@mcp.tool()
def list_payment_links(limit: int = 10) -> Dict[str, Any]:
    """List payment links."""
    params = {"limit": limit}
    return stripe_request("GET", "/v1/payment_links", params=params)


@mcp.tool()
def create_payment_link(
    line_items: List[Dict[str, Any]],
    custom_text: Optional[Dict[str, str]] = None,
    custom_url: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    """Create a new payment link."""
    data = {}
    for i, item in enumerate(line_items):
        for key, value in item.items():
            data[f"line_items[{i}][{key}]"] = value
    if custom_text:
        data["custom_text"] = json.dumps(custom_text)
    if custom_url:
        data["custom_url"] = custom_url
    if metadata:
        data["metadata"] = metadata
    return stripe_request("POST", "/v1/payment_links", data=data)


@mcp.tool()
def update_payment_link(payment_link_id: str, active: bool = True, metadata: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
    """Update a payment link."""
    data = {"active": str(active).lower()}
    if metadata:
        data["metadata"] = metadata
    return stripe_request("POST", f"/v1/payment_links/{payment_link_id}", data=data)


# Connect Accounts

@mcp.tool()
def get_connect_account(account_id: str) -> Dict[str, Any]:
    """Retrieve a Connect account by ID."""
    return stripe_request("GET", f"/v1/accounts/{account_id}")


@mcp.tool()
def list_connect_accounts(
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
) -> Dict[str, Any]:
    """List Connect accounts."""
    params = {"limit": limit}
    if starting_after:
        params["starting_after"] = starting_after
    if ending_before:
        params["ending_before"] = ending_before
    return stripe_request("GET", "/v1/accounts", params=params)


@mcp.tool()
def create_connect_account(
    type: str = "express",
    country: str = "US",
    email: Optional[str] = None,
    capabilities: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    """Create a new Connect account."""
    data = {"type": type, "country": country}
    if email:
        data["email"] = email
    if capabilities:
        data["capabilities"] = json.dumps(capabilities)
    if metadata:
        data["metadata"] = metadata
    return stripe_request("POST", "/v1/accounts", data=data)


@mcp.tool()
def update_connect_account(
    account_id: str,
    email: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    settings: Optional[Dict[str, Any]] = None,
    capabilities: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Update a Connect account."""
    data = {}
    if email is not None:
        data["email"] = email
    if metadata:
        data["metadata"] = metadata
    if settings:
        data["settings"] = json.dumps(settings)
    if capabilities:
        data["capabilities"] = json.dumps(capabilities)
    return stripe_request("POST", f"/v1/accounts/{account_id}", data=data)


@mcp.tool()
def delete_connect_account(account_id: str) -> Dict[str, Any]:
    """Delete a Connect account."""
    return stripe_request("DELETE", f"/v1/accounts/{account_id}")


# Balance

@mcp.tool()
def get_balance() -> Dict[str, Any]:
    """Retrieve the current balance."""
    return stripe_request("GET", "/v1/balance")


@mcp.tool()
def get_balance_transaction(transaction_id: str) -> Dict[str, Any]:
    """Retrieve a balance transaction by ID."""
    return stripe_request("GET", f"/v1/balance_transactions/{transaction_id}")


@mcp.tool()
def list_balance_transactions(
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    type: Optional[str] = None,
) -> Dict[str, Any]:
    """List balance transactions."""
    params = {"limit": limit}
    if starting_after:
        params["starting_after"] = starting_after
    if ending_before:
        params["ending_before"] = ending_before
    if type:
        params["type"] = type
    return stripe_request("GET", "/v1/balance_transactions", params=params)


# Transfers

@mcp.tool()
def get_transfer(transfer_id: str) -> Dict[str, Any]:
    """Retrieve a transfer by ID."""
    return stripe_request("GET", f"/v1/transfers/{transfer_id}")


@mcp.tool()
def list_transfers(
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    destination: Optional[str] = None,
    status: Optional[str] = None,
) -> Dict[str, Any]:
    """List transfers with optional filtering."""
    params = {"limit": limit}
    if starting_after:
        params["starting_after"] = starting_after
    if ending_before:
        params["ending_before"] = ending_before
    if destination:
        params["destination"] = destination
    if status:
        params["status"] = status
    return stripe_request("GET", "/v1/transfers", params=params)


@mcp.tool()
def create_transfer(
    amount: int,
    currency: str,
    destination: str,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    """Create a new transfer."""
    data = {
        "amount": amount,
        "currency": currency,
        "destination": destination,
    }
    if description:
        data["description"] = description
    if metadata:
        data["metadata"] = metadata
    return stripe_request("POST", "/v1/transfers", data=data)


@mcp.tool()
def cancel_transfer(transfer_id: str) -> Dict[str, Any]:
    """Cancel a transfer."""
    return stripe_request("POST", f"/v1/transfers/{transfer_id}/cancel")


# Payouts

@mcp.tool()
def get_payout(payout_id: str) -> Dict[str, Any]:
    """Retrieve a payout by ID."""
    return stripe_request("GET", f"/v1/payouts/{payout_id}")


@mcp.tool()
def list_payouts(
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    status: Optional[str] = None,
) -> Dict[str, Any]:
    """List payouts with optional filtering."""
    params = {"limit": limit}
    if starting_after:
        params["starting_after"] = starting_after
    if ending_before:
        params["ending_before"] = ending_before
    if status:
        params["status"] = status
    return stripe_request("GET", "/v1/payouts", params=params)


@mcp.tool()
def create_payout(
    amount: int,
    currency: str,
    method: str = "standard",
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    """Create a new payout."""
    data = {
        "amount": amount,
        "currency": currency,
        "method": method,
    }
    if description:
        data["description"] = description
    if metadata:
        data["metadata"] = metadata
    return stripe_request("POST", "/v1/payouts", data=data)


@mcp.tool()
def cancel_payout(payout_id: str) -> Dict[str, Any]:
    """Cancel a payout."""
    return stripe_request("POST", f"/v1/payouts/{payout_id}/cancel")


# Events

@mcp.tool()
def get_event(event_id: str) -> Dict[str, Any]:
    """Retrieve an event by ID."""
    return stripe_request("GET", f"/v1/events/{event_id}")


@mcp.tool()
def list_events(
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    types: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """List events with optional filtering."""
    params = {"limit": limit}
    if starting_after:
        params["starting_after"] = starting_after
    if ending_before:
        params["ending_before"] = ending_before
    if types:
        for i, t in enumerate(types):
            params[f"types[{i}]"] = t
    return stripe_request("GET", "/v1/events", params=params)


# Invoice Items

@mcp.tool()
def get_invoice_item(invoice_item_id: str) -> Dict[str, Any]:
    """Retrieve an invoice item by ID."""
    return stripe_request("GET", f"/v1/invoiceitems/{invoice_item_id}")


@mcp.tool()
def list_invoice_items(
    customer: str,
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
) -> Dict[str, Any]:
    """List invoice items for a customer."""
    params = {"customer": customer, "limit": limit}
    if starting_after:
        params["starting_after"] = starting_after
    if ending_before:
        params["ending_before"] = ending_before
    return stripe_request("GET", "/v1/invoiceitems", params=params)


@mcp.tool()
def create_invoice_item(
    customer: str,
    price: Optional[str] = None,
    quantity: Optional[int] = 1,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    """Create a new invoice item."""
    data = {"customer": customer, "quantity": quantity}
    if price:
        data["price"] = price
    if description:
        data["description"] = description
    if metadata:
        data["metadata"] = metadata
    return stripe_request("POST", "/v1/invoiceitems", data=data)


@mcp.tool()
def delete_invoice_item(invoice_item_id: str) -> Dict[str, Any]:
    """Delete an invoice item."""
    return stripe_request("DELETE", f"/v1/invoiceitems/{invoice_item_id}")


# Subscription Items

@mcp.tool()
def get_subscription_item(subscription_item_id: str) -> Dict[str, Any]:
    """Retrieve a subscription item by ID."""
    return stripe_request("GET", f"/v1/subscription_items/{subscription_item_id}")


@mcp.tool()
def list_subscription_items(
    subscription_id: str,
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
) -> Dict[str, Any]:
    """List subscription items for a subscription."""
    params = {"limit": limit}
    if starting_after:
        params["starting_after"] = starting_after
    if ending_before:
        params["ending_before"] = ending_before
    return stripe_request("GET", f"/v1/subscriptions/{subscription_id}/items", params=params)


@mcp.tool()
def create_subscription_item(
    subscription_id: str,
    price: Optional[str] = None,
    quantity: Optional[int] = 1,
    metadata: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    """Create a new subscription item."""
    data = {"quantity": quantity}
    if price:
        data["price"] = price
    if metadata:
        data["metadata"] = metadata
    return stripe_request("POST", f"/v1/subscriptions/{subscription_id}/items", data=data)


@mcp.tool()
def update_subscription_item(
    subscription_item_id: str,
    quantity: Optional[int] = None,
    price: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    """Update a subscription item."""
    data = {}
    if quantity is not None:
        data["quantity"] = quantity
    if price:
        data["price"] = price
    if metadata:
        data["metadata"] = metadata
    return stripe_request("POST", f"/v1/subscription_items/{subscription_item_id}", data=data)


@mcp.tool()
def delete_subscription_item(subscription_item_id: str) -> Dict[str, Any]:
    """Delete a subscription item."""
    return stripe_request("DELETE", f"/v1/subscription_items/{subscription_item_id}")


# Standard tools

@mcp.tool()
def get_account() -> Dict[str, Any]:
    """Retrieve the account details."""
    return stripe_request("GET", "/v1/account")


if __name__ == "__main__":
    mcp.run()
