from mcp.server.fastmcp import FastMCP

from generated_tools.recipes import (
    recipe_analyzed_instructions,
    recipe_ingredients_widget,
    recipe_information,
    recipe_nutrition_widget,
    recipe_similar,
    recipes_autocomplete,
    recipes_complex_search,
    recipes_find_by_ingredients,
    recipes_find_by_nutrients,
)
from generated_tools.ingredients import (
    ingredient_information,
    ingredients_autocomplete,
    ingredients_search,
    parse_ingredients,
)
from generated_tools.meal_planning import meal_plan_generate
from generated_tools.nutrition import guess_nutrition_by_dish_name
from generated_tools.wine import wine_description, wine_pairing


mcp = FastMCP("spoonacular")


@mcp.tool()
def recipes_complex_search_tool(**kwargs):
    return recipes_complex_search(**kwargs)


@mcp.tool()
def recipes_find_by_ingredients_tool(ingredients: str, number: int = 10, ranking: int = 1, ignorePantry: bool = True):
    return recipes_find_by_ingredients(ingredients=ingredients, number=number, ranking=ranking, ignorePantry=ignorePantry)


@mcp.tool()
def recipes_find_by_nutrients_tool(**kwargs):
    return recipes_find_by_nutrients(**kwargs)


@mcp.tool()
def recipes_autocomplete_tool(query: str, number: int = 10):
    return recipes_autocomplete(query=query, number=number)


@mcp.tool()
def recipe_information_tool(recipe_id: int, includeNutrition: bool = False):
    return recipe_information(recipe_id=recipe_id, includeNutrition=includeNutrition)


@mcp.tool()
def recipe_analyzed_instructions_tool(recipe_id: int, stepBreakdown: bool = True):
    return recipe_analyzed_instructions(recipe_id=recipe_id, stepBreakdown=stepBreakdown)


@mcp.tool()
def recipe_similar_tool(recipe_id: int, number: int = 10):
    return recipe_similar(recipe_id=recipe_id, number=number)


@mcp.tool()
def recipe_ingredients_widget_tool(recipe_id: int):
    return recipe_ingredients_widget(recipe_id=recipe_id)


@mcp.tool()
def recipe_nutrition_widget_tool(recipe_id: int):
    return recipe_nutrition_widget(recipe_id=recipe_id)


@mcp.tool()
def ingredients_search_tool(query: str, number: int = 10, offset: int = 0):
    return ingredients_search(query=query, number=number, offset=offset)


@mcp.tool()
def ingredient_information_tool(ingredient_id: int, amount: float | None = None, unit: str | None = None):
    return ingredient_information(ingredient_id=ingredient_id, amount=amount, unit=unit)


@mcp.tool()
def ingredients_autocomplete_tool(query: str, number: int = 10, metaInformation: bool = True):
    return ingredients_autocomplete(query=query, number=number, metaInformation=metaInformation)


@mcp.tool()
def parse_ingredients_tool(ingredientList: str, servings: int | None = None, includeNutrition: bool = False):
    return parse_ingredients(ingredientList=ingredientList, servings=servings, includeNutrition=includeNutrition)


@mcp.tool()
def meal_plan_generate_tool(timeFrame: str = "day", targetCalories: int | None = None, diet: str | None = None, exclude: str | None = None):
    return meal_plan_generate(timeFrame=timeFrame, targetCalories=targetCalories, diet=diet, exclude=exclude)


@mcp.tool()
def guess_nutrition_by_dish_name_tool(title: str):
    return guess_nutrition_by_dish_name(title=title)


@mcp.tool()
def wine_pairing_tool(food: str, maxPrice: float | None = None, minRating: float | None = None):
    return wine_pairing(food=food, maxPrice=maxPrice, minRating=minRating)


@mcp.tool()
def wine_description_tool(wine: str):
    return wine_description(wine=wine)


if __name__ == "__main__":
    mcp.run()
