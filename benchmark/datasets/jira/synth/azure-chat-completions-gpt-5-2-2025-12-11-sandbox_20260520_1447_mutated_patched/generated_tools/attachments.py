import os
from typing import Any, Dict, List, Optional, Union

import requests

from .jira_client import JiraClient


def get_attachment_meta():
    """GET /attachment/meta"""
    client = JiraClient()
    return client.request("GET", "/attachment/meta")


def get_attachment(attachment_id: str):
    """GET /attachment/{id}"""
    client = JiraClient()
    return client.request("GET", f"/attachment/{attachment_id}")


def delete_attachment(attachment_id: str):
    """DELETE /attachment/{id}"""
    client = JiraClient()
    return client.request("DELETE", f"/attachment/{attachment_id}")


def add_attachment(issueIdOrKey: str, file_paths: List[str]):
    """POST /issue/{issueIdOrKey}/attachments

    Note: requires X-Atlassian-Token: no-check and multipart form field name 'file'.
    """
    # Use requests directly because JiraClient is JSON-oriented.
    base = os.environ.get("JIRA_BASE_URL", "").rstrip("/")
    if not base:
        return {"error": "JIRA_BASE_URL is required"}
    url = f"{base}/rest/api/3/issue/{issueIdOrKey}/attachments"

    # Build auth header same as JiraClient
    try:
        client = JiraClient()
    except Exception as e:
        return {"error": str(e)}

    files = []
    opened = []
    try:
        for p in file_paths:
            f = open(p, "rb")
            opened.append(f)
            files.append(("file", (os.path.basename(p), f)))
        headers = dict(client._headers)
        headers.pop("Accept", None)
        headers["Accept"] = "application/json"
        headers["X-Atlassian-Token"] = "no-check"
        resp = requests.post(url, headers=headers, files=files, timeout=120)
        if resp.status_code >= 400:
            try:
                data = resp.json()
            except Exception:
                data = resp.text
            return {"error": f"HTTP {resp.status_code}", "details": data}
        try:
            return resp.json()
        except Exception:
            return resp.text
    except OSError as e:
        return {"error": str(e)}
    finally:
        for f in opened:
            try:
                f.close()
            except Exception:
                pass
