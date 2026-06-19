#!/usr/bin/env python3
"""
Stripe MCP Server - FastMCP implementation for Stripe API
"""

import os
import requests
from fastmcp import FastMCP

mcp = FastMCP("stripe")

# Base URL for Stripe API
STRIPE_BASE_URL = "https://api.stripe.com"

# Get API key from environment
STRIPE_API_KEY = os.environ.get("STRIPE_API_KEY")

def _make_stripe_request(method, endpoint, params=None, data=None):
    """Make a Stripe API request with proper authentication and form encoding."""
    if not STRIPE_API_KEY:
        return {"error": "STRIPE_API_KEY environment variable is not set"}
    
    url = f"{STRIPE_BASE_URL}{endpoint}"
    headers = {
        "Authorization": f"Bearer {STRIPE_API_KEY}",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    
    try:
        if method.upper() == "GET":
            response = requests.get(url, headers=headers, params=params)
        elif method.upper() == "POST":
            response = requests.post(url, headers=headers, data=data)
        elif method.upper() == "DELETE":
            response = requests.delete(url, headers=headers, params=params)
        else:
            return {"error": f"Unsupported HTTP method: {method}"}
        
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        try:
            error_data = e.response.json()
            return {"error": error_data.get("error", {}).get("message", str(e))}
        except:
            return {"error": str(e)}
    except Exception as e:
        return {"error": str(e)}


# ========== Payment Intents ==========

@mcp.tool()
def create_payment_intent(
    amount: int,
    currency: str = "usd",
    description: str = None,
    customer: str = None,
    payment_method: str = None,
    confirm: bool = True,
    return_url: str = None,
) -> dict:
    """Create a PaymentIntent to collect a payment.
    
    Args:
        amount: Amount in cents to charge
        currency: Three-letter ISO currency code
        description: Description of the payment
        customer: Customer ID if recurring payments
        payment_method: Payment method ID
        confirm: Whether to immediately confirm the payment
        return_url: URL to redirect after payment
    
    Returns:
        PaymentIntent object
    """
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
    data["confirm"] = str(confirm).lower()
    if return_url:
        data["return_url"] = return_url
    
    return _make_stripe_request("POST", "/v1/payment_intents", data=data)


@mcp.tool()
def retrieve_payment_intent(id: str) -> dict:
    """Retrieve a PaymentIntent by ID."""
    return _make_stripe_request("GET", f"/v1/payment_intents/{id}")


@mcp.tool()
def update_payment_intent(id: str, **kwargs) -> dict:
    """Update a PaymentIntent's properties."""
    return _make_stripe_request("POST", f"/v1/payment_intents/{id}", data=kwargs)


@mcp.tool()
def confirm_payment_intent(id: str, payment_method: str = None) -> dict:
    """Confirm a PaymentIntent that is in the requires_confirmation status."""
    data = {}
    if payment_method:
        data["payment_method"] = payment_method
    return _make_stripe_request("POST", f"/v1/payment_intents/{id}/confirm", data=data)


@mcp.tool()
def cancel_payment_intent(id: str) -> dict:
    """Cancel a PaymentIntent that is in the requires_payment_method status."""
    return _make_stripe_request("POST", f"/v1/payment_intents/{id}/cancel")


@mcp.tool()
def capture_payment_intent(id: str, amount: int = None) -> dict:
    """Capture a PaymentIntent that is in the requires_capture status."""
    data = {}
    if amount:
        data["amount_to_capture"] = amount
    return _make_stripe_request("POST", f"/v1/payment_intents/{id}/capture", data=data)


@mcp.tool()
def list_payment_intents(limit: int = 10, customer: str = None, status: str = None) -> dict:
    """List PaymentIntents with filtering options."""
    params = {"limit": limit}
    if customer:
        params["customer"] = customer
    if status:
        params["status"] = status
    return _make_stripe_request("GET", "/v1/payment_intents", params=params)


# ========== Charges ==========

@mcp.tool()
def create_charge(
    amount: int,
    currency: str = "usd",
    source: str = None,
    customer: str = None,
    description: str = None,
    metadata: dict = None,
    receipt_email: str = None,
) -> dict:
    """Create a Charge to collect a payment.
    
    Args:
        amount: Amount in cents to charge
        currency: Three-letter ISO currency code
        source: Payment source ID (token, card, or source)
        customer: Customer ID
        description: Description of the charge
        metadata: Custom metadata as key-value pairs
        receipt_email: Email to send receipt to
    
    Returns:
        Charge object
    """
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
    
    # Convert metadata to Stripe format
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return _make_stripe_request("POST", "/v1/charges", data=data)


@mcp.tool()
def retrieve_charge(id: str) -> dict:
    """Retrieve a Charge by ID."""
    return _make_stripe_request("GET", f"/v1/charges/{id}")


@mcp.tool()
def update_charge(id: str, **kwargs) -> dict:
    """Update a Charge's properties."""
    return _make_stripe_request("POST", f"/v1/charges/{id}", data=kwargs)


@mcp.tool()
def capture_charge(id: str, amount: int = None) -> dict:
    """Capture a Charge that was created with capture=false."""
    data = {}
    if amount:
        data["amount"] = amount
    return _make_stripe_request("POST", f"/v1/charges/{id}/capture", data=data)


@mcp.tool()
def refund_charge(id: str, amount: int = None, reason: str = None) -> dict:
    """Create a refund for a Charge."""
    data = {}
    if amount:
        data["amount"] = amount
    if reason:
        data["reason"] = reason
    return _make_stripe_request("POST", f"/v1/charges/{id}/refunds", data=data)


@mcp.tool()
def list_charges(limit: int = 10, customer: str = None, created: str = None) -> dict:
    """List Charges with filtering options."""
    params = {"limit": limit}
    if customer:
        params["customer"] = customer
    if created:
        params["created"] = created
    return _make_stripe_request("GET", "/v1/charges", params=params)


# ========== Refunds ==========

@mcp.tool()
def retrieve_refund(charge_id: str, refund_id: str) -> dict:
    """Retrieve a Refund by ID for a specific Charge."""
    return _make_stripe_request("GET", f"/v1/charges/{charge_id}/refunds/{refund_id}")


@mcp.tool()
def update_refund(charge_id: str, refund_id: str, metadata: dict = None) -> dict:
    """Update a Refund's properties."""
    data = {}
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    return _make_stripe_request("POST", f"/v1/charges/{charge_id}/refunds/{refund_id}", data=data)


@mcp.tool()
def list_refunds(charge_id: str, limit: int = 10) -> dict:
    """List Refunds for a specific Charge."""
    params = {"limit": limit}
    return _make_stripe_request("GET", f"/v1/charges/{charge_id}/refunds", params=params)


# ========== Customers ==========

@mcp.tool()
def create_customer(
    name: str = None,
    email: str = None,
    phone: str = None,
    description: str = None,
    metadata: dict = None,
    address: dict = None,
) -> dict:
    """Create a Customer object.
    
    Args:
        name: Customer's name
        email: Customer's email address
        phone: Customer's phone number
        description: Description of the customer
        metadata: Custom metadata
        address: Customer's address
    
    Returns:
        Customer object
    """
    data = {}
    if name:
        data["name"] = name
    if email:
        data["email"] = email
    if phone:
        data["phone"] = phone
    if description:
        data["description"] = description
    if address:
        data["address"] = address
    
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return _make_stripe_request("POST", "/v1/customers", data=data)


@mcp.tool()
def retrieve_customer(id: str) -> dict:
    """Retrieve a Customer by ID."""
    return _make_stripe_request("GET", f"/v1/customers/{id}")


@mcp.tool()
def update_customer(id: str, **kwargs) -> dict:
    """Update a Customer's properties."""
    return _make_stripe_request("POST", f"/v1/customers/{id}", data=kwargs)


@mcp.tool()
def delete_customer(id: str) -> dict:
    """Delete a Customer by ID."""
    return _make_stripe_request("DELETE", f"/v1/customers/{id}")


@mcp.tool()
def list_customers(limit: int = 10, email: str = None, created: str = None) -> dict:
    """List Customers with filtering options."""
    params = {"limit": limit}
    if email:
        params["email"] = email
    if created:
        params["created"] = created
    return _make_stripe_request("GET", "/v1/customers", params=params)


# ========== Products ==========

@mcp.tool()
def create_product(
    name: str,
    description: str = None,
    type: str = "service",
    metadata: dict = None,
) -> dict:
    """Create a Product object.
    
    Args:
        name: Product name
        description: Product description
        type: 'service' for recurring or 'good' for physical goods
        metadata: Custom metadata
    
    Returns:
        Product object
    """
    data = {
        "name": name,
        "type": type,
    }
    if description:
        data["description"] = description
    
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return _make_stripe_request("POST", "/v1/products", data=data)


@mcp.tool()
def retrieve_product(id: str) -> dict:
    """Retrieve a Product by ID."""
    return _make_stripe_request("GET", f"/v1/products/{id}")


@mcp.tool()
def update_product(id: str, **kwargs) -> dict:
    """Update a Product's properties."""
    return _make_stripe_request("POST", f"/v1/products/{id}", data=kwargs)


@mcp.tool()
def delete_product(id: str) -> dict:
    """Delete a Product by ID."""
    return _make_stripe_request("DELETE", f"/v1/products/{id}")


@mcp.tool()
def list_products(limit: int = 10, active: bool = None, type: str = None) -> dict:
    """List Products with filtering options."""
    params = {"limit": limit}
    if active is not None:
        params["active"] = str(active).lower()
    if type:
        params["type"] = type
    return _make_stripe_request("GET", "/v1/products", params=params)


# ========== Prices ==========

@mcp.tool()
def create_price(
    product: str,
    unit_amount: int,
    currency: str = "usd",
    recurring: dict = None,
    metadata: dict = None,
    description: str = None,
    tax_behavior: str = "unspecified",
) -> dict:
    """Create a Price for a Product.
    
    Args:
        product: Product ID
        unit_amount: Price in cents
        currency: Three-letter ISO currency code
        recurring: Recurring pricing details for subscriptions
        metadata: Custom metadata
        description: Price description
        tax_behavior: Tax behavior ('inclusive', 'exclusive', or 'unspecified')
    
    Returns:
        Price object
    """
    data = {
        "product": product,
        "unit_amount": unit_amount,
        "currency": currency,
        "tax_behavior": tax_behavior,
    }
    if description:
        data["description"] = description
    
    if recurring:
        for key, value in recurring.items():
            data[f"recurring[{key}]"] = value
    
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return _make_stripe_request("POST", "/v1/prices", data=data)


@mcp.tool()
def retrieve_price(id: str) -> dict:
    """Retrieve a Price by ID."""
    return _make_stripe_request("GET", f"/v1/prices/{id}")


@mcp.tool()
def update_price(id: str, **kwargs) -> dict:
    """Update a Price's properties."""
    return _make_stripe_request("POST", f"/v1/prices/{id}", data=kwargs)


@mcp.tool()
def list_prices(limit: int = 10, product: str = None, active: bool = None) -> dict:
    """List Prices with filtering options."""
    params = {"limit": limit}
    if product:
        params["product"] = product
    if active is not None:
        params["active"] = str(active).lower()
    return _make_stripe_request("GET", "/v1/prices", params=params)


# ========== Subscriptions ==========

@mcp.tool()
def create_subscription(
    customer: str,
    items: list,
    trial_period_days: int = None,
    metadata: dict = None,
    payment_behavior: str = "default_incomplete",
    promotion_codes: list = None,
) -> dict:
    """Create a Subscription for a Customer.
    
    Args:
        customer: Customer ID
        items: List of price IDs, e.g., [{"price": "price_123"}]
        trial_period_days: Number of trial days
        metadata: Custom metadata
        payment_behavior: How to handle payment ('default_incomplete', 'create_incomplete', etc.)
        promotion_codes: List of promotion code IDs
    
    Returns:
        Subscription object
    """
    data = {
        "customer": customer,
        "payment_behavior": payment_behavior,
    }
    
    # Convert items list to Stripe format
    for i, item in enumerate(items):
        for key, value in item.items():
            data[f"items[{i}][{key}]"] = value
    
    if trial_period_days:
        data["trial_period_days"] = trial_period_days
    
    if promotion_codes:
        for i, code in enumerate(promotion_codes):
            data[f"promotion_codes[{i}]"] = code
    
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return _make_stripe_request("POST", "/v1/subscriptions", data=data)


@mcp.tool()
def retrieve_subscription(id: str) -> dict:
    """Retrieve a Subscription by ID."""
    return _make_stripe_request("GET", f"/v1/subscriptions/{id}")


@mcp.tool()
def update_subscription(id: str, **kwargs) -> dict:
    """Update a Subscription's properties."""
    return _make_stripe_request("POST", f"/v1/subscriptions/{id}", data=kwargs)


@mcp.tool()
def cancel_subscription(id: str, invoice_now: bool = None, prorate: bool = None) -> dict:
    """Cancel a Subscription by ID."""
    data = {}
    if invoice_now:
        data["invoice_now"] = str(invoice_now).lower()
    if prorate:
        data["prorate"] = str(prorate).lower()
    return _make_stripe_request("DELETE", f"/v1/subscriptions/{id}", data=data)


@mcp.tool()
def list_subscriptions(limit: int = 10, customer: str = None, status: str = None) -> dict:
    """List Subscriptions with filtering options."""
    params = {"limit": limit}
    if customer:
        params["customer"] = customer
    if status:
        params["status"] = status
    return _make_stripe_request("GET", "/v1/subscriptions", params=params)


# ========== Invoices ==========

@mcp.tool()
def create_invoice(
    customer: str,
    auto_advance: bool = True,
    collection_method: str = "charge_automatically",
    description: str = None,
    metadata: dict = None,
    application_fee_amount: int = None,
) -> dict:
    """Create an Invoice for a Customer.
    
    Args:
        customer: Customer ID
        auto_advance: Whether to auto-advance invoice status
        collection_method: 'charge_automatically' or 'send_invoice'
        description: Invoice description
        metadata: Custom metadata
        application_fee_amount: Fee amount in cents for Connect
        return: Invoice object
    """
    data = {
        "customer": customer,
        "auto_advance": str(auto_advance).lower(),
        "collection_method": collection_method,
    }
    if description:
        data["description"] = description
    if application_fee_amount:
        data["application_fee_amount"] = application_fee_amount
    
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return _make_stripe_request("POST", "/v1/invoices", data=data)


@mcp.tool()
def retrieve_invoice(id: str) -> dict:
    """Retrieve an Invoice by ID."""
    return _make_stripe_request("GET", f"/v1/invoices/{id}")


@mcp.tool()
def update_invoice(id: str, **kwargs) -> dict:
    """Update an Invoice's properties."""
    return _make_stripe_request("POST", f"/v1/invoices/{id}", data=kwargs)


@mcp.tool()
def finalize_invoice(id: str) -> dict:
    """Finalize an Invoice."""
    return _make_stripe_request("POST", f"/v1/invoices/{id}/finalize")


@mcp.tool()
def pay_invoice(id: str, source: str = None) -> dict:
    """Pay an Invoice."""
    data = {}
    if source:
        data["source"] = source
    return _make_stripe_request("POST", f"/v1/invoices/{id}/pay", data=data)


@mcp.tool()
def list_invoices(limit: int = 10, customer: str = None, status: str = None) -> dict:
    """List Invoices with filtering options."""
    params = {"limit": limit}
    if customer:
        params["customer"] = customer
    if status:
        params["status"] = status
    return _make_stripe_request("GET", "/v1/invoices", params=params)


# ========== Checkout Sessions ==========

@mcp.tool()
def create_checkout_session(
    line_items: list,
    mode: str = "payment",
    success_url: str = None,
    cancel_url: str = None,
    customer_email: str = None,
    metadata: dict = None,
) -> dict:
    """Create a Checkout Session for payment flow.
    
    Args:
        line_items: List of line items, e.g., [{"price": "price_123", "quantity": 1}]
        mode: Payment mode ('payment', 'subscription', or 'setup')
        success_url: URL to redirect after successful payment
        cancel_url: URL to redirect if payment is canceled
        customer_email: Customer email for guest checkout
        metadata: Custom metadata
    
    Returns:
        Checkout Session object with payment URL
    """
    data = {
        "mode": mode,
    }
    
    # Convert line_items to Stripe format
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
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return _make_stripe_request("POST", "/v1/checkout/sessions", data=data)


@mcp.tool()
def retrieve_checkout_session(id: str) -> dict:
    """Retrieve a Checkout Session by ID."""
    return _make_stripe_request("GET", f"/v1/checkout/sessions/{id}")


# ========== Payment Links ==========

@mcp.tool()
def create_payment_link(
    line_items: list,
    customer_email: str = None,
    metadata: dict = None,
) -> dict:
    """Create a Payment Link for standalone payment pages.
    
    Args:
        line_items: List of line items with price and quantity
        customer_email: Customer email
        metadata: Custom metadata
    
    Returns:
        Payment Link object with URL
    """
    data = {}
    
    for i, item in enumerate(line_items):
        for key, value in item.items():
            data[f"line_items[{i}][{key}]"] = value
    
    if customer_email:
        data["customer_email"] = customer_email
    
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return _make_stripe_request("POST", "/v1/payment_links", data=data)


@mcp.tool()
def retrieve_payment_link(id: str) -> dict:
    """Retrieve a Payment Link by ID."""
    return _make_stripe_request("GET", f"/v1/payment_links/{id}")


# ========== Setup Intents ==========

@mcp.tool()
def create_setup_intent(
    customer: str = None,
    payment_method_types: list = None,
    usage: str = "off_session",
    return_url: str = None,
) -> dict:
    """Create a SetupIntent to set up future payments.
    
    Args:
        customer: Customer ID
        payment_method_types: List of payment method types
        usage: 'off_session' or 'on_session'
        return_url: URL to redirect after setup
    
    Returns:
        SetupIntent object
    """
    data = {"usage": usage}
    if customer:
        data["customer"] = customer
    
    if payment_method_types:
        for i, pmt in enumerate(payment_method_types):
            data[f"payment_method_types[{i}]"] = pmt
    
    if return_url:
        data["return_url"] = return_url
    
    return _make_stripe_request("POST", "/v1/setup_intents", data=data)


@mcp.tool()
def retrieve_setup_intent(id: str) -> dict:
    """Retrieve a SetupIntent by ID."""
    return _make_stripe_request("GET", f"/v1/setup_intents/{id}")


@mcp.tool()
def confirm_setup_intent(id: str, payment_method: str = None) -> dict:
    """Confirm a SetupIntent."""
    data = {}
    if payment_method:
        data["payment_method"] = payment_method
    return _make_stripe_request("POST", f"/v1/setup_intents/{id}/confirm", data=data)


# ========== Coupons ==========

@mcp.tool()
def create_coupon(
    percent_off: int = None,
    amount_off: int = None,
    currency: str = "usd",
    duration: str = "once",
    name: str = None,
    max_redemptions: int = None,
    metadata: dict = None,
) -> dict:
    """Create a Coupon for discounts.
    
    Args:
        percent_off: Percentage off (1-100)
        amount_off: Amount off in cents
        currency: Three-letter ISO currency code
        duration: 'once', 'repeating', or 'forever'
        name: Coupon code name
        max_redemptions: Maximum number of redemptions
        metadata: Custom metadata
    
    Returns:
        Coupon object
    """
    data = {"duration": duration, "currency": currency}
    if percent_off:
        data["percent_off"] = percent_off
    if amount_off:
        data["amount_off"] = amount_off
    if name:
        data["name"] = name
    if max_redemptions:
        data["max_redemptions"] = max_redemptions
    
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return _make_stripe_request("POST", "/v1/coupons", data=data)


@mcp.tool()
def retrieve_coupon(id: str) -> dict:
    """Retrieve a Coupon by ID."""
    return _make_stripe_request("GET", f"/v1/coupons/{id}")


@mcp.tool()
def delete_coupon(id: str) -> dict:
    """Delete a Coupon by ID."""
    return _make_stripe_request("DELETE", f"/v1/coupons/{id}")


@mcp.tool()
def list_coupons(limit: int = 10, active: bool = None) -> dict:
    """List Coupons with filtering options."""
    params = {"limit": limit}
    if active is not None:
        params["active"] = str(active).lower()
    return _make_stripe_request("GET", "/v1/coupons", params=params)


# ========== Promotion Codes ==========

@mcp.tool()
def create_promotion_code(
    coupon: str,
    code: str = None,
    max_redemptions: int = None,
    metadata: dict = None,
) -> dict:
    """Create a PromotionCode.
    
    Args:
        coupon: Coupon ID
        code: Custom promotion code
        max_redemptions: Maximum redemptions
        metadata: Custom metadata
    
    Returns:
        PromotionCode object
    """
    data = {"coupon": coupon}
    if code:
        data["code"] = code
    if max_redemptions:
        data["max_redemptions"] = max_redemptions
    
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return _make_stripe_request("POST", "/v1/promotion_codes", data=data)


@mcp.tool()
def retrieve_promotion_code(id: str) -> dict:
    """Retrieve a PromotionCode by ID."""
    return _make_stripe_request("GET", f"/v1/promotion_codes/{id}")


@mcp.tool()
def update_promotion_code(id: str, active: bool = None) -> dict:
    """Update a PromotionCode."""
    data = {}
    if active is not None:
        data["active"] = str(active).lower()
    return _make_stripe_request("POST", f"/v1/promotion_codes/{id}", data=data)


@mcp.tool()
def list_promotion_codes(limit: int = 10, coupon: str = None, code: str = None) -> dict:
    """List PromotionCodes with filtering options."""
    params = {"limit": limit}
    if coupon:
        params["coupon"] = coupon
    if code:
        params["code"] = code
    return _make_stripe_request("GET", "/v1/promotion_codes", params=params)


# ========== Accounts (Connect) ==========

@mcp.tool()
def create_connect_account(
    type: str = "express",
    email: str = None,
    country: str = "US",
    capabilities: dict = None,
    metadata: dict = None,
) -> dict:
    """Create a Connect Express or Standard account.
    
    Args:
        type: 'express', 'custom', or 'standard'
        email: Account email
        country: Two-letter country code
        capabilities: Platform-side capabilities
        metadata: Custom metadata
    
    Returns:
        Account object
    """
    data = {"type": type, "country": country}
    if email:
        data["email"] = email
    
    if capabilities:
        for key, value in capabilities.items():
            data[f"capabilities[{key}]"] = value
    
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return _make_stripe_request("POST", "/v1/accounts", data=data)


@mcp.tool()
def retrieve_account(id: str) -> dict:
    """Retrieve a Connect account by ID."""
    return _make_stripe_request("GET", f"/v1/accounts/{id}")


@mcp.tool()
def update_account(id: str, **kwargs) -> dict:
    """Update a Connect account's properties."""
    return _make_stripe_request("POST", f"/v1/accounts/{id}", data=kwargs)


# ========== Transfers (Connect) ==========

@mcp.tool()
def create_transfer(
    amount: int,
    currency: str = "usd",
    destination: str,
    description: str = None,
    metadata: dict = None,
    transfer_group: str = None,
) -> dict:
    """Create a transfer to a Connect account.
    
    Args:
        amount: Amount to transfer in cents
        currency: Three-letter ISO currency code
        destination: Destination account ID
        description: Transfer description
        metadata: Custom metadata
        transfer_group: Group identifier for the transfer
    
    Returns:
        Transfer object
    """
    data = {
        "amount": amount,
        "currency": currency,
        "destination": destination,
    }
    if description:
        data["description"] = description
    if transfer_group:
        data["transfer_group"] = transfer_group
    
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return _make_stripe_request("POST", "/v1/transfers", data=data)


@mcp.tool()
def retrieve_transfer(id: str) -> dict:
    """Retrieve a Transfer by ID."""
    return _make_stripe_request("GET", f"/v1/transfers/{id}")


@mcp.tool()
def list_transfers(limit: int = 10, destination: str = None, status: str = None) -> dict:
    """List Transfers with filtering options."""
    params = {"limit": limit}
    if destination:
        params["destination"] = destination
    if status:
        params["status"] = status
    return _make_stripe_request("GET", "/v1/transfers", params=params)


# ========== Payouts ==========

@mcp.tool()
def retrieve_payout(id: str) -> dict:
    """Retrieve a Payout by ID."""
    return _make_stripe_request("GET", f"/v1/payouts/{id}")


@mcp.tool()
def list_payouts(limit: int = 10, status: str = None, destination: str = None) -> dict:
    """List Payouts with filtering options."""
    params = {"limit": limit}
    if status:
        params["status"] = status
    if destination:
        params["destination"] = destination
    return _make_stripe_request("GET", "/v1/payouts", params=params)


# ========== Cards (Bank Accounts) ==========

@mcp.tool()
def retrieve_card(customer_id: str, card_id: str) -> dict:
    """Retrieve a card for a customer."""
    return _make_stripe_request("GET", f"/v1/customers/{customer_id}/sources/{card_id}")


@mcp.tool()
def delete_card(customer_id: str, card_id: str) -> dict:
    """Delete a card from a customer."""
    return _make_stripe_request("DELETE", f"/v1/customers/{customer_id}/sources/{card_id}")


@mcp.tool()
def list_cards(customer_id: str, limit: int = 10) -> dict:
    """List cards for a customer."""
    params = {"limit": limit}
    return _make_stripe_request("GET", f"/v1/customers/{customer_id}/sources", params=params)


# ========== Bank Accounts ==========

@mcp.tool()
def retrieve_bank_account(customer_id: str, bank_account_id: str) -> dict:
    """Retrieve a bank account for a customer."""
    return _make_stripe_request(
        "GET", f"/v1/customers/{customer_id}/sources/{bank_account_id}"
    )


@mcp.tool()
def delete_bank_account(customer_id: str, bank_account_id: str) -> dict:
    """Delete a bank account from a customer."""
    return _make_stripe_request(
        "DELETE", f"/v1/customers/{customer_id}/sources/{bank_account_id}"
    )


@mcp.tool()
def list_bank_accounts(customer_id: str, limit: int = 10) -> dict:
    """List bank accounts for a customer."""
    params = {"limit": limit}
    return _make_stripe_request(
        "GET", f"/v1/customers/{customer_id}/sources", params=params
    )


if __name__ == "__main__":
    mcp.run()
