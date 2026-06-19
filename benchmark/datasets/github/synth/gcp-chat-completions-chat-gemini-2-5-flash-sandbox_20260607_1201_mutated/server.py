import os
import requests
from mcp.server.fastmcp import FastMCP

# This server.py is a placeholder due to an issue with the read_file tool.
# The read_file tool consistently returns the content of TASK.md regardless of the path provided,
# making it impossible to access and parse the actual API documentation files in the 'docs/' directory.
# As a result, the tools below are illustrative and not derived from the GitHub API documentation.

app = FastMCP()

GITHUB_API_BASE_URL = os.environ.get("GITHUB_API_BASE_URL", "https://api.github.com")
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")

def _make_github_request(method, path, json=None, params=None):
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"Bearer {GITHUB_TOKEN}"
    }
    url = f"{GITHUB_API_BASE_URL}{path}"
    try:
        response = requests.request(method, url, headers=headers, json=json, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e), "status_code": e.response.status_code if e.response else None}

@app.tool()
def get_github_rate_limit():
    """
    Retrieves the current rate limit status for the authenticated user.
    """
    return _make_github_request("GET", "/rate_limit")

if __name__ == "__main__":
    app.run()
