from typing import Any, Dict, Optional

from generated_tools.jira_client import JiraClient

client = JiraClient()


def get_components(projectIdsOrKeys: Optional[list] = None, startAt: Optional[int] = None, maxResults: Optional[int] = None, orderBy: Optional[str] = None, query: Optional[str] = None) -> Any:
    return client.request("GET", "/component", query={"projectIdsOrKeys": projectIdsOrKeys, "startAt": startAt, "maxResults": maxResults, "orderBy": orderBy, "query": query})


def create_component(name: str, project: str, description: Optional[str] = None, leadAccountId: Optional[str] = None, leadUserName: Optional[str] = None, assigneeType: Optional[str] = None) -> Any:
    body: Dict[str, Any] = {"name": name, "project": project}
    for k, v in {"description": description, "leadAccountId": leadAccountId, "leadUserName": leadUserName, "assigneeType": assigneeType}.items():
        if v is not None:
            body[k] = v
    return client.request("POST", "/component", body=body)
