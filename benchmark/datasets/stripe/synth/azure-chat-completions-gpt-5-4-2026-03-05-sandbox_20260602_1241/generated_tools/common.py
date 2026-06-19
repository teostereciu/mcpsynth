import json
import os
from typing import Any, Dict, Optional

import httpx

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


def encode_form(data: Optional[Dict[str, Any]]) -> Dict[str, str]:
    result: Dict[str, str] = {}
    if not data:
        return result
    for key, value in data.items():
        _flatten(str(key), value, result)
    return result


def stripe_request(method: str, path: str, params: Optional[Dict[str, Any]] = None) -> Any:
    api_key = os.getenv("STRIPE_API_KEY")
    if not api_key:
        raise RuntimeError("STRIPE_API_KEY environment variable is required")

    url = f"{BASE_URL}{path}"
    headers = {"Authorization": f"Bearer {api_key}"}
    encoded = encode_form(params)

    with httpx.Client(timeout=60.0) as client:
        if method.upper() == "GET":
            response = client.get(url, headers=headers, params=encoded)
        elif method.upper() == "DELETE":
            response = client.delete(url, headers=headers, data=encoded)
        else:
            response = client.request(method.upper(), url, headers=headers, data=encoded)

    try:
        response.raise_for_status()
    except httpx.HTTPStatusError as exc:
        detail = exc.response.text
        raise RuntimeError(f"Stripe API error ({exc.response.status_code}): {detail}") from exc

    content_type = response.headers.get("content-type", "")
    if "application/json" in content_type:
        return response.json()
    try:
        return response.json()
    except Exception:
        return {"status_code": response.status_code, "text": response.text}


def compact_result(result: Any) -> str:
    return json.dumps(result, indent=2, sort_keys=True, default=str)
