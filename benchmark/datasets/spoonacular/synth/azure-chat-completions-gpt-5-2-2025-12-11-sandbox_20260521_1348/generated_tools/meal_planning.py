from typing import Any, Dict, Optional

from .http_client import request_json


def get_meal_plan_week(*, username: str, start_date: str, hash: str) -> Any:
    """GET /mealplanner/{username}/week/{start-date}"""
    return request_json("GET", f"/mealplanner/{username}/week/{start_date}", params={"hash": hash})


def get_meal_plan_day(*, username: str, date: str, hash: str) -> Any:
    """GET /mealplanner/{username}/day/{date}"""
    return request_json("GET", f"/mealplanner/{username}/day/{date}", params={"hash": hash})


def generate_meal_plan(
    *,
    timeFrame: str,
    targetCalories: Optional[float] = None,
    diet: Optional[str] = None,
    exclude: Optional[str] = None,
) -> Any:
    """GET /mealplanner/generate"""
    params: Dict[str, Any] = {k: v for k, v in {"timeFrame": timeFrame, "targetCalories": targetCalories, "diet": diet, "exclude": exclude}.items() if v is not None}
    return request_json("GET", "/mealplanner/generate", params=params)


def add_to_meal_plan(*, username: str, hash: str, date: str, slot: int, position: int, type: str, value: Dict[str, Any]) -> Any:
    """POST /mealplanner/{username}/items"""
    body = {"date": date, "slot": slot, "position": position, "type": type, "value": value}
    return request_json("POST", f"/mealplanner/{username}/items", params={"hash": hash}, json=body)


def clear_meal_plan_day(*, username: str, date: str, hash: str) -> Any:
    """DELETE /mealplanner/{username}/day/{date}"""
    return request_json("DELETE", f"/mealplanner/{username}/day/{date}", params={"hash": hash})


def delete_from_meal_plan(*, username: str, id: int, hash: str) -> Any:
    """DELETE /mealplanner/{username}/items/{id}"""
    return request_json("DELETE", f"/mealplanner/{username}/items/{id}", params={"hash": hash})


def get_meal_plan_templates(*, username: str, hash: str) -> Any:
    """GET /mealplanner/{username}/templates"""
    return request_json("GET", f"/mealplanner/{username}/templates", params={"hash": hash})


def get_meal_plan_template(*, username: str, id: int, hash: str) -> Any:
    """GET /mealplanner/{username}/templates/{id}"""
    return request_json("GET", f"/mealplanner/{username}/templates/{id}", params={"hash": hash})


def add_meal_plan_template(*, username: str, hash: str, name: str) -> Any:
    """POST /mealplanner/{username}/templates"""
    body = {"name": name}
    return request_json("POST", f"/mealplanner/{username}/templates", params={"hash": hash}, json=body)


def delete_meal_plan_template(*, username: str, id: int, hash: str) -> Any:
    """DELETE /mealplanner/{username}/templates/{id}"""
    return request_json("DELETE", f"/mealplanner/{username}/templates/{id}", params={"hash": hash})


def get_shopping_list(*, username: str, hash: str) -> Any:
    """GET /mealplanner/{username}/shopping-list"""
    return request_json("GET", f"/mealplanner/{username}/shopping-list", params={"hash": hash})


def add_to_shopping_list(*, username: str, hash: str, item: str, aisle: Optional[str] = None, parse: Optional[bool] = None) -> Any:
    """POST /mealplanner/{username}/shopping-list/items"""
    body: Dict[str, Any] = {k: v for k, v in {"item": item, "aisle": aisle, "parse": parse}.items() if v is not None}
    return request_json("POST", f"/mealplanner/{username}/shopping-list/items", params={"hash": hash}, json=body)


def delete_from_shopping_list(*, username: str, id: int, hash: str) -> Any:
    """DELETE /mealplanner/{username}/shopping-list/items/{id}"""
    return request_json("DELETE", f"/mealplanner/{username}/shopping-list/items/{id}", params={"hash": hash})


def generate_shopping_list(*, username: str, start_date: str, end_date: str, hash: str) -> Any:
    """POST /mealplanner/{username}/shopping-list/{start-date}/{end-date}"""
    return request_json(
        "POST",
        f"/mealplanner/{username}/shopping-list/{start_date}/{end_date}",
        params={"hash": hash},
    )


def search_custom_foods(*, query: str, username: str, hash: str) -> Any:
    """GET /mealplanner/{username}/foods/search"""
    return request_json("GET", f"/mealplanner/{username}/foods/search", params={"hash": hash, "query": query})


def connect_user(*, username: str, firstName: Optional[str] = None, lastName: Optional[str] = None, email: Optional[str] = None) -> Any:
    """POST /users/connect"""
    body: Dict[str, Any] = {k: v for k, v in {"username": username, "firstName": firstName, "lastName": lastName, "email": email}.items() if v is not None}
    return request_json("POST", "/users/connect", json=body)
