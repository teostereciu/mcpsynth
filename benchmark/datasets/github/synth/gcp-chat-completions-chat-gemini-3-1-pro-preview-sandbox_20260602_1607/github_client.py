import os
import requests

def get_github_client():
    token = os.environ.get("GITHUB_TOKEN")
    base_url = os.environ.get("GITHUB_API_BASE_URL", "https://api.github.com")
    
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
        
    return base_url, headers

def make_request(method, endpoint, **kwargs):
    base_url, headers = get_github_client()
    url = f"{base_url}{endpoint}"
    
    if "headers" in kwargs:
        headers.update(kwargs.pop("headers"))
        
    try:
        response = requests.request(method, url, headers=headers, **kwargs)
        response.raise_for_status()
        if response.content:
            return response.json()
        return {"status": "success"}
    except requests.exceptions.RequestException as e:
        if e.response is not None:
            try:
                return {"error": e.response.json()}
            except ValueError:
                return {"error": e.response.text}
        return {"error": str(e)}
