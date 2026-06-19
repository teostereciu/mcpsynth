#!/usr/bin/env python3
"""
Stripe MCP Server - FastMCP implementation for Stripe API
"""

import os
import requests
from typing import Any, Dict, Optional
from fastmcp import FastMCP
from fastmcp.server import Context
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize FastMCP server
mcp = FastMCP(
    name="Stripe",
    version="1.0.0",
    description="Stripe API MCP Server for managing payments, customers, subscriptions, and more"
)

# Constants
STRIPE_API_KEY = os.getenv("STRIPE_API_KEY")
STRIPE_API_BASE = "https://api.stripe.com/v1"

# Helper functions
def make_stripe_request(
    method: str,
    endpoint: str,
    params: Optional[Dict[str, Any]] = None,
    context: Optional[Context] = None
) -> Dict[str, Any]:
    """Make an authenticated request to the Stripe API."""
    url = f"{STRIPE_API_BASE}{endpoint}"
    headers = {
        "Authorization": f"Bearer {STRIPE_API_KEY}",
        "Stripe-Version": "2024-12-18.acacia"
    }
    
    try:
        if method.upper() == "GET":
            response = requests.get(url, headers=headers, params=params or {})
        elif method.upper() == "POST":
            response = requests.post(url, headers=headers, data=params or {})
        elif method.upper() == "PUT":
            response = requests.put(url, headers=headers, data=params or {})
        elif method.upper() == "DELETE":
            response = requests.delete(url, headers=headers, params=params or {})
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
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


# ====================
# Charge Operations
# ====================

@mcp.tool()
async def create_charge(
    amount: int,
    currency: str,
    source: str,
    customer: Optional[str] = None,
    description: Optional[str] = None,
    receipt_email: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    context: Context = None
) -> Dict[str, Any]:
    """Create a new charge to collect payment."""
    params = {"amount": amount, "currency": currency, "source": source}
    if customer: params["customer"] = customer
    if description: params["description"] = description
    if receipt_email: params["receipt_email"] = receipt_email
    if metadata:
        for k, v in metadata.items():
            params[f"metadata[{k}]"] = v
    return make_stripe_request("POST", "/charges", params, context)


@mcp.tool()
async def retrieve_charge(charge_id: str, context: Context = None) -> Dict[str, Any]:
    """Retrieve details of a specific charge."""
    return make_stripe_request("GET", f"/charges/{charge_id}", context=context)


@mcp.tool()
async def update_charge(
    charge_id: str,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    context: Context = None
) -> Dict[str, Any]:
    """Update a charge's metadata and description."""
    params = {}
    if description: params["description"] = description
    if metadata:
        for k, v in metadata.items():
            params[f"metadata[{k}]"] = v
    return make_stripe_request("POST", f"/charges/{charge_id}", params, context)


@mcp.tool()
async def list_charges(
    customer: Optional[str] = None,
    limit: int = 10,
    starting_after: Optional[str] = None,
    context: Context = None
) -> Dict[str, Any]:
    """List charges with optional filtering."""
    params = {"limit": limit}
    if customer: params["customer"] = customer
    if starting_after: params["starting_after"] = starting_after
    return make_stripe_request("GET", "/charges", params, context)


# ====================
# Refund Operations
# ====================

@mcp.tool()
async def create_refund(
    charge: Optional[str] = None,
    payment_intent: Optional[str] = None,
    amount: Optional[int] = None,
    reason: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    context: Context = None
) -> Dict[str, Any]:
    """Create a refund for a charge or payment intent."""
    if not charge and not payment_intent:
        return {"error": "Either charge or payment_intent must be provided"}
    params = {}
    if charge: params["charge"] = charge
    if payment_intent: params["payment_intent"] = payment_intent
    if amount: params["amount"] = amount
    if reason: params["reason"] = reason
    if metadata:
        for k, v in metadata.items():
            params[f"metadata[{k}]"] = v
    return make_stripe_request("POST", "/refunds", params, context)


@mcp.tool()
async def retrieve_refund(refund_id: str, context: Context = None) -> Dict[str, Any]:
    """Retrieve details of a specific refund."""
    return make_stripe_request("GET", f"/refunds/{refund_id}", context=context)


@mcp.tool()
async def update_refund(
    refund_id: str,
    metadata: Optional[Dict[str, str]] = None,
    context: Context = None
) -> Dict[str, Any]:
    """Update a refund's metadata."""
    params = {}
    if metadata:
        for k, v in metadata.items():
            params[f"metadata[{k}]"] = v
    return make_stripe_request("POST", f"/refunds/{refund_id}", params, context)


@mcp.tool()
async def list_refunds(
    charge: Optional[str] = None,
    payment_intent: Optional[str] = None,
    limit: int = 10,
    context: Context = None
) -> Dict[str, Any]:
    """List refunds with optional filtering."""
    params = {"limit": limit}
    if charge: params["charge"] = charge
    if payment_intent: params["payment_intent"] = payment_intent
    return make_stripe_request("GET", "/refunds", params, context)


# ====================
# Customer Operations
# ====================

@mcp.tool()
async def create_customer(
    email: Optional[str] = None,
    name: Optional[str] = None,
    description: Optional[str] = None,
    payment_method: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    context: Context = None
) -> Dict[str, Any]:
    """Create a new customer."""
    params = {}
    if email: params["email"] = email
    if name: params["name"] = name
    if description: params["description"] = description
    if payment_method: params["payment_method"] = payment_method
    if metadata:
        for k, v in metadata.items():
            params[f"metadata[{k}]"] = v
    return make_stripe_request("POST", "/customers", params, context)


