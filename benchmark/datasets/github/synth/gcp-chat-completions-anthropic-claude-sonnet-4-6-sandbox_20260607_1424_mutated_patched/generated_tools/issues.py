"""GitHub Issues, Comments, Labels, Assignees, and Milestones tools."""
import os
import requests
from mcp.server.fastmcp import FastMCP

BASE_URL = os.environ.get("GITHUB_API_BASE_URL", "https://api.github.com")
TOKEN = os.environ.get("GITHUB_TOKEN", "")

def _headers():
    h = {"Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28"}
    if TOKEN:
        h["Authorization"] = f"Bearer {TOKEN}"
    return h

def _get(path, params=None):
    try:
        r = requests.get(f"{BASE_URL}{path}", headers=_headers(), params=params, timeout=30)
        if r.status_code == 204:
            return {"status": "no_content"}
        return r.json()
    except Exception as e:
        return {"error": str(e)}

def _post(path, json=None):
    try:
        r = requests.post(f"{BASE_URL}{path}", headers=_headers(), json=json, timeout=30)
        if r.status_code == 204:
            return {"status": "no_content"}
        return r.json()
    except Exception as e:
        return {"error": str(e)}

def _patch(path, json=None):
    try:
        r = requests.patch(f"{BASE_URL}{path}", headers=_headers(), json=json, timeout=30)
        if r.status_code == 204:
            return {"status": "no_content"}
        return r.json()
    except Exception as e:
        return {"error": str(e)}

def _put(path, json=None):
    try:
        r = requests.put(f"{BASE_URL}{path}", headers=_headers(), json=json, timeout=30)
        if r.status_code == 204:
            return {"status": "no_content"}
        return r.json()
    except Exception as e:
        return {"error": str(e)}

