from typing import Any, Dict, List, Optional, Union

from .http_client import JiraClient


def bulk_get_statuses(ids: List[str]) -> Union[Dict[str, Any], list, str]:
    """GET /statuses"""
    client = JiraClient()
    return client.request("GET", "/statuses", params={"id": ids})


def bulk_update_statuses(statuses: List[Dict[str, Any]]) -> Union[Dict[str, Any], list, str]:
    """PUT /statuses"""
    client = JiraClient()
    return client.request("PUT", "/statuses", json={"statuses": statuses})


def bulk_create_statuses(scope: Dict[str, Any], statuses: List[Dict[str, Any]]) -> Union[Dict[str, Any], list, str]:
    """POST /statuses"""
    client = JiraClient()
    return client.request("POST", "/statuses", json={"scope": scope, "statuses": statuses})


def bulk_delete_statuses(ids: List[str]) -> Union[Dict[str, Any], list, str]:
    """DELETE /statuses"""
    client = JiraClient()
    return client.request("DELETE", "/statuses", params={"id": ids})


def bulk_get_statuses_by_names(names: List[str], project_id: Optional[str] = None) -> Union[Dict[str, Any], list, str]:
    """GET /statuses/byNames"""
    client = JiraClient()
    params: Dict[str, Any] = {"name": names}
    if project_id is not None:
        params["projectId"] = project_id
    return client.request("GET", "/statuses/byNames", params=params)


def search_statuses(project_id: Optional[str] = None, start_at: Optional[int] = None, max_results: Optional[int] = None, search_string: Optional[str] = None, status_category: Optional[str] = None) -> Union[Dict[str, Any], list, str]:
    """GET /statuses/search"""
    client = JiraClient()
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


def get_status_project_issue_type_usages(status_id: str, project_id: str, next_page_token: Optional[str] = None, max_results: Optional[int] = None) -> Union[Dict[str, Any], list, str]:
    """GET /statuses/{statusId}/project/{projectId}/issueTypeUsages"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if next_page_token is not None:
        params["nextPageToken"] = next_page_token
    if max_results is not None:
        params["maxResults"] = max_results
    return client.request("GET", f"/statuses/{status_id}/project/{project_id}/issueTypeUsages", params=params or None)


def get_status_project_usages(status_id: str, next_page_token: Optional[str] = None, max_results: Optional[int] = None) -> Union[Dict[str, Any], list, str]:
    """GET /statuses/{statusId}/projectUsages"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if next_page_token is not None:
        params["nextPageToken"] = next_page_token
    if max_results is not None:
        params["maxResults"] = max_results
    return client.request("GET", f"/statuses/{status_id}/projectUsages", params=params or None)


def get_status_workflow_usages(status_id: str, next_page_token: Optional[str] = None, max_results: Optional[int] = None) -> Union[Dict[str, Any], list, str]:
    """GET /statuses/{statusId}/workflowUsages"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if next_page_token is not None:
        params["nextPageToken"] = next_page_token
    if max_results is not None:
        params["maxResults"] = max_results
    return client.request("GET", f"/statuses/{status_id}/workflowUsages", params=params or None)
