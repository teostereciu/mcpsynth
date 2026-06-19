import json
import os
from typing import Any, Dict, Optional

import requests
from fastmcp import FastMCP

mcp = FastMCP("ebay-sell-api")

BASE_URLS = {
    "SANDBOX": "https://api.sandbox.ebay.com",
    "PRODUCTION": "https://api.ebay.com",
}


def _env() -> str:
    return os.getenv("EBAY_ENVIRONMENT", "SANDBOX").upper()


def _base_url() -> str:
    return BASE_URLS.get(_env(), BASE_URLS["SANDBOX"])


def _token() -> Dict[str, Any]:
    app_id = os.getenv("EBAY_APP_ID")
    cert_id = os.getenv("EBAY_CERT_ID")
    refresh_token = os.getenv("EBAY_REFRESH_TOKEN")
    if not app_id or not cert_id or not refresh_token:
        return {"error": "Missing EBAY_APP_ID, EBAY_CERT_ID, or EBAY_REFRESH_TOKEN"}
    url = f"{_base_url()}/identity/v1/oauth2/token"
    auth = (app_id, cert_id)
    data = {"grant_type": "refresh_token", "refresh_token": refresh_token}
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    resp = requests.post(url, auth=auth, data=data, headers=headers, timeout=30)
    if not resp.ok:
        return {"error": f"Token request failed: {resp.status_code}", "details": resp.text}
    return resp.json()


def _request(method: str, path: str, *, params: Optional[dict] = None, json_body: Any = None) -> Dict[str, Any]:
    token = _token()
    if "error" in token:
        return token
    access_token = token.get("access_token")
    if not access_token:
        return {"error": "No access_token in token response", "details": token}
    url = f"{_base_url()}{path}"
    headers = {"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"}
    resp = requests.request(method, url, params=params, json=json_body, headers=headers, timeout=30)
    if resp.status_code == 404:
        return {"error": "Not found", "status": 404}
    if not resp.ok:
        try:
            details = resp.json()
        except Exception:
            details = resp.text
        return {"error": f"Request failed: {resp.status_code}", "details": details}
    if resp.text:
        try:
            return resp.json()
        except Exception:
            return {"result": resp.text}
    return {}


@mcp.tool()
def get_orders(limit: int = 50) -> Dict[str, Any]:
    return _request("GET", "/sell/fulfillment/v1/order", params={"limit": limit})


@mcp.tool()
def get_inventory_items(limit: int = 50) -> Dict[str, Any]:
    return _request("GET", "/sell/inventory/v1/inventory_item", params={"limit": limit})


@mcp.tool()
def get_offers(limit: int = 50) -> Dict[str, Any]:
    return _request("GET", "/sell/inventory/v1/offer", params={"limit": limit})


@mcp.tool()
def get_listing_fees(sku: str) -> Dict[str, Any]:
    return _request("GET", "/sell/inventory/v1/offer", params={"sku": sku})


@mcp.tool()
def get_policies() -> Dict[str, Any]:
    return _request("GET", "/sell/account/v1/fulfillment_policy")


if __name__ == "__main__":
    mcp.run(transport="stdio")
