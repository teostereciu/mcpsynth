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


def _get(path: str, params: dict) -> dict | list:
    params = {k: v for k, v in params.items() if v is not None}
    params["apiKey"] = _api_key()
    try:
        r = requests.get(f"{BASE_URL}{path}", params=params, timeout=30)
        r.raise_for_status()
        return r.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": e.response.status_code if e.response else None}
    except Exception as e:
        return {"error": str(e)}


def _post(path: str, params: dict, json_body: dict) -> dict | list:
    params = {k: v for k, v in params.items() if v is not None}
    params["apiKey"] = _api_key()
    try:
        r = requests.post(f"{BASE_URL}{path}", params=params, json=json_body, timeout=30)
        r.raise_for_status()
        return r.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": e.response.status_code if e.response else None}
    except Exception as e:
        return {"error": str(e)}


def _delete(path: str, params: dict) -> dict:
    params = {k: v for k, v in params.items() if v is not None}
    params["apiKey"] = _api_key()
    try:
        r = requests.delete(f"{BASE_URL}{path}", params=params, timeout=30)
        r.raise_for_status()
        return r.json() if r.content else {"success": True}
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": e.response.status_code if e.response else None}
    except Exception as e:
        return {"error": str(e)}


def get_meal_plan_week(username: str, start_date: str, hash: str) -> dict:
    """Retrieve a meal planned week for a user.
    start_date: format yyyy-mm-dd (Monday of the week).
    hash: the user's private hash from Connect User."""
    return _get(f"/mealplanner/{username}/week/{start_date}", {"hash": hash})


def get_meal_plan_day(username: str, date: str, hash: str) -> dict:
    """Retrieve a meal planned day for a user.
    date: format yyyy-mm-dd.
    hash: the user's private hash from Connect User."""
    return _get(f"/mealplanner/{username}/day/{date}", {"hash": hash})


def generate_meal_plan(
    time_frame: Optional[str] = None,
    target_calories: Optional[float] = None,
    diet: Optional[str] = None,
    exclude: Optional[str] = None,
) -> dict:
    """Generate a meal plan with three meals per day for a specific time frame.
    time_frame: 'day' or 'week'.
    exclude: comma-separated list of ingredients or allergens to exclude."""
    return _get("/mealplanner/generate", {
        "timeFrame": time_frame,
        "targetCalories": target_calories,
        "diet": diet,
        "exclude": exclude,
    })


def add_to_meal_plan(
    username: str,
    hash: str,
    date: int,
    slot: int,
    position: int,
    type: str,
    value: dict,
) -> dict:
    """Add a recipe, product, or ingredient to a user's meal plan.
    date: Unix timestamp of the day.
    slot: 1=breakfast, 2=lunch, 3=dinner.
    type: 'RECIPE', 'PRODUCT', or 'INGREDIENTS'.
    value: dict with item details (id, servings, title, etc.)."""
    return _post(f"/mealplanner/{username}/items", {"hash": hash}, {
        "date": date,
        "slot": slot,
        "position": position,
        "type": type,
        "value": value,
    })


def clear_meal_plan_day(username: str, date: str, hash: str) -> dict:
    """Delete all planned meals for a specific day for a user.
    date: format yyyy-mm-dd."""
    return _delete(f"/mealplanner/{username}/day/{date}", {"hash": hash})


def delete_from_meal_plan(username: str, item_id: int, hash: str) -> dict:
    """Delete a specific item from a user's meal plan by item ID."""
    return _delete(f"/mealplanner/{username}/items/{item_id}", {"hash": hash})


def get_meal_plan_templates(username: str, hash: str) -> dict:
    """Get all meal plan templates available for a user."""
    return _get(f"/mealplanner/{username}/templates", {"hash": hash})


def get_meal_plan_template(username: str, template_id: int, hash: str) -> dict:
    """Get a specific meal plan template by ID for a user."""
    return _get(f"/mealplanner/{username}/templates/{template_id}", {"hash": hash})


def add_meal_plan_template(username: str, hash: str, name: Optional[str] = None) -> dict:
    """Create a new meal plan template for a user."""
    body = {}
    if name:
        body["name"] = name
    return _post(f"/mealplanner/{username}/templates", {"hash": hash}, body)


def delete_meal_plan_template(username: str, template_id: int, hash: str) -> dict:
    """Delete a meal plan template by ID for a user."""
    return _delete(f"/mealplanner/{username}/templates/{template_id}", {"hash": hash})


def get_shopping_list(username: str, hash: str) -> dict:
    """Get the current shopping list for a user."""
    return _get(f"/mealplanner/{username}/shopping-list", {"hash": hash})


def add_to_shopping_list(
    username: str,
    hash: str,
    item: str,
    aisle: str,
    parse: Optional[bool] = None,
) -> dict:
    """Add an item to a user's shopping list.
    item: the item name/description.
    aisle: the aisle category (e.g. 'Produce', 'Dairy')."""
    return _post(f"/mealplanner/{username}/shopping-list/items", {"hash": hash}, {
        "item": item,
        "aisle": aisle,
        "parse": parse,
    })


def delete_from_shopping_list(username: str, item_id: int, hash: str) -> dict:
    """Delete a specific item from a user's shopping list by item ID."""
    return _delete(f"/mealplanner/{username}/shopping-list/items/{item_id}", {"hash": hash})


def generate_shopping_list(
    username: str,
    hash: str,
    start_date: str,
    end_date: str,
) -> dict:
    """Generate a shopping list from a user's meal plan between two dates.
    start_date, end_date: format yyyy-mm-dd."""
    return _post(
        f"/mealplanner/{username}/shopping-list/{start_date}/{end_date}",
        {"hash": hash},
        {},
    )


def compute_shopping_list(ingredients: list) -> dict:
    """Compute a shopping list from a set of simple food items (no user account required).
    ingredients: list of ingredient strings."""
    params = {"apiKey": _api_key()}
    try:
        r = requests.post(
            f"{BASE_URL}/mealplanner/shopping-list/compute",
            params=params,
            json={"ingredients": ingredients},
            timeout=30,
        )
        r.raise_for_status()
        return r.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": e.response.status_code if e.response else None}
    except Exception as e:
        return {"error": str(e)}


def connect_user(
    username: str,
    first_name: str,
    last_name: str,
    email: str,
) -> dict:
    """Connect your app's user to spoonacular to get a username and hash for meal planning endpoints."""
    return _post("/users/connect", {}, {
        "username": username,
        "firstName": first_name,
        "lastName": last_name,
        "email": email,
    })
