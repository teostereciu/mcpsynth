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


def _store_url() -> str:
    store = os.getenv("SHOPIFY_STORE_URL")
    if not store:
        raise ValueError("SHOPIFY_STORE_URL is not set")
    return store


def _request(method: str, path: str, params: Dict[str, Any] | None = None, json: Dict[str, Any] | None = None):
    try:
        url = BASE_URL.format(store=_store_url()) + path
        resp = requests.request(method, url, headers=_headers(), params=params, json=json, timeout=30)
        if resp.status_code >= 400:
            try:
                return {"error": resp.json()}
            except Exception:
                return {"error": resp.text or f"HTTP {resp.status_code}"}
        if not resp.text:
            return {}
        try:
            return resp.json()
        except Exception:
            return {"raw": resp.text}
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def list_tools() -> Dict[str, Any]:
    return {"tools": ["list_tools"]}


if __name__ == "__main__":
    mcp.run(transport="stdio")
