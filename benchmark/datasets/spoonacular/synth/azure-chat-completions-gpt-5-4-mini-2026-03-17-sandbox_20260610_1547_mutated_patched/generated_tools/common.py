import os
import requests

BASE_URL = "https://api.spoonacular.com"


def api_get(path, params=None):
    params = dict(params or {})
    params["apiKey"] = os.getenv("SPOONACULAR_API_KEY", "")
    try:
        resp = requests.get(f"{BASE_URL}{path}", params=params, timeout=30)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def api_post(path, data=None):
    data = dict(data or {})
    data["apiKey"] = os.getenv("SPOONACULAR_API_KEY", "")
    try:
        resp = requests.post(f"{BASE_URL}{path}", data=data, timeout=30)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        return {"error": str(e)}
