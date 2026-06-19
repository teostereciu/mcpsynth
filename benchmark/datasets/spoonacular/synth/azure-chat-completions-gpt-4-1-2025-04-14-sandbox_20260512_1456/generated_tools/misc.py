import os
import requests

def search_all_food(params):
    """
    Search all food content (recipes, products, menu items, ingredients, videos).
    Corresponds to GET /food/search
    Accepts params as a dict of query parameters.
    Returns JSON-serializable dict.
    """
    try:
        api_key = os.environ.get('SPOONACULAR_API_KEY')
        if not api_key:
            return {"error": "Missing SPOONACULAR_API_KEY environment variable"}
        base_url = "https://api.spoonacular.com/food/search"
        params = params.copy()
        params['apiKey'] = api_key
        resp = requests.get(base_url, params=params)
        if resp.status_code != 200:
            return {"error": f"HTTP {resp.status_code}: {resp.text}"}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def search_food_videos(params):
    """
    Find recipe and other food related videos.
    Corresponds to GET /food/videos/search
    Accepts params as a dict of query parameters.
    Returns JSON-serializable dict.
    """
    try:
        api_key = os.environ.get('SPOONACULAR_API_KEY')
        if not api_key:
            return {"error": "Missing SPOONACULAR_API_KEY environment variable"}
        base_url = "https://api.spoonacular.com/food/videos/search"
        params = params.copy()
        params['apiKey'] = api_key
        resp = requests.get(base_url, params=params)
        if resp.status_code != 200:
            return {"error": f"HTTP {resp.status_code}: {resp.text}"}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def quick_answer(q):
    """
    Answer a nutrition related natural language question.
    Corresponds to GET /recipes/quickAnswer
    Accepts q (str).
    Returns JSON-serializable dict.
    """
    try:
        api_key = os.environ.get('SPOONACULAR_API_KEY')
        if not api_key:
            return {"error": "Missing SPOONACULAR_API_KEY environment variable"}
        base_url = "https://api.spoonacular.com/recipes/quickAnswer"
        params = {'apiKey': api_key, 'q': q}
        resp = requests.get(base_url, params=params)
        if resp.status_code != 200:
            return {"error": f"HTTP {resp.status_code}: {resp.text}"}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def detect_food_in_text(text):
    """
    Find all mentions of food contained within text (NER).
    Corresponds to POST /food/detect
    Accepts text (str).
    Returns JSON-serializable dict.
    """
    try:
        api_key = os.environ.get('SPOONACULAR_API_KEY')
        if not api_key:
            return {"error": "Missing SPOONACULAR_API_KEY environment variable"}
        base_url = "https://api.spoonacular.com/food/detect"
        data = {'apiKey': api_key, 'text': text}
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        resp = requests.post(base_url, data=data, headers=headers)
        if resp.status_code != 200:
            return {"error": f"HTTP {resp.status_code}: {resp.text}"}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}
