from typing import Any, Optional

from .common import JiraClient, compact_dict


def get_all_projects(expand: Optional[str] = None, recent: Optional[int] = None, properties: Optional[str] = None) -> Any:
    client = JiraClient()
    return client.request("GET", "/rest/api/3/project", params=compact_dict({"expand": expand, "recent": recent, "properties": properties}))


def create_project(body: dict) -> Any:
    client = JiraClient()
    return client.request("POST", "/rest/api/3/project", json_body=body)


def get_recent_projects(expand: Optional[str] = None, properties: Optional[str] = None) -> Any:
    client = JiraClient()
    return client.request("GET", "/rest/api/3/project/recent", params=compact_dict({"expand": expand, "properties": properties}))


def search_projects(start_at: Optional[int] = None, max_results: Optional[int] = None, order_by: Optional[str] = None, query: Optional[str] = None, type_key: Optional[str] = None, category_id: Optional[int] = None, action: Optional[str] = None, expand: Optional[str] = None, status: Optional[str] = None, properties: Optional[str] = None) -> Any:
    client = JiraClient()
    return client.request(
        "GET",
        "/rest/api/3/project/search",
        params=compact_dict({"startAt": start_at, "maxResults": max_results, "orderBy": order_by, "query": query, "typeKey": type_key, "categoryId": category_id, "action": action, "expand": expand, "status": status, "properties": properties}),
    )


def get_project(project_id_or_key: str, expand: Optional[str] = None, properties: Optional[str] = None) -> Any:
    client = JiraClient()
    return client.request("GET", f"/rest/api/3/project/{project_id_or_key}", params=compact_dict({"expand": expand, "properties": properties}))


def update_project(project_id_or_key: str, body: dict) -> Any:
    client = JiraClient()
    return client.request("PUT", f"/rest/api/3/project/{project_id_or_key}", json_body=body)


def delete_project(project_id_or_key: str, enable_undo: Optional[bool] = None) -> Any:
    client = JiraClient()
    return client.request("DELETE", f"/rest/api/3/project/{project_id_or_key}", params=compact_dict({"enableUndo": enable_undo}))


def archive_project(project_id_or_key: str) -> Any:
    client = JiraClient()
    return client.request("POST", f"/rest/api/3/project/{project_id_or_key}/archive")


def restore_project(project_id_or_key: str) -> Any:
    client = JiraClient()
    return client.request("POST", f"/rest/api/3/project/{project_id_or_key}/restore")


def get_project_statuses(project_id_or_key: str) -> Any:
    client = JiraClient()
    return client.request("GET", f"/rest/api/3/project/{project_id_or_key}/statuses")


def get_project_notification_scheme(project_key_or_id: str, expand: Optional[str] = None) -> Any:
    client = JiraClient()
    return client.request("GET", f"/rest/api/3/project/{project_key_or_id}/notificationscheme", params=compact_dict({"expand": expand}))


def find_components(project_ids_or_keys: Optional[str] = None, start_at: Optional[int] = None, max_results: Optional[int] = None, order_by: Optional[str] = None, query: Optional[str] = None) -> Any:
    client = JiraClient()
    return client.request("GET", "/rest/api/3/component", params=compact_dict({"projectIdsOrKeys": project_ids_or_keys, "startAt": start_at, "maxResults": max_results, "orderBy": order_by, "query": query}))


def create_component(name: str, project: str, description: Optional[str] = None, assignee_type: Optional[str] = None, lead_account_id: Optional[str] = None) -> Any:
    client = JiraClient()
    return client.request("POST", "/rest/api/3/component", json_body=compact_dict({"name": name, "project": project, "description": description, "assigneeType": assignee_type, "leadAccountId": lead_account_id}))


def get_component(component_id: str) -> Any:
    client = JiraClient()
    return client.request("GET", f"/rest/api/3/component/{component_id}")


def update_component(component_id: str, name: Optional[str] = None, description: Optional[str] = None, assignee_type: Optional[str] = None, lead_account_id: Optional[str] = None, project: Optional[str] = None) -> Any:
    client = JiraClient()
    return client.request("PUT", f"/rest/api/3/component/{component_id}", json_body=compact_dict({"name": name, "description": description, "assigneeType": assignee_type, "leadAccountId": lead_account_id, "project": project}))


def delete_component(component_id: str, move_issues_to: Optional[str] = None) -> Any:
    client = JiraClient()
    return client.request("DELETE", f"/rest/api/3/component/{component_id}", params=compact_dict({"moveIssuesTo": move_issues_to}))


def get_project_components(project_id_or_key: str) -> Any:
    client = JiraClient()
    return client.request("GET", f"/rest/api/3/project/{project_id_or_key}/components")


def get_project_versions_paginated(project_id_or_key: str, start_at: Optional[int] = None, max_results: Optional[int] = None, order_by: Optional[str] = None, query: Optional[str] = None, status: Optional[str] = None, expand: Optional[str] = None) -> Any:
    client = JiraClient()
    return client.request("GET", f"/rest/api/3/project/{project_id_or_key}/version", params=compact_dict({"startAt": start_at, "maxResults": max_results, "orderBy": order_by, "query": query, "status": status, "expand": expand}))


def get_project_versions(project_id_or_key: str, expand: Optional[str] = None) -> Any:
    client = JiraClient()
    return client.request("GET", f"/rest/api/3/project/{project_id_or_key}/versions", params=compact_dict({"expand": expand}))


def create_version(body: dict) -> Any:
    client = JiraClient()
    return client.request("POST", "/rest/api/3/version", json_body=body)


def get_version(version_id: str, expand: Optional[str] = None) -> Any:
    client = JiraClient()
    return client.request("GET", f"/rest/api/3/version/{version_id}", params=compact_dict({"expand": expand}))


def update_version(version_id: str, body: dict) -> Any:
    client = JiraClient()
    return client.request("PUT", f"/rest/api/3/version/{version_id}", json_body=body)


def delete_version(version_id: str, move_fix_issues_to: Optional[str] = None, move_affected_issues_to: Optional[str] = None) -> Any:
    client = JiraClient()
    return client.request("DELETE", f"/rest/api/3/version/{version_id}", params=compact_dict({"moveFixIssuesTo": move_fix_issues_to, "moveAffectedIssuesTo": move_affected_issues_to}))


def merge_versions(version_id: str, move_issues_to: str) -> Any:
    client = JiraClient()
    return client.request("PUT", f"/rest/api/3/version/{version_id}/mergeto/{move_issues_to}")


def move_version(version_id: str, after: Optional[str] = None, position: Optional[str] = None) -> Any:
    client = JiraClient()
    return client.request("POST", f"/rest/api/3/version/{version_id}/move", json_body=compact_dict({"after": after, "position": position}))
