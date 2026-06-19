from __future__ import annotations

import os
from typing import Any, Dict

import requests
from mcp.server.fastmcp import FastMCP


def _env(name: str) -> str:
    v = os.getenv(name)
    if not v:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return v


class ZulipClient:
    def __init__(self) -> None:
        self.site = _env("ZULIP_SITE").rstrip("/")
        self.email = _env("ZULIP_EMAIL")
        self.api_key = _env("ZULIP_API_KEY")
        self.base = f"{self.site}/api/v1"
        self.session = requests.Session()
        self.session.auth = (self.email, self.api_key)

    def request(self, method: str, path: str, *, params: Dict[str, Any] | None = None, data: Dict[str, Any] | None = None) -> Dict[str, Any]:
        url = f"{self.base}{path}"
        try:
            r = self.session.request(method, url, params=params, data=data, timeout=30)
        except requests.RequestException as e:
            return {"error": str(e)}

        try:
            payload = r.json()
        except ValueError:
            payload = {"raw": r.text}

        if r.status_code >= 400:
            if isinstance(payload, dict):
                payload.setdefault("error", f"HTTP {r.status_code}")
                payload.setdefault("status_code", r.status_code)
                return payload
            return {"error": f"HTTP {r.status_code}", "status_code": r.status_code, "response": payload}

        return payload if isinstance(payload, dict) else {"result": payload}


mcp = FastMCP("zulip")
client = ZulipClient()


@mcp.tool()
def zulip_server_status() -> Dict[str, Any]:
    """Get Zulip server status.

    Endpoint: GET /server_settings (approx; depends on Zulip version)
    """
    # Best-effort: common endpoint is /server_settings
    return client.request("GET", "/server_settings")


if __name__ == "__main__":
    mcp.run()
