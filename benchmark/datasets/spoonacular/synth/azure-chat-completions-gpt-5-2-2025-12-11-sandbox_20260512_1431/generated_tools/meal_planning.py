from typing import Any, Dict, Optional

from .http_client import request_json


def mealplanner_get_week(username: str, start_date: str, hash: str) -> Dict[str, Any]:
    """GET /mealplanner/{username}/week/{start-date}"""
    return request_json(
        "GET",
        f"/mealplanner/{username}/week/{start_date}",
        params={"hash": hash},
    )


def mealplanner_get_day(username: str, date: str, hash: str) -> Dict[str, Any]:
    """GET /mealplanner/{username}/day/{date}"""
    return request_json(
        "GET",
        f"/mealplanner/{username}/day/{date}",
        params={"hash": hash},
    )


def mealplanner_generate(timeFrame: str, targetCalories: Optional[int] = None, diet: Optional[str] = None, exclude: Optional[str] = None) -> Dict[str, Any]:
    """GET /mealplanner/generate"""
    params: Dict[str, Any] = {"timeFrame": timeFrame}
    for k, v in {"targetCalories": targetCalories, "diet": diet, "exclude": exclude}.items():
        if v is not None:
            params[k] = v
    return request_json("GET", "/mealplanner/generate", params=params)


def mealplanner_add_item(username: str, hash: str, item: Dict[str, Any]) -> Dict[str, Any]:
    """POST /mealplanner/{username}/items

    item should match Spoonacular schema, e.g.
    {"date": 1589155200, "slot": 1, "position": 0, "type": "RECIPE", "value": {"id": 123, "servings": 2, "title": "..."}}
    """
    return request_json("POST", f"/mealplanner/{username}/items", params={"hash": hash}, json_body=item)


def mealplanner_clear_day(username: str, date: str, hash: str) -> Dict[str, Any]:
    """DELETE /mealplanner/{username}/day/{date}"""
    return request_json("DELETE", f"/mealplanner/{username}/day/{date}", params={"hash": hash})


def mealplanner_delete_item(username: str, id: int, hash: str) -> Dict[str, Any]:
    """DELETE /mealplanner/{username}/items/{id}"""
    return request_json("DELETE", f"/mealplanner/{username}/items/{id}", params={"hash": hash})


def mealplanner_get_templates(username: str, hash: str) -> Dict[str, Any]:
    """GET /mealplanner/{username}/templates"""
    return request_json("GET", f"/mealplanner/{username}/templates", params={"hash": hash})


def mealplanner_get_public_templates() -> Dict[str, Any]:
    """GET /mealplanner/public-templates"""
    return request_json("GET", "/mealplanner/public-templates")


def mealplanner_get_template(username: str, id: int, hash: str) -> Dict[str, Any]:
    """GET /mealplanner/{username}/templates/{id}"""
    return request_json("GET", f"/mealplanner/{username}/templates/{id}", params={"hash": hash})


def mealplanner_add_template(username: str, hash: str, template: Dict[str, Any]) -> Dict[str, Any]:
    """POST /mealplanner/{username}/templates"""
    return request_json("POST", f"/mealplanner/{username}/templates", params={"hash": hash}, json_body=template)


def mealplanner_delete_template(username: str, id: int, hash: str) -> Dict[str, Any]:
    """DELETE /mealplanner/{username}/templates/{id}"""
    return request_json("DELETE", f"/mealplanner/{username}/templates/{id}", params={"hash": hash})


def mealplanner_get_shopping_list(username: str, hash: str) -> Dict[str, Any]:
    """GET /mealplanner/{username}/shopping-list"""
    return request_json("GET", f"/mealplanner/{username}/shopping-list", params={"hash": hash})


def mealplanner_add_shopping_list_item(username: str, hash: str, item: Dict[str, Any]) -> Dict[str, Any]:
    """POST /mealplanner/{username}/shopping-list/items"""
    return request_json(
        "POST",
        f"/mealplanner/{username}/shopping-list/items",
        params={"hash": hash},
        json_body=item,
    )


def mealplanner_delete_shopping_list_item(username: str, id: int, hash: str) -> Dict[str, Any]:
    """DELETE /mealplanner/{username}/shopping-list/items/{id}"""
    return request_json("DELETE", f"/mealplanner/{username}/shopping-list/items/{id}", params={"hash": hash})


def mealplanner_generate_shopping_list(username: str, start_date: str, end_date: str, hash: str) -> Dict[str, Any]:
    """POST /mealplanner/{username}/shopping-list/{start-date}/{end-date}"""
    return request_json(
        "POST",
        f"/mealplanner/{username}/shopping-list/{start_date}/{end_date}",
        params={"hash": hash},
    )


def mealplanner_compute_shopping_list(username: str, hash: str, items: Dict[str, Any]) -> Dict[str, Any]:
    """POST /mealplanner/shopping-list/compute"""
    return request_json("POST", "/mealplanner/shopping-list/compute", params={"username": username, "hash": hash}, json_body=items)


def custom_foods_search(query: str, username: str, hash: str, number: Optional[int] = None, offset: Optional[int] = None) -> Dict[str, Any]:
    """GET /food/customFoods/search"""
    params: Dict[str, Any] = {"query": query, "username": username, "hash": hash}
    if number is not None:
        params["number"] = number
    if offset is not None:
        params["offset"] = offset
    return request_json("GET", "/food/customFoods/search", params=params)


def mealplanner_connect_user(body: Dict[str, Any]) -> Dict[str, Any]:
    """POST /users/connect

    Body example: {"username": "your-app-user", "firstName": "...", "lastName": "...", "email": "..."}
    """
    return request_json("POST", "/users/connect", json_body=body)
