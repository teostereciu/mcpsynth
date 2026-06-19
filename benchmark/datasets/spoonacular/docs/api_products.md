# Products

*Source: https://spoonacular.com/food-api/docs#Products*

---

## Search Grocery Products

Search packaged food products, such as frozen pizza or Greek yogurt.

GET

https://api.spoonacular.com/food/products/search

#### Headers

Response Headers:

  * `Content-Type: application/json`


#### Parameters

Name | Type | Example | Description
---|---|---|---
**`query`** | string | greek yogurt | The search query.
`minCalories` | number | 50 | The minimum amount of calories the product must have per serving.
`maxCalories` | number | 800 | The maximum amount of calories the product can have per serving.
`minCarbs` | number | 10 | The minimum amount of carbohydrates in grams the product must have per serving.
`maxCarbs` | number | 100 | The maximum amount of carbohydrates in grams the product can have per serving.
`minProtein` | number | 10 | The minimum amount of protein in grams the product must have per serving.
`maxProtein` | number | 100 | The maximum amount of protein in grams the product can have per serving.
`minFat` | number | 1 | The minimum amount of fat in grams the product must have per serving.
`maxFat` | number | 100 | The maximum amount of fat in grams the product can have per serving.
`addProductInformation` | boolean | false | If set to true, you get more information about the products returned.
`offset` | number | 0 | The number of results to skip (between 0 and 990).
`number` | number | 10 | The number of expected results (between 1 and 100).

Example Request and Response

GET

https://api.spoonacular.com/food/products/search?query=pizza&number=2


    {
        "products": [
            {
                "id": 192386,
                "title": "Pizza Buddy: Frozen Pizza Dough, 16 Oz",
                "imageType": "jpg"
            },
            {
                "id": 27693,
                "title": "Uno Pizza",
                "imageType": "jpg"
            }
        ],
        "totalProducts": 1258,
        "type": "product",
        "offset": 0,
        "number": 2
    }

#### Quotas

Calling this endpoint requires

1 point

and

0.01 points

per result returned. Since this endpoint combines the capabilities of four different endpoints into one, additional points may be required depending on the parameters you set. If `addProductInformation` is set to true,

1 point

will be added per product returned. Learn more about quotas.

#### Need Help? Just ask!

Ask AI

## Grocery Products Overview

The spoonacular grocery products API allows you to search through all products. You can find products by query (e.g. "pizza") and/or by macro-nutrients (e.g. <500 calories).

Once you found a product, you can get a lot of detailed information about it such as nutrition, ingredients, cost, and where to find it in the supermarket.

spoonacular analyzes every product and tries to retrieve meta information. This information is stored in `badges`.

Here is a list of all possible badges a product can have:

  * egg_free
  * wheat_free
  * grain_free
  * peanut_free
  * primal
  * vegetarian
  * nut_free
  * vegan
  * pescetarian
  * dairy_free
  * gluten_free
  * paleo
  * msg_free
  * no_artificial_colors
  * no_artificial_flavors
  * no_artificial_ingredients
  * grass_fed
  * no_added_sugar
  * pasture_raised
  * free_range
  * cage_free
  * wild_caught
  * fair_trade
  * no_additives
  * hormone_free
  * no_preservatives
  * sugar_free
  * sulfite_free
  * corn_free
  * soy_free
  * nitrate_free
  * gmo_free
  * organic
  * kosher
  * halal
  * sustainable
  * non_alcoholic
  * lactose_free
  * whole_grain
  * whole_wheat
  * multigrain
  * sprouted_grain


## Search Grocery Products by UPC

Get information about a packaged food using its UPC.

GET

https://api.spoonacular.com/food/products/upc/{upc}

#### Headers

Response Headers:

  * `Content-Type: application/json`


#### Parameters

Name | Type | Example | Description
---|---|---|---
**`upc`** | number | 041631000564 | The product's UPC.

Example Request and Response

GET

