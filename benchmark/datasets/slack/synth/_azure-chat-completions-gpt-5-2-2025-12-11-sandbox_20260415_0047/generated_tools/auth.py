from __future__ import annotations

from typing import Any, Dict, Optional

from . import mcp
from .http import SlackAPIError, slack_api_call


@mcp.tool(name="auth_test")
def auth_test() -> Dict[str, Any]:
    """Checks authentication & identity (auth.test)."""

    try:
        return slack_api_call("auth.test", http_method="POST", json={})
    except SlackAPIError as e:
        return {"ok": False, "error": "http_error", "detail": e.message, "status_code": e.status_code}


@mcp.tool(name="auth_revoke")
def auth_revoke(test: Optional[bool] = None) -> Dict[str, Any]:
    """Revokes a token (auth.revoke)."""

    payload: Dict[str, Any] = {}
    if test is not None:
        payload["test"] = test
    try:
        return slack_api_call("auth.revoke", http_method="GET", params=payload)
    except SlackAPIError as e:
        return {"ok": False, "error": "http_error", "detail": e.message, "status_code": e.status_code}
