from typing import Any, Dict, Optional

from ._client import get_client


def get_myself(expand: Optional[str] = None) -> Any:
    """GET /myself"""
    params: Dict[str, Any] = {}
    if expand is not None:
        params["expand"] = expand
    return get_client().request("GET", "/myself", params=params or None)
