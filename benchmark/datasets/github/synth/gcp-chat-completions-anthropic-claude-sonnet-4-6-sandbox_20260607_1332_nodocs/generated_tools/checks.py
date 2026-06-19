"""MCP tools for GitHub Checks API (check runs, check suites)."""
from mcp.server.fastmcp import FastMCP
from .client import gh_get, gh_post, gh_patch

def register(mcp: FastMCP):

    # --- Check Runs ---

    @mcp.tool()
    def create_check_run(
        owner: str,
        repo: str,
        name: str,
        head_sha: str,
        details_url: str = "",
        external_id: str = "",
        status: str = "queued",
        started_at: str = "",
        conclusion: str = "",
        completed_at: str = "",
        output: dict | None = None,
        actions: list[dict] | None = None,
    ) -> dict | list:
        """Create a check run. status: queued|in_progress|completed. conclusion: success|failure|neutral|cancelled|skipped|timed_out|action_required."""
        payload: dict = {"name": name, "head_sha": head_sha, "status": status}
        if details_url:
            payload["details_url"] = details_url
        if external_id:
            payload["external_id"] = external_id
        if started_at:
            payload["started_at"] = started_at
        if conclusion:
            payload["conclusion"] = conclusion
        if completed_at:
            payload["completed_at"] = completed_at
        if output:
            payload["output"] = output
        if actions:
            payload["actions"] = actions
        return gh_post(f"/repos/{owner}/{repo}/check-runs", json=payload)

    @mcp.tool()
    def update_check_run(
        owner: str,
        repo: str,
        check_run_id: int,
        name: str = "",
        details_url: str = "",
        external_id: str = "",
        status: str = "",
        started_at: str = "",
        conclusion: str = "",
        completed_at: str = "",
        output: dict | None = None,
        actions: list[dict] | None = None,
    ) -> dict | list:
        """Update a check run."""
        payload: dict = {}
        if name:
            payload["name"] = name
        if details_url:
            payload["details_url"] = details_url
        if external_id:
            payload["external_id"] = external_id
        if status:
            payload["status"] = status
        if started_at:
            payload["started_at"] = started_at
        if conclusion:
            payload["conclusion"] = conclusion
        if completed_at:
            payload["completed_at"] = completed_at
        if output:
            payload["output"] = output
        if actions:
            payload["actions"] = actions
        return gh_patch(f"/repos/{owner}/{repo}/check-runs/{check_run_id}", json=payload)

    @mcp.tool()
    def get_check_run(owner: str, repo: str, check_run_id: int) -> dict | list:
        """Get a check run by ID."""
        return gh_get(f"/repos/{owner}/{repo}/check-runs/{check_run_id}")

    @mcp.tool()
    def list_check_runs_for_ref(
        owner: str,
        repo: str,
        ref: str,
        check_name: str = "",
        status: str = "",
        filter: str = "latest",
        per_page: int = 30,
        page: int = 1,
    ) -> dict | list:
        """List check runs for a Git ref (SHA, branch, or tag)."""
        params: dict = {"filter": filter, "per_page": per_page, "page": page}
        if check_name:
            params["check_name"] = check_name
        if status:
            params["status"] = status
        return gh_get(f"/repos/{owner}/{repo}/commits/{ref}/check-runs", params=params)

    @mcp.tool()
    def list_check_run_annotations(
        owner: str, repo: str, check_run_id: int, per_page: int = 30, page: int = 1
    ) -> dict | list:
        """List annotations for a check run."""
        return gh_get(f"/repos/{owner}/{repo}/check-runs/{check_run_id}/annotations",
                      params={"per_page": per_page, "page": page})

    # --- Check Suites ---

    @mcp.tool()
    def get_check_suite(owner: str, repo: str, check_suite_id: int) -> dict | list:
        """Get a check suite by ID."""
        return gh_get(f"/repos/{owner}/{repo}/check-suites/{check_suite_id}")

    @mcp.tool()
    def list_check_suites_for_ref(
        owner: str,
        repo: str,
        ref: str,
        app_id: int | None = None,
        check_name: str = "",
        per_page: int = 30,
        page: int = 1,
    ) -> dict | list:
        """List check suites for a Git ref."""
        params: dict = {"per_page": per_page, "page": page}
        if app_id is not None:
            params["app_id"] = app_id
        if check_name:
            params["check_name"] = check_name
        return gh_get(f"/repos/{owner}/{repo}/commits/{ref}/check-suites", params=params)

    @mcp.tool()
    def rerequest_check_suite(owner: str, repo: str, check_suite_id: int) -> dict | list:
        """Rerequest a check suite."""
        return gh_post(f"/repos/{owner}/{repo}/check-suites/{check_suite_id}/rerequest")

    @mcp.tool()
    def list_check_runs_in_check_suite(
        owner: str, repo: str, check_suite_id: int,
        check_name: str = "", status: str = "", filter: str = "latest",
        per_page: int = 30, page: int = 1
    ) -> dict | list:
        """List check runs in a check suite."""
        params: dict = {"filter": filter, "per_page": per_page, "page": page}
        if check_name:
            params["check_name"] = check_name
        if status:
            params["status"] = status
        return gh_get(f"/repos/{owner}/{repo}/check-suites/{check_suite_id}/check-runs", params=params)

    # --- Commit Statuses ---

    @mcp.tool()
    def get_combined_commit_status(owner: str, repo: str, ref: str) -> dict | list:
        """Get the combined commit status for a ref."""
        return gh_get(f"/repos/{owner}/{repo}/commits/{ref}/status")

    @mcp.tool()
    def list_commit_statuses(
        owner: str, repo: str, ref: str, per_page: int = 30, page: int = 1
    ) -> dict | list:
        """List commit statuses for a ref."""
        return gh_get(f"/repos/{owner}/{repo}/commits/{ref}/statuses",
                      params={"per_page": per_page, "page": page})

    @mcp.tool()
    def create_commit_status(
        owner: str,
        repo: str,
        sha: str,
        state: str,
        target_url: str = "",
        description: str = "",
        context: str = "default",
    ) -> dict | list:
        """Create a commit status. state: error|failure|pending|success."""
        payload: dict = {"state": state, "context": context}
        if target_url:
            payload["target_url"] = target_url
        if description:
            payload["description"] = description
        return gh_post(f"/repos/{owner}/{repo}/statuses/{sha}", json=payload)
