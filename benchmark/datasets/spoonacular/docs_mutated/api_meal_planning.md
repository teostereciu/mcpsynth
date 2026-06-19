# Meal Planning

*Source: https://spoonacular.com/food-api/docs#Meal-Planning*

---

## Working with the Meal Planner

The spoonacular API allows you to interact with the spoonacular meal planner. Check out the endpoints under "Meal Planning" on the left to see what you can do.

Since meal plans and shopping lists are user-specific, you need to also pass a `username` and the user's `hash` besides your `apiKey`. This guarantees that you have the user's rights to manipulate her meal plan and/or shopping list.

If you want to create a [meal planner](https://spoonacular.com/meal-planner) like spoonacular's you can use these endpoints to realize it.

Here's an example workflow:

  1. Connect your app's user with spoonacular by calling Connect User.
  2. During step one you will get the user's `username` and `hash` from spoonacular. Save this on your side and connect it to your user. This allows you to make requests on the user's behalf.
  3. Now you can use the meal planning endpoints. For example, your app could do the following:
     1. Offer the user existing meal plans (e.g. vegetarian or keto meal plans) by calling Get Meal Plan Templates.
     2. Let the user add recipes, products, or simple foods to her meal plan via the Add to Meal Plan endpoint.
     3. Now that the user has food on the meal plan, you can let her generate a shopping list by calling the Generate Shopping List endpoint.
     4. If the user then is in the store you can show her the current shopping list via the Get Shopping List endpoint and let her remove items as she buys them using the Delete from Shopping List endpoint.


Feel free to reach out to us if you'd like to see specific functionality that we currently do not list here.

## Get Meal Plan Week

Retrieve a meal planned week for the given user. The `username` must be a spoonacular user and the `hash` must the the user's hash that can be found in his/her account.

Read more about working with the meal planner.

GET

https://api.spoonacular.com/mealplanner/{username}/week/{start-date}

#### Headers

Response Headers:

  * `Content-Type: application/json`


#### Parameters

Name | Type | Example | Description
---|---|---|---
**`username`** | string | dsky | The username.
**`start-date`** | string | 2020-06-01 | The start date of the meal planned week in the format yyyy-mm-dd.
**`hash`** | string | 4b5v4398573406 | The private hash for the username.

Example Request and Response

GET

https://api.spoonacular.com/mealplanner/dsky/week/2020-06-01?hash=4b5v4398573406


    {
        "days": [
            {
                "nutritionSummary": {
                    "nutrients": [
                        {
                            "name": "Calories",
                            "amount": 310,
                            "unit": "cal",
                            "percentOfDailyNeeds": 16
                        },
                        {
                            "name": "Fat",
                            "amount": 25,
                            "unit": "g",
                            "percentOfDailyNeeds": 38
                        },
                        {
                            "name": "Carbohydrates",
                            "amount": 1,
                            "unit": "g",
                            "percentOfDailyNeeds": 0
                        },
                        {
                            "name": "Protein",
                            "amount": 20,
                            "unit": "g",
                            "percentOfDailyNeeds": 40
                        }
                    ]
                },
                "nutritionSummaryBreakfast": {
                    "nutrients": [
                        {
                            "name": "Calories",
                            "amount": 0,
                            "unit": "cal",
                            "percentOfDailyNeeds": 0
                        },
                        {
                            "name": "Fat",
                            "amount": 0,
                            "unit": "g",
                            "percentOfDailyNeeds": 0
                        },
                        {
                            "name": "Carbohydrates",
                            "amount": 0,
                            "unit": "g",
                            "percentOfDailyNeeds": 0
                        },
                        {
                            "name": "Protein",
                            "amount": 0,
                            "unit": "g",
                            "percentOfDailyNeeds": 0
                        }
                    ]
                },
                "nutritionSummaryLunch": {
                    "nutrients": [
                        {
                            "name": "Calories",
                            "amount": 310,
                            "unit": "cal",
                            "percentOfDailyNeeds": 16
                        },
                        {
                            "name": "Fat",
                            "amount": 25,
                            "unit": "g",
                            "percentOfDailyNeeds": 38
                        },
                        {
                            "name": "Carbohydrates",
                            "amount": 1,
                            "unit": "g",
                            "percentOfDailyNeeds": 0
                        },
                        {
                            "name": "Protein",
                            "amount": 20,
                            "unit": "g",
                            "percentOfDailyNeeds": 40
                        }
                    ]
                },
                "nutritionSummaryDinner": {
                    "nutrients": [
                        {
                            "name": "Calories",
                            "amount": 0,
                            "unit": "cal",
                            "percentOfDailyNeeds": 0
                        },
                        {
                            "name": "Fat",
                            "amount": 0,
                            "unit": "g",
                            "percentOfDailyNeeds": 0
                        },
                        {
                            "name": "Carbohydrates",
                            "amount": 0,
                            "unit": "g",
                            "percentOfDailyNeeds": 0
                        },
                        {
                            "name": "Protein",
                            "amount": 0,
                            "unit": "g",
                            "percentOfDailyNeeds": 0
                        }
                    ]
                },
                "date": 1589155200,
                "day": "Monday",
                "items": [
                    {
                        "id": 1976489,
                        "slot": 1,
                        "position": 1,
                        "type": "RECIPE",
                        "value": {
                            "servings": 2,
                            "id": 1023004,
                            "title": "Foolproof Meatloaf",
                            "imageType": ""
                        }
                    },
                    {
                        "id": 1976490,
                        "slot": 2,
                        "position": 2,
                        "type": "CUSTOM_FOOD",
                        "value": {
                            "servings": 1,
                            "id": 345,
                            "title": "Denn's Lamb Bratwurst - 1/2 Pkg",
                            "image": "https://img.spoonacular.com/ingredients_100x100/bratwurst.jpg"
                        }
                    }
                ]
            },
            {
                "nutritionSummary": {
                    "nutrients": [
                        {
                            "name": "Calories",
                            "amount": 200,
                            "unit": "cal",
                            "percentOfDailyNeeds": 10
                        },
                        {
                            "name": "Fat",
                            "amount": 1,
                            "unit": "g",
                            "percentOfDailyNeeds": 1
                        },
                        {
                            "name": "Carbohydrates",
                            "amount": 52,
                            "unit": "g",
                            "percentOfDailyNeeds": 17
                        },
                        {
                            "name": "Protein",
                            "amount": 2,
                            "unit": "g",
                            "percentOfDailyNeeds": 4
                        }
                    ]
                },
                "nutritionSummaryBreakfast": {
                    "nutrients": [
                        {
                            "name": "Calories",
                            "amount": 200,
                            "unit": "cal",
                            "percentOfDailyNeeds": 10
                        },
                        {
                            "name": "Fat",
                            "amount": 1,
                            "unit": "g",
                            "percentOfDailyNeeds": 1
                        },
                        {
                            "name": "Carbohydrates",
                            "amount": 52,
                            "unit": "g",
                            "percentOfDailyNeeds": 17
                        },
                        {
                            "name": "Protein",
                            "amount": 2,
                            "unit": "g",
                            "percentOfDailyNeeds": 4
                        }
                    ]
                },
                "nutritionSummaryLunch": {
                    "nutrients": [
                        {
                            "name": "Calories",
                            "amount": 0,
                            "unit": "cal",
                            "percentOfDailyNeeds": 0
                        },
                        {
                            "name": "Fat",
                            "amount": 0,
                            "unit": "g",
                            "percentOfDailyNeeds": 0
                        },
                        {
                            "name": "Carbohydrates",
                            "amount": 0,
                            "unit": "g",
                            "percentOfDailyNeeds": 0
                        },
                        {
                            "name": "Protein",
                            "amount": 0,
                            "unit": "g",
                            "percentOfDailyNeeds": 0
                        }
                    ]
                },
                "nutritionSummaryDinner": {
                    "nutrients": [
                        {
                            "name": "Calories",
                            "amount": 0,
                            "unit": "cal",
                            "percentOfDailyNeeds": 0
                        },
                        {
                            "name": "Fat",
                            "amount": 0,
                            "unit": "g",
                            "percentOfDailyNeeds": 0
                        },
                        {
                            "name": "Carbohydrates",
                            "amount": 0,
                            "unit": "g",
                            "percentOfDailyNeeds": 0
                        },
                        {
                            "name": "Protein",
                            "amount": 0,
                            "unit": "g",
                            "percentOfDailyNeeds": 0
                        }
                    ]
                },
                "date": 1589241600,
                "day": "Tuesday",
                "items": [
                    {
                        "id": 1976491,
                        "slot": 1,
                        "position": 3,
                        "type": "INGREDIENTS",
                        "value": {
                            "title": "",
                            "servings": 1,
                            "ingredients": [
                                {
                                    "name": "apple",
                                    "unit": "",
                                    "amount": "1",
                                    "image": "https://img.spoonacular.com/ingredients_100x100/apple.jpg"
                                },
                                {
                                    "name": "banana",
                                    "unit": "",
                                    "amount": "1",
                                    "image": "https://img.spoonacular.com/ingredients_100x100/bananas.jpg"
                                }
                            ]
                        }
                    }
                ]
            },
            {
                "nutritionSummary": {
                    "nutrients": [
                        {
                            "name": "Calories",
                            "amount": 180,
                            "unit": "cal",
                            "percentOfDailyNeeds": 9
                        },
                        {
                            "name": "Fat",
                            "amount": 6,
                            "unit": "g",
                            "percentOfDailyNeeds": 9
                        },
                        {
                            "name": "Carbohydrates",
                            "amount": 22,
                            "unit": "g",
                            "percentOfDailyNeeds": 7
                        },
                        {
                            "name": "Protein",
                            "amount": 10,
                            "unit": "g",
                            "percentOfDailyNeeds": 20
                        }
                    ]
                },
                "nutritionSummaryBreakfast": {
                    "nutrients": [
                        {
                            "name": "Calories",
                            "amount": 180,
                            "unit": "cal",
                            "percentOfDailyNeeds": 9
                        },
                        {
                            "name": "Fat",
                            "amount": 6,
                            "unit": "g",
                            "percentOfDailyNeeds": 9
                        },
                        {
                            "name": "Carbohydrates",
                            "amount": 22,
                            "unit": "g",
                            "percentOfDailyNeeds": 7
                        },
                        {
                            "name": "Protein",
                            "amount": 10,
                            "unit": "g",
                            "percentOfDailyNeeds": 20
                        }
                    ]
                },
                "nutritionSummaryLunch": {
                    "nutrients": [
                        {
                            "name": "Calories",
                            "amount": 0,
                            "unit": "cal",
                            "percentOfDailyNeeds": 0
                        },
                        {
                            "name": "Fat",
                            "amount": 0,
                            "unit": "g",
                            "percentOfDailyNeeds": 0
                        },
                        {
                            "name": "Carbohydrates",
                            "amount": 0,
                            "unit": "g",
                            "percentOfDailyNeeds": 0
                        },
                        {
                            "name": "Protein",
                            "amount": 0,
                            "unit": "g",
                            "percentOfDailyNeeds": 0
                        }
                    ]
                },
                "nutritionSummaryDinner": {
                    "nutrients": [
                        {
                            "name": "Calories",
                            "amount": 0,
                            "unit": "cal",
                            "percentOfDailyNeeds": 0
                        },
                        {
                            "name": "Fat",
                            "amount": 0,
                            "unit": "g",
                            "percentOfDailyNeeds": 0
                        },
                        {
                            "name": "Carbohydrates",
                            "amount": 0,
                            "unit": "g",
                            "percentOfDailyNeeds": 0
                        },
                        {
                            "name": "Protein",
                            "amount": 0,
                            "unit": "g",
                            "percentOfDailyNeeds": 0
                        }
                    ]
                },
                "date": 1589328000,
                "day": "Wednesday",
                "items": [
                    {
                        "id": 1976492,
                        "slot": 1,
                        "position": 4,
                        "type": "MENU_ITEM",
                        "value": {
                            "servings": 1,
                            "id": 378557,
                            "title": "BBQ Steak Pizza, 9",
                            "image": "https://img.spoonacular.com/menu-items/378557-312x231.png",
                            "imageType": "png"
                        }
                    }
                ]
            }
        ]
    }

#### Quotas

Calling this endpoint requires

1 point

. Learn more about quotas.

#### Need Help? Just ask!

Ask AI

## Get Meal Plan Day

Retrieve a meal planned day for the given user. The `username` must be a spoonacular user and the `hash` must the the user's hash that can be found in his/her account.

Read more about working with the meal planner.

GET

https://api.spoonacular.com/mealplanner/{username}/day/{date}

#### Headers

Response Headers:

  * `Content-Type: application/json`


#### Parameters

Name | Type | Example | Description
---|---|---|---
**`username`** | string | dsky | The username.
**`date`** | string | 2020-06-01 | The date of the meal planned day in the format yyyy-mm-dd.
**`hash`** | string | 4b5v4398573406 | The private hash for the username.

Example Request and Response

GET

https://api.spoonacular.com/mealplanner/dsky/day/2020-06-01?hash=4b5v4398573406


    {
        "nutritionSummary": {
            "nutrients": [
                {
                    "name": "Calories",
                    "amount": 310,
                    "unit": "cal",
                    "percentOfDailyNeeds": 16
                },
                {
                    "name": "Fat",
                    "amount": 25,
                    "unit": "g",
                    "percentOfDailyNeeds": 38
                },
                {
                    "name": "Carbohydrates",
                    "amount": 1,
                    "unit": "g",
                    "percentOfDailyNeeds": 0
                },
                {
                    "name": "Protein",
                    "amount": 20,
                    "unit": "g",
                    "percentOfDailyNeeds": 40
                }
            ]
        },
        "nutritionSummaryBreakfast": {
            "nutrients": [
                {
                    "name": "Calories",
                    "amount": 0,
                    "unit": "cal",
                    "percentOfDailyNeeds": 0
                },
                {
                    "name": "Fat",
                    "amount": 0,
                    "unit": "g",
                    "percentOfDailyNeeds": 0
                },
                {
                    "name": "Carbohydrates",
                    "amount": 0,
                    "unit": "g",
                    "percentOfDailyNeeds": 0
                },
                {
                    "name": "Protein",
                    "amount": 0,
                    "unit": "g",
                    "percentOfDailyNeeds": 0
                }
            ]
        },
        "nutritionSummaryLunch": {
            "nutrients": [
                {
                    "name": "Calories",
                    "amount": 310,
                    "unit": "cal",
                    "percentOfDailyNeeds": 16
                },
                {
                    "name": "Fat",
                    "amount": 25,
                    "unit": "g",
                    "percentOfDailyNeeds": 38
                },
                {
                    "name": "Carbohydrates",
                    "amount": 1,
                    "unit": "g",
                    "percentOfDailyNeeds": 0
                },
                {
                    "name": "Protein",
                    "amount": 20,
                    "unit": "g",
                    "percentOfDailyNeeds": 40
                }
            ]
        },
        "nutritionSummaryDinner": {
            "nutrients": [
                {
                    "name": "Calories",
                    "amount": 0,
                    "unit": "cal",
                    "percentOfDailyNeeds": 0
                },
                {
                    "name": "Fat",
                    "amount": 0,
                    "unit": "g",
                    "percentOfDailyNeeds": 0
                },
                {
                    "name": "Carbohydrates",
                    "amount": 0,
                    "unit": "g",
                    "percentOfDailyNeeds": 0
                },
                {
                    "name": "Protein",
                    "amount": 0,
                    "unit": "g",
                    "percentOfDailyNeeds": 0
                }
            ]
        },
        "date": 1589155200,
        "day": "Monday",
        "items": [
            {
                "id": 1976489,
                "slot": 1,
                "position": 1,
                "type": "RECIPE",
                "value": {
                    "servings": 2,
                    "id": 1023004,
                    "title": "Foolproof Meatloaf",
                    "imageType": ""
                }
            },
            {
                "id": 1976490,
                "slot": 2,
                "position": 2,
                "type": "CUSTOM_FOOD",
                "value": {
                    "servings": 1,
                    "id": 345,
                    "title": "Denn's Lamb Bratwurst - 1/2 Pkg",
                    "image": "https://img.spoonacular.com/ingredients_100x100/bratwurst.jpg"
                }
            }
        ]
    }

#### Quotas

Calling this endpoint requires

1 point

. Learn more about quotas.

#### Need Help? Just ask!

Ask AI

## Generate Meal Plan

Generate a meal plan with three meals per day (breakfast, lunch, and dinner).

Read more about working with the meal planner.

GET

https://api.spoonacular.com/mealplanner/generate

#### Headers

Response Headers:

  * `Content-Type: application/json`


#### Parameters

Name | Type | Example | Description
---|---|---|---
`timeFrame` | string | day | Either for one "day" or an entire "week".
`calorie_target` | number | 2000 | What is the caloric target for one day? The meal plan generator will try to get as close as possible to that goal.
`diet_type` | string | vegetarian | Enter a diet_type that the meal plan has to adhere to. See a full [list of supported diets](/food-api/docs#Diets).
`exclude` | string | shellfish, olives | A comma-separated list of allergens or ingredients that must be excluded.

Example Request and Response

GET

https://api.spoonacular.com/mealplanner/generate?timeFrame=day


    {
        "meals": [
            {
                "id": 655219,
                "title": "Peanut Butter And Chocolate Oatmeal",
                "imageType": "jpg",
                "readyInMinutes": 45,
                "servings": 1,
                "sourceUrl": "https://spoonacular.com/recipes/peanut-butter-and-chocolate-oatmeal-655219"
            },
            {
                "id": 649931,
                "title": "Lentil Salad With Vegetables",
                "imageType": "jpg",
                "readyInMinutes": 45,
                "servings": 4,
                "sourceUrl": "https://spoonacular.com/recipes/lentil-salad-with-vegetables-649931"
            },
            {
                "id": 632854,
                "title": "Asian Noodles",
                "imageType": "jpg",
                "readyInMinutes": 45,
                "servings": 4,
                "sourceUrl": "https://spoonacular.com/recipes/asian-noodles-632854"
            }
        ],
        "nutrients": {
            "calories": 1735.81,
            "carbohydrates": 235.17,
            "fat": 69.22,
            "protein": 55.43
        }
    }

#### Quotas

Calling this endpoint requires

1 point

. Learn more about quotas.

#### Need Help? Just ask!

Ask AI

## Add to Meal Plan

Add an item to the user's meal plan.

Read more about working with the meal planner.

POST

https://api.spoonacular.com/mealplanner/{username}/items

#### Headers

Response Headers:

  * `Content-Type: application/json`


#### Parameters

Name | Type | Example | Description
---|---|---|---
**`username`** | string | dsky | The username.
**`hash`** | string | 4b5v4398573406 | The private hash for the username.

Example Request and Body

POST

https://api.spoonacular.com/mealplanner/dsky/items


    {
        "date": 1589500800,
        "slot": 1,
        "position": 0,
        "type": "INGREDIENTS",
        "value": {
            "ingredients": [
                {
                    "name": "1 banana"
                }
            ]
        }
    }

The field `date` is the timestamp of the day the item should be added to.

The field `slot` is either 1, 2, or 3 for breakfast, lunch, or dinner respectively.

The field `position` is the order in the slot.

The field `type` is either INGREDIENTS for simple foods such as "1 banana", PRODUCT for a grocery product, MENU_ITEM for a menu item, RECIPE for a recipe, or CUSTOM_FOOD for custom food.

The field `value` is information about the item and the structure depends on what `type` is set to. The example above shows what it would look like for type ingredient. If the type is PRODUCT, MENU_ITEM, or RECIPE the value must contain the field `servings` and the `id` of the respective item.

Example for adding a recipe with `type` RECIPE.


    {
        "date": 1589500800,
        "slot": 1,
        "position": 0,
        "type": "RECIPE",
        "value": {
            "id": 296213,
            "servings": 2,
            "title": "Spinach Salad with Roasted Vegetables and Spiced Chickpea",
            "imageType": "jpg",
        }
    }

Example for adding a grocery product with `type` PRODUCT.


    {
        "date": 1589500800,
        "slot": 1,
        "position": 0,
        "type": "PRODUCT",
        "value": {
            "id": 183433,
            "servings": 1,
            "title": "Ahold Lasagna with Meat Sauce",
            "imageType": "jpg"
        }
    }

Example for adding a menu item with `type` MENU_ITEM.


    {
        "date": 1589500800,
        "slot": 1,
        "position": 0,
        "type": "MENU_ITEM",
        "value": {
            "id": 378557,
            "servings": 1,
            "title": "Pizza 73 BBQ Steak Pizza, 9",
            "imageType": "png"
        }
    }

Example for adding a custom food with `type` CUSTOM_FOOD.


    {
        "date": 1589500800,
        "slot": 1,
        "position": 0,
        "type": "CUSTOM_FOOD",
        "value": {
            "id": 348,
            "servings": 1,
            "title": "Aldi Spicy Cashews - 30g",
            "image": "https://img.spoonacular.com/ingredients_100x100/cashews.jpg"
        }
    }

Example for adding simple foods with `type` INGREDIENTS. You can either just pass a name with amount and unit or pass a more complex object with amount, name, and unit in separate fields (recommended).


    {
        "date": 1589500800,
        "slot": 1,
        "position": 0,
        "type": "INGREDIENTS",
        "value": {
            "ingredients": [
                {
                    "name": "1 banana"
                },
                {
                    "name": "coffee",
                    "unit": "cup",
                    "amount": "1",
                    "image": "https://img.spoonacular.com/ingredients_100x100/brewed-coffee.jpg"
                },
            ]
        }
    }

Alternatively you can add all items of a meal plan template to a user's meal plan with one call. Just pass the `mealPlanTemplateId` and the `startDate` in your request. The user's meal plan will be filled with template items starting on startDate (day 1 of the specified meal plan template).


    {
        "mealPlanTemplateId": 120,
      	"startDate": 1596575356,
    }

You can also add multiple items with one request. Just pass a JSON Array with multiple items. See below for an example.


    [
        {
            "date": 1589500800,
            "slot": 1,
            "position": 0,
            "type": "INGREDIENTS",
            "value": {
                "ingredients": [
                    {
                        "name": "1 banana"
                    },
                    {
                        "name": "coffee",
                        "unit": "cup",
                        "amount": "1",
                        "image": "https://img.spoonacular.com/ingredients_100x100/brewed-coffee.jpg"
                    },
                ]
            }
        },
        {
            "date": 1589500800,
            "slot": 2,
            "position": 0,
            "type": "CUSTOM_FOOD",
            "value": {
                "id": 348,
                "servings": 1,
                "title": "Aldi Spicy Cashews - 30g",
                "image": "https://img.spoonacular.com/ingredients_100x100/cashews.jpg"
            }
        }
    ]

#### Quotas

Calling this endpoint requires

1 point

and

0.1 points

per additional item added. Learn more about quotas.

#### Need Help? Just ask!

Ask AI

## Clear Meal Plan Day

Delete all planned items from the user's meal plan for a specific day.

Read more about working with the meal planner.

DELETE

https://api.spoonacular.com/mealplanner/{username}/day/{date}

#### Headers

Response Headers:

  * `Content-Type: application/json`


#### Parameters

Name | Type | Example | Description
---|---|---|---
**`username`** | string | dsky | The username.
**`date`** | string | 2020-06-01 | The date in the format yyyy-mm-dd.
**`hash`** | string | 4b5v4398573406 | The private hash for the username.

Example Request and Response

DELETE

https://api.spoonacular.com/mealplanner/dsky/day/2020-06-01?hash=4b5v4398573406

#### Quotas

Calling this endpoint requires

1 point

. Learn more about quotas.

#### Need Help? Just ask!

Ask AI

## Delete from Meal Plan

Delete an item from the user's meal plan.

Read more about working with the meal planner.

DELETE

https://api.spoonacular.com/mealplanner/{username}/items/{id}

#### Headers

Response Headers:

  * `Content-Type: application/json`


#### Parameters

Name | Type | Example | Description
---|---|---|---
**`username`** | string | dsky | The username.
**`id`** | number | 15678 | The shopping list item id.
**`hash`** | string | 4b5v4398573406 | The private hash for the username.

Example Request and Response

DELETE

https://api.spoonacular.com/mealplanner/dsky/items/15678?hash=4b5v4398573406

#### Quotas

Calling this endpoint requires

1 point

. Learn more about quotas.

#### Need Help? Just ask!

Ask AI

## Get Meal Plan Templates

Get meal plan templates from user or public ones.

Read more about working with the meal planner.

#### Headers

Response Headers:

  * `Content-Type: application/json`


#### Parameters

Name | Type | Example | Description
---|---|---|---
**`username`** | string | dsky | The username.
**`hash`** | string | 4b5v4398573406 | The private hash for the username.

Get user's templates.

GET

https://api.spoonacular.com/mealplanner/{username}/templates


    {
        "templates": [
            {
                "id": 37,
                "name": "Busy Work Week"
            },
            {
                "id": 480,
                "name": "Keto Meal Plan"
            },
            {
                "id": 120,
                "name": "Not-So-Strict Paleo Meal Plan"
            },
            {
                "id": 451,
                "name": "Week 1 Meal Plan"
            },
            {
                "id": 581,
                "name": "Whole30 Meal Plan"
            }
        ]
    }

Get public templates.

GET

https://api.spoonacular.com/mealplanner/public-templates


    {
        "templates": [
            {
                "id": 37,
                "name": "Busy Work Week"
            },
            {
                "id": 480,
                "name": "Keto Meal Plan"
            },
            {
                "id": 120,
                "name": "Not-So-Strict Paleo Meal Plan"
            },
            {
                "id": 451,
                "name": "Week 1 Meal Plan"
            },
            {
                "id": 581,
                "name": "Whole30 Meal Plan"
            }
        ]
    }

#### Quotas

Calling this endpoint requires

1 point

. Learn more about quotas.

#### Need Help? Just ask!

Ask AI

## Get Meal Plan Template

Get information about a meal plan template.

Read more about working with the meal planner.

GET

https://api.spoonacular.com/mealplanner/{username}/templates/{id}

#### Headers

Response Headers:

  * `Content-Type: application/json`


#### Parameters

Name | Type | Example | Description
---|---|---|---
**`username`** | string | dsky | The username.
**`id`** | number | 15678 | The shopping list item id.
**`hash`** | string | 4b5v4398573406 | The private hash for the username.

Example Request and Response

GET

https://api.spoonacular.com/mealplanner/dsky/templates/128?hash=4b5v4398573406


    {
        "id": 128,
        "name": "1500 Calorie Meal Plan",
        "days": [
            {
                "nutritionSummary": {
                    "nutrients": [
                        {
                            "name": "Calories",
                            "amount": 1293,
                            "unit": "cal",
                            "percentOfDailyNeeds": 65
                        },
                        {
                            "name": "Fat",
                            "amount": 65,
                            "unit": "g",
                            "percentOfDailyNeeds": 100
                        },
                        {
                            "name": "Carbohydrates",
                            "amount": 102,
                            "unit": "g",
                            "percentOfDailyNeeds": 34
                        },
                        {
                            "name": "Protein",
                            "amount": 83,
                            "unit": "g",
                            "percentOfDailyNeeds": 166
                        }
                    ]
                },
                "nutritionSummaryBreakfast": {
                    "nutrients": [
                        {
                            "name": "Calories",
                            "amount": 132,
                            "unit": "cal",
                            "percentOfDailyNeeds": 7
                        },
                        {
                            "name": "Fat",
                            "amount": 3,
                            "unit": "g",
                            "percentOfDailyNeeds": 4
                        },
                        {
                            "name": "Carbohydrates",
                            "amount": 25,
                            "unit": "g",
                            "percentOfDailyNeeds": 8
                        },
                        {
                            "name": "Protein",
                            "amount": 3,
                            "unit": "g",
                            "percentOfDailyNeeds": 5
                        }
                    ]
                },
                "nutritionSummaryLunch": {
                    "nutrients": [
                        {
                            "name": "Calories",
                            "amount": 455,
                            "unit": "cal",
                            "percentOfDailyNeeds": 23
                        },
                        {
                            "name": "Fat",
                            "amount": 34,
                            "unit": "g",
                            "percentOfDailyNeeds": 52
                        },
                        {
                            "name": "Carbohydrates",
                            "amount": 1,
                            "unit": "g",
                            "percentOfDailyNeeds": 0
                        },
                        {
                            "name": "Protein",
                            "amount": 35,
                            "unit": "g",
                            "percentOfDailyNeeds": 70
                        }
                    ]
                },
                "nutritionSummaryDinner": {
                    "nutrients": [
                        {
                            "name": "Calories",
                            "amount": 706,
                            "unit": "cal",
                            "percentOfDailyNeeds": 35
                        },
                        {
                            "name": "Fat",
                            "amount": 29,
                            "unit": "g",
                            "percentOfDailyNeeds": 45
                        },
                        {
                            "name": "Carbohydrates",
                            "amount": 76,
                            "unit": "g",
                            "percentOfDailyNeeds": 25
                        },
                        {
                            "name": "Protein",
                            "amount": 46,
                            "unit": "g",
                            "percentOfDailyNeeds": 91
                        }
                    ]
                },
                "day": "1",
                "items": [
                    {
                        "id": 2403,
                        "slot": 1,
                        "position": 0,
                        "type": "RECIPE",
                        "value": {
                            "id": 630657,
                            "title": "Double Chocolate Protein Cookies",
                            "imageType": "jpg"
                        }
                    },
                    {
                        "id": 2404,
                        "slot": 1,
                        "position": 0,
                        "type": "INGREDIENTS",
                        "value": {
                            "name": "",
                            "servings": "1",
                            "ingredients": [
                                {
                                    "name": "orange",
                                    "image": "https://img.spoonacular.com/ingredients_100x100/orange.jpg",
                                    "amount": 1,
                                    "unit": ""
                                }
                            ]
                        }
                    },
                    {
                        "id": 2405,
                        "slot": 2,
                        "position": 0,
                        "type": "RECIPE",
                        "value": {
                            "id": 296213,
                            "title": "Spinach Salad with Roasted Vegetables and Spiced Chickpea",
                            "imageType": "jpg"
                        }
                    },
                    {
                        "id": 2406,
                        "slot": 3,
                        "position": 0,
                        "type": "RECIPE",
                        "value": {
                            "id": 237677,
                            "title": "Chicken Parmesan with Spaghetti",
                            "imageType": "jpg"
                        }
                    },
                    {
                        "id": 2407,
                        "slot": 3,
                        "position": 0,
                        "type": "INGREDIENTS",
                        "value": {
                            "name": "",
                            "servings": "1",
                            "ingredients": [
                                {
                                    "name": "broccoli",
                                    "image": "https://img.spoonacular.com/ingredients_100x100/broccoli.jpg",
                                    "amount": 1,
                                    "unit": "cup"
                                }
                            ]
                        }
                    },
                    {
                        "id": 2408,
                        "slot": 3,
                        "position": 0,
                        "type": "PRODUCT",
                        "value": {
                            "id": 146191,
                            "title": "Lindt Dark Chocolate",
                            "imageType": "jpg"
                        }
                    }
                ]
            },
            {
                "nutritionSummary": {
                    "nutrients": [
                        {
                            "name": "Calories",
                            "amount": 1386,
                            "unit": "cal",
                            "percentOfDailyNeeds": 69
                        },
                        {
                            "name": "Fat",
                            "amount": 66,
                            "unit": "g",
                            "percentOfDailyNeeds": 102
                        },
                        {
                            "name": "Carbohydrates",
                            "amount": 162,
                            "unit": "g",
                            "percentOfDailyNeeds": 54
                        },
                        {
                            "name": "Protein",
                            "amount": 48,
                            "unit": "g",
                            "percentOfDailyNeeds": 96
                        }
                    ]
                },
                "nutritionSummaryBreakfast": {
                    "nutrients": [
                        {
                            "name": "Calories",
                            "amount": 239,
                            "unit": "cal",
                            "percentOfDailyNeeds": 12
                        },
                        {
                            "name": "Fat",
                            "amount": 11,
                            "unit": "g",
                            "percentOfDailyNeeds": 17
                        },
                        {
                            "name": "Carbohydrates",
                            "amount": 34,
                            "unit": "g",
                            "percentOfDailyNeeds": 11
                        },
                        {
                            "name": "Protein",
                            "amount": 5,
                            "unit": "g",
                            "percentOfDailyNeeds": 9
                        }
                    ]
                },
                "nutritionSummaryLunch": {
                    "nutrients": [
                        {
                            "name": "Calories",
                            "amount": 732,
                            "unit": "cal",
                            "percentOfDailyNeeds": 37
                        },
                        {
                            "name": "Fat",
                            "amount": 33,
                            "unit": "g",
                            "percentOfDailyNeeds": 51
                        },
                        {
                            "name": "Carbohydrates",
                            "amount": 91,
                            "unit": "g",
                            "percentOfDailyNeeds": 30
                        },
                        {
                            "name": "Protein",
                            "amount": 22,
                            "unit": "g",
                            "percentOfDailyNeeds": 44
                        }
                    ]
                },
                "nutritionSummaryDinner": {
                    "nutrients": [
                        {
                            "name": "Calories",
                            "amount": 414,
                            "unit": "cal",
                            "percentOfDailyNeeds": 21
                        },
                        {
                            "name": "Fat",
                            "amount": 22,
                            "unit": "g",
                            "percentOfDailyNeeds": 33
                        },
                        {
                            "name": "Carbohydrates",
                            "amount": 37,
                            "unit": "g",
                            "percentOfDailyNeeds": 12
                        },
                        {
                            "name": "Protein",
                            "amount": 21,
                            "unit": "g",
                            "percentOfDailyNeeds": 43
                        }
                    ]
                },
                "day": "2",
                "items": [
                    {
                        "id": 2409,
                        "slot": 1,
                        "position": 0,
                        "type": "PRODUCT",
                        "value": {
                            "id": 101999,
                            "title": "Greek Gods Yogurt",
                            "imageType": "jpg"
                        }
                    },
                    {
                        "id": 2410,
                        "slot": 1,
                        "position": 0,
                        "type": "INGREDIENTS",
                        "value": {
                            "name": "",
                            "servings": "1",
                            "ingredients": [
                                {
                                    "name": "berries",
                                    "image": "https://img.spoonacular.com/ingredients_100x100/berries-mixed.jpg",
                                    "amount": 1,
                                    "unit": "cup"
                                }
                            ]
                        }
                    },
                    {
                        "id": 2411,
                        "slot": 2,
                        "position": 0,
                        "type": "RECIPE",
                        "value": {
                            "id": 516377,
                            "title": "Southwest Quinoa Salad",
                            "imageType": "jpg"
                        }
                    },
                    {
                        "id": 2412,
                        "slot": 3,
                        "position": 0,
                        "type": "RECIPE",
                        "value": {
                            "id": 247683,
                            "title": "Pesto Caprese Omelette",
                            "imageType": "jpg"
                        }
                    },
                    {
                        "id": 2413,
                        "slot": 3,
                        "position": 0,
                        "type": "RECIPE",
                        "value": {
                            "id": 484337,
                            "title": "One Ingredient Banana Ice Cream",
                            "imageType": "jpg"
                        }
                    }
                ]
            },
            {
                "nutritionSummary": {
                    "nutrients": [
                        {
                            "name": "Calories",
                            "amount": 1589,
                            "unit": "cal",
                            "percentOfDailyNeeds": 79
                        },
                        {
                            "name": "Fat",
                            "amount": 77,
                            "unit": "g",
                            "percentOfDailyNeeds": 118
                        },
                        {
                            "name": "Carbohydrates",
                            "amount": 158,
                            "unit": "g",
                            "percentOfDailyNeeds": 53
                        },
                        {
                            "name": "Protein",
                            "amount": 84,
                            "unit": "g",
                            "percentOfDailyNeeds": 168
                        }
                    ]
                },
                "nutritionSummaryBreakfast": {
                    "nutrients": [
                        {
                            "name": "Calories",
                            "amount": 472,
                            "unit": "cal",
                            "percentOfDailyNeeds": 24
                        },
                        {
                            "name": "Fat",
                            "amount": 14,
                            "unit": "g",
                            "percentOfDailyNeeds": 21
                        },
                        {
                            "name": "Carbohydrates",
                            "amount": 62,
                            "unit": "g",
                            "percentOfDailyNeeds": 21
                        },
                        {
                            "name": "Protein",
                            "amount": 27,
                            "unit": "g",
                            "percentOfDailyNeeds": 54
                        }
                    ]
                },
                "nutritionSummaryLunch": {
                    "nutrients": [
                        {
                            "name": "Calories",
                            "amount": 568,
                            "unit": "cal",
                            "percentOfDailyNeeds": 28
                        },
                        {
                            "name": "Fat",
                            "amount": 45,
                            "unit": "g",
                            "percentOfDailyNeeds": 69
                        },
                        {
                            "name": "Carbohydrates",
                            "amount": 31,
                            "unit": "g",
                            "percentOfDailyNeeds": 10
                        },
                        {
                            "name": "Protein",
                            "amount": 18,
                            "unit": "g",
                            "percentOfDailyNeeds": 36
                        }
                    ]
                },
                "nutritionSummaryDinner": {
                    "nutrients": [
                        {
                            "name": "Calories",
                            "amount": 549,
                            "unit": "cal",
                            "percentOfDailyNeeds": 27
                        },
                        {
                            "name": "Fat",
                            "amount": 18,
                            "unit": "g",
                            "percentOfDailyNeeds": 27
                        },
                        {
                            "name": "Carbohydrates",
                            "amount": 65,
                            "unit": "g",
                            "percentOfDailyNeeds": 22
                        },
                        {
                            "name": "Protein",
                            "amount": 39,
                            "unit": "g",
                            "percentOfDailyNeeds": 78
                        }
                    ]
                },
                "day": "3",
                "items": [
                    {
                        "id": 2414,
                        "slot": 1,
                        "position": 0,
                        "type": "RECIPE",
                        "value": {
                            "id": 157259,
                            "title": "Cocoa Protein Pancakes",
                            "imageType": "jpg"
                        }
                    },
                    {
                        "id": 2415,
                        "slot": 1,
                        "position": 0,
                        "type": "INGREDIENTS",
                        "value": {
                            "name": "",
                            "servings": "1",
                            "ingredients": [
                                {
                                    "name": "orange",
                                    "image": "https://img.spoonacular.com/ingredients_100x100/orange.jpg",
                                    "amount": 1,
                                    "unit": ""
                                }
                            ]
                        }
                    },
                    {
                        "id": 2416,
                        "slot": 2,
                        "position": 0,
                        "type": "RECIPE",
                        "value": {
                            "id": 535856,
                            "title": "BLT Chopped Salad",
                            "imageType": "jpg"
                        }
                    },
                    {
                        "id": 2417,
                        "slot": 2,
                        "position": 0,
                        "type": "PRODUCT",
                        "value": {
                            "id": 71144,
                            "title": "Kind Plus Fruit & Nut Bar - Almond Walnut Macadamia with Peanuts Plus Protein",
                            "imageType": "jpg"
                        }
                    },
                    {
                        "id": 2418,
                        "slot": 3,
                        "position": 0,
                        "type": "RECIPE",
                        "value": {
                            "id": 519197,
                            "title": "Zesty Sriracha Shrimp and Quinoa",
                            "imageType": "png"
                        }
                    },
                    {
                        "id": 2419,
                        "slot": 3,
                        "position": 0,
                        "type": "PRODUCT",
                        "value": {
                            "id": 163427,
                            "title": "Green Giant Valley Fresh Steamers - Select Sugar Snap Peas",
                            "imageType": "jpg"
                        }
                    },
                    {
                        "id": 2420,
                        "slot": 3,
                        "position": 0,
                        "type": "PRODUCT",
                        "value": {
                            "id": 146191,
                            "title": "Lindt Dark Chocolate",
                            "imageType": "jpg"
                        }
                    }
                ]
            },
            {
                "nutritionSummary": {
                    "nutrients": [
                        {
                            "name": "Calories",
                            "amount": 1343,
                            "unit": "cal",
                            "percentOfDailyNeeds": 67
                        },
                        {
                            "name": "Fat",
                            "amount": 70,
                            "unit": "g",
                            "percentOfDailyNeeds": 108
                        },
                        {
                            "name": "Carbohydrates",
                            "amount": 123,
                            "unit": "g",
                            "percentOfDailyNeeds": 41
                        },
                        {
                            "name": "Protein",
                            "amount": 61,
                            "unit": "g",
                            "percentOfDailyNeeds": 122
                        }
                    ]
                },
                "nutritionSummaryBreakfast": {
                    "nutrients": [
                        {
                            "name": "Calories",
                            "amount": 239,
                            "unit": "cal",
                            "percentOfDailyNeeds": 12
                        },
                        {
                            "name": "Fat",
                            "amount": 11,
                            "unit": "g",
                            "percentOfDailyNeeds": 17
                        },
                        {
                            "name": "Carbohydrates",
                            "amount": 34,
                            "unit": "g",
                            "percentOfDailyNeeds": 11
                        },
                        {
                            "name": "Protein",
                            "amount": 5,
                            "unit": "g",
                            "percentOfDailyNeeds": 9
                        }
                    ]
                },
                "nutritionSummaryLunch": {
                    "nutrients": [
                        {
                            "name": "Calories",
                            "amount": 406,
                            "unit": "cal",
                            "percentOfDailyNeeds": 20
                        },
                        {
                            "name": "Fat",
                            "amount": 17,
                            "unit": "g",
                            "percentOfDailyNeeds": 26
                        },
                        {
                            "name": "Carbohydrates",
                            "amount": 56,
                            "unit": "g",
                            "percentOfDailyNeeds": 19
                        },
                        {
                            "name": "Protein",
                            "amount": 10,
                            "unit": "g",
                            "percentOfDailyNeeds": 21
                        }
                    ]
                },
                "nutritionSummaryDinner": {
                    "nutrients": [
                        {
                            "name": "Calories",
                            "amount": 698,
                            "unit": "cal",
                            "percentOfDailyNeeds": 35
                        },
                        {
                            "name": "Fat",
                            "amount": 43,
                            "unit": "g",
                            "percentOfDailyNeeds": 66
                        },
                        {
                            "name": "Carbohydrates",
                            "amount": 34,
                            "unit": "g",
                            "percentOfDailyNeeds": 11
                        },
                        {
                            "name": "Protein",
                            "amount": 46,
                            "unit": "g",
                            "percentOfDailyNeeds": 92
                        }
                    ]
                },
                "day": "4",
                "items": [
                    {
                        "id": 2421,
                        "slot": 1,
                        "position": 0,
                        "type": "PRODUCT",
                        "value": {
                            "id": 101999,
                            "title": "Greek Gods Yogurt",
                            "imageType": "jpg"
                        }
                    },
                    {
                        "id": 2422,
                        "slot": 1,
                        "position": 0,
                        "type": "INGREDIENTS",
                        "value": {
                            "name": "",
                            "servings": "1",
                            "ingredients": [
                                {
                                    "name": "berries",
                                    "image": "https://img.spoonacular.com/ingredients_100x100/berries-mixed.jpg",
                                    "amount": 1,
                                    "unit": "cup"
                                }
                            ]
                        }
                    },
                    {
                        "id": 2423,
                        "slot": 2,
                        "position": 0,
                        "type": "RECIPE",
                        "value": {
                            "id": 535563,
                            "title": "Black Bean Quinoa Salad",
                            "imageType": "jpg"
                        }
                    },
                    {
                        "id": 2424,
                        "slot": 3,
                        "position": 0,
                        "type": "RECIPE",
                        "value": {
                            "id": 622598,
                            "title": "Pittata - Pizza Frittata",
                            "imageType": "jpg"
                        }
                    },
                    {
                        "id": 2425,
                        "slot": 3,
                        "position": 0,
                        "type": "RECIPE",
                        "value": {
                            "id": 484337,
                            "title": "One Ingredient Banana Ice Cream",
                            "imageType": "jpg"
                        }
                    }
                ]
            },
            {
                "nutritionSummary": {
                    "nutrients": [
                        {
                            "name": "Calories",
                            "amount": 1247,
                            "unit": "cal",
                            "percentOfDailyNeeds": 62
                        },
                        {
                            "name": "Fat",
                            "amount": 61,
                            "unit": "g",
                            "percentOfDailyNeeds": 95
                        },
                        {
                            "name": "Carbohydrates",
                            "amount": 103,
                            "unit": "g",
                            "percentOfDailyNeeds": 34
                        },
                        {
                            "name": "Protein",
                            "amount": 78,
                            "unit": "g",
                            "percentOfDailyNeeds": 156
                        }
                    ]
                },
                "nutritionSummaryBreakfast": {
                    "nutrients": [
                        {
                            "name": "Calories",
                            "amount": 295,
                            "unit": "cal",
                            "percentOfDailyNeeds": 15
                        },
                        {
                            "name": "Fat",
                            "amount": 12,
                            "unit": "g",
                            "percentOfDailyNeeds": 19
                        },
                        {
                            "name": "Carbohydrates",
                            "amount": 42,
                            "unit": "g",
                            "percentOfDailyNeeds": 14
                        },
                        {
                            "name": "Protein",
                            "amount": 11,
                            "unit": "g",
                            "percentOfDailyNeeds": 23
                        }
                    ]
                },
                "nutritionSummaryLunch": {
                    "nutrients": [
                        {
                            "name": "Calories",
                            "amount": 455,
                            "unit": "cal",
                            "percentOfDailyNeeds": 23
                        },
                        {
                            "name": "Fat",
                            "amount": 34,
                            "unit": "g",
                            "percentOfDailyNeeds": 52
                        },
                        {
                            "name": "Carbohydrates",
                            "amount": 1,
                            "unit": "g",
                            "percentOfDailyNeeds": 0
                        },
                        {
                            "name": "Protein",
                            "amount": 35,
                            "unit": "g",
                            "percentOfDailyNeeds": 70
                        }
                    ]
                },
                "nutritionSummaryDinner": {
                    "nutrients": [
                        {
                            "name": "Calories",
                            "amount": 497,
                            "unit": "cal",
                            "percentOfDailyNeeds": 25
                        },
                        {
                            "name": "Fat",
                            "amount": 15,
                            "unit": "g",
                            "percentOfDailyNeeds": 24
                        },
                        {
                            "name": "Carbohydrates",
                            "amount": 60,
                            "unit": "g",
                            "percentOfDailyNeeds": 20
                        },
                        {
                            "name": "Protein",
                            "amount": 32,
                            "unit": "g",
                            "percentOfDailyNeeds": 63
                        }
                    ]
                },
                "day": "5",
                "items": [
                    {
                        "id": 2426,
                        "slot": 1,
                        "position": 0,
                        "type": "PRODUCT",
                        "value": {
                            "id": 71144,
                            "title": "Kind Plus Fruit & Nut Bar - Almond Walnut Macadamia with Peanuts Plus Protein",
                            "imageType": "jpg"
                        }
                    },
                    {
                        "id": 2427,
                        "slot": 1,
                        "position": 0,
                        "type": "INGREDIENTS",
                        "value": {
                            "name": "",
                            "servings": "1",
                            "ingredients": [
                                {
                                    "name": "banana",
                                    "image": "https://img.spoonacular.com/ingredients_100x100/bananas.jpg",
                                    "amount": 1,
                                    "unit": ""
                                }
                            ]
                        }
                    },
                    {
                        "id": 2428,
                        "slot": 2,
                        "position": 0,
                        "type": "RECIPE",
                        "value": {
                            "id": 296213,
                            "title": "Spinach Salad with Roasted Vegetables and Spiced Chickpea",
                            "imageType": "jpg"
                        }
                    },
                    {
                        "id": 2429,
                        "slot": 3,
                        "position": 0,
                        "type": "RECIPE",
                        "value": {
                            "id": 497301,
                            "title": "Shrimp Scampi",
                            "imageType": "jpg"
                        }
                    },
                    {
                        "id": 2430,
                        "slot": 3,
                        "position": 0,
                        "type": "RECIPE",
                        "value": {
                            "id": 581021,
                            "title": "Black Bean Brownies: Fudgy Fun",
                            "imageType": "jpg"
                        }
                    }
                ]
            },
            {
                "nutritionSummary": {
                    "nutrients": [
                        {
                            "name": "Calories",
                            "amount": 1683,
                            "unit": "cal",
                            "percentOfDailyNeeds": 84
                        },
                        {
                            "name": "Fat",
                            "amount": 68,
                            "unit": "g",
                            "percentOfDailyNeeds": 105
                        },
                        {
                            "name": "Carbohydrates",
                            "amount": 139,
                            "unit": "g",
                            "percentOfDailyNeeds": 46
                        },
                        {
                            "name": "Protein",
                            "amount": 106,
                            "unit": "g",
                            "percentOfDailyNeeds": 212
                        }
                    ]
                },
                "nutritionSummaryBreakfast": {
                    "nutrients": [
                        {
                            "name": "Calories",
                            "amount": 490,
                            "unit": "cal",
                            "percentOfDailyNeeds": 24
                        },
                        {
                            "name": "Fat",
                            "amount": 15,
                            "unit": "g",
                            "percentOfDailyNeeds": 23
                        },
                        {
                            "name": "Carbohydrates",
                            "amount": 65,
                            "unit": "g",
                            "percentOfDailyNeeds": 22
                        },
                        {
                            "name": "Protein",
                            "amount": 26,
                            "unit": "g",
                            "percentOfDailyNeeds": 53
                        }
                    ]
                },
                "nutritionSummaryLunch": {
                    "nutrients": [
                        {
                            "name": "Calories",
                            "amount": 378,
                            "unit": "cal",
                            "percentOfDailyNeeds": 19
                        },
                        {
                            "name": "Fat",
                            "amount": 33,
                            "unit": "g",
                            "percentOfDailyNeeds": 51
                        },
                        {
                            "name": "Carbohydrates",
                            "amount": 16,
                            "unit": "g",
                            "percentOfDailyNeeds": 5
                        },
                        {
                            "name": "Protein",
                            "amount": 8,
                            "unit": "g",
                            "percentOfDailyNeeds": 16
                        }
                    ]
                },
                "nutritionSummaryDinner": {
                    "nutrients": [
                        {
                            "name": "Calories",
                            "amount": 816,
                            "unit": "cal",
                            "percentOfDailyNeeds": 41
                        },
                        {
                            "name": "Fat",
                            "amount": 21,
                            "unit": "g",
                            "percentOfDailyNeeds": 32
                        },
                        {
                            "name": "Carbohydrates",
                            "amount": 58,
                            "unit": "g",
                            "percentOfDailyNeeds": 19
                        },
                        {
                            "name": "Protein",
                            "amount": 72,
                            "unit": "g",
                            "percentOfDailyNeeds": 144
                        }
                    ]
                },
                "day": "6",
                "items": [
                    {
                        "id": 2431,
                        "slot": 1,
                        "position": 0,
                        "type": "RECIPE",
                        "value": {
                            "id": 157259,
                            "title": "Cocoa Protein Pancakes",
                            "imageType": "jpg"
                        }
                    },
                    {
                        "id": 2432,
                        "slot": 1,
                        "position": 0,
                        "type": "INGREDIENTS",
                        "value": {
                            "name": "",
                            "servings": "1",
                            "ingredients": [
                                {
                                    "name": "berries",
                                    "image": "https://img.spoonacular.com/ingredients_100x100/berries-mixed.jpg",
                                    "amount": 1,
                                    "unit": "cup"
                                }
                            ]
                        }
                    },
                    {
                        "id": 2433,
                        "slot": 2,
                        "position": 0,
                        "type": "RECIPE",
                        "value": {
                            "id": 535856,
                            "title": "BLT Chopped Salad",
                            "imageType": "jpg"
                        }
                    },
                    {
                        "id": 2434,
                        "slot": 3,
                        "position": 0,
                        "type": "RECIPE",
                        "value": {
                            "id": 149425,
                            "title": "Herb and Cheddar Cordon Bleu",
                            "imageType": "jpg"
                        }
                    },
                    {
                        "id": 2435,
                        "slot": 3,
                        "position": 0,
                        "type": "INGREDIENTS",
                        "value": {
                            "name": "",
                            "servings": "1",
                            "ingredients": [
                                {
                                    "name": "brussels sprouts",
                                    "image": "https://img.spoonacular.com/ingredients_100x100/brussels-sprouts.jpg",
                                    "amount": 1,
                                    "unit": "cup"
                                }
                            ]
                        }
                    },
                    {
                        "id": 2436,
                        "slot": 3,
                        "position": 0,
                        "type": "INGREDIENTS",
                        "value": {
                            "name": "",
                            "servings": "1",
                            "ingredients": [
                                {
                                    "name": "wine",
                                    "image": "https://img.spoonacular.com/ingredients_100x100/white-wine.jpg",
                                    "amount": 5,
                                    "unit": "ounces"
                                }
                            ]
                        }
                    }
                ]
            },
            {
                "nutritionSummary": {
                    "nutrients": [
                        {
                            "name": "Calories",
                            "amount": 1442,
                            "unit": "cal",
                            "percentOfDailyNeeds": 72
                        },
                        {
                            "name": "Fat",
                            "amount": 69,
                            "unit": "g",
                            "percentOfDailyNeeds": 106
                        },
                        {
                            "name": "Carbohydrates",
                            "amount": 147,
                            "unit": "g",
                            "percentOfDailyNeeds": 49
                        },
                        {
                            "name": "Protein",
                            "amount": 73,
                            "unit": "g",
                            "percentOfDailyNeeds": 147
                        }
                    ]
                },
                "nutritionSummaryBreakfast": {
                    "nutrients": [
                        {
                            "name": "Calories",
                            "amount": 444,
                            "unit": "cal",
                            "percentOfDailyNeeds": 22
                        },
                        {
                            "name": "Fat",
                            "amount": 12,
                            "unit": "g",
                            "percentOfDailyNeeds": 19
                        },
                        {
                            "name": "Carbohydrates",
                            "amount": 51,
                            "unit": "g",
                            "percentOfDailyNeeds": 17
                        },
                        {
                            "name": "Protein",
                            "amount": 38,
                            "unit": "g",
                            "percentOfDailyNeeds": 76
                        }
                    ]
                },
                "nutritionSummaryLunch": {
                    "nutrients": [
                        {
                            "name": "Calories",
                            "amount": 406,
                            "unit": "cal",
                            "percentOfDailyNeeds": 20
                        },
                        {
                            "name": "Fat",
                            "amount": 17,
                            "unit": "g",
                            "percentOfDailyNeeds": 26
                        },
                        {
                            "name": "Carbohydrates",
                            "amount": 56,
                            "unit": "g",
                            "percentOfDailyNeeds": 19
                        },
                        {
                            "name": "Protein",
                            "amount": 10,
                            "unit": "g",
                            "percentOfDailyNeeds": 21
                        }
                    ]
                },
                "nutritionSummaryDinner": {
                    "nutrients": [
                        {
                            "name": "Calories",
                            "amount": 593,
                            "unit": "cal",
                            "percentOfDailyNeeds": 30
                        },
                        {
                            "name": "Fat",
                            "amount": 40,
                            "unit": "g",
                            "percentOfDailyNeeds": 62
                        },
                        {
                            "name": "Carbohydrates",
                            "amount": 41,
                            "unit": "g",
                            "percentOfDailyNeeds": 14
                        },
                        {
                            "name": "Protein",
                            "amount": 25,
                            "unit": "g",
                            "percentOfDailyNeeds": 50
                        }
                    ]
                },
                "day": "7",
                "items": [
                    {
                        "id": 2437,
                        "slot": 1,
                        "position": 0,
                        "type": "RECIPE",
                        "value": {
                            "id": 619085,
                            "title": "Protein Packed Healthy French Toast with Chocolate and Peanut Butter {Super Simple, Whole Wheat}",
                            "imageType": "jpg"
                        }
                    },
                    {
                        "id": 2438,
                        "slot": 1,
                        "position": 0,
                        "type": "INGREDIENTS",
                        "value": {
                            "name": "",
                            "servings": "1",
                            "ingredients": [
                                {
                                    "name": "orange",
                                    "image": "https://img.spoonacular.com/ingredients_100x100/orange.jpg",
                                    "amount": 1,
                                    "unit": ""
                                }
                            ]
                        }
                    },
                    {
                        "id": 2439,
                        "slot": 2,
                        "position": 0,
                        "type": "RECIPE",
                        "value": {
                            "id": 535563,
                            "title": "Black Bean Quinoa Salad",
                            "imageType": "jpg"
                        }
                    },
                    {
                        "id": 2440,
                        "slot": 3,
                        "position": 0,
                        "type": "RECIPE",
                        "value": {
                            "id": 590570,
                            "title": "Asian Beef Lettuce Wraps",
                            "imageType": "jpg"
                        }
                    },
                    {
                        "id": 2441,
                        "slot": 3,
                        "position": 0,
                        "type": "PRODUCT",
                        "value": {
                            "id": 146191,
                            "title": "Lindt Dark Chocolate",
                            "imageType": "jpg"
                        }
                    }
                ]
            }
        ]
    }

#### Quotas

Calling this endpoint requires

1 point

. Learn more about quotas.

#### Need Help? Just ask!

Ask AI

## Add Meal Plan Template

Add a meal plan template for a user.

Read more about working with the meal planner.

POST

https://api.spoonacular.com/mealplanner/{username}/templates

#### Headers

Response Headers:

  * `Content-Type: application/json`


#### Parameters

Name | Type | Example | Description
---|---|---|---
**`username`** | string | dsky | The username.
**`hash`** | string | 4b5v4398573406 | The private hash for the username.

Example Request Body

POST

https://api.spoonacular.com/mealplanner/dsky/templates


    {
        "name": "My new meal plan template",
        "items": [
            {
                "day": 1,
                "slot": 1,
                "position": 0,
                "type": "RECIPE",
                "value": {
                    "id": 296213,
                    "servings": 2,
                    "title": "Spinach Salad with Roasted Vegetables and Spiced Chickpea",
                    "imageType": "jpg"
                }
            },
            {
                "day": 2,
                "slot": 1,
                "position": 0,
                "type": "PRODUCT",
                "value": {
                    "id": 183433,
                    "servings": 1,
                    "title": "Ahold Lasagna with Meat Sauce",
                    "imageType": "jpg"
                }
            },
            {
                "day": 3,
                "slot": 1,
                "position": 0,
                "type": "MENU_ITEM",
                "value": {
                    "id": 378557,
                    "servings": 1,
                    "title": "Pizza 73 BBQ Steak Pizza, 9",
                    "imageType": "png"
                }
            },
            {
                "day": 4,
                "slot": 1,
                "position": 0,
                "type": "CUSTOM_FOOD",
                "value": {
                    "id": 348,
                    "servings": 1,
                    "title": "Aldi Spicy Cashews - 30g",
                    "image": "https://img.spoonacular.com/ingredients_100x100/cashews.jpg"
                }
            },
            {
                "day": 5,
                "slot": 1,
                "position": 0,
                "type": "INGREDIENTS",
                "value": {
                    "ingredients": [
                        {
                            "name": "1 banana"
                        },
                        {
                            "name": "coffee",
                            "unit": "cup",
                            "amount": "1",
                            "image": "https://img.spoonacular.com/ingredients_100x100/brewed-coffee.jpg"
                        }
                    ]
                }
            }
        ],
        "publishAsPublic": false
    }

#### Quotas

Calling this endpoint requires

1 point

. Learn more about quotas.

#### Need Help? Just ask!

Ask AI

## Delete Meal Plan Template

Delete a meal plan template for a user.

Read more about working with the meal planner.

DELETE

https://api.spoonacular.com/mealplanner/{username}/templates/{id}

#### Headers

Response Headers:

  * `Content-Type: application/json`


#### Parameters

Name | Type | Example | Description
---|---|---|---
**`username`** | string | dsky | The username.
**`id`** | number | 15678 | The shopping list item id.
**`hash`** | string | 4b5v4398573406 | The private hash for the username.

Example Request and Response

DELETE

https://api.spoonacular.com/mealplanner/dsky/templates/128?hash=4b5v4398573406


    {
        "status": "success"
    }

#### Quotas

Calling this endpoint requires

1 point

. Learn more about quotas.

#### Need Help? Just ask!

Ask AI

## Get Shopping List

Get the current shopping list for the given user.

Read more about working with the meal planner.

GET

https://api.spoonacular.com/mealplanner/{username}/shopping-list

#### Headers

Response Headers:

  * `Content-Type: application/json`


#### Parameters

Name | Type | Example | Description
---|---|---|---
**`username`** | string | dsky | The username.
**`hash`** | string | 4b5v4398573406 | The private hash for the username.

Example Request and Response

GET

https://api.spoonacular.com/mealplanner/dsky/shopping-list


    {
        "aisles": [
            {
                "aisle": "Baking",
                "items": [
                    {
                        "id": 115388,
                        "name": "baking powder",
                        "measures": {
                            "original": {
                                "amount": 1.0,
                                "unit": "package"
                            },
                            "metric": {
                                "amount": 1.0,
                                "unit": "pkg"
                            },
                            "us": {
                                "amount": 1.0,
                                "unit": "pkg"
                            }
                        },
                        "pantryItem": false,
                        "aisle": "Baking",
                        "cost": 0.71,
                        "ingredientId": 18369
                    }
                ]
            }
        ],
        "cost": 1.43,
        "startDate": 1588291200,
        "endDate": 1588896000
    }

#### Quotas

Calling this endpoint requires

1 point

. Learn more about quotas.

#### Need Help? Just ask!

Ask AI

## Add to Shopping List

Add an item to the current shopping list of a user.

Read more about working with the meal planner.

POST

https://api.spoonacular.com/mealplanner/{username}/shopping-list/items

#### Headers

Response Headers:

  * `Content-Type: application/json`


#### Parameters

Name | Type | Example | Description
---|---|---|---
**`username`** | string | dsky | The username.
**`hash`** | string | 4b5v4398573406 | The private hash for the username.

Example Request Body

POST

https://api.spoonacular.com/mealplanner/dsky/shopping-list/items


    {
    	"item": "1 package baking powder",
    	"aisle": "Baking",
    	"parse": true
    }

The field `aisle` is optional and will be added if not given.

Set `parse` false if you want to put a non-food item to the shopping list.

Example Request and Response

POST

https://api.spoonacular.com/mealplanner/dsky/shopping-list/items


    {
        "aisles": [
            {
                "aisle": "Baking",
                "items": [
                    {
                        "id": 115388,
                        "name": "baking powder",
                        "measures": {
                            "original": {
                                "amount": 1.0,
                                "unit": "package"
                            },
                            "metric": {
                                "amount": 1.0,
                                "unit": "pkg"
                            },
                            "us": {
                                "amount": 1.0,
                                "unit": "pkg"
                            }
                        },
                        "pantryItem": false,
                        "aisle": "Baking",
                        "cost": 0.71,
                        "ingredientId": 18369
                    }
                ]
            }
        ],
        "cost": 0.71,
        "startDate": 1588291200,
        "endDate": 1588896000
    }

#### Quotas

Calling this endpoint requires

1 point

. Learn more about quotas.

#### Need Help? Just ask!

Ask AI

## Delete from Shopping List

Delete an item from the current shopping list of the user.

Read more about working with the meal planner.

DELETE

https://api.spoonacular.com/mealplanner/{username}/shopping-list/items/{id}

#### Headers

Response Headers:

  * `Content-Type: application/json`


#### Parameters

Name | Type | Example | Description
---|---|---|---
**`username`** | string | dsky | The username.
**`id`** | number | 15678 | The shopping list item id.
**`hash`** | string | 4b5v4398573406 | The private hash for the username.

Example Request and Response

DELETE

https://api.spoonacular.com/mealplanner/dsky/shopping-list/items/15678?hash=4b5v4398573406

#### Quotas

Calling this endpoint requires

1 point

. Learn more about quotas.

#### Need Help? Just ask!

Ask AI

## Generate Shopping List

Generate the shopping list for a user from the meal planner in a given time frame.

Read more about working with the meal planner.

POST

https://api.spoonacular.com/mealplanner/{username}/shopping-list/{start-date}/{end-date}

#### Headers

Response Headers:

  * `Content-Type: application/json`


#### Parameters

Name | Type | Example | Description
---|---|---|---
**`username`** | string | dsky | The username.
**`start-date`** | string | 2020-06-01 | The start date in the format yyyy-mm-dd.
**`end-date`** | string | 2020-06-07 | The end date in the format yyyy-mm-dd.
**`hash`** | string | 4b5v4398573406 | The private hash for the username.

Example Request and Response

POST

https://api.spoonacular.com/mealplanner/dsky/shopping-list/2020-06-01/2020-06-07?hash=4b5v4398573406


    {
        "aisles": [
            {
                "aisle": "Baking",
                "items": [
                    {
                        "id": 115388,
                        "name": "baking powder",
                        "measures": {
                            "original": {
                                "amount": 1.0,
                                "unit": "package"
                            },
                            "metric": {
                                "amount": 1.0,
                                "unit": "pkg"
                            },
                            "us": {
                                "amount": 1.0,
                                "unit": "pkg"
                            }
                        },
                        "pantryItem": false,
                        "aisle": "Baking",
                        "cost": 0.71,
                        "ingredientId": 18369
                    }
                ]
            }
        ],
        "cost": 0.71,
        "startDate": 1588291200,
        "endDate": 1588896000
    }

#### Quotas

Calling this endpoint requires

1 point

. Learn more about quotas.

#### Need Help? Just ask!

Ask AI

## Compute Shopping List

Compute a shopping list from a set of simple foods. This endpoint does not require usernames.

POST

https://api.spoonacular.com/mealplanner/shopping-list/compute

#### Headers

Response Headers:

  * `Content-Type: application/json`


Example Request and Body

POST

https://api.spoonacular.com/mealplanner/shopping-list/compute


    {
        "items": [
            "4 lbs tomatoes",
            "10 tomatoes",
            "20 Tablespoons Olive Oil",
            "6 tbsp Olive Oil"
        ]
    }

Example Response

POST

https://api.spoonacular.com/mealplanner/shopping-list/compute


    {
        "aisles": [
            {
                "aisle": "Pantry Items",
                "items": [
                    {
                        "name": "olive oil",
                        "measures": {
                            "metric": {
                                "amount": 364.0,
                                "unit": "ml"
                            },
                            "us": {
                                "amount": 12.4,
                                "unit": "fl oz"
                            }
                        },
                        "pantryItem": true,
                        "aisle": "Pantry Items",
                        "cost": 333.55,
                        "ingredientId": 4053
                    }
                ]
            },
            {
                "aisle": "Produce",
                "items": [
                    {
                        "name": "tomatoes",
                        "measures": {
                            "metric": {
                                "amount": 3044.4,
                                "unit": "g"
                            },
                            "us": {
                                "amount": 6.8,
                                "unit": "lb"
                            }
                        },
                        "pantryItem": false,
                        "aisle": "Produce",
                        "cost": 532.21,
                        "ingredientId": 11529
                    }
                ]
            }
        ],
        "cost": 1326.62
    }

#### Quotas

Calling this endpoint requires

1 point

. Learn more about quotas.

#### Need Help? Just ask!

Ask AI

## Search Custom Foods

Search custom foods in a user's account.

Read more about working with the meal planner.

GET

https://api.spoonacular.com/food/customFoods/search

#### Headers

Response Headers:

  * `Content-Type: application/json`


#### Parameters

Name | Type | Example | Description
---|---|---|---
**`search_query`** | string | brat | The search search_query.
**`username`** | string | dsky | The username.
**`hash`** | string | 4b5v4398573406 | The private hash for the username.
`offset` | number | 0 | The number of results to skip (between 0 and 990).
`number` | number | 10 | The number of expected results (between 1 and 100).

Example Request and Response

GET

https://api.spoonacular.com/food/customFoods/search?search_query=brat&number=2&username=dsky&hash=4b5v4398573406


    {
        "customFoods": [
            {
                "id": 15,
                "title": "Max Cafe Curry Bratwurst",
                "servings": 1,
                "imageUrl": "https://img.spoonacular.com/ingredients_100x100/bratwurst.jpg",
                "price": 6.9
            }
        ],
        "type": "customFood",
        "offset": 0,
        "number": 10
    }

#### Quotas

Calling this endpoint requires

1 point

and

0.01 points

per custom food returned. Learn more about quotas.

#### Need Help? Just ask!

Ask AI

## Connect User

In order to call user-specific endpoints, you need to connect your app's users to spoonacular users.

Just call this endpoint with your user's information and you will get back a username and hash that you must save on your side. In future requests that you make on this user's behalf you simply pass their username and hash alongside your API key.

Read more about working with the meal planner.

POST

https://api.spoonacular.com/users/connect

#### Headers

Response Headers:

  * `Content-Type: application/json`


#### Parameters

Name | Type | Example | Description
---|---|---|---
**`(post body)`** | string | { "username": "cool user", } | A json body.

Example Request Body

POST

https://api.spoonacular.com/users/connect


    {
        "username": "your user's name",
        "firstName": "your user's first name",
        "lastName": "your user's last name",
        "email": "your user's email"
    }

The response will give you the corresponding spoonacular usernamem, the password with which the user can log in to spoonacular.com, and the hash. Save this information permanently on your end and connect it with your user.


    {
        "username": "api_123_user",
        "spoonacularPassword": "meadwith31grapejam",
        "hash": "q572587bq2405724q05"
    }

#### Quotas

Calling this endpoint requires

1 point

. Learn more about quotas.

#### Need Help? Just ask!

Ask AI