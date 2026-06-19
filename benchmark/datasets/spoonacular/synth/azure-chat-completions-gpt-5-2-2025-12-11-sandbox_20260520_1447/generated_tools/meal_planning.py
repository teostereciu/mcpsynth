from typing import Any, Dict, Optional

from .http_client import request_json


def get_meal_plan_week(username: str, start_date: str, hash: str) -> Any:
    """GET /mealplanner/{username}/week/{start-date}"""
    return request_json("GET", f"/mealplanner/{username}/week/{start_date}", params={"hash": hash})


def get_meal_plan_day(username: str, date: str, hash: str) -> Any:
    """GET /mealplanner/{username}/day/{date}"""
    return request_json("GET", f"/mealplanner/{username}/day/{date}", params={"hash": hash})


def generate_meal_plan(
    timeFrame: str,
    targetCalories: Optional[int] = None,
    diet: Optional[str] = None,
    exclude: Optional[str] = None,
) -> Any:
    """GET /mealplanner/generate"""
    params: Dict[str, Any] = {
        "timeFrame": timeFrame,
        "targetCalories": targetCalories,
        "diet": diet,
        "exclude": exclude,
    }
    return request_json("GET", "/mealplanner/generate", params=params)


def add_to_meal_plan(username: str, hash: str, body: Dict[str, Any]) -> Any:
    """POST /mealplanner/{username}/items"""
    return request_json("POST", f"/mealplanner/{username}/items", params={"hash": hash}, json_body=body)


def clear_meal_plan_day(username: str, date: str, hash: str) -> Any:
    """DELETE /mealplanner/{username}/day/{date}

    Docs show this under 'Clear Meal Plan Day'.
    """
    return request_json("DELETE", f"/mealplanner/{username}/day/{date}", params={"hash": hash})


def delete_from_meal_plan(username: str, id: int, hash: str) -> Any:
    """DELETE /mealplanner/{username}/items/{id}"""
    return request_json("DELETE", f"/mealplanner/{username}/items/{id}", params={"hash": hash})


def get_meal_plan_templates(username: Optional[str] = None, hash: Optional[str] = None) -> Any:
    """GET /mealplanner/{username}/templates OR GET /mealplanner/public-templates

    If username/hash are provided, fetch user templates; otherwise fetch public templates.
    """
    if username and hash:
        return request_json("GET", f"/mealplanner/{username}/templates", params={"hash": hash})
    return request_json("GET", "/mealplanner/public-templates")


def get_meal_plan_template(username: str, id: int, hash: str) -> Any:
    """GET /mealplanner/{username}/templates/{id}"""
    return request_json("GET", f"/mealplanner/{username}/templates/{id}", params={"hash": hash})


def add_meal_plan_template(username: str, hash: str, body: Dict[str, Any]) -> Any:
    """POST /mealplanner/{username}/templates"""
    return request_json("POST", f"/mealplanner/{username}/templates", params={"hash": hash}, json_body=body)


def delete_meal_plan_template(username: str, id: int, hash: str) -> Any:
    """DELETE /mealplanner/{username}/templates/{id}"""
    return request_json("DELETE", f"/mealplanner/{username}/templates/{id}", params={"hash": hash})


def get_shopping_list(username: str, hash: str) -> Any:
    """GET /mealplanner/{username}/shopping-list"""
    return request_json("GET", f"/mealplanner/{username}/shopping-list", params={"hash": hash})


def add_to_shopping_list(username: str, hash: str, body: Dict[str, Any]) -> Any:
    """POST /mealplanner/{username}/shopping-list/items"""
    return request_json(
        "POST",
        f"/mealplanner/{username}/shopping-list/items",
        params={"hash": hash},
        json_body=body,
    )


def delete_from_shopping_list(username: str, id: int, hash: str) -> Any:
    """DELETE /mealplanner/{username}/shopping-list/items/{id}"""
    return request_json("DELETE", f"/mealplanner/{username}/shopping-list/items/{id}", params={"hash": hash})


def generate_shopping_list(username: str, start_date: str, end_date: str, hash: str) -> Any:
    """POST /mealplanner/{username}/shopping-list/{start-date}/{end-date}"""
    return request_json(
        "POST",
        f"/mealplanner/{username}/shopping-list/{start_date}/{end_date}",
        params={"hash": hash},
    )


def compute_shopping_list(body: Dict[str, Any]) -> Any:
    """POST /mealplanner/shopping-list/compute"""
    return request_json("POST", "/mealplanner/shopping-list/compute", json_body=body)


def search_custom_foods(query: str, username: str, hash: str, offset: Optional[int] = None, number: Optional[int] = None) -> Any:
    """GET /food/customFoods/search"""
    params: Dict[str, Any] = {"query": query, "username": username, "hash": hash, "offset": offset, "number": number}
    return request_json("GET", "/food/customFoods/search", params=params)


def connect_user(body: Dict[str, Any]) -> Any:
    """POST /users/connect

    Docs: Connect User.
    """
    return request_json("POST", "/users/connect", json_body=body)
