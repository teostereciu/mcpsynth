from typing import Any, Dict

from .ebay_client import EbayClient, get_environment


IDENTITY_SCOPE_USER = "https://api.ebay.com/oauth/api_scope/commerce.identity.readonly"


def _identity_base_url() -> str:
    # Identity API uses apiz subdomain per docs
    env = get_environment()
    if env == "PRODUCTION":
        return "https://apiz.ebay.com"
    return "https://apiz.sandbox.ebay.com"


def get_user() -> Dict[str, Any]:
    """Get the authenticated user's account profile.

    GET https://apiz.ebay.com/commerce/identity/v1/user/
    OAuth: user token with commerce.identity.readonly
    """
    client = EbayClient()
    # Bypass client's base URL because identity uses apiz.*
    url_path = "/commerce/identity/v1/user/"
    # Use client's request but with full URL by temporarily calling requests directly is not supported;
    # instead, call client's underlying requests via a small hack: pass is_media=False and override base.
    # We'll just call requests here for clarity.
    import requests

    token = client.oauth.get_user_token(IDENTITY_SCOPE_USER)
    r = requests.get(
        _identity_base_url() + url_path,
        headers={"Authorization": f"Bearer {token}", "Accept": "application/json"},
        timeout=60,
    )
    ct = r.headers.get("Content-Type", "")
    data: Any
    if "application/json" in ct:
        try:
            data = r.json()
        except Exception:
            data = {"raw": r.text}
    else:
        data = {"raw": r.text}
    if r.status_code >= 400:
        return {"error": "ebay_api_error", "status": r.status_code, "url": str(r.url), "response": data}
    return data
