from typing import Any, Dict, Optional

from .http_client import request_json


def food_search_all(query: str, number: Optional[int] = None, offset: Optional[int] = None) -> Dict[str, Any]:
    """GET /food/search"""
    params: Dict[str, Any] = {"query": query}
    if number is not None:
        params["number"] = number
    if offset is not None:
        params["offset"] = offset
    return request_json("GET", "/food/search", params=params)


def food_videos_search(
    query: str,
    type: Optional[str] = None,
    cuisine: Optional[str] = None,
    diet: Optional[str] = None,
    includeIngredients: Optional[str] = None,
    excludeIngredients: Optional[str] = None,
    minLength: Optional[int] = None,
    maxLength: Optional[int] = None,
    number: Optional[int] = None,
    offset: Optional[int] = None,
) -> Dict[str, Any]:
    """GET /food/videos/search"""
    params: Dict[str, Any] = {"query": query}
    for k, v in {
        "type": type,
        "cuisine": cuisine,
        "diet": diet,
        "includeIngredients": includeIngredients,
        "excludeIngredients": excludeIngredients,
        "minLength": minLength,
        "maxLength": maxLength,
        "number": number,
        "offset": offset,
    }.items():
        if v is not None:
            params[k] = v
    return request_json("GET", "/food/videos/search", params=params)


def recipes_quick_answer(q: str) -> Dict[str, Any]:
    """GET /recipes/quickAnswer"""
    return request_json("GET", "/recipes/quickAnswer", params={"q": q})


def food_detect(text: str) -> Dict[str, Any]:
    """POST /food/detect

    Docs specify x-www-form-urlencoded; we send JSON body.
    """
    return request_json("POST", "/food/detect", json_body={"text": text})


def food_site_search(query: str) -> Dict[str, Any]:
    """GET /food/site/search"""
    return request_json("GET", "/food/site/search", params={"query": query})


def food_joke_random() -> Dict[str, Any]:
    """GET /food/jokes/random"""
    return request_json("GET", "/food/jokes/random")


def food_trivia_random() -> Dict[str, Any]:
    """GET /food/trivia/random"""
    return request_json("GET", "/food/trivia/random")


def food_converse(text: str, contextId: Optional[str] = None) -> Dict[str, Any]:
    """GET /food/converse"""
    params: Dict[str, Any] = {"text": text}
    if contextId is not None:
        params["contextId"] = contextId
    return request_json("GET", "/food/converse", params=params)


def food_converse_suggest(query: str, number: Optional[int] = None) -> Dict[str, Any]:
    """GET /food/converse/suggest"""
    params: Dict[str, Any] = {"query": query}
    if number is not None:
        params["number"] = number
    return request_json("GET", "/food/converse/suggest", params=params)


def recipes_nutrition_label(id: int, showOptionalNutrients: Optional[bool] = None, showZeroValues: Optional[bool] = None, showIngredients: Optional[bool] = None) -> Dict[str, Any]:
    """GET /recipes/{id}/nutritionLabel (HTML)"""
    params: Dict[str, Any] = {}
    for k, v in {
        "showOptionalNutrients": showOptionalNutrients,
        "showZeroValues": showZeroValues,
        "showIngredients": showIngredients,
    }.items():
        if v is not None:
            params[k] = v
    return request_json("GET", f"/recipes/{id}/nutritionLabel", params=params)


def recipes_visualize_nutrition(body: Dict[str, Any]) -> Dict[str, Any]:
    """POST /recipes/visualizeNutrition (HTML)"""
    return request_json("POST", "/recipes/visualizeNutrition", json_body=body)
