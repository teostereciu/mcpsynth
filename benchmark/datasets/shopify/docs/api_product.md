# Product

*Source: https://shopify.dev/docs/api/admin-rest/2026-01/resources/product*

---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04

2026-01latest

# Product

Ask assistant

Requires `products` access scope.

**Requires `products` access scope.:**

Important

Listing, creating, updating, and deleting products is deprecated as of REST API 2024-04. For more information, refer to the [guide to the new product model](/docs/api/admin/migrate/new-product-model).

**Important:**

Listing, creating, updating, and deleting products is deprecated as of REST API 2024-04. For more information, refer to the [guide to the new product model](/docs/api/admin/migrate/new-product-model).

The Product resource lets you update and create products in a merchant's store. You can use [product variants](/docs/admin-api/rest/reference/products/product-variant) with the Product resource to create or update different versions of the same product. You can also add or update [product images](/docs/admin-api/rest/reference/products/product-image).

You can add products to collections with the [CustomCollection](/docs/admin-api/rest/reference/products/customcollection) resource and the [SmartCollection](/docs/admin-api/rest/reference/products/smartcollection) resource.

Was this section helpful?

YesNo

#

## Endpoints

  * [post/admin/api/latest/products.json](/docs/api/admin-rest/latest/resources/product#post-products)

Create a new product

[productCreate](/docs/api/admin-graphql/latest/mutations/productCreate)

  * [get/admin/api/latest/products.json?ids=632910392,921728736](/docs/api/admin-rest/latest/resources/product#get-products?ids=632910392,921728736)

Retrieve a list of products

[products](/docs/api/admin-graphql/latest/queries/products?example=retrieve-a-list-of-products)

  * [get/admin/api/latest/products/{product_id}.json](/docs/api/admin-rest/latest/resources/product#get-products-product-id)

Retrieve a single product

[product](/docs/api/admin-graphql/latest/queries/product?example=retrieve-a-single-product)

  * [get/admin/api/latest/products/count.json](/docs/api/admin-rest/latest/resources/product#get-products-count)

Retrieve a count of products

[productsCount](/docs/api/admin-graphql/latest/queries/productsCount?example=retrieve-a-count-of-products)

  * [put/admin/api/latest/products/{product_id}.json](/docs/api/admin-rest/latest/resources/product#put-products-product-id)

Updates a product

[productUpdate](/docs/api/admin-graphql/latest/mutations/productUpdate)

  * [del/admin/api/latest/products/{product_id}.json](/docs/api/admin-rest/latest/resources/product#delete-products-product-id)

Delete a product

[productDelete](/docs/api/admin-graphql/latest/mutations/productDelete?example=delete-a-product)


* * *

[Anchor to ](/docs/api/admin-rest/latest/resources/product#resource-object)

## The Product resource

[Anchor to ](/docs/api/admin-rest/latest/resources/product#resource-object-properties)

### Properties

* * *

body_html

string**string**

->[descriptionHtml](/docs/api/admin-graphql/latest/objects/Product#field-Product.fields.descriptionHtml)

A description of the product. Supports HTML formatting.

* * *

created_at

date**date**

ISO 8601**ISO 8601**

read-only**read-only**

->[createdAt](/docs/api/admin-graphql/latest/objects/Product#field-Product.fields.createdAt)

The date and time ([ISO 8601 format](https://en.wikipedia.org/wiki/ISO_8601)) when the product was created.

* * *

handle

string**string**

->[handle](/docs/api/admin-graphql/latest/objects/Product#field-Product.fields.handle)

A unique human-friendly string for the product. Automatically generated from the product's `title`. Used by the Liquid templating language to refer to objects.

* * *

id

integer**integer**

int64**int64**

read-only**read-only**

->[id](/docs/api/admin-graphql/latest/objects/Product#field-Product.fields.id)

An unsigned 64-bit integer that's used as a unique identifier for the product. Each `id` is unique across the Shopify system. No two products will have the same `id`, even if they're from different shops.

* * *

images

array**array**

->[media](/docs/api/admin-graphql/latest/objects/Product#field-Product.fields.media)

A list of [product image](/docs/admin-api/rest/reference/products/product-image) objects, each one representing an image associated with the product.

* * *

options

array**array**

->[options](/docs/api/admin-graphql/latest/objects/Product#field-Product.fields.options)

The custom product properties. For example, **Size** , **Color** , and **Material**. Each product can have up to 3 options and each option value can be up to 255 characters. Product variants are made of up combinations of option values.

Options cannot be created without values. To create new options, a variant with an associated option value also needs to be created.

* * *

product_type

string**string**

->[productType](/docs/api/admin-graphql/latest/objects/Product#field-Product.fields.productType)

A categorization for the product used for filtering and searching products.

* * *

published_at

date**date**

ISO 8601**ISO 8601**

->[publishedAt](/docs/api/admin-graphql/latest/objects/Product#field-Product.fields.publishedAt)

The date and time ([ISO 8601 format](https://en.wikipedia.org/wiki/ISO_8601)) when the product was published. Can be set to `null` to unpublish the product from the Online Store channel.

* * *

published_scope

string**string**

->[publishedOnPublication](/docs/api/admin-graphql/latest/objects/Product#field-Product.fields.publishedOnPublication)

Whether the product is published to the Point of Sale channel. Valid values:

Show published_scope properties

  * `web`: The product isn't published to the Point of Sale channel.
  * `global`: The product is published to the Point of Sale channel.


* * *

status

string**string**

->[status](/docs/api/admin-graphql/latest/objects/Product#field-Product.fields.status)

The status of the product. Valid values:

Show status properties

  * `active`: The product is ready to sell and is available to customers on the online store, sales channels, and apps. By default, existing products are set to active.
  * `archived`: The product is no longer being sold and isn't available to customers on sales channels and apps.
  * `draft`: The product isn't ready to sell and is unavailable to customers on sales channels and apps. By default, duplicated and unarchived products are set to draft.


* * *

tags

string**string**

->[tags](/docs/api/admin-graphql/latest/objects/Product#field-Product.fields.tags)

A string of comma-separated tags that are used for filtering and search. A product can have up to 250 tags. Each tag can have up to 255 characters.

* * *

template_suffix

string**string**

->[templateSuffix](/docs/api/admin-graphql/latest/objects/Product#field-Product.fields.templateSuffix)

The suffix of the Liquid template used for the product page. If this property is specified, then the product page uses a template called "product.suffix.liquid", where "suffix" is the value of this property. If this property is <code>"" or `null`, then the product page uses the default template "product.liquid". (default: `null`)

* * *

Show 4 hidden fields

Was this section helpful?

YesNo

{}

## The Product resource

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

61

62

63

64

65

66

67

{

"body_html": "It's the small iPod with a big idea: Video.",

"created_at": "2012-02-15T15:12:21-05:00",

"handle": "ipod-nano",

"id": 632910392,

"images": [

{

"id": 850703190,

"product_id": 632910392,

"position": 1,

"created_at": "2018-01-08T12:34:47-05:00",

"updated_at": "2018-01-08T12:34:47-05:00",

"width": 110,

"height": 140,

"src": "http://example.com/burton.jpg",

"variant_ids": [

{}

]

}

],

"options": {

"id": 594680422,

"product_id": 632910392,

"name": "Color",

"position": 1,

"values": [

"Pink",

"Red",

"Green",

"Black"

]

},

"product_type": "Cult Products",

"published_at": "2007-12-31T19:00:00-05:00",

"published_scope": "global",

"status": "active",

"tags": "Emotive, Flash Memory, MP3, Music",

"template_suffix": "special",

"title": "IPod Nano - 8GB",

"updated_at": "2012-08-24T14:01:47-04:00",

"variants": [

{

"barcode": "1234_pink",

"compare_at_price": null,

"created_at": "2012-08-24T14:01:47-04:00",

"fulfillment_service": "manual",

"grams": 567,

"weight": 0.2,

"weight_unit": "kg",

"id": 808950810,

"inventory_item_id": 341629,

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

}

],

"vendor": "Apple"

}

* * *

##

[Anchor to POST request, Create a new product](/docs/api/admin-rest/latest/resources/product#post-products)

post

Create a new product

[productCreate](/docs/api/admin-graphql/latest/mutations/productCreate)

Create a new product




###

[Anchor to Parameters of Create a new product](/docs/api/admin-rest/latest/resources/product#post-products-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to post-products-examples](/docs/api/admin-rest/latest/resources/product#post-products-examples)Examples

Create a new draft product

Request body

product

Product resource**Product resource**

Show product properties

product.title:"Burton Custom Freestyle 151"

string**string**

->[title](/docs/api/admin-graphql/latest/input-objects/ProductInput#fields-title)

The name of the product.

product.body_html:"<strong>Good snowboard!</strong>"

string**string**

->[descriptionHtml](/docs/api/admin-graphql/latest/input-objects/ProductInput#fields-descriptionHtml)

A description of the product. Supports HTML formatting.

product.vendor:"Burton"

string**string**

->[vendor](/docs/api/admin-graphql/latest/input-objects/ProductInput#fields-vendor)

The name of the product's vendor.

product.product_type:"Snowboard"

string**string**

->[productType](/docs/api/admin-graphql/latest/input-objects/ProductInput#fields-productType)

A categorization for the product used for filtering and searching products.

product.status:"draft"

string**string**

->[status](/docs/api/admin-graphql/latest/input-objects/ProductInput#fields-status)

The status of the product. Valid values:

Show status properties

  * `active`: The product is ready to sell and is available to customers on the online store, sales channels, and apps. By default, existing products are set to active.
  * `archived`: The product is no longer being sold and isn't available to customers on sales channels and apps.
  * `draft`: The product isn't ready to sell and is unavailable to customers on sales channels and apps. By default, duplicated and unarchived products are set to draft.


Create a new product with multiple product variants

Request body

product

Product resource**Product resource**

Show product properties

product.title:"Burton Custom Freestyle 151"

string**string**

->[title](/docs/api/admin-graphql/latest/input-objects/ProductInput#fields-title)

The name of the product.

product.body_html:"<strong>Good snowboard!</strong>"

string**string**

->[descriptionHtml](/docs/api/admin-graphql/latest/input-objects/ProductInput#fields-descriptionHtml)

A description of the product. Supports HTML formatting.

product.vendor:"Burton"

string**string**

->[vendor](/docs/api/admin-graphql/latest/input-objects/ProductInput#fields-vendor)

The name of the product's vendor.

product.product_type:"Snowboard"

string**string**

->[productType](/docs/api/admin-graphql/latest/input-objects/ProductInput#fields-productType)

A categorization for the product used for filtering and searching products.

product.variants:[{"option1":"First","price":"10.00","sku":"123"},{"option1":"Second","price":"20.00","sku":"123"}]

array**array**

An array of [product variants](/docs/admin-api/rest/reference/products/product-variant), each representing a different version of the product.

The `position` property is read-only. The position of variants is indicated by the order in which they are listed.

Create a new product with multiple product variants and multiple options

Request body

product

Product resource**Product resource**

Show product properties

product.title:"Burton Custom Freestyle 151"

string**string**

->[title](/docs/api/admin-graphql/latest/input-objects/ProductInput#fields-title)

The name of the product.

product.body_html:"<strong>Good snowboard!</strong>"

string**string**

->[descriptionHtml](/docs/api/admin-graphql/latest/input-objects/ProductInput#fields-descriptionHtml)

A description of the product. Supports HTML formatting.

product.vendor:"Burton"

string**string**

->[vendor](/docs/api/admin-graphql/latest/input-objects/ProductInput#fields-vendor)

The name of the product's vendor.

product.product_type:"Snowboard"

string**string**

->[productType](/docs/api/admin-graphql/latest/input-objects/ProductInput#fields-productType)

A categorization for the product used for filtering and searching products.

product.variants:[{"option1":"Blue","option2":"155"},{"option1":"Black","option2":"159"}]

array**array**

An array of [product variants](/docs/admin-api/rest/reference/products/product-variant), each representing a different version of the product.

The `position` property is read-only. The position of variants is indicated by the order in which they are listed.

product.options:[{"name":"Color","values":["Blue","Black"]},{"name":"Size","values":["155","159"]}]

array**array**

The custom product properties. For example, **Size** , **Color** , and **Material**. Each product can have up to 3 options and each option value can be up to 255 characters. Product variants are made of up combinations of option values.

Options cannot be created without values. To create new options, a variant with an associated option value also needs to be created.

Create a new product with the default product variant

Request body

product

Product resource**Product resource**

Show product properties

product.title:"Burton Custom Freestyle 151"

string**string**

->[title](/docs/api/admin-graphql/latest/input-objects/ProductInput#fields-title)

The name of the product.

product.body_html:"<strong>Good snowboard!</strong>"

string**string**

->[descriptionHtml](/docs/api/admin-graphql/latest/input-objects/ProductInput#fields-descriptionHtml)

A description of the product. Supports HTML formatting.

product.vendor:"Burton"

string**string**

->[vendor](/docs/api/admin-graphql/latest/input-objects/ProductInput#fields-vendor)

The name of the product's vendor.

product.product_type:"Snowboard"

string**string**

->[productType](/docs/api/admin-graphql/latest/input-objects/ProductInput#fields-productType)

A categorization for the product used for filtering and searching products.

product.tags:["Barnes & Noble","Big Air","John's Fav"]

string**string**

->[tags](/docs/api/admin-graphql/latest/input-objects/ProductInput#fields-tags)

A string of comma-separated tags that are used for filtering and search. A product can have up to 250 tags. Each tag can have up to 255 characters.

Create a new product with the default variant and a product image that will be downloaded by Shopify

Request body

product

Product resource**Product resource**

Show product properties

product.title:"Burton Custom Freestyle 151"

string**string**

->[title](/docs/api/admin-graphql/latest/input-objects/ProductInput#fields-title)

The name of the product.

product.body_html:"<strong>Good snowboard!</strong>"

string**string**

->[descriptionHtml](/docs/api/admin-graphql/latest/input-objects/ProductInput#fields-descriptionHtml)

A description of the product. Supports HTML formatting.

product.vendor:"Burton"

string**string**

->[vendor](/docs/api/admin-graphql/latest/input-objects/ProductInput#fields-vendor)

The name of the product's vendor.

product.product_type:"Snowboard"

string**string**

->[productType](/docs/api/admin-graphql/latest/input-objects/ProductInput#fields-productType)

A categorization for the product used for filtering and searching products.

product.images:[{"src":"http://example.com/rails_logo.gif"}]

array**array**

A list of [product image](/docs/admin-api/rest/reference/products/product-image) objects, each one representing an image associated with the product.

Create a new product with the default variant and base64 encoded image

Request body

product

Product resource**Product resource**

Show product properties

product.title:"Burton Custom Freestyle 151"

string**string**

->[title](/docs/api/admin-graphql/latest/input-objects/ProductInput#fields-title)

The name of the product.

product.body_html:"<strong>Good snowboard!</strong>"

string**string**

->[descriptionHtml](/docs/api/admin-graphql/latest/input-objects/ProductInput#fields-descriptionHtml)

A description of the product. Supports HTML formatting.

product.vendor:"Burton"

string**string**

->[vendor](/docs/api/admin-graphql/latest/input-objects/ProductInput#fields-vendor)

The name of the product's vendor.

product.product_type:"Snowboard"

string**string**

->[productType](/docs/api/admin-graphql/latest/input-objects/ProductInput#fields-productType)

A categorization for the product used for filtering and searching products.

product.images:[{"attachment":"R0lGODlhAQABAIAAAAAAAAAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==\n"}]

array**array**

A list of [product image](/docs/admin-api/rest/reference/products/product-image) objects, each one representing an image associated with the product.

Create a new unpublished product

Request body

product

Product resource**Product resource**

Show product properties

product.title:"Burton Custom Freestyle 151"

string**string**

->[title](/docs/api/admin-graphql/latest/input-objects/ProductInput#fields-title)

The name of the product.

product.body_html:"<strong>Good snowboard!</strong>"

string**string**

->[descriptionHtml](/docs/api/admin-graphql/latest/input-objects/ProductInput#fields-descriptionHtml)

A description of the product. Supports HTML formatting.

product.vendor:"Burton"

string**string**

->[vendor](/docs/api/admin-graphql/latest/input-objects/ProductInput#fields-vendor)

The name of the product's vendor.

product.product_type:"Snowboard"

string**string**

->[productType](/docs/api/admin-graphql/latest/input-objects/ProductInput#fields-productType)

A categorization for the product used for filtering and searching products.

Create a product with a metafield

Request body

product

Product resource**Product resource**

Show product properties

product.title:"Burton Custom Freestyle 151"

string**string**

->[title](/docs/api/admin-graphql/latest/input-objects/ProductInput#fields-title)

The name of the product.

product.body_html:"<strong>Good snowboard!</strong>"

string**string**

->[descriptionHtml](/docs/api/admin-graphql/latest/input-objects/ProductInput#fields-descriptionHtml)

A description of the product. Supports HTML formatting.

product.vendor:"Burton"

string**string**

->[vendor](/docs/api/admin-graphql/latest/input-objects/ProductInput#fields-vendor)

The name of the product's vendor.

product.product_type:"Snowboard"

string**string**

->[productType](/docs/api/admin-graphql/latest/input-objects/ProductInput#fields-productType)

A categorization for the product used for filtering and searching products.

Create a product with an SEO title and description

Request body

product

Product resource**Product resource**

Show product properties

product.title:"Burton Custom Freestyle 151"

string**string**

->[title](/docs/api/admin-graphql/latest/input-objects/ProductInput#fields-title)

The name of the product.

product.body_html:"<strong>Good snowboard!</strong>"

string**string**

->[descriptionHtml](/docs/api/admin-graphql/latest/input-objects/ProductInput#fields-descriptionHtml)

A description of the product. Supports HTML formatting.

product.vendor:"Burton"

string**string**

->[vendor](/docs/api/admin-graphql/latest/input-objects/ProductInput#fields-vendor)

The name of the product's vendor.

product.product_type:"Snowboard"

string**string**

->[productType](/docs/api/admin-graphql/latest/input-objects/ProductInput#fields-productType)

A categorization for the product used for filtering and searching products.

Creating a product without a title will return an error

Request body

product

Product resource**Product resource**

Show product properties

product.body_html:"A mystery!"

string**string**

->[descriptionHtml](/docs/api/admin-graphql/latest/input-objects/ProductInput#fields-descriptionHtml)

A description of the product. Supports HTML formatting.

Was this section helpful?

YesNo

post

## /admin/api/2026-01/products.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{"product":{"title":"Burton Custom Freestyle 151","body_html":"<strong>Good snowboard!</strong>","vendor":"Burton","product_type":"Snowboard","status":"draft"}}' \

-X POST "https://your-development-store.myshopify.com/admin/api/2026-01/products.json" \

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

61

62

63

64

65

66

67

68

69

70

71

HTTP/1.1 201 Created

{

"product": {

"id": 1072481062,

"title": "Burton Custom Freestyle 151",

"body_html": "<strong>Good snowboard!</strong>",

"vendor": "Burton",

"product_type": "Snowboard",

"created_at": "2026-01-09T19:39:49-05:00",

"handle": "burton-custom-freestyle-151",

"updated_at": "2026-01-09T19:39:49-05:00",

"published_at": null,

"template_suffix": null,

"published_scope": "web",

"tags": "",

"status": "draft",

"admin_graphql_api_id": "gid://shopify/Product/1072481062",

"variants": [

{

"id": 1070325053,

"product_id": 1072481062,

"title": "Default Title",

"price": "0.00",

"position": 1,

"inventory_policy": "deny",

"compare_at_price": null,

"option1": "Default Title",

"option2": null,

"option3": null,

"created_at": "2026-01-09T19:39:49-05:00",

"updated_at": "2026-01-09T19:39:49-05:00",

"taxable": true,

"barcode": null,

"fulfillment_service": "manual",

"grams": 0,

"inventory_management": null,

"requires_shipping": true,

"sku": null,

"weight": 0,

"weight_unit": "lb",

"inventory_item_id": 1070325053,

"inventory_quantity": 0,

"old_inventory_quantity": 0,

"presentment_prices": [

{

"price": {

"amount": "0.00",

"currency_code": "USD"

},

"compare_at_price": null

}

],

"admin_graphql_api_id": "gid://shopify/ProductVariant/1070325053",

"image_id": null

}

],

"options": [

{

"id": 1064576516,

"product_id": 1072481062,

"name": "Title",

"position": 1,

"values": [

"Default Title"

]

}

],

"images": [],

"image": null

}

}

### examples

  * #### Create a new draft product

#####

        curl -d '{"product":{"title":"Burton Custom Freestyle 151","body_html":"<strong>Good snowboard!</strong>","vendor":"Burton","product_type":"Snowboard","status":"draft"}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/products.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const product = new admin.rest.resources.Product({session: session});

        product.title = "Burton Custom Freestyle 151";
        product.body_html = "<strong>Good snowboard!</strong>";
        product.vendor = "Burton";
        product.product_type = "Snowboard";
        product.status = "draft";
        await product.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        product = ShopifyAPI::Product.new(session: test_session)
        product.title = "Burton Custom Freestyle 151"
        product.body_html = "<strong>Good snowboard!</strong>"
        product.vendor = "Burton"
        product.product_type = "Snowboard"
        product.status = "draft"
        product.save!

#####

        // Session is built by the OAuth process

        const product = new shopify.rest.Product({session: session});
        product.title = "Burton Custom Freestyle 151";
        product.body_html = "<strong>Good snowboard!</strong>";
        product.vendor = "Burton";
        product.product_type = "Snowboard";
        product.status = "draft";
        await product.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"product":{"id":1072481062,"title":"Burton Custom Freestyle 151","body_html":"<strong>Good snowboard!</strong>","vendor":"Burton","product_type":"Snowboard","created_at":"2026-01-09T19:39:49-05:00","handle":"burton-custom-freestyle-151","updated_at":"2026-01-09T19:39:49-05:00","published_at":null,"template_suffix":null,"published_scope":"web","tags":"","status":"draft","admin_graphql_api_id":"gid://shopify/Product/1072481062","variants":[{"id":1070325053,"product_id":1072481062,"title":"Default Title","price":"0.00","position":1,"inventory_policy":"deny","compare_at_price":null,"option1":"Default Title","option2":null,"option3":null,"created_at":"2026-01-09T19:39:49-05:00","updated_at":"2026-01-09T19:39:49-05:00","taxable":true,"barcode":null,"fulfillment_service":"manual","grams":0,"inventory_management":null,"requires_shipping":true,"sku":null,"weight":0.0,"weight_unit":"lb","inventory_item_id":1070325053,"inventory_quantity":0,"old_inventory_quantity":0,"presentment_prices":[{"price":{"amount":"0.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/1070325053","image_id":null}],"options":[{"id":1064576516,"product_id":1072481062,"name":"Title","position":1,"values":["Default Title"]}],"images":[],"image":null}}

  * #### Create a new product with multiple product variants

#####

        curl -d '{"product":{"title":"Burton Custom Freestyle 151","body_html":"<strong>Good snowboard!</strong>","vendor":"Burton","product_type":"Snowboard","variants":[{"option1":"First","price":"10.00","sku":"123"},{"option1":"Second","price":"20.00","sku":"123"}]}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/products.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const product = new admin.rest.resources.Product({session: session});

        product.title = "Burton Custom Freestyle 151";
        product.body_html = "<strong>Good snowboard!</strong>";
        product.vendor = "Burton";
        product.product_type = "Snowboard";
        product.variants = [
          {
            "option1": "First",
            "price": "10.00",
            "sku": "123"
          },
          {
            "option1": "Second",
            "price": "20.00",
            "sku": "123"
          }
        ];
        await product.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        product = ShopifyAPI::Product.new(session: test_session)
        product.title = "Burton Custom Freestyle 151"
        product.body_html = "<strong>Good snowboard!</strong>"
        product.vendor = "Burton"
        product.product_type = "Snowboard"
        product.variants = [
          {
            "option1" => "First",
            "price" => "10.00",
            "sku" => "123"
          },
          {
            "option1" => "Second",
            "price" => "20.00",
            "sku" => "123"
          }
        ]
        product.save!

#####

        // Session is built by the OAuth process

        const product = new shopify.rest.Product({session: session});
        product.title = "Burton Custom Freestyle 151";
        product.body_html = "<strong>Good snowboard!</strong>";
        product.vendor = "Burton";
        product.product_type = "Snowboard";
        product.variants = [
          {
            "option1": "First",
            "price": "10.00",
            "sku": "123"
          },
          {
            "option1": "Second",
            "price": "20.00",
            "sku": "123"
          }
        ];
        await product.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"product":{"id":1072481068,"title":"Burton Custom Freestyle 151","body_html":"<strong>Good snowboard!</strong>","vendor":"Burton","product_type":"Snowboard","created_at":"2026-01-09T19:40:41-05:00","handle":"burton-custom-freestyle-151","updated_at":"2026-01-09T19:40:41-05:00","published_at":"2026-01-09T19:40:41-05:00","template_suffix":null,"published_scope":"global","tags":"","status":"active","admin_graphql_api_id":"gid://shopify/Product/1072481068","variants":[{"id":1070325062,"product_id":1072481068,"title":"First","price":"10.00","position":1,"inventory_policy":"deny","compare_at_price":null,"option1":"First","option2":null,"option3":null,"created_at":"2026-01-09T19:40:41-05:00","updated_at":"2026-01-09T19:40:41-05:00","taxable":true,"barcode":null,"fulfillment_service":"manual","grams":0,"inventory_management":null,"requires_shipping":true,"sku":"123","weight":0.0,"weight_unit":"lb","inventory_item_id":1070325062,"inventory_quantity":0,"old_inventory_quantity":0,"presentment_prices":[{"price":{"amount":"10.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/1070325062","image_id":null},{"id":1070325063,"product_id":1072481068,"title":"Second","price":"20.00","position":2,"inventory_policy":"deny","compare_at_price":null,"option1":"Second","option2":null,"option3":null,"created_at":"2026-01-09T19:40:41-05:00","updated_at":"2026-01-09T19:40:41-05:00","taxable":true,"barcode":null,"fulfillment_service":"manual","grams":0,"inventory_management":null,"requires_shipping":true,"sku":"123","weight":0.0,"weight_unit":"lb","inventory_item_id":1070325063,"inventory_quantity":0,"old_inventory_quantity":0,"presentment_prices":[{"price":{"amount":"20.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/1070325063","image_id":null}],"options":[{"id":1064576524,"product_id":1072481068,"name":"Title","position":1,"values":["First","Second"]}],"images":[],"image":null}}

  * #### Create a new product with multiple product variants and multiple options

#####

        curl -d '{"product":{"title":"Burton Custom Freestyle 151","body_html":"<strong>Good snowboard!</strong>","vendor":"Burton","product_type":"Snowboard","variants":[{"option1":"Blue","option2":"155"},{"option1":"Black","option2":"159"}],"options":[{"name":"Color","values":["Blue","Black"]},{"name":"Size","values":["155","159"]}]}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/products.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const product = new admin.rest.resources.Product({session: session});

        product.title = "Burton Custom Freestyle 151";
        product.body_html = "<strong>Good snowboard!</strong>";
        product.vendor = "Burton";
        product.product_type = "Snowboard";
        product.variants = [
          {
            "option1": "Blue",
            "option2": "155"
          },
          {
            "option1": "Black",
            "option2": "159"
          }
        ];
        product.options = [
          {
            "name": "Color",
            "values": [
              "Blue",
              "Black"
            ]
          },
          {
            "name": "Size",
            "values": [
              "155",
              "159"
            ]
          }
        ];
        await product.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        product = ShopifyAPI::Product.new(session: test_session)
        product.title = "Burton Custom Freestyle 151"
        product.body_html = "<strong>Good snowboard!</strong>"
        product.vendor = "Burton"
        product.product_type = "Snowboard"
        product.variants = [
          {
            "option1" => "Blue",
            "option2" => "155"
          },
          {
            "option1" => "Black",
            "option2" => "159"
          }
        ]
        product.options = [
          {
            "name" => "Color",
            "values" => [
              "Blue",
              "Black"
            ]
          },
          {
            "name" => "Size",
            "values" => [
              "155",
              "159"
            ]
          }
        ]
        product.save!

#####

        // Session is built by the OAuth process

        const product = new shopify.rest.Product({session: session});
        product.title = "Burton Custom Freestyle 151";
        product.body_html = "<strong>Good snowboard!</strong>";
        product.vendor = "Burton";
        product.product_type = "Snowboard";
        product.variants = [
          {
            "option1": "Blue",
            "option2": "155"
          },
          {
            "option1": "Black",
            "option2": "159"
          }
        ];
        product.options = [
          {
            "name": "Color",
            "values": [
              "Blue",
              "Black"
            ]
          },
          {
            "name": "Size",
            "values": [
              "155",
              "159"
            ]
          }
        ];
        await product.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"product":{"id":1072481063,"title":"Burton Custom Freestyle 151","body_html":"<strong>Good snowboard!</strong>","vendor":"Burton","product_type":"Snowboard","created_at":"2026-01-09T19:39:50-05:00","handle":"burton-custom-freestyle-151","updated_at":"2026-01-09T19:39:51-05:00","published_at":"2026-01-09T19:39:50-05:00","template_suffix":null,"published_scope":"global","tags":"","status":"active","admin_graphql_api_id":"gid://shopify/Product/1072481063","variants":[{"id":1070325054,"product_id":1072481063,"title":"Blue / 155","price":"0.00","position":1,"inventory_policy":"deny","compare_at_price":null,"option1":"Blue","option2":"155","option3":null,"created_at":"2026-01-09T19:39:51-05:00","updated_at":"2026-01-09T19:39:51-05:00","taxable":true,"barcode":null,"fulfillment_service":"manual","grams":0,"inventory_management":null,"requires_shipping":true,"sku":null,"weight":0.0,"weight_unit":"lb","inventory_item_id":1070325054,"inventory_quantity":0,"old_inventory_quantity":0,"presentment_prices":[{"price":{"amount":"0.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/1070325054","image_id":null},{"id":1070325055,"product_id":1072481063,"title":"Black / 159","price":"0.00","position":2,"inventory_policy":"deny","compare_at_price":null,"option1":"Black","option2":"159","option3":null,"created_at":"2026-01-09T19:39:51-05:00","updated_at":"2026-01-09T19:39:51-05:00","taxable":true,"barcode":null,"fulfillment_service":"manual","grams":0,"inventory_management":null,"requires_shipping":true,"sku":null,"weight":0.0,"weight_unit":"lb","inventory_item_id":1070325055,"inventory_quantity":0,"old_inventory_quantity":0,"presentment_prices":[{"price":{"amount":"0.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/1070325055","image_id":null}],"options":[{"id":1064576517,"product_id":1072481063,"name":"Color","position":1,"values":["Blue","Black"]},{"id":1064576518,"product_id":1072481063,"name":"Size","position":2,"values":["155","159"]}],"images":[],"image":null}}

  * #### Create a new product with the default product variant

#####

        curl -d '{"product":{"title":"Burton Custom Freestyle 151","body_html":"<strong>Good snowboard!</strong>","vendor":"Burton","product_type":"Snowboard","tags":["Barnes & Noble","Big Air","John's Fav"]}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/products.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const product = new admin.rest.resources.Product({session: session});

        product.title = "Burton Custom Freestyle 151";
        product.body_html = "<strong>Good snowboard!</strong>";
        product.vendor = "Burton";
        product.product_type = "Snowboard";
        product.tags = [
          "Barnes & Noble",
          "Big Air",
          "John's Fav"
        ];
        await product.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        product = ShopifyAPI::Product.new(session: test_session)
        product.title = "Burton Custom Freestyle 151"
        product.body_html = "<strong>Good snowboard!</strong>"
        product.vendor = "Burton"
        product.product_type = "Snowboard"
        product.tags = [
          "Barnes & Noble",
          "Big Air",
          "John's Fav"
        ]
        product.save!

#####

        // Session is built by the OAuth process

        const product = new shopify.rest.Product({session: session});
        product.title = "Burton Custom Freestyle 151";
        product.body_html = "<strong>Good snowboard!</strong>";
        product.vendor = "Burton";
        product.product_type = "Snowboard";
        product.tags = [
          "Barnes & Noble",
          "Big Air",
          "John's Fav"
        ];
        await product.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"product":{"id":1072481058,"title":"Burton Custom Freestyle 151","body_html":"<strong>Good snowboard!</strong>","vendor":"Burton","product_type":"Snowboard","created_at":"2026-01-09T19:39:22-05:00","handle":"burton-custom-freestyle-151","updated_at":"2026-01-09T19:39:23-05:00","published_at":"2026-01-09T19:39:22-05:00","template_suffix":null,"published_scope":"global","tags":"Barnes & Noble, Big Air, John's Fav","status":"active","admin_graphql_api_id":"gid://shopify/Product/1072481058","variants":[{"id":1070325049,"product_id":1072481058,"title":"Default Title","price":"0.00","position":1,"inventory_policy":"deny","compare_at_price":null,"option1":"Default Title","option2":null,"option3":null,"created_at":"2026-01-09T19:39:23-05:00","updated_at":"2026-01-09T19:39:23-05:00","taxable":true,"barcode":null,"fulfillment_service":"manual","grams":0,"inventory_management":null,"requires_shipping":true,"sku":null,"weight":0.0,"weight_unit":"lb","inventory_item_id":1070325049,"inventory_quantity":0,"old_inventory_quantity":0,"presentment_prices":[{"price":{"amount":"0.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/1070325049","image_id":null}],"options":[{"id":1064576510,"product_id":1072481058,"name":"Title","position":1,"values":["Default Title"]}],"images":[],"image":null}}

  * #### Create a new product with the default variant and a product image that will be downloaded by Shopify

#####

        curl -d '{"product":{"title":"Burton Custom Freestyle 151","body_html":"<strong>Good snowboard!</strong>","vendor":"Burton","product_type":"Snowboard","images":[{"src":"http://example.com/rails_logo.gif"}]}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/products.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const product = new admin.rest.resources.Product({session: session});

        product.title = "Burton Custom Freestyle 151";
        product.body_html = "<strong>Good snowboard!</strong>";
        product.vendor = "Burton";
        product.product_type = "Snowboard";
        product.images = [
          {
            "src": "http://example.com/rails_logo.gif"
          }
        ];
        await product.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        product = ShopifyAPI::Product.new(session: test_session)
        product.title = "Burton Custom Freestyle 151"
        product.body_html = "<strong>Good snowboard!</strong>"
        product.vendor = "Burton"
        product.product_type = "Snowboard"
        product.images = [
          {
            "src" => "http://example.com/rails_logo.gif"
          }
        ]
        product.save!

#####

        // Session is built by the OAuth process

        const product = new shopify.rest.Product({session: session});
        product.title = "Burton Custom Freestyle 151";
        product.body_html = "<strong>Good snowboard!</strong>";
        product.vendor = "Burton";
        product.product_type = "Snowboard";
        product.images = [
          {
            "src": "http://example.com/rails_logo.gif"
          }
        ];
        await product.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"product":{"id":1072481064,"title":"Burton Custom Freestyle 151","body_html":"<strong>Good snowboard!</strong>","vendor":"Burton","product_type":"Snowboard","created_at":"2026-01-09T19:40:05-05:00","handle":"burton-custom-freestyle-151","updated_at":"2026-01-09T19:40:05-05:00","published_at":"2026-01-09T19:40:05-05:00","template_suffix":null,"published_scope":"global","tags":"","status":"active","admin_graphql_api_id":"gid://shopify/Product/1072481064","variants":[{"id":1070325057,"product_id":1072481064,"title":"Default Title","price":"0.00","position":1,"inventory_policy":"deny","compare_at_price":null,"option1":"Default Title","option2":null,"option3":null,"created_at":"2026-01-09T19:40:05-05:00","updated_at":"2026-01-09T19:40:05-05:00","taxable":true,"barcode":null,"fulfillment_service":"manual","grams":0,"inventory_management":null,"requires_shipping":true,"sku":null,"weight":0.0,"weight_unit":"lb","inventory_item_id":1070325057,"inventory_quantity":0,"old_inventory_quantity":0,"presentment_prices":[{"price":{"amount":"0.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/1070325057","image_id":null}],"options":[{"id":1064576519,"product_id":1072481064,"name":"Title","position":1,"values":["Default Title"]}],"images":[{"id":1001473921,"alt":null,"position":1,"product_id":1072481064,"created_at":"2026-01-09T19:40:05-05:00","updated_at":"2026-01-09T19:40:05-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/1072273214","width":110,"height":140,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/files/rails_logo20260109-27647-zd8xsg.gif?v=1768005605","variant_ids":[]}],"image":{"id":1001473921,"alt":null,"position":1,"product_id":1072481064,"created_at":"2026-01-09T19:40:05-05:00","updated_at":"2026-01-09T19:40:05-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/1072273214","width":110,"height":140,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/files/rails_logo20260109-27647-zd8xsg.gif?v=1768005605","variant_ids":[]}}}

  * #### Create a new product with the default variant and base64 encoded image

#####

        curl -d '{"product":{"title":"Burton Custom Freestyle 151","body_html":"<strong>Good snowboard!</strong>","vendor":"Burton","product_type":"Snowboard","images":[{"attachment":"R0lGODlhAQABAIAAAAAAAAAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==\n"}]}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/products.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const product = new admin.rest.resources.Product({session: session});

        product.title = "Burton Custom Freestyle 151";
        product.body_html = "<strong>Good snowboard!</strong>";
        product.vendor = "Burton";
        product.product_type = "Snowboard";
        product.images = [
          {
            "attachment": "R0lGODlhAQABAIAAAAAAAAAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==\n"
          }
        ];
        await product.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        product = ShopifyAPI::Product.new(session: test_session)
        product.title = "Burton Custom Freestyle 151"
        product.body_html = "<strong>Good snowboard!</strong>"
        product.vendor = "Burton"
        product.product_type = "Snowboard"
        product.images = [
          {
            "attachment" => "R0lGODlhAQABAIAAAAAAAAAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==\n"
          }
        ]
        product.save!

#####

        // Session is built by the OAuth process

        const product = new shopify.rest.Product({session: session});
        product.title = "Burton Custom Freestyle 151";
        product.body_html = "<strong>Good snowboard!</strong>";
        product.vendor = "Burton";
        product.product_type = "Snowboard";
        product.images = [
          {
            "attachment": "R0lGODlhAQABAIAAAAAAAAAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==\n"
          }
        ];
        await product.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"product":{"id":1072481061,"title":"Burton Custom Freestyle 151","body_html":"<strong>Good snowboard!</strong>","vendor":"Burton","product_type":"Snowboard","created_at":"2026-01-09T19:39:36-05:00","handle":"burton-custom-freestyle-151","updated_at":"2026-01-09T19:39:37-05:00","published_at":"2026-01-09T19:39:36-05:00","template_suffix":null,"published_scope":"global","tags":"","status":"active","admin_graphql_api_id":"gid://shopify/Product/1072481061","variants":[{"id":1070325052,"product_id":1072481061,"title":"Default Title","price":"0.00","position":1,"inventory_policy":"deny","compare_at_price":null,"option1":"Default Title","option2":null,"option3":null,"created_at":"2026-01-09T19:39:37-05:00","updated_at":"2026-01-09T19:39:37-05:00","taxable":true,"barcode":null,"fulfillment_service":"manual","grams":0,"inventory_management":null,"requires_shipping":true,"sku":null,"weight":0.0,"weight_unit":"lb","inventory_item_id":1070325052,"inventory_quantity":0,"old_inventory_quantity":0,"presentment_prices":[{"price":{"amount":"0.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/1070325052","image_id":null}],"options":[{"id":1064576515,"product_id":1072481061,"name":"Title","position":1,"values":["Default Title"]}],"images":[{"id":1001473920,"alt":null,"position":1,"product_id":1072481061,"created_at":"2026-01-09T19:39:37-05:00","updated_at":"2026-01-09T19:39:37-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/1072273213","width":1,"height":1,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/files/df3e567d6f16d040326c7a0ea29a4f41.gif?v=1768005577","variant_ids":[]}],"image":{"id":1001473920,"alt":null,"position":1,"product_id":1072481061,"created_at":"2026-01-09T19:39:37-05:00","updated_at":"2026-01-09T19:39:37-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/1072273213","width":1,"height":1,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/files/df3e567d6f16d040326c7a0ea29a4f41.gif?v=1768005577","variant_ids":[]}}}

  * #### Create a new unpublished product

#####

        curl -d '{"product":{"title":"Burton Custom Freestyle 151","body_html":"<strong>Good snowboard!</strong>","vendor":"Burton","product_type":"Snowboard","published":false}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/products.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const product = new admin.rest.resources.Product({session: session});

        product.title = "Burton Custom Freestyle 151";
        product.body_html = "<strong>Good snowboard!</strong>";
        product.vendor = "Burton";
        product.product_type = "Snowboard";
        product.published = false;
        await product.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        product = ShopifyAPI::Product.new(session: test_session)
        product.title = "Burton Custom Freestyle 151"
        product.body_html = "<strong>Good snowboard!</strong>"
        product.vendor = "Burton"
        product.product_type = "Snowboard"
        product.published = false
        product.save!

#####

        // Session is built by the OAuth process

        const product = new shopify.rest.Product({session: session});
        product.title = "Burton Custom Freestyle 151";
        product.body_html = "<strong>Good snowboard!</strong>";
        product.vendor = "Burton";
        product.product_type = "Snowboard";
        product.published = false;
        await product.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"product":{"id":1072481066,"title":"Burton Custom Freestyle 151","body_html":"<strong>Good snowboard!</strong>","vendor":"Burton","product_type":"Snowboard","created_at":"2026-01-09T19:40:25-05:00","handle":"burton-custom-freestyle-151","updated_at":"2026-01-09T19:40:25-05:00","published_at":null,"template_suffix":null,"published_scope":"global","tags":"","status":"active","admin_graphql_api_id":"gid://shopify/Product/1072481066","variants":[{"id":1070325059,"product_id":1072481066,"title":"Default Title","price":"0.00","position":1,"inventory_policy":"deny","compare_at_price":null,"option1":"Default Title","option2":null,"option3":null,"created_at":"2026-01-09T19:40:25-05:00","updated_at":"2026-01-09T19:40:25-05:00","taxable":true,"barcode":null,"fulfillment_service":"manual","grams":0,"inventory_management":null,"requires_shipping":true,"sku":null,"weight":0.0,"weight_unit":"lb","inventory_item_id":1070325059,"inventory_quantity":0,"old_inventory_quantity":0,"presentment_prices":[{"price":{"amount":"0.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/1070325059","image_id":null}],"options":[{"id":1064576521,"product_id":1072481066,"name":"Title","position":1,"values":["Default Title"]}],"images":[],"image":null}}

  * #### Create a product with a metafield

#####

        curl -d '{"product":{"title":"Burton Custom Freestyle 151","body_html":"<strong>Good snowboard!</strong>","vendor":"Burton","product_type":"Snowboard","metafields":[{"key":"new","value":"newvalue","type":"single_line_text_field","namespace":"global"}]}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/products.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const product = new admin.rest.resources.Product({session: session});

        product.title = "Burton Custom Freestyle 151";
        product.body_html = "<strong>Good snowboard!</strong>";
        product.vendor = "Burton";
        product.product_type = "Snowboard";
        product.metafields = [
          {
            "key": "new",
            "value": "newvalue",
            "type": "single_line_text_field",
            "namespace": "global"
          }
        ];
        await product.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        product = ShopifyAPI::Product.new(session: test_session)
        product.title = "Burton Custom Freestyle 151"
        product.body_html = "<strong>Good snowboard!</strong>"
        product.vendor = "Burton"
        product.product_type = "Snowboard"
        product.metafields = [
          {
            "key" => "new",
            "value" => "newvalue",
            "type" => "single_line_text_field",
            "namespace" => "global"
          }
        ]
        product.save!

#####

        // Session is built by the OAuth process

        const product = new shopify.rest.Product({session: session});
        product.title = "Burton Custom Freestyle 151";
        product.body_html = "<strong>Good snowboard!</strong>";
        product.vendor = "Burton";
        product.product_type = "Snowboard";
        product.metafields = [
          {
            "key": "new",
            "value": "newvalue",
            "type": "single_line_text_field",
            "namespace": "global"
          }
        ];
        await product.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"product":{"id":1072481056,"title":"Burton Custom Freestyle 151","body_html":"<strong>Good snowboard!</strong>","vendor":"Burton","product_type":"Snowboard","created_at":"2026-01-09T19:39:02-05:00","handle":"burton-custom-freestyle-151","updated_at":"2026-01-09T19:39:02-05:00","published_at":"2026-01-09T19:39:02-05:00","template_suffix":null,"published_scope":"global","tags":"","status":"active","admin_graphql_api_id":"gid://shopify/Product/1072481056","variants":[{"id":1070325047,"product_id":1072481056,"title":"Default Title","price":"0.00","position":1,"inventory_policy":"deny","compare_at_price":null,"option1":"Default Title","option2":null,"option3":null,"created_at":"2026-01-09T19:39:02-05:00","updated_at":"2026-01-09T19:39:02-05:00","taxable":true,"barcode":null,"fulfillment_service":"manual","grams":0,"inventory_management":null,"requires_shipping":true,"sku":null,"weight":0.0,"weight_unit":"lb","inventory_item_id":1070325047,"inventory_quantity":0,"old_inventory_quantity":0,"presentment_prices":[{"price":{"amount":"0.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/1070325047","image_id":null}],"options":[{"id":1064576505,"product_id":1072481056,"name":"Title","position":1,"values":["Default Title"]}],"images":[],"image":null}}

  * #### Create a product with an SEO title and description

#####

        curl -d '{"product":{"title":"Burton Custom Freestyle 151","body_html":"<strong>Good snowboard!</strong>","vendor":"Burton","product_type":"Snowboard","metafields_global_title_tag":"Product SEO Title","metafields_global_description_tag":"Product SEO Description"}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/products.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const product = new admin.rest.resources.Product({session: session});

        product.title = "Burton Custom Freestyle 151";
        product.body_html = "<strong>Good snowboard!</strong>";
        product.vendor = "Burton";
        product.product_type = "Snowboard";
        product.metafields_global_title_tag = "Product SEO Title";
        product.metafields_global_description_tag = "Product SEO Description";
        await product.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        product = ShopifyAPI::Product.new(session: test_session)
        product.title = "Burton Custom Freestyle 151"
        product.body_html = "<strong>Good snowboard!</strong>"
        product.vendor = "Burton"
        product.product_type = "Snowboard"
        product.metafields_global_title_tag = "Product SEO Title"
        product.metafields_global_description_tag = "Product SEO Description"
        product.save!

#####

        // Session is built by the OAuth process

        const product = new shopify.rest.Product({session: session});
        product.title = "Burton Custom Freestyle 151";
        product.body_html = "<strong>Good snowboard!</strong>";
        product.vendor = "Burton";
        product.product_type = "Snowboard";
        product.metafields_global_title_tag = "Product SEO Title";
        product.metafields_global_description_tag = "Product SEO Description";
        await product.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"product":{"id":1072481065,"title":"Burton Custom Freestyle 151","body_html":"<strong>Good snowboard!</strong>","vendor":"Burton","product_type":"Snowboard","created_at":"2026-01-09T19:40:08-05:00","handle":"burton-custom-freestyle-151","updated_at":"2026-01-09T19:40:08-05:00","published_at":"2026-01-09T19:40:08-05:00","template_suffix":null,"published_scope":"global","tags":"","status":"active","admin_graphql_api_id":"gid://shopify/Product/1072481065","variants":[{"id":1070325058,"product_id":1072481065,"title":"Default Title","price":"0.00","position":1,"inventory_policy":"deny","compare_at_price":null,"option1":"Default Title","option2":null,"option3":null,"created_at":"2026-01-09T19:40:08-05:00","updated_at":"2026-01-09T19:40:08-05:00","taxable":true,"barcode":null,"fulfillment_service":"manual","grams":0,"inventory_management":null,"requires_shipping":true,"sku":null,"weight":0.0,"weight_unit":"lb","inventory_item_id":1070325058,"inventory_quantity":0,"old_inventory_quantity":0,"presentment_prices":[{"price":{"amount":"0.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/1070325058","image_id":null}],"options":[{"id":1064576520,"product_id":1072481065,"name":"Title","position":1,"values":["Default Title"]}],"images":[],"image":null}}

  * #### Creating a product without a title will return an error

#####

        curl -d '{"product":{"body_html":"A mystery!"}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/products.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const product = new admin.rest.resources.Product({session: session});

        product.body_html = "A mystery!";
        await product.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        product = ShopifyAPI::Product.new(session: test_session)
        product.body_html = "A mystery!"
        product.save!

#####

        // Session is built by the OAuth process

        const product = new shopify.rest.Product({session: session});
        product.body_html = "A mystery!";
        await product.save({
          update: true,
        });

#### response

        HTTP/1.1 422 Unprocessable Entity{"errors":{"title":["can't be blank"]}}


* * *

##

[Anchor to GET request, Retrieve a list of products](/docs/api/admin-rest/latest/resources/product#get-products?ids=632910392,921728736)

get

Retrieve a list of products

[products](/docs/api/admin-graphql/latest/queries/products?example=retrieve-a-list-of-products)

Retrieve a list of products.

###

[Anchor to Parameters of Retrieve a list of products](/docs/api/admin-rest/latest/resources/product#get-products?ids=632910392,921728736-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

collection_id

Return products by product collection ID.

* * *

created_at_max

Return products created before a specified date. (format: 2014-04-25T16:15:47-04:00)

* * *

created_at_min

Return products created after a specified date. (format: 2014-04-25T16:15:47-04:00)

* * *

fields

Return fields by a comma-separated list of field names. Fields: admin_graphql_api_id, body_html, created_at, handle, id, image, images, options, product_type, published_at, published_scope, status, tags, template_suffix, title, updated_at, variants, vendor

* * *

handle

Return only products specified by a comma-separated list of product handles.

* * *

ids

Return only products specified by a comma-separated list of product IDs.

* * *

limit

≤ 250**≤ 250**

default 50**default 50**

Return up to this many results per page.

* * *

presentment_currencies

Return presentment prices in only certain currencies, specified by a comma-separated list of [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency codes.

* * *

product_type

Return products by product type.

* * *

published_at_max

Return products published before a specified date. (format: 2014-04-25T16:15:47-04:00)

* * *

published_at_min

Return products published after a specified date. (format: 2014-04-25T16:15:47-04:00)

* * *

Show 7 hidden fields

Was this section helpful?

YesNo

###

[Anchor to get-products?ids=632910392,921728736-examples](/docs/api/admin-rest/latest/resources/product#get-products?ids=632910392,921728736-examples)Examples

Retrieve a list of specific products

Query parameters

ids=632910392,921728736

Return only products specified by a comma-separated list of product IDs.

Retrieve all products

Retrieve all products after the specified ID

Query parameters

since_id=632910392

Return only products after the specified ID.

Retrieve all products that belong to a certain collection

Query parameters

collection_id=841564295

Return products by product collection ID.

Retrieve all products with prices in selected presentment currencies

Query parameters

presentment_currencies=USD

Return presentment prices in only certain currencies, specified by a comma-separated list of [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency codes.

Retrieve all products, showing only some attributes

Query parameters

fields=id,images,title

Return fields by a comma-separated list of field names. Fields: admin_graphql_api_id, body_html, created_at, handle, id, image, images, options, product_type, published_at, published_scope, status, tags, template_suffix, title, updated_at, variants, vendor

Was this section helpful?

YesNo

get

## /admin/api/2026-01/products.json?ids=632910392,921728736

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/products.json?ids=632910392%2C921728736" \

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

"products": [

{

"id": 632910392,

"title": "IPod Nano - 8GB",

"body_html": "<p>It's the small iPod with one very big idea: Video. Now the world's most popular music player, available in 4GB and 8GB models, lets you enjoy TV shows, movies, video podcasts, and more. The larger, brighter display means amazing picture quality. In six eye-catching colors, iPod nano is stunning all around. And with models starting at just $149, little speaks volumes.</p>",

"vendor": "Apple",

"product_type": "Cult Products",

"created_at": "2026-01-09T19:38:20-05:00",

"handle": "ipod-nano",

"updated_at": "2026-01-09T19:38:20-05:00",

"published_at": "2007-12-31T19:00:00-05:00",

"template_suffix": null,

"published_scope": "web",

"tags": "Emotive, Flash Memory, MP3, Music",

"status": "active",

"admin_graphql_api_id": "gid://shopify/Product/632910392",

"variants": [

{

"id": 808950810,

"product_id": 632910392,

"title": "Pink",

"price": "199.00",

"position": 1,

"inventory_policy": "continue",

"compare_at_price": null,

"option1": "Pink",

"option2": null,

"option3": null,

"created_at": "2026-01-09T19:38:20-05:00",

"updated_at": "2026-01-09T19:38:20-05:00",

"taxable": true,

"barcode": "1234_pink",

"fulfillment_service": "manual",

"grams": 567,

### examples

  * #### Retrieve a list of specific products

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/products.json?ids=632910392%2C921728736" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Product.all({
          session: session,
          ids: "632910392,921728736",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Product.all(
          session: test_session,
          ids: "632910392,921728736",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Product.all({
          session: session,
          ids: "632910392,921728736",
        });

#### response

        HTTP/1.1 200 OK{"products":[{"id":632910392,"title":"IPod Nano - 8GB","body_html":"<p>It's the small iPod with one very big idea: Video. Now the world's most popular music player, available in 4GB and 8GB models, lets you enjoy TV shows, movies, video podcasts, and more. The larger, brighter display means amazing picture quality. In six eye-catching colors, iPod nano is stunning all around. And with models starting at just $149, little speaks volumes.</p>","vendor":"Apple","product_type":"Cult Products","created_at":"2026-01-09T19:38:20-05:00","handle":"ipod-nano","updated_at":"2026-01-09T19:38:20-05:00","published_at":"2007-12-31T19:00:00-05:00","template_suffix":null,"published_scope":"web","tags":"Emotive, Flash Memory, MP3, Music","status":"active","admin_graphql_api_id":"gid://shopify/Product/632910392","variants":[{"id":808950810,"product_id":632910392,"title":"Pink","price":"199.00","position":1,"inventory_policy":"continue","compare_at_price":null,"option1":"Pink","option2":null,"option3":null,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","taxable":true,"barcode":"1234_pink","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008PINK","weight":1.25,"weight_unit":"lb","inventory_item_id":808950810,"inventory_quantity":10,"old_inventory_quantity":10,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/808950810","image_id":562641783},{"id":49148385,"product_id":632910392,"title":"Red","price":"199.00","position":2,"inventory_policy":"continue","compare_at_price":null,"option1":"Red","option2":null,"option3":null,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","taxable":true,"barcode":"1234_red","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008RED","weight":1.25,"weight_unit":"lb","inventory_item_id":49148385,"inventory_quantity":20,"old_inventory_quantity":20,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/49148385","image_id":null},{"id":39072856,"product_id":632910392,"title":"Green","price":"199.00","position":3,"inventory_policy":"continue","compare_at_price":null,"option1":"Green","option2":null,"option3":null,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","taxable":true,"barcode":"1234_green","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008GREEN","weight":1.25,"weight_unit":"lb","inventory_item_id":39072856,"inventory_quantity":30,"old_inventory_quantity":30,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/39072856","image_id":null},{"id":457924702,"product_id":632910392,"title":"Black","price":"199.00","position":4,"inventory_policy":"continue","compare_at_price":null,"option1":"Black","option2":null,"option3":null,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","taxable":true,"barcode":"1234_black","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008BLACK","weight":1.25,"weight_unit":"lb","inventory_item_id":457924702,"inventory_quantity":40,"old_inventory_quantity":40,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/457924702","image_id":null}],"options":[{"id":594680422,"product_id":632910392,"name":"Color","position":1,"values":["Pink","Red","Green","Black"]}],"images":[{"id":850703190,"alt":null,"position":1,"product_id":632910392,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/498048120","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano.png?v=1768005500","variant_ids":[]},{"id":562641783,"alt":null,"position":2,"product_id":632910392,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/1071517486","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano-2.png?v=1768005500","variant_ids":[808950810]},{"id":378407906,"alt":null,"position":3,"product_id":632910392,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/220090436","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano.png?v=1768005500","variant_ids":[]}],"image":{"id":850703190,"alt":null,"position":1,"product_id":632910392,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/498048120","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano.png?v=1768005500","variant_ids":[]}},{"id":921728736,"title":"IPod Touch 8GB","body_html":"<p>The iPod Touch has the iPhone's multi-touch interface, with a physical home button off the touch screen. The home screen has a list of buttons for the available applications.</p>","vendor":"Apple","product_type":"Cult Products","created_at":"2026-01-09T19:38:20-05:00","handle":"ipod-touch","updated_at":"2026-01-09T19:38:20-05:00","published_at":"2008-09-25T20:00:00-04:00","template_suffix":null,"published_scope":"web","tags":"","status":"active","admin_graphql_api_id":"gid://shopify/Product/921728736","variants":[{"id":447654529,"product_id":921728736,"title":"Black","price":"199.00","position":1,"inventory_policy":"continue","compare_at_price":null,"option1":"Black","option2":null,"option3":null,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","taxable":true,"barcode":"1234_black","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2009BLACK","weight":1.25,"weight_unit":"lb","inventory_item_id":447654529,"inventory_quantity":13,"old_inventory_quantity":13,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/447654529","image_id":null}],"options":[{"id":891236591,"product_id":921728736,"name":"Title","position":1,"values":["Black"]}],"images":[],"image":null}]}

  * #### Retrieve all products

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/products.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Product.all({
          session: session,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Product.all(
          session: test_session,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Product.all({
          session: session,
        });

#### response

        HTTP/1.1 200 OK{"products":[{"id":632910392,"title":"IPod Nano - 8GB","body_html":"<p>It's the small iPod with one very big idea: Video. Now the world's most popular music player, available in 4GB and 8GB models, lets you enjoy TV shows, movies, video podcasts, and more. The larger, brighter display means amazing picture quality. In six eye-catching colors, iPod nano is stunning all around. And with models starting at just $149, little speaks volumes.</p>","vendor":"Apple","product_type":"Cult Products","created_at":"2026-01-09T19:38:20-05:00","handle":"ipod-nano","updated_at":"2026-01-09T19:38:20-05:00","published_at":"2007-12-31T19:00:00-05:00","template_suffix":null,"published_scope":"web","tags":"Emotive, Flash Memory, MP3, Music","status":"active","admin_graphql_api_id":"gid://shopify/Product/632910392","variants":[{"id":808950810,"product_id":632910392,"title":"Pink","price":"199.00","position":1,"inventory_policy":"continue","compare_at_price":null,"option1":"Pink","option2":null,"option3":null,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","taxable":true,"barcode":"1234_pink","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008PINK","weight":1.25,"weight_unit":"lb","inventory_item_id":808950810,"inventory_quantity":10,"old_inventory_quantity":10,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/808950810","image_id":562641783},{"id":49148385,"product_id":632910392,"title":"Red","price":"199.00","position":2,"inventory_policy":"continue","compare_at_price":null,"option1":"Red","option2":null,"option3":null,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","taxable":true,"barcode":"1234_red","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008RED","weight":1.25,"weight_unit":"lb","inventory_item_id":49148385,"inventory_quantity":20,"old_inventory_quantity":20,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/49148385","image_id":null},{"id":39072856,"product_id":632910392,"title":"Green","price":"199.00","position":3,"inventory_policy":"continue","compare_at_price":null,"option1":"Green","option2":null,"option3":null,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","taxable":true,"barcode":"1234_green","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008GREEN","weight":1.25,"weight_unit":"lb","inventory_item_id":39072856,"inventory_quantity":30,"old_inventory_quantity":30,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/39072856","image_id":null},{"id":457924702,"product_id":632910392,"title":"Black","price":"199.00","position":4,"inventory_policy":"continue","compare_at_price":null,"option1":"Black","option2":null,"option3":null,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","taxable":true,"barcode":"1234_black","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008BLACK","weight":1.25,"weight_unit":"lb","inventory_item_id":457924702,"inventory_quantity":40,"old_inventory_quantity":40,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/457924702","image_id":null}],"options":[{"id":594680422,"product_id":632910392,"name":"Color","position":1,"values":["Pink","Red","Green","Black"]}],"images":[{"id":850703190,"alt":null,"position":1,"product_id":632910392,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/498048120","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano.png?v=1768005500","variant_ids":[]},{"id":562641783,"alt":null,"position":2,"product_id":632910392,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/1071517486","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano-2.png?v=1768005500","variant_ids":[808950810]},{"id":378407906,"alt":null,"position":3,"product_id":632910392,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/220090436","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano.png?v=1768005500","variant_ids":[]}],"image":{"id":850703190,"alt":null,"position":1,"product_id":632910392,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/498048120","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano.png?v=1768005500","variant_ids":[]}},{"id":921728736,"title":"IPod Touch 8GB","body_html":"<p>The iPod Touch has the iPhone's multi-touch interface, with a physical home button off the touch screen. The home screen has a list of buttons for the available applications.</p>","vendor":"Apple","product_type":"Cult Products","created_at":"2026-01-09T19:38:20-05:00","handle":"ipod-touch","updated_at":"2026-01-09T19:38:20-05:00","published_at":"2008-09-25T20:00:00-04:00","template_suffix":null,"published_scope":"web","tags":"","status":"active","admin_graphql_api_id":"gid://shopify/Product/921728736","variants":[{"id":447654529,"product_id":921728736,"title":"Black","price":"199.00","position":1,"inventory_policy":"continue","compare_at_price":null,"option1":"Black","option2":null,"option3":null,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","taxable":true,"barcode":"1234_black","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2009BLACK","weight":1.25,"weight_unit":"lb","inventory_item_id":447654529,"inventory_quantity":13,"old_inventory_quantity":13,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/447654529","image_id":null}],"options":[{"id":891236591,"product_id":921728736,"name":"Title","position":1,"values":["Black"]}],"images":[],"image":null}]}

  * #### Retrieve all products after the specified ID

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/products.json?since_id=632910392" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Product.all({
          session: session,
          since_id: "632910392",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Product.all(
          session: test_session,
          since_id: "632910392",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Product.all({
          session: session,
          since_id: "632910392",
        });

#### response

        HTTP/1.1 200 OK{"products":[{"id":921728736,"title":"IPod Touch 8GB","body_html":"<p>The iPod Touch has the iPhone's multi-touch interface, with a physical home button off the touch screen. The home screen has a list of buttons for the available applications.</p>","vendor":"Apple","product_type":"Cult Products","created_at":"2026-01-09T19:38:20-05:00","handle":"ipod-touch","updated_at":"2026-01-09T19:38:20-05:00","published_at":"2008-09-25T20:00:00-04:00","template_suffix":null,"published_scope":"web","tags":"","status":"active","admin_graphql_api_id":"gid://shopify/Product/921728736","variants":[{"id":447654529,"product_id":921728736,"title":"Black","price":"199.00","position":1,"inventory_policy":"continue","compare_at_price":null,"option1":"Black","option2":null,"option3":null,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","taxable":true,"barcode":"1234_black","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2009BLACK","weight":1.25,"weight_unit":"lb","inventory_item_id":447654529,"inventory_quantity":13,"old_inventory_quantity":13,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/447654529","image_id":null}],"options":[{"id":891236591,"product_id":921728736,"name":"Title","position":1,"values":["Black"]}],"images":[],"image":null}]}

  * #### Retrieve all products that belong to a certain collection

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/products.json?collection_id=841564295" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Product.all({
          session: session,
          collection_id: "841564295",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Product.all(
          session: test_session,
          collection_id: "841564295",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Product.all({
          session: session,
          collection_id: "841564295",
        });

#### response

        HTTP/1.1 200 OK{"products":[{"id":632910392,"title":"IPod Nano - 8GB","body_html":"<p>It's the small iPod with one very big idea: Video. Now the world's most popular music player, available in 4GB and 8GB models, lets you enjoy TV shows, movies, video podcasts, and more. The larger, brighter display means amazing picture quality. In six eye-catching colors, iPod nano is stunning all around. And with models starting at just $149, little speaks volumes.</p>","vendor":"Apple","product_type":"Cult Products","created_at":"2026-01-09T19:38:20-05:00","handle":"ipod-nano","updated_at":"2026-01-09T19:38:20-05:00","published_at":"2007-12-31T19:00:00-05:00","template_suffix":null,"published_scope":"web","tags":"Emotive, Flash Memory, MP3, Music","status":"active","admin_graphql_api_id":"gid://shopify/Product/632910392","variants":[{"id":808950810,"product_id":632910392,"title":"Pink","price":"199.00","position":1,"inventory_policy":"continue","compare_at_price":null,"option1":"Pink","option2":null,"option3":null,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","taxable":true,"barcode":"1234_pink","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008PINK","weight":1.25,"weight_unit":"lb","inventory_item_id":808950810,"inventory_quantity":10,"old_inventory_quantity":10,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/808950810","image_id":562641783},{"id":49148385,"product_id":632910392,"title":"Red","price":"199.00","position":2,"inventory_policy":"continue","compare_at_price":null,"option1":"Red","option2":null,"option3":null,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","taxable":true,"barcode":"1234_red","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008RED","weight":1.25,"weight_unit":"lb","inventory_item_id":49148385,"inventory_quantity":20,"old_inventory_quantity":20,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/49148385","image_id":null},{"id":39072856,"product_id":632910392,"title":"Green","price":"199.00","position":3,"inventory_policy":"continue","compare_at_price":null,"option1":"Green","option2":null,"option3":null,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","taxable":true,"barcode":"1234_green","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008GREEN","weight":1.25,"weight_unit":"lb","inventory_item_id":39072856,"inventory_quantity":30,"old_inventory_quantity":30,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/39072856","image_id":null},{"id":457924702,"product_id":632910392,"title":"Black","price":"199.00","position":4,"inventory_policy":"continue","compare_at_price":null,"option1":"Black","option2":null,"option3":null,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","taxable":true,"barcode":"1234_black","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008BLACK","weight":1.25,"weight_unit":"lb","inventory_item_id":457924702,"inventory_quantity":40,"old_inventory_quantity":40,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/457924702","image_id":null}],"options":[{"id":594680422,"product_id":632910392,"name":"Color","position":1,"values":["Pink","Red","Green","Black"]}],"images":[{"id":850703190,"alt":null,"position":1,"product_id":632910392,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/498048120","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano.png?v=1768005500","variant_ids":[]},{"id":562641783,"alt":null,"position":2,"product_id":632910392,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/1071517486","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano-2.png?v=1768005500","variant_ids":[808950810]},{"id":378407906,"alt":null,"position":3,"product_id":632910392,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/220090436","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano.png?v=1768005500","variant_ids":[]}],"image":{"id":850703190,"alt":null,"position":1,"product_id":632910392,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/498048120","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano.png?v=1768005500","variant_ids":[]}}]}

  * #### Retrieve all products with prices in selected presentment currencies

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/products.json?presentment_currencies=USD" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Product.all({
          session: session,
          presentment_currencies: "USD",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Product.all(
          session: test_session,
          presentment_currencies: "USD",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Product.all({
          session: session,
          presentment_currencies: "USD",
        });

#### response

        HTTP/1.1 200 OK{"products":[{"id":632910392,"title":"IPod Nano - 8GB","body_html":"<p>It's the small iPod with one very big idea: Video. Now the world's most popular music player, available in 4GB and 8GB models, lets you enjoy TV shows, movies, video podcasts, and more. The larger, brighter display means amazing picture quality. In six eye-catching colors, iPod nano is stunning all around. And with models starting at just $149, little speaks volumes.</p>","vendor":"Apple","product_type":"Cult Products","created_at":"2026-01-09T19:38:20-05:00","handle":"ipod-nano","updated_at":"2026-01-09T19:38:20-05:00","published_at":"2007-12-31T19:00:00-05:00","template_suffix":null,"published_scope":"web","tags":"Emotive, Flash Memory, MP3, Music","status":"active","admin_graphql_api_id":"gid://shopify/Product/632910392","variants":[{"id":808950810,"product_id":632910392,"title":"Pink","price":"199.00","position":1,"inventory_policy":"continue","compare_at_price":null,"option1":"Pink","option2":null,"option3":null,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","taxable":true,"barcode":"1234_pink","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008PINK","weight":1.25,"weight_unit":"lb","inventory_item_id":808950810,"inventory_quantity":10,"old_inventory_quantity":10,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/808950810","image_id":562641783},{"id":49148385,"product_id":632910392,"title":"Red","price":"199.00","position":2,"inventory_policy":"continue","compare_at_price":null,"option1":"Red","option2":null,"option3":null,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","taxable":true,"barcode":"1234_red","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008RED","weight":1.25,"weight_unit":"lb","inventory_item_id":49148385,"inventory_quantity":20,"old_inventory_quantity":20,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/49148385","image_id":null},{"id":39072856,"product_id":632910392,"title":"Green","price":"199.00","position":3,"inventory_policy":"continue","compare_at_price":null,"option1":"Green","option2":null,"option3":null,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","taxable":true,"barcode":"1234_green","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008GREEN","weight":1.25,"weight_unit":"lb","inventory_item_id":39072856,"inventory_quantity":30,"old_inventory_quantity":30,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/39072856","image_id":null},{"id":457924702,"product_id":632910392,"title":"Black","price":"199.00","position":4,"inventory_policy":"continue","compare_at_price":null,"option1":"Black","option2":null,"option3":null,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","taxable":true,"barcode":"1234_black","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008BLACK","weight":1.25,"weight_unit":"lb","inventory_item_id":457924702,"inventory_quantity":40,"old_inventory_quantity":40,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/457924702","image_id":null}],"options":[{"id":594680422,"product_id":632910392,"name":"Color","position":1,"values":["Pink","Red","Green","Black"]}],"images":[{"id":850703190,"alt":null,"position":1,"product_id":632910392,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/498048120","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano.png?v=1768005500","variant_ids":[]},{"id":562641783,"alt":null,"position":2,"product_id":632910392,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/1071517486","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano-2.png?v=1768005500","variant_ids":[808950810]},{"id":378407906,"alt":null,"position":3,"product_id":632910392,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/220090436","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano.png?v=1768005500","variant_ids":[]}],"image":{"id":850703190,"alt":null,"position":1,"product_id":632910392,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/498048120","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano.png?v=1768005500","variant_ids":[]}},{"id":921728736,"title":"IPod Touch 8GB","body_html":"<p>The iPod Touch has the iPhone's multi-touch interface, with a physical home button off the touch screen. The home screen has a list of buttons for the available applications.</p>","vendor":"Apple","product_type":"Cult Products","created_at":"2026-01-09T19:38:20-05:00","handle":"ipod-touch","updated_at":"2026-01-09T19:38:20-05:00","published_at":"2008-09-25T20:00:00-04:00","template_suffix":null,"published_scope":"web","tags":"","status":"active","admin_graphql_api_id":"gid://shopify/Product/921728736","variants":[{"id":447654529,"product_id":921728736,"title":"Black","price":"199.00","position":1,"inventory_policy":"continue","compare_at_price":null,"option1":"Black","option2":null,"option3":null,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","taxable":true,"barcode":"1234_black","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2009BLACK","weight":1.25,"weight_unit":"lb","inventory_item_id":447654529,"inventory_quantity":13,"old_inventory_quantity":13,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/447654529","image_id":null}],"options":[{"id":891236591,"product_id":921728736,"name":"Title","position":1,"values":["Black"]}],"images":[],"image":null}]}

  * #### Retrieve all products, showing only some attributes

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/products.json?fields=id%2Cimages%2Ctitle" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Product.all({
          session: session,
          fields: "id,images,title",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Product.all(
          session: test_session,
          fields: "id,images,title",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Product.all({
          session: session,
          fields: "id,images,title",
        });

#### response

        HTTP/1.1 200 OK{"products":[{"id":632910392,"title":"IPod Nano - 8GB","images":[{"id":850703190,"alt":null,"position":1,"product_id":632910392,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/498048120","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano.png?v=1768005500","variant_ids":[]},{"id":562641783,"alt":null,"position":2,"product_id":632910392,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/1071517486","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano-2.png?v=1768005500","variant_ids":[808950810]},{"id":378407906,"alt":null,"position":3,"product_id":632910392,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/220090436","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano.png?v=1768005500","variant_ids":[]}]},{"id":921728736,"title":"IPod Touch 8GB","images":[]}]}


* * *

##

[Anchor to GET request, Retrieve a single product](/docs/api/admin-rest/latest/resources/product#get-products-product-id)

get

Retrieve a single product

[product](/docs/api/admin-graphql/latest/queries/product?example=retrieve-a-single-product)

Retrieve a single product.

###

[Anchor to Parameters of Retrieve a single product](/docs/api/admin-rest/latest/resources/product#get-products-product-id-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

product_id

string**string**

required**required**

* * *

fields

A comma-separated list of fields to include in the response.

* * *

Was this section helpful?

YesNo

###

[Anchor to get-products-product-id-examples](/docs/api/admin-rest/latest/resources/product#get-products-product-id-examples)Examples

Retrieve a single product by ID

Path parameters

product_id=632910392

string**string**

required**required**

Retrieve only particular fields from a single product

Path parameters

product_id=632910392

string**string**

required**required**

Query parameters

fields=id,images,title

A comma-separated list of fields to include in the response.

Was this section helpful?

YesNo

get

## /admin/api/2026-01/products/632910392.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/products/632910392.json" \

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

"product": {

"id": 632910392,

"title": "IPod Nano - 8GB",

"body_html": "<p>It's the small iPod with one very big idea: Video. Now the world's most popular music player, available in 4GB and 8GB models, lets you enjoy TV shows, movies, video podcasts, and more. The larger, brighter display means amazing picture quality. In six eye-catching colors, iPod nano is stunning all around. And with models starting at just $149, little speaks volumes.</p>",

"vendor": "Apple",

"product_type": "Cult Products",

"created_at": "2026-01-09T19:38:20-05:00",

"handle": "ipod-nano",

"updated_at": "2026-01-09T19:38:20-05:00",

"published_at": "2007-12-31T19:00:00-05:00",

"template_suffix": null,

"published_scope": "web",

"tags": "Emotive, Flash Memory, MP3, Music",

"status": "active",

"admin_graphql_api_id": "gid://shopify/Product/632910392",

"variants": [

{

"id": 808950810,

"product_id": 632910392,

"title": "Pink",

"price": "199.00",

"position": 1,

"inventory_policy": "continue",

"compare_at_price": null,

"option1": "Pink",

"option2": null,

"option3": null,

"created_at": "2026-01-09T19:38:20-05:00",

"updated_at": "2026-01-09T19:38:20-05:00",

"taxable": true,

"barcode": "1234_pink",

"fulfillment_service": "manual",

"grams": 567,

"inventory_management": "shopify",

### examples

  * #### Retrieve a single product by ID

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/products/632910392.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Product.find({
          session: session,
          id: 632910392,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Product.find(
          session: test_session,
          id: 632910392,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Product.find({
          session: session,
          id: 632910392,
        });

#### response

        HTTP/1.1 200 OK{"product":{"id":632910392,"title":"IPod Nano - 8GB","body_html":"<p>It's the small iPod with one very big idea: Video. Now the world's most popular music player, available in 4GB and 8GB models, lets you enjoy TV shows, movies, video podcasts, and more. The larger, brighter display means amazing picture quality. In six eye-catching colors, iPod nano is stunning all around. And with models starting at just $149, little speaks volumes.</p>","vendor":"Apple","product_type":"Cult Products","created_at":"2026-01-09T19:38:20-05:00","handle":"ipod-nano","updated_at":"2026-01-09T19:38:20-05:00","published_at":"2007-12-31T19:00:00-05:00","template_suffix":null,"published_scope":"web","tags":"Emotive, Flash Memory, MP3, Music","status":"active","admin_graphql_api_id":"gid://shopify/Product/632910392","variants":[{"id":808950810,"product_id":632910392,"title":"Pink","price":"199.00","position":1,"inventory_policy":"continue","compare_at_price":null,"option1":"Pink","option2":null,"option3":null,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","taxable":true,"barcode":"1234_pink","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008PINK","weight":1.25,"weight_unit":"lb","inventory_item_id":808950810,"inventory_quantity":10,"old_inventory_quantity":10,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/808950810","image_id":562641783},{"id":49148385,"product_id":632910392,"title":"Red","price":"199.00","position":2,"inventory_policy":"continue","compare_at_price":null,"option1":"Red","option2":null,"option3":null,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","taxable":true,"barcode":"1234_red","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008RED","weight":1.25,"weight_unit":"lb","inventory_item_id":49148385,"inventory_quantity":20,"old_inventory_quantity":20,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/49148385","image_id":null},{"id":39072856,"product_id":632910392,"title":"Green","price":"199.00","position":3,"inventory_policy":"continue","compare_at_price":null,"option1":"Green","option2":null,"option3":null,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","taxable":true,"barcode":"1234_green","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008GREEN","weight":1.25,"weight_unit":"lb","inventory_item_id":39072856,"inventory_quantity":30,"old_inventory_quantity":30,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/39072856","image_id":null},{"id":457924702,"product_id":632910392,"title":"Black","price":"199.00","position":4,"inventory_policy":"continue","compare_at_price":null,"option1":"Black","option2":null,"option3":null,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","taxable":true,"barcode":"1234_black","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008BLACK","weight":1.25,"weight_unit":"lb","inventory_item_id":457924702,"inventory_quantity":40,"old_inventory_quantity":40,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/457924702","image_id":null}],"options":[{"id":594680422,"product_id":632910392,"name":"Color","position":1,"values":["Pink","Red","Green","Black"]}],"images":[{"id":850703190,"alt":null,"position":1,"product_id":632910392,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/498048120","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano.png?v=1768005500","variant_ids":[]},{"id":562641783,"alt":null,"position":2,"product_id":632910392,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/1071517486","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano-2.png?v=1768005500","variant_ids":[808950810]},{"id":378407906,"alt":null,"position":3,"product_id":632910392,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/220090436","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano.png?v=1768005500","variant_ids":[]}],"image":{"id":850703190,"alt":null,"position":1,"product_id":632910392,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/498048120","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano.png?v=1768005500","variant_ids":[]}}}

  * #### Retrieve only particular fields from a single product

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/products/632910392.json?fields=id%2Cimages%2Ctitle" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Product.find({
          session: session,
          id: 632910392,
          fields: "id,images,title",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Product.find(
          session: test_session,
          id: 632910392,
          fields: "id,images,title",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Product.find({
          session: session,
          id: 632910392,
          fields: "id,images,title",
        });

#### response

        HTTP/1.1 200 OK{"product":{"id":632910392,"title":"IPod Nano - 8GB","images":[{"id":850703190,"alt":null,"position":1,"product_id":632910392,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/498048120","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano.png?v=1768005500","variant_ids":[]},{"id":562641783,"alt":null,"position":2,"product_id":632910392,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/1071517486","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano-2.png?v=1768005500","variant_ids":[808950810]},{"id":378407906,"alt":null,"position":3,"product_id":632910392,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/220090436","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano.png?v=1768005500","variant_ids":[]}]}}


* * *

##

[Anchor to GET request, Retrieve a count of products](/docs/api/admin-rest/latest/resources/product#get-products-count)

get

Retrieve a count of products

[productsCount](/docs/api/admin-graphql/latest/queries/productsCount?example=retrieve-a-count-of-products)

Retrieve a count of products.

###

[Anchor to Parameters of Retrieve a count of products](/docs/api/admin-rest/latest/resources/product#get-products-count-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

collection_id

Return products by product collection ID.

* * *

created_at_max

Return products created before a specified date. (format: 2014-04-25T16:15:47-04:00)

* * *

created_at_min

Return products created after a specified date. (format: 2014-04-25T16:15:47-04:00)

* * *

product_type

Return products by product type.

* * *

published_at_max

Return products published before a specified date. (format: 2014-04-25T16:15:47-04:00)

* * *

published_at_min

Return products published after a specified date. (format: 2014-04-25T16:15:47-04:00)

* * *

published_status

default any**default any**

Return products by their published status.

Show published_status properties

  * **published** : Return only published products.

  * **unpublished** : Return only unpublished products.

  * **any** : Return all products.


* * *

updated_at_max

Return products last updated before a specified date. (format: 2014-04-25T16:15:47-04:00)

* * *

updated_at_min

Return products last updated after a specified date. (format: 2014-04-25T16:15:47-04:00)

* * *

vendor

Return products by product vendor.

* * *

Was this section helpful?

YesNo

###

[Anchor to get-products-count-examples](/docs/api/admin-rest/latest/resources/product#get-products-count-examples)Examples

Retrieve a count of all products

Retrieve a count of all products of a given collection

Query parameters

collection_id=841564295

Return products by product collection ID.

Was this section helpful?

YesNo

get

## /admin/api/2026-01/products/count.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/products/count.json" \

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

  * #### Retrieve a count of all products

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/products/count.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Product.count({
          session: session,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Product.count(
          session: test_session,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Product.count({
          session: session,
        });

#### response

        HTTP/1.1 200 OK{"count":2}

  * #### Retrieve a count of all products of a given collection

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/products/count.json?collection_id=841564295" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Product.count({
          session: session,
          collection_id: "841564295",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Product.count(
          session: test_session,
          collection_id: "841564295",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Product.count({
          session: session,
          collection_id: "841564295",
        });

#### response

        HTTP/1.1 200 OK{"count":1}


* * *

##

[Anchor to PUT request, Updates a product](/docs/api/admin-rest/latest/resources/product#put-products-product-id)

put

Updates a product

[productUpdate](/docs/api/admin-graphql/latest/mutations/productUpdate)

Update a product




###

[Anchor to Parameters of Updates a product](/docs/api/admin-rest/latest/resources/product#put-products-product-id-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

product_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to put-products-product-id-examples](/docs/api/admin-rest/latest/resources/product#put-products-product-id-examples)Examples

Add a metafield to an existing product

Path parameters

product_id=632910392

string**string**

required**required**

Request body

product

Product resource**Product resource**

Show product properties

product.id:632910392

integer**integer**

int64**int64**

read-only**read-only**

An unsigned 64-bit integer that's used as a unique identifier for the product. Each `id` is unique across the Shopify system. No two products will have the same `id`, even if they're from different shops.

Hide a published product by changing the published attribute to false

Path parameters

product_id=632910392

string**string**

required**required**

Request body

product

Product resource**Product resource**

Show product properties

product.id:632910392

integer**integer**

int64**int64**

read-only**read-only**

An unsigned 64-bit integer that's used as a unique identifier for the product. Each `id` is unique across the Shopify system. No two products will have the same `id`, even if they're from different shops.

Show a hidden product by changing the published attribute to true

Path parameters

product_id=632910392

string**string**

required**required**

Request body

product

Product resource**Product resource**

Show product properties

product.id:632910392

integer**integer**

int64**int64**

read-only**read-only**

An unsigned 64-bit integer that's used as a unique identifier for the product. Each `id` is unique across the Shopify system. No two products will have the same `id`, even if they're from different shops.

Update a product and one of its variants

Path parameters

product_id=632910392

string**string**

required**required**

Request body

product

Product resource**Product resource**

Show product properties

product.id:632910392

integer**integer**

int64**int64**

read-only**read-only**

An unsigned 64-bit integer that's used as a unique identifier for the product. Each `id` is unique across the Shopify system. No two products will have the same `id`, even if they're from different shops.

product.title:"Updated Product Title"

string**string**

->[title](/docs/api/admin-graphql/latest/input-objects/ProductInput#fields-title)

The name of the product.

product.variants:[{"id":808950810,"price":"2000.00","sku":"Updating the Product SKU"},{"id":49148385},{"id":39072856},{"id":457924702}]

array**array**

An array of [product variants](/docs/admin-api/rest/reference/products/product-variant), each representing a different version of the product.

The `position` property is read-only. The position of variants is indicated by the order in which they are listed.

Update a product by adding a new product image

Path parameters

product_id=632910392

string**string**

required**required**

Request body

product

Product resource**Product resource**

Show product properties

product.id:632910392

integer**integer**

int64**int64**

read-only**read-only**

An unsigned 64-bit integer that's used as a unique identifier for the product. Each `id` is unique across the Shopify system. No two products will have the same `id`, even if they're from different shops.

product.images:[{"id":850703190},{"id":562641783},{"id":378407906},{"src":"http://example.com/rails_logo.gif"}]

array**array**

A list of [product image](/docs/admin-api/rest/reference/products/product-image) objects, each one representing an image associated with the product.

Update a product by clearing product images

Path parameters

product_id=632910392

string**string**

required**required**

Request body

product

Product resource**Product resource**

Show product properties

product.id:632910392

integer**integer**

int64**int64**

read-only**read-only**

An unsigned 64-bit integer that's used as a unique identifier for the product. Each `id` is unique across the Shopify system. No two products will have the same `id`, even if they're from different shops.

product.images:[]

array**array**

A list of [product image](/docs/admin-api/rest/reference/products/product-image) objects, each one representing an image associated with the product.

Update a product by reordering the product images

Path parameters

product_id=632910392

string**string**

required**required**

Request body

product

Product resource**Product resource**

Show product properties

product.id:632910392

integer**integer**

int64**int64**

read-only**read-only**

An unsigned 64-bit integer that's used as a unique identifier for the product. Each `id` is unique across the Shopify system. No two products will have the same `id`, even if they're from different shops.

product.images:[{"id":850703190,"position":3},{"id":562641783,"position":2},{"id":378407906,"position":1}]

array**array**

A list of [product image](/docs/admin-api/rest/reference/products/product-image) objects, each one representing an image associated with the product.

Update a product by reordering the product variants

Path parameters

product_id=632910392

string**string**

required**required**

Request body

product

Product resource**Product resource**

Show product properties

product.id:632910392

integer**integer**

int64**int64**

read-only**read-only**

An unsigned 64-bit integer that's used as a unique identifier for the product. Each `id` is unique across the Shopify system. No two products will have the same `id`, even if they're from different shops.

product.variants:[{"id":457924702},{"id":39072856},{"id":49148385},{"id":808950810}]

array**array**

An array of [product variants](/docs/admin-api/rest/reference/products/product-variant), each representing a different version of the product.

The `position` property is read-only. The position of variants is indicated by the order in which they are listed.

Update a product's SEO title and description

Path parameters

product_id=632910392

string**string**

required**required**

Request body

product

Product resource**Product resource**

Show product properties

product.id:632910392

integer**integer**

int64**int64**

read-only**read-only**

An unsigned 64-bit integer that's used as a unique identifier for the product. Each `id` is unique across the Shopify system. No two products will have the same `id`, even if they're from different shops.

Update a product's status

Path parameters

product_id=632910392

string**string**

required**required**

Request body

product

Product resource**Product resource**

Show product properties

product.id:632910392

integer**integer**

int64**int64**

read-only**read-only**

An unsigned 64-bit integer that's used as a unique identifier for the product. Each `id` is unique across the Shopify system. No two products will have the same `id`, even if they're from different shops.

product.status:"draft"

string**string**

->[status](/docs/api/admin-graphql/latest/input-objects/ProductInput#fields-status)

The status of the product. Valid values:

Show status properties

  * `active`: The product is ready to sell and is available to customers on the online store, sales channels, and apps. By default, existing products are set to active.
  * `archived`: The product is no longer being sold and isn't available to customers on sales channels and apps.
  * `draft`: The product isn't ready to sell and is unavailable to customers on sales channels and apps. By default, duplicated and unarchived products are set to draft.


Update a product's tags

Path parameters

product_id=632910392

string**string**

required**required**

Request body

product

Product resource**Product resource**

Show product properties

product.id:632910392

integer**integer**

int64**int64**

read-only**read-only**

An unsigned 64-bit integer that's used as a unique identifier for the product. Each `id` is unique across the Shopify system. No two products will have the same `id`, even if they're from different shops.

product.tags:"Barnes & Noble, John's Fav"

string**string**

->[tags](/docs/api/admin-graphql/latest/input-objects/ProductInput#fields-tags)

A string of comma-separated tags that are used for filtering and search. A product can have up to 250 tags. Each tag can have up to 255 characters.

Update a product's title

Path parameters

product_id=632910392

string**string**

required**required**

Request body

product

Product resource**Product resource**

Show product properties

product.id:632910392

integer**integer**

int64**int64**

read-only**read-only**

An unsigned 64-bit integer that's used as a unique identifier for the product. Each `id` is unique across the Shopify system. No two products will have the same `id`, even if they're from different shops.

product.title:"New product title"

string**string**

->[title](/docs/api/admin-graphql/latest/input-objects/ProductInput#fields-title)

The name of the product.

Was this section helpful?

YesNo

put

## /admin/api/2026-01/products/632910392.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{"product":{"id":632910392,"metafields":[{"key":"new","value":"newvalue","type":"single_line_text_field","namespace":"global"}]}}' \

-X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/products/632910392.json" \

-H "X-Shopify-Access-Token: {access_token}" \

-H "Content-Type: application/json"

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

"product": {

"id": 632910392,

"title": "IPod Nano - 8GB",

"body_html": "<p>It's the small iPod with one very big idea: Video. Now the world's most popular music player, available in 4GB and 8GB models, lets you enjoy TV shows, movies, video podcasts, and more. The larger, brighter display means amazing picture quality. In six eye-catching colors, iPod nano is stunning all around. And with models starting at just $149, little speaks volumes.</p>",

"vendor": "Apple",

"product_type": "Cult Products",

"created_at": "2026-01-09T19:38:20-05:00",

"handle": "ipod-nano",

"updated_at": "2026-01-09T19:40:43-05:00",

"published_at": "2007-12-31T19:00:00-05:00",

"template_suffix": null,

"published_scope": "web",

"tags": "Emotive, Flash Memory, MP3, Music",

"status": "active",

"admin_graphql_api_id": "gid://shopify/Product/632910392",

"variants": [

{

"id": 808950810,

"product_id": 632910392,

"title": "Pink",

"price": "199.00",

"position": 1,

"inventory_policy": "continue",

"compare_at_price": null,

"option1": "Pink",

"option2": null,

"option3": null,

"created_at": "2026-01-09T19:38:20-05:00",

"updated_at": "2026-01-09T19:38:20-05:00",

"taxable": true,

"barcode": "1234_pink",

"fulfillment_service": "manual",

"grams": 567,

"inventory_management": "shopify",

### examples

  * #### Add a metafield to an existing product

#####

        curl -d '{"product":{"id":632910392,"metafields":[{"key":"new","value":"newvalue","type":"single_line_text_field","namespace":"global"}]}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/products/632910392.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const product = new admin.rest.resources.Product({session: session});

        product.id = 632910392;
        product.metafields = [
          {
            "key": "new",
            "value": "newvalue",
            "type": "single_line_text_field",
            "namespace": "global"
          }
        ];
        await product.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        product = ShopifyAPI::Product.new(session: test_session)
        product.id = 632910392
        product.metafields = [
          {
            "key" => "new",
            "value" => "newvalue",
            "type" => "single_line_text_field",
            "namespace" => "global"
          }
        ]
        product.save!

#####

        // Session is built by the OAuth process

        const product = new shopify.rest.Product({session: session});
        product.id = 632910392;
        product.metafields = [
          {
            "key": "new",
            "value": "newvalue",
            "type": "single_line_text_field",
            "namespace": "global"
          }
        ];
        await product.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"product":{"id":632910392,"title":"IPod Nano - 8GB","body_html":"<p>It's the small iPod with one very big idea: Video. Now the world's most popular music player, available in 4GB and 8GB models, lets you enjoy TV shows, movies, video podcasts, and more. The larger, brighter display means amazing picture quality. In six eye-catching colors, iPod nano is stunning all around. And with models starting at just $149, little speaks volumes.</p>","vendor":"Apple","product_type":"Cult Products","created_at":"2026-01-09T19:38:20-05:00","handle":"ipod-nano","updated_at":"2026-01-09T19:40:43-05:00","published_at":"2007-12-31T19:00:00-05:00","template_suffix":null,"published_scope":"web","tags":"Emotive, Flash Memory, MP3, Music","status":"active","admin_graphql_api_id":"gid://shopify/Product/632910392","variants":[{"id":808950810,"product_id":632910392,"title":"Pink","price":"199.00","position":1,"inventory_policy":"continue","compare_at_price":null,"option1":"Pink","option2":null,"option3":null,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","taxable":true,"barcode":"1234_pink","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008PINK","weight":1.25,"weight_unit":"lb","inventory_item_id":808950810,"inventory_quantity":10,"old_inventory_quantity":10,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/808950810","image_id":562641783},{"id":49148385,"product_id":632910392,"title":"Red","price":"199.00","position":2,"inventory_policy":"continue","compare_at_price":null,"option1":"Red","option2":null,"option3":null,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","taxable":true,"barcode":"1234_red","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008RED","weight":1.25,"weight_unit":"lb","inventory_item_id":49148385,"inventory_quantity":20,"old_inventory_quantity":20,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/49148385","image_id":null},{"id":39072856,"product_id":632910392,"title":"Green","price":"199.00","position":3,"inventory_policy":"continue","compare_at_price":null,"option1":"Green","option2":null,"option3":null,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","taxable":true,"barcode":"1234_green","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008GREEN","weight":1.25,"weight_unit":"lb","inventory_item_id":39072856,"inventory_quantity":30,"old_inventory_quantity":30,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/39072856","image_id":null},{"id":457924702,"product_id":632910392,"title":"Black","price":"199.00","position":4,"inventory_policy":"continue","compare_at_price":null,"option1":"Black","option2":null,"option3":null,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","taxable":true,"barcode":"1234_black","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008BLACK","weight":1.25,"weight_unit":"lb","inventory_item_id":457924702,"inventory_quantity":40,"old_inventory_quantity":40,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/457924702","image_id":null}],"options":[{"id":594680422,"product_id":632910392,"name":"Color","position":1,"values":["Pink","Red","Green","Black"]}],"images":[{"id":850703190,"alt":null,"position":1,"product_id":632910392,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/498048120","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano.png?v=1768005500","variant_ids":[]},{"id":562641783,"alt":null,"position":2,"product_id":632910392,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/1071517486","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano-2.png?v=1768005500","variant_ids":[808950810]},{"id":378407906,"alt":null,"position":3,"product_id":632910392,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/220090436","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano.png?v=1768005500","variant_ids":[]}],"image":{"id":850703190,"alt":null,"position":1,"product_id":632910392,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/498048120","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano.png?v=1768005500","variant_ids":[]}}}

  * #### Hide a published product by changing the published attribute to false

#####

        curl -d '{"product":{"id":632910392,"published":false}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/products/632910392.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const product = new admin.rest.resources.Product({session: session});

        product.id = 632910392;
        product.published = false;
        await product.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        product = ShopifyAPI::Product.new(session: test_session)
        product.id = 632910392
        product.published = false
        product.save!

#####

        // Session is built by the OAuth process

        const product = new shopify.rest.Product({session: session});
        product.id = 632910392;
        product.published = false;
        await product.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"product":{"id":632910392,"title":"IPod Nano - 8GB","body_html":"<p>It's the small iPod with one very big idea: Video. Now the world's most popular music player, available in 4GB and 8GB models, lets you enjoy TV shows, movies, video podcasts, and more. The larger, brighter display means amazing picture quality. In six eye-catching colors, iPod nano is stunning all around. And with models starting at just $149, little speaks volumes.</p>","vendor":"Apple","product_type":"Cult Products","created_at":"2026-01-09T19:38:20-05:00","handle":"ipod-nano","updated_at":"2026-01-09T19:39:41-05:00","published_at":null,"template_suffix":null,"published_scope":"web","tags":"Emotive, Flash Memory, MP3, Music","status":"active","admin_graphql_api_id":"gid://shopify/Product/632910392","variants":[{"id":808950810,"product_id":632910392,"title":"Pink","price":"199.00","position":1,"inventory_policy":"continue","compare_at_price":null,"option1":"Pink","option2":null,"option3":null,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","taxable":true,"barcode":"1234_pink","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008PINK","weight":1.25,"weight_unit":"lb","inventory_item_id":808950810,"inventory_quantity":10,"old_inventory_quantity":10,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/808950810","image_id":562641783},{"id":49148385,"product_id":632910392,"title":"Red","price":"199.00","position":2,"inventory_policy":"continue","compare_at_price":null,"option1":"Red","option2":null,"option3":null,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","taxable":true,"barcode":"1234_red","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008RED","weight":1.25,"weight_unit":"lb","inventory_item_id":49148385,"inventory_quantity":20,"old_inventory_quantity":20,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/49148385","image_id":null},{"id":39072856,"product_id":632910392,"title":"Green","price":"199.00","position":3,"inventory_policy":"continue","compare_at_price":null,"option1":"Green","option2":null,"option3":null,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","taxable":true,"barcode":"1234_green","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008GREEN","weight":1.25,"weight_unit":"lb","inventory_item_id":39072856,"inventory_quantity":30,"old_inventory_quantity":30,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/39072856","image_id":null},{"id":457924702,"product_id":632910392,"title":"Black","price":"199.00","position":4,"inventory_policy":"continue","compare_at_price":null,"option1":"Black","option2":null,"option3":null,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","taxable":true,"barcode":"1234_black","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008BLACK","weight":1.25,"weight_unit":"lb","inventory_item_id":457924702,"inventory_quantity":40,"old_inventory_quantity":40,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/457924702","image_id":null}],"options":[{"id":594680422,"product_id":632910392,"name":"Color","position":1,"values":["Pink","Red","Green","Black"]}],"images":[{"id":850703190,"alt":null,"position":1,"product_id":632910392,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/498048120","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano.png?v=1768005500","variant_ids":[]},{"id":562641783,"alt":null,"position":2,"product_id":632910392,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/1071517486","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano-2.png?v=1768005500","variant_ids":[808950810]},{"id":378407906,"alt":null,"position":3,"product_id":632910392,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/220090436","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano.png?v=1768005500","variant_ids":[]}],"image":{"id":850703190,"alt":null,"position":1,"product_id":632910392,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/498048120","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano.png?v=1768005500","variant_ids":[]}}}

  * #### Show a hidden product by changing the published attribute to true

#####

        curl -d '{"product":{"id":632910392,"published":true}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/products/632910392.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const product = new admin.rest.resources.Product({session: session});

        product.id = 632910392;
        product.published = true;
        await product.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        product = ShopifyAPI::Product.new(session: test_session)
        product.id = 632910392
        product.published = true
        product.save!

#####

        // Session is built by the OAuth process

        const product = new shopify.rest.Product({session: session});
        product.id = 632910392;
        product.published = true;
        await product.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"product":{"id":632910392,"title":"IPod Nano - 8GB","body_html":"<p>It's the small iPod with one very big idea: Video. Now the world's most popular music player, available in 4GB and 8GB models, lets you enjoy TV shows, movies, video podcasts, and more. The larger, brighter display means amazing picture quality. In six eye-catching colors, iPod nano is stunning all around. And with models starting at just $149, little speaks volumes.</p>","vendor":"Apple","product_type":"Cult Products","created_at":"2026-01-09T19:38:20-05:00","handle":"ipod-nano","updated_at":"2026-01-09T19:40:44-05:00","published_at":"2026-01-09T19:40:44-05:00","template_suffix":null,"published_scope":"web","tags":"Emotive, Flash Memory, MP3, Music","status":"active","admin_graphql_api_id":"gid://shopify/Product/632910392","variants":[{"id":808950810,"product_id":632910392,"title":"Pink","price":"199.00","position":1,"inventory_policy":"continue","compare_at_price":null,"option1":"Pink","option2":null,"option3":null,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","taxable":true,"barcode":"1234_pink","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008PINK","weight":1.25,"weight_unit":"lb","inventory_item_id":808950810,"inventory_quantity":10,"old_inventory_quantity":10,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/808950810","image_id":562641783},{"id":49148385,"product_id":632910392,"title":"Red","price":"199.00","position":2,"inventory_policy":"continue","compare_at_price":null,"option1":"Red","option2":null,"option3":null,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","taxable":true,"barcode":"1234_red","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008RED","weight":1.25,"weight_unit":"lb","inventory_item_id":49148385,"inventory_quantity":20,"old_inventory_quantity":20,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/49148385","image_id":null},{"id":39072856,"product_id":632910392,"title":"Green","price":"199.00","position":3,"inventory_policy":"continue","compare_at_price":null,"option1":"Green","option2":null,"option3":null,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","taxable":true,"barcode":"1234_green","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008GREEN","weight":1.25,"weight_unit":"lb","inventory_item_id":39072856,"inventory_quantity":30,"old_inventory_quantity":30,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/39072856","image_id":null},{"id":457924702,"product_id":632910392,"title":"Black","price":"199.00","position":4,"inventory_policy":"continue","compare_at_price":null,"option1":"Black","option2":null,"option3":null,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","taxable":true,"barcode":"1234_black","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008BLACK","weight":1.25,"weight_unit":"lb","inventory_item_id":457924702,"inventory_quantity":40,"old_inventory_quantity":40,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/457924702","image_id":null}],"options":[{"id":594680422,"product_id":632910392,"name":"Color","position":1,"values":["Pink","Red","Green","Black"]}],"images":[{"id":850703190,"alt":null,"position":1,"product_id":632910392,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/498048120","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano.png?v=1768005500","variant_ids":[]},{"id":562641783,"alt":null,"position":2,"product_id":632910392,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/1071517486","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano-2.png?v=1768005500","variant_ids":[808950810]},{"id":378407906,"alt":null,"position":3,"product_id":632910392,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/220090436","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano.png?v=1768005500","variant_ids":[]}],"image":{"id":850703190,"alt":null,"position":1,"product_id":632910392,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/498048120","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano.png?v=1768005500","variant_ids":[]}}}

  * #### Update a product and one of its variants

#####

        curl -d '{"product":{"id":632910392,"title":"Updated Product Title","variants":[{"id":808950810,"price":"2000.00","sku":"Updating the Product SKU"},{"id":49148385},{"id":39072856},{"id":457924702}]}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/products/632910392.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const product = new admin.rest.resources.Product({session: session});

        product.id = 632910392;
        product.title = "Updated Product Title";
        product.variants = [
          {
            "id": 808950810,
            "price": "2000.00",
            "sku": "Updating the Product SKU"
          },
          {
            "id": 49148385
          },
          {
            "id": 39072856
          },
          {
            "id": 457924702
          }
        ];
        await product.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        product = ShopifyAPI::Product.new(session: test_session)
        product.id = 632910392
        product.title = "Updated Product Title"
        product.variants = [
          {
            "id" => 808950810,
            "price" => "2000.00",
            "sku" => "Updating the Product SKU"
          },
          {
            "id" => 49148385
          },
          {
            "id" => 39072856
          },
          {
            "id" => 457924702
          }
        ]
        product.save!

#####

        // Session is built by the OAuth process

        const product = new shopify.rest.Product({session: session});
        product.id = 632910392;
        product.title = "Updated Product Title";
        product.variants = [
          {
            "id": 808950810,
            "price": "2000.00",
            "sku": "Updating the Product SKU"
          },
          {
            "id": 49148385
          },
          {
            "id": 39072856
          },
          {
            "id": 457924702
          }
        ];
        await product.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"product":{"id":632910392,"title":"Updated Product Title","body_html":"<p>It's the small iPod with one very big idea: Video. Now the world's most popular music player, available in 4GB and 8GB models, lets you enjoy TV shows, movies, video podcasts, and more. The larger, brighter display means amazing picture quality. In six eye-catching colors, iPod nano is stunning all around. And with models starting at just $149, little speaks volumes.</p>","vendor":"Apple","product_type":"Cult Products","created_at":"2026-01-09T19:38:20-05:00","handle":"ipod-nano","updated_at":"2026-01-09T19:40:16-05:00","published_at":"2007-12-31T19:00:00-05:00","template_suffix":null,"published_scope":"web","tags":"Emotive, Flash Memory, MP3, Music","status":"active","admin_graphql_api_id":"gid://shopify/Product/632910392","variants":[{"id":808950810,"product_id":632910392,"title":"Pink","price":"2000.00","position":1,"inventory_policy":"continue","compare_at_price":null,"option1":"Pink","option2":null,"option3":null,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:40:16-05:00","taxable":true,"barcode":"1234_pink","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"Updating the Product SKU","weight":1.25,"weight_unit":"lb","inventory_item_id":808950810,"inventory_quantity":10,"old_inventory_quantity":10,"presentment_prices":[{"price":{"amount":"2000.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/808950810","image_id":562641783},{"id":49148385,"product_id":632910392,"title":"Red","price":"199.00","position":2,"inventory_policy":"continue","compare_at_price":null,"option1":"Red","option2":null,"option3":null,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","taxable":true,"barcode":"1234_red","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008RED","weight":1.25,"weight_unit":"lb","inventory_item_id":49148385,"inventory_quantity":20,"old_inventory_quantity":20,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/49148385","image_id":null},{"id":39072856,"product_id":632910392,"title":"Green","price":"199.00","position":3,"inventory_policy":"continue","compare_at_price":null,"option1":"Green","option2":null,"option3":null,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","taxable":true,"barcode":"1234_green","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008GREEN","weight":1.25,"weight_unit":"lb","inventory_item_id":39072856,"inventory_quantity":30,"old_inventory_quantity":30,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/39072856","image_id":null},{"id":457924702,"product_id":632910392,"title":"Black","price":"199.00","position":4,"inventory_policy":"continue","compare_at_price":null,"option1":"Black","option2":null,"option3":null,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","taxable":true,"barcode":"1234_black","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008BLACK","weight":1.25,"weight_unit":"lb","inventory_item_id":457924702,"inventory_quantity":40,"old_inventory_quantity":40,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/457924702","image_id":null}],"options":[{"id":594680422,"product_id":632910392,"name":"Color","position":1,"values":["Pink","Red","Green","Black"]}],"images":[{"id":850703190,"alt":null,"position":1,"product_id":632910392,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/498048120","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano.png?v=1768005500","variant_ids":[]},{"id":562641783,"alt":null,"position":2,"product_id":632910392,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/1071517486","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano-2.png?v=1768005500","variant_ids":[808950810]},{"id":378407906,"alt":null,"position":3,"product_id":632910392,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/220090436","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano.png?v=1768005500","variant_ids":[]}],"image":{"id":850703190,"alt":null,"position":1,"product_id":632910392,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/498048120","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano.png?v=1768005500","variant_ids":[]}}}

  * #### Update a product by adding a new product image

#####

        curl -d '{"product":{"id":632910392,"images":[{"id":850703190},{"id":562641783},{"id":378407906},{"src":"http://example.com/rails_logo.gif"}]}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/products/632910392.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const product = new admin.rest.resources.Product({session: session});

        product.id = 632910392;
        product.images = [
          {
            "id": 850703190
          },
          {
            "id": 562641783
          },
          {
            "id": 378407906
          },
          {
            "src": "http://example.com/rails_logo.gif"
          }
        ];
        await product.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        product = ShopifyAPI::Product.new(session: test_session)
        product.id = 632910392
        product.images = [
          {
            "id" => 850703190
          },
          {
            "id" => 562641783
          },
          {
            "id" => 378407906
          },
          {
            "src" => "http://example.com/rails_logo.gif"
          }
        ]
        product.save!

#####

        // Session is built by the OAuth process

        const product = new shopify.rest.Product({session: session});
        product.id = 632910392;
        product.images = [
          {
            "id": 850703190
          },
          {
            "id": 562641783
          },
          {
            "id": 378407906
          },
          {
            "src": "http://example.com/rails_logo.gif"
          }
        ];
        await product.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"product":{"id":632910392,"title":"IPod Nano - 8GB","body_html":"<p>It's the small iPod with one very big idea: Video. Now the world's most popular music player, available in 4GB and 8GB models, lets you enjoy TV shows, movies, video podcasts, and more. The larger, brighter display means amazing picture quality. In six eye-catching colors, iPod nano is stunning all around. And with models starting at just $149, little speaks volumes.</p>","vendor":"Apple","product_type":"Cult Products","created_at":"2026-01-09T19:38:20-05:00","handle":"ipod-nano","updated_at":"2026-01-09T19:38:20-05:00","published_at":"2007-12-31T19:00:00-05:00","template_suffix":null,"published_scope":"web","tags":"Emotive, Flash Memory, MP3, Music","status":"active","admin_graphql_api_id":"gid://shopify/Product/632910392","variants":[{"id":808950810,"product_id":632910392,"title":"Pink","price":"199.00","position":1,"inventory_policy":"continue","compare_at_price":null,"option1":"Pink","option2":null,"option3":null,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","taxable":true,"barcode":"1234_pink","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008PINK","weight":1.25,"weight_unit":"lb","inventory_item_id":808950810,"inventory_quantity":10,"old_inventory_quantity":10,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/808950810","image_id":562641783},{"id":49148385,"product_id":632910392,"title":"Red","price":"199.00","position":2,"inventory_policy":"continue","compare_at_price":null,"option1":"Red","option2":null,"option3":null,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","taxable":true,"barcode":"1234_red","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008RED","weight":1.25,"weight_unit":"lb","inventory_item_id":49148385,"inventory_quantity":20,"old_inventory_quantity":20,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/49148385","image_id":null},{"id":39072856,"product_id":632910392,"title":"Green","price":"199.00","position":3,"inventory_policy":"continue","compare_at_price":null,"option1":"Green","option2":null,"option3":null,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","taxable":true,"barcode":"1234_green","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008GREEN","weight":1.25,"weight_unit":"lb","inventory_item_id":39072856,"inventory_quantity":30,"old_inventory_quantity":30,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/39072856","image_id":null},{"id":457924702,"product_id":632910392,"title":"Black","price":"199.00","position":4,"inventory_policy":"continue","compare_at_price":null,"option1":"Black","option2":null,"option3":null,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","taxable":true,"barcode":"1234_black","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008BLACK","weight":1.25,"weight_unit":"lb","inventory_item_id":457924702,"inventory_quantity":40,"old_inventory_quantity":40,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/457924702","image_id":null}],"options":[{"id":594680422,"product_id":632910392,"name":"Color","position":1,"values":["Pink","Red","Green","Black"]}],"images":[{"id":850703190,"alt":null,"position":1,"product_id":632910392,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/498048120","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano.png?v=1768005500","variant_ids":[]},{"id":562641783,"alt":null,"position":2,"product_id":632910392,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/1071517486","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano-2.png?v=1768005500","variant_ids":[808950810]},{"id":378407906,"alt":null,"position":3,"product_id":632910392,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/220090436","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano.png?v=1768005500","variant_ids":[]},{"id":1001473922,"alt":null,"position":4,"product_id":632910392,"created_at":"2026-01-09T19:40:39-05:00","updated_at":"2026-01-09T19:40:39-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/1072273215","width":110,"height":140,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/files/rails_logo20260109-27647-chr82g.gif?v=1768005639","variant_ids":[]}],"image":{"id":850703190,"alt":null,"position":1,"product_id":632910392,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/498048120","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano.png?v=1768005500","variant_ids":[]}}}

  * #### Update a product by clearing product images

#####

        curl -d '{"product":{"id":632910392,"images":[]}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/products/632910392.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const product = new admin.rest.resources.Product({session: session});

        product.id = 632910392;
        product.images = [];
        await product.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        product = ShopifyAPI::Product.new(session: test_session)
        product.id = 632910392
        product.images = []
        product.save!

#####

        // Session is built by the OAuth process

        const product = new shopify.rest.Product({session: session});
        product.id = 632910392;
        product.images = [];
        await product.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"product":{"id":632910392,"title":"IPod Nano - 8GB","body_html":"<p>It's the small iPod with one very big idea: Video. Now the world's most popular music player, available in 4GB and 8GB models, lets you enjoy TV shows, movies, video podcasts, and more. The larger, brighter display means amazing picture quality. In six eye-catching colors, iPod nano is stunning all around. And with models starting at just $149, little speaks volumes.</p>","vendor":"Apple","product_type":"Cult Products","created_at":"2026-01-09T19:38:20-05:00","handle":"ipod-nano","updated_at":"2026-01-09T19:38:59-05:00","published_at":"2007-12-31T19:00:00-05:00","template_suffix":null,"published_scope":"web","tags":"Emotive, Flash Memory, MP3, Music","status":"active","admin_graphql_api_id":"gid://shopify/Product/632910392","variants":[{"id":808950810,"product_id":632910392,"title":"Pink","price":"199.00","position":1,"inventory_policy":"continue","compare_at_price":null,"option1":"Pink","option2":null,"option3":null,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:59-05:00","taxable":true,"barcode":"1234_pink","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008PINK","weight":1.25,"weight_unit":"lb","inventory_item_id":808950810,"inventory_quantity":10,"old_inventory_quantity":10,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/808950810","image_id":null},{"id":49148385,"product_id":632910392,"title":"Red","price":"199.00","position":2,"inventory_policy":"continue","compare_at_price":null,"option1":"Red","option2":null,"option3":null,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","taxable":true,"barcode":"1234_red","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008RED","weight":1.25,"weight_unit":"lb","inventory_item_id":49148385,"inventory_quantity":20,"old_inventory_quantity":20,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/49148385","image_id":null},{"id":39072856,"product_id":632910392,"title":"Green","price":"199.00","position":3,"inventory_policy":"continue","compare_at_price":null,"option1":"Green","option2":null,"option3":null,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","taxable":true,"barcode":"1234_green","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008GREEN","weight":1.25,"weight_unit":"lb","inventory_item_id":39072856,"inventory_quantity":30,"old_inventory_quantity":30,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/39072856","image_id":null},{"id":457924702,"product_id":632910392,"title":"Black","price":"199.00","position":4,"inventory_policy":"continue","compare_at_price":null,"option1":"Black","option2":null,"option3":null,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","taxable":true,"barcode":"1234_black","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008BLACK","weight":1.25,"weight_unit":"lb","inventory_item_id":457924702,"inventory_quantity":40,"old_inventory_quantity":40,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/457924702","image_id":null}],"options":[{"id":594680422,"product_id":632910392,"name":"Color","position":1,"values":["Pink","Red","Green","Black"]}],"images":[],"image":null}}

  * #### Update a product by reordering the product images

#####

        curl -d '{"product":{"id":632910392,"images":[{"id":850703190,"position":3},{"id":562641783,"position":2},{"id":378407906,"position":1}]}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/products/632910392.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const product = new admin.rest.resources.Product({session: session});

        product.id = 632910392;
        product.images = [
          {
            "id": 850703190,
            "position": 3
          },
          {
            "id": 562641783,
            "position": 2
          },
          {
            "id": 378407906,
            "position": 1
          }
        ];
        await product.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        product = ShopifyAPI::Product.new(session: test_session)
        product.id = 632910392
        product.images = [
          {
            "id" => 850703190,
            "position" => 3
          },
          {
            "id" => 562641783,
            "position" => 2
          },
          {
            "id" => 378407906,
            "position" => 1
          }
        ]
        product.save!

#####

        // Session is built by the OAuth process

        const product = new shopify.rest.Product({session: session});
        product.id = 632910392;
        product.images = [
          {
            "id": 850703190,
            "position": 3
          },
          {
            "id": 562641783,
            "position": 2
          },
          {
            "id": 378407906,
            "position": 1
          }
        ];
        await product.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"product":{"id":632910392,"title":"IPod Nano - 8GB","body_html":"<p>It's the small iPod with one very big idea: Video. Now the world's most popular music player, available in 4GB and 8GB models, lets you enjoy TV shows, movies, video podcasts, and more. The larger, brighter display means amazing picture quality. In six eye-catching colors, iPod nano is stunning all around. And with models starting at just $149, little speaks volumes.</p>","vendor":"Apple","product_type":"Cult Products","created_at":"2026-01-09T19:38:20-05:00","handle":"ipod-nano","updated_at":"2026-01-09T19:39:13-05:00","published_at":"2007-12-31T19:00:00-05:00","template_suffix":null,"published_scope":"web","tags":"Emotive, Flash Memory, MP3, Music","status":"active","admin_graphql_api_id":"gid://shopify/Product/632910392","variants":[{"id":808950810,"product_id":632910392,"title":"Pink","price":"199.00","position":1,"inventory_policy":"continue","compare_at_price":null,"option1":"Pink","option2":null,"option3":null,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","taxable":true,"barcode":"1234_pink","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008PINK","weight":1.25,"weight_unit":"lb","inventory_item_id":808950810,"inventory_quantity":10,"old_inventory_quantity":10,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/808950810","image_id":562641783},{"id":49148385,"product_id":632910392,"title":"Red","price":"199.00","position":2,"inventory_policy":"continue","compare_at_price":null,"option1":"Red","option2":null,"option3":null,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","taxable":true,"barcode":"1234_red","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008RED","weight":1.25,"weight_unit":"lb","inventory_item_id":49148385,"inventory_quantity":20,"old_inventory_quantity":20,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/49148385","image_id":null},{"id":39072856,"product_id":632910392,"title":"Green","price":"199.00","position":3,"inventory_policy":"continue","compare_at_price":null,"option1":"Green","option2":null,"option3":null,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","taxable":true,"barcode":"1234_green","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008GREEN","weight":1.25,"weight_unit":"lb","inventory_item_id":39072856,"inventory_quantity":30,"old_inventory_quantity":30,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/39072856","image_id":null},{"id":457924702,"product_id":632910392,"title":"Black","price":"199.00","position":4,"inventory_policy":"continue","compare_at_price":null,"option1":"Black","option2":null,"option3":null,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","taxable":true,"barcode":"1234_black","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008BLACK","weight":1.25,"weight_unit":"lb","inventory_item_id":457924702,"inventory_quantity":40,"old_inventory_quantity":40,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/457924702","image_id":null}],"options":[{"id":594680422,"product_id":632910392,"name":"Color","position":1,"values":["Pink","Red","Green","Black"]}],"images":[{"id":378407906,"alt":null,"position":1,"product_id":632910392,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:39:13-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/220090436","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano.png?v=1768005553","variant_ids":[]},{"id":562641783,"alt":null,"position":2,"product_id":632910392,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:39:13-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/1071517486","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano-2.png?v=1768005553","variant_ids":[808950810]},{"id":850703190,"alt":null,"position":3,"product_id":632910392,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:39:13-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/498048120","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano.png?v=1768005553","variant_ids":[]}],"image":{"id":378407906,"alt":null,"position":1,"product_id":632910392,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:39:13-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/220090436","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano.png?v=1768005553","variant_ids":[]}}}

  * #### Update a product by reordering the product variants

#####

        curl -d '{"product":{"id":632910392,"variants":[{"id":457924702},{"id":39072856},{"id":49148385},{"id":808950810}]}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/products/632910392.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const product = new admin.rest.resources.Product({session: session});

        product.id = 632910392;
        product.variants = [
          {
            "id": 457924702
          },
          {
            "id": 39072856
          },
          {
            "id": 49148385
          },
          {
            "id": 808950810
          }
        ];
        await product.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        product = ShopifyAPI::Product.new(session: test_session)
        product.id = 632910392
        product.variants = [
          {
            "id" => 457924702
          },
          {
            "id" => 39072856
          },
          {
            "id" => 49148385
          },
          {
            "id" => 808950810
          }
        ]
        product.save!

#####

        // Session is built by the OAuth process

        const product = new shopify.rest.Product({session: session});
        product.id = 632910392;
        product.variants = [
          {
            "id": 457924702
          },
          {
            "id": 39072856
          },
          {
            "id": 49148385
          },
          {
            "id": 808950810
          }
        ];
        await product.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"product":{"id":632910392,"title":"IPod Nano - 8GB","body_html":"<p>It's the small iPod with one very big idea: Video. Now the world's most popular music player, available in 4GB and 8GB models, lets you enjoy TV shows, movies, video podcasts, and more. The larger, brighter display means amazing picture quality. In six eye-catching colors, iPod nano is stunning all around. And with models starting at just $149, little speaks volumes.</p>","vendor":"Apple","product_type":"Cult Products","created_at":"2026-01-09T19:38:20-05:00","handle":"ipod-nano","updated_at":"2026-01-09T19:40:10-05:00","published_at":"2007-12-31T19:00:00-05:00","template_suffix":null,"published_scope":"web","tags":"Emotive, Flash Memory, MP3, Music","status":"active","admin_graphql_api_id":"gid://shopify/Product/632910392","variants":[{"id":457924702,"product_id":632910392,"title":"Black","price":"199.00","position":1,"inventory_policy":"continue","compare_at_price":null,"option1":"Black","option2":null,"option3":null,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:40:10-05:00","taxable":true,"barcode":"1234_black","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008BLACK","weight":1.25,"weight_unit":"lb","inventory_item_id":457924702,"inventory_quantity":40,"old_inventory_quantity":40,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/457924702","image_id":null},{"id":39072856,"product_id":632910392,"title":"Green","price":"199.00","position":2,"inventory_policy":"continue","compare_at_price":null,"option1":"Green","option2":null,"option3":null,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:40:10-05:00","taxable":true,"barcode":"1234_green","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008GREEN","weight":1.25,"weight_unit":"lb","inventory_item_id":39072856,"inventory_quantity":30,"old_inventory_quantity":30,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/39072856","image_id":null},{"id":49148385,"product_id":632910392,"title":"Red","price":"199.00","position":3,"inventory_policy":"continue","compare_at_price":null,"option1":"Red","option2":null,"option3":null,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:40:10-05:00","taxable":true,"barcode":"1234_red","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008RED","weight":1.25,"weight_unit":"lb","inventory_item_id":49148385,"inventory_quantity":20,"old_inventory_quantity":20,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/49148385","image_id":null},{"id":808950810,"product_id":632910392,"title":"Pink","price":"199.00","position":4,"inventory_policy":"continue","compare_at_price":null,"option1":"Pink","option2":null,"option3":null,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:40:10-05:00","taxable":true,"barcode":"1234_pink","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008PINK","weight":1.25,"weight_unit":"lb","inventory_item_id":808950810,"inventory_quantity":10,"old_inventory_quantity":10,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/808950810","image_id":562641783}],"options":[{"id":594680422,"product_id":632910392,"name":"Color","position":1,"values":["Black","Green","Red","Pink"]}],"images":[{"id":850703190,"alt":null,"position":1,"product_id":632910392,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/498048120","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano.png?v=1768005500","variant_ids":[]},{"id":562641783,"alt":null,"position":2,"product_id":632910392,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/1071517486","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano-2.png?v=1768005500","variant_ids":[808950810]},{"id":378407906,"alt":null,"position":3,"product_id":632910392,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/220090436","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano.png?v=1768005500","variant_ids":[]}],"image":{"id":850703190,"alt":null,"position":1,"product_id":632910392,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/498048120","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano.png?v=1768005500","variant_ids":[]}}}

  * #### Update a product's SEO title and description

#####

        curl -d '{"product":{"id":632910392,"metafields_global_title_tag":"Brand new title","metafields_global_description_tag":"Brand new description"}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/products/632910392.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const product = new admin.rest.resources.Product({session: session});

        product.id = 632910392;
        product.metafields_global_title_tag = "Brand new title";
        product.metafields_global_description_tag = "Brand new description";
        await product.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        product = ShopifyAPI::Product.new(session: test_session)
        product.id = 632910392
        product.metafields_global_title_tag = "Brand new title"
        product.metafields_global_description_tag = "Brand new description"
        product.save!

#####

        // Session is built by the OAuth process

        const product = new shopify.rest.Product({session: session});
        product.id = 632910392;
        product.metafields_global_title_tag = "Brand new title";
        product.metafields_global_description_tag = "Brand new description";
        await product.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"product":{"id":632910392,"title":"IPod Nano - 8GB","body_html":"<p>It's the small iPod with one very big idea: Video. Now the world's most popular music player, available in 4GB and 8GB models, lets you enjoy TV shows, movies, video podcasts, and more. The larger, brighter display means amazing picture quality. In six eye-catching colors, iPod nano is stunning all around. And with models starting at just $149, little speaks volumes.</p>","vendor":"Apple","product_type":"Cult Products","created_at":"2026-01-09T19:38:20-05:00","handle":"ipod-nano","updated_at":"2026-01-09T19:38:20-05:00","published_at":"2007-12-31T19:00:00-05:00","template_suffix":null,"published_scope":"web","tags":"Emotive, Flash Memory, MP3, Music","status":"active","admin_graphql_api_id":"gid://shopify/Product/632910392","variants":[{"id":808950810,"product_id":632910392,"title":"Pink","price":"199.00","position":1,"inventory_policy":"continue","compare_at_price":null,"option1":"Pink","option2":null,"option3":null,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","taxable":true,"barcode":"1234_pink","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008PINK","weight":1.25,"weight_unit":"lb","inventory_item_id":808950810,"inventory_quantity":10,"old_inventory_quantity":10,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/808950810","image_id":562641783},{"id":49148385,"product_id":632910392,"title":"Red","price":"199.00","position":2,"inventory_policy":"continue","compare_at_price":null,"option1":"Red","option2":null,"option3":null,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","taxable":true,"barcode":"1234_red","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008RED","weight":1.25,"weight_unit":"lb","inventory_item_id":49148385,"inventory_quantity":20,"old_inventory_quantity":20,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/49148385","image_id":null},{"id":39072856,"product_id":632910392,"title":"Green","price":"199.00","position":3,"inventory_policy":"continue","compare_at_price":null,"option1":"Green","option2":null,"option3":null,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","taxable":true,"barcode":"1234_green","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008GREEN","weight":1.25,"weight_unit":"lb","inventory_item_id":39072856,"inventory_quantity":30,"old_inventory_quantity":30,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/39072856","image_id":null},{"id":457924702,"product_id":632910392,"title":"Black","price":"199.00","position":4,"inventory_policy":"continue","compare_at_price":null,"option1":"Black","option2":null,"option3":null,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","taxable":true,"barcode":"1234_black","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008BLACK","weight":1.25,"weight_unit":"lb","inventory_item_id":457924702,"inventory_quantity":40,"old_inventory_quantity":40,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/457924702","image_id":null}],"options":[{"id":594680422,"product_id":632910392,"name":"Color","position":1,"values":["Pink","Red","Green","Black"]}],"images":[{"id":850703190,"alt":null,"position":1,"product_id":632910392,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/498048120","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano.png?v=1768005500","variant_ids":[]},{"id":562641783,"alt":null,"position":2,"product_id":632910392,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/1071517486","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano-2.png?v=1768005500","variant_ids":[808950810]},{"id":378407906,"alt":null,"position":3,"product_id":632910392,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/220090436","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano.png?v=1768005500","variant_ids":[]}],"image":{"id":850703190,"alt":null,"position":1,"product_id":632910392,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/498048120","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano.png?v=1768005500","variant_ids":[]}}}

  * #### Update a product's status

#####

        curl -d '{"product":{"id":632910392,"status":"draft"}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/products/632910392.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const product = new admin.rest.resources.Product({session: session});

        product.id = 632910392;
        product.status = "draft";
        await product.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        product = ShopifyAPI::Product.new(session: test_session)
        product.id = 632910392
        product.status = "draft"
        product.save!

#####

        // Session is built by the OAuth process

        const product = new shopify.rest.Product({session: session});
        product.id = 632910392;
        product.status = "draft";
        await product.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"product":{"id":632910392,"title":"IPod Nano - 8GB","body_html":"<p>It's the small iPod with one very big idea: Video. Now the world's most popular music player, available in 4GB and 8GB models, lets you enjoy TV shows, movies, video podcasts, and more. The larger, brighter display means amazing picture quality. In six eye-catching colors, iPod nano is stunning all around. And with models starting at just $149, little speaks volumes.</p>","vendor":"Apple","product_type":"Cult Products","created_at":"2026-01-09T19:38:20-05:00","handle":"ipod-nano","updated_at":"2026-01-09T19:40:22-05:00","published_at":null,"template_suffix":null,"published_scope":"web","tags":"Emotive, Flash Memory, MP3, Music","status":"draft","admin_graphql_api_id":"gid://shopify/Product/632910392","variants":[{"id":808950810,"product_id":632910392,"title":"Pink","price":"199.00","position":1,"inventory_policy":"continue","compare_at_price":null,"option1":"Pink","option2":null,"option3":null,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","taxable":true,"barcode":"1234_pink","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008PINK","weight":1.25,"weight_unit":"lb","inventory_item_id":808950810,"inventory_quantity":10,"old_inventory_quantity":10,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/808950810","image_id":562641783},{"id":49148385,"product_id":632910392,"title":"Red","price":"199.00","position":2,"inventory_policy":"continue","compare_at_price":null,"option1":"Red","option2":null,"option3":null,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","taxable":true,"barcode":"1234_red","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008RED","weight":1.25,"weight_unit":"lb","inventory_item_id":49148385,"inventory_quantity":20,"old_inventory_quantity":20,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/49148385","image_id":null},{"id":39072856,"product_id":632910392,"title":"Green","price":"199.00","position":3,"inventory_policy":"continue","compare_at_price":null,"option1":"Green","option2":null,"option3":null,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","taxable":true,"barcode":"1234_green","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008GREEN","weight":1.25,"weight_unit":"lb","inventory_item_id":39072856,"inventory_quantity":30,"old_inventory_quantity":30,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/39072856","image_id":null},{"id":457924702,"product_id":632910392,"title":"Black","price":"199.00","position":4,"inventory_policy":"continue","compare_at_price":null,"option1":"Black","option2":null,"option3":null,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","taxable":true,"barcode":"1234_black","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008BLACK","weight":1.25,"weight_unit":"lb","inventory_item_id":457924702,"inventory_quantity":40,"old_inventory_quantity":40,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/457924702","image_id":null}],"options":[{"id":594680422,"product_id":632910392,"name":"Color","position":1,"values":["Pink","Red","Green","Black"]}],"images":[{"id":850703190,"alt":null,"position":1,"product_id":632910392,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/498048120","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano.png?v=1768005500","variant_ids":[]},{"id":562641783,"alt":null,"position":2,"product_id":632910392,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/1071517486","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano-2.png?v=1768005500","variant_ids":[808950810]},{"id":378407906,"alt":null,"position":3,"product_id":632910392,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/220090436","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano.png?v=1768005500","variant_ids":[]}],"image":{"id":850703190,"alt":null,"position":1,"product_id":632910392,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/498048120","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano.png?v=1768005500","variant_ids":[]}}}

  * #### Update a product's tags

#####

        curl -d '{"product":{"id":632910392,"tags":"Barnes & Noble, John's Fav"}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/products/632910392.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const product = new admin.rest.resources.Product({session: session});

        product.id = 632910392;
        product.tags = "Barnes & Noble, John's Fav";
        await product.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        product = ShopifyAPI::Product.new(session: test_session)
        product.id = 632910392
        product.tags = "Barnes & Noble, John's Fav"
        product.save!

#####

        // Session is built by the OAuth process

        const product = new shopify.rest.Product({session: session});
        product.id = 632910392;
        product.tags = "Barnes & Noble, John's Fav";
        await product.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"product":{"id":632910392,"title":"IPod Nano - 8GB","body_html":"<p>It's the small iPod with one very big idea: Video. Now the world's most popular music player, available in 4GB and 8GB models, lets you enjoy TV shows, movies, video podcasts, and more. The larger, brighter display means amazing picture quality. In six eye-catching colors, iPod nano is stunning all around. And with models starting at just $149, little speaks volumes.</p>","vendor":"Apple","product_type":"Cult Products","created_at":"2026-01-09T19:38:20-05:00","handle":"ipod-nano","updated_at":"2026-01-09T19:40:11-05:00","published_at":"2007-12-31T19:00:00-05:00","template_suffix":null,"published_scope":"web","tags":"Barnes & Noble, John's Fav","status":"active","admin_graphql_api_id":"gid://shopify/Product/632910392","variants":[{"id":808950810,"product_id":632910392,"title":"Pink","price":"199.00","position":1,"inventory_policy":"continue","compare_at_price":null,"option1":"Pink","option2":null,"option3":null,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","taxable":true,"barcode":"1234_pink","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008PINK","weight":1.25,"weight_unit":"lb","inventory_item_id":808950810,"inventory_quantity":10,"old_inventory_quantity":10,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/808950810","image_id":562641783},{"id":49148385,"product_id":632910392,"title":"Red","price":"199.00","position":2,"inventory_policy":"continue","compare_at_price":null,"option1":"Red","option2":null,"option3":null,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","taxable":true,"barcode":"1234_red","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008RED","weight":1.25,"weight_unit":"lb","inventory_item_id":49148385,"inventory_quantity":20,"old_inventory_quantity":20,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/49148385","image_id":null},{"id":39072856,"product_id":632910392,"title":"Green","price":"199.00","position":3,"inventory_policy":"continue","compare_at_price":null,"option1":"Green","option2":null,"option3":null,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","taxable":true,"barcode":"1234_green","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008GREEN","weight":1.25,"weight_unit":"lb","inventory_item_id":39072856,"inventory_quantity":30,"old_inventory_quantity":30,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/39072856","image_id":null},{"id":457924702,"product_id":632910392,"title":"Black","price":"199.00","position":4,"inventory_policy":"continue","compare_at_price":null,"option1":"Black","option2":null,"option3":null,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","taxable":true,"barcode":"1234_black","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008BLACK","weight":1.25,"weight_unit":"lb","inventory_item_id":457924702,"inventory_quantity":40,"old_inventory_quantity":40,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/457924702","image_id":null}],"options":[{"id":594680422,"product_id":632910392,"name":"Color","position":1,"values":["Pink","Red","Green","Black"]}],"images":[{"id":850703190,"alt":null,"position":1,"product_id":632910392,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/498048120","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano.png?v=1768005500","variant_ids":[]},{"id":562641783,"alt":null,"position":2,"product_id":632910392,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/1071517486","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano-2.png?v=1768005500","variant_ids":[808950810]},{"id":378407906,"alt":null,"position":3,"product_id":632910392,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/220090436","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano.png?v=1768005500","variant_ids":[]}],"image":{"id":850703190,"alt":null,"position":1,"product_id":632910392,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/498048120","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano.png?v=1768005500","variant_ids":[]}}}

  * #### Update a product's title

#####

        curl -d '{"product":{"id":632910392,"title":"New product title"}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/products/632910392.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const product = new admin.rest.resources.Product({session: session});

        product.id = 632910392;
        product.title = "New product title";
        await product.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        product = ShopifyAPI::Product.new(session: test_session)
        product.id = 632910392
        product.title = "New product title"
        product.save!

#####

        // Session is built by the OAuth process

        const product = new shopify.rest.Product({session: session});
        product.id = 632910392;
        product.title = "New product title";
        await product.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"product":{"id":632910392,"title":"New product title","body_html":"<p>It's the small iPod with one very big idea: Video. Now the world's most popular music player, available in 4GB and 8GB models, lets you enjoy TV shows, movies, video podcasts, and more. The larger, brighter display means amazing picture quality. In six eye-catching colors, iPod nano is stunning all around. And with models starting at just $149, little speaks volumes.</p>","vendor":"Apple","product_type":"Cult Products","created_at":"2026-01-09T19:38:20-05:00","handle":"ipod-nano","updated_at":"2026-01-09T19:39:04-05:00","published_at":"2007-12-31T19:00:00-05:00","template_suffix":null,"published_scope":"web","tags":"Emotive, Flash Memory, MP3, Music","status":"active","admin_graphql_api_id":"gid://shopify/Product/632910392","variants":[{"id":808950810,"product_id":632910392,"title":"Pink","price":"199.00","position":1,"inventory_policy":"continue","compare_at_price":null,"option1":"Pink","option2":null,"option3":null,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","taxable":true,"barcode":"1234_pink","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008PINK","weight":1.25,"weight_unit":"lb","inventory_item_id":808950810,"inventory_quantity":10,"old_inventory_quantity":10,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/808950810","image_id":562641783},{"id":49148385,"product_id":632910392,"title":"Red","price":"199.00","position":2,"inventory_policy":"continue","compare_at_price":null,"option1":"Red","option2":null,"option3":null,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","taxable":true,"barcode":"1234_red","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008RED","weight":1.25,"weight_unit":"lb","inventory_item_id":49148385,"inventory_quantity":20,"old_inventory_quantity":20,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/49148385","image_id":null},{"id":39072856,"product_id":632910392,"title":"Green","price":"199.00","position":3,"inventory_policy":"continue","compare_at_price":null,"option1":"Green","option2":null,"option3":null,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","taxable":true,"barcode":"1234_green","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008GREEN","weight":1.25,"weight_unit":"lb","inventory_item_id":39072856,"inventory_quantity":30,"old_inventory_quantity":30,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/39072856","image_id":null},{"id":457924702,"product_id":632910392,"title":"Black","price":"199.00","position":4,"inventory_policy":"continue","compare_at_price":null,"option1":"Black","option2":null,"option3":null,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","taxable":true,"barcode":"1234_black","fulfillment_service":"manual","grams":567,"inventory_management":"shopify","requires_shipping":true,"sku":"IPOD2008BLACK","weight":1.25,"weight_unit":"lb","inventory_item_id":457924702,"inventory_quantity":40,"old_inventory_quantity":40,"presentment_prices":[{"price":{"amount":"199.00","currency_code":"USD"},"compare_at_price":null}],"admin_graphql_api_id":"gid://shopify/ProductVariant/457924702","image_id":null}],"options":[{"id":594680422,"product_id":632910392,"name":"Color","position":1,"values":["Pink","Red","Green","Black"]}],"images":[{"id":850703190,"alt":null,"position":1,"product_id":632910392,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/498048120","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano.png?v=1768005500","variant_ids":[]},{"id":562641783,"alt":null,"position":2,"product_id":632910392,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/1071517486","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano-2.png?v=1768005500","variant_ids":[808950810]},{"id":378407906,"alt":null,"position":3,"product_id":632910392,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/220090436","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano.png?v=1768005500","variant_ids":[]}],"image":{"id":850703190,"alt":null,"position":1,"product_id":632910392,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/498048120","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano.png?v=1768005500","variant_ids":[]}}}


* * *

##

[Anchor to DELETE request, Delete a product](/docs/api/admin-rest/latest/resources/product#delete-products-product-id)

del

Delete a product

[productDelete](/docs/api/admin-graphql/latest/mutations/productDelete?example=delete-a-product)

Deletes a product.

###

[Anchor to Parameters of Delete a product](/docs/api/admin-rest/latest/resources/product#delete-products-product-id-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

product_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to delete-products-product-id-examples](/docs/api/admin-rest/latest/resources/product#delete-products-product-id-examples)Examples

Delete a product along with all its variants and images

Path parameters

product_id=632910392

string**string**

required**required**

Was this section helpful?

YesNo

del

## /admin/api/2026-01/products/632910392.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X DELETE "https://your-development-store.myshopify.com/admin/api/2026-01/products/632910392.json" \

-H "X-Shopify-Access-Token: {access_token}"

{}

## Response

JSON

9

1

2

HTTP/1.1 200 OK

{}

### examples

  * #### Delete a product along with all its variants and images

#####

        curl -X DELETE "https://your-development-store.myshopify.com/admin/api/2026-01/products/632910392.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Product.delete({
          session: session,
          id: 632910392,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Product.delete(
          session: test_session,
          id: 632910392,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Product.delete({
          session: session,
          id: 632910392,
        });

#### response

        HTTP/1.1 200 OK{}