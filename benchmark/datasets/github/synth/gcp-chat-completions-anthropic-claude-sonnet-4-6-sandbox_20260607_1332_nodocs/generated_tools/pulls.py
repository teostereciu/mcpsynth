"""MCP tools for GitHub Pull Requests (create, review, merge, comments)."""
from mcp.server.fastmcp import FastMCP
from .client import gh_get, gh_post, gh_patch, gh_delete, gh_put

def register(mcp: FastMCP):

    @mcp.tool()
    def list_pull_requests(
        owner: str,
        repo: str,
        state: str = "open",
        head: str = "",
        base: str = "",
        sort: str = "created",
        direction: str = "desc",
        per_page: int = 30,
        page: int = 1,
    ) -> dict | list:
        """List pull requests for a repository."""
        params: dict = {"state": state, "sort": sort, "direction": direction,
                        "per_page": per_page, "page": page}
        if head:
            params["head"] = head
        if base:
            params["base"] = base
        return gh_get(f"/repos/{owner}/{repo}/pulls", params=params)

    @mcp.tool()
    def get_pull_request(owner: str, repo: str, pull_number: int) -> dict | list:
        """Get a single pull request by number."""
        return gh_get(f"/repos/{owner}/{repo}/pulls/{pull_number}")

    @mcp.tool()
    def create_pull_request(
        owner: str,
        repo: str,
        title: str,
        head: str,
        base: str,
        body: str = "",
        draft: bool = False,
        maintainer_can_modify: bool = True,
    ) -> dict | list:
        """Create a pull request. head is the branch with changes, base is the target branch."""
        payload: dict = {
            "title": title,
            "head": head,
            "base": base,
            "draft": draft,
            "maintainer_can_modify": maintainer_can_modify,
        }
        if body:
            payload["body"] = body
        return gh_post(f"/repos/{owner}/{repo}/pulls", json=payload)

    @mcp.tool()
    def update_pull_request(
        owner: str,
        repo: str,
        pull_number: int,
        title: str = "",
        body: str = "",
        state: str = "",
        base: str = "",
        maintainer_can_modify: bool | None = None,
    ) -> dict | list:
        """Update a pull request (title, body, state open|closed, base branch)."""
        payload: dict = {}
        if title:
            payload["title"] = title
        if body:
            payload["body"] = body
        if state:
            payload["state"] = state
        if base:
            payload["base"] = base
        if maintainer_can_modify is not None:
            payload["maintainer_can_modify"] = maintainer_can_modify
        return gh_patch(f"/repos/{owner}/{repo}/pulls/{pull_number}", json=payload)

    @mcp.tool()
    def merge_pull_request(
        owner: str,
        repo: str,
        pull_number: int,
        commit_title: str = "",
        commit_message: str = "",
        merge_method: str = "merge",
    ) -> dict | list:
        """Merge a pull request. merge_method: merge|squash|rebase."""
        payload: dict = {"merge_method": merge_method}
        if commit_title:
            payload["commit_title"] = commit_title
        if commit_message:
            payload["commit_message"] = commit_message
        return gh_put(f"/repos/{owner}/{repo}/pulls/{pull_number}/merge", json=payload)

    @mcp.tool()
    def list_pull_request_commits(
        owner: str, repo: str, pull_number: int, per_page: int = 30, page: int = 1
    ) -> dict | list:
        """List commits on a pull request."""
        return gh_get(f"/repos/{owner}/{repo}/pulls/{pull_number}/commits",
                      params={"per_page": per_page, "page": page})

    @mcp.tool()
    def list_pull_request_files(
        owner: str, repo: str, pull_number: int, per_page: int = 30, page: int = 1
    ) -> dict | list:
        """List files changed in a pull request."""
        return gh_get(f"/repos/{owner}/{repo}/pulls/{pull_number}/files",
                      params={"per_page": per_page, "page": page})

    @mcp.tool()
    def check_pull_request_merged(owner: str, repo: str, pull_number: int) -> dict | list:
        """Check if a pull request has been merged."""
        return gh_get(f"/repos/{owner}/{repo}/pulls/{pull_number}/merge")

    # --- Reviews ---

    @mcp.tool()
    def list_pull_request_reviews(
        owner: str, repo: str, pull_number: int, per_page: int = 30, page: int = 1
    ) -> dict | list:
        """List reviews on a pull request."""
        return gh_get(f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews",
                      params={"per_page": per_page, "page": page})

    @mcp.tool()
    def get_pull_request_review(owner: str, repo: str, pull_number: int, review_id: int) -> dict | list:
        """Get a specific review on a pull request."""
        return gh_get(f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}")

    @mcp.tool()
    def create_pull_request_review(
        owner: str,
        repo: str,
        pull_number: int,
        event: str = "COMMENT",
        body: str = "",
        commit_id: str = "",
        comments: list[dict] | None = None,
    ) -> dict | list:
        """Create a review on a pull request. event: APPROVE|REQUEST_CHANGES|COMMENT."""
        payload: dict = {"event": event}
        if body:
            payload["body"] = body
        if commit_id:
            payload["commit_id"] = commit_id
        if comments:
            payload["comments"] = comments
        return gh_post(f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews", json=payload)

    @mcp.tool()
    def submit_pull_request_review(
        owner: str, repo: str, pull_number: int, review_id: int, event: str, body: str = ""
    ) -> dict | list:
        """Submit a pending review. event: APPROVE|REQUEST_CHANGES|COMMENT."""
        payload: dict = {"event": event}
        if body:
            payload["body"] = body
        return gh_post(f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}/events", json=payload)

    @mcp.tool()
    def dismiss_pull_request_review(
        owner: str, repo: str, pull_number: int, review_id: int, message: str
    ) -> dict | list:
        """Dismiss a pull request review."""
        return gh_put(f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}/dismissals",
                      json={"message": message})

    # --- Review Comments ---

    @mcp.tool()
    def list_pull_request_review_comments(
        owner: str, repo: str, pull_number: int, per_page: int = 30, page: int = 1
    ) -> dict | list:
        """List review comments on a pull request."""
        return gh_get(f"/repos/{owner}/{repo}/pulls/{pull_number}/comments",
                      params={"per_page": per_page, "page": page})

    @mcp.tool()
    def create_pull_request_review_comment(
        owner: str,
        repo: str,
        pull_number: int,
        body: str,
        commit_id: str,
        path: str,
        line: int | None = None,
        side: str = "RIGHT",
        in_reply_to: int | None = None,
    ) -> dict | list:
        """Create a review comment on a pull request diff."""
        payload: dict = {"body": body, "commit_id": commit_id, "path": path, "side": side}
        if line is not None:
            payload["line"] = line
        if in_reply_to is not None:
            payload["in_reply_to"] = in_reply_to
        return gh_post(f"/repos/{owner}/{repo}/pulls/{pull_number}/comments", json=payload)

    @mcp.tool()
    def update_pull_request_review_comment(
        owner: str, repo: str, comment_id: int, body: str
    ) -> dict | list:
        """Update a review comment on a pull request."""
        return gh_patch(f"/repos/{owner}/{repo}/pulls/comments/{comment_id}", json={"body": body})

    @mcp.tool()
    def delete_pull_request_review_comment(owner: str, repo: str, comment_id: int) -> dict | list:
        """Delete a review comment on a pull request."""
        return gh_delete(f"/repos/{owner}/{repo}/pulls/comments/{comment_id}")

    # --- Requested Reviewers ---

    @mcp.tool()
    def request_reviewers(
        owner: str,
        repo: str,
        pull_number: int,
        reviewers: list[str] | None = None,
        team_reviewers: list[str] | None = None,
    ) -> dict | list:
        """Request reviewers for a pull request."""
        payload: dict = {}
        if reviewers:
            payload["reviewers"] = reviewers
        if team_reviewers:
            payload["team_reviewers"] = team_reviewers
        return gh_post(f"/repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers", json=payload)

    @mcp.tool()
    def remove_requested_reviewers(
        owner: str,
        repo: str,
        pull_number: int,
        reviewers: list[str] | None = None,
        team_reviewers: list[str] | None = None,
    ) -> dict | list:
        """Remove requested reviewers from a pull request."""
        payload: dict = {}
        if reviewers:
            payload["reviewers"] = reviewers
        if team_reviewers:
            payload["team_reviewers"] = team_reviewers
        return gh_delete(f"/repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers", json=payload)

    @mcp.tool()
    def update_pull_request_branch(
        owner: str, repo: str, pull_number: int, expected_head_sha: str = ""
    ) -> dict | list:
        """Update a pull request branch with the latest upstream changes."""
        payload: dict = {}
        if expected_head_sha:
            payload["expected_head_sha"] = expected_head_sha
        return gh_put(f"/repos/{owner}/{repo}/pulls/{pull_number}/update-branch", json=payload)
