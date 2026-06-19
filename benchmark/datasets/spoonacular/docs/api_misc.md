# Misc

*Source: https://spoonacular.com/food-api/docs#Misc*

---

## Search All Food

Search all food content with one call. That includes recipes, grocery products, menu items, simple foods (ingredients), and food videos.

GET

https://api.spoonacular.com/food/search

#### Headers

Response Headers:

  * `Content-Type: application/json`


#### Parameters

Name | Type | Example | Description
---|---|---|---
**`query`** | string | apple | The search query.
`offset` | number | 0 | The number of results to skip (between 0 and 990).
`number` | number | 10 | The number of expected results (between 1 and 100).

Example Request and Response

GET

https://api.spoonacular.com/food/search?query=apple&number=2


    {
      "query": "apple",
      "totalResults": 5826,
      "limit": 2,
      "offset": 0,
      "searchResults": [
        {
          "name": "Recipes",
          "totalResults": 167,
          "results": [
            {
        	  "id": 632485,
              "name": "Apple Cake",
              "image": "https://img.spoonacular.com/recipes/632485-312x231.jpg",
              "link": "https://spoonacular.com/recipes/apple-cake-632485",
              "type": "HTML",
              "relevance": 10000,
              "content": "Apple Cake might be just the dessert you are searching for..."
            },
            {
        	  "id": 632522,
              "name": "Apple Crumble",
              "image": "https://img.spoonacular.com/recipes/632522-312x231.jpg",
              "link": "https://spoonacular.com/recipes/apple-crumble-632522",
              "type": "HTML",
              "relevance": 9999,
              "content": "Apple Crumble might be just the dessert you are searching for..."
            }
          ]
        },
        {
          "name": "Products",
          "totalResults": 3219,
          "results": [
            {
              "id": 428571,
              "name": "Pleasant Valley Apple Wine",
              "image": "https://img.spoonacular.com/products/469604-312x231.jpg",
              "link": "https://spoonacular.com/products/pleasant-valley-apple-wine-469604",
              "type": "HTML",
              "relevance": 10000
            },
            {
              "id": 428573,
              "name": "NV Georgetown Vineyards Apple Wine",
              "image": "https://img.spoonacular.com/products/428573-312x231.jpg",
              "link": "https://spoonacular.com/products/nv-georgetown-vineyards-apple-wine-428573",
              "type": "HTML",
              "relevance": 9999
            }
          ]
        },
        {
          "name": "Menu Items",
          "totalResults": 2410,
          "results": [
            {
        	  "id": 334550,
              "name": "Old Chicago Applewood Spiced BBQ Chicken Pizza, Chicago Thick, 12 Inch (Slice)",
              "image": null,
              "link": "https://spoonacular.com/menu-items/old-chicago-applewood-spiced-bbq-chicken-pizza-chicago-thick-12-inch--334550",
              "type": "HTML",
              "relevance": 10000
            },
            {
        	  "id": 422013,
              "name": "Huddle House Apple Cobbler a la mode",
              "image": null,
              "link": "https://spoonacular.com/menu-items/huddle-house-apple-cobbler-a-la-mode-422013",
              "type": "HTML",
              "relevance": 9999
            }
          ]
        },
        {
          "name": "Articles",
          "totalResults": 28,
          "results": [
            {
              "name": "Apples",
              "image": "https://img.spoonacular.com/ingredients_100x100/braeburn-apples.jpg",
              "link": "https://spoonacular.com/academy/apples",
              "type": "HTML",
              "relevance": 90.46
            },
            {
              "name": "Vinegar",
              "image": "https://img.spoonacular.com/ingredients_100x100/red-wine-vinegar.jpg",
              "link": "https://spoonacular.com/academy/vinegar",
              "type": "HTML",
              "relevance": 23.80
            }
          ]
        },
        {
          "name": "Videos",
          "totalResults": 2,
          "results": [
            {
        	  "id": "G0HENy59YkE",
              "name": "Pineapple Bundt Cake",
              "image": "https://i.ytimg.com/vi/G0HENy59YkE/hqdefault.jpg",
              "link": "https://www.youtube.com/watch?v=G0HENy59YkE",
              "type": "YOUTUBE_VIDEO",
              "relevance": 10000,
              "content": "FULL RECIPE HERE: https://tatyanaseverydayfood.com/recipe-items/pineapple-bundt-cake/..."
            },
            {
        	  "id": "xEENgO5Z5To",
              "name": "Pineapple Shrimp Tacos",
              "image": "https://i.ytimg.com/vi/xEENgO5Z5To/mqdefault.jpg",
              "link": null,
              "type": "YOUTUBE_VIDEO",
              "relevance": 9999,
              "content": "RECIPE: Below in description.\nThese Pineapple Shrimp Tacos cook in 5 minutes and assembly is a breeze..."
            }
          ]
        },
        {
          "name": "Simple Foods",
          "totalResults": 2,
          "results": [
            {
              "id": 78541,
              "name": "apple",
              "image": "apple.jpg",
              "type": "HTML",
              "relevance": 10000
            },
            {
        	  "id": 8782,
              "name": "applesauce",
              "image": "applesauce.png",
              "type": "HTML",
              "relevance": 9999
            }
          ]
        }
      ]
    }

#### Quotas

Calling this endpoint requires

3 points

and

0.01 points

per result returned. Learn more about quotas.

#### Need Help? Just ask!

Ask AI

## Search Food Videos

