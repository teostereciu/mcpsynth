# ProductListing

*Source: https://shopify.dev/docs/api/admin-rest/2026-01/resources/productlisting*

---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04

2026-01latest

# ProductListing

Ask assistant

Multiple access scopes needed — refer to each endpoint for access scope requirements.

**Multiple access scopes needed — refer to each endpoint for access scope requirements.:**

A ProductListing resource represents a [Product](/docs/admin-api/rest/reference/products/product) which is available to your sales channel. Merchants can make products available to your sales channel directly from their Shopify admin.

You can use this resource to retrieve products that a merchant has published and display them to customers in your marketplace for sale.

A ProductListing resource itself is unable to have its attributes modified directly. The attributes of a ProductListing are inherited from the Product resource to which it is associated. Therefore, all attributes of a ProductListing should be considered _read-only_.

A product can have one of the following statuses: `active`, `draft`, or `archived`. Draft and archived are considered non-active statuses. If you create a listing for a non-active product, then the product won't be published immediately. You must change the product status to active to make the product available on a sales channel.

If the product is sold exclusively on subscription, then you can create a listing for the product only on an online store.

Was this section helpful?

YesNo

#

## Endpoints

  * [get/admin/api/latest/product_listings.json](/docs/api/admin-rest/latest/resources/productlisting#get-product-listings)

Retrieve product listings that are published to your app

[products](/docs/api/admin-graphql/latest/queries/products)

  * [get/admin/api/latest/product_listings/{product_listing_id}.json](/docs/api/admin-rest/latest/resources/productlisting#get-product-listings-product-listing-id)

Retrieve a specific product listing that is published to your app

[product](/docs/api/admin-graphql/latest/queries/product)

  * [get/admin/api/latest/product_listings/count.json](/docs/api/admin-rest/latest/resources/productlisting#get-product-listings-count)

Retrieve a count of products that are published to your app

[publishedProductsCount](/docs/api/admin-graphql/latest/queries/publishedProductsCount?example=retrieve-a-count-of-products-that-are-published-to-your-app)

  * [get/admin/api/latest/product_listings/product_ids.json](/docs/api/admin-rest/latest/resources/productlisting#get-product-listings-product-ids)

Retrieve <code>product_ids</code> that are published to your app

[products](/docs/api/admin-graphql/latest/queries/products)

  * [put/admin/api/latest/product_listings/{product_listing_id}.json](/docs/api/admin-rest/latest/resources/productlisting#put-product-listings-product-listing-id)

Create a product listing to publish a product to your app

[publishablePublish](/docs/api/admin-graphql/latest/mutations/publishablePublish?example=create-a-product-listing-to-publish-a-product-to-your-app)

  * [del/admin/api/latest/product_listings/{product_listing_id}.json](/docs/api/admin-rest/latest/resources/productlisting#delete-product-listings-product-listing-id)

Delete a product listing to unpublish a product from your app

[publishableUnpublish](/docs/api/admin-graphql/latest/mutations/publishableUnpublish?example=delete-a-product-listing-to-unpublish-a-product-from-your-app)


* * *

[Anchor to ](/docs/api/admin-rest/latest/resources/productlisting#resource-object)

## The ProductListing resource

[Anchor to ](/docs/api/admin-rest/latest/resources/productlisting#resource-object-properties)

### Properties

* * *

product_id

read-only**read-only**

->[id](/docs/api/admin-graphql/latest/objects/Product#field-Product.fields.id)

The unique identifer of the product this listing is for. The primary key for this resource.

* * *

body_html

read-only**read-only**

->[descriptionHtml](/docs/api/admin-graphql/latest/objects/Product#field-Product.fields.descriptionHtml)

The description of the product, complete with HTML formatting.

* * *

created_at

read-only**read-only**

->[createdAt](/docs/api/admin-graphql/latest/objects/Product#field-Product.fields.createdAt)

The date and time when the product was created. The API returns this in ISO 8601.

* * *

handle

read-only**read-only**

->[handle](/docs/api/admin-graphql/latest/objects/Product#field-Product.fields.handle)

A human-friendly unique string for the Product automatically generated from its title.

* * *

images

read-only**read-only**

->[media](/docs/api/admin-graphql/latest/objects/Product#field-Product.fields.media)

A list of image objects, each one representing an image associated with the product.

* * *

options

read-only**read-only**

->[options](/docs/api/admin-graphql/latest/objects/Product#field-Product.fields.options)

Custom product property names like "Size", "Color", and "Material".

* * *

product_type

read-only**read-only**

->[productType](/docs/api/admin-graphql/latest/objects/Product#field-Product.fields.productType)

A categorization that a product can be tagged with, commonly used for filtering.

* * *

published_at

read-only**read-only**

->[publishedAt](/docs/api/admin-graphql/latest/objects/Product#field-Product.fields.publishedAt)

The date and time when the product was published. The API returns this in ISO 8601.

* * *

tags

read-only**read-only**

->[tags](/docs/api/admin-graphql/latest/objects/Product#field-Product.fields.tags)

A categorization that a product can be tagged with, commonly used for filtering.

* * *

title

read-only**read-only**

->[title](/docs/api/admin-graphql/latest/objects/Product#field-Product.fields.title)

The name of the product.

* * *

updated_at

read-only**read-only**

->[updatedAt](/docs/api/admin-graphql/latest/objects/Product#field-Product.fields.updatedAt)

The date and time when the product was last modified. The API returns this in ISO 8601.

* * *

variants

read-only**read-only**

->[variants](/docs/api/admin-graphql/latest/objects/Product#field-Product.fields.variants)

A list of variant objects, each one representing a slightly different version of the product. For example, if a product comes in different sizes and colors, each size and color permutation (such as "small black", "medium black", "large blue"), would be a variant.

To reorder variants, update the product with the variants in the desired order. The position attribute on the variant will be ignored.

Show variants properties

  * **barcode** : The barcode, UPC or ISBN number for the product.
  * **compare_at_price** : The competitor's price for the same item.
  * **created_at** : The date and time when the product variant was created. The API returns this in ISO 8601.
  * **fulfillment_service** : Service which is handling fulfillment. Valid values are: `manual`, `gift_card`, or the handle of a [FulfillmentService](/docs/admin-api/rest/reference/shipping-and-fulfillment/fulfillmentservice).
  * **grams** : The weight of the product variant in grams.
  * **weight** : The weight of the product variant in the unit system specified with **weight_unit**.
  * **weight_unit** : The unit system that the product variant's weight is measure in. The weight_unit can be either "g", "kg, "oz", or "lb".
  * **id** : The unique numeric identifier for the product variant.
  * **inventory_management** : Specifies whether or not Shopify tracks the number of items in stock for this product variant.
  * **inventory_policy** : Specifies whether or not customers are allowed to place an order for a product variant when it's out of stock.
  * **inventory_quantity** : The number of items available to the product listing for the product variant.
  * **metafield** : Attaches additional information to a shop's resources.
  * **option** : Custom properties that a shop owner can use to define product variants. Multiple options can exist. Options are represented as: `option1`, `option2`, `option3`, etc.
  * **position** : The order of the product variant in the list of product variants. 1 is the first position. To reorder variants, update the product with the variants in the desired order. The position attribute on the variant will be ignored.
  * **price** : The price of the product variant.
  * **product_id** : The unique numeric identifier for the product.
  * **requires_shipping** : Specifies whether or not a customer needs to provide a shipping address when placing an order for this product variant.
  * **sku** : A unique identifier for the product in the shop.
  * **taxable** : Specifies whether or not a tax is charged when the product variant is sold.
  * **title** : The title of the product variant.
  * **updated_at** : The date and time when the product variant was last modified. The API returns this in ISO 8601.


* * *

vendor

read-only**read-only**

->[vendor](/docs/api/admin-graphql/latest/objects/Product#field-Product.fields.vendor)

The name of the vendor of the product.

* * *

Was this section helpful?

YesNo

{}

## The ProductListing resource

99

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

30

31

32

33

34

35

36

37

38

39

40

41

42

43

44

45

46

{

"product_id": {

"product_id": 1053727709

},

"body_html": "It's the small iPod with a big idea: Video.",

"created_at": "2012-02-15T15:12:21-05:00",

"handle": "ipod-nano",

"images": [

{

"src": "http://example.com/burton.jpg"

}

],

"options": [

{

"name": "Title"

}

],

"product_type": "Cult Products",

"published_at": "2007-12-31T19:00:00-05:00",

"tags": "Emotive, Flash Memory, MP3, Music",

"title": "IPod Nano - 8GB",

"updated_at": "2012-08-24T14:01:47-04:00",

"variants": {

"barcode": "1234_pink",

"compare_at_price": null,

"created_at": "2012-08-24T14:01:47-04:00",

"fulfillment_service": "manual",

"grams": 567,

"weight": 0.2,

"weight_unit": "kg",

"id": 808950810,

"inventory_management": "shopify",

"inventory_policy": "continue",

"inventory_quantity": 10,

"option1": "Pink",

"position": 1,

"price": 199.99,

"product_id": 632910392,

"requires_shipping": true,

"sku": "IPOD2008PINK",

"taxable": true,

"title": "Pink",

"updated_at": "2012-08-24T14:01:47-04:00"

},

"vendor": "Apple"

}

* * *

##

[Anchor to GET request, Retrieve product listings that are published to your app](/docs/api/admin-rest/latest/resources/productlisting#get-product-listings)

get

Retrieve product listings that are published to your app

[products](/docs/api/admin-graphql/latest/queries/products)

Requires `product_listings` access scope.

**Requires `product_listings` access scope.:**

Retrieve product listings that are published to your app. **Note:** This endpoint implements pagination by using links that are provided in the response header. To learn more, refer to [Make paginated requests to the REST Admin API](/api/usage/pagination-rest).

###

[Anchor to Parameters of Retrieve product listings that are published to your app](/docs/api/admin-rest/latest/resources/productlisting#get-product-listings-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

collection_id

Filter by products belonging to a particular collection

* * *

handle

Filter by product handle

* * *

limit

≤ 1000**≤ 1000**

default 50**default 50**

Amount of results

* * *

product_ids

A comma-separated list of product ids

* * *

updated_at_min

Filter by product listings last updated after a certain date and time (formatted in ISO 8601)

* * *

Was this section helpful?

YesNo

###

[Anchor to get-product-listings-examples](/docs/api/admin-rest/latest/resources/productlisting#get-product-listings-examples)Examples

Retrieve product listings that are published to your app

Was this section helpful?

YesNo

get

## /admin/api/2026-01/product_listings.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/product_listings.json" \

-H "X-Shopify-Access-Token: {access_token}"

{}

## Response

JSON

999

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

30

31

32

33

34

35

36

HTTP/1.1 200 OK

{

"product_listings": [

{

"product_id": 632910392,

"created_at": "2026-01-09T17:04:11-05:00",

"updated_at": "2026-01-09T17:04:11-05:00",

"body_html": "<p>It's the small iPod with one very big idea: Video. Now the world's most popular music player, available in 4GB and 8GB models, lets you enjoy TV shows, movies, video podcasts, and more. The larger, brighter display means amazing picture quality. In six eye-catching colors, iPod nano is stunning all around. And with models starting at just $149, little speaks volumes.</p>",

"handle": "ipod-nano",

"product_type": "Cult Products",

"title": "IPod Nano - 8GB",

"vendor": "Apple",

"available": true,

"tags": "Emotive, Flash Memory, MP3, Music",

"published_at": "2017-08-31T20:00:00-04:00",

"variants": [

{

"id": 808950810,

"title": "Pink",

"option_values": [

{

"option_id": 594680422,

"name": "Color",

"value": "Pink"

}

],

"price": "199.00",

"formatted_price": "$199.00",

"compare_at_price": null,

"grams": 567,

"requires_shipping": true,

"sku": "IPOD2008PINK",

"barcode": "1234_pink",

"taxable": true,

"position": 1,

"available": true,

### examples

  * #### Retrieve product listings that are published to your app

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/product_listings.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.ProductListing.all({
          session: session,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::ProductListing.all(
          session: test_session,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.ProductListing.all({
          session: session,
        });

#### response

        HTTP/1.1 200 OK{"product_listings":[{"product_id":632910392,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","body_html":"<p>It's the small iPod with one very big idea: Video. Now the world's most popular music player, available in 4GB and 8GB models, lets you enjoy TV shows, movies, video podcasts, and more. The larger, brighter display means amazing picture quality. In six eye-catching colors, iPod nano is stunning all around. And with models starting at just $149, little speaks volumes.</p>","handle":"ipod-nano","product_type":"Cult Products","title":"IPod Nano - 8GB","vendor":"Apple","available":true,"tags":"Emotive, Flash Memory, MP3, Music","published_at":"2017-08-31T20:00:00-04:00","variants":[{"id":808950810,"title":"Pink","option_values":[{"option_id":594680422,"name":"Color","value":"Pink"}],"price":"199.00","formatted_price":"$199.00","compare_at_price":null,"grams":567,"requires_shipping":true,"sku":"IPOD2008PINK","barcode":"1234_pink","taxable":true,"position":1,"available":true,"inventory_policy":"continue","inventory_quantity":10,"inventory_management":"shopify","fulfillment_service":"manual","weight":1.25,"weight_unit":"lb","image_id":562641783,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00"},{"id":49148385,"title":"Red","option_values":[{"option_id":594680422,"name":"Color","value":"Red"}],"price":"199.00","formatted_price":"$199.00","compare_at_price":null,"grams":567,"requires_shipping":true,"sku":"IPOD2008RED","barcode":"1234_red","taxable":true,"position":2,"available":true,"inventory_policy":"continue","inventory_quantity":20,"inventory_management":"shopify","fulfillment_service":"manual","weight":1.25,"weight_unit":"lb","image_id":null,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00"},{"id":39072856,"title":"Green","option_values":[{"option_id":594680422,"name":"Color","value":"Green"}],"price":"199.00","formatted_price":"$199.00","compare_at_price":null,"grams":567,"requires_shipping":true,"sku":"IPOD2008GREEN","barcode":"1234_green","taxable":true,"position":3,"available":true,"inventory_policy":"continue","inventory_quantity":30,"inventory_management":"shopify","fulfillment_service":"manual","weight":1.25,"weight_unit":"lb","image_id":null,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00"},{"id":457924702,"title":"Black","option_values":[{"option_id":594680422,"name":"Color","value":"Black"}],"price":"199.00","formatted_price":"$199.00","compare_at_price":null,"grams":567,"requires_shipping":true,"sku":"IPOD2008BLACK","barcode":"1234_black","taxable":true,"position":4,"available":true,"inventory_policy":"continue","inventory_quantity":40,"inventory_management":"shopify","fulfillment_service":"manual","weight":1.25,"weight_unit":"lb","image_id":null,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00"}],"images":[{"id":850703190,"created_at":"2026-01-09T17:04:11-05:00","position":1,"updated_at":"2026-01-09T17:04:11-05:00","product_id":632910392,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano.png?v=1767996251","variant_ids":[],"width":123,"height":456},{"id":562641783,"created_at":"2026-01-09T17:04:11-05:00","position":2,"updated_at":"2026-01-09T17:04:11-05:00","product_id":632910392,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano-2.png?v=1767996251","variant_ids":[808950810],"width":123,"height":456},{"id":378407906,"created_at":"2026-01-09T17:04:11-05:00","position":3,"updated_at":"2026-01-09T17:04:11-05:00","product_id":632910392,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano.png?v=1767996251","variant_ids":[],"width":123,"height":456}],"options":[{"id":594680422,"name":"Color","product_id":632910392,"position":1,"values":["Pink","Red","Green","Black"]}]},{"product_id":921728736,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","body_html":"<p>The iPod Touch has the iPhone's multi-touch interface, with a physical home button off the touch screen. The home screen has a list of buttons for the available applications.</p>","handle":"ipod-touch","product_type":"Cult Products","title":"IPod Touch 8GB","vendor":"Apple","available":true,"tags":"","published_at":"2017-08-31T20:00:00-04:00","variants":[{"id":447654529,"title":"Black","option_values":[{"option_id":891236591,"name":"Title","value":"Black"}],"price":"199.00","formatted_price":"$199.00","compare_at_price":null,"grams":567,"requires_shipping":true,"sku":"IPOD2009BLACK","barcode":"1234_black","taxable":true,"position":1,"available":true,"inventory_policy":"continue","inventory_quantity":13,"inventory_management":"shopify","fulfillment_service":"manual","weight":1.25,"weight_unit":"lb","image_id":null,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00"}],"images":[],"options":[{"id":891236591,"name":"Title","product_id":921728736,"position":1,"values":["Black"]}]}]}


* * *

##

[Anchor to GET request, Retrieve a specific product listing that is published to your app](/docs/api/admin-rest/latest/resources/productlisting#get-product-listings-product-listing-id)

get

Retrieve a specific product listing that is published to your app

[product](/docs/api/admin-graphql/latest/queries/product)

Requires `product_listings` access scope.

**Requires `product_listings` access scope.:**

Retrieve a specific product listing that is published to your app

###

[Anchor to Parameters of Retrieve a specific product listing that is published to your app](/docs/api/admin-rest/latest/resources/productlisting#get-product-listings-product-listing-id-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

product_listing_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to get-product-listings-product-listing-id-examples](/docs/api/admin-rest/latest/resources/productlisting#get-product-listings-product-listing-id-examples)Examples

Retrieve a specific product listing that is published to your app

Path parameters

product_listing_id=921728736

string**string**

required**required**

Was this section helpful?

YesNo

get

## /admin/api/2026-01/product_listings/921728736.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/product_listings/921728736.json" \

-H "X-Shopify-Access-Token: {access_token}"

{}

## Response

JSON

99

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

30

31

32

33

34

35

36

37

38

39

40

41

42

43

44

45

46

47

48

49

50

51

52

53

54

55

56

57

58

59

60

HTTP/1.1 200 OK

{

"product_listing": {

"product_id": 921728736,

"created_at": "2026-01-09T17:04:11-05:00",

"updated_at": "2026-01-09T17:04:11-05:00",

"body_html": "<p>The iPod Touch has the iPhone's multi-touch interface, with a physical home button off the touch screen. The home screen has a list of buttons for the available applications.</p>",

"handle": "ipod-touch",

"product_type": "Cult Products",

"title": "IPod Touch 8GB",

"vendor": "Apple",

"available": true,

"tags": "",

"published_at": "2017-08-31T20:00:00-04:00",

"variants": [

{

"id": 447654529,

"title": "Black",

"option_values": [

{

"option_id": 891236591,

"name": "Title",

"value": "Black"

}

],

"price": "199.00",

"formatted_price": "$199.00",

"compare_at_price": null,

"grams": 567,

"requires_shipping": true,

"sku": "IPOD2009BLACK",

"barcode": "1234_black",

"taxable": true,

"position": 1,

"available": true,

"inventory_policy": "continue",

"inventory_quantity": 13,

"inventory_management": "shopify",

"fulfillment_service": "manual",

"weight": 1.25,

"weight_unit": "lb",

"image_id": null,

"created_at": "2026-01-09T17:04:11-05:00",

"updated_at": "2026-01-09T17:04:11-05:00"

}

],

"images": [],

"options": [

{

"id": 891236591,

"name": "Title",

"product_id": 921728736,

"position": 1,

"values": [

"Black"

]

}

]

}

}

### examples

  * #### Retrieve a specific product listing that is published to your app

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/product_listings/921728736.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.ProductListing.find({
          session: session,
          product_id: 921728736,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::ProductListing.find(
          session: test_session,
          product_id: 921728736,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.ProductListing.find({
          session: session,
          product_id: 921728736,
        });

#### response

        HTTP/1.1 200 OK{"product_listing":{"product_id":921728736,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","body_html":"<p>The iPod Touch has the iPhone's multi-touch interface, with a physical home button off the touch screen. The home screen has a list of buttons for the available applications.</p>","handle":"ipod-touch","product_type":"Cult Products","title":"IPod Touch 8GB","vendor":"Apple","available":true,"tags":"","published_at":"2017-08-31T20:00:00-04:00","variants":[{"id":447654529,"title":"Black","option_values":[{"option_id":891236591,"name":"Title","value":"Black"}],"price":"199.00","formatted_price":"$199.00","compare_at_price":null,"grams":567,"requires_shipping":true,"sku":"IPOD2009BLACK","barcode":"1234_black","taxable":true,"position":1,"available":true,"inventory_policy":"continue","inventory_quantity":13,"inventory_management":"shopify","fulfillment_service":"manual","weight":1.25,"weight_unit":"lb","image_id":null,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00"}],"images":[],"options":[{"id":891236591,"name":"Title","product_id":921728736,"position":1,"values":["Black"]}]}}


* * *

##

[Anchor to GET request, Retrieve a count of products that are published to your app](/docs/api/admin-rest/latest/resources/productlisting#get-product-listings-count)

get

Retrieve a count of products that are published to your app

[publishedProductsCount](/docs/api/admin-graphql/latest/queries/publishedProductsCount?example=retrieve-a-count-of-products-that-are-published-to-your-app)

Requires `product_listings` access scope.

**Requires `product_listings` access scope.:**

Retrieve a count of products that are published to your app

###

[Anchor to Parameters of Retrieve a count of products that are published to your app](/docs/api/admin-rest/latest/resources/productlisting#get-product-listings-count-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to get-product-listings-count-examples](/docs/api/admin-rest/latest/resources/productlisting#get-product-listings-count-examples)Examples

Retrieve a count of products that are published to your app

Was this section helpful?

YesNo

get

## /admin/api/2026-01/product_listings/count.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/product_listings/count.json" \

-H "X-Shopify-Access-Token: {access_token}"

{}

## Response

JSON

9

1

2

3

4

HTTP/1.1 200 OK

{

"count": 2

}

### examples

  * #### Retrieve a count of products that are published to your app

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/product_listings/count.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.ProductListing.count({
          session: session,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::ProductListing.count(
          session: test_session,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.ProductListing.count({
          session: session,
        });

#### response

        HTTP/1.1 200 OK{"count":2}


* * *

##

[Anchor to GET request, Retrieve <code>product_ids</code> that are published to your app](/docs/api/admin-rest/latest/resources/productlisting#get-product-listings-product-ids)

get

Retrieve product_ids that are published to your app

[products](/docs/api/admin-graphql/latest/queries/products)

Retrieve `product_ids` that are published to your app. Maximum 1,000 results per page.

###

[Anchor to Parameters of Retrieve <code>product_ids</code> that are published to your app](/docs/api/admin-rest/latest/resources/productlisting#get-product-listings-product-ids-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

limit

≤ 1000**≤ 1000**

default 50**default 50**

Amount of results

* * *

Was this section helpful?

YesNo

###

[Anchor to get-product-listings-product-ids-examples](/docs/api/admin-rest/latest/resources/productlisting#get-product-listings-product-ids-examples)Examples

Retrieve `product_ids` that are published to your app

Was this section helpful?

YesNo

get

## /admin/api/2026-01/product_listings/product_ids.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/product_listings/product_ids.json" \

-H "X-Shopify-Access-Token: {access_token}"

{}

## Response

JSON

9

1

2

3

4

5

6

7

HTTP/1.1 200 OK

{

"product_ids": [

921728736,

632910392

]

}

### examples

  * #### Retrieve <code>product_ids</code> that are published to your app

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/product_listings/product_ids.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.ProductListing.product_ids({
          session: session,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::ProductListing.product_ids(
          session: test_session,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.ProductListing.product_ids({
          session: session,
        });

#### response

        HTTP/1.1 200 OK{"product_ids":[921728736,632910392]}


* * *

##

[Anchor to PUT request, Create a product listing to publish a product to your app](/docs/api/admin-rest/latest/resources/productlisting#put-product-listings-product-listing-id)

put

Create a product listing to publish a product to your app

[publishablePublish](/docs/api/admin-graphql/latest/mutations/publishablePublish?example=create-a-product-listing-to-publish-a-product-to-your-app)

Requires `product_listings` access scope.

**Requires `product_listings` access scope.:**

Create a product listing to publish a product to your app

###

[Anchor to Parameters of Create a product listing to publish a product to your app](/docs/api/admin-rest/latest/resources/productlisting#put-product-listings-product-listing-id-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

product_listing_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to put-product-listings-product-listing-id-examples](/docs/api/admin-rest/latest/resources/productlisting#put-product-listings-product-listing-id-examples)Examples

Create a product listing to publish a product to your app

Path parameters

product_listing_id=921728736

string**string**

required**required**

Request body

product_listing

Product_listing resource**Product_listing resource**

Show product_listing properties

product_listing.product_id:921728736

read-only**read-only**

The unique identifer of the product this listing is for. The primary key for this resource.

Was this section helpful?

YesNo

put

## /admin/api/2026-01/product_listings/921728736.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{"product_listing":{"product_id":921728736}}' \

-X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/product_listings/921728736.json" \

-H "X-Shopify-Access-Token: {access_token}" \

-H "Content-Type: application/json"

{}

## Response

JSON

99

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

30

31

32

33

34

35

36

37

38

39

40

41

42

43

44

45

46

47

48

49

50

51

52

53

54

55

56

57

58

59

60

HTTP/1.1 200 OK

{

"product_listing": {

"product_id": 921728736,

"created_at": "2026-01-09T17:04:11-05:00",

"updated_at": "2026-01-09T17:04:11-05:00",

"body_html": "<p>The iPod Touch has the iPhone's multi-touch interface, with a physical home button off the touch screen. The home screen has a list of buttons for the available applications.</p>",

"handle": "ipod-touch",

"product_type": "Cult Products",

"title": "IPod Touch 8GB",

"vendor": "Apple",

"available": true,

"tags": "",

"published_at": "2017-08-31T20:00:00-04:00",

"variants": [

{

"id": 447654529,

"title": "Black",

"option_values": [

{

"option_id": 891236591,

"name": "Title",

"value": "Black"

}

],

"price": "199.00",

"formatted_price": "$199.00",

"compare_at_price": null,

"grams": 567,

"requires_shipping": true,

"sku": "IPOD2009BLACK",

"barcode": "1234_black",

"taxable": true,

"position": 1,

"available": true,

"inventory_policy": "continue",

"inventory_quantity": 13,

"inventory_management": "shopify",

"fulfillment_service": "manual",

"weight": 1.25,

"weight_unit": "lb",

"image_id": null,

"created_at": "2026-01-09T17:04:11-05:00",

"updated_at": "2026-01-09T17:04:11-05:00"

}

],

"images": [],

"options": [

{

"id": 891236591,

"name": "Title",

"product_id": 921728736,

"position": 1,

"values": [

"Black"

]

}

]

}

}

### examples

  * #### Create a product listing to publish a product to your app

#####

        curl -d '{"product_listing":{"product_id":921728736}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/product_listings/921728736.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const product_listing = new admin.rest.resources.ProductListing({session: session});

        product_listing.product_id = 921728736;
        await product_listing.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        product_listing = ShopifyAPI::ProductListing.new(session: test_session)
        product_listing.product_id = 921728736
        product_listing.save!

#####

        // Session is built by the OAuth process

        const product_listing = new shopify.rest.ProductListing({session: session});
        product_listing.product_id = 921728736;
        await product_listing.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"product_listing":{"product_id":921728736,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","body_html":"<p>The iPod Touch has the iPhone's multi-touch interface, with a physical home button off the touch screen. The home screen has a list of buttons for the available applications.</p>","handle":"ipod-touch","product_type":"Cult Products","title":"IPod Touch 8GB","vendor":"Apple","available":true,"tags":"","published_at":"2017-08-31T20:00:00-04:00","variants":[{"id":447654529,"title":"Black","option_values":[{"option_id":891236591,"name":"Title","value":"Black"}],"price":"199.00","formatted_price":"$199.00","compare_at_price":null,"grams":567,"requires_shipping":true,"sku":"IPOD2009BLACK","barcode":"1234_black","taxable":true,"position":1,"available":true,"inventory_policy":"continue","inventory_quantity":13,"inventory_management":"shopify","fulfillment_service":"manual","weight":1.25,"weight_unit":"lb","image_id":null,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00"}],"images":[],"options":[{"id":891236591,"name":"Title","product_id":921728736,"position":1,"values":["Black"]}]}}


* * *

##

[Anchor to DELETE request, Delete a product listing to unpublish a product from your app](/docs/api/admin-rest/latest/resources/productlisting#delete-product-listings-product-listing-id)

del

Delete a product listing to unpublish a product from your app

[publishableUnpublish](/docs/api/admin-graphql/latest/mutations/publishableUnpublish?example=delete-a-product-listing-to-unpublish-a-product-from-your-app)

Requires `product_listings` access scope.

**Requires `product_listings` access scope.:**

Delete a product listing to unpublish a product from your app

###

[Anchor to Parameters of Delete a product listing to unpublish a product from your app](/docs/api/admin-rest/latest/resources/productlisting#delete-product-listings-product-listing-id-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

product_listing_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to delete-product-listings-product-listing-id-examples](/docs/api/admin-rest/latest/resources/productlisting#delete-product-listings-product-listing-id-examples)Examples

Delete a product listing to unpublish a product from your app

Path parameters

product_listing_id=921728736

string**string**

required**required**

Was this section helpful?

YesNo

del

## /admin/api/2026-01/product_listings/921728736.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X DELETE "https://your-development-store.myshopify.com/admin/api/2026-01/product_listings/921728736.json" \

-H "X-Shopify-Access-Token: {access_token}"

{}

## Response

JSON

9

1

HTTP/1.1 200 OK

### examples

  * #### Delete a product listing to unpublish a product from your app

#####

        curl -X DELETE "https://your-development-store.myshopify.com/admin/api/2026-01/product_listings/921728736.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.ProductListing.delete({
          session: session,
          product_id: 921728736,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::ProductListing.delete(
          session: test_session,
          product_id: 921728736,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.ProductListing.delete({
          session: session,
          product_id: 921728736,
        });

#### response

        HTTP/1.1 200 OK