https://api.spoonacular.com/food/products/upc/041631000564


    {
        "id": 30004,
        "title": "Swan Flour",
        "badges": [
            "egg_free",
            "wheat_free",
            "grain_free",
            "peanut_free",
            "primal",
            "vegetarian",
            "nut_free",
            "vegan",
            "pescetarian",
            "dairy_free",
            "paleo",
            "gluten_free"
        ],
        "importantBadges": [
            "gluten_free",
            "paleo",
            "primal",
            "wheat_free",
            "grain_free"
        ],
        "breadcrumbs": [
            "flour"
        ],
        "generatedText": "Swan Flour: This product is an awesome fit if you are searching for a healthy flour. This product has 1 ingredient (in our experience: the fewer ingredients, the better!) This product contains no ingredients that some research suggests you should avoid. One serving of this product provides 30 calories, 0g grams of fat, 0g grams of protein, and 8g grams of carbs.",
        "imageType": "jpg",
        "ingredientCount": null,
        "ingredientList": "Potato Starch",
        "ingredients": [
            {
                "description": null,
                "name": "",
                "safety_level": null
            },
            {
                "description": null,
                "name": "starch",
                "safety_level": null
            },
            {
                "description": null,
                "name": "potato starch",
                "safety_level": null
            }
        ],
        "likes": 0,
        "nutrition": {
            "nutrients": [
                {
                    "name": "Fat",
                    "amount": 0,
                    "unit": "g",
                    "percentOfDailyNeeds": 0
                },
                {
                    "name": "Protein",
                    "amount": 0,
                    "unit": "g",
                    "percentOfDailyNeeds": 0
                },
                {
                    "name": "Calories",
                    "amount": 30,
                    "unit": "cal",
                    "percentOfDailyNeeds": 10
                },
                {
                    "name": "Carbohydrates",
                    "amount": 8,
                    "unit": "g",
                    "percentOfDailyNeeds": 9.45
                }
            ],
            "caloricBreakdown": {
                "percentProtein": 22.22,
                "percentFat": 20,
                "percentCarbs": 57.78
            }
        },
        "price": 0.0,
        "servings": {
            "number": 34,
            "size": 1,
            "unit": "tbsp"
        },
        "spoonacularScore": 99.0,
        "credits": {
            "text": "openfoodtacts.org under (ODbL) v1.0",
            "link": "https://opendatacommons.org/licenses/odbl/1-0/",
            "image": "openfoodfacts.org under CC BY-SA 3.0 DEED",
            "imageLink": "https://creativecommons.org/licenses/by-sa/3.0/deed.en"
        }
    }

#### Quotas

Calling this endpoint requires

1 point

. Learn more about quotas.

#### Need Help? Just ask!

Ask AI

## Get Product Information

Use a product id to get full information about a product, such as ingredients, nutrition, etc. The nutritional information is per serving.

GET

https://api.spoonacular.com/food/products/{id}

#### Headers

Response Headers:

  * `Content-Type: application/json`


#### Parameters

Name | Type | Example | Description
---|---|---|---
**`id`** | number | 22347 | The id of the packaged food.

Example Request and Response

GET

