import os
import json
from typing import Any, Dict, Optional, Tuple

import requests


def _env(name: str) -> Optional[str]:
    v = os.getenv(name)
    return v.strip() if isinstance(v, str) else v


def get_base_url() -> str:
    base = _env("MASTODON_BASE_URL")
    if not base:
        raise RuntimeError("MASTODON_BASE_URL is not set")
    return base.rstrip("/")


def get_access_token() -> Optional[str]:
    return _env("MASTODON_ACCESS_TOKEN")


def _headers(require_auth: bool = True, extra: Optional[Dict[str, str]] = None) -> Dict[str, str]:
    h: Dict[str, str] = {"Accept": "application/json"}
    token = get_access_token()
    if require_auth:
        if not token:
            raise RuntimeError("MASTODON_ACCESS_TOKEN is not set")
        h["Authorization"] = f"Bearer {token}"
    elif token:
        h["Authorization"] = f"Bearer {token}"
    if extra:
        h.update({k: v for k, v in extra.items() if v is not None})
    return h


def _parse_response(resp: requests.Response) -> Tuple[Any, Dict[str, Any]]:
    meta: Dict[str, Any] = {
        "status_code": resp.status_code,
        "headers": {k: v for k, v in resp.headers.items()},
    }
    if resp.status_code == 204:
        return {}, meta
    ctype = resp.headers.get("Content-Type", "")
    if "application/json" in ctype:
        try:
            return resp.json(), meta
        except Exception:
            return {"error": "Failed to parse JSON response", "text": resp.text}, meta
    # Mastodon sometimes returns empty JSON object with text/plain
    txt = resp.text.strip()
    if txt == "":
        return {}, meta
    try:
        return json.loads(txt), meta
    except Exception:
        return {"text": resp.text}, meta


def request_json(
    method: str,
    path: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    data: Optional[Dict[str, Any]] = None,
    json_body: Optional[Dict[str, Any]] = None,
    files: Optional[Dict[str, Any]] = None,
    require_auth: bool = True,
    extra_headers: Optional[Dict[str, str]] = None,
    timeout: int = 60,
) -> Dict[str, Any]:
    """Make a Mastodon API request and return JSON-serializable dict.

    Always returns a dict. On success: {"data": ..., "meta": ...}
    On error: {"error": ..., "status_code": ..., "details": ...}
    """
    try:
        url = f"{get_base_url()}{path}"
        resp = requests.request(
            method.upper(),
            url,
            headers=_headers(require_auth=require_auth, extra=extra_headers),
            params=params,
            data=data,
            json=json_body,
            files=files,
            timeout=timeout,
        )
        parsed, meta = _parse_response(resp)
        if 200 <= resp.status_code < 300:
            return {"data": parsed, "meta": meta}
        # Mastodon error bodies are often {"error": "..."}
        err_msg = None
        if isinstance(parsed, dict):
            err_msg = parsed.get("error")
        return {
            "error": err_msg or f"HTTP {resp.status_code}",
            "status_code": resp.status_code,
            "details": parsed,
            "meta": meta,
        }
    except Exception as e:
        return {"error": str(e)}
