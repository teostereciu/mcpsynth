#!/usr/bin/env python3
"""
MCP Server for Stripe API
Provides tools for interacting with the Stripe API over the MCP protocol.
"""

import os
import json
import requests
from typing import Any, Dict, Optional
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
server = FastMCP("stripe-api")

# Configuration
STRIPE_API_KEY = os.environ.get("STRIPE_API_KEY", "")
BASE_URL = "https://api.stripe.com/v1"

# Helper function to make API requests
def stripe_request(
    method: str,
    endpoint: str,
    params: Optional[Dict[str, Any]] = None,
    data: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Make a request to the Stripe API."""
    if not STRIPE_API_KEY:
        return {"error": "STRIPE_API_KEY environment variable not set"}
    
    url = f"{BASE_URL}{endpoint}"
    headers = {
        "Authorization": f"Bearer {STRIPE_API_KEY}",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    
    try:
        if method == "GET":
            response = requests.get(url, params=params, headers=headers, timeout=30)
        elif method == "POST":
            response = requests.post(url, data=data, headers=headers, timeout=30)
        elif method == "DELETE":
            response = requests.delete(url, params=params, headers=headers, timeout=30)
        else:
            return {"error": f"Unsupported HTTP method: {method}"}
        
        if response.status_code >= 400:
            return {"error": f"API error {response.status_code}: {response.text}"}
        
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}
    except json.JSONDecodeError:
        return {"error": "Failed to parse API response"}


# ============================================================================
# PAYMENT INTENTS
# ============================================================================

@server.tool()
def create_payment_intent(
    amount: int,
    currency: str,
    customer: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    payment_method: Optional[str] = None,
    confirm: Optional[bool] = None,
    return_url: Optional[str] = None,
    statement_descriptor: Optional[str] = None,
) -> Dict[str, Any]:
    """Create a payment intent for processing payments."""
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
    if payment_method:
        data["payment_method"] = payment_method
    if confirm is not None:
        data["confirm"] = str(confirm).lower()
    if return_url:
        data["return_url"] = return_url
    if statement_descriptor:
        data["statement_descriptor"] = statement_descriptor
    
    return stripe_request("POST", "/payment_intents", data=data)


@server.tool()
def get_payment_intent(payment_intent_id: str) -> Dict[str, Any]:
    """Retrieve a payment intent by ID."""
    return stripe_request("GET", f"/payment_intents/{payment_intent_id}")


@server.tool()
def update_payment_intent(
    payment_intent_id: str,
    amount: Optional[int] = None,
    customer: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    payment_method: Optional[str] = None,
    statement_descriptor: Optional[str] = None,
) -> Dict[str, Any]:
    """Update a payment intent."""
    data = {}
    if amount is not None:
        data["amount"] = amount
    if customer:
        data["customer"] = customer
    if description:
        data["description"] = description
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    if payment_method:
        data["payment_method"] = payment_method
    if statement_descriptor:
        data["statement_descriptor"] = statement_descriptor
    
    return stripe_request("POST", f"/payment_intents/{payment_intent_id}", data=data)


@server.tool()
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
    
    return stripe_request("POST", f"/payment_intents/{payment_intent_id}/confirm", data=data)


@server.tool()
def cancel_payment_intent(
    payment_intent_id: str,
    cancellation_reason: Optional[str] = None,
) -> Dict[str, Any]:
    """Cancel a payment intent."""
    data = {}
    if cancellation_reason:
        data["cancellation_reason"] = cancellation_reason
    
    return stripe_request("POST", f"/payment_intents/{payment_intent_id}/cancel", data=data)


@server.tool()
def list_payment_intents(
    limit: Optional[int] = None,
    customer: Optional[str] = None,
    created_after: Optional[int] = None,
    created_before: Optional[int] = None,
) -> Dict[str, Any]:
    """List payment intents."""
    params = {}
    if limit:
        params["limit"] = limit
    if customer:
        params["customer"] = customer
    if created_after:
        params["created[gte]"] = created_after
    if created_before:
        params["created[lte]"] = created_before
    
    return stripe_request("GET", "/payment_intents", params=params)


# ============================================================================
# CHARGES
# ============================================================================

@server.tool()
def create_charge(
    amount: int,
    currency: str,
    source: Optional[str] = None,
    customer: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    statement_descriptor: Optional[str] = None,
) -> Dict[str, Any]:
    """Create a charge."""
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
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    if statement_descriptor:
        data["statement_descriptor"] = statement_descriptor
    
    return stripe_request("POST", "/charges", data=data)


@server.tool()
def get_charge(charge_id: str) -> Dict[str, Any]:
    """Retrieve a charge by ID."""
    return stripe_request("GET", f"/charges/{charge_id}")


@server.tool()
def update_charge(
    charge_id: str,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    """Update a charge."""
    data = {}
    if description:
        data["description"] = description
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return stripe_request("POST", f"/charges/{charge_id}", data=data)


@server.tool()
def list_charges(
    limit: Optional[int] = None,
    customer: Optional[str] = None,
    created_after: Optional[int] = None,
    created_before: Optional[int] = None,
) -> Dict[str, Any]:
    """List charges."""
    params = {}
    if limit:
        params["limit"] = limit
    if customer:
        params["customer"] = customer
    if created_after:
        params["created[gte]"] = created_after
    if created_before:
        params["created[lte]"] = created_before
    
    return stripe_request("GET", "/charges", params=params)


# ============================================================================
# REFUNDS
# ============================================================================

@server.tool()
def create_refund(
    charge_id: Optional[str] = None,
    payment_intent_id: Optional[str] = None,
    amount: Optional[int] = None,
    reason: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    """Create a refund."""
    data = {}
    if charge_id:
        data["charge"] = charge_id
    if payment_intent_id:
        data["payment_intent"] = payment_intent_id
    if amount is not None:
        data["amount"] = amount
    if reason:
        data["reason"] = reason
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return stripe_request("POST", "/refunds", data=data)


@server.tool()
def get_refund(refund_id: str) -> Dict[str, Any]:
    """Retrieve a refund by ID."""
    return stripe_request("GET", f"/refunds/{refund_id}")


@server.tool()
def update_refund(
    refund_id: str,
    metadata: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    """Update a refund."""
    data = {}
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return stripe_request("POST", f"/refunds/{refund_id}", data=data)


@server.tool()
def list_refunds(
    limit: Optional[int] = None,
    charge_id: Optional[str] = None,
    payment_intent_id: Optional[str] = None,
    created_after: Optional[int] = None,
    created_before: Optional[int] = None,
) -> Dict[str, Any]:
    """List refunds."""
    params = {}
    if limit:
        params["limit"] = limit
    if charge_id:
        params["charge"] = charge_id
    if payment_intent_id:
        params["payment_intent"] = payment_intent_id
    if created_after:
        params["created[gte]"] = created_after
    if created_before:
        params["created[lte]"] = created_before
    
    return stripe_request("GET", "/refunds", params=params)


# ============================================================================
# CUSTOMERS
# ============================================================================

@server.tool()
def create_customer(
    email: Optional[str] = None,
    name: Optional[str] = None,
    description: Optional[str] = None,
    phone: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    payment_method: Optional[str] = None,
    invoice_settings: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Create a customer."""
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
    if payment_method:
        data["payment_method"] = payment_method
    if invoice_settings:
        for key, value in invoice_settings.items():
            data[f"invoice_settings[{key}]"] = value
    
    return stripe_request("POST", "/customers", data=data)


@server.tool()
def get_customer(customer_id: str) -> Dict[str, Any]:
    """Retrieve a customer by ID."""
    return stripe_request("GET", f"/customers/{customer_id}")


@server.tool()
def update_customer(
    customer_id: str,
    email: Optional[str] = None,
    name: Optional[str] = None,
    description: Optional[str] = None,
    phone: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    """Update a customer."""
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
    
    return stripe_request("POST", f"/customers/{customer_id}", data=data)


@server.tool()
def delete_customer(customer_id: str) -> Dict[str, Any]:
    """Delete a customer."""
    return stripe_request("DELETE", f"/customers/{customer_id}")


@server.tool()
def list_customers(
    limit: Optional[int] = None,
    email: Optional[str] = None,
    created_after: Optional[int] = None,
    created_before: Optional[int] = None,
) -> Dict[str, Any]:
    """List customers."""
    params = {}
    if limit:
        params["limit"] = limit
    if email:
        params["email"] = email
    if created_after:
        params["created[gte]"] = created_after
    if created_before:
        params["created[lte]"] = created_before
    
    return stripe_request("GET", "/customers", params=params)


# ============================================================================
# PRODUCTS
# ============================================================================

@server.tool()
def create_product(
    name: str,
    type: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    active: Optional[bool] = None,
    url: Optional[str] = None,
) -> Dict[str, Any]:
    """Create a product."""
    data = {"name": name}
    if type:
        data["type"] = type
    if description:
        data["description"] = description
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    if active is not None:
        data["active"] = str(active).lower()
    if url:
        data["url"] = url
    
    return stripe_request("POST", "/products", data=data)


@server.tool()
def get_product(product_id: str) -> Dict[str, Any]:
    """Retrieve a product by ID."""
    return stripe_request("GET", f"/products/{product_id}")


@server.tool()
def update_product(
    product_id: str,
    name: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    active: Optional[bool] = None,
    url: Optional[str] = None,
) -> Dict[str, Any]:
    """Update a product."""
    data = {}
    if name:
        data["name"] = name
    if description:
        data["description"] = description
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    if active is not None:
        data["active"] = str(active).lower()
    if url:
        data["url"] = url
    
    return stripe_request("POST", f"/products/{product_id}", data=data)


@server.tool()
def delete_product(product_id: str) -> Dict[str, Any]:
    """Delete a product."""
    return stripe_request("DELETE", f"/products/{product_id}")


@server.tool()
def list_products(
    limit: Optional[int] = None,
    active: Optional[bool] = None,
    created_after: Optional[int] = None,
    created_before: Optional[int] = None,
) -> Dict[str, Any]:
    """List products."""
    params = {}
    if limit:
        params["limit"] = limit
    if active is not None:
        params["active"] = str(active).lower()
    if created_after:
        params["created[gte]"] = created_after
    if created_before:
        params["created[lte]"] = created_before
    
    return stripe_request("GET", "/products", params=params)


# ============================================================================
# PRICES
# ============================================================================

@server.tool()
def create_price(
    product: str,
    currency: str,
    unit_amount: Optional[int] = None,
    recurring: Optional[Dict[str, Any]] = None,
    billing_scheme: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    nickname: Optional[str] = None,
) -> Dict[str, Any]:
    """Create a price."""
    data = {
        "product": product,
        "currency": currency,
    }
    if unit_amount is not None:
        data["unit_amount"] = unit_amount
    if recurring:
        for key, value in recurring.items():
            data[f"recurring[{key}]"] = value
    if billing_scheme:
        data["billing_scheme"] = billing_scheme
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    if nickname:
        data["nickname"] = nickname
    
    return stripe_request("POST", "/prices", data=data)


@server.tool()
def get_price(price_id: str) -> Dict[str, Any]:
    """Retrieve a price by ID."""
    return stripe_request("GET", f"/prices/{price_id}")


@server.tool()
def update_price(
    price_id: str,
    metadata: Optional[Dict[str, str]] = None,
    nickname: Optional[str] = None,
) -> Dict[str, Any]:
    """Update a price."""
    data = {}
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    if nickname:
        data["nickname"] = nickname
    
    return stripe_request("POST", f"/prices/{price_id}", data=data)


@server.tool()
def list_prices(
    limit: Optional[int] = None,
    product: Optional[str] = None,
    currency: Optional[str] = None,
    created_after: Optional[int] = None,
    created_before: Optional[int] = None,
) -> Dict[str, Any]:
    """List prices."""
    params = {}
    if limit:
        params["limit"] = limit
    if product:
        params["product"] = product
    if currency:
        params["currency"] = currency
    if created_after:
        params["created[gte]"] = created_after
    if created_before:
        params["created[lte]"] = created_before
    
    return stripe_request("GET", "/prices", params=params)


# ============================================================================
# SUBSCRIPTIONS
# ============================================================================

@server.tool()
def create_subscription(
    customer: str,
    items: list,
    billing_cycle_anchor: Optional[int] = None,
    collection_method: Optional[str] = None,
    currency: Optional[str] = None,
    days_until_due: Optional[int] = None,
    default_payment_method: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    off_session: Optional[bool] = None,
    payment_behavior: Optional[str] = None,
    payment_settings: Optional[Dict[str, Any]] = None,
    trial_end: Optional[int] = None,
    trial_period_days: Optional[int] = None,
) -> Dict[str, Any]:
    """Create a subscription."""
    data = {"customer": customer}
    
    # Add items
    for i, item in enumerate(items):
        for key, value in item.items():
            data[f"items[{i}][{key}]"] = value
    
    if billing_cycle_anchor is not None:
        data["billing_cycle_anchor"] = billing_cycle_anchor
    if collection_method:
        data["collection_method"] = collection_method
    if currency:
        data["currency"] = currency
    if days_until_due is not None:
        data["days_until_due"] = days_until_due
    if default_payment_method:
        data["default_payment_method"] = default_payment_method
    if description:
        data["description"] = description
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    if off_session is not None:
        data["off_session"] = str(off_session).lower()
    if payment_behavior:
        data["payment_behavior"] = payment_behavior
    if payment_settings:
        for key, value in payment_settings.items():
            data[f"payment_settings[{key}]"] = value
    if trial_end is not None:
        data["trial_end"] = trial_end
    if trial_period_days is not None:
        data["trial_period_days"] = trial_period_days
    
    return stripe_request("POST", "/subscriptions", data=data)


@server.tool()
def get_subscription(subscription_id: str) -> Dict[str, Any]:
    """Retrieve a subscription by ID."""
    return stripe_request("GET", f"/subscriptions/{subscription_id}")


@server.tool()
def update_subscription(
    subscription_id: str,
    billing_cycle_anchor: Optional[int] = None,
    collection_method: Optional[str] = None,
    currency: Optional[str] = None,
    days_until_due: Optional[int] = None,
    default_payment_method: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    payment_behavior: Optional[str] = None,
    trial_end: Optional[int] = None,
) -> Dict[str, Any]:
    """Update a subscription."""
    data = {}
    if billing_cycle_anchor is not None:
        data["billing_cycle_anchor"] = billing_cycle_anchor
    if collection_method:
        data["collection_method"] = collection_method
    if currency:
        data["currency"] = currency
    if days_until_due is not None:
        data["days_until_due"] = days_until_due
    if default_payment_method:
        data["default_payment_method"] = default_payment_method
    if description:
        data["description"] = description
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    if payment_behavior:
        data["payment_behavior"] = payment_behavior
    if trial_end is not None:
        data["trial_end"] = trial_end
    
    return stripe_request("POST", f"/subscriptions/{subscription_id}", data=data)


@server.tool()
def cancel_subscription(
    subscription_id: str,
    cancellation_details: Optional[Dict[str, str]] = None,
    invoice_now: Optional[bool] = None,
    prorate: Optional[bool] = None,
) -> Dict[str, Any]:
    """Cancel a subscription."""
    data = {}
    if cancellation_details:
        for key, value in cancellation_details.items():
            data[f"cancellation_details[{key}]"] = value
    if invoice_now is not None:
        data["invoice_now"] = str(invoice_now).lower()
    if prorate is not None:
        data["prorate"] = str(prorate).lower()
    
    return stripe_request("DELETE", f"/subscriptions/{subscription_id}", params=data)


@server.tool()
def list_subscriptions(
    limit: Optional[int] = None,
    customer: Optional[str] = None,
    status: Optional[str] = None,
    created_after: Optional[int] = None,
    created_before: Optional[int] = None,
) -> Dict[str, Any]:
    """List subscriptions."""
    params = {}
    if limit:
        params["limit"] = limit
    if customer:
        params["customer"] = customer
    if status:
        params["status"] = status
    if created_after:
        params["created[gte]"] = created_after
    if created_before:
        params["created[lte]"] = created_before
    
    return stripe_request("GET", "/subscriptions", params=params)


# ============================================================================
# INVOICES
# ============================================================================

@server.tool()
def create_invoice(
    customer: str,
    auto_advance: Optional[bool] = None,
    collection_method: Optional[str] = None,
    currency: Optional[str] = None,
    custom_fields: Optional[list] = None,
    days_until_due: Optional[int] = None,
    description: Optional[str] = None,
    due_date: Optional[int] = None,
    footer: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    statement_descriptor: Optional[str] = None,
) -> Dict[str, Any]:
    """Create an invoice."""
    data = {"customer": customer}
    if auto_advance is not None:
        data["auto_advance"] = str(auto_advance).lower()
    if collection_method:
        data["collection_method"] = collection_method
    if currency:
        data["currency"] = currency
    if custom_fields:
        for i, field in enumerate(custom_fields):
            for key, value in field.items():
                data[f"custom_fields[{i}][{key}]"] = value
    if days_until_due is not None:
        data["days_until_due"] = days_until_due
    if description:
        data["description"] = description
    if due_date is not None:
        data["due_date"] = due_date
    if footer:
        data["footer"] = footer
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    if statement_descriptor:
        data["statement_descriptor"] = statement_descriptor
    
    return stripe_request("POST", "/invoices", data=data)


@server.tool()
def get_invoice(invoice_id: str) -> Dict[str, Any]:
    """Retrieve an invoice by ID."""
    return stripe_request("GET", f"/invoices/{invoice_id}")


@server.tool()
def update_invoice(
    invoice_id: str,
    auto_advance: Optional[bool] = None,
    collection_method: Optional[str] = None,
    currency: Optional[str] = None,
    days_until_due: Optional[int] = None,
    description: Optional[str] = None,
    due_date: Optional[int] = None,
    footer: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    statement_descriptor: Optional[str] = None,
) -> Dict[str, Any]:
    """Update an invoice."""
    data = {}
    if auto_advance is not None:
        data["auto_advance"] = str(auto_advance).lower()
    if collection_method:
        data["collection_method"] = collection_method
    if currency:
        data["currency"] = currency
    if days_until_due is not None:
        data["days_until_due"] = days_until_due
    if description:
        data["description"] = description
    if due_date is not None:
        data["due_date"] = due_date
    if footer:
        data["footer"] = footer
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    if statement_descriptor:
        data["statement_descriptor"] = statement_descriptor
    
    return stripe_request("POST", f"/invoices/{invoice_id}", data=data)


@server.tool()
def finalize_invoice(invoice_id: str, auto_advance: Optional[bool] = None) -> Dict[str, Any]:
    """Finalize an invoice."""
    data = {}
    if auto_advance is not None:
        data["auto_advance"] = str(auto_advance).lower()
    
    return stripe_request("POST", f"/invoices/{invoice_id}/finalize", data=data)


@server.tool()
def pay_invoice(
    invoice_id: str,
    paid_out_of_band: Optional[bool] = None,
    payment_method: Optional[str] = None,
    source: Optional[str] = None,
) -> Dict[str, Any]:
    """Pay an invoice."""
    data = {}
    if paid_out_of_band is not None:
        data["paid_out_of_band"] = str(paid_out_of_band).lower()
    if payment_method:
        data["payment_method"] = payment_method
    if source:
        data["source"] = source
    
    return stripe_request("POST", f"/invoices/{invoice_id}/pay", data=data)


@server.tool()
def send_invoice(invoice_id: str) -> Dict[str, Any]:
    """Send an invoice."""
    return stripe_request("POST", f"/invoices/{invoice_id}/send", data={})


@server.tool()
def void_invoice(invoice_id: str) -> Dict[str, Any]:
    """Void an invoice."""
    return stripe_request("POST", f"/invoices/{invoice_id}/void", data={})


@server.tool()
def delete_invoice(invoice_id: str) -> Dict[str, Any]:
    """Delete an invoice."""
    return stripe_request("DELETE", f"/invoices/{invoice_id}")


@server.tool()
def list_invoices(
    limit: Optional[int] = None,
    customer: Optional[str] = None,
    status: Optional[str] = None,
    created_after: Optional[int] = None,
    created_before: Optional[int] = None,
) -> Dict[str, Any]:
    """List invoices."""
    params = {}
    if limit:
        params["limit"] = limit
    if customer:
        params["customer"] = customer
    if status:
        params["status"] = status
    if created_after:
        params["created[gte]"] = created_after
    if created_before:
        params["created[lte]"] = created_before
    
    return stripe_request("GET", "/invoices", params=params)


# ============================================================================
# CHECKOUT SESSIONS
# ============================================================================

@server.tool()
def create_checkout_session(
    payment_method_types: list,
    mode: str,
    success_url: str,
    cancel_url: str,
    customer: Optional[str] = None,
    customer_email: Optional[str] = None,
    line_items: Optional[list] = None,
    subscription_data: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, str]] = None,
    locale: Optional[str] = None,
    payment_intent_data: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Create a checkout session."""
    data = {
        "mode": mode,
        "success_url": success_url,
        "cancel_url": cancel_url,
    }
    
    # Add payment method types
    for i, pmt_type in enumerate(payment_method_types):
        data[f"payment_method_types[{i}]"] = pmt_type
    
    if customer:
        data["customer"] = customer
    if customer_email:
        data["customer_email"] = customer_email
    
    # Add line items
    if line_items:
        for i, item in enumerate(line_items):
            for key, value in item.items():
                data[f"line_items[{i}][{key}]"] = value
    
    if subscription_data:
        for key, value in subscription_data.items():
            data[f"subscription_data[{key}]"] = value
    
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    if locale:
        data["locale"] = locale
    
    if payment_intent_data:
        for key, value in payment_intent_data.items():
            data[f"payment_intent_data[{key}]"] = value
    
    return stripe_request("POST", "/checkout/sessions", data=data)


@server.tool()
def get_checkout_session(session_id: str) -> Dict[str, Any]:
    """Retrieve a checkout session by ID."""
    return stripe_request("GET", f"/checkout/sessions/{session_id}")


@server.tool()
def list_checkout_sessions(
    limit: Optional[int] = None,
    customer: Optional[str] = None,
    payment_intent: Optional[str] = None,
    created_after: Optional[int] = None,
    created_before: Optional[int] = None,
) -> Dict[str, Any]:
    """List checkout sessions."""
    params = {}
    if limit:
        params["limit"] = limit
    if customer:
        params["customer"] = customer
    if payment_intent:
        params["payment_intent"] = payment_intent
    if created_after:
        params["created[gte]"] = created_after
    if created_before:
        params["created[lte]"] = created_before
    
    return stripe_request("GET", "/checkout/sessions", params=params)


# ============================================================================
# PAYMENT LINKS
# ============================================================================

@server.tool()
def create_payment_link(
    line_items: list,
    after_completion: Optional[Dict[str, Any]] = None,
    allow_promotion_codes: Optional[bool] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    billing_address_collection: Optional[str] = None,
    currency: Optional[str] = None,
    customer_creation: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    phone_number_collection: Optional[Dict[str, Any]] = None,
    shipping_address_collection: Optional[Dict[str, Any]] = None,
    subscription_data: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Create a payment link."""
    data = {}
    
    # Add line items
    for i, item in enumerate(line_items):
        for key, value in item.items():
            data[f"line_items[{i}][{key}]"] = value
    
    if after_completion:
        for key, value in after_completion.items():
            data[f"after_completion[{key}]"] = value
    
    if allow_promotion_codes is not None:
        data["allow_promotion_codes"] = str(allow_promotion_codes).lower()
    
    if automatic_tax:
        for key, value in automatic_tax.items():
            data[f"automatic_tax[{key}]"] = value
    
    if billing_address_collection:
        data["billing_address_collection"] = billing_address_collection
    
    if currency:
        data["currency"] = currency
    
    if customer_creation:
        data["customer_creation"] = customer_creation
    
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    if phone_number_collection:
        for key, value in phone_number_collection.items():
            data[f"phone_number_collection[{key}]"] = value
    
    if shipping_address_collection:
        for key, value in shipping_address_collection.items():
            data[f"shipping_address_collection[{key}]"] = value
    
    if subscription_data:
        for key, value in subscription_data.items():
            data[f"subscription_data[{key}]"] = value
    
    return stripe_request("POST", "/payment_links", data=data)


@server.tool()
def get_payment_link(payment_link_id: str) -> Dict[str, Any]:
    """Retrieve a payment link by ID."""
    return stripe_request("GET", f"/payment_links/{payment_link_id}")


@server.tool()
def update_payment_link(
    payment_link_id: str,
    active: Optional[bool] = None,
    after_completion: Optional[Dict[str, Any]] = None,
    allow_promotion_codes: Optional[bool] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    billing_address_collection: Optional[str] = None,
    customer_creation: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    phone_number_collection: Optional[Dict[str, Any]] = None,
    shipping_address_collection: Optional[Dict[str, Any]] = None,
    subscription_data: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Update a payment link."""
    data = {}
    
    if active is not None:
        data["active"] = str(active).lower()
    
    if after_completion:
        for key, value in after_completion.items():
            data[f"after_completion[{key}]"] = value
    
    if allow_promotion_codes is not None:
        data["allow_promotion_codes"] = str(allow_promotion_codes).lower()
    
    if automatic_tax:
        for key, value in automatic_tax.items():
            data[f"automatic_tax[{key}]"] = value
    
    if billing_address_collection:
        data["billing_address_collection"] = billing_address_collection
    
    if customer_creation:
        data["customer_creation"] = customer_creation
    
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    if phone_number_collection:
        for key, value in phone_number_collection.items():
            data[f"phone_number_collection[{key}]"] = value
    
    if shipping_address_collection:
        for key, value in shipping_address_collection.items():
            data[f"shipping_address_collection[{key}]"] = value
    
    if subscription_data:
        for key, value in subscription_data.items():
            data[f"subscription_data[{key}]"] = value
    
    return stripe_request("POST", f"/payment_links/{payment_link_id}", data=data)


@server.tool()
def list_payment_links(
    limit: Optional[int] = None,
    active: Optional[bool] = None,
    created_after: Optional[int] = None,
    created_before: Optional[int] = None,
) -> Dict[str, Any]:
    """List payment links."""
    params = {}
    if limit:
        params["limit"] = limit
    if active is not None:
        params["active"] = str(active).lower()
    if created_after:
        params["created[gte]"] = created_after
    if created_before:
        params["created[lte]"] = created_before
    
    return stripe_request("GET", "/payment_links", params=params)


# ============================================================================
# SETUP INTENTS
# ============================================================================

@server.tool()
def create_setup_intent(
    confirm: Optional[bool] = None,
    customer: Optional[str] = None,
    description: Optional[str] = None,
    flow_directions: Optional[list] = None,
    metadata: Optional[Dict[str, str]] = None,
    payment_method: Optional[str] = None,
    payment_method_types: Optional[list] = None,
    single_use_mandate: Optional[bool] = None,
    usage: Optional[str] = None,
) -> Dict[str, Any]:
    """Create a setup intent."""
    data = {}
    if confirm is not None:
        data["confirm"] = str(confirm).lower()
    if customer:
        data["customer"] = customer
    if description:
        data["description"] = description
    if flow_directions:
        for i, direction in enumerate(flow_directions):
            data[f"flow_directions[{i}]"] = direction
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    if payment_method:
        data["payment_method"] = payment_method
    if payment_method_types:
        for i, pmt_type in enumerate(payment_method_types):
            data[f"payment_method_types[{i}]"] = pmt_type
    if single_use_mandate is not None:
        data["single_use_mandate"] = str(single_use_mandate).lower()
    if usage:
        data["usage"] = usage
    
    return stripe_request("POST", "/setup_intents", data=data)


@server.tool()
def get_setup_intent(setup_intent_id: str) -> Dict[str, Any]:
    """Retrieve a setup intent by ID."""
    return stripe_request("GET", f"/setup_intents/{setup_intent_id}")


@server.tool()
def update_setup_intent(
    setup_intent_id: str,
    customer: Optional[str] = None,
    description: Optional[str] = None,
    flow_directions: Optional[list] = None,
    metadata: Optional[Dict[str, str]] = None,
    payment_method: Optional[str] = None,
) -> Dict[str, Any]:
    """Update a setup intent."""
    data = {}
    if customer:
        data["customer"] = customer
    if description:
        data["description"] = description
    if flow_directions:
        for i, direction in enumerate(flow_directions):
            data[f"flow_directions[{i}]"] = direction
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    if payment_method:
        data["payment_method"] = payment_method
    
    return stripe_request("POST", f"/setup_intents/{setup_intent_id}", data=data)


@server.tool()
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
    
    return stripe_request("POST", f"/setup_intents/{setup_intent_id}/confirm", data=data)


@server.tool()
def cancel_setup_intent(setup_intent_id: str, cancellation_reason: Optional[str] = None) -> Dict[str, Any]:
    """Cancel a setup intent."""
    data = {}
    if cancellation_reason:
        data["cancellation_reason"] = cancellation_reason
    
    return stripe_request("POST", f"/setup_intents/{setup_intent_id}/cancel", data=data)


@server.tool()
def list_setup_intents(
    limit: Optional[int] = None,
    customer: Optional[str] = None,
    created_after: Optional[int] = None,
    created_before: Optional[int] = None,
) -> Dict[str, Any]:
    """List setup intents."""
    params = {}
    if limit:
        params["limit"] = limit
    if customer:
        params["customer"] = customer
    if created_after:
        params["created[gte]"] = created_after
    if created_before:
        params["created[lte]"] = created_before
    
    return stripe_request("GET", "/setup_intents", params=params)


# ============================================================================
# COUPONS
# ============================================================================

@server.tool()
def create_coupon(
    duration: str,
    amount_off: Optional[int] = None,
    currency: Optional[str] = None,
    duration_in_months: Optional[int] = None,
    id: Optional[str] = None,
    max_redemptions: Optional[int] = None,
    metadata: Optional[Dict[str, str]] = None,
    percent_off: Optional[float] = None,
    redeem_by: Optional[int] = None,
) -> Dict[str, Any]:
    """Create a coupon."""
    data = {"duration": duration}
    if amount_off is not None:
        data["amount_off"] = amount_off
    if currency:
        data["currency"] = currency
    if duration_in_months is not None:
        data["duration_in_months"] = duration_in_months
    if id:
        data["id"] = id
    if max_redemptions is not None:
        data["max_redemptions"] = max_redemptions
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    if percent_off is not None:
        data["percent_off"] = percent_off
    if redeem_by is not None:
        data["redeem_by"] = redeem_by
    
    return stripe_request("POST", "/coupons", data=data)


@server.tool()
def get_coupon(coupon_id: str) -> Dict[str, Any]:
    """Retrieve a coupon by ID."""
    return stripe_request("GET", f"/coupons/{coupon_id}")


@server.tool()
def update_coupon(
    coupon_id: str,
    metadata: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    """Update a coupon."""
    data = {}
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return stripe_request("POST", f"/coupons/{coupon_id}", data=data)


@server.tool()
def delete_coupon(coupon_id: str) -> Dict[str, Any]:
    """Delete a coupon."""
    return stripe_request("DELETE", f"/coupons/{coupon_id}")


@server.tool()
def list_coupons(
    limit: Optional[int] = None,
    created_after: Optional[int] = None,
    created_before: Optional[int] = None,
) -> Dict[str, Any]:
    """List coupons."""
    params = {}
    if limit:
        params["limit"] = limit
    if created_after:
        params["created[gte]"] = created_after
    if created_before:
        params["created[lte]"] = created_before
    
    return stripe_request("GET", "/coupons", params=params)


# ============================================================================
# PROMOTION CODES
# ============================================================================

@server.tool()
def create_promotion_code(
    coupon: str,
    active: Optional[bool] = None,
    code: Optional[str] = None,
    customer: Optional[str] = None,
    expires_at: Optional[int] = None,
    max_redemptions: Optional[int] = None,
    metadata: Optional[Dict[str, str]] = None,
    restrictions: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Create a promotion code."""
    data = {"coupon": coupon}
    if active is not None:
        data["active"] = str(active).lower()
    if code:
        data["code"] = code
    if customer:
        data["customer"] = customer
    if expires_at is not None:
        data["expires_at"] = expires_at
    if max_redemptions is not None:
        data["max_redemptions"] = max_redemptions
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    if restrictions:
        for key, value in restrictions.items():
            data[f"restrictions[{key}]"] = value
    
    return stripe_request("POST", "/promotion_codes", data=data)


@server.tool()
def get_promotion_code(promotion_code_id: str) -> Dict[str, Any]:
    """Retrieve a promotion code by ID."""
    return stripe_request("GET", f"/promotion_codes/{promotion_code_id}")


@server.tool()
def update_promotion_code(
    promotion_code_id: str,
    active: Optional[bool] = None,
    expires_at: Optional[int] = None,
    metadata: Optional[Dict[str, str]] = None,
    restrictions: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Update a promotion code."""
    data = {}
    if active is not None:
        data["active"] = str(active).lower()
    if expires_at is not None:
        data["expires_at"] = expires_at
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    if restrictions:
        for key, value in restrictions.items():
            data[f"restrictions[{key}]"] = value
    
    return stripe_request("POST", f"/promotion_codes/{promotion_code_id}", data=data)


@server.tool()
def list_promotion_codes(
    limit: Optional[int] = None,
    active: Optional[bool] = None,
    coupon: Optional[str] = None,
    customer: Optional[str] = None,
    created_after: Optional[int] = None,
    created_before: Optional[int] = None,
) -> Dict[str, Any]:
    """List promotion codes."""
    params = {}
    if limit:
        params["limit"] = limit
    if active is not None:
        params["active"] = str(active).lower()
    if coupon:
        params["coupon"] = coupon
    if customer:
        params["customer"] = customer
    if created_after:
        params["created[gte]"] = created_after
    if created_before:
        params["created[lte]"] = created_before
    
    return stripe_request("GET", "/promotion_codes", params=params)


# ============================================================================
# PAYMENT METHODS
# ============================================================================

@server.tool()
def create_payment_method(
    type: str,
    billing_details: Optional[Dict[str, Any]] = None,
    card: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    """Create a payment method."""
    data = {"type": type}
    if billing_details:
        for key, value in billing_details.items():
            data[f"billing_details[{key}]"] = value
    if card:
        for key, value in card.items():
            data[f"card[{key}]"] = value
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return stripe_request("POST", "/payment_methods", data=data)


@server.tool()
def get_payment_method(payment_method_id: str) -> Dict[str, Any]:
    """Retrieve a payment method by ID."""
    return stripe_request("GET", f"/payment_methods/{payment_method_id}")


@server.tool()
def update_payment_method(
    payment_method_id: str,
    billing_details: Optional[Dict[str, Any]] = None,
    card: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    """Update a payment method."""
    data = {}
    if billing_details:
        for key, value in billing_details.items():
            data[f"billing_details[{key}]"] = value
    if card:
        for key, value in card.items():
            data[f"card[{key}]"] = value
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return stripe_request("POST", f"/payment_methods/{payment_method_id}", data=data)


@server.tool()
def attach_payment_method(payment_method_id: str, customer: str) -> Dict[str, Any]:
    """Attach a payment method to a customer."""
    data = {"customer": customer}
    return stripe_request("POST", f"/payment_methods/{payment_method_id}/attach", data=data)


@server.tool()
def detach_payment_method(payment_method_id: str) -> Dict[str, Any]:
    """Detach a payment method from a customer."""
    return stripe_request("POST", f"/payment_methods/{payment_method_id}/detach", data={})


@server.tool()
def list_payment_methods(
    customer: str,
    type: str,
    limit: Optional[int] = None,
) -> Dict[str, Any]:
    """List payment methods for a customer."""
    params = {
        "customer": customer,
        "type": type,
    }
    if limit:
        params["limit"] = limit
    
    return stripe_request("GET", "/payment_methods", params=params)


# ============================================================================
# CONNECT - ACCOUNTS
# ============================================================================

@server.tool()
def create_connect_account(
    type: str,
    country: str,
    email: str,
    business_profile: Optional[Dict[str, Any]] = None,
    business_type: Optional[str] = None,
    company: Optional[Dict[str, Any]] = None,
    individual: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, str]] = None,
    requested_capabilities: Optional[list] = None,
    settings: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Create a Connect account."""
    data = {
        "type": type,
        "country": country,
        "email": email,
    }
    if business_profile:
        for key, value in business_profile.items():
            data[f"business_profile[{key}]"] = value
    if business_type:
        data["business_type"] = business_type
    if company:
        for key, value in company.items():
            data[f"company[{key}]"] = value
    if individual:
        for key, value in individual.items():
            data[f"individual[{key}]"] = value
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    if requested_capabilities:
        for i, cap in enumerate(requested_capabilities):
            data[f"requested_capabilities[{i}]"] = cap
    if settings:
        for key, value in settings.items():
            data[f"settings[{key}]"] = value
    
    return stripe_request("POST", "/accounts", data=data)


@server.tool()
def get_connect_account(account_id: str) -> Dict[str, Any]:
    """Retrieve a Connect account by ID."""
    return stripe_request("GET", f"/accounts/{account_id}")


@server.tool()
def update_connect_account(
    account_id: str,
    business_profile: Optional[Dict[str, Any]] = None,
    business_type: Optional[str] = None,
    company: Optional[Dict[str, Any]] = None,
    individual: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, str]] = None,
    settings: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Update a Connect account."""
    data = {}
    if business_profile:
        for key, value in business_profile.items():
            data[f"business_profile[{key}]"] = value
    if business_type:
        data["business_type"] = business_type
    if company:
        for key, value in company.items():
            data[f"company[{key}]"] = value
    if individual:
        for key, value in individual.items():
            data[f"individual[{key}]"] = value
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    if settings:
        for key, value in settings.items():
            data[f"settings[{key}]"] = value
    
    return stripe_request("POST", f"/accounts/{account_id}", data=data)


@server.tool()
def delete_connect_account(account_id: str) -> Dict[str, Any]:
    """Delete a Connect account."""
    return stripe_request("DELETE", f"/accounts/{account_id}")


@server.tool()
def list_connect_accounts(
    limit: Optional[int] = None,
    created_after: Optional[int] = None,
    created_before: Optional[int] = None,
) -> Dict[str, Any]:
    """List Connect accounts."""
    params = {}
    if limit:
        params["limit"] = limit
    if created_after:
        params["created[gte]"] = created_after
    if created_before:
        params["created[lte]"] = created_before
    
    return stripe_request("GET", "/accounts", params=params)


# ============================================================================
# CONNECT - TRANSFERS
# ============================================================================

@server.tool()
def create_transfer(
    amount: int,
    currency: str,
    destination: str,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    source_transaction: Optional[str] = None,
    transfer_group: Optional[str] = None,
) -> Dict[str, Any]:
    """Create a transfer."""
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
    if source_transaction:
        data["source_transaction"] = source_transaction
    if transfer_group:
        data["transfer_group"] = transfer_group
    
    return stripe_request("POST", "/transfers", data=data)


@server.tool()
def get_transfer(transfer_id: str) -> Dict[str, Any]:
    """Retrieve a transfer by ID."""
    return stripe_request("GET", f"/transfers/{transfer_id}")


@server.tool()
def update_transfer(
    transfer_id: str,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    """Update a transfer."""
    data = {}
    if description:
        data["description"] = description
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return stripe_request("POST", f"/transfers/{transfer_id}", data=data)


@server.tool()
def list_transfers(
    limit: Optional[int] = None,
    destination: Optional[str] = None,
    created_after: Optional[int] = None,
    created_before: Optional[int] = None,
) -> Dict[str, Any]:
    """List transfers."""
    params = {}
    if limit:
        params["limit"] = limit
    if destination:
        params["destination"] = destination
    if created_after:
        params["created[gte]"] = created_after
    if created_before:
        params["created[lte]"] = created_before
    
    return stripe_request("GET", "/transfers", params=params)


# ============================================================================
# CONNECT - PAYOUTS
# ============================================================================

@server.tool()
def create_payout(
    amount: int,
    currency: str,
    destination: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    method: Optional[str] = None,
    original_payout: Optional[str] = None,
    source_type: Optional[str] = None,
    statement_descriptor: Optional[str] = None,
) -> Dict[str, Any]:
    """Create a payout."""
    data = {
        "amount": amount,
        "currency": currency,
    }
    if destination:
        data["destination"] = destination
    if description:
        data["description"] = description
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    if method:
        data["method"] = method
    if original_payout:
        data["original_payout"] = original_payout
    if source_type:
        data["source_type"] = source_type
    if statement_descriptor:
        data["statement_descriptor"] = statement_descriptor
    
    return stripe_request("POST", "/payouts", data=data)


@server.tool()
def get_payout(payout_id: str) -> Dict[str, Any]:
    """Retrieve a payout by ID."""
    return stripe_request("GET", f"/payouts/{payout_id}")


@server.tool()
def update_payout(
    payout_id: str,
    metadata: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    """Update a payout."""
    data = {}
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return stripe_request("POST", f"/payouts/{payout_id}", data=data)


@server.tool()
def cancel_payout(payout_id: str) -> Dict[str, Any]:
    """Cancel a payout."""
    return stripe_request("POST", f"/payouts/{payout_id}/cancel", data={})


@server.tool()
def reverse_payout(payout_id: str, metadata: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
    """Reverse a payout."""
    data = {}
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return stripe_request("POST", f"/payouts/{payout_id}/reverse", data=data)


@server.tool()
def list_payouts(
    limit: Optional[int] = None,
    status: Optional[str] = None,
    created_after: Optional[int] = None,
    created_before: Optional[int] = None,
) -> Dict[str, Any]:
    """List payouts."""
    params = {}
    if limit:
        params["limit"] = limit
    if status:
        params["status"] = status
    if created_after:
        params["created[gte]"] = created_after
    if created_before:
        params["created[lte]"] = created_before
    
    return stripe_request("GET", "/payouts", params=params)


# ============================================================================
# DISPUTES
# ============================================================================

@server.tool()
def get_dispute(dispute_id: str) -> Dict[str, Any]:
    """Retrieve a dispute by ID."""
    return stripe_request("GET", f"/disputes/{dispute_id}")


@server.tool()
def update_dispute(
    dispute_id: str,
    evidence: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, str]] = None,
    submit: Optional[bool] = None,
) -> Dict[str, Any]:
    """Update a dispute."""
    data = {}
    if evidence:
        for key, value in evidence.items():
            data[f"evidence[{key}]"] = value
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    if submit is not None:
        data["submit"] = str(submit).lower()
    
    return stripe_request("POST", f"/disputes/{dispute_id}", data=data)


@server.tool()
def close_dispute(dispute_id: str) -> Dict[str, Any]:
    """Close a dispute."""
    return stripe_request("POST", f"/disputes/{dispute_id}/close", data={})


@server.tool()
def list_disputes(
    limit: Optional[int] = None,
    charge: Optional[str] = None,
    payment_intent: Optional[str] = None,
    status: Optional[str] = None,
    created_after: Optional[int] = None,
    created_before: Optional[int] = None,
) -> Dict[str, Any]:
    """List disputes."""
    params = {}
    if limit:
        params["limit"] = limit
    if charge:
        params["charge"] = charge
    if payment_intent:
        params["payment_intent"] = payment_intent
    if status:
        params["status"] = status
    if created_after:
        params["created[gte]"] = created_after
    if created_before:
        params["created[lte]"] = created_before
    
    return stripe_request("GET", "/disputes", params=params)


# ============================================================================
# BALANCE
# ============================================================================

@server.tool()
def get_balance() -> Dict[str, Any]:
    """Retrieve the account balance."""
    return stripe_request("GET", "/balance")


@server.tool()
def list_balance_transactions(
    limit: Optional[int] = None,
    type: Optional[str] = None,
    available_on_after: Optional[int] = None,
    available_on_before: Optional[int] = None,
    created_after: Optional[int] = None,
    created_before: Optional[int] = None,
) -> Dict[str, Any]:
    """List balance transactions."""
    params = {}
    if limit:
        params["limit"] = limit
    if type:
        params["type"] = type
    if available_on_after:
        params["available_on[gte]"] = available_on_after
    if available_on_before:
        params["available_on[lte]"] = available_on_before
    if created_after:
        params["created[gte]"] = created_after
    if created_before:
        params["created[lte]"] = created_before
    
    return stripe_request("GET", "/balance_transactions", params=params)


# ============================================================================
# WEBHOOK ENDPOINTS
# ============================================================================

@server.tool()
def create_webhook_endpoint(
    url: str,
    enabled_events: list,
    api_version: Optional[str] = None,
) -> Dict[str, Any]:
    """Create a webhook endpoint."""
    data = {"url": url}
    for i, event in enumerate(enabled_events):
        data[f"enabled_events[{i}]"] = event
    if api_version:
        data["api_version"] = api_version
    
    return stripe_request("POST", "/webhook_endpoints", data=data)


@server.tool()
def get_webhook_endpoint(webhook_endpoint_id: str) -> Dict[str, Any]:
    """Retrieve a webhook endpoint by ID."""
    return stripe_request("GET", f"/webhook_endpoints/{webhook_endpoint_id}")


@server.tool()
def update_webhook_endpoint(
    webhook_endpoint_id: str,
    enabled_events: Optional[list] = None,
    url: Optional[str] = None,
) -> Dict[str, Any]:
    """Update a webhook endpoint."""
    data = {}
    if enabled_events:
        for i, event in enumerate(enabled_events):
            data[f"enabled_events[{i}]"] = event
    if url:
        data["url"] = url
    
    return stripe_request("POST", f"/webhook_endpoints/{webhook_endpoint_id}", data=data)


@server.tool()
def delete_webhook_endpoint(webhook_endpoint_id: str) -> Dict[str, Any]:
    """Delete a webhook endpoint."""
    return stripe_request("DELETE", f"/webhook_endpoints/{webhook_endpoint_id}")


@server.tool()
def list_webhook_endpoints(limit: Optional[int] = None) -> Dict[str, Any]:
    """List webhook endpoints."""
    params = {}
    if limit:
        params["limit"] = limit
    
    return stripe_request("GET", "/webhook_endpoints", params=params)


# ============================================================================
# EVENTS
# ============================================================================

@server.tool()
def get_event(event_id: str) -> Dict[str, Any]:
    """Retrieve an event by ID."""
    return stripe_request("GET", f"/events/{event_id}")


@server.tool()
def list_events(
    limit: Optional[int] = None,
    type: Optional[str] = None,
    created_after: Optional[int] = None,
    created_before: Optional[int] = None,
) -> Dict[str, Any]:
    """List events."""
    params = {}
    if limit:
        params["limit"] = limit
    if type:
        params["type"] = type
    if created_after:
        params["created[gte]"] = created_after
    if created_before:
        params["created[lte]"] = created_before
    
    return stripe_request("GET", "/events", params=params)


if __name__ == "__main__":
    server.run()
