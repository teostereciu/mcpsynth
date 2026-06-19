import os
import time
from typing import Any, Dict, Optional, Tuple, Union

import requests


JSON = Union[Dict[str, Any], list, str, int, float, bool, None]


def _base_url() -> str:
    store = os.getenv("SHOPIFY_STORE_URL", "").strip()
    if not store:
        raise RuntimeError("SHOPIFY_STORE_URL is not set")
    return f"https://{store}/admin/api/2026-01"


def _headers() -> Dict[str, str]:
    token = os.getenv("SHOPIFY_ACCESS_TOKEN", "").strip()
    if not token:
        raise RuntimeError("SHOPIFY_ACCESS_TOKEN is not set")
    return {
        "X-Shopify-Access-Token": token,
        "Content-Type": "application/json",
        "Accept": "application/json",
    }


def request_json(
    method: str,
    path: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    json_body: Optional[Dict[str, Any]] = None,
    timeout: int = 60,
    retries: int = 3,
) -> Dict[str, Any]:
    """Make a Shopify Admin REST request.

    Returns JSON-decoded dict on success, or {"error": ...} on failure.
    """

    url = _base_url() + path
    method = method.upper()

    last_err: Optional[str] = None
    for attempt in range(retries):
        try:
            resp = requests.request(
                method,
                url,
                headers=_headers(),
                params=params,
                json=json_body,
                timeout=timeout,
            )

            # Basic rate-limit backoff if present
            if resp.status_code == 429:
                retry_after = resp.headers.get("Retry-After")
                sleep_s = float(retry_after) if retry_after else (1.0 + attempt)
                time.sleep(min(10.0, sleep_s))
                continue

            if resp.status_code >= 400:
                try:
                    data = resp.json()
                except Exception:
                    data = resp.text
                return {
                    "error": "Shopify API error",
                    "status": resp.status_code,
                    "method": method,
                    "path": path,
                    "details": data,
                }

            if resp.status_code == 204:
                return {"ok": True}

            try:
                return resp.json()
            except Exception:
                return {"error": "Invalid JSON response", "status": resp.status_code, "text": resp.text}

        except Exception as e:
            last_err = str(e)
            time.sleep(min(2.0, 0.5 * (attempt + 1)))

    return {"error": "Request failed", "details": last_err, "method": method, "path": path}
