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
    params["apiKey"] = _api_key()
    url = f"{BASE_URL}{path}"
    resp = requests.get(url, params=params, timeout=15)
    resp.raise_for_status()
    return resp.json()


# ---------------------------------------------------------------------------
# Generate meal plan
# ---------------------------------------------------------------------------

def generate_meal_plan(
    time_frame: str = "day",
    target_calories: int = 2000,
    diet: str = "",
    exclude: str = "",
) -> dict:
    """
    Generate a meal plan for a day or a week based on calorie target and diet.

    Args:
        time_frame: 'day' for a single day or 'week' for a full week.
        target_calories: Target daily calorie intake.
        diet: Diet label (e.g. 'vegetarian', 'vegan', 'ketogenic', 'paleo').
        exclude: Comma-separated ingredients or allergens to exclude
                 (e.g. 'shellfish,olives').

    Returns:
        dict with meals list and nutrients summary. For 'week', returns a dict
        with days of the week each containing meals and nutrients.
    """
    try:
        params: dict = {
            "timeFrame": time_frame,
            "targetCalories": target_calories,
        }
        if diet:
            params["diet"] = diet
        if exclude:
            params["exclude"] = exclude
        return _get("/mealplanner/generate", params)
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# User meal plan (requires username/hash — Spoonacular user endpoints)
# ---------------------------------------------------------------------------

def get_meal_plan_week(username: str, start_date: str, hash_token: str) -> dict:
    """
    Get a user's meal plan for a specific week.

    Args:
        username: The Spoonacular username.
        start_date: The start date of the week in 'YYYY-MM-DD' format
                    (must be a Monday).
        hash_token: The user's hash token for authentication.

    Returns:
        dict with the week's meal plan including days, meals, and nutrients.
    """
    try:
        params = {"hash": hash_token}
        return _get(f"/mealplanner/{username}/week/{start_date}", params)
    except Exception as exc:
        return {"error": str(exc)}


def get_meal_plan_day(username: str, date: str, hash_token: str) -> dict:
    """
    Get a user's meal plan for a specific day.

    Args:
        username: The Spoonacular username.
        date: The date in 'YYYY-MM-DD' format.
        hash_token: The user's hash token for authentication.

    Returns:
        dict with the day's meal plan including meals and nutrients.
    """
    try:
        params = {"hash": hash_token}
        return _get(f"/mealplanner/{username}/day/{date}", params)
    except Exception as exc:
        return {"error": str(exc)}


def add_meal_plan_item(
    username: str,
    hash_token: str,
    date: int,
    slot: int,
    position: int,
    item_type: str,
    value: dict,
) -> dict:
    """
    Add an item (recipe or custom food) to a user's meal plan.

    Args:
        username: The Spoonacular username.
        hash_token: The user's hash token for authentication.
        date: The date as a Unix timestamp (seconds).
        slot: The meal slot (1=breakfast, 2=lunch, 3=dinner).
        position: The position within the slot.
        item_type: 'RECIPE' or 'CUSTOM_FOOD' or 'PRODUCT'.
        value: Dict describing the item. For RECIPE: {'id': 123, 'servings': 2,
               'title': 'Pasta', 'imageType': 'jpg'}.

    Returns:
        dict with the created meal plan item ID.
    """
    try:
        key = _api_key()
        url = f"{BASE_URL}/mealplanner/{username}/items"
        payload = {
            "date": date,
            "slot": slot,
            "position": position,
            "type": item_type,
            "value": value,
        }
        resp = requests.post(
            url,
            params={"apiKey": key, "hash": hash_token},
            json=payload,
            timeout=15,
        )
        resp.raise_for_status()
        return resp.json()
    except Exception as exc:
        return {"error": str(exc)}


def delete_meal_plan_item(username: str, item_id: int, hash_token: str) -> dict:
    """
    Delete an item from a user's meal plan.

    Args:
        username: The Spoonacular username.
        item_id: The ID of the meal plan item to delete.
        hash_token: The user's hash token for authentication.

    Returns:
        dict with status of the deletion.
    """
    try:
        key = _api_key()
        url = f"{BASE_URL}/mealplanner/{username}/items/{item_id}"
        resp = requests.delete(
            url,
            params={"apiKey": key, "hash": hash_token},
            timeout=15,
        )
        resp.raise_for_status()
        return resp.json()
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Shopping list
# ---------------------------------------------------------------------------

def get_shopping_list(username: str, hash_token: str) -> dict:
    """
    Get a user's current shopping list.

    Args:
        username: The Spoonacular username.
        hash_token: The user's hash token for authentication.

    Returns:
        dict with shopping list items grouped by aisle.
    """
    try:
        params = {"hash": hash_token}
        return _get(f"/mealplanner/{username}/shopping-list", params)
    except Exception as exc:
        return {"error": str(exc)}


def add_to_shopping_list(
    username: str,
    hash_token: str,
    item: str,
    aisle: str = "",
    parse: bool = True,
) -> dict:
    """
    Add an item to a user's shopping list.

    Args:
        username: The Spoonacular username.
        hash_token: The user's hash token for authentication.
        item: The item to add (e.g. '1 package spaghetti').
        aisle: The aisle where the item can be found (optional).
        parse: Whether to parse the item string automatically.

    Returns:
        dict with the added shopping list item.
    """
    try:
        key = _api_key()
        url = f"{BASE_URL}/mealplanner/{username}/shopping-list/items"
        payload: dict = {"item": item, "parse": parse}
        if aisle:
            payload["aisle"] = aisle
        resp = requests.post(
            url,
            params={"apiKey": key, "hash": hash_token},
            json=payload,
            timeout=15,
        )
        resp.raise_for_status()
        return resp.json()
    except Exception as exc:
        return {"error": str(exc)}


def delete_from_shopping_list(
    username: str,
    item_id: int,
    hash_token: str,
) -> dict:
    """
    Delete an item from a user's shopping list.

    Args:
        username: The Spoonacular username.
        item_id: The ID of the shopping list item to delete.
        hash_token: The user's hash token for authentication.

    Returns:
        dict with status of the deletion.
    """
    try:
        key = _api_key()
        url = f"{BASE_URL}/mealplanner/{username}/shopping-list/items/{item_id}"
        resp = requests.delete(
            url,
            params={"apiKey": key, "hash": hash_token},
            timeout=15,
        )
        resp.raise_for_status()
        return resp.json()
    except Exception as exc:
        return {"error": str(exc)}
