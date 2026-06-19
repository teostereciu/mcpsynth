import os
import requests
from typing import Any, Dict, Optional


def _base_url() -> str:
    return os.environ.get("CODEBERG_BASE_URL", "https://codeberg.org").rstrip("/")


def _token() -> Optional[str]:
    return os.environ.get("CODEBERG_TOKEN")


def request_json(method: str, path: str, *, params: Optional[Dict[str, Any]] = None, json: Any = None) -> Any:
    """Make an authenticated request to Forgejo/Codeberg API v1.

    Returns JSON-decoded response, or {"error": ...} on failure.
    """
    url = f"{_base_url()}/api/v1{path}"
    headers = {"Accept": "application/json"}
    tok = _token()
    if tok:
        headers["Authorization"] = f"token {tok}"

    try:
        resp = requests.request(method.upper(), url, headers=headers, params=params, json=json, timeout=30)
    except Exception as e:
        return {"error": f"request_failed: {e}"}

    if resp.status_code >= 400:
        # Try to parse error body
        try:
            body = resp.json()
        except Exception:
            body = resp.text
        return {"error": f"http_{resp.status_code}", "details": body, "url": url}

    if resp.status_code == 204:
        return {"ok": True}

    # Some endpoints may return empty body
    if not resp.content:
        return {"ok": True}

    try:
        return resp.json()
    except Exception:
        return {"ok": True, "text": resp.text}
