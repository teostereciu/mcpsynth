from typing import Any, Dict, Optional

from ._client import get_client


def get_issue_types() -> Any:
    """GET /issuetype"""
    return get_client().request("GET", "/issuetype")


def get_issue_type(issue_type_id: str) -> Any:
    """GET /issuetype/{id}"""
    return get_client().request("GET", f"/issuetype/{issue_type_id}")


def get_issue_types_for_project(project_id: int, level: Optional[int] = None) -> Any:
    """GET /issuetype/project"""
    params: Dict[str, Any] = {"projectId": project_id}
    if level is not None:
        params["level"] = level
    return get_client().request("GET", "/issuetype/project", params=params)


def get_issue_type_alternatives(issue_type_id: str) -> Any:
    """GET /issuetype/{id}/alternatives"""
    return get_client().request("GET", f"/issuetype/{issue_type_id}/alternatives")
