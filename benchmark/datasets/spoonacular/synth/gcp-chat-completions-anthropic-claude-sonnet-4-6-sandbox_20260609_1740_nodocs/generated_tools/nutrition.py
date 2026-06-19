"""
Spoonacular Nutrition tools — analyze recipes, compute nutrition, detect diet/allergens.
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
    except requests.HTTPError as e:
        return {"error": f"HTTP {resp.status_code}: {resp.text[:300]}"}
    except Exception as e:
        return {"error": str(e)}


def get_recipe_nutrition_by_id(recipe_id: int) -> dict:
    """
    Get the full nutritional breakdown for a recipe by its Spoonacular ID,
    including calories, macros, vitamins, and minerals per serving.
    """
    return _get(f"/recipes/{recipe_id}/nutritionWidget.json", {})


def get_recipe_nutrition_label(recipe_id: int, show_optional_nutrients: bool = None,
                                show_zero_values: bool = None,
                                show_ingredients: bool = None) -> str:
    """
    Get an HTML nutrition label for a recipe by its ID, suitable for display.
    Optionally show optional nutrients, zero-value rows, and ingredient list.
    """
    params = {
        "showOptionalNutrients": show_optional_nutrients,
        "showZeroValues": show_zero_values,
        "showIngredients": show_ingredients,
    }
    params = {k: v for k, v in params.items() if v is not None}
    params["apiKey"] = _api_key()
    try:
        resp = requests.get(
            f"{BASE_URL}/recipes/{recipe_id}/nutritionLabel",
            params=params,
            timeout=15,
        )
        resp.raise_for_status()
        return resp.text
    except requests.HTTPError as e:
        return {"error": f"HTTP {resp.status_code}: {resp.text[:300]}"}
    except Exception as e:
        return {"error": str(e)}


def analyze_recipe_nutrition(
    title: str,
    ingredient_list: str,
    servings: int,
    include_nutrition: bool = True,
) -> dict:
    """
    Analyze the nutrition of a recipe given its title, a newline-separated
    ingredient list, and the number of servings. Returns full nutritional data.
    """
    try:
        api_key = _api_key()
        data = {
            "title": title,
            "ingredientList": ingredient_list,
            "servings": servings,
            "includeNutrition": include_nutrition,
        }
        resp = requests.post(
            f"{BASE_URL}/recipes/analyze",
            params={"apiKey": api_key},
            data=data,
            timeout=15,
        )
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": f"HTTP {resp.status_code}: {resp.text[:300]}"}
    except Exception as e:
        return {"error": str(e)}


def compute_glycemic_load(
    ingredient_list: str,
    servings: int = 1,
    language: str = None,
) -> dict:
    """
    Compute the glycemic load of a recipe from a newline-separated ingredient
    list and number of servings.
    """
    try:
        api_key = _api_key()
        params = {"apiKey": api_key}
        if language:
            params["language"] = language
        payload = {"ingredientList": ingredient_list, "servings": servings}
        resp = requests.post(
            f"{BASE_URL}/food/ingredients/glycemicLoad",
            params=params,
            json=payload,
            timeout=15,
        )
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": f"HTTP {resp.status_code}: {resp.text[:300]}"}
    except Exception as e:
        return {"error": str(e)}


def detect_food_in_text(text: str) -> dict:
    """
    Detect food items mentioned in a free-text string. Returns a list of
    detected food annotations with their positions in the text.
    """
    try:
        api_key = _api_key()
        resp = requests.post(
            f"{BASE_URL}/food/detect",
            params={"apiKey": api_key},
            data={"text": text},
            timeout=15,
        )
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": f"HTTP {resp.status_code}: {resp.text[:300]}"}
    except Exception as e:
        return {"error": str(e)}


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
    Search for food-related videos by query with optional filters for type,
    cuisine, diet, ingredients, and video length (in seconds).
    """
    params = {
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
    }
    return _get("/food/videos/search", params)


def get_random_food_videos(tags: str = None, number: int = 10) -> dict:
    """
    Get a set of random food-related videos, optionally filtered by tags.
    """
    params = {"tags": tags, "number": number}
    return _get("/food/videos/random", params)


def get_conversation_suggests(query: str, number: float = None) -> dict:
    """
    Get suggestions for a chatbot conversation about food, given a partial
    query string. Useful for building food-related conversational interfaces.
    """
    params = {"query": query, "number": number}
    return _get("/food/converse/suggest", params)


def talk_to_chatbot(text: str, context_id: str = None) -> dict:
    """
    Send a message to the Spoonacular food chatbot and receive a response.
    Optionally provide a context ID to maintain conversation state.
    """
    params = {"text": text, "contextId": context_id}
    return _get("/food/converse", params)
