import os
from typing import Any, Dict

import requests
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("ebay-sell-api")

BASE_URLS = {
    "SANDBOX": "https://api.sandbox.ebay.com",
    "PRODUCTION": "https://api.ebay.com",
}


def _env() -> str:
    return os.getenv("EBAY_ENVIRONMENT", "SANDBOX").upper()


def _base_url() -> str:
    return BASE_URLS.get(_env(), BASE_URLS["SANDBOX"])


def _token() -> str:
    app_id = os.getenv("EBAY_APP_ID")
    cert_id = os.getenv("EBAY_CERT_ID")
    refresh_token = os.getenv("EBAY_REFRESH_TOKEN")
    if not all([app_id, cert_id, refresh_token]):
        raise ValueError("Missing EBAY_APP_ID, EBAY_CERT_ID, or EBAY_REFRESH_TOKEN")
    resp = requests.post(
        f"{_base_url()}/identity/v1/oauth2/token",
        auth=(app_id, cert_id),
        data={"grant_type": "refresh_token", "refresh_token": refresh_token},
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()["access_token"]


def _request(method: str, path: str, *, params=None, json=None, headers=None) -> Dict[str, Any]:
    try:
        token = _token()
        h = {"Authorization": f"Bearer {token}", "Accept": "application/json"}
        if headers:
            h.update(headers)
        resp = requests.request(method, f"{_base_url()}{path}", params=params, json=json, headers=h, timeout=60)
        if resp.status_code >= 400:
            return {"error": f"HTTP {resp.status_code}", "details": resp.text}
        if resp.text:
            return resp.json()
        return {"status": "ok"}
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def get_inventory_item(seller_sku: str):
    return _request("GET", f"/inventory_item/{seller_sku}")


@mcp.tool()
def get_offers(seller_sku: str, format: str | None = None, limit: str | None = None, market_id: str | None = None, offset: str | None = None):
    params = {k: v for k, v in {"seller_sku": seller_sku, "format": format, "limit": limit, "market_id": market_id, "offset": offset}.items() if v is not None}
    return _request("GET", "/offer", params=params)


@mcp.tool()
def get_fulfillment_policies(market_id: str, content_language: str | None = None):
    headers = {"Content-Language": content_language} if content_language else None
    return _request("GET", "/fulfillment_policy", params={"market_id": market_id}, headers=headers)


@mcp.tool()
def get_tasks(feed_type: str | None = None, schedule_id: str | None = None, date_range: str | None = None, limit: str | None = None, look_back_days: str | None = None, offset: str | None = None):
    params = {k: v for k, v in {"feed_type": feed_type, "schedule_id": schedule_id, "date_range": date_range, "limit": limit, "look_back_days": look_back_days, "offset": offset}.items() if v is not None}
    return _request("GET", "/task", params=params)


if __name__ == "__main__":
    mcp.run()
