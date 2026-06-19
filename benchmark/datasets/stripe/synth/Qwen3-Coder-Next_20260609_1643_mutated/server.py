import os
import requests
from typing import Any, Dict, Optional
from fastmcp import FastMCP

# Initialize MCP server
mcp = FastMCP(name="stripe-server")

# Base URL for Stripe API
STRIPE_API_URL = "https://api.stripe.com"

def get_api_key() -> str:
    """Get the Stripe API key from environment variables."""
    api_key = os.environ.get("STRIPE_API_KEY")
    if not api_key:
        raise ValueError("STRIPE_API_KEY environment variable is not set")
    return api_key

def make_stripe_request(
    method: str,
    endpoint: str,
    params: Optional[Dict[str, Any]] = None,
    data: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """Make a request to the Stripe API."""
    url = f"{STRIPE_API_URL}/v1{endpoint}"
    api_key = get_api_key()
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    
    try:
        if method.upper() == "GET":
            response = requests.get(url, headers=headers, params=params)
        elif method.upper() == "POST":
            response = requests.post(url, headers=headers, data=data)
        else:
            response = requests.request(method, url, headers=headers, params=params, data=data)
        
        if response.status_code >= 200 and response.status_code < 300:
            return response.json()
        else:
            return {
                "error": f"Stripe API error: {response.status_code}",
                "message": response.json().get("error", {}).get("message", response.text)
            }
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

# ===================== Payment Intents =====================

@mcp.tool()
def create_payment_intent(
    amount: int,
    currency: str,
    automatic_payment_methods_enabled: Optional[bool] = None,
    confirm: Optional[bool] = False,
    customer_id: Optional[str] = None,
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
    **kwargs
) -> Dict[str, Any]:
    """
    Creates a PaymentIntent object to guide you through the process of collecting a payment from your customer.
    
    Args:
        amount: Amount intended to be collected (in smallest currency unit)
        currency: Three-letter ISO currency code (e.g., "usd")
        automatic_payment_methods_enabled: Whether to enable automatic payment methods
        confirm: Whether to immediately confirm the PaymentIntent
        customer_id: ID of the Customer this PaymentIntent belongs to
        customer_account: ID of the Account representing the customer
        description: Arbitrary string attached to the object
        metadata: Set of key-value pairs for storing additional information
        off_session: Whether the customer isn't present in your checkout flow
        payment_method: ID of the payment method to attach
        receipt_email: Email address to send the receipt to
        setup_future_usage: Indicates intent for future payments ("off_session" or "on_session")
        shipping: Shipping information for this PaymentIntent
        statement_descriptor: Text that appears on the customer's statement
        statement_descriptor_suffix: Provides information about a card charge
        **kwargs: Additional parameters
    
    Returns:
        PaymentIntent object if successful, error dict otherwise
    """
    data = {
        "amount": amount,
        "currency": currency,
        **({} if automatic_payment_methods_enabled is None else {"automatic_payment_methods[enabled]": str(automatic_payment_methods_enabled).lower()}),
        **({"confirm": "true"} if confirm else {}),
        **({} if customer_id is None else {"customer": customer_id}),
        **({} if customer_account is None else {"customer_account": customer_account}),
        **({} if description is None else {"description": description}),
        **({} if metadata is None else {f"metadata[{k}]": v for k, v in metadata.items()}),
        **({} if off_session is None else {"off_session": str(off_session).lower()}),
        **({} if payment_method is None else {"payment_method": payment_method}),
        **({} if receipt_email is None else {"receipt_email": receipt_email}),
        **({} if setup_future_usage is None else {"setup_future_usage": setup_future_usage}),
        **({} if shipping is None else {f"shipping[{k}]": v for k, v in shipping.items()}),
        **({} if statement_descriptor is None else {"statement_descriptor": statement_descriptor}),
        **({} if statement_descriptor_suffix is None else {"statement_descriptor_suffix": statement_descriptor_suffix}),
        **kwargs
    }
    
    return make_stripe_request("POST", "/payment_intents", data=data)

@mcp.tool()
def retrieve_payment_intent(payment_intent_id: str) -> Dict[str, Any]:
    """
    Retrieves the details of a PaymentIntent that has previously been created.
    
    Args:
        payment_intent_id: The ID of the PaymentIntent to retrieve
    
    Returns:
        PaymentIntent object if successful, error dict otherwise
    """
    return make_stripe_request("GET", f"/payment_intents/{payment_intent_id}")

@mcp.tool()
def update_payment_intent(
    payment_intent_id: str,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    receipt_email: Optional[str] = None,
    shipping: Optional[Dict[str, Any]] = None,
    statement_descriptor: Optional[str] = None,
    statement_descriptor_suffix: Optional[str] = None,
    **kwargs
) -> Dict[str, Any]:
    """
    Updates the specified PaymentIntent by setting the values of the parameters passed.
    
    Args:
        payment_intent_id: The ID of the PaymentIntent to update
        description: Arbitrary string attached to the object
        metadata: Set of key-value pairs for storing additional information
        receipt_email: Email address to send the receipt to
        shipping: Shipping information for this PaymentIntent
        statement_descriptor: Text that appears on the customer's statement
        statement_descriptor_suffix: Provides information about a card charge
        **kwargs: Additional parameters
    
    Returns:
        Updated PaymentIntent object if successful, error dict otherwise
    """
    data = {
        **({} if description is None else {"description": description}),
        **({} if metadata is None else {f"metadata[{k}]": v for k, v in metadata.items()}),
        **({} if receipt_email is None else {"receipt_email": receipt_email}),
        **({} if shipping is None else {f"shipping[{k}]": v for k, v in shipping.items()}),
        **({} if statement_descriptor is None else {"statement_descriptor": statement_descriptor}),
        **({} if statement_descriptor_suffix is None else {"statement_descriptor_suffix": statement_descriptor_suffix}),
        **kwargs
    }
    
    return make_stripe_request("POST", f"/payment_intents/{payment_intent_id}", data=data)

# ===================== Refunds =====================

@mcp.tool()
def create_refund(
    amount: Optional[int] = None,
    charge: Optional[str] = None,
    payment_intent: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    reason: Optional[str] = None,
    **kwargs
) -> Dict[str, Any]:
    """
    Creates a refund to refund a previously created charge.
    
    Args:
        amount: Amount to refund (must not exceed the unrefunded amount of the charge)
        charge: The identifier of the charge to refund
        payment_intent: The identifier of the PaymentIntent to refund
        metadata: Set of key-value pairs for storing additional information
        reason: Reason for the refund ("duplicate", "fraudulent", "requested_by_customer")
        **kwargs: Additional parameters
    
    Returns:
        Refund object if successful, error dict otherwise
    """
    data = {
        **({} if amount is None else {"amount": amount}),
        **({} if charge is None else {"charge": charge}),
        **({} if payment_intent is None else {"payment_intent": payment_intent}),
        **({} if metadata is None else {f"metadata[{k}]": v for k, v in metadata.items()}),
        **({} if reason is None else {"reason": reason}),
        **kwargs
    }
    
    return make_stripe_request("POST", "/refunds", data=data)

@mcp.tool()
def retrieve_refund(refund_id: str) -> Dict[str, Any]:
    """
    Retrieves the details of an existing refund.
    
    Args:
        refund_id: The ID of the Refund to retrieve
    
    Returns:
        Refund object if successful, error dict otherwise
    """
    return make_stripe_request("GET", f"/refunds/{refund_id}")

# ===================== Subscriptions =====================

@mcp.tool()
def create_subscription(
    customer: str,
    items: list,
    automatic_tax_enabled: Optional[bool] = None,
    currency: Optional[str] = None,
    customer_account: Optional[str] = None,
    default_payment_method: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    payment_behavior: Optional[str] = None,
    **kwargs
) -> Dict[str, Any]:
    """
    Creates a new subscription on an existing customer.
    
    Args:
        customer: The identifier of the customer to subscribe
        items: A list of up to 20 subscription items, each with an attached price
        automatic_tax_enabled: Whether to enable automatic tax for this subscription
        currency: Three-letter ISO currency code (if different from customer's currency)
        customer_account: The identifier of the account representing the customer
        default_payment_method: ID of the default payment method for the subscription
        description: The subscription's notes
        metadata: Set of key-value pairs for storing additional information
        payment_behavior: How to handle the initial payment ("allow_incomplete", "default_incomplete", etc.)
        **kwargs: Additional parameters
    
    Returns:
        Subscription object if successful, error dict otherwise
    """
    data = {
        "customer": customer,
        **{f"items[{i}][{k}]": v for i, item in enumerate(items) for k, v in item.items()},
        **({} if automatic_tax_enabled is None else {"automatic_tax[enabled]": str(automatic_tax_enabled).lower()}),
        **({} if currency is None else {"currency": currency}),
        **({} if customer_account is None else {"customer_account": customer_account}),
        **({} if default_payment_method is None else {"default_payment_method": default_payment_method}),
        **({} if description is None else {"description": description}),
        **({} if metadata is None else {f"metadata[{k}]": v for k, v in metadata.items()}),
        **({} if payment_behavior is None else {"payment_behavior": payment_behavior}),
        **kwargs
    }
    
    return make_stripe_request("POST", "/subscriptions", data=data)

@mcp.tool()
def retrieve_subscription(subscription_id: str) -> Dict[str, Any]:
    """
    Retrieves the details of a Subscription.
    
    Args:
        subscription_id: The ID of the Subscription to retrieve
    
    Returns:
        Subscription object if successful, error dict otherwise
    """
    return make_stripe_request("GET", f"/subscriptions/{subscription_id}")

@mcp.tool()
def cancel_subscription(subscription_id: str, **kwargs) -> Dict[str, Any]:
    """
    Cancels an existing subscription.
    
    Args:
        subscription_id: The ID of the Subscription to cancel
        **kwargs: Additional parameters
    
    Returns:
        Canceled Subscription object if successful, error dict otherwise
    """
    data = kwargs
    return make_stripe_request("DELETE", f"/subscriptions/{subscription_id}", data=data)

# ===================== Invoices =====================

@mcp.tool()
def create_preview_invoice(
    customer: str,
    subscription: Optional[str] = None,
    automatic_tax_enabled: Optional[bool] = None,
    currency: Optional[str] = None,
    customer_account: Optional[str] = None,
    **kwargs
) -> Dict[str, Any]:
    """
    Creates a preview invoice to see upcoming charges.
    
    Args:
        customer: The identifier of the customer whose upcoming invoice you're retrieving
        subscription: The identifier of the subscription for which you'd like to retrieve the upcoming invoice
        automatic_tax_enabled: Whether to enable automatic tax for this invoice preview
        currency: Three-letter ISO currency code
        customer_account: The identifier of the account representing the customer
        **kwargs: Additional parameters
    
    Returns:
        Invoice object if successful, error dict otherwise
    """
    data = {
        "customer": customer,
        **({} if subscription is None else {"subscription": subscription}),
        **({} if automatic_tax_enabled is None else {"automatic_tax[enabled]": str(automatic_tax_enabled).lower()}),
        **({} if currency is None else {"currency": currency}),
        **({} if customer_account is None else {"customer_account": customer_account}),
        **kwargs
    }
    
    return make_stripe_request("POST", "/invoices/create_preview", data=data)

@mcp.tool()
def retrieve_invoice(invoice_id: str) -> Dict[str, Any]:
    """
    Retrieves the details of an Invoice.
    
    Args:
        invoice_id: The ID of the Invoice to retrieve
    
    Returns:
        Invoice object if successful, error dict otherwise
    """
    return make_stripe_request("GET", f"/invoices/{invoice_id}")

# ===================== Products =====================

@mcp.tool()
def create_product(
    name: str,
    active: Optional[bool] = None,
    description: Optional[str] = None,
    id: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    tax_code: Optional[str] = None,
    **kwargs
) -> Dict[str, Any]:
    """
    Creates a new Product object.
    
    Args:
        name: The product's name (required)
        active: Whether the product is currently available for purchase
        description: The product's notes
        id: An identifier for the product (will be randomly generated if not provided)
        metadata: Set of key-value pairs for storing additional information
        tax_code: A tax code ID
        **kwargs: Additional parameters
    
    Returns:
        Product object if successful, error dict otherwise
    """
    data = {
        "name": name,
        **({} if active is None else {"active": str(active).lower()}),
        **({} if description is None else {"description": description}),
        **({} if id is None else {"id": id}),
        **({} if metadata is None else {f"metadata[{k}]": v for k, v in metadata.items()}),
        **({} if tax_code is None else {"tax_code": tax_code}),
        **kwargs
    }
    
    return make_stripe_request("POST", "/products", data=data)

@mcp.tool()
def retrieve_product(product_id: str) -> Dict[str, Any]:
    """
    Retrieves the details of a Product.
    
    Args:
        product_id: The ID of the Product to retrieve
    
    Returns:
        Product object if successful, error dict otherwise
    """
    return make_stripe_request("GET", f"/products/{product_id}")

@mcp.tool()
def update_product(
    product_id: str,
    name: Optional[str] = None,
    active: Optional[bool] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    tax_code: Optional[str] = None,
    default_price: Optional[str] = None,
    **kwargs
) -> Dict[str, Any]:
    """
    Updates the specified Product by setting the values of the parameters passed.
    
    Args:
        product_id: The ID of the Product to update
        name: The product's name
        active: Whether the product is available for purchase
        description: The product's notes
        metadata: Set of key-value pairs for storing additional information
        tax_code: A tax code ID
        default_price: The ID of the Price object that is the default price
        **kwargs: Additional parameters
    
    Returns:
        Updated Product object if successful, error dict otherwise
    """
    data = {
        **({} if name is None else {"name": name}),
        **({} if active is None else {"active": str(active).lower()}),
        **({} if description is None else {"description": description}),
        **({} if metadata is None else {f"metadata[{k}]": v for k, v in metadata.items()}),
        **({} if tax_code is None else {"tax_code": tax_code}),
        **({} if default_price is None else {"default_price": default_price}),
        **kwargs
    }
    
    return make_stripe_request("POST", f"/products/{product_id}", data=data)

# ===================== Prices =====================

@mcp.tool()
def create_price(
    currency: str,
    unit_amount: Optional[int] = None,
    product: Optional[str] = None,
    active: Optional[bool] = None,
    metadata: Optional[Dict[str, str]] = None,
    nickname: Optional[str] = None,
    recurring: Optional[Dict[str, Any]] = None,
    tax_behavior: Optional[str] = None,
    billing_scheme: Optional[str] = None,
    **kwargs
) -> Dict[str, Any]:
    """
    Creates a new Price object.
    
    Args:
        currency: Three-letter ISO currency code (required)
        unit_amount: The unit amount (in smallest currency unit) to charge
        product: The ID of the Product this Price belongs to
        active: Whether the price can be used for new purchases
        metadata: Set of key-value pairs for storing additional information
        nickname: A brief note of the price
        recurring: The recurring components of a price (interval, usage_type, etc.)
        tax_behavior: Specifies whether the price is inclusive or exclusive of taxes
        billing_scheme: The billing scheme for this price ("per_unit" or "tiered")
        **kwargs: Additional parameters
    
    Returns:
        Price object if successful, error dict otherwise
    """
    data = {
        "currency": currency,
        **({} if unit_amount is None else {"unit_amount": unit_amount}),
        **({} if product is None else {"product": product}),
        **({} if active is None else {"active": str(active).lower()}),
        **({} if metadata is None else {f"metadata[{k}]": v for k, v in metadata.items()}),
        **({} if nickname is None else {"nickname": nickname}),
        **({} if recurring is None else {f"recurring[{k}]": v for k, v in recurring.items()}),
        **({} if tax_behavior is None else {"tax_behavior": tax_behavior}),
        **({} if billing_scheme is None else {"billing_scheme": billing_scheme}),
        **kwargs
    }
    
    return make_stripe_request("POST", "/prices", data=data)

@mcp.tool()
def retrieve_price(price_id: str) -> Dict[str, Any]:
    """
    Retrieves the details of a Price.
    
    Args:
        price_id: The ID of the Price to retrieve
    
    Returns:
        Price object if successful, error dict otherwise
    """
    return make_stripe_request("GET", f"/prices/{price_id}")

# ===================== Customers =====================

@mcp.tool()
def create_customer(
    email: Optional[str] = None,
    name: Optional[str] = None,
    description: Optional[str] = None,
    address: Optional[Dict[str, Any]] = None,
    phone: Optional[str] = None,
    shipping: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, str]] = None,
    payment_method: Optional[str] = None,
    tax: Optional[Dict[str, Any]] = None,
    **kwargs
) -> Dict[str, Any]:
    """
    Creates a Customer object to track payments and subscriptions.
    
    Args:
        email: Customer's email address
        name: Customer's full name or business name
        description: Arbitrary string attached to the Customer object
        address: The customer's address
        phone: The customer's phone number
        shipping: The customer's shipping information
        metadata: Set of key-value pairs for storing additional information
        payment_method: The ID of the PaymentMethod to attach to the customer
        tax: Tax details about the customer
        **kwargs: Additional parameters
    
    Returns:
        Customer object if successful, error dict otherwise
    """
    data = {
        **({} if email is None else {"email": email}),
        **({} if name is None else {"name": name}),
        **({} if description is None else {"description": description}),
        **({} if address is None else {f"address[{k}]": v for k, v in address.items()}),
        **({} if phone is None else {"phone": phone}),
        **({} if shipping is None else {f"shipping[{k}]": v for k, v in shipping.items()}),
        **({} if metadata is None else {f"metadata[{k}]": v for k, v in metadata.items()}),
        **({} if payment_method is None else {"payment_method": payment_method}),
        **({} if tax is None else {f"tax[{k}]": v for k, v in tax.items()}),
        **kwargs
    }
    
    return make_stripe_request("POST", "/customers", data=data)

