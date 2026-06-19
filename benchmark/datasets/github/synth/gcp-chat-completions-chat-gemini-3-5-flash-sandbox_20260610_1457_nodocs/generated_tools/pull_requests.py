from typing import Any, Dict, List, Optional, Union
from github_client import client

def list_pull_requests(
    owner: str,
    repo: str,
    state: Optional[str] = "open",
    head: Optional[str] = None,
    base: Optional[str] = None,
    sort: Optional[str] = "created",
    direction: Optional[str] = "desc",
    per_page: Optional[int] = 30,
    page: Optional[int] = 1
) -> Union[List[Dict[str, Any]], Dict[str, Any]]:
    """
    List pull requests in a repository.
    
    Parameters:
    - owner: The account owner of the repository.
    - repo: The name of the repository.
    - state: Either open, closed, or all.
    - head: Filter by source branch and/or user (e.g. 'user:branch-name').
    - base: Filter by destination branch.
    - sort: What to sort results by. Can be created, updated, popularity, long-running.
    - direction: The direction of the sort. Can be asc or desc.
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
    if head: params["head"] = head
    if base: params["base"] = base

    return client.request("GET", f"/repos/{owner}/{repo}/pulls", params=params)

def get_pull_request(owner: str, repo: str, pull_number: int) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
    """
    Get a single pull request.
    
    Parameters:
    - owner: The account owner of the repository.
    - repo: The name of the repository.
    - pull_number: The number that identifies the pull request.
    """
    return client.request("GET", f"/repos/{owner}/{repo}/pulls/{pull_number}")

def create_pull_request(
    owner: str,
    repo: str,
    title: str,
    head: str,
    base: str,
    body: Optional[str] = None,
    draft: Optional[bool] = None,
    maintainer_can_modify: Optional[bool] = None
) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
    """
    Create a pull request.
    
    Parameters:
    - owner: The account owner of the repository.
    - repo: The name of the repository.
    - title: The title of the pull request.
    - head: The name of the branch where your changes are implemented.
    - base: The name of the branch you want your changes pulled into.
    - body: The contents of the pull request.
    - draft: Indicates whether the pull request is a draft.
    - maintainer_can_modify: Indicates whether maintainers can modify the pull request.
    """
    data = {
        "title": title,
        "head": head,
        "base": base
    }
    if body is not None: data["body"] = body
    if draft is not None: data["draft"] = draft
    if maintainer_can_modify is not None: data["maintainer_can_modify"] = maintainer_can_modify

    return client.request("POST", f"/repos/{owner}/{repo}/pulls", json_data=data)

def update_pull_request(
    owner: str,
    repo: str,
    pull_number: int,
    title: Optional[str] = None,
    body: Optional[str] = None,
    state: Optional[str] = None,
    base: Optional[str] = None,
    maintainer_can_modify: Optional[bool] = None
) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
    """
    Update a pull request.
    
    Parameters:
    - owner: The account owner of the repository.
    - repo: The name of the repository.
    - pull_number: The number that identifies the pull request.
    - title: The title of the pull request.
    - body: The contents of the pull request.
    - state: State of the pull request. Either open or closed.
    - base: The name of the branch you want your changes pulled into.
    - maintainer_can_modify: Indicates whether maintainers can modify the pull request.
    """
    data = {}
    if title is not None: data["title"] = title
    if body is not None: data["body"] = body
    if state is not None: data["state"] = state
    if base is not None: data["base"] = base
    if maintainer_can_modify is not None: data["maintainer_can_modify"] = maintainer_can_modify

    return client.request("PATCH", f"/repos/{owner}/{repo}/pulls/{pull_number}", json_data=data)

def create_pull_request_review(
    owner: str,
    repo: str,
    pull_number: int,
    commit_id: Optional[str] = None,
    body: Optional[str] = None,
    event: Optional[str] = None,
    comments: Optional[List[Dict[str, Any]]] = None
) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
    """
    Create a review for a pull request.
    
    Parameters:
    - owner: The account owner of the repository.
    - repo: The name of the repository.
    - pull_number: The number that identifies the pull request.
    - commit_id: The SHA of the commit that needs a review.
    - body: The body text of the pull request review.
    - event: The review action you want to perform. Can be APPROVE, REQUEST_CHANGES, or COMMENT.
    - comments: Use the following format: [{"path": "file.txt", "position": 1, "body": "comment"}]
    """
    data = {}
    if commit_id is not None: data["commit_id"] = commit_id
    if body is not None: data["body"] = body
    if event is not None: data["event"] = event
    if comments is not None: data["comments"] = comments

    return client.request("POST", f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews", json_data=data)

def merge_pull_request(
    owner: str,
    repo: str,
    pull_number: int,
    commit_title: Optional[str] = None,
    commit_message: Optional[str] = None,
    sha: Optional[str] = None,
    merge_method: Optional[str] = "merge"
) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
    """
    Merge a pull request.
    
    Parameters:
    - owner: The account owner of the repository.
    - repo: The name of the repository.
    - pull_number: The number that identifies the pull request.
    - commit_title: Title for the automatic commit message.
    - commit_message: Extra detail to append to the automatic commit message.
    - sha: SHA that pull request head must match to allow merge.
    - merge_method: The merge method to use. Can be merge, squash, or rebase.
    """
    data = {}
    if commit_title is not None: data["commit_title"] = commit_title
    if commit_message is not None: data["commit_message"] = commit_message
    if sha is not None: data["sha"] = sha
    if merge_method is not None: data["merge_method"] = merge_method

    return client.request("PUT", f"/repos/{owner}/{repo}/pulls/{pull_number}/merge", json_data=data)
