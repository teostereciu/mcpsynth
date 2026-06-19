"""
Spoonacular Meal Planning tools — generate daily/weekly meal plans,
manage meal plan items, and shopping lists.
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
    except requests.HTTPError as exc:
        return {"error": f"HTTP {exc.response.status_code}: {exc.response.text}"}
    except Exception as exc:
        return {"error": str(exc)}


def _post_json(path: str, payload: dict, params: dict = None) -> dict | list:
    if params is None:
        params = {}
    params = {k: v for k, v in params.items() if v is not None}
    try:
        params["apiKey"] = _api_key()
    except ValueError as exc:
        return {"error": str(exc)}
    try:
        resp = requests.post(
            f"{BASE_URL}{path}",
            params=params,
            json={k: v for k, v in payload.items() if v is not None},
            timeout=15,
        )
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as exc:
        return {"error": f"HTTP {exc.response.status_code}: {exc.response.text}"}
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Meal Plan Generation
# ---------------------------------------------------------------------------

def generate_meal_plan_daily(
    time_frame: str = "day",
    target_calories: float = None,
    diet: str = None,
    exclude: str = None,
) -> dict:
    """
    Generate a single-day meal plan with breakfast, lunch, and dinner.

    Args:
        time_frame: Must be 'day' for a daily plan.
        target_calories: Target total calories for the day.
        diet: Diet label to follow (e.g. 'vegetarian', 'vegan', 'ketogenic',
              'gluten free', 'paleo').
        exclude: Comma-separated ingredients or food groups to exclude
                 (e.g. 'shellfish,olives').

    Returns:
        dict with 'meals' list (breakfast, lunch, dinner) and 'nutrients' summary.
    """
    return _get("/mealplanner/generate", {
        "timeFrame": time_frame,
        "targetCalories": target_calories,
        "diet": diet,
        "exclude": exclude,
    })


def generate_meal_plan_weekly(
    target_calories: float = None,
    diet: str = None,
    exclude: str = None,
) -> dict:
    """
    Generate a full week meal plan (7 days × 3 meals).

    Args:
        target_calories: Target total calories per day.
        diet: Diet label (e.g. 'vegetarian', 'vegan', 'ketogenic', 'paleo').
        exclude: Comma-separated ingredients or food groups to exclude.

    Returns:
        dict with 'week' containing daily meal plans and nutrient summaries.
    """
    return _get("/mealplanner/generate", {
        "timeFrame": "week",
        "targetCalories": target_calories,
        "diet": diet,
        "exclude": exclude,
    })


# ---------------------------------------------------------------------------
# User Meal Plan (requires Spoonacular user account / connect)
# ---------------------------------------------------------------------------

def get_meal_plan_week(
    username: str,
    start_date: str,
    hash: str,
) -> dict:
    """
    Get a user's meal plan for a specific week.

    Args:
        username: Spoonacular username.
        start_date: Start date of the week in 'YYYY-MM-DD' format (must be a Monday).
        hash: User-specific hash for authentication.

    Returns:
        dict with the user's meal plan for the requested week.
    """
    return _get(f"/mealplanner/{username}/week/{start_date}", {"hash": hash})


def get_meal_plan_day(
    username: str,
    date: str,
    hash: str,
) -> dict:
    """
    Get a user's meal plan for a specific day.

    Args:
        username: Spoonacular username.
        date: Date in 'YYYY-MM-DD' format.
        hash: User-specific hash for authentication.

    Returns:
        dict with the user's meal plan for the requested day.
    """
    return _get(f"/mealplanner/{username}/day/{date}", {"hash": hash})


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
        slot: Meal slot — 1 = breakfast, 2 = lunch, 3 = dinner.
        position: Position within the slot (0-indexed).
        item_type: Type of item: 'RECIPE', 'PRODUCT', or 'CUSTOM_FOOD'.
        value: Item value dict, e.g. {'id': 715538, 'servings': 2, 'title': 'Pasta'}.

    Returns:
        dict with the created meal plan item details.
    """
    return _post_json(
        f"/mealplanner/{username}/items",
        {
            "date": date,
            "slot": slot,
            "position": position,
            "type": item_type,
            "value": value,
        },
        params={"hash": hash},
    )