@mcp.tool()
async def retrieve_customer(customer_id: str, context: Context = None) -> Dict[str, Any]:
    """Retrieve details of a specific customer."""
    return make_stripe_request("GET", f"/customers/{customer_id}", context=context)


@mcp.tool()
async def update_customer(
    customer_id: str,
    email: Optional[str] = None,
    name: Optional[str] = None,
    description: Optional[str] = None,
    payment_method: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    context: Context = None
) -> Dict[str, Any]:
    """Update a customer's information."""
    params = {}
    if email: params["email"] = email
    if name: params["name"] = name
    if description: params["description"] = description
    if payment_method: params["payment_method"] = payment_method
    if metadata:
        for k, v in metadata.items():
            params[f"metadata[{k}]"] = v
    return make_stripe_request("POST", f"/customers/{customer_id}", params, context)


@mcp.tool()
async def delete_customer(customer_id: str, context: Context = None) -> Dict[str, Any]:
    """Delete a customer."""
    return make_stripe_request("DELETE", f"/customers/{customer_id}", context=context)


@mcp.tool()
async def list_customers(
    limit: int = 10,
    starting_after: Optional[str] = None,
    context: Context = None
) -> Dict[str, Any]:
    """List customers."""
    params = {"limit": limit}
    if starting_after: params["starting_after"] = starting_after
    return make_stripe_request("GET", "/customers", params, context)


# ====================
# Subscription Operations
# ====================

@mcp.tool()
async def create_subscription(
    customer: str,
    items: list,
    payment_behavior: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    context: Context = None
) -> Dict[str, Any]:
    """Create a new subscription for a customer."""
    params = {"customer": customer, "items": items}
    if payment_behavior: params["payment_behavior"] = payment_behavior
    if metadata:
        for k, v in metadata.items():
            params[f"metadata[{k}]"] = v
    return make_stripe_request("POST", "/subscriptions", params, context)


@mcp.tool()
async def retrieve_subscription(subscription_id: str, context: Context = None) -> Dict[str, Any]:
    """Retrieve details of a specific subscription."""
    return make_stripe_request("GET", f"/subscriptions/{subscription_id}", context=context)


@mcp.tool()
async def update_subscription(
    subscription_id: str,
    items: Optional[list] = None,
    metadata: Optional[Dict[str, str]] = None,
    context: Context = None
) -> Dict[str, Any]:
    """Update a subscription's items or metadata."""
    params = {}
    if items: params["items"] = items
    if metadata:
        for k, v in metadata.items():
            params[f"metadata[{k}]"] = v
    return make_stripe_request("POST", f"/subscriptions/{subscription_id}", params, context)


@mcp.tool()
async def cancel_subscription(
    subscription_id: str,
    at_period_end: Optional[bool] = None,
    context: Context = None
) -> Dict[str, Any]:
    """Cancel a subscription."""
    params = {}
    if at_period_end: params["cancel_at_period_end"] = at_period_end
    return make_stripe_request("DELETE", f"/subscriptions/{subscription_id}", params, context)


@mcp.tool()
async def list_subscriptions(
    customer: Optional[str] = None,
    status: Optional[str] = None,
    limit: int = 10,
    context: Context = None
) -> Dict[str, Any]:
    """List subscriptions with optional filtering."""
    params = {"limit": limit}
    if customer: params["customer"] = customer
    if status: params["status"] = status
    return make_stripe_request("GET", "/subscriptions", params, context)


# ====================
# Invoice Operations
# ====================

@mcp.tool()
async def create_invoice(
    customer: str,
    collection_method: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    context: Context = None
) -> Dict[str, Any]:
    """Create a new invoice."""
    params = {"customer": customer}
    if collection_method: params["collection_method"] = collection_method
    if metadata:
        for k, v in metadata.items():
            params[f"metadata[{k}]"] = v
    return make_stripe_request("POST", "/invoices", params, context)


@mcp.tool()
async def retrieve_invoice(invoice_id: str, context: Context = None) -> Dict[str, Any]:
    """Retrieve details of a specific invoice."""
    return make_stripe_request("GET", f"/invoices/{invoice_id}", context=context)


@mcp.tool()
async def update_invoice(
    invoice_id: str,
    metadata: Optional[Dict[str, str]] = None,
    context: Context = None
) -> Dict[str, Any]:
    """Update an invoice's metadata."""
    params = {}
    if metadata:
        for k, v in metadata.items():
            params[f"metadata[{k}]"] = v
    return make_stripe_request("POST", f"/invoices/{invoice_id}", params, context)


@mcp.tool()
async def pay_invoice(invoice_id: str, context: Context = None) -> Dict[str, Any]:
    """Pay an invoice."""
    return make_stripe_request("POST", f"/invoices/{invoice_id}/pay", context=context)


@mcp.tool()
async def list_invoices(
    customer: Optional[str] = None,
    status: Optional[str] = None,
    limit: int = 10,
    context: Context = None
) -> Dict[str, Any]:
    """List invoices with optional filtering."""
    params = {"limit": limit}
    if customer: params["customer"] = customer
    if status: params["status"] = status
    return make_stripe_request("GET", "/invoices", params, context)


# ====================
# Payment Intent Operations
# ====================

