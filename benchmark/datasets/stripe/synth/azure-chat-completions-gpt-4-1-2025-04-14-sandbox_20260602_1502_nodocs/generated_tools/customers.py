import os
import requests
from typing import Optional, Dict, Any

STRIPE_API_KEY = os.environ.get("STRIPE_API_KEY")
BASE_URL = "https://api.stripe.com/v1"
HEADERS = {"Authorization": f"Bearer {STRIPE_API_KEY}"}

def create_customer(email: Optional[str] = None, **kwargs) -> Dict[str, Any]:
    """
    Create a Customer object.
    Args:
        email: Customer's email address (optional).
        kwargs: Additional Stripe parameters (e.g. name, description, etc.)
    Returns:
        JSON response from Stripe or error dict.
    """
    data = {}
    if email:
        data["email"] = email
    data.update(kwargs)
    try:
        resp = requests.post(f"{BASE_URL}/customers", data=data, headers=HEADERS)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

def retrieve_customer(customer_id: str) -> Dict[str, Any]:
    """
    Retrieve a Customer object.
    Args:
        customer_id: The ID of the Customer.
    Returns:
        JSON response from Stripe or error dict.
    """
    try:
        resp = requests.get(f"{BASE_URL}/customers/{customer_id}", headers=HEADERS)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

def update_customer(customer_id: str, **kwargs) -> Dict[str, Any]:
    """
    Update a Customer object.
    Args:
        customer_id: The ID of the Customer.
        kwargs: Fields to update.
    Returns:
        JSON response from Stripe or error dict.
    """
    try:
        resp = requests.post(f"{BASE_URL}/customers/{customer_id}", data=kwargs, headers=HEADERS)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

def delete_customer(customer_id: str) -> Dict[str, Any]:
    """
    Delete a Customer object.
    Args:
        customer_id: The ID of the Customer.
    Returns:
        JSON response from Stripe or error dict.
    """
    try:
        resp = requests.delete(f"{BASE_URL}/customers/{customer_id}", headers=HEADERS)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}
