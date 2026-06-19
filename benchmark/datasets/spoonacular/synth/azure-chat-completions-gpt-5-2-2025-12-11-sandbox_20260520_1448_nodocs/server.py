from mcp.server.fastmcp import FastMCP

from generated_tools.recipes import (
    recipes_autocomplete,
    recipes_complex_search,
    recipes_find_by_ingredients,
    recipes_get_analyzed_instructions,
    recipes_get_information,
    recipes_get_ingredient_widget,
    recipes_get_nutrition_widget,
    recipes_get_similar,
    recipes_search_by_nutrients,
)
from generated_tools.ingredients import (
    ingredients_autocomplete,
    ingredients_get_information,
    ingredients_parse,
    ingredients_search,
)
from generated_tools.meal_planning import mealplan_generate
from generated_tools.nutrition import nutrition_guess_by_dish_name, nutrition_visualize_recipe_nutrition
from generated_tools.wine import wine_description, wine_pairing

mcp = FastMCP("spoonacular")

# Recipes
mcp.tool()(recipes_complex_search)
mcp.tool()(recipes_find_by_ingredients)
mcp.tool()(recipes_search_by_nutrients)
mcp.tool()(recipes_autocomplete)
mcp.tool()(recipes_get_information)
mcp.tool()(recipes_get_analyzed_instructions)
mcp.tool()(recipes_get_similar)
mcp.tool()(recipes_get_ingredient_widget)
mcp.tool()(recipes_get_nutrition_widget)

# Ingredients
mcp.tool()(ingredients_autocomplete)
mcp.tool()(ingredients_search)
mcp.tool()(ingredients_get_information)
mcp.tool()(ingredients_parse)

# Meal planning
mcp.tool()(mealplan_generate)

# Nutrition
mcp.tool()(nutrition_guess_by_dish_name)
mcp.tool()(nutrition_visualize_recipe_nutrition)

# Wine
mcp.tool()(wine_pairing)
mcp.tool()(wine_description)


if __name__ == "__main__":
    mcp.run_stdio()
