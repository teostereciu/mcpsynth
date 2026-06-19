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
  - POST /mealplanner/shopping-list/compute
  - GET  /mealplanner/{username}/custom-foods
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
    params = {k: v for k, v in params.items() if v is not None}
    params["apiKey"] = _api_key()
    try:
        resp = requests.get(f"{BASE_URL}{path}", params=params, timeout=15)
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


def _post_json(path: str, body: dict, params: dict | None = None) -> dict:
    if params is None:
        params = {}
    params = {k: v for k, v in params.items() if v is not None}
    params["apiKey"] = _api_key()
    body = {k: v for k, v in body.items() if v is not None}
    try:
        resp = requests.post(
            f"{BASE_URL}{path}",
            json=body,
            params=params,
            timeout=15,
        )
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


def _post_form(path: str, data: dict, params: dict | None = None) -> dict:
    if params is None:
        params = {}
    params = {k: v for k, v in params.items() if v is not None}
    params["apiKey"] = _api_key()
    data = {k: v for k, v in data.items() if v is not None}
    try:
        resp = requests.post(
            f"{BASE_URL}{path}",
            data=data,
            params=params,
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            timeout=15,
        )
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


def _delete(path: str, params: dict) -> dict:
    params = {k: v for k, v in params.items() if v is not None}
    params["apiKey"] = _api_key()
    try:
        resp = requests.delete(f"{BASE_URL}{path}", params=params, timeout=15)
        resp.raise_for_status()
        if resp.content:
            return resp.json()
        return {"success": True}
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


# ---------------------------------------------------------------------------
# Get Meal Plan Week
# ---------------------------------------------------------------------------

def get_meal_plan_week(username: str, start_date: str, hash: str) -> dict:
    """Retrieve a meal planned week for a user (format: yyyy-mm-dd)."""
    return _get(f"/mealplanner/{username}/week/{start_date}", {"hash": hash})


# ---------------------------------------------------------------------------
# Get Meal Plan Day
# ---------------------------------------------------------------------------

def get_meal_plan_day(username: str, date: str, hash: str) -> dict:
    """Retrieve a meal planned day for a user (format: yyyy-mm-dd)."""
    return _get(f"/mealplanner/{username}/day/{date}", {"hash": hash})


# ---------------------------------------------------------------------------
# Generate Meal Plan
# ---------------------------------------------------------------------------

def generate_meal_plan(
    time_frame: Optional[str] = None,
    target_calories: Optional[int] = None,
    diet: Optional[str] = None,
    exclude: Optional[str] = None,
) -> dict:
    """Generate a meal plan with daily or weekly recipes that fit nutritional goals."""
    return _get("/recipes/mealplans/generate", {
        "timeFrame": time_frame,
        "targetCalories": target_calories,
        "diet": diet,
        "exclude": exclude,
    })


# ---------------------------------------------------------------------------
# Add to Meal Plan
# ---------------------------------------------------------------------------

def add_to_meal_plan(
    username: str,
    hash: str,
    date: int,
    slot: int,
    position: int,
    type: str,
    value: dict,
) -> dict:
    """Add a recipe, product, or ingredient to a user's meal plan."""
    body = {
        "date": date,
        "slot": slot,
        "position": position,
        "type": type,
        "value": value,
    }
    return _post_json(f"/mealplanner/{username}/items", body, {"hash": hash})


# ---------------------------------------------------------------------------
# Clear Meal Plan Day
# ---------------------------------------------------------------------------

def clear_meal_plan_day(username: str, date: str, hash: str) -> dict:
    """Delete all planned meals for a specific day."""
    return _delete(f"/mealplanner/{username}/day/{date}", {"hash": hash})


# ---------------------------------------------------------------------------
# Delete from Meal Plan
# ---------------------------------------------------------------------------

def delete_from_meal_plan(username: str, item_id: int, hash: str) -> dict:
    """Delete a specific item from a user's meal plan."""
    return _delete(f"/mealplanner/{username}/items/{item_id}", {"hash": hash})


