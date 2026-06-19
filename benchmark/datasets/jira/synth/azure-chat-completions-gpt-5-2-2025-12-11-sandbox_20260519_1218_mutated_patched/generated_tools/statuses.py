from typing import Any, Dict, List, Optional

from ._client import JiraClient


def get_statuses(client: JiraClient, ids: List[str]) -> Any:
    return client.request("GET", "/statuses", params={"id": ids})


def get_statuses_by_names(client: JiraClient, names: List[str], *, project_id: Optional[str] = None) -> Any:
    params: Dict[str, Any] = {"name": names}
    if project_id is not None:
        params["projectId"] = project_id
    return client.request("GET", "/statuses/byNames", params=params)


def search_statuses(
    client: JiraClient,
    *,
    project_id: Optional[str] = None,
    start_at: Optional[int] = None,
    max_results: Optional[int] = None,
    search_string: Optional[str] = None,
    status_category: Optional[str] = None,
) -> Any:
    params: Dict[str, Any] = {}
    if project_id is not None:
        params["projectId"] = project_id
    if start_at is not None:
        params["startAt"] = start_at
    if max_results is not None:
        params["maxResults"] = max_results
    if search_string is not None:
        params["searchString"] = search_string
    if status_category is not None:
        params["statusCategory"] = status_category
    return client.request("GET", "/statuses/search", params=params or None)


def create_statuses(client: JiraClient, scope: Dict[str, Any], statuses: List[Dict[str, Any]]) -> Any:
    return client.request("POST", "/statuses", json={"scope": scope, "statuses": statuses})


def update_statuses(client: JiraClient, statuses: List[Dict[str, Any]]) -> Any:
    return client.request("PUT", "/statuses", json={"statuses": statuses})


def delete_statuses(client: JiraClient, ids: List[str]) -> Any:
    return client.request("DELETE", "/statuses", params={"id": ids})


def get_status_project_usages(client: JiraClient, status_id: str, *, next_page_token: Optional[str] = None, page_size: Optional[int] = None) -> Any:
    params: Dict[str, Any] = {}
    if next_page_token is not None:
        params["nextPageToken"] = next_page_token
    if page_size is not None:
        params["maxResults"] = page_size
    return client.request("GET", f"/statuses/{status_id}/projectUsages", params=params or None)


def get_status_workflow_usages(client: JiraClient, status_id: str, *, next_page_token: Optional[str] = None, page_size: Optional[int] = None) -> Any:
    params: Dict[str, Any] = {}
    if next_page_token is not None:
        params["nextPageToken"] = next_page_token
    if page_size is not None:
        params["maxResults"] = page_size
    return client.request("GET", f"/statuses/{status_id}/workflowUsages", params=params or None)


def get_status_issue_type_usages(client: JiraClient, status_id: str, project_id: str, *, next_page_token: Optional[str] = None, page_size: Optional[int] = None) -> Any:
    params: Dict[str, Any] = {}
    if next_page_token is not None:
        params["nextPageToken"] = next_page_token
    if page_size is not None:
        params["maxResults"] = page_size
    return client.request("GET", f"/statuses/{status_id}/project/{project_id}/issueTypeUsages", params=params or None)
