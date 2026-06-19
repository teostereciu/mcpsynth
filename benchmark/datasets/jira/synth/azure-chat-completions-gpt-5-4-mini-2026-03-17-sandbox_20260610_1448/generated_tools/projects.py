from typing import Any, Dict, Optional
from .jira_client import JiraClient

client = JiraClient()


def get_projects() -> Any:
    return client.request("GET", "/project/search")


def get_project(projectIdOrKey: str) -> Any:
    return client.request("GET", f"/project/{projectIdOrKey}")


def create_project(key: str, name: str, projectTypeKey: str, leadAccountId: str, description: Optional[str] = None) -> Any:
    body: Dict[str, Any] = {"key": key, "name": name, "projectTypeKey": projectTypeKey, "leadAccountId": leadAccountId}
    if description is not None:
        body["description"] = description
    return client.request("POST", "/project", body=body)


def update_project(projectIdOrKey: str, name: Optional[str] = None, description: Optional[str] = None) -> Any:
    body: Dict[str, Any] = {}
    if name is not None:
        body["name"] = name
    if description is not None:
        body["description"] = description
    return client.request("PUT", f"/project/{projectIdOrKey}", body=body)
