import os
import requests
from typing import Any, Dict, Optional

BASE_URL = "https://api.spoonacular.com"

def get_api_key() -> str:
    api_key = os.environ.get("SPOONACULAR_API_KEY")
    if not api_key:
        raise ValueError("SPOONACULAR_API_KEY environment variable is not set")
    return api_key

def request(method: str, path: str, params: Optional[Dict[str, Any]] = None, data: Optional[Dict[str, Any]] = None, json_data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Make an HTTP request to the Spoonacular API.
    """
    try:
        api_key = get_api_key()
    except ValueError as e:
        return {"error": str(e)}

    url = f"{BASE_URL}{path}"
    
    if params is None:
        params = {}
    params["apiKey"] = api_key

    try:
        if method.upper() == "GET":
            response = requests.get(url, params=params, timeout=15)
        elif method.upper() == "POST":
            if data:
                response = requests.post(url, params=params, data=data, timeout=15)
            elif json_data:
                response = requests.post(url, params=params, json=json_data, timeout=15)
            else:
                response = requests.post(url, params=params, timeout=15)
        else:
            return {"error": f"Unsupported HTTP method: {method}"}

        response.raise_for_status()
        
        # Some endpoints might return non-JSON or empty responses, but most return JSON
        if response.status_code == 204:
            return {"success": True}
        
        try:
            return response.json()
        except ValueError:
            return {"text": response.text}

    except requests.exceptions.HTTPError as e:
        try:
            err_json = e.response.json()
            return {"error": f"HTTP {e.response.status_code}: {err_json.get('message', str(e))}"}
        except Exception:
            return {"error": f"HTTP {e.response.status_code}: {str(e)}"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}
