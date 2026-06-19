import os
from typing import Any, Dict

import requests
from fastmcp import FastMCP

API_VERSION = "2026-01"
BASE_URL = f"https://{{store}}/admin/api/{API_VERSION}"

mcp = FastMCP("shopify-admin-rest")


def _headers() -> Dict[str, str]:
    token = os.getenv("SHOPIFY_ACCESS_TOKEN")
    if not token:
        return {}
    return {
        "X-Shopify-Access-Token": token,
        "Content-Type": "application/json",
        "Accept": "application/json",
    }


def _request(method: str, path: str, params: Dict[str, Any] | None = None, json: Dict[str, Any] | None = None):
    store = os.getenv("SHOPIFY_STORE_URL")
    if not store:
        return {"error": "SHOPIFY_STORE_URL is not set"}
    headers = _headers()
    if not headers:
        return {"error": "SHOPIFY_ACCESS_TOKEN is not set"}
    url = BASE_URL.format(store=store) + path
    try:
        resp = requests.request(method, url, headers=headers, params=params, json=json, timeout=30)
        if resp.status_code >= 400:
            try:
                return {"error": resp.json()}
            except Exception:
                return {"error": resp.text}
        if not resp.text:
            return {}
        return resp.json()
    except requests.RequestException as e:
        return {"error": str(e)}


@mcp.tool()
def list_tools() -> Dict[str, Any]:
    return {"tools": ["shopify_placeholder"]}


@mcp.tool()
def shopify_placeholder() -> Dict[str, Any]:
    return {"error": "No tools implemented because docs are unavailable in this workspace."}


if __name__ == "__main__":
    mcp.run(transport="stdio")
