import os
import requests
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("jira")

JIRA_BASE_URL = os.environ.get("JIRA_BASE_URL", "").rstrip("/")
JIRA_EMAIL = os.environ.get("JIRA_EMAIL")
JIRA_API_TOKEN = os.environ.get("JIRA_API_TOKEN")

def get_auth():
    return (JIRA_EMAIL, JIRA_API_TOKEN)

def get_base_url():
    return f"{JIRA_BASE_URL}/rest/api/3"

def make_request(method, endpoint, **kwargs):
    url = f"{get_base_url()}{endpoint}"
    auth = get_auth()
    
    headers = kwargs.pop("headers", {})
    if "Accept" not in headers:
        headers["Accept"] = "application/json"
    
    try:
        response = requests.request(method, url, auth=auth, headers=headers, **kwargs)
        response.raise_for_status()
        if response.status_code == 204:
            return {"status": "success"}
        return response.json()
    except requests.exceptions.RequestException as e:
        if e.response is not None:
            try:
                return {"error": e.response.json()}
            except ValueError:
                return {"error": e.response.text}
        return {"error": str(e)}

if __name__ == "__main__":
    mcp.run()
