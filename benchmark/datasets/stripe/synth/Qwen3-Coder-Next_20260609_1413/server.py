#!/usr/bin/env python3
"""Stripe MCP Server - An MCP server for Stripe API operations."""

import os
import requests
from fastmcp import FastMCP

# Create MCP server
mcp = FastMCP("stripe")

# Base URL for Stripe API
STRIPE_BASE_URL = "https://api.stripe.com"
STRIPE_API_VERSION = "2024-10-28.acacia"


def make_stripe_request(method: str, endpoint: str, params: dict = None) -> dict:
    """Make a request to the Stripe API.
    
    Args:
        method: HTTP method (GET, POST, etc.)
        endpoint: API endpoint path (e.g., "/v1/payment_intents")
        params: Request parameters
        
    Returns:
        JSON response from Stripe API
    """
    url = f"{STRIPE_BASE_URL}{endpoint}"
    headers = {
        "Authorization": f"Bearer {os.environ.get('STRIPE_API_KEY')}",
        "Stripe-Version": STRIPE_API_VERSION
    }
    
    try:
        if method.upper() == "GET":
            response = requests.get(url, headers=headers, params=params)
        else:
            # For POST/PUT/PATCH, use form-encoded data
            response = requests.request(method, url, headers=headers, data=params)
        
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        error_dict = {"error": str(e)}
        if hasattr(e, 'response') and e.response is not None:
            try:
                error_dict = e.response.json()
                error_dict["error"] = error_dict.get("error", {}).get("message", str(e))
            except:
                error_dict["error"] = e.response.text
        return error_dict
    except Exception as e:
        return {"error": str(e)}


# ==================== Payment Intents ====================

@mcp.tool()
def create_payment_intent(
    amount: int,
    currency: str,
    automatic_payment_methods_enabled: bool = None,
    confirm: bool = False,
    customer: str = None,
    description: str = None,
    metadata: dict = None,
    payment_method: str = None,
    receipt_email: str = None,
    setup_future_usage: str = None,
    shipping: dict = None,
    statement_descriptor: str = None,
    statement_descriptor_suffix: str = None
) -> dict:
    """Create a PaymentIntent to collect a payment from a customer.
    
    Args:
        amount: Amount intended to be collected (in smallest currency unit)
        currency: Three-letter ISO currency code
        automatic_payment_methods_enabled: Whether to enable automatic payment methods
        confirm: Whether to immediately confirm the PaymentIntent
        customer: ID of the Customer if applicable
        description: Arbitrary description string
        metadata: Key-value pairs for storing additional structured info
        payment_method: ID of the payment method to attach
        receipt_email: Email to send the receipt to
        setup_future_usage: Indicates intent for future payments (off_session or on_session)
        shipping: Shipping information
        statement_descriptor: Statement descriptor for non-card charges
        statement_descriptor_suffix: Statement descriptor suffix for card charges
        
    Returns:
        PaymentIntent object
    """
    params = {
        "amount": amount,
        "currency": currency,
        "confirm": str(confirm).lower() if confirm else None
    }
    
    if automatic_payment_methods_enabled is not None:
        params["automatic_payment_methods[enabled]"] = str(automatic_payment_methods_enabled)
    if customer:
        params["customer"] = customer
    if description:
        params["description"] = description
    if metadata:
        for key, value in metadata.items():
            params[f"metadata[{key}]"] = value
    if payment_method:
        params["payment_method"] = payment_method
    if receipt_email:
        params["receipt_email"] = receipt_email
    if setup_future_usage:
        params["setup_future_usage"] = setup_future_usage
    if shipping:
        # Handle shipping object
        for key, value in shipping.items():
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    params[f"shipping[{key}][{sub_key}]"] = sub_value
            else:
                params[f"shipping[{key}]"] = value
    if statement_descriptor:
        params["statement_descriptor"] = statement_descriptor
    if statement_descriptor_suffix:
        params["statement_descriptor_suffix"] = statement_descriptor_suffix
        
    return make_stripe_request("POST", "/v1/payment_intents", params)


@mcp.tool()
def retrieve_payment_intent(payment_intent_id: str) -> dict:
    """Retrieve the details of a PaymentIntent.
    
    Args:
        payment_intent_id: ID of the PaymentIntent to retrieve
        
    Returns:
        PaymentIntent object
    """
    return make_stripe_request("GET", f"/v1/payment_intents/{payment_intent_id}")


@mcp.tool()
def update_payment_intent(payment_intent_id: str, metadata: dict = None, description: str = None) -> dict:
    """Update a PaymentIntent.
    
    Args:
        payment_intent_id: ID of the PaymentIntent to update
        metadata: Key-value pairs for storing additional structured info
        description: Arbitrary description string
        
    Returns:
        Updated PaymentIntent object
    """
    params = {}
    
    if metadata:
        for key, value in metadata.items():
            params[f"metadata[{key}]"] = value
    if description:
        params["description"] = description
        
    return make_stripe_request("POST", f"/v1/payment_intents/{payment_intent_id}", params)


@mcp.tool()
def confirm_payment_intent(payment_intent_id: str, payment_method: str = None, metadata: dict = None) -> dict:
    """Confirm a PaymentIntent.
    
    Args:
        payment_intent_id: ID of the PaymentIntent to confirm
        payment_method: ID of the payment method to use
        metadata: Key-value pairs for storing additional structured info
        
    Returns:
        PaymentIntent object after confirmation
    """
    params = {"confirm": "true"}
    
    if payment_method:
        params["payment_method"] = payment_method
    if metadata:
        for key, value in metadata.items():
            params[f"metadata[{key}]"] = value
            
    return make_stripe_request("POST", f"/v1/payment_intents/{payment_intent_id}/confirm", params)


@mcp.tool()
def capture_payment_intent(payment_intent_id: str, amount_to_capture: int = None, metadata: dict = None) -> dict:
    """Capture the funds for a PaymentIntent that has been confirmed but not captured.
    
    Args:
        payment_intent_id: ID of the PaymentIntent to capture
        amount_to_capture: Amount to capture (optional, defaults to full amount)
        metadata: Key-value pairs for storing additional structured info
        
    Returns:
        PaymentIntent object after capture
    """
    params = {"capture": "true"}
    
    if amount_to_capture:
        params["amount_to_capture"] = amount_to_capture
    if metadata:
        for key, value in metadata.items():
            params[f"metadata[{key}]"] = value
            
    return make_stripe_request("POST", f"/v1/payment_intents/{payment_intent_id}", params)


@mcp.tool()
def cancel_payment_intent(payment_intent_id: str, cancellation_reason: str = None) -> dict:
    """Cancel a PaymentIntent.
    
    Args:
        payment_intent_id: ID of the PaymentIntent to cancel
        cancellation_reason: Reason for cancellation (duplicate, fraudulent, or requested_by_customer)
        
    Returns:
        PaymentIntent object after cancellation
    """
    params = {}
    
    if cancellation_reason:
        params["cancellation_reason"] = cancellation_reason
        
    return make_stripe_request("POST", f"/v1/payment_intents/{payment_intent_id}/cancel", params)


@mcp.tool()
def list_payment_intents(limit: int = 10, created: str = None, customer: str = None, status: str = None) -> dict:
    """List all PaymentIntents.
    
    Args:
        limit: Number of PaymentIntents to return (default 10, max 100)
        created: Filter by creation timestamp
        customer: Filter by Customer ID
        status: Filter by status (requires_payment_method, requires_confirmation, 
                requires_action, processing, requires_capture, canceled, or succeeded)
                
    Returns:
        List of PaymentIntents
    """
    params = {"limit": limit}
    
    if created:
        params["created"] = created
    if customer:
        params["customer"] = customer
    if status:
        params["status"] = status
        
    return make_stripe_request("GET", "/v1/payment_intents", params)


# ==================== Charges ====================

@mcp.tool()
def create_charge(
    amount: int,
    currency: str,
    source: str = None,
    customer: str = None,
    description: str = None,
    metadata: dict = None,
    receipt_email: str = None,
    shipping: dict = None,
    statement_descriptor: str = None,
    statement_descriptor_suffix: str = None,
    capture: bool = True
) -> dict:
    """Create a Charge to move money into your Stripe account.
    
    Args:
        amount: Amount to charge (in smallest currency unit)
        currency: Three-letter ISO currency code
        source: ID of the payment source (card, bank account, or source token)
        customer: ID of an existing customer
        description: Arbitrary description string
        metadata: Key-value pairs for storing additional structured info
        receipt_email: Email to send the receipt to
        shipping: Shipping information for physical goods
        statement_descriptor: Statement descriptor for non-card charges
        statement_descriptor_suffix: Statement descriptor suffix for card charges
        capture: Whether to immediately capture the charge (default True)
        
    Returns:
        Charge object
    """
    params = {
        "amount": amount,
        "currency": currency,
        "capture": str(capture).lower()
    }
    
    if source:
        params["source"] = source
    if customer:
        params["customer"] = customer
    if description:
        params["description"] = description
    if metadata:
        for key, value in metadata.items():
            params[f"metadata[{key}]"] = value
    if receipt_email:
        params["receipt_email"] = receipt_email
    if shipping:
        for key, value in shipping.items():
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    params[f"shipping[{key}][{sub_key}]"] = sub_value
            else:
                params[f"shipping[{key}]"] = value
    if statement_descriptor:
        params["statement_descriptor"] = statement_descriptor
    if statement_descriptor_suffix:
        params["statement_descriptor_suffix"] = statement_descriptor_suffix
        
    return make_stripe_request("POST", "/v1/charges", params)


