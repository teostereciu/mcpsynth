import json

from mcp.server.fastmcp import FastMCP

from generated_tools.recipes import search_recipes_complex, search_recipes_by_nutrients
from generated_tools.ingredients import (
    ingredient_search,
    get_ingredient_information,
    compute_ingredient_amount,
    convert_amounts,
    parse_ingredients,
    compute_glycemic_load,
    autocomplete_ingredient_search,
    get_ingredient_substitutes,
    get_ingredient_substitutes_by_id,
)
from generated_tools.meal_planning import (
    get_meal_plan_week,
    get_meal_plan_day,
    generate_meal_plan,
    add_to_meal_plan,
    clear_meal_plan_day,
    delete_from_meal_plan,
    get_meal_plan_templates,
    get_meal_plan_template,
    add_meal_plan_template,
    delete_meal_plan_template,
    get_shopping_list,
    add_to_shopping_list,
    delete_from_shopping_list,
    generate_shopping_list,
    search_custom_foods,
    connect_user,
)
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
mcp.tool()(compute_glycemic_load)
mcp.tool()(autocomplete_ingredient_search)
mcp.tool()(get_ingredient_substitutes)
mcp.tool()(get_ingredient_substitutes_by_id)

# Meal planning
mcp.tool()(get_meal_plan_week)
mcp.tool()(get_meal_plan_day)
mcp.tool()(generate_meal_plan)
mcp.tool()(add_to_meal_plan)
mcp.tool()(clear_meal_plan_day)
mcp.tool()(delete_from_meal_plan)
mcp.tool()(get_meal_plan_templates)
mcp.tool()(get_meal_plan_template)
mcp.tool()(add_meal_plan_template)
mcp.tool()(delete_meal_plan_template)
mcp.tool()(get_shopping_list)
mcp.tool()(add_to_shopping_list)
mcp.tool()(delete_from_shopping_list)
mcp.tool()(generate_shopping_list)
mcp.tool()(search_custom_foods)
mcp.tool()(connect_user)

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
