from typing import Any, Dict, List, Optional, Union
from github_client import client

def list_issues(
    owner: str,
    repo: str,
    state: Optional[str] = "open",
    labels: Optional[str] = None,
    assignee: Optional[str] = None,
    creator: Optional[str] = None,
    mentioned: Optional[str] = None,
    milestone: Optional[str] = None,
    sort: Optional[str] = "created",
    direction: Optional[str] = "desc",
    since: Optional[str] = None,
    per_page: Optional[int] = 30,
    page: Optional[int] = 1
) -> Union[List[Dict[str, Any]], Dict[str, Any]]:
    """
    List issues in a repository.
    
    Parameters:
    - owner: The account owner of the repository.
    - repo: The name of the repository.
    - state: Indicates the state of the issues to return. Can be either open, closed, or all.
    - labels: A list of comma separated label names.
    - assignee: Can be the name of a user, 'none', or '*'.
    - creator: The user that created the issue.
    - mentioned: A user that is mentioned in the issue.
    - milestone: Can be an integer (milestone number), 'none', or '*'.
    - sort: What to sort results by. Can be created, updated, comments.
    - direction: The direction of the sort. Can be asc or desc.
    - since: Only show results that were last updated after this time (ISO 8601 format).
    - per_page: The number of results per page (max 100).
    - page: Page number of the results to fetch.
    """
    params = {
        "state": state,
        "sort": sort,
        "direction": direction,
        "per_page": per_page,
        "page": page
    }
    if labels: params["labels"] = labels
    if assignee: params["assignee"] = assignee
    if creator: params["creator"] = creator
    if mentioned: params["mentioned"] = mentioned
    if milestone: params["milestone"] = milestone
    if since: params["since"] = since

    return client.request("GET", f"/repos/{owner}/{repo}/issues", params=params)

def get_issue(owner: str, repo: str, issue_number: int) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
    """
    Get a single issue.
    
    Parameters:
    - owner: The account owner of the repository.
    - repo: The name of the repository.
    - issue_number: The number that identifies the issue.
    """
    return client.request("GET", f"/repos/{owner}/{repo}/issues/{issue_number}")

def create_issue(
    owner: str,
    repo: str,
    title: str,
    body: Optional[str] = None,
    assignees: Optional[List[str]] = None,
    milestone: Optional[int] = None,
    labels: Optional[List[str]] = None
) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
    """
    Create an issue.
    
    Parameters:
    - owner: The account owner of the repository.
    - repo: The name of the repository.
    - title: The title of the issue.
    - body: The contents of the issue.
    - assignees: Logins for users to assign to this issue.
    - milestone: The number of the milestone to associate this issue with.
    - labels: Labels to associate with this issue.
    """
    data = {"title": title}
    if body is not None: data["body"] = body
    if assignees is not None: data["assignees"] = assignees
    if milestone is not None: data["milestone"] = milestone
    if labels is not None: data["labels"] = labels

    return client.request("POST", f"/repos/{owner}/{repo}/issues", json_data=data)

def update_issue(
    owner: str,
    repo: str,
    issue_number: int,
    title: Optional[str] = None,
    body: Optional[str] = None,
    state: Optional[str] = None,
    state_reason: Optional[str] = None,
    assignees: Optional[List[str]] = None,
    milestone: Optional[int] = None,
    labels: Optional[List[str]] = None
) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
    """
    Update an issue.
    
    Parameters:
    - owner: The account owner of the repository.
    - repo: The name of the repository.
    - issue_number: The number that identifies the issue.
    - title: The title of the issue.
    - body: The contents of the issue.
    - state: The state of the issue. Either open or closed.
    - state_reason: The reason for the state change. Can be completed, not_planned, or null.
    - assignees: Logins for users to assign to this issue.
    - milestone: The number of the milestone to associate this issue with.
    - labels: Labels to associate with this issue.
    """
    data = {}
    if title is not None: data["title"] = title
    if body is not None: data["body"] = body
    if state is not None: data["state"] = state
    if state_reason is not None: data["state_reason"] = state_reason
    if assignees is not None: data["assignees"] = assignees
    if milestone is not None: data["milestone"] = milestone
    if labels is not None: data["labels"] = labels

    return client.request("PATCH", f"/repos/{owner}/{repo}/issues/{issue_number}", json_data=data)

