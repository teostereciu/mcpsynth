import os
import time
from typing import Any, Dict, Optional, Tuple

import requests


class ShopifyClient:
    def __init__(
        self,
        store_url: Optional[str] = None,
        access_token: Optional[str] = None,
        api_version: str = "2026-01",
        timeout: int = 30,
    ):
        self.store_url = (store_url or os.getenv("SHOPIFY_STORE_URL") or "").strip()
        self.access_token = (access_token or os.getenv("SHOPIFY_ACCESS_TOKEN") or "").strip()
        self.api_version = api_version
        self.timeout = timeout

        if self.store_url.startswith("https://"):
            self.store_url = self.store_url[len("https://") :]
        if self.store_url.endswith("/"):
            self.store_url = self.store_url[:-1]

    @property
    def base_url(self) -> str:
        return f"https://{self.store_url}/admin/api/{self.api_version}"

    def _headers(self) -> Dict[str, str]:
        return {
            "X-Shopify-Access-Token": self.access_token,
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

    def request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        retries: int = 3,
    ) -> Dict[str, Any]:
        if not self.store_url:
            return {"error": "SHOPIFY_STORE_URL is not set"}
        if not self.access_token:
            return {"error": "SHOPIFY_ACCESS_TOKEN is not set"}

        url = self.base_url + path
        headers = self._headers()
        if extra_headers:
            headers.update(extra_headers)

        last_err: Optional[str] = None
        for attempt in range(retries):
            try:
                resp = requests.request(
                    method.upper(),
                    url,
                    headers=headers,
                    params=params,
                    json=json,
                    timeout=self.timeout,
                )

                # Basic rate-limit handling (429) and transient errors
                if resp.status_code == 429:
                    retry_after = resp.headers.get("Retry-After")
                    sleep_s = float(retry_after) if retry_after else (1.0 + attempt)
                    time.sleep(sleep_s)
                    continue
                if resp.status_code in (500, 502, 503, 504) and attempt < retries - 1:
                    time.sleep(0.5 * (attempt + 1))
                    continue

                if resp.status_code >= 400:
                    try:
                        data = resp.json()
                    except Exception:
                        data = {"message": resp.text}
                    return {
                        "error": "Shopify API error",
                        "status": resp.status_code,
                        "path": path,
                        "details": data,
                    }

                if resp.status_code == 204:
                    return {"ok": True}

                try:
                    return resp.json()
                except Exception:
                    return {"ok": True, "raw": resp.text}

            except requests.RequestException as e:
                last_err = str(e)
                time.sleep(0.5 * (attempt + 1))

        return {"error": "Request failed", "details": last_err or "unknown"}


def build_pagination_params(
    *,
    limit: Optional[int] = None,
    page_info: Optional[str] = None,
    since_id: Optional[int] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if page_info is not None:
        params["page_info"] = page_info
    if since_id is not None:
        params["since_id"] = since_id
    return params


def parse_link_header(link_header: Optional[str]) -> Dict[str, str]:
    # Shopify uses RFC5988 Link header for cursor pagination.
    # Example: <https://.../products.json?limit=50&page_info=xxx>; rel="next"
    if not link_header:
        return {}
    out: Dict[str, str] = {}
    parts = [p.strip() for p in link_header.split(",")]
    for part in parts:
        if ";" not in part:
            continue
        url_part, *params = [x.strip() for x in part.split(";")]
        if not (url_part.startswith("<") and url_part.endswith(">")):
            continue
        url = url_part[1:-1]
        rel = None
        for p in params:
            if p.startswith("rel="):
                rel = p.split("=", 1)[1].strip().strip('"')
        if rel:
            out[rel] = url
    return out


def extract_page_info(url: str) -> Optional[str]:
    # Extract page_info query param from a URL
    try:
        from urllib.parse import urlparse, parse_qs

        q = parse_qs(urlparse(url).query)
        vals = q.get("page_info")
        return vals[0] if vals else None
    except Exception:
        return None
