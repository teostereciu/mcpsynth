"""Spoonacular Miscellaneous API tools."""
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
        resp = requests.get(f"{BASE_URL}{path}", params=params, timeout=30)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def _post(path: str, data: dict, params: dict = None) -> dict:
    p = params or {}
    p["apiKey"] = _api_key()
    try:
        resp = requests.post(f"{BASE_URL}{path}", data=data, params=p, timeout=30)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def search_all_food(query: str, offset: int = 0, number: int = 10) -> dict:
    """Search all food content: recipes, grocery products, menu items, ingredients, and videos."""
    params = {"query": query, "offset": offset, "number": number}
    return _get("/food/search", params)


def search_food_videos(
    query: str,
    type: Optional[str] = None,
    cuisine: Optional[str] = None,
    diet: Optional[str] = None,
    ingredients: Optional[str] = None,
    exclude_ingredients: Optional[str] = None,
    min_length: Optional[float] = None,
    max_length: Optional[float] = None,
    offset: int = 0,
    number: int = 10,
) -> dict:
    """Search for food and recipe videos on YouTube."""
    params: dict = {"query": query, "offset": offset, "number": number}
    if type: params["type"] = type
    if cuisine: params["cuisine"] = cuisine
    if diet: params["diet"] = diet
    if ingredients: params["includeIngredients"] = ingredients
    if exclude_ingredients: params["excludeIngredients"] = exclude_ingredients
    if min_length is not None: params["minLength"] = min_length
    if max_length is not None: params["maxLength"] = max_length
    return _get("/food/videos/search", params)


def quick_answer(q: str) -> dict:
    """Answer a nutrition-related natural language question (e.g. 'How much vitamin C is in 2 apples?')."""
    return _get("/recipes/quickAnswer", {"q": q})


def detect_food_in_text(text: str) -> dict:
    """Detect and extract food mentions (dishes and ingredients) from any text using NER."""
    return _post("/food/detect", {"text": text})


def search_site_content(query: str) -> dict:
    """Search spoonacular's site content (recipes, articles, products, menu items) with partial queries."""
    return _get("/food/site/search", {"query": query})


def get_random_food_joke() -> dict:
    """Get a random food-related joke."""
    return _get("/food/jokes/random", {})


def get_random_food_trivia() -> dict:
    """Get a random food trivia fact."""
    return _get("/food/trivia/random", {})


def talk_to_chatbot(text: str, context_id: Optional[str] = None) -> dict:
    """Have a conversation about food with the spoonacular chatbot."""
    params: dict = {"text": text}
    if context_id:
        params["contextId"] = context_id
    return _get("/food/converse", params)


def get_conversation_suggests(query: str, number: float = 5) -> dict:
    """Get suggestions for what a user can say to the spoonacular chatbot."""
    params = {"query": query, "number": number}
    return _get("/food/converse/suggest", params)
