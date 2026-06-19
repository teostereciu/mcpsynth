from typing import Any, Dict, Optional

from .http import request_json


def search_all_food(*, search_query: str, offset: Optional[int] = None, number: Optional[int] = None) -> Any:
    """GET /food/search"""
    params: Dict[str, Any] = {"search_query": search_query, "offset": offset, "number": number}
    return request_json("GET", "/food/search", params=params)


def search_food_videos(
    *,
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
    """GET /food/videos/search"""
    params: Dict[str, Any] = {
        "search_query": search_query,
        "type": type,
        "cuisine": cuisine,
        "diet_type": diet_type,
        "ingredients": ingredients,
        "excludeIngredients": excludeIngredients,
        "minLength": minLength,
        "maxLength": maxLength,
        "offset": offset,
        "number": number,
    }
    return request_json("GET", "/food/videos/search", params=params)


def quick_answer(*, q: str) -> Any:
    """GET /recipes/quickAnswer"""
    return request_json("GET", "/recipes/quickAnswer", params={"q": q})


def detect_food_in_text(*, text: str) -> Any:
    """POST /food/detect

    Docs specify x-www-form-urlencoded; we send as query params for simplicity.
    """
    return request_json("POST", "/food/detect", params={"text": text})


def search_site_content(*, search_query: str) -> Any:
    """GET /food/site/search"""
    return request_json("GET", "/food/site/search", params={"search_query": search_query})
