# Ingredients

*Source: https://spoonacular.com/food-api/docs#Ingredients*

---

## Ingredient Search

Search for simple whole foods (e.g. fruits, vegetables, nuts, grains, meat, fish, dairy etc.).

GET

https://api.spoonacular.com/food/ingredients/search

#### Headers

Response Headers:

  * `Content-Type: application/json`


#### Parameters

Name | Type | Example | Description
---|---|---|---
**`query`** | string | apple | The partial or full ingredient name.
`addChildren` | boolean | true | Whether to add children of found foods.
`minProteinPercent` | number | 10 | The minimum percentage of protein the food must have (between 0 and 100).
`maxProteinPercent` | number | 90 | The maximum percentage of protein the food can have (between 0 and 100).
`minFatPercent` | number | 10 | The minimum percentage of fat the food must have (between 0 and 100).
`maxFatPercent` | number | 90 | The maximum percentage of fat the food can have (between 0 and 100).
`minCarbsPercent` | number | 10 | The minimum percentage of carbs the food must have (between 0 and 100).
`maxCarbsPercent` | number | 90 | The maximum percentage of carbs the food can have (between 0 and 100).
`metaInformation` | boolean | false | Whether to return more meta information about the ingredients.
`intolerances` | string | egg | A comma-separated list of intolerances. All recipes returned must not contain ingredients that are not suitable for people with the intolerances entered. See a full [list of supported intolerances](/food-api/docs#Intolerances).
`sort` | string | calories | The strategy to sort ingredients by. You can sort by any nutrient listed [here](/food-api/docs#Recipe-Sorting-Options).
`sortDirection` | string | asc | The direction in which to sort. Must be either 'asc' (ascending) or 'desc' (descending).
`language` | text | en | Language code, either "en" or "de".
`offset` | number | 0 | The number of results to skip (between 0 and 990).
`number` | number | 10 | The number of expected results (between 1 and 100).

Example Request and Response

GET

https://api.spoonacular.com/food/ingredients/search?query=banana&number=2&sort=calories&sortDirection=desc


    {
        "results": [
            {
                "id": 19400,
                "name": "banana chips",
                "image": "banana-chips.jpg"
            },
            {
                "id": 93779,
                "name": "banana liqueur",
                "image": "limoncello.jpg"
            }
        ],
        "offset": 0,
        "number": 2,
        "totalResults": 13
    }

#### Quotas

Calling this endpoint requires

1 point

and

0.01 points

per result if `metaInformation` is set to true. Learn more about quotas.

#### Need Help? Just ask!

Ask AI

## Get Ingredient Information

Use an ingredient id to get all available information about an ingredient, such as its image and supermarket aisle.

GET

https://api.spoonacular.com/food/ingredients/{id}/information

#### Headers

Response Headers:

  * `Content-Type: application/json`


#### Parameters

Name | Type | Example | Description
---|---|---|---
**`id`** | number | 9266 | The ingredient id.
`amount` | number | 150 | The amount of this ingredient.
`unit` | string | grams | The unit for the given amount.
`locale` | string | en_US | The display name of the returned category, supported is en_US (for American English) and en_GB (for British English).

Example Request and Response

GET

https://api.spoonacular.com/food/ingredients/9266/information?amount=1


    {
        "id": 9266,
        "original": "pineapples",
        "originalName": "pineapples",
        "name": "pineapples",
        "amount": 1.0,
        "unit": "",
        "unitShort": "",
        "unitLong": "",
        "possibleUnits": [
            "piece",
            "slice",
            "fruit",
            "g",
            "oz",
            "cup",
            "serving"
        ],
        "estimatedCost": {
            "value": 299.0,
            "unit": "US Cents"
        },
        "consistency": "solid",
        "shoppingListUnits": [
            "pieces"
        ],
        "aisle": "Produce",
        "image": "pineapple.jpg",
        "meta": [],
        "nutrition": {
            "nutrients": [
                {
                    "name": "Calories",
                    "amount": 452.5,
                    "unit": "cal",
                    "percentOfDailyNeeds": 22.63
                },
                {
                    "name": "Fat",
                    "amount": 1.09,
                    "unit": "g",
                    "percentOfDailyNeeds": 1.67
                },
                {
                    "name": "Saturated Fat",
                    "amount": 0.08,
                    "unit": "g",
                    "percentOfDailyNeeds": 0.51
                },
                {
                    "name": "Carbohydrates",
                    "amount": 118.74,
                    "unit": "g",
                    "percentOfDailyNeeds": 39.58
                },
                {
                    "name": "Net Carbohydrates",
                    "amount": 106.07,
                    "unit": "g",
                    "percentOfDailyNeeds": 38.57
                },
                {
                    "name": "Sugar",
                    "amount": 89.14,
                    "unit": "g",
                    "percentOfDailyNeeds": 99.05
                },
                {
                    "name": "Cholesterol",
                    "amount": 0.0,
                    "unit": "mg",
                    "percentOfDailyNeeds": 0.0
                },
                {
                    "name": "Sodium",
                    "amount": 9.05,
                    "unit": "mg",
                    "percentOfDailyNeeds": 0.39
                },
                {
                    "name": "Protein",
                    "amount": 4.89,
                    "unit": "g",
                    "percentOfDailyNeeds": 9.77
                },
                {
                    "name": "Vitamin C",
                    "amount": 432.59,
                    "unit": "mg",
                    "percentOfDailyNeeds": 524.35
                },
                {
                    "name": "Manganese",
                    "amount": 8.39,
                    "unit": "mg",
                    "percentOfDailyNeeds": 419.47
                },
                {
                    "name": "Fiber",
                    "amount": 12.67,
                    "unit": "g",
                    "percentOfDailyNeeds": 50.68
                },
                {
                    "name": "Vitamin B6",
                    "amount": 1.01,
                    "unit": "mg",
                    "percentOfDailyNeeds": 50.68
                },
                {
                    "name": "Copper",
                    "amount": 1.0,
                    "unit": "mg",
                    "percentOfDailyNeeds": 49.78
                },
                {
                    "name": "Vitamin B1",
                    "amount": 0.72,
                    "unit": "mg",
                    "percentOfDailyNeeds": 47.66
                },
                {
                    "name": "Folate",
                    "amount": 162.9,
                    "unit": "µg",
                    "percentOfDailyNeeds": 40.73
                },
                {
                    "name": "Potassium",
                    "amount": 986.45,
                    "unit": "mg",
                    "percentOfDailyNeeds": 28.18
                },
                {
                    "name": "Magnesium",
                    "amount": 108.6,
                    "unit": "mg",
                    "percentOfDailyNeeds": 27.15
                },
                {
                    "name": "Vitamin B3",
                    "amount": 4.53,
                    "unit": "mg",
                    "percentOfDailyNeeds": 22.63
                },
                {
                    "name": "Vitamin B5",
                    "amount": 1.93,
                    "unit": "mg",
                    "percentOfDailyNeeds": 19.28
                },
                {
                    "name": "Vitamin B2",
                    "amount": 0.29,
                    "unit": "mg",
                    "percentOfDailyNeeds": 17.04
                },
                {
                    "name": "Iron",
                    "amount": 2.62,
                    "unit": "mg",
                    "percentOfDailyNeeds": 14.58
                },
                {
                    "name": "Calcium",
                    "amount": 117.65,
                    "unit": "mg",
                    "percentOfDailyNeeds": 11.77
                },
                {
                    "name": "Vitamin A",
                    "amount": 524.9,
                    "unit": "IU",
                    "percentOfDailyNeeds": 10.5
                },
                {
                    "name": "Zinc",
                    "amount": 1.09,
                    "unit": "mg",
                    "percentOfDailyNeeds": 7.24
                },
                {
                    "name": "Phosphorus",
                    "amount": 72.4,
                    "unit": "mg",
                    "percentOfDailyNeeds": 7.24
                },
                {
                    "name": "Vitamin K",
                    "amount": 6.34,
                    "unit": "Âµg",
                    "percentOfDailyNeeds": 6.03
                },
                {
                    "name": "Selenium",
                    "amount": 0.91,
                    "unit": "Âµg",
                    "percentOfDailyNeeds": 1.29
                },
                {
                    "name": "Vitamin E",
                    "amount": 0.18,
                    "unit": "mg",
                    "percentOfDailyNeeds": 1.21
                }
            ],
            "properties": [
                {
                    "name": "Glycemic Index",
                    "amount": 58.67,
                    "unit": ""
                },
                {
                    "name": "Glycemic Load",
                    "amount": 62.23,
                    "unit": ""
                }
            ],
            "flavonoids": [
                {
                    "name": "Cyanidin",
                    "amount": 0.0,
                    "unit": "mg"
                }
            ],
            "caloricBreakdown": {
                "percentProtein": 3.88,
                "percentFat": 1.94,
                "percentCarbs": 94.18
            },
            "weightPerServing": {
                "amount": 905,
                "unit": "g"
            }
        },
        "categoryPath": [
            "tropical fruit",
            "fruit"
        ]
    }

#### Quotas

Calling this endpoint requires

1 point

. Learn more about quotas.

#### Need Help? Just ask!

Ask AI

## Compute Ingredient Amount

Compute the amount you need of a certain ingredient for a certain nutritional goal. For example, how much pineapple do you have to eat to get 10 grams of protein?

GET

https://api.spoonacular.com/food/ingredients/{id}/amount

#### Headers

Response Headers:

  * `Content-Type: application/json`


#### Parameters

Name | Type | Example | Description
---|---|---|---
**`id`** | number | 9266 | The id of the ingredient you want the amount for.
**`nutrient`** | string | protein | The target nutrient. See a [list of supported nutrients](/food-api/docs#Nutrition).
**`target`** | number | 2 | The target number of the given nutrient.
`unit` | string | oz | The target unit.

Example Request and Response

GET

https://api.spoonacular.com/food/ingredients/9266/amount?nutrient=protein⌖=10&unit=oz


    {
        "amount": 65.32,
        "unit": "oz"
    }

#### Quotas

Calling this endpoint requires

1 point

. Learn more about quotas.

#### Need Help? Just ask!

Ask AI

## Convert Amounts

Convert amounts like "2 cups of flour to grams".

GET

https://api.spoonacular.com/recipes/convert

#### Headers

Response Headers:

  * `Content-Type: application/json`


#### Parameters

Name | Type | Example | Description
---|---|---|---
**`ingredientName`** | string | flour | The ingredient which you want to convert.
**`sourceAmount`** | number | 2.5 | The amount from which you want to convert, e.g. the 2.5 in "2.5 cups of flour to grams".
**`sourceUnit`** | string | cups | The unit from which you want to convert, e.g. the grams in "2.5 cups of flour to grams". You can also use "piece", e.g. "3.4 oz tomatoes to piece"
**`targetUnit`** | string | grams | The unit to which you want to convert, e.g. the grams in "2.5 cups of flour to grams". You can also use "piece", e.g. "3.4 oz tomatoes to piece"

Example Request and Response

GET

https://api.spoonacular.com/recipes/convert?ingredientName=flour&sourceAmount=2.5&sourceUnit=cups&targetUnit=grams


    {
        "sourceAmount": 2.5,
        "sourceUnit": "cups",
        "targetAmount": 312.5,
        "targetUnit": "grams",
        "answer": "2.5 cups flour translates to 312.5 grams."
    }

#### Quotas

Calling this endpoint requires

1 point

. Learn more about quotas.

#### Need Help? Just ask!

Ask AI

## Parse Ingredients

Extract an ingredient from plain text.

POST

https://api.spoonacular.com/recipes/parseIngredients

#### Headers

Request Headers:

  * `Content-Type: application/x-www-form-urlencoded`


Response Headers:

  * `Content-Type: application/json`


#### Parameters

Name | Type | Example | Description
---|---|---|---
**`ingredientList`** | string | 1 cup green tea | The ingredient list of the recipe, one ingredient per line.
**`servings`** | number | 1 | The number of servings that you can make from the ingredients.
`includeNutrition` | boolean | true | Whether nutrition data should be added to correctly parsed ingredients.
`language` | string | en | The input language, either "en" or "de".

Example Request and Response

POST

https://api.spoonacular.com/recipes/parseIngredients


    [
        {
            "id": 10014355,
            "original": "1 cup green tea",
            "originalName": "green tea",
            "name": "tea",
            "amount": 1.0,
            "unit": "cup",
            "unitShort": "cup",
            "unitLong": "cup",
            "possibleUnits": [
                "g",
                "oz",
                "fluid ounce",
                "cup"
            ],
            "estimatedCost": {
                "value": 1786.86,
                "unit": "US Cents"
            },
            "consistency": "solid",
            "aisle": "Tea and Coffee",
            "image": "green-tea-leaves.jpg",
            "meta": [
                "green"
            ],
            "nutrition": {
                "nutrients": [
                    {
                        "name": "Calories",
                        "amount": 2.36,
                        "unit": "kcal",
                        "percentOfDailyNeeds": 0.12
                    },
                    {
                        "name": "Fat",
                        "amount": 0.0,
                        "unit": "g",
                        "percentOfDailyNeeds": 0.0
                    },
                    {
                        "name": "Saturated Fat",
                        "amount": 0.0,
                        "unit": "g",
                        "percentOfDailyNeeds": 0.03
                    },
                    {
                        "name": "Carbohydrates",
                        "amount": 0.71,
                        "unit": "g",
                        "percentOfDailyNeeds": 0.24
                    },
                    {
                        "name": "Net Carbohydrates",
                        "amount": 0.71,
                        "unit": "g",
                        "percentOfDailyNeeds": 0.26
                    },
                    {
                        "name": "Sugar",
                        "amount": 0.0,
                        "unit": "g",
                        "percentOfDailyNeeds": 0.0
                    },
                    {
                        "name": "Cholesterol",
                        "amount": 0.0,
                        "unit": "mg",
                        "percentOfDailyNeeds": 0.0
                    },
                    {
                        "name": "Sodium",
                        "amount": 7.08,
                        "unit": "mg",
                        "percentOfDailyNeeds": 0.31
                    },
                    {
                        "name": "Caffeine",
                        "amount": 47.2,
                        "unit": "mg",
                        "percentOfDailyNeeds": 15.73
                    },
                    {
                        "name": "Protein",
                        "amount": 0.0,
                        "unit": "g",
                        "percentOfDailyNeeds": 0.0
                    },
                    {
                        "name": "Manganese",
                        "amount": 0.52,
                        "unit": "mg",
                        "percentOfDailyNeeds": 25.84
                    },
                    {
                        "name": "Folate",
                        "amount": 11.8,
                        "unit": "Âµg",
                        "percentOfDailyNeeds": 2.95
                    },
                    {
                        "name": "Potassium",
                        "amount": 87.32,
                        "unit": "mg",
                        "percentOfDailyNeeds": 2.49
                    },
                    {
                        "name": "Vitamin B2",
                        "amount": 0.03,
                        "unit": "mg",
                        "percentOfDailyNeeds": 1.94
                    },
                    {
                        "name": "Magnesium",
                        "amount": 7.08,
                        "unit": "mg",
                        "percentOfDailyNeeds": 1.77
                    },
                    {
                        "name": "Copper",
                        "amount": 0.02,
                        "unit": "mg",
                        "percentOfDailyNeeds": 1.18
                    }
                ],
                "properties": [
                    {
                        "name": "Glycemic Index",
                        "amount": 0.0,
                        "unit": ""
                    },
                    {
                        "name": "Glycemic Load",
                        "amount": 0.0,
                        "unit": ""
                    }
                ],
                "flavonoids": [
                    {
                        "name": "Cyanidin",
                        "amount": 0.0,
                        "unit": ""
                    },
                    {
                        "name": "Petunidin",
                        "amount": 0.0,
                        "unit": ""
                    },
                    {
                        "name": "Delphinidin",
                        "amount": 0.0,
                        "unit": ""
                    },
                    {
                        "name": "Malvidin",
                        "amount": 0.0,
                        "unit": ""
                    },
                    {
                        "name": "Pelargonidin",
                        "amount": 0.0,
                        "unit": ""
                    },
                    {
                        "name": "Peonidin",
                        "amount": 0.0,
                        "unit": ""
                    },
                    {
                        "name": "Catechin",
                        "amount": 3.56,
                        "unit": "mg"
                    },
                    {
                        "name": "Epigallocatechin",
                        "amount": 19.0,
                        "unit": "mg"
                    },
                    {
                        "name": "Epicatechin",
                        "amount": 5.03,
                        "unit": "mg"
                    },
                    {
                        "name": "Epicatechin 3-gallate",
                        "amount": 13.83,
                        "unit": "mg"
                    },
                    {
                        "name": "Epigallocatechin 3-gallate",
                        "amount": 22.09,
                        "unit": "mg"
                    },
                    {
                        "name": "Theaflavin",
                        "amount": 3.73,
                        "unit": "mg"
                    },
                    {
                        "name": "Thearubigins",
                        "amount": 191.87,
                        "unit": "mg"
                    },
                    {
                        "name": "Eriodictyol",
                        "amount": 0.0,
                        "unit": ""
                    },
                    {
                        "name": "Hesperetin",
                        "amount": 0.0,
                        "unit": ""
                    },
                    {
                        "name": "Naringenin",
                        "amount": 0.0,
                        "unit": ""
                    },
                    {
                        "name": "Apigenin",
                        "amount": 0.0,
                        "unit": "mg"
                    },
                    {
                        "name": "Luteolin",
                        "amount": 0.0,
                        "unit": "mg"
                    },
                    {
                        "name": "Isorhamnetin",
                        "amount": 0.0,
                        "unit": ""
                    },
                    {
                        "name": "Kaempferol",
                        "amount": 3.33,
                        "unit": "mg"
                    },
                    {
                        "name": "Myricetin",
                        "amount": 1.06,
                        "unit": "mg"
                    },
                    {
                        "name": "Quercetin",
                        "amount": 5.17,
                        "unit": "mg"
                    },
                    {
                        "name": "Theaflavin-3,3'-digallate",
                        "amount": 4.13,
                        "unit": "mg"
                    },
                    {
                        "name": "Theaflavin-3'-gallate",
                        "amount": 3.56,
                        "unit": "mg"
                    },
                    {
                        "name": "Theaflavin-3-gallate",
                        "amount": 0.0,
                        "unit": ""
                    },
                    {
                        "name": "Gallocatechin",
                        "amount": 2.95,
                        "unit": "mg"
                    }
                ],
                "caloricBreakdown": {
                    "percentProtein": 0.0,
                    "percentFat": 0.0,
                    "percentCarbs": 100.0
                },
                "weightPerServing": {
                    "amount": 236,
                    "unit": "g"
                }
            }
        }
    ]

#### Quotas

Calling this endpoint requires

1 point

per parsed ingredient. Learn more about quotas.

#### Need Help? Just ask!

Ask AI

## Compute Glycemic Load

Retrieve the glycemic index for a list of ingredients and compute the individual and total glycemic load.

POST

https://api.spoonacular.com/food/ingredients/glycemicLoad

#### Headers

Request Headers:

  * `Content-Type: application/json`


Response Headers:

  * `Content-Type: application/json`


#### Parameters

Name | Type | Example | Description
---|---|---|---
**`(post body)`** | string | { "ingredients":[ "1 kiwi", "2 cups rice", "2 glasses of water" ] } | A json body.
`language` | string | en | The input language, either "en" or "de".

Example Request

POST

https://api.spoonacular.com/food/ingredients/glycemicLoad


    {
        "ingredients":[
            "1 kiwi",
            "2 cups rice",
            "2 glasses of water"
        ]
    }

Example Response


    {
        "totalGlycemicLoad": 183.64,
        "ingredients": [
            {
                "id": 9148,
                "original": "1 kiwi",
                "glycemicIndex": 52.67,
                "glycemicLoad": 5.59
            },
            {
                "id": 20444,
                "original": "2 cups rice",
                "glycemicIndex": 61.19,
                "glycemicLoad": 178.05
            },
            {
                "id": 14412,
                "original": "2 glasses of water",
                "glycemicIndex": 0.0,
                "glycemicLoad": 0.0
            }
        ]
    }

#### Quotas

Calling this endpoint requires

1 point

and

0.1 points

per ingredient. Learn more about quotas.

#### Need Help? Just ask!

Ask AI

## Autocomplete Ingredient Search

Autocomplete the entry of an ingredient.

GET

https://api.spoonacular.com/food/ingredients/autocomplete

#### Headers

Response Headers:

  * `Content-Type: application/json`


#### Parameters

Name | Type | Example | Description
---|---|---|---
**`query`** | string | appl | The partial or full ingredient name.
`number` | number | 10 | The number of results to return (between 1 and 100).
`language` | text | en | Language code, either "en" or "de".
`metaInformation` | boolean | false | Whether to return more meta information about the ingredients.
`intolerances` | string | egg | A comma-separated list of intolerances. All recipes returned must not contain ingredients that are not suitable for people with the intolerances entered. See a full [list of supported intolerances](/food-api/docs#Intolerances).

Example Request and Response

GET

https://api.spoonacular.com/food/ingredients/autocomplete?query=appl&number=5


    [
        {
            "name": "apple",
            "image": "apple.jpg",
            "id": 9003,
            "aisle": "Produce",
            "possibleUnits": [
                "small",
                "large",
                "piece",
                "slice",
                "g",
                "extra small",
                "medium",
                "oz",
                "cup slice",
                "cup",
                "serving"
            ]
        },
        {
            "name": "applesauce",
            "image": "applesauce.png",
            "id": 9019,
            "aisle": "Canned and Jarred",
            "possibleUnits": [
                "g",
                "oz",
                "cup",
                "serving",
                "tablespoon"
            ]
        },
        {
            "name": "apple juice",
            "image": "apple-juice.jpg",
            "id": 9016,
            "aisle": "Beverages",
            "possibleUnits": [
                "g",
                "drink box",
                "fl oz",
                "oz",
                "teaspoon",
                "cup",
                "serving",
                "tablespoon"
            ]
        },
        {
            "name": "apple cider",
            "image": "apple-cider.jpg",
            "id": 1009016,
            "aisle": "Beverages",
            "possibleUnits": [
                "g",
                "drink box",
                "fl oz",
                "oz",
                "teaspoon",
                "bottle NFS",
                "cup",
                "serving",
                "tablespoon"
            ]
        },
        {
            "name": "apple jelly",
            "image": "apple-jelly.jpg",
            "id": 10019297,
            "aisle": "Nut butters, Jams, and Honey",
            "possibleUnits": [
                "g",
                "oz",
                "packet",
                "teaspoon",
                "cup",
                "serving",
                "tablespoon"
            ]
        }
    ]

#### Quotas

Calling this endpoint requires

0.1 points

and

0.01 points

if `metaInformation` is set to true. Learn more about quotas.

#### Need Help? Just ask!

Ask AI

## Get Ingredient Substitutes

Search for substitutes for a given ingredient.

GET

https://api.spoonacular.com/food/ingredients/substitutes

#### Headers

Response Headers:

  * `Content-Type: application/json`


#### Parameters

Name | Type | Example | Description
---|---|---|---
**`ingredientName`** | string | butter | The name of the ingredient you want to replace.

Example Request and Response

GET

https://api.spoonacular.com/food/ingredients/substitutes?ingredientName=butter


    {
        "ingredient": "butter",
        "substitutes": [
            "1 cup = 7/8 cup shortening and 1/2 tsp salt",
            "1 cup = 7/8 cup vegetable oil + 1/2 tsp salt",
            "1/2 cup = 1/4 cup buttermilk + 1/4 cup unsweetened applesauce",
            "1 cup = 1 cup margarine"
        ],
        "message": "Found 4 substitutes for the ingredient."
    }

#### Quotas

Calling this endpoint requires

1 point

. Learn more about quotas.

#### Need Help? Just ask!

Ask AI

## Get Ingredient Substitutes by ID

Search for substitutes for a given ingredient.

GET

https://api.spoonacular.com/food/ingredients/{id}/substitutes

#### Headers

Response Headers:

  * `Content-Type: application/json`


#### Parameters

Name | Type | Example | Description
---|---|---|---
**`id`** | number | 1001 | The id of the ingredient you want substitutes for.

Example Request and Response

GET

https://api.spoonacular.com/food/ingredients/1001/substitutes


    {
        "ingredient": "butter",
        "substitutes": [
            "1 cup = 7/8 cup shortening and 1/2 tsp salt",
            "1 cup = 7/8 cup vegetable oil + 1/2 tsp salt",
            "1/2 cup = 1/4 cup buttermilk + 1/4 cup unsweetened applesauce",
            "1 cup = 1 cup margarine"
        ],
        "message": "Found 4 substitutes for the ingredient."
    }

#### Quotas

Calling this endpoint requires

1 point

. Learn more about quotas.

#### Need Help? Just ask!

Ask AI