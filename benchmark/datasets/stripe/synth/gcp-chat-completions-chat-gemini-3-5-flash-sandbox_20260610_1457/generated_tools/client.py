import os
import requests
from typing import Any, Dict, Optional

STRIPE_API_KEY = os.environ.get("STRIPE_API_KEY", "")
BASE_URL = "https://api.stripe.com"

def flatten_params(params: Any, prefix: str = "") -> Dict[str, str]:
    flat = {}
    if isinstance(params, dict):
        for k, v in params.items():
            key = f"{prefix}[{k}]" if prefix else k
            flat.update(flatten_params(v, key))
    elif isinstance(params, (list, tuple)):
        for i, v in enumerate(params):
            key = f"{prefix}[{i}]"
            flat.update(flatten_params(v, key))
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
    url = f"{BASE_URL}{path}"
    headers = {
        "Authorization": f"Bearer {STRIPE_API_KEY}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    
    # Stripe API version header can be set if needed, but default is fine.
    
    data = None
    query_params = None
    
    if params:
        flat_data = flatten_params(params)
        if method.upper() in ["POST", "PUT", "DELETE"]:
            data = flat_data
        else:
            query_params = flat_data

    try:
        response = requests.request(
            method=method,
            url=url,
            headers=headers,
            data=data,
            params=query_params,
            timeout=30
        )
        
        try:
            res_json = response.json()
        except ValueError:
            return {"error": f"Invalid JSON response from Stripe: {response.text}", "status_code": response.status_code}
            
        if not response.ok:
            # Return error as a dict instead of raising exception
            return {
                "error": res_json.get("error", {}).get("message", "Unknown Stripe API error"),
                "type": res_json.get("error", {}).get("type"),
                "code": res_json.get("error", {}).get("code"),
                "status_code": response.status_code
            }
            
        return res_json
    except Exception as e:
        return {"error": f"Request failed: {str(e)}"}
