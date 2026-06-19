import os
import requests
from typing import Any, Dict, Optional


API_VERSION = "2026-01"


def _base_url() -> str:
    store = os.environ.get("SHOPIFY_STORE_URL", "").strip()
    if not store:
        raise RuntimeError("SHOPIFY_STORE_URL is not set")
    store = store.replace("https://", "").replace("http://", "").strip("/")
    return f"https://{store}/admin/api/{API_VERSION}"


def _headers() -> Dict[str, str]:
    token = os.environ.get("SHOPIFY_ACCESS_TOKEN", "").strip()
    if not token:
        raise RuntimeError("SHOPIFY_ACCESS_TOKEN is not set")
    return {
        "X-Shopify-Access-Token": token,
        "Content-Type": "application/json",
        "Accept": "application/json",
    }


def shopify_request(
    method: str,
    path: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    json_body: Optional[Dict[str, Any]] = None,
    timeout: int = 60,
) -> Dict[str, Any]:
    """Make a Shopify Admin REST request.

    Returns JSON dict on success, or {"error": ..., "status": ..., "details": ...} on failure.
    """
    try:
        url = _base_url() + path
        resp = requests.request(
            method=method.upper(),
            url=url,
            headers=_headers(),
            params=params,
            json=json_body,
            timeout=timeout,
        )
        if resp.status_code >= 400:
            details: Any
            try:
                details = resp.json()
            except Exception:
                details = resp.text
            return {
                "error": "Shopify API error",
                "status": resp.status_code,
                "details": details,
                "method": method.upper(),
                "path": path,
            }
        if resp.status_code == 204:
            return {"ok": True}
        try:
            return resp.json()
        except Exception:
            return {"ok": True, "text": resp.text}
    except Exception as e:
        return {"error": "Request failed", "details": str(e), "method": method.upper(), "path": path}
