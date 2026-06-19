import os
import requests
from fastmcp import tool

STRIPE_API_KEY = os.environ.get("STRIPE_API_KEY")
BASE_URL = "https://api.stripe.com/v1"
HEADERS = {
    "Authorization": f"Bearer {STRIPE_API_KEY}",
    "Content-Type": "application/x-www-form-urlencoded"
}

@tool("create_customer")
def create_customer(address: dict = None, description: str = None, email: str = None, metadata: dict = None, name: str = None, payment_method: str = None, phone: str = None, shipping: dict = None, tax: dict = None):
    """
    Create a Customer object.
    """
    data = {}
    if address:
        for k, v in address.items():
            data[f"address[{k}]"] = v
    if description:
        data["description"] = description
    if email:
        data["email"] = email
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    if name:
        data["name"] = name
    if payment_method:
        data["payment_method"] = payment_method
    if phone:
        data["phone"] = phone
    if shipping:
        for k, v in shipping.items():
            data[f"shipping[{k}]"] = v
    if tax:
        for k, v in tax.items():
            data[f"tax[{k}]"] = v
    try:
        resp = requests.post(f"{BASE_URL}/customers", data=data, headers=HEADERS)
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": str(e), "details": resp.text}

@tool("retrieve_customer")
def retrieve_customer(customer_id: str):
    """
    Retrieve a Customer object.
    """
    try:
        resp = requests.get(f"{BASE_URL}/customers/{customer_id}", headers=HEADERS)
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": str(e), "details": resp.text}

@tool("update_customer")
def update_customer(customer_id: str, address: dict = None, description: str = None, email: str = None, metadata: dict = None, name: str = None, phone: str = None, shipping: dict = None, tax: dict = None):
    """
    Update a Customer object.
    """
    data = {}
    if address:
        for k, v in address.items():
            data[f"address[{k}]"] = v
    if description:
        data["description"] = description
    if email:
        data["email"] = email
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    if name:
        data["name"] = name
    if phone:
        data["phone"] = phone
    if shipping:
        for k, v in shipping.items():
            data[f"shipping[{k}]"] = v
    if tax:
        for k, v in tax.items():
            data[f"tax[{k}]"] = v
    try:
        resp = requests.post(f"{BASE_URL}/customers/{customer_id}", data=data, headers=HEADERS)
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": str(e), "details": resp.text}
