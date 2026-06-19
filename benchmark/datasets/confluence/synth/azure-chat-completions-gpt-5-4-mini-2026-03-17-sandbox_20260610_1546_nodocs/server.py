import base64
import os
from typing import Any, Dict, Optional

import requests
from fastmcp import FastMCP

mcp = FastMCP("confluence-cloud")


def _base_url() -> str:
    return os.environ.get("CONFLUENCE_BASE_URL", "").rstrip("/")


def _auth() -> Optional[tuple[str, str]]:
    email = os.environ.get("JIRA_EMAIL")
    token = os.environ.get("JIRA_API_TOKEN")
    if email and token:
        return email, token
    return None


def _request(method: str, path: str, *, params=None, json=None, data=None, headers=None, files=None) -> Dict[str, Any]:
    base = _base_url()
    if not base:
        return {"error": "CONFLUENCE_BASE_URL is not set"}
    url = f"{base}{path}"
    try:
        resp = requests.request(
            method,
            url,
            params=params,
            json=json,
            data=data,
            headers=headers,
            files=files,
            auth=_auth(),
            timeout=60,
        )
        if resp.status_code >= 400:
            try:
                return {"error": resp.json()}
            except Exception:
                return {"error": resp.text}
        if resp.text:
            try:
                return resp.json()
            except Exception:
                return {"result": resp.text}
        return {}
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def list_tools() -> Dict[str, Any]:
    return {"tools": ["list_tools"]}


if __name__ == "__main__":
    mcp.run(transport="stdio")
