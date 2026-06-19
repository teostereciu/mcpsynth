from typing import Any, Dict, List, Optional

from .jira_client import JiraClient, clean_params


def statuses_get(ids: List[str]) -> Any:
    """GET /statuses - Bulk get statuses by IDs."""
    client = JiraClient()
    params = clean_params({"id": ids})
    return client.request("GET", "/statuses", params=params)


def statuses_update(statuses: List[Dict[str, Any]]) -> Dict[str, Any]:
    """PUT /statuses - Bulk update statuses."""
    client = JiraClient()
    return client.request("PUT", "/statuses", json_body={"statuses": statuses})  # type: ignore[return-value]


def statuses_create(scope: Dict[str, Any], statuses: List[Dict[str, Any]]) -> Any:
    """POST /statuses - Bulk create statuses."""
    client = JiraClient()
    return client.request("POST", "/statuses", json_body={"scope": scope, "statuses": statuses})


def statuses_delete(ids: List[str]) -> Dict[str, Any]:
    """DELETE /statuses - Bulk delete statuses."""
    client = JiraClient()
    params = clean_params({"id": ids})
    return client.request("DELETE", "/statuses", params=params)  # type: ignore[return-value]


def statuses_by_names(names: List[str], project_id: Optional[str] = None) -> Any:
    """GET /statuses/byNames - Bulk get statuses by names."""
    client = JiraClient()
    params = clean_params({"name": names, "projectId": project_id})
    return client.request("GET", "/statuses/byNames", params=params)


def statuses_search(project_id: Optional[str] = None, start_at: Optional[int] = None, max_results: Optional[int] = None, search_string: Optional[str] = None, status_category: Optional[str] = None) -> Dict[str, Any]:
    """GET /statuses/search - Search statuses paginated."""
    client = JiraClient()
    params = clean_params({"projectId": project_id, "startAt": start_at, "maxResults": max_results, "searchString": search_string, "statusCategory": status_category})
    return client.request("GET", "/statuses/search", params=params)  # type: ignore[return-value]
