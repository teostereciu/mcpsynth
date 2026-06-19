from typing import Any, List, Optional

from generated_tools.github_common import clean_params, github_request


def list_pull_requests(owner: str, repo: str, state: Optional[str] = None, head: Optional[str] = None, base: Optional[str] = None, sort: Optional[str] = None, direction: Optional[str] = None, per_page: int = 30, page: int = 1) -> Any:
    params = clean_params(state=state, head=head, base=base, sort=sort, direction=direction, per_page=per_page, page=page)
    return github_request("GET", f"/repos/{owner}/{repo}/pulls", params=params)


def get_pull_request(owner: str, repo: str, pull_number: int) -> Any:
    return github_request("GET", f"/repos/{owner}/{repo}/pulls/{pull_number}")


def create_pull_request(owner: str, repo: str, title: str, head: str, base: str, body: Optional[str] = None, maintainer_can_modify: Optional[bool] = None, draft: Optional[bool] = None) -> Any:
    payload = clean_params(title=title, head=head, base=base, body=body, maintainer_can_modify=maintainer_can_modify, draft=draft)
    return github_request("POST", f"/repos/{owner}/{repo}/pulls", json_body=payload)


def update_pull_request(owner: str, repo: str, pull_number: int, title: Optional[str] = None, body: Optional[str] = None, state: Optional[str] = None, base: Optional[str] = None, maintainer_can_modify: Optional[bool] = None) -> Any:
    payload = clean_params(title=title, body=body, state=state, base=base, maintainer_can_modify=maintainer_can_modify)
    return github_request("PATCH", f"/repos/{owner}/{repo}/pulls/{pull_number}", json_body=payload)


def list_pull_request_files(owner: str, repo: str, pull_number: int, per_page: int = 30, page: int = 1) -> Any:
    return github_request("GET", f"/repos/{owner}/{repo}/pulls/{pull_number}/files", params=clean_params(per_page=per_page, page=page))


def list_pull_request_commits(owner: str, repo: str, pull_number: int, per_page: int = 30, page: int = 1) -> Any:
    return github_request("GET", f"/repos/{owner}/{repo}/pulls/{pull_number}/commits", params=clean_params(per_page=per_page, page=page))


def merge_pull_request(owner: str, repo: str, pull_number: int, commit_title: Optional[str] = None, commit_message: Optional[str] = None, sha: Optional[str] = None, merge_method: Optional[str] = None) -> Any:
    payload = clean_params(commit_title=commit_title, commit_message=commit_message, sha=sha, merge_method=merge_method)
    return github_request("PUT", f"/repos/{owner}/{repo}/pulls/{pull_number}/merge", json_body=payload)


def request_pull_request_reviewers(owner: str, repo: str, pull_number: int, reviewers: Optional[List[str]] = None, team_reviewers: Optional[List[str]] = None) -> Any:
    payload = clean_params(reviewers=reviewers, team_reviewers=team_reviewers)
    return github_request("POST", f"/repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers", json_body=payload)


def create_pull_request_review(owner: str, repo: str, pull_number: int, body: Optional[str] = None, event: Optional[str] = None, commit_id: Optional[str] = None) -> Any:
    payload = clean_params(body=body, event=event, commit_id=commit_id)
    return github_request("POST", f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews", json_body=payload)
