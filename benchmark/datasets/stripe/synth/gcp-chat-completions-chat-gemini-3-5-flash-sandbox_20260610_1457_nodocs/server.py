import os
import requests
from typing import Any, Dict, List, Optional
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("Stripe API")

BASE_URL = "https://api.stripe.com"

def stripe_encode(params: Any, prefix: str = "") -> Dict[str, str]:
    """
    Recursively encode nested dicts/lists into Stripe's form-encoded format.
    Returns a flat dict of key-value pairs.
    """
    flat = {}
    if isinstance(params, dict):
        for k, v in params.items():
            key = f"{prefix}[{k}]" if prefix else k
            flat.update(stripe_encode(v, key))
    elif isinstance(params, list):
        for i, v in enumerate(params):
            key = f"{prefix}[{i}]"
            flat.update(stripe_encode(v, key))
    elif params is True:
        flat[prefix] = "true"
    elif params is False:
        flat[prefix] = "false"
    elif params is None:
        flat[prefix] = ""
    else:
        flat[prefix] = str(params)
    return flat

def stripe_request(method: str, path: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Make a request to the Stripe API.
    Handles authentication, form-encoding, and error handling.
    """
    api_key = os.environ.get("STRIPE_API_KEY")
    if not api_key:
        return {"error": "STRIPE_API_KEY environment variable is not set."}

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    url = f"{BASE_URL}{path}"
    
    try:
        if method.upper() in ["POST", "PUT", "PATCH"]:
            data = stripe_encode(params) if params else {}
            response = requests.request(method, url, headers=headers, data=data)
        else:
            query_params = stripe_encode(params) if params else {}
            response = requests.request(method, url, headers=headers, params=query_params)

        try:
            res_json = response.json()
        except ValueError:
            return {"error": f"Invalid JSON response from Stripe: {response.text}"}

        if not response.ok:
            if isinstance(res_json, dict) and "error" in res_json:
                return {"error": res_json["error"]}
            return {"error": f"HTTP {response.status_code}: {response.text}"}

        return res_json

    except Exception as e:
        return {"error": f"Request failed: {str(e)}"}


# ==========================================
# 1. PAYMENT INTENTS
# ==========================================

@mcp.tool()
def create_payment_intent(
    amount: int,
    currency: str,
    payment_method_types: Optional[List[str]] = None,
    metadata: Optional[Dict[str, str]] = None,
    description: Optional[str] = None,
    receipt_email: Optional[str] = None,
    customer: Optional[str] = None,
    setup_future_usage: Optional[str] = None,
    statement_descriptor: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Create a PaymentIntent to track and guide a customer through the payment flow.
    
    Args:
        amount: Amount intended to be collected in the smallest currency unit (e.g., 1000 for $10.00).
        currency: Three-letter ISO currency code, in lowercase (e.g., usd, eur).
        payment_method_types: List of payment method types (e.g., ['card']).
        metadata: Set of key-value pairs for storing custom data.
        description: An arbitrary string attached to the object.
        receipt_email: Email address that the receipt for this charge will be sent to.
        customer: ID of the Customer this PaymentIntent is for, if one exists.
        setup_future_usage: Indicates how you intend to use the payment method (e.g., 'off_session', 'on_session').
        statement_descriptor: Text that appears on the customer's statement.
    """
    params = {
        "amount": amount,
        "currency": currency,
    }
    if payment_method_types is not None:
        params["payment_method_types"] = payment_method_types
    if metadata is not None:
        params["metadata"] = metadata
    if description is not None:
        params["description"] = description
    if receipt_email is not None:
        params["receipt_email"] = receipt_email
    if customer is not None:
        params["customer"] = customer
    if setup_future_usage is not None:
        params["setup_future_usage"] = setup_future_usage
    if statement_descriptor is not None:
        params["statement_descriptor"] = statement_descriptor

    return stripe_request("POST", "/v1/payment_intents", params)

@mcp.tool()
def retrieve_payment_intent(id: str) -> Dict[str, Any]:
    """
    Retrieve the details of an existing PaymentIntent.
    
    Args:
        id: The identifier of the PaymentIntent to retrieve.
    """
    return stripe_request("GET", f"/v1/payment_intents/{id}")

@mcp.tool()
def update_payment_intent(
    id: str,
    amount: Optional[int] = None,
    currency: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    description: Optional[str] = None,
    receipt_email: Optional[str] = None,
    customer: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Update properties on a PaymentIntent.
    
    Args:
        id: The identifier of the PaymentIntent to update.
        amount: Amount intended to be collected.
        currency: Three-letter ISO currency code.
        metadata: Set of key-value pairs for storing custom data.
        description: An arbitrary string attached to the object.
        receipt_email: Email address that the receipt for this charge will be sent to.
        customer: ID of the Customer this PaymentIntent is for.
    """
    params = {}
    if amount is not None:
        params["amount"] = amount
    if currency is not None:
        params["currency"] = currency
    if metadata is not None:
        params["metadata"] = metadata
    if description is not None:
        params["description"] = description
    if receipt_email is not None:
        params["receipt_email"] = receipt_email
    if customer is not None:
        params["customer"] = customer

    return stripe_request("POST", f"/v1/payment_intents/{id}", params)

@mcp.tool()
def confirm_payment_intent(
    id: str,
    payment_method: Optional[str] = None,
    receipt_email: Optional[str] = None,
    return_url: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Confirm that the customer intends to pay with the presented payment method.
    
    Args:
        id: The identifier of the PaymentIntent to confirm.
        payment_method: ID of the payment method to associate with this PaymentIntent.
        receipt_email: Email address that the receipt for this charge will be sent to.
        return_url: The URL to redirect your customer back to after they authenticate or complete the payment.
    """
    params = {}
    if payment_method is not None:
        params["payment_method"] = payment_method
    if receipt_email is not None:
        params["receipt_email"] = receipt_email
    if return_url is not None:
        params["return_url"] = return_url

    return stripe_request("POST", f"/v1/payment_intents/{id}/confirm", params)

@mcp.tool()
def cancel_payment_intent(
    id: str,
    cancellation_reason: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Cancel a PaymentIntent.
    
    Args:
        id: The identifier of the PaymentIntent to cancel.
        cancellation_reason: Reason for canceling this PaymentIntent (e.g., 'duplicate', 'fraudulent', 'requested_by_customer').
    """
    params = {}
    if cancellation_reason is not None:
        params["cancellation_reason"] = cancellation_reason

    return stripe_request("POST", f"/v1/payment_intents/{id}/cancel", params)

@mcp.tool()
def list_payment_intents(
    limit: Optional[int] = 10,
    starting_after: Optional[str] = None,
    customer: Optional[str] = None,
) -> Dict[str, Any]:
    """
    List all PaymentIntents.
    
    Args:
        limit: A limit on the number of objects to be returned, between 1 and 100.
        starting_after: A cursor for pagination (an object ID).
        customer: Only return PaymentIntents for the customer specified by this customer ID.
    """
    params = {}
    if limit is not None:
        params["limit"] = limit
    if starting_after is not None:
        params["starting_after"] = starting_after
    if customer is not None:
        params["customer"] = customer

    return stripe_request("GET", "/v1/payment_intents", params)


# ==========================================
# 2. CHARGES
# ==========================================

@mcp.tool()
def create_charge(
    amount: int,
    currency: str,
    source: Optional[str] = None,
    customer: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    receipt_email: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Create a charge (legacy payment method). Use PaymentIntents for new integrations.
    
    Args:
        amount: Amount intended to be collected in the smallest currency unit.
        currency: Three-letter ISO currency code.
        source: A payment source (e.g., a token like 'tok_123' or card ID).
        customer: ID of an existing customer.
        description: An arbitrary string attached to the charge.
        metadata: Set of key-value pairs for custom data.
        receipt_email: Email address to send the receipt to.
    """
    params = {
        "amount": amount,
        "currency": currency,
    }
    if source is not None:
        params["source"] = source
    if customer is not None:
        params["customer"] = customer
    if description is not None:
        params["description"] = description
    if metadata is not None:
        params["metadata"] = metadata
    if receipt_email is not None:
        params["receipt_email"] = receipt_email

    return stripe_request("POST", "/v1/charges", params)

@mcp.tool()
def retrieve_charge(id: str) -> Dict[str, Any]:
    """
    Retrieve details of an existing charge.
    
    Args:
        id: The identifier of the charge to retrieve.
    """
    return stripe_request("GET", f"/v1/charges/{id}")

@mcp.tool()
def update_charge(
    id: str,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    receipt_email: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Update properties of an existing charge.
    
    Args:
        id: The identifier of the charge to update.
        description: An arbitrary string attached to the charge.
        metadata: Set of key-value pairs for custom data.
        receipt_email: Email address to send the receipt to.
    """
    params = {}
    if description is not None:
        params["description"] = description
    if metadata is not None:
        params["metadata"] = metadata
    if receipt_email is not None:
        params["receipt_email"] = receipt_email

    return stripe_request("POST", f"/v1/charges/{id}", params)

@mcp.tool()
def list_charges(
    limit: Optional[int] = 10,
    starting_after: Optional[str] = None,
    customer: Optional[str] = None,
) -> Dict[str, Any]:
    """
    List all charges.
    
    Args:
        limit: A limit on the number of objects to be returned, between 1 and 100.
        starting_after: A cursor for pagination.
        customer: Only return charges for this customer.
    """
    params = {}
    if limit is not None:
        params["limit"] = limit
    if starting_after is not None:
        params["starting_after"] = starting_after
    if customer is not None:
        params["customer"] = customer

    return stripe_request("GET", "/v1/charges", params)


# ==========================================
# 3. REFUNDS
# ==========================================

@mcp.tool()
def create_refund(
    charge: Optional[str] = None,
    payment_intent: Optional[str] = None,
    amount: Optional[int] = None,
    reason: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    """
    Create a refund for a charge or PaymentIntent.
    
    Args:
        charge: ID of the charge to refund.
        payment_intent: ID of the PaymentIntent to refund.
        amount: A positive integer in cents representing how much of this charge to refund.
        reason: String indicating the reason for the refund (e.g., 'duplicate', 'fraudulent', 'requested_by_customer').
        metadata: Set of key-value pairs for custom data.
    """
    params = {}
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

    return stripe_request("POST", "/v1/refunds", params)

@mcp.tool()
def retrieve_refund(id: str) -> Dict[str, Any]:
    """
    Retrieve details of an existing refund.
    
    Args:
        id: The identifier of the refund to retrieve.
    """
    return stripe_request("GET", f"/v1/refunds/{id}")

@mcp.tool()
def update_refund(
    id: str,
    metadata: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    """
    Update properties of an existing refund.
    
    Args:
        id: The identifier of the refund to update.
        metadata: Set of key-value pairs for custom data.
    """
    params = {}
    if metadata is not None:
        params["metadata"] = metadata

    return stripe_request("POST", f"/v1/refunds/{id}", params)

@mcp.tool()
def list_refunds(
    limit: Optional[int] = 10,
    starting_after: Optional[str] = None,
    charge: Optional[str] = None,
    payment_intent: Optional[str] = None,
) -> Dict[str, Any]:
    """
    List all refunds.
    
    Args:
        limit: A limit on the number of objects to be returned.
        starting_after: A cursor for pagination.
        charge: Only return refunds for this charge.
        payment_intent: Only return refunds for this PaymentIntent.
    """
    params = {}
    if limit is not None:
        params["limit"] = limit
    if starting_after is not None:
        params["starting_after"] = starting_after
    if charge is not None:
        params["charge"] = charge
    if payment_intent is not None:
        params["payment_intent"] = payment_intent

    return stripe_request("GET", "/v1/refunds", params)


# ==========================================
# 4. CUSTOMERS
# ==========================================

@mcp.tool()
def create_customer(
    email: Optional[str] = None,
    name: Optional[str] = None,
    phone: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    payment_method: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Create a new customer.
    
    Args:
        email: Customer's email address.
        name: Customer's full name.
        phone: Customer's phone number.
        description: An arbitrary string attached to the customer.
        metadata: Set of key-value pairs for custom data.
        payment_method: ID of the PaymentMethod to attach to the customer.
    """
    params = {}
    if email is not None:
        params["email"] = email
    if name is not None:
        params["name"] = name
    if phone is not None:
        params["phone"] = phone
    if description is not None:
        params["description"] = description
    if metadata is not None:
        params["metadata"] = metadata
    if payment_method is not None:
        params["payment_method"] = payment_method

    return stripe_request("POST", "/v1/customers", params)

@mcp.tool()
def retrieve_customer(id: str) -> Dict[str, Any]:
    """
    Retrieve details of an existing customer.
    
    Args:
        id: The identifier of the customer to retrieve.
    """
    return stripe_request("GET", f"/v1/customers/{id}")

@mcp.tool()
def update_customer(
    id: str,
    email: Optional[str] = None,
    name: Optional[str] = None,
    phone: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    """
    Update properties of an existing customer.
    
    Args:
        id: The identifier of the customer to update.
        email: Customer's email address.
        name: Customer's full name.
        phone: Customer's phone number.
        description: An arbitrary string attached to the customer.
        metadata: Set of key-value pairs for custom data.
    """
    params = {}
    if email is not None:
        params["email"] = email
    if name is not None:
        params["name"] = name
    if phone is not None:
        params["phone"] = phone
    if description is not None:
        params["description"] = description
    if metadata is not None:
        params["metadata"] = metadata

    return stripe_request("POST", f"/v1/customers/{id}", params)

@mcp.tool()
def delete_customer(id: str) -> Dict[str, Any]:
    """
    Delete a customer.
    
    Args:
        id: The identifier of the customer to delete.
    """
    return stripe_request("DELETE", f"/v1/customers/{id}")

@mcp.tool()
def list_customers(
    limit: Optional[int] = 10,
    starting_after: Optional[str] = None,
    email: Optional[str] = None,
) -> Dict[str, Any]:
    """
    List all customers.
    
    Args:
        limit: A limit on the number of objects to be returned.
        starting_after: A cursor for pagination.
        email: Only return customers with this email address.
    """
    params = {}
    if limit is not None:
        params["limit"] = limit
    if starting_after is not None:
        params["starting_after"] = starting_after
    if email is not None:
        params["email"] = email

    return stripe_request("GET", "/v1/customers", params)


# ==========================================
# 5. PRODUCTS
# ==========================================

@mcp.tool()
def create_product(
    name: str,
    active: Optional[bool] = True,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    statement_descriptor: Optional[str] = None,
    unit_label: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Create a new product.
    
    Args:
        name: The product's name, meant to be displayable to the customer.
        active: Whether the product is currently available for purchase.
        description: The product's description, meant to be displayable to the customer.
        metadata: Set of key-value pairs for custom data.
        statement_descriptor: Extra information about a product which will appear on the customer's credit card statement.
        unit_label: A label that represents the unit of this product (e.g., 'seat', 'user').
    """
    params = {
        "name": name,
        "active": active,
    }
    if description is not None:
        params["description"] = description
    if metadata is not None:
        params["metadata"] = metadata
    if statement_descriptor is not None:
        params["statement_descriptor"] = statement_descriptor
    if unit_label is not None:
        params["unit_label"] = unit_label

    return stripe_request("POST", "/v1/products", params)

@mcp.tool()
def retrieve_product(id: str) -> Dict[str, Any]:
    """
    Retrieve details of an existing product.
    
    Args:
        id: The identifier of the product to retrieve.
    """
    return stripe_request("GET", f"/v1/products/{id}")

@mcp.tool()
def update_product(
    id: str,
    name: Optional[str] = None,
    active: Optional[bool] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    """
    Update properties of an existing product.
    
    Args:
        id: The identifier of the product to update.
        name: The product's name.
        active: Whether the product is currently available for purchase.
        description: The product's description.
        metadata: Set of key-value pairs for custom data.
    """
    params = {}
    if name is not None:
        params["name"] = name
    if active is not None:
        params["active"] = active
    if description is not None:
        params["description"] = description
    if metadata is not None:
        params["metadata"] = metadata

    return stripe_request("POST", f"/v1/products/{id}", params)

@mcp.tool()
def delete_product(id: str) -> Dict[str, Any]:
    """
    Delete a product.
    
    Args:
        id: The identifier of the product to delete.
    """
    return stripe_request("DELETE", f"/v1/products/{id}")

@mcp.tool()
def list_products(
    limit: Optional[int] = 10,
    starting_after: Optional[str] = None,
    active: Optional[bool] = None,
) -> Dict[str, Any]:
    """
    List all products.
    
    Args:
        limit: A limit on the number of objects to be returned.
        starting_after: A cursor for pagination.
        active: Only return products that are active or inactive.
    """
    params = {}
    if limit is not None:
        params["limit"] = limit
    if starting_after is not None:
        params["starting_after"] = starting_after
    if active is not None:
        params["active"] = active

    return stripe_request("GET", "/v1/products", params)


# ==========================================
# 6. PRICES
# ==========================================

@mcp.tool()
def create_price(
    currency: str,
    product: Optional[str] = None,
    product_data: Optional[Dict[str, Any]] = None,
    unit_amount: Optional[int] = None,
    recurring: Optional[Dict[str, Any]] = None,
    active: Optional[bool] = True,
    metadata: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    """
    Create a new price.
    
    Args:
        currency: Three-letter ISO currency code.
        product: The ID of the product that this price will belong to.
        product_data: These parameters can be used to create a new product that this price will belong to.
        unit_amount: A positive integer in cents representing how much to charge.
        recurring: Describes how to recurringly charge (e.g., {'interval': 'month', 'interval_count': 1}).
        active: Whether the price can be used for new purchases.
        metadata: Set of key-value pairs for custom data.
    """
    params = {
        "currency": currency,
        "active": active,
    }
    if product is not None:
        params["product"] = product
    if product_data is not None:
        params["product_data"] = product_data
    if unit_amount is not None:
        params["unit_amount"] = unit_amount
    if recurring is not None:
        params["recurring"] = recurring
    if metadata is not None:
        params["metadata"] = metadata

    return stripe_request("POST", "/v1/prices", params)

@mcp.tool()
def retrieve_price(id: str) -> Dict[str, Any]:
    """
    Retrieve details of an existing price.
    
    Args:
        id: The identifier of the price to retrieve.
    """
    return stripe_request("GET", f"/v1/prices/{id}")

@mcp.tool()
def update_price(
    id: str,
    active: Optional[bool] = None,
    metadata: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    """
    Update properties of an existing price.
    
    Args:
        id: The identifier of the price to update.
        active: Whether the price can be used for new purchases.
        metadata: Set of key-value pairs for custom data.
    """
    params = {}
    if active is not None:
        params["active"] = active
    if metadata is not None:
        params["metadata"] = metadata

    return stripe_request("POST", f"/v1/prices/{id}", params)

@mcp.tool()
def list_prices(
    limit: Optional[int] = 10,
    starting_after: Optional[str] = None,
    product: Optional[str] = None,
    active: Optional[bool] = None,
) -> Dict[str, Any]:
    """
    List all prices.
    
    Args:
        limit: A limit on the number of objects to be returned.
        starting_after: A cursor for pagination.
        product: Only return prices for this product.
        active: Only return prices that are active or inactive.
    """
    params = {}
    if limit is not None:
        params["limit"] = limit
    if starting_after is not None:
        params["starting_after"] = starting_after
    if product is not None:
        params["product"] = product
    if active is not None:
        params["active"] = active

    return stripe_request("GET", "/v1/prices", params)


# ==========================================
# 7. SUBSCRIPTIONS
# ==========================================

@mcp.tool()
def create_subscription(
    customer: str,
    items: List[Dict[str, Any]],
    cancel_at_period_end: Optional[bool] = None,
    default_payment_method: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    trial_period_days: Optional[int] = None,
    promotion_code: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Create a new subscription.
    
    Args:
        customer: The identifier of the customer to subscribe.
        items: A list of subscription items, each with at least a 'price' ID (e.g., [{'price': 'price_123'}]).
        cancel_at_period_end: Boolean indicating whether this subscription should cancel at the end of the current period.
        default_payment_method: ID of the default payment method.
        metadata: Set of key-value pairs for custom data.
        trial_period_days: Number of days the trial period should last.
        promotion_code: ID of a promotion code to apply to this subscription.
    """
    params = {
        "customer": customer,
        "items": items,
    }
    if cancel_at_period_end is not None:
        params["cancel_at_period_end"] = cancel_at_period_end
    if default_payment_method is not None:
        params["default_payment_method"] = default_payment_method
    if metadata is not None:
        params["metadata"] = metadata
    if trial_period_days is not None:
        params["trial_period_days"] = trial_period_days
    if promotion_code is not None:
        params["promotion_code"] = promotion_code

    return stripe_request("POST", "/v1/subscriptions", params)

@mcp.tool()
def retrieve_subscription(id: str) -> Dict[str, Any]:
    """
    Retrieve details of an existing subscription.
    
    Args:
        id: The identifier of the subscription to retrieve.
    """
    return stripe_request("GET", f"/v1/subscriptions/{id}")

@mcp.tool()
def update_subscription(
    id: str,
    items: Optional[List[Dict[str, Any]]] = None,
    cancel_at_period_end: Optional[bool] = None,
    default_payment_method: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    trial_end: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Update properties of an existing subscription.
    
    Args:
        id: The identifier of the subscription to update.
        items: List of subscription items to update or add.
        cancel_at_period_end: Boolean indicating whether this subscription should cancel at the end of the current period.
        default_payment_method: ID of the default payment method.
        metadata: Set of key-value pairs for custom data.
        trial_end: Unix timestamp representing the end of the trial period, or 'now'.
    """
    params = {}
    if items is not None:
        params["items"] = items
    if cancel_at_period_end is not None:
        params["cancel_at_period_end"] = cancel_at_period_end
    if default_payment_method is not None:
        params["default_payment_method"] = default_payment_method
    if metadata is not None:
        params["metadata"] = metadata
    if trial_end is not None:
        params["trial_end"] = trial_end

    return stripe_request("POST", f"/v1/subscriptions/{id}", params)

@mcp.tool()
def cancel_subscription(id: str) -> Dict[str, Any]:
    """
    Cancel a subscription immediately.
    
    Args:
        id: The identifier of the subscription to cancel.
    """
    return stripe_request("DELETE", f"/v1/subscriptions/{id}")

@mcp.tool()
def list_subscriptions(
    limit: Optional[int] = 10,
    starting_after: Optional[str] = None,
    customer: Optional[str] = None,
    status: Optional[str] = None,
) -> Dict[str, Any]:
    """
    List all subscriptions.
    
    Args:
        limit: A limit on the number of objects to be returned.
        starting_after: A cursor for pagination.
        customer: Only return subscriptions for this customer.
        status: Only return subscriptions with this status (e.g., 'active', 'trialing', 'canceled').
    """
    params = {}
    if limit is not None:
        params["limit"] = limit
    if starting_after is not None:
        params["starting_after"] = starting_after
    if customer is not None:
        params["customer"] = customer
    if status is not None:
        params["status"] = status

    return stripe_request("GET", "/v1/subscriptions", params)


# ==========================================
# 8. INVOICES
# ==========================================

@mcp.tool()
def create_invoice(
    customer: str,
    auto_advance: Optional[bool] = None,
    collection_method: Optional[str] = None,
    days_until_due: Optional[int] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    """
    Create a draft invoice for a customer.
    
    Args:
        customer: The ID of the customer to bill.
        auto_advance: Controls whether Stripe will perform automatic collection of the invoice.
        collection_method: Either 'charge_automatically' or 'send_invoice'.
        days_until_due: Number of days until the invoice is due (only valid when collection_method is 'send_invoice').
        description: An arbitrary string attached to the invoice.
        metadata: Set of key-value pairs for custom data.
    """
    params = {
        "customer": customer,
    }
    if auto_advance is not None:
        params["auto_advance"] = auto_advance
    if collection_method is not None:
        params["collection_method"] = collection_method
    if days_until_due is not None:
        params["days_until_due"] = days_until_due
    if description is not None:
        params["description"] = description
    if metadata is not None:
        params["metadata"] = metadata

    return stripe_request("POST", "/v1/invoices", params)

@mcp.tool()
def retrieve_invoice(id: str) -> Dict[str, Any]:
    """
    Retrieve details of an existing invoice.
    
    Args:
        id: The identifier of the invoice to retrieve.
    """
    return stripe_request("GET", f"/v1/invoices/{id}")

@mcp.tool()
def update_invoice(
    id: str,
    auto_advance: Optional[bool] = None,
    collection_method: Optional[str] = None,
    days_until_due: Optional[int] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    """
    Update properties of an existing invoice.
    
    Args:
        id: The identifier of the invoice to update.
        auto_advance: Controls whether Stripe will perform automatic collection of the invoice.
        collection_method: Either 'charge_automatically' or 'send_invoice'.
        days_until_due: Number of days until the invoice is due.
        description: An arbitrary string attached to the invoice.
        metadata: Set of key-value pairs for custom data.
    """
    params = {}
    if auto_advance is not None:
        params["auto_advance"] = auto_advance
    if collection_method is not None:
        params["collection_method"] = collection_method
    if days_until_due is not None:
        params["days_until_due"] = days_until_due
    if description is not None:
        params["description"] = description
    if metadata is not None:
        params["metadata"] = metadata

    return stripe_request("POST", f"/v1/invoices/{id}", params)

@mcp.tool()
def finalize_invoice(id: str, auto_advance: Optional[bool] = None) -> Dict[str, Any]:
    """
    Finalize a draft invoice, making it ready to be paid.
    
    Args:
        id: The identifier of the invoice to finalize.
        auto_advance: Controls whether Stripe will perform automatic collection of the invoice.
    """
    params = {}
    if auto_advance is not None:
        params["auto_advance"] = auto_advance

    return stripe_request("POST", f"/v1/invoices/{id}/finalize", params)

@mcp.tool()
def pay_invoice(id: str, payment_method: Optional[str] = None) -> Dict[str, Any]:
    """
    Pay an open invoice.
    
    Args:
        id: The identifier of the invoice to pay.
        payment_method: ID of the payment method to use.
    """
    params = {}
    if payment_method is not None:
        params["payment_method"] = payment_method

    return stripe_request("POST", f"/v1/invoices/{id}/pay", params)

@mcp.tool()
def void_invoice(id: str) -> Dict[str, Any]:
    """
    Void a finalized invoice.
    
    Args:
        id: The identifier of the invoice to void.
    """
    return stripe_request("POST", f"/v1/invoices/{id}/void")

@mcp.tool()
def list_invoices(
    limit: Optional[int] = 10,
    starting_after: Optional[str] = None,
    customer: Optional[str] = None,
    status: Optional[str] = None,
) -> Dict[str, Any]:
    """
    List all invoices.
    
    Args:
        limit: A limit on the number of objects to be returned.
        starting_after: A cursor for pagination.
        customer: Only return invoices for this customer.
        status: Only return invoices with this status (e.g., 'draft', 'open', 'paid', 'uncollectible', 'void').
    """
    params = {}
    if limit is not None:
        params["limit"] = limit
    if starting_after is not None:
        params["starting_after"] = starting_after
    if customer is not None:
        params["customer"] = customer
    if status is not None:
        params["status"] = status

    return stripe_request("GET", "/v1/invoices", params)


# ==========================================
# 9. CHECKOUT SESSIONS
# ==========================================

@mcp.tool()
def create_checkout_session(
    success_url: str,
    line_items: List[Dict[str, Any]],
    mode: str,
    cancel_url: Optional[str] = None,
    customer: Optional[str] = None,
    customer_email: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    payment_method_types: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """
    Create a Checkout Session for Stripe Checkout.
    
    Args:
        success_url: The URL to redirect your customer back to after they complete the payment.
        line_items: A list of items the customer is purchasing (e.g., [{'price': 'price_123', 'quantity': 1}]).
        mode: The mode of the Checkout Session ('payment', 'setup', or 'subscription').
        cancel_url: The URL to redirect your customer back to if they cancel the payment.
        customer: ID of an existing Customer.
        customer_email: Email address of the customer.
        metadata: Set of key-value pairs for custom data.
        payment_method_types: List of payment method types (e.g., ['card']).
    """
    params = {
        "success_url": success_url,
        "line_items": line_items,
        "mode": mode,
    }
    if cancel_url is not None:
        params["cancel_url"] = cancel_url
    if customer is not None:
        params["customer"] = customer
    if customer_email is not None:
        params["customer_email"] = customer_email
    if metadata is not None:
        params["metadata"] = metadata
    if payment_method_types is not None:
        params["payment_method_types"] = payment_method_types

    return stripe_request("POST", "/v1/checkout/sessions", params)

@mcp.tool()
def retrieve_checkout_session(id: str) -> Dict[str, Any]:
    """
    Retrieve details of an existing Checkout Session.
    
    Args:
        id: The identifier of the Checkout Session to retrieve.
    """
    return stripe_request("GET", f"/v1/checkout/sessions/{id}")

@mcp.tool()
def list_checkout_sessions(
    limit: Optional[int] = 10,
    starting_after: Optional[str] = None,
    customer: Optional[str] = None,
) -> Dict[str, Any]:
    """
    List all Checkout Sessions.
    
    Args:
        limit: A limit on the number of objects to be returned.
        starting_after: A cursor for pagination.
        customer: Only return Checkout Sessions for this customer.
    """
    params = {}
    if limit is not None:
        params["limit"] = limit
    if starting_after is not None:
        params["starting_after"] = starting_after
    if customer is not None:
        params["customer"] = customer

    return stripe_request("GET", "/v1/checkout/sessions", params)


# ==========================================
# 10. PAYMENT LINKS
# ==========================================

@mcp.tool()
def create_payment_link(
    line_items: List[Dict[str, Any]],
    after_completion: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, str]] = None,
    restrictions: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Create a Payment Link.
    
    Args:
        line_items: A list of line items (e.g., [{'price': 'price_123', 'quantity': 1}]).
        after_completion: Behavior after customer completes payment (e.g., {'type': 'redirect', 'redirect': {'url': 'https://example.com'}}).
        metadata: Set of key-value pairs for custom data.
        restrictions: Restrictions on the payment link.
    """
    params = {
        "line_items": line_items,
    }
    if after_completion is not None:
        params["after_completion"] = after_completion
    if metadata is not None:
        params["metadata"] = metadata
    if restrictions is not None:
        params["restrictions"] = restrictions

    return stripe_request("POST", "/v1/payment_links", params)

@mcp.tool()
def retrieve_payment_link(id: str) -> Dict[str, Any]:
    """
    Retrieve details of an existing Payment Link.
    
    Args:
        id: The identifier of the Payment Link to retrieve.
    """
    return stripe_request("GET", f"/v1/payment_links/{id}")

@mcp.tool()
def update_payment_link(
    id: str,
    active: Optional[bool] = None,
    metadata: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    """
    Update properties of an existing Payment Link.
    
    Args:
        id: The identifier of the Payment Link to update.
        active: Whether the payment link is active.
        metadata: Set of key-value pairs for custom data.
    """
    params = {}
    if active is not None:
        params["active"] = active
    if metadata is not None:
        params["metadata"] = metadata

    return stripe_request("POST", f"/v1/payment_links/{id}", params)

@mcp.tool()
def list_payment_links(
    limit: Optional[int] = 10,
    starting_after: Optional[str] = None,
    active: Optional[bool] = None,
) -> Dict[str, Any]:
    """
    List all Payment Links.
    
    Args:
        limit: A limit on the number of objects to be returned.
        starting_after: A cursor for pagination.
        active: Only return active or inactive payment links.
    """
    params = {}
    if limit is not None:
        params["limit"] = limit
    if starting_after is not None:
        params["starting_after"] = starting_after
    if active is not None:
        params["active"] = active

    return stripe_request("GET", "/v1/payment_links", params)


# ==========================================
# 11. CONNECT (ACCOUNTS, TRANSFERS, PAYOUTS)
# ==========================================

@mcp.tool()
def create_account(
    type: str,
    country: Optional[str] = None,
    email: Optional[str] = None,
    capabilities: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    """
    Create a Stripe Connect account.
    
    Args:
        type: The type of Stripe account to create ('custom', 'express', or 'standard').
        country: The country in which the account holder resides.
        email: The email address of the account holder.
        capabilities: Capabilities to enable on the account (e.g., {'card_payments': {'requested': True}}).
        metadata: Set of key-value pairs for custom data.
    """
    params = {
        "type": type,
    }
    if country is not None:
        params["country"] = country
    if email is not None:
        params["email"] = email
    if capabilities is not None:
        params["capabilities"] = capabilities
    if metadata is not None:
        params["metadata"] = metadata

    return stripe_request("POST", "/v1/accounts", params)

@mcp.tool()
def retrieve_account(id: Optional[str] = None) -> Dict[str, Any]:
    """
    Retrieve details of a Stripe Connect account.
    
    Args:
        id: The identifier of the account to retrieve. If omitted, retrieves the platform account.
    """
    path = f"/v1/accounts/{id}" if id else "/v1/account"
    return stripe_request("GET", path)

@mcp.tool()
def list_accounts(
    limit: Optional[int] = 10,
    starting_after: Optional[str] = None,
) -> Dict[str, Any]:
    """
    List all connected accounts.
    
    Args:
        limit: A limit on the number of objects to be returned.
        starting_after: A cursor for pagination.
    """
    params = {}
    if limit is not None:
        params["limit"] = limit
    if starting_after is not None:
        params["starting_after"] = starting_after

    return stripe_request("GET", "/v1/accounts", params)

@mcp.tool()
def create_transfer(
    amount: int,
    currency: str,
    destination: str,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    source_transaction: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Create a transfer to a connected account.
    
    Args:
        amount: A positive integer in cents representing how much to transfer.
        currency: Three-letter ISO currency code.
        destination: ID of an existing connected account.
        description: An arbitrary string attached to the transfer.
        metadata: Set of key-value pairs for custom data.
        source_transaction: ID of an existing charge on the platform account.
    """
    params = {
        "amount": amount,
        "currency": currency,
        "destination": destination,
    }
    if description is not None:
        params["description"] = description
    if metadata is not None:
        params["metadata"] = metadata
    if source_transaction is not None:
        params["source_transaction"] = source_transaction

    return stripe_request("POST", "/v1/transfers", params)

@mcp.tool()
def retrieve_transfer(id: str) -> Dict[str, Any]:
    """
    Retrieve details of an existing transfer.
    
    Args:
        id: The identifier of the transfer to retrieve.
    """
    return stripe_request("GET", f"/v1/transfers/{id}")

@mcp.tool()
def list_transfers(
    limit: Optional[int] = 10,
    starting_after: Optional[str] = None,
    destination: Optional[str] = None,
) -> Dict[str, Any]:
    """
    List all transfers.
    
    Args:
        limit: A limit on the number of objects to be returned.
        starting_after: A cursor for pagination.
        destination: Only return transfers to this connected account.
    """
    params = {}
    if limit is not None:
        params["limit"] = limit
    if starting_after is not None:
        params["starting_after"] = starting_after
    if destination is not None:
        params["destination"] = destination

    return stripe_request("GET", "/v1/transfers", params)

@mcp.tool()
def create_payout(
    amount: int,
    currency: str,
    description: Optional[str] = None,
    destination: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    method: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Create a payout to a bank account or debit card.
    
    Args:
        amount: A positive integer in cents representing how much to payout.
        currency: Three-letter ISO currency code.
        description: An arbitrary string attached to the payout.
        destination: ID of a bank account or card.
        metadata: Set of key-value pairs for custom data.
        method: Payout speed ('standard' or 'instant').
    """
    params = {
        "amount": amount,
        "currency": currency,
    }
    if description is not None:
        params["description"] = description
    if destination is not None:
        params["destination"] = destination
    if metadata is not None:
        params["metadata"] = metadata
    if method is not None:
        params["method"] = method

    return stripe_request("POST", "/v1/payouts", params)

@mcp.tool()
def retrieve_payout(id: str) -> Dict[str, Any]:
    """
    Retrieve details of an existing payout.
    
    Args:
        id: The identifier of the payout to retrieve.
    """
    return stripe_request("GET", f"/v1/payouts/{id}")

@mcp.tool()
def list_payouts(
    limit: Optional[int] = 10,
    starting_after: Optional[str] = None,
) -> Dict[str, Any]:
    """
    List all payouts.
    
    Args:
        limit: A limit on the number of objects to be returned.
        starting_after: A cursor for pagination.
    """
    params = {}
    if limit is not None:
        params["limit"] = limit
    if starting_after is not None:
        params["starting_after"] = starting_after

    return stripe_request("GET", "/v1/payouts", params)


# ==========================================
# 12. SETUP INTENTS
# ==========================================

@mcp.tool()
def create_setup_intent(
    payment_method_types: Optional[List[str]] = None,
    customer: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    description: Optional[str] = None,
    usage: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Create a SetupIntent to collect payment credentials for future payments.
    
    Args:
        payment_method_types: List of payment method types (e.g., ['card']).
        customer: ID of the Customer this SetupIntent is for.
        metadata: Set of key-value pairs for custom data.
        description: An arbitrary string attached to the object.
        usage: Indicates how you intend to use the payment method (e.g., 'off_session', 'on_session').
    """
    params = {}
    if payment_method_types is not None:
        params["payment_method_types"] = payment_method_types
    if customer is not None:
        params["customer"] = customer
    if metadata is not None:
        params["metadata"] = metadata
    if description is not None:
        params["description"] = description
    if usage is not None:
        params["usage"] = usage

    return stripe_request("POST", "/v1/setup_intents", params)

@mcp.tool()
def retrieve_setup_intent(id: str) -> Dict[str, Any]:
    """
    Retrieve details of an existing SetupIntent.
    
    Args:
        id: The identifier of the SetupIntent to retrieve.
    """
    return stripe_request("GET", f"/v1/setup_intents/{id}")

@mcp.tool()
def update_setup_intent(
    id: str,
    customer: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    description: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Update properties of an existing SetupIntent.
    
    Args:
        id: The identifier of the SetupIntent to update.
        customer: ID of the Customer this SetupIntent is for.
        metadata: Set of key-value pairs for custom data.
        description: An arbitrary string attached to the object.
    """
    params = {}
    if customer is not None:
        params["customer"] = customer
    if metadata is not None:
        params["metadata"] = metadata
    if description is not None:
        params["description"] = description

    return stripe_request("POST", f"/v1/setup_intents/{id}", params)

@mcp.tool()
def confirm_setup_intent(
    id: str,
    payment_method: Optional[str] = None,
    return_url: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Confirm a SetupIntent.
    
    Args:
        id: The identifier of the SetupIntent to confirm.
        payment_method: ID of the payment method to associate with this SetupIntent.
        return_url: The URL to redirect your customer back to after they complete authentication.
    """
    params = {}
    if payment_method is not None:
        params["payment_method"] = payment_method
    if return_url is not None:
        params["return_url"] = return_url

    return stripe_request("POST", f"/v1/setup_intents/{id}/confirm", params)

@mcp.tool()
def cancel_setup_intent(
    id: str,
    cancellation_reason: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Cancel a SetupIntent.
    
    Args:
        id: The identifier of the SetupIntent to cancel.
        cancellation_reason: Reason for canceling this SetupIntent (e.g., 'abandoned', 'requested_by_customer').
    """
    params = {}
    if cancellation_reason is not None:
        params["cancellation_reason"] = cancellation_reason

    return stripe_request("POST", f"/v1/setup_intents/{id}/cancel", params)

@mcp.tool()
def list_setup_intents(
    limit: Optional[int] = 10,
    starting_after: Optional[str] = None,
    customer: Optional[str] = None,
) -> Dict[str, Any]:
    """
    List all SetupIntents.
    
    Args:
        limit: A limit on the number of objects to be returned.
        starting_after: A cursor for pagination.
        customer: Only return SetupIntents for this customer.
    """
    params = {}
    if limit is not None:
        params["limit"] = limit
    if starting_after is not None:
        params["starting_after"] = starting_after
    if customer is not None:
        params["customer"] = customer

    return stripe_request("GET", "/v1/setup_intents", params)


# ==========================================
# 13. COUPONS
# ==========================================

@mcp.tool()
def create_coupon(
    id: Optional[str] = None,
    duration: str = "once",
    amount_off: Optional[int] = None,
    currency: Optional[str] = None,
    percent_off: Optional[float] = None,
    duration_in_months: Optional[int] = None,
    metadata: Optional[Dict[str, str]] = None,
    name: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Create a coupon.
    
    Args:
        id: Unique string of your choosing that will identify the coupon.
        duration: Describes how long a customer who applies this coupon will get the discount ('once', 'repeating', or 'forever').
        amount_off: A positive integer representing the amount to subtract from an invoice total.
        currency: Three-letter ISO currency code (required if amount_off is passed).
        percent_off: A positive float between 1 and 100 representing the percentage of the subscription invoice that will be discounted.
        duration_in_months: Required if duration is 'repeating'.
        metadata: Set of key-value pairs for custom data.
        name: Name of the coupon.
    """
    params = {
        "duration": duration,
    }
    if id is not None:
        params["id"] = id
    if amount_off is not None:
        params["amount_off"] = amount_off
    if currency is not None:
        params["currency"] = currency
    if percent_off is not None:
        params["percent_off"] = percent_off
    if duration_in_months is not None:
        params["duration_in_months"] = duration_in_months
    if metadata is not None:
        params["metadata"] = metadata
    if name is not None:
        params["name"] = name

    return stripe_request("POST", "/v1/coupons", params)

@mcp.tool()
def retrieve_coupon(id: str) -> Dict[str, Any]:
    """
    Retrieve details of an existing coupon.
    
    Args:
        id: The identifier of the coupon to retrieve.
    """
    return stripe_request("GET", f"/v1/coupons/{id}")

@mcp.tool()
def delete_coupon(id: str) -> Dict[str, Any]:
    """
    Delete a coupon.
    
    Args:
        id: The identifier of the coupon to delete.
    """
    return stripe_request("DELETE", f"/v1/coupons/{id}")

@mcp.tool()
def list_coupons(
    limit: Optional[int] = 10,
    starting_after: Optional[str] = None,
) -> Dict[str, Any]:
    """
    List all coupons.
    
    Args:
        limit: A limit on the number of objects to be returned.
        starting_after: A cursor for pagination.
    """
    params = {}
    if limit is not None:
        params["limit"] = limit
    if starting_after is not None:
        params["starting_after"] = starting_after

    return stripe_request("GET", "/v1/coupons", params)


# ==========================================
# 14. PROMOTION CODES
# ==========================================

@mcp.tool()
def create_promotion_code(
    coupon: str,
    code: Optional[str] = None,
    active: Optional[bool] = True,
    customer: Optional[str] = None,
    expires_at: Optional[int] = None,
    max_redemptions: Optional[int] = None,
    metadata: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    """
    Create a promotion code.
    
    Args:
        coupon: The ID of the coupon to associate with this promotion code.
        code: The customer-facing code. If not provided, Stripe will generate one.
        active: Whether the promotion code is active.
        customer: Only this customer can use this promotion code.
        expires_at: Unix timestamp representing when the promotion code expires.
        max_redemptions: Maximum number of times this promotion code can be redeemed.
        metadata: Set of key-value pairs for custom data.
    """
    params = {
        "coupon": coupon,
        "active": active,
    }
    if code is not None:
        params["code"] = code
    if customer is not None:
        params["customer"] = customer
    if expires_at is not None:
        params["expires_at"] = expires_at
    if max_redemptions is not None:
        params["max_redemptions"] = max_redemptions
    if metadata is not None:
        params["metadata"] = metadata

    return stripe_request("POST", "/v1/promo_codes", params)

@mcp.tool()
def retrieve_promotion_code(id: str) -> Dict[str, Any]:
    """
    Retrieve details of an existing promotion code.
    
    Args:
        id: The identifier of the promotion code to retrieve.
    """
    return stripe_request("GET", f"/v1/promo_codes/{id}")

@mcp.tool()
def update_promotion_code(
    id: str,
    active: Optional[bool] = None,
    metadata: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    """
    Update properties of an existing promotion code.
    
    Args:
        id: The identifier of the promotion code to update.
        active: Whether the promotion code is active.
        metadata: Set of key-value pairs for custom data.
    """
    params = {}
    if active is not None:
        params["active"] = active
    if metadata is not None:
        params["metadata"] = metadata

    return stripe_request("POST", f"/v1/promo_codes/{id}", params)

@mcp.tool()
def list_promotion_codes(
    limit: Optional[int] = 10,
    starting_after: Optional[str] = None,
    code: Optional[str] = None,
    active: Optional[bool] = None,
) -> Dict[str, Any]:
    """
    List all promotion codes.
    
    Args:
        limit: A limit on the number of objects to be returned.
        starting_after: A cursor for pagination.
        code: Only return promotion codes with this customer-facing code.
        active: Only return active or inactive promotion codes.
    """
    params = {}
    if limit is not None:
        params["limit"] = limit
    if starting_after is not None:
        params["starting_after"] = starting_after
    if code is not None:
        params["code"] = code
    if active is not None:
        params["active"] = active

    return stripe_request("GET", "/v1/promo_codes", params)


if __name__ == "__main__":
    mcp.run()
