import os
import json
from typing import Any, Dict, Optional

import requests
from requests.auth import HTTPBasicAuth


class TwilioClient:
    def __init__(
        self,
        account_sid: Optional[str] = None,
        auth_token: Optional[str] = None,
        timeout: int = 30,
    ):
        self.account_sid = account_sid or os.getenv("TWILIO_ACCOUNT_SID")
        self.auth_token = auth_token or os.getenv("TWILIO_AUTH_TOKEN")
        self.timeout = timeout

        if not self.account_sid or not self.auth_token:
            raise ValueError(
                "Missing TWILIO_ACCOUNT_SID/TWILIO_AUTH_TOKEN environment variables"
            )

        self._auth = HTTPBasicAuth(self.account_sid, self.auth_token)

    def request(
        self,
        method: str,
        url: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Dict[str, Any]:
        try:
            resp = requests.request(
                method=method.upper(),
                url=url,
                params={k: v for k, v in (params or {}).items() if v is not None},
                data={k: self._encode_value(v) for k, v in (data or {}).items() if v is not None},
                headers=headers,
                auth=self._auth,
                timeout=self.timeout,
            )
        except requests.RequestException as e:
            return {"error": str(e)}

        content_type = resp.headers.get("content-type", "")
        parsed: Any
        if "application/json" in content_type:
            try:
                parsed = resp.json()
            except Exception:
                parsed = resp.text
        else:
            parsed = resp.text

        if resp.status_code >= 400:
            return {
                "error": "Twilio API error",
                "status_code": resp.status_code,
                "response": parsed,
            }

        if isinstance(parsed, (dict, list)):
            return parsed
        return {"raw": parsed}

    @staticmethod
    def _encode_value(v: Any) -> Any:
        if isinstance(v, (dict, list)):
            return json.dumps(v)
        if isinstance(v, bool):
            return "true" if v else "false"
        return v


def accounts_base_url(account_sid: str) -> str:
    return f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}"


def verify_base_url() -> str:
    return "https://verify.twilio.com/v2"


def conversations_base_url() -> str:
    return "https://conversations.twilio.com/v1"