def delete_meal_plan_item(
    username: str,
    item_id: int,
    hash: str,
) -> dict:
    """
    Delete an item from a user's meal plan.

    Args:
        username: Spoonacular username.
        item_id: ID of the meal plan item to delete.
        hash: User-specific hash for authentication.

    Returns:
        dict with deletion status.
    """
    try:
        key = _api_key()
    except ValueError as exc:
        return {"error": str(exc)}
    try:
        resp = requests.delete(
            f"{BASE_URL}/mealplanner/{username}/items/{item_id}",
            params={"apiKey": key, "hash": hash},
            timeout=15,
        )
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as exc:
        return {"error": f"HTTP {exc.response.status_code}: {exc.response.text}"}
    except Exception as exc:
        return {"error": str(exc)}


def get_meal_plan_templates(username: str, hash: str) -> dict:
    """
    Get all meal plan templates for a user.

    Args:
        username: Spoonacular username.
        hash: User-specific hash for authentication.

    Returns:
        dict with list of meal plan templates.
    """
    return _get(f"/mealplanner/{username}/templates", {"hash": hash})


# ---------------------------------------------------------------------------
# Shopping List
# ---------------------------------------------------------------------------

def get_shopping_list(username: str, hash: str) -> dict:
    """
    Get the current shopping list for a user.

    Args:
        username: Spoonacular username.
        hash: User-specific hash for authentication.

    Returns:
        dict with shopping list items grouped by aisle.
    """
    return _get(f"/mealplanner/{username}/shopping-list", {"hash": hash})


def add_to_shopping_list(
    username: str,
    hash: str,
    item: str,
    aisle: str = None,
    parse: bool = True,
) -> dict:
    """
    Add an item to a user's shopping list.

    Args:
        username: Spoonacular username.
        hash: User-specific hash for authentication.
        item: Item string to add (e.g. '1 cup of milk', '2 apples').
        aisle: Aisle category for the item (e.g. 'Dairy', 'Produce').
        parse: Attempt to parse the item string into structured data when True.

    Returns:
        dict with the added shopping list item.
    """
    return _post_json(
        f"/mealplanner/{username}/shopping-list/items",
        {"item": item, "aisle": aisle, "parse": parse},
        params={"hash": hash},
    )


def delete_from_shopping_list(
    username: str,
    item_id: int,
    hash: str,
) -> dict:
    """
    Delete an item from a user's shopping list.

    Args:
        username: Spoonacular username.
        item_id: ID of the shopping list item to delete.
        hash: User-specific hash for authentication.

    Returns:
        dict with deletion status.
    """
    try:
        key = _api_key()
    except ValueError as exc:
        return {"error": str(exc)}
    try:
        resp = requests.delete(
            f"{BASE_URL}/mealplanner/{username}/shopping-list/items/{item_id}",
            params={"apiKey": key, "hash": hash},
            timeout=15,
        )
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as exc:
        return {"error": f"HTTP {exc.response.status_code}: {exc.response.text}"}
    except Exception as exc:
        return {"error": str(exc)}


def generate_shopping_list(
    username: str,
    start_date: str,
    end_date: str,
    hash: str,
) -> dict:
    """
    Generate a shopping list from a user's meal plan for a date range.

    Args:
        username: Spoonacular username.
        start_date: Start date in 'YYYY-MM-DD' format.
        end_date: End date in 'YYYY-MM-DD' format.
        hash: User-specific hash for authentication.

    Returns:
        dict with aggregated shopping list items grouped by aisle.
    """
    return _post_json(
        f"/mealplanner/{username}/shopping-list/{start_date}/{end_date}",
        {},
        params={"hash": hash},
    )