Find recipe and other food related videos. This endpoint searches YouTube for relevant recipe or other food-related videos. Please be sure to read the [YouTube Terms of Service](https://www.youtube.com/static?template=terms) before embedding videos into your site or app.

GET

https://api.spoonacular.com/food/videos/search

#### Headers

Response Headers:

  * `Content-Type: application/json`


#### Parameters

Name | Type | Example | Description
---|---|---|---
**`query`** | string | chicken soup | The search query.
`type` | string | main course | The type of the recipes. See a full [list of supported meal types](/food-api/docs#Meal-Types).
`cuisine` | string | italian | The cuisine(s) of the recipes. One or more, comma separated. See a full [list of supported cuisines](/food-api/docs#Cuisines).
`diet` | string | vegetarian | The diet for which the recipes must be suitable. See a full [list of supported diets](/food-api/docs#Diets).
`includeIngredients` | string | tomato,cheese | A comma-separated list of ingredients that the recipes should contain.
`excludeIngredients` | string | eggs | A comma-separated list of ingredients or ingredient types that the recipes must not contain.
`minLength` | number | 0 | Minimum video length in seconds.
`maxLength` | number | 999 | Maximum video length in seconds.
`offset` | number | 0 | The number of results to skip (between 0 and 900).
`number` | number | 10 | The number of results to return (between 1 and 100).

Example Request and Response

GET

https://api.spoonacular.com/food/videos/search?query=pasta&number=2


    {
        "videos": [
            {
                "title": "8 One-Pot Pastas",
                "length": 370,
                "rating": 0.985984219269103,
                "shortTitle": "8 One-Pot Pastas",
                "thumbnail": "https://i.ytimg.com/vi/YTZGPCCB2FU/mqdefault.jpg",
                "views": 550467,
                "youTubeId": "YTZGPCCB2FU"
            },
            {
                "title": "Macaroni salad - pasta salad recipes - healthy recipe channel - quick tasty recipe - cooking channel",
                "length": 333,
                "rating": 1.0,
                "shortTitle": "Macaroni salad",
                "thumbnail": "https://i.ytimg.com/vi/81bn4p8H3Kg/mqdefault.jpg",
                "views": 307,
                "youTubeId": "81bn4p8H3Kg"
            }
        ],
        "totalResults": 172
    }

#### Quotas

Calling this endpoint requires

1 point

and

0.01 points

per video returned. Learn more about quotas.

#### Need Help? Just ask!

Ask AI

## Quick Answer

Answer a nutrition related natural language question.

GET

https://api.spoonacular.com/recipes/quickAnswer

#### Headers

Response Headers:

  * `Content-Type: application/json`


#### Parameters

Name | Type | Example | Description
---|---|---|---
**`q`** | string | How much vitamin c is in 2 apples? | The nutrition related question.

Example Request and Response

GET

https://api.spoonacular.com/recipes/quickAnswer?q=How+much+vitamin+c+is+in+2+apples


    {
        "answer": "There are 16.74 mg of Vitamin C in 2 apples. This covers about 20% of your daily needs of Vitamin C.",
        "image": "https://img.spoonacular.com/ingredients_100x100/apple.jpg"
    }

#### Quotas

Calling this endpoint requires

1 point

. Learn more about quotas.

#### Need Help? Just ask!

Ask AI

## Detect Food in Text

Take any text and find all mentions of food contained within it. This task is also called **Named Entity Recognition (NER)**. In this case, the entities are foods. Either dishes, such as pizza or cheeseburger, or ingredients, such as cucumber or almonds.

POST

https://api.spoonacular.com/food/detect

#### Headers

Request Headers:

  * `Content-Type: application/x-www-form-urlencoded`


Response Headers:

  * `Content-Type: application/json`


#### Parameters

Name | Type | Example | Description
---|---|---|---
**`text`** | string | I like to eat delicious tacos. The only thing better is a cheeseburger with cheddar. But then again, pizza with pepperoni, mushrooms, and tomatoes is so good too! | The text in which food items, such as dish names and ingredients, should be detected in.

Example Request and Response

POST

https://api.spoonacular.com/food/detect


    {
        "annotations": [
            {
                "annotation": "cheeseburger",
                "image": "https://spoonacular.com/menuItemImages/cheeseburger.jpg",
                "tag": "dish"
            },
            {
                "annotation": "mushrooms",
                "image": "https://img.spoonacular.com/ingredients_100x100/mushrooms.png",
                "tag": "ingredient"
            },
            {
                "annotation": "pepperoni",
                "image": "https://img.spoonacular.com/ingredients_100x100/pepperoni.png",
                "tag": "ingredient"
            },
            {
                "annotation": "tomatoes",
                "image": "https://img.spoonacular.com/ingredients_100x100/tomato.png",
                "tag": "ingredient"
            },
            {
                "annotation": "cheddar",
                "image": "https://img.spoonacular.com/ingredients_100x100/cheddar-cheese.png",
                "tag": "ingredient"
            },
            {
                "annotation": "tacos",
                "image": "https://spoonacular.com/menuItemImages/taco-isolated.jpg",
                "tag": "dish"
            },
            {
                "annotation": "pizza",
                "image": "https://spoonacular.com/menuItemImages/cheese-pizza.png",
                "tag": "dish"
            }
        ]
    }


#### Interactive Demo

Change the text in the box and press "Detect". The detected dishes will be displayed in red and the detected ingredients in purple.

I like to eat delicious tacos. Only cheeseburger with cheddar are better than that. But then again, pizza with pepperoni, mushrooms, and tomatoes is so good, too!

Detect

#### Quotas

Calling this endpoint requires

1 point

. Learn more about quotas.

#### Need Help? Just ask!

Ask AI

## Search Site Content

Search spoonacular's site content. You'll be able to find everything that you could also find using the search suggestions on spoonacular.com. This is a suggest API so you can send partial strings as queries.

GET

https://api.spoonacular.com/food/site/search

#### Headers

Response Headers:

  * `Content-Type: application/json`


#### Parameters

Name | Type | Example | Description
---|---|---|---
**`query`** | string | past | The query to search for. You can also use partial queries such as "spagh" to already find spaghetti recipes, articles, grocery products, and other content.

Example Request and Response

GET

https://api.spoonacular.com/food/site/search?query=past


    {
        "Articles": [
            {
                "dataPoints": [],
                "image": "https://spoonacular.com/application/frontend/images/academy/vietnamese-cuisine.jpg",
                "link": "https://spoonacular.com/academy/vietnamese",
                "name": "Traditional Vietnamese Recipes"
            },
            {
                "dataPoints": [],
                "image": "https://spoonacular.com/application/frontend/images/academy/thai-cuisine.jpg",
                "link": "https://spoonacular.com/academy/thai",
                "name": "Authentic Thai Recipes"
            },
            {
                "dataPoints": [],
                "image": "https://spoonacular.com/application/frontend/images/academy/korean-food.jpg",
                "link": "https://spoonacular.com/academy/korean",
                "name": "Typical Korean Recipes"
            }
        ],
        "Grocery Products": [
            {
                "dataPoints": [
                    {
                        "key": "Calories",
                        "value": "30 Calories"
                    },
                    {
                        "key": "Protein",
                        "value": "2g Protein"
                    },
                    {
                        "key": "Fat",
                        "value": "0.0g Total Fat"
                    },
                    {
                        "key": "Carbs",
                        "value": "6g Carbs"
                    }
                ],
                "image": "https://img.spoonacular.com/products/218909-312x231.jpg",
                "link": "https://spoonacular.com/products/vine-ripe-tomato-paste-218909",
                "name": "Vine-ripe Tomato Paste"
            },
            {
                "dataPoints": [
                    {
                        "key": "Calories",
                        "value": "30 Calories"
                    },
                    {
                        "key": "Protein",
                        "value": "2g Protein"
                    },
                    {
                        "key": "Fat",
                        "value": "0.0g Total Fat"
                    },
                    {
                        "key": "Carbs",
                        "value": "6g Carbs"
                    }
                ],
                "image": "https://img.spoonacular.com/products/178883-312x231.jpg",
                "link": "https://spoonacular.com/products/contadina-tomato-paste-178883",
                "name": "Contadina Tomato Paste"
            },
            {
                "dataPoints": [
                    {
                        "key": "Calories",
                        "value": "30 Calories"
                    },
                    {
                        "key": "Protein",
                        "value": "2g Protein"
                    },
                    {
                        "key": "Fat",
                        "value": "0.0g Total Fat"
                    },
                    {
                        "key": "Carbs",
                        "value": "6g Carbs"
                    }
                ],
                "image": "https://img.spoonacular.com/products/137031-312x231.jpg",
                "link": "https://spoonacular.com/products/cento-tomato-paste-137031",
                "name": "Cento Tomato Paste"
            }
        ],
        "Menu Items": [
            {
                "dataPoints": [
                    {
                        "key": "Calories",
                        "value": "230 Calories"
                    },
                    {
                        "key": "Protein",
                        "value": "1g Protein"
                    },
                    {
                        "key": "Fat",
                        "value": "15g Total Fat"
                    },
                    {
                        "key": "Carbs",
                        "value": "23g Carbs"
                    }
                ],
                "image": "https://spoonacular.com/menuItemImages/stir-fry.jpg",
                "link": "https://spoonacular.com/menu-items/thai-express-stir-fry-chilli-paste-401670",
                "name": "Thai Express Stir-Fry, Chilli Paste"
            }
        ],
        "Recipes": [
            {
                "dataPoints": [
                    {
                        "key": "Cost",
                        "value": "$10.51 per serving"
                    },
                    {
                        "key": "Calories",
                        "value": "400 Calories"
                    },
                    {
                        "key": "Protein",
                        "value": "9g Protein"
                    },
                    {
                        "key": "Fat",
                        "value": "32g Total Fat"
                    },
                    {
                        "key": "Carbs",
                        "value": "26g Carbs"
                    }
                ],
                "image": "https://img.spoonacular.com/recipes/224844-556x370.jpg",
                "link": "https://spoonacular.com/recipes/chermoula-paste-224844",
                "name": "Chermoula Paste"
            },
            {
                "dataPoints": [
                    {
                        "key": "Cost",
                        "value": "$8.37 per serving"
                    },
                    {
                        "key": "Calories",
                        "value": "3560 Calories"
                    },
                    {
                        "key": "Protein",
                        "value": "119g Protein"
                    },
                    {
                        "key": "Fat",
                        "value": "319g Total Fat"
                    },
                    {
                        "key": "Carbs",
                        "value": "54g Carbs"
                    }
                ],
                "image": "https://img.spoonacular.com/recipes/146847-556x370.jpg",
                "link": "https://spoonacular.com/recipes/lulu-paste-146847",
                "name": "Lulu Paste"
            },
            {
                "dataPoints": [
                    {
                        "key": "Cost",
                        "value": "$6.68 per serving"
                    },
                    {
                        "key": "Calories",
                        "value": "990 Calories"
                    },
                    {
                        "key": "Protein",
                        "value": "53g Protein"
                    },
                    {
                        "key": "Fat",
                        "value": "86g Total Fat"
                    },
                    {
                        "key": "Carbs",
                        "value": "0.82g Carbs"
                    }
                ],
                "image": "https://img.spoonacular.com/recipes/84670-556x370.jpg",
                "link": "https://spoonacular.com/recipes/steak-paste-84670",
                "name": "Steak Paste"
            }
        ]
    }

#### Quotas

Calling this endpoint requires

0.1 points

. Learn more about quotas.

#### Need Help? Just ask!

Ask AI

## Random Food Joke

Get a random joke that is related to food. Caution: this is an endpoint for adults!

GET

https://api.spoonacular.com/food/jokes/random

#### Headers

Response Headers:

  * `Content-Type: application/json`


Example Request and Response

GET

https://api.spoonacular.com/food/jokes/random


    {
        "text": "Any salad can be a Caesar salad if you stab it enough."
    }

#### Quotas

Calling this endpoint requires

1 point

. Learn more about quotas.

#### Need Help? Just ask!

Ask AI

## Random Food Trivia

Returns random food trivia.

GET

https://api.spoonacular.com/food/trivia/random

#### Headers

Response Headers:

  * `Content-Type: application/json`


Example Request and Response

GET

https://api.spoonacular.com/food/trivia/random


    {
        "text": "The red food-coloring carmine used in Skittles and other candies is made from boiled cochineal bugs, a type of beetle."
    }

#### Quotas

Calling this endpoint requires

1 point

. Learn more about quotas.

#### Need Help? Just ask!

Ask AI

## Talk to Chatbot

This endpoint can be used to have a conversation about food with the spoonacular chatbot. Use the "Conversation Suggests" endpoint to show your user what he or she can say.

GET

https://api.spoonacular.com/food/converse

#### Headers

Response Headers:

  * `Content-Type: application/json`


#### Parameters

Name | Type | Example | Description
---|---|---|---
**`text`** | string | donut recipes | The request / question / answer from the user to the chatbot.
`contextId` | string | 342938 | An arbitrary globally unique id for your conversation. The conversation can contain states so you should pass your context id if you want the bot to be able to remember the conversation.

Example Request and Response

GET

https://api.spoonacular.com/food/converse?text=tell+me+a+joke


    {
        "answerText": "Baby, if you were a fruit you'd be a fineapple.",
        "media": []
    }


#### Learn more

See how you can write your own chatbot or test spoonacular's [food chatbot](https://spoonacular.com/chatbot).


#### Quotas

Calling this endpoint requires

1 point

. Learn more about quotas.

#### Need Help? Just ask!

Ask AI

## Conversation Suggests

This endpoint returns suggestions for things the user can say or ask the chatbot.

GET

https://api.spoonacular.com/food/converse/suggest

#### Headers

Response Headers:

  * `Content-Type: application/json`


#### Parameters

Name | Type | Example | Description
---|---|---|---
**`query`** | string | tell | A (partial) query from the user. The endpoint will return if it matches topics it can talk about.
`number` | number | 5 | The number of suggestions to return (between 1 and 25).

Example Request and Response

GET

https://api.spoonacular.com/food/converse/suggest?query=tell&number=5


    {
        "suggests": {
            "_": [
                {
                    "name": "Tell me something funny"
                },
                {
                    "name": "Tell me a food fact"
                },
                {
                    "name": "Tell me a joke"
                },
                {
                    "name": "Tell me food trivia"
                },
                {
                    "name": "Tell me a fact about food"
                }
            ]
        },
        "words": []
    }

#### Quotas

Calling this endpoint requires

0.1 points

. Learn more about quotas.

#### Need Help? Just ask!

Ask AI

## Authentication

To use the API you need an **API key**. You can get a free one by simply [signing up here](/food-api/console).

Once you have your API key, you have to put it in the request URL for every request you make like so **?apiKey=YOUR-API-KEY**.

**Attention:** Only the first query parameter is prefixed with a **?** (question mark), all subsequent ones will be prefixed with a **&** (ampersand). That is how URLs work and nothing related to our API. Here's a full example with two parameters `apiKey` and `includeNutrition`: [https://api.spoonacular.com/recipes/716429/information?apiKey=YOUR-API-KEY&includeNutrition=true](https://api.spoonacular.com/recipes/716429/information?apiKey=YOUR-API-KEY&includeNutrition=true).

Please further note that parameters are case sensitive, it is `apiKey` **not** `apikey`.

Alternatively, you can put the API key in the request header as `x-api-key`.

## Show Images

#### Ingredients

Endpoints like the ingredient autosuggestion will only give you an image name. You have to build the full URL by adding the base path to the beginning. The base path for ingredient images is **https://img.spoonacular.com/ingredients_{SIZE}/** , where **{SIZE}** is one of the following:

  * 100x100
  * 250x250
  * 500x500


So for "apple.jpg" the full path for 100x100 is <https://img.spoonacular.com/ingredients_100x100/apple.jpg>

#### Cooking Equipment

The recipe instruction endpoint will give you information about the equipment used for cooking the dish. You will again only receive the image name for the equipment. You have to build the full URL by adding the base path to the beginning. The base path for equipment images is **https://img.spoonacular.com/equipment_{SIZE}/** , where **{SIZE}** is one of the following:

  * 100x100
  * 250x250
  * 500x500


So for "slow-cooker.jpg" the full path for 100x100 is <https://img.spoonacular.com/equipment_100x100/slow-cooker.jpg>

#### Recipes

Recipe endpoints will almost always give you a recipe `id` **{ID}**. With that and the `imageType` **{TYPE}** you can build the complete image paths depending on your needs.

The base path for image URLs is **https://img.spoonacular.com/recipes/**. Once you know the recipe id **{ID}** and image type **{TYPE}** , you can complete that path to show an image. The complete path follows this pattern **https://img.spoonacular.com/recipes/{ID}-{SIZE}.{TYPE}** , where **{SIZE}** is one of the following:

  * 90x90
  * 240x150
  * 312x150
  * 312x231
  * 480x360
  * 556x370
  * 636x393


A complete image path might look like this: <https://img.spoonacular.com/recipes/1697885-556x370.jpg>

Or this: <https://img.spoonacular.com/recipes/1697885-90x90.jpg>

#### Grocery Products

Grocery product endpoints will almost always give you a product id **{ID}**. With that and the imageType **{TYPE}** you can build the complete image paths depending on your needs.

The base path for image URLs is **https://img.spoonacular.com/products/**. Once you know the product id **{ID}** and image type **{TYPE}** , you can complete that path to show an image. The complete path follows this pattern **https://img.spoonacular.com/products/{ID}-{SIZE}.{TYPE}** , where **{SIZE}** is one of the following:

  * 90x90
  * 312x231
  * 636x393


A complete image path might look like this: <https://img.spoonacular.com/products/35507-636x393.jpeg>

Or this: <https://img.spoonacular.com/products/35507-90x90.jpeg>

#### Menu Items

Menu item will almost always give you a menu item id **{ID}**. With that and the imageType **{TYPE}** you can build the complete image paths depending on your needs.

The base path for image URLs is **https://img.spoonacular.com/menu-items/**. Once you know the menu item id **{ID}** and image type **{TYPE}** , you can complete that path to show an image. The complete path follows this pattern **https://img.spoonacular.com/menu-items/{ID}-{SIZE}.{TYPE}** , where **{SIZE}** is one of the following:

  * 90x90
  * 312x231
  * 636x393


A complete image path might look like this: <https://img.spoonacular.com/menu-items/423186-636x393.png>

Or this: <https://img.spoonacular.com/menu-items/423186-90x90.png>

## List of Ingredients

If you need ingredient names in your application, you can download a list of the 1,000 most frequently used ingredients including their id so you can call the API for more information. You are allowed to cache this list on your end but it is advised to update it every once in a while due to possible ingredient id changes.

[Download ingredient list with possible units](/application/frontend/downloads/ingredients-with-possible-units.csv)


## Nutrition

Food objects (whole foods, recipes, grocery products, menu items) have nutrition. Endpoints that expose nutritional information group nutrition into three categories: Nutrients (Macro and Micro), Food Properties, and Flavonoids.

### Nutrients - Macro and Micro Nutrients

  * Calories (in kcal)
  * Fat (in g)
  * Trans Fat (in g)
  * Saturated Fat (in g)
  * Mono Unsaturated Fat (in g)
  * Poly Unsaturated Fat (in g)
  * Protein (in g)
  * Cholesterol (in mg)
  * Carbohydrates (in g)
  * Net Carbohydrates (in g)
  * Alcohol (in g)
  * Fiber (in g)
  * Sugar (in g)
  * Sodium (in mg)
  * Caffein (in mg)
  * Manganese (in mg)
  * Potassium (in mg)
  * Magnesium (in mg)
  * Calcium (in mg)
  * Copper (in mg)
  * Zinc (in mg)
  * Phosphorus (in mg)
  * Fluoride (in mg)
  * Choline (in mg)
  * Iron (in mg)
  * Vitamin A (in IU)
  * Vitamin B1 (in mg)
  * Vitamin B2 (in mg)
  * Vitamin B3 (in mg)
  * Vitamin B5 (in mg)
  * Vitamin B6 (in mg)
  * Vitamin B12 (in Âµg)
  * Vitamin C (in mg)
  * Vitamin D (in Âµg)
  * Vitamin E (in mg)
  * Vitamin K (in Âµg)
  * Folate (in Âµg)
  * Folic Acid (in Âµg)
  * Iodine (in Âµg)
  * Selenium (in Âµg)


### Food Properties

  * Glycemic Index
  * Glycemic Load


### Flavonoids

Flavonoids are food compounds called phytonutrients, which are found in many plants (fruit and vegetables) that have multiple health benefits.

  * Cyanidin (in mg)
  * Petunidin (in mg)
  * Delphinidin (in mg)
  * Malvidin (in mg)
  * Pelargonidin (in mg)
  * Peonidin (in mg)
  * Catechin (in mg)
  * Epigallocatechin (in mg)
  * Epicatechin (in mg)
  * Epicatechin 3-gallate (in mg)
  * Epigallocatechin 3-gallate (in mg)
  * Theaflavin (in mg)
  * Theaflavin-3,3'-digallate (in mg)
  * Theaflavin-3'-gallate (in mg)
  * Theaflavin-3-gallate (in mg)
  * Thearubigins (in mg)
  * Eriodictyol (in mg)
  * Hesperetin (in mg)
  * Naringenin (in mg)
  * Apigenin (in mg)
  * Luteolin (in mg)
  * Isorhamnetin (in mg)
  * Kaempferol (in mg)
  * Myricetin (in mg)
  * Quercetin (in mg)
  * Gallocatechin (in mg)


## Intolerances

Every API endpoint asking for a `intolerances` parameter can be fed with any of these intolerances.

  * Dairy
  * Egg
  * Gluten
  * Grain
  * Peanut
  * Seafood
  * Sesame
  * Shellfish
  * Soy
  * Sulfite
  * Tree Nut
  * Wheat


## Cuisines

Every API endpoint asking for a `cuisine` parameter can be fed with any of these cuisines.

  * African
  * Asian
  * American
  * British
  * Cajun
  * Caribbean
  * Chinese
  * Eastern European
  * European
  * French
  * German
  * Greek
  * Indian
  * Irish
  * Italian
  * Japanese
  * Jewish
  * Korean
  * Latin American
  * Mediterranean
  * Mexican
  * Middle Eastern
  * Nordic
  * Southern
  * Spanish
  * Thai
  * Vietnamese


## Meal Types

Every API endpoint asking for a `type` parameter can be fed with any of these meal types.

  * main course
  * side dish
  * dessert
  * appetizer
  * salad
  * bread
  * breakfast
  * soup
  * beverage
  * sauce
  * marinade
  * fingerfood
  * snack
  * drink


## Recipe Sorting Options

This is a list of possible values for the `sort` parameter of the complex recipe search endpoint.

  * (empty)
  * meta-score
  * popularity
  * healthiness
  * price
  * time
  * random
  * max-used-ingredients
  * min-missing-ingredients
  * alcohol
  * caffeine
  * copper
  * energy
  * calories
  * calcium
  * carbohydrates
  * carbs
  * choline
  * cholesterol
  * total-fat
  * fluoride
  * trans-fat
  * saturated-fat
  * mono-unsaturated-fat
  * poly-unsaturated-fat
  * fiber
  * folate
  * folic-acid
  * iodine
  * iron
  * magnesium
  * manganese
  * vitamin-b3
  * niacin
  * vitamin-b5
  * pantothenic-acid
  * phosphorus
  * potassium
  * protein
  * vitamin-b2
  * riboflavin
  * selenium
  * sodium
  * vitamin-b1
  * thiamin
  * vitamin-a
  * vitamin-b6
  * vitamin-b12
  * vitamin-c
  * vitamin-d
  * vitamin-e
  * vitamin-k
  * sugar
  * zinc


#### Health Score ('healthiness')

Score % (between 0 and 100) = Average coverage of "good" nutrients - Average coverage of "bad" nutrients.

That is, the more of your daily requirements of vitamins and minerals are covered and lower amounts of things you should limit (sugar, salt etc.) the higher the score.

## Image Classification Categories

The image classification and image analysis API endpoints can detect the following classes.

  * agnolotti
  * ahi_tuna
  * antipasto_salad
  * apple_cake
  * babka
  * baked_apple
  * baked_beans
  * baked_potato
  * baked_salmon
  * baklava
  * beef_ribs
  * beef_stew
  * beef_stroganoff
  * beer
  * bibimbap
  * biscotti
  * brisket
  * brownies
  * burger
  * burrito
  * calzone
  * caprese_salad
  * cheesecake
  * chicken_nuggets
  * chicken_wings
  * chili
  * chow_mein
  * chowder
  * churros
  * coffee
  * coleslaw
  * cookies
  * creme_brulee
  * crepes
  * cupcakes
  * donut
  * falafel
  * fish_and_chips
  * french_toast
  * fruit_salad
  * gyros
  * ice_cream
  * lasagne
  * lobster_roll
  * macarons
  * nachos
  * omelet
  * paella
  * pancakes
  * sushi


Interested in learning more? Read the entire [article](/food-api/docs#Image-Classification).

## Image Classification

This article compares **7 online image recognition services** in the context of food recognition. In particular, my goal was to find out which service is best suited to recognize and classify the dish you ordered in a restaurant based on a picture you took.

There are plenty of services out there, but I decided to compare the following as they are leaders in the field and have stable APIs:

[Amazon Rekognition](https://aws.amazon.com/rekognition/)

Image analysis by Amazon. They do not seem to have a pre-trained food model, so I used their generic tagger. Each classified image comes back with a number of tags and confidences.

[Clarifai](https://www.clarifai.com/predict)

An image analysis service that also features a special [food model](https://www.clarifai.com/models/food-image-recognition-model-bd367be194cf45149e75f01d59f77ba7), which I used for testing.

[Google Cloud Vision](https://cloud.google.com/vision)

An image analysis service by Google that also does not come with a pre-trained food model.

[Imagga](https://imagga.com/solutions/categorization-api)

Another image analysis service without a pre-trained food model. I used their generic tagger.

[Microsoft Computer Vision](https://azure.microsoft.com/en-us/services/cognitive-services/computer-vision/)

An image analysis service or (as they call it) "cognitive service" by Microsoft. No food model available.

[Watson Visual Recognition](https://www.ibm.com/cloud/watson-visual-recognition)

IBM Watson for image analysis by IBM. IBM also created a pre-trained [food-specific model](https://www.ibm.com/blogs/cloud-archive/2017/05/watson-learns-see-food-introducing-watson-visual-recognition-food-model/) that I was able to use in their API.

[spoonacular](https://spoonacular.com/food-api)

The spoonacular food API offers a food-specific model specifically trained on our test dataset.

Okay, now that we know our contenders, let's take a look at what dataset we're working with.

### The 50-Class Food Dataset

Our goal is to build/test a food dish recognizer. That is, we don't want to recognize single ingredients, such as an apple, milk, or a cup of mushrooms, but rather complex dishes that you would order in a restaurant.

To achieve this, we used the spoonacular food ontology to create a set of 518 dishes and gathered 2,781,306 images in total (over 417 GB in file size). The spoonacular food ontology is rather fine-grained, so many of the dish categories were a bit too specific (e.g. "lemon cookies"), so I reduced it down to 50 common classes with about 300 manually checked images per class.

The final dataset is **50 classes with a total of 15,742 images** (4.4 GB in size).

The images are a mixture of high quality, professional photographs (showing the perfect execution of the dish, usually NOT taken in a real restaurant setting) and "real world" images taken by people that actually ordered and received that dish (like pictures taken from the spoonacular food journal). The differences between the two types are often extreme, so I found it to be valuable to have both types in the dataset.

Have a look at the following example classes, "cookies", "burger", and "pancakes":

Now, here is the full list of the 50 food categories with images (here in [plain text](https://spoonacular.com/food-api/docs#Image-Classification-Categories)):

### Comparison of Image Classification Services

Now that we know the dataset we're working with we can test the services with pictures from the dataset. These tests can only give us a rough idea of how well the service works because, as stated earlier, not all of them have a food-specific model. More importantly, they are trained on a completely different taxonomy, which means they might not even know what "bibimbap" is or what "churros" look like.

The goal of this article, however, is to find out which services are well suited for real-world dish recognition without training your own models (as dataset preparation is the really hard part). In this context, it is fair to compare them against an unknown set of images and see what they think the images are.

I classified the same 50 images per class using each service for 2,500 classifications in total. The super long image below shows the top 5 tags/categories that each service assigned the images for each class. The percentage after the classified category is the percentage of images that received that particular tag. For example, Amazon Rekognition classified 98% of the "agnolotti" images as "Food". Good start.

Additionally, I **bolded** the category names which we should consider correct for the given images. Since the other taxonomies are not exactly the same as spoonacular's, we should still count "doughnut" as correct even if the spoonacular class is "donut".

The spoonacular column is just there for referenceâ€”since spoonacular's classifier was trained using the dataset, the category names always match and the percentage of matches is of course often higher.

The last row in the table shows how many classes in the top 5 can be considered correct. Aside from the expected 50/50 for spoonacular, we can see that the two services with special food-related classifiers, Clarifai and Watson, outperformed the other services dramatically.

In particular, the Watson food classifier seems to have been trained on a more fine-grained taxonomy. This is not surprising, since they say they have 2,000 tags, ranging from specific dishes to broader categories like "sweet" and "delicacy" as well. They even differentiate between "barbecued wing" and "buffalo wing"!

To give you an idea which tags/categories each service assigned to the provided images, here are the top 50 tags for each service (for all 2,500 classified images). You can also [download the raw data](https://spoonacular.com/application/frontend/downloads/visual-recognition-comparison-charts.xlsx) if you're interested in seeing it all.

##### Top 50 Classes for Amazon Rekognition

Amazon answered with **1,029 different tags** , which is to be expected for a general classifier. The funniest tags were "T-Rex", "dynamite", and "toilet" :)

##### Top 50 Classes for Clarifai

Clarifai answered with a total of **740 different food-specific tags** (remember, they have a food-specific model). Looking at the tags with a low frequency we can see that they don't only use dishes in their model, but also have plain ingredients such as "starfruit", "watercress", and even spices like "cumin" in their model.

##### Top 50 Classes for Google Cloud Vision

Google only had a generic model, which shows in the poor results. They answered with a total of **1,831 distinct tags** , most of them food-related and some controversial ones like "shark fin soup" and "foie gras" as well.

##### Top 50 Classes for Imagga

Imagga answered with a total of **832 distinct tags** from their generic model. While most of them were food related, I also got back "concrete", "snake", and "winter" at times.

##### Top 50 Classes for Microsoft Cloud Vision

Microsoft Cognitive Services' generic model came back with at total of **1,070 distinct tags** \- most of them food related.

##### Top 50 Classes for IBM Watson

Watson returned **873 distinct food-related tags** from the food model.

##### spoonacular Confusion Matrix

For spoonacular, we were able to create an actual confusion matrix. The y-axis shows the tested classes and the x-axis the model's prediction. The diagonal (top left to bottom right) shows correct classifications.

The total accuracy of spoonacular's model is 90%. Most problematic seems to be "baked apple" with only 71% accuracy, while "beer" and "burger" are recognized with 100% accuracy - cheers to that!

### Resources and Tools Used

To run all the tests I used the [Palladian Java Toolkit](https://palladian.ai/). Its wrappers for the cloud services Clarifai, Imagga, Amazon Rekognition, IBM Watson, Google Cloud Vision, and Microsoft Cloud Vision made evaluation much easiser.

Thanks to BjÃ¶rn Hempel for writing his bachelor thesis on this topic, which you can [read here](https://palladian.ai/publications/Bj%C3%B6rn%20Hempel%20-%20Investigation%20of%20strategies%20for%20image%20classi%EF%AC%81cation.pdf).

If you're interested in more detailed information you can download the [raw data (Excel)](https://spoonacular.com/application/frontend/downloads/visual-recognition-comparison-charts.xlsx).

### Summary

If you want to reliably tag food-related images, you may want to use a service that comes with a pre-trained food model such as Clarifai, Watson, or spoonacular. If you have the time, knowledge, and resources, you can of course create your own dataset and create a custom model. Most online services allow for custom training models, but dataset creation is definitely not to be underestimated.

Also, if you want to play around with the spoonacular dish classifier, I built this [demo](https://spoonacular.com/food-api/image-analyzer-demo).

## Recipe Nutrition Label Widget

Get a recipe's nutrition label as an HTML widget.

GET

https://api.spoonacular.com/recipes/{id}/nutritionLabel

#### Headers

Response Headers:

  * `Content-Type: text/html`


#### Parameters

Name | Type | Example | Description
---|---|---|---
**`id`** | number | 641166 | The recipe id.
`defaultCss` | boolean | true | Whether the default CSS should be added to the response.
`showOptionalNutrients` | boolean | false | Whether to show optional nutrients.
`showZeroValues` | boolean | false | Whether to show zero values.
`showIngredients` | boolean | false | Whether to show a list of ingredients.

Example Request and Response

GET

https://api.spoonacular.com/recipes/641166/nutritionLabel


The response will be an HTML that may look like this:


#### Quotas

Calling this endpoint requires

1 point

. Learn more about quotas.

#### Need Help? Just ask!

Ask AI

## Recipe Nutrition Label Image

Get a recipe's nutrition label as an image.

GET

https://api.spoonacular.com/recipes/{id}/nutritionLabel.png

#### Headers

Response Headers:

  * `Content-Type: image/png`


#### Parameters

Name | Type | Example | Description
---|---|---|---
**`id`** | number | 641166 | The recipe id.
`showOptionalNutrients` | boolean | false | Whether to show optional nutrients.
`showZeroValues` | boolean | false | Whether to show zero values.
`showIngredients` | boolean | false | Whether to show a list of ingredients.

Example Request and Response

GET

https://api.spoonacular.com/recipes/641166/nutritionLabel.png


The response will be an image that may look like this:


#### Quotas

Calling this endpoint requires

3 points

. Learn more about quotas.

#### Need Help? Just ask!

Ask AI

## Recipe Nutrition Widget

Visualize a recipe's nutritional information as HTML including CSS. You can play around with that endpoint!

Full example code of how to work with widgets can be found in our [spoonacular-widget GitHub](https://github.com/ddsky/spoonacular-widgets).

POST

https://api.spoonacular.com/recipes/visualizeNutrition

#### Headers

Request Headers:

  * `Accept: text/html`
  * `Content-Type: application/x-www-form-urlencoded`


Response Headers:

  * `Content-Type: text/html`


#### Parameters

Name | Type | Example | Description
---|---|---|---
**`ingredientList`** | string | 3 oz flour | The ingredient list of the recipe, one ingredient per line.
**`servings`** | number | 2 | The number of servings.
`defaultCss` | boolean | true | Whether the default CSS should be added to the response.
`showBacklink` | boolean | true | Whether to show a backlink to spoonacular. If set false, this call counts against your quota.
`language` | string | en | The input language, either "en" or "de".

Example Request and Response

POST

https://api.spoonacular.com/recipes/visualizeNutrition


    /* HTML response */


The API response will be HTML and and could look like this, for example:


#### Quotas

Calling this endpoint requires

1 point

unless "showBacklink" is true, then 0 points. Learn more about quotas.

#### Need Help? Just ask!

Ask AI

## Recipe Nutrition by ID Widget

Visualize a recipe's nutritional information as HTML including CSS.

GET

https://api.spoonacular.com/recipes/{id}/nutritionWidget

#### Headers

Request Headers:

  * `Accept: text/html`


Response Headers:

  * `Content-Type: text/html`


#### Parameters

Name | Type | Example | Description
---|---|---|---
**`id`** | number | 1082038 | The recipe id.
`defaultCss` | boolean | true | Whether the default CSS should be added to the response.

Example Request and Response

GET

https://api.spoonacular.com/recipes/1082038/nutritionWidget


    /* HTML response */


The API response will be HTML and could look like this, for example:


#### Quotas

Calling this endpoint requires

1 point

. Learn more about quotas.

#### Need Help? Just ask!

Ask AI

## Recipe Nutrition by ID Image

Visualize a recipe's nutritional information as an image.

GET

https://api.spoonacular.com/recipes/{id}/nutritionWidget.png

#### Headers

Request Headers:

  * `Accept: image/png`


Response Headers:

  * `Content-Type: image/png`


#### Parameters

Name | Type | Example | Description
---|---|---|---
**`id`** | number | 1082038 | The recipe id.

Example Request and Response

GET

https://api.spoonacular.com/recipes/1082038/nutritionWidget.png


The response will be an image that may look like this:


#### Quotas

Calling this endpoint requires

3 points

. Learn more about quotas.

#### Need Help? Just ask!

Ask AI

## Recipe Taste Widget

Visualize a recipe's taste information as HTML including CSS. You can play around with that endpoint!

Full example code of how to work with widgets can be found in our [spoonacular-widget GitHub](https://github.com/ddsky/spoonacular-widgets).

POST

https://api.spoonacular.com/recipes/visualizeTaste

#### Headers

Request Headers:

  * `Accept: text/html`
  * `Content-Type: application/x-www-form-urlencoded`


Response Headers:

  * `Content-Type: text/html`


#### Parameters

Name | Type | Example | Description
---|---|---|---
**`ingredientList`** | string | 1 lemon | The ingredient list of the recipe, one ingredient per line.
`normalize` | boolean | false | Normalize to the strongest taste.
`rgb` | string | 75,192,192 | Red, green, blue values for the chart color.
`language` | string | en | The input language, either "en" or "de".

Example Request and Response

POST

https://api.spoonacular.com/recipes/visualizeTaste


    /* HTML response */


The API response will be HTML and and could look like this, for example:


#### Quotas

Calling this endpoint requires

1 point

. Learn more about quotas.

#### Need Help? Just ask!

Ask AI

## Recipe Taste by ID Widget

Get a recipe's taste. The tastes supported are sweet, salty, sour, bitter, savory, and fatty.

GET

https://api.spoonacular.com/recipes/{id}/tasteWidget

#### Headers

Request Headers:

  * `Accept: text/html`


Response Headers:

  * `Content-Type: text/html`


#### Parameters

Name | Type | Example | Description
---|---|---|---
**`id`** | number | 69095 | The recipe id.
`normalize` | boolean | false | Normalize to the strongest taste.
`rgb` | string | 75,192,192 | Red, green, blue values for the chart color.

Example Request and Response

GET

https://api.spoonacular.com/recipes/69095/tasteWidget


    /* HTML response */


The API response will be HTML and could look like this, for example:


#### Quotas

Calling this endpoint requires

1 point

. Learn more about quotas.

#### Need Help? Just ask!

Ask AI

## Recipe Taste by ID Image

Get a recipe's taste as an image. The tastes supported are sweet, salty, sour, bitter, savory, and fatty.

GET

https://api.spoonacular.com/recipes/{id}/tasteWidget.png

#### Headers

Request Headers:

  * `Accept: image/png`


Response Headers:

  * `Content-Type: image/png`


#### Parameters

Name | Type | Example | Description
---|---|---|---
**`id`** | number | 69095 | The recipe id.
`normalize` | boolean | false | Normalize to the strongest taste.
`rgb` | string | 75,192,192 | Red, green, blue values for the chart color.

Example Request and Response

GET

https://api.spoonacular.com/recipes/69095/tasteWidget.png


The response will be an image that may look like this:


#### Quotas

Calling this endpoint requires

3 points

. Learn more about quotas.

#### Need Help? Just ask!

Ask AI

## Equipment Widget

Visualize the equipment used to make a recipe. You can play around with that endpoint!

Full example code of how to work with widgets can be found in our [spoonacular-widget GitHub](https://github.com/ddsky/spoonacular-widgets).

POST

https://api.spoonacular.com/recipes/visualizeEquipment

#### Headers

Request Headers:

  * `Accept: text/html`
  * `Content-Type: application/x-www-form-urlencoded`


Response Headers:

  * `Content-Type: text/html`


#### Parameters

Name | Type | Example | Description
---|---|---|---
**`instructions`** | string | Preheat oven. Cut cucumber with a knife and put in a blender. | The recipe's instructions.
`view` | string | grid | How to visualize the equipment, either "grid" or "list".
`defaultCss` | boolean | true | Whether the default CSS should be added to the response.
`showBacklink` | boolean | true | Whether to show a backlink to spoonacular. If set false, this call counts against your quota.

Example Request and Response

POST

https://api.spoonacular.com/recipes/visualizeEquipment


    /* HTML response */


The API response will be HTML and could look like this, for example:


#### Quotas

Calling this endpoint requires

1 point

unless "showBacklink" is true, then 0 points. Learn more about quotas.

#### Need Help? Just ask!

Ask AI

## Equipment by ID Widget

Visualize a recipe's equipment list.

GET

https://api.spoonacular.com/recipes/{id}/equipmentWidget

#### Headers

Request Headers:

  * `Accept: text/html`


Response Headers:

  * `Content-Type: text/html`


#### Parameters

Name | Type | Example | Description
---|---|---|---
**`id`** | number | 44860 | The recipe id.
`defaultCss` | boolean | true | Whether the default CSS should be added to the response.

Example Request and Response

GET

https://api.spoonacular.com/recipes/44860/equipmentWidget


    /* HTML response */


The API response will be HTML and could look like this, for example:


#### Quotas

Calling this endpoint requires

1 point

. Learn more about quotas.

#### Need Help? Just ask!

Ask AI

## Equipment by ID Image

Visualize a recipe's equipment list as an image.

GET

https://api.spoonacular.com/recipes/{id}/equipmentWidget.png

#### Headers

Request Headers:

  * `Accept: image/png`


Response Headers:

  * `Content-Type: image/png`


#### Parameters

Name | Type | Example | Description
---|---|---|---
**`id`** | number | 44860 | The recipe id.

Example Request and Response

GET

https://api.spoonacular.com/recipes/44860/equipmentWidget.png


The response will be an image that may look like this:


#### Quotas

Calling this endpoint requires

3 points

. Learn more about quotas.

#### Need Help? Just ask!

Ask AI

## Ingredients Widget

Visualize ingredients of a recipe. You can play around with that endpoint!

Full example code of how to work with widgets can be found in our [spoonacular-widget GitHub](https://github.com/ddsky/spoonacular-widgets).

POST

https://api.spoonacular.com/recipes/visualizeIngredients

#### Headers

Request Headers:

  * `Accept: text/html`
  * `Content-Type: application/x-www-form-urlencoded`


Response Headers:

  * `Content-Type: text/html`


#### Parameters

Name | Type | Example | Description
---|---|---|---
**`ingredientList`** | string | 3 oz flour | The ingredient list of the recipe, one ingredient per line.
**`servings`** | number | 2 | The number of servings.
`measure` | string | metric | The original system of measurement, either "metric" or "us".
`view` | string | grid | How to visualize the ingredients, either "grid" or "list".
`defaultCss` | boolean | true | Whether the default CSS should be added to the response.
`showBacklink` | boolean | true | Whether to show a backlink to spoonacular. If set false, this call counts against your quota.
`language` | string | en | The input language, either "en" or "de".

Example Request and Response

POST

https://api.spoonacular.com/recipes/visualizeIngredients


    /* HTML response */


The API response will be HTML and could look like this, for example:


#### Quotas

Calling this endpoint requires

1 point

unless "showBacklink" is true, then 0 points. Learn more about quotas.

#### Need Help? Just ask!

Ask AI

## Ingredients by ID Widget

Visualize a recipe's ingredient list.

GET

https://api.spoonacular.com/recipes/{id}/ingredientWidget

#### Headers

Request Headers:

  * `Accept: text/html`


Response Headers:

  * `Content-Type: text/html`


#### Parameters

Name | Type | Example | Description
---|---|---|---
**`id`** | number | 1082038 | The recipe id.
`defaultCss` | boolean | true | Whether the default CSS should be added to the response.
`measure` | string | us | Whether the the measures should be 'us' or 'metric'.

Example Request and Response

GET

https://api.spoonacular.com/recipes/1082038/ingredientWidget


    /* HTML response */


The API response will be HTML and could look like this, for example:


#### Quotas

Calling this endpoint requires

1 point

. Learn more about quotas.

#### Need Help? Just ask!

Ask AI

## Ingredients by ID Image

Visualize a recipe's ingredient list.

GET

https://api.spoonacular.com/recipes/{id}/ingredientWidget.png

#### Headers

Request Headers:

  * `Accept: image/png`


Response Headers:

  * `Content-Type: image/png`


#### Parameters

Name | Type | Example | Description
---|---|---|---
**`id`** | number | 1082038 | The recipe id.
`measure` | string | metric | Whether the the measures should be 'us' or 'metric'.

Example Request and Response

GET

https://api.spoonacular.com/recipes/1082038/ingredientWidget


The response will be an image that may look like this:


#### Quotas

Calling this endpoint requires

3 points

. Learn more about quotas.

#### Need Help? Just ask!

Ask AI

## Price Breakdown Widget

Visualize the price breakdown of a recipe. You can play around with that endpoint!

Full example code of how to work with widgets can be found in our [spoonacular-widget GitHub](https://github.com/ddsky/spoonacular-widgets).

POST

https://api.spoonacular.com/recipes/visualizePriceEstimator

#### Headers

Request Headers:

  * `Accept: text/html`
  * `Content-Type: application/x-www-form-urlencoded`


Response Headers:

  * `Content-Type: text/html`


#### Parameters

Name | Type | Example | Description
---|---|---|---
**`ingredientList`** | string | 3 oz flour | The ingredient list of the recipe, one ingredient per line.
**`servings`** | number | 2 | The number of servings.
`mode` | number | 1 | The mode in which the widget should be delivered. 1 = separate views (compact), 2 = all in one view (full).
`defaultCss` | boolean | true | Whether the default CSS should be added to the response.
`showBacklink` | boolean | true | Whether to show a backlink to spoonacular. If set false, this call counts against your quota.
`language` | string | en | The input language, either "en" or "de".

Example Request and Response

POST

https://api.spoonacular.com/recipes/visualizePriceEstimator


    /* HTML response */


The API response will be HTML and could look like this, for example::


#### Quotas

Calling this endpoint requires

1 point

unless "showBacklink" is true, then 0 points. Learn more about quotas.

#### Need Help? Just ask!

Ask AI

## Price Breakdown by ID Widget

Visualize a recipe's price breakdown.

GET

https://api.spoonacular.com/recipes/{id}/priceBreakdownWidget

#### Headers

Request Headers:

  * `Accept: text/html`


Response Headers:

  * `Content-Type: text/html`


#### Parameters

Name | Type | Example | Description
---|---|---|---
**`id`** | number | 1082038 | The recipe id.
`defaultCss` | boolean | true | Whether the default CSS should be added to the response.
`mode` | number | 1 | The mode in which the widget should be delivered. 1 = separate views (compact), 2 = all in one view (full).

Example Request and Response

GET

https://api.spoonacular.com/recipes/1082038/priceBreakdownWidget


    /* HTML response */


The API response will be HTML and and could look like this, for example:


#### Quotas

Calling this endpoint requires

1 point

. Learn more about quotas.

#### Need Help? Just ask!

Ask AI

## Price Breakdown by ID Image

Visualize a recipe's price breakdown.

GET

https://api.spoonacular.com/recipes/{id}/priceBreakdownWidget.png

#### Headers

Request Headers:

  * `Accept: image/png`


Response Headers:

  * `Content-Type: image/png`


#### Parameters

Name | Type | Example | Description
---|---|---|---
**`id`** | number | 1082038 | The recipe id.
`mode` | number | 1 | The mode in which the widget should be delivered. 1 = separate views (compact), 2 = all in one view (full).

Example Request and Response

GET

https://api.spoonacular.com/recipes/1082038/priceBreakdownWidget.png


The response will be an image that may look like this:


#### Quotas

Calling this endpoint requires

3 points

. Learn more about quotas.

#### Need Help? Just ask!

Ask AI

## Product Nutrition Label Widget

Get a product's nutrition label as an HTML widget.

GET

https://api.spoonacular.com/food/products/{id}/nutritionLabel

#### Headers

Response Headers:

  * `Content-Type: text/html`


#### Parameters

Name | Type | Example | Description
---|---|---|---
**`id`** | number | 22347 | The product id.
`defaultCss` | boolean | true | Whether the default CSS should be added to the response.
`showOptionalNutrients` | boolean | false | Whether to show optional nutrients.
`showZeroValues` | boolean | false | Whether to show zero values.
`showIngredients` | boolean | false | Whether to show a list of ingredients.

Example Request and Response

GET

https://api.spoonacular.com/food/products/22347/nutritionLabel


    /* HTML response */


The response will be an HTML widget that may look like this:


#### Quotas

Calling this endpoint requires

1 point

. Learn more about quotas.

#### Need Help? Just ask!

Ask AI

## Product Nutrition Label Image

Get a product's nutrition label as an image.

GET

https://api.spoonacular.com/food/products/{id}/nutritionLabel.png

#### Headers

Response Headers:

  * `Content-Type: image/png`


#### Parameters

Name | Type | Example | Description
---|---|---|---
**`id`** | number | 22347 | The product id.
`showOptionalNutrients` | boolean | false | Whether to show optional nutrients.
`showZeroValues` | boolean | false | Whether to show zero values.
`showIngredients` | boolean | false | Whether to show a list of ingredients.

Example Request and Response

GET

https://api.spoonacular.com/food/products/22347/nutritionLabel.png


The response will be an image that may look like this:


#### Quotas

Calling this endpoint requires

3 points

. Learn more about quotas.

#### Need Help? Just ask!

Ask AI

## Product Nutrition by ID Widget

Visualize a product's nutritional information as HTML including CSS.

GET

https://api.spoonacular.com/food/products/{id}/nutritionWidget

#### Headers

Request Headers:

  * `Accept: text/html`


Response Headers:

  * `Content-Type: text/html`


#### Parameters

Name | Type | Example | Description
---|---|---|---
**`id`** | number | 7657 | The id of the product.
`defaultCss` | boolean | true | Whether the default CSS should be added to the response.

Example Request and Response

GET

https://api.spoonacular.com/food/products/7657/nutritionWidget


    /* HTML response */


The API response will be HTML and could look like this, for example:


#### Quotas

Calling this endpoint requires

1 point

. Learn more about quotas.

#### Need Help? Just ask!

Ask AI

## Product Nutrition by ID Image

Visualize a product's nutritional information as an image.

GET

https://api.spoonacular.com/food/products/{id}/nutritionWidget.png

#### Headers

Request Headers:

  * `Accept: image/png`


Response Headers:

  * `Content-Type: image/png`


#### Parameters

Name | Type | Example | Description
---|---|---|---
**`id`** | number | 7657 | The id of the product.

Example Request and Response

GET

https://api.spoonacular.com/food/products/7657/nutritionWidget.png


The response will be an image that may look like this:


#### Quotas

Calling this endpoint requires

3 points

. Learn more about quotas.

#### Need Help? Just ask!

Ask AI

## Menu Item Nutrition Label Widget

Visualize a menu item's nutritional label information as HTML including CSS.

GET

https://api.spoonacular.com/food/menuItems/{id}/nutritionLabel

#### Headers

Request Headers:

  * `Accept: text/html`


Response Headers:

  * `Content-Type: text/html`


#### Parameters

Name | Type | Example | Description
---|---|---|---
**`id`** | number | 342313 | The menu item id.
`defaultCss` | boolean | true | Whether the default CSS should be added to the response.
`showOptionalNutrients` | boolean | false | Whether to show optional nutrients.
`showZeroValues` | boolean | false | Whether to show zero values.
`showIngredients` | boolean | false | Whether to show a list of ingredients.

Example Request and Response

GET

https://api.spoonacular.com/food/menuItems/342313/nutritionLabel


    /* HTML response */


The response will be an HTML widget that may look like this:


#### Quotas

Calling this endpoint requires

1 point

. Learn more about quotas.

#### Need Help? Just ask!

Ask AI

## Menu Item Nutrition Label Image

Visualize a menu item's nutritional label information as an image.

GET

https://api.spoonacular.com/food/menuItems/{id}/nutritionLabel.png

#### Headers

Request Headers:

  * `Accept: image/png`


Response Headers:

  * `Content-Type: image/png`


#### Parameters

Name | Type | Example | Description
---|---|---|---
**`id`** | number | 342313 | The menu item id.
`showOptionalNutrients` | boolean | false | Whether to show optional nutrients.
`showZeroValues` | boolean | false | Whether to show zero values.
`showIngredients` | boolean | false | Whether to show a list of ingredients.

Example Request and Response

GET

https://api.spoonacular.com/food/menuItems/342313/nutritionLabel.png


The response will be an image that may look like this:


#### Quotas

Calling this endpoint requires

3 points

. Learn more about quotas.

#### Need Help? Just ask!

Ask AI

## Menu Item Nutrition by ID Widget

Visualize a menu item's nutritional information as HTML including CSS.

GET

https://api.spoonacular.com/food/menuItems/{id}/nutritionWidget

#### Headers

Request Headers:

  * `Accept: text/html`


Response Headers:

  * `Content-Type: text/html`


#### Parameters

Name | Type | Example | Description
---|---|---|---
**`id`** | number | 424571 | The menu item id.
`defaultCss` | boolean | true | Whether the default CSS should be added to the response.

Example Request and Response

GET

https://api.spoonacular.com/food/menuItems/424571/nutritionWidget


    /* HTML response */


The API response will be HTML and could look like this, for example:


#### Quotas

Calling this endpoint requires

1 point

. Learn more about quotas.

#### Need Help? Just ask!

Ask AI

## Menu Item Nutrition by ID Image

Visualize a menu item's nutritional information as HTML including CSS.

GET

https://api.spoonacular.com/food/menuItems/{id}/nutritionWidget.png

#### Headers

Request Headers:

  * `Accept: image/png`


Response Headers:

  * `Content-Type: image/png`


#### Parameters

Name | Type | Example | Description
---|---|---|---
**`id`** | number | 424571 | The menu item id.

Example Request and Response

GET

https://api.spoonacular.com/food/menuItems/424571/nutritionWidget.png


The response will be an image that may look like this:


#### Quotas

Calling this endpoint requires

3 points

. Learn more about quotas.

#### Need Help? Just ask!

Ask AI

## Create Recipe Card

Generate a recipe card for a recipe.

GET

https://api.spoonacular.com/recipes/{id}/card

#### Headers

Response Headers:

  * `Content-Type: application/json`


#### Parameters

Name | Type | Example | Description
---|---|---|---
**`id`** | number | 4632 | The recipe id.
`mask` | string | ellipseMask | The mask to put over the recipe image ("ellipseMask", "diamondMask", "starMask", "heartMask", "potMask", "fishMask").
`backgroundImage` | string | background1 | The background image ("none","background1", or "background2").
`backgroundColor` | string | ffffff | The background color for the recipe card as a hex-string.
`fontColor` | string | 333333 | The font color for the recipe card as a hex-string.

Example Request and Response

GET

https://api.spoonacular.com/recipes/4632/card


    {
        "url": "https://spoonacular.com/url-to-generated-recipe-card.jpg",
    }


The API response will contain a link to the generated image. It could look like this for example:


#### Quotas

Calling this endpoint requires

1 point

. Learn more about quotas.

#### Need Help? Just ask!

Ask AI