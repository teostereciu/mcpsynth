"""
MCP tools for Jira Issues (CRUD, assign, transition, metadata).
"""

from typing import Any, Dict, List, Optional
from mcp.server.fastmcp import FastMCP
from generated_tools.client import jira_get, jira_post, jira_put, jira_delete

mcp = FastMCP("jira-issues")


@mcp.tool()
def get_issue(
    issue_id_or_key: str,
    fields: Optional[str] = None,
    expand: Optional[str] = None,
    properties: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Get a single Jira issue by ID or key.

    Args:
        issue_id_or_key: The issue ID or key (e.g. 'PROJ-123').
        fields: Comma-separated list of fields to return (e.g. 'summary,status,assignee').
        expand: Comma-separated list of entities to expand (e.g. 'renderedFields,transitions').
        properties: Comma-separated list of issue properties to return.
    """
    params: Dict[str, Any] = {}
    if fields:
        params["fields"] = fields
    if expand:
        params["expand"] = expand
    if properties:
        params["properties"] = properties
    return jira_get(f"/issue/{issue_id_or_key}", params=params)


@mcp.tool()
def create_issue(
    project_key: str,
    summary: str,
    issue_type: str = "Task",
    description: Optional[str] = None,
    assignee_account_id: Optional[str] = None,
    priority: Optional[str] = None,
    labels: Optional[List[str]] = None,
    components: Optional[List[str]] = None,
    fix_versions: Optional[List[str]] = None,
    parent_key: Optional[str] = None,
    story_points: Optional[float] = None,
    due_date: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Create a new Jira issue.

    Args:
        project_key: The project key (e.g. 'PROJ').
        summary: Issue summary/title.
        issue_type: Issue type name (e.g. 'Task', 'Bug', 'Story', 'Epic', 'Sub-task').
        description: Plain-text description (converted to Atlassian Document Format).
        assignee_account_id: Account ID of the assignee.
        priority: Priority name (e.g. 'High', 'Medium', 'Low').
        labels: List of label strings.
        components: List of component names.
        fix_versions: List of version names.
        parent_key: Parent issue key (for sub-tasks or child issues).
        story_points: Story points estimate (uses 'story_points' field).
        due_date: Due date in YYYY-MM-DD format.
    """
    fields: Dict[str, Any] = {
        "project": {"key": project_key},
        "summary": summary,
        "issuetype": {"name": issue_type},
    }
    if description:
        fields["description"] = {
            "type": "doc",
            "version": 1,
            "content": [
                {
                    "type": "paragraph",
                    "content": [{"type": "text", "text": description}],
                }
            ],
        }
    if assignee_account_id:
        fields["assignee"] = {"accountId": assignee_account_id}
    if priority:
        fields["priority"] = {"name": priority}
    if labels:
        fields["labels"] = labels
    if components:
        fields["components"] = [{"name": c} for c in components]
    if fix_versions:
        fields["fixVersions"] = [{"name": v} for v in fix_versions]
    if parent_key:
        fields["parent"] = {"key": parent_key}
    if story_points is not None:
        fields["story_points"] = story_points
    if due_date:
        fields["duedate"] = due_date
    return jira_post("/issue", json={"fields": fields})


@mcp.tool()
def update_issue(
    issue_id_or_key: str,
    summary: Optional[str] = None,
    description: Optional[str] = None,
    assignee_account_id: Optional[str] = None,
    priority: Optional[str] = None,
    labels: Optional[List[str]] = None,
    components: Optional[List[str]] = None,
    fix_versions: Optional[List[str]] = None,
    due_date: Optional[str] = None,
    story_points: Optional[float] = None,
) -> Dict[str, Any]:
    """
    Update fields on an existing Jira issue.

    Args:
        issue_id_or_key: The issue ID or key.
        summary: New summary/title.
        description: New plain-text description.
        assignee_account_id: Account ID of the new assignee.
        priority: New priority name.
        labels: New list of labels (replaces existing).
        components: New list of component names (replaces existing).
        fix_versions: New list of fix version names (replaces existing).
        due_date: Due date in YYYY-MM-DD format.
        story_points: Story points estimate.
    """
    fields: Dict[str, Any] = {}
    if summary is not None:
        fields["summary"] = summary
    if description is not None:
        fields["description"] = {
            "type": "doc",
            "version": 1,
            "content": [
                {
                    "type": "paragraph",
                    "content": [{"type": "text", "text": description}],
                }
            ],
        }
    if assignee_account_id is not None:
        fields["assignee"] = {"accountId": assignee_account_id}
    if priority is not None:
        fields["priority"] = {"name": priority}
    if labels is not None:
        fields["labels"] = labels
    if components is not None:
        fields["components"] = [{"name": c} for c in components]
    if fix_versions is not None:
        fields["fixVersions"] = [{"name": v} for v in fix_versions]
    if due_date is not None:
        fields["duedate"] = due_date
    if story_points is not None:
        fields["story_points"] = story_points
    if not fields:
        return {"error": "No fields provided to update."}
    return jira_put(f"/issue/{issue_id_or_key}", json={"fields": fields})


@mcp.tool()
def delete_issue(issue_id_or_key: str, delete_subtasks: bool = False) -> Dict[str, Any]:
    """
    Delete a Jira issue.

    Args:
        issue_id_or_key: The issue ID or key.
        delete_subtasks: If True, also delete sub-tasks of this issue.
    """
    params = {"deleteSubtasks": "true" if delete_subtasks else "false"}
    return jira_delete(f"/issue/{issue_id_or_key}", params=params)


@mcp.tool()
def assign_issue(issue_id_or_key: str, account_id: Optional[str] = None) -> Dict[str, Any]:
    """
    Assign a Jira issue to a user, or unassign it.

    Args:
        issue_id_or_key: The issue ID or key.
        account_id: Account ID of the assignee. Pass None or omit to unassign.
    """
    body: Dict[str, Any] = {"accountId": account_id}
    return jira_put(f"/issue/{issue_id_or_key}/assignee", json=body)


@mcp.tool()
def get_issue_transitions(issue_id_or_key: str) -> Dict[str, Any]:
    """
    Get available workflow transitions for an issue.

    Args:
        issue_id_or_key: The issue ID or key.
    """
    return jira_get(f"/issue/{issue_id_or_key}/transitions")


@mcp.tool()
def transition_issue(
    issue_id_or_key: str,
    transition_id: str,
    comment: Optional[str] = None,
    resolution: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Perform a workflow transition on an issue (e.g. move to 'In Progress' or 'Done').

    Args:
        issue_id_or_key: The issue ID or key.
        transition_id: The ID of the transition to perform (from get_issue_transitions).
        comment: Optional comment to add when transitioning.
        resolution: Optional resolution name (e.g. 'Fixed', 'Won't Fix') for closing transitions.
    """
    body: Dict[str, Any] = {"transition": {"id": transition_id}}
    if comment:
        body["update"] = {
            "comment": [
                {
                    "add": {
                        "body": {
                            "type": "doc",
                            "version": 1,
                            "content": [
                                {
                                    "type": "paragraph",
                                    "content": [{"type": "text", "text": comment}],
                                }
                            ],
                        }
                    }
                }
            ]
        }
    if resolution:
        body.setdefault("fields", {})["resolution"] = {"name": resolution}
    return jira_post(f"/issue/{issue_id_or_key}/transitions", json=body)


@mcp.tool()
def get_issue_metadata(issue_id_or_key: str) -> Dict[str, Any]:
    """
    Get editable field metadata for an issue (useful before updating).

    Args:
        issue_id_or_key: The issue ID or key.
    """
    return jira_get(f"/issue/{issue_id_or_key}/editmeta")


@mcp.tool()
def get_create_issue_metadata(
    project_keys: Optional[str] = None,
    issue_type_names: Optional[str] = None,
    expand: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Get metadata needed to create issues (available fields, issue types per project).

    Args:
        project_keys: Comma-separated project keys to filter by.
        issue_type_names: Comma-separated issue type names to filter by.
        expand: Expand options (e.g. 'projects.issuetypes.fields').
    """
    params: Dict[str, Any] = {}
    if project_keys:
        params["projectKeys"] = project_keys
    if issue_type_names:
        params["issuetypeNames"] = issue_type_names
    if expand:
        params["expand"] = expand
    return jira_get("/issue/createmeta", params=params)


@mcp.tool()
def bulk_create_issues(issues: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Create multiple Jira issues in a single request.

    Args:
        issues: List of issue field dicts. Each dict must contain at minimum:
                {"project": {"key": "PROJ"}, "summary": "...", "issuetype": {"name": "Task"}}
    """
    issue_updates = [{"fields": issue} for issue in issues]
    return jira_post("/issue/bulk", json={"issueUpdates": issue_updates})


@mcp.tool()
def get_issue_changelog(
    issue_id_or_key: str,
    start_at: int = 0,
    max_results: int = 50,
) -> Dict[str, Any]:
    """
    Get the changelog (history of field changes) for an issue.

    Args:
        issue_id_or_key: The issue ID or key.
        start_at: Index of the first item to return (for pagination).
        max_results: Maximum number of items to return.
    """
    params = {"startAt": start_at, "maxResults": max_results}
    return jira_get(f"/issue/{issue_id_or_key}/changelog", params=params)


@mcp.tool()
def get_issue_watchers(issue_id_or_key: str) -> Dict[str, Any]:
    """
    Get the list of watchers for an issue.

    Args:
        issue_id_or_key: The issue ID or key.
    """
    return jira_get(f"/issue/{issue_id_or_key}/watchers")


@mcp.tool()
def add_watcher(issue_id_or_key: str, account_id: str) -> Dict[str, Any]:
    """
    Add a user as a watcher on an issue.

    Args:
        issue_id_or_key: The issue ID or key.
        account_id: The account ID of the user to add as a watcher.
    """
    return jira_post(f"/issue/{issue_id_or_key}/watchers", json=account_id)


@mcp.tool()
def remove_watcher(issue_id_or_key: str, account_id: str) -> Dict[str, Any]:
    """
    Remove a user from the watchers of an issue.

    Args:
        issue_id_or_key: The issue ID or key.
        account_id: The account ID of the user to remove.
    """
    return jira_delete(
        f"/issue/{issue_id_or_key}/watchers", params={"accountId": account_id}
    )


@mcp.tool()
def get_issue_votes(issue_id_or_key: str) -> Dict[str, Any]:
    """
    Get vote information for an issue.

    Args:
        issue_id_or_key: The issue ID or key.
    """
    return jira_get(f"/issue/{issue_id_or_key}/votes")


@mcp.tool()
def add_vote(issue_id_or_key: str) -> Dict[str, Any]:
    """
    Cast a vote for an issue (vote as the authenticated user).

    Args:
        issue_id_or_key: The issue ID or key.
    """
    return jira_post(f"/issue/{issue_id_or_key}/votes")


@mcp.tool()
def remove_vote(issue_id_or_key: str) -> Dict[str, Any]:
    """
    Remove the authenticated user's vote from an issue.

    Args:
        issue_id_or_key: The issue ID or key.
    """
    return jira_delete(f"/issue/{issue_id_or_key}/votes")


@mcp.tool()
def get_issue_remote_links(issue_id_or_key: str) -> Dict[str, Any]:
    """
    Get remote links (web links) attached to an issue.

    Args:
        issue_id_or_key: The issue ID or key.
    """
    return jira_get(f"/issue/{issue_id_or_key}/remotelink")


@mcp.tool()
def add_remote_link(
    issue_id_or_key: str,
    url: str,
    title: str,
    summary: Optional[str] = None,
    relationship: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Add a remote (web) link to an issue.

    Args:
        issue_id_or_key: The issue ID or key.
        url: The URL of the remote resource.
        title: Display title for the link.
        summary: Optional summary/description of the link.
        relationship: Relationship type (e.g. 'relates to', 'mentioned in').
    """
    body: Dict[str, Any] = {
        "object": {"url": url, "title": title},
    }
    if summary:
        body["object"]["summary"] = summary
    if relationship:
        body["relationship"] = relationship
    return jira_post(f"/issue/{issue_id_or_key}/remotelink", json=body)


@mcp.tool()
def delete_remote_link(issue_id_or_key: str, link_id: str) -> Dict[str, Any]:
    """
    Delete a remote link from an issue.

    Args:
        issue_id_or_key: The issue ID or key.
        link_id: The ID of the remote link to delete.
    """
    return jira_delete(f"/issue/{issue_id_or_key}/remotelink/{link_id}")


@mcp.tool()
def notify_issue(
    issue_id_or_key: str,
    subject: str,
    text_body: str,
    html_body: Optional[str] = None,
    to_reporter: bool = False,
    to_assignee: bool = False,
    to_watchers: bool = False,
    to_voters: bool = False,
) -> Dict[str, Any]:
    """
    Send a notification email about an issue.

    Args:
        issue_id_or_key: The issue ID or key.
        subject: Email subject.
        text_body: Plain-text email body.
        html_body: Optional HTML email body.
        to_reporter: Send to the issue reporter.
        to_assignee: Send to the issue assignee.
        to_watchers: Send to all watchers.
        to_voters: Send to all voters.
    """
    body: Dict[str, Any] = {
        "subject": subject,
        "textBody": text_body,
        "to": {
            "reporter": to_reporter,
            "assignee": to_assignee,
            "watchers": to_watchers,
            "voters": to_voters,
        },
    }
    if html_body:
        body["htmlBody"] = html_body
    return jira_post(f"/issue/{issue_id_or_key}/notify", json=body)
