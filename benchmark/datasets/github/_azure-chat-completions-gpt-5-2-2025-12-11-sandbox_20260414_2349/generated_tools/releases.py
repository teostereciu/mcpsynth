"""Release tools (create releases, upload assets)."""

from __future__ import annotations

import mimetypes
import os
from typing import Any, Dict, Optional

import requests

from . import mcp
from .http import github_request, split_repo


@mcp.tool
def releases_create(
    repo: str,
    tag_name: str,
    target_commitish: Optional[str] = None,
    name: Optional[str] = None,
    body: Optional[str] = None,
    draft: bool = False,
    prerelease: bool = False,
) -> Dict[str, Any]:
    """Create a release."""
    try:
        r = split_repo(repo)
    except ValueError as e:
        return {"error": str(e)}

    payload: Dict[str, Any] = {
        "tag_name": tag_name,
        "draft": draft,
        "prerelease": prerelease,
    }
    if target_commitish is not None:
        payload["target_commitish"] = target_commitish
    if name is not None:
        payload["name"] = name
    if body is not None:
        payload["body"] = body

    return github_request("POST", f"/repos/{r['owner']}/{r['repo']}/releases", json=payload)


@mcp.tool
def releases_upload_asset(
    upload_url: str,
    file_path: str,
    name: Optional[str] = None,
    label: Optional[str] = None,
    content_type: Optional[str] = None,
) -> Dict[str, Any]:
    """Upload a release asset.

    `upload_url` is the `upload_url` field from the release response.
    """
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        return {"error": "GITHUB_TOKEN is not set"}

    if not os.path.exists(file_path):
        return {"error": f"File not found: {file_path}"}

    asset_name = name or os.path.basename(file_path)
    ct = content_type or mimetypes.guess_type(asset_name)[0] or "application/octet-stream"

    # upload_url looks like: https://uploads.github.com/repos/{owner}/{repo}/releases/{id}/assets{?name,label}
    base = upload_url.split("{")[0]
    params: Dict[str, str] = {"name": asset_name}
    if label is not None:
        params["label"] = label

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "Content-Type": ct,
    }

    try:
        with open(file_path, "rb") as f:
            resp = requests.post(base, headers=headers, params=params, data=f, timeout=120)
    except requests.RequestException as e:
        return {"error": f"Upload failed: {e}"}

    try:
        data = resp.json()
    except ValueError:
        data = resp.text

    out = {"status": resp.status_code, "headers": dict(resp.headers), "data": data}
    if resp.status_code >= 400:
        msg = data.get("message") if isinstance(data, dict) else None
        return {"error": msg or f"GitHub API error ({resp.status_code})", **out}
    return out
