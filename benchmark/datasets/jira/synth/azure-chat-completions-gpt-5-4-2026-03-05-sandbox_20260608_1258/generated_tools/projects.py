from typing import Any, Dict, Optional

from generated_tools.issues import _request


def list_projects(expand: Optional[str] = None, recent: Optional[int] = None, properties: Optional[list] = None) -> Any:
    params = {}
    if expand is not None:
        params["expand"] = expand
    if recent is not None:
        params["recent"] = recent
    if properties is not None:
        params["properties"] = properties
    return _request("GET", "/project", params=params or None)


def search_projects(start_at: Optional[int] = None, max_results: Optional[int] = None, order_by: Optional[str] = None, ids: Optional[list[int]] = None, keys: Optional[list[str]] = None, query: Optional[str] = None, type_key: Optional[str] = None, category_id: Optional[int] = None, action: Optional[str] = None, expand: Optional[str] = None) -> Any:
    params = {}
    if start_at is not None:
        params["startAt"] = start_at
    if max_results is not None:
        params["maxResults"] = max_results
    if order_by is not None:
        params["orderBy"] = order_by
    if ids is not None:
        params["id"] = ids
    if keys is not None:
        params["keys"] = keys
    if query is not None:
        params["query"] = query
    if type_key is not None:
        params["typeKey"] = type_key
    if category_id is not None:
        params["categoryId"] = category_id
    if action is not None:
        params["action"] = action
    if expand is not None:
        params["expand"] = expand
    return _request("GET", "/project/search", params=params or None)


def get_project(project_id_or_key: str, expand: Optional[str] = None, properties: Optional[list] = None) -> Any:
    params = {}
    if expand is not None:
        params["expand"] = expand
    if properties is not None:
        params["properties"] = properties
    return _request("GET", f"/project/{project_id_or_key}", params=params or None)


def create_project(key: str, name: str, project_type_key: str, project_template_key: str, lead_account_id: str, description: Optional[str] = None, url: Optional[str] = None, assignee_type: Optional[str] = None, category_id: Optional[int] = None, avatar_id: Optional[int] = None, issue_security_scheme: Optional[int] = None, notification_scheme: Optional[int] = None, permission_scheme: Optional[int] = None) -> Any:
    payload: Dict[str, Any] = {
        "key": key,
        "name": name,
        "projectTypeKey": project_type_key,
        "projectTemplateKey": project_template_key,
        "leadAccountId": lead_account_id,
    }
    if description is not None:
        payload["description"] = description
    if url is not None:
        payload["url"] = url
    if assignee_type is not None:
        payload["assigneeType"] = assignee_type
    if category_id is not None:
        payload["categoryId"] = category_id
    if avatar_id is not None:
        payload["avatarId"] = avatar_id
    if issue_security_scheme is not None:
        payload["issueSecurityScheme"] = issue_security_scheme
    if notification_scheme is not None:
        payload["notificationScheme"] = notification_scheme
    if permission_scheme is not None:
        payload["permissionScheme"] = permission_scheme
    return _request("POST", "/project", json_body=payload)


def list_components(project_ids_or_keys: Optional[list[str]] = None, start_at: Optional[int] = None, max_results: Optional[int] = None, order_by: Optional[str] = None, query: Optional[str] = None) -> Any:
    params = {}
    if project_ids_or_keys is not None:
        params["projectIdsOrKeys"] = project_ids_or_keys
    if start_at is not None:
        params["startAt"] = start_at
    if max_results is not None:
        params["maxResults"] = max_results
    if order_by is not None:
        params["orderBy"] = order_by
    if query is not None:
        params["query"] = query
    return _request("GET", "/component", params=params or None)


def create_component(name: str, project: str, description: Optional[str] = None, lead_account_id: Optional[str] = None, assignee_type: Optional[str] = None) -> Any:
    payload: Dict[str, Any] = {"name": name, "project": project}
    if description is not None:
        payload["description"] = description
    if lead_account_id is not None:
        payload["leadAccountId"] = lead_account_id
    if assignee_type is not None:
        payload["assigneeType"] = assignee_type
    return _request("POST", "/component", json_body=payload)


def get_component(component_id: str) -> Any:
    return _request("GET", f"/component/{component_id}")