def _delete(path, json=None):
    try:
        r = requests.delete(f"{BASE_URL}{path}", headers=_headers(), json=json, timeout=30)
        if r.status_code == 204:
            return {"status": "no_content"}
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def register_issues_tools(mcp: FastMCP):

    @mcp.tool()
    def list_repo_issues(owner: str, repo: str, state: str = "open", labels: str = "",
                         sort: str = "created", direction: str = "desc",
                         since: str = "", per_page: int = 30, page: int = 1) -> dict:
        """List issues for a repository. state: open|closed|all."""
        params = {"state": state, "sort": sort, "direction": direction,
                  "per_page": per_page, "page": page}
        if labels:
            params["labels"] = labels
        if since:
            params["since"] = since
        return _get(f"/repos/{owner}/{repo}/issues", params)

    @mcp.tool()
    def get_issue(owner: str, repo: str, issue_number: int) -> dict:
        """Get a single issue by number."""
        return _get(f"/repos/{owner}/{repo}/issues/{issue_number}")

    @mcp.tool()
    def create_issue(owner: str, repo: str, title: str, body: str = "",
                     assignees: list = None, labels: list = None,
                     milestone: int = None) -> dict:
        """Create a new issue in a repository."""
        payload = {"title": title}
        if body:
            payload["body"] = body
        if assignees:
            payload["assignees"] = assignees
        if labels:
            payload["labels"] = labels
        if milestone is not None:
            payload["milestone"] = milestone
        return _post(f"/repos/{owner}/{repo}/issues", payload)

    @mcp.tool()
    def update_issue(owner: str, repo: str, issue_number: int,
                     title: str = None, body: str = None, state: str = None,
                     assignees: list = None, labels: list = None,
                     milestone: int = None, state_reason: str = None) -> dict:
        """Update an existing issue. state: open|closed."""
        payload = {}
        if title is not None:
            payload["title"] = title
        if body is not None:
            payload["body"] = body
        if state is not None:
            payload["state"] = state
        if assignees is not None:
            payload["assignees"] = assignees
        if labels is not None:
            payload["labels"] = labels
        if milestone is not None:
            payload["milestone"] = milestone
        if state_reason is not None:
            payload["state_reason"] = state_reason
        return _patch(f"/repos/{owner}/{repo}/issues/{issue_number}", payload)

    @mcp.tool()
    def lock_issue(owner: str, repo: str, issue_number: int, lock_reason: str = "") -> dict:
        """Lock an issue. lock_reason: off-topic|too heated|resolved|spam."""
        payload = {}
        if lock_reason:
            payload["lock_reason"] = lock_reason
        return _put(f"/repos/{owner}/{repo}/issues/{issue_number}/lock", payload)

    @mcp.tool()
    def unlock_issue(owner: str, repo: str, issue_number: int) -> dict:
        """Unlock an issue."""
        return _delete(f"/repos/{owner}/{repo}/issues/{issue_number}/lock")

    @mcp.tool()
    def list_issue_comments(owner: str, repo: str, issue_number: int,
                            per_page: int = 30, page: int = 1) -> dict:
        """List comments on an issue."""
        return _get(f"/repos/{owner}/{repo}/issues/{issue_number}/comments",
                    {"per_page": per_page, "page": page})

    @mcp.tool()
    def get_issue_comment(owner: str, repo: str, comment_id: int) -> dict:
        """Get a single issue comment by ID."""
        return _get(f"/repos/{owner}/{repo}/issues/comments/{comment_id}")

    @mcp.tool()
    def create_issue_comment(owner: str, repo: str, issue_number: int, body: str) -> dict:
        """Create a comment on an issue or pull request."""
        return _post(f"/repos/{owner}/{repo}/issues/{issue_number}/comments", {"body": body})

    @mcp.tool()
    def update_issue_comment(owner: str, repo: str, comment_id: int, body: str) -> dict:
        """Update an issue comment."""
        return _patch(f"/repos/{owner}/{repo}/issues/comments/{comment_id}", {"body": body})

    @mcp.tool()
    def delete_issue_comment(owner: str, repo: str, comment_id: int) -> dict:
        """Delete an issue comment."""
        return _delete(f"/repos/{owner}/{repo}/issues/comments/{comment_id}")

    @mcp.tool()
    def list_issue_labels(owner: str, repo: str, issue_number: int) -> dict:
        """List labels on an issue."""
        return _get(f"/repos/{owner}/{repo}/issues/{issue_number}/labels")

    @mcp.tool()
    def add_labels_to_issue(owner: str, repo: str, issue_number: int, labels: list) -> dict:
        """Add labels to an issue."""
        return _post(f"/repos/{owner}/{repo}/issues/{issue_number}/labels", {"labels": labels})

    @mcp.tool()
    def set_labels_for_issue(owner: str, repo: str, issue_number: int, labels: list) -> dict:
        """Replace all labels on an issue."""
        return _put(f"/repos/{owner}/{repo}/issues/{issue_number}/labels", {"labels": labels})

    @mcp.tool()
    def remove_label_from_issue(owner: str, repo: str, issue_number: int, name: str) -> dict:
        """Remove a specific label from an issue."""
        return _delete(f"/repos/{owner}/{repo}/issues/{issue_number}/labels/{name}")

    @mcp.tool()
    def remove_all_labels_from_issue(owner: str, repo: str, issue_number: int) -> dict:
        """Remove all labels from an issue."""
        return _delete(f"/repos/{owner}/{repo}/issues/{issue_number}/labels")

    @mcp.tool()
    def list_repo_labels(owner: str, repo: str, per_page: int = 30, page: int = 1) -> dict:
        """List all labels for a repository."""
        return _get(f"/repos/{owner}/{repo}/labels", {"per_page": per_page, "page": page})

    @mcp.tool()
    def create_label(owner: str, repo: str, name: str, color: str, description: str = "") -> dict:
        """Create a label in a repository. color is hex without #."""
        payload = {"name": name, "color": color}
        if description:
            payload["description"] = description
        return _post(f"/repos/{owner}/{repo}/labels", payload)

    @mcp.tool()
    def update_label(owner: str, repo: str, name: str, new_name: str = None,
                     color: str = None, description: str = None) -> dict:
        """Update a label."""
        payload = {}
        if new_name is not None:
            payload["new_name"] = new_name
        if color is not None:
            payload["color"] = color
        if description is not None:
            payload["description"] = description
        return _patch(f"/repos/{owner}/{repo}/labels/{name}", payload)

    @mcp.tool()
    def delete_label(owner: str, repo: str, name: str) -> dict:
        """Delete a label from a repository."""
        return _delete(f"/repos/{owner}/{repo}/labels/{name}")

    @mcp.tool()
    def list_assignees(owner: str, repo: str, per_page: int = 30, page: int = 1) -> dict:
        """List available assignees for a repository."""
        return _get(f"/repos/{owner}/{repo}/assignees", {"per_page": per_page, "page": page})

    @mcp.tool()
    def add_assignees_to_issue(owner: str, repo: str, issue_number: int, assignees: list) -> dict:
        """Add assignees to an issue."""
        return _post(f"/repos/{owner}/{repo}/issues/{issue_number}/assignees", {"assignees": assignees})

    @mcp.tool()
    def remove_assignees_from_issue(owner: str, repo: str, issue_number: int, assignees: list) -> dict:
        """Remove assignees from an issue."""
        return _delete(f"/repos/{owner}/{repo}/issues/{issue_number}/assignees")

    @mcp.tool()
    def list_milestones(owner: str, repo: str, state: str = "open",
                        sort: str = "due_on", direction: str = "asc",
                        per_page: int = 30, page: int = 1) -> dict:
        """List milestones for a repository."""
        return _get(f"/repos/{owner}/{repo}/milestones",
                    {"state": state, "sort": sort, "direction": direction,
                     "per_page": per_page, "page": page})

    @mcp.tool()
    def get_milestone(owner: str, repo: str, milestone_number: int) -> dict:
        """Get a milestone by number."""
        return _get(f"/repos/{owner}/{repo}/milestones/{milestone_number}")

    @mcp.tool()
    def create_milestone(owner: str, repo: str, title: str, state: str = "open",
                         description: str = "", due_on: str = "") -> dict:
        """Create a milestone. due_on is ISO 8601 timestamp."""
        payload = {"title": title, "state": state}
        if description:
            payload["description"] = description
        if due_on:
            payload["due_on"] = due_on
        return _post(f"/repos/{owner}/{repo}/milestones", payload)

    @mcp.tool()
    def update_milestone(owner: str, repo: str, milestone_number: int,
                         title: str = None, state: str = None,
                         description: str = None, due_on: str = None) -> dict:
        """Update a milestone."""
        payload = {}
        if title is not None:
            payload["title"] = title
        if state is not None:
            payload["state"] = state
        if description is not None:
            payload["description"] = description
        if due_on is not None:
            payload["due_on"] = due_on
        return _patch(f"/repos/{owner}/{repo}/milestones/{milestone_number}", payload)

    @mcp.tool()
    def delete_milestone(owner: str, repo: str, milestone_number: int) -> dict:
        """Delete a milestone."""
        return _delete(f"/repos/{owner}/{repo}/milestones/{milestone_number}")
