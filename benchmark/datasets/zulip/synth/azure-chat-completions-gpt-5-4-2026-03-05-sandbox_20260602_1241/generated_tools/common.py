import json
import os
from typing import Any, Dict, Optional

import requests


class ZulipClient:
    def __init__(self) -> None:
        site = os.getenv("ZULIP_SITE", "").rstrip("/")
        email = os.getenv("ZULIP_EMAIL")
        api_key = os.getenv("ZULIP_API_KEY")
        self.base_url = f"{site}/api/v1" if site else ""
        self.auth = (email or "", api_key or "")

    def _check_config(self) -> Optional[Dict[str, str]]:
        if not self.base_url or not self.auth[0] or not self.auth[1]:
            return {
                "error": "Missing Zulip configuration. Set ZULIP_SITE, ZULIP_EMAIL, and ZULIP_API_KEY."
            }
        return None

    def request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
        files: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        config_error = self._check_config()
        if config_error:
            return config_error
        url = f"{self.base_url}{path}"
        try:
            response = requests.request(
                method,
                url,
                auth=self.auth,
                params=self._normalize(params),
                data=self._normalize(data),
                files=files,
                timeout=60,
            )
            payload = response.json()
            if isinstance(payload, dict):
                return payload
            return {"result": "success", "data": payload}
        except requests.RequestException as exc:
            return {"error": str(exc)}
        except ValueError:
            return {"error": f"Non-JSON response from Zulip: {response.text[:500]}"}

    def _normalize(self, payload: Optional[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
        if payload is None:
            return None
        normalized: Dict[str, Any] = {}
        for key, value in payload.items():
            if value is None:
                continue
            if isinstance(value, (dict, list)):
                normalized[key] = json.dumps(value)
            elif isinstance(value, bool):
                normalized[key] = json.dumps(value)
            else:
                normalized[key] = value
        return normalized


client = ZulipClient()
