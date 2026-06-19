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
def create_price(currency: str, unit_amount: int, product_id: str, nickname: str = None, recurring: dict = None):
    """Create a new price.

    Args:
        currency: Three-letter ISO currency code.
        unit_amount: The unit amount in cents to be charged, represented as a whole integer.
        product_id: The ID of the product this price is for.
        nickname: A brief description of the price.
        recurring: The recurring components of a price.
    """
    data = {
        "currency": currency,
        "unit_amount": unit_amount,
        "product": product_id,
    }
    if nickname:
        data["nickname"] = nickname
    if recurring:
        for key, value in recurring.items():
            data[f"recurring[{key}]"] = value

    response = requests.post(f"{base_url}/prices", headers=headers, data=data)
    return response.json()

@tool
def retrieve_price(price_id: str):
    """Retrieves the details of an existing price.

    Args:
        price_id: The ID of the price to retrieve.
    """
    response = requests.get(f"{base_url}/prices/{price_id}", headers=headers)
    return response.json()

@tool
def update_price(price_id: str, nickname: str = None, active: bool = None):
    """Updates the specified price by setting the values of the parameters passed.

    Args:
        price_id: The ID of the price to update.
        nickname: A brief description of the price.
        active: Whether the price is currently available for purchase.
    """
    data = {}
    if nickname:
        data["nickname"] = nickname
    if active is not None:
        data["active"] = active

    response = requests.post(f"{base_url}/prices/{price_id}", headers=headers, data=data)
    return response.json()

@tool
def list_prices(limit: int = 10, starting_after: str = None, ending_before: str = None, product: str = None):
    """Returns a list of your prices.

    Args:
        limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
        starting_after: A cursor for use in pagination.
        ending_before: A cursor for use in pagination.
        product: The ID of the product whose prices to list.
    """
    params = {"limit": limit}
    if starting_after:
        params["starting_after"] = starting_after
    if ending_before:
        params["ending_before"] = ending_before
    if product:
        params["product"] = product

    response = requests.get(f"{base_url}/prices", headers=headers, params=params)
    return response.json()
