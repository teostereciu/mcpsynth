import os
import json
from typing import Any, Dict, Optional, Union

import requests


class ZulipClient:
    def __init__(self, site: Optional[str] = None, email: Optional[str] = None, api_key: Optional[str] = None):
        self.site = (site or os.environ.get("ZULIP_SITE") or "").rstrip("/")
        self.email = email or os.environ.get("ZULIP_EMAIL")
        self.api_key = api_key or os.environ.get("ZULIP_API_KEY")
        if not self.site:
            raise ValueError("ZULIP_SITE is required")
        if not self.email or not self.api_key:
            raise ValueError("ZULIP_EMAIL and ZULIP_API_KEY are required")

        self.base_url = f"{self.site}/api/v1"
        self.session = requests.Session()
        self.session.auth = (self.email, self.api_key)
        self.session.headers.update({"User-Agent": "mcp-zulip/0.1"})

    def request(
        self,
        method: str,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
        json_body: Optional[Dict[str, Any]] = None,
        files: Optional[Dict[str, Any]] = None,
        timeout: int = 30,
    ) -> Dict[str, Any]:
        url = self.base_url + (path if path.startswith("/") else f"/{path}")
        try:
            resp = self.session.request(
                method=method.upper(),
                url=url,
                params=params,
                data=data,
                json=json_body,
                files=files,
                timeout=timeout,
            )
        except requests.RequestException as e:
            return {"error": str(e)}

        content_type = resp.headers.get("content-type", "")
        if "application/json" in content_type:
            try:
                payload = resp.json()
            except Exception:
                payload = {"error": "Invalid JSON response", "status_code": resp.status_code, "text": resp.text}
        else:
            payload = {"status_code": resp.status_code, "text": resp.text}

        if resp.status_code >= 400:
            if isinstance(payload, dict):
                payload.setdefault("status_code", resp.status_code)
                payload.setdefault("error", payload.get("msg") or resp.reason)
                return payload
            return {"status_code": resp.status_code, "error": resp.reason, "body": payload}

        return payload


def _coerce_to_jsonable(value: Any) -> Any:
    if value is None:
        return None
    if isinstance(value, (str, int, float, bool)):
        return value
    if isinstance(value, (list, tuple)):
        return [_coerce_to_jsonable(v) for v in value]
    if isinstance(value, dict):
        return {str(k): _coerce_to_jsonable(v) for k, v in value.items()}
    return str(value)


def clean_params(d: Optional[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
    if not d:
        return None
    out: Dict[str, Any] = {}
    for k, v in d.items():
        if v is None:
            continue
        # Zulip expects some complex params as JSON-encoded strings.
        if isinstance(v, (dict, list)):
            out[k] = json.dumps(v)
        else:
            out[k] = v
    return out
