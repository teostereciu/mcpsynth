import base64
import json
import os
from typing import Any, Dict, Optional
from urllib.parse import urlencode

import requests
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("ebay-commerce-api")

TOKEN_URL = "https://api.ebay.com/identity/v1/oauth2/token"
STANDARD_BASE = "https://api.ebay.com"
MEDIA_BASE = "https://apim.ebay.com"
SCOPE_APP = "https://api.ebay.com/oauth/api_scope"
SCOPE_USER = "https://api.ebay.com/oauth/api_scope/commerce.identity.readonly"

_token_cache: Dict[str, Dict[str, Any]] = {}


def _env_base() -> str:
    env = os.getenv("EBAY_ENVIRONMENT", "SANDBOX").upper()
    if env == "PRODUCTION":
        return STANDARD_BASE, MEDIA_BASE
    return STANDARD_BASE.replace("api.ebay.com", "api.sandbox.ebay.com"), MEDIA_BASE.replace("apim.ebay.com", "apim.sandbox.ebay.com")


def _auth_header(grant_type: str, scope: str, refresh_token: Optional[str] = None) -> Dict[str, str]:
    cache_key = f"{grant_type}:{scope}:{refresh_token or ''}"
    cached = _token_cache.get(cache_key)
    if cached and cached.get("access_token"):
        return {"Authorization": f"Bearer {cached['access_token']}"}
    app_id = os.getenv("EBAY_APP_ID")
    cert_id = os.getenv("EBAY_CERT_ID")
    if not app_id or not cert_id:
        raise RuntimeError("Missing EBAY_APP_ID or EBAY_CERT_ID")
    basic = base64.b64encode(f"{app_id}:{cert_id}".encode()).decode()
    headers = {"Authorization": f"Basic {basic}", "Content-Type": "application/x-www-form-urlencoded"}
    data = {"grant_type": grant_type, "scope": scope}
    if refresh_token:
        data["refresh_token"] = refresh_token
    resp = requests.post(TOKEN_URL, headers=headers, data=urlencode(data), timeout=30)
    resp.raise_for_status()
    token = resp.json()
    _token_cache[cache_key] = token
    return {"Authorization": f"Bearer {token['access_token']}"}


def _request(method: str, url: str, *, user_token: bool = False, app_token: bool = False, params=None, json_body=None, headers=None):
    base_standard, base_media = _env_base()
    if url.startswith("/media/"):
        url = base_media + url
    else:
        url = base_standard + url
    req_headers = {"Accept": "application/json"}
    if headers:
        req_headers.update(headers)
    if app_token:
        req_headers.update(_auth_header("client_credentials", SCOPE_APP))
    elif user_token:
        req_headers.update(_auth_header("refresh_token", SCOPE_USER, os.getenv("EBAY_REFRESH_TOKEN")))
    resp = requests.request(method, url, params=params, json=json_body, headers=req_headers, timeout=60)
    if resp.status_code >= 400:
        try:
            return {"error": resp.json()}
        except Exception:
            return {"error": resp.text, "status_code": resp.status_code}
    if not resp.text:
        return {"status_code": resp.status_code}
    try:
        return resp.json()
    except Exception:
        return {"text": resp.text, "status_code": resp.status_code}


@mcp.tool()
def get_product(epid: str, marketplace_id: Optional[str] = None):
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id} if marketplace_id else None
    return _request("GET", f"/commerce/catalog/v1_beta/product/{epid}", app_token=True, headers=headers)


@mcp.tool()
def search_products(query: Optional[str] = None, gtin: Optional[str] = None, mpn: Optional[str] = None, category_id: Optional[str] = None, aspects: Optional[str] = None, field_groups: Optional[str] = None, page_size: Optional[int] = None):
    params = {k: v for k, v in {"query": query, "gtin": gtin, "mpn": mpn, "category_id": category_id, "aspects": aspects, "field_groups": field_groups, "page_size": page_size}.items() if v is not None}
    return _request("GET", "/commerce/catalog/v1_beta/product_summary/search", params=params, app_token=True)


@mcp.tool()
def get_user():
    return _request("GET", "/commerce/identity/v1/user/", user_token=True)


@mcp.tool()
def get_image(image_id: str):
    return _request("GET", f"/media/commerce/media/v1_beta/image/{image_id}", user_token=True)


@mcp.tool()
def get_destinations(page_size: Optional[int] = None, continuation_token: Optional[str] = None):
    params = {k: v for k, v in {"page_size": page_size, "continuation_token": continuation_token}.items() if v is not None}
    return _request("GET", "/commerce/notification/v1/destination", user_token=True, params=params)


if __name__ == "__main__":
    mcp.run()
