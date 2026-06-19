"""
Spoonacular Meal Planning tools — generate daily/weekly meal plans,
manage meal plan items, and retrieve meal plan templates.
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
    try:
        resp = requests.get(url, params=params, timeout=15)
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as exc:
        return {"error": f"HTTP {exc.response.status_code}: {exc.response.text}"}
    except Exception as exc:
        return {"error": str(exc)}


def _post(path: str, json_body: dict) -> dict | list:
    params = {"apiKey": _api_key()}
    url = f"{BASE_URL}{path}"
    try:
        resp = requests.post(url, params=params, json=json_body, timeout=15)
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as exc:
        return {"error": f"HTTP {exc.response.status_code}: {exc.response.text}"}
    except Exception as exc:
        return {"error": str(exc)}


def _delete(path: str, params: dict) -> dict:
    params["apiKey"] = _api_key()
    url = f"{BASE_URL}{path}"
    try:
        resp = requests.delete(url, params=params, timeout=15)
        resp.raise_for_status()
        return resp.json() if resp.text else {"status": "deleted"}
    except requests.HTTPError as exc:
        return {"error": f"HTTP {exc.response.status_code}: {exc.response.text}"}
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Meal Plan Generation
# ---------------------------------------------------------------------------

def generate_meal_plan(
    time_frame: str = "day",
    target_calories: float = 2000,
    diet: str = "",
    exclude: str = "",
) -> dict:
    """
    Generate a meal plan for a day or a week based on calorie target, diet,
    and exclusions. No account required.

    Args:
        time_frame: "day" for a single day or "week" for a full week.
        target_calories: Daily calorie target (e.g. 2000).
        diet: Diet label (e.g. "vegetarian", "vegan", "ketogenic").
        exclude: Comma-separated ingredients or food groups to exclude
                 (e.g. "shellfish,olives").

    Returns:
        dict with meals list and nutrients summary. For "week", returns
        a dict with days of the week each containing meals and nutrients.
    """
    params: dict = {
        "timeFrame": time_frame,
        "targetCalories": target_calories,
    }
    if diet:
        params["diet"] = diet
    if exclude:
        params["exclude"] = exclude
    return _get("/mealplanner/generate", params)


# ---------------------------------------------------------------------------
# User Meal Plan (requires Spoonacular user account / username + hash)
# ---------------------------------------------------------------------------

def get_meal_plan_week(username: str, start_date: str, hash: str) -> dict:
    """
    Get a user's meal plan for a specific week.

    Args:
        username: Spoonacular username.
        start_date: Start date of the week in YYYY-MM-DD format (must be a Monday).
        hash: User-specific hash for authentication.

    Returns:
        dict with the week's meal plan including days, meals, and nutrients.
    """
    params = {"hash": hash}
    return _get(f"/mealplanner/{username}/week/{start_date}", params)


def get_meal_plan_day(username: str, date: str, hash: str) -> dict:
    """
    Get a user's meal plan for a specific day.

    Args:
        username: Spoonacular username.
        date: Date in YYYY-MM-DD format.
        hash: User-specific hash for authentication.

    Returns:
        dict with the day's meal plan including meals and nutrients.
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
    Add an item (recipe, product, or custom food) to a user's meal plan.

    Args:
        username: Spoonacular username.
        hash: User-specific hash for authentication.
        date: Unix timestamp (seconds) for the meal plan date.
        slot: Meal slot (1=breakfast, 2=lunch, 3=dinner).
        position: Position within the slot (0-indexed).
        item_type: Type of item: "RECIPE", "PRODUCT", or "MENU_ITEM".
        value: Dict describing the item, e.g.:
               {"id": 715538, "servings": 1, "title": "...", "imageType": "jpg"}

    Returns:
        dict with the created meal plan item ID.
    """
    body = {
        "date": date,
        "slot": slot,
        "position": position,
        "type": item_type,
        "value": value,
    }
    return _post(f"/mealplanner/{username}/items", body)


def delete_meal_plan_item(username: str, item_id: int, hash: str) -> dict:
    """
    Delete an item from a user's meal plan.

    Args:
        username: Spoonacular username.
        item_id: ID of the meal plan item to delete.
        hash: User-specific hash for authentication.

    Returns:
        dict confirming deletion.
    """
    return _delete(f"/mealplanner/{username}/items/{item_id}", {"hash": hash})


def get_meal_plan_templates(username: str, hash: str) -> dict:
    """
    Get all meal plan templates for a user.

    Args:
        username: Spoonacular username.
        hash: User-specific hash for authentication.

    Returns:
        dict with list of meal plan templates.
    """
    params = {"hash": hash}
    return _get(f"/mealplanner/{username}/templates", params)


def get_meal_plan_template(username: str, template_id: int, hash: str) -> dict:
    """
    Get a specific meal plan template for a user.

    Args:
        username: Spoonacular username.
        template_id: ID of the meal plan template.
        hash: User-specific hash for authentication.

    Returns:
        dict with the meal plan template details.
    """
    params = {"hash": hash}
    return _get(f"/mealplanner/{username}/templates/{template_id}", params)


def delete_meal_plan_template(username: str, template_id: int, hash: str) -> dict:
    """
    Delete a meal plan template for a user.

    Args:
        username: Spoonacular username.
        template_id: ID of the meal plan template to delete.
        hash: User-specific hash for authentication.

    Returns:
        dict confirming deletion.
    """
    return _delete(f"/mealplanner/{username}/templates/{template_id}", {"hash": hash})


# ---------------------------------------------------------------------------
# Shopping List
# ---------------------------------------------------------------------------

def get_shopping_list(username: str, hash: str) -> dict:
    """
    Get a user's current shopping list.

    Args:
        username: Spoonacular username.
        hash: User-specific hash for authentication.

    Returns:
        dict with shopping list items grouped by aisle.
    """
    params = {"hash": hash}
    return _get(f"/mealplanner/{username}/shopping-list", params)


def add_to_shopping_list(
    username: str,
    hash: str,
    item: str,
    aisle: str,
    parse: bool = True,
) -> dict:
    """
    Add an item to a user's shopping list.

    Args:
        username: Spoonacular username.
        hash: User-specific hash for authentication.
        item: Item string to add (e.g. "1 package baking powder").
        aisle: Aisle category (e.g. "Baking", "Produce").
        parse: Whether to parse the item string automatically.

    Returns:
        dict with the created shopping list item.
    """
    body = {"item": item, "aisle": aisle, "parse": parse}
    return _post(f"/mealplanner/{username}/shopping-list/items", body)


def delete_shopping_list_item(username: str, item_id: int, hash: str) -> dict:
    """
    Delete an item from a user's shopping list.

    Args:
        username: Spoonacular username.
        item_id: ID of the shopping list item to delete.
        hash: User-specific hash for authentication.

    Returns:
        dict confirming deletion.
    """
    return _delete(
        f"/mealplanner/{username}/shopping-list/items/{item_id}",
        {"hash": hash},
    )
