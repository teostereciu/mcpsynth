"""GitHub Issues tools."""

from typing import Any, Optional
from generated_tools.github_client import github_get, github_post, github_patch, github_put, github_delete


def list_repository_issues(owner: str, repo: str, state: str = "open", labels: Optional[str] = None,
                           sort: str = "created", direction: str = "desc", since: Optional[str] = None,
                           assignee: Optional[str] = None, creator: Optional[str] = None,
                           milestone: Optional[str] = None, per_page: int = 30, page: int = 1) -> Any:
    """List issues in a repository.

    Args:
        owner: Repository owner
        repo: Repository name
        state: State of issues (open, closed, all)
        labels: Comma-separated label names
        sort: Sort by (created, updated, comments)
        direction: Sort direction (asc, desc)
        since: Only issues updated after this ISO 8601 timestamp
        assignee: Filter by assignee username, 'none', or '*'
        creator: Filter by creator username
        milestone: Filter by milestone number, 'none', or '*'
        per_page: Results per page (max 100)
        page: Page number
    """
    params = {"state": state, "sort": sort, "direction": direction, "per_page": per_page, "page": page}
    if labels:
        params["labels"] = labels
    if since:
        params["since"] = since
    if assignee:
        params["assignee"] = assignee
    if creator:
        params["creator"] = creator
    if milestone:
        params["milestone"] = milestone
    return github_get(f"/repos/{owner}/{repo}/issues", params)


def create_issue(owner: str, repo: str, title: str, body: Optional[str] = None,
                 assignees: Optional[list] = None, labels: Optional[list] = None,
                 milestone: Optional[int] = None) -> Any:
    """Create an issue in a repository.

    Args:
        owner: Repository owner
        repo: Repository name
        title: Issue title
        body: Issue body text
        assignees: List of usernames to assign
        labels: List of label names
        milestone: Milestone number to associate
    """
    data = {"title": title}
    if body is not None:
        data["body"] = body
    if assignees:
        data["assignees"] = assignees
    if labels:
        data["labels"] = labels
    if milestone is not None:
        data["milestone"] = milestone
    return github_post(f"/repos/{owner}/{repo}/issues", data)


def get_issue(owner: str, repo: str, issue_number: int) -> Any:
    """Get a specific issue.

    Args:
        owner: Repository owner
        repo: Repository name
        issue_number: Issue number
    """
    return github_get(f"/repos/{owner}/{repo}/issues/{issue_number}")


def update_issue(owner: str, repo: str, issue_number: int, title: Optional[str] = None,
                 body: Optional[str] = None, state: Optional[str] = None,
                 state_reason: Optional[str] = None, labels: Optional[list] = None,
                 assignees: Optional[list] = None, milestone: Optional[int] = None) -> Any:
    """Update an issue.

    Args:
        owner: Repository owner
        repo: Repository name
        issue_number: Issue number
        title: New title
        body: New body text
        state: New state (open, closed)
        state_reason: Reason for state change (completed, not_planned, reopened)
        labels: New list of label names (replaces existing)
        assignees: New list of assignee usernames (replaces existing)
        milestone: Milestone number or null
    """
    data = {}
    if title is not None:
        data["title"] = title
    if body is not None:
        data["body"] = body
    if state is not None:
        data["state"] = state
    if state_reason is not None:
        data["state_reason"] = state_reason
    if labels is not None:
        data["labels"] = labels
    if assignees is not None:
        data["assignees"] = assignees
    if milestone is not None:
        data["milestone"] = milestone
    return github_patch(f"/repos/{owner}/{repo}/issues/{issue_number}", data)


def lock_issue(owner: str, repo: str, issue_number: int, lock_reason: Optional[str] = None) -> Any:
    """Lock an issue.

    Args:
        owner: Repository owner
        repo: Repository name
        issue_number: Issue number
        lock_reason: Reason for locking (off-topic, too heated, resolved, spam)
    """
    data = {}
    if lock_reason:
        data["lock_reason"] = lock_reason
    return github_put(f"/repos/{owner}/{repo}/issues/{issue_number}/lock", data)


def unlock_issue(owner: str, repo: str, issue_number: int) -> Any:
    """Unlock an issue.

    Args:
        owner: Repository owner
        repo: Repository name
        issue_number: Issue number
    """
    return github_delete(f"/repos/{owner}/{repo}/issues/{issue_number}/lock")


