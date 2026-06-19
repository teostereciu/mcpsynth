from generated_tools.common import api_get, api_post


def search_recipes(**kwargs):
    return api_get("/recipes/complexSearch", kwargs)


def search_recipes_by_nutrients(**kwargs):
    return api_get("/recipes/findByNutrients", kwargs)


def search_recipes_by_ingredients(**kwargs):
    return api_get("/recipes/findByIngredients", kwargs)


def get_recipe_information(recipe_id, **kwargs):
    return api_get(f"/recipes/{recipe_id}/information", kwargs)


def get_similar_recipes(recipe_id, **kwargs):
    return api_get(f"/recipes/{recipe_id}/similar", kwargs)


def autocomplete_recipe_search(query, **kwargs):
    params = {"query": query, **kwargs}
    return api_get("/recipes/autocomplete", params)


def get_nutrition_by_id(recipe_id):
    return api_get(f"/recipes/{recipe_id}/nutritionWidget.json")


def parse_ingredients(ingredientList, **kwargs):
    data = {"ingredientList": ingredientList, **kwargs}
    return api_post("/recipes/parseIngredients", data)
