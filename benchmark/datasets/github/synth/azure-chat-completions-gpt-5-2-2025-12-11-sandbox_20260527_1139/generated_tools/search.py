from typing import Any, Dict, Optional

from ._client import request_json


def search_code(
    *,
    q: str,
    sort: Optional[str] = None,
    order: Optional[str] = None,
    per_page: int = 30,
    page: int = 1,
    accept: Optional[str] = None,
) -> Any:
    """GET /search/code

    Searches for query terms inside of a file.
    """
    params: Dict[str, Any] = {"q": q, "per_page": per_page, "page": page}
    if sort is not None:
        params["sort"] = sort
    if order is not None:
        params["order"] = order
    return request_json("GET", "/search/code", params=params, accept=accept)
