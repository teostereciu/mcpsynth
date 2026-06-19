from mcp.server.fastmcp import FastMCP

from generated_tools.recipes import (
    recipes_autocomplete,
    recipes_complex_search,
    recipes_find_by_ingredients,
    recipes_get_analyzed_instructions,
    recipes_get_information,
    recipes_get_similar,
)
from generated_tools.ingredients import (
    ingredients_autocomplete,
    ingredients_get_information,
    ingredients_parse,
    ingredients_search,
)
from generated_tools.meal_planning import mealplan_generate
from generated_tools.nutrition import recipes_get_nutrition_widget, recipes_get_nutrition_widget_json
from generated_tools.wine import wine_description, wine_pairing, wine_recommendation

mcp = FastMCP("spoonacular")


@mcp.tool()
def recipes_complex_search_tool(**kwargs):
    return recipes_complex_search(**kwargs)


@mcp.tool()
def recipes_find_by_ingredients_tool(ingredients: str, number: int | None = None, ranking: int | None = None, ignorePantry: bool | None = None):
    return recipes_find_by_ingredients(ingredients=ingredients, number=number, ranking=ranking, ignorePantry=ignorePantry)


@mcp.tool()
def recipes_get_information_tool(id: int, includeNutrition: bool | None = None):
    return recipes_get_information(id=id, includeNutrition=includeNutrition)


@mcp.tool()
def recipes_get_analyzed_instructions_tool(id: int):
    return recipes_get_analyzed_instructions(id=id)


@mcp.tool()
def recipes_get_similar_tool(id: int, number: int | None = None):
    return recipes_get_similar(id=id, number=number)


@mcp.tool()
def recipes_autocomplete_tool(query: str, number: int | None = None):
    return recipes_autocomplete(query=query, number=number)


@mcp.tool()
def ingredients_search_tool(query: str, number: int | None = None, offset: int | None = None):
    return ingredients_search(query=query, number=number, offset=offset)


@mcp.tool()
def ingredients_get_information_tool(id: int, amount: float | None = None, unit: str | None = None):
    return ingredients_get_information(id=id, amount=amount, unit=unit)


@mcp.tool()
def ingredients_autocomplete_tool(query: str, number: int | None = None):
    return ingredients_autocomplete(query=query, number=number)


@mcp.tool()
def ingredients_parse_tool(ingredientList: str, servings: int | None = None, includeNutrition: bool | None = None):
    return ingredients_parse(ingredientList=ingredientList, servings=servings, includeNutrition=includeNutrition)


@mcp.tool()
def mealplan_generate_tool(timeFrame: str = "day", targetCalories: int | None = None, diet: str | None = None, exclude: str | None = None):
    return mealplan_generate(timeFrame=timeFrame, targetCalories=targetCalories, diet=diet, exclude=exclude)


@mcp.tool()
def recipes_get_nutrition_widget_json_tool(id: int):
    return recipes_get_nutrition_widget_json(id=id)


@mcp.tool()
def recipes_get_nutrition_widget_tool(id: int):
    return recipes_get_nutrition_widget(id=id)


@mcp.tool()
def wine_pairing_tool(dish: str):
    return wine_pairing(dish=dish)


@mcp.tool()
def wine_description_tool(wine: str):
    return wine_description(wine=wine)


@mcp.tool()
def wine_recommendation_tool(wine: str, maxPrice: float | None = None, minRating: float | None = None, number: int | None = None):
    return wine_recommendation(wine=wine, maxPrice=maxPrice, minRating=minRating, number=number)


if __name__ == "__main__":
    mcp.run()
