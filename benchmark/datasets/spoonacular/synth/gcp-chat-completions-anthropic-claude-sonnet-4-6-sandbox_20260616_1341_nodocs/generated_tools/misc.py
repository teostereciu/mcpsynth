"""
Spoonacular miscellaneous tools — jokes, trivia, talk, image classification.
"""
import os
import requests

BASE_URL = "https://api.spoonacular.com"


def _api_key() -> str:
    key = os.environ.get("SPOONACULAR_API_KEY", "")
    if not key:
        raise ValueError("SPOONACULAR_API_KEY environment variable is not set")
    return key


def _get(path: str, params: dict) -> dict | list:
    params["apiKey"] = _api_key()
    url = f"{BASE_URL}{path}"
    resp = requests.get(url, params=params, timeout=15)
    resp.raise_for_status()
    return resp.json()


# ---------------------------------------------------------------------------
# Food jokes
# ---------------------------------------------------------------------------

def get_random_food_joke() -> dict:
    """
    Get a random food-related joke.

    Returns:
        dict with 'text' containing the joke.
    """
    try:
        return _get("/food/jokes/random", {})
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Food trivia
# ---------------------------------------------------------------------------

def get_random_food_trivia() -> dict:
    """
    Get a random food trivia fact.

    Returns:
        dict with 'text' containing the trivia fact.
    """
    try:
        return _get("/food/trivia/random", {})
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Conversation / talk
# ---------------------------------------------------------------------------

def talk_to_chatbot(text: str, context_id: str = "") -> dict:
    """
    Talk to the Spoonacular food chatbot. It can answer food-related questions,
    find recipes, and provide cooking advice.

    Args:
        text: The message to send to the chatbot.
        context_id: Optional conversation context ID to maintain conversation state.

    Returns:
        dict with 'answerText', 'media' (optional), and 'contextId'.
    """
    try:
        params: dict = {"text": text}
        if context_id:
            params["contextId"] = context_id
        return _get("/food/converse", params)
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Image classification / analysis
# ---------------------------------------------------------------------------

def classify_food_image_by_url(image_url: str) -> dict:
    """
    Classify a food image from a URL to identify the dish or food item.

    Args:
        image_url: The URL of the food image to classify.

    Returns:
        dict with 'category', 'probability', and 'recipes' suggestions.
    """
    try:
        params = {"imageUrl": image_url}
        return _get("/food/images/classify", params)
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Search all food (recipes + grocery products + menu items)
# ---------------------------------------------------------------------------

def search_all_food(
    query: str,
    offset: int = 0,
    number: int = 10,
) -> dict:
    """
    Search across all Spoonacular food databases simultaneously: recipes,
    grocery products, and menu items.

    Args:
        query: The search query.
        offset: Pagination offset.
        number: Number of results per category.

    Returns:
        dict with 'searchResults' containing results from each category.
    """
    try:
        params = {"query": query, "offset": offset, "number": number}
        return _get("/food/search", params)
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Quick answer
# ---------------------------------------------------------------------------

def get_quick_answer(q: str) -> dict:
    """
    Get a quick answer to a simple food-related question.

    Args:
        q: A food-related question (e.g. 'How much vitamin C is in an apple?').

    Returns:
        dict with 'answer' and 'image'.
    """
    try:
        params = {"q": q}
        return _get("/recipes/quickAnswer", params)
    except Exception as exc:
        return {"error": str(exc)}
