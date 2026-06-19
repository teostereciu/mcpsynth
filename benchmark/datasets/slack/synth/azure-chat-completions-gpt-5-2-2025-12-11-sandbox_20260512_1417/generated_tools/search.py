from typing import Any, Dict, Optional

from .slack_client import get_client


def search_messages(
    query: str,
    count: Optional[int] = None,
    highlight: Optional[bool] = None,
    page: Optional[int] = None,
    cursor: Optional[str] = None,
    sort: Optional[str] = None,
    sort_dir: Optional[str] = None,
    team_id: Optional[str] = None,
) -> Dict[str, Any]:
    payload: Dict[str, Any] = {"query": query}
    if count is not None:
        payload["count"] = count
    if highlight is not None:
        payload["highlight"] = highlight
    if page is not None:
        payload["page"] = page
    if cursor is not None:
        payload["cursor"] = cursor
    if sort is not None:
        payload["sort"] = sort
    if sort_dir is not None:
        payload["sort_dir"] = sort_dir
    if team_id is not None:
        payload["team_id"] = team_id
    return get_client().request("GET", "/search.messages", json=payload)


def search_files(
    query: str,
    count: Optional[int] = None,
    highlight: Optional[bool] = None,
    page: Optional[int] = None,
    sort: Optional[str] = None,
    sort_dir: Optional[str] = None,
    team_id: Optional[str] = None,
) -> Dict[str, Any]:
    payload: Dict[str, Any] = {"query": query}
    if count is not None:
        payload["count"] = count
    if highlight is not None:
        payload["highlight"] = highlight
    if page is not None:
        payload["page"] = page
    if sort is not None:
        payload["sort"] = sort
    if sort_dir is not None:
        payload["sort_dir"] = sort_dir
    if team_id is not None:
        payload["team_id"] = team_id
    return get_client().request("GET", "/search.files", json=payload)
