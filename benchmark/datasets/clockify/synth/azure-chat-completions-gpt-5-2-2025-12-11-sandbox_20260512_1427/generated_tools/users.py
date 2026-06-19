from typing import Any, Dict, Optional

from .http import request_json


def upload_user_photo(file_url: str) -> Any:
    """Upload a photo. Docs specify multipart/form-data to /file/image.

    MCP tools can't stream binary easily; accept a file_url and return an error explaining.
    """
    return {
        "error": "Photo upload requires multipart/form-data binary upload to /file/image; provide a custom implementation with file bytes. This tool is a placeholder.",
        "endpoint": "/file/image",
        "hint": "Implement with requests.post(..., files={'file': open(...)})",
        "file_url": file_url,
    }


def get_current_user(include_memberships: bool = False) -> Any:
    params = {"include-memberships": str(include_memberships).lower()}
    return request_json("GET", "/user", params=params)


def get_workspace_user_profile(workspaceId: str, userId: str) -> Any:
    return request_json("GET", f"/workspaces/{workspaceId}/users/{userId}")


def update_workspace_user_profile(
    workspaceId: str,
    userId: str,
    imageUrl: Optional[str] = None,
    name: Optional[str] = None,
    removeProfileImage: Optional[bool] = None,
    userCustomFields: Optional[list] = None,
    weekStart: Optional[str] = None,
    workCapacity: Optional[str] = None,
    workingDays: Optional[str] = None,
) -> Any:
    body: Dict[str, Any] = {}
    if imageUrl is not None:
        body["imageUrl"] = imageUrl
    if name is not None:
        body["name"] = name
    if removeProfileImage is not None:
        body["removeProfileImage"] = removeProfileImage
    if userCustomFields is not None:
        body["userCustomFields"] = userCustomFields
    if weekStart is not None:
        body["weekStart"] = weekStart
    if workCapacity is not None:
        body["workCapacity"] = workCapacity
    if workingDays is not None:
        body["workingDays"] = workingDays
    return request_json("PUT", f"/workspaces/{workspaceId}/users/{userId}", json=body)


def list_workspace_users(
    workspaceId: str,
    email: Optional[str] = None,
    project_id: Optional[str] = None,
    status: Optional[str] = None,
    account_statuses: Optional[str] = None,
    name: Optional[str] = None,
    sort_column: Optional[str] = None,
    sort_order: Optional[str] = None,
    page: Optional[int] = None,
    page_size: Optional[int] = None,
    memberships: Optional[str] = None,
    include_roles: bool = False,
) -> Any:
    params: Dict[str, Any] = {"include-roles": str(include_roles).lower()}
    if email is not None:
        params["email"] = email
    if project_id is not None:
        params["project-id"] = project_id
    if status is not None:
        params["status"] = status
    if account_statuses is not None:
        params["account-statuses"] = account_statuses
    if name is not None:
        params["name"] = name
    if sort_column is not None:
        params["sort-column"] = sort_column
    if sort_order is not None:
        params["sort-order"] = sort_order
    if page is not None:
        params["page"] = page
    if page_size is not None:
        params["page-size"] = page_size
    if memberships is not None:
        params["memberships"] = memberships
    return request_json("GET", f"/workspaces/{workspaceId}/users", params=params)


def filter_workspace_users(workspaceId: str, filter_body: Dict[str, Any]) -> Any:
    return request_json("POST", f"/workspaces/{workspaceId}/users/filter", json=filter_body)


def update_user_custom_field(workspaceId: str, userId: str, customFieldId: str, value: Any) -> Any:
    return request_json(
        "POST",
        f"/workspaces/{workspaceId}/users/{userId}/customFields/{customFieldId}",
        json={"value": value},
    )


def find_users_team_manager(
    workspaceId: str,
    userId: str,
    sort_column: Optional[str] = None,
    sort_order: Optional[str] = None,
    page: Optional[int] = None,
    page_size: Optional[int] = None,
) -> Any:
    params: Dict[str, Any] = {}
    if sort_column is not None:
        params["sort-column"] = sort_column
    if sort_order is not None:
        params["sort-order"] = sort_order
    if page is not None:
        params["page"] = page
    if page_size is not None:
        params["page-size"] = page_size
    return request_json("GET", f"/workspaces/{workspaceId}/users/{userId}/teamManager", params=params or None)


def remove_users_manager_role(workspaceId: str, userId: str, entityId: str, role: str, sourceType: Optional[str] = None) -> Any:
    body: Dict[str, Any] = {"entityId": entityId, "role": role}
    if sourceType is not None:
        body["sourceType"] = sourceType
    return request_json("DELETE", f"/workspaces/{workspaceId}/users/{userId}/managerRole", json=body)


def give_manager_role_to_user(workspaceId: str, userId: str, entityId: str, role: str, sourceType: Optional[str] = None) -> Any:
    body: Dict[str, Any] = {"entityId": entityId, "role": role}
    if sourceType is not None:
        body["sourceType"] = sourceType
    return request_json("POST", f"/workspaces/{workspaceId}/users/{userId}/managerRole", json=body)
