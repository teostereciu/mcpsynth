import os
import requests

def search_recipes(params):
    """
    Search recipes with advanced filtering and ranking.
    Corresponds to GET /recipes/complexSearch
    Accepts params as a dict of query parameters.
    Returns JSON-serializable dict.
    """
    try:
        api_key = os.environ.get('SPOONACULAR_API_KEY')
        if not api_key:
            return {"error": "Missing SPOONACULAR_API_KEY environment variable"}
        base_url = "https://api.spoonacular.com/recipes/complexSearch"
        params = params.copy()
        params['apiKey'] = api_key
        resp = requests.get(base_url, params=params)
        if resp.status_code != 200:
            return {"error": f"HTTP {resp.status_code}: {resp.text}"}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def search_recipes_by_nutrients(params):
    """
    Find recipes that adhere to nutritional limits.
    Corresponds to GET /recipes/findByNutrients
    Accepts params as a dict of query parameters.
    Returns JSON-serializable dict.
    """
    try:
        api_key = os.environ.get('SPOONACULAR_API_KEY')
        if not api_key:
            return {"error": "Missing SPOONACULAR_API_KEY environment variable"}
        base_url = "https://api.spoonacular.com/recipes/findByNutrients"
        params = params.copy()
        params['apiKey'] = api_key
        resp = requests.get(base_url, params=params)
        if resp.status_code != 200:
            return {"error": f"HTTP {resp.status_code}: {resp.text}"}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def search_recipes_by_ingredients(params):
    """
    Search recipes by a list of ingredients.
    Corresponds to GET /recipes/findByIngredients
    Accepts params as a dict of query parameters.
    Returns JSON-serializable dict.
    """
    try:
        api_key = os.environ.get('SPOONACULAR_API_KEY')
        if not api_key:
            return {"error": "Missing SPOONACULAR_API_KEY environment variable"}
        base_url = "https://api.spoonacular.com/recipes/findByIngredients"
        params = params.copy()
        params['apiKey'] = api_key
        resp = requests.get(base_url, params=params)
        if resp.status_code != 200:
            return {"error": f"HTTP {resp.status_code}: {resp.text}"}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def get_recipe_information(recipe_id, params=None):
    """
    Get detailed information about a recipe by ID.
    Corresponds to GET /recipes/{id}/information
    Accepts recipe_id (int) and optional params dict.
    Returns JSON-serializable dict.
    """
    try:
        api_key = os.environ.get('SPOONACULAR_API_KEY')
        if not api_key:
            return {"error": "Missing SPOONACULAR_API_KEY environment variable"}
        base_url = f"https://api.spoonacular.com/recipes/{recipe_id}/information"
        params = params.copy() if params else {}
        params['apiKey'] = api_key
        resp = requests.get(base_url, params=params)
        if resp.status_code != 200:
            return {"error": f"HTTP {resp.status_code}: {resp.text}"}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def get_recipe_ingredients(recipe_id):
    """
    Get ingredients for a recipe by ID.
    Corresponds to GET /recipes/{id}/ingredientWidget.json
    Accepts recipe_id (int).
    Returns JSON-serializable dict.
    """
    try:
        api_key = os.environ.get('SPOONACULAR_API_KEY')
        if not api_key:
            return {"error": "Missing SPOONACULAR_API_KEY environment variable"}
        base_url = f"https://api.spoonacular.com/recipes/{recipe_id}/ingredientWidget.json"
        params = {'apiKey': api_key}
        resp = requests.get(base_url, params=params)
        if resp.status_code != 200:
            return {"error": f"HTTP {resp.status_code}: {resp.text}"}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def get_recipe_nutrition(recipe_id):
    """
    Get nutrition for a recipe by ID.
    Corresponds to GET /recipes/{id}/nutritionWidget.json
    Accepts recipe_id (int).
    Returns JSON-serializable dict.
    """
    try:
        api_key = os.environ.get('SPOONACULAR_API_KEY')
        if not api_key:
            return {"error": "Missing SPOONACULAR_API_KEY environment variable"}
        base_url = f"https://api.spoonacular.com/recipes/{recipe_id}/nutritionWidget.json"
        params = {'apiKey': api_key}
        resp = requests.get(base_url, params=params)
        if resp.status_code != 200:
            return {"error": f"HTTP {resp.status_code}: {resp.text}"}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def get_recipe_instructions(recipe_id):
    """
    Get analyzed recipe instructions by ID.
    Corresponds to GET /recipes/{id}/analyzedInstructions
    Accepts recipe_id (int).
    Returns JSON-serializable dict.
    """
    try:
        api_key = os.environ.get('SPOONACULAR_API_KEY')
        if not api_key:
            return {"error": "Missing SPOONACULAR_API_KEY environment variable"}
        base_url = f"https://api.spoonacular.com/recipes/{recipe_id}/analyzedInstructions"
        params = {'apiKey': api_key}
        resp = requests.get(base_url, params=params)
        if resp.status_code != 200:
            return {"error": f"HTTP {resp.status_code}: {resp.text}"}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def get_similar_recipes(recipe_id, params=None):
    """
    Get similar recipes by recipe ID.
    Corresponds to GET /recipes/{id}/similar
    Accepts recipe_id (int) and optional params dict.
    Returns JSON-serializable dict.
    """
    try:
        api_key = os.environ.get('SPOONACULAR_API_KEY')
        if not api_key:
            return {"error": "Missing SPOONACULAR_API_KEY environment variable"}
        base_url = f"https://api.spoonacular.com/recipes/{recipe_id}/similar"
        params = params.copy() if params else {}
        params['apiKey'] = api_key
        resp = requests.get(base_url, params=params)
        if resp.status_code != 200:
            return {"error": f"HTTP {resp.status_code}: {resp.text}"}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def autocomplete_recipe_search(params):
    """
    Autocomplete recipe search.
    Corresponds to GET /recipes/autocomplete
    Accepts params as a dict of query parameters.
    Returns JSON-serializable dict.
    """
    try:
        api_key = os.environ.get('SPOONACULAR_API_KEY')
        if not api_key:
            return {"error": "Missing SPOONACULAR_API_KEY environment variable"}
        base_url = "https://api.spoonacular.com/recipes/autocomplete"
        params = params.copy()
        params['apiKey'] = api_key
        resp = requests.get(base_url, params=params)
        if resp.status_code != 200:
            return {"error": f"HTTP {resp.status_code}: {resp.text}"}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}
