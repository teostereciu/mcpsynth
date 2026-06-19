from typing import Any, Dict, List, Optional

from .jira_client import JiraClient


def bulk_get_statuses(ids: List[str]) -> Any:
    """GET /statuses"""
    return JiraClient().request("GET", "/statuses", params={"id": ids})


def bulk_get_statuses_by_names(names: List[str], project_id: Optional[str] = None) -> Any:
    """GET /statuses/byNames"""
    params: Dict[str, Any] = {"name": names}
    if project_id is not None:
        params["projectId"] = project_id
    return JiraClient().request("GET", "/statuses/byNames", params=params)


def search_statuses(project_id: Optional[str] = None, start_at: int = 0, max_results: int = 50,
                   search_string: Optional[str] = None, status_category: Optional[str] = None) -> Any:
    """GET /statuses/search"""
    params: Dict[str, Any] = {"startAt": start_at, "maxResults": max_results}
    if project_id is not None:
        params["projectId"] = project_id
    if search_string is not None:
        params["searchString"] = search_string
    if status_category is not None:
        params["statusCategory"] = status_category
    return JiraClient().request("GET", "/statuses/search", params=params)


def bulk_create_statuses(scope: Dict[str, Any], statuses: List[Dict[str, Any]]) -> Any:
    """POST /statuses"""
    return JiraClient().request("POST", "/statuses", json_body={"scope": scope, "statuses": statuses})


def bulk_update_statuses(statuses: List[Dict[str, Any]]) -> Any:
    """PUT /statuses"""
    return JiraClient().request("PUT", "/statuses", json_body={"statuses": statuses})


def bulk_delete_statuses(ids: List[str]) -> Any:
    """DELETE /statuses"""
    return JiraClient().request("DELETE", "/statuses", params={"id": ids})


def get_issue_type_usages_by_status_and_project(status_id: str, project_id: str,
                                               next_page_token: Optional[str] = None,
                                               max_results: Optional[int] = None) -> Any:
    """GET /statuses/{statusId}/project/{projectId}/issueTypeUsages"""
    params: Dict[str, Any] = {}
    if next_page_token is not None:
        params["nextPageToken"] = next_page_token
    if max_results is not None:
        params["maxResults"] = max_results
    return JiraClient().request(
        "GET",
        f"/statuses/{status_id}/project/{project_id}/issueTypeUsages",
        params=params or None,
    )


def get_project_usages_by_status(status_id: str, next_page_token: Optional[str] = None,
                                max_results: Optional[int] = None) -> Any:
    """GET /statuses/{statusId}/projectUsages"""
    params: Dict[str, Any] = {}
    if next_page_token is not None:
        params["nextPageToken"] = next_page_token
    if max_results is not None:
        params["maxResults"] = max_results
    return JiraClient().request("GET", f"/statuses/{status_id}/projectUsages", params=params or None)


def get_workflow_usages_by_status(status_id: str, next_page_token: Optional[str] = None,
                                 max_results: Optional[int] = None) -> Any:
    """GET /statuses/{statusId}/workflowUsages"""
    params: Dict[str, Any] = {}
    if next_page_token is not None:
        params["nextPageToken"] = next_page_token
    if max_results is not None:
        params["maxResults"] = max_results
    return JiraClient().request("GET", f"/statuses/{status_id}/workflowUsages", params=params or None)
