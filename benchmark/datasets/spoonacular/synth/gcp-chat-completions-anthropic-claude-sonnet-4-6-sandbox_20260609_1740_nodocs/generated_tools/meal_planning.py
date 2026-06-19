"""
Spoonacular Meal Planning tools — generate daily/weekly plans, manage meal plan items.
"""
import os
import requests

BASE_URL = "https://api.spoonacular.com"


def _api_key() -> str:
    key = os.environ.get("SPOONACULAR_API_KEY", "")
    if not key:
        raise ValueError("SPOONACULAR_API_KEY environment variable is not set")
    return key


def _get(path: str, params: dict) -> dict | list:
    params = {k: v for k, v in params.items() if v is not None}
    params["apiKey"] = _api_key()
    try:
        resp = requests.get(f"{BASE_URL}{path}", params=params, timeout=15)
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": f"HTTP {resp.status_code}: {resp.text[:300]}"}
    except Exception as e:
        return {"error": str(e)}


def generate_meal_plan_daily(
    target_calories: float = None,
    diet: str = None,
    exclude: str = None,
) -> dict:
    """
    Generate a single-day meal plan with breakfast, lunch, and dinner.
    Optionally specify target calories, a diet (e.g. 'vegetarian', 'vegan',
    'ketogenic'), and ingredients to exclude (comma-separated).
    """
    params = {
        "timeFrame": "day",
        "targetCalories": target_calories,
        "diet": diet,
        "exclude": exclude,
    }
    return _get("/mealplanner/generate", params)


def generate_meal_plan_weekly(
    target_calories: float = None,
    diet: str = None,
    exclude: str = None,
) -> dict:
    """
    Generate a full week meal plan (7 days) with breakfast, lunch, and dinner
    for each day. Optionally specify target calories, a diet, and ingredients
    to exclude (comma-separated).
    """
    params = {
        "timeFrame": "week",
        "targetCalories": target_calories,
        "diet": diet,
        "exclude": exclude,
    }
    return _get("/mealplanner/generate", params)


def get_meal_plan_week(
    username: str,
    start_date: str,
    hash: str,
) -> dict:
    """
    Retrieve a user's meal plan for a specific week. Requires the username,
    the start date of the week (YYYY-MM-DD format), and the user's hash token.
    """
    params = {"hash": hash}
    return _get(f"/mealplanner/{username}/week/{start_date}", params)


def get_meal_plan_day(
    username: str,
    date: str,
    hash: str,
) -> dict:
    """
    Retrieve a user's meal plan for a specific day. Requires the username,
    the date (YYYY-MM-DD format), and the user's hash token.
    """
    params = {"hash": hash}
    return _get(f"/mealplanner/{username}/day/{date}", params)


def add_meal_plan_item(
    username: str,
    hash: str,
    date: int,
    slot: int,
    position: int,
    item_type: str,
    value: dict,
) -> dict:
    """
    Add an item to a user's meal plan. Provide the username, hash, date
    (Unix timestamp), slot (1=breakfast, 2=lunch, 3=dinner), position,
    item type ('RECIPE' or 'INGREDIENTS'), and a value dict with recipe/ingredient info.
    """
    try:
        api_key = _api_key()
        payload = {
            "date": date,
            "slot": slot,
            "position": position,
            "type": item_type,
            "value": value,
        }
        resp = requests.post(
            f"{BASE_URL}/mealplanner/{username}/items",
            params={"apiKey": api_key, "hash": hash},
            json=payload,
            timeout=15,
        )
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": f"HTTP {resp.status_code}: {resp.text[:300]}"}
    except Exception as e:
        return {"error": str(e)}


def delete_meal_plan_item(
    username: str,
    item_id: int,
    hash: str,
) -> dict:
    """
    Delete an item from a user's meal plan by its item ID.
    Requires the username and hash token.
    """
    try:
        api_key = _api_key()
        resp = requests.delete(
            f"{BASE_URL}/mealplanner/{username}/items/{item_id}",
            params={"apiKey": api_key, "hash": hash},
            timeout=15,
        )
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": f"HTTP {resp.status_code}: {resp.text[:300]}"}
    except Exception as e:
        return {"error": str(e)}


def get_meal_plan_templates(username: str, hash: str) -> dict:
    """
    Get all meal plan templates for a user. Requires the username and hash token.
    """
    params = {"hash": hash}
    return _get(f"/mealplanner/{username}/templates", params)


def get_shopping_list(username: str, start_date: str, end_date: str, hash: str) -> dict:
    """
    Generate a shopping list for a user's meal plan between two dates.
    Dates should be in YYYY-MM-DD format. Requires username and hash token.
    """
    params = {"hash": hash}
    return _get(f"/mealplanner/{username}/shopping-list/{start_date}/{end_date}", params)


def add_to_shopping_list(
    username: str,
    hash: str,
    item: str,
    aisle: str,
    parse: bool = True,
) -> dict:
    """
    Add an item to a user's shopping list. Provide the item name/description,
    the aisle it belongs to, and whether to parse the item string automatically.
    """
    try:
        api_key = _api_key()
        payload = {"item": item, "aisle": aisle, "parse": parse}
        resp = requests.post(
            f"{BASE_URL}/mealplanner/{username}/shopping-list/items",
            params={"apiKey": api_key, "hash": hash},
            json=payload,
            timeout=15,
        )
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": f"HTTP {resp.status_code}: {resp.text[:300]}"}
    except Exception as e:
        return {"error": str(e)}


def delete_from_shopping_list(
    username: str,
    item_id: int,
    hash: str,
) -> dict:
    """
    Delete an item from a user's shopping list by its item ID.
    Requires the username and hash token.
    """
    try:
        api_key = _api_key()
        resp = requests.delete(
            f"{BASE_URL}/mealplanner/{username}/shopping-list/items/{item_id}",
            params={"apiKey": api_key, "hash": hash},
            timeout=15,
        )
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": f"HTTP {resp.status_code}: {resp.text[:300]}"}
    except Exception as e:
        return {"error": str(e)}
