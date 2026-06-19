import os
import requests

BASE_URL = os.environ.get("ZULIP_SITE", "") + "/api/v1"
AUTH = (os.environ.get("ZULIP_EMAIL"), os.environ.get("ZULIP_API_KEY"))


def get_user(user_id: int, client_gravatar=True, include_custom_profile_fields=False):
    """Fetch details for a single user by user ID."""
    url = f"{BASE_URL}/users/{user_id}"
    params = {
        "client_gravatar": str(client_gravatar).lower(),
        "include_custom_profile_fields": str(include_custom_profile_fields).lower(),
    }
    try:
        response = requests.get(url, auth=AUTH, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        try:
            return response.json()
        except Exception:
            return {"error": str(e)}
    except Exception as e:
        return {"error": str(e)}


def list_tools():
    return ["get_user"]
