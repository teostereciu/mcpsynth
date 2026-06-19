from typing import Any, Dict, Optional

from ._client import GitHubClient, split_repo


def list_pull_requests(repo: str, state: str = "open", base: Optional[str] = None, head: Optional[str] = None, sort: str = "created", direction: str = "desc", per_page: int = 30, page: int = 1) -> Any:
    owner, name = split_repo(repo)
    client = GitHubClient()
    params: Dict[str, Any] = {"state": state, "sort": sort, "direction": direction, "per_page": per_page, "page": page}
    if base is not None:
        params["base"] = base
    if head is not None:
        params["head"] = head
    return client.request("GET", f"/repos/{owner}/{name}/pulls", params=params)


def get_pull_request(repo: str, pull_number: int) -> Any:
    owner, name = split_repo(repo)
    client = GitHubClient()
    return client.request("GET", f"/repos/{owner}/{name}/pulls/{pull_number}")


def create_pull_request(repo: str, title: str, head: str, base: str, body: Optional[str] = None, draft: Optional[bool] = None, maintainer_can_modify: Optional[bool] = None) -> Any:
    owner, name = split_repo(repo)
    client = GitHubClient()
    payload: Dict[str, Any] = {"title": title, "head": head, "base": base}
    if body is not None:
        payload["body"] = body
    if draft is not None:
        payload["draft"] = draft
    if maintainer_can_modify is not None:
        payload["maintainer_can_modify"] = maintainer_can_modify
    return client.request("POST", f"/repos/{owner}/{name}/pulls", json=payload, expected=(201,))


def update_pull_request(repo: str, pull_number: int, title: Optional[str] = None, body: Optional[str] = None, state: Optional[str] = None, base: Optional[str] = None, maintainer_can_modify: Optional[bool] = None) -> Any:
    owner, name = split_repo(repo)
    client = GitHubClient()
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
    return client.request("PATCH", f"/repos/{owner}/{name}/pulls/{pull_number}", json=payload)


def merge_pull_request(repo: str, pull_number: int, commit_title: Optional[str] = None, commit_message: Optional[str] = None, merge_method: Optional[str] = None, sha: Optional[str] = None) -> Any:
    owner, name = split_repo(repo)
    client = GitHubClient()
    payload: Dict[str, Any] = {}
    if commit_title is not None:
        payload["commit_title"] = commit_title
    if commit_message is not None:
        payload["commit_message"] = commit_message
    if merge_method is not None:
        payload["merge_method"] = merge_method
    if sha is not None:
        payload["sha"] = sha
    return client.request("PUT", f"/repos/{owner}/{name}/pulls/{pull_number}/merge", json=payload)


def list_pull_reviews(repo: str, pull_number: int, per_page: int = 30, page: int = 1) -> Any:
    owner, name = split_repo(repo)
    client = GitHubClient()
    return client.request("GET", f"/repos/{owner}/{name}/pulls/{pull_number}/reviews", params={"per_page": per_page, "page": page})


def create_pull_review(repo: str, pull_number: int, body: Optional[str] = None, event: Optional[str] = None, comments: Optional[list] = None, commit_id: Optional[str] = None) -> Any:
    owner, name = split_repo(repo)
    client = GitHubClient()
    payload: Dict[str, Any] = {}
    if body is not None:
        payload["body"] = body
    if event is not None:
        payload["event"] = event
    if comments is not None:
        payload["comments"] = comments
    if commit_id is not None:
        payload["commit_id"] = commit_id
    return client.request("POST", f"/repos/{owner}/{name}/pulls/{pull_number}/reviews", json=payload, expected=(200, 201))


def request_reviewers(repo: str, pull_number: int, reviewers: Optional[list] = None, team_reviewers: Optional[list] = None) -> Any:
    owner, name = split_repo(repo)
    client = GitHubClient()
    payload: Dict[str, Any] = {}
    if reviewers is not None:
        payload["reviewers"] = reviewers
    if team_reviewers is not None:
        payload["team_reviewers"] = team_reviewers
    return client.request("POST", f"/repos/{owner}/{name}/pulls/{pull_number}/requested_reviewers", json=payload)


def list_pull_commits(repo: str, pull_number: int, per_page: int = 30, page: int = 1) -> Any:
    owner, name = split_repo(repo)
    client = GitHubClient()
    return client.request("GET", f"/repos/{owner}/{name}/pulls/{pull_number}/commits", params={"per_page": per_page, "page": page})


def list_pull_files(repo: str, pull_number: int, per_page: int = 30, page: int = 1) -> Any:
    owner, name = split_repo(repo)
    client = GitHubClient()
    return client.request("GET", f"/repos/{owner}/{name}/pulls/{pull_number}/files", params={"per_page": per_page, "page": page})