@mcp.tool()
def retrieve_charge(charge_id: str) -> dict:
    """Retrieve the details of a Charge.
    
    Args:
        charge_id: ID of the Charge to retrieve
        
    Returns:
        Charge object
    """
    return make_stripe_request("GET", f"/v1/charges/{charge_id}")


@mcp.tool()
def update_charge(charge_id: str, metadata: dict = None, description: str = None, receipt_email: str = None) -> dict:
    """Update a Charge.
    
    Args:
        charge_id: ID of the Charge to update
        metadata: Key-value pairs for storing additional structured info
        description: Arbitrary description string
        receipt_email: Email to send the receipt to
        
    Returns:
        Updated Charge object
    """
    params = {}
    
    if metadata:
        for key, value in metadata.items():
            params[f"metadata[{key}]"] = value
    if description:
        params["description"] = description
    if receipt_email:
        params["receipt_email"] = receipt_email
        
    return make_stripe_request("POST", f"/v1/charges/{charge_id}", params)


@mcp.tool()
def list_charges(limit: int = 10, created: str = None, customer: str = None, status: str = None) -> dict:
    """List all Charges.
    
    Args:
        limit: Number of Charges to return (default 10, max 100)
        created: Filter by creation timestamp
        customer: Filter by Customer ID
        status: Filter by status (succeeded, pending, or failed)
        
    Returns:
        List of Charges
    """
    params = {"limit": limit}
    
    if created:
        params["created"] = created
    if customer:
        params["customer"] = customer
    if status:
        params["status"] = status
        
    return make_stripe_request("GET", "/v1/charges", params)


# ==================== Customers ====================

@mcp.tool()
def create_customer(
    email: str = None,
    name: str = None,
    description: str = None,
    metadata: dict = None,
    address: dict = None,
    phone: str = None,
    shipping: dict = None,
    payment_method: str = None,
    tax: dict = None
) -> dict:
    """Create a Customer object.
    
    Args:
        email: Customer's email address
        name: Customer's full name or business name
        description: Arbitrary description string
        metadata: Key-value pairs for storing additional structured info
        address: Customer's address
        phone: Customer's phone number
        shipping: Customer's shipping information
        payment_method: ID of the PaymentMethod to attach
        tax: Tax details about the customer
        
    Returns:
        Customer object
    """
    params = {}
    
    if email:
        params["email"] = email
    if name:
        params["name"] = name
    if description:
        params["description"] = description
    if metadata:
        for key, value in metadata.items():
            params[f"metadata[{key}]"] = value
    if address:
        for key, value in address.items():
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    params[f"address[{key}][{sub_key}]"] = sub_value
            else:
                params[f"address[{key}]"] = value
    if phone:
        params["phone"] = phone
    if shipping:
        for key, value in shipping.items():
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    params[f"shipping[{key}][{sub_key}]"] = sub_value
            else:
                params[f"shipping[{key}]"] = value
    if payment_method:
        params["payment_method"] = payment_method
    if tax:
        for key, value in tax.items():
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    params[f"tax[{key}][{sub_key}]"] = sub_value
            else:
                params[f"tax[{key}]"] = value
        
    return make_stripe_request("POST", "/v1/customers", params)


@mcp.tool()
def retrieve_customer(customer_id: str) -> dict:
    """Retrieve the details of a Customer.
    
    Args:
        customer_id: ID of the Customer to retrieve
        
    Returns:
        Customer object
    """
    return make_stripe_request("GET", f"/v1/customers/{customer_id}")


@mcp.tool()
def update_customer(customer_id: str, email: str = None, name: str = None, description: str = None, 
                   metadata: dict = None, address: dict = None, phone: str = None, shipping: dict = None) -> dict:
    """Update a Customer.
    
    Args:
        customer_id: ID of the Customer to update
        email: Customer's email address
        name: Customer's full name or business name
        description: Arbitrary description string
        metadata: Key-value pairs for storing additional structured info
        address: Customer's address
        phone: Customer's phone number
        shipping: Customer's shipping information
        
    Returns:
        Updated Customer object
    """
    params = {}
    
    if email:
        params["email"] = email
    if name:
        params["name"] = name
    if description:
        params["description"] = description
    if metadata:
        for key, value in metadata.items():
            params[f"metadata[{key}]"] = value
    if address:
        for key, value in address.items():
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    params[f"address[{key}][{sub_key}]"] = sub_value
            else:
                params[f"address[{key}]"] = value
    if phone:
        params["phone"] = phone
    if shipping:
        for key, value in shipping.items():
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    params[f"shipping[{key}][{sub_key}]"] = sub_value
            else:
                params[f"shipping[{key}]"] = value
        
    return make_stripe_request("POST", f"/v1/customers/{customer_id}", params)


@mcp.tool()
def delete_customer(customer_id: str) -> dict:
    """Delete a Customer.
    
    Args:
        customer_id: ID of the Customer to delete
        
    Returns:
        Deletion confirmation
    """
    return make_stripe_request("DELETE", f"/v1/customers/{customer_id}")


@mcp.tool()
def list_customers(limit: int = 10, created: str = None, email: str = None) -> dict:
    """List all Customers.
    
    Args:
        limit: Number of Customers to return (default 10, max 100)
        created: Filter by creation timestamp
        email: Filter by email address
        
    Returns:
        List of Customers
    """
    params = {"limit": limit}
    
    if created:
        params["created"] = created
    if email:
        params["email"] = email
        
    return make_stripe_request("GET", "/v1/customers", params)


# ==================== Refunds ====================

@mcp.tool()
def create_refund(
    charge: str = None,
    payment_intent: str = None,
    amount: int = None,
    metadata: dict = None,
    reason: str = None,
    instructions_email: str = None
) -> dict:
    """Create a Refund to return funds to a customer.
    
    Args:
        charge: ID of the charge to refund (required unless payment_intent is provided)
        payment_intent: ID of the PaymentIntent to refund (required unless charge is provided)
        amount: Amount to refund (optional, defaults to full amount)
        metadata: Key-value pairs for storing additional structured info
        reason: Reason for the refund (duplicate, fraudulent, or requested_by_customer)
        instructions_email: Email to send refund instructions to
        
    Returns:
        Refund object
    """
    params = {}
    
    if charge:
        params["charge"] = charge
    if payment_intent:
        params["payment_intent"] = payment_intent
    if amount:
        params["amount"] = amount
    if metadata:
        for key, value in metadata.items():
            params[f"metadata[{key}]"] = value
    if reason:
        params["reason"] = reason
    if instructions_email:
        params["instructions_email"] = instructions_email
        
    return make_stripe_request("POST", "/v1/refunds", params)


@mcp.tool()
def retrieve_refund(refund_id: str) -> dict:
    """Retrieve the details of a Refund.
    
    Args:
        refund_id: ID of the Refund to retrieve
        
    Returns:
        Refund object
    """
    return make_stripe_request("GET", f"/v1/refunds/{refund_id}")


@mcp.tool()
def update_refund(refund_id: str, metadata: dict = None) -> dict:
    """Update a Refund.
    
    Args:
        refund_id: ID of the Refund to update
        metadata: Key-value pairs for storing additional structured info
        
    Returns:
        Updated Refund object
    """
    params = {}
    
    if metadata:
        for key, value in metadata.items():
            params[f"metadata[{key}]"] = value
        
    return make_stripe_request("POST", f"/v1/refunds/{refund_id}", params)


@mcp.tool()
def list_refunds(limit: int = 10, created: str = None, charge: str = None, status: str = None) -> dict:
    """List all Refunds.
    
    Args:
        limit: Number of Refunds to return (default 10, max 100)
        created: Filter by creation timestamp
        charge: Filter by Charge ID
        status: Filter by status (pending, requires_action, succeeded, failed, or canceled)
        
    Returns:
        List of Refunds
    """
    params = {"limit": limit}
    
    if created:
        params["created"] = created
    if charge:
        params["charge"] = charge
    if status:
        params["status"] = status
        
    return make_stripe_request("GET", "/v1/refunds", params)


# ==================== Products ====================

