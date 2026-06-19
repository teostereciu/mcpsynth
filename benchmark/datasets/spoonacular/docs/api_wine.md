# Wine

*Source: https://spoonacular.com/food-api/docs#Wine*

---

## Wine Guide

Here you can see the classification spoonacular uses for wines. If you are missing a wine please let us know!


### Classification of Wines


    wine
     - white_wine
       - dry_white_wine
         - assyrtiko
         - pinot_blanc
         - cortese
         - roussanne
         - moschofilero
         - muscadet
         - viognier
         - verdicchio
         - greco
         - marsanne
         - white_burgundy
         - chardonnay
         - gruener_veltliner
         - white_rioja
         - frascati
         - gavi
         - l_acadie_blanc
         - trebbiano
         - sauvignon_blanc
         - catarratto
         - albarino
         - arneis
         - verdejo
         - vermentino
         - soave
         - pinot_grigio
         - dry_riesling
         - torrontes
       - mueller_thurgau
       - grechetto
       - gewurztraminer
       - chenin_blanc
       - white_bordeaux
       - semillon
       - riesling
       - sauternes
       - sylvaner
       - lillet_blanc
     - red_wine
       - dry_red_wine
         - petite_sirah
         - zweigelt
         - baco_noir
         - bonarda
         - cabernet_franc
         - bairrada
         - barbera_wine
         - primitivo
         - pinot_noir
         - nebbiolo
         - dolcetto
         - tannat
         - negroamaro
         - red_burgundy
         - corvina
         - rioja
         - cotes_du_rhone
         - grenache
         - malbec
         - zinfandel
         - sangiovese
         - carignan
         - carmenere
         - cesanese
         - cabernet_sauvignon
         - aglianico
         - tempranillo
         - shiraz
         - mourvedre
         - merlot
         - nero_d_avola
       - bordeaux
       - marsala
       - port
       - gamay
       - dornfelder
       - concord_wine
       - sparkling_red_wine
       - pinotage
       - agiorgitiko
     - dessert_wine
       - pedro_ximenez
       - moscato
       - late_harvest
       - ice_wine
       - white_port
       - lambrusco_dolce
       - madeira
       - banyuls
       - vin_santo
       - port
     - rose_wine
       - sparkling_rose
     - sparkling_wine
       - cava
       - cremant
       - champagne
       - prosecco
       - spumante
       - sparkling_rose
     - sherry
       - cream_sherry
       - dry_sherry
     - vermouth
       - dry_vermouth
     - fruit_wine
     - mead


## Dish Pairing for Wine

Find a dish that goes well with a given wine.

GET

https://api.spoonacular.com/food/wine/dishes

#### Headers

Response Headers:

  * `Content-Type: application/json`


#### Parameters

Name | Type | Example | Description
---|---|---|---
**`wine`** | string | malbec | The type of wine that should be paired, e.g. "merlot", "riesling", or "malbec".

Example Request and Response

GET

https://api.spoonacular.com/food/wine/dishes?wine=malbec


    {
        "pairings": [
            "stew",
            "steak",
            "chili",
            "burger"
        ],
        "text": "Malbec is a dry red wine which is bold and full bodied. It goes especially well with round steak, tri tip steak, steak, boneless pork chops, and pizza burger."
    }

#### Quotas

Calling this endpoint requires

1 point

. Learn more about quotas.

#### Need Help? Just ask!

Ask AI

## Wine Pairing

Find a wine that goes well with a food. Food can be a dish name ("steak"), an ingredient name ("salmon"), or a cuisine ("italian").

GET

https://api.spoonacular.com/food/wine/pairing

#### Headers

Response Headers:

  * `Content-Type: application/json`


#### Parameters

Name | Type | Example | Description
---|---|---|---
**`food`** | string | steak | The food to get a pairing for. This can be a dish ("steak"), an ingredient ("salmon"), or a cuisine ("italian").
`maxPrice` | number | 50 | The maximum price for the specific wine recommendation in USD.

Example Request and Response

GET