@mcp.tool()
def retrieve_customer(customer_id: str) -> Dict[str, Any]:
    """
    Retrieves the details of a Customer.
    
    Args:
        customer_id: The ID of the Customer to retrieve
    
    Returns:
        Customer object if successful, error dict otherwise
    """
    return make_stripe_request("GET", f"/customers/{customer_id}")

@mcp.tool()
def update_customer(
    customer_id: str,
    email: Optional[str] = None,
    name: Optional[str] = None,
    description: Optional[str] = None,
    address: Optional[Dict[str, Any]] = None,
    phone: Optional[str] = None,
    shipping: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, str]] = None,
    payment_method: Optional[str] = None,
    tax: Optional[Dict[str, Any]] = None,
    default_source: Optional[str] = None,
    **kwargs
) -> Dict[str, Any]:
    """
    Updates the specified Customer by setting the values of the parameters passed.
    
    Args:
        customer_id: The ID of the Customer to update
        email: Customer's email address
        name: Customer's full name or business name
        description: Arbitrary string attached to the Customer object
        address: The customer's address
        phone: The customer's phone number
        shipping: The customer's shipping information
        metadata: Set of key-value pairs for storing additional information
        payment_method: The ID of the PaymentMethod to attach to the customer
        tax: Tax details about the customer
        default_source: ID of the default payment source
        **kwargs: Additional parameters
    
    Returns:
        Updated Customer object if successful, error dict otherwise
    """
    data = {
        **({} if email is None else {"email": email}),
        **({} if name is None else {"name": name}),
        **({} if description is None else {"description": description}),
        **({} if address is None else {f"address[{k}]": v for k, v in address.items()}),
        **({} if phone is None else {"phone": phone}),
        **({} if shipping is None else {f"shipping[{k}]": v for k, v in shipping.items()}),
        **({} if metadata is None else {f"metadata[{k}]": v for k, v in metadata.items()}),
        **({} if payment_method is None else {"payment_method": payment_method}),
        **({} if tax is None else {f"tax[{k}]": v for k, v in tax.items()}),
        **({} if default_source is None else {"default_source": default_source}),
        **kwargs
    }
    
    return make_stripe_request("POST", f"/customers/{customer_id}", data=data)

