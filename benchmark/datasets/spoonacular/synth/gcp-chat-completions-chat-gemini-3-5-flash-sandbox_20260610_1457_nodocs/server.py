from mcp.server.fastmcp import FastMCP
from typing import Optional, List, Dict, Any

# Import tools from our modules
from generated_tools.recipes import (
    search_recipes,
    search_recipes_by_ingredients,
    search_recipes_by_nutrients,
    get_recipe_information,
    get_recipe_instructions,
    get_similar_recipes,
    get_recipe_equipment,
    get_recipe_price_breakdown,
    summarize_recipe,
    extract_recipe,
    convert_amounts,
    autocomplete_recipe_search
)
from generated_tools.ingredients import (
    search_ingredients,
    get_ingredient_information,
    parse_ingredients,
    autocomplete_ingredient_search
)
from generated_tools.meal_planning import generate_meal_plan
from generated_tools.nutrition import get_recipe_nutrition
from generated_tools.wine import get_wine_pairing, get_wine_description

# Initialize FastMCP server
mcp = FastMCP("Spoonacular Food API")

# Register Recipe Tools
@mcp.tool()
def search_recipes_tool(
    query: Optional[str] = None,
    cuisine: Optional[str] = None,
    excludeCuisine: Optional[str] = None,
    diet: Optional[str] = None,
    intolerances: Optional[str] = None,
    equipment: Optional[str] = None,
    includeIngredients: Optional[str] = None,
    excludeIngredients: Optional[str] = None,
    type: Optional[str] = None,
    instructionsRequired: Optional[bool] = None,
    fillIngredients: Optional[bool] = None,
    addRecipeInformation: Optional[bool] = None,
    addRecipeNutrition: Optional[bool] = None,
    author: Optional[str] = None,
    tags: Optional[str] = None,
    titleMatch: Optional[str] = None,
    maxReadyTime: Optional[int] = None,
    ignorePantry: Optional[bool] = None,
    sort: Optional[str] = None,
    sortDirection: Optional[str] = None,
    minCarbs: Optional[float] = None,
    maxCarbs: Optional[float] = None,
    minProtein: Optional[float] = None,
    maxProtein: Optional[float] = None,
    minCalories: Optional[float] = None,
    maxCalories: Optional[float] = None,
    minFat: Optional[float] = None,
    maxFat: Optional[float] = None,
    offset: Optional[int] = None,
    number: Optional[int] = None
) -> Dict[str, Any]:
    """
    Search through thousands of recipes using advanced filtering and search criteria.
    
    Args:
        query: The recipe name or keywords to search for (e.g., "pasta").
        cuisine: The cuisine(s) the recipes must match (comma-separated, e.g., "italian,mexican").
        excludeCuisine: The cuisine(s) the recipes must not match.
        diet: The diet for which the recipes must be suitable (e.g., "vegetarian", "vegan", "gluten free").
        intolerances: Food intolerances that the recipes must exclude (comma-separated, e.g., "dairy,egg").
        equipment: Equipment required for the recipe (comma-separated, e.g., "blender").
        includeIngredients: Ingredients that must be in the recipe (comma-separated, e.g., "tomato,cheese").
        excludeIngredients: Ingredients that must not be in the recipe.
        type: The type of recipe (e.g., "main course", "side dish", "dessert").
        instructionsRequired: Whether the recipes must have instructions.
        fillIngredients: Add information about the used and missing ingredients in each recipe.
        addRecipeInformation: If set to true, you get more information about the recipes returned.
        addRecipeNutrition: If set to true, you get nutritional information for each recipe.
        author: The username of the recipe author.
        tags: User tags that the recipes must have.
        titleMatch: A string that must be contained in the title of the recipe.
        maxReadyTime: The maximum time in minutes it should take to prepare/cook the recipe.
        ignorePantry: Whether to ignore typical pantry items like water, salt, flour, etc.
        sort: The strategy to sort results (e.g., "meta-score", "popularity", "healthiness", "price", "time").
        sortDirection: The direction of sorting ("asc" or "desc").
        minCarbs: Minimum amount of carbohydrates in grams.
        maxCarbs: Maximum amount of carbohydrates in grams.
        minProtein: Minimum amount of protein in grams.
        maxProtein: Maximum amount of protein in grams.
        minCalories: Minimum amount of calories.
        maxCalories: Maximum amount of calories.
        minFat: Minimum amount of fat in grams.
        maxFat: Maximum amount of fat in grams.
        offset: The number of results to skip (for pagination).
        number: The number of expected results (between 1 and 100).
    """
    return search_recipes(
        query=query, cuisine=cuisine, excludeCuisine=excludeCuisine, diet=diet,
        intolerances=intolerances, equipment=equipment, includeIngredients=includeIngredients,
        excludeIngredients=excludeIngredients, type=type, instructionsRequired=instructionsRequired,
        fillIngredients=fillIngredients, addRecipeInformation=addRecipeInformation,
        addRecipeNutrition=addRecipeNutrition, author=author, tags=tags, titleMatch=titleMatch,
        maxReadyTime=maxReadyTime, ignorePantry=ignorePantry, sort=sort, sortDirection=sortDirection,
        minCarbs=minCarbs, maxCarbs=maxCarbs, minProtein=minProtein, maxProtein=maxProtein,
        minCalories=minCalories, maxCalories=maxCalories, minFat=minFat, maxFat=maxFat,
        offset=offset, number=number
    )

