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
def create_subscription(customer_id: str, items: list, expand: list = None):
    """Create a new subscription.

    Args:
        customer_id: The ID of the customer.
        items: A list of subscription items, each with an associated price.
        expand: Specifies which fields in the response should be expanded.
    """
    data = {
        "customer": customer_id,
    }
    for i, item in enumerate(items):
        for key, value in item.items():
            data[f"items[{i}][{key}]"] = value
    if expand:
        data["expand"] = expand

    response = requests.post(f"{base_url}/subscriptions", headers=headers, data=data)
    return response.json()

@tool
def retrieve_subscription(subscription_id: str):
    """Retrieves the details of an existing subscription.

    Args:
        subscription_id: The ID of the subscription to retrieve.
    """
    response = requests.get(f"{base_url}/subscriptions/{subscription_id}", headers=headers)
    return response.json()

@tool
def update_subscription(subscription_id: str, cancel_at_period_end: bool = None, proration_behavior: str = None, items: list = None):
    """Updates the specified subscription by setting the values of the parameters passed.

    Args:
        subscription_id: The ID of the subscription to update.
        cancel_at_period_end: Boolean indicating whether this subscription should cancel at the end of the current period.
        proration_behavior: Determines how to handle prorations when the subscription is updated.
        items: A list of subscription items, each with an associated price.
    """
    data = {}
    if cancel_at_period_end is not None:
        data["cancel_at_period_end"] = cancel_at_period_end
    if proration_behavior:
        data["proration_behavior"] = proration_behavior
    if items:
        for i, item in enumerate(items):
            for key, value in item.items():
                data[f"items[{i}][{key}]"] = value

    response = requests.post(f"{base_url}/subscriptions/{subscription_id}", headers=headers, data=data)
    return response.json()

@tool
def cancel_subscription(subscription_id: str):
    """Cancels a subscription immediately.

    Args:
        subscription_id: The ID of the subscription to cancel.
    """
    response = requests.delete(f"{base_url}/subscriptions/{subscription_id}", headers=headers)
    return response.json()

@tool
def list_subscriptions(limit: int = 10, starting_after: str = None, ending_before: str = None, customer: str = None, price: str = None, status: str = None):
    """Returns a list of your subscriptions.

    Args:
        limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
        starting_after: A cursor for use in pagination.
        ending_before: A cursor for use in pagination.
        customer: The ID of the customer whose subscriptions to retrieve.
        price: The ID of the price whose subscriptions to retrieve.
        status: The status of the subscriptions to retrieve.
    """
    params = {"limit": limit}
    if starting_after:
        params["starting_after"] = starting_after
    if ending_before:
        params["ending_before"] = ending_before
    if customer:
        params["customer"] = customer
    if price:
        params["price"] = price
    if status:
        params["status"] = status

    response = requests.get(f"{base_url}/subscriptions", headers=headers, params=params)
    return response.json()