def list_issue_comments(owner: str, repo: str, issue_number: int, since: Optional[str] = None,
                        per_page: int = 30, page: int = 1) -> Any:
    """List comments on an issue.

    Args:
        owner: Repository owner
        repo: Repository name
        issue_number: Issue number
        since: Only comments updated after this ISO 8601 timestamp
        per_page: Results per page (max 100)
        page: Page number
    """
    params = {"per_page": per_page, "page": page}
    if since:
        params["since"] = since
    return github_get(f"/repos/{owner}/{repo}/issues/{issue_number}/comments", params)


def create_issue_comment(owner: str, repo: str, issue_number: int, body: str) -> Any:
    """Create a comment on an issue.

    Args:
        owner: Repository owner
        repo: Repository name
        issue_number: Issue number
        body: Comment body text
    """
    return github_post(f"/repos/{owner}/{repo}/issues/{issue_number}/comments", {"body": body})


def update_issue_comment(owner: str, repo: str, comment_id: int, body: str) -> Any:
    """Update an issue comment.

    Args:
        owner: Repository owner
        repo: Repository name
        comment_id: Comment ID
        body: New comment body text
    """
    return github_patch(f"/repos/{owner}/{repo}/issues/comments/{comment_id}", {"body": body})


def delete_issue_comment(owner: str, repo: str, comment_id: int) -> Any:
    """Delete an issue comment.

    Args:
        owner: Repository owner
        repo: Repository name
        comment_id: Comment ID
    """
    return github_delete(f"/repos/{owner}/{repo}/issues/comments/{comment_id}")


def list_issue_labels(owner: str, repo: str, issue_number: int, per_page: int = 30, page: int = 1) -> Any:
    """List labels on an issue.

    Args:
        owner: Repository owner
        repo: Repository name
        issue_number: Issue number
        per_page: Results per page (max 100)
        page: Page number
    """
    return github_get(f"/repos/{owner}/{repo}/issues/{issue_number}/labels", {"per_page": per_page, "page": page})


def add_labels_to_issue(owner: str, repo: str, issue_number: int, labels: list) -> Any:
    """Add labels to an issue.

    Args:
        owner: Repository owner
        repo: Repository name
        issue_number: Issue number
        labels: List of label names to add
    """
    return github_post(f"/repos/{owner}/{repo}/issues/{issue_number}/labels", {"labels": labels})


def remove_label_from_issue(owner: str, repo: str, issue_number: int, name: str) -> Any:
    """Remove a label from an issue.

    Args:
        owner: Repository owner
        repo: Repository name
        issue_number: Issue number
        name: Label name to remove
    """
    return github_delete(f"/repos/{owner}/{repo}/issues/{issue_number}/labels/{name}")


def set_labels_for_issue(owner: str, repo: str, issue_number: int, labels: list) -> Any:
    """Set labels for an issue (replaces all existing labels).

    Args:
        owner: Repository owner
        repo: Repository name
        issue_number: Issue number
        labels: List of label names to set
    """
    return github_put(f"/repos/{owner}/{repo}/issues/{issue_number}/labels", {"labels": labels})


def list_repository_labels(owner: str, repo: str, per_page: int = 30, page: int = 1) -> Any:
    """List all labels for a repository.

    Args:
        owner: Repository owner
        repo: Repository name
        per_page: Results per page (max 100)
        page: Page number
    """
    return github_get(f"/repos/{owner}/{repo}/labels", {"per_page": per_page, "page": page})


def create_label(owner: str, repo: str, name: str, color: Optional[str] = None,
                 description: Optional[str] = None) -> Any:
    """Create a label in a repository.

    Args:
        owner: Repository owner
        repo: Repository name
        name: Label name
        color: Color hex code (without #)
        description: Label description
    """
    data = {"name": name}
    if color:
        data["color"] = color
    if description:
        data["description"] = description
    return github_post(f"/repos/{owner}/{repo}/labels", data)


def get_label(owner: str, repo: str, name: str) -> Any:
    """Get a label.

    Args:
        owner: Repository owner
        repo: Repository name
        name: Label name
    """
    return github_get(f"/repos/{owner}/{repo}/labels/{name}")


def update_label(owner: str, repo: str, name: str, new_name: Optional[str] = None,
                 color: Optional[str] = None, description: Optional[str] = None) -> Any:
    """Update a label.

    Args:
        owner: Repository owner
        repo: Repository name
        name: Current label name
        new_name: New label name
        color: New color hex code
        description: New description
    """
    data = {}
    if new_name:
        data["new_name"] = new_name
    if color:
        data["color"] = color
    if description is not None:
        data["description"] = description
    return github_patch(f"/repos/{owner}/{repo}/labels/{name}", data)


