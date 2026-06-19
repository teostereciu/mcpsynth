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

def get_authenticated_user() -> dict:
    """
    Retrieves information about the authenticated user.
    https://docs.github.com/en/rest/users/users#get-the-authenticated-user
    """
    url = f"{GITHUB_API_BASE_URL}/user"
    response = session.get(url)
    try:
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {"error": str(e), "status_code": e.response.status_code, "response": response.json()}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


def get_user(username: str) -> dict:
    """
    Retrieves information about a specific user.
    https://docs.github.com/en/rest/users/users#get-a-user
    """
    url = f"{GITHUB_API_BASE_URL}/users/{username}"
    response = session.get(url)
    try:
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {"error": str(e), "status_code": e.response.status_code, "response": response.json()}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
