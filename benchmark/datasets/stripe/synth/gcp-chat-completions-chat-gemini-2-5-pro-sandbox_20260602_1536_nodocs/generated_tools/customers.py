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
def create_customer(email: str, name: str = None, description: str = None):
    """Create a new customer.

    Args:
        email: The customer's email address.
        name: The customer's full name or business name.
        description: An arbitrary string that you can attach to a customer object.
    """
    data = {"email": email}
    if name:
        data["name"] = name
    if description:
        data["description"] = description
    
    response = requests.post(f"{base_url}/customers", headers=headers, data=data)
    return response.json()

@tool
def retrieve_customer(customer_id: str):
    """Retrieves the details of an existing customer.

    Args:
        customer_id: The ID of the customer to retrieve.
    """
    response = requests.get(f"{base_url}/customers/{customer_id}", headers=headers)
    return response.json()

@tool
def update_customer(customer_id: str, email: str = None, name: str = None, description: str = None):
    """Updates the specified customer by setting the values of the parameters passed.

    Args:
        customer_id: The ID of the customer to update.
        email: The customer's email address.
        name: The customer's full name or business name.
        description: An arbitrary string that you can attach to a customer object.
    """
    data = {}
    if email:
        data["email"] = email
    if name:
        data["name"] = name
    if description:
        data["description"] = description

    response = requests.post(f"{base_url}/customers/{customer_id}", headers=headers, data=data)
    return response.json()

@tool
def delete_customer(customer_id: str):
    """Deletes a customer object.

    Args:
        customer_id: The ID of the customer to delete.
    """
    response = requests.delete(f"{base_url}/customers/{customer_id}", headers=headers)
    return response.json()

@tool
def list_customers(limit: int = 10, starting_after: str = None, ending_before: str = None):
    """Returns a list of your customers.

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

    response = requests.get(f"{base_url}/customers", headers=headers, params=params)
    return response.json()
