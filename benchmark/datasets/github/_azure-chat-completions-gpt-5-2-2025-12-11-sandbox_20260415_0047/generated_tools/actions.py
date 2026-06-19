from __future__ import annotations

from typing import Any, Dict, Optional

from . import mcp
from .http import GitHubClient, split_repo


@mcp.tool()
def actions_workflow_dispatch(repo: str, workflow_id: str, ref: str, inputs: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Trigger a workflow_dispatch event for a workflow file/id."""
    try:
        owner, r = split_repo(repo)
        client = GitHubClient.from_env()
        json_body: Dict[str, Any] = {"ref": ref}
        if inputs is not None:
            json_body["inputs"] = inputs
        status, payload = client.request(
            "POST",
            f"/repos/{owner}/{r}/actions/workflows/{workflow_id}/dispatches",
            json_body=json_body,
        )
        return client.ok_or_error(status, payload)  # type: ignore[return-value]
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def actions_list_workflow_runs(repo: str, workflow_id: str, per_page: int = 30, page: int = 1) -> Any:
    """List workflow runs for a workflow."""
    try:
        owner, r = split_repo(repo)
        client = GitHubClient.from_env()
        status, payload = client.request(
            "GET",
            f"/repos/{owner}/{r}/actions/workflows/{workflow_id}/runs",
            params={"per_page": per_page, "page": page},
        )
        return client.ok_or_error(status, payload)
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def actions_get_workflow_run(repo: str, run_id: int) -> Dict[str, Any]:
    """Get a workflow run."""
    try:
        owner, r = split_repo(repo)
        client = GitHubClient.from_env()
        status, payload = client.request("GET", f"/repos/{owner}/{r}/actions/runs/{run_id}")
        return client.ok_or_error(status, payload)  # type: ignore[return-value]
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def actions_cancel_workflow_run(repo: str, run_id: int) -> Dict[str, Any]:
    """Cancel a workflow run."""
    try:
        owner, r = split_repo(repo)
        client = GitHubClient.from_env()
        status, payload = client.request("POST", f"/repos/{owner}/{r}/actions/runs/{run_id}/cancel")
        return client.ok_or_error(status, payload)  # type: ignore[return-value]
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def actions_rerun_workflow_run(repo: str, run_id: int) -> Dict[str, Any]:
    """Re-run a workflow run."""
    try:
        owner, r = split_repo(repo)
        client = GitHubClient.from_env()
        status, payload = client.request("POST", f"/repos/{owner}/{r}/actions/runs/{run_id}/rerun")
        return client.ok_or_error(status, payload)  # type: ignore[return-value]
    except Exception as e:
        return {"error": str(e)}
