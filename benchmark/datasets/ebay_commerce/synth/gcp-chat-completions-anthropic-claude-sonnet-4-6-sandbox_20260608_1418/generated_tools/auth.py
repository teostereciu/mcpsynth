"""Authentication helpers for eBay Commerce API."""
import os
import time
import base64
import requests

_token_cache: dict = {}

def _get_env():
    env = os.environ.get("EBAY_ENVIRONMENT", "SANDBOX").upper()
    return env

def get_base_url() -> str:
    env = _get_env()
    if env == "PRODUCTION":
        return "https://api.ebay.com"
    return "https://api.sandbox.ebay.com"

def get_media_base_url() -> str:
    env = _get_env()
    if env == "PRODUCTION":
        return "https://apim.ebay.com"
    return "https://apim.sandbox.ebay.com"

def _get_credentials():
    app_id = os.environ.get("EBAY_APP_ID", "")
    cert_id = os.environ.get("EBAY_CERT_ID", "")
    return app_id, cert_id

def get_app_token() -> dict:
    """Obtain an application token via client_credentials grant. Cached until expiry."""
    cache_key = "app_token"
    now = time.time()
    if cache_key in _token_cache and _token_cache[cache_key]["expires_at"] > now + 60:
        return _token_cache[cache_key]

    app_id, cert_id = _get_credentials()
    if not app_id or not cert_id:
        return {"error": "EBAY_APP_ID and EBAY_CERT_ID environment variables are required"}

    credentials = base64.b64encode(f"{app_id}:{cert_id}".encode()).decode()
    token_url = "https://api.sandbox.ebay.com/identity/v1/oauth2/token"
    if _get_env() == "PRODUCTION":
        token_url = "https://api.ebay.com/identity/v1/oauth2/token"

    try:
        resp = requests.post(
            token_url,
            headers={
                "Authorization": f"Basic {credentials}",
                "Content-Type": "application/x-www-form-urlencoded",
            },
            data={
                "grant_type": "client_credentials",
                "scope": "https://api.ebay.com/oauth/api_scope",
            },
            timeout=30,
        )
        if resp.status_code == 200:
            data = resp.json()
            data["expires_at"] = now + int(data.get("expires_in", 7200))
            _token_cache[cache_key] = data
            return data
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}

def get_user_token() -> dict:
    """Obtain a user token via refresh_token grant. Cached until expiry."""
    cache_key = "user_token"
    now = time.time()
    if cache_key in _token_cache and _token_cache[cache_key]["expires_at"] > now + 60:
        return _token_cache[cache_key]

    app_id, cert_id = _get_credentials()
    refresh_token = os.environ.get("EBAY_REFRESH_TOKEN", "")
    if not app_id or not cert_id:
        return {"error": "EBAY_APP_ID and EBAY_CERT_ID environment variables are required"}
    if not refresh_token:
        return {"error": "EBAY_REFRESH_TOKEN environment variable is required"}

    credentials = base64.b64encode(f"{app_id}:{cert_id}".encode()).decode()
    token_url = "https://api.sandbox.ebay.com/identity/v1/oauth2/token"
    if _get_env() == "PRODUCTION":
        token_url = "https://api.ebay.com/identity/v1/oauth2/token"

    try:
        resp = requests.post(
            token_url,
            headers={
                "Authorization": f"Basic {credentials}",
                "Content-Type": "application/x-www-form-urlencoded",
            },
            data={
                "grant_type": "refresh_token",
                "refresh_token": refresh_token,
            },
            timeout=30,
        )
        if resp.status_code == 200:
            data = resp.json()
            data["expires_at"] = now + int(data.get("expires_in", 7200))
            _token_cache[cache_key] = data
            return data
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}
