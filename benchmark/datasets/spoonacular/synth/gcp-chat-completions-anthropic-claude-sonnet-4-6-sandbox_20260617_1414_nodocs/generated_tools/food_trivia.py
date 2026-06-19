"""
Spoonacular miscellaneous tools — food trivia, jokes, food detection in text,
cuisine classification, dish type detection, and unit conversion.
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
    params = {k: v for k, v in params.items() if v is not None}
    params["apiKey"] = _api_key()
    try:
        resp = requests.get(f"{BASE_URL}{path}", params=params, timeout=15)
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as exc:
        return {"error": f"HTTP {exc.response.status_code}: {exc.response.text}"}
    except Exception as exc:
        return {"error": str(exc)}


def _post_form(path: str, data: dict, params: dict = None) -> dict | list:
    if params is None:
        params = {}
    params = {k: v for k, v in params.items() if v is not None}
    data = {k: v for k, v in data.items() if v is not None}
    try:
        params["apiKey"] = _api_key()
    except ValueError as exc:
        return {"error": str(exc)}
    try:
        resp = requests.post(
            f"{BASE_URL}{path}", params=params, data=data, timeout=15
        )
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
        dict with a 'text' field containing the trivia fact.
    """
    return _get("/food/trivia/random", {})


def get_random_food_joke() -> dict:
    """
    Get a random food-related joke.

    Returns:
        dict with a 'text' field containing the joke.
    """
    return _get("/food/jokes/random", {})


def detect_food_in_text(text: str) -> dict:
    """
    Detect and extract food items mentioned in a block of text using NLP.

    Args:
        text: Free-form text that may contain food mentions
              (e.g. 'I had pizza and a coke for lunch').

    Returns:
        dict with 'annotations' list of detected food items with their
        positions in the text and Spoonacular IDs.
    """
    return _post_form("/food/detect", {"text": text})


def classify_cuisine(
    title: str,
    ingredient_list: str = None,
) -> dict:
    """
    Classify the cuisine of a recipe based on its title and optionally its
    ingredient list.

    Args:
        title: Recipe title (e.g. 'Pad Thai', 'Beef Tacos').
        ingredient_list: Newline-separated ingredient strings to improve accuracy.

    Returns:
        dict with 'cuisine' (primary classification) and 'cuisines' list
        with confidence scores.
    """
    return _post_form("/recipes/cuisine", {
        "title": title,
        "ingredientList": ingredient_list,
    })


def classify_grocery_product(
    title: str,
    upc: str = None,
) -> dict:
    """
    Classify a grocery product into a category based on its title or UPC barcode.

    Args:
        title: Product title (e.g. 'Organic Whole Milk').
        upc: UPC barcode string (optional, improves accuracy).

    Returns:
        dict with 'cleanTitle', 'image', 'category', 'breadcrumbs', and
        'usdaCode'.
    """
    return _post_form("/food/products/classify", {
        "title": title,
        "upc": upc,
    })


def search_food_videos(
    query: str,
    type: str = None,
    cuisine: str = None,
    diet: str = None,
    include_ingredients: str = None,
    exclude_ingredients: str = None,
    min_length: float = None,
    max_length: float = None,
    offset: int = None,
    number: int = 10,
) -> dict:
    """
    Search for food-related videos on Spoonacular.

    Args:
        query: Search query (e.g. 'how to make pasta').
        type: Meal type filter (e.g. 'main course', 'dessert').
        cuisine: Cuisine filter (e.g. 'italian').
        diet: Diet filter (e.g. 'vegetarian').
        include_ingredients: Comma-separated ingredients to include.
        exclude_ingredients: Comma-separated ingredients to exclude.
        min_length: Minimum video length in seconds.
        max_length: Maximum video length in seconds.
        offset: Pagination offset.
        number: Number of results (default 10).

    Returns:
        dict with 'videos' list and 'totalResults'.
    """
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


def get_random_food_videos(
    tags: str = None,
    number: int = 10,
) -> dict:
    """
    Get random food-related videos, optionally filtered by tags.

    Args:
        tags: Comma-separated tags to filter videos (e.g. 'italian,pasta').
        number: Number of videos to return (default 10).

    Returns:
        dict with 'videos' list.
    """
    return _get("/food/videos/random", {"tags": tags, "number": number})


def search_site_content(query: str) -> dict:
    """
    Search across all Spoonacular content types (recipes, grocery products,
    menu items) in a single call.

    Args:
        query: Search query string.

    Returns:
        dict with 'recipes', 'groceryProducts', and 'menuItems' result lists.
    """
    return _get("/food/site/search", {"query": query})


def talk_to_chatbot(
    text: str,
    context_id: str = None,
) -> dict:
    """
    Interact with the Spoonacular food chatbot for conversational food queries.

    Args:
        text: User message to send to the chatbot
              (e.g. 'What can I make with chicken and rice?').
        context_id: Conversation context ID to maintain multi-turn dialogue.

    Returns:
        dict with 'answerText', 'media', and 'contextId' for follow-up turns.
    """
    return _get("/food/converse", {"text": text, "contextId": context_id})
