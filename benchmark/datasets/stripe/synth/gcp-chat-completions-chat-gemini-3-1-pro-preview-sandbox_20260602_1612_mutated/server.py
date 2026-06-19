import os
import json
import requests
from typing import Any, Dict, List, Optional, Union
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("stripe")

STRIPE_API_KEY = os.environ.get("STRIPE_API_KEY")
BASE_URL = "https://api.stripe.com/v1"

def flatten_dict(d: Dict[str, Any], parent_key: str = '') -> Dict[str, Any]:
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}[{k}]" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key).items())
        elif isinstance(v, list):
            for i, item in enumerate(v):
                if isinstance(item, dict):
                    items.extend(flatten_dict(item, f"{new_key}[{i}]").items())
                else:
                    items.append((f"{new_key}[{i}]", item))
        else:
            items.append((new_key, v))
    return dict(items)

def make_request(method: str, path: str, data: Optional[Dict[str, Any]] = None, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    if not STRIPE_API_KEY:
        return {"error": "STRIPE_API_KEY environment variable is not set"}
    
    url = f"{BASE_URL}{path}"
    headers = {
        "Authorization": f"Bearer {STRIPE_API_KEY}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    
    if data:
        data = {k: v for k, v in data.items() if v is not None}
        data = flatten_dict(data)
    if params:
        params = {k: v for k, v in params.items() if v is not None}
        params = flatten_dict(params)
        
    try:
        response = requests.request(method, url, headers=headers, data=data, params=params)
        return response.json()
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    mcp.run()
