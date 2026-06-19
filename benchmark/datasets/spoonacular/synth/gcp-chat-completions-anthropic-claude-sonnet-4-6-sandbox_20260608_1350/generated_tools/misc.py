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


def _get(path: str, params: dict) -> dict | list:
    params = {k: v for k, v in params.items() if v is not None}
    params["apiKey"] = _api_key()
    try:
        r = requests.get(f"{BASE_URL}{path}", params=params, timeout=30)
        r.raise_for_status()
        return r.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": e.response.status_code if e.response else None}
    except Exception as e:
        return {"error": str(e)}


def _post_form(path: str, params: dict, data: dict) -> dict | list:
    params = {k: v for k, v in params.items() if v is not None}
    params["apiKey"] = _api_key()
    data = {k: v for k, v in data.items() if v is not None}
    try:
        r = requests.post(f"{BASE_URL}{path}", params=params, data=data, timeout=30)
        r.raise_for_status()
        return r.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": e.response.status_code if e.response else None}
    except Exception as e:
        return {"error": str(e)}


def search_all_food(
    query: str,
    offset: Optional[int] = None,
    number: Optional[int] = None,
) -> dict:
    """Search all food content in one call: recipes, grocery products, menu items, ingredients, and videos."""
    return _get("/food/search", {
        "query": query,
        "offset": offset,
        "number": number,
    })


def search_food_videos(
    query: str,
    type: Optional[str] = None,
    cuisine: Optional[str] = None,
    diet: Optional[str] = None,
    include_ingredients: Optional[str] = None,
    exclude_ingredients: Optional[str] = None,
    min_length: Optional[float] = None,
    max_length: Optional[float] = None,
    offset: Optional[int] = None,
    number: Optional[int] = None,
) -> dict:
    """Search for food and recipe related YouTube videos."""
    return _get("/food/videos/search", {
        "query": query,
        "type": type,
        "cuisine": cuisine,
        "diet": diet,
        "includeIngredients": include_ingredients,
        "excludeIngredients": exclude_ingredients,
        "minLength": min_length,
        "maxLength": max_length,
        "offset": offset,
        "number": number,
    })


def quick_answer(q: str) -> dict:
    """Answer a nutrition-related natural language question.
    E.g. 'How much vitamin C is in 2 apples?'"""
    return _get("/recipes/quickAnswer", {"q": q})


def detect_food_in_text(text: str) -> dict:
    """Detect all food mentions (dishes and ingredients) in a given text using Named Entity Recognition."""
    return _post_form("/food/detect", {}, {"text": text})


def search_site_content(query: str) -> dict:
    """Search spoonacular's site content (recipes, articles, grocery products, menu items).
    Supports partial queries for autocomplete-style search."""
    return _get("/food/site/search", {"query": query})


def get_random_food_joke() -> dict:
    """Get a random food-related joke."""
    return _get("/food/jokes/random", {})


def get_random_food_trivia() -> dict:
    """Get a random food trivia fact."""
    return _get("/food/trivia/random", {})


def talk_to_chatbot(text: str, context_id: Optional[str] = None) -> dict:
    """Have a conversation about food with the spoonacular chatbot.
    context_id: pass the context_id from a previous response to maintain conversation context."""
    return _get("/food/converse", {
        "text": text,
        "contextId": context_id,
    })


def conversation_suggests(query: str, number: Optional[float] = None) -> dict:
    """Get suggestions for things a user can say or ask the spoonacular chatbot."""
    return _get("/food/converse/suggest", {
        "query": query,
        "number": number,
    })