@mcp.tool()
def search_recipes_by_ingredients_tool(
    ingredients: str,
    number: Optional[int] = None,
    ranking: Optional[int] = None,
    ignorePantry: Optional[bool] = None
) -> Dict[str, Any]:
    """
    Find recipes that use as many of the given ingredients as possible.
    
    Args:
        ingredients: A comma-separated list of ingredients that the recipes should contain (e.g., "apples,flour,sugar").
        number: The maximum number of recipes to return (default 10, max 100).
        ranking: Whether to maximize used ingredients (1) or minimize missing ingredients (2) first.
        ignorePantry: Whether to ignore typical pantry items like water, salt, flour, etc.
    """
    return search_recipes_by_ingredients(
        ingredients=ingredients, number=number, ranking=ranking, ignorePantry=ignorePantry
    )

@mcp.tool()
def search_recipes_by_nutrients_tool(
    minCarbs: Optional[float] = None,
    maxCarbs: Optional[float] = None,
    minProtein: Optional[float] = None,
    maxProtein: Optional[float] = None,
    minCalories: Optional[float] = None,
    maxCalories: Optional[float] = None,
    minFat: Optional[float] = None,
    maxFat: Optional[float] = None,
    number: Optional[int] = None,
    offset: Optional[int] = None
) -> Dict[str, Any]:
    """
    Find recipes which meet certain nutritional criteria.
    
    Args:
        minCarbs: Minimum carbs in grams.
        maxCarbs: Maximum carbs in grams.
        minProtein: Minimum protein in grams.
        maxProtein: Maximum protein in grams.
        minCalories: Minimum calories.
        maxCalories: Maximum calories.
        minFat: Minimum fat in grams.
        maxFat: Maximum fat in grams.
        number: The number of expected results (between 1 and 100).
        offset: The number of results to skip.
    """
    return search_recipes_by_nutrients(
        minCarbs=minCarbs, maxCarbs=maxCarbs, minProtein=minProtein, maxProtein=maxProtein,
        minCalories=minCalories, maxCalories=maxCalories, minFat=minFat, maxFat=maxFat,
        number=number, offset=offset
    )

@mcp.tool()
def get_recipe_information_tool(
    id: int,
    includeNutrition: Optional[bool] = None
) -> Dict[str, Any]:
    """
    Get full information about a recipe, including ingredients, instructions, and nutrition.
    
    Args:
        id: The recipe ID.
        includeNutrition: Include nutrition data in the recipe information.
    """
    return get_recipe_information(id=id, includeNutrition=includeNutrition)

@mcp.tool()
def get_recipe_instructions_tool(
    id: int,
    stepBreakdown: Optional[bool] = None
) -> Dict[str, Any]:
    """
    Get analyzed instructions for a recipe, broken down into steps, equipment, and ingredients.
    
    Args:
        id: The recipe ID.
        stepBreakdown: Whether to break down steps even more.
    """
    return get_recipe_instructions(id=id, stepBreakdown=stepBreakdown)

