#!/usr/bin/env python3
"""Stripe MCP Server - FastMCP implementation for Stripe API"""

import os
import json
from typing import Any, Dict, Optional
import requests
from fastmcp import FastMCP


# Initialize FastMCP server
mcp = FastMCP(
    name="stripe",
    version="1.0.0",
    instructions="Stripe MCP Server for managing payments, customers, subscriptions, and more. Use the tools provided to interact with the Stripe API.",
)


def get_stripe_key() -> str:
    """Get Stripe API key from environment variable."""
    key = os.environ.get("STRIPE_API_KEY")
    if not key:
        raise ValueError("STRIPE_API_KEY environment variable is not set")
    return key


def make_stripe_request(
    method: str, 
    endpoint: str, 
    params: Optional[Dict[str, Any]] = None,
    data: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """Make a request to the Stripe API."""
    api_key = get_stripe_key()
    base_url = "https://api.stripe.com"
    url = f"{base_url}{endpoint}"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Stripe-Version": "2024-12-19.acacia"
    }
    
    try:
        if method.upper() == "GET":
            response = requests.get(url, headers=headers, params=params)
        elif method.upper() == "POST":
            # Stripe uses form-encoded data for POST requests
            response = requests.post(url, headers=headers, data=data)
        else:
            raise ValueError(f"Unsupported HTTP method: {method}")
        
        # Try to parse JSON response
        try:
            result = response.json()
        except json.JSONDecodeError:
            result = {"raw_response": response.text}
        
        # Handle errors
        if not response.ok:
            error_details = result.get("error", {})
            return {
                "error": {
                    "message": error_details.get("message", f"HTTP {response.status_code}"),
                    "type": error_details.get("type", "unknown"),
                    "code": error_details.get("code", "unknown"),
                    "http_status": response.status_code
                }
            }
        
        return result
        
    except requests.exceptions.RequestException as e:
        return {"error": {"message": str(e), "type": "request_error"}}


# ==============================================================================
# CHARGES
# ==============================================================================

