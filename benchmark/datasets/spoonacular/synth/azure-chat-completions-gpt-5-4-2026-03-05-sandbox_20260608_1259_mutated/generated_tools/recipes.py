from typing import Any, Optional

from .common import spoonacular_request


def search_recipes(
    search_query: Optional[str] = None,
    cuisine: Optional[str] = None,
    excludeCuisine: Optional[str] = None,
    diet_type: Optional[str] = None,
    intolerances: Optional[str] = None,
    equipment: Optional[str] = None,
    ingredients: Optional[str] = None,
    excludeIngredients: Optional[str] = None,
    type: Optional[str] = None,
    instructionsRequired: Optional[bool] = None,
    fillIngredients: Optional[bool] = None,
    addRecipeInformation: Optional[bool] = None,
    addRecipeInstructions: Optional[bool] = None,
    addRecipeNutrition: Optional[bool] = None,
    author: Optional[str] = None,
    tags: Optional[str] = None,
    recipeBoxId: Optional[int] = None,
    titleMatch: Optional[str] = None,
    maxReadyTime: Optional[int] = None,
    minServings: Optional[int] = None,
    maxServings: Optional[int] = None,
    ignorePantry: Optional[bool] = None,
    sort: Optional[str] = None,
    sortDirection: Optional[str] = None,
    minCarbs: Optional[float] = None,
    maxCarbs: Optional[float] = None,
    minProtein: Optional[float] = None,
    maxProtein: Optional[float] = None,
    minCalories: Optional[float] = None,
    maxCalories: Optional[float] = None,
    minFat: Optional[float] = None,
    maxFat: Optional[float] = None,
    offset: Optional[int] = None,
    number: Optional[int] = None,
) -> Any:
    return spoonacular_request("GET", "/recipes/complexSearch", params=locals())


def search_recipes_by_nutrients(
    minCarbs: Optional[float] = None,
    maxCarbs: Optional[float] = None,
    minProtein: Optional[float] = None,
    maxProtein: Optional[float] = None,
    minCalories: Optional[float] = None,
    maxCalories: Optional[float] = None,
    minFat: Optional[float] = None,
    maxFat: Optional[float] = None,
    minAlcohol: Optional[float] = None,
    maxAlcohol: Optional[float] = None,
    minCaffeine: Optional[float] = None,
    maxCaffeine: Optional[float] = None,
    minCopper: Optional[float] = None,
    maxCopper: Optional[float] = None,
    minCalcium: Optional[float] = None,
    maxCalcium: Optional[float] = None,
    minCholine: Optional[float] = None,
    maxCholine: Optional[float] = None,
    minCholesterol: Optional[float] = None,
    maxCholesterol: Optional[float] = None,
    minFluoride: Optional[float] = None,
    maxFluoride: Optional[float] = None,
    minSaturatedFat: Optional[float] = None,
    maxSaturatedFat: Optional[float] = None,
    minVitaminA: Optional[float] = None,
    maxVitaminA: Optional[float] = None,
    minVitaminC: Optional[float] = None,
    maxVitaminC: Optional[float] = None,
    minVitaminD: Optional[float] = None,
    maxVitaminD: Optional[float] = None,
    minVitaminE: Optional[float] = None,
    maxVitaminE: Optional[float] = None,
    minVitaminK: Optional[float] = None,
    maxVitaminK: Optional[float] = None,
    minVitaminB1: Optional[float] = None,
    maxVitaminB1: Optional[float] = None,
    minVitaminB2: Optional[float] = None,
    maxVitaminB2: Optional[float] = None,
    minVitaminB5: Optional[float] = None,
    maxVitaminB5: Optional[float] = None,
    minVitaminB3: Optional[float] = None,
    maxVitaminB3: Optional[float] = None,
    minVitaminB6: Optional[float] = None,
    maxVitaminB6: Optional[float] = None,
    minVitaminB12: Optional[float] = None,
    maxVitaminB12: Optional[float] = None,
    minFiber: Optional[float] = None,
    maxFiber: Optional[float] = None,
    minFolate: Optional[float] = None,
    maxFolate: Optional[float] = None,
    minFolicAcid: Optional[float] = None,
    maxFolicAcid: Optional[float] = None,
    minIodine: Optional[float] = None,
    maxIodine: Optional[float] = None,
    minIron: Optional[float] = None,
    maxIron: Optional[float] = None,
    minMagnesium: Optional[float] = None,
    maxMagnesium: Optional[float] = None,
    minManganese: Optional[float] = None,
    maxManganese: Optional[float] = None,
    minPhosphorus: Optional[float] = None,
    maxPhosphorus: Optional[float] = None,
    minPotassium: Optional[float] = None,
    maxPotassium: Optional[float] = None,
    minSelenium: Optional[float] = None,
    maxSelenium: Optional[float] = None,
    minSodium: Optional[float] = None,
    maxSodium: Optional[float] = None,
    minSugar: Optional[float] = None,
    maxSugar: Optional[float] = None,
    minZinc: Optional[float] = None,
    maxZinc: Optional[float] = None,
    random: Optional[bool] = None,
    offset: Optional[int] = None,
    number: Optional[int] = None,
) -> Any:
    return spoonacular_request("GET", "/recipes/findByNutrients", params=locals())


