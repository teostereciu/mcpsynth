import os
from typing import Any, Dict

import requests
from mcp.server.fastmcp import FastMCP

BASE_URL = "https://api.stripe.com/v1"
API_KEY = os.environ.get("STRIPE_API_KEY", "")

mcp = FastMCP("stripe")


def _headers() -> Dict[str, str]:
    return {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/x-www-form-urlencoded",
    }


def _request(method: str, path: str, data: Dict[str, Any] | None = None) -> Dict[str, Any]:
    if not API_KEY:
        return {"error": "STRIPE_API_KEY is not set"}
    try:
        resp = requests.request(method, f"{BASE_URL}{path}", headers=_headers(), data=data, timeout=30)
        payload = resp.json() if resp.content else {}
        if resp.status_code >= 400:
            if isinstance(payload, dict) and "error" in payload:
                return {"error": payload["error"].get("message", "Stripe API error"), "details": payload["error"]}
            return {"error": f"Stripe API error ({resp.status_code})", "details": payload}
        return payload
    except requests.RequestException as e:
        return {"error": str(e)}


@mcp.tool()
def create_customer(name: str, email: str | None = None, description: str | None = None) -> Dict[str, Any]:
    data: Dict[str, Any] = {"name": name}
    if email is not None:
        data["email"] = email
    if description is not None:
        data["description"] = description
    return _request("POST", "/customers", data)


@mcp.tool()
def update_customer(customer_id: str, name: str | None = None, email: str | None = None, description: str | None = None, metadata: Dict[str, Any] | None = None) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    for k, v in {"name": name, "email": email, "description": description}.items():
        if v is not None:
            data[k] = v
    if metadata is not None:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    return _request("POST", f"/customers/{customer_id}", data)


@mcp.tool()
def retrieve_customer(customer_id: str) -> Dict[str, Any]:
    return _request("GET", f"/customers/{customer_id}")


@mcp.tool()
def create_product(name: str, active: bool | None = None, description: str | None = None) -> Dict[str, Any]:
    data: Dict[str, Any] = {"name": name}
    if active is not None:
        data["active"] = active
    if description is not None:
        data["description"] = description
    return _request("POST", "/products", data)


@mcp.tool()
def update_product(product_id: str, name: str | None = None, active: bool | None = None, description: str | None = None, metadata: Dict[str, Any] | None = None) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    for k, v in {"name": name, "active": active, "description": description}.items():
        if v is not None:
            data[k] = v
    if metadata is not None:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    return _request("POST", f"/products/{product_id}", data)


@mcp.tool()
def retrieve_product(product_id: str) -> Dict[str, Any]:
    return _request("GET", f"/products/{product_id}")


@mcp.tool()
def create_price(currency: str, unit_amount: int, product: str, nickname: str | None = None, active: bool | None = None) -> Dict[str, Any]:
    data: Dict[str, Any] = {"currency": currency, "unit_amount": unit_amount, "product": product}
    if nickname is not None:
        data["nickname"] = nickname
    if active is not None:
        data["active"] = active
    return _request("POST", "/prices", data)


@mcp.tool()
def update_price(price_id: str, nickname: str | None = None, active: bool | None = None, metadata: Dict[str, Any] | None = None) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    if nickname is not None:
        data["nickname"] = nickname
    if active is not None:
        data["active"] = active
    if metadata is not None:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    return _request("POST", f"/prices/{price_id}", data)


@mcp.tool()
def retrieve_price(price_id: str) -> Dict[str, Any]:
    return _request("GET", f"/prices/{price_id}")


if __name__ == "__main__":
    mcp.run()
