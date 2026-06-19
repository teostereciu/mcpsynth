import base64
import json
import os
from typing import Any, Dict, Optional

import requests

STANDARD_BASE = "https://api.sandbox.ebay.com"
MEDIA_BASE = "https://apim.sandbox.ebay.com"
TOKEN_URL = f"{STANDARD_BASE}/identity/v1/oauth2/token"


def _env(name: str, default: Optional[str] = None) -> Optional[str]:
    return os.getenv(name, default)


def get_base_url(is_media: bool = False) -> str:
    env = (_env("EBAY_ENVIRONMENT", "SANDBOX") or "SANDBOX").upper()
    if env == "PRODUCTION":
        return "https://apim.ebay.com" if is_media else "https://api.ebay.com"
    return MEDIA_BASE if is_media else STANDARD_BASE


def _basic_auth() -> str:
    app_id = _env("EBAY_APP_ID", "") or ""
    cert_id = _env("EBAY_CERT_ID", "") or ""
    token = base64.b64encode(f"{app_id}:{cert_id}".encode()).decode()
    return f"Basic {token}"


def get_token(grant_type: str) -> Dict[str, Any]:
    headers = {"Authorization": _basic_auth(), "Content-Type": "application/x-www-form-urlencoded"}
    data = {"grant_type": grant_type}
    if grant_type == "client_credentials":
        data["scope"] = "https://api.ebay.com/oauth/api_scope"
    else:
        data["refresh_token"] = _env("EBAY_REFRESH_TOKEN", "") or ""
    resp = requests.post(TOKEN_URL, headers=headers, data=data, timeout=30)
    if resp.status_code >= 400:
        return {"error": f"token request failed", "status": resp.status_code, "body": safe_json(resp)}
    return resp.json()


def safe_json(resp: requests.Response) -> Any:
    try:
        return resp.json()
    except Exception:
        return resp.text


def request_json(method: str, url: str, token: str, params: Optional[dict] = None, json_body: Any = None, headers: Optional[dict] = None) -> Dict[str, Any]:
    h = {"Authorization": f"Bearer {token}", "Accept": "application/json"}
    if headers:
        h.update(headers)
    resp = requests.request(method, url, params=params, json=json_body, headers=h, timeout=60)
    if resp.status_code >= 400:
        return {"error": "request failed", "status": resp.status_code, "body": safe_json(resp)}
    return safe_json(resp)
