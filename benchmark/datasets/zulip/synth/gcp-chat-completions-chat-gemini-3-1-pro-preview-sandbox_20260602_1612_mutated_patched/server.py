import os
import requests
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Zulip")

def get_session():
    email = os.environ.get("ZULIP_EMAIL")
    api_key = os.environ.get("ZULIP_API_KEY")
    site = os.environ.get("ZULIP_SITE")
    
    if not all([email, api_key, site]):
        raise ValueError("ZULIP_EMAIL, ZULIP_API_KEY, and ZULIP_SITE environment variables are required.")
        
    session = requests.Session()
    session.auth = (email, api_key)
    return session, site.rstrip("/") + "/api/v1"

def make_request(method, endpoint, **kwargs):
    session, base_url = get_session()
    url = f"{base_url}{endpoint}"
    
    try:
        response = session.request(method, url, **kwargs)
        if response.status_code == 204:
            return {"result": "success"}
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
    except ValueError:
        return {"error": "Invalid JSON response", "content": response.text}

if __name__ == "__main__":
    mcp.run()
