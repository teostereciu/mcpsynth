import base64
import os
from typing import Any, Dict

import requests

SANDBOX_API = "https://api.sandbox.ebay.com"
SANDBOX_MEDIA = "https://apim.sandbox.ebay.com"
TOKEN_URL = f"{SANDBOX_API}/identity/v1/oauth2/token"


def _env(name: str, default: str = "") -> str:
    return os.getenv(name, default).strip()


def get_base_url() -> str:
    return SANDBOX_API if _env("EBAY_ENVIRONMENT", "SANDBOX").upper() != "PRODUCTION" else "https://api.ebay.com"


def get_media_base_url() -> str:
    return SANDBOX_MEDIA if _env("EBAY_ENVIRONMENT", "SANDBOX").upper() != "PRODUCTION" else "https://apim.ebay.com"


def _token(scope: str, grant_type: str, extra: Dict[str, str] | None = None) -> Dict[str, Any]:
    app_id = _env("EBAY_APP_ID")
    cert_id = _env("EBAY_CERT_ID")
    if not app_id or not cert_id:
        return {"error": "Missing EBAY_APP_ID or EBAY_CERT_ID"}
    auth = base64.b64encode(f"{app_id}:{cert_id}".encode()).decode()
    data = {"grant_type": grant_type, "scope": scope}
    if extra:
        data.update(extra)
    r = requests.post(TOKEN_URL, headers={"Authorization": f"Basic {auth}", "Content-Type": "application/x-www-form-urlencoded"}, data=data, timeout=30)
    if r.status_code >= 400:
        return {"error": f"token request failed", "status": r.status_code, "body": r.text}
    return r.json()


def get_app_token() -> Dict[str, Any]:
    return _token("https://api.ebay.com/oauth/api_scope/commerce.catalog.readonly", "client_credentials")


def get_user_token() -> Dict[str, Any]:
    refresh = _env("EBAY_REFRESH_TOKEN")
    if not refresh:
        return {"error": "Missing EBAY_REFRESH_TOKEN"}
    return _token("https://api.ebay.com/oauth/api_scope", "refresh_token", {"refresh_token": refresh})


def request(method: str, url: str, token: str, params=None, json=None, files=None) -> Dict[str, Any]:
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    r = requests.request(method, url, headers=headers, params=params, json=json, files=files, timeout=60)
    try:
        body = r.json()
    except Exception:
        body = r.text
    if r.status_code >= 400:
        return {"error": "request failed", "status": r.status_code, "body": body}
    return body
