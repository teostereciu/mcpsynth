"""
Spoonacular Miscellaneous API tools.
Endpoints covered:
  - GET  /food/search
  - GET  /food/videos/search
  - GET  /recipes/quickAnswer
  - POST /food/detect
  - GET  /food/site/search
  - GET  /food/jokes/random
  - GET  /food/trivia/random
  - GET  /food/converse
  - GET  /food/converse/suggest
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
    params["apiKey"] = _api_key()
    try:
        resp = requests.get(f"{BASE_URL}{path}", params=params, timeout=15)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def _post(path: str, params: dict, data: dict) -> dict:
    params["apiKey"] = _api_key()
    try:
        resp = requests.post(f"{BASE_URL}{path}", params=params, data=data, timeout=15)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def search_all_food(
    search_query: str,
    offset: int = 0,
    number: int = 10,
) -> dict:
    """Search all food content in one call: recipes, grocery products, menu items, ingredients, and videos."""
    params: dict = {"search_query": search_query, "offset": offset, "number": number}
    return _get("/food/search", params)


def search_food_videos(
    search_query: str,
    type: Optional[str] = None,
    cuisine: Optional[str] = None,
    diet_type: Optional[str] = None,
    ingredients: Optional[str] = None,
    exclude_ingredients: Optional[str] = None,
    min_length: Optional[float] = None,
    max_length: Optional[float] = None,
    offset: int = 0,
    number: int = 10,
) -> dict:
    """Find recipe and food-related YouTube videos. Supports filtering by type, cuisine, diet, and ingredients."""
    params: dict = {"search_query": search_query, "offset": offset, "number": number}
    if type is not None:
        params["type"] = type
    if cuisine is not None:
        params["cuisine"] = cuisine
    if diet_type is not None:
        params["diet_type"] = diet_type
    if ingredients is not None:
        params["ingredients"] = ingredients
    if exclude_ingredients is not None:
        params["excludeIngredients"] = exclude_ingredients
    if min_length is not None:
        params["minLength"] = min_length
    if max_length is not None:
        params["maxLength"] = max_length
    return _get("/food/videos/search", params)


def quick_answer(q: str) -> dict:
    """Answer a nutrition-related natural language question.
    E.g. 'How much vitamin C is in 2 apples?'"""
    return _get("/recipes/quickAnswer", {"q": q})


def detect_food_in_text(text: str) -> dict:
    """Detect and extract all food mentions (dishes and ingredients) from a block of text using NER."""
    return _post("/food/detect", {}, {"text": text})


def search_site_content(search_query: str) -> dict:
    """Search spoonacular's site content (recipes, articles, products, menu items). Supports partial queries."""
    return _get("/food/site/search", {"search_query": search_query})


def get_random_food_joke() -> dict:
    """Get a random food-related joke."""
    return _get("/food/jokes/random", {})


def get_random_food_trivia() -> dict:
    """Get a random food trivia fact."""
    return _get("/food/trivia/random", {})


def talk_to_chatbot(
    text: str,
    context_id: Optional[str] = None,
) -> dict:
    """Talk to the spoonacular chatbot about food and recipes.
    context_id: pass the context ID from a previous response to maintain conversation context."""
    params: dict = {"text": text}
    if context_id is not None:
        params["contextId"] = context_id
    return _get("/food/converse", params)


def get_conversation_suggests(
    query: str,
    number: Optional[float] = None,
) -> dict:
    """Get conversation suggestions for the spoonacular chatbot based on a partial query."""
    params: dict = {"query": query}
    if number is not None:
        params["number"] = number
    return _get("/food/converse/suggest", params)
