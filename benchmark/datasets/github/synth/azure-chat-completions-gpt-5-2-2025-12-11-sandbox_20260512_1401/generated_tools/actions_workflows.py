from typing import Any, Dict, Optional, Union

from ._client import GitHubClient


def list_workflows(*, owner: str, repo: str, per_page: int = 30, page: int = 1) -> Dict[str, Any]:
    """GET /repos/{owner}/{repo}/actions/workflows - List repository workflows."""
    c = GitHubClient()
    return c.request(
        "GET",
        f"/repos/{owner}/{repo}/actions/workflows",
        params={"per_page": per_page, "page": page},
    )


def get_workflow(*, owner: str, repo: str, workflow_id: Union[int, str]) -> Dict[str, Any]:
    """GET /repos/{owner}/{repo}/actions/workflows/{workflow_id} - Get a workflow."""
    c = GitHubClient()
    return c.request("GET", f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}")


def disable_workflow(*, owner: str, repo: str, workflow_id: Union[int, str]) -> Dict[str, Any]:
    """PUT /repos/{owner}/{repo}/actions/workflows/{workflow_id}/disable - Disable a workflow."""
    c = GitHubClient()
    return c.request("PUT", f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/disable")


def enable_workflow(*, owner: str, repo: str, workflow_id: Union[int, str]) -> Dict[str, Any]:
    """PUT /repos/{owner}/{repo}/actions/workflows/{workflow_id}/enable - Enable a workflow."""
    c = GitHubClient()
    return c.request("PUT", f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/enable")


def dispatch_workflow(
    *,
    owner: str,
    repo: str,
    workflow_id: Union[int, str],
    ref: str,
    inputs: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """POST /repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches - Create a workflow dispatch event."""
    c = GitHubClient()
    payload: Dict[str, Any] = {"ref": ref}
    if inputs is not None:
        payload["inputs"] = inputs
    return c.request(
        "POST",
        f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches",
        json=payload,
    )


def get_workflow_usage(*, owner: str, repo: str, workflow_id: Union[int, str]) -> Dict[str, Any]:
    """GET /repos/{owner}/{repo}/actions/workflows/{workflow_id}/timing - Get workflow usage."""
    c = GitHubClient()
    return c.request("GET", f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/timing")
