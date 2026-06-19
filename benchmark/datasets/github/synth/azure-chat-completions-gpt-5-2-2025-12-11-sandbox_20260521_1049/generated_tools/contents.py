from typing import Any, Dict, Optional

from .http_client import request_json


def get_repo_content(
    *,
    owner: str,
    repo: str,
    path: str,
    ref: Optional[str] = None,
    accept: str = "application/vnd.github+json",
) -> Any:
    """GET /repos/{owner}/{repo}/contents/{path} - Get repository content."""
    _, data, _ = request_json(
        "GET",
        f"/repos/{owner}/{repo}/contents/{path}",
        params={"ref": ref},
        accept=accept,
    )
    return data


def create_or_update_file_contents(
    *,
    owner: str,
    repo: str,
    path: str,
    message: str,
    content_base64: str,
    sha: Optional[str] = None,
    branch: Optional[str] = None,
    committer: Optional[Dict[str, Any]] = None,
    author: Optional[Dict[str, Any]] = None,
    accept: str = "application/vnd.github+json",
) -> Any:
    """PUT /repos/{owner}/{repo}/contents/{path} - Create or update file contents."""
    _, data, _ = request_json(
        "PUT",
        f"/repos/{owner}/{repo}/contents/{path}",
        json_body={
            "message": message,
            "content": content_base64,
            "sha": sha,
            "branch": branch,
            "committer": committer,
            "author": author,
        },
        accept=accept,
    )
    return data


def delete_file(
    *,
    owner: str,
    repo: str,
    path: str,
    message: str,
    sha: str,
    branch: Optional[str] = None,
    committer: Optional[Dict[str, Any]] = None,
    author: Optional[Dict[str, Any]] = None,
    accept: str = "application/vnd.github+json",
) -> Any:
    """DELETE /repos/{owner}/{repo}/contents/{path} - Delete a file."""
    _, data, _ = request_json(
        "DELETE",
        f"/repos/{owner}/{repo}/contents/{path}",
        json_body={
            "message": message,
            "sha": sha,
            "branch": branch,
            "committer": committer,
            "author": author,
        },
        accept=accept,
    )
    return data
