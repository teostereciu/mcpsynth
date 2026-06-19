import os
import requests
from fastmcp import tool

GITHUB_API_BASE_URL = os.environ.get("GITHUB_API_BASE_URL", "https://api.github.com")
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
HEADERS = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json",
}

def handle_response(resp):
    try:
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": resp.status_code, "body": resp.text}

@tool("search_code")
def search_code(query: str, sort: str = None, order: str = None):
    """Search code on GitHub."""
    url = f"{GITHUB_API_BASE_URL}/search/code"
    params = {"q": query}
    if sort:
        params["sort"] = sort
    if order:
        params["order"] = order
    resp = requests.get(url, headers=HEADERS, params=params)
    return handle_response(resp)
