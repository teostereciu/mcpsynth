from typing import Any, Dict, Optional

from ._client import GitHubClient


def get_content(
    *,
    owner: str,
    repo: str,
    path: str,
    ref: Optional[str] = None,
    media_type: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /repos/{owner}/{repo}/contents/{path} - Get repository content.

    media_type: one of application/vnd.github.raw+json, application/vnd.github.html+json,
    application/vnd.github.object+json, or None for default.
    """
    c = GitHubClient()
    headers = {}
    if media_type:
        headers["Accept"] = media_type
    return c.request(
        "GET",
        f"/repos/{owner}/{repo}/contents/{path}",
        params={"ref": ref},
        headers=headers or None,
    )


def put_file_contents(
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
) -> Dict[str, Any]:
    """PUT /repos/{owner}/{repo}/contents/{path} - Create or update file contents."""
    c = GitHubClient()
    payload: Dict[str, Any] = {"message": message, "content": content_base64}
    for k, v in {
        "sha": sha,
        "branch": branch,
        "committer": committer,
        "author": author,
    }.items():
        if v is not None:
            payload[k] = v
    return c.request("PUT", f"/repos/{owner}/{repo}/contents/{path}", json=payload)


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
) -> Dict[str, Any]:
    """DELETE /repos/{owner}/{repo}/contents/{path} - Delete a file."""
    c = GitHubClient()
    payload: Dict[str, Any] = {"message": message, "sha": sha}
    for k, v in {"branch": branch, "committer": committer, "author": author}.items():
        if v is not None:
            payload[k] = v
    return c.request("DELETE", f"/repos/{owner}/{repo}/contents/{path}", json=payload)
