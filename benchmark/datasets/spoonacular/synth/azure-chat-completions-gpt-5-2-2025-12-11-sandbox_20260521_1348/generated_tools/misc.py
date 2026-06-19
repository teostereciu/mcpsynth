from typing import Any, Dict, Optional

from .http_client import request_json


def search_all_food(*, query: str, offset: Optional[int] = None, number: Optional[int] = None) -> Any:
    """GET /food/search"""
    params: Dict[str, Any] = {k: v for k, v in {"query": query, "offset": offset, "number": number}.items() if v is not None}
    return request_json("GET", "/food/search", params=params)


def search_food_videos(
    *,
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
        k: v
        for k, v in {
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
        }.items()
        if v is not None
    }
    return request_json("GET", "/food/videos/search", params=params)


def quick_answer(*, q: str) -> Any:
    """GET /recipes/quickAnswer"""
    return request_json("GET", "/recipes/quickAnswer", params={"q": q})


def detect_food_in_text(*, text: str) -> Any:
    """POST /food/detect (docs specify x-www-form-urlencoded; we send as query params)"""
    return request_json("POST", "/food/detect", params={"text": text})


def search_site_content(*, query: str) -> Any:
    """GET /food/site/search"""
    return request_json("GET", "/food/site/search", params={"query": query})