@mcp.tool()
async def create_payment_intent(
    amount: int,
    currency: str,
    confirm: Optional[bool] = None,
    customer: Optional[str] = None,
    payment_method: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    context: Context = None
) -> Dict[str, Any]:
    """Create a new PaymentIntent."""
    params = {"amount": amount, "currency": currency}
    if confirm: params["confirm"] = confirm
    if customer: params["customer"] = customer
    if payment_method: params["payment_method"] = payment_method
    if description: params["description"] = description
    if metadata:
        for k, v in metadata.items():
            params[f"metadata[{k}]"] = v
    return make_stripe_request("POST", "/payment_intents", params, context)


@mcp.tool()
async def retrieve_payment_intent(payment_intent_id: str, context: Context = None) -> Dict[str, Any]:
    """Retrieve details of a specific PaymentIntent."""
    return make_stripe_request("GET", f"/payment_intents/{payment_intent_id}", context=context)


@mcp.tool()
async def update_payment_intent(
    payment_intent_id: str,
    metadata: Optional[Dict[str, str]] = None,
    description: Optional[str] = None,
    context: Context = None
) -> Dict[str, Any]:
    """Update a PaymentIntent's metadata and description."""
    params = {}
    if metadata:
        for k, v in metadata.items():
            params[f"metadata[{k}]"] = v
    if description: params["description"] = description
    return make_stripe_request("POST", f"/payment_intents/{payment_intent_id}", params, context)


@mcp.tool()
async def confirm_payment_intent(
    payment_intent_id: str,
    payment_method: Optional[str] = None,
    context: Context = None
) -> Dict[str, Any]:
    """Confirm a PaymentIntent."""
    params = {}
    if payment_method: params["payment_method"] = payment_method
    return make_stripe_request("POST", f"/payment_intents/{payment_intent_id}/confirm", params, context)


@mcp.tool()
async def cancel_payment_intent(
    payment_intent_id: str,
    reason: Optional[str] = None,
    context: Context = None
) -> Dict[str, Any]:
    """Cancel a PaymentIntent."""
    params = {}
    if reason: params["cancellation_reason"] = reason
    return make_stripe_request("POST", f"/payment_intents/{payment_intent_id}/cancel", params, context)


@mcp.tool()
async def list_payment_intents(
    customer: Optional[str] = None,
    limit: int = 10,
    context: Context = None
) -> Dict[str, Any]:
    """List PaymentIntents with optional filtering."""
    params = {"limit": limit}
    if customer: params["customer"] = customer
    return make_stripe_request("GET", "/payment_intents", params, context)


# ====================
# Payment Method Operations
# ====================

@mcp.tool()
async def create_payment_method(
    type: str,
    billing_details: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, str]] = None,
    context: Context = None
) -> Dict[str, Any]:
    """Create a new PaymentMethod."""
    params = {"type": type}
    if billing_details:
        for k, v in billing_details.items():
            params[f"billing_details[{k}]"] = v
    if metadata:
        for k, v in metadata.items():
            params[f"metadata[{k}]"] = v
    return make_stripe_request("POST", "/payment_methods", params, context)


@mcp.tool()
async def retrieve_payment_method(payment_method_id: str, context: Context = None) -> Dict[str, Any]:
    """Retrieve details of a specific PaymentMethod."""
    return make_stripe_request("GET", f"/payment_methods/{payment_method_id}", context=context)


@mcp.tool()
async def update_payment_method(
    payment_method_id: str,
    billing_details: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, str]] = None,
    context: Context = None
) -> Dict[str, Any]:
    """Update a PaymentMethod's billing details and metadata."""
    params = {}
    if billing_details:
        for k, v in billing_details.items():
            params[f"billing_details[{k}]"] = v
    if metadata:
        for k, v in metadata.items():
            params[f"metadata[{k}]"] = v
    return make_stripe_request("POST", f"/payment_methods/{payment_method_id}", params, context)


@mcp.tool()
async def attach_payment_method(
    payment_method_id: str,
    customer: str,
    context: Context = None
) -> Dict[str, Any]:
    """Attach a PaymentMethod to a Customer."""
    params = {"customer": customer}
    return make_stripe_request("POST", f"/payment_methods/{payment_method_id}/attach", params, context)


@mcp.tool()
async def detach_payment_method(
    payment_method_id: str,
    context: Context = None
) -> Dict[str, Any]:
    """Detach a PaymentMethod from a Customer."""
    return make_stripe_request("POST", f"/payment_methods/{payment_method_id}/detach", context=context)


@mcp.tool()
async def list_payment_methods(
    customer: str,
    type: Optional[str] = None,
    limit: int = 10,
    context: Context = None
) -> Dict[str, Any]:
    """List PaymentMethods for a Customer."""
    params = {"customer": customer, "limit": limit}
    if type: params["type"] = type
    return make_stripe_request("GET", "/payment_methods", params, context)


# ====================
# Product Operations
# ====================

@mcp.tool()
async def create_product(
    name: str,
    active: Optional[bool] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    context: Context = None
) -> Dict[str, Any]:
    """Create a new Product."""
    params = {"name": name}
    if active is not None: params["active"] = active
    if description: params["description"] = description
    if metadata:
        for k, v in metadata.items():
            params[f"metadata[{k}]"] = v
    return make_stripe_request("POST", "/products", params, context)


@mcp.tool()
async def retrieve_product(product_id: str, context: Context = None) -> Dict[str, Any]:
    """Retrieve details of a specific Product."""
    return make_stripe_request("GET", f"/products/{product_id}", context=context)


@mcp.tool()
async def update_product(
    product_id: str,
    name: Optional[str] = None,
    active: Optional[bool] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    context: Context = None
) -> Dict[str, Any]:
    """Update a Product's information."""
    params = {}
    if name: params["name"] = name
    if active is not None: params["active"] = active
    if description: params["description"] = description
    if metadata:
        for k, v in metadata.items():
            params[f"metadata[{k}]"] = v
    return make_stripe_request("POST", f"/products/{product_id}", params, context)


