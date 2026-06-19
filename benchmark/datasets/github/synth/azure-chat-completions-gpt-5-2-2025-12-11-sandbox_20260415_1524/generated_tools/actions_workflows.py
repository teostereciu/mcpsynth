from __future__ import annotations

from typing import Any, Dict, Optional, Union

from .github_client import GitHubClient


def list_workflows(
    client: GitHubClient,
    *,
    owner: str,
    repo: str,
    per_page: int = 30,
    page: int = 1,
) -> Any:
    params = {"per_page": per_page, "page": page}
    return client.request("GET", f"/repos/{owner}/{repo}/actions/workflows", params=params)


def get_workflow(client: GitHubClient, *, owner: str, repo: str, workflow_id: Union[int, str]) -> Any:
    return client.request("GET", f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}")


def disable_workflow(client: GitHubClient, *, owner: str, repo: str, workflow_id: Union[int, str]) -> Any:
    return client.request("PUT", f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/disable")


def enable_workflow(client: GitHubClient, *, owner: str, repo: str, workflow_id: Union[int, str]) -> Any:
    return client.request("PUT", f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/enable")


def create_workflow_dispatch(
    client: GitHubClient,
    *,
    owner: str,
    repo: str,
    workflow_id: Union[int, str],
    ref: str,
    inputs: Optional[Dict[str, Any]] = None,
) -> Any:
    payload: Dict[str, Any] = {"ref": ref, "inputs": inputs}
    payload = {k: v for k, v in payload.items() if v is not None}
    return client.request("POST", f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches", json=payload)


def get_workflow_timing(client: GitHubClient, *, owner: str, repo: str, workflow_id: Union[int, str]) -> Any:
    return client.request("GET", f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/timing")