# ===================== Disputes =====================

@mcp.tool()
def update_dispute(dispute_id: str, evidence: Optional[Dict[str, Any]] = None, metadata: Optional[Dict[str, str]] = None, submit: Optional[bool] = None, **kwargs) -> Dict[str, Any]:
    """
    Updates a dispute by submitting evidence to help resolve it.
    
    Args:
        dispute_id: The ID of the Dispute to update
        evidence: Evidence to upload (access_activity_log, billing_address, etc.)
        metadata: Set of key-value pairs for storing additional information
        submit: Whether to immediately submit evidence to the bank
        **kwargs: Additional parameters
    
    Returns:
        Updated Dispute object if successful, error dict otherwise
    """
    data = {
        **({} if evidence is None else {f"evidence[{k}]": v for k, v in evidence.items()}),
        **({} if metadata is None else {f"metadata[{k}]": v for k, v in metadata.items()}),
        **({} if submit is None else {"submit": str(submit).lower()}),
        **kwargs
    }
    
    return make_stripe_request("POST", f"/disputes/{dispute_id}", data=data)

@mcp.tool()
def retrieve_dispute(dispute_id: str) -> Dict[str, Any]:
    """
    Retrieves the details of a Dispute.
    
    Args:
        dispute_id: The ID of the Dispute to retrieve
    
    Returns:
        Dispute object if successful, error dict otherwise
    """
    return make_stripe_request("GET", f"/disputes/{dispute_id}")