@mcp.tool()
def get_similar_recipes_tool(
    id: int,
    number: Optional[int] = None
) -> Dict[str, Any]:
    """
    Find recipes similar to the given recipe ID.
    
    Args:
        id: The recipe ID.
        number: The number of similar recipes to return (default 7).
    """
    return get_similar_recipes(id=id, number=number)

@mcp.tool()
def get_recipe_equipment_tool(id: int) -> Dict[str, Any]:
    """
    Get a list of equipment used in a recipe.
    
    Args:
        id: The recipe ID.
    """
    return get_recipe_equipment(id=id)

@mcp.tool()
def get_recipe_price_breakdown_tool(id: int) -> Dict[str, Any]:
    """
    Get the price breakdown of a recipe's ingredients.
    
    Args:
        id: The recipe ID.
    """
    return get_recipe_price_breakdown(id=id)

@mcp.tool()
def summarize_recipe_tool(id: int) -> Dict[str, Any]:
    """
    Get a short summary of a recipe, including its key characteristics.
    
    Args:
        id: The recipe ID.
    """
    return summarize_recipe(id=id)

@mcp.tool()
def extract_recipe_tool(
    url: str,
    forceExtraction: Optional[bool] = None,
    analyze: Optional[bool] = None,
    includeNutrition: Optional[bool] = None
) -> Dict[str, Any]:
    """
    Extract recipe data from any website/web page.
    
    Args:
        url: The URL of the recipe page.
        forceExtraction: Force extraction even if the site is not in the database.
        analyze: Analyze the recipe (extract ingredients, instructions, etc.).
        includeNutrition: Include nutrition data in the response.
    """
    return extract_recipe(
        url=url, forceExtraction=forceExtraction, analyze=analyze, includeNutrition=includeNutrition
    )

@mcp.tool()
def convert_amounts_tool(
    ingredientName: str,
    sourceAmount: float,
    sourceUnit: str,
    targetUnit: str
) -> Dict[str, Any]:
    """
    Convert an amount of an ingredient from one unit to another.
    
    Args:
        ingredientName: The name of the ingredient (e.g., "flour").
        sourceAmount: The amount to convert (e.g., 2.5).
        sourceUnit: The unit to convert from (e.g., "cups").
        targetUnit: The unit to convert to (e.g., "grams").
    """
    return convert_amounts(
        ingredientName=ingredientName, sourceAmount=sourceAmount, sourceUnit=sourceUnit, targetUnit=targetUnit
    )

@mcp.tool()
def autocomplete_recipe_search_tool(
    query: str,
    number: Optional[int] = None
) -> Dict[str, Any]:
    """
    Autocomplete a search query for recipes.
    
    Args:
        query: The query to autocomplete.
        number: The number of results to return (default 5).
    """
    return autocomplete_recipe_search(query=query, number=number)

# Register Ingredient Tools
@mcp.tool()
def search_ingredients_tool(
    query: str,
    addChildren: Optional[bool] = None,
    minProteinPercent: Optional[float] = None,
    maxProteinPercent: Optional[float] = None,
    minFatPercent: Optional[float] = None,
    maxFatPercent: Optional[float] = None,
    minCarbsPercent: Optional[float] = None,
    maxCarbsPercent: Optional[float] = None,
    metaInformation: Optional[bool] = None,
    intolerances: Optional[str] = None,
    sort: Optional[str] = None,
    sortDirection: Optional[str] = None,
    offset: Optional[int] = None,
    number: Optional[int] = None
) -> Dict[str, Any]:
    """
    Search for ingredients in the Spoonacular database.
    
    Args:
        query: The search query (e.g., "apple").
        addChildren: Whether to add children of the ingredient.
        minProteinPercent: Minimum protein percentage.
        maxProteinPercent: Maximum protein percentage.
        minFatPercent: Minimum fat percentage.
        maxFatPercent: Maximum fat percentage.
        minCarbsPercent: Minimum carbs percentage.
        maxCarbsPercent: Maximum carbs percentage.
        metaInformation: Whether to return more meta information about the ingredients.
        intolerances: A comma-separated list of intolerances (e.g., "dairy,gluten").
        sort: The strategy to sort results (e.g., "calories").
        sortDirection: The direction of sorting ("asc" or "desc").
        offset: The number of results to skip.
        number: The number of expected results (between 1 and 100).
    """
    return search_ingredients(
        query=query, addChildren=addChildren, minProteinPercent=minProteinPercent,
        maxProteinPercent=maxProteinPercent, minFatPercent=minFatPercent, maxFatPercent=maxFatPercent,
        minCarbsPercent=minCarbsPercent, maxCarbsPercent=maxCarbsPercent, metaInformation=metaInformation,
        intolerances=intolerances, sort=sort, sortDirection=sortDirection, offset=offset, number=number
    )

