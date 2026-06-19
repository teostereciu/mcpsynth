import base64
import json
import os
from typing import Any, Dict, Optional

import requests

SANDBOX_BASE = "https://api.sandbox.ebay.com"
SANDBOX_MEDIA_BASE = "https://apim.sandbox.ebay.com"
PROD_BASE = "https://api.ebay.com"
PROD_MEDIA_BASE = "https://apim.ebay.com"


def _env(name: str, default: Optional[str] = None) -> Optional[str]:
    return os.getenv(name, default)


def get_base_url(media: bool = False) -> str:
    env = (_env("EBAY_ENVIRONMENT", "SANDBOX") or "SANDBOX").upper()
    if env == "PRODUCTION":
        return PROD_MEDIA_BASE if media else PROD_BASE
    return SANDBOX_MEDIA_BASE if media else SANDBOX_BASE


def _token_request(data: Dict[str, str]) -> Dict[str, Any]:
    app_id = _env("EBAY_APP_ID")
    cert_id = _env("EBAY_CERT_ID")
    if not app_id or not cert_id:
        return {"error": "Missing EBAY_APP_ID or EBAY_CERT_ID"}
    auth = base64.b64encode(f"{app_id}:{cert_id}".encode()).decode()
    headers = {"Authorization": f"Basic {auth}", "Content-Type": "application/x-www-form-urlencoded"}
    resp = requests.post(f"{get_base_url()}/identity/v1/oauth2/token", headers=headers, data=data, timeout=30)
    if resp.status_code >= 400:
        return {"error": "token_request_failed", "status": resp.status_code, "details": safe_json(resp)}
    return resp.json()


def get_app_token() -> Dict[str, Any]:
    return _token_request({"grant_type": "client_credentials", "scope": "https://api.ebay.com/oauth/api_scope"})


def get_user_token() -> Dict[str, Any]:
    refresh = _env("EBAY_REFRESH_TOKEN")
    if not refresh:
        return {"error": "Missing EBAY_REFRESH_TOKEN"}
    return _token_request({"grant_type": "refresh_token", "refresh_token": refresh, "scope": "https://api.ebay.com/oauth/api_scope"})


def safe_json(resp: requests.Response) -> Any:
    try:
        return resp.json()
    except Exception:
        return resp.text


def request_json(method: str, path: str, *, media: bool = False, token_type: str = "user", params=None, json_body=None, headers=None, files=None) -> Dict[str, Any]:
    token = get_app_token() if token_type == "app" else get_user_token()
    if isinstance(token, dict) and token.get("error"):
        return token
    access_token = token.get("access_token")
    if not access_token:
        return {"error": "missing_access_token", "details": token}
    req_headers = {"Authorization": f"Bearer {access_token}", "Accept": "application/json"}
    if headers:
        req_headers.update(headers)
    url = f"{get_base_url(media=media)}{path}"
    resp = requests.request(method, url, params=params, json=json_body, headers=req_headers, files=files, timeout=60)
    if resp.status_code >= 400:
        return {"error": "request_failed", "status": resp.status_code, "details": safe_json(resp)}
    return safe_json(resp)