def search_recipes_by_ingredients(ingredients: str, number: Optional[int] = None, ranking: Optional[int] = None, ignorePantry: Optional[bool] = None) -> Any:
    return spoonacular_request("GET", "/recipes/findByIngredients", params=locals())


def get_recipe_information(id: int, includeNutrition: Optional[bool] = None) -> Any:
    return spoonacular_request("GET", f"/recipes/{id}/information", params={"includeNutrition": includeNutrition})


def get_recipe_information_bulk(ids: str) -> Any:
    return spoonacular_request("GET", "/recipes/informationBulk", params=locals())


def get_similar_recipes(id: int, number: Optional[int] = None) -> Any:
    return spoonacular_request("GET", f"/recipes/{id}/similar", params={"number": number})


def get_random_recipes(number: Optional[int] = None, include_tags: Optional[str] = None, exclude_tags: Optional[str] = None) -> Any:
    return spoonacular_request("GET", "/recipes/random", params={"number": number, "include-tags": include_tags, "exclude-tags": exclude_tags})


def autocomplete_recipe_search(search_query: str, number: Optional[int] = None) -> Any:
    return spoonacular_request("GET", "/recipes/autocomplete", params=locals())


def get_recipe_nutrition_widget(id: int, defaultCss: Optional[bool] = None) -> Any:
    return spoonacular_request("GET", f"/recipes/{id}/nutritionWidget.json", params={"defaultCss": defaultCss})


def get_recipe_analyzed_instructions(id: int, stepBreakdown: Optional[bool] = None) -> Any:
    return spoonacular_request("GET", f"/recipes/{id}/analyzedInstructions", params={"stepBreakdown": stepBreakdown})


def extract_recipe_from_website(url: str, forceExtraction: Optional[bool] = None, analyze: Optional[bool] = None, includeNutrition: Optional[bool] = None, includeTaste: Optional[bool] = None) -> Any:
    return spoonacular_request("GET", "/recipes/extract", params=locals())


def analyze_recipe(search_query: str, includeNutrition: Optional[bool] = None, includeTaste: Optional[bool] = None, language: Optional[str] = None) -> Any:
    return spoonacular_request("POST", "/recipes/analyze", params={"includeNutrition": includeNutrition, "includeTaste": includeTaste, "language": language}, data={"search_query": search_query})


def get_recipe_summary(id: int) -> Any:
    return spoonacular_request("GET", f"/recipes/{id}/summary")


def analyze_recipe_instructions(instructions: str) -> Any:
    return spoonacular_request("POST", "/recipes/analyzeInstructions", data={"instructions": instructions})


def classify_cuisine(title: str, ingredientList: str, language: Optional[str] = None) -> Any:
    return spoonacular_request("POST", "/recipes/cuisine", params={"language": language}, data={"title": title, "ingredientList": ingredientList})


def analyze_recipe_search_query(q: str) -> Any:
    return spoonacular_request("GET", "/recipes/queries/analyze", params=locals())
