from typing import Any, Dict, Optional

from .http import request_json


def list_projects(
    workspaceId: str,
    name: Optional[str] = None,
    strict_name_search: Optional[bool] = None,
    archived: Optional[bool] = None,
    billable: Optional[bool] = None,
    clients: Optional[str] = None,
    contains_client: Optional[bool] = None,
    client_status: Optional[str] = None,
    users: Optional[str] = None,
    contains_user: Optional[bool] = None,
    user_status: Optional[str] = None,
    is_template: Optional[bool] = None,
    sort_column: Optional[str] = None,
    sort_order: Optional[str] = None,
    hydrated: Optional[bool] = None,
    page: Optional[int] = None,
    page_size: Optional[int] = None,
    access: Optional[str] = None,
    expense_limit: Optional[int] = None,
    expense_date: Optional[str] = None,
    userGroups: Optional[str] = None,
    contains_group: Optional[bool] = None,
) -> Any:
    params: Dict[str, Any] = {}
    if name is not None:
        params["name"] = name
    if strict_name_search is not None:
        params["strict-name-search"] = str(strict_name_search).lower()
    if archived is not None:
        params["archived"] = str(archived).lower()
    if billable is not None:
        params["billable"] = str(billable).lower()
    if clients is not None:
        parts = [c.strip() for c in clients.split(",") if c.strip()]
        params["clients"] = parts if len(parts) > 1 else clients
    if contains_client is not None:
        params["contains-client"] = str(contains_client).lower()
    if client_status is not None:
        params["client-status"] = client_status
    if users is not None:
        parts = [u.strip() for u in users.split(",") if u.strip()]
        params["users"] = parts if len(parts) > 1 else users
    if contains_user is not None:
        params["contains-user"] = str(contains_user).lower()
    if user_status is not None:
        params["user-status"] = user_status
    if is_template is not None:
        params["is-template"] = str(is_template).lower()
    if sort_column is not None:
        params["sort-column"] = sort_column
    if sort_order is not None:
        params["sort-order"] = sort_order
    if hydrated is not None:
        params["hydrated"] = str(hydrated).lower()
    if page is not None:
        params["page"] = page
    if page_size is not None:
        params["page-size"] = page_size
    if access is not None:
        params["access"] = access
    if expense_limit is not None:
        params["expense-limit"] = expense_limit
    if expense_date is not None:
        params["expense-date"] = expense_date
    if userGroups is not None:
        parts = [g.strip() for g in userGroups.split(",") if g.strip()]
        params["userGroups"] = parts if len(parts) > 1 else userGroups
    if contains_group is not None:
        params["contains-group"] = str(contains_group).lower()

    return request_json("GET", f"/workspaces/{workspaceId}/projects", params=params or None)


def create_project(workspaceId: str, name: str, **fields: Any) -> Any:
    body: Dict[str, Any] = {"name": name}
    body.update(fields)
    return request_json("POST", f"/workspaces/{workspaceId}/projects", json=body)


def create_project_from_template(workspaceId: str, name: str, templateProjectId: str, **fields: Any) -> Any:
    body: Dict[str, Any] = {"name": name, "templateProjectId": templateProjectId}
    body.update(fields)
    return request_json("POST", f"/workspaces/{workspaceId}/projects/from-template", json=body)


def delete_project(workspaceId: str, projectId: str) -> Any:
    return request_json("DELETE", f"/workspaces/{workspaceId}/projects/{projectId}")


def get_project(workspaceId: str, projectId: str, hydrated: bool = False, custom_field_entity_type: str = "TIMEENTRY", expense_limit: Optional[int] = None, expense_date: Optional[str] = None) -> Any:
    params: Dict[str, Any] = {"hydrated": str(hydrated).lower(), "custom-field-entity-type": custom_field_entity_type}
    if expense_limit is not None:
        params["expense-limit"] = expense_limit
    if expense_date is not None:
        params["expense-date"] = expense_date
    return request_json("GET", f"/workspaces/{workspaceId}/projects/{projectId}", params=params)


def update_project(workspaceId: str, projectId: str, **fields: Any) -> Any:
    return request_json("PUT", f"/workspaces/{workspaceId}/projects/{projectId}", json=fields)


def update_project_estimate(workspaceId: str, projectId: str, **fields: Any) -> Any:
    return request_json("PUT", f"/workspaces/{workspaceId}/projects/{projectId}/estimate", json=fields)


def update_project_memberships(workspaceId: str, projectId: str, memberships: list, userGroups: Optional[dict] = None) -> Any:
    body: Dict[str, Any] = {"memberships": memberships}
    if userGroups is not None:
        body["userGroups"] = userGroups
    return request_json("PUT", f"/workspaces/{workspaceId}/projects/{projectId}/memberships", json=body)


def assign_or_remove_users_from_project(workspaceId: str, projectId: str, userIds: Optional[list] = None, userGroups: Optional[dict] = None, remove: bool = False) -> Any:
    body: Dict[str, Any] = {"remove": remove}
    if userIds is not None:
        body["userIds"] = userIds
    if userGroups is not None:
        body["userGroups"] = userGroups
    return request_json("PUT", f"/workspaces/{workspaceId}/projects/{projectId}/users", json=body)


def update_project_template(workspaceId: str, projectId: str, isTemplate: bool) -> Any:
    return request_json("PUT", f"/workspaces/{workspaceId}/projects/{projectId}/template", json={"isTemplate": isTemplate})


def update_project_user_cost_rate(workspaceId: str, projectId: str, userId: str, amount: int, since: Optional[str] = None) -> Any:
    body: Dict[str, Any] = {"amount": amount}
    if since is not None:
        body["since"] = since
    return request_json("PUT", f"/workspaces/{workspaceId}/projects/{projectId}/users/{userId}/cost-rate", json=body)


def update_project_user_billable_rate(workspaceId: str, projectId: str, userId: str, amount: int, since: Optional[str] = None) -> Any:
    body: Dict[str, Any] = {"amount": amount}
    if since is not None:
        body["since"] = since
    return request_json("PUT", f"/workspaces/{workspaceId}/projects/{projectId}/users/{userId}/billable-rate", json=body)