@mcp.tool()
async def delete_product(product_id: str, context: Context = None) -> Dict[str, Any]:
    """Delete a Product."""
    return make_stripe_request("DELETE", f"/products/{product_id}", context=context)


@mcp.tool()
async def list_products(
    active: Optional[bool] = None,
    limit: int = 10,
    context: Context = None
) -> Dict[str, Any]:
    """List Products with optional filtering."""
    params = {"limit": limit}
    if active is not None: params["active"] = active
    return make_stripe_request("GET", "/products", params, context)


# ====================
# Price Operations
# ====================

@mcp.tool()
async def create_price(
    currency: str,
    unit_amount: int,
    product: Optional[str] = None,
    recurring: Optional[Dict[str, Any]] = None,
    tax_behavior: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    context: Context = None
) -> Dict[str, Any]:
    """Create a new Price for a Product."""
    params = {"currency": currency, "unit_amount": unit_amount}
    if product: params["product"] = product
    if recurring:
        for k, v in recurring.items():
            params[f"recurring[{k}]"] = v
    if tax_behavior: params["tax_behavior"] = tax_behavior
    if metadata:
        for k, v in metadata.items():
            params[f"metadata[{k}]"] = v
    return make_stripe_request("POST", "/prices", params, context)


@mcp.tool()
async def retrieve_price(price_id: str, context: Context = None) -> Dict[str, Any]:
    """Retrieve details of a specific Price."""
    return make_stripe_request("GET", f"/prices/{price_id}", context=context)


@mcp.tool()
async def update_price(
    price_id: str,
    metadata: Optional[Dict[str, str]] = None,
    context: Context = None
) -> Dict[str, Any]:
    """Update a Price's metadata."""
    params = {}
    if metadata:
        for k, v in metadata.items():
            params[f"metadata[{k}]"] = v
    return make_stripe_request("POST", f"/prices/{price_id}", params, context)


@mcp.tool()
async def list_prices(
    product: Optional[str] = None,
    active: Optional[bool] = None,
    limit: int = 10,
    context: Context = None
) -> Dict[str, Any]:
    """List Prices with optional filtering."""
    params = {"limit": limit}
    if product: params["product"] = product
    if active is not None: params["active"] = active
    return make_stripe_request("GET", "/prices", params, context)


# ====================
# Coupon Operations
# ====================

@mcp.tool()
async def create_coupon(
    duration: str,
    percent_off: Optional[float] = None,
    amount_off: Optional[int] = None,
    currency: Optional[str] = None,
    name: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    context: Context = None
) -> Dict[str, Any]:
    """Create a new Coupon."""
    params = {"duration": duration}
    if percent_off is not None: params["percent_off"] = percent_off
    if amount_off is not None: params["amount_off"] = amount_off
    if currency: params["currency"] = currency
    if name: params["name"] = name
    if metadata:
        for k, v in metadata.items():
            params[f"metadata[{k}]"] = v
    return make_stripe_request("POST", "/coupons", params, context)


@mcp.tool()
async def retrieve_coupon(coupon_id: str, context: Context = None) -> Dict[str, Any]:
    """Retrieve details of a specific Coupon."""
    return make_stripe_request("GET", f"/coupons/{coupon_id}", context=context)


@mcp.tool()
async def update_coupon(
    coupon_id: str,
    metadata: Optional[Dict[str, str]] = None,
    name: Optional[str] = None,
    context: Context = None
) -> Dict[str, Any]:
    """Update a Coupon's metadata and name."""
    params = {}
    if metadata:
        for k, v in metadata.items():
            params[f"metadata[{k}]"] = v
    if name: params["name"] = name
    return make_stripe_request("POST", f"/coupons/{coupon_id}", params, context)


@mcp.tool()
async def list_coupons(
    limit: int = 10,
    context: Context = None
) -> Dict[str, Any]:
    """List Coupons."""
    params = {"limit": limit}
    return make_stripe_request("GET", "/coupons", params, context)


# ====================
# Promotion Code Operations
# ====================

@mcp.tool()
async def create_promotion_code(
    promotion: Dict[str, Any],
    code: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    context: Context = None
) -> Dict[str, Any]:
    """Create a new PromotionCode."""
    params = {"promotion[type]": promotion.get("type"), "promotion[coupon]": promotion.get("coupon")}
    if code: params["code"] = code
    if metadata:
        for k, v in metadata.items():
            params[f"metadata[{k}]"] = v
    return make_stripe_request("POST", "/promotion_codes", params, context)


@mcp.tool()
async def retrieve_promotion_code(promotion_code_id: str, context: Context = None) -> Dict[str, Any]:
    """Retrieve details of a specific PromotionCode."""
    return make_stripe_request("GET", f"/promotion_codes/{promotion_code_id}", context=context)


@mcp.tool()
async def update_promotion_code(
    promotion_code_id: str,
    metadata: Optional[Dict[str, str]] = None,
    context: Context = None
) -> Dict[str, Any]:
    """Update a PromotionCode's metadata."""
    params = {}
    if metadata:
        for k, v in metadata.items():
            params[f"metadata[{k}]"] = v
    return make_stripe_request("POST", f"/promotion_codes/{promotion_code_id}", params, context)


@mcp.tool()
async def list_promotion_codes(
    active: Optional[bool] = None,
    limit: int = 10,
    context: Context = None
) -> Dict[str, Any]:
    """List PromotionCodes with optional filtering."""
    params = {"limit": limit}
    if active is not None: params["active"] = active
    return make_stripe_request("GET", "/promotion_codes", params, context)