@mcp.tool()
def create_product(
    name: str,
    active: bool = True,
    description: str = None,
    id: str = None,
    metadata: dict = None,
    tax_code: str = None,
    images: list = None,
    package_dimensions: dict = None,
    shippable: bool = None,
    statement_descriptor: str = None,
    unit_label: str = None
) -> dict:
    """Create a Product object.
    
    Args:
        name: Product's name (required)
        active: Whether the product is available for purchase (default True)
        description: Product's description
        id: Optional custom product ID
        metadata: Key-value pairs for storing additional structured info
        tax_code: Tax code ID
        images: List of image URLs
        package_dimensions: Package dimensions
        shippable: Whether the product is shippable
        statement_descriptor: Statement descriptor
        unit_label: Unit label
        
    Returns:
        Product object
    """
    params = {"name": name}
    
    if active is not None:
        params["active"] = str(active).lower()
    if description:
        params["description"] = description
    if id:
        params["id"] = id
    if metadata:
        for key, value in metadata.items():
            params[f"metadata[{key}]"] = value
    if tax_code:
        params["tax_code"] = tax_code
    if images:
        for i, image in enumerate(images):
            params[f"images[{i}]"] = image
    if package_dimensions:
        for key, value in package_dimensions.items():
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    params[f"package_dimensions[{key}][{sub_key}]"] = sub_value
            else:
                params[f"package_dimensions[{key}]"] = value
    if shippable is not None:
        params["shippable"] = str(shippable).lower()
    if statement_descriptor:
        params["statement_descriptor"] = statement_descriptor
    if unit_label:
        params["unit_label"] = unit_label
        
    return make_stripe_request("POST", "/v1/products", params)


@mcp.tool()
def retrieve_product(product_id: str) -> dict:
    """Retrieve the details of a Product.
    
    Args:
        product_id: ID of the Product to retrieve
        
    Returns:
        Product object
    """
    return make_stripe_request("GET", f"/v1/products/{product_id}")


@mcp.tool()
def update_product(product_id: str, name: str = None, active: bool = None, description: str = None,
                  metadata: dict = None, default_price: str = None, tax_code: str = None) -> dict:
    """Update a Product.
    
    Args:
        product_id: ID of the Product to update
        name: Product's name
        active: Whether the product is available for purchase
        description: Product's description
        metadata: Key-value pairs for storing additional structured info
        default_price: ID of the default Price
        tax_code: Tax code ID
        
    Returns:
        Updated Product object
    """
    params = {}
    
    if name:
        params["name"] = name
    if active is not None:
        params["active"] = str(active).lower()
    if description:
        params["description"] = description
    if metadata:
        for key, value in metadata.items():
            params[f"metadata[{key}]"] = value
    if default_price:
        params["default_price"] = default_price
    if tax_code:
        params["tax_code"] = tax_code
        
    return make_stripe_request("POST", f"/v1/products/{product_id}", params)


@mcp.tool()
def delete_product(product_id: str) -> dict:
    """Delete a Product.
    
    Args:
        product_id: ID of the Product to delete
        
    Returns:
        Deletion confirmation
    """
    return make_stripe_request("DELETE", f"/v1/products/{product_id}")


@mcp.tool()
def list_products(limit: int = 10, created: str = None, active: bool = None) -> dict:
    """List all Products.
    
    Args:
        limit: Number of Products to return (default 10, max 100)
        created: Filter by creation timestamp
        active: Filter by active status
        
    Returns:
        List of Products
    """
    params = {"limit": limit}
    
    if created:
        params["created"] = created
    if active is not None:
        params["active"] = str(active).lower()
        
    return make_stripe_request("GET", "/v1/products", params)


# ==================== Payment Methods ====================

@mcp.tool()
def create_payment_method(
    type: str,
    billing_details: dict = None,
    metadata: dict = None,
    card: dict = None,
    us_bank_account: dict = None,
    sepa_debit: dict = None,
    ideal: dict = None,
    sofort: dict = None,
    acss_debit: dict = None
) -> dict:
    """Create a PaymentMethod object.
    
    Args:
        type: Type of the PaymentMethod (required)
        billing_details: Billing information
        metadata: Key-value pairs for storing additional structured info
        card: Card details (for card type)
        us_bank_account: US bank account details (for us_bank_account type)
        sepa_debit: SEPA debit details (for sepa_debit type)
        ideal: iDEAL details (for ideal type)
        sofort: SOFORT details (for sofort type)
        acss_debit: ACSS debit details (for acss_debit type)
        
    Returns:
        PaymentMethod object
    """
    params = {"type": type}
    
    if billing_details:
        for key, value in billing_details.items():
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    params[f"billing_details[{key}][{sub_key}]"] = sub_value
            else:
                params[f"billing_details[{key}]"] = value
    if metadata:
        for key, value in metadata.items():
            params[f"metadata[{key}]"] = value
    if card:
        for key, value in card.items():
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    params[f"card[{key}][{sub_key}]"] = sub_value
            else:
                params[f"card[{key}]"] = value
    if us_bank_account:
        for key, value in us_bank_account.items():
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    params[f"us_bank_account[{key}][{sub_key}]"] = sub_value
            else:
                params[f"us_bank_account[{key}]"] = value
    if sepa_debit:
        for key, value in sepa_debit.items():
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    params[f"sepa_debit[{key}][{sub_key}]"] = sub_value
            else:
                params[f"sepa_debit[{key}]"] = value
    if ideal:
        for key, value in ideal.items():
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    params[f"ideal[{key}][{sub_key}]"] = sub_value
            else:
                params[f"ideal[{key}]"] = value
    if sofort:
        for key, value in sofort.items():
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    params[f"sofort[{key}][{sub_key}]"] = sub_value
            else:
                params[f"sofort[{key}]"] = value
    if acss_debit:
        for key, value in acss_debit.items():
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    params[f"acss_debit[{key}][{sub_key}]"] = sub_value
            else:
                params[f"acss_debit[{key}]"] = value
        
    return make_stripe_request("POST", "/v1/payment_methods", params)


@mcp.tool()
def retrieve_payment_method(payment_method_id: str) -> dict:
    """Retrieve the details of a PaymentMethod.
    
    Args:
        payment_method_id: ID of the PaymentMethod to retrieve
        
    Returns:
        PaymentMethod object
    """
    return make_stripe_request("GET", f"/v1/payment_methods/{payment_method_id}")


@mcp.tool()
def update_payment_method(payment_method_id: str, billing_details: dict = None, metadata: dict = None) -> dict:
    """Update a PaymentMethod.
    
    Args:
        payment_method_id: ID of the PaymentMethod to update
        billing_details: Billing information
        metadata: Key-value pairs for storing additional structured info
        
    Returns:
        Updated PaymentMethod object
    """
    params = {}
    
    if billing_details:
        for key, value in billing_details.items():
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    params[f"billing_details[{key}][{sub_key}]"] = sub_value
            else:
                params[f"billing_details[{key}]"] = value
    if metadata:
        for key, value in metadata.items():
            params[f"metadata[{key}]"] = value
        
    return make_stripe_request("POST", f"/v1/payment_methods/{payment_method_id}", params)


@mcp.tool()
def list_payment_methods(customer: str = None, type: str = None, limit: int = 10) -> dict:
    """List PaymentMethods for a Customer or for an account.
    
    Args:
        customer: Customer ID to list PaymentMethods for
        type: Filter by PaymentMethod type
        limit: Number of PaymentMethods to return (default 10, max 100)
        
    Returns:
        List of PaymentMethods
    """
    params = {"limit": limit}
    
    if customer:
        params["customer"] = customer
    if type:
        params["type"] = type
        
    return make_stripe_request("GET", "/v1/payment_methods", params)


# ==================== Subscriptions ====================

@mcp.tool()
def create_subscription(
    customer: str,
    items: list,
    currency: str = None,
    customer_account: str = None,
    default_payment_method: str = None,
    description: str = None,
    metadata: dict = None,
    payment_behavior: str = "default_incomplete",
    collection_method: str = None,
    trial_period_days: int = None,
    trial_end: str = None
) -> dict:
    """Create a Subscription for a Customer.
    
    Args:
        customer: Customer ID to subscribe
        items: List of subscription items with price IDs
        currency: Three-letter ISO currency code
        customer_account: Account representing the customer
        default_payment_method: Default payment method ID
        description: Subscription description
        metadata: Key-value pairs for storing additional structured info
        payment_behavior: Behavior when first invoice can't be paid
        collection_method: Collection method (charge_automatically or send_invoice)
        trial_period_days: Number of trial days
        trial_end: Trial end timestamp or string
        
    Returns:
        Subscription object
    """
    params = {"customer": customer}
    
    # Handle items array
    if items:
        for i, item in enumerate(items):
            for key, value in item.items():
                params[f"items[{i}][{key}]"] = value
    if currency:
        params["currency"] = currency
    if customer_account:
        params["customer_account"] = customer_account
    if default_payment_method:
        params["default_payment_method"] = default_payment_method
    if description:
        params["description"] = description
    if metadata:
        for key, value in metadata.items():
            params[f"metadata[{key}]"] = value
    if payment_behavior:
        params["payment_behavior"] = payment_behavior
    if collection_method:
        params["collection_method"] = collection_method
    if trial_period_days:
        params["trial_period_days"] = trial_period_days
    if trial_end:
        params["trial_end"] = trial_end
        
    return make_stripe_request("POST", "/v1/subscriptions", params)


