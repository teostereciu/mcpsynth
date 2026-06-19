from typing import Any, Optional

from .common import spoonacular_request


def search_all_food(search_query: str, offset: Optional[int] = None, number: Optional[int] = None) -> Any:
    return spoonacular_request("GET", "/food/search", params=locals())


def search_food_videos(
    search_query: str,
    type: Optional[str] = None,
    cuisine: Optional[str] = None,
    diet_type: Optional[str] = None,
    ingredients: Optional[str] = None,
    excludeIngredients: Optional[str] = None,
    minLength: Optional[int] = None,
    maxLength: Optional[int] = None,
    offset: Optional[int] = None,
    number: Optional[int] = None,
) -> Any:
    return spoonacular_request("GET", "/food/videos/search", params=locals())


def quick_answer(q: str) -> Any:
    return spoonacular_request("GET", "/recipes/quickAnswer", params=locals())


def detect_food_in_text(text: str) -> Any:
    return spoonacular_request("POST", "/food/detect", data=locals())


def search_site_content(search_query: str) -> Any:
    return spoonacular_request("GET", "/food/site/search", params=locals())


def get_random_food_joke() -> Any:
    return spoonacular_request("GET", "/food/jokes/random")


def get_random_food_trivia() -> Any:
    return spoonacular_request("GET", "/food/trivia/random")


def classify_grocery_product(title: str, upc: Optional[str] = None, plu_code: Optional[str] = None, brand: Optional[str] = None) -> Any:
    return spoonacular_request("POST", "/food/products/classify", data=locals())


def map_ingredients_to_grocery_products(ingredients: str, servings: Optional[int] = None) -> Any:
    return spoonacular_request("POST", "/food/ingredients/map", data={"ingredients": ingredients, "servings": servings})
