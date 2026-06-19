from typing import Any, Dict, List, Optional, Union
from github_client import client

def search_code(
    q: str,
    sort: Optional[str] = None,
    order: Optional[str] = "desc",
    per_page: Optional[int] = 30,
    page: Optional[int] = 1
) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
    """
    Search code.
    
    Parameters:
    - q: The query containing search terms and qualifiers.
    - sort: Sorts the results of your query. Can only be indexed.
    - order: The sort order. Can be asc or desc.
    - per_page: The number of results per page (max 100).
    - page: Page number of the results to fetch.
    """
    params = {
        "q": q,
        "order": order,
        "per_page": per_page,
        "page": page
    }
    if sort: params["sort"] = sort

    return client.request("GET", "/search/code", params=params)
