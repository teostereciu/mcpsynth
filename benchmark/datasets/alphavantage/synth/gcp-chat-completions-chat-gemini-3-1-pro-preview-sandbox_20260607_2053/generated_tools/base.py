import os
import requests

BASE_URL = "https://www.alphavantage.co/query"

def get_api_key() -> str:
    key = os.environ.get("ALPHAVANTAGE_API_KEY")
    if not key:
        raise ValueError("ALPHAVANTAGE_API_KEY environment variable is not set")
    return key

def make_request(params: dict) -> dict:
    params["apikey"] = get_api_key()
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        if "Error Message" in data:
            return {"error": data["Error Message"]}
        if "Information" in data:
            return {"error": data["Information"]}
        return data
    except Exception as e:
        return {"error": str(e)}
