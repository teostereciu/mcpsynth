from mcp.server.fastmcp import FastMCP

from generated_tools.ingredients import (
    autocomplete_ingredient_search,
    get_ingredient_information,
    parse_ingredients,
    search_ingredients,
)
from generated_tools.meal_planning import generate_meal_plan, get_meal_plan_week
from generated_tools.nutrition import get_recipe_nutrition_by_id, visualize_recipe_nutrition
from generated_tools.recipes import (
    autocomplete_recipe_search,
    get_recipe_ingredient_information,
    get_recipe_information,
    get_recipe_instructions,
    get_recipe_nutrition_widget,
    get_similar_recipes,
    search_recipes,
    search_recipes_by_ingredients,
    search_recipes_by_nutrients,
)
from generated_tools.wine import get_wine_description, get_wine_pairing

mcp = FastMCP("spoonacular")

mcp.tool()(search_recipes)
mcp.tool()(search_recipes_by_ingredients)
mcp.tool()(search_recipes_by_nutrients)
mcp.tool()(get_recipe_information)
mcp.tool()(get_recipe_ingredient_information)
mcp.tool()(get_recipe_nutrition_widget)
mcp.tool()(get_recipe_instructions)
mcp.tool()(get_similar_recipes)
mcp.tool()(autocomplete_recipe_search)

mcp.tool()(search_ingredients)
mcp.tool()(get_ingredient_information)
mcp.tool()(parse_ingredients)
mcp.tool()(autocomplete_ingredient_search)

mcp.tool()(generate_meal_plan)
mcp.tool()(get_meal_plan_week)

mcp.tool()(get_recipe_nutrition_by_id)
mcp.tool()(visualize_recipe_nutrition)

mcp.tool()(get_wine_pairing)
mcp.tool()(get_wine_description)


if __name__ == "__main__":
    mcp.run()
