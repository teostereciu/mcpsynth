import generated_tools as tools
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("spoonacular")


# Recipes
mcp.tool()(tools.recipes_complex_search)
mcp.tool()(tools.recipes_find_by_nutrients)
mcp.tool()(tools.recipes_find_by_ingredients)
mcp.tool()(tools.recipes_get_information)
mcp.tool()(tools.recipes_get_information_bulk)
mcp.tool()(tools.recipes_get_similar)
mcp.tool()(tools.recipes_random)
mcp.tool()(tools.recipes_autocomplete)
mcp.tool()(tools.recipes_analyzed_instructions)
mcp.tool()(tools.recipes_extract)
mcp.tool()(tools.recipes_taste_widget_json)
mcp.tool()(tools.recipes_equipment_widget_json)
mcp.tool()(tools.recipes_price_breakdown_widget_json)
mcp.tool()(tools.recipes_ingredient_widget_json)
mcp.tool()(tools.recipes_nutrition_widget_json)

# Ingredients
mcp.tool()(tools.ingredients_search)
mcp.tool()(tools.ingredients_get_information)
mcp.tool()(tools.ingredients_compute_amount)
mcp.tool()(tools.recipes_convert_amounts)
mcp.tool()(tools.recipes_parse_ingredients)
mcp.tool()(tools.ingredients_glycemic_load)
mcp.tool()(tools.ingredients_autocomplete)
mcp.tool()(tools.ingredients_substitutes)
mcp.tool()(tools.ingredients_substitutes_by_id)

# Meal planning
mcp.tool()(tools.mealplanner_get_week)
mcp.tool()(tools.mealplanner_get_day)
mcp.tool()(tools.mealplanner_generate)
mcp.tool()(tools.mealplanner_add_item)
mcp.tool()(tools.mealplanner_clear_day)
mcp.tool()(tools.mealplanner_delete_item)
mcp.tool()(tools.mealplanner_get_templates)
mcp.tool()(tools.mealplanner_get_public_templates)
mcp.tool()(tools.mealplanner_get_template)
mcp.tool()(tools.mealplanner_add_template)
mcp.tool()(tools.mealplanner_delete_template)
mcp.tool()(tools.mealplanner_get_shopping_list)
mcp.tool()(tools.mealplanner_add_shopping_list_item)
mcp.tool()(tools.mealplanner_delete_shopping_list_item)
mcp.tool()(tools.mealplanner_generate_shopping_list)
mcp.tool()(tools.mealplanner_compute_shopping_list)
mcp.tool()(tools.custom_foods_search)
mcp.tool()(tools.mealplanner_connect_user)

# Wine
mcp.tool()(tools.wine_dish_pairing)
mcp.tool()(tools.wine_pairing)
mcp.tool()(tools.wine_description)
mcp.tool()(tools.wine_recommendation)

# Misc
mcp.tool()(tools.food_search_all)
mcp.tool()(tools.food_videos_search)
mcp.tool()(tools.recipes_quick_answer)
mcp.tool()(tools.food_detect)
mcp.tool()(tools.food_site_search)
mcp.tool()(tools.food_joke_random)
mcp.tool()(tools.food_trivia_random)
mcp.tool()(tools.food_converse)
mcp.tool()(tools.food_converse_suggest)
mcp.tool()(tools.recipes_nutrition_label)
mcp.tool()(tools.recipes_visualize_nutrition)

# Products
mcp.tool()(tools.products_search)
mcp.tool()(tools.products_get_by_upc)
mcp.tool()(tools.products_get_information)
mcp.tool()(tools.products_comparable_by_upc)
mcp.tool()(tools.products_autocomplete)
mcp.tool()(tools.products_classify)
mcp.tool()(tools.products_classify_batch)
mcp.tool()(tools.ingredients_map_to_products)

# Menu items
mcp.tool()(tools.menu_items_search)
mcp.tool()(tools.menu_items_get_information)
mcp.tool()(tools.menu_items_autocomplete)


if __name__ == "__main__":
    mcp.run()