# ===================== Setup Intents =====================

@mcp.tool()
def create_setup_intent(
    usage: Optional[str] = None,
    confirm: Optional[bool] = False,
    automatic_payment_methods_enabled: Optional[bool] = None,
    customer: Optional[str] = None,
    customer_account: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    payment_method: Optional[str] = None,
    **kwargs
) -> Dict[str, Any]:
    """
    Creates a SetupIntent to set up and save payment credentials for future payments.
    
    Args:
        usage: How the payment method is intended to be used ("off_session" or "on_session")
        confirm: Whether to immediately confirm the SetupIntent
        automatic_payment_methods_enabled: Whether to enable automatic payment methods
        customer: ID of the Customer this SetupIntent belongs to
        customer_account: ID of the Account this SetupIntent belongs to
        description: Arbitrary string attached to the object
        metadata: Set of key-value pairs for storing additional information
        payment_method: ID of the payment method to attach
        **kwargs: Additional parameters
    
    Returns:
        SetupIntent object if successful, error dict otherwise
    """
    data = {
        **({} if usage is None else {"usage": usage}),
        **({"confirm": "true"} if confirm else {}),
        **({} if automatic_payment_methods_enabled is None else {"automatic_payment_methods[enabled]": str(automatic_payment_methods_enabled).lower()}),
        **({} if customer is None else {"customer": customer}),
        **({} if customer_account is None else {"customer_account": customer_account}),
        **({} if description is None else {"description": description}),
        **({} if metadata is None else {f"metadata[{k}]": v for k, v in metadata.items()}),
        **({} if payment_method is None else {"payment_method": payment_method}),
        **kwargs
    }
    
    return make_stripe_request("POST", "/setup_intents", data=data)

@mcp.tool()
def retrieve_setup_intent(setup_intent_id: str) -> Dict[str, Any]:
    """
    Retrieves the details of a SetupIntent.
    
    Args:
        setup_intent_id: The ID of the SetupIntent to retrieve
    
    Returns:
        SetupIntent object if successful, error dict otherwise
    """
    return make_stripe_request("GET", f"/setup_intents/{setup_intent_id}")

# ===================== Charges =====================

@mcp.tool()
def create_charge(
    amount: int,
    currency: str,
    customer_id: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    receipt_email: Optional[str] = None,
    shipping: Optional[Dict[str, Any]] = None,
    source: Optional[str] = None,
    statement_descriptor: Optional[str] = None,
    statement_descriptor_suffix: Optional[str] = None,
    capture: Optional[bool] = None,
    **kwargs
) -> Dict[str, Any]:
    """
    Creates a Charge object to move money into your Stripe account.
    Note: This method is deprecated. Use Payment Intents instead.
    
    Args:
        amount: Amount intended to be collected (in smallest currency unit)
        currency: Three-letter ISO currency code (e.g., "usd")
        customer_id: ID of an existing customer to charge
        description: Arbitrary string attached to the Charge object
        metadata: Set of key-value pairs for storing additional information
        receipt_email: Email address to send the receipt to
        shipping: Shipping information for the charge
        source: ID of a payment source (card, bank account, etc.)
        statement_descriptor: Text that appears on the customer's statement
        statement_descriptor_suffix: Provides information about a card charge
        capture: Whether to immediately capture the charge
        **kwargs: Additional parameters
    
    Returns:
        Charge object if successful, error dict otherwise
    """
    data = {
        "amount": amount,
        "currency": currency,
        **({} if customer_id is None else {"customer": customer_id}),
        **({} if description is None else {"description": description}),
        **({} if metadata is None else {f"metadata[{k}]": v for k, v in metadata.items()}),
        **({} if receipt_email is None else {"receipt_email": receipt_email}),
        **({} if shipping is None else {f"shipping[{k}]": v for k, v in shipping.items()}),
        **({} if source is None else {"source": source}),
        **({} if statement_descriptor is None else {"statement_descriptor": statement_descriptor}),
        **({} if statement_descriptor_suffix is None else {"statement_descriptor_suffix": statement_descriptor_suffix}),
        **({} if capture is None else {"capture": str(capture).lower()}),
        **kwargs
    }
    
    return make_stripe_request("POST", "/charges", data=data)

@mcp.tool()
def retrieve_charge(charge_id: str) -> Dict[str, Any]:
    """
    Retrieves the details of a Charge.
    
    Args:
        charge_id: The ID of the Charge to retrieve
    
    Returns:
        Charge object if successful, error dict otherwise
    """
    return make_stripe_request("GET", f"/charges/{charge_id}")

# ===================== Coupons =====================

@mcp.tool()
def create_coupon(
    percent_off: Optional[float] = None,
    amount_off: Optional[int] = None,
    currency: Optional[str] = None,
    duration: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    name: Optional[str] = None,
    **kwargs
) -> Dict[str, Any]:
    """
    Creates a coupon for applying discounts to customers.
    
    Args:
        percent_off: Percent that will be taken off the subtotal (required if amount_off is not provided)
        amount_off: Amount that will be taken off the subtotal (required if percent_off is not provided)
        currency: Three-letter ISO currency code (required if amount_off is provided)
        duration: How long the discount will be in effect ("forever", "once", "repeating")
        metadata: Set of key-value pairs for storing additional information
        name: Name of the coupon displayed to customers
        **kwargs: Additional parameters
    
    Returns:
        Coupon object if successful, error dict otherwise
    """
    data = {
        **({} if percent_off is None else {"percent_off": percent_off}),
        **({} if amount_off is None else {"amount_off": amount_off}),
        **({} if currency is None else {"currency": currency}),
        **({} if duration is None else {"duration": duration}),
        **({} if metadata is None else {f"metadata[{k}]": v for k, v in metadata.items()}),
        **({} if name is None else {"name": name}),
        **kwargs
    }
    
    return make_stripe_request("POST", "/coupons", data=data)

@mcp.tool()
def retrieve_coupon(coupon_id: str) -> Dict[str, Any]:
    """
    Retrieves the details of a Coupon.
    
    Args:
        coupon_id: The ID of the Coupon to retrieve
    
    Returns:
        Coupon object if successful, error dict otherwise
    """
    return make_stripe_request("GET", f"/coupons/{coupon_id}")

# ===================== Payment Links =====================

@mcp.tool()
def create_payment_link(
    line_items: list,
    metadata: Optional[Dict[str, str]] = None,
    active: Optional[bool] = None,
    allow_promotion_codes: Optional[bool] = None,
    automatic_tax_enabled: Optional[bool] = None,
    billing_address_collection: Optional[str] = None,
    currency: Optional[str] = None,
    custom_fields: Optional[list] = None,
    custom_text: Optional[Dict[str, Any]] = None,
    customer_creation: Optional[str] = None,
    invoice_creation_enabled: Optional[bool] = None,
    phone_number_collection_enabled: Optional[bool] = None,
    tax_id_collection_enabled: Optional[bool] = None,
    **kwargs
) -> Dict[str, Any]:
    """
    Creates a payment link that can be shared with customers.
    
    Args:
        line_items: A list of items being sold
        metadata: Set of key-value pairs for storing additional information
        active: Whether the payment link's URL is active
        allow_promotion_codes: Whether to allow promotion codes
        automatic_tax_enabled: Whether to enable automatic tax
        billing_address_collection: Whether to collect billing address ("auto", "required")
        currency: Three-letter ISO currency code
        custom_fields: Custom fields to collect from the customer
        custom_text: Custom text to display during checkout
        customer_creation: Whether to allow customer creation ("if_required", "always")
        invoice_creation_enabled: Whether to enable invoice creation
        phone_number_collection_enabled: Whether to collect phone number
        tax_id_collection_enabled: Whether to collect tax ID
        **kwargs: Additional parameters
    
    Returns:
        Payment Link object if successful, error dict otherwise
    """
    data = {
        **{f"line_items[{i}][{k}]": v for i, item in enumerate(line_items) for k, v in item.items()},
        **({} if metadata is None else {f"metadata[{k}]": v for k, v in metadata.items()}),
        **({} if active is None else {"active": str(active).lower()}),
        **({} if allow_promotion_codes is None else {"allow_promotion_codes": str(allow_promotion_codes).lower()}),
        **({} if automatic_tax_enabled is None else {"automatic_tax[enabled]": str(automatic_tax_enabled).lower()}),
        **({} if billing_address_collection is None else {"billing_address_collection": billing_address_collection}),
        **({} if currency is None else {"currency": currency}),
        **({} if custom_fields is None else {f"custom_fields[{i}]": str(item) for i, item in enumerate(custom_fields)}),
        **({} if custom_text is None else {f"custom_text[{k}]": str(v) for k, v in custom_text.items()}),
        **({} if customer_creation is None else {"customer_creation": customer_creation}),
        **({} if invoice_creation_enabled is None else {"invoice_creation[enabled]": str(invoice_creation_enabled).lower()}),
        **({} if phone_number_collection_enabled is None else {"phone_number_collection[enabled]": str(phone_number_collection_enabled).lower()}),
        **({} if tax_id_collection_enabled is None else {"tax_id_collection[enabled]": str(tax_id_collection_enabled).lower()}),
        **kwargs
    }
    
    return make_stripe_request("POST", "/payment_links", data=data)

