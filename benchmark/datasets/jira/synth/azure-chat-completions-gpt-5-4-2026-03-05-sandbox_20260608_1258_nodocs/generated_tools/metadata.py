from typing import Any, Dict, Optional

from generated_tools.jira_client import jira_client


def list_issue_types() -> Any:
    return jira_client.request("GET", "/issuetype")


def list_priorities() -> Any:
    return jira_client.request("GET", "/priority")


def list_statuses() -> Any:
    return jira_client.request("GET", "/status")


def list_users(query: Optional[str] = None, start_at: int = 0, max_results: int = 50) -> Any:
    return jira_client.request(
        "GET",
        "/users/search",
        params={"query": query, "startAt": start_at, "maxResults": max_results},
    )


def get_user(account_id: str, expand: Optional[str] = None) -> Any:
    return jira_client.request("GET", "/user", params={"accountId": account_id, "expand": expand})


def list_groups(query: Optional[str] = None, max_results: int = 50) -> Any:
    return jira_client.request("GET", "/groups/picker", params={"query": query, "maxResults": max_results})


def get_group_members(groupname: str, start_at: int = 0, max_results: int = 50) -> Any:
    return jira_client.request(
        "GET",
        "/group/member",
        params={"groupname": groupname, "startAt": start_at, "maxResults": max_results},
    )


def list_filters(start_at: int = 0, max_results: int = 50) -> Any:
    return jira_client.request("GET", "/filter/search", params={"startAt": start_at, "maxResults": max_results})


def get_filter(filter_id: str, expand: Optional[str] = None) -> Any:
    return jira_client.request("GET", f"/filter/{filter_id}", params={"expand": expand})


def create_filter(name: str, jql: str, description: Optional[str] = None) -> Any:
    payload: Dict[str, Any] = {"name": name, "jql": jql}
    if description is not None:
        payload["description"] = description
    return jira_client.request("POST", "/filter", json_body=payload)


def delete_filter(filter_id: str) -> Any:
    return jira_client.request("DELETE", f"/filter/{filter_id}")