@mcp.tool()
def retrieve_subscription(subscription_id: str) -> dict:
    """Retrieve the details of a Subscription.
    
    Args:
        subscription_id: ID of the Subscription to retrieve
        
    Returns:
        Subscription object
    """
    return make_stripe_request("GET", f"/v1/subscriptions/{subscription_id}")


@mcp.tool()
def update_subscription(subscription_id: str, metadata: dict = None, description: str = None,
                       cancel_at_period_end: bool = None) -> dict:
    """Update a Subscription.
    
    Args:
        subscription_id: ID of the Subscription to update
        metadata: Key-value pairs for storing additional structured info
        description: Subscription description
        cancel_at_period_end: Whether to cancel at the end of the current period
        
    Returns:
        Updated Subscription object
    """
    params = {}
    
    if metadata:
        for key, value in metadata.items():
            params[f"metadata[{key}]"] = value
    if description:
        params["description"] = description
    if cancel_at_period_end is not None:
        params["cancel_at_period_end"] = str(cancel_at_period_end).lower()
        
    return make_stripe_request("POST", f"/v1/subscriptions/{subscription_id}", params)


@mcp.tool()
def cancel_subscription(subscription_id: str, invoice_now: bool = None) -> dict:
    """Cancel a Subscription.
    
    Args:
        subscription_id: ID of the Subscription to cancel
        invoice_now: Whether to invoice immediately
        
    Returns:
        Subscription object after cancellation
    """
    params = {}
    
    if invoice_now is not None:
        params["invoice_now"] = str(invoice_now).lower()
        
    return make_stripe_request("POST", f"/v1/subscriptions/{subscription_id}/cancel", params)


@mcp.tool()
def list_subscriptions(limit: int = 10, customer: str = None, status: str = None, created: str = None) -> dict:
    """List all Subscriptions.
    
    Args:
        limit: Number of Subscriptions to return (default 10, max 100)
        customer: Filter by Customer ID
        status: Filter by status (incomplete, incomplete_expired, trialing, active, past_due, canceled, unpaid, or paused)
        created: Filter by creation timestamp
        
    Returns:
        List of Subscriptions
    """
    params = {"limit": limit}
    
    if customer:
        params["customer"] = customer
    if status:
        params["status"] = status
    if created:
        params["created"] = created
        
    return make_stripe_request("GET", "/v1/subscriptions", params)


# ==================== Invoices ====================

@mcp.tool()
def create_invoice(
    customer: str,
    auto_advance: bool = False,
    collection_method: str = "charge_automatically",
    description: str = None,
    metadata: dict = None,
    statement_descriptor: str = None,
    default_payment_method: str = None,
    default_source: str = None
) -> dict:
    """Create an Invoice.
    
    Args:
        customer: Customer ID to invoice
        auto_advance: Whether to auto-advance the invoice (default False)
        collection_method: Collection method (charge_automatically or send_invoice)
        description: Invoice description
        metadata: Key-value pairs for storing additional structured info
        statement_descriptor: Statement descriptor
        default_payment_method: Default payment method ID
        default_source: Default payment source ID
        
    Returns:
        Invoice object
    """
    params = {"customer": customer}
    
    if auto_advance is not None:
        params["auto_advance"] = str(auto_advance).lower()
    if collection_method:
        params["collection_method"] = collection_method
    if description:
        params["description"] = description
    if metadata:
        for key, value in metadata.items():
            params[f"metadata[{key}]"] = value
    if statement_descriptor:
        params["statement_descriptor"] = statement_descriptor
    if default_payment_method:
        params["default_payment_method"] = default_payment_method
    if default_source:
        params["default_source"] = default_source
        
    return make_stripe_request("POST", "/v1/invoices", params)


@mcp.tool()
def retrieve_invoice(invoice_id: str) -> dict:
    """Retrieve the details of an Invoice.
    
    Args:
        invoice_id: ID of the Invoice to retrieve
        
    Returns:
        Invoice object
    """
    return make_stripe_request("GET", f"/v1/invoices/{invoice_id}")


@mcp.tool()
def update_invoice(invoice_id: str, metadata: dict = None, description: str = None,
                  statement_descriptor: str = None) -> dict:
    """Update an Invoice.
    
    Args:
        invoice_id: ID of the Invoice to update
        metadata: Key-value pairs for storing additional structured info
        description: Invoice description
        statement_descriptor: Statement descriptor
        
    Returns:
        Updated Invoice object
    """
    params = {}
    
    if metadata:
        for key, value in metadata.items():
            params[f"metadata[{key}]"] = value
    if description:
        params["description"] = description
    if statement_descriptor:
        params["statement_descriptor"] = statement_descriptor
        
    return make_stripe_request("POST", f"/v1/invoices/{invoice_id}", params)


@mcp.tool()
def finalize_invoice(invoice_id: str, close: bool = True) -> dict:
    """Finalize an Invoice.
    
    Args:
        invoice_id: ID of the Invoice to finalize
        close: Whether to close the invoice after finalization (default True)
        
    Returns:
        Finalized Invoice object
    """
    params = {"finalize": "true"}
    
    if close is not None:
        params["close"] = str(close).lower()
        
    return make_stripe_request("POST", f"/v1/invoices/{invoice_id}/finalize", params)


@mcp.tool()
def pay_invoice(invoice_id: str, pay_out_of_band: bool = None) -> dict:
    """Pay an Invoice.
    
    Args:
        invoice_id: ID of the Invoice to pay
        pay_out_of_band: Whether to pay out of band
        
    Returns:
        Invoice object after payment
    """
    params = {"pay": "true"}
    
    if pay_out_of_band is not None:
        params["pay_out_of_band"] = str(pay_out_of_band).lower()
        
    return make_stripe_request("POST", f"/v1/invoices/{invoice_id}/pay", params)


@mcp.tool()
def list_invoices(limit: int = 10, customer: str = None, status: str = None, created: str = None) -> dict:
    """List all Invoices.
    
    Args:
        limit: Number of Invoices to return (default 10, max 100)
        customer: Filter by Customer ID
        status: Filter by status (draft, open, paid, uncollectible, or void)
        created: Filter by creation timestamp
        
    Returns:
        List of Invoices
    """
    params = {"limit": limit}
    
    if customer:
        params["customer"] = customer
    if status:
        params["status"] = status
    if created:
        params["created"] = created
        
    return make_stripe_request("GET", "/v1/invoices", params)


# ==================== Accounts ====================

@mcp.tool()
def create_account(
    country: str = None,
    email: str = None,
    type: str = "express",
    business_type: str = None,
    company: dict = None,
    individual: dict = None,
    capabilities: dict = None,
    controller: dict = None,
    tos_acceptance: dict = None,
    metadata: dict = None,
    settings: dict = None
) -> dict:
    """Create a Stripe account.
    
    Args:
        country: Account country
        email: Account email address
        type: Account type (custom, express, or standard)
        business_type: Business type (company, government_entity, individual, or non_profit)
        company: Company information
        individual: Individual information
        capabilities: Account capabilities
        controller: Account controller configuration
        tos_acceptance: Terms of service acceptance details
        metadata: Key-value pairs for storing additional structured info
        settings: Account settings
        
    Returns:
        Account object
    """
    params = {}
    
    if country:
        params["country"] = country
    if email:
        params["email"] = email
    if type:
        params["type"] = type
    if business_type:
        params["business_type"] = business_type
    if company:
        for key, value in company.items():
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    params[f"company[{key}][{sub_key}]"] = sub_value
            else:
                params[f"company[{key}]"] = value
    if individual:
        for key, value in individual.items():
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    params[f"individual[{key}][{sub_key}]"] = sub_value
            else:
                params[f"individual[{key}]"] = value
    if capabilities:
        for key, value in capabilities.items():
            params[f"capabilities[{key}]"] = value
    if controller:
        for key, value in controller.items():
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    params[f"controller[{key}][{sub_key}]"] = sub_value
            else:
                params[f"controller[{key}]"] = value
    if tos_acceptance:
        for key, value in tos_acceptance.items():
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    params[f"tos_acceptance[{key}][{sub_key}]"] = sub_value
            else:
                params[f"tos_acceptance[{key}]"] = value
    if metadata:
        for key, value in metadata.items():
            params[f"metadata[{key}]"] = value
    if settings:
        for key, value in settings.items():
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    params[f"settings[{key}][{sub_key}]"] = sub_value
            else:
                params[f"settings[{key}]"] = value
        
    return make_stripe_request("POST", "/v1/accounts", params)


