from typing import Any, List, Optional

from generated_tools.github_common import clean_params, github_request


def list_issues(owner: str, repo: str, milestone: Optional[str] = None, state: Optional[str] = None, assignee: Optional[str] = None, creator: Optional[str] = None, mentioned: Optional[str] = None, labels: Optional[str] = None, sort: Optional[str] = None, direction: Optional[str] = None, since: Optional[str] = None, per_page: int = 30, page: int = 1) -> Any:
    params = clean_params(milestone=milestone, state=state, assignee=assignee, creator=creator, mentioned=mentioned, labels=labels, sort=sort, direction=direction, since=since, per_page=per_page, page=page)
    return github_request("GET", f"/repos/{owner}/{repo}/issues", params=params)


def get_issue(owner: str, repo: str, issue_number: int) -> Any:
    return github_request("GET", f"/repos/{owner}/{repo}/issues/{issue_number}")


def create_issue(owner: str, repo: str, title: str, body: Optional[str] = None, assignees: Optional[List[str]] = None, milestone: Optional[int] = None, labels: Optional[List[str]] = None) -> Any:
    payload = clean_params(title=title, body=body, assignees=assignees, milestone=milestone, labels=labels)
    return github_request("POST", f"/repos/{owner}/{repo}/issues", json_body=payload)


def update_issue(owner: str, repo: str, issue_number: int, title: Optional[str] = None, body: Optional[str] = None, state: Optional[str] = None, state_reason: Optional[str] = None, milestone: Optional[int] = None, labels: Optional[List[str]] = None, assignees: Optional[List[str]] = None) -> Any:
    payload = clean_params(title=title, body=body, state=state, state_reason=state_reason, milestone=milestone, labels=labels, assignees=assignees)
    return github_request("PATCH", f"/repos/{owner}/{repo}/issues/{issue_number}", json_body=payload)


def list_issue_comments(owner: str, repo: str, issue_number: int, since: Optional[str] = None, per_page: int = 30, page: int = 1) -> Any:
    params = clean_params(since=since, per_page=per_page, page=page)
    return github_request("GET", f"/repos/{owner}/{repo}/issues/{issue_number}/comments", params=params)


def create_issue_comment(owner: str, repo: str, issue_number: int, body: str) -> Any:
    return github_request("POST", f"/repos/{owner}/{repo}/issues/{issue_number}/comments", json_body={"body": body})


def update_issue_comment(owner: str, repo: str, comment_id: int, body: str) -> Any:
    return github_request("PATCH", f"/repos/{owner}/{repo}/issues/comments/{comment_id}", json_body={"body": body})


def delete_issue_comment(owner: str, repo: str, comment_id: int) -> Any:
    return github_request("DELETE", f"/repos/{owner}/{repo}/issues/comments/{comment_id}")


def add_assignees(owner: str, repo: str, issue_number: int, assignees: List[str]) -> Any:
    return github_request("POST", f"/repos/{owner}/{repo}/issues/{issue_number}/assignees", json_body={"assignees": assignees})


def remove_assignees(owner: str, repo: str, issue_number: int, assignees: List[str]) -> Any:
    return github_request("DELETE", f"/repos/{owner}/{repo}/issues/{issue_number}/assignees", json_body={"assignees": assignees})


def list_labels(owner: str, repo: str, per_page: int = 30, page: int = 1) -> Any:
    return github_request("GET", f"/repos/{owner}/{repo}/labels", params=clean_params(per_page=per_page, page=page))


def create_label(owner: str, repo: str, name: str, color: str, description: Optional[str] = None) -> Any:
    return github_request("POST", f"/repos/{owner}/{repo}/labels", json_body=clean_params(name=name, color=color, description=description))


def update_label(owner: str, repo: str, name: str, new_name: Optional[str] = None, color: Optional[str] = None, description: Optional[str] = None) -> Any:
    return github_request("PATCH", f"/repos/{owner}/{repo}/labels/{name}", json_body=clean_params(new_name=new_name, color=color, description=description))


def delete_label(owner: str, repo: str, name: str) -> Any:
    return github_request("DELETE", f"/repos/{owner}/{repo}/labels/{name}")
