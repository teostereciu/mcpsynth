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
def create_product(name: str, description: str = None, active: bool = None, url: str = None):
    """Create a new product.

    Args:
        name: The product's name.
        description: The product's description.
        active: Whether the product is currently available for purchase.
        url: A URL of a publicly-accessible website related to this product.
    """
    data = {"name": name}
    if description:
        data["description"] = description
    if active is not None:
        data["active"] = active
    if url:
        data["url"] = url

    response = requests.post(f"{base_url}/products", headers=headers, data=data)
    return response.json()

@tool
def retrieve_product(product_id: str):
    """Retrieves the details of an existing product.

    Args:
        product_id: The ID of the product to retrieve.
    """
    response = requests.get(f"{base_url}/products/{product_id}", headers=headers)
    return response.json()

@tool
def update_product(product_id: str, name: str = None, description: str = None, active: bool = None, url: str = None):
    """Updates the specified product by setting the values of the parameters passed.

    Args:
        product_id: The ID of the product to update.
        name: The product's name.
        description: The product's description.
        active: Whether the product is currently available for purchase.
        url: A URL of a publicly-accessible website related to this product.
    """
    data = {}
    if name:
        data["name"] = name
    if description:
        data["description"] = description
    if active is not None:
        data["active"] = active
    if url:
        data["url"] = url

    response = requests.post(f"{base_url}/products/{product_id}", headers=headers, data=data)
    return response.json()

@tool
def delete_product(product_id: str):
    """Deletes a product object.

    Args:
        product_id: The ID of the product to delete.
    """
    response = requests.delete(f"{base_url}/products/{product_id}", headers=headers)
    return response.json()

@tool
def list_products(limit: int = 10, starting_after: str = None, ending_before: str = None):
    """Returns a list of your products.

    Args:
        limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
        starting_after: A cursor for use in pagination.
        ending_before: A cursor for use in pagination.
    """
    params = {"limit": limit}
    if starting_after:
        params["starting_after"] = starting_after
    if ending_before:
        params["ending_before"] = ending_before

    response = requests.get(f"{base_url}/products", headers=headers, params=params)
    return response.json()
