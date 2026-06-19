"""Spoonacular Meal Planning API tools."""
import os
import requests
from typing import Optional

BASE_URL = "https://api.spoonacular.com"


def _api_key() -> str:
    key = os.environ.get("SPOONACULAR_API_KEY", "")
    if not key:
        raise ValueError("SPOONACULAR_API_KEY environment variable not set")
    return key


def _get(path: str, params: dict) -> dict:
    params["apiKey"] = _api_key()
    try:
        resp = requests.get(f"{BASE_URL}{path}", params=params, timeout=30)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def _post(path: str, json_body: dict, params: dict = None) -> dict:
    p = params or {}
    p["apiKey"] = _api_key()
    try:
        resp = requests.post(f"{BASE_URL}{path}", json=json_body, params=p, timeout=30)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def _delete(path: str, params: dict) -> dict:
    params["apiKey"] = _api_key()
    try:
        resp = requests.delete(f"{BASE_URL}{path}", params=params, timeout=30)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def get_meal_plan_week(username: str, start_date: str, hash: str) -> dict:
    """Retrieve a meal planned week for a user (format: yyyy-mm-dd)."""
    params = {"hash": hash}
    return _get(f"/mealplanner/{username}/week/{start_date}", params)


def get_meal_plan_day(username: str, date: str, hash: str) -> dict:
    """Retrieve a meal planned day for a user (format: yyyy-mm-dd)."""
    params = {"hash": hash}
    return _get(f"/mealplanner/{username}/day/{date}", params)


def generate_meal_plan(
    time_frame: str = "day",
    target_calories: Optional[float] = None,
    diet: Optional[str] = None,
    exclude: Optional[str] = None,
) -> dict:
    """Generate a meal plan with target calories, diet, and exclusions for a day or week."""
    params: dict = {"timeFrame": time_frame}
    if target_calories is not None:
        params["targetCalories"] = target_calories
    if diet:
        params["diet"] = diet
    if exclude:
        params["exclude"] = exclude
    return _get("/mealplanner/generate", params)


def add_to_meal_plan(username: str, hash: str, item: dict) -> dict:
    """Add a recipe, product, or custom food to a user's meal plan.

    item should be a dict with keys: date (epoch), slot, position, type, value.
    """
    params = {"hash": hash}
    return _post(f"/mealplanner/{username}/items", item, params)


def clear_meal_plan_day(username: str, date: str, hash: str) -> dict:
    """Clear all items from a specific day in a user's meal plan."""
    params = {"hash": hash}
    return _delete(f"/mealplanner/{username}/day/{date}", params)


def delete_from_meal_plan(username: str, item_id: int, hash: str) -> dict:
    """Delete a specific item from a user's meal plan by item ID."""
    params = {"hash": hash}
    return _delete(f"/mealplanner/{username}/items/{item_id}", params)


def get_meal_plan_templates(username: str, hash: str) -> dict:
    """Get all meal plan templates available for a user."""
    params = {"hash": hash}
    return _get(f"/mealplanner/{username}/templates", params)


def get_meal_plan_template(username: str, template_id: int, hash: str) -> dict:
    """Get a specific meal plan template by ID."""
    params = {"hash": hash}
    return _get(f"/mealplanner/{username}/templates/{template_id}", params)


def add_meal_plan_template(username: str, hash: str) -> dict:
    """Add a new meal plan template for a user."""
    params = {"hash": hash}
    return _post(f"/mealplanner/{username}/templates", {}, params)


def delete_meal_plan_template(username: str, template_id: int, hash: str) -> dict:
    """Delete a meal plan template by ID."""
    params = {"hash": hash}
    return _delete(f"/mealplanner/{username}/templates/{template_id}", params)


def get_shopping_list(username: str, hash: str) -> dict:
    """Get the current shopping list for a user."""
    params = {"hash": hash}
    return _get(f"/mealplanner/{username}/shopping-list", params)


def add_to_shopping_list(username: str, hash: str, item: dict) -> dict:
    """Add an item to a user's shopping list.

    item should be a dict with keys: item, aisle, parse (bool).
    """
    params = {"hash": hash}
    return _post(f"/mealplanner/{username}/shopping-list/items", item, params)


def delete_from_shopping_list(username: str, item_id: int, hash: str) -> dict:
    """Delete an item from a user's shopping list by item ID."""
    params = {"hash": hash}
    return _delete(f"/mealplanner/{username}/shopping-list/items/{item_id}", params)


def generate_shopping_list(
    username: str,
    start_date: str,
    end_date: str,
    hash: str,
) -> dict:
    """Generate a shopping list for a user based on their meal plan between two dates."""
    params = {"hash": hash}
    return _post(
        f"/mealplanner/{username}/shopping-list/{start_date}/{end_date}",
        {},
        params,
    )


def compute_shopping_list(ingredients: list) -> dict:
    """Compute a shopping list from a list of ingredient strings (no user required).

    ingredients: list of ingredient strings, e.g. ["1 cup flour", "2 eggs"]
    """
    try:
        params = {"apiKey": _api_key()}
        resp = requests.post(
            f"{BASE_URL}/mealplanner/shopping-list/compute",
            json={"ingredients": ingredients},
            params=params,
            timeout=30,
        )
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def search_custom_foods(
    username: str,
    hash: str,
    query: Optional[str] = None,
    offset: int = 0,
    number: int = 10,
) -> dict:
    """Search custom foods added by a user."""
    params: dict = {"hash": hash, "offset": offset, "number": number}
    if query:
        params["query"] = query
    return _get(f"/food/customFoods/search", params)


def connect_user(username: str, first_name: str, last_name: str, email: str) -> dict:
    """Connect an app user to spoonacular to get a username and hash for meal planning."""
    params = {"apiKey": _api_key()}
    try:
        resp = requests.post(
            f"{BASE_URL}/users/connect",
            json={
                "username": username,
                "firstName": first_name,
                "lastName": last_name,
                "email": email,
            },
            params=params,
            timeout=30,
        )
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        return {"error": str(e)}
