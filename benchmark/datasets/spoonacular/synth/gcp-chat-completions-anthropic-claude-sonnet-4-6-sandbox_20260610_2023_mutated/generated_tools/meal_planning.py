"""
Spoonacular Meal Planning API tools.
Endpoints covered:
  - GET  /mealplanner/{username}/week/{start-date}
  - GET  /mealplanner/{username}/day/{date}
  - GET  /recipes/mealplans/generate
  - POST /mealplanner/{username}/items
  - DELETE /mealplanner/{username}/day/{date}
  - DELETE /mealplanner/{username}/items/{id}
  - GET  /mealplanner/{username}/templates
  - GET  /mealplanner/{username}/templates/{id}
  - POST /mealplanner/{username}/templates
  - DELETE /mealplanner/{username}/templates/{id}
  - GET  /mealplanner/{username}/shopping-list
  - POST /mealplanner/{username}/shopping-list/items
  - DELETE /mealplanner/{username}/shopping-list/items/{id}
  - POST /mealplanner/{username}/shopping-list/{start-date}/{end-date}
  - GET  /food/customFoods/search
  - POST /users/connect
"""

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
        resp = requests.get(f"{BASE_URL}{path}", params=params, timeout=15)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def _post(path: str, params: dict, json_body: Optional[dict] = None, data: Optional[dict] = None) -> dict:
    params["apiKey"] = _api_key()
    try:
        if json_body is not None:
            resp = requests.post(f"{BASE_URL}{path}", params=params, json=json_body, timeout=15)
        else:
            resp = requests.post(f"{BASE_URL}{path}", params=params, data=data, timeout=15)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def _delete(path: str, params: dict) -> dict:
    params["apiKey"] = _api_key()
    try:
        resp = requests.delete(f"{BASE_URL}{path}", params=params, timeout=15)
        resp.raise_for_status()
        return resp.json() if resp.content else {"status": "deleted"}
    except Exception as e:
        return {"error": str(e)}


def get_meal_plan_week(
    username: str,
    start_date: str,
    hash: str,
) -> dict:
    """Retrieve a meal planned week for a user.
    start_date: format yyyy-mm-dd (must be a Monday).
    hash: the user's private hash from spoonacular."""
    params: dict = {"hash": hash}
    return _get(f"/mealplanner/{username}/week/{start_date}", params)


def get_meal_plan_day(
    username: str,
    date: str,
    hash: str,
) -> dict:
    """Retrieve a meal planned day for a user.
    date: format yyyy-mm-dd.
    hash: the user's private hash from spoonacular."""
    params: dict = {"hash": hash}
    return _get(f"/mealplanner/{username}/day/{date}", params)


def generate_meal_plan(
    time_frame: str = "day",
    target_calories: Optional[float] = None,
    diet: Optional[str] = None,
    exclude: Optional[str] = None,
) -> dict:
    """Generate a meal plan with recipes for a day or week.
    time_frame: 'day' or 'week'.
    target_calories: the target number of calories per day.
    diet: the diet type (e.g. 'vegetarian', 'vegan', 'ketogenic').
    exclude: comma-separated list of ingredients or ingredient types to exclude."""
    params: dict = {"timeFrame": time_frame}
    if target_calories is not None:
        params["targetCalories"] = target_calories
    if diet is not None:
        params["diet"] = diet
    if exclude is not None:
        params["exclude"] = exclude
    return _get("/recipes/mealplans/generate", params)


def add_to_meal_plan(
    username: str,
    hash: str,
    date: int,
    slot: int,
    position: int,
    type: str,
    value: dict,
) -> dict:
    """Add a recipe, product, or custom food to a user's meal plan.
    date: Unix timestamp of the day.
    slot: 1=breakfast, 2=lunch, 3=dinner.
    type: 'RECIPE', 'PRODUCT', 'MENU_ITEM', or 'CUSTOM_FOOD'.
    value: dict with item details (id, servings, title, etc.)."""
    params: dict = {"hash": hash}
    body: dict = {
        "date": date,
        "slot": slot,
        "position": position,
        "type": type,
        "value": value,
    }
    return _post(f"/mealplanner/{username}/items", params, json_body=body)


