from typing import Any, Dict, Optional

from generated_tools.jira_client import JiraClient

client = JiraClient()


def get_versions(projectIdOrKey: str, expand: Optional[str] = None) -> Any:
    return client.request("GET", f"/project/{projectIdOrKey}/versions", query={"expand": expand})


def create_version(name: str, projectId: Optional[int] = None, project: Optional[str] = None, description: Optional[str] = None, archived: Optional[bool] = None, released: Optional[bool] = None, releaseDate: Optional[str] = None, moveUnfixedIssuesTo: Optional[str] = None) -> Any:
    body: Dict[str, Any] = {"name": name}
    for k, v in {"projectId": projectId, "project": project, "description": description, "archived": archived, "released": released, "releaseDate": releaseDate, "moveUnfixedIssuesTo": moveUnfixedIssuesTo}.items():
        if v is not None:
            body[k] = v
    return client.request("POST", "/version", body=body)
