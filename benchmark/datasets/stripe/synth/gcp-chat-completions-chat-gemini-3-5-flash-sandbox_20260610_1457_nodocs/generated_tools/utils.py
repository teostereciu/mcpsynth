import os
import requests
from typing import Any, Dict, Optional

BASE_URL = "https://api.stripe.com"

def stripe_encode(params: Any, prefix: str = "") -> Dict[str, str]:
    """
    Recursively encode nested dicts/lists into Stripe's form-encoded format.
    Returns a flat dict of key-value pairs.
    """
    flat = {}
    if isinstance(params, dict):
        for k, v in params.items():
            key = f"{prefix}[{k}]" if prefix else k
            flat.update(stripe_encode(v, key))
    elif isinstance(params, list):
        for i, v in enumerate(params):
            key = f"{prefix}[{i}]"
            flat.update(stripe_encode(v, key))
    elif params is True:
        flat[prefix] = "true"
    elif params is False:
        flat[prefix] = "false"
    elif params is None:
        flat[prefix] = ""
    else:
        flat[prefix] = str(params)
    return flat

def stripe_request(method: str, path: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Make a request to the Stripe API.
    Handles authentication, form-encoding, and error handling.
    """
    api_key = os.environ.get("STRIPE_API_KEY")
    if not api_key:
        return {"error": "STRIPE_API_KEY environment variable is not set."}

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    url = f"{BASE_URL}{path}"
    
    try:
        if method.upper() in ["POST", "PUT", "PATCH"]:
            data = stripe_encode(params) if params else {}
            response = requests.request(method, url, headers=headers, data=data)
        else:
            # For GET/DELETE, Stripe also supports nested query parameters in the same format
            query_params = stripe_encode(params) if params else {}
            response = requests.request(method, url, headers=headers, params=query_params)

        try:
            res_json = response.json()
        except ValueError:
            return {"error": f"Invalid JSON response from Stripe: {response.text}"}

        if not response.ok:
            # Stripe errors usually have an 'error' object
            if isinstance(res_json, dict) and "error" in res_json:
                return {"error": res_json["error"]}
            return {"error": f"HTTP {response.status_code}: {response.text}"}

        return res_json

    except Exception as e:
        return {"error": f"Request failed: {str(e)}"}
