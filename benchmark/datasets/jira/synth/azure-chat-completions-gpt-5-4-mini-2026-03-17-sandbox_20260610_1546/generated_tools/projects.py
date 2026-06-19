from typing import Any, Dict, Optional

from generated_tools.jira_client import JiraClient

client = JiraClient()


def get_projects(startAt: Optional[int] = None, maxResults: Optional[int] = None, orderBy: Optional[str] = None, id: Optional[list] = None, keys: Optional[list] = None, query: Optional[str] = None, typeKey: Optional[str] = None, categoryId: Optional[int] = None, action: Optional[str] = None, expand: Optional[str] = None, properties: Optional[list] = None) -> Any:
    return client.request("GET", "/project/search", query={"startAt": startAt, "maxResults": maxResults, "orderBy": orderBy, "id": id, "keys": keys, "query": query, "typeKey": typeKey, "categoryId": categoryId, "action": action, "expand": expand, "properties": properties})


def get_project(projectIdOrKey: str, expand: Optional[str] = None, properties: Optional[list] = None) -> Any:
    return client.request("GET", f"/project/{projectIdOrKey}", query={"expand": expand, "properties": properties})


def create_project(key: str, name: str, projectTypeKey: Optional[str] = None, projectTemplateKey: Optional[str] = None, leadAccountId: Optional[str] = None, description: Optional[str] = None, url: Optional[str] = None, assigneeType: Optional[str] = None, avatarId: Optional[int] = None, categoryId: Optional[int] = None, issueSecurityScheme: Optional[int] = None, notificationScheme: Optional[int] = None, permissionScheme: Optional[int] = None) -> Any:
    body: Dict[str, Any] = {"key": key, "name": name}
    for k, v in {"projectTypeKey": projectTypeKey, "projectTemplateKey": projectTemplateKey, "leadAccountId": leadAccountId, "description": description, "url": url, "assigneeType": assigneeType, "avatarId": avatarId, "categoryId": categoryId, "issueSecurityScheme": issueSecurityScheme, "notificationScheme": notificationScheme, "permissionScheme": permissionScheme}.items():
        if v is not None:
            body[k] = v
    return client.request("POST", "/project", body=body)
