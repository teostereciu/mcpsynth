
import os
import requests
import json

ZULIP_EMAIL = os.environ.get("ZULIP_EMAIL")
ZULIP_API_KEY = os.environ.get("ZULIP_API_KEY")
ZULIP_SITE = os.environ.get("ZULIP_SITE")

BASE_URL = f"{ZULIP_SITE}/api/v1"

def make_request(method, endpoint, params=None, data=None):
    """Helper function to make authenticated requests to the Zulip API."""
    url = f"{BASE_URL}/{endpoint}"
    auth = (ZULIP_EMAIL, ZULIP_API_KEY)
    
    try:
        response = requests.request(method, url, params=params, data=data, auth=auth)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        try:
            return {"error": e.response.json()}
        except json.JSONDecodeError:
            return {"error": e.response.text}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

