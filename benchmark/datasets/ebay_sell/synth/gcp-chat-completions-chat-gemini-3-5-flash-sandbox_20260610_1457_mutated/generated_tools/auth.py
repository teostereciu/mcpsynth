import os
import time
import base64
import requests

_token_cache = {
    "access_token": None,
    "expires_at": 0
}

def get_base_url():
    env = os.environ.get("EBAY_ENVIRONMENT", "SANDBOX").upper()
    if env == "PRODUCTION":
        return "https://api.ebay.com"
    return "https://api.sandbox.ebay.com"

def get_access_token():
    global _token_cache
    now = time.time()
    # If token is still valid (with 60s buffer), return it
    if _token_cache["access_token"] and _token_cache["expires_at"] > now + 60:
        return _token_cache["access_token"]

    app_id = os.environ.get("EBAY_APP_ID")
    cert_id = os.environ.get("EBAY_CERT_ID")
    refresh_token = os.environ.get("EBAY_REFRESH_TOKEN")

    if not app_id or not cert_id or not refresh_token:
        raise ValueError("Missing required environment variables: EBAY_APP_ID, EBAY_CERT_ID, or EBAY_REFRESH_TOKEN")

    # Base64 encode client credentials
    credentials = f"{app_id}:{cert_id}"
    encoded_creds = base64.b64encode(credentials.encode("utf-8")).decode("utf-8")

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": f"Basic {encoded_creds}"
    }

    data = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token
    }

    token_url = f"{get_base_url()}/identity/v1/oauth2/token"
    response = requests.post(token_url, headers=headers, data=data)
    
    if response.status_code != 200:
        raise RuntimeError(f"Failed to refresh eBay access token: {response.status_code} - {response.text}")

    res_data = response.json()
    _token_cache["access_token"] = res_data["access_token"]
    # expires_in is usually 7200 seconds
    _token_cache["expires_at"] = now + int(res_data.get("expires_in", 7200))

    return _token_cache["access_token"]

def ebay_request(method, path, params=None, json_data=None, headers=None, content_type="application/json"):
    try:
        token = get_access_token()
    except Exception as e:
        return {"error": f"Authentication error: {str(e)}"}

    base_url = get_base_url()
    url = f"{base_url}{path}"

    req_headers = {
        "Authorization": f"Bearer {token}"
    }
    if content_type:
        req_headers["Content-Type"] = content_type
    if headers:
        req_headers.update(headers)

    try:
        response = requests.request(
            method=method,
            url=url,
            params=params,
            json=json_data,
            headers=req_headers
        )
        
        # Check if response is empty
        if not response.content:
            return {"status_code": response.status_code, "message": "Success (No Content)"}

        try:
            res_json = response.json()
            if response.status_code >= 400:
                return {"error": f"API error {response.status_code}", "details": res_json}
            return res_json
        except ValueError:
            if response.status_code >= 400:
                return {"error": f"API error {response.status_code}", "details": response.text}
            return {"status_code": response.status_code, "text": response.text}

    except Exception as e:
        return {"error": f"HTTP request failed: {str(e)}"}
