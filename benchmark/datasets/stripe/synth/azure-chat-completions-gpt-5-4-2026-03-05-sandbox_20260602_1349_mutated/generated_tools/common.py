import json
import os
from typing import Any, Dict, Optional
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from urllib.error import HTTPError

BASE_URL = "https://api.stripe.com"


def _flatten(prefix: str, value: Any, out: Dict[str, str]) -> None:
    if value is None:
        return
    if isinstance(value, dict):
        for k, v in value.items():
            key = f"{prefix}[{k}]" if prefix else str(k)
            _flatten(key, v, out)
    elif isinstance(value, list):
        for i, item in enumerate(value):
            key = f"{prefix}[{i}]"
            _flatten(key, item, out)
    elif isinstance(value, bool):
        out[prefix] = "true" if value else "false"
    else:
        out[prefix] = str(value)


def form_encode(data: Optional[Dict[str, Any]]) -> bytes:
    flat: Dict[str, str] = {}
    for k, v in (data or {}).items():
        _flatten(k, v, flat)
    return urlencode(flat).encode()


def stripe_request(method: str, path: str, data: Optional[Dict[str, Any]] = None, query: Optional[Dict[str, Any]] = None) -> Any:
    api_key = os.getenv("STRIPE_API_KEY")
    if not api_key:
        raise RuntimeError("STRIPE_API_KEY is required")

    url = f"{BASE_URL}{path}"
    if query:
        qflat: Dict[str, str] = {}
        for k, v in query.items():
            _flatten(k, v, qflat)
        if qflat:
            url += "?" + urlencode(qflat)

    body = None if method.upper() == "GET" else form_encode(data)
    req = Request(url, data=body, method=method.upper())
    req.add_header("Authorization", f"Bearer {api_key}")
    req.add_header("Content-Type", "application/x-www-form-urlencoded")

    try:
        with urlopen(req) as resp:
            return json.loads(resp.read().decode())
    except HTTPError as e:
        payload = e.read().decode()
        try:
            detail = json.loads(payload)
        except Exception:
            detail = {"error": payload}
        raise RuntimeError(json.dumps(detail))
