from typing import Any, Optional

from generated_tools.common import mastodon_request


def search(query: str, type: Optional[str] = None, resolve: Optional[bool] = None, limit: Optional[int] = None, offset: Optional[int] = None) -> Any:
    return mastodon_request(
        "GET",
        "/api/v2/search",
        params={"q": query, "type": type, "resolve": resolve, "limit": limit, "offset": offset},
    )
