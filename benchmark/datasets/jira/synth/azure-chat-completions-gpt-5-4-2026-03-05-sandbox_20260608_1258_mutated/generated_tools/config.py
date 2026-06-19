from typing import Any, Optional

from .common import JiraClient, compact_dict


def create_filter(name: str, jql: Optional[str] = None, description: Optional[str] = None, favourite: Optional[bool] = None, share_permissions: Optional[list] = None, edit_permissions: Optional[list] = None, expand: Optional[str] = None, override_share_permissions: Optional[bool] = None) -> Any:
    client = JiraClient()
    return client.request(
        "POST",
        "/rest/api/3/filter",
        params=compact_dict({"expand": expand, "overrideSharePermissions": override_share_permissions}),
        json_body=compact_dict({"name": name, "jql": jql, "jql_query": jql, "description": description, "favourite": favourite, "sharePermissions": share_permissions, "editPermissions": edit_permissions}),
    )


def get_favorite_filters(expand: Optional[str] = None) -> Any:
    client = JiraClient()
    return client.request("GET", "/rest/api/3/filter/favourite", params=compact_dict({"expand": expand}))


def get_my_filters(expand: Optional[str] = None, include_favourites: Optional[bool] = None) -> Any:
    client = JiraClient()
    return client.request("GET", "/rest/api/3/filter/my", params=compact_dict({"expand": expand, "includeFavourites": include_favourites}))


def search_filters(filter_name: Optional[str] = None, account_id: Optional[str] = None, owner: Optional[str] = None, groupname: Optional[str] = None, group_id: Optional[str] = None, project_id: Optional[int] = None, ids: Optional[list[int]] = None, order_by: Optional[str] = None, start_at: Optional[int] = None, max_results: Optional[int] = None, expand: Optional[str] = None) -> Any:
    client = JiraClient()
    return client.request("GET", "/rest/api/3/filter/search", params=compact_dict({"filterName": filter_name, "accountId": account_id, "user_id": account_id, "owner": owner, "groupname": groupname, "groupId": group_id, "projectId": project_id, "id": ids, "orderBy": order_by, "startAt": start_at, "maxResults": max_results, "expand": expand}))


def get_filter(filter_id: str, expand: Optional[str] = None, override_share_permissions: Optional[bool] = None) -> Any:
    client = JiraClient()
    return client.request("GET", f"/rest/api/3/filter/{filter_id}", params=compact_dict({"expand": expand, "overrideSharePermissions": override_share_permissions}))


def update_filter(filter_id: str, body: dict, expand: Optional[str] = None, override_share_permissions: Optional[bool] = None) -> Any:
    client = JiraClient()
    return client.request("PUT", f"/rest/api/3/filter/{filter_id}", params=compact_dict({"expand": expand, "overrideSharePermissions": override_share_permissions}), json_body=body)


def delete_filter(filter_id: str) -> Any:
    client = JiraClient()
    return client.request("DELETE", f"/rest/api/3/filter/{filter_id}")


def get_issue_types() -> Any:
    client = JiraClient()
    return client.request("GET", "/rest/api/3/issuetype")


def create_issue_type(name: str, description: Optional[str] = None, hierarchy_level: Optional[int] = None, type: Optional[str] = None) -> Any:
    client = JiraClient()
    return client.request("POST", "/rest/api/3/issuetype", json_body=compact_dict({"name": name, "description": description, "hierarchyLevel": hierarchy_level, "type": type}))


def get_issue_types_for_project(project_id: int, level: Optional[int] = None) -> Any:
    client = JiraClient()
    return client.request("GET", "/rest/api/3/issuetype/project", params=compact_dict({"projectId": project_id, "level": level}))


def get_issue_type(issue_type_id: str) -> Any:
    client = JiraClient()
    return client.request("GET", f"/rest/api/3/issuetype/{issue_type_id}")


def update_issue_type(issue_type_id: str, name: Optional[str] = None, description: Optional[str] = None, avatar_id: Optional[int] = None) -> Any:
    client = JiraClient()
    return client.request("PUT", f"/rest/api/3/issuetype/{issue_type_id}", json_body=compact_dict({"name": name, "description": description, "avatarId": avatar_id}))


