# Collection

*Source: https://shopify.dev/docs/api/admin-rest/2026-01/resources/collection*

---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04

2026-01latest

# Collection

Ask assistant

Requires `products` access scope.

**Requires `products` access scope.:**

A collection is a grouping of products that merchants can create to make their stores easier to browse. For example, a merchant might create a collection for a specific type of product that they sell, such as **Footwear**. Merchants can create collections by selecting products individually or by defining rules that automatically determine whether products are included.

Shopify stores start with a single collection, called **Frontpage**. This is a collection of products that are shown on the front page of the online store.

There are two different types of collection:

  * **Custom collections** , which contain products that are manually added to a collection by a merchant. For more information, see the [CustomCollection](/docs/admin-api/rest/reference/products/customcollection) resource.
  * **Smart collections** , which contain products that are automatically added based on selection conditions that a merchant chooses. For more information, see the [SmartCollection](/docs/admin-api/rest/reference/products/smartcollection) resource.


The [Collect](/docs/admin-api/rest/reference/products/collect) resource is used to connect a product to a [custom collection](/docs/admin-api/rest/reference/products/customcollection).

Was this section helpful?

YesNo

#

## Endpoints

  * [get/admin/api/latest/collections/{collection_id}.json](/docs/api/admin-rest/latest/resources/collection#get-collections-collection-id)

Retrieves a single collection

[collection](/docs/api/admin-graphql/latest/queries/collection)

  * [get/admin/api/latest/collections/{collection_id}/products.json](/docs/api/admin-rest/latest/resources/collection#get-collections-collection-id-products)

Retrieve a list of products belonging to a collection

[collection](/docs/api/admin-graphql/latest/queries/collection)


* * *

[Anchor to ](/docs/api/admin-rest/latest/resources/collection#resource-object)

## The Collection resource

[Anchor to ](/docs/api/admin-rest/latest/resources/collection#resource-object-properties)

### Properties

* * *

body_html

->[descriptionHtml](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.descriptionHtml)

A description of the collection, complete with HTML markup. Many templates display this on their collection pages.

* * *

handle

->[handle](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.handle)

A unique, human-readable string for the collection automatically generated from its title. This is used in themes by the Liquid templating language to refer to the collection. (count: 255 characters)

* * *

image

->[image](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.image)

Image associated with the collection. Valid values are:

Show image properties

  * **attachment** : An image attached to a collection returned as Base64-encoded binary data.
  * **src** : The source URL that specifies the location of the image.
  * **alt** : The alternative text that describes the collection image.
  * **created_at** : The time and date ([ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format) when the image was added to the collection.
  * **width** : The width of the image in pixels.
  * **height** : The height of the image in pixels.


* * *

id

read-only**read-only**

->[id](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.id)

The ID for the collection.

* * *

published_at

read-only**read-only**

->[publishDate](/docs/api/admin-graphql/latest/objects/ResourcePublication#field-ResourcePublication.fields.publishDate)

The time and date ([ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format) when the collection was made visible. Returns `null` for a hidden collection.

* * *

published_scope

read-only**read-only**

->[publishable](/docs/api/admin-graphql/latest/objects/ResourcePublication#field-ResourcePublication.fields.publishable)

Whether the collection is published to the Point of Sale channel. Valid values:

Show published_scope properties

  * `web`: The collection is published to the Online Store channel but not published to the Point of Sale channel.
  * `global`: The collection is published to both the Online Store channel and the Point of Sale channel.


* * *

sort_order

->[sortOrder](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.sortOrder)

The order in which products in the collection appear. Valid values:

Show sort_order properties

  * **alpha-asc** : Alphabetically, in ascending order (A - Z).
  * **alpha-desc** : Alphabetically, in descending order (Z - A).
  * **best-selling** : By best-selling products.
  * **created** : By date created, in ascending order (oldest - newest).
  * **created-desc** : By date created, in descending order (newest - oldest).
  * **manual** : In the order set manually by the shop owner.
  * **price-asc** : By price, in ascending order (lowest - highest).
  * **price-desc** : By price, in descending order (highest - lowest).


* * *

template_suffix

->[templateSuffix](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.templateSuffix)

The suffix of the liquid template being used. For example, if the value is `custom`, then the collection is using the `collection.custom.liquid` template. If the value is `null`, then the collection is using the default `collection.liquid`.

* * *

title

->[title](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.title)

The name of the collection. (count: 255 characters)

* * *

updated_at

read-only**read-only**

->[updatedAt](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.updatedAt)

The date and time ([ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format) when the collection was last modified.

* * *

Was this section helpful?

YesNo

{}

## The Collection resource

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

{

"body_html": "<p>The best selling iPods ever</p>",

"handle": "ipods",

"image": {

"src": "http://static.shopify.com/collections/ipod.jpg?0",

"alt": "iPods",

"width": 500,

"height": 488,

"created_at": "2018-04-19T09:34:47-04:00"

},

"id": 841564295,

"published_at": "2008-02-01T19:00:00-05:00",

"published_scope": "global",

"sort_order": "manual",

"template_suffix": "custom",

"title": "IPods",

"updated_at": "2008-02-01T19:00:00-05:00"

}

* * *

##

[Anchor to GET request, Retrieves a single collection](/docs/api/admin-rest/latest/resources/collection#get-collections-collection-id)

get

Retrieves a single collection

[collection](/docs/api/admin-graphql/latest/queries/collection)

Retrieves a single collection

###

[Anchor to Parameters of Retrieves a single collection](/docs/api/admin-rest/latest/resources/collection#get-collections-collection-id-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

collection_id

string**string**

required**required**

* * *

fields

Show only certain fields, specified by a comma-separated list of field names.

* * *

Was this section helpful?

YesNo

###

[Anchor to get-collections-collection-id-examples](/docs/api/admin-rest/latest/resources/collection#get-collections-collection-id-examples)Examples

Retrieve a specific collection by its ID

Path parameters

collection_id=841564295

string**string**

required**required**

Was this section helpful?

YesNo

get

## /admin/api/2026-01/collections/841564295.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/collections/841564295.json" \

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

HTTP/1.1 200 OK

{

"collection": {

"id": 841564295,

"handle": "ipods",

"title": "IPods",

"updated_at": "2008-02-01T19:00:00-05:00",

"body_html": "<p>The best selling ipod ever</p>",

"published_at": "2008-02-01T19:00:00-05:00",

"sort_order": "manual",

"template_suffix": null,

"products_count": 1,

"collection_type": "custom",

"published_scope": "web",

"admin_graphql_api_id": "gid://shopify/Collection/841564295",

"image": {

"created_at": "2026-01-09T17:04:11-05:00",

"alt": "MP3 Player 8gb",

"width": 123,

"height": 456,

"src": "https://cdn.shopify.com/s/files/1/0005/4838/0009/collections/ipod_nano_8gb.jpg?v=1767996251"

}

}

}

### examples

  * #### Retrieve a specific collection by its ID

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/collections/841564295.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Collection.find({
          session: session,
          id: 841564295,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Collection.find(
          session: test_session,
          id: 841564295,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Collection.find({
          session: session,
          id: 841564295,
        });

#### response

        HTTP/1.1 200 OK{"collection":{"id":841564295,"handle":"ipods","title":"IPods","updated_at":"2008-02-01T19:00:00-05:00","body_html":"<p>The best selling ipod ever</p>","published_at":"2008-02-01T19:00:00-05:00","sort_order":"manual","template_suffix":null,"products_count":1,"collection_type":"custom","published_scope":"web","admin_graphql_api_id":"gid://shopify/Collection/841564295","image":{"created_at":"2026-01-09T17:04:11-05:00","alt":"MP3 Player 8gb","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/collections/ipod_nano_8gb.jpg?v=1767996251"}}}


* * *

##

[Anchor to GET request, Retrieve a list of products belonging to a collection](/docs/api/admin-rest/latest/resources/collection#get-collections-collection-id-products)

get

Retrieve a list of products belonging to a collection

[collection](/docs/api/admin-graphql/latest/queries/collection)

Retrieve a list of products belonging to a collection. **Note:** This endpoint implements pagination by using links that are provided in the response header. To learn more, refer to [Make paginated requests to the REST Admin API](/api/usage/pagination-rest).. The products returned are sorted by the collection's sort order.

###

[Anchor to Parameters of Retrieve a list of products belonging to a collection](/docs/api/admin-rest/latest/resources/collection#get-collections-collection-id-products-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

collection_id

string**string**

required**required**

* * *

count

≤ 250**≤ 250**

default 50**default 50**

The number of products to retrieve.

* * *

Was this section helpful?

YesNo

###

[Anchor to get-collections-collection-id-products-examples](/docs/api/admin-rest/latest/resources/collection#get-collections-collection-id-products-examples)Examples

Retrieve a list of products belonging to a collection

Path parameters

collection_id=841564295

string**string**

required**required**

Was this section helpful?

YesNo

get

## /admin/api/2026-01/collections/841564295/products.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/collections/841564295/products.json" \

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

72

73

74

75

76

77

78

79

HTTP/1.1 200 OK

{

"products": [

{

"id": 632910392,

"title": "IPod Nano - 8GB",

"body_html": "<p>It's the small iPod with one very big idea: Video. Now the world's most popular music player, available in 4GB and 8GB models, lets you enjoy TV shows, movies, video podcasts, and more. The larger, brighter display means amazing picture quality. In six eye-catching colors, iPod nano is stunning all around. And with models starting at just $149, little speaks volumes.</p>",

"vendor": "Apple",

"product_type": "Cult Products",

"created_at": "2026-01-09T17:04:11-05:00",

"handle": "ipod-nano",

"updated_at": "2026-01-09T17:04:11-05:00",

"published_at": "2007-12-31T19:00:00-05:00",

"template_suffix": null,

"published_scope": "web",

"tags": "Emotive, Flash Memory, MP3, Music",

"status": "active",

"admin_graphql_api_id": "gid://shopify/Product/632910392",

"options": [

{

"id": 594680422,

"product_id": 632910392,

"name": "Color",

"position": 1

}

],

"images": [

{

"id": 850703190,

"alt": null,

"position": 1,

"product_id": 632910392,

"created_at": "2026-01-09T17:04:11-05:00",

"updated_at": "2026-01-09T17:04:11-05:00",

"admin_graphql_api_id": "gid://shopify/MediaImage/498048120",

"width": 123,

"height": 456,

"src": "https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano.png?v=1767996251"

},

{

"id": 562641783,

"alt": null,

"position": 2,

"product_id": 632910392,

"created_at": "2026-01-09T17:04:11-05:00",

"updated_at": "2026-01-09T17:04:11-05:00",

"admin_graphql_api_id": "gid://shopify/MediaImage/1071517486",

"width": 123,

"height": 456,

"src": "https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano-2.png?v=1767996251"

},

{

"id": 378407906,

"alt": null,

"position": 3,

"product_id": 632910392,

"created_at": "2026-01-09T17:04:11-05:00",

"updated_at": "2026-01-09T17:04:11-05:00",

"admin_graphql_api_id": "gid://shopify/MediaImage/220090436",

"width": 123,

"height": 456,

"src": "https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano.png?v=1767996251"

}

],

"image": {

"id": 850703190,

"alt": null,

"position": 1,

"product_id": 632910392,

"created_at": "2026-01-09T17:04:11-05:00",

"updated_at": "2026-01-09T17:04:11-05:00",

"admin_graphql_api_id": "gid://shopify/MediaImage/498048120",

"width": 123,

"height": 456,

"src": "https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano.png?v=1767996251"

}

}

]

}

### examples

  * #### Retrieve a list of products belonging to a collection

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/collections/841564295/products.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Collection.products({
          session: session,
          id: 841564295,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Collection.products(
          session: test_session,
          id: 841564295,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Collection.products({
          session: session,
          id: 841564295,
        });

#### response

        HTTP/1.1 200 OK{"products":[{"id":632910392,"title":"IPod Nano - 8GB","body_html":"<p>It's the small iPod with one very big idea: Video. Now the world's most popular music player, available in 4GB and 8GB models, lets you enjoy TV shows, movies, video podcasts, and more. The larger, brighter display means amazing picture quality. In six eye-catching colors, iPod nano is stunning all around. And with models starting at just $149, little speaks volumes.</p>","vendor":"Apple","product_type":"Cult Products","created_at":"2026-01-09T17:04:11-05:00","handle":"ipod-nano","updated_at":"2026-01-09T17:04:11-05:00","published_at":"2007-12-31T19:00:00-05:00","template_suffix":null,"published_scope":"web","tags":"Emotive, Flash Memory, MP3, Music","status":"active","admin_graphql_api_id":"gid://shopify/Product/632910392","options":[{"id":594680422,"product_id":632910392,"name":"Color","position":1}],"images":[{"id":850703190,"alt":null,"position":1,"product_id":632910392,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/498048120","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano.png?v=1767996251"},{"id":562641783,"alt":null,"position":2,"product_id":632910392,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/1071517486","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano-2.png?v=1767996251"},{"id":378407906,"alt":null,"position":3,"product_id":632910392,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/220090436","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano.png?v=1767996251"}],"image":{"id":850703190,"alt":null,"position":1,"product_id":632910392,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","admin_graphql_api_id":"gid://shopify/MediaImage/498048120","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/products/ipod-nano.png?v=1767996251"}}]}