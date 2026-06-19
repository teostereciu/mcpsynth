from typing import Any, Dict

from .http import EbayAuth, request_json


AUTH = EbayAuth()


def get_user() -> Dict[str, Any]:
    """GET /commerce/identity/v1/user/ (apiz domain in docs; works via api base for token, but identity endpoint is on apiz).

    Note: docs show apiz.ebay.com; we call via standard api base host which may not work for identity.
    To be safe, we call apiz host based on environment.
    """
    token = AUTH.get_user_token("https://api.ebay.com/oauth/api_scope/commerce.identity.readonly")
    if token.startswith("{"):
        return {"error": "oauth_error", "details": token}

    # Identity API uses apiz subdomain.
    import os

    env = (os.getenv("EBAY_ENVIRONMENT", "SANDBOX") or "SANDBOX").upper()
    base = "https://apiz.sandbox.ebay.com" if env == "SANDBOX" else "https://apiz.ebay.com"

    # Use request_json but with full URL by temporarily calling requests directly.
    import requests

    url = base + "/commerce/identity/v1/user/"
    try:
        r = requests.get(url, headers={"Accept": "application/json", "Authorization": f"Bearer {token}"}, timeout=60)
    except Exception as e:
        return {"error": "request_failed", "message": str(e), "url": url}

    if r.status_code >= 400:
        try:
            body = r.json()
        except Exception:
            body = {"text": r.text}
        return {"error": "http_error", "status": r.status_code, "url": url, "response": body}

    return r.json()
