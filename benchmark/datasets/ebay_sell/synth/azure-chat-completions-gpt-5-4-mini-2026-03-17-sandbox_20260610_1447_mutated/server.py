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
        if resp.status_code == 404:
            return {"error": "not found"}
        if resp.status_code >= 400:
            try:
                return {"error": resp.json()}
            except Exception:
                return {"error": resp.text}
        if not resp.text:
            return {"ok": True}
        try:
            return resp.json()
        except Exception:
            return resp.text
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def get_inventory_items(limit: int | None = None, offset: int | None = None):
    return _request("GET", "/sell/inventory/v1/inventory_item", params={k: v for k, v in {"limit": limit, "offset": offset}.items() if v is not None})


@mcp.tool()
def get_inventory_item(seller_sku: str):
    return _request("GET", f"/sell/inventory/v1/inventory_item/{seller_sku}")


@mcp.tool()
def create_or_replace_inventory_item(seller_sku: str, body: Dict[str, Any]):
    return _request("PUT", f"/sell/inventory/v1/inventory_item/{seller_sku}", json_body=body)


@mcp.tool()
def delete_inventory_item(seller_sku: str):
    return _request("DELETE", f"/sell/inventory/v1/inventory_item/{seller_sku}")


@mcp.tool()
def get_orders(limit: int | None = None, offset: int | None = None):
    return _request("GET", "/sell/fulfillment/v1/order", params={k: v for k, v in {"limit": limit, "offset": offset}.items() if v is not None})


@mcp.tool()
def get_order(order_id: str):
    return _request("GET", f"/sell/fulfillment/v1/order/{order_id}")


@mcp.tool()
def create_shipping_fulfillment(order_id: str, body: Dict[str, Any]):
    return _request("POST", f"/sell/fulfillment/v1/order/{order_id}/shipping_fulfillment", json_body=body)


@mcp.tool()
def issue_refund(order_id: str, body: Dict[str, Any]):
    return _request("POST", f"/sell/fulfillment/v1/order/{order_id}/issue_refund", json_body=body)


@mcp.tool()
def get_fulfillment_policies():
    return _request("GET", "/sell/account/v1/fulfillment_policy")


@mcp.tool()
def create_fulfillment_policy(body: Dict[str, Any]):
    return _request("POST", "/sell/account/v1/fulfillment_policy/", json_body=body)


@mcp.tool()
def delete_fulfillment_policy(fulfillment_policy_id: str):
    return _request("DELETE", f"/sell/account/v1/fulfillment_policy/{fulfillment_policy_id}")


@mcp.tool()
def get_campaigns():
    return _request("GET", "/sell/marketing/v1/ad_campaign")


@mcp.tool()
def create_ad_group(campaign_id: str, body: Dict[str, Any]):
    return _request("POST", f"/sell/marketing/v1/ad_campaign/{campaign_id}/ad_group", json_body=body)


@mcp.tool()
def get_payouts(limit: int | None = None, offset: int | None = None):
    return _request("GET", "/sell/finances/v1/payout", params={k: v for k, v in {"limit": limit, "offset": offset}.items() if v is not None})


@mcp.tool()
def get_transactions(limit: int | None = None, offset: int | None = None):
    return _request("GET", "/sell/finances/v1/transaction", params={k: v for k, v in {"limit": limit, "offset": offset}.items() if v is not None})


@mcp.tool()
def create_inventory_task(body: Dict[str, Any]):
    return _request("POST", "/sell/feed/v1/inventory_task", json_body=body)


if __name__ == "__main__":
    mcp.run()
