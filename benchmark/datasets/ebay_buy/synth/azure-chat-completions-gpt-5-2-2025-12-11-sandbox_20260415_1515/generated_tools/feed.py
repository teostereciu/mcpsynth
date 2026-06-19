from typing import Any, Dict, Optional

from .http_client import EbayClient


client = EbayClient()


def feed_get_item_snapshot(
    *,
    category_id: str,
    snapshot_date: str,
    marketplace_id: Optional[str] = None,
    range_header: Optional[str] = None,
) -> Dict[str, Any]:
    """Download hourly snapshot feed.

    Note: Successful response is TSV_GZIP binary. This tool returns metadata and (optionally) a base64 chunk
    if Range is used and response is not JSON.
    """
    params = {"category_id": category_id, "snapshot_date": snapshot_date}
    headers: Dict[str, str] = {}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    if range_header:
        headers["Range"] = range_header

    # Use raw requests to handle binary
    import base64
    import requests
    from .http_client import get_base_url

    url = get_base_url().rstrip("/") + "/buy/feed/v1/item_snapshot"
    try:
        resp = requests.get(url, params=params, headers={**headers, "Authorization": f"Bearer {client._get_token()}"}, timeout=120)
    except requests.RequestException as e:
        return {"error": str(e), "url": url}

    ct = resp.headers.get("Content-Type", "")
    if "application/json" in ct:
        try:
            body: Any = resp.json()
        except Exception:
            body = resp.text
        if resp.status_code >= 400:
            return {"error": "ebay_api_error", "status": resp.status_code, "url": str(resp.url), "response": body}
        return {"status": resp.status_code, "url": str(resp.url), "response": body, "headers": dict(resp.headers)}

    if resp.status_code >= 400:
        return {"error": "ebay_api_error", "status": resp.status_code, "url": str(resp.url), "response": resp.text, "headers": dict(resp.headers)}

    content_b64 = base64.b64encode(resp.content).decode("ascii") if range_header else None
    return {
        "status": resp.status_code,
        "url": str(resp.url),
        "content_type": ct,
        "content_length": len(resp.content),
        "headers": dict(resp.headers),
        "content_base64": content_b64,
        "note": "Binary TSV_GZIP. Use Range header to fetch in chunks; content_base64 returned only when Range is provided.",
    }
