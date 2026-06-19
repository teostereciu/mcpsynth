import json
import os
from typing import Any, Dict

import requests
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("ebay-sell-api")

BASE_URLS = {
    "SANDBOX": "https://api.sandbox.ebay.com",
    "PRODUCTION": "https://api.ebay.com",
}


def _base_url() -> str:
    return BASE_URLS.get(os.getenv("EBAY_ENVIRONMENT", "SANDBOX").upper(), BASE_URLS["SANDBOX"])


def _token() -> str:
    app_id = os.getenv("EBAY_APP_ID")
    cert_id = os.getenv("EBAY_CERT_ID")
    refresh_token = os.getenv("EBAY_REFRESH_TOKEN")
    if not app_id or not cert_id or not refresh_token:
        raise RuntimeError("Missing EBAY_APP_ID, EBAY_CERT_ID, or EBAY_REFRESH_TOKEN")
    resp = requests.post(
        f"{_base_url()}/identity/v1/oauth2/token",
        auth=(app_id, cert_id),
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data={"grant_type": "refresh_token", "refresh_token": refresh_token},
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()["access_token"]


def _request(method: str, path: str, *, params=None, json_body=None, headers=None) -> Any:
    try:
        token = _token()
        resp = requests.request(
            method,
            f"{_base_url()}{path}",
            params=params,
            json=json_body,
            headers={"Authorization": f"Bearer {token}", **(headers or {})},
            timeout=60,
        )
        if resp.status_code >= 400:
            return {"error": f"HTTP {resp.status_code}", "details": resp.text}
        if not resp.text:
            return {"status": "ok"}
        return resp.json()
    except requests.RequestException as e:
        return {"error": str(e)}
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def get_inventory_item(sku: str) -> Dict[str, Any]:
    return _request("GET", f"/inventory_item/{sku}")


@mcp.tool()
def create_or_replace_inventory_item(sku: str, item: Dict[str, Any], content_language: str = "en-US") -> Dict[str, Any]:
    return _request("PUT", f"/inventory_item/{sku}", json_body=item, headers={"Content-Language": content_language, "Content-Type": "application/json"})


@mcp.tool()
def get_orders(filter: str = None, orderIds: str = None, limit: str = None, offset: str = None, fieldGroups: str = None) -> Dict[str, Any]:
    params = {k: v for k, v in {"filter": filter, "orderIds": orderIds, "limit": limit, "offset": offset, "fieldGroups": fieldGroups}.items() if v is not None}
    return _request("GET", "/order", params=params)


@mcp.tool()
def get_fulfillment_policies(marketplace_id: str, content_language: str = None) -> Dict[str, Any]:
    headers = {"Content-Language": content_language} if content_language else None
    return _request("GET", "/fulfillment_policy", params={"marketplace_id": marketplace_id}, headers=headers)


@mcp.tool()
def get_campaigns(campaign_name: str = None, campaign_status: str = None, campaign_targeting_types: str = None, channels: str = None, end_date_range: str = None, funding_strategy: str = None, limit: str = None, offset: str = None, start_date_range: str = None) -> Dict[str, Any]:
    params = {k: v for k, v in {"campaign_name": campaign_name, "campaign_status": campaign_status, "campaign_targeting_types": campaign_targeting_types, "channels": channels, "end_date_range": end_date_range, "funding_strategy": funding_strategy, "limit": limit, "offset": offset, "start_date_range": start_date_range}.items() if v is not None}
    return _request("GET", "/ad_campaign", params=params)


if __name__ == "__main__":
    mcp.run()
