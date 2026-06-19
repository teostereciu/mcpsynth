from typing import Optional

from generated_tools.github_common import compact, github_request


def list_repository_issues(owner: str, repo: str, state: str = "open", labels: Optional[str] = None, sort: str = "created", direction: str = "desc", since: Optional[str] = None, per_page: int = 30, page: int = 1) -> str:
    return compact(github_request("GET", f"/repos/{owner}/{repo}/issues", params={"state": state, "labels": labels, "sort": sort, "direction": direction, "since": since, "per_page": per_page, "page": page}))


def get_issue(owner: str, repo: str, issue_number: int) -> str:
    return compact(github_request("GET", f"/repos/{owner}/{repo}/issues/{issue_number}"))


def create_issue(owner: str, repo: str, title: str, body: Optional[str] = None, assignees: Optional[list[str]] = None, milestone: Optional[int] = None, labels: Optional[list[str]] = None) -> str:
    return compact(github_request("POST", f"/repos/{owner}/{repo}/issues", json_body={"title": title, "body": body, "assignees": assignees, "milestone": milestone, "labels": labels}))


def update_issue(owner: str, repo: str, issue_number: int, title: Optional[str] = None, body: Optional[str] = None, state: Optional[str] = None, state_reason: Optional[str] = None, milestone: Optional[int] = None, labels: Optional[list[str]] = None, assignees: Optional[list[str]] = None) -> str:
    return compact(github_request("PATCH", f"/repos/{owner}/{repo}/issues/{issue_number}", json_body={"title": title, "body": body, "state": state, "state_reason": state_reason, "milestone": milestone, "labels": labels, "assignees": assignees}))


def create_issue_comment(owner: str, repo: str, issue_number: int, body: str) -> str:
    return compact(github_request("POST", f"/repos/{owner}/{repo}/issues/{issue_number}/comments", json_body={"body": body}))


def list_issue_comments(owner: str, repo: str, issue_number: int, per_page: int = 30, page: int = 1) -> str:
    return compact(github_request("GET", f"/repos/{owner}/{repo}/issues/{issue_number}/comments", params={"per_page": per_page, "page": page}))
