import os
import requests
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("ebay-sell-api")

BASE_URLS = {
    "SANDBOX": "https://api.sandbox.ebay.com",
    "PRODUCTION": "https://api.ebay.com",
}


def _base_url():
    return BASE_URLS.get(os.getenv("EBAY_ENVIRONMENT", "SANDBOX").upper(), BASE_URLS["SANDBOX"])


def _token():
    app_id = os.getenv("EBAY_APP_ID")
    cert_id = os.getenv("EBAY_CERT_ID")
    refresh_token = os.getenv("EBAY_REFRESH_TOKEN")
    if not app_id or not cert_id or not refresh_token:
        return {"error": "Missing EBAY_APP_ID, EBAY_CERT_ID, or EBAY_REFRESH_TOKEN"}
    resp = requests.post(
        f"{_base_url()}/identity/v1/oauth2/token",
        auth=(app_id, cert_id),
        data={"grant_type": "refresh_token", "refresh_token": refresh_token},
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        timeout=30,
    )
    if resp.status_code >= 400:
        return {"error": resp.text}
    return resp.json().get("access_token")


def _request(method, path, params=None, json=None, headers=None):
    token = _token()
    if isinstance(token, dict):
        return token
    h = {"Authorization": f"Bearer {token}", "Accept": "application/json"}
    if headers:
        h.update(headers)
    resp = requests.request(method, f"{_base_url()}{path}", params=params, json=json, headers=h, timeout=30)
    try:
        data = resp.json()
    except Exception:
        data = resp.text
    if resp.status_code >= 400:
        return {"error": data}
    return data


@mcp.tool()
def inventory_get_offers(sku: str = None, marketplace_id: str = None, format: str = None, limit: str = None, offset: str = None):
    params = {k: v for k, v in {"sku": sku, "marketplace_id": marketplace_id, "format": format, "limit": limit, "offset": offset}.items() if v is not None}
    return _request("GET", "/offer", params=params)


@mcp.tool()
def inventory_create_offer(body: dict, content_language: str = "en-US"):
    return _request("POST", "/offer", json=body, headers={"Content-Language": content_language, "Content-Type": "application/json"})


if __name__ == "__main__":
    mcp.run()
