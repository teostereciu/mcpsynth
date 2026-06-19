import requests
import os
import json

BASE_URL = os.environ.get("GITHUB_API_BASE_URL", "https://api.github.com")
TOKEN = os.environ.get("GITHUB_TOKEN")

def _github_api_request(method, endpoint, params=None, json_data=None):
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"Bearer {TOKEN}"
    }

    url = f"{BASE_URL}{endpoint}"

    try:
        response = requests.request(method, url, params=params, json=json_data, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        if response.status_code == 204:
            return {}
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
