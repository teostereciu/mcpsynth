import os
import requests
import json
from typing import Any, Dict, Optional

def get_client_config() -> Dict[str, str]:
    email = os.environ.get("ZULIP_EMAIL")
    api_key = os.environ.get("ZULIP_API_KEY")
    site = os.environ.get("ZULIP_SITE")
    
    if not email or not api_key or not site:
        raise ValueError("Missing required environment variables: ZULIP_EMAIL, ZULIP_API_KEY, or ZULIP_SITE")
    
    site = site.rstrip("/")
    base_url = f"{site}/api/v1"
    return {
        "email": email,
        "api_key": api_key,
        "base_url": base_url
    }

def request(
    method: str,
    endpoint: str,
    params: Optional[Dict[str, Any]] = None,
    data: Optional[Dict[str, Any]] = None,
    files: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    try:
        config = get_client_config()
    except ValueError as e:
        return {"error": str(e)}
    
    url = f"{config['base_url']}/{endpoint.lstrip('/')}"
    auth = (config["email"], config["api_key"])
    
    # Clean up None values from params and data
    if params:
        params = {k: (json.dumps(v) if isinstance(v, (list, dict)) else v) for k, v in params.items() if v is not None}
    if data:
        data = {k: (json.dumps(v) if isinstance(v, (list, dict)) else v) for k, v in data.items() if v is not None}
        
    try:
        response = requests.request(
            method=method,
            url=url,
            auth=auth,
            params=params,
            data=data,
            files=files,
            timeout=30
        )
        try:
            res_json = response.json()
            if not response.ok:
                return {"error": f"HTTP {response.status_code}: {res_json.get('msg', response.text)}", "code": response.status_code}
            return res_json
        except ValueError:
            if not response.ok:
                return {"error": f"HTTP {response.status_code}: {response.text}", "code": response.status_code}
            return {"result": "success", "text": response.text}
    except Exception as e:
        return {"error": f"Request failed: {str(e)}"}
