from typing import Any, Optional

from generated_tools.recipes import _request


def search_all_food(query: str, offset: Optional[int] = None, number: Optional[int] = None) -> Any:
    return _request("GET", "/food/search", locals())


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
    return _request("GET", "/food/videos/search", locals())


def quick_answer(q: str) -> Any:
    return _request("GET", "/recipes/quickAnswer", {"q": q})


def detect_food_in_text(text: str) -> Any:
    return _request("POST", "/food/detect", data={"text": text}, headers={"Content-Type": "application/x-www-form-urlencoded"})


def search_site_content(query: str) -> Any:
    return _request("GET", "/food/site/search", locals())


def random_food_joke() -> Any:
    return _request("GET", "/food/jokes/random")


def random_food_trivia() -> Any:
    return _request("GET", "/food/trivia/random")


def talk_to_chatbot(text: str, contextId: Optional[str] = None) -> Any:
    return _request("GET", "/food/converse", {"text": text, "contextId": contextId})


def conversation_suggests(query: str, number: Optional[int] = None) -> Any:
    return _request("GET", "/food/converse/suggest", locals())
