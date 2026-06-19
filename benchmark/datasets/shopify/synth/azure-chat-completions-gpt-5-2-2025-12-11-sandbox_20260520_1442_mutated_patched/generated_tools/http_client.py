import os
import time
from typing import Any, Dict, Optional, Tuple

import requests


def _base_url() -> str:
    store = os.environ.get("SHOPIFY_STORE_URL", "").strip()
    if not store:
        raise RuntimeError("SHOPIFY_STORE_URL is not set")
    return f"https://{store}/admin/api/2026-01"


def _headers() -> Dict[str, str]:
    token = os.environ.get("SHOPIFY_ACCESS_TOKEN", "").strip()
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
    timeout: float = 30.0,
) -> Dict[str, Any]:
    """Make a Shopify Admin REST request.

    Returns JSON-serializable dict:
      - success: parsed JSON (dict/list) under "data"
      - error: {"error": ..., "status": ..., "details": ...}

    Handles basic 429 retry using Retry-After header.
    """
    url = _base_url() + path
    try:
        for attempt in range(2):
            resp = requests.request(
                method.upper(),
                url,
                headers=_headers(),
                params=params,
                json=json_body,
                timeout=timeout,
            )
            if resp.status_code == 429 and attempt == 0:
                retry_after = resp.headers.get("Retry-After")
                try:
                    sleep_s = float(retry_after) if retry_after else 1.0
                except Exception:
                    sleep_s = 1.0
                time.sleep(min(max(sleep_s, 0.5), 5.0))
                continue
            break

        if 200 <= resp.status_code < 300:
            if resp.text.strip() == "":
                return {"data": None, "status": resp.status_code}
            try:
                return {"data": resp.json(), "status": resp.status_code}
            except Exception:
                return {"data": resp.text, "status": resp.status_code}

        # error
        details: Any
        try:
            details = resp.json()
        except Exception:
            details = resp.text
        return {
            "error": "Shopify API error",
            "status": resp.status_code,
            "details": details,
        }
    except Exception as e:
        return {"error": "Request failed", "details": str(e)}