https://api.spoonacular.com/food/products/22347


    {
        "id": 22347,
        "title": "SNICKERS Minis Size Chocolate Candy Bars Variety Mix 10.5-oz. Bag",
        "breadcrumbs": [
            "bars"
        ],
        "imageType": "jpg",
        "badges": [
            "msg_free",
            "no_artificial_colors",
            "no_artificial_flavors",
            "no_artificial_ingredients",
            "gluten_free"
        ],
        "importantBadges": [
            "no_artificial_flavors",
            "no_artificial_colors",
            "no_artificial_ingredients",
            "gluten_free",
            "msg_free"
        ],
        "ingredientCount": 32,
        "generatedText": null,
        "ingredientList": "Snickers Brand Almond Bar: Milk Chocolate (Sugar, Cocoa Butter, Chocolate, Skim Milk, Lactose, Milkfat, Soy Lecithin, Artificial Flavor), Corn Syrup, Almonds, Sugar, Milkfat, Skim Milk, Less than 2% - Lactose, Salt, Hydrogenated Palm Kernel Oil and/or Palm Oil, Egg Whites, Chocolate, Artificial Flavor. Snickers Brand: Milk Chocolate (Sugar, Cocoa Butter, Chocolate, Skim Milk, Lactose, Milkfat, Soy Lecithin, Artificial Flavor), Peanuts, Corn Syrup, Sugar, Milkfat, Skim Milk, Partially Hydrogenated Soybean Oil, Lactose, Salt, Egg Whites, Chocolate, Artificial Flavor. Snickers Brand Peanut Butter Squared Bars: Milk Chocolate (Sugar, Cocoa Butter, Chocolate, Skim Milk, Lactose, Milkfat, Soy Lecithin, Artificial Flavor), Peanut Butter (Peanuts, Partially Hydrogenated Soybean Oil), Peanuts, Sugar, Corn Syrup, Vegetable Oil (Hydrogenated Palm Kernel Oil, Palm Oil, Rapeseed Oil and Cottonseed Oil and/or Partially Hydrogenated Palm Kernel Oil), Lactose, Corn Syrup Solids, Invert Sugar, Less than 2% - Glycerin, Dextrose, Skim Milk, Salt, Calcium Carbonate, Partially Hydrogenated Soybean Oil, Egg Whites, Artificial Flavor, TBHQ to Maintain Freshness",
        "ingredients": [
            {
                "description": null,
                "name": "emulsifier",
                "safety_level": null
            },
            {
                "description": null,
                "name": "added sugar",
                "safety_level": null
            },
            {
                "description": null,
                "name": "sweetener",
                "safety_level": null
            },
            {
                "description": null,
                "name": "cooking fat",
                "safety_level": null
            },
            {
                "description": null,
                "name": "cooking oil",
                "safety_level": null
            },
            {
                "description": null,
                "name": "lecithin",
                "safety_level": null
            },
            {
                "description": null,
                "name": "yeast",
                "safety_level": null
            },
            {
                "description": null,
                "name": "menu item type",
                "safety_level": null
            },
            {
                "description": null,
                "name": "nuts",
                "safety_level": null
            },
            {
                "description": null,
                "name": "partially hydrogenated vegetable oil",
                "safety_level": "low"
            },
            {
                "description": "Unlike partially hydrogenated oils, fully hydrogenated oils do not contain trans fat and thus are currently considered safer.",
                "name": "hydrogenated vegetable oil",
                "safety_level": "high"
            },
            {
                "description": null,
                "name": "calcium",
                "safety_level": null
            },
            {
                "description": null,
                "name": "nut butter",
                "safety_level": null
            },
            {
                "description": null,
                "name": "legumes",
                "safety_level": null
            },
            {
                "description": null,
                "name": "refined sweetener",
                "safety_level": null
            },
            {
                "description": null,
                "name": "non food item",
                "safety_level": null
            },
            {
                "description": null,
                "name": "tree nuts",
                "safety_level": null
            },
            {
                "description": null,
                "name": "chocolate",
                "safety_level": null
            },
            {
                "description": null,
                "name": "sugar",
                "safety_level": null
            },
            {
                "description": null,
                "name": "snack",
                "safety_level": null
            },
            {
                "description": null,
                "name": "corn syrup",
                "safety_level": null
            },
            {
                "description": null,
                "name": "drink",
                "safety_level": null
            },
            {
                "description": null,
                "name": "milk",
                "safety_level": null
            },
            {
                "description": null,
                "name": "spread",
                "safety_level": null
            },
            {
                "description": null,
                "name": "vegetable oil",
                "safety_level": null
            },
            {
                "description": null,
                "name": "yeast nutrient",
                "safety_level": null
            },
            {
                "description": null,
                "name": "palm kernel oil",
                "safety_level": null
            },
            {
                "description": null,
                "name": "artificial ingredient",
                "safety_level": null
            },
            {
                "description": null,
                "name": "stabilizer",
                "safety_level": null
            },
            {
                "description": null,
                "name": "additive",
                "safety_level": null
            },
            {
                "description": null,
                "name": "nutrient",
                "safety_level": null
            },
            {
                "description": null,
                "name": "soybean oil",
                "safety_level": null
            },
            {
                "description": null,
                "name": "supplement",
                "safety_level": null
            },
            {
                "description": null,
                "name": "mineral",
                "safety_level": null
            },
            {
                "description": null,
                "name": "artificial flavor",
                "safety_level": "medium"
            },
            {
                "description": null,
                "name": "skim milk",
                "safety_level": null
            },
            {
                "description": null,
                "name": "peanuts",
                "safety_level": null
            },
            {
                "description": null,
                "name": "corn syrup solids",
                "safety_level": "medium"
            },
            {
                "description": "Unlike partially hydrogenated oils, fully hydrogenated oils do not contain trans fat and thus are currently considered safer.",
                "name": "hydrogenated palm kernel oil",
                "safety_level": "high"
            },
            {
                "description": null,
                "name": "cottonseed oil",
                "safety_level": null
            },
            {
                "description": null,
                "name": "milkfat",
                "safety_level": "high"
            },
            {
                "description": null,
                "name": "lactose",
                "safety_level": null
            },
            {
                "description": null,
                "name": "corn syrup",
                "safety_level": null
            },
            {
                "description": null,
                "name": "cocoa butter",
                "safety_level": "high"
            },
            {
                "description": null,
                "name": "tbhq to maintain freshness",
                "safety_level": null
            },
            {
                "description": null,
                "name": "peanut butter",
                "safety_level": null
            },
            {
                "description": null,
                "name": "egg whites",
                "safety_level": null
            },
            {
                "description": null,
                "name": "sugar",
                "safety_level": null
            },
            {
                "description": null,
                "name": "milk chocolate",
                "safety_level": null
            },
            {
                "description": null,
                "name": "palm oil",
                "safety_level": null
            },
            {
                "description": null,
                "name": "artificial flavor",
                "safety_level": null
            },
            {
                "description": null,
                "name": "salt",
                "safety_level": null
            },
            {
                "description": null,
                "name": "almonds",
                "safety_level": null
            },
            {
                "description": null,
                "name": "skim milk less than 2% - lactose",
                "safety_level": null
            },
            {
                "description": null,
                "name": "vegetable oil",
                "safety_level": null
            },
            {
                "description": null,
                "name": "less than 2% - glycerin",
                "safety_level": null
            },
            {
                "description": null,
                "name": "dextrose",
                "safety_level": "high"
            },
            {
                "description": "Soy lecithin is [not a concern](\\"http://farrp.unl.edu/resources/gi-fas/opinion-and-summaries/soy-lecithin\\") for most people allergic to soy.",
                "name": "soy lecithin",
                "safety_level": "high"
            },
            {
                "description": null,
                "name": "invert sugar",
                "safety_level": "high"
            },
            {
                "description": null,
                "name": "chocolate",
                "safety_level": null
            },
            {
                "description": null,
                "name": "rapeseed oil",
                "safety_level": null
            },
            {
                "description": null,
                "name": "partially hydrogenated soybean oil",
                "safety_level": "low"
            },
            {
                "description": null,
                "name": "calcium carbonate",
                "safety_level": "high"
            },
            {
                "description": null,
                "name": "partially hydrogenated palm kernel oil",
                "safety_level": "low"
            },
            {
                "description": null,
                "name": "artificial flavor.snickers brand",
                "safety_level": null
            },
            {
                "description": null,
                "name": "snickers brand almond bar",
                "safety_level": null
            }
        ],
        "likes": 0,
        "aisle": "Sweet Snacks",
        "nutrition": {
            "nutrients": [
                {
                    "name": "Fat",
                    "amount": 4,
                    "unit": "g",
                    "percentOfDailyNeeds": 6.15
                },
                {
                    "name": "Protein",
                    "amount": 10,
                    "unit": "g",
                    "percentOfDailyNeeds": 20
                },
                {
                    "name": "Calories",
                    "amount": 200,
                    "unit": "cal",
                    "percentOfDailyNeeds": 10
                },
                {
                    "name": "Carbohydrates",
                    "amount": 26,
                    "unit": "g",
                    "percentOfDailyNeeds": 9.45
                }
            ],
            "caloricBreakdown": {
                "percentProtein": 22.22,
                "percentFat": 20,
                "percentCarbs": 57.78
            }
        },
        "price": 324.0,
        "servings": {
            "number": 8,
            "size": 4,
            "unit": "pieces",
            "raw": "pcs"
        },
        "spoonacularScore": 0.0
    }

