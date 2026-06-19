import os
import requests
from mcp_tools import mcp_tool

BASE_URL = "https://api.stripe.com/v1"
API_KEY = os.environ.get("STRIPE_API_KEY")
HEADERS = {"Authorization": f"Bearer {API_KEY}"}

def _handle_response(resp):
    try:
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError:
        try:
            return {"error": resp.json()}
        except Exception:
            return {"error": resp.text}

@mcp_tool
def create_customer(email: str = None, name: str = None, description: str = None, phone: str = None, metadata: dict = None, address: dict = None, shipping: dict = None):
    """
    Create a Customer object.
    Optional: email, name, description, phone, metadata, address, shipping
    """
    url = f"{BASE_URL}/customers"
    data = {}
    if email:
        data["email"] = email
    if name:
        data["name"] = name
    if description:
        data["description"] = description
    if phone:
        data["phone"] = phone
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    if address:
        for k, v in address.items():
            data[f"address[{k}]"] = v
    if shipping:
        for k, v in shipping.items():
            data[f"shipping[{k}]"] = v
    resp = requests.post(url, headers=HEADERS, data=data)
    return _handle_response(resp)

@mcp_tool
def retrieve_customer(customer_id: str):
    """
    Retrieve a Customer object by ID.
    """
    url = f"{BASE_URL}/customers/{customer_id}"
    resp = requests.get(url, headers=HEADERS)
    return _handle_response(resp)

@mcp_tool
def update_customer(customer_id: str, email: str = None, name: str = None, description: str = None, phone: str = None, metadata: dict = None, address: dict = None, shipping: dict = None):
    """
    Update a Customer object. Optional fields: email, name, description, phone, metadata, address, shipping
    """
    url = f"{BASE_URL}/customers/{customer_id}"
    data = {}
    if email:
        data["email"] = email
    if name:
        data["name"] = name
    if description:
        data["description"] = description
    if phone:
        data["phone"] = phone
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    if address:
        for k, v in address.items():
            data[f"address[{k}]"] = v
    if shipping:
        for k, v in shipping.items():
            data[f"shipping[{k}]"] = v
    resp = requests.post(url, headers=HEADERS, data=data)
    return _handle_response(resp)