@mcp.tool()
def create_charge(
    amount: int,
    currency: str,
    customer: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    receipt_email: Optional[str] = None,
    source: Optional[str] = None,
    statement_descriptor: Optional[str] = None,
    statement_descriptor_suffix: Optional[str] = None,
    capture: Optional[bool] = None,
    shipping: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """Create a new charge.
    
    Note: The Charges API is deprecated. Use Payment Intents API for new integrations.
    
    Args:
        amount: Amount intended to be collected (in smallest currency unit)
        currency: Three-letter ISO currency code (e.g., 'usd')
        customer: ID of an existing customer
        description: Arbitrary string attached to the charge
        metadata: Key-value pairs for storing additional structured info
        receipt_email: Email address to send receipt to
        source: Payment source (card ID, bank account, token, etc.)
        statement_descriptor: Text that appears on customer's statement
        statement_descriptor_suffix: Suffix for card charge statement descriptor
        capture: Whether to immediately capture the payment
        shipping: Shipping information for fraud prevention
    """
    data = {
        "amount": amount,
        "currency": currency
    }
    
    if customer:
        data["customer"] = customer
    if description:
        data["description"] = description
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    if receipt_email:
        data["receipt_email"] = receipt_email
    if source:
        data["source"] = source
    if statement_descriptor:
        data["statement_descriptor"] = statement_descriptor
    if statement_descriptor_suffix:
        data["statement_descriptor_suffix"] = statement_descriptor_suffix
    if capture is not None:
        data["capture"] = "true" if capture else "false"
    if shipping:
        # Handle shipping object - convert to form-encoded format
        if "address" in shipping:
            addr = shipping["address"]
            if "line1" in addr:
                data["shipping[address][line1]"] = addr["line1"]
            if "line2" in addr:
                data["shipping[address][line2]"] = addr["line2"]
            if "city" in addr:
                data["shipping[address][city]"] = addr["city"]
            if "state" in addr:
                data["shipping[address][state]"] = addr["state"]
            if "postal_code" in addr:
                data["shipping[address][postal_code]"] = addr["postal_code"]
            if "country" in addr:
                data["shipping[address][country]"] = addr["country"]
        if "name" in shipping:
            data["shipping[name]"] = shipping["name"]
        if "phone" in shipping:
            data["shipping[phone]"] = shipping["phone"]
    
    return make_stripe_request("POST", "/v1/charges", data=data)


@mcp.tool()
def retrieve_charge(charge_id: str) -> Dict[str, Any]:
    """Retrieve a charge by ID."""
    return make_stripe_request("GET", f"/v1/charges/{charge_id}")


@mcp.tool()
def update_charge(
    charge_id: str,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    receipt_email: Optional[str] = None,
    shipping: Optional[Dict[str, Any]] = None,
    fraud_details: Optional[Dict[str, str]] = None,
    transfer_group: Optional[str] = None
) -> Dict[str, Any]:
    """Update a charge by setting new values for specified parameters."""
    data = {}
    
    if description:
        data["description"] = description
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    if receipt_email:
        data["receipt_email"] = receipt_email
    if shipping:
        if "address" in shipping:
            addr = shipping["address"]
            if "line1" in addr:
                data["shipping[address][line1]"] = addr["line1"]
            if "line2" in addr:
                data["shipping[address][line2]"] = addr["line2"]
            if "city" in addr:
                data["shipping[address][city]"] = addr["city"]
            if "state" in addr:
                data["shipping[address][state]"] = addr["state"]
            if "postal_code" in addr:
                data["shipping[address][postal_code]"] = addr["postal_code"]
            if "country" in addr:
                data["shipping[address][country]"] = addr["country"]
        if "name" in shipping:
            data["shipping[name]"] = shipping["name"]
        if "phone" in shipping:
            data["shipping[phone]"] = shipping["phone"]
    if fraud_details:
        for key, value in fraud_details.items():
            data[f"fraud_details[{key}]"] = value
    if transfer_group:
        data["transfer_group"] = transfer_group
    
    return make_stripe_request("POST", f"/v1/charges/{charge_id}", data=data)


@mcp.tool()
def list_charges(
    created: Optional[int] = None,
    customer: Optional[str] = None,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None
) -> Dict[str, Any]:
    """List all charges.
    
    Args:
        created: Filter charges created within a specific timestamp range
        customer: Filter charges for a specific customer
        limit: Number of charges to return (default: 10, max: 100)
        starting_after: ID after which to start listing
        ending_before: ID before which to end listing
    """
    params = {}
    
    if created:
        params["created"] = created
    if customer:
        params["customer"] = customer
    if limit:
        params["limit"] = limit
    if starting_after:
        params["starting_after"] = starting_after
    if ending_before:
        params["ending_before"] = ending_before
    
    return make_stripe_request("GET", "/v1/charges", params=params)


# ==============================================================================
# CUSTOMERS
# ==============================================================================

@mcp.tool()
def create_customer(
    address: Optional[Dict[str, Any]] = None,
    description: Optional[str] = None,
    email: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    name: Optional[str] = None,
    payment_method: Optional[str] = None,
    phone: Optional[str] = None,
    shipping: Optional[Dict[str, Any]] = None,
    tax: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """Create a new customer.
    
    Args:
        address: Customer's address
        description: Arbitrary string attached to customer
        email: Customer's email address
        metadata: Key-value pairs for storing additional structured info
        name: Customer's full name or business name
        payment_method: ID of PaymentMethod to attach to customer
        phone: Customer's phone number
        shipping: Customer's shipping information
        tax: Tax details about the customer
    """
    data = {}
    
    if address:
        if "city" in address:
            data["address[city]"] = address["city"]
        if "country" in address:
            data["address[country]"] = address["country"]
        if "line1" in address:
            data["address[line1]"] = address["line1"]
        if "line2" in address:
            data["address[line2]"] = address["line2"]
        if "postal_code" in address:
            data["address[postal_code]"] = address["postal_code"]
        if "state" in address:
            data["address[state]"] = address["state"]
    if description:
        data["description"] = description
    if email:
        data["email"] = email
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    if name:
        data["name"] = name
    if payment_method:
        data["payment_method"] = payment_method
    if phone:
        data["phone"] = phone
    if shipping:
        if "address" in shipping:
            addr = shipping["address"]
            if "city" in addr:
                data["shipping[address][city]"] = addr["city"]
            if "country" in addr:
                data["shipping[address][country]"] = addr["country"]
            if "line1" in addr:
                data["shipping[address][line1]"] = addr["line1"]
            if "line2" in addr:
                data["shipping[address][line2]"] = addr["line2"]
            if "postal_code" in addr:
                data["shipping[address][postal_code]"] = addr["postal_code"]
            if "state" in addr:
                data["shipping[address][state]"] = addr["state"]
        if "name" in shipping:
            data["shipping[name]"] = shipping["name"]
        if "phone" in shipping:
            data["shipping[phone]"] = shipping["phone"]
    if tax:
        if "address" in tax:
            addr = tax["address"]
            if "city" in addr:
                data["tax[address][city]"] = addr["city"]
            if "country" in addr:
                data["tax[address][country]"] = addr["country"]
            if "line1" in addr:
                data["tax[address][line1]"] = addr["line1"]
            if "line2" in addr:
                data["tax[address][line2]"] = addr["line2"]
            if "postal_code" in addr:
                data["tax[address][postal_code]"] = addr["postal_code"]
            if "state" in addr:
                data["tax[address][state]"] = addr["state"]
        if "customer_type" in tax:
            data["tax[customer_type]"] = tax["customer_type"]
        if "tax_id" in tax:
            data["tax[tax_id]"] = tax["tax_id"]
        if "tax_id_type" in tax:
            data["tax[tax_id_type]"] = tax["tax_id_type"]
    
    return make_stripe_request("POST", "/v1/customers", data=data)


@mcp.tool()
def retrieve_customer(customer_id: str) -> Dict[str, Any]:
    """Retrieve a customer by ID."""
    return make_stripe_request("GET", f"/v1/customers/{customer_id}")


@mcp.tool()
def update_customer(
    customer_id: str,
    address: Optional[Dict[str, Any]] = None,
    description: Optional[str] = None,
    email: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    name: Optional[str] = None,
    phone: Optional[str] = None,
    shipping: Optional[Dict[str, Any]] = None,
    tax: Optional[Dict[str, Any]] = None,
    default_source: Optional[str] = None,
    invoice_prefix: Optional[str] = None,
    invoice_settings: Optional[Dict[str, Any]] = None,
    tax_exempt: Optional[str] = None
) -> Dict[str, Any]:
    """Update a customer by setting new values for specified parameters."""
    data = {}
    
    if address:
        if "city" in address:
            data["address[city]"] = address["city"]
        if "country" in address:
            data["address[country]"] = address["country"]
        if "line1" in address:
            data["address[line1]"] = address["line1"]
        if "line2" in address:
            data["address[line2]"] = address["line2"]
        if "postal_code" in address:
            data["address[postal_code]"] = address["postal_code"]
        if "state" in address:
            data["address[state]"] = address["state"]
    if description:
        data["description"] = description
    if email:
        data["email"] = email
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    if name:
        data["name"] = name
    if phone:
        data["phone"] = phone
    if shipping:
        if "address" in shipping:
            addr = shipping["address"]
            if "city" in addr:
                data["shipping[address][city]"] = addr["city"]
            if "country" in addr:
                data["shipping[address][country]"] = addr["country"]
            if "line1" in addr:
                data["shipping[address][line1]"] = addr["line1"]
            if "line2" in addr:
                data["shipping[address][line2]"] = addr["line2"]
            if "postal_code" in addr:
                data["shipping[address][postal_code]"] = addr["postal_code"]
            if "state" in addr:
                data["shipping[address][state]"] = addr["state"]
        if "name" in shipping:
            data["shipping[name]"] = shipping["name"]
        if "phone" in shipping:
            data["shipping[phone]"] = shipping["phone"]
    if tax:
        if "address" in tax:
            addr = tax["address"]
            if "city" in addr:
                data["tax[address][city]"] = addr["city"]
            if "country" in addr:
                data["tax[address][country]"] = addr["country"]
            if "line1" in addr:
                data["tax[address][line1]"] = addr["line1"]
            if "line2" in addr:
                data["tax[address][line2]"] = addr["line2"]
            if "postal_code" in addr:
                data["tax[address][postal_code]"] = addr["postal_code"]
            if "state" in addr:
                data["tax[address][state]"] = addr["state"]
        if "customer_type" in tax:
            data["tax[customer_type]"] = tax["customer_type"]
        if "tax_id" in tax:
            data["tax[tax_id]"] = tax["tax_id"]
        if "tax_id_type" in tax:
            data["tax[tax_id_type]"] = tax["tax_id_type"]
    if default_source:
        data["default_source"] = default_source
    if invoice_prefix:
        data["invoice_prefix"] = invoice_prefix
    if invoice_settings:
        if "custom_fields" in invoice_settings:
            for i, field in enumerate(invoice_settings["custom_fields"]):
                data[f"invoice_settings[custom_fields][{i}][name]"] = field.get("name", "")
                data[f"invoice_settings[custom_fields][{i}][value]"] = field.get("value", "")
        if "footer" in invoice_settings:
            data["invoice_settings[footer]"] = invoice_settings["footer"]
        if "rendering_options" in invoice_settings:
            if "amount_decimal_places" in invoice_settings["rendering_options"]:
                data["invoice_settings[rendering_options][amount_decimal_places]"] = invoice_settings["rendering_options"]["amount_decimal_places"]
            if "amount_currency_code" in invoice_settings["rendering_options"]:
                data["invoice_settings[rendering_options][amount_currency_code]"] = invoice_settings["rendering_options"]["amount_currency_code"]
    if tax_exempt:
        data["tax_exempt"] = tax_exempt
    
    return make_stripe_request("POST", f"/v1/customers/{customer_id}", data=data)


@mcp.tool()
def list_customers(
    created: Optional[int] = None,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    email: Optional[str] = None
) -> Dict[str, Any]:
    """List all customers.
    
    Args:
        created: Filter customers created within a specific timestamp range
        limit: Number of customers to return (default: 10, max: 100)
        starting_after: ID after which to start listing
        ending_before: ID before which to end listing
        email: Filter customers by email address
    """
    params = {}
    
    if created:
        params["created"] = created
    if limit:
        params["limit"] = limit
    if starting_after:
        params["starting_after"] = starting_after
    if ending_before:
        params["ending_before"] = ending_before
    if email:
        params["email"] = email
    
    return make_stripe_request("GET", "/v1/customers", params=params)


# ==============================================================================
# PAYMENT INTENTS
# ==============================================================================

@mcp.tool()
def create_payment_intent(
    amount: int,
    currency: str,
    automatic_payment_methods: Optional[Dict[str, Any]] = None,
    confirm: Optional[bool] = None,
    customer: Optional[str] = None,
    customer_account: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    off_session: Optional[bool] = None,
    payment_method: Optional[str] = None,
    receipt_email: Optional[str] = None,
    setup_future_usage: Optional[str] = None,
    shipping: Optional[Dict[str, Any]] = None,
    statement_descriptor: Optional[str] = None,
    statement_descriptor_suffix: Optional[str] = None,
    payment_method_types: Optional[list] = None,
    capture_method: Optional[str] = None,
    confirmation_method: Optional[str] = None,
    payment_method_options: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """Create a new PaymentIntent.
    
    Args:
        amount: Amount intended to be collected (in smallest currency unit)
        currency: Three-letter ISO currency code (e.g., 'usd')
        automatic_payment_methods: Configure compatible payment methods
        confirm: Whether to immediately confirm the PaymentIntent
        customer: ID of the Customer this PaymentIntent belongs to
        customer_account: ID of the Account representing the customer
        description: Arbitrary string attached to the object
        metadata: Key-value pairs for storing additional structured info
        off_session: Whether customer is present during payment
        payment_method: ID of the payment method to attach
        receipt_email: Email to send receipt to
        setup_future_usage: Indicates intent for future payments
        shipping: Shipping information for this PaymentIntent
        statement_descriptor: Text that appears on customer's statement
        statement_descriptor_suffix: Suffix for card charge statement descriptor
        payment_method_types: List of payment method types to support
        capture_method: Whether to immediately capture the payment
        confirmation_method: Whether to immediately confirm or require manual confirmation
        payment_method_options: Payment method-specific options
    """
    data = {
        "amount": amount,
        "currency": currency
    }
    
    if automatic_payment_methods:
        if "enabled" in automatic_payment_methods:
            data["automatic_payment_methods[enabled]"] = (
                "true" if automatic_payment_methods["enabled"] else "false"
            )
    if confirm is not None:
        data["confirm"] = "true" if confirm else "false"
    if customer:
        data["customer"] = customer
    if customer_account:
        data["customer_account"] = customer_account
    if description:
        data["description"] = description
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    if off_session is not None:
        data["off_session"] = "true" if off_session else "false"
    if payment_method:
        data["payment_method"] = payment_method
    if receipt_email:
        data["receipt_email"] = receipt_email
    if setup_future_usage:
        data["setup_future_usage"] = setup_future_usage
    if shipping:
        if "address" in shipping:
            addr = shipping["address"]
            if "city" in addr:
                data["shipping[address][city]"] = addr["city"]
            if "country" in addr:
                data["shipping[address][country]"] = addr["country"]
            if "line1" in addr:
                data["shipping[address][line1]"] = addr["line1"]
            if "line2" in addr:
                data["shipping[address][line2]"] = addr["line2"]
            if "postal_code" in addr:
                data["shipping[address][postal_code]"] = addr["postal_code"]
            if "state" in addr:
                data["shipping[address][state]"] = addr["state"]
        if "name" in shipping:
            data["shipping[name]"] = shipping["name"]
        if "phone" in shipping:
            data["shipping[phone]"] = shipping["phone"]
    if statement_descriptor:
        data["statement_descriptor"] = statement_descriptor
    if statement_descriptor_suffix:
        data["statement_descriptor_suffix"] = statement_descriptor_suffix
    if payment_method_types:
        for i, pmt in enumerate(payment_method_types):
            data[f"payment_method_types[{i}]"] = pmt
    if capture_method:
        data["capture_method"] = capture_method
    if confirmation_method:
        data["confirmation_method"] = confirmation_method
    if payment_method_options:
        for key, value in payment_method_options.items():
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    data[f"payment_method_options[{key}][{sub_key}]"] = sub_value
            else:
                data[f"payment_method_options[{key}]"] = value
    
    return make_stripe_request("POST", "/v1/payment_intents", data=data)


@mcp.tool()
def retrieve_payment_intent(payment_intent_id: str) -> Dict[str, Any]:
    """Retrieve a PaymentIntent by ID."""
    return make_stripe_request("GET", f"/v1/payment_intents/{payment_intent_id}")


@mcp.tool()
def confirm_payment_intent(
    payment_intent_id: str,
    payment_method: Optional[str] = None,
    off_session: Optional[bool] = None
) -> Dict[str, Any]:
    """Confirm a PaymentIntent.
    
    Args:
        payment_intent_id: ID of the PaymentIntent to confirm
        payment_method: ID of the payment method to use
        off_session: Whether customer is present during payment
    """
    data = {}
    
    if payment_method:
        data["payment_method"] = payment_method
    if off_session is not None:
        data["off_session"] = "true" if off_session else "false"
    
    return make_stripe_request("POST", f"/v1/payment_intents/{payment_intent_id}/confirm", data=data)


@mcp.tool()
def update_payment_intent(
    payment_intent_id: str,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    receipt_email: Optional[str] = None,
    shipping: Optional[Dict[str, Any]] = None,
    statement_descriptor: Optional[str] = None,
    statement_descriptor_suffix: Optional[str] = None,
    payment_method_options: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """Update a PaymentIntent by setting new values for specified parameters."""
    data = {}
    
    if description:
        data["description"] = description
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    if receipt_email:
        data["receipt_email"] = receipt_email
    if shipping:
        if "address" in shipping:
            addr = shipping["address"]
            if "city" in addr:
                data["shipping[address][city]"] = addr["city"]
            if "country" in addr:
                data["shipping[address][country]"] = addr["country"]
            if "line1" in addr:
                data["shipping[address][line1]"] = addr["line1"]
            if "line2" in addr:
                data["shipping[address][line2]"] = addr["line2"]
            if "postal_code" in addr:
                data["shipping[address][postal_code]"] = addr["postal_code"]
            if "state" in addr:
                data["shipping[address][state]"] = addr["state"]
        if "name" in shipping:
            data["shipping[name]"] = shipping["name"]
        if "phone" in shipping:
            data["shipping[phone]"] = shipping["phone"]
    if statement_descriptor:
        data["statement_descriptor"] = statement_descriptor
    if statement_descriptor_suffix:
        data["statement_descriptor_suffix"] = statement_descriptor_suffix
    if payment_method_options:
        for key, value in payment_method_options.items():
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    data[f"payment_method_options[{key}][{sub_key}]"] = sub_value
            else:
                data[f"payment_method_options[{key}]"] = value
    
    return make_stripe_request("POST", f"/v1/payment_intents/{payment_intent_id}", data=data)


@mcp.tool()
def cancel_payment_intent(
    payment_intent_id: str,
    cancellation_reason: Optional[str] = None
) -> Dict[str, Any]:
    """Cancel a PaymentIntent.
    
    Args:
        payment_intent_id: ID of the PaymentIntent to cancel
        cancellation_reason: Reason for cancellation (duplicate, fraudulent, requested_by_customer)
    """
    data = {}
    
    if cancellation_reason:
        data["cancellation_reason"] = cancellation_reason
    
    return make_stripe_request("POST", f"/v1/payment_intents/{payment_intent_id}/cancel", data=data)


# ==============================================================================
# SUBSCRIPTIONS
# ==============================================================================

@mcp.tool()
def create_subscription(
    customer: str,
    items: list,
    automatic_tax: Optional[Dict[str, Any]] = None,
    currency: Optional[str] = None,
    customer_account: Optional[str] = None,
    default_payment_method: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    payment_behavior: Optional[str] = None,
    billing_cycle_anchor: Optional[str] = None,
    billing_thresholds: Optional[Dict[str, Any]] = None,
    cancel_at: Optional[int] = None,
    cancel_at_period_end: Optional[bool] = None,
    collection_method: Optional[str] = None,
    days_until_due: Optional[int] = None,
    default_source: Optional[str] = None,
    default_tax_rates: Optional[list] = None,
    discounts: Optional[list] = None,
    invoice_settings: Optional[Dict[str, Any]] = None,
    off_session: Optional[bool] = None,
    payment_settings: Optional[Dict[str, Any]] = None,
    proration_behavior: Optional[str] = None,
    trial_end: Optional[int] = None,
    trial_from_plan: Optional[bool] = None,
    trial_period_days: Optional[int] = None,
    trial_settings: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """Create a new subscription.
    
    Args:
        customer: ID of the customer to subscribe
        items: List of subscription items with prices
        automatic_tax: Automatic tax settings
        currency: Three-letter ISO currency code
        customer_account: ID of the account representing the customer
        default_payment_method: ID of the default payment method
        description: Description for the subscription
        metadata: Key-value pairs for storing additional structured info
        payment_behavior: Behavior when initial payment fails
        billing_cycle_anchor: When to set the subscription's billing cycle
        billing_thresholds: Billing thresholds for the subscription
        cancel_at: Timestamp at which to cancel the subscription
        cancel_at_period_end: Whether to cancel at end of current period
        collection_method: Collection method for the subscription
        days_until_due: Number of days until the invoice is due
        default_source: Default payment source for the subscription
        default_tax_rates: Tax rates to apply to the subscription
        discounts: Discounts to apply to the subscription
        invoice_settings: Invoice settings for the subscription
        off_session: Whether customer is present during payment
        payment_settings: Payment settings for the subscription
        proration_behavior: How to handle prorated charges
        trial_end: Unix timestamp for trial end
        trial_from_plan: Whether to use the plan's trial settings
        trial_period_days: Number of trial days
        trial_settings: Trial settings for the subscription
    """
    data = {
        "customer": customer
    }
    
    # Format items as form-encoded
    for i, item in enumerate(items):
        if "price" in item:
            data[f"items[{i}][price]"] = item["price"]
        if "quantity" in item:
            data[f"items[{i}][quantity]"] = item["quantity"]
        if "metadata" in item:
            for key, value in item["metadata"].items():
                data[f"items[{i}][metadata][{key}]"] = value
        if "tax_rates" in item:
            for j, tax_rate in enumerate(item["tax_rates"]):
                data[f"items[{i}][tax_rates][{j}]"] = tax_rate
    
    if automatic_tax:
        if "enabled" in automatic_tax:
            data["automatic_tax[enabled]"] = "true" if automatic_tax["enabled"] else "false"
        if "liability" in automatic_tax:
            liability = automatic_tax["liability"]
            if "account" in liability:
                data["automatic_tax[liability][account]"] = liability["account"]
    if currency:
        data["currency"] = currency
    if customer_account:
        data["customer_account"] = customer_account
    if default_payment_method:
        data["default_payment_method"] = default_payment_method
    if description:
        data["description"] = description
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    if payment_behavior:
        data["payment_behavior"] = payment_behavior
    if billing_cycle_anchor:
        data["billing_cycle_anchor"] = billing_cycle_anchor
    if billing_thresholds:
        if "amount_gte" in billing_thresholds:
            data["billing_thresholds[amount_gte]"] = billing_thresholds["amount_gte"]
        if "reset_billing_cycle_anchor" in billing_thresholds:
            data["billing_thresholds[reset_billing_cycle_anchor]"] = "true" if billing_thresholds["reset_billing_cycle_anchor"] else "false"
    if cancel_at:
        data["cancel_at"] = cancel_at
    if cancel_at_period_end is not None:
        data["cancel_at_period_end"] = "true" if cancel_at_period_end else "false"
    if collection_method:
        data["collection_method"] = collection_method
    if days_until_due:
        data["days_until_due"] = days_until_due
    if default_source:
        data["default_source"] = default_source
    if default_tax_rates:
        for i, tax_rate in enumerate(default_tax_rates):
            data[f"default_tax_rates[{i}]"] = tax_rate
    if discounts:
        for i, discount in enumerate(discounts):
            if "coupon" in discount:
                data[f"discounts[{i}][coupon]"] = discount["coupon"]
            if "promotion_code" in discount:
                data[f"discounts[{i}][promotion_code]"] = discount["promotion_code"]
    if invoice_settings:
        if "issuer" in invoice_settings:
            issuer = invoice_settings["issuer"]
            if "type" in issuer:
                data["invoice_settings[issuer][type]"] = issuer["type"]
        if "custom_fields" in invoice_settings:
            for i, field in enumerate(invoice_settings["custom_fields"]):
                data[f"invoice_settings[custom_fields][{i}][name]"] = field.get("name", "")
                data[f"invoice_settings[custom_fields][{i}][value]"] = field.get("value", "")
        if "footer" in invoice_settings:
            data["invoice_settings[footer]"] = invoice_settings["footer"]
        if "rendering_options" in invoice_settings:
            if "amount_decimal_places" in invoice_settings["rendering_options"]:
                data["invoice_settings[rendering_options][amount_decimal_places]"] = invoice_settings["rendering_options"]["amount_decimal_places"]
            if "amount_currency_code" in invoice_settings["rendering_options"]:
                data["invoice_settings[rendering_options][amount_currency_code]"] = invoice_settings["rendering_options"]["amount_currency_code"]
    if off_session is not None:
        data["off_session"] = "true" if off_session else "false"
    if payment_settings:
        if "payment_method_options" in payment_settings:
            for key, value in payment_settings["payment_method_options"].items():
                if isinstance(value, dict):
                    for sub_key, sub_value in value.items():
                        data[f"payment_settings[payment_method_options][{key}][{sub_key}]"] = sub_value
                else:
                    data[f"payment_settings[payment_method_options][{key}]"] = value
        if "payment_method_types" in payment_settings:
            for i, pmt in enumerate(payment_settings["payment_method_types"]):
                data[f"payment_settings[payment_method_types][{i}]"] = pmt
        if "save_default_payment_method" in payment_settings:
            data["payment_settings[save_default_payment_method]"] = payment_settings["save_default_payment_method"]
    if proration_behavior:
        data["proration_behavior"] = proration_behavior
    if trial_end:
        data["trial_end"] = trial_end
    if trial_from_plan is not None:
        data["trial_from_plan"] = "true" if trial_from_plan else "false"
    if trial_period_days:
        data["trial_period_days"] = trial_period_days
    if trial_settings:
        if "end_behavior" in trial_settings:
            end_behavior = trial_settings["end_behavior"]
            if "missing_payment_method" in end_behavior:
                data["trial_settings[end_behavior][missing_payment_method]"] = end_behavior["missing_payment_method"]
    
    return make_stripe_request("POST", "/v1/subscriptions", data=data)


@mcp.tool()
def retrieve_subscription(subscription_id: str) -> Dict[str, Any]:
    """Retrieve a subscription by ID."""
    return make_stripe_request("GET", f"/v1/subscriptions/{subscription_id}")


@mcp.tool()
def update_subscription(
    subscription_id: str,
    automatic_tax: Optional[Dict[str, Any]] = None,
    default_payment_method: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    payment_behavior: Optional[str] = None,
    billing_cycle_anchor: Optional[str] = None,
    billing_thresholds: Optional[Dict[str, Any]] = None,
    cancel_at: Optional[int] = None,
    cancel_at_period_end: Optional[bool] = None,
    collection_method: Optional[str] = None,
    days_until_due: Optional[int] = None,
    default_source: Optional[str] = None,
    default_tax_rates: Optional[list] = None,
    discounts: Optional[list] = None,
    invoice_settings: Optional[Dict[str, Any]] = None,
    off_session: Optional[bool] = None,
    payment_settings: Optional[Dict[str, Any]] = None,
    proration_behavior: Optional[str] = None,
    trial_end: Optional[int] = None,
    trial_from_plan: Optional[bool] = None,
    trial_period_days: Optional[int] = None,
    trial_settings: Optional[Dict[str, Any]] = None,
    items: Optional[list] = None,
    proration_date: Optional[int] = None
) -> Dict[str, Any]:
    """Update a subscription by setting new values for specified parameters."""
    data = {}
    
    if automatic_tax:
        if "enabled" in automatic_tax:
            data["automatic_tax[enabled]"] = "true" if automatic_tax["enabled"] else "false"
        if "liability" in automatic_tax:
            liability = automatic_tax["liability"]
            if "account" in liability:
                data["automatic_tax[liability][account]"] = liability["account"]
    if default_payment_method:
        data["default_payment_method"] = default_payment_method
    if description:
        data["description"] = description
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    if payment_behavior:
        data["payment_behavior"] = payment_behavior
    if billing_cycle_anchor:
        data["billing_cycle_anchor"] = billing_cycle_anchor
    if billing_thresholds:
        if "amount_gte" in billing_thresholds:
            data["billing_thresholds[amount_gte]"] = billing_thresholds["amount_gte"]
        if "reset_billing_cycle_anchor" in billing_thresholds:
            data["billing_thresholds[reset_billing_cycle_anchor]"] = "true" if billing_thresholds["reset_billing_cycle_anchor"] else "false"
    if cancel_at:
        data["cancel_at"] = cancel_at
    if cancel_at_period_end is not None:
        data["cancel_at_period_end"] = "true" if cancel_at_period_end else "false"
    if collection_method:
        data["collection_method"] = collection_method
    if days_until_due:
        data["days_until_due"] = days_until_due
    if default_source:
        data["default_source"] = default_source
    if default_tax_rates:
        for i, tax_rate in enumerate(default_tax_rates):
            data[f"default_tax_rates[{i}]"] = tax_rate
    if discounts:
        for i, discount in enumerate(discounts):
            if "coupon" in discount:
                data[f"discounts[{i}][coupon]"] = discount["coupon"]
            if "promotion_code" in discount:
                data[f"discounts[{i}][promotion_code]"] = discount["promotion_code"]
    if invoice_settings:
        if "issuer" in invoice_settings:
            issuer = invoice_settings["issuer"]
            if "type" in issuer:
                data["invoice_settings[issuer][type]"] = issuer["type"]
        if "custom_fields" in invoice_settings:
            for i, field in enumerate(invoice_settings["custom_fields"]):
                data[f"invoice_settings[custom_fields][{i}][name]"] = field.get("name", "")
                data[f"invoice_settings[custom_fields][{i}][value]"] = field.get("value", "")
        if "footer" in invoice_settings:
            data["invoice_settings[footer]"] = invoice_settings["footer"]
        if "rendering_options" in invoice_settings:
            if "amount_decimal_places" in invoice_settings["rendering_options"]:
                data["invoice_settings[rendering_options][amount_decimal_places]"] = invoice_settings["rendering_options"]["amount_decimal_places"]
            if "amount_currency_code" in invoice_settings["rendering_options"]:
                data["invoice_settings[rendering_options][amount_currency_code]"] = invoice_settings["rendering_options"]["amount_currency_code"]
    if off_session is not None:
        data["off_session"] = "true" if off_session else "false"
    if payment_settings:
        if "payment_method_options" in payment_settings:
            for key, value in payment_settings["payment_method_options"].items():
                if isinstance(value, dict):
                    for sub_key, sub_value in value.items():
                        data[f"payment_settings[payment_method_options][{key}][{sub_key}]"] = sub_value
                else:
                    data[f"payment_settings[payment_method_options][{key}]"] = value
        if "payment_method_types" in payment_settings:
            for i, pmt in enumerate(payment_settings["payment_method_types"]):
                data[f"payment_settings[payment_method_types][{i}]"] = pmt
        if "save_default_payment_method" in payment_settings:
            data["payment_settings[save_default_payment_method]"] = payment_settings["save_default_payment_method"]
    if proration_behavior:
        data["proration_behavior"] = proration_behavior
    if trial_end:
        data["trial_end"] = trial_end
    if trial_from_plan is not None:
        data["trial_from_plan"] = "true" if trial_from_plan else "false"
    if trial_period_days:
        data["trial_period_days"] = trial_period_days
    if trial_settings:
        if "end_behavior" in trial_settings:
            end_behavior = trial_settings["end_behavior"]
            if "missing_payment_method" in end_behavior:
                data["trial_settings[end_behavior][missing_payment_method]"] = end_behavior["missing_payment_method"]
    if items:
        for i, item in enumerate(items):
            if "id" in item:
                data[f"items[{i}][id]"] = item["id"]
            if "price" in item:
                data[f"items[{i}][price]"] = item["price"]
            if "quantity" in item:
                data[f"items[{i}][quantity]"] = item["quantity"]
            if "metadata" in item:
                for key, value in item["metadata"].items():
                    data[f"items[{i}][metadata][{key}]"] = value
            if "tax_rates" in item:
                for j, tax_rate in enumerate(item["tax_rates"]):
                    data[f"items[{i}][tax_rates][{j}]"] = tax_rate
    if proration_date:
        data["proration_date"] = proration_date
    
    return make_stripe_request("POST", f"/v1/subscriptions/{subscription_id}", data=data)


@mcp.tool()
def cancel_subscription(
    subscription_id: str,
    cancellation_details: Optional[Dict[str, str]] = None,
    invoice_now: Optional[bool] = None,
    prorate: Optional[bool] = None
) -> Dict[str, Any]:
    """Cancel a subscription.
    
    Args:
        subscription_id: ID of the subscription to cancel
        cancellation_details: Details about why the subscription is being canceled
        invoice_now: Whether to invoice immediately
        prorate: Whether to prorate the subscription
    """
    data = {}
    
    if cancellation_details:
        if "reason" in cancellation_details:
            data["cancellation_details[reason]"] = cancellation_details["reason"]
        if "comment" in cancellation_details:
            data["cancellation_details[comment]"] = cancellation_details["comment"]
    if invoice_now is not None:
        data["invoice_now"] = "true" if invoice_now else "false"
    if prorate is not None:
        data["prorate"] = "true" if prorate else "false"
    
    return make_stripe_request("POST", f"/v1/subscriptions/{subscription_id}/cancel", data=data)


# ==============================================================================
# INVOICES
# ==============================================================================

@mcp.tool()
def create_invoice(
    customer: str,
    auto_advance: Optional[bool] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    collection_method: Optional[str] = None,
    currency: Optional[str] = None,
    customer_description: Optional[str] = None,
    customer_email: Optional[str] = None,
    default_payment_method: Optional[str] = None,
    default_source: Optional[str] = None,
    default_tax_rates: Optional[list] = None,
    description: Optional[str] = None,
    discount: Optional[Dict[str, Any]] = None,
    discounts: Optional[list] = None,
    due_date: Optional[int] = None,
    footer: Optional[str] = None,
    invoice_items: Optional[list] = None,
    issuer: Optional[Dict[str, str]] = None,
    lines: Optional[list] = None,
    metadata: Optional[Dict[str, str]] = None,
    on_behalf_of: Optional[str] = None,
    payment_settings: Optional[Dict[str, Any]] = None,
    rendering_options: Optional[Dict[str, Any]] = None,
    shipping_cost: Optional[Dict[str, Any]] = None,
    shipping_details: Optional[Dict[str, Any]] = None,
    subscription: Optional[str] = None
) -> Dict[str, Any]:
    """Create a new invoice.
    
    Args:
        customer: ID of the customer to invoice
        auto_advance: Whether to automatically finalize and collect the invoice
        automatic_tax: Automatic tax settings
        collection_method: Collection method for the invoice
        currency: Three-letter ISO currency code
        customer_description: Description for the customer
        customer_email: Email address for the customer
        default_payment_method: Default payment method for the invoice
        default_source: Default payment source for the invoice
        default_tax_rates: Tax rates to apply to the invoice
        description: Description for the invoice
        discount: Discount information (deprecated)
        discounts: List of discounts to apply
        due_date: When the invoice is due
        footer: Footer text for the invoice
        invoice_items: Invoice items to add to the invoice
        issuer: Information about who issued the invoice
        lines: Line items for the invoice
        metadata: Key-value pairs for storing additional structured info
        on_behalf_of: Connect account on behalf of which to create the invoice
        payment_settings: Payment settings for the invoice
        rendering_options: Options for rendering the invoice
        shipping_cost: Shipping cost information
        shipping_details: Shipping details
        subscription: Subscription to invoice
    """
    data = {
        "customer": customer
    }
    
    if auto_advance is not None:
        data["auto_advance"] = "true" if auto_advance else "false"
    if automatic_tax:
        if "enabled" in automatic_tax:
            data["automatic_tax[enabled]"] = "true" if automatic_tax["enabled"] else "false"
        if "liability" in automatic_tax:
            liability = automatic_tax["liability"]
            if "account" in liability:
                data["automatic_tax[liability][account]"] = liability["account"]
    if collection_method:
        data["collection_method"] = collection_method
    if currency:
        data["currency"] = currency
    if customer_description:
        data["customer_description"] = customer_description
    if customer_email:
        data["customer_email"] = customer_email
    if default_payment_method:
        data["default_payment_method"] = default_payment_method
    if default_source:
        data["default_source"] = default_source
    if default_tax_rates:
        for i, tax_rate in enumerate(default_tax_rates):
            data[f"default_tax_rates[{i}]"] = tax_rate
    if description:
        data["description"] = description
    if discount:
        if "coupon" in discount:
            data["discount[coupon]"] = discount["coupon"]
        if "customer" in discount:
            data["discount[customer]"] = discount["customer"]
        if "promotion_code" in discount:
            data["discount[promotion_code]"] = discount["promotion_code"]
    if discounts:
        for i, disc in enumerate(discounts):
            if "coupon" in disc:
                data[f"discounts[{i}][coupon]"] = disc["coupon"]
            if "customer" in disc:
                data[f"discounts[{i}][customer]"] = disc["customer"]
            if "promotion_code" in disc:
                data[f"discounts[{i}][promotion_code]"] = disc["promotion_code"]
    if due_date:
        data["due_date"] = due_date
    if footer:
        data["footer"] = footer
    if issuer:
        if "type" in issuer:
            data["issuer[type]"] = issuer["type"]
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    if on_behalf_of:
        data["on_behalf_of"] = on_behalf_of
    if payment_settings:
        if "payment_method_options" in payment_settings:
            for key, value in payment_settings["payment_method_options"].items():
                if isinstance(value, dict):
                    for sub_key, sub_value in value.items():
                        data[f"payment_settings[payment_method_options][{key}][{sub_key}]"] = sub_value
                else:
                    data[f"payment_settings[payment_method_options][{key}]"] = value
        if "payment_method_types" in payment_settings:
            for i, pmt in enumerate(payment_settings["payment_method_types"]):
                data[f"payment_settings[payment_method_types][{i}]"] = pmt
        if "save_default_payment_method" in payment_settings:
            data["payment_settings[save_default_payment_method]"] = payment_settings["save_default_payment_method"]
    if rendering_options:
        if "amount_decimal_places" in rendering_options:
            data["rendering_options[amount_decimal_places]"] = rendering_options["amount_decimal_places"]
        if "amount_currency_code" in rendering_options:
            data["rendering_options[amount_currency_code]"] = rendering_options["amount_currency_code"]
    if shipping_cost:
        if "shipping_amount" in shipping_cost:
            shipping_amount = shipping_cost["shipping_amount"]
            if "amount" in shipping_amount:
                data["shipping_cost[shipping_amount][amount]"] = shipping_amount["amount"]
            if "currency" in shipping_amount:
                data["shipping_cost[shipping_amount][currency]"] = shipping_amount["currency"]
        if "shipping_rate" in shipping_cost:
            data["shipping_cost[shipping_rate]"] = shipping_cost["shipping_rate"]
    if shipping_details:
        if "address" in shipping_details:
            addr = shipping_details["address"]
            if "city" in addr:
                data["shipping_details[address][city]"] = addr["city"]
            if "country" in addr:
                data["shipping_details[address][country]"] = addr["country"]
            if "line1" in addr:
                data["shipping_details[address][line1]"] = addr["line1"]
            if "line2" in addr:
                data["shipping_details[address][line2]"] = addr["line2"]
            if "postal_code" in addr:
                data["shipping_details[address][postal_code]"] = addr["postal_code"]
            if "state" in addr:
                data["shipping_details[address][state]"] = addr["state"]
        if "name" in shipping_details:
            data["shipping_details[name]"] = shipping_details["name"]
        if "phone" in shipping_details:
            data["shipping_details[phone]"] = shipping_details["phone"]
    if subscription:
        data["subscription"] = subscription
    
    return make_stripe_request("POST", "/v1/invoices", data=data)


@mcp.tool()
def retrieve_invoice(invoice_id: str) -> Dict[str, Any]:
    """Retrieve an invoice by ID."""
    return make_stripe_request("GET", f"/v1/invoices/{invoice_id}")


@mcp.tool()
def update_invoice(
    invoice_id: str,
    auto_advance: Optional[bool] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    collection_method: Optional[str] = None,
    customer_description: Optional[str] = None,
    customer_email: Optional[str] = None,
    default_payment_method: Optional[str] = None,
    default_source: Optional[str] = None,
    default_tax_rates: Optional[list] = None,
    description: Optional[str] = None,
    discount: Optional[Dict[str, Any]] = None,
    discounts: Optional[list] = None,
    due_date: Optional[int] = None,
    footer: Optional[str] = None,
    issuer: Optional[Dict[str, str]] = None,
    lines: Optional[list] = None,
    metadata: Optional[Dict[str, str]] = None,
    on_behalf_of: Optional[str] = None,
    payment_settings: Optional[Dict[str, Any]] = None,
    rendering_options: Optional[Dict[str, Any]] = None,
    shipping_cost: Optional[Dict[str, Any]] = None,
    shipping_details: Optional[Dict[str, Any]] = None,
    subscription: Optional[str] = None
) -> Dict[str, Any]:
    """Update an invoice by setting new values for specified parameters."""
    data = {}
    
    if auto_advance is not None:
        data["auto_advance"] = "true" if auto_advance else "false"
    if automatic_tax:
        if "enabled" in automatic_tax:
            data["automatic_tax[enabled]"] = "true" if automatic_tax["enabled"] else "false"
        if "liability" in automatic_tax:
            liability = automatic_tax["liability"]
            if "account" in liability:
                data["automatic_tax[liability][account]"] = liability["account"]
    if collection_method:
        data["collection_method"] = collection_method
    if customer_description:
        data["customer_description"] = customer_description
    if customer_email:
        data["customer_email"] = customer_email
    if default_payment_method:
        data["default_payment_method"] = default_payment_method
    if default_source:
        data["default_source"] = default_source
    if default_tax_rates:
        for i, tax_rate in enumerate(default_tax_rates):
            data[f"default_tax_rates[{i}]"] = tax_rate
    if description:
        data["description"] = description
    if discount:
        if "coupon" in discount:
            data["discount[coupon]"] = discount["coupon"]
        if "customer" in discount:
            data["discount[customer]"] = discount["customer"]
        if "promotion_code" in discount:
            data["discount[promotion_code]"] = discount["promotion_code"]
    if discounts:
        for i, disc in enumerate(discounts):
            if "coupon" in disc:
                data[f"discounts[{i}][coupon]"] = disc["coupon"]
            if "customer" in disc:
                data[f"discounts[{i}][customer]"] = disc["customer"]
            if "promotion_code" in disc:
                data[f"discounts[{i}][promotion_code]"] = disc["promotion_code"]
    if due_date:
        data["due_date"] = due_date
    if footer:
        data["footer"] = footer
    if issuer:
        if "type" in issuer:
            data["issuer[type]"] = issuer["type"]
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    if on_behalf_of:
        data["on_behalf_of"] = on_behalf_of
    if payment_settings:
        if "payment_method_options" in payment_settings:
            for key, value in payment_settings["payment_method_options"].items():
                if isinstance(value, dict):
                    for sub_key, sub_value in value.items():
                        data[f"payment_settings[payment_method_options][{key}][{sub_key}]"] = sub_value
                else:
                    data[f"payment_settings[payment_method_options][{key}]"] = value
        if "payment_method_types" in payment_settings:
            for i, pmt in enumerate(payment_settings["payment_method_types"]):
                data[f"payment_settings[payment_method_types][{i}]"] = pmt
        if "save_default_payment_method" in payment_settings:
            data["payment_settings[save_default_payment_method]"] = payment_settings["save_default_payment_method"]
    if rendering_options:
        if "amount_decimal_places" in rendering_options:
            data["rendering_options[amount_decimal_places]"] = rendering_options["amount_decimal_places"]
        if "amount_currency_code" in rendering_options:
            data["rendering_options[amount_currency_code]"] = rendering_options["amount_currency_code"]
    if shipping_cost:
        if "shipping_amount" in shipping_cost:
            shipping_amount = shipping_cost["shipping_amount"]
            if "amount" in shipping_amount:
                data["shipping_cost[shipping_amount][amount]"] = shipping_amount["amount"]
            if "currency" in shipping_amount:
                data["shipping_cost[shipping_amount][currency]"] = shipping_amount["currency"]
        if "shipping_rate" in shipping_cost:
            data["shipping_cost[shipping_rate]"] = shipping_cost["shipping_rate"]
    if shipping_details:
        if "address" in shipping_details:
            addr = shipping_details["address"]
            if "city" in addr:
                data["shipping_details[address][city]"] = addr["city"]
            if "country" in addr:
                data["shipping_details[address][country]"] = addr["country"]
            if "line1" in addr:
                data["shipping_details[address][line1]"] = addr["line1"]
            if "line2" in addr:
                data["shipping_details[address][line2]"] = addr["line2"]
            if "postal_code" in addr:
                data["shipping_details[address][postal_code]"] = addr["postal_code"]
            if "state" in addr:
                data["shipping_details[address][state]"] = addr["state"]
        if "name" in shipping_details:
            data["shipping_details[name]"] = shipping_details["name"]
        if "phone" in shipping_details:
            data["shipping_details[phone]"] = shipping_details["phone"]
    if subscription:
        data["subscription"] = subscription
    
    return make_stripe_request("POST", f"/v1/invoices/{invoice_id}", data=data)


@mcp.tool()
def finalize_invoice(invoice_id: str) -> Dict[str, Any]:
    """Finalize an invoice.
    
    Args:
        invoice_id: ID of the invoice to finalize
    """
    return make_stripe_request("POST", f"/v1/invoices/{invoice_id}/finalize", data={})


@mcp.tool()
def pay_invoice(invoice_id: str, out_of_band: Optional[bool] = None) -> Dict[str, Any]:
    """Pay an invoice.
    
    Args:
        invoice_id: ID of the invoice to pay
        out_of_band: Whether to pay out of band
    """
    data = {}
    
    if out_of_band is not None:
        data["out_of_band"] = "true" if out_of_band else "false"
    
    return make_stripe_request("POST", f"/v1/invoices/{invoice_id}/pay", data=data)


@mcp.tool()
def void_invoice(invoice_id: str) -> Dict[str, Any]:
    """Void an invoice.
    
    Args:
        invoice_id: ID of the invoice to void
    """
    return make_stripe_request("POST", f"/v1/invoices/{invoice_id}/void", data={})


# ==============================================================================
# REFUNDS
# ==============================================================================

@mcp.tool()
def create_refund(
    amount: Optional[int] = None,
    charge: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    payment_intent: Optional[str] = None,
    reason: Optional[str] = None,
    instructions_email: Optional[str] = None,
    origin: Optional[str] = None,
    reverse_transfer: Optional[bool] = None,
    refund_application_fee: Optional[bool] = None
) -> Dict[str, Any]:
    """Create a new refund.
    
    Args:
        amount: Amount to refund (in smallest currency unit)
        charge: ID of the charge to refund
        metadata: Key-value pairs for storing additional structured info
        payment_intent: ID of the PaymentIntent to refund
        reason: Reason for the refund (duplicate, fraudulent, requested_by_customer)
        instructions_email: Email to send refund instructions to
        origin: Origin of the refund (exchange, external_refund, refund_failed_charge)
        reverse_transfer: Whether to reverse the transfer
        refund_application_fee: Whether to refund the application fee
    """
    data = {}
    
    if amount:
        data["amount"] = amount
    if charge:
        data["charge"] = charge
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    if payment_intent:
        data["payment_intent"] = payment_intent
    if reason:
        data["reason"] = reason
    if instructions_email:
        data["instructions_email"] = instructions_email
    if origin:
        data["origin"] = origin
    if reverse_transfer is not None:
        data["reverse_transfer"] = "true" if reverse_transfer else "false"
    if refund_application_fee is not None:
        data["refund_application_fee"] = "true" if refund_application_fee else "false"
    
    return make_stripe_request("POST", "/v1/refunds", data=data)


@mcp.tool()
def retrieve_refund(refund_id: str) -> Dict[str, Any]:
    """Retrieve a refund by ID."""
    return make_stripe_request("GET", f"/v1/refunds/{refund_id}")


@mcp.tool()
def update_refund(
    refund_id: str,
    metadata: Optional[Dict[str, str]] = None,
    instructions_email: Optional[str] = None
) -> Dict[str, Any]:
    """Update a refund by setting new values for specified parameters."""
    data = {}
    
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    if instructions_email:
        data["instructions_email"] = instructions_email
    
    return make_stripe_request("POST", f"/v1/refunds/{refund_id}", data=data)


# ==============================================================================
# TRANSFERS
# ==============================================================================

@mcp.tool()
def create_transfer(
    amount: int,
    currency: str,
    destination: str,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    source_transaction: Optional[str] = None,
    source_type: Optional[str] = None,
    transfer_group: Optional[str] = None
) -> Dict[str, Any]:
    """Create a new transfer.
    
    Args:
        amount: Amount to transfer (in smallest currency unit)
        currency: Three-letter ISO currency code
        destination: ID of the connected Stripe account
        description: Description for the transfer
        metadata: Key-value pairs for storing additional structured info
        source_transaction: ID of the charge to transfer
        source_type: Type of source (card, bank_account, etc.)
        transfer_group: Group identifier for related transfers
    """
    data = {
        "amount": amount,
        "currency": currency,
        "destination": destination
    }
    
    if description:
        data["description"] = description
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    if source_transaction:
        data["source_transaction"] = source_transaction
    if source_type:
        data["source_type"] = source_type
    if transfer_group:
        data["transfer_group"] = transfer_group
    
    return make_stripe_request("POST", "/v1/transfers", data=data)


@mcp.tool()
def retrieve_transfer(transfer_id: str) -> Dict[str, Any]:
    """Retrieve a transfer by ID."""
    return make_stripe_request("GET", f"/v1/transfers/{transfer_id}")


@mcp.tool()
def update_transfer(
    transfer_id: str,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None
) -> Dict[str, Any]:
    """Update a transfer by setting new values for specified parameters."""
    data = {}
    
    if description:
        data["description"] = description
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    
    return make_stripe_request("POST", f"/v1/transfers/{transfer_id}", data=data)


# ==============================================================================
# DISPUTES
# ==============================================================================

@mcp.tool()
def retrieve_dispute(dispute_id: str) -> Dict[str, Any]:
    """Retrieve a dispute by ID."""
    return make_stripe_request("GET", f"/v1/disputes/{dispute_id}")


@mcp.tool()
def update_dispute(
    dispute_id: str,
    evidence: Optional[Dict[str, str]] = None,
    metadata: Optional[Dict[str, str]] = None,
    submit: Optional[bool] = None
) -> Dict[str, Any]:
    """Update a dispute by submitting evidence.
    
    Args:
        dispute_id: ID of the dispute to update
        evidence: Evidence to submit for the dispute
        metadata: Key-value pairs for storing additional structured info
        submit: Whether to immediately submit evidence to the bank
    """
    data = {}
    
    if evidence:
        evidence_fields = [
            "access_activity_log", "billing_address", "cancellation_policy",
            "cancellation_policy_disclosure", "cancellation_rebuttal",
            "customer_communication", "customer_email_address", "customer_name",
            "customer_purchase_ip", "customer_signature", "duplicate_charge_documentation",
            "duplicate_charge_explanation", "duplicate_charge_id", "product_description",
            "receipt", "refund_policy", "refund_policy_disclosure", "refund_refusal_explanation",
            "service_date", "service_documentation", "shipping_address", "shipping_carrier",
            "shipping_date", "shipping_documentation", "shipping_tracking_number",
            "uncategorized_file", "uncategorized_text"
        ]
        for field in evidence_fields:
            if field in evidence:
                data[f"evidence[{field}]"] = evidence[field]
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    if submit is not None:
        data["submit"] = "true" if submit else "false"
    
    return make_stripe_request("POST", f"/v1/disputes/{dispute_id}", data=data)


@mcp.tool()
def list_disputes(
    charge: Optional[str] = None,
    payment_intent: Optional[str] = None,
    created: Optional[Dict[str, int]] = None,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None
) -> Dict[str, Any]:
    """List all disputes.
    
    Args:
        charge: Filter disputes for a specific charge
        payment_intent: Filter disputes for a specific PaymentIntent
        created: Filter disputes created within a specific timestamp range
        limit: Number of disputes to return (default: 10, max: 100)
        starting_after: ID after which to start listing
        ending_before: ID before which to end listing
    """
    params = {}
    
    if charge:
        params["charge"] = charge
    if payment_intent:
        params["payment_intent"] = payment_intent
    if created:
        if "gte" in created:
            params["created[gte]"] = created["gte"]
        if "lte" in created:
            params["created[lte]"] = created["lte"]
    if limit:
        params["limit"] = limit
    if starting_after:
        params["starting_after"] = starting_after
    if ending_before:
        params["ending_before"] = ending_before
    
    return make_stripe_request("GET", "/v1/disputes", params=params)


# ==============================================================================
# PRODUCTS
# ==============================================================================

@mcp.tool()
def create_product(
    name: str,
    active: Optional[bool] = None,
    description: Optional[str] = None,
    id: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    tax_code: Optional[str] = None,
    default_price_data: Optional[Dict[str, Any]] = None,
    images: Optional[list] = None,
    marketing_features: Optional[list] = None,
    package_dimensions: Optional[Dict[str, Any]] = None,
    shippable: Optional[bool] = None,
    statement_descriptor: Optional[str] = None,
    unit_label: Optional[str] = None,
    url: Optional[str] = None
) -> Dict[str, Any]:
    """Create a new product.
    
    Args:
        name: Product's name (required)
        active: Whether the product is available for purchase
        description: Product's description
        id: Product ID (randomly generated if not provided)
        metadata: Key-value pairs for storing additional structured info
        tax_code: Tax code ID
        default_price_data: Data to create a default price
        images: Product images
        marketing_features: Marketing features
        package_dimensions: Package dimensions
        shippable: Whether the product is shippable
        statement_descriptor: Statement descriptor
        unit_label: Unit label
        url: URL for the product
    """
    data = {
        "name": name
    }
    
    if active is not None:
        data["active"] = "true" if active else "false"
    if description:
        data["description"] = description
    if id:
        data["id"] = id
    if metadata:
        for key, value in metadata.items():
            data[f"metadata[{key}]"] = value
    if tax_code:
        data["tax_code"] = tax_code
    if default_price_data:
        if "currency" in default_price_data:
            data["default_price_data[currency]"] = default_price_data["currency"]
        if "recurring" in default_price_data:
            recurring = default_price_data["recurring"]
            if "interval" in recurring:
                data["default_price_data[recurring][interval]"] = recurring["interval"]
            if "interval_count" in recurring:
                data["default_price_data[recurring][interval_count]"] = recurring["interval_count"]
        if "unit_amount" in default_price_data:
            data["default_price_data[unit_amount]"] = default_price_data["unit_amount"]
        if "product_data" in default_price_data:
            product_data = default_price_data["product_data"]
            if "name" in product_data:
                data["default_price_data[product_data][name]"] = product_data["name"]
    if images:
        for i, img in enumerate(images):
            data[f"images[{i}]"] = img
    if marketing_features:
        for i, feature in enumerate(marketing_features):
            if "type" in feature:
                data[f"marketing_features[{i}][type]"] = feature["type"]
            if "url" in feature:
                data[f"marketing_features[{i}][url]"] = feature["url"]
    if package_dimensions:
        if "height" in package_dimensions:
            data["package_dimensions[height]"] = package_dimensions["height"]
        if "length" in package_dimensions:
            data["package_dimensions[length]"] = package_dimensions["length"]
        if "weight" in package_dimensions:
            data["package_dimensions[weight]"] = package_dimensions["weight"]
        if "width" in package_dimensions:
            data["package_dimensions[width]"] = package_dimensions["width"]
    if shippable is not None:
        data["shippable"] = "true" if shippable else "false"
    if statement_descriptor:
        data["statement_descriptor"] = statement_descriptor
    if unit_label:
        data["unit_label"] = unit_label
    if url:
        data["url"] = url
    
    return make_stripe_request("POST", "/v1/products", data=data)


@mcp.tool()
def retrieve_product(product_id: str) -> Dict[str, Any]:
    """Retrieve a product by ID."""
    return make_stripe_request("GET", f"/v1/products/{product_id}")


@mcp.tool()
def update_product(
    product_id: str,
    active: Optional[bool] = None,
    default_price: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    name: