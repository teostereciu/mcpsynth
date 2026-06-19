from mcp.server.fastmcp import FastMCP, tool
import requests
import os

stripe_api_key = os.environ.get("STRIPE_API_KEY")
base_url = "https://api.stripe.com/v1"

headers = {
    "Authorization": f"Bearer {stripe_api_key}",
    "Content-Type": "application/x-www-form-urlencoded",
}

@tool
def create_payment_intent(amount: int, currency: str, customer_id: str = None, payment_method_types: list = None):
    """Create a new payment intent.

    Args:
        amount: Amount intended to be collected by this PaymentIntent.
        currency: Three-letter ISO currency code.
        customer_id: The ID of the customer this PaymentIntent is for.
        payment_method_types: The list of payment method types that this PaymentIntent is allowed to use.
    """
    data = {
        "amount": amount,
        "currency": currency,
    }
    if customer_id:
        data["customer"] = customer_id
    if payment_method_types:
        for i, item in enumerate(payment_method_types):
            data[f"payment_method_types[{i}]"] = item

    response = requests.post(f"{base_url}/payment_intents", headers=headers, data=data)
    return response.json()

@tool
def retrieve_payment_intent(payment_intent_id: str):
    """Retrieves the details of an existing payment intent.

    Args:
        payment_intent_id: The ID of the payment intent to retrieve.
    """
    response = requests.get(f"{base_url}/payment_intents/{payment_intent_id}", headers=headers)
    return response.json()

@tool
def update_payment_intent(payment_intent_id: str, amount: int = None, currency: str = None, customer_id: str = None):
    """Updates the specified payment intent by setting the values of the parameters passed.

    Args:
        payment_intent_id: The ID of the payment intent to update.
        amount: Amount intended to be collected by this PaymentIntent.
        currency: Three-letter ISO currency code.
        customer_id: The ID of the customer this PaymentIntent is for.
    """
    data = {}
    if amount:
        data["amount"] = amount
    if currency:
        data["currency"] = currency
    if customer_id:
        data["customer"] = customer_id

    response = requests.post(f"{base_url}/payment_intents/{payment_intent_id}", headers=headers, data=data)
    return response.json()

@tool
def confirm_payment_intent(payment_intent_id: str, payment_method: str = None):
    """Confirm a payment intent.

    Args:
        payment_intent_id: The ID of the payment intent to confirm.
        payment_method: The ID of the payment method to use for confirmation.
    """
    data = {}
    if payment_method:
        data["payment_method"] = payment_method

    response = requests.post(f"{base_url}/payment_intents/{payment_intent_id}/confirm", headers=headers, data=data)
    return response.json()

@tool
def capture_payment_intent(payment_intent_id: str, amount_to_capture: int = None):
    """Capture the funds of an existing uncaptured payment intent.

    Args:
        payment_intent_id: The ID of the payment intent to capture.
        amount_to_capture: The amount to capture.
    """
    data = {}
    if amount_to_capture:
        data["amount_to_capture"] = amount_to_capture

    response = requests.post(f"{base_url}/payment_intents/{payment_intent_id}/capture", headers=headers, data=data)
    return response.json()

@tool
def cancel_payment_intent(payment_intent_id: str, cancellation_reason: str = None):
    """Cancel a payment intent.

    Args:
        payment_intent_id: The ID of the payment intent to cancel.
        cancellation_reason: Reason for canceling this PaymentIntent.
    """
    data = {}
    if cancellation_reason:
        data["cancellation_reason"] = cancellation_reason

    response = requests.post(f"{base_url}/payment_intents/{payment_intent_id}/cancel", headers=headers, data=data)
    return response.json()

@tool
def list_payment_intents(limit: int = 10, starting_after: str = None, ending_before: str = None, customer: str = None):
    """Returns a list of your payment intents.

    Args:
        limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
        starting_after: A cursor for use in pagination.
        ending_before: A cursor for use in pagination.
        customer: The ID of the customer whose payment intents to retrieve.
    """
    params = {"limit": limit}
    if starting_after:
        params["starting_after"] = starting_after
    if ending_before:
        params["ending_before"] = ending_before
    if customer:
        params["customer"] = customer

    response = requests.get(f"{base_url}/payment_intents", headers=headers, params=params)
    return response.json()
