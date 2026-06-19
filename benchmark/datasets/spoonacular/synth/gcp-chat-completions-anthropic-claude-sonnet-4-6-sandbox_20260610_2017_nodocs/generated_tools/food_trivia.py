"""
Spoonacular miscellaneous tools — food trivia, jokes, food detection in text,
dish classification, and cuisine classification.
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
    try:
        resp = requests.get(url, params=params, timeout=15)
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as exc:
        return {"error": f"HTTP {exc.response.status_code}: {exc.response.text}"}
    except Exception as exc:
        return {"error": str(exc)}


def _post(path: str, data: dict) -> dict | list:
    params = {"apiKey": _api_key()}
    url = f"{BASE_URL}{path}"
    try:
        resp = requests.post(url, params=params, data=data, timeout=15)
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as exc:
        return {"error": f"HTTP {exc.response.status_code}: {exc.response.text}"}
    except Exception as exc:
        return {"error": str(exc)}


def get_random_food_trivia() -> dict:
    """
    Get a random food trivia fact.

    Returns:
        dict with 'text' containing the trivia fact.
    """
    return _get("/food/trivia/random", {})


def get_random_food_joke() -> dict:
    """
    Get a random food-related joke.

    Returns:
        dict with 'text' containing the joke.
    """
    return _get("/food/jokes/random", {})


def detect_food_in_text(text: str) -> dict:
    """
    Detect food items mentioned in a piece of text using NLP.

    Args:
        text: Any text that may contain food mentions
              (e.g. "I had pizza and a coke for lunch").

    Returns:
        dict with 'annotations' list of detected food items with positions.
    """
    return _post("/food/detect", {"text": text})


def classify_cuisine(
    title: str,
    ingredient_list: str = "",
    language: str = "en",
) -> dict:
    """
    Classify the cuisine of a recipe based on its title and/or ingredients.

    Args:
        title: Recipe title (e.g. "Spaghetti Carbonara").
        ingredient_list: Newline-separated ingredient strings (optional).
        language: Language of the input ("en" or "de").

    Returns:
        dict with 'cuisine' (top prediction) and 'cuisines' list with
        confidence scores.
    """
    data: dict = {"title": title, "language": language}
    if ingredient_list:
        data["ingredientList"] = ingredient_list
    return _post("/recipes/cuisine", data)


def classify_grocery_product(
    title: str,
    upc: str = "",
    plu_code: str = "",
) -> dict:
    """
    Classify a grocery product into a category.

    Args:
        title: Product title (e.g. "Organic Whole Milk").
        upc: UPC barcode (optional).
        plu_code: PLU code (optional).

    Returns:
        dict with 'cleanTitle', 'category', 'probabilities', and 'breadcrumbs'.
    """
    data: dict = {"title": title}
    if upc:
        data["upc"] = upc
    if plu_code:
        data["pluCode"] = plu_code
    return _post("/food/products/classify", data)


def search_all_food(
    query: str,
    offset: int = 0,
    number: int = 10,
) -> dict:
    """
    Search across all Spoonacular food databases at once: recipes, grocery
    products, menu items, and ingredients.

    Args:
        query: Search term.
        offset: Pagination offset.
        number: Number of results per category.

    Returns:
        dict with results grouped by category (recipes, groceryProducts,
        menuItems, ingredients).
    """
    params = {"query": query, "offset": offset, "number": number}
    return _get("/food/search", params)


def get_conversation_suggests(query: str, number: int = 5) -> dict:
    """
    Get conversation suggestions for a food-related chatbot query.
    Useful for building food-related conversational agents.

    Args:
        query: Partial user query or intent.
        number: Number of suggestions to return.

    Returns:
        dict with 'suggests' list.
    """
    return _get("/food/converse/suggest", {"query": query, "number": number})


def talk_to_chatbot(text: str, context_id: str = "") -> dict:
    """
    Send a message to the Spoonacular food chatbot and get a response.

    Args:
        text: User message (e.g. "What can I cook with chicken and rice?").
        context_id: Conversation context ID for multi-turn conversations.
                    Leave empty to start a new conversation.

    Returns:
        dict with 'answerText', 'media', and 'contextId' for follow-up turns.
    """
    params: dict = {"text": text}
    if context_id:
        params["contextId"] = context_id
    return _get("/food/converse", params)
