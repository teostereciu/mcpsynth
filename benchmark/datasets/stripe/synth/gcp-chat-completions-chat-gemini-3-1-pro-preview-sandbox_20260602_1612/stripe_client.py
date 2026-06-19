import os
import requests
from typing import Any, Dict, Optional

BASE_URL = "https://api.stripe.com/v1"

def get_headers() -> Dict[str, str]:
    api_key = os.environ.get("STRIPE_API_KEY")
    if not api_key:
        raise ValueError("STRIPE_API_KEY environment variable is not set")
    return {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/x-www-form-urlencoded"
    }

def make_request(method: str, path: str, data: Optional[Dict[str, Any]] = None, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    url = f"{BASE_URL}{path}"
    headers = get_headers()
    
    if data:
        data = {k: v for k, v in data.items() if v is not None}
    if params:
        params = {k: v for k, v in params.items() if v is not None}
        
    try:
        response = requests.request(method, url, headers=headers, data=data, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        if e.response is not None:
            try:
                return e.response.json()
            except ValueError:
                return {"error": str(e), "status_code": e.response.status_code}
        return {"error": str(e)}