def delete_issue_type(issue_type_id: str, alternative_issue_type_id: Optional[str] = None) -> Any:
    client = JiraClient()
    return client.request("DELETE", f"/rest/api/3/issuetype/{issue_type_id}", params=compact_dict({"alternativeIssueTypeId": alternative_issue_type_id}))


def get_alternative_issue_types(issue_type_id: str) -> Any:
    client = JiraClient()
    return client.request("GET", f"/rest/api/3/issuetype/{issue_type_id}/alternatives")


def get_priorities() -> Any:
    client = JiraClient()
    return client.request("GET", "/rest/api/3/priority")


def create_priority(name: str, status_color: str, description: Optional[str] = None, icon_url: Optional[str] = None, avatar_id: Optional[int] = None) -> Any:
    client = JiraClient()
    return client.request("POST", "/rest/api/3/priority", json_body=compact_dict({"name": name, "statusColor": status_color, "description": description, "iconUrl": icon_url, "avatarId": avatar_id}))


def set_default_priority(priority_id: str) -> Any:
    client = JiraClient()
    return client.request("PUT", "/rest/api/3/priority/default", json_body={"id": priority_id})


def move_priorities(ids: list[str], after: Optional[str] = None, position: Optional[str] = None) -> Any:
    client = JiraClient()
    return client.request("PUT", "/rest/api/3/priority/move", json_body=compact_dict({"ids": ids, "after": after, "position": position}))


def search_priorities(start_at: Optional[int] = None, max_results: Optional[int] = None, ids: Optional[list[str]] = None, project_ids: Optional[list[str]] = None, priority_name: Optional[str] = None, only_default: Optional[bool] = None, expand: Optional[str] = None) -> Any:
    client = JiraClient()
    return client.request("GET", "/rest/api/3/priority/search", params=compact_dict({"startAt": start_at, "maxResults": max_results, "id": ids, "projectId": project_ids, "priorityName": priority_name, "onlyDefault": only_default, "expand": expand}))


def get_priority(priority_id: str) -> Any:
    client = JiraClient()
    return client.request("GET", f"/rest/api/3/priority/{priority_id}")


def update_priority(priority_id: str, name: Optional[str] = None, description: Optional[str] = None, status_color: Optional[str] = None, icon_url: Optional[str] = None, avatar_id: Optional[int] = None) -> Any:
    client = JiraClient()
    return client.request("PUT", f"/rest/api/3/priority/{priority_id}", json_body=compact_dict({"name": name, "description": description, "statusColor": status_color, "iconUrl": icon_url, "avatarId": avatar_id}))


def delete_priority(priority_id: str) -> Any:
    client = JiraClient()
    return client.request("DELETE", f"/rest/api/3/priority/{priority_id}")


def bulk_get_statuses(ids: list[str]) -> Any:
    client = JiraClient()
    return client.request("GET", "/rest/api/3/statuses", params={"id": ids})


def bulk_update_statuses(statuses: list[dict]) -> Any:
    client = JiraClient()
    return client.request("PUT", "/rest/api/3/statuses", json_body={"statuses": statuses})


def bulk_create_statuses(scope: dict, statuses: list[dict]) -> Any:
    client = JiraClient()
    return client.request("POST", "/rest/api/3/statuses", json_body={"scope": scope, "statuses": statuses})


def bulk_delete_statuses(ids: list[str]) -> Any:
    client = JiraClient()
    return client.request("DELETE", "/rest/api/3/statuses", params={"id": ids})


def bulk_get_statuses_by_name(names: list[str], project_id: Optional[str] = None) -> Any:
    client = JiraClient()
    return client.request("GET", "/rest/api/3/statuses/byNames", params=compact_dict({"name": names, "projectId": project_id}))


def search_statuses(project_id: Optional[str] = None, start_at: Optional[int] = None, max_results: Optional[int] = None, search_string: Optional[str] = None, status_category: Optional[str] = None) -> Any:
    client = JiraClient()
    return client.request("GET", "/rest/api/3/statuses/search", params=compact_dict({"projectId": project_id, "startAt": start_at, "maxResults": max_results, "searchString": search_string, "statusCategory": status_category}))
