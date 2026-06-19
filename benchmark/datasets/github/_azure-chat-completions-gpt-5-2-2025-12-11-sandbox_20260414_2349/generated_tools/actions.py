"""GitHub Actions tools (workflow dispatch, runs lifecycle)."""

from __future__ import annotations

from typing import Any, Dict, Optional

from . import mcp
from .http import github_request, split_repo


@mcp.tool
def actions_workflow_dispatch(repo: str, workflow_id: str, ref: str, inputs: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Trigger a workflow_dispatch event for a workflow file or ID."""
    try:
        r = split_repo(repo)
    except ValueError as e:
        return {"error": str(e)}
    payload: Dict[str, Any] = {"ref": ref}
    if inputs is not None:
        payload["inputs"] = inputs
    return github_request(
        "POST",
        f"/repos/{r['owner']}/{r['repo']}/actions/workflows/{workflow_id}/dispatches",
        json=payload,
    )


@mcp.tool
def actions_list_workflow_runs(repo: str, workflow_id: str, per_page: int = 5, page: int = 1) -> Dict[str, Any]:
    """List workflow runs for a workflow."""
    try:
        r = split_repo(repo)
    except ValueError as e:
        return {"error": str(e)}
    return github_request(
        "GET",
        f"/repos/{r['owner']}/{r['repo']}/actions/workflows/{workflow_id}/runs",
        params={"per_page": per_page, "page": page},
    )


@mcp.tool
def actions_get_workflow_run(repo: str, run_id: int) -> Dict[str, Any]:
    """Get a workflow run."""
    try:
        r = split_repo(repo)
    except ValueError as e:
        return {"error": str(e)}
    return github_request("GET", f"/repos/{r['owner']}/{r['repo']}/actions/runs/{run_id}")


@mcp.tool
def actions_cancel_workflow_run(repo: str, run_id: int) -> Dict[str, Any]:
    """Cancel a workflow run."""
    try:
        r = split_repo(repo)
    except ValueError as e:
        return {"error": str(e)}
    return github_request("POST", f"/repos/{r['owner']}/{r['repo']}/actions/runs/{run_id}/cancel")


@mcp.tool
def actions_rerun_workflow_run(repo: str, run_id: int) -> Dict[str, Any]:
    """Re-run a workflow run."""
    try:
        r = split_repo(repo)
    except ValueError as e:
        return {"error": str(e)}
    return github_request("POST", f"/repos/{r['owner']}/{r['repo']}/actions/runs/{run_id}/rerun")
