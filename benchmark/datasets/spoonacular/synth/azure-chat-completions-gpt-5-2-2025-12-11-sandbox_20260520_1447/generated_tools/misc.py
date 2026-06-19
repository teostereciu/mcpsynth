from typing import Any, Dict, Optional

from .http_client import request_json


def search_all_food(query: str, offset: Optional[int] = None, number: Optional[int] = None) -> Any:
    """GET /food/search"""
    return request_json("GET", "/food/search", params={"query": query, "offset": offset, "number": number})


def search_food_videos(
    query: str,
    type: Optional[str] = None,
    cuisine: Optional[str] = None,
    diet: Optional[str] = None,
    includeIngredients: Optional[str] = None,
    excludeIngredients: Optional[str] = None,
    minLength: Optional[int] = None,
    maxLength: Optional[int] = None,
    offset: Optional[int] = None,
    number: Optional[int] = None,
) -> Any:
    """GET /food/videos/search"""
    params: Dict[str, Any] = {
        "query": query,
        "type": type,
        "cuisine": cuisine,
        "diet": diet,
        "includeIngredients": includeIngredients,
        "excludeIngredients": excludeIngredients,
        "minLength": minLength,
        "maxLength": maxLength,
        "offset": offset,
        "number": number,
    }
    return request_json("GET", "/food/videos/search", params=params)


def quick_answer(q: str) -> Any:
    """GET /recipes/quickAnswer"""
    return request_json("GET", "/recipes/quickAnswer", params={"q": q})


def detect_food_in_text(text: str) -> Any:
    """POST /food/detect

    Docs specify x-www-form-urlencoded; we send as query params.
    """
    return request_json("POST", "/food/detect", params={"text": text})


def search_site_content(query: str) -> Any:
    """GET /food/site/search"""
    return request_json("GET", "/food/site/search", params={"query": query})


def random_food_joke() -> Any:
    """GET /food/jokes/random"""
    return request_json("GET", "/food/jokes/random")


def random_food_trivia() -> Any:
    """GET /food/trivia/random"""
    return request_json("GET", "/food/trivia/random")


def talk_to_chatbot(text: str, contextId: Optional[str] = None) -> Any:
    """GET /food/converse"""
    return request_json("GET", "/food/converse", params={"text": text, "contextId": contextId})


def conversation_suggest(query: str, number: Optional[int] = None) -> Any:
    """GET /food/converse/suggest"""
    return request_json("GET", "/food/converse/suggest", params={"query": query, "number": number})
