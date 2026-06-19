import os
import requests
import json

GITHUB_API_BASE_URL = os.getenv("GITHUB_API_BASE_URL", "https://api.github.com")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

session = requests.Session()
session.headers.update({
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
})

def list_gists(per_page: int = 30, page: int = 1) -> dict:
    """
    Lists gists for the authenticated user.
    https://docs.github.com/en/rest/gists/gists#list-gists-for-the-authenticated-user
    """
    url = f"{GITHUB_API_BASE_URL}/gists"
    params = {
        "per_page": per_page,
        "page": page
    }
    response = session.get(url, params=params)
    try:
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {"error": str(e), "status_code": e.response.status_code, "response": response.json()}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


def get_gist(gist_id: str) -> dict:
    """
    Retrieves a specific gist.
    https://docs.github.com/en/rest/gists/gists#get-a-gist
    """
    url = f"{GITHUB_API_BASE_URL}/gists/{gist_id}"
    response = session.get(url)
    try:
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {"error": str(e), "status_code": e.response.status_code, "response": response.json()}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


def create_gist(description: str, public: bool, files: dict) -> dict:
    """
    Creates a new gist.
    https://docs.github.com/en/rest/gists/gists#create-a-gist
    """
    url = f"{GITHUB_API_BASE_URL}/gists"
    payload = {
        "description": description,
        "public": public,
        "files": files
    }
    response = session.post(url, data=json.dumps(payload))
    try:
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {"error": str(e), "status_code": e.response.status_code, "response": response.json()}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