def add_issue_labels(owner: str, repo: str, issue_number: int, labels: List[str]) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
    """
    Add labels to an issue.
    
    Parameters:
    - owner: The account owner of the repository.
    - repo: The name of the repository.
    - issue_number: The number that identifies the issue.
    - labels: The names of the labels to add.
    """
    return client.request("POST", f"/repos/{owner}/{repo}/issues/{issue_number}/labels", json_data={"labels": labels})

def remove_issue_label(owner: str, repo: str, issue_number: int, name: str) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
    """
    Remove a label from an issue.
    
    Parameters:
    - owner: The account owner of the repository.
    - repo: The name of the repository.
    - issue_number: The number that identifies the issue.
    - name: The name of the label to remove.
    """
    return client.request("DELETE", f"/repos/{owner}/{repo}/issues/{issue_number}/labels/{name}")

def add_issue_assignees(owner: str, repo: str, issue_number: int, assignees: List[str]) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
    """
    Add assignees to an issue.
    
    Parameters:
    - owner: The account owner of the repository.
    - repo: The name of the repository.
    - issue_number: The number that identifies the issue.
    - assignees: Usernames of people to assign this issue to.
    """
    return client.request("POST", f"/repos/{owner}/{repo}/issues/{issue_number}/assignees", json_data={"assignees": assignees})

def remove_issue_assignees(owner: str, repo: str, issue_number: int, assignees: List[str]) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
    """
    Remove assignees from an issue.
    
    Parameters:
    - owner: The account owner of the repository.
    - repo: The name of the repository.
    - issue_number: The number that identifies the issue.
    - assignees: Usernames of people to remove from this issue.
    """
    return client.request("DELETE", f"/repos/{owner}/{repo}/issues/{issue_number}/assignees", json_data={"assignees": assignees})

def list_issue_comments(
    owner: str,
    repo: str,
    issue_number: int,
    since: Optional[str] = None,
    per_page: Optional[int] = 30,
    page: Optional[int] = 1
) -> Union[List[Dict[str, Any]], Dict[str, Any]]:
    """
    List comments on an issue.
    
    Parameters:
    - owner: The account owner of the repository.
    - repo: The name of the repository.
    - issue_number: The number that identifies the issue.
    - since: Only show results that were last updated after this time (ISO 8601 format).
    - per_page: The number of results per page (max 100).
    - page: Page number of the results to fetch.
    """
    params = {"per_page": per_page, "page": page}
    if since: params["since"] = since
    return client.request("GET", f"/repos/{owner}/{repo}/issues/{issue_number}/comments", params=params)

def create_issue_comment(owner: str, repo: str, issue_number: int, body: str) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
    """
    Create an issue comment.
    
    Parameters:
    - owner: The account owner of the repository.
    - repo: The name of the repository.
    - issue_number: The number that identifies the issue.
    - body: The contents of the comment.
    """
    return client.request("POST", f"/repos/{owner}/{repo}/issues/{issue_number}/comments", json_data={"body": body})

def update_issue_comment(owner: str, repo: str, comment_id: int, body: str) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
    """
    Update an issue comment.
    
    Parameters:
    - owner: The account owner of the repository.
    - repo: The name of the repository.
    - comment_id: The unique identifier of the comment.
    - body: The contents of the comment.
    """
    return client.request("PATCH", f"/repos/{owner}/{repo}/issues/comments/{comment_id}", json_data={"body": body})

def delete_issue_comment(owner: str, repo: str, comment_id: int) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
    """
    Delete an issue comment.
    
    Parameters:
    - owner: The account owner of the repository.
    - repo: The name of the repository.
    - comment_id: The unique identifier of the comment.
    """
    return client.request("DELETE", f"/repos/{owner}/{repo}/issues/comments/{comment_id}")
