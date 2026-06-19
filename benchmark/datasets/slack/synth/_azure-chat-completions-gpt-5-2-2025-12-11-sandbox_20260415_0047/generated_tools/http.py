from __future__ import annotations

import os
import time
from dataclasses import dataclass
from typing import Any, Dict, Optional

import requests

SLACK_API_BASE = "https://slack.com/api"


@dataclass
class SlackAPIError(Exception):
    """Raised for unexpected Slack API failures (network/HTTP), not for ok:false responses."""

    message: str
    status_code: Optional[int] = None
    response_text: Optional[str] = None


def _auth_headers() -> Dict[str, str]:
    token = os.environ.get("SLACK_BOT_TOKEN")
    if not token:
        # Return a sentinel header; callers will handle missing token gracefully.
        return {}
    return {"Authorization": f"Bearer {token}"}


def slack_api_call(
    method: str,
    http_method: str = "POST",
    params: Optional[Dict[str, Any]] = None,
    json: Optional[Dict[str, Any]] = None,
    timeout_s: float = 30.0,
    max_retries: int = 1,
) -> Dict[str, Any]:
    """Call Slack Web API.

    Returns Slack's JSON response (including ok:false).
    Never raises for ok:false; only raises for unexpected HTTP/network errors.
    """

    if not os.environ.get("SLACK_BOT_TOKEN"):
        return {"ok": False, "error": "not_authed", "detail": "SLACK_BOT_TOKEN is not set"}

    url = f"{SLACK_API_BASE}/{method}"
    headers = _auth_headers()

    # Slack expects JSON for many methods; GET uses query params.
    request_fn = requests.get if http_method.upper() == "GET" else requests.post

    last_exc: Optional[Exception] = None
    for attempt in range(max_retries + 1):
        try:
            resp = request_fn(
                url,
                headers={
                    **headers,
                    **({"Content-Type": "application/json; charset=utf-8"} if http_method.upper() != "GET" else {}),
                },
                params=params or {},
                json=json if http_method.upper() != "GET" else None,
                timeout=timeout_s,
            )

            # Handle rate limiting with a single retry by default.
            if resp.status_code == 429 and attempt < max_retries:
                retry_after = resp.headers.get("Retry-After")
                try:
                    sleep_s = float(retry_after) if retry_after else 1.0
                except ValueError:
                    sleep_s = 1.0
                time.sleep(max(0.0, sleep_s))
                continue

            resp.raise_for_status()
            data = resp.json()
            if not isinstance(data, dict):
                return {"ok": False, "error": "invalid_response", "detail": "Non-object JSON response"}
            return data
        except requests.RequestException as e:
            last_exc = e

    raise SlackAPIError(
        message="Slack API request failed",
        status_code=getattr(getattr(last_exc, "response", None), "status_code", None),
        response_text=getattr(getattr(last_exc, "response", None), "text", None),
    )


def slack_upload_to_external_url(upload_url: str, content: bytes, timeout_s: float = 60.0) -> Dict[str, Any]:
    """Upload bytes to the pre-signed URL returned by files.getUploadURLExternal.

    Slack returns an upload_url (usually to AWS S3). This is not a Slack API endpoint.
    """

    try:
        resp = requests.post(upload_url, data=content, timeout=timeout_s)
        resp.raise_for_status()
        return {"ok": True, "status_code": resp.status_code}
    except requests.RequestException as e:
        return {
            "ok": False,
            "error": "upload_failed",
            "detail": str(e),
            "status_code": getattr(getattr(e, "response", None), "status_code", None),
            "response_text": getattr(getattr(e, "response", None), "text", None),
        }
