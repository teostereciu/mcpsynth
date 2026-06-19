from typing import Any, Dict

from server import _request


def search_all_food(**params: Any) -> Dict[str, Any]:
    return _request("GET", "/food/search", params=params)


def search_food_videos(**params: Any) -> Dict[str, Any]:
    return _request("GET", "/food/videos/search", params=params)


def quick_answer(**params: Any) -> Dict[str, Any]:
    return _request("GET", "/recipes/quickAnswer", params=params)


def detect_food(**params: Any) -> Dict[str, Any]:
    return _request("POST", "/food/detect", data=params)


def search_site_content(**params: Any) -> Dict[str, Any]:
    return _request("GET", "/food/site/search", params=params)


def random_food_joke(**params: Any) -> Dict[str, Any]:
    return _request("GET", "/food/jokes/random", params=params)


def random_food_trivia(**params: Any) -> Dict[str, Any]:
    return _request("GET", "/food/trivia/random", params=params)


def talk_to_chatbot(**params: Any) -> Dict[str, Any]:
    return _request("GET", "/food/converse", params=params)


def conversation_suggests(**params: Any) -> Dict[str, Any]:
    return _request("GET", "/food/converse/suggest", params=params)
