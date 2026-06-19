import base64
import json
import os
from typing import Any, Dict, Optional

import requests


def _load_service_account_token() -> str:
    creds_path = os.environ.get("GOOGLE_WORKSPACE_CREDENTIALS") or os.environ.get(
        "GOOGLE_SHEETS_CREDENTIALS"
    )
    if not creds_path:
        raise RuntimeError("Set GOOGLE_ACCESS_TOKEN or GOOGLE_WORKSPACE_CREDENTIALS")

    from google.oauth2 import service_account
    import google.auth.transport.requests

    scopes = [
        "https://www.googleapis.com/auth/gmail.modify",
        "https://www.googleapis.com/auth/calendar",
        "https://www.googleapis.com/auth/drive",
        "https://www.googleapis.com/auth/documents",
        "https://www.googleapis.com/auth/presentations",
        "https://www.googleapis.com/auth/spreadsheets",
    ]

    creds = service_account.Credentials.from_service_account_file(creds_path, scopes=scopes)
    req = google.auth.transport.requests.Request()
    creds.refresh(req)
    return creds.token


def get_access_token() -> str:
    token = os.environ.get("GOOGLE_ACCESS_TOKEN")
    if token:
        return token
    return _load_service_account_token()


def _error_dict(resp: requests.Response) -> Dict[str, Any]:
    try:
        data = resp.json()
    except Exception:
        data = {"message": resp.text}
    err = data.get("error") if isinstance(data, dict) else None
    if isinstance(err, dict):
        message = err.get("message")
    else:
        message = data.get("message") if isinstance(data, dict) else None
    return {
        "error": message or resp.reason or "HTTP error",
        "status": resp.status_code,
        "details": data,
    }


def request_json(
    method: str,
    url: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    json_body: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    timeout: int = 60,
) -> Any:
    token = get_access_token()
    h = {"Authorization": f"Bearer {token}"}
    if headers:
        h.update(headers)
    if json_body is not None:
        h.setdefault("Content-Type", "application/json")

    try:
        resp = requests.request(
            method,
            url,
            params=params or {},
            json=json_body,
            headers=h,
            timeout=timeout,
        )
    except requests.RequestException as e:
        return {"error": str(e), "status": None}

    if resp.status_code >= 400:
        return _error_dict(resp)

    if resp.status_code == 204:
        return {"status": 204}

    ctype = resp.headers.get("Content-Type", "")
    if "application/json" in ctype:
        return resp.json()
    return {"content": resp.text, "contentType": ctype}


def base64url_encode(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).decode("utf-8").rstrip("=")


def rfc2822_message(to: str, subject: str, body: str, *, from_addr: Optional[str] = None) -> str:
    lines = []
    if from_addr:
        lines.append(f"From: {from_addr}")
    lines.append(f"To: {to}")
    lines.append(f"Subject: {subject}")
    lines.append("MIME-Version: 1.0")
    lines.append("Content-Type: text/plain; charset=utf-8")
    lines.append("")
    lines.append(body)
    raw = "\r\n".join(lines).encode("utf-8")
    return base64url_encode(raw)
