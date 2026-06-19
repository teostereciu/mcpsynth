from typing import Any, Dict, Optional, Union

from .http_client import request_json


def list_repo_workflows(
    *,
    owner: str,
    repo: str,
    per_page: int = 30,
    page: int = 1,
    accept: str = "application/vnd.github+json",
) -> Any:
    """GET /repos/{owner}/{repo}/actions/workflows - List repository workflows."""
    _, data, _ = request_json(
        "GET",
        f"/repos/{owner}/{repo}/actions/workflows",
        params={"per_page": per_page, "page": page},
        accept=accept,
    )
    return data


def get_workflow(
    *,
    owner: str,
    repo: str,
    workflow_id: Union[int, str],
    accept: str = "application/vnd.github+json",
) -> Any:
    """GET /repos/{owner}/{repo}/actions/workflows/{workflow_id} - Get a workflow."""
    _, data, _ = request_json(
        "GET",
        f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}",
        accept=accept,
    )
    return data


def disable_workflow(
    *,
    owner: str,
    repo: str,
    workflow_id: Union[int, str],
    accept: str = "application/vnd.github+json",
) -> Any:
    """PUT /repos/{owner}/{repo}/actions/workflows/{workflow_id}/disable - Disable a workflow."""
    _, data, _ = request_json(
        "PUT",
        f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/disable",
        accept=accept,
    )
    return {"disabled": True} if data is None else data


def enable_workflow(
    *,
    owner: str,
    repo: str,
    workflow_id: Union[int, str],
    accept: str = "application/vnd.github+json",
) -> Any:
    """PUT /repos/{owner}/{repo}/actions/workflows/{workflow_id}/enable - Enable a workflow."""
    _, data, _ = request_json(
        "PUT",
        f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/enable",
        accept=accept,
    )
    return {"enabled": True} if data is None else data


def create_workflow_dispatch(
    *,
    owner: str,
    repo: str,
    workflow_id: Union[int, str],
    ref: str,
    inputs: Optional[Dict[str, str]] = None,
    accept: str = "application/vnd.github+json",
) -> Any:
    """POST /repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches - Create a workflow dispatch event."""
    _, data, _ = request_json(
        "POST",
        f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches",
        json_body={"ref": ref, "inputs": inputs},
        accept=accept,
    )
    return data


def get_workflow_usage(
    *,
    owner: str,
    repo: str,
    workflow_id: Union[int, str],
    accept: str = "application/vnd.github+json",
) -> Any:
    """GET /repos/{owner}/{repo}/actions/workflows/{workflow_id}/timing - Get workflow usage."""
    _, data, _ = request_json(
        "GET",
        f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/timing",
        accept=accept,
    )
    return data
