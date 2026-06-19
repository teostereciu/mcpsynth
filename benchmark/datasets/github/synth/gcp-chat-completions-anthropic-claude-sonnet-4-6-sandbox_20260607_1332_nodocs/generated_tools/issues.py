"""MCP tools for GitHub Issues (CRUD, labels, assignees, comments, milestones)."""
from mcp.server.fastmcp import FastMCP
from .client import gh_get, gh_post, gh_patch, gh_delete, gh_put

def register(mcp: FastMCP):

    @mcp.tool()
    def list_repo_issues(
        owner: str,
        repo: str,
        state: str = "open",
        labels: str = "",
        assignee: str = "",
        milestone: str = "",
        sort: str = "created",
        direction: str = "desc",
        per_page: int = 30,
        page: int = 1,
    ) -> dict | list:
        """List issues for a repository. state: open|closed|all."""
        params = {"state": state, "sort": sort, "direction": direction,
                  "per_page": per_page, "page": page}
        if labels:
            params["labels"] = labels
        if assignee:
            params["assignee"] = assignee
        if milestone:
            params["milestone"] = milestone
        return gh_get(f"/repos/{owner}/{repo}/issues", params=params)

    @mcp.tool()
    def get_issue(owner: str, repo: str, issue_number: int) -> dict | list:
        """Get a single issue by number."""
        return gh_get(f"/repos/{owner}/{repo}/issues/{issue_number}")

    @mcp.tool()
    def create_issue(
        owner: str,
        repo: str,
        title: str,
        body: str = "",
        assignees: list[str] | None = None,
        labels: list[str] | None = None,
        milestone: int | None = None,
    ) -> dict | list:
        """Create a new issue in a repository."""
        payload: dict = {"title": title}
        if body:
            payload["body"] = body
        if assignees:
            payload["assignees"] = assignees
        if labels:
            payload["labels"] = labels
        if milestone is not None:
            payload["milestone"] = milestone
        return gh_post(f"/repos/{owner}/{repo}/issues", json=payload)

    @mcp.tool()
    def update_issue(
        owner: str,
        repo: str,
        issue_number: int,
        title: str = "",
        body: str = "",
        state: str = "",
        assignees: list[str] | None = None,
        labels: list[str] | None = None,
        milestone: int | None = None,
    ) -> dict | list:
        """Update an existing issue (title, body, state, assignees, labels, milestone)."""
        payload: dict = {}
        if title:
            payload["title"] = title
        if body:
            payload["body"] = body
        if state:
            payload["state"] = state
        if assignees is not None:
            payload["assignees"] = assignees
        if labels is not None:
            payload["labels"] = labels
        if milestone is not None:
            payload["milestone"] = milestone
        return gh_patch(f"/repos/{owner}/{repo}/issues/{issue_number}", json=payload)

    @mcp.tool()
    def lock_issue(owner: str, repo: str, issue_number: int, lock_reason: str = "") -> dict | list:
        """Lock an issue. lock_reason: off-topic|too heated|resolved|spam."""
        payload: dict = {}
        if lock_reason:
            payload["lock_reason"] = lock_reason
        return gh_put(f"/repos/{owner}/{repo}/issues/{issue_number}/lock", json=payload)

    @mcp.tool()
    def unlock_issue(owner: str, repo: str, issue_number: int) -> dict | list:
        """Unlock an issue."""
        return gh_delete(f"/repos/{owner}/{repo}/issues/{issue_number}/lock")

    # --- Comments ---

    @mcp.tool()
    def list_issue_comments(
        owner: str, repo: str, issue_number: int, per_page: int = 30, page: int = 1
    ) -> dict | list:
        """List comments on an issue."""
        return gh_get(f"/repos/{owner}/{repo}/issues/{issue_number}/comments",
                      params={"per_page": per_page, "page": page})

    @mcp.tool()
    def get_issue_comment(owner: str, repo: str, comment_id: int) -> dict | list:
        """Get a single issue comment by ID."""
        return gh_get(f"/repos/{owner}/{repo}/issues/comments/{comment_id}")

    @mcp.tool()
    def create_issue_comment(owner: str, repo: str, issue_number: int, body: str) -> dict | list:
        """Create a comment on an issue or pull request."""
        return gh_post(f"/repos/{owner}/{repo}/issues/{issue_number}/comments", json={"body": body})

    @mcp.tool()
    def update_issue_comment(owner: str, repo: str, comment_id: int, body: str) -> dict | list:
        """Update an issue comment."""
        return gh_patch(f"/repos/{owner}/{repo}/issues/comments/{comment_id}", json={"body": body})

    @mcp.tool()
    def delete_issue_comment(owner: str, repo: str, comment_id: int) -> dict | list:
        """Delete an issue comment."""
        return gh_delete(f"/repos/{owner}/{repo}/issues/comments/{comment_id}")

    # --- Labels ---

    @mcp.tool()
    def list_issue_labels(owner: str, repo: str, issue_number: int) -> dict | list:
        """List labels on an issue."""
        return gh_get(f"/repos/{owner}/{repo}/issues/{issue_number}/labels")

    @mcp.tool()
    def add_labels_to_issue(owner: str, repo: str, issue_number: int, labels: list[str]) -> dict | list:
        """Add labels to an issue."""
        return gh_post(f"/repos/{owner}/{repo}/issues/{issue_number}/labels", json={"labels": labels})

    @mcp.tool()
    def remove_label_from_issue(owner: str, repo: str, issue_number: int, label: str) -> dict | list:
        """Remove a label from an issue."""
        return gh_delete(f"/repos/{owner}/{repo}/issues/{issue_number}/labels/{label}")

    @mcp.tool()
    def replace_issue_labels(owner: str, repo: str, issue_number: int, labels: list[str]) -> dict | list:
        """Replace all labels on an issue."""
        return gh_put(f"/repos/{owner}/{repo}/issues/{issue_number}/labels", json={"labels": labels})

    @mcp.tool()
    def list_repo_labels(owner: str, repo: str, per_page: int = 30, page: int = 1) -> dict | list:
        """List all labels for a repository."""
        return gh_get(f"/repos/{owner}/{repo}/labels", params={"per_page": per_page, "page": page})

    @mcp.tool()
    def create_label(owner: str, repo: str, name: str, color: str, description: str = "") -> dict | list:
        """Create a label in a repository. color is a 6-char hex without #."""
        payload: dict = {"name": name, "color": color}
        if description:
            payload["description"] = description
        return gh_post(f"/repos/{owner}/{repo}/labels", json=payload)

    @mcp.tool()
    def update_label(
        owner: str, repo: str, label_name: str,
        new_name: str = "", color: str = "", description: str = ""
    ) -> dict | list:
        """Update a label."""
        payload: dict = {}
        if new_name:
            payload["new_name"] = new_name
        if color:
            payload["color"] = color
        if description:
            payload["description"] = description
        return gh_patch(f"/repos/{owner}/{repo}/labels/{label_name}", json=payload)

    @mcp.tool()
    def delete_label(owner: str, repo: str, label_name: str) -> dict | list:
        """Delete a label from a repository."""
        return gh_delete(f"/repos/{owner}/{repo}/labels/{label_name}")

    # --- Assignees ---

    @mcp.tool()
    def list_issue_assignees(owner: str, repo: str, per_page: int = 30, page: int = 1) -> dict | list:
        """List available assignees for a repository."""
        return gh_get(f"/repos/{owner}/{repo}/assignees", params={"per_page": per_page, "page": page})

    @mcp.tool()
    def add_assignees_to_issue(owner: str, repo: str, issue_number: int, assignees: list[str]) -> dict | list:
        """Add assignees to an issue."""
        return gh_post(f"/repos/{owner}/{repo}/issues/{issue_number}/assignees", json={"assignees": assignees})

    @mcp.tool()
    def remove_assignees_from_issue(owner: str, repo: str, issue_number: int, assignees: list[str]) -> dict | list:
        """Remove assignees from an issue."""
        return gh_delete(f"/repos/{owner}/{repo}/issues/{issue_number}/assignees", json={"assignees": assignees})

    # --- Milestones ---

    @mcp.tool()
    def list_milestones(
        owner: str, repo: str, state: str = "open",
        sort: str = "due_on", direction: str = "asc",
        per_page: int = 30, page: int = 1
    ) -> dict | list:
        """List milestones for a repository."""
        return gh_get(f"/repos/{owner}/{repo}/milestones",
                      params={"state": state, "sort": sort, "direction": direction,
                              "per_page": per_page, "page": page})

    @mcp.tool()
    def get_milestone(owner: str, repo: str, milestone_number: int) -> dict | list:
        """Get a milestone by number."""
        return gh_get(f"/repos/{owner}/{repo}/milestones/{milestone_number}")

    @mcp.tool()
    def create_milestone(
        owner: str, repo: str, title: str,
        state: str = "open", description: str = "", due_on: str = ""
    ) -> dict | list:
        """Create a milestone. due_on is ISO 8601 format."""
        payload: dict = {"title": title, "state": state}
        if description:
            payload["description"] = description
        if due_on:
            payload["due_on"] = due_on
        return gh_post(f"/repos/{owner}/{repo}/milestones", json=payload)

    @mcp.tool()
    def update_milestone(
        owner: str, repo: str, milestone_number: int,
        title: str = "", state: str = "", description: str = "", due_on: str = ""
    ) -> dict | list:
        """Update a milestone."""
        payload: dict = {}
        if title:
            payload["title"] = title
        if state:
            payload["state"] = state
        if description:
            payload["description"] = description
        if due_on:
            payload["due_on"] = due_on
        return gh_patch(f"/repos/{owner}/{repo}/milestones/{milestone_number}", json=payload)

    @mcp.tool()
    def delete_milestone(owner: str, repo: str, milestone_number: int) -> dict | list:
        """Delete a milestone."""
        return gh_delete(f"/repos/{owner}/{repo}/milestones/{milestone_number}")

    # --- Reactions ---

    @mcp.tool()
    def list_issue_reactions(owner: str, repo: str, issue_number: int) -> dict | list:
        """List reactions for an issue."""
        return gh_get(f"/repos/{owner}/{repo}/issues/{issue_number}/reactions")

    @mcp.tool()
    def create_issue_reaction(owner: str, repo: str, issue_number: int, content: str) -> dict | list:
        """Create a reaction on an issue. content: +1|-1|laugh|confused|heart|hooray|rocket|eyes."""
        return gh_post(f"/repos/{owner}/{repo}/issues/{issue_number}/reactions", json={"content": content})
