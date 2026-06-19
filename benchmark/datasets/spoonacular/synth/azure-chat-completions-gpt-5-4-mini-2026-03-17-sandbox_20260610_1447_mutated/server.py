from mcp.server.fastmcp import FastMCP

from generated_tools.ingredients import (
    autocomplete_ingredient_search,
    compute_ingredient_amount,
    convert_amounts,
    get_ingredient_information,
    parse_ingredients,
    search_ingredients,
)
from generated_tools.meal_planning import generate_meal_plan, get_meal_plan_day, get_meal_plan_week
from generated_tools.recipes import (
    autocomplete_recipe_search,
    get_analyzed_recipe_instructions,
    get_recipe_information,
    get_recipe_nutrition_by_id,
    get_similar_recipes,
    search_recipes,
    search_recipes_by_ingredients,
    search_recipes_by_nutrients,
)
from generated_tools.wine import dish_pairing_for_wine, wine_description, wine_pairing

mcp = FastMCP("spoonacular")

mcp.tool()(search_recipes)
mcp.tool()(search_recipes_by_nutrients)
mcp.tool()(search_recipes_by_ingredients)
mcp.tool()(get_recipe_information)
mcp.tool()(get_similar_recipes)
mcp.tool()(autocomplete_recipe_search)
mcp.tool()(get_analyzed_recipe_instructions)
mcp.tool()(get_recipe_nutrition_by_id)
mcp.tool()(search_ingredients)
mcp.tool()(get_ingredient_information)
mcp.tool()(compute_ingredient_amount)
mcp.tool()(convert_amounts)
mcp.tool()(parse_ingredients)
mcp.tool()(autocomplete_ingredient_search)
mcp.tool()(get_meal_plan_week)
mcp.tool()(get_meal_plan_day)
mcp.tool()(generate_meal_plan)
mcp.tool()(dish_pairing_for_wine)
mcp.tool()(wine_pairing)
mcp.tool()(wine_description)


def list_tools():
    return [tool.name for tool in mcp.get_tools()]


if __name__ == "__main__":
    mcp.run()
