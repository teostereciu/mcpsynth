from typing import Any, Dict, Optional

from .client import EbayApiClient


def get_item_snapshot_feed(
    category_id: str,
    snapshot_date: str,
    range_header: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /buy/feed/v1_beta/item_snapshot

    Note: Successful responses are TSV_GZIP binary. This tool returns metadata and (optionally)
    a base64-encoded chunk if Range is used and response is not JSON.
    """
    client = EbayApiClient()
    params: Dict[str, Any] = {"category_id": category_id, "snapshot_date": snapshot_date}
    headers: Dict[str, str] = {}
    if range_header:
        headers["Range"] = range_header

    # Use low-level requests to capture binary if needed
    url_path = "/buy/feed/v1_beta/item_snapshot"
    url = f"{client.base_url}{url_path}"
    token = client._get_token() if client.app_id and client.cert_id else None
    if not token:
        return {"error": "Missing credentials or failed to obtain token"}

    import base64
    import requests

    h = {"Authorization": f"Bearer {token}", "Accept": "application/json"}
    h.update({k: v for k, v in headers.items() if v is not None})

    try:
        resp = requests.get(url, params=params, headers=h, timeout=60)
    except Exception as e:
        return {"error": str(e)}

    ct = resp.headers.get("Content-Type", "")
    if resp.status_code >= 400:
        if "application/json" in ct:
            try:
                return {"error": resp.json(), "status": resp.status_code}
            except Exception:
                return {"error": resp.text, "status": resp.status_code}
        return {"error": resp.text, "status": resp.status_code}

    if "application/json" in ct:
        try:
            return resp.json()
        except Exception:
            return {"error": "Failed to parse JSON response", "status": resp.status_code, "text": resp.text}

    # Binary TSV_GZIP
    return {
        "status": resp.status_code,
        "content_type": ct,
        "content_range": resp.headers.get("Content-Range"),
        "content_length": resp.headers.get("Content-Length"),
        "data_base64": base64.b64encode(resp.content).decode("ascii"),
    }