def delete_label(owner: str, repo: str, name: str) -> Any:
    """Delete a label.

    Args:
        owner: Repository owner
        repo: Repository name
        name: Label name
    """
    return github_delete(f"/repos/{owner}/{repo}/labels/{name}")


def add_assignees_to_issue(owner: str, repo: str, issue_number: int, assignees: list) -> Any:
    """Add assignees to an issue.

    Args:
        owner: Repository owner
        repo: Repository name
        issue_number: Issue number
        assignees: List of usernames to assign
    """
    return github_post(f"/repos/{owner}/{repo}/issues/{issue_number}/assignees", {"assignees": assignees})


def remove_assignees_from_issue(owner: str, repo: str, issue_number: int, assignees: list) -> Any:
    """Remove assignees from an issue.

    Args:
        owner: Repository owner
        repo: Repository name
        issue_number: Issue number
        assignees: List of usernames to remove
    """
    return github_delete(f"/repos/{owner}/{repo}/issues/{issue_number}/assignees", {"assignees": assignees})


def list_milestones(owner: str, repo: str, state: str = "open", sort: str = "due_on",
                    direction: str = "asc", per_page: int = 30, page: int = 1) -> Any:
    """List milestones for a repository.

    Args:
        owner: Repository owner
        repo: Repository name
        state: State filter (open, closed, all)
        sort: Sort by (due_on, completeness)
        direction: Sort direction (asc, desc)
        per_page: Results per page (max 100)
        page: Page number
    """
    return github_get(f"/repos/{owner}/{repo}/milestones",
                      {"state": state, "sort": sort, "direction": direction, "per_page": per_page, "page": page})


def create_milestone(owner: str, repo: str, title: str, state: str = "open",
                     description: Optional[str] = None, due_on: Optional[str] = None) -> Any:
    """Create a milestone.

    Args:
        owner: Repository owner
        repo: Repository name
        title: Milestone title
        state: State (open, closed)
        description: Description
        due_on: Due date ISO 8601 timestamp
    """
    data = {"title": title, "state": state}
    if description:
        data["description"] = description
    if due_on:
        data["due_on"] = due_on
    return github_post(f"/repos/{owner}/{repo}/milestones", data)


def get_milestone(owner: str, repo: str, milestone_number: int) -> Any:
    """Get a milestone.

    Args:
        owner: Repository owner
        repo: Repository name
        milestone_number: Milestone number
    """
    return github_get(f"/repos/{owner}/{repo}/milestones/{milestone_number}")


def update_milestone(owner: str, repo: str, milestone_number: int, title: Optional[str] = None,
                     state: Optional[str] = None, description: Optional[str] = None,
                     due_on: Optional[str] = None) -> Any:
    """Update a milestone.

    Args:
        owner: Repository owner
        repo: Repository name
        milestone_number: Milestone number
        title: New title
        state: New state (open, closed)
        description: New description
        due_on: New due date
    """
    data = {}
    if title:
        data["title"] = title
    if state:
        data["state"] = state
    if description is not None:
        data["description"] = description
    if due_on is not None:
        data["due_on"] = due_on
    return github_patch(f"/repos/{owner}/{repo}/milestones/{milestone_number}", data)


def delete_milestone(owner: str, repo: str, milestone_number: int) -> Any:
    """Delete a milestone.

    Args:
        owner: Repository owner
        repo: Repository name
        milestone_number: Milestone number
    """
    return github_delete(f"/repos/{owner}/{repo}/milestones/{milestone_number}")


def list_issue_events(owner: str, repo: str, issue_number: int, per_page: int = 30, page: int = 1) -> Any:
    """List events for an issue.

    Args:
        owner: Repository owner
        repo: Repository name
        issue_number: Issue number
        per_page: Results per page (max 100)
        page: Page number
    """
    return github_get(f"/repos/{owner}/{repo}/issues/{issue_number}/events", {"per_page": per_page, "page": page})


def list_issue_timeline(owner: str, repo: str, issue_number: int, per_page: int = 30, page: int = 1) -> Any:
    """List timeline events for an issue.

    Args:
        owner: Repository owner
        repo: Repository name
        issue_number: Issue number
        per_page: Results per page (max 100)
        page: Page number
    """
    return github_get(f"/repos/{owner}/{repo}/issues/{issue_number}/timeline", {"per_page": per_page, "page": page})