@mcp.tool()
def retrieve_account(account_id: str) -> dict:
    """Retrieve the details of a Stripe account.
    
    Args:
        account_id: ID of the Account to retrieve
        
    Returns:
        Account object
    """
    return make_stripe_request("GET", f"/v1/accounts/{account_id}")


@mcp.tool()
def update_account(account_id: str, metadata: dict = None, settings: dict = None, 
                  tos_acceptance: dict = None) -> dict:
    """Update a Stripe account.
    
    Args:
        account_id: ID of the Account to update
        metadata: Key-value pairs for storing additional structured info
        settings: Account settings
        tos_acceptance: Terms of service acceptance details
        
    Returns:
        Updated Account object
    """
    params = {}
    
    if metadata:
        for key, value in metadata.items():
            params[f"metadata[{key}]"] = value
    if settings:
        for key, value in settings.items():
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    params[f"settings[{key}][{sub_key}]"] = sub_value
            else:
                params[f"settings[{key}]"] = value
    if tos_acceptance:
        for key, value in tos_acceptance.items():
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    params[f"tos_acceptance[{key}][{sub_key}]"] = sub_value
            else:
                params[f"tos_acceptance[{key}]"] = value
        
    return make_stripe_request("POST", f"/v1/accounts/{account_id}", params)


@mcp.tool()
def list_accounts(limit: int = 10, created: str = None, email: str = None) -> dict:
    """List all Stripe accounts.
    
    Args:
        limit: Number of Accounts to return (default 10, max 100)
        created: Filter by creation timestamp
        email: Filter by email address
        
    Returns:
        List of Accounts
    """
    params = {"limit": limit}
    
    if created:
        params["created"] = created
    if email:
        params["email"] = email
        
    return make_stripe_request("GET", "/v1/accounts", params)


# ==================== Transfers ====================

@mcp.tool()
def create_transfer(
    amount: int,
    currency: str,
    destination: str,
    description: str = None,
    metadata: dict = None,
    source_transaction: str = None,
    source_type: str = None,
    transfer_group: str = None
) -> dict:
    """Create a Transfer to move funds between Stripe accounts.
    
    Args:
        amount: Amount to transfer (in smallest currency unit)
        currency: Three-letter ISO currency code
        destination: Destination Stripe account ID
        description: Transfer description
        metadata: Key-value pairs for storing additional structured info
        source_transaction: Source transaction ID
        source_type: Source type
        transfer_group: Transfer group ID
        
    Returns:
        Transfer object
    """
    params = {
        "amount": amount,
        "currency": currency,
        "destination": destination
    }
    
    if description:
        params["description"] = description
    if metadata:
        for key, value in metadata.items():
            params[f"metadata[{key}]"] = value
    if source_transaction:
        params["source_transaction"] = source_transaction
    if source_type:
        params["source_type"] = source_type
    if transfer_group:
        params["transfer_group"] = transfer_group
        
    return make_stripe_request("POST", "/v1/transfers", params)


@mcp.tool()
def retrieve_transfer(transfer_id: str) -> dict:
    """Retrieve the details of a Transfer.
    
    Args:
        transfer_id: ID of the Transfer to retrieve
        
    Returns:
        Transfer object
    """
    return make_stripe_request("GET", f"/v1/transfers/{transfer_id}")


@mcp.tool()
def update_transfer(transfer_id: str, metadata: dict = None, description: str = None) -> dict:
    """Update a Transfer.
    
    Args:
        transfer_id: ID of the Transfer to update
        metadata: Key-value pairs for storing additional structured info
        description: Transfer description
        
    Returns:
        Updated Transfer object
    """
    params = {}
    
    if metadata:
        for key, value in metadata.items():
            params[f"metadata[{key}]"] = value
    if description:
        params["description"] = description
        
    return make_stripe_request("POST", f"/v1/transfers/{transfer_id}", params)


@mcp.tool()
def list_transfers(limit: int = 10, created: str = None, destination: str = None, 
                  status: str = None) -> dict:
    """List all Transfers.
    
    Args:
        limit: Number of Transfers to return (default 10, max 100)
        created: Filter by creation timestamp
        destination: Filter by destination account
        status: Filter by status (pending, in_transit, canceled, or failed)
        
    Returns:
        List of Transfers
    """
    params = {"limit": limit}
    
    if created:
        params["created"] = created
    if destination:
        params["destination"] = destination
    if status:
        params["status"] = status
        
    return make_stripe_request("GET", "/v1/transfers", params)


# ==================== Setup Intents ====================

@mcp.tool()
def create_setup_intent(
    payment_method_types: list = None,
    customer: str = None,
    usage: str = "off_session",
    metadata: dict = None,
    description: str = None,
    return_url: str = None
) -> dict:
    """Create a SetupIntent to set up future payments.
    
    Args:
        payment_method_types: List of payment method types
        customer: Customer ID
        usage: How the payment method will be used (off_session or on_session)
        metadata: Key-value pairs for storing additional structured info
        description: Setup intent description
        return_url: URL to redirect to after setup
        
    Returns:
        SetupIntent object
    """
    params = {}
    
    if payment_method_types:
        for i, pt in enumerate(payment_method_types):
            params[f"payment_method_types[{i}]"] = pt
    if customer:
        params["customer"] = customer
    if usage:
        params["usage"] = usage
    if metadata:
        for key, value in metadata.items():
            params[f"metadata[{key}]"] = value
    if description:
        params["description"] = description
    if return_url:
        params["return_url"] = return_url
        
    return make_stripe_request("POST", "/v1/setup_intents", params)


@mcp.tool()
def retrieve_setup_intent(setup_intent_id: str) -> dict:
    """Retrieve the details of a SetupIntent.
    
    Args:
        setup_intent_id: ID of the SetupIntent to retrieve
        
    Returns:
        SetupIntent object
    """
    return make_stripe_request("GET", f"/v1/setup_intents/{setup_intent_id}")


@mcp.tool()
def confirm_setup_intent(setup_intent_id: str, payment_method: str = None) -> dict:
    """Confirm a SetupIntent.
    
    Args:
        setup_intent_id: ID of the SetupIntent to confirm
        payment_method: Payment method ID to use
        
    Returns:
        SetupIntent object after confirmation
    """
    params = {"confirm": "true"}
    
    if payment_method:
        params["payment_method"] = payment_method
        
    return make_stripe_request("POST", f"/v1/setup_intents/{setup_intent_id}/confirm", params)


@mcp.tool()
def cancel_setup_intent(setup_intent_id: str) -> dict:
    """Cancel a SetupIntent.
    
    Args:
        setup_intent_id: ID of the SetupIntent to cancel
        
    Returns:
        SetupIntent object after cancellation
    """
    return make_stripe_request("POST", f"/v1/setup_intents/{setup_intent_id}/cancel", params)


# ==================== Balances ====================

@mcp.tool()
def retrieve_balance() -> dict:
    """Retrieve the current Stripe balance.
    
    Returns:
        Balance object
    """
    return make_stripe_request("GET", "/v1/balance")


@mcp.tool()
def retrieve_balance_transaction(balance_transaction_id: str) -> dict:
    """Retrieve a balance transaction.
    
    Args:
        balance_transaction_id: ID of the balance transaction to retrieve
        
    Returns:
        Balance transaction object
    """
    return make_stripe_request("GET", f"/v1/balance_transactions/{balance_transaction_id}")


@mcp.tool()
def list_balance_transactions(limit: int = 10, created: str = None, type: str = None) -> dict:
    """List balance transactions.
    
    Args:
        limit: Number of transactions to return (default 10, max 100)
        created: Filter by creation timestamp
        type: Filter by transaction type
        
    Returns:
        List of balance transactions
    """
    params = {"limit": limit}
    
    if created:
        params["created"] = created
    if type:
        params["type"] = type
        
    return make_stripe_request("GET", "/v1/balance_transactions", params)


# ==================== Referral Program ====================

@mcp.tool()
def create_referral(referral_type: str, email: str = None, name: str = None, 
                   metadata: dict = None) -> dict:
    """Create a referral for the Stripe referral program.
    
    Args:
        referral_type: Type of referral (affiliate or influencer)
        email: Email address of the referee
        name: Name of the referee
        metadata: Key-value pairs for storing additional structured info
        
    Returns:
        Referral object
    """
    params = {"type": referral_type}
    
    if email:
        params["email"] = email
    if name:
        params["name"] = name
    if metadata:
        for key, value in metadata.items():
            params[f"metadata[{key}]"] = value
        
    return make_stripe_request("POST", "/v1/referrals", params)


# ==================== Run the server ====================

if __name__ == "__main__":
    mcp.run()
tr = None, status: str = None) -> dict:
    """List all Refunds.
    
    Args:
        limit: Number of Refunds to return (default 10, max 100)
        created: Filter by creation timestamp
        charge: Filter by Charge ID
        status: Filter by status (pending, requires_action, succeeded, failed, or canceled)
        
    Returns:
        List of Refunds
    """
    params = {"limit": limit}
    
    if created:
        params["created"] = created
    if charge:
        params["charge"] = charge
    if status:
        params["status"] = status
        
    return make_stripe_request("GET", "/v1/refunds", params)