@mcp.tool()
def retrieve_payment_link(payment_link_id: str) -> Dict[str, Any]:
    """
    Retrieves the details of a Payment Link.
    
    Args:
        payment_link_id: The ID of the Payment Link to retrieve
    
    Returns:
        Payment Link object if successful, error dict otherwise
    """
    return make_stripe_request("GET", f"/payment_links/{payment_link_id}")

# ===================== Transfers =====================

@mcp.tool()
def create_transfer(
    amount: int,
    currency: str,
    destination: str,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    source_transaction: Optional[str] = None,
    source_type: Optional[str] = None,
    transfer_group: Optional[str] = None,
    **kwargs
) -> Dict[str, Any]:
    """
    Creates a Transfer object to move funds between Stripe accounts (Connect).
    
    Args:
        amount: Amount to transfer (in smallest currency unit)
        currency: Three-letter ISO currency code
        destination: The ID of a connected Stripe account
        description: Arbitrary string attached to the object
        metadata: Set of key-value pairs for storing additional information
        source_transaction: ID of a charge or payout to fund the transfer
        source_type: The source type (e.g., "card")
        transfer_group: A string that identifies the transfer group
        **kwargs: Additional parameters
    
    Returns:
        Transfer object if successful, error dict otherwise
    """
    data = {
        "amount": amount,
        "currency": currency,
        "destination": destination,
        **({} if description is None else {"description": description}),
        **({} if metadata is None else {f"metadata[{k}]": v for k, v in metadata.items()}),
        **({} if source_transaction is None else {"source_transaction": source_transaction}),
        **({} if source_type is None else {"source_type": source_type}),
        **({} if transfer_group is None else {"transfer_group": transfer_group}),
        **kwargs
    }
    
    return make_stripe_request("POST", "/transfers", data=data)

@mcp.tool()
def retrieve_transfer(transfer_id: str) -> Dict[str, Any]:
    """
    Retrieves the details of a Transfer.
    
    Args:
        transfer_id: The ID of the Transfer to retrieve
    
    Returns:
        Transfer object if successful, error dict otherwise
    """
    return make_stripe_request("GET", f"/transfers/{transfer_id}")

# ===================== Accounts =====================

@mcp.tool()
def create_account(
    country: Optional[str] = None,
    email: Optional[str] = None,
    business_type: Optional[str] = None,
    capabilities: Optional[Dict[str, Any]] = None,
    company: Optional[Dict[str, Any]] = None,
    controller: Optional[Dict[str, Any]] = None,
    individual: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, str]] = None,
    tos_acceptance: Optional[Dict[str, Any]] = None,
    type: Optional[str] = None,
    **kwargs
) -> Dict[str, Any]:
    """
    Creates a new Stripe account (Connect).
    
    Args:
        country: The country in which the account holder resides
        email: The email address of the account holder
        business_type: The business type ("company", "individual", etc.)
        capabilities: Each key represents a capability and its settings
        company: Information about the company or business
        controller: Configuration describing the account controller's attributes
        individual: Information about the person represented by the account
        metadata: Set of key-value pairs for storing additional information
        tos_acceptance: Details on the account's acceptance of the Stripe Services Agreement
        type: The type of Stripe account to create ("custom", "express", "standard")
        **kwargs: Additional parameters
    
    Returns:
        Account object if successful, error dict otherwise
    """
    data = {
        **({} if country is None else {"country": country}),
        **({} if email is None else {"email": email}),
        **({} if business_type is None else {"business_type": business_type}),
        **({} if capabilities is None else {f"capabilities[{k}]": v for k, v in capabilities.items()}),
        **({} if company is None else {f"company[{k}]": v for k, v in company.items()}),
        **({} if controller is None else {f"controller[{k}]": v for k, v in controller.items()}),
        **({} if individual is None else {f"individual[{k}]": v for k, v in individual.items()}),
        **({} if metadata is None else {f"metadata[{k}]": v for k, v in metadata.items()}),
        **({} if tos_acceptance is None else {f"tos_acceptance[{k}]": v for k, v in tos_acceptance.items()}),
        **({} if type is None else {"type": type}),
        **kwargs
    }
    
    return make_stripe_request("POST", "/accounts", data=data)

