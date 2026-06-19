import os
import requests

def get_base_url():
    store_url = os.environ.get("SHOPIFY_STORE_URL")
    if not store_url:
        raise ValueError("SHOPIFY_STORE_URL environment variable is required")
    return f"https://{store_url}/admin/api/2026-01"

def get_headers():
    token = os.environ.get("SHOPIFY_ACCESS_TOKEN")
    if not token:
        raise ValueError("SHOPIFY_ACCESS_TOKEN environment variable is required")
    return {
        "X-Shopify-Access-Token": token,
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

def make_request(method, endpoint, params=None, json_data=None):
    url = f"{get_base_url()}{endpoint}"
    try:
        response = requests.request(
            method=method,
            url=url,
            headers=get_headers(),
            params=params,
            json=json_data
        )
        if response.status_code == 204:
            return {"status": "success"}
        try:
            return response.json()
        except ValueError:
            return {"error": "Invalid JSON response", "status_code": response.status_code, "text": response.text}
    except Exception as e:
        return {"error": str(e)}
