from mcp.server.fastmcp import FastMCP

from generated_tools.recipes import search_recipes_complex, search_recipes_by_nutrients
from generated_tools.ingredients import (
    ingredient_search,
    get_ingredient_information,
    compute_ingredient_amount,
    convert_amounts,
    parse_ingredients,
)
from generated_tools.meal_planning import connect_user, get_meal_plan_week, get_meal_plan_day, generate_meal_plan
from generated_tools.wine import wine_dish_pairing, wine_pairing, wine_description, wine_recommendation
from generated_tools.misc import search_all_food, search_food_videos, quick_answer, detect_food_in_text, search_site_content
from generated_tools.menu_items import search_menu_items, get_menu_item_information, autocomplete_menu_item_search
from generated_tools.products import search_grocery_products, search_grocery_products_by_upc, get_product_information

mcp = FastMCP("spoonacular")

# Recipes
mcp.tool()(search_recipes_complex)
mcp.tool()(search_recipes_by_nutrients)

# Ingredients
mcp.tool()(ingredient_search)
mcp.tool()(get_ingredient_information)
mcp.tool()(compute_ingredient_amount)
mcp.tool()(convert_amounts)
mcp.tool()(parse_ingredients)

# Meal planning
mcp.tool()(connect_user)
mcp.tool()(get_meal_plan_week)
mcp.tool()(get_meal_plan_day)
mcp.tool()(generate_meal_plan)

# Wine
mcp.tool()(wine_dish_pairing)
mcp.tool()(wine_pairing)
mcp.tool()(wine_description)
mcp.tool()(wine_recommendation)

# Misc
mcp.tool()(search_all_food)
mcp.tool()(search_food_videos)
mcp.tool()(quick_answer)
mcp.tool()(detect_food_in_text)
mcp.tool()(search_site_content)

# Menu items
mcp.tool()(search_menu_items)
mcp.tool()(get_menu_item_information)
mcp.tool()(autocomplete_menu_item_search)

# Products
mcp.tool()(search_grocery_products)
mcp.tool()(search_grocery_products_by_upc)
mcp.tool()(get_product_information)


if __name__ == "__main__":
    mcp.run()
