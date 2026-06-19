"""
Spoonacular Meal Planning API tools.
Source: docs/api_meal_planning.md
"""

import os
import requests
from mcp.server.fastmcp import FastMCP

BASE_URL = "https://api.spoonacular.com"


def _api_key() -> str:
    key = os.environ.get("SPOONACULAR_API_KEY", "")
    if not key:
        raise ValueError("SPOONACULAR_API_KEY environment variable is not set")
    return key


def _get(path: str, params: dict) -> dict | list:
    params["apiKey"] = _api_key()
    try:
        resp = requests.get(BASE_URL + path, params=params, timeout=30)
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": f"HTTP {e.response.status_code}: {e.response.text}"}
    except Exception as e:
        return {"error": str(e)}


def _post(path: str, params: dict, json_body: dict) -> dict | list:
    params["apiKey"] = _api_key()
    try:
        resp = requests.post(BASE_URL + path, params=params, json=json_body, timeout=30)
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": f"HTTP {e.response.status_code}: {e.response.text}"}
    except Exception as e:
        return {"error": str(e)}


def _delete(path: str, params: dict) -> dict:
    params["apiKey"] = _api_key()
    try:
        resp = requests.delete(BASE_URL + path, params=params, timeout=30)
        resp.raise_for_status()
        return resp.json() if resp.content else {"success": True}
    except requests.HTTPError as e:
        return {"error": f"HTTP {e.response.status_code}: {e.response.text}"}
    except Exception as e:
        return {"error": str(e)}


def register_meal_planning(mcp: FastMCP):

    @mcp.tool()
    def get_meal_plan_week(
        username: str,
        start_date: str,
        hash: str,
    ) -> dict:
        """Retrieve a meal planned week for a user. start_date format: yyyy-mm-dd.
        Requires the user's username and private hash."""
        params = {"hash": hash}
        return _get(f"/mealplanner/{username}/week/{start_date}", params)

    @mcp.tool()
    def get_meal_plan_day(
        username: str,
        date: str,
        hash: str,
    ) -> dict:
        """Retrieve a meal planned day for a user. date format: yyyy-mm-dd.
        Requires the user's username and private hash."""
        params = {"hash": hash}
        return _get(f"/mealplanner/{username}/day/{date}", params)

    @mcp.tool()
    def generate_meal_plan(
        time_frame: str = "day",
        target_calories: float = None,
        diet: str = "",
        exclude: str = "",
    ) -> dict:
        """Generate a meal plan for a day or week. time_frame: 'day' or 'week'.
        Optionally specify target calories, diet type, and ingredients to exclude."""
        params = {"timeFrame": time_frame}
        if target_calories is not None:
            params["targetCalories"] = target_calories
        if diet:
            params["diet"] = diet
        if exclude:
            params["exclude"] = exclude
        return _get("/mealplanner/generate", params)

    @mcp.tool()
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
        type: 'RECIPE', 'PRODUCT', 'MENU_ITEM', or 'CUSTOM_FOOD'.
        date: Unix timestamp. slot: 1=breakfast, 2=lunch, 3=dinner."""
        params = {"hash": hash}
        body = {
            "date": date,
            "slot": slot,
            "position": position,
            "type": type,
            "value": value,
        }
        return _post(f"/mealplanner/{username}/items", params, body)

    @mcp.tool()
    def clear_meal_plan_day(
        username: str,
        date: str,
        hash: str,
    ) -> dict:
        """Clear (delete) all items from a specific day in a user's meal plan. date format: yyyy-mm-dd."""
        params = {"hash": hash}
        return _delete(f"/mealplanner/{username}/day/{date}", params)

    @mcp.tool()
    def delete_from_meal_plan(
        username: str,
        item_id: int,
        hash: str,
    ) -> dict:
        """Delete a specific item from a user's meal plan by its item ID."""
        params = {"hash": hash}
        return _delete(f"/mealplanner/{username}/items/{item_id}", params)

    @mcp.tool()
    def get_meal_plan_templates(
        username: str,
        hash: str,
    ) -> dict:
        """Get all meal plan templates available for a user."""
        params = {"hash": hash}
        return _get(f"/mealplanner/{username}/templates", params)

    @mcp.tool()
    def get_meal_plan_template(
        username: str,
        template_id: int,
        hash: str,
    ) -> dict:
        """Get a specific meal plan template by its ID for a user."""
        params = {"hash": hash}
        return _get(f"/mealplanner/{username}/templates/{template_id}", params)

    @mcp.tool()
    def add_meal_plan_template(
        username: str,
        hash: str,
        name: str,
    ) -> dict:
        """Create a new meal plan template for a user."""
        params = {"hash": hash}
        body = {"name": name}
        return _post(f"/mealplanner/{username}/templates", params, body)

    @mcp.tool()
    def delete_meal_plan_template(
        username: str,
        template_id: int,
        hash: str,
    ) -> dict:
        """Delete a meal plan template by its ID for a user."""
        params = {"hash": hash}
        return _delete(f"/mealplanner/{username}/templates/{template_id}", params)

    @mcp.tool()
    def get_shopping_list(
        username: str,
        hash: str,
    ) -> dict:
        """Get the current shopping list for a user."""
        params = {"hash": hash}
        return _get(f"/mealplanner/{username}/shopping-list", params)

    @mcp.tool()
    def add_to_shopping_list(
        username: str,
        hash: str,
        item: str,
        aisle: str,
        parse: bool = True,
    ) -> dict:
        """Add an item to a user's shopping list."""
        params = {"hash": hash}
        body = {"item": item, "aisle": aisle, "parse": parse}
        return _post(f"/mealplanner/{username}/shopping-list/items", params, body)

    @mcp.tool()
    def delete_from_shopping_list(
        username: str,
        item_id: int,
        hash: str,
    ) -> dict:
        """Delete a specific item from a user's shopping list by its item ID."""
        params = {"hash": hash}
        return _delete(f"/mealplanner/{username}/shopping-list/items/{item_id}", params)

    @mcp.tool()
    def generate_shopping_list(
        username: str,
        start_date: str,
        end_date: str,
        hash: str,
    ) -> dict:
        """Generate a shopping list from a user's meal plan between two dates.
        date format: yyyy-mm-dd."""
        params = {"hash": hash}
        return _post(
            f"/mealplanner/{username}/shopping-list/{start_date}/{end_date}",
            params,
            {},
        )

    @mcp.tool()
    def connect_user(
        username: str,
        first_name: str,
        last_name: str,
        email: str,
    ) -> dict:
        """Connect a user to spoonacular to get their username and hash for meal planning endpoints."""
        params = {}
        body = {
            "username": username,
            "firstName": first_name,
            "lastName": last_name,
            "email": email,
        }
        return _post("/users/connect", params, body)
