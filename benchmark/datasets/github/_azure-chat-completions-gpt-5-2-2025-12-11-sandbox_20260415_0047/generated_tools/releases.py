from __future__ import annotations

import mimetypes
import os
from typing import Any, Dict, Optional

import requests

from . import mcp
from .http import GitHubClient, split_repo


@mcp.tool()
def releases_create(
    repo: str,
    tag_name: str,
    target_commitish: Optional[str] = None,
    name: Optional[str] = None,
    body: Optional[str] = None,
    draft: bool = False,
    prerelease: bool = False,
    generate_release_notes: bool = False,
) -> Dict[str, Any]:
    """Create a release."""
    try:
        owner, r = split_repo(repo)
        client = GitHubClient.from_env()
        json_body = {
            k: v
            for k, v in {
                "tag_name": tag_name,
                "target_commitish": target_commitish,
                "name": name,
                "body": body,
                "draft": draft,
                "prerelease": prerelease,
                "generate_release_notes": generate_release_notes,
            }.items()
            if v is not None
        }
        status, payload = client.request("POST", f"/repos/{owner}/{r}/releases", json_body=json_body)
        return client.ok_or_error(status, payload)  # type: ignore[return-value]
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def releases_upload_asset(
    repo: str,
    release_id: int,
    file_path: str,
    name: Optional[str] = None,
    label: Optional[str] = None,
    content_type: Optional[str] = None,
) -> Dict[str, Any]:
    """Upload a release asset from a local file path."""
    try:
        if not os.path.exists(file_path):
            return {"error": f"File not found: {file_path}"}
        owner, r = split_repo(repo)
        client = GitHubClient.from_env()

        asset_name = name or os.path.basename(file_path)
        ctype = content_type or mimetypes.guess_type(asset_name)[0] or "application/octet-stream"

        # Uploads use uploads.github.com; for GHE, base_url may differ.
        upload_base = client.base_url.replace("api.github.com", "uploads.github.com")
        url = f"{upload_base}/repos/{owner}/{r}/releases/{release_id}/assets"
        params = {"name": asset_name}
        if label:
            params["label"] = label

        with open(file_path, "rb") as f:
            resp = requests.post(
                url,
                headers={
                    **client.headers(),
                    "Content-Type": ctype,
                },
                params=params,
                data=f,
            )
        payload: Any
        if "application/json" in resp.headers.get("content-type", ""):
            payload = resp.json()
        else:
            payload = resp.text
        return client.ok_or_error(resp.status_code, payload)  # type: ignore[return-value]
    except Exception as e:
        return {"error": str(e)}
