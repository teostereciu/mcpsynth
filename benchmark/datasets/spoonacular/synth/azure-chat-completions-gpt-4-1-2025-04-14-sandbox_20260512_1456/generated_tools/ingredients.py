import os
import requests

def search_ingredients(params):
    """
    Search for simple whole foods (ingredients).
    Corresponds to GET /food/ingredients/search
    Accepts params as a dict of query parameters.
    Returns JSON-serializable dict.
    """
    try:
        api_key = os.environ.get('SPOONACULAR_API_KEY')
        if not api_key:
            return {"error": "Missing SPOONACULAR_API_KEY environment variable"}
        base_url = "https://api.spoonacular.com/food/ingredients/search"
        params = params.copy()
        params['apiKey'] = api_key
        resp = requests.get(base_url, params=params)
        if resp.status_code != 200:
            return {"error": f"HTTP {resp.status_code}: {resp.text}"}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def get_ingredient_information(ingredient_id, params=None):
    """
    Get all available information about an ingredient by ID.
    Corresponds to GET /food/ingredients/{id}/information
    Accepts ingredient_id (int) and optional params dict.
    Returns JSON-serializable dict.
    """
    try:
        api_key = os.environ.get('SPOONACULAR_API_KEY')
        if not api_key:
            return {"error": "Missing SPOONACULAR_API_KEY environment variable"}
        base_url = f"https://api.spoonacular.com/food/ingredients/{ingredient_id}/information"
        params = params.copy() if params else {}
        params['apiKey'] = api_key
        resp = requests.get(base_url, params=params)
        if resp.status_code != 200:
            return {"error": f"HTTP {resp.status_code}: {resp.text}"}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def compute_ingredient_amount(ingredient_id, nutrient, target, unit=None):
    """
    Compute the amount needed of an ingredient for a nutritional goal.
    Corresponds to GET /food/ingredients/{id}/amount
    Accepts ingredient_id (int), nutrient (str), target (number), unit (optional str).
    Returns JSON-serializable dict.
    """
    try:
        api_key = os.environ.get('SPOONACULAR_API_KEY')
        if not api_key:
            return {"error": "Missing SPOONACULAR_API_KEY environment variable"}
        base_url = f"https://api.spoonacular.com/food/ingredients/{ingredient_id}/amount"
        params = {'apiKey': api_key, 'nutrient': nutrient, 'target': target}
        if unit:
            params['unit'] = unit
        resp = requests.get(base_url, params=params)
        if resp.status_code != 200:
            return {"error": f"HTTP {resp.status_code}: {resp.text}"}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def convert_amounts(ingredient_name, source_amount, source_unit, target_unit):
    """
    Convert amounts like '2 cups of flour to grams'.
    Corresponds to GET /recipes/convert
    Accepts ingredient_name (str), source_amount (number), source_unit (str), target_unit (str).
    Returns JSON-serializable dict.
    """
    try:
        api_key = os.environ.get('SPOONACULAR_API_KEY')
        if not api_key:
            return {"error": "Missing SPOONACULAR_API_KEY environment variable"}
        base_url = "https://api.spoonacular.com/recipes/convert"
        params = {
            'apiKey': api_key,
            'ingredientName': ingredient_name,
            'sourceAmount': source_amount,
            'sourceUnit': source_unit,
            'targetUnit': target_unit
        }
        resp = requests.get(base_url, params=params)
        if resp.status_code != 200:
            return {"error": f"HTTP {resp.status_code}: {resp.text}"}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def parse_ingredients(ingredient_list, servings=1, include_nutrition=False, language="en"):
    """
    Extract ingredients from plain text.
    Corresponds to POST /recipes/parseIngredients
    Accepts ingredient_list (str, one per line), servings (int), include_nutrition (bool), language (str).
    Returns JSON-serializable list.
    """
    try:
        api_key = os.environ.get('SPOONACULAR_API_KEY')
        if not api_key:
            return {"error": "Missing SPOONACULAR_API_KEY environment variable"}
        base_url = "https://api.spoonacular.com/recipes/parseIngredients"
        data = {
            'apiKey': api_key,
            'ingredientList': ingredient_list,
            'servings': servings,
            'includeNutrition': include_nutrition,
            'language': language
        }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        resp = requests.post(base_url, data=data, headers=headers)
        if resp.status_code != 200:
            return {"error": f"HTTP {resp.status_code}: {resp.text}"}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}
