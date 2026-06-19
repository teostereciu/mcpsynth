"""Shopify Admin REST API — Customers and Customer Addresses tools."""
import os, requests
from typing import Optional, Any

BASE_URL = f"https://{os.environ.get('SHOPIFY_STORE_URL', '')}/admin/api/2026-01"

def _headers():
    return {
        "X-Shopify-Access-Token": os.environ.get("SHOPIFY_ACCESS_TOKEN", ""),
        "Content-Type": "application/json",
    }

def _get(path, params=None):
    try:
        r = requests.get(f"{BASE_URL}{path}", headers=_headers(), params=params, timeout=30)
        return r.json()
    except Exception as e:
        return {"error": str(e)}

def _post(path, payload):
    try:
        r = requests.post(f"{BASE_URL}{path}", headers=_headers(), json=payload, timeout=30)
        return r.json()
    except Exception as e:
        return {"error": str(e)}

def _put(path, payload):
    try:
        r = requests.put(f"{BASE_URL}{path}", headers=_headers(), json=payload, timeout=30)
        return r.json()
    except Exception as e:
        return {"error": str(e)}

def _delete(path):
    try:
        r = requests.delete(f"{BASE_URL}{path}", headers=_headers(), timeout=30)
        if r.status_code == 200:
            return r.json()
        return {"status": r.status_code}
    except Exception as e:
        return {"error": str(e)}


# ── Customers ─────────────────────────────────────────────────────────────────

def list_customers(limit: int = 50, ids: Optional[str] = None,
                   created_at_min: Optional[str] = None,
                   created_at_max: Optional[str] = None,
                   updated_at_min: Optional[str] = None) -> dict:
    """Retrieve a list of customers."""
    params: dict[str, Any] = {"limit": limit}
    if ids: params["ids"] = ids
    if created_at_min: params["created_at_min"] = created_at_min
    if created_at_max: params["created_at_max"] = created_at_max
    if updated_at_min: params["updated_at_min"] = updated_at_min
    return _get("/customers.json", params)

def get_customer(customer_id: int) -> dict:
    """Retrieve a single customer by ID."""
    return _get(f"/customers/{customer_id}.json")

def count_customers() -> dict:
    """Retrieve a count of customers."""
    return _get("/customers/count.json")

def search_customers(query: str, limit: int = 50) -> dict:
    """Search for customers matching a query (e.g. 'email:bob@example.com')."""
    return _get("/customers/search.json", {"query": query, "limit": limit})

def create_customer(first_name: Optional[str] = None, last_name: Optional[str] = None,
                    email: Optional[str] = None, phone: Optional[str] = None,
                    note: Optional[str] = None, tags: Optional[str] = None,
                    addresses: Optional[list] = None,
                    tax_exempt: bool = False,
                    verified_email: bool = False,
                    send_email_welcome: bool = False) -> dict:
    """Create a new customer."""
    customer: dict[str, Any] = {
        "tax_exempt": tax_exempt,
        "verified_email": verified_email,
        "send_email_welcome": send_email_welcome,
    }
    if first_name: customer["first_name"] = first_name
    if last_name: customer["last_name"] = last_name
    if email: customer["email"] = email
    if phone: customer["phone"] = phone
    if note: customer["note"] = note
    if tags: customer["tags"] = tags
    if addresses: customer["addresses"] = addresses
    return _post("/customers.json", {"customer": customer})

def update_customer(customer_id: int, first_name: Optional[str] = None,
                    last_name: Optional[str] = None, email: Optional[str] = None,
                    phone: Optional[str] = None, note: Optional[str] = None,
                    tags: Optional[str] = None, tax_exempt: Optional[bool] = None) -> dict:
    """Update an existing customer."""
    customer: dict[str, Any] = {"id": customer_id}
    if first_name is not None: customer["first_name"] = first_name
    if last_name is not None: customer["last_name"] = last_name
    if email is not None: customer["email"] = email
    if phone is not None: customer["phone"] = phone
    if note is not None: customer["note"] = note
    if tags is not None: customer["tags"] = tags
    if tax_exempt is not None: customer["tax_exempt"] = tax_exempt
    return _put(f"/customers/{customer_id}.json", {"customer": customer})

def get_customer_orders(customer_id: int, status: Optional[str] = None) -> dict:
    """Retrieve all orders that belong to a customer."""
    params: dict[str, Any] = {}
    if status: params["status"] = status
    return _get(f"/customers/{customer_id}/orders.json", params)

def create_customer_activation_url(customer_id: int) -> dict:
    """Create an account activation URL for a customer."""
    return _post(f"/customers/{customer_id}/account_activation_url.json", {})

def send_customer_invite(customer_id: int, to: Optional[str] = None,
                         subject: Optional[str] = None,
                         custom_message: Optional[str] = None) -> dict:
    """Send an account invite to a customer."""
    invite: dict[str, Any] = {}
    if to: invite["to"] = to
    if subject: invite["subject"] = subject
    if custom_message: invite["custom_message"] = custom_message
    return _post(f"/customers/{customer_id}/send_invite.json",
                 {"customer_invite": invite})


# ── Customer Addresses ────────────────────────────────────────────────────────

def list_customer_addresses(customer_id: int, limit: int = 50) -> dict:
    """Retrieve a list of addresses for a customer."""
    return _get(f"/customers/{customer_id}/addresses.json", {"limit": limit})

def get_customer_address(customer_id: int, address_id: int) -> dict:
    """Retrieve a single customer address."""
    return _get(f"/customers/{customer_id}/addresses/{address_id}.json")

def create_customer_address(customer_id: int, address1: str,
                            city: Optional[str] = None, country: Optional[str] = None,
                            zip: Optional[str] = None, first_name: Optional[str] = None,
                            last_name: Optional[str] = None, company: Optional[str] = None,
                            phone: Optional[str] = None, province: Optional[str] = None,
                            address2: Optional[str] = None,
                            country_code: Optional[str] = None,
                            province_code: Optional[str] = None) -> dict:
    """Create a new address for a customer."""
    address: dict[str, Any] = {"address1": address1}
    if city: address["city"] = city
    if country: address["country"] = country
    if zip: address["zip"] = zip
    if first_name: address["first_name"] = first_name
    if last_name: address["last_name"] = last_name
    if company: address["company"] = company
    if phone: address["phone"] = phone
    if province: address["province"] = province
    if address2: address["address2"] = address2
    if country_code: address["country_code"] = country_code
    if province_code: address["province_code"] = province_code
    return _post(f"/customers/{customer_id}/addresses.json", {"address": address})

def update_customer_address(customer_id: int, address_id: int,
                            address1: Optional[str] = None,
                            city: Optional[str] = None, country: Optional[str] = None,
                            zip: Optional[str] = None, phone: Optional[str] = None,
                            province: Optional[str] = None) -> dict:
    """Update an existing customer address."""
    address: dict[str, Any] = {}
    if address1: address["address1"] = address1
    if city: address["city"] = city
    if country: address["country"] = country
    if zip: address["zip"] = zip
    if phone: address["phone"] = phone
    if province: address["province"] = province
    return _put(f"/customers/{customer_id}/addresses/{address_id}.json",
                {"address": address})

def set_default_customer_address(customer_id: int, address_id: int) -> dict:
    """Set the default address for a customer."""
    return _put(f"/customers/{customer_id}/addresses/{address_id}/default.json", {})

def delete_customer_address(customer_id: int, address_id: int) -> dict:
    """Remove an address from a customer's address list."""
    return _delete(f"/customers/{customer_id}/addresses/{address_id}.json")
