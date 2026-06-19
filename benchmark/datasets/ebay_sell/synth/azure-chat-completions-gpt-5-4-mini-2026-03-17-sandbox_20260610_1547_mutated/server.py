import os
import requests
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("ebay-sell-api")

BASE_URLS = {
    "SANDBOX": "https://api.sandbox.ebay.com",
    "PRODUCTION": "https://api.ebay.com",
}


def _env():
    return os.getenv("EBAY_ENVIRONMENT", "SANDBOX").upper()


def _base_url():
    return BASE_URLS.get(_env(), BASE_URLS["SANDBOX"])


def _token():
    app_id = os.getenv("EBAY_APP_ID")
    cert_id = os.getenv("EBAY_CERT_ID")
    refresh_token = os.getenv("EBAY_REFRESH_TOKEN")
    if not all([app_id, cert_id, refresh_token]):
        return {"error": "Missing EBAY_APP_ID, EBAY_CERT_ID, or EBAY_REFRESH_TOKEN"}
    resp = requests.post(
        f"{_base_url()}/identity/v1/oauth2/token",
        auth=(app_id, cert_id),
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data={"grant_type": "refresh_token", "refresh_token": refresh_token},
        timeout=30,
    )
    if resp.status_code >= 400:
        return {"error": "Token request failed", "status": resp.status_code, "body": resp.text}
    return resp.json().get("access_token")


def _request(method, path, *, params=None, json=None, headers=None):
    token = _token()
    if isinstance(token, dict):
        return token
    h = {"Authorization": f"Bearer {token}", "Accept": "application/json"}
    if headers:
        h.update(headers)
    resp = requests.request(method, f"{_base_url()}{path}", params=params, json=json, headers=h, timeout=60)
    if resp.status_code >= 400:
        try:
            body = resp.json()
        except Exception:
            body = resp.text
        return {"error": "Request failed", "status": resp.status_code, "body": body}
    if not resp.text:
        return {"ok": True}
    try:
        return resp.json()
    except Exception:
        return {"raw": resp.text}


@mcp.tool()
def get_inventory_item(seller_sku: str):
    return _request("GET", f"/inventory_item/{seller_sku}")


@mcp.tool()
def get_inventory_items(limit: int | None = None, offset: int | None = None):
    params = {k: v for k, v in {"limit": limit, "offset": offset}.items() if v is not None}
    return _request("GET", "/inventory_item", params=params)


@mcp.tool()
def create_or_replace_inventory_item(seller_sku: str, body: dict):
    return _request("PUT", f"/inventory_item/{seller_sku}", json=body)


@mcp.tool()
def delete_inventory_item(seller_sku: str):
    return _request("DELETE", f"/inventory_item/{seller_sku}")


@mcp.tool()
def get_orders(limit: int | None = None, offset: int | None = None, orderfulfillmentstatus: str | None = None):
    params = {k: v for k, v in {"limit": limit, "offset": offset, "orderfulfillmentstatus": orderfulfillmentstatus}.items() if v is not None}
    return _request("GET", "/order", params=params)


@mcp.tool()
def get_order(orderId: str, fieldGroups: str | None = None):
    params = {"fieldGroups": fieldGroups} if fieldGroups else None
    return _request("GET", f"/order/{orderId}", params=params)


@mcp.tool()
def get_fulfillment_policies(market_id: str, content_language: str | None = None):
    headers = {"Content-Language": content_language} if content_language else None
    return _request("GET", "/fulfillment_policy", params={"market_id": market_id}, headers=headers)


if __name__ == "__main__":
    mcp.run()
