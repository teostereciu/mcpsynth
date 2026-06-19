# Menu Items

*Source: https://spoonacular.com/food-api/docs#Menu-Items*

---

## Search Menu Items

Search over 115,000 menu items from over 800 fast food and chain restaurants. For example, McDonald's Big Mac or Starbucks Mocha.

GET

https://api.spoonacular.com/food/menuItems/search

#### Headers

Response Headers:

  * `Content-Type: application/json`


#### Parameters

Name | Type | Example | Description
---|---|---|---
**`query`** | string | snickers | The search query.
`minCalories` | number | 50 | The minimum amount of calories the menu item must have per serving.
`maxCalories` | number | 800 | The maximum amount of calories the menu item can have per serving.
`minCarbs` | number | 10 | The minimum amount of carbohydrates in grams the menu item must have per serving.
`maxCarbs` | number | 100 | The maximum amount of carbohydrates in grams the menu item can have per serving.
`minProtein` | number | 10 | The minimum amount of protein in grams the menu item must have per serving.
`maxProtein` | number | 100 | The maximum amount of protein in grams the menu item can have per serving.
`minFat` | number | 1 | The minimum amount of fat in grams the menu item must have per serving.
`maxFat` | number | 100 | The maximum amount of fat in grams the menu item can have per serving.
`addMenuItemInformation` | boolean | false | If set to true, you get more information about the menu items returned.
`offset` | number | 0 | The offset number for paging (between 0 and 990).
`number` | number | 100 | The number of expected results (between 1 and 10).

Example Request and Response

GET

https://api.spoonacular.com/food/menuItems/search?query=burger&number=2


    {
        "menuItems": [
            {
                "id": 419357,
                "title": "Burger Sliders",
                "restaurantChain": "Hooters",
                "image": "https://img.spoonacular.com/menu-items/419357-312x231.png",
                "imageType": "png",
                "servings": {
                    "number": 1,
                    "size": 2,
                    "unit": "oz"
                }
            },
            {
                "id": 424571,
                "title": "Bacon King Burger",
                "restaurantChain": "Burger King",
                "image": "https://img.spoonacular.com/menu-items/424571-312x231.png",
                "imageType": "png",
                "servings": {
                    "number": 1,
                    "size": 2,
                    "unit": "oz"
                }
            }
        ],
        "totalMenuItems": 6749,
        "type": "menuItem",
        "offset": 0,
        "number": 2
    }

#### Quotas

Calling this endpoint requires

1 point

and

0.01 points

per result returned. Since this endpoint combines the capabilities of four different endpoints into one, additional points may be required depending on the parameters you set. If `addMenuItemInformation` is set to true,

1 point

will be added per menu item returned. Learn more about quotas.

#### Need Help? Just ask!

Ask AI

## Get Menu Item Information

Use a menu item id to get all available information about a menu item, such as nutrition.

GET

https://api.spoonacular.com/food/menuItems/{id}

#### Headers

Response Headers:

  * `Content-Type: application/json`


#### Parameters

Name | Type | Example | Description
---|---|---|---
**`id`** | number | 424571 | The menu item id.

Example Request and Response

GET

https://api.spoonacular.com/food/menuItems/424571


    {
        "id": 424571,
        "title": "Bacon King Burger",
        "restaurantChain": "Burger King",
        "nutrition": {
            "nutrients": [
                {
                    "name": "Fat",
                    "amount": 69,
                    "unit": "g",
                    "percentOfDailyNeeds": 30
                },
                {
                    "name": "Protein",
                    "amount": 57,
                    "unit": "g",
                    "percentOfDailyNeeds": 35
                },
                {
                    "name": "Calories",
                    "amount": 1040,
                    "unit": "cal",
                    "percentOfDailyNeeds": 50
                },
                {
                    "name": "Carbohydrates",
                    "amount": 48,
                    "unit": "g",
                    "percentOfDailyNeeds": 35
                }
            ],
            "caloricBreakdown": {
                "percentProtein": 35,
                "percentFat": 30,
                "percentCarbs": 35
            }
        },
        "badges": [],
        "breadcrumbs": [
            "burger",
            "main course",
            "food product category"
        ],
        "generatedText": null,
        "imageType": "png",
        "likes": 0,
        "servings": {
            "number": 1,
            "size": 2,
            "unit": "oz"
        },
        "price": null,
        "spoonacularScore": null
    }

#### Quotas

Calling this endpoint requires

1 point

. Learn more about quotas.

#### Need Help? Just ask!

Ask AI

## Autocomplete Menu Item Search

Generate suggestions for menu items based on a (partial) query. The matches will be found by looking in the title only.

GET

https://api.spoonacular.com/food/menuItems/suggest

#### Headers

Response Headers:

  * `Content-Type: application/json`


#### Parameters

Name | Type | Example | Description
---|---|---|---
**`query`** | string | chicke | The (partial) search query.
`number` | number | 10 | The number of results to return (between 1 and 25).

Example Request and Response

GET

https://api.spoonacular.com/food/menuItems/suggest?query=chicke&number=2


    {
        "results": [
            {
                "id": 253419,
                "title": "pei wei asian diner thai chicken lettuce wraps"
            },
            {
                "id": 380722,
                "title": "camille's chicken caesar salad includes 2 oz. caesar dressing"
            }
        ]
    }

#### Quotas

Calling this endpoint requires

0.1 points

. Learn more about quotas.

#### Need Help? Just ask!

Ask AI