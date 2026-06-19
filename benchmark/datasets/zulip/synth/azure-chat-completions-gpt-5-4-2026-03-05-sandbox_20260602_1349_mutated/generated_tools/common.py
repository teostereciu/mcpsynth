import json
import os
from typing import Any, Dict, Optional

import requests


class ZulipClient:
    def __init__(self) -> None:
        self.email = os.getenv("ZULIP_EMAIL")
        self.api_key = os.getenv("ZULIP_API_KEY")
        self.site = os.getenv("ZULIP_SITE", "").rstrip("/")

    def _check_config(self) -> Optional[Dict[str, str]]:
        missing = [
            name
            for name, value in {
                "ZULIP_EMAIL": self.email,
                "ZULIP_API_KEY": self.api_key,
                "ZULIP_SITE": self.site,
            }.items()
            if not value
        ]
        if missing:
            return {"error": f"Missing environment variables: {', '.join(missing)}"}
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
        url = f"{self.site}/api/v1{path}"
        try:
            response = requests.request(
                method,
                url,
                auth=(self.email, self.api_key),
                params=self._normalize(params),
                data=self._normalize(data),
                files=files,
                timeout=60,
            )
        except requests.RequestException as exc:
            return {"error": str(exc)}

        try:
            payload = response.json()
        except ValueError:
            return {"error": f"HTTP {response.status_code}", "text": response.text}

        if response.ok:
            return payload
        if isinstance(payload, dict):
            payload.setdefault("http_status", response.status_code)
            return payload
        return {"error": f"HTTP {response.status_code}", "response": payload}

    def _normalize(self, value: Optional[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        normalized: Dict[str, Any] = {}
        for key, item in value.items():
            if item is None:
                continue
            if isinstance(item, (list, dict, bool)):
                normalized[key] = json.dumps(item)
            else:
                normalized[key] = item
        return normalized


client = ZulipClient()
