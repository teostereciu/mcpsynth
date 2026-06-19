import os
import requests

def get_meal_plan_week(username, start_date, hash_value):
    """
    Retrieve a meal planned week for the given user.
    Corresponds to GET /mealplanner/{username}/week/{start-date}
    Accepts username (str), start_date (str, yyyy-mm-dd), hash_value (str).
    Returns JSON-serializable dict.
    """
    try:
        api_key = os.environ.get('SPOONACULAR_API_KEY')
        if not api_key:
            return {"error": "Missing SPOONACULAR_API_KEY environment variable"}
        base_url = f"https://api.spoonacular.com/mealplanner/{username}/week/{start_date}"
        params = {'apiKey': api_key, 'hash': hash_value}
        resp = requests.get(base_url, params=params)
        if resp.status_code != 200:
            return {"error": f"HTTP {resp.status_code}: {resp.text}"}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def get_meal_plan_day(username, date, hash_value):
    """
    Retrieve a meal planned day for the given user.
    Corresponds to GET /mealplanner/{username}/day/{date}
    Accepts username (str), date (str, yyyy-mm-dd), hash_value (str).
    Returns JSON-serializable dict.
    """
    try:
        api_key = os.environ.get('SPOONACULAR_API_KEY')
        if not api_key:
            return {"error": "Missing SPOONACULAR_API_KEY environment variable"}
        base_url = f"https://api.spoonacular.com/mealplanner/{username}/day/{date}"
        params = {'apiKey': api_key, 'hash': hash_value}
        resp = requests.get(base_url, params=params)
        if resp.status_code != 200:
            return {"error": f"HTTP {resp.status_code}: {resp.text}"}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def generate_meal_plan(params):
    """
    Generate a meal plan (daily or weekly).
    Corresponds to GET /mealplanner/generate
    Accepts params as a dict of query parameters (e.g. timeFrame, targetCalories, diet, exclude).
    Returns JSON-serializable dict.
    """
    try:
        api_key = os.environ.get('SPOONACULAR_API_KEY')
        if not api_key:
            return {"error": "Missing SPOONACULAR_API_KEY environment variable"}
        base_url = "https://api.spoonacular.com/mealplanner/generate"
        params = params.copy()
        params['apiKey'] = api_key
        resp = requests.get(base_url, params=params)
        if resp.status_code != 200:
            return {"error": f"HTTP {resp.status_code}: {resp.text}"}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}