#### Quotas

Calling this endpoint requires

1 point

. Learn more about quotas.

#### Need Help? Just ask!

Ask AI

## Get Comparable Products

Find comparable products to the given one.

GET

https://api.spoonacular.com/food/products/upc/{upc}/comparable

#### Headers

Response Headers:

  * `Content-Type: application/json`


#### Parameters

Name | Type | Example | Description
---|---|---|---
**`upc`** | number | 033698816271 | The UPC of the product for which you want to find comparable products.

Example Request and Response

GET

https://api.spoonacular.com/food/products/upc/033698816271/comparable


    {
        "comparableProducts": {
            "calories": [],
            "likes": [],
            "price": [],
            "protein": [
                {
                    "difference": 3,
                    "id": 11797,
                    "image": "https://img.spoonacular.com/products/11797.jpg",
                    "title": "Casa Visco Capers"
                },
                {
                    "difference": 1,
                    "id": 90962,
                    "image": "https://img.spoonacular.com/products/90962.jpg",
                    "title": "Colavita Capers"
                },
                {
                    "difference": 1,
                    "id": 88139,
                    "image": "https://img.spoonacular.com/products/88139.jpg",
                    "title": "Mezzetta Capers"
                },
                {
                    "difference": 1,
                    "id": 152832,
                    "image": "https://spoonacular.com/com/productImages/152832.jpg",
                    "title": "Victoria Imported Capers"
                }
            ],
            "spoonacularScore": [
                {
                    "difference": 7,
                    "id": 125354,
                    "image": "https://img.spoonacular.com/products/125354.jpg",
                    "title": "DeLallo Capers"
                },
                {
                    "difference": 7,
                    "id": 118361,
                    "image": "https://spoonacular.com/com/productImages/118361.jpg",
                    "title": "Haddon House Non Pareil Capers"
                },
                {
                    "difference": 7,
                    "id": 113686,
                    "image": "https://img.spoonacular.com/products/113686.jpg",
                    "title": "Dell Alpe Capers"
                },
                {
                    "difference": 7,
                    "id": 112078,
                    "image": "https://img.spoonacular.com/products/112078.jpg",
                    "title": "Paesana Imported Capers"
                }
            ],
            "sugar": []
        }
    }