# ==================== Products ====================

@mcp.tool()
def create_product(
    name: str,
    active: bool = True,
    description: str = None,
    id: str = None,
    metadata: dict = None,
    tax_code: str = None,
    images: list = None,
    package_dimensions: dict = None,
    shippable: bool = None,
    statement_descriptor: str = None,
    unit_label: str = None
) -> dict:
    """Create a Product object.
    
    Args:
        name: Product's name (required)
        active: Whether the product is available for purchase (default True)
        description: Product's description
        id: Optional custom product ID
        metadata: Key-value pairs for storing additional structured info
        tax_code: Tax code ID
        images: List of image URLs
        package_dimensions: Package dimensions
        shippable: Whether the product is shippable
        statement_descriptor: Statement descriptor
        unit_label: Unit label
        
    Returns:
        Product object
    """
    params = {"name": name}
    
    if active is not None:
        params["active"] = str(active).lower()
    if description:
        params["description"] = description
    if id:
        params["id"] = id
    if metadata:
        for key, value in metadata.items():
            params[f"metadata[{key}]"] = value
    if tax_code:
        params["tax_code"] = tax_code
    if images:
        for i, image in enumerate(images):
            params[f"images[{i}]"] = image
    if package_dimensions:
        for key, value in package_dimensions.items():
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    params[f"package_dimensions[{key}][{sub_key}]"] = sub_value
            else:
                params[f"package_dimensions[{key}]"] = value
    if shippable is not None:
        params["shippable"] = str(shippable).lower()
    if statement_descriptor:
        params["statement_descriptor"] = statement_descriptor
    if unit_label:
        params["unit_label"] = unit_label
        
    return make_stripe_request("POST", "/v1/products", params)


@mcp.tool()
def retrieve_product(product_id: str) -> dict:
    """Retrieve the details of a Product.
    
    Args:
        product_id: ID of the Product to retrieve
        
    Returns:
        Product object
    """
    return make_stripe_request("GET", f"/v1/products/{product_id}")


@mcp.tool()
def update_product(product_id: str, name: str = None, active: bool = None, description: str = None,
                  metadata: dict = None, default_price: str = None, tax_code: str = None) -> dict:
    """Update a Product.
    
    Args:
        product_id: ID of the Product to update
        name: Product's name
        active: Whether the product is available for purchase
        description: Product's description
        metadata: Key-value pairs for storing additional structured info
        default_price: ID of the default Price
        tax_code: Tax code ID
        
    Returns:
        Updated Product object
    """
    params = {}
    
    if name:
        params["name"] = name
    if active is not None:
        params["active"] = str(active).lower()
    if description:
        params["description"] = description
    if metadata:
        for key, value in metadata.items():
            params[f"metadata[{key}]"] = value
    if default_price:
        params["default_price"] = default_price
    if tax_code:
        params["tax_code"] = tax_code
        
    return make_stripe_request("POST", f"/v1/products/{product_id}", params)


@mcp.tool()
def delete_product(product_id: str) -> dict:
    """Delete a Product.
    
    Args:
        product_id: ID of the Product to delete
        
    Returns:
        Deletion confirmation
    """
    return make_stripe_request("DELETE", f"/v1/products/{product_id}")


@mcp.tool()
def list_products(limit: int = 10, created: str = None, active: bool = None) -> dict:
    """List all Products.
    
    Args:
        limit: Number of Products to return (default 10, max 100)
        created: Filter by creation timestamp
        active: Filter by active status
        
    Returns:
        List of Products
    """
    params = {"limit": limit}
    
    if created:
        params["created"] = created
    if active is not None:
        params["active"] = str(active).lower()
        
    return make_stripe_request("GET", "/v1/products", params)


# ==================== Payment Methods ====================

@mcp.tool()
def create_payment_method(
    type: str,
    billing_details: dict = None,
    metadata: dict = None,
    card: dict = None,
    us_bank_account: dict = None,
    sepa_debit: dict = None,
    ideal: dict = None,
    sofort: dict = None,
    acss_debit: dict = None
) -> dict:
    """Create a PaymentMethod object.
    
    Args:
        type: Type of the PaymentMethod (required)
        billing_details: Billing information
        metadata: Key-value pairs for storing additional structured info
        card: Card details (for card type)
        us_bank_account: US bank account details (for us_bank_account type)
        sepa_debit: SEPA debit details (for sepa_debit type)
        ideal: iDEAL details (for ideal type)
        sofort: SOFORT details (for sofort type)
        acss_debit: ACSS debit details (for acss_debit type)
        
    Returns:
        PaymentMethod object
    """
    params = {"type": type}
    
    if billing_details:
        for key, value in billing_details.items():
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    params[f"billing_details[{key}][{sub_key}]"] = sub_value
            else:
                params[f"billing_details[{key}]"] = value
    if metadata:
        for key, value in metadata.items():
            params[f"metadata[{key}]"] = value
    if card:
        for key, value in card.items():
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    params[f"card[{key}][{sub_key}]"] = sub_value
            else:
                params[f"card[{key}]"] = value
    if us_bank_account:
        for key, value in us_bank_account.items():
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    params[f"us_bank_account[{key}][{sub_key}]"] = sub_value
            else:
                params[f"us_bank_account[{key}]"] = value
    if sepa_debit:
        for key, value in sepa_debit.items():
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    params[f"sepa_debit[{key}][{sub_key}]"] = sub_value
            else:
                params[f"sepa_debit[{key}]"] = value
    if ideal:
        for key, value in ideal.items():
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    params[f"ideal[{key}][{sub_key}]"] = sub_value
            else:
                params[f"ideal[{key}]"] = value
    if sofort:
        for key, value in sofort.items():
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    params[f"sofort[{key}][{sub_key}]"] = sub_value
            else:
                params[f"sofort[{key}]"] = value
    if acss_debit:
        for key, value in acss_debit.items():
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    params[f"acss_debit[{key}][{sub_key}]"] = sub_value
            else:
                params[f"acss_debit[{key}]"] = value
        
    return make_stripe_request("POST", "/v1/payment_methods", params)


@mcp.tool()
def retrieve_payment_method(payment_method_id: str) -> dict:
    """Retrieve the details of a PaymentMethod.
    
    Args:
        payment_method_id: ID of the PaymentMethod to retrieve
        
    Returns:
        PaymentMethod object
    """
    return make_stripe_request("GET", f"/v1/payment_methods/{payment_method_id}")


@mcp.tool()
def update_payment_method(payment_method_id: str, billing_details: dict = None, metadata: dict = None) -> dict:
    """Update a PaymentMethod.
    
    Args:
        payment_method_id: ID of the PaymentMethod to update
        billing_details: Billing information
        metadata: Key-value pairs for storing additional structured info
        
    Returns:
        Updated PaymentMethod object
    """
    params = {}
    
    if billing_details:
        for key, value in billing_details.items():
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    params[f"billing_details[{key}][{sub_key}]"] = sub_value
            else:
                params[f"billing_details[{key}]"] = value
    if metadata:
        for key, value in metadata.items():
            params[f"metadata[{key}]"] = value
        
    return make_stripe_request("POST", f"/v1/payment_methods/{payment_method_id}", params)


@mcp.tool()
def list_payment_methods(customer: str = None, type: str = None, limit: int = 10) -> dict:
    """List PaymentMethods for a Customer or for an account.
    
    Args:
        customer: Customer ID to list PaymentMethods for
        type: Filter by PaymentMethod type
        limit: Number of PaymentMethods to return (default 10, max 100)
        
    Returns:
        List of PaymentMethods
    """
    params = {"limit": limit}
    
    if customer:
        params["customer"] = customer
    if type:
        params["type"] = type
        
    return make_stripe_request("GET", "/v1/payment_methods", params)


# ==================== Subscriptions ====================

@mcp.tool()
def create_subscription(
    customer: str,
    items: list,
    currency: str = None,
    customer_account: str = None,
    default_payment_method: str = None,
    description: str = None,
    metadata: dict = None,
    payment_behavior: str = "default_incomplete",
    collection_method: str = None,
    trial_period_days: int = None,
    trial_end: str = None
) -> dict:
    """Create a Subscription for a Customer.
    
    Args:
        customer: Customer ID to subscribe
        items: List of subscription items with price IDs
        currency: Three-letter ISO currency code
        customer_account: Account representing the customer
        default_payment_method: Default payment method ID
        description: Subscription description
        metadata: Key-value pairs for storing additional structured info
        payment_behavior: Behavior when first invoice can't be paid
        collection_method: Collection method (charge_automatically or send_invoice)
        trial_period_days: Number of trial days
        trial_end: Trial end timestamp or string
        
    Returns:
        Subscription object
    """
    params = {"customer": customer}
    
    # Handle items array
    if items:
        for i, item in enumerate(items):
            for key, value in item.items():
                params[f"items[{i}][{key}]"] = value
    if currency:
        params["currency"] = currency
    if customer_account:
        params["customer_account"] = customer_account
    if default_payment_method:
        params["default_payment_method"] = default_payment_method
    if description:
        params["description"] = description
    if metadata:
        for key, value in metadata.items():
            params[f"metadata[{key}]"] = value
    if payment_behavior:
        params["payment_behavior"] = payment_behavior
    if collection_method:
        params["collection_method"] = collection_method
    if trial_period_days:
        params["trial_period_days"] = trial_period_days
    if trial_end:
        params["trial_end"] = trial_end
        
    return make_stripe_request("POST", "/v1/subscriptions", params)


