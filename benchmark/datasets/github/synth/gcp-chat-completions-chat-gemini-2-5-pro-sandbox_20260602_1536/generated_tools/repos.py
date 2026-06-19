
import os
import requests
from typing import Optional, Dict, Any

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
GITHUB_API_BASE_URL = os.environ.get("GITHUB_API_BASE_URL", "https://api.github.com")

def build_headers():
    headers = {
        "Accept": "application/vnd.github.v3+json",
    }
    if GITHUB_TOKEN:
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"
    return headers

def get_repository_content(owner: str, repo: str, path: str, ref: Optional[str] = None) -> Dict[str, Any]:
    """
    Gets the contents of a file or directory in a repository.
    """
    url = f"{GITHUB_API_BASE_URL}/repos/{owner}/{repo}/contents/{path}"
    params = {}
    if ref:
        params["ref"] = ref
    response = requests.get(url, headers=build_headers(), params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.json()}
