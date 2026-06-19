# Collect

*Source: https://shopify.dev/docs/api/admin-rest/2026-01/resources/collect*

---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04

2026-01latest

# Collect

Ask assistant

Requires `products` access scope.

**Requires `products` access scope.:**

The Collect resource connects a product to a custom collection.

Collects are meant for managing the relationship between products and custom collections. For every product in a custom collection there is a collect that tracks the ID of both the product and the custom collection. A product can be in more than one collection, and will have a collect connecting it to each collection. Unlike many Shopify resources, collects aren't apparent to store owners.

Collects are for placing products in custom collections only. [Smart collections](/docs/admin-api/rest/reference/products/smartcollection) use rules to determine which products are their members. Creating a collect that links a product to a smart collection results in a **403 Forbidden** error.

For more information on custom collections, see the [CustomCollection](/docs/admin-api/rest/reference/products/customcollection) resource.

Was this section helpful?

YesNo

#

## Endpoints

  * [post/admin/api/latest/collects.json](/docs/api/admin-rest/latest/resources/collect#post-collects)

Adds a product to a custom collection

[collectionAddProducts](/docs/api/admin-graphql/latest/mutations/collectionAddProducts?example=adds-a-product-to-a-custom-collection)

  * [get/admin/api/latest/collects.json](/docs/api/admin-rest/latest/resources/collect#get-collects)

Retrieves a list of collects

[collection](/docs/api/admin-graphql/latest/queries/collection)

[product](/docs/api/admin-graphql/latest/queries/product)

  * [get/admin/api/latest/collects/{collect_id}.json](/docs/api/admin-rest/latest/resources/collect#get-collects-collect-id)

Retrieves a specific collect by its ID

deprecated

**

deprecated

**

  * [ get/admin/api/latest/collects/count.json](/docs/api/admin-rest/latest/resources/collect#get-collects-count)

Retrieves a count of collects

[collection](/docs/api/admin-graphql/latest/queries/collection)

  * [del/admin/api/latest/collects/{collect_id}.json](/docs/api/admin-rest/latest/resources/collect#delete-collects-collect-id)

Removes a product from a collection

[collectionRemoveProducts](/docs/api/admin-graphql/latest/mutations/collectionRemoveProducts?example=removes-a-product-from-a-collection)


* * *

[Anchor to ](/docs/api/admin-rest/latest/resources/collect#resource-object)

## The Collect resource

[Anchor to ](/docs/api/admin-rest/latest/resources/collect#resource-object-properties)

### Properties

* * *

collection_id

deprecated**deprecated**

The ID of the custom collection containing the product.

* * *

created_at

deprecated**deprecated**

The date and time ([ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format) when the collect was created.

* * *

id

deprecated**deprecated**

A unique numeric identifier for the collect.

* * *

position

deprecated**deprecated**

The position of this product in a manually sorted custom collection. The positions are not guaranteed to be consecutive. This value is applied only when the custom collection is sorted manually.

* * *

product_id

deprecated**deprecated**

The unique numeric identifier for the product in the custom collection.

* * *

sort_value

deprecated**deprecated**

This is the same value as `position` but padded with leading zeroes to make it alphanumeric-sortable. This value is applied only when the custom collection is sorted manually.

* * *

updated_at

deprecated**deprecated**

The date and time ([ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format) when the collect was last updated.

* * *

Was this section helpful?

YesNo

{}

## The Collect resource

9

1

2

3

4

5

6

7

8

9

{

"collection_id": 841564295,

"created_at": "2018-04-25T13:51:12-04:00",

"id": 841564295,

"position": 2,

"product_id": 632910392,

"sort_value": "0000000002",

"updated_at": "2018-04-25T13:51:12-04:00"

}

* * *

##

[Anchor to POST request, Adds a product to a custom collection](/docs/api/admin-rest/latest/resources/collect#post-collects)

post

Adds a product to a custom collection

[collectionAddProducts](/docs/api/admin-graphql/latest/mutations/collectionAddProducts?example=adds-a-product-to-a-custom-collection)

Adds a product to a custom collection.

###

[Anchor to Parameters of Adds a product to a custom collection](/docs/api/admin-rest/latest/resources/collect#post-collects-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to post-collects-examples](/docs/api/admin-rest/latest/resources/collect#post-collects-examples)Examples

Create a new link between an existing product and an existing collection

Request body

collect

Collect resource**Collect resource**

Show collect properties

collect.product_id:921728736

deprecated**deprecated**

The unique numeric identifier for the product in the custom collection.

collect.collection_id:841564295

deprecated**deprecated**

The ID of the custom collection containing the product.

Creating a collect without a product or collection ID fails and returns an error

Was this section helpful?

YesNo

post

## /admin/api/2026-01/collects.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{"collect":{"product_id":921728736,"collection_id":841564295}}' \

-X POST "https://your-development-store.myshopify.com/admin/api/2026-01/collects.json" \

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

HTTP/1.1 201 Created

{

"collect": {

"id": 1071559583,

"collection_id": 841564295,

"product_id": 921728736,

"created_at": "2026-01-09T19:34:10-05:00",

"updated_at": "2026-01-09T19:34:10-05:00",

"position": 1044982312524966,

"sort_value": "1044982312524966"

}

}

### examples

  * #### Create a new link between an existing product and an existing collection

#####

        curl -d '{"collect":{"product_id":921728736,"collection_id":841564295}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/collects.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const collect = new admin.rest.resources.Collect({session: session});

        collect.product_id = 921728736;
        collect.collection_id = 841564295;
        await collect.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        collect = ShopifyAPI::Collect.new(session: test_session)
        collect.product_id = 921728736
        collect.collection_id = 841564295
        collect.save!

#####

        // Session is built by the OAuth process

        const collect = new shopify.rest.Collect({session: session});
        collect.product_id = 921728736;
        collect.collection_id = 841564295;
        await collect.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"collect":{"id":1071559583,"collection_id":841564295,"product_id":921728736,"created_at":"2026-01-09T19:34:10-05:00","updated_at":"2026-01-09T19:34:10-05:00","position":1044982312524966,"sort_value":"1044982312524966"}}

  * #### Creating a collect without a product or collection ID fails and returns an error

#####

        curl -d '{"collect":{"body":"foobar"}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/collects.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const collect = new admin.rest.resources.Collect({session: session});

        collect.body = "foobar";
        await collect.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        collect = ShopifyAPI::Collect.new(session: test_session)
        collect.body = "foobar"
        collect.save!

#####

        // Session is built by the OAuth process

        const collect = new shopify.rest.Collect({session: session});
        collect.body = "foobar";
        await collect.save({
          update: true,
        });

#### response

        HTTP/1.1 422 Unprocessable Entity{"errors":{"product":["can't be blank"],"collection":["can't be blank"],"product_id":["must belong to John Smith Test Store"],"collection_id":["must belong to John Smith Test Store"]}}


* * *

##

[Anchor to GET request, Retrieves a list of collects](/docs/api/admin-rest/latest/resources/collect#get-collects)

get

Retrieves a list of collects

[collection](/docs/api/admin-graphql/latest/queries/collection)

[product](/docs/api/admin-graphql/latest/queries/product)

Retrieves a list of collects. **Note:** This endpoint implements pagination by using links that are provided in the response header. To learn more, refer to [Make paginated requests to the REST Admin API](/api/usage/pagination-rest).

###

[Anchor to Parameters of Retrieves a list of collects](/docs/api/admin-rest/latest/resources/collect#get-collects-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

fields

Show only certain fields, specified by a comma-separated list of field names.

* * *

count

≤ 250**≤ 250**

default 50**default 50**

The maximum number of results to show.

* * *

after_id

Restrict results to after the specified ID.

* * *

Was this section helpful?

YesNo

###

[Anchor to get-collects-examples](/docs/api/admin-rest/latest/resources/collect#get-collects-examples)Examples

Retrieve all collects for the shop

Retrieve only collects for a certain collection

Query parameters

collection_id=841564295

The ID of the custom collection containing the product.

Retrieve only collects for a certain product

Query parameters

product_id=632910392

The unique numeric identifier for the product in the custom collection.

Was this section helpful?

YesNo

get

## /admin/api/2026-01/collects.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/collects.json" \

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

HTTP/1.1 200 OK

{

"collects": [

{

"id": 455204334,

"collection_id": 841564295,

"product_id": 632910392,

"created_at": null,

"updated_at": null,

"position": 1044616696680960,

"sort_value": "1044616696680960"

},

{

"id": 773559378,

"collection_id": 395646240,

"product_id": 632910392,

"created_at": null,

"updated_at": null,

"position": 1044616696680960,

"sort_value": "1044616696680960"

}

]

}

### examples

  * #### Retrieve all collects for the shop

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/collects.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Collect.all({
          session: session,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Collect.all(
          session: test_session,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Collect.all({
          session: session,
        });

#### response

        HTTP/1.1 200 OK{"collects":[{"id":455204334,"collection_id":841564295,"product_id":632910392,"created_at":null,"updated_at":null,"position":1044616696680960,"sort_value":"1044616696680960"},{"id":773559378,"collection_id":395646240,"product_id":632910392,"created_at":null,"updated_at":null,"position":1044616696680960,"sort_value":"1044616696680960"}]}

  * #### Retrieve only collects for a certain collection

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/collects.json?collection_id=841564295" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Collect.all({
          session: session,
          collection_id: "841564295",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Collect.all(
          session: test_session,
          collection_id: "841564295",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Collect.all({
          session: session,
          collection_id: "841564295",
        });

#### response

        HTTP/1.1 200 OK{"collects":[{"id":455204334,"collection_id":841564295,"product_id":632910392,"created_at":null,"updated_at":null,"position":1044616696680960,"sort_value":"1044616696680960"},{"id":1071559581,"collection_id":841564295,"product_id":921728736,"created_at":"2026-01-09T19:33:55-05:00","updated_at":"2026-01-09T19:33:55-05:00","position":1044982312524966,"sort_value":"1044982312524966"}]}

  * #### Retrieve only collects for a certain product

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/collects.json?product_id=632910392" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Collect.all({
          session: session,
          product_id: "632910392",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Collect.all(
          session: test_session,
          product_id: "632910392",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Collect.all({
          session: session,
          product_id: "632910392",
        });

#### response

        HTTP/1.1 200 OK{"collects":[{"id":455204334,"collection_id":841564295,"product_id":632910392,"created_at":null,"updated_at":null,"position":1044616696680960,"sort_value":"1044616696680960"},{"id":773559378,"collection_id":395646240,"product_id":632910392,"created_at":null,"updated_at":null,"position":1044616696680960,"sort_value":"1044616696680960"}]}


* * *

##

[Anchor to GET request, Retrieves a specific collect by its ID](/docs/api/admin-rest/latest/resources/collect#get-collects-collect-id)

get

Retrieves a specific collect by its ID

deprecated**deprecated**

Retrieves a specific collect by its ID.

###

[Anchor to Parameters of Retrieves a specific collect by its ID](/docs/api/admin-rest/latest/resources/collect#get-collects-collect-id-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

collect_id

string**string**

required**required**

* * *

fields

Show only certain fields, specified by a comma-separated list of field names.

* * *

Was this section helpful?

YesNo

###

[Anchor to get-collects-collect-id-examples](/docs/api/admin-rest/latest/resources/collect#get-collects-collect-id-examples)Examples

Retrieve a collect with a certain ID

Path parameters

collect_id=455204334

string**string**

required**required**

Was this section helpful?

YesNo

get

## /admin/api/2026-01/collects/455204334.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/collects/455204334.json" \

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

HTTP/1.1 200 OK

{

"collect": {

"id": 455204334,

"collection_id": 841564295,

"product_id": 632910392,

"created_at": null,

"updated_at": null,

"position": 1044616696680960,

"sort_value": "1044616696680960"

}

}

### examples

  * #### Retrieve a collect with a certain ID

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/collects/455204334.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Collect.find({
          session: session,
          id: 455204334,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Collect.find(
          session: test_session,
          id: 455204334,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Collect.find({
          session: session,
          id: 455204334,
        });

#### response

        HTTP/1.1 200 OK{"collect":{"id":455204334,"collection_id":841564295,"product_id":632910392,"created_at":null,"updated_at":null,"position":1044616696680960,"sort_value":"1044616696680960"}}


* * *

##

[Anchor to GET request, Retrieves a count of collects](/docs/api/admin-rest/latest/resources/collect#get-collects-count)

get

Retrieves a count of collects

[collection](/docs/api/admin-graphql/latest/queries/collection)

Retrieves a count of collects.

###

[Anchor to Parameters of Retrieves a count of collects](/docs/api/admin-rest/latest/resources/collect#get-collects-count-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to get-collects-count-examples](/docs/api/admin-rest/latest/resources/collect#get-collects-count-examples)Examples

Count all collects for the shop

Count only collects for a certain collection

Query parameters

collection_id=841564295

The ID of the custom collection containing the product.

Count only collects for a certain product

Query parameters

product_id=632910392

The unique numeric identifier for the product in the custom collection.

Was this section helpful?

YesNo

get

## /admin/api/2026-01/collects/count.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/collects/count.json" \

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

  * #### Count all collects for the shop

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/collects/count.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Collect.count({
          session: session,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Collect.count(
          session: test_session,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Collect.count({
          session: session,
        });

#### response

        HTTP/1.1 200 OK{"count":2}

  * #### Count only collects for a certain collection

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/collects/count.json?collection_id=841564295" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Collect.count({
          session: session,
          collection_id: "841564295",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Collect.count(
          session: test_session,
          collection_id: "841564295",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Collect.count({
          session: session,
          collection_id: "841564295",
        });

#### response

        HTTP/1.1 200 OK{"count":1}

  * #### Count only collects for a certain product

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/collects/count.json?product_id=632910392" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Collect.count({
          session: session,
          product_id: "632910392",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Collect.count(
          session: test_session,
          product_id: "632910392",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Collect.count({
          session: session,
          product_id: "632910392",
        });

#### response

        HTTP/1.1 200 OK{"count":2}


* * *

##

[Anchor to DELETE request, Removes a product from a collection](/docs/api/admin-rest/latest/resources/collect#delete-collects-collect-id)

del

Removes a product from a collection

[collectionRemoveProducts](/docs/api/admin-graphql/latest/mutations/collectionRemoveProducts?example=removes-a-product-from-a-collection)

Removes a product from a collection.

###

[Anchor to Parameters of Removes a product from a collection](/docs/api/admin-rest/latest/resources/collect#delete-collects-collect-id-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

collect_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to delete-collects-collect-id-examples](/docs/api/admin-rest/latest/resources/collect#delete-collects-collect-id-examples)Examples

Delete the link between a product an a collection

Path parameters

collect_id=455204334

string**string**

required**required**

Was this section helpful?

YesNo

del

## /admin/api/2026-01/collects/455204334.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X DELETE "https://your-development-store.myshopify.com/admin/api/2026-01/collects/455204334.json" \

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

  * #### Delete the link between a product an a collection

#####

        curl -X DELETE "https://your-development-store.myshopify.com/admin/api/2026-01/collects/455204334.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Collect.delete({
          session: session,
          id: 455204334,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Collect.delete(
          session: test_session,
          id: 455204334,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Collect.delete({
          session: session,
          id: 455204334,
        });

#### response

        HTTP/1.1 200 OK{}