@mcp.tool()
def retrieve_subscription(subscription_id: str) -> dict:
    """Retrieve the details of a Subscription.
    
    Args:
        subscription_id: ID of the Subscription to retrieve
        
    Returns:
        Subscription object
    """
    return make_stripe_request("GET", f"/v1/subscriptions/{subscription_id}")


@mcp.tool()
def update_subscription(subscription_id: str, metadata: dict = None, description: str = None,
                       cancel_at_period_end: bool = None) -> dict:
    """Update a Subscription.
    
    Args:
        subscription_id: ID of the Subscription to update
        metadata: Key-value pairs for storing additional structured info
        description: Subscription description
        cancel_at_period_end: Whether to cancel at the end of the current period
        
    Returns:
        Updated Subscription object
    """
    params = {}
    
    if metadata:
        for key, value in metadata.items():
            params[f"metadata[{key}]"] = value
    if description:
        params["description"] = description
    if cancel_at_period_end is not None:
        params["cancel_at_period_end"] = str(cancel_at_period_end).lower()
        
    return make_stripe_request("POST", f"/v1/subscriptions/{subscription_id}", params)


@mcp.tool()
def cancel_subscription(subscription_id: str, invoice_now: bool = None) -> dict:
    """Cancel a Subscription.
    
    Args:
        subscription_id: ID of the Subscription to cancel
        invoice_now: Whether to invoice immediately
        
    Returns:
        Subscription object after cancellation
    """
    params = {}
    
    if invoice_now is not None:
        params["invoice_now"] = str(invoice_now).lower()
        
    return make_stripe_request("POST", f"/v1/subscriptions/{subscription_id}/cancel", params)


@mcp.tool()
def list_subscriptions(limit: int = 10, customer: str = None, status: str = None, created: str = None) -> dict:
    """List all Subscriptions.
    
    Args:
        limit: Number of Subscriptions to return (default 10, max 100)
        customer: Filter by Customer ID
        status: Filter by status (incomplete, incomplete_expired, trialing, active, past_due, canceled, unpaid, or paused)
        created: Filter by creation timestamp
        
    Returns:
        List of Subscriptions
    """
    params = {"limit": limit}
    
    if customer:
        params["customer"] = customer
    if status:
        params["status"] = status
    if created:
        params["created"] = created
        
    return make_stripe_request("GET", "/v1/subscriptions", params)


# ==================== Invoices ====================

@mcp.tool()
def create_invoice(
    customer: str,
    auto_advance: bool = False,
    collection_method: str = "charge_automatically",
    description: str = None,
    metadata: dict = None,
    statement_descriptor: str = None,
    default_payment_method: str = None,
    default_source: str = None
) -> dict:
    """Create an Invoice.
    
    Args:
        customer: Customer ID to invoice
        auto_advance: Whether to auto-advance the invoice (default False)
        collection_method: Collection method (charge_automatically or send_invoice)
        description: Invoice description
        metadata: Key-value pairs for storing additional structured info
        statement_descriptor: Statement descriptor
        default_payment_method: Default payment method ID
        default_source: Default payment source ID
        
    Returns:
        Invoice object
    """
    params = {"customer": customer}
    
    if auto_advance is not None:
        params["auto_advance"] = str(auto_advance).lower()
    if collection_method:
        params["collection_method"] = collection_method
    if description:
        params["description"] = description
    if metadata:
        for key, value in metadata.items():
            params[f"metadata[{key}]"] = value
    if statement_descriptor:
        params["statement_descriptor"] = statement_descriptor
    if default_payment_method:
        params["default_payment_method"] = default_payment_method
    if default_source:
        params["default_source"] = default_source
        
    return make_stripe_request("POST", "/v1/invoices", params)


@mcp.tool()
def retrieve_invoice(invoice_id: str) -> dict:
    """Retrieve the details of an Invoice.
    
    Args:
        invoice_id: ID of the Invoice to retrieve
        
    Returns:
        Invoice object
    """
    return make_stripe_request("GET", f"/v1/invoices/{invoice_id}")


@mcp.tool()
def update_invoice(invoice_id: str, metadata: dict = None, description: str = None,
                  statement_descriptor: str = None) -> dict:
    """Update an Invoice.
    
    Args:
        invoice_id: ID of the Invoice to update
        metadata: Key-value pairs for storing additional structured info
        description: Invoice description
        statement_descriptor: Statement descriptor
        
    Returns:
        Updated Invoice object
    """
    params = {}
    
    if metadata:
        for key, value in metadata.items():
            params[f"metadata[{key}]"] = value
    if description:
        params["description"] = description
    if statement_descriptor:
        params["statement_descriptor"] = statement_descriptor
        
    return make_stripe_request("POST", f"/v1/invoices/{invoice_id}", params)


@mcp.tool()
def finalize_invoice(invoice_id: str, close: bool = True) -> dict:
    """Finalize an Invoice.
    
    Args:
        invoice_id: ID of the Invoice to finalize
        close: Whether to close the invoice after finalization (default True)
        
    Returns:
        Finalized Invoice object
    """
    params = {"finalize": "true"}
    
    if close is not None:
        params["close"] = str(close).lower()
        
    return make_stripe_request("POST", f"/v1/invoices/{invoice_id}/finalize", params)


@mcp.tool()
def pay_invoice(invoice_id: str, pay_out_of_band: bool = None) -> dict:
    """Pay an Invoice.
    
    Args:
        invoice_id: ID of the Invoice to pay
        pay_out_of_band: Whether to pay out of band
        
    Returns:
        Invoice object after payment
    """
    params = {"pay": "true"}
    
    if pay_out_of_band is not None:
        params["pay_out_of_band"] = str(pay_out_of_band).lower()
        
    return make_stripe_request("POST", f"/v1/invoices/{invoice_id}/pay", params)


@mcp.tool()
def list_invoices(limit: int = 10, customer: str = None, status: str = None, created: str = None) -> dict:
    """List all Invoices.
    
    Args:
        limit: Number of Invoices to return (default 10, max 100)
        customer: Filter by Customer ID
        status: Filter by status (draft, open, paid, uncollectible, or void)
        created: Filter by creation timestamp
        
    Returns:
        List of Invoices
    """
    params = {"limit": limit}
    
    if customer:
        params["customer"] = customer
    if status:
        params["status"] = status
    if created:
        params["created"] = created
        
    return make_stripe_request("GET", "/v1/invoices", params)


# ==================== Accounts ====================

@mcp.tool()
def create_account(
    country: str = None,
    email: str = None,
    type: str = "express",
    business_type: str = None,
    company: dict = None,
    individual: dict = None,
    capabilities: dict = None,
    controller: dict = None,
    tos_acceptance: dict = None,
    metadata: dict = None,
    settings: dict = None
) -> dict:
    """Create a Stripe account.
    
    Args:
        country: Account country
        email: Account email address
        type: Account type (custom, express, or standard)
        business_type: Business type (company, government_entity, individual, or non_profit)
        company: Company information
        individual: Individual information
        capabilities: Account capabilities
        controller: Account controller configuration
        tos_acceptance: Terms of service acceptance details
        metadata: Key-value pairs for storing additional structured info
        settings: Account settings
        
    Returns:
        Account object
    """
    params = {}
    
    if country:
        params["country"] = country
    if email:
        params["email"] = email
    if type:
        params["type"] = type
    if business_type:
        params["business_type"] = business_type
    if company:
        for key, value in company.items():
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    params[f"company[{key}][{sub_key}]"] = sub_value
            else:
                params[f"company[{key}]"] = value
    if individual:
        for key, value in individual.items():
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    params[f"individual[{key}][{sub_key}]"] = sub_value
            else:
                params[f"individual[{key}]"] = value
    if capabilities:
        for key, value in capabilities.items():
            params[f"capabilities[{key}]"] = value
    if controller:
        for key, value in controller.items():
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    params[f"controller[{key}][{sub_key}]"] = sub_value
            else:
                params[f"controller[{key}]"] = value
    if tos_acceptance:
        for key, value in tos_acceptance.items():
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    params[f"tos_acceptance[{key}][{sub_key}]"] = sub_value
            else:
                params[f"tos_acceptance[{key}]"] = value
    if metadata:
        for key, value in metadata.items():
            params[f"metadata[{key}]"] = value
    if settings:
        for key, value in settings.items():
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    params[f"settings[{key}][{sub_key}]"] = sub_value
            else:
                params[f"settings[{key}]"] = value
        
    return make_stripe_request("POST", "/v1/accounts", params)


