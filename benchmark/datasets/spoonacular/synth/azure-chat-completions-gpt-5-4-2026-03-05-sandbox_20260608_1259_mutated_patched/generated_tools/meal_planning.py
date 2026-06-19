from typing import Any, Optional

from .common import spoonacular_request


def get_meal_plan_week(username: str, start_date: str, hash: str) -> Any:
    return spoonacular_request("GET", f"/mealplanner/{username}/week/{start_date}", params={"hash": hash})


def get_meal_plan_day(username: str, date: str, hash: str) -> Any:
    return spoonacular_request("GET", f"/mealplanner/{username}/day/{date}", params={"hash": hash})


def generate_meal_plan(timeFrame: Optional[str] = None, targetCalories: Optional[int] = None, diet: Optional[str] = None, exclude: Optional[str] = None) -> Any:
    return spoonacular_request("GET", "/mealplanner/generate", params=locals())


def add_to_meal_plan(username: str, hash: str, date: int, slot: int, position: int, type: str, value: str) -> Any:
    return spoonacular_request("POST", f"/mealplanner/{username}/items", params={"hash": hash}, data={"date": date, "slot": slot, "position": position, "type": type, "value": value})


def clear_meal_plan_day(username: str, date: str, hash: str) -> Any:
    return spoonacular_request("DELETE", f"/mealplanner/{username}/day/{date}", params={"hash": hash})


def delete_meal_plan_item(username: str, item_id: int, hash: str) -> Any:
    return spoonacular_request("DELETE", f"/mealplanner/{username}/items/{item_id}", params={"hash": hash})


def get_meal_plan_templates(username: str, hash: str) -> Any:
    return spoonacular_request("GET", f"/mealplanner/{username}/templates", params={"hash": hash})


def get_public_meal_plan_templates() -> Any:
    return spoonacular_request("GET", "/mealplanner/public-templates")


def get_meal_plan_template(username: str, template_id: int, hash: str) -> Any:
    return spoonacular_request("GET", f"/mealplanner/{username}/templates/{template_id}", params={"hash": hash})


def add_meal_plan_template(username: str, hash: str, name: str, items: str) -> Any:
    return spoonacular_request("POST", f"/mealplanner/{username}/templates", params={"hash": hash}, data={"name": name, "items": items})


def delete_meal_plan_template(username: str, template_id: int, hash: str) -> Any:
    return spoonacular_request("DELETE", f"/mealplanner/{username}/templates/{template_id}", params={"hash": hash})


def generate_shopping_list(username: str, start_date: str, end_date: str, hash: str) -> Any:
    return spoonacular_request("GET", f"/mealplanner/{username}/shopping-list/{start_date}/{end_date}", params={"hash": hash})


def get_shopping_list(username: str, hash: str) -> Any:
    return spoonacular_request("GET", f"/mealplanner/{username}/shopping-list", params={"hash": hash})


def add_to_shopping_list(username: str, hash: str, item: str) -> Any:
    return spoonacular_request("POST", f"/mealplanner/{username}/shopping-list/items", params={"hash": hash}, data={"item": item})


def delete_from_shopping_list(username: str, item_id: int, hash: str) -> Any:
    return spoonacular_request("DELETE", f"/mealplanner/{username}/shopping-list/items/{item_id}", params={"hash": hash})


def compute_shopping_list(items: str) -> Any:
    return spoonacular_request("POST", "/mealplanner/shopping-list/compute", data={"items": items})


def search_custom_foods(username: str, hash: str, search_query: str, number: Optional[int] = None) -> Any:
    return spoonacular_request("GET", "/food/customFoods/search", params={"username": username, "hash": hash, "query": search_query, "number": number})


def connect_user(username: str, firstName: str, lastName: str, email: str) -> Any:
    return spoonacular_request("POST", "/users/connect", data={"username": username, "firstName": firstName, "lastName": lastName, "email": email})
