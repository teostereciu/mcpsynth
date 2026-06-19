from mcp.server.fastmcp import FastMCP
from generated_tools.recipes import search_recipes, search_recipes_by_nutrients, search_recipes_by_ingredients, get_recipe_information, get_similar_recipes, autocomplete_recipe_search, get_nutrition_by_id, parse_ingredients
from generated_tools.ingredients import search_ingredients, get_ingredient_information, compute_ingredient_amount, autocomplete_ingredient_search
from generated_tools.meal_planning import get_meal_plan_week, get_meal_plan_day, generate_meal_plan
from generated_tools.wine import wine_dishes, wine_pairing, wine_description, wine_recommendation
from generated_tools.misc import search_all_food, search_food_videos, quick_answer, detect_food, search_site_content

mcp = FastMCP("spoonacular")

mcp.tool()(search_recipes)
mcp.tool()(search_recipes_by_nutrients)
mcp.tool()(search_recipes_by_ingredients)
mcp.tool()(get_recipe_information)
mcp.tool()(get_similar_recipes)
mcp.tool()(autocomplete_recipe_search)
mcp.tool()(get_nutrition_by_id)
mcp.tool()(parse_ingredients)
mcp.tool()(search_ingredients)
mcp.tool()(get_ingredient_information)
mcp.tool()(compute_ingredient_amount)
mcp.tool()(autocomplete_ingredient_search)
mcp.tool()(get_meal_plan_week)
mcp.tool()(get_meal_plan_day)
mcp.tool()(generate_meal_plan)
mcp.tool()(wine_dishes)
mcp.tool()(wine_pairing)
mcp.tool()(wine_description)
mcp.tool()(wine_recommendation)
mcp.tool()(search_all_food)
mcp.tool()(search_food_videos)
mcp.tool()(quick_answer)
mcp.tool()(detect_food)
mcp.tool()(search_site_content)

if __name__ == "__main__":
    mcp.run(transport="stdio")