https://api.spoonacular.com/food/wine/pairing?food=steak


    {
        "pairedWines": [
            "merlot",
            "cabernet sauvignon",
            "pinot noir"
        ],
        "pairingText": "Merlot, Cabernet Sauvignon, and Pinot Noir are my top picks for Steak. After all, beef and red wine are a classic combination. Generally, leaner steaks go well with light or medium-bodied reds, such as pinot noir or merlot, while fattier steaks can handle a bold red, such as cabernet sauvingnon. The Sterling Vineyards Merlot with a 5 out of 5 star rating seems like a good match. It costs about 29 dollars per bottle.",
        "productMatches": [
            {
                "id": 428278,
                "title": "Sterling Vineyards Merlot",
                "averageRating": 1.0,
                "description": null,
                "imageUrl": "https://img.spoonacular.com/products/428278-312x231.jpg",
                "link": "https://www.amazon.com/2014-Sterling-Vineyards-Valley-Merlot/dp/B071FP8NPG?tag=spoonacular-20",
                "price": "$28.99",
                "ratingCount": 1.0,
                "score": 0.75
            }
        ]
    }

#### Quotas

Calling this endpoint requires

1 point

. Learn more about quotas.

#### Need Help? Just ask!

Ask AI

## Wine Description

Get a simple description of a certain wine, e.g. "malbec", "riesling", or "merlot".

GET

https://api.spoonacular.com/food/wine/description

#### Headers

Response Headers:

  * `Content-Type: application/json`


#### Parameters

Name | Type | Example | Description
---|---|---|---
**`wine`** | string | merlot | The name of the wine that should be paired, e.g. "merlot", "riesling", or "malbec".

Example Request and Response

GET

https://api.spoonacular.com/food/wine/description?wine=merlot


    {
        "wineDescription": "Merlot is a dry red wine which is smooth and medium bodied."
    }

#### Quotas

Calling this endpoint requires

1 point

. Learn more about quotas.

#### Need Help? Just ask!

Ask AI

## Wine Recommendation

Get a specific wine recommendation (concrete product) for a given wine type, e.g. "merlot".

GET

https://api.spoonacular.com/food/wine/recommendation

#### Headers

Response Headers:

  * `Content-Type: application/json`


#### Parameters

Name | Type | Example | Description
---|---|---|---
**`wine`** | string | merlot | The type of wine to get a specific product recommendation for.
`maxPrice` | number | 50 | The maximum price for the specific wine recommendation in USD.
`minRating` | number | 0.7 | The minimum rating of the recommended wine between 0 and 1. For example, 0.8 equals 4 out of 5 stars.
`number` | number | 3 | The number of wine recommendations expected (between 1 and 100).

Example Request and Response

GET

https://api.spoonacular.com/food/wine/recommendation?wine=merlot&number=2


    {
        "recommendedWines": [
            {
                "id": 447938,
                "title": "Rombauer Merlot",
                "averageRating": 0.96,
                "description": "Enticing and lively red color; beautifully aromatic with black cherry and ripe plum. On the palate a purity of blackcurrant, cedar and mint flavors blend together seamlessly. Soft and supple, this wine has a medium-bodied mouth-feel with plush tannins that integrate with the generous finish.Our favorite pairings for this wine include chicken parmesan, cedar-planked salmon over wild rice, and mushroom pizza.",
                "imageUrl": "https://img.spoonacular.com/products/447938-312x231.jpg",
                "link": "https://click.linksynergy.com/deeplink?id=*QCiIS6t4gA∣=2025&murl=https%3A%2F%2Fwww.wine.com%2Fproduct%2Frombauer-merlot-2008%2F116883",
                "price": "$25.59",
                "ratingCount": 5.0,
                "score": 0.8975
            },
            {
                "id": 430475,
                "title": "NV The Big Kahuna Merlot",
                "averageRating": 0.9,
                "description": "A ripe and rounded Merlot with notes of plum, blackberry, and hint of spice.",
                "imageUrl": "https://img.spoonacular.com/products/430475-312x231.jpg",
                "link": "https://www.amazon.com/Big-Kahuna-Merlot-Red-Wine/dp/B01F5XPTUW?tag=spoonacular-20",
                "price": "$6.99",
                "ratingCount": 4.0,
                "score": 0.823076923076923
            }
        ],
        "totalFound": 21
    }

#### Quotas

Calling this endpoint requires

1 point

and

0.01 points

per wine returned. Learn more about quotas.

#### Need Help? Just ask!

Ask AI