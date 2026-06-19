from typing import Any, Dict, Optional

from .github_client import GitHubClient


def list_workflows(
    client: GitHubClient,
    *,
    owner: str,
    repo: str,
    per_page: Optional[int] = None,
    page: Optional[int] = None,
) -> Dict[str, Any]:
    """GET /repos/{owner}/{repo}/actions/workflows"""
    return client.request(
        "GET",
        f"/repos/{owner}/{repo}/actions/workflows",
        params={"per_page": per_page, "page": page},
    )


def get_workflow(
    client: GitHubClient,
    *,
    owner: str,
    repo: str,
    workflow_id: str,
) -> Dict[str, Any]:
    """GET /repos/{owner}/{repo}/actions/workflows/{workflow_id}"""
    return client.request("GET", f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}")


def enable_workflow(client: GitHubClient, *, owner: str, repo: str, workflow_id: str) -> Dict[str, Any]:
    """PUT /repos/{owner}/{repo}/actions/workflows/{workflow_id}/enable"""
    return client.request("PUT", f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/enable")


def disable_workflow(client: GitHubClient, *, owner: str, repo: str, workflow_id: str) -> Dict[str, Any]:
    """PUT /repos/{owner}/{repo}/actions/workflows/{workflow_id}/disable"""
    return client.request("PUT", f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/disable")


def create_workflow_dispatch(
    client: GitHubClient,
    *,
    owner: str,
    repo: str,
    workflow_id: str,
    ref: str,
    inputs: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """POST /repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches"""
    payload: Dict[str, Any] = {"ref": ref}
    if inputs is not None:
        payload["inputs"] = inputs
    return client.request(
        "POST",
        f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches",
        json=payload,
    )


def get_workflow_timing(
    client: GitHubClient,
    *,
    owner: str,
    repo: str,
    workflow_id: str,
) -> Dict[str, Any]:
    """GET /repos/{owner}/{repo}/actions/workflows/{workflow_id}/timing"""
    return client.request("GET", f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/timing")
