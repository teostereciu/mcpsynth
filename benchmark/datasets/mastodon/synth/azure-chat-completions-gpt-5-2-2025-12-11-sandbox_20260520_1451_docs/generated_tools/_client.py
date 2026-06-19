import os
import requests
from typing import Any, Dict, Optional


def _base_url() -> str:
    base = os.environ.get("MASTODON_BASE_URL", "").strip()
    if not base:
        raise RuntimeError("MASTODON_BASE_URL is not set")
    return base.rstrip("/")


def _auth_headers() -> Dict[str, str]:
    token = os.environ.get("MASTODON_ACCESS_TOKEN", "").strip()
    headers: Dict[str, str] = {"Accept": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


def request_json(method: str, path: str, *, params: Optional[Dict[str, Any]] = None,
                 data: Optional[Dict[str, Any]] = None,
                 files: Optional[Dict[str, Any]] = None,
                 headers: Optional[Dict[str, str]] = None,
                 timeout: int = 30) -> Any:
    url = f"{_base_url()}{path}"
    h = _auth_headers()
    if headers:
        h.update(headers)
    try:
        resp = requests.request(method, url, params=params, data=data, files=files, headers=h, timeout=timeout)
        ct = resp.headers.get("content-type", "")
        if resp.status_code >= 400:
            try:
                err = resp.json() if "json" in ct else {"error": resp.text}
            except Exception:
                err = {"error": resp.text}
            if isinstance(err, dict):
                err.setdefault("status_code", resp.status_code)
                err.setdefault("url", url)
            return err
        if resp.status_code == 204:
            return {"ok": True}
        if "json" in ct:
            return resp.json()
        return resp.text
    except Exception as e:
        return {"error": str(e), "url": url}
