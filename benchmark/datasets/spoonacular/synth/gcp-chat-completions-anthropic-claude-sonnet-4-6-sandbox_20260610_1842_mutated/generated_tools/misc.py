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
    params = {k: v for k, v in params.items() if v is not None}
    params["apiKey"] = _api_key()
    try:
        resp = requests.get(f"{BASE_URL}{path}", params=params, timeout=15)
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


def _post_form(path: str, data: dict, params: dict | None = None) -> dict:
    if params is None:
        params = {}
    params = {k: v for k, v in params.items() if v is not None}
    params["apiKey"] = _api_key()
    data = {k: v for k, v in data.items() if v is not None}
    try:
        resp = requests.post(
            f"{BASE_URL}{path}",
            data=data,
            params=params,
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            timeout=15,
        )
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


# ---------------------------------------------------------------------------
# Search All Food
# ---------------------------------------------------------------------------

def search_all_food(
    query: str,
    offset: Optional[int] = None,
    number: Optional[int] = None,
) -> dict:
    """Search all food content: recipes, grocery products, menu items, ingredients, and videos."""
    return _get("/food/search", {
        "query": query,
        "offset": offset,
        "number": number,
    })


# ---------------------------------------------------------------------------
# Search Food Videos
# ---------------------------------------------------------------------------

def search_food_videos(
    query: str,
    type: Optional[str] = None,
    cuisine: Optional[str] = None,
    diet: Optional[str] = None,
    include_ingredients: Optional[str] = None,
    exclude_ingredients: Optional[str] = None,
    min_length: Optional[int] = None,
    max_length: Optional[int] = None,
    offset: Optional[int] = None,
    number: Optional[int] = None,
) -> dict:
    """Find recipe and food-related videos on YouTube."""
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


# ---------------------------------------------------------------------------
# Quick Answer
# ---------------------------------------------------------------------------

def quick_answer(question: str) -> dict:
    """Answer a nutrition-related natural language question (e.g. 'How much vitamin C is in 2 apples?')."""
    return _get("/recipes/quickAnswer", {"q": question})


# ---------------------------------------------------------------------------
# Detect Food in Text
# ---------------------------------------------------------------------------

def detect_food_in_text(text: str) -> dict:
    """Detect all mentions of food (dishes and ingredients) in a given text using NER."""
    return _post_form("/food/detect", {"text": text})


# ---------------------------------------------------------------------------
# Search Site Content
# ---------------------------------------------------------------------------

def search_site_content(query: str) -> dict:
    """Search spoonacular's site content (recipes, articles, products, menu items). Supports partial queries."""
    return _get("/food/site/search", {"query": query})


# ---------------------------------------------------------------------------
# Random Food Joke
# ---------------------------------------------------------------------------

def get_random_food_joke() -> dict:
    """Get a random food-related joke."""
    return _get("/food/jokes/random", {})


# ---------------------------------------------------------------------------
# Random Food Trivia
# ---------------------------------------------------------------------------

def get_random_food_trivia() -> dict:
    """Get a random food trivia fact."""
    return _get("/food/trivia/random", {})


# ---------------------------------------------------------------------------
# Talk to Chatbot
# ---------------------------------------------------------------------------

def talk_to_chatbot(
    text: str,
    context_id: Optional[str] = None,
) -> dict:
    """Have a conversation about food with the spoonacular chatbot."""
    return _get("/food/converse", {
        "text": text,
        "contextId": context_id,
    })


# ---------------------------------------------------------------------------
# Conversation Suggests
# ---------------------------------------------------------------------------

def get_conversation_suggests(
    query: str,
    number: Optional[float] = None,
) -> dict:
    """Get suggestions for what a user can say or ask the spoonacular chatbot."""
    return _get("/food/converse/suggest", {
        "query": query,
        "number": number,
    })
