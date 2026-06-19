from typing import Any, Dict, Optional

from .github_client import GitHubClient, parse_owner_repo


def list_pulls(owner_repo: str, state: str = "open", base: Optional[str] = None, head: Optional[str] = None, sort: str = "created", direction: str = "desc", per_page: int = 100, max_pages: int = 5) -> Dict[str, Any]:
    try:
        owner, repo = parse_owner_repo(owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    params: Dict[str, Any] = {"state": state, "sort": sort, "direction": direction}
    if base is not None:
        params["base"] = base
    if head is not None:
        params["head"] = head
    return GitHubClient().paginate(f"/repos/{owner}/{repo}/pulls", params=params, per_page=per_page, max_pages=max_pages)


def get_pull(owner_repo: str, pull_number: int) -> Dict[str, Any]:
    try:
        owner, repo = parse_owner_repo(owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    return GitHubClient().request("GET", f"/repos/{owner}/{repo}/pulls/{pull_number}")


def create_pull(owner_repo: str, title: str, head: str, base: str, body: Optional[str] = None, draft: bool = False, maintainer_can_modify: Optional[bool] = None) -> Dict[str, Any]:
    try:
        owner, repo = parse_owner_repo(owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    payload: Dict[str, Any] = {"title": title, "head": head, "base": base, "draft": draft}
    if body is not None:
        payload["body"] = body
    if maintainer_can_modify is not None:
        payload["maintainer_can_modify"] = maintainer_can_modify
    return GitHubClient().request("POST", f"/repos/{owner}/{repo}/pulls", json=payload)


def update_pull(owner_repo: str, pull_number: int, title: Optional[str] = None, body: Optional[str] = None, state: Optional[str] = None, base: Optional[str] = None, maintainer_can_modify: Optional[bool] = None) -> Dict[str, Any]:
    try:
        owner, repo = parse_owner_repo(owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    payload: Dict[str, Any] = {}
    if title is not None:
        payload["title"] = title
    if body is not None:
        payload["body"] = body
    if state is not None:
        payload["state"] = state
    if base is not None:
        payload["base"] = base
    if maintainer_can_modify is not None:
        payload["maintainer_can_modify"] = maintainer_can_modify
    return GitHubClient().request("PATCH", f"/repos/{owner}/{repo}/pulls/{pull_number}", json=payload)


def list_pull_commits(owner_repo: str, pull_number: int, per_page: int = 100, max_pages: int = 5) -> Dict[str, Any]:
    try:
        owner, repo = parse_owner_repo(owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    return GitHubClient().paginate(f"/repos/{owner}/{repo}/pulls/{pull_number}/commits", per_page=per_page, max_pages=max_pages)


def list_pull_files(owner_repo: str, pull_number: int, per_page: int = 100, max_pages: int = 5) -> Dict[str, Any]:
    try:
        owner, repo = parse_owner_repo(owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    return GitHubClient().paginate(f"/repos/{owner}/{repo}/pulls/{pull_number}/files", per_page=per_page, max_pages=max_pages)


def create_review(owner_repo: str, pull_number: int, body: Optional[str] = None, event: str = "COMMENT", comments: Optional[list] = None, commit_id: Optional[str] = None) -> Dict[str, Any]:
    """event: APPROVE | REQUEST_CHANGES | COMMENT"""
    try:
        owner, repo = parse_owner_repo(owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    payload: Dict[str, Any] = {"event": event}
    if body is not None:
        payload["body"] = body
    if comments is not None:
        payload["comments"] = comments
    if commit_id is not None:
        payload["commit_id"] = commit_id
    return GitHubClient().request("POST", f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews", json=payload)


def merge_pull(owner_repo: str, pull_number: int, commit_title: Optional[str] = None, commit_message: Optional[str] = None, merge_method: str = "merge", sha: Optional[str] = None) -> Dict[str, Any]:
    """merge_method: merge | squash | rebase"""
    try:
        owner, repo = parse_owner_repo(owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    payload: Dict[str, Any] = {"merge_method": merge_method}
    if commit_title is not None:
        payload["commit_title"] = commit_title
    if commit_message is not None:
        payload["commit_message"] = commit_message
    if sha is not None:
        payload["sha"] = sha
    return GitHubClient().request("PUT", f"/repos/{owner}/{repo}/pulls/{pull_number}/merge", json=payload)
