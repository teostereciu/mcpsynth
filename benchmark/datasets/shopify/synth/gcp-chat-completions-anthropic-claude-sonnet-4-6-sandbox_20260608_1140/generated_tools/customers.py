"""Shopify Admin REST API — Customers, Customer Addresses tools."""
import os, requests
from mcp.server.fastmcp import FastMCP

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

def _post(path, body=None):
    try:
        r = requests.post(f"{BASE_URL}{path}", headers=_headers(), json=body, timeout=30)
        return r.json()
    except Exception as e:
        return {"error": str(e)}

def _put(path, body):
    try:
        r = requests.put(f"{BASE_URL}{path}", headers=_headers(), json=body, timeout=30)
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


def register_customers(mcp: FastMCP):

    # ── Customers ─────────────────────────────────────────────────────────────

    @mcp.tool()
    def list_customers(
        limit: int = 50,
        ids: str = None,
        since_id: int = None,
        created_at_min: str = None,
        created_at_max: str = None,
        fields: str = None,
    ) -> dict:
        """Retrieve a list of customers."""
        params = {"limit": limit}
        if ids: params["ids"] = ids
        if since_id: params["since_id"] = since_id
        if created_at_min: params["created_at_min"] = created_at_min
        if created_at_max: params["created_at_max"] = created_at_max
        if fields: params["fields"] = fields
        return _get("/customers.json", params)

    @mcp.tool()
    def get_customer(customer_id: int, fields: str = None) -> dict:
        """Retrieve a single customer by ID."""
        params = {}
        if fields: params["fields"] = fields
        return _get(f"/customers/{customer_id}.json", params)

    @mcp.tool()
    def search_customers(query: str, limit: int = 50, fields: str = None) -> dict:
        """Search for customers matching a query. e.g. query='email:bob@example.com'."""
        params = {"query": query, "limit": limit}
        if fields: params["fields"] = fields
        return _get("/customers/search.json", params)

    @mcp.tool()
    def count_customers() -> dict:
        """Retrieve a count of customers."""
        return _get("/customers/count.json")

    @mcp.tool()
    def create_customer(
        first_name: str = None,
        last_name: str = None,
        email: str = None,
        phone: str = None,
        note: str = None,
        tags: str = None,
        verified_email: bool = True,
        accepts_marketing: bool = False,
        addresses: list = None,
        tax_exempt: bool = False,
    ) -> dict:
        """Create a new customer."""
        customer = {"verified_email": verified_email, "accepts_marketing": accepts_marketing, "tax_exempt": tax_exempt}
        if first_name: customer["first_name"] = first_name
        if last_name: customer["last_name"] = last_name
        if email: customer["email"] = email
        if phone: customer["phone"] = phone
        if note: customer["note"] = note
        if tags: customer["tags"] = tags
        if addresses: customer["addresses"] = addresses
        return _post("/customers.json", {"customer": customer})

    @mcp.tool()
    def update_customer(
        customer_id: int,
        first_name: str = None,
        last_name: str = None,
        email: str = None,
        phone: str = None,
        note: str = None,
        tags: str = None,
        accepts_marketing: bool = None,
        tax_exempt: bool = None,
    ) -> dict:
        """Update an existing customer."""
        customer = {}
        if first_name is not None: customer["first_name"] = first_name
        if last_name is not None: customer["last_name"] = last_name
        if email is not None: customer["email"] = email
        if phone is not None: customer["phone"] = phone
        if note is not None: customer["note"] = note
        if tags is not None: customer["tags"] = tags
        if accepts_marketing is not None: customer["accepts_marketing"] = accepts_marketing
        if tax_exempt is not None: customer["tax_exempt"] = tax_exempt
        return _put(f"/customers/{customer_id}.json", {"customer": customer})

    @mcp.tool()
    def get_customer_orders(customer_id: int, status: str = "any") -> dict:
        """Retrieve all orders that belong to a customer."""
        return _get(f"/customers/{customer_id}/orders.json", {"status": status})

    @mcp.tool()
    def create_customer_activation_url(customer_id: int) -> dict:
        """Create an account activation URL for a customer."""
        return _post(f"/customers/{customer_id}/account_activation_url.json", {})

    # ── Customer Addresses ────────────────────────────────────────────────────

    @mcp.tool()
    def list_customer_addresses(customer_id: int, limit: int = 50) -> dict:
        """Retrieve a list of addresses for a customer."""
        return _get(f"/customers/{customer_id}/addresses.json", {"limit": limit})

    @mcp.tool()
    def get_customer_address(customer_id: int, address_id: int) -> dict:
        """Retrieve details for a single customer address."""
        return _get(f"/customers/{customer_id}/addresses/{address_id}.json")

    @mcp.tool()
    def create_customer_address(
        customer_id: int,
        address1: str,
        city: str,
        country: str,
        first_name: str = None,
        last_name: str = None,
        address2: str = None,
        company: str = None,
        phone: str = None,
        province: str = None,
        zip: str = None,
        country_code: str = None,
        province_code: str = None,
    ) -> dict:
        """Create a new address for a customer."""
        address = {"address1": address1, "city": city, "country": country}
        if first_name: address["first_name"] = first_name
        if last_name: address["last_name"] = last_name
        if address2: address["address2"] = address2
        if company: address["company"] = company
        if phone: address["phone"] = phone
        if province: address["province"] = province
        if zip: address["zip"] = zip
        if country_code: address["country_code"] = country_code
        if province_code: address["province_code"] = province_code
        return _post(f"/customers/{customer_id}/addresses.json", {"address": address})

    @mcp.tool()
    def update_customer_address(
        customer_id: int,
        address_id: int,
        address1: str = None,
        city: str = None,
        country: str = None,
        first_name: str = None,
        last_name: str = None,
        phone: str = None,
        zip: str = None,
    ) -> dict:
        """Update an existing customer address."""
        address = {}
        if address1: address["address1"] = address1
        if city: address["city"] = city
        if country: address["country"] = country
        if first_name: address["first_name"] = first_name
        if last_name: address["last_name"] = last_name
        if phone: address["phone"] = phone
        if zip: address["zip"] = zip
        return _put(f"/customers/{customer_id}/addresses/{address_id}.json", {"address": address})

    @mcp.tool()
    def set_default_customer_address(customer_id: int, address_id: int) -> dict:
        """Set the default address for a customer."""
        return _put(f"/customers/{customer_id}/addresses/{address_id}/default.json", {})

    @mcp.tool()
    def delete_customer_address(customer_id: int, address_id: int) -> dict:
        """Remove an address from a customer's address list."""
        return _delete(f"/customers/{customer_id}/addresses/{address_id}.json")
