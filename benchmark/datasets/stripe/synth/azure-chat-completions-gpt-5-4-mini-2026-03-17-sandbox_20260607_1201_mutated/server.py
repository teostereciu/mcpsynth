from __future__ import annotations

import os
from typing import Any, Dict, Optional

import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("stripe")
BASE_URL = "https://api.stripe.com"
API_KEY = os.environ.get("STRIPE_API_KEY", "")


def _client() -> httpx.Client:
    headers = {"Authorization": f"Bearer {API_KEY}"} if API_KEY else {}
    return httpx.Client(base_url=BASE_URL, headers=headers, timeout=60.0)


def _request(method: str, path: str, data: Optional[Dict[str, Any]] = None) -> Any:
    with _client() as client:
        resp = client.request(method, path, data=data)
        resp.raise_for_status()
        return resp.json()


@mcp.tool()
def create_customer(name: str, email: Optional[str] = None, description: Optional[str] = None, metadata: Optional[Dict[str, str]] = None) -> Any:
    data: Dict[str, Any] = {"name": name}
    if email is not None:
        data["email"] = email
    if description is not None:
        data["description"] = description
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    return _request("POST", "/v1/customers", data)


@mcp.tool()
def update_customer(customer_id: str, name: Optional[str] = None, email: Optional[str] = None, description: Optional[str] = None, metadata: Optional[Dict[str, str]] = None) -> Any:
    data: Dict[str, Any] = {}
    if name is not None:
        data["name"] = name
    if email is not None:
        data["email"] = email
    if description is not None:
        data["description"] = description
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    return _request("POST", f"/v1/customers/{customer_id}", data)


@mcp.tool()
def retrieve_customer(customer_id: str) -> Any:
    return _request("GET", f"/v1/customers/{customer_id}")


@mcp.tool()
def create_product(name: str, active: Optional[bool] = None, description: Optional[str] = None, metadata: Optional[Dict[str, str]] = None) -> Any:
    data: Dict[str, Any] = {"name": name}
    if active is not None:
        data["active"] = active
    if description is not None:
        data["description"] = description
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    return _request("POST", "/v1/products", data)


@mcp.tool()
def update_product(product_id: str, active: Optional[bool] = None, default_price: Optional[str] = None, description: Optional[str] = None, metadata: Optional[Dict[str, str]] = None) -> Any:
    data: Dict[str, Any] = {}
    if active is not None:
        data["active"] = active
    if default_price is not None:
        data["default_price"] = default_price
    if description is not None:
        data["description"] = description
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    return _request("POST", f"/v1/products/{product_id}", data)


@mcp.tool()
def retrieve_product(product_id: str) -> Any:
    return _request("GET", f"/v1/products/{product_id}")


@mcp.tool()
def create_price(currency: str, product: str, unit_amount: Optional[int] = None, nickname: Optional[str] = None, active: Optional[bool] = None, metadata: Optional[Dict[str, str]] = None) -> Any:
    data: Dict[str, Any] = {"currency": currency, "product": product}
    if unit_amount is not None:
        data["unit_amount"] = unit_amount
    if nickname is not None:
        data["nickname"] = nickname
    if active is not None:
        data["active"] = active
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    return _request("POST", "/v1/prices", data)


@mcp.tool()
def update_price(price_id: str, active: Optional[bool] = None, nickname: Optional[str] = None, metadata: Optional[Dict[str, str]] = None) -> Any:
    data: Dict[str, Any] = {}
    if active is not None:
        data["active"] = active
    if nickname is not None:
        data["nickname"] = nickname
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    return _request("POST", f"/v1/prices/{price_id}", data)


@mcp.tool()
def retrieve_price(price_id: str) -> Any:
    return _request("GET", f"/v1/prices/{price_id}")


@mcp.tool()
def create_payment_intent(amount: int, currency: str, customer: Optional[str] = None, description: Optional[str] = None, payment_method: Optional[str] = None, confirm: Optional[bool] = None, metadata: Optional[Dict[str, str]] = None) -> Any:
    data: Dict[str, Any] = {"amount": amount, "currency": currency}
    if customer is not None:
        data["customer"] = customer
    if description is not None:
        data["description"] = description
    if payment_method is not None:
        data["payment_method"] = payment_method
    if confirm is not None:
        data["confirm"] = confirm
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    return _request("POST", "/v1/payment_intents", data)


@mcp.tool()
def update_payment_intent(payment_intent_id: str, description: Optional[str] = None, metadata: Optional[Dict[str, str]] = None) -> Any:
    data: Dict[str, Any] = {}
    if description is not None:
        data["description"] = description
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    return _request("POST", f"/v1/payment_intents/{payment_intent_id}", data)


@mcp.tool()
def retrieve_payment_intent(payment_intent_id: str) -> Any:
    return _request("GET", f"/v1/payment_intents/{payment_intent_id}")


@mcp.tool()
def create_charge(amount: int, currency: str, source: str, customer: Optional[str] = None, description: Optional[str] = None, receipt_email: Optional[str] = None, metadata: Optional[Dict[str, str]] = None) -> Any:
    data: Dict[str, Any] = {"amount": amount, "currency": currency, "source": source}
    if customer is not None:
        data["customer"] = customer
    if description is not None:
        data["description"] = description
    if receipt_email is not None:
        data["receipt_email"] = receipt_email
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    return _request("POST", "/v1/charges", data)


@mcp.tool()
def update_charge(charge_id: str, customer: Optional[str] = None, description: Optional[str] = None, receipt_email: Optional[str] = None, metadata: Optional[Dict[str, str]] = None) -> Any:
    data: Dict[str, Any] = {}
    if customer is not None:
        data["customer"] = customer
    if description is not None:
        data["description"] = description
    if receipt_email is not None:
        data["receipt_email"] = receipt_email
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    return _request("POST", f"/v1/charges/{charge_id}", data)


@mcp.tool()
def retrieve_charge(charge_id: str) -> Any:
    return _request("GET", f"/v1/charges/{charge_id}")


@mcp.tool()
def create_refund(charge: Optional[str] = None, payment_intent: Optional[str] = None, amount: Optional[int] = None, reason: Optional[str] = None, metadata: Optional[Dict[str, str]] = None) -> Any:
    data: Dict[str, Any] = {}
    if charge is not None:
        data["charge"] = charge
    if payment_intent is not None:
        data["payment_intent"] = payment_intent
    if amount is not None:
        data["amount"] = amount
    if reason is not None:
        data["reason"] = reason
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    return _request("POST", "/v1/refunds", data)


@mcp.tool()
def update_refund(refund_id: str, metadata: Optional[Dict[str, str]] = None) -> Any:
    data: Dict[str, Any] = {}
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    return _request("POST", f"/v1/refunds/{refund_id}", data)


@mcp.tool()
def retrieve_refund(refund_id: str) -> Any:
    return _request("GET", f"/v1/refunds/{refund_id}")


if __name__ == "__main__":
    mcp.run()