#### Quotas

Calling this endpoint requires

1 point

. Learn more about quotas.

#### Need Help? Just ask!

Ask AI

## Autocomplete Product Search

Generate suggestions for grocery products based on a (partial) query. The matches will be found by looking in the title only.

GET

https://api.spoonacular.com/food/products/suggest

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

https://api.spoonacular.com/food/products/suggest?query=chicke&number=2


    {
        "results": [
            {
                "id": 208698,
                "title": "buddig premium deli chicken breast - rotisserie flavored"
            },
            {
                "id": 41291,
                "title": "tyson all natural chicken breasts tenderloins"
            }
        ]
    }

#### Quotas

Calling this endpoint requires

0.1 points

. Learn more about quotas.

#### Need Help? Just ask!

Ask AI

## Classify Grocery Product

This endpoint allows you to match a packaged food to a basic category, e.g. a specific brand of milk to the category milk.

POST

https://api.spoonacular.com/food/products/classify

#### Headers

Request Headers:

  * `Content-Type: application/json`


Response Headers:

  * `Content-Type: application/json`


#### Parameters

Name | Type | Example | Description
---|---|---|---
**`(post body)`** | string | { "title": "Kroger Vitamin A & D Reduced Fat 2% Milk", "upc": "", "plu_code": "" } | A json object containing the product title.
`locale` | string | en_US | The display name of the returned category, supported is en_US (for American English) and en_GB (for British English).