# ====================
# Dispute Operations
# ====================

@mcp.tool()
async def retrieve_dispute(dispute_id: str, context: Context = None) -> Dict[str, Any]:
    """Retrieve details of a specific dispute."""
    return make_stripe_request("GET", f"/disputes/{dispute_id}", context=context)


@mcp.tool()
async def update_dispute(
    dispute_id: str,
    evidence: Optional[Dict[str, str]] = None,
    metadata: Optional[Dict[str, str]] = None,
    submit: Optional[bool] = None,
    context: Context = None
) -> Dict[str, Any]:
    """Update a dispute with evidence."""
    params = {}
    if evidence:
        for k, v in evidence.items():
            params[f"evidence[{k}]"] = v
    if metadata:
        for k, v in metadata.items():
            params[f"metadata[{k}]"] = v
    if submit is not None: params["submit"] = submit
    return make_stripe_request("POST", f"/disputes/{dispute_id}", params, context)


@mcp.tool()
async def list_disputes(
    charge: Optional[str] = None,
    status: Optional[str] = None,
    limit: int = 10,
    context: Context = None
) -> Dict[str, Any]:
    """List disputes with optional filtering."""
    params = {"limit": limit}
    if charge: params["charge"] = charge
    if status: params["status"] = status
    return make_stripe_request("GET", "/disputes", params, context)


# ====================
# Transfer Operations
# ====================

@mcp.tool()
async def create_transfer(
    amount: int,
    currency: str,
    destination: str,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    context: Context = None
) -> Dict[str, Any]:
    """Create a new transfer to a connected account."""
    params = {"amount": amount, "currency": currency, "destination": destination}
    if description: params["description"] = description
    if metadata:
        for k, v in metadata.items():
            params[f"metadata[{k}]"] = v
    return make_stripe_request("POST", "/transfers", params, context)


@mcp.tool()
async def retrieve_transfer(transfer_id: str, context: Context = None) -> Dict[str, Any]:
    """Retrieve details of a specific transfer."""
    return make_stripe_request("GET", f"/transfers/{transfer_id}", context=context)


@mcp.tool()
async def update_transfer(
    transfer_id: str,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    context: Context = None
) -> Dict[str, Any]:
    """Update a transfer's description and metadata."""
    params = {}
    if description: params["description"] = description
    if metadata:
        for k, v in metadata.items():
            params[f"metadata[{k}]"] = v
    return make_stripe_request("POST", f"/transfers/{transfer_id}", params, context)


@mcp.tool()
async def list_transfers(
    limit: int = 10,
    context: Context = None
) -> Dict[str, Any]:
    """List transfers."""
    params = {"limit": limit}
    return make_stripe_request("GET", "/transfers", params, context)


# ====================
# Payout Operations
# ====================

@mcp.tool()
async def create_payout(
    amount: int,
    currency: str,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    statement_descriptor: Optional[str] = None,
    context: Context = None
) -> Dict[str, Any]:
    """Create a new payout to your bank account."""
    params = {"amount": amount, "currency": currency}
    if description: params["description"] = description
    if metadata:
        for k, v in metadata.items():
            params[f"metadata[{k}]"] = v
    if statement_descriptor: params["statement_descriptor"] = statement_descriptor
    return make_stripe_request("POST", "/payouts", params, context)


@mcp.tool()
async def retrieve_payout(payout_id: str, context: Context = None) -> Dict[str, Any]:
    """Retrieve details of a specific payout."""
    return make_stripe_request("GET", f"/payouts/{payout_id}", context=context)


@mcp.tool()
async def update_payout(
    payout_id: str,
    metadata: Optional[Dict[str, str]] = None,
    context: Context = None
) -> Dict[str, Any]:
    """Update a payout's metadata."""
    params = {}
    if metadata:
        for k, v in metadata.items():
            params[f"metadata[{k}]"] = v
    return make_stripe_request("POST", f"/payouts/{payout_id}", params, context)


@mcp.tool()
async def list_payouts(
    status: Optional[str] = None,
    limit: int = 10,
    context: Context = None
) -> Dict[str, Any]:
    """List payouts with optional filtering."""
    params = {"limit": limit}
    if status: params["status"] = status
    return make_stripe_request("GET", "/payouts", params, context)


# ====================
# Checkout Session Operations
# ====================

@mcp.tool()
async def create_checkout_session(
    mode: str,
    success_url: str,
    cancel_url: str,
    line_items: list,
    customer: Optional[str] = None,
    customer_email: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    context: Context = None
) -> Dict[str, Any]:
    """Create a new Checkout Session."""
    params = {
        "mode": mode, "success_url": success_url, "cancel_url": cancel_url,
        "line_items": line_items
    }
    if customer: params["customer"] = customer
    if customer_email: params["customer_email"] = customer_email
    if metadata:
        for k, v in metadata.items():
            params[f"metadata[{k}]"] = v
    return make_stripe_request("POST", "/checkout/sessions", params, context)


@mcp.tool()
async def retrieve_checkout_session(session_id: str, context: Context = None) -> Dict[str, Any]:
    """Retrieve details of a specific Checkout Session."""
    return make_stripe_request("GET", f"/checkout/sessions/{session_id}", context=context)


@mcp.tool()
async def list_checkout_sessions(
    limit: int = 10,
    context: Context = None
) -> Dict[str, Any]:
    """List Checkout Sessions."""
    params = {"limit": limit}
    return make_stripe_request("GET", "/checkout/sessions", params, context)