@mcp.tool()
def retrieve_account(account_id: str) -> dict:
    """Retrieve the details of a Stripe account.
    
    Args:
        account_id: ID of the Account to retrieve
        
    Returns:
        Account object
    """
    return make_stripe_request("GET", f"/v1/accounts/{account_id}")


@mcp.tool()
def update_account(account_id: str, metadata: dict = None, settings: dict = None, 
                  tos_acceptance: dict = None) -> dict:
    """Update a Stripe account.
    
    Args:
        account_id: ID of the Account to update
        metadata: Key-value pairs for storing additional structured info
        settings: Account settings
        tos_acceptance: Terms of service acceptance details
        
    Returns:
        Updated Account object
    """
    params = {}
    
    if metadata:
        for key, value in metadata.items():
            params[f"metadata[{key}]"] = value
    if settings:
        for key, value in settings.items():
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    params[f"settings[{key}][{sub_key}]"] = sub_value
            else:
                params[f"settings[{key}]"] = value
    if tos_acceptance:
        for key, value in tos_acceptance.items():
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    params[f"tos_acceptance[{key}][{sub_key}]"] = sub_value
            else:
                params[f"tos_acceptance[{key}]"] = value
        
    return make_stripe_request("POST", f"/v1/accounts/{account_id}", params)


@mcp.tool()
def list_accounts(limit: int = 10, created: str = None, email: str = None) -> dict:
    """List all Stripe accounts.
    
    Args:
        limit: Number of Accounts to return (default 10, max 100)
        created: Filter by creation timestamp
        email: Filter by email address
        
    Returns:
        List of Accounts
    """
    params = {"limit": limit}
    
    if created:
        params["created"] = created
    if email:
        params["email"] = email
        
    return make_stripe_request("GET", "/v1/accounts", params)


# ==================== Transfers ====================

@mcp.tool()
def create_transfer(
    amount: int,
    currency: str,
    destination: str,
    description: str = None,
    metadata: dict = None,
    source_transaction: str = None,
    source_type: str = None,
    transfer_group: str = None
) -> dict:
    """Create a Transfer to move funds between Stripe accounts.
    
    Args:
        amount: Amount to transfer (in smallest currency unit)
        currency: Three-letter ISO currency code
        destination: Destination Stripe account ID
        description: Transfer description
        metadata: Key-value pairs for storing additional structured info
        source_transaction: Source transaction ID
        source_type: Source type
        transfer_group: Transfer group ID
        
    Returns:
        Transfer object
    """
    params = {
        "amount": amount,
        "currency": currency,
        "destination": destination
    }
    
    if description:
        params["description"] = description
    if metadata:
        for key, value in metadata.items():
            params[f"metadata[{key}]"] = value
    if source_transaction:
        params["source_transaction"] = source_transaction
    if source_type:
        params["source_type"] = source_type
    if transfer_group:
        params["transfer_group"] = transfer_group
        
    return make_stripe_request("POST", "/v1/transfers", params)


@mcp.tool()
def retrieve_transfer(transfer_id: str) -> dict:
    """Retrieve the details of a Transfer.
    
    Args:
        transfer_id: ID of the Transfer to retrieve
        
    Returns:
        Transfer object
    """
    return make_stripe_request("GET", f"/v1/transfers/{transfer_id}")


@mcp.tool()
def update_transfer(transfer_id: str, metadata: dict = None, description: str = None) -> dict:
    """Update a Transfer.
    
    Args:
        transfer_id: ID of the Transfer to update
        metadata: Key-value pairs for storing additional structured info
        description: Transfer description
        
    Returns:
        Updated Transfer object
    """
    params = {}
    
    if metadata:
        for key, value in metadata.items():
            params[f"metadata[{key}]"] = value
    if description:
        params["description"] = description
        
    return make_stripe_request("POST", f"/v1/transfers/{transfer_id}", params)


@mcp.tool()
def list_transfers(limit: int = 10, created: str = None, destination: str = None, 
                  status: str = None) -> dict:
    """List all Transfers.
    
    Args:
        limit: Number of Transfers to return (default 10, max 100)
        created: Filter by creation timestamp
        destination: Filter by destination account
        status: Filter by status (pending, in_transit, canceled, or failed)
        
    Returns:
        List of Transfers
    """
    params = {"limit": limit}
    
    if created:
        params["created"] = created
    if destination:
        params["destination"] = destination
    if status:
        params["status"] = status
        
    return make_stripe_request("GET", "/v1/transfers", params)


# ==================== Setup Intents ====================

@mcp.tool()
def create_setup_intent(
    payment_method_types: list = None,
    customer: str = None,
    usage: str = "off_session",
    metadata: dict = None,
    description: str = None,
    return_url: str = None
) -> dict:
    """Create a SetupIntent to set up future payments.
    
    Args:
        payment_method_types: List of payment method types
        customer: Customer ID
        usage: How the payment method will be used (off_session or on_session)
        metadata: Key-value pairs for storing additional structured info
        description: Setup intent description
        return_url: URL to redirect to after setup
        
    Returns:
        SetupIntent object
    """
    params = {}
    
    if payment_method_types:
        for i, pt in enumerate(payment_method_types):
            params[f"payment_method_types[{i}]"] = pt
    if customer:
        params["customer"] = customer
    if usage:
        params["usage"] = usage
    if metadata:
        for key, value in metadata.items():
            params[f"metadata[{key}]"] = value
    if description:
        params["description"] = description
    if return_url:
        params["return_url"] = return_url
        
    return make_stripe_request("POST", "/v1/setup_intents", params)


@mcp.tool()
def retrieve_setup_intent(setup_intent_id: str) -> dict:
    """Retrieve the details of a SetupIntent.
    
    Args:
        setup_intent_id: ID of the SetupIntent to retrieve
        
    Returns:
        SetupIntent object
    """
    return make_stripe_request("GET", f"/v1/setup_intents/{setup_intent_id}")


@mcp.tool()
def confirm_setup_intent(setup_intent_id: str, payment_method: str = None) -> dict:
    """Confirm a SetupIntent.
    
    Args:
        setup_intent_id: ID of the SetupIntent to confirm
        payment_method: Payment method ID to use
        
    Returns:
        SetupIntent object after confirmation
    """
    params = {"confirm": "true"}
    
    if payment_method:
        params["payment_method"] = payment_method
        
    return make_stripe_request("POST", f"/v1/setup_intents/{setup_intent_id}/confirm", params)


@mcp.tool()
def cancel_setup_intent(setup_intent_id: str) -> dict:
    """Cancel a SetupIntent.
    
    Args:
        setup_intent_id: ID of the SetupIntent to cancel
        
    Returns:
        SetupIntent object after cancellation
    """
    return make_stripe_request("POST", f"/v1/setup_intents/{setup_intent_id}/cancel", params)


# ==================== Balances ====================

@mcp.tool()
def retrieve_balance() -> dict:
    """Retrieve the current Stripe balance.
    
    Returns:
        Balance object
    """
    return make_stripe_request("GET", "/v1/balance")


@mcp.tool()
def retrieve_balance_transaction(balance_transaction_id: str) -> dict:
    """Retrieve a balance transaction.
    
    Args:
        balance_transaction_id: ID of the balance transaction to retrieve
        
    Returns:
        Balance transaction object
    """
    return make_stripe_request("GET", f"/v1/balance_transactions/{balance_transaction_id}")


@mcp.tool()
def list_balance_transactions(limit: int = 10, created: str = None, type: str = None) -> dict:
    """List balance transactions.
    
    Args:
        limit: Number of transactions to return (default 10, max 100)
        created: Filter by creation timestamp
        type: Filter by transaction type
        
    Returns:
        List of balance transactions
    """
    params = {"limit": limit}
    
    if created:
        params["created"] = created
    if type:
        params["type"] = type
        
    return make_stripe_request("GET", "/v1/balance_transactions", params)


# ==================== Referral Program ====================

@mcp.tool()
def create_referral(referral_type: str, email: str = None, name: str = None, 
                   metadata: dict = None) -> dict:
    """Create a referral for the Stripe referral program.
    
    Args:
        referral_type: Type of referral (affiliate or influencer)
        email: Email address of the referee
        name: Name of the referee
        metadata: Key-value pairs for storing additional structured info
        
    Returns:
        Referral object
    """
    params = {"type": referral_type}
    
    if email:
        params["email"] = email
    if name:
        params["name"] = name
    if metadata:
        for key, value in metadata.items():
            params[f"metadata[{key}]"] = value
        
    return make_stripe_request("POST", "/v1/referrals", params)


# ==================== Run the server ====================

if __name__ == "__main__":
    mcp.run()