def clear_meal_plan_day(
    username: str,
    date: str,
    hash: str,
) -> dict:
    """Clear (delete) all items from a specific day in a user's meal plan.
    date: format yyyy-mm-dd."""
    params: dict = {"hash": hash}
    return _delete(f"/mealplanner/{username}/day/{date}", params)


def delete_from_meal_plan(
    username: str,
    item_id: int,
    hash: str,
) -> dict:
    """Delete a specific item from a user's meal plan by its item ID."""
    params: dict = {"hash": hash}
    return _delete(f"/mealplanner/{username}/items/{item_id}", params)


def get_meal_plan_templates(
    username: str,
    hash: str,
) -> dict:
    """Get all meal plan templates available for a user (both public and user-created)."""
    params: dict = {"hash": hash}
    return _get(f"/mealplanner/{username}/templates", params)


def get_meal_plan_template(
    username: str,
    template_id: int,
    hash: str,
) -> dict:
    """Get a specific meal plan template by its ID."""
    params: dict = {"hash": hash}
    return _get(f"/mealplanner/{username}/templates/{template_id}", params)


def add_meal_plan_template(
    username: str,
    hash: str,
    name: str,
) -> dict:
    """Create a new meal plan template for a user."""
    params: dict = {"hash": hash}
    return _post(f"/mealplanner/{username}/templates", params, json_body={"name": name})


def delete_meal_plan_template(
    username: str,
    template_id: int,
    hash: str,
) -> dict:
    """Delete a meal plan template by its ID."""
    params: dict = {"hash": hash}
    return _delete(f"/mealplanner/{username}/templates/{template_id}", params)


def get_shopping_list(
    username: str,
    hash: str,
) -> dict:
    """Get the current shopping list for a user."""
    params: dict = {"hash": hash}
    return _get(f"/mealplanner/{username}/shopping-list", params)


def add_to_shopping_list(
    username: str,
    hash: str,
    item: str,
    aisle: str,
    parse: bool = True,
) -> dict:
    """Add an item to a user's shopping list.
    item: the item name/description (e.g. '1 package baking powder').
    aisle: the aisle in the supermarket (e.g. 'Baking').
    parse: whether to parse the item into structured data."""
    params: dict = {"hash": hash}
    body: dict = {"item": item, "aisle": aisle, "parse": parse}
    return _post(f"/mealplanner/{username}/shopping-list/items", params, json_body=body)


def delete_from_shopping_list(
    username: str,
    item_id: int,
    hash: str,
) -> dict:
    """Delete a specific item from a user's shopping list by its item ID."""
    params: dict = {"hash": hash}
    return _delete(f"/mealplanner/{username}/shopping-list/items/{item_id}", params)


def generate_shopping_list(
    username: str,
    start_date: str,
    end_date: str,
    hash: str,
) -> dict:
    """Generate a shopping list from a user's meal plan between two dates.
    start_date / end_date: format yyyy-mm-dd."""
    params: dict = {"hash": hash}
    return _post(f"/mealplanner/{username}/shopping-list/{start_date}/{end_date}", params, json_body={})


def search_custom_foods(
    username: str,
    hash: str,
    search_query: Optional[str] = None,
    offset: int = 0,
    number: int = 10,
) -> dict:
    """Search a user's custom foods."""
    params: dict = {"hash": hash, "offset": offset, "number": number}
    if search_query is not None:
        params["query"] = search_query
    return _get("/food/customFoods/search", params)


def connect_user(
    username: str,
    first_name: str,
    last_name: str,
    email: str,
) -> dict:
    """Connect an app user with spoonacular to get a username and hash for meal planning.
    Returns the spoonacular username and hash needed for all meal planning endpoints."""
    body: dict = {
        "username": username,
        "firstName": first_name,
        "lastName": last_name,
        "email": email,
    }
    return _post("/users/connect", {}, json_body=body)