# ---------------------------------------------------------------------------
# Get Meal Plan Templates
# ---------------------------------------------------------------------------

def get_meal_plan_templates(username: str, hash: str) -> dict:
    """Get meal plan templates available to a user."""
    return _get(f"/mealplanner/{username}/templates", {"hash": hash})


# ---------------------------------------------------------------------------
# Get Meal Plan Template
# ---------------------------------------------------------------------------

def get_meal_plan_template(username: str, template_id: int, hash: str) -> dict:
    """Get a specific meal plan template by ID."""
    return _get(f"/mealplanner/{username}/templates/{template_id}", {"hash": hash})


# ---------------------------------------------------------------------------
# Add Meal Plan Template
# ---------------------------------------------------------------------------

def add_meal_plan_template(username: str, hash: str) -> dict:
    """Add a meal plan template for a user."""
    return _post_form(f"/mealplanner/{username}/templates", {}, {"hash": hash})


# ---------------------------------------------------------------------------
# Delete Meal Plan Template
# ---------------------------------------------------------------------------

def delete_meal_plan_template(username: str, template_id: int, hash: str) -> dict:
    """Delete a meal plan template by ID."""
    return _delete(f"/mealplanner/{username}/templates/{template_id}", {"hash": hash})


# ---------------------------------------------------------------------------
# Get Shopping List
# ---------------------------------------------------------------------------

def get_shopping_list(username: str, hash: str) -> dict:
    """Get a user's current shopping list."""
    return _get(f"/mealplanner/{username}/shopping-list", {"hash": hash})


# ---------------------------------------------------------------------------
# Add to Shopping List
# ---------------------------------------------------------------------------

def add_to_shopping_list(
    username: str,
    hash: str,
    item: str,
    aisle: str,
    parse: Optional[bool] = None,
) -> dict:
    """Add an item to a user's shopping list."""
    body = {"item": item, "aisle": aisle, "parse": parse}
    return _post_json(f"/mealplanner/{username}/shopping-list/items", body, {"hash": hash})


# ---------------------------------------------------------------------------
# Delete from Shopping List
# ---------------------------------------------------------------------------

def delete_from_shopping_list(username: str, item_id: int, hash: str) -> dict:
    """Delete an item from a user's shopping list."""
    return _delete(f"/mealplanner/{username}/shopping-list/items/{item_id}", {"hash": hash})


# ---------------------------------------------------------------------------
# Generate Shopping List
# ---------------------------------------------------------------------------

def generate_shopping_list(
    username: str,
    start_date: str,
    end_date: str,
    hash: str,
) -> dict:
    """Generate a shopping list from a user's meal plan between two dates."""
    return _post_form(
        f"/mealplanner/{username}/shopping-list/{start_date}/{end_date}",
        {},
        {"hash": hash},
    )


# ---------------------------------------------------------------------------
# Compute Shopping List
# ---------------------------------------------------------------------------

def compute_shopping_list(ingredient_list: str) -> dict:
    """Compute a shopping list from a set of simple foods (no username required)."""
    return _post_form("/mealplanner/shopping-list/compute", {
        "ingredientList": ingredient_list,
    })


# ---------------------------------------------------------------------------
# Search Custom Foods
# ---------------------------------------------------------------------------

def search_custom_foods(
    username: str,
    hash: str,
    query: Optional[str] = None,
    offset: Optional[int] = None,
    number: Optional[int] = None,
) -> dict:
    """Search a user's custom foods."""
    return _get(f"/mealplanner/{username}/custom-foods", {
        "hash": hash,
        "query": query,
        "offset": offset,
        "number": number,
    })


# ---------------------------------------------------------------------------
# Connect User
# ---------------------------------------------------------------------------

def connect_user(
    username: str,
    first_name: str,
    last_name: str,
    email: str,
) -> dict:
    """Connect an app user to spoonacular to get a username and hash for meal planning."""
    return _post_json("/users/connect", {
        "username": username,
        "firstName": first_name,
        "lastName": last_name,
        "email": email,
    })
