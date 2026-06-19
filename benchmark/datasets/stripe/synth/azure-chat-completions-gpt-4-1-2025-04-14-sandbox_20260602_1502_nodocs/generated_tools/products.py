import os
import requests
from typing import Optional, Dict, Any

STRIPE_API_KEY = os.environ.get("STRIPE_API_KEY")
BASE_URL = "https://api.stripe.com/v1"
HEADERS = {"Authorization": f"Bearer {STRIPE_API_KEY}"}

def create_product(name: str, **kwargs) -> Dict[str, Any]:
    """
    Create a Product object.
    Args:
        name: Name of the product.
        kwargs: Additional Stripe parameters (e.g. description, metadata, etc.)
    Returns:
        JSON response from Stripe or error dict.
    """
    data = {"name": name}
    data.update(kwargs)
    try:
        resp = requests.post(f"{BASE_URL}/products", data=data, headers=HEADERS)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

def retrieve_product(product_id: str) -> Dict[str, Any]:
    """
    Retrieve a Product object.
    Args:
        product_id: The ID of the Product.
    Returns:
        JSON response from Stripe or error dict.
    """
    try:
        resp = requests.get(f"{BASE_URL}/products/{product_id}", headers=HEADERS)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

def update_product(product_id: str, **kwargs) -> Dict[str, Any]:
    """
    Update a Product object.
    Args:
        product_id: The ID of the Product.
        kwargs: Fields to update.
    Returns:
        JSON response from Stripe or error dict.
    """
    try:
        resp = requests.post(f"{BASE_URL}/products/{product_id}", data=kwargs, headers=HEADERS)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

def delete_product(product_id: str) -> Dict[str, Any]:
    """
    Delete a Product object.
    Args:
        product_id: The ID of the Product.
    Returns:
        JSON response from Stripe or error dict.
    """
    try:
        resp = requests.delete(f"{BASE_URL}/products/{product_id}", headers=HEADERS)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}
