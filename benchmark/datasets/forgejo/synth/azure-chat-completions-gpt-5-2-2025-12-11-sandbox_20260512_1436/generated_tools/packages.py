from typing import Any, Dict, Optional

from .http_client import request


def packages_list_owner(owner: str, *, page: Optional[int] = None, limit: Optional[int] = None, type: Optional[str] = None, q: Optional[str] = None) -> Any:
    params: Dict[str, Any] = {}
    if page is not None:
        params["page"] = page
    if limit is not None:
        params["limit"] = limit
    if type is not None:
        params["type"] = type
    if q is not None:
        params["q"] = q
    return request("GET", f"/packages/{owner}", params=params or None)


def package_get(owner: str, type: str, name: str, version: str) -> Any:
    return request("GET", f"/packages/{owner}/{type}/{name}/{version}")


def package_delete(owner: str, type: str, name: str, version: str) -> Any:
    return request("DELETE", f"/packages/{owner}/{type}/{name}/{version}")


def package_files_list(owner: str, type: str, name: str, version: str) -> Any:
    return request("GET", f"/packages/{owner}/{type}/{name}/{version}/files")