@mcp.tool()
def retrieve_account(account_id: str) -> Dict[str, Any]:
    """
    Retrieves the details of a Stripe account.
    
    Args:
        account_id: The ID of the Account to retrieve
    
    Returns:
        Account object if successful, error dict otherwise
    """
    return make_stripe_request("GET", f"/accounts/{account_id}")

# ===================== Payment Methods =====================

@mcp.tool()
def create_payment_method(
    type: str,
    billing_details: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, str]] = None,
    **kwargs
) -> Dict[str, Any]:
    """
    Creates a PaymentMethod object.
    Note: It's recommended to use Payment Intents to accept payments directly instead of creating PaymentMethods directly.
    
    Args:
        type: The type of the PaymentMethod (e.g., "card", "us_bank_account")
        billing_details: Billing information associated with the PaymentMethod
        metadata: Set of key-value pairs for storing additional information
        **kwargs: Additional parameters specific to the payment method type
    
    Returns:
        PaymentMethod object if successful, error dict otherwise
    """
    data = {
        "type": type,
        **({} if billing_details is None else {f"billing_details[{k}]": v for k, v in billing_details.items()}),
        **({} if metadata is None else {f"metadata[{k}]": v for k, v in metadata.items()}),
        **kwargs
    }
    
    return make_stripe_request("POST", "/payment_methods", data=data)

@mcp.tool()
def retrieve_payment_method(payment_method_id: str) -> Dict[str, Any]:
    """
    Retrieves the details of a PaymentMethod.
    
    Args:
        payment_method_id: The ID of the PaymentMethod to retrieve
    
    Returns:
        PaymentMethod object if successful, error dict otherwise
    """
    return make_stripe_request("GET", f"/payment_methods/{payment_method_id}")

# ===================== Checkout Sessions =====================

@mcp.tool()
def create_checkout_session(
    line_items: list,
    mode: str,
    success_url: str,
    cancel_url: str,
    automatic_tax_enabled: Optional[bool] = None,
    client_reference_id: Optional[str] = None,
    customer: Optional[str] = None,
    customer_email: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    mode_enum: Optional[str] = None,
    ui_mode: Optional[str] = None,
    **kwargs
) -> Dict[str, Any]:
    """
    Creates a Checkout Session for payment or subscription flows.
    
    Args:
        line_items: A list of items the customer is purchasing
        mode: The mode of the Checkout Session ("payment", "subscription", or "setup")
        success_url: The URL to redirect customers to when payment is successful
        cancel_url: The URL to redirect customers to when they cancel
        automatic_tax_enabled: Whether to enable automatic tax for this session
        client_reference_id: A unique string to reference the Checkout Session
        customer: ID of an existing Customer
        customer_email: Email to prefill for new customers
        metadata: Set of key-value pairs for storing additional information
        mode_enum: The mode of the Checkout Session (alternative to mode parameter)
        ui_mode: The UI mode ("hosted", "embedded", or "custom")
        **kwargs: Additional parameters
    
    Returns:
        Checkout Session object if successful, error dict otherwise
    """
    data = {
        **{f"line_items[{i}][{k}]": v for i, item in enumerate(line_items) for k, v in item.items()},
        "mode": mode,
        "success_url": success_url,
        "cancel_url": cancel_url,
        **({} if automatic_tax_enabled is None else {"automatic_tax[enabled]": str(automatic_tax_enabled).lower()}),
        **({} if client_reference_id is None else {"client_reference_id": client_reference_id}),
        **({} if customer is None else {"customer": customer}),
        **({} if customer_email is None else {"customer_email": customer_email}),
        **({} if metadata is None else {f"metadata[{k}]": v for k, v in metadata.items()}),
        **({} if mode_enum is None else {"mode": mode_enum}),
        **({} if ui_mode is None else {"ui_mode": ui_mode}),
        **kwargs
    }
    
    return make_stripe_request("POST", "/checkout/sessions", data=data)

@mcp.tool()
def retrieve_checkout_session(session_id: str) -> Dict[str, Any]:
    """
    Retrieves the details of a Checkout Session.
    
    Args:
        session_id: The ID of the Checkout Session to retrieve
    
    Returns:
        Checkout Session object if successful, error dict otherwise
    """
    return make_stripe_request("GET", f"/checkout/sessions/{session_id}")
