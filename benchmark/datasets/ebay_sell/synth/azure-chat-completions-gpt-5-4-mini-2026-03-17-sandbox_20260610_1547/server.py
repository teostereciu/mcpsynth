import base64
import json
import os
from typing import Any, Dict, Optional

import requests
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("ebay-sell-api")

BASE_URLS = {
    "SANDBOX": "https://api.sandbox.ebay.com",
    "PRODUCTION": "https://api.ebay.com",
}


def _base_url() -> str:
    return BASE_URLS.get(os.getenv("EBAY_ENVIRONMENT", "SANDBOX").upper(), BASE_URLS["SANDBOX"])


def _token() -> Dict[str, Any]:
    app_id = os.getenv("EBAY_APP_ID")
    cert_id = os.getenv("EBAY_CERT_ID")
    refresh_token = os.getenv("EBAY_REFRESH_TOKEN")
    if not app_id or not cert_id or not refresh_token:
        return {"error": "Missing EBAY_APP_ID, EBAY_CERT_ID, or EBAY_REFRESH_TOKEN"}
    basic = base64.b64encode(f"{app_id}:{cert_id}".encode()).decode()
    resp = requests.post(
        f"{_base_url()}/identity/v1/oauth2/token",
        headers={"Authorization": f"Basic {basic}", "Content-Type": "application/x-www-form-urlencoded"},
        data={"grant_type": "refresh_token", "refresh_token": refresh_token},
        timeout=30,
    )
    if resp.status_code >= 400:
        return {"error": "Token request failed", "status": resp.status_code, "details": resp.text}
    return resp.json()


def _request(method: str, path: str, *, params: Optional[dict] = None, json_body: Any = None, headers: Optional[dict] = None) -> Dict[str, Any]:
    tok = _token()
    if "error" in tok:
        return tok
    access_token = tok.get("access_token")
    if not access_token:
        return {"error": "No access token returned"}
    resp = requests.request(
        method,
        f"{_base_url()}{path}",
        params=params,
        json=json_body,
        headers={"Authorization": f"Bearer {access_token}", "Accept": "application/json", **(headers or {})},
        timeout=60,
    )
    if resp.status_code == 204:
        return {"status": 204}
    try:
        data = resp.json()
    except Exception:
        data = resp.text
    if resp.status_code >= 400:
        return {"error": "API request failed", "status": resp.status_code, "details": data}
    return data


@mcp.tool()
def get_inventory_item(sku: str) -> Dict[str, Any]:
    return _request("GET", f"/inventory_item/{sku}")


@mcp.tool()
def create_or_replace_inventory_item(sku: str, item: Dict[str, Any], content_language: str = "en-US") -> Dict[str, Any]:
    return _request("PUT", f"/inventory_item/{sku}", json_body=item, headers={"Content-Type": "application/json", "Content-Language": content_language})


if __name__ == "__main__":
    mcp.run()
