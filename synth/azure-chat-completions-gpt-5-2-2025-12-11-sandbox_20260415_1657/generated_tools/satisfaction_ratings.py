from typing import Any, Dict, Optional

from ._client import get_client


def list_satisfaction_ratings(
    page: Optional[int] = None,
    per_page: Optional[int] = None,
    sort: Optional[str] = None,
    score: Optional[str] = None,
    start_time: Optional[int] = None,
    end_time: Optional[int] = None,
) -> Dict[str, Any]:
    """GET /api/v2/satisfaction_ratings"""
    client = get_client()
    params: Dict[str, Any] = {}
    if page is not None:
        params["page"] = page
    if per_page is not None:
        params["per_page"] = per_page
    if sort is not None:
        params["sort"] = sort
    if score is not None:
        params["score"] = score
    if start_time is not None:
        params["start_time"] = start_time
    if end_time is not None:
        params["end_time"] = end_time
    return client.request("GET", f"{client.base_support}/satisfaction_ratings", params=params)  # type: ignore


def show_satisfaction_rating(satisfaction_rating_id: int) -> Dict[str, Any]:
    """GET /api/v2/satisfaction_ratings/{satisfaction_rating_id}"""
    client = get_client()
    return client.request(
        "GET", f"{client.base_support}/satisfaction_ratings/{satisfaction_rating_id}"
    )  # type: ignore


def create_satisfaction_rating(ticket_id: int, satisfaction_rating: Dict[str, Any]) -> Dict[str, Any]:
    """POST /api/v2/tickets/{ticket_id}/satisfaction_rating

    Body: {"satisfaction_rating": {...}}
    """
    client = get_client()
    return client.request(
        "POST",
        f"{client.base_support}/tickets/{ticket_id}/satisfaction_rating",
        json={"satisfaction_rating": satisfaction_rating},
    )  # type: ignore
