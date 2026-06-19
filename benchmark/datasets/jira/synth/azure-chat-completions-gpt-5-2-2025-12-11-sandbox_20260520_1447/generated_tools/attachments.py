import os
from typing import Any, Dict, List, Optional, Union

import requests

from .http_client import JiraClient


def get_attachment_settings() -> Union[Dict[str, Any], list, str]:
    """GET /attachment/meta"""
    client = JiraClient()
    return client.request("GET", "/attachment/meta")


def get_attachment_metadata(attachment_id: str) -> Union[Dict[str, Any], list, str]:
    """GET /attachment/{id}"""
    client = JiraClient()
    return client.request("GET", f"/attachment/{attachment_id}")


def delete_attachment(attachment_id: str) -> Union[Dict[str, Any], list, str]:
    """DELETE /attachment/{id}"""
    client = JiraClient()
    return client.request("DELETE", f"/attachment/{attachment_id}")


def get_attachment_archive_metadata_human(attachment_id: str) -> Union[Dict[str, Any], list, str]:
    """GET /attachment/{id}/expand/human"""
    client = JiraClient()
    return client.request("GET", f"/attachment/{attachment_id}/expand/human")


def get_attachment_archive_metadata_raw(attachment_id: str) -> Union[Dict[str, Any], list, str]:
    """GET /attachment/{id}/expand/raw"""
    client = JiraClient()
    return client.request("GET", f"/attachment/{attachment_id}/expand/raw")


def add_attachment(issue_id_or_key: str, file_paths: List[str]) -> Union[Dict[str, Any], list, str]:
    """POST /issue/{issueIdOrKey}/attachments

    Note: uses multipart/form-data and requires X-Atlassian-Token: no-check.
    """
    # We can't reuse JiraClient.request because it assumes JSON.
    base = os.environ.get("JIRA_BASE_URL", "").rstrip("/")
    if not base:
        return {"error": "JIRA_BASE_URL is not set"}

    # Build auth header same way as JiraClient
    try:
        client = JiraClient()
    except Exception as e:
        return {"error": str(e)}

    url = f"{base}/rest/api/3/issue/{issue_id_or_key}/attachments"
    headers = {
        "Authorization": client._headers.get("Authorization"),
        "Accept": "application/json",
        "X-Atlassian-Token": "no-check",
    }

    files = []
    opened = []
    try:
        for p in file_paths:
            f = open(p, "rb")
            opened.append(f)
            files.append(("file", (os.path.basename(p), f)))
        resp = requests.post(url, headers=headers, files=files, timeout=120)
    except Exception as e:
        return {"error": str(e)}
    finally:
        for f in opened:
            try:
                f.close()
            except Exception:
                pass

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