# ====================
# Account Operations
# ====================

@mcp.tool()
async def create_account(
    country: str,
    email: Optional[str] = None,
    type: Optional[str] = None,
    controller: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, str]] = None,
    context: Context = None
) -> Dict[str, Any]:
    """Create a new Stripe account (Connect)."""
    params = {"country": country}
    if email: params["email"] = email
    if type: params["type"] = type
    if controller:
        for k, v in controller.items():
            params[f"controller[{k}]"] = v
    if metadata:
        for k, v in metadata.items():
            params[f"metadata[{k}]"] = v
    return make_stripe_request("POST", "/accounts", params, context)


@mcp.tool()
async def retrieve_account(account_id: str, context: Context = None) -> Dict[str, Any]:
    """Retrieve details of a specific account."""
    return make_stripe_request("GET", f"/accounts/{account_id}", context=context)


@mcp.tool()
async def update_account(
    account_id: str,
    metadata: Optional[Dict[str, str]] = None,
    context: Context = None
) -> Dict[str, Any]:
    """Update an account's metadata."""
    params = {}
    if metadata:
        for k, v in metadata.items():
            params[f"metadata[{k}]"] = v
    return make_stripe_request("POST", f"/accounts/{account_id}", params, context)


@mcp.tool()
async def list_accounts(
    limit: int = 10,
    context: Context = None
) -> Dict[str, Any]:
    """List connected accounts."""
    params = {"limit": limit}
    return make_stripe_request("GET", "/accounts", params, context)


# ====================
# Setup Intent Operations
# ====================

@mcp.tool()
async def create_setup_intent(
    automatic_payment_methods: Optional[Dict[str, Any]] = None,
    confirm: Optional[bool] = None,
    customer: Optional[str] = None,
    customer_account: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    payment_method: Optional[str] = None,
    usage: Optional[str] = None,
    context: Context = None
) -> Dict[str, Any]:
    """Create a new SetupIntent."""
    params = {}
    if automatic_payment_methods:
        for k, v in automatic_payment_methods.items():
            params[f"automatic_payment_methods[{k}]"] = v
    if confirm: params["confirm"] = confirm
    if customer: params["customer"] = customer
    if customer_account: params["customer_account"] = customer_account
    if description: params["description"] = description
    if metadata:
        for k, v in metadata.items():
            params[f"metadata[{k}]"] = v
    if payment_method: params["payment_method"] = payment_method
    if usage: params["usage"] = usage
    return make_stripe_request("POST", "/setup_intents", params, context)


@mcp.tool()
async def retrieve_setup_intent(setup_intent_id: str, context: Context = None) -> Dict[str, Any]:
    """Retrieve details of a specific SetupIntent."""
    return make_stripe_request("GET", f"/setup_intents/{setup_intent_id}", context=context)


@mcp.tool()
async def update_setup_intent(
    setup_intent_id: str,
    customer: Optional[str] = None,
    customer_account: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    payment_method: Optional[str] = None,
    context: Context = None
) -> Dict[str, Any]:
    """Update a SetupIntent's information."""
    params = {}
    if customer: params["customer"] = customer
    if customer_account: params["customer_account"] = customer_account
    if description: params["description"] = description
    if metadata:
        for k, v in metadata.items():
            params[f"metadata[{k}]"] = v
    if payment_method: params["payment_method"] = payment_method
    return make_stripe_request("POST", f"/setup_intents/{setup_intent_id}", params, context)


@mcp.tool()
async def list_setup_intents(
    customer: Optional[str] = None,
    limit: int = 10,
    context: Context = None
) -> Dict[str, Any]:
    """List SetupIntents with optional filtering."""
    params = {"limit": limit}
    if customer: params["customer"] = customer
    return make_stripe_request("GET", "/setup_intents", params, context)


# ====================
# Card Operations
# ====================

@mcp.tool()
async def create_card(
    customer: str,
    card: Dict[str, Any],
    metadata: Optional[Dict[str, str]] = None,
    context: Context = None
) -> Dict[str, Any]:
    """Create a new Card for a Customer."""
    params = {"customer": customer}
    if card:
        for k, v in card.items():
            params[f"card[{k}]"] = v
    if metadata:
        for k, v in metadata.items():
            params[f"metadata[{k}]"] = v
    return make_stripe_request("POST", "/cards", params, context)


@mcp.tool()
async def retrieve_card(customer_id: str, card_id: str, context: Context = None) -> Dict[str, Any]:
    """Retrieve details of a specific Card."""
    return make_stripe_request("GET", f"/customers/{customer_id}/cards/{card_id}", context=context)


@mcp.tool()
async def update_card(
    customer_id: str,
    card_id: str,
    metadata: Optional[Dict[str, str]] = None,
    name: Optional[str] = None,
    address: Optional[Dict[str, Any]] = None,
    context: Context = None
) -> Dict[str, Any]:
    """Update a Card's information."""
    params = {}
    if metadata:
        for k, v in metadata.items():
            params[f"metadata[{k}]"] = v
    if name: params["name"] = name
    if address:
        for k, v in address.items():
            params[f"address[{k}]"] = v
    return make_stripe_request("POST", f"/customers/{customer_id}/cards/{card_id}", params, context)


@mcp.tool()
async def delete_card(customer_id: str, card_id: str, context: Context = None) -> Dict[str, Any]:
    """Delete a Card."""
    return make_stripe_request("DELETE", f"/customers/{customer_id}/cards/{card_id}", context=context)


@mcp.tool()
async def list_cards(
    customer_id: str,
    limit: int = 10,
    context: Context = None
) -> Dict[str, Any]:
    """List Cards for a Customer."""
    params = {"limit": limit}
    return make_stripe_request("GET", f"/customers/{customer_id}/cards", params, context)


# ====================
# Bank Account Operations
# ====================

@mcp.tool()
async def create_bank_account(
    customer: str,
    bank_account: Dict[str, Any],
    metadata: Optional[Dict[str, str]] = None,
    context: Context = None
) -> Dict[str, Any]:
    """Create a new BankAccount for a Customer."""
    params = {"customer": customer}
    if bank_account:
        for k, v in bank_account.items():
            params[f"bank_account[{k}]"] = v
    if metadata:
        for k, v in metadata.items():
            params[f"metadata[{k}]"] = v
    return make_stripe_request("POST", "/customers/" + customer + "/external_accounts", params, context)


@mcp.tool()
async def retrieve_bank_account(customer_id: str, bank_account_id: str, context: Context = None) -> Dict[str, Any]:
    """Retrieve details of a specific BankAccount."""
    return make_stripe_request("GET", f"/customers/{customer_id}/external_accounts/{bank_account_id}", context=context)


@mcp.tool()
async def update_bank_account(
    customer_id: str,
    bank_account_id: str,
    metadata: Optional[Dict[str, str]] = None,
    name: Optional[str] = None,
    address: Optional[Dict[str, Any]] = None,
    context: Context = None
) -> Dict[str, Any]:
    """Update a BankAccount's information."""
    params = {}
    if metadata:
        for k, v in metadata.items():
            params[f"metadata[{k}]"] = v
    if name: params["name"] = name
    if address:
        for k, v in address.items():
            params[f"address[{k}]"] = v
    return make_stripe_request("POST", f"/customers/{customer_id}/external_accounts/{bank_account_id}", params, context)


@mcp.tool()
async def delete_bank_account(customer_id: str, bank_account_id: str, context: Context = None) -> Dict[str, Any]:
    """Delete a BankAccount."""
    return make_stripe_request("DELETE", f"/customers/{customer_id}/external_accounts/{bank_account_id}", context=context)


@mcp.tool()
async def list_bank_accounts(
    customer_id: str,
    limit: int = 10,
    context: Context = None
) -> Dict[str, Any]:
    """List BankAccounts for a Customer."""
    params = {"limit": limit}
    return make_stripe_request("GET", f"/customers/{customer_id}/external_accounts", params, context)


# ====================
# Balance Operations
# ====================

@mcp.tool()
async def retrieve_balance(context: Context = None) -> Dict[str, Any]:
    """Retrieve your Stripe account's current balance."""
    return make_stripe_request("GET", "/balance", context=context)


@mcp.tool()
async def retrieve_balance_transaction(transaction_id: str, context: Context = None) -> Dict[str, Any]:
    """Retrieve details of a specific balance transaction."""
    return make_stripe_request("GET", f"/balance_transactions/{transaction_id}", context=context)


@mcp.tool()
async def list_balance_transactions(
    limit: int = 10,
    starting_after: Optional[str] = None,
    context: Context = None
) -> Dict[str, Any]:
    """List balance transactions."""
    params = {"limit": limit}
    if starting_after: params["starting_after"] = starting_after
    return make_stripe_request("GET", "/balance_transactions", params, context)


# ====================
# Application Fee Operations
# ====================

@mcp.tool()
async def retrieve_application_fee(fee_id: str, context: Context = None) -> Dict[str, Any]:
    """Retrieve details of a specific application fee."""
    return make_stripe_request("GET", f"/application_fees/{fee_id}", context=context)


@mcp.tool()
async def list_application_fees(
    limit: int = 10,
    context: Context = None
) -> Dict[str, Any]:
    """List application fees."""
    params = {"limit": limit}
    return make_stripe_request("GET", "/application_fees", params, context)


# ====================
# Fee Refund Operations
# ====================

@mcp.tool()
async def create_fee_refund(
    fee: str,
    amount: Optional[int] = None,
    metadata: Optional[Dict[str, str]] = None,
    context: Context = None
) -> Dict[str, Any]:
    """Create a new fee refund."""
    params = {"fee": fee}
    if amount: params["amount"] = amount
    if metadata:
        for k, v in metadata.items():
            params[f"metadata[{k}]"] = v
    return make_stripe_request("POST", "/application_fees/" + fee + "/refunds", params, context)


@mcp.tool()
async def retrieve_fee_refund(fee_id: str, refund_id: str, context: Context = None) -> Dict[str, Any]:
    """Retrieve details of a specific fee refund."""
    return make_stripe_request("GET", f"/application_fees/{fee_id}/refunds/{refund_id}", context=context)


@mcp.tool()
async def update_fee_refund(
    fee_id: str,
    refund_id: str,
    metadata: Optional[Dict[str, str]] = None,
    context: Context = None
) -> Dict[str, Any]:
    """Update a fee refund's metadata."""
    params = {}
    if metadata:
        for k, v in metadata.items():
            params[f"metadata[{k}]"] = v
    return make_stripe_request("POST", f"/application_fees/{fee_id}/refunds/{refund_id}", params, context)


@mcp.tool()
async def list_fee_refunds(
    fee: str,
    limit: int = 10,
    context: Context = None
) -> Dict[str, Any]:
    """List fee refunds for an application fee."""
    params = {"limit": limit}
    return make_stripe_request("GET", f"/application_fees/{fee}/refunds", params, context)


# ====================
# Account Link Operations
# ====================

