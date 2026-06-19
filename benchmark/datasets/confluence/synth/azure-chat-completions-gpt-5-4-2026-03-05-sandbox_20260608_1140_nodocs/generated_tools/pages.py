from typing import Any, Dict, Optional

from generated_tools.confluence_client import client


def list_pages(limit: int = 25, cursor: Optional[str] = None, space_id: Optional[str] = None, title: Optional[str] = None, status: Optional[str] = None) -> Dict[str, Any]:
    params = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    if space_id:
        params["space-id"] = space_id
    if title:
        params["title"] = title
    if status:
        params["status"] = status
    return client.request("GET", "/api/v2/pages", params=params)


def get_page(page_id: str, body_format: str = "storage") -> Dict[str, Any]:
    return client.request("GET", f"/api/v2/pages/{page_id}", params={"body-format": body_format})


def create_page(title: str, body_value: str, space_id: Optional[str] = None, parent_id: Optional[str] = None, status: str = "current") -> Dict[str, Any]:
    payload = {
        "title": title,
        "status": status,
        "body": {"representation": "storage", "value": body_value},
    }
    if space_id:
        payload["spaceId"] = space_id
    elif client.space_key:
        space = client.request("GET", "/rest/api/space", params={"spaceKey": client.space_key})
        results = space.get("results", []) if isinstance(space, dict) else []
        if results:
            payload["spaceId"] = results[0].get("id")
    if parent_id:
        payload["parentId"] = parent_id
    return client.request("POST", "/api/v2/pages", json_body=payload)


def update_page(page_id: str, title: str, body_value: str, version_number: int, status: str = "current") -> Dict[str, Any]:
    payload = {
        "id": page_id,
        "status": status,
        "title": title,
        "body": {"representation": "storage", "value": body_value},
        "version": {"number": version_number},
    }
    return client.request("PUT", f"/api/v2/pages/{page_id}", json_body=payload)


def delete_page(page_id: str, purge: bool = False) -> Dict[str, Any]:
    params = {"purge": str(purge).lower()}
    return client.request("DELETE", f"/api/v2/pages/{page_id}", params=params)


def get_page_children(page_id: str, limit: int = 25, cursor: Optional[str] = None) -> Dict[str, Any]:
    params = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    return client.request("GET", f"/api/v2/pages/{page_id}/children", params=params)


def get_page_ancestors(page_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/api/v2/pages/{page_id}/ancestors")


def move_page(page_id: str, target_parent_id: str) -> Dict[str, Any]:
    current = get_page(page_id)
    if current.get("error"):
        return current
    title = current.get("title", "")
    version = ((current.get("version") or {}).get("number") or 0) + 1
    body = (((current.get("body") or {}).get("storage") or {}).get("value"))
    if body is None:
        body = (((current.get("body") or {}).get("view") or {}).get("value"))
    payload = {
        "id": page_id,
        "status": current.get("status", "current"),
        "title": title,
        "parentId": target_parent_id,
        "body": {"representation": "storage", "value": body or ""},
        "version": {"number": version},
    }
    return client.request("PUT", f"/api/v2/pages/{page_id}", json_body=payload)


def list_page_versions(page_id: str, limit: int = 25) -> Dict[str, Any]:
    return client.request("GET", f"/api/v2/pages/{page_id}/versions", params={"limit": limit})


def get_page_version(page_id: str, version_number: int) -> Dict[str, Any]:
    return client.request("GET", f"/api/v2/pages/{page_id}/versions/{version_number}")


def restore_page_version(page_id: str, version_number: int, message: Optional[str] = None) -> Dict[str, Any]:
    payload = {"operationKey": "restore", "params": {"versionNumber": version_number}}
    if message:
        payload["params"]["message"] = message
    return client.request("POST", f"/rest/api/content/{page_id}/version", json_body=payload)
