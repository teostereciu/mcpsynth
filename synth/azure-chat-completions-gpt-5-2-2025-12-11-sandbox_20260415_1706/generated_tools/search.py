from typing import Any, Dict, Optional

from .slack_client import SlackWebAPIClient, _clean_dict


def search_messages(
    query: str,
    count: Optional[int] = None,
    page: Optional[int] = None,
    cursor: Optional[str] = None,
    highlight: Optional[bool] = None,
    sort: Optional[str] = None,
    sort_dir: Optional[str] = None,
    team_id: Optional[str] = None,
    client: Optional[SlackWebAPIClient] = None,
) -> Dict[str, Any]:
    client = client or SlackWebAPIClient()
    params = _clean_dict(
        {
            "query": query,
            "count": count,
            "page": page,
            "cursor": cursor,
            "highlight": highlight,
            "sort": sort,
            "sort_dir": sort_dir,
            "team_id": team_id,
        }
    )
    return client.get("search.messages", params)


def search_files(
    query: str,
    count: Optional[int] = None,
    page: Optional[int] = None,
    highlight: Optional[bool] = None,
    sort: Optional[str] = None,
    sort_dir: Optional[str] = None,
    team_id: Optional[str] = None,
    client: Optional[SlackWebAPIClient] = None,
) -> Dict[str, Any]:
    client = client or SlackWebAPIClient()
    params = _clean_dict(
        {
            "query": query,
            "count": count,
            "page": page,
            "highlight": highlight,
            "sort": sort,
            "sort_dir": sort_dir,
            "team_id": team_id,
        }
    )
    return client.get("search.files", params)