@mcp.tool()
def get_ingredient_information_tool(
    id: int,
    amount: Optional[float] = None,
    unit: Optional[str] = None
) -> Dict[str, Any]:
    """
    Get detailed information about an ingredient by its ID, including nutrition.
    
    Args:
        id: The ingredient ID.
        amount: The amount of the ingredient (e.g., 150).
        unit: The unit of the amount (e.g., "grams").
    """
    return get_ingredient_information(id=id, amount=amount, unit=unit)

@mcp.tool()
def parse_ingredients_tool(
    ingredientList: str,
    servings: float,
    includeNutrition: Optional[bool] = None
) -> Dict[str, Any]:
    """
    Parse a list of ingredient strings into structured data.
    
    Args:
        ingredientList: A newline-separated list of ingredient strings (e.g., "3 oz pork\n2 cups flour").
        servings: The number of servings.
        includeNutrition: Whether to include nutrition data in the response.
    """
    return parse_ingredients(
        ingredientList=ingredientList, servings=servings, includeNutrition=includeNutrition
    )

@mcp.tool()
def autocomplete_ingredient_search_tool(
    query: str,
    number: Optional[int] = None,
    metaInformation: Optional[bool] = None
) -> Dict[str, Any]:
    """
    Autocomplete a search query for ingredients.
    
    Args:
        query: The query to autocomplete.
        number: The number of results to return (default 5).
        metaInformation: Whether to return more meta information about the ingredients.
    """
    return autocomplete_ingredient_search(
        query=query, number=number, metaInformation=metaInformation
    )

# Register Meal Planning Tools
@mcp.tool()
def generate_meal_plan_tool(
    timeFrame: Optional[str] = None,
    targetCalories: Optional[float] = None,
    diet: Optional[str] = None,
    exclude: Optional[str] = None
) -> Dict[str, Any]:
    """
    Generate a meal plan for a day or a week based on target calories and dietary preferences.
    
    Args:
        timeFrame: The time frame of the meal plan ('day' or 'week').
        targetCalories: The target calories for the day/week.
        diet: The diet for which the meal plan must be suitable (e.g., "vegetarian", "vegan", "paleo").
        exclude: A comma-separated list of ingredients or allergens to exclude (e.g., "shellfish,olives").
    """
    return generate_meal_plan(
        timeFrame=timeFrame, targetCalories=targetCalories, diet=diet, exclude=exclude
    )

# Register Nutrition Tools
@mcp.tool()
def get_recipe_nutrition_tool(id: int) -> Dict[str, Any]:
    """
    Get nutritional information for a recipe by its ID.
    
    Args:
        id: The recipe ID.
    """
    return get_recipe_nutrition(id=id)

# Register Wine Tools
@mcp.tool()
def get_wine_pairing_tool(
    food: str,
    maxPrice: Optional[float] = None
) -> Dict[str, Any]:
    """
    Get wine pairings for a given food/dish.
    
    Args:
        food: The food/dish to pair wine with (e.g., "steak", "salmon").
        maxPrice: The maximum price of the wine in USD.
    """
    return get_wine_pairing(food=food, maxPrice=maxPrice)

@mcp.tool()
def get_wine_description_tool(wine: str) -> Dict[str, Any]:
    """
    Get a description and information about a specific wine type.
    
    Args:
        wine: The wine type (e.g., "merlot", "chardonnay").
    """
    return get_wine_description(wine=wine)

if __name__ == "__main__":
    mcp.run()
