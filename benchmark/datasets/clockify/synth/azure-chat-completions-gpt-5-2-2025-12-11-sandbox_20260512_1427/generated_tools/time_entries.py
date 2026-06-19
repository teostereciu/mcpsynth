from typing import Any, Dict, Optional

from .http import request_json


def create_time_entry(workspaceId: str, **fields: Any) -> Any:
    return request_json("POST", f"/workspaces/{workspaceId}/time-entries", json=fields)


def mark_time_entries_invoiced(workspaceId: str, invoiced: bool, timeEntryIds: list) -> Any:
    body = {"invoiced": invoiced, "timeEntryIds": timeEntryIds}
    return request_json("PUT", f"/workspaces/{workspaceId}/time-entries/invoiced", json=body)


def list_in_progress_time_entries(workspaceId: str, page: int = 1, page_size: int = 10) -> Any:
    params = {"page": page, "page-size": page_size}
    return request_json("GET", f"/workspaces/{workspaceId}/time-entries/in-progress", params=params)


def delete_time_entry(workspaceId: str, id: str) -> Any:
    return request_json("DELETE", f"/workspaces/{workspaceId}/time-entries/{id}")


def get_time_entry(workspaceId: str, id: str, hydrated: bool = False) -> Any:
    params = {"hydrated": str(hydrated).lower()}
    return request_json("GET", f"/workspaces/{workspaceId}/time-entries/{id}", params=params)


def update_time_entry(workspaceId: str, id: str, **fields: Any) -> Any:
    return request_json("PUT", f"/workspaces/{workspaceId}/time-entries/{id}", json=fields)


def delete_time_entries_for_user(workspaceId: str, userId: str, time_entry_ids: str) -> Any:
    parts = [x.strip() for x in time_entry_ids.split(",") if x.strip()]
    params = {"time-entry-ids": parts if len(parts) > 1 else time_entry_ids}
    return request_json("DELETE", f"/workspaces/{workspaceId}/user/{userId}/time-entries", params=params)


def list_time_entries_for_user(
    workspaceId: str,
    userId: str,
    description: Optional[str] = None,
    start: Optional[str] = None,
    end: Optional[str] = None,
    project: Optional[str] = None,
    task: Optional[str] = None,
    tags: Optional[str] = None,
    project_required: Optional[bool] = None,
    task_required: Optional[bool] = None,
    hydrated: Optional[bool] = None,
    page: Optional[int] = None,
    page_size: Optional[int] = None,
    in_progress: Optional[str] = None,
    get_week_before: Optional[str] = None,
) -> Any:
    params: Dict[str, Any] = {}
    if description is not None:
        params["description"] = description
    if start is not None:
        params["start"] = start
    if end is not None:
        params["end"] = end
    if project is not None:
        params["project"] = project
    if task is not None:
        params["task"] = task
    if tags is not None:
        parts = [t.strip() for t in tags.split(",") if t.strip()]
        params["tags"] = parts if len(parts) > 1 else tags
    if project_required is not None:
        params["project-required"] = str(project_required).lower()
    if task_required is not None:
        params["task-required"] = str(task_required).lower()
    if hydrated is not None:
        params["hydrated"] = str(hydrated).lower()
    if page is not None:
        params["page"] = page
    if page_size is not None:
        params["page-size"] = page_size
    if in_progress is not None:
        params["in-progress"] = in_progress
    if get_week_before is not None:
        params["get-week-before"] = get_week_before

    return request_json("GET", f"/workspaces/{workspaceId}/user/{userId}/time-entries", params=params or None)


def stop_running_timer(workspaceId: str, userId: str, end: str) -> Any:
    return request_json("PATCH", f"/workspaces/{workspaceId}/user/{userId}/time-entries", json={"end": end})


def create_time_entry_for_user(workspaceId: str, userId: str, from_entry: Optional[str] = None, **fields: Any) -> Any:
    params = {"from-entry": from_entry} if from_entry is not None else None
    return request_json("POST", f"/workspaces/{workspaceId}/user/{userId}/time-entries", params=params, json=fields)


def bulk_edit_time_entries(workspaceId: str, userId: str, entries: list, hydrated: bool = False) -> Any:
    params = {"hydrated": str(hydrated).lower()}
    return request_json("PUT", f"/workspaces/{workspaceId}/user/{userId}/time-entries", params=params, json=entries)


def duplicate_time_entry(workspaceId: str, userId: str, id: str) -> Any:
    return request_json("POST", f"/workspaces/{workspaceId}/user/{userId}/time-entries/{id}/duplicate")
