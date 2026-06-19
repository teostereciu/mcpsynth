import os
import base64
import json
from typing import Any, Dict, Optional

import requests

BASE_URLS = {
    "SANDBOX": "https://api.sandbox.ebay.com",
    "PRODUCTION": "https://api.ebay.com",
}


def get_base_url() -> str:
    env = os.getenv("EBAY_ENVIRONMENT", "SANDBOX").upper()
    return BASE_URLS.get(env, BASE_URLS["SANDBOX"])


def get_access_token() -> str:
    app_id = os.getenv("EBAY_APP_ID")
    cert_id = os.getenv("EBAY_CERT_ID")
    if not app_id or not cert_id:
        raise RuntimeError("Missing EBAY_APP_ID or EBAY_CERT_ID")
    auth = base64.b64encode(f"{app_id}:{cert_id}".encode()).decode()
    resp = requests.post(
        f"{get_base_url()}/identity/v1/oauth2/token",
        headers={"Content-Type": "application/x-www-form-urlencoded", "Authorization": f"Basic {auth}"},
        data={"grant_type": "client_credentials", "scope": "https://api.ebay.com/oauth/api_scope"},
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()["access_token"]


def request(method: str, path: str, *, params: Optional[Dict[str, Any]] = None, json_body: Any = None, headers: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
    try:
        token = get_access_token()
        h = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
        if headers:
            h.update(headers)
        resp = requests.request(method, f"{get_base_url()}{path}", params=params, json=json_body, headers=h, timeout=60)
        if resp.status_code >= 400:
            try:
                return {"error": resp.json()}
            except Exception:
                return {"error": resp.text}
        if resp.text:
            return resp.json()
        return {}
    except Exception as e:
        return {"error": str(e)}
