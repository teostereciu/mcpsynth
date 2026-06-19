from typing import Any, Dict, List, Optional

from generated_tools.common import spoonacular_request


def search_recipes(
    query: Optional[str] = None,
    cuisine: Optional[str] = None,
    diet: Optional[str] = None,
    intolerances: Optional[List[str]] = None,
    include_ingredients: Optional[List[str]] = None,
    exclude_ingredients: Optional[List[str]] = None,
    type: Optional[str] = None,
    instructions_required: Optional[bool] = None,
    fill_ingredients: Optional[bool] = None,
    add_recipe_information: Optional[bool] = None,
    add_recipe_nutrition: Optional[bool] = None,
    max_ready_time: Optional[int] = None,
    min_calories: Optional[int] = None,
    max_calories: Optional[int] = None,
    min_protein: Optional[int] = None,
    max_protein: Optional[int] = None,
    min_fat: Optional[int] = None,
    max_fat: Optional[int] = None,
    min_carbs: Optional[int] = None,
    max_carbs: Optional[int] = None,
    number: Optional[int] = None,
    offset: Optional[int] = None,
    sort: Optional[str] = None,
    sort_direction: Optional[str] = None,
) -> Any:
    return spoonacular_request(
        "GET",
        "/recipes/complexSearch",
        {
            "query": query,
            "cuisine": cuisine,
            "diet": diet,
            "intolerances": intolerances,
            "includeIngredients": include_ingredients,
            "excludeIngredients": exclude_ingredients,
            "type": type,
            "instructionsRequired": instructions_required,
            "fillIngredients": fill_ingredients,
            "addRecipeInformation": add_recipe_information,
            "addRecipeNutrition": add_recipe_nutrition,
            "maxReadyTime": max_ready_time,
            "minCalories": min_calories,
            "maxCalories": max_calories,
            "minProtein": min_protein,
            "maxProtein": max_protein,
            "minFat": min_fat,
            "maxFat": max_fat,
            "minCarbs": min_carbs,
            "maxCarbs": max_carbs,
            "number": number,
            "offset": offset,
            "sort": sort,
            "sortDirection": sort_direction,
        },
    )


def search_recipes_by_ingredients(
    ingredients: List[str],
    number: Optional[int] = None,
    ranking: Optional[int] = None,
    ignore_pantry: Optional[bool] = None,
) -> Any:
    return spoonacular_request(
        "GET",
        "/recipes/findByIngredients",
        {
            "ingredients": ingredients,
            "number": number,
            "ranking": ranking,
            "ignorePantry": ignore_pantry,
        },
    )


def search_recipes_by_nutrients(
    min_calories: Optional[int] = None,
    max_calories: Optional[int] = None,
    min_carbs: Optional[int] = None,
    max_carbs: Optional[int] = None,
    min_protein: Optional[int] = None,
    max_protein: Optional[int] = None,
    min_fat: Optional[int] = None,
    max_fat: Optional[int] = None,
    number: Optional[int] = None,
    offset: Optional[int] = None,
    random: Optional[bool] = None,
) -> Any:
    return spoonacular_request(
        "GET",
        "/recipes/findByNutrients",
        {
            "minCalories": min_calories,
            "maxCalories": max_calories,
            "minCarbs": min_carbs,
            "maxCarbs": max_carbs,
            "minProtein": min_protein,
            "maxProtein": max_protein,
            "minFat": min_fat,
            "maxFat": max_fat,
            "number": number,
            "offset": offset,
            "random": random,
        },
    )


def get_recipe_information(recipe_id: int, include_nutrition: Optional[bool] = None) -> Any:
    return spoonacular_request(
        "GET",
        f"/recipes/{recipe_id}/information",
        {"includeNutrition": include_nutrition},
    )


def get_recipe_ingredient_information(recipe_id: int) -> Any:
    return spoonacular_request("GET", f"/recipes/{recipe_id}/ingredientWidget.json")


def get_recipe_nutrition_widget(recipe_id: int) -> Any:
    return spoonacular_request("GET", f"/recipes/{recipe_id}/nutritionWidget.json")


def get_recipe_instructions(recipe_id: int, step_breakdown: Optional[bool] = None) -> Any:
    return spoonacular_request(
        "GET",
        f"/recipes/{recipe_id}/analyzedInstructions",
        {"stepBreakdown": step_breakdown},
    )


def get_similar_recipes(recipe_id: int, number: Optional[int] = None) -> Any:
    return spoonacular_request("GET", f"/recipes/{recipe_id}/similar", {"number": number})


def autocomplete_recipe_search(query: str, number: Optional[int] = None) -> Any:
    return spoonacular_request("GET", "/recipes/autocomplete", {"query": query, "number": number})
