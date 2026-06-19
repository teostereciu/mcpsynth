from typing import Any, Dict, Optional

from .common import BASE_URL, ACCESS_TOKEN
import requests


def search_content(q: str, type: Optional[str] = None, resolve: Optional[bool] = None, following: Optional[bool] = None, account_id: Optional[str] = None, exclude_unreviewed: Optional[bool] = None, max_id: Optional[str] = None, min_id: Optional[str] = None, limit: Optional[int] = None, offset: Optional[int] = None) -> Any:
    if not BASE_URL:
        return {"error": "MASTODON_BASE_URL is not set"}
    url = f"{BASE_URL}/api/v2/search"
    headers = {"Accept": "application/json"}
    if ACCESS_TOKEN:
        headers["Authorization"] = f"Bearer {ACCESS_TOKEN}"
    params: Dict[str, Any] = {"q": q, "type": type, "resolve": resolve, "following": following, "account_id": account_id, "exclude_unreviewed": exclude_unreviewed, "max_id": max_id, "min_id": min_id, "limit": limit, "offset": offset}
    try:
        response = requests.get(url, headers=headers, params={k: v for k, v in params.items() if v is not None}, timeout=60)
        payload = response.json()
    except Exception as exc:
        return {"error": str(exc)}
    if not response.ok:
        return {"error": f"HTTP {response.status_code}", "details": payload}
    return payload