Example Request and Response

POST

https://api.spoonacular.com/food/products/classify


    {
        "cleanTitle": "Kroger Vitamin A & D Reduced Fat 2% Milk",
        "image": "https://img.spoonacular.com/ingredients_100x100/milk.png",
        "category": "2 percent milk",
        "breadcrumbs": [
            "2 percent milk",
            "milk",
            "drink",
            "ingredient"
        ],
        "usdaCode": 1174
    }

#### Quotas

Calling this endpoint requires

0.5 points

. Learn more about quotas.

#### Need Help? Just ask!

Ask AI

## Classify Grocery Product Bulk

Provide a set of product jsons, get back classified products.

POST

https://api.spoonacular.com/food/products/classifyBatch

#### Headers

Request Headers:

  * `Content-Type: application/json`


Response Headers:

  * `Content-Type: application/json`


#### Parameters

Name | Type | Example | Description
---|---|---|---
**`(post body)`** | string | [{ "title": "Kroger Vitamin A & D Reduced Fat 2% Milk", "upc": "", "plu_code": "" }] | A json array containing objects, each with the product title.
`locale` | string | en_US | The display name of the returned category, supported is en_US (for American English) and en_GB (for British English).

Example Request and Response

POST

https://api.spoonacular.com/food/products/classifyBatch


    [
            { /* see classify grocery product result */ }
    ]

#### Quotas

Calling this endpoint requires

0.5 points

per classified product. Learn more about quotas.

#### Need Help? Just ask!

Ask AI

## Map Ingredients to Grocery Products

Map a set of ingredients to products you can buy in the grocery store.

POST

https://api.spoonacular.com/food/ingredients/map

#### Headers

Request Headers:

  * `Content-Type: application/json`


Response Headers:

  * `Content-Type: application/json`


#### Parameters

Name | Type | Example | Description
---|---|---|---
**`(post body)`** | string | { "ingredients": ["eggs","bacon"], "servings": 2 } | Input for grocery product mapping.

Example Request and Response

POST

https://api.spoonacular.com/food/ingredients/map


    [
        {
            "original": "eggs",
            "originalName": "eggs",
            "ingredientImage": "egg.png",
            "meta": [
                "egg"
            ],
            "products": [
                {
                    "id": 209945,
                    "title": "Crystal Farms Eggs - Fresh Accents Peeled Hard Cooked 2 ct Packs",
                    "upc": "075925889498"
                },
                {
                    "id": 214723,
                    "title": "Organic Valley Eggs - Organic Medium Brown",
                    "upc": "093966811100"
                },
                {
                    "id": 183228,
                    "title": "Eggland's Best Grade A Eggs Jumbo - 12 CT",
                    "upc": "715141328615"
                }
            ]
        },
        {
            "ingredientImage": "raw-bacon.png",
            "meta": [
                "bacon"
            ],
            "original": "bacon",
            "originalName": "bacon",
            "products": [
                {
                    "id": 159164,
                    "title": "Wright Bacon - Naturally Hickory Smoked",
                    "upc": "079621461552"
                },
                {
                    "id": 87924,
                    "title": "Sugardale Bacon",
                    "upc": "073890006025"
                },
                {
                    "id": 213315,
                    "title": "John Morrell Bacon - Applewood Smoked",
                    "upc": "070100060877"
                },
                {
                    "id": 94585,
                    "title": "Hormel Black Label Bacon Thick Cut",
                    "upc": "037600153041"
                }
            ]
        }
    ]

#### Quotas

Calling this endpoint requires

1 point

per mapped ingredient. Learn more about quotas.

#### Need Help? Just ask!

Ask AI