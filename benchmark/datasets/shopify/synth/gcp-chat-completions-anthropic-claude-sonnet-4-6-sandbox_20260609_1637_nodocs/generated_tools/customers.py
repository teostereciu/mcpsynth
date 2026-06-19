"""Shopify Admin REST API — Customers tools."""

import os, requests
from mcp.server.fastmcp import FastMCP

def _session():
    token = os.environ["SHOPIFY_ACCESS_TOKEN"]
    store = os.environ["SHOPIFY_STORE_URL"]
    base  = f"https://{store}/admin/api/2026-01"
    s = requests.Session()
    s.headers.update({"X-Shopify-Access-Token": token, "Content-Type": "application/json"})
    return s, base

def register(mcp: FastMCP):

    @mcp.tool()
    def list_customers(limit: int = 50, page_info: str = "") -> dict:
        """List customers in the store."""
        s, base = _session()
        params: dict = {"limit": limit}
        if page_info:
            params["page_info"] = page_info
        r = s.get(f"{base}/customers.json", params=params)
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def search_customers(query: str, limit: int = 50) -> dict:
        """Search customers by name, email, phone, etc."""
        s, base = _session()
        r = s.get(f"{base}/customers/search.json",
                  params={"query": query, "limit": limit})
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def get_customer(customer_id: str) -> dict:
        """Get a single customer by ID."""
        s, base = _session()
        r = s.get(f"{base}/customers/{customer_id}.json")
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def create_customer(first_name: str, last_name: str, email: str = "",
                        phone: str = "", tags: str = "",
                        accepts_marketing: bool = False,
                        addresses: list = []) -> dict:
        """Create a new customer."""
        s, base = _session()
        data: dict = {"first_name": first_name, "last_name": last_name,
                      "accepts_marketing": accepts_marketing}
        if email:     data["email"]     = email
        if phone:     data["phone"]     = phone
        if tags:      data["tags"]      = tags
        if addresses: data["addresses"] = addresses
        r = s.post(f"{base}/customers.json", json={"customer": data})
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def update_customer(customer_id: str, first_name: str = "", last_name: str = "",
                        email: str = "", phone: str = "", tags: str = "",
                        accepts_marketing: bool = None, note: str = "") -> dict:
        """Update an existing customer."""
        s, base = _session()
        data: dict = {}
        if first_name:              data["first_name"]         = first_name
        if last_name:               data["last_name"]          = last_name
        if email:                   data["email"]              = email
        if phone:                   data["phone"]              = phone
        if tags:                    data["tags"]               = tags
        if accepts_marketing is not None:
            data["accepts_marketing"] = accepts_marketing
        if note:                    data["note"]               = note
        r = s.put(f"{base}/customers/{customer_id}.json", json={"customer": data})
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def delete_customer(customer_id: str) -> dict:
        """Delete a customer."""
        s, base = _session()
        r = s.delete(f"{base}/customers/{customer_id}.json")
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return {"deleted": True, "customer_id": customer_id}

    @mcp.tool()
    def count_customers() -> dict:
        """Count all customers in the store."""
        s, base = _session()
        r = s.get(f"{base}/customers/count.json")
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def list_customer_orders(customer_id: str, status: str = "any") -> dict:
        """List all orders for a specific customer."""
        s, base = _session()
        r = s.get(f"{base}/customers/{customer_id}/orders.json",
                  params={"status": status})
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def list_customer_addresses(customer_id: str) -> dict:
        """List all addresses for a customer."""
        s, base = _session()
        r = s.get(f"{base}/customers/{customer_id}/addresses.json")
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def create_customer_address(customer_id: str, address1: str, city: str,
                                country: str, zip: str = "", province: str = "",
                                first_name: str = "", last_name: str = "",
                                phone: str = "") -> dict:
        """Add a new address to a customer."""
        s, base = _session()
        data: dict = {"address1": address1, "city": city, "country": country}
        if zip:        data["zip"]        = zip
        if province:   data["province"]   = province
        if first_name: data["first_name"] = first_name
        if last_name:  data["last_name"]  = last_name
        if phone:      data["phone"]      = phone
        r = s.post(f"{base}/customers/{customer_id}/addresses.json",
                   json={"address": data})
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def delete_customer_address(customer_id: str, address_id: str) -> dict:
        """Delete a customer address."""
        s, base = _session()
        r = s.delete(f"{base}/customers/{customer_id}/addresses/{address_id}.json")
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return {"deleted": True, "address_id": address_id}

    @mcp.tool()
    def set_default_customer_address(customer_id: str, address_id: str) -> dict:
        """Set a customer's default address."""
        s, base = _session()
        r = s.put(f"{base}/customers/{customer_id}/addresses/{address_id}/default.json")
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()
