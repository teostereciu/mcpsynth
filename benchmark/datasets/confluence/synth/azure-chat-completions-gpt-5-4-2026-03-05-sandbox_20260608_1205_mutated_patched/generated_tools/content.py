from typing import Any, List, Optional

from generated_tools.core import client


def archive_pages(page_ids: List[int]) -> Any:
    return client.request("POST", "/rest/api/content/archive", json={"pages": [{"id": page_id} for page_id in page_ids]})


def publish_shared_draft(draft_id: str, version_number: int, title: str, type: str = "page", content_status: Optional[str] = None, space_key: Optional[str] = None, ancestor_ids: Optional[List[str]] = None, include: Optional[List[str]] = None) -> Any:
    return client.request(
        "PUT",
        f"/rest/api/content/blueprint/instance/{draft_id}",
        params={"status": content_status, "expand": include},
        json={
            "version": {"number": version_number},
            "title": title,
            "type": type,
            "status": content_status,
            "space": {"key": space_key} if space_key else None,
            "ancestors": [{"id": ancestor_id} for ancestor_id in (ancestor_ids or [])],
        },
    )


def publish_legacy_draft(draft_id: str, body: dict, status: Optional[str] = None) -> Any:
    return client.request("POST", f"/rest/api/content/blueprint/instance/{draft_id}", params={"status": status}, json=body)


def search_content_by_cql(cql: str, cqlcontext: Optional[str] = None, expand: Optional[List[str]] = None, start: Optional[int] = None, limit: Optional[int] = None, include_archived_spaces: Optional[bool] = None, excerpt: Optional[str] = None) -> Any:
    return client.request("GET", "/rest/api/content/search", params={"cql": cql, "cqlcontext": cqlcontext, "expand": expand, "start": start, "limit": limit, "includeArchivedSpaces": include_archived_spaces, "excerpt": excerpt})