@mcp.tool()
async def create_account_link(
    account: str,
    type: str,
    refresh_url: str,
    return_url: str,
    context: Context = None
) -> Dict[str, Any]:
    """Create an AccountLink for Connect onboarding."""
    params = {
        "account": account,
        "type": type,
        "refresh_url": refresh_url,
        "return_url": return_url
    }
    return make_stripe_request("POST", "/account_links", params, context)


# ====================
# Webhook Endpoint Operations
# ====================

@mcp.tool()
async def create_webhook_endpoint(
    url: str,
    enabled_events: list,
    api_version: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    context: Context = None
) -> Dict[str, Any]:
    """Create a new webhook endpoint."""
    params = {"url": url, "enabled_events": enabled_events}
    if api_version: params["api_version"] = api_version
    if description: params["description"] = description
    if metadata:
        for k, v in metadata.items():
            params[f"metadata[{k}]"] = v
    return make_stripe_request("POST", "/webhook_endpoints", params, context)


@mcp.tool()
async def retrieve_webhook_endpoint(webhook_id: str, context: Context = None) -> Dict[str, Any]:
    """Retrieve details of a specific webhook endpoint."""
    return make_stripe_request("GET", f"/webhook_endpoints/{webhook_id}", context=context)


@mcp.tool()
async def update_webhook_endpoint(
    webhook_id: str,
    description: Optional[str] = None,
    enabled_events: Optional[list] = None,
    url: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    context: Context = None
) -> Dict[str, Any]:
    """Update a webhook endpoint."""
    params = {}
    if description: params["description"] = description
    if enabled_events: params["enabled_events"] = enabled_events
    if url: params["url"] = url
    if metadata:
        for k, v in metadata.items():
            params[f"metadata[{k}]"] = v
    return make_stripe_request("POST", f"/webhook_endpoints/{webhook_id}", params, context)


@mcp.tool()
async def delete_webhook_endpoint(webhook_id: str, context: Context = None) -> Dict[str, Any]:
    """Delete a webhook endpoint."""
    return make_stripe_request("DELETE", f"/webhook_endpoints/{webhook_id}", context=context)


@mcp.tool()
async def list_webhook_endpoints(
    limit: int = 10,
    context: Context = None
) -> Dict[str, Any]:
    """List webhook endpoints."""
    params = {"limit": limit}
    return make_stripe_request("GET", "/webhook_endpoints", params, context)


# ====================
# Event Operations
# ====================

@mcp.tool()
async def retrieve_event(event_id: str, context: Context = None) -> Dict[str, Any]:
    """Retrieve details of a specific event."""
    return make_stripe_request("GET", f"/events/{event_id}", context=context)


@mcp.tool()
async def list_events(
    types: Optional[list] = None,
    limit: int = 10,
    context: Context = None
) -> Dict[str, Any]:
    """List events with optional filtering."""
    params = {"limit": limit}
    if types: params["types[]"] = types
    return make_stripe_request("GET", "/events", params, context)


# ====================
# Capability Operations
# ====================

@mcp.tool()
async def update_capability(
    account_id: str,
    capability_id: str,
    requested: bool,
    context: Context = None
) -> Dict[str, Any]:
    """Update an Account Capability."""
    params = {"requested": requested}
    return make_stripe_request("POST", f"/accounts/{account_id}/capabilities/{capability_id}", params, context)


@mcp.tool()
async def retrieve_capability(
    account_id: str,
    capability_id: str,
    context: Context = None
) -> Dict[str, Any]:
    """Retrieve details of a specific Account Capability."""
    return make_stripe_request("GET", f"/accounts/{account_id}/capabilities/{capability_id}", context=context)


@mcp.tool()
async def list_capabilities(
    account_id: str,
    limit: int = 10,
    context: Context = None
) -> Dict[str, Any]:
    """List capabilities for an account."""
    params = {"limit": limit}
    return make_stripe_request("GET", f"/accounts/{account_id}/capabilities", params, context)


# ====================
# Payment Method Configuration Operations
# ====================

@mcp.tool()
async def create_payment_method_configuration(
    display_name: str,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    context: Context = None
) -> Dict[str, Any]:
    """Create a new PaymentMethodConfiguration."""
    params = {"display_name": display_name}
    if description: params["description"] = description
    if metadata:
        for k, v in metadata.items():
            params[f"metadata[{k}]"] = v
    return make_stripe_request("POST", "/payment_method_configurations", params, context)


@mcp.tool()
async def retrieve_payment_method_configuration(
    configuration_id: str,
    context: Context = None
) -> Dict[str, Any]:
    """Retrieve details of a specific PaymentMethodConfiguration."""
    return make_stripe_request("GET", f"/payment_method_configurations/{configuration_id}", context=context)


@mcp.tool()
async def update_payment_method_configuration(
    configuration_id: str,
    display_name: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    context: Context = None
) -> Dict[str, Any]:
    """Update a PaymentMethodConfiguration's information."""
    params = {}
    if description: params["description"] = description
    if metadata:
        for k, v in metadata.items():
            params[f"metadata[{k}]"] = v
    return make_stripe_request("POST", f"/payment_method_configurations/{configuration_id}", params, context)


@mcp.tool()
async def list_payment_method_configurations(
    limit: int = 10,
    context: Context = None
) -> Dict[str, Any]:
    """List PaymentMethodConfigurations."""
    params = {"limit": limit}
    return make_stripe_request("GET", "/payment_method_configurations", params, context)


if __name__ == "__main__":
    import asyncio
    async def main():
        await mcp.run_stdio_async()
    asyncio.run(main())
