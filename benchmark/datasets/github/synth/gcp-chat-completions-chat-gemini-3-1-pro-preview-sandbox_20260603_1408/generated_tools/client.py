import os
import requests
from typing import Any, Dict, List, Optional, Union

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
GITHUB_API_BASE_URL = os.environ.get("GITHUB_API_BASE_URL", "https://api.github.com").rstrip("/")

def make_request(method: str, endpoint: str, **kwargs) -> Any:
    """Helper to make GitHub API requests."""
    url = f"{GITHUB_API_BASE_URL}{endpoint}"
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    if GITHUB_TOKEN:
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"
    
    if "headers" in kwargs:
        headers.update(kwargs.pop("headers"))
        
    response = requests.request(method, url, headers=headers, **kwargs)
    
    try:
        response.raise_for_status()
        if response.content:
            return response.json()
        return {"status": "success"}
    except requests.exceptions.HTTPError as e:
        try:
            error_data = response.json()
            return {"error": str(e), "details": error_data}
        except ValueError:
            return {"error": str(e), "details": response.text}
    except Exception as e:
        return {"error": str(e)}
