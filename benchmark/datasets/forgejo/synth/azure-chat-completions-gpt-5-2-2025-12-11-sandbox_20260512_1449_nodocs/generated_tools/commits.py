from typing import Any, Dict, Optional

from .client import request_json


def list_commits(owner: str, repo: str, sha: Optional[str] = None, path: Optional[str] = None, page: Optional[int] = None, limit: Optional[int] = None) -> Any:
    params: Dict[str, Any] = {}
    if sha is not None:
        params["sha"] = sha
    if path is not None:
        params["path"] = path
    if page is not None:
        params["page"] = page
    if limit is not None:
        params["limit"] = limit
    return request_json("GET", f"/repos/{owner}/{repo}/commits", params=params if params else None)


def get_commit(owner: str, repo: str, sha: str) -> Any:
    return request_json("GET", f"/repos/{owner}/{repo}/git/commits/{sha}")
