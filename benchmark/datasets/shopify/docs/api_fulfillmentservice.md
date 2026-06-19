# FulfillmentService

*Source: https://shopify.dev/docs/api/admin-rest/2026-01/resources/fulfillmentservice*

---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04

2026-01latest

# FulfillmentService

Ask assistant

Requires `fulfillments` access scope.

**Requires `fulfillments` access scope.:**

A **Fulfillment Service** is a third party warehouse that prepares and ships orders on behalf of the store owner. Fulfillment services charge a fee to package and ship items and update product inventory levels. Some well known fulfillment services with Shopify integrations include: Amazon, Shipwire, and Rakuten. When an app registers a new `FulfillmentService` on a store, Shopify automatically creates a `Location` that's associated to the fulfillment service. To learn more about fulfillment services, refer to [Manage fulfillments as a fulfillment service app](/apps/fulfillment/fulfillment-service-apps) guide.

Using the `FulfillmentService` resource, you can register, edit, and delete a new fulfillment service.

## Hosted endpoints

Fulfillment service providers integrate with Shopify by providing Shopify with a set of hosted endpoints that Shopify can query on certain conditions. These endpoints must have a common prefix, and this prefix should be supplied in the `callback_url` parameter in the request that creates the fulfillment service.

  * Shopify sends POST requests to the `callback_url/fulfillment_order_notification` endpoint to notify the fulfillment service about fulfillment requests and fulfillment cancellation requests.
[As of the 2022-07 API version](/changelog/legacy-fulfillment-api-deprecation), it's mandatory for a fulfillment service to follow a fulfillment order based workflow by hosting the `callback_url/fulfillment_order_notification` endpoint, and acting on fulfillment requests and cancellations.
For more information, refer to [Receive fulfillment requests and cancellations](/apps/fulfillment/fulfillment-service-apps/manage-fulfillments#step-2-receive-fulfillment-requests-and-cancellations).
  * Shopify sends GET requests to the `callback_url/fetch_tracking_numbers` endpoint to retrieve tracking numbers for orders if `tracking_support` is set to `true`.
For more information, refer to [Enable tracking support](/apps/build/orders-fulfillment/fulfillment-service-apps/build-for-fulfillment-services#step-9-optional-enable-tracking-support).
Fulfillment services can also update tracking information with a [corresponding API](/api/admin-rest/latest/resources/fulfillment#post-fulfillments-fulfillment-id-update-tracking), rather than waiting for Shopify to ask for tracking numbers.
  * Shopify sends GET requests to the `callback_url/fetch_stock` endpoint to retrieve on hand inventory levels for the fulfillment service location if `inventory_management` is set to `true`.
For more information, refer to [Sharing inventory levels with Shopify](/apps/build/orders-fulfillment/fulfillment-service-apps/build-for-fulfillment-services#step-10-optional-share-inventory-levels-with-shopify).


To make sure you have everything set up correctly, you can test the `callback_url`-prefixed endpoints in your development store.

## Resources and webhooks

There are a variety of REST resources and webhooks that enable a fulfillment service to work. To exchange fulfillment information with Shopify, fulfillment services use the [FulfillmentOrder](/api/admin-rest/latest/resources/fulfillmentorder), [FulfillmentRequest](/api/admin-rest/latest/resources/fulfillmentrequest), and [CancellationRequest](/api/admin-rest/latest/resources/cancellationrequest), [Fulfillment](/api/admin-rest/latest/resources/fulfillment) and [Order](/api/admin-rest/latest/resources/order) resources. To act on fulfillment process events that happen on the Shopify side, besides awaiting calls to `callback_url`-prefixed endpoints, fulfillment services can subscribe to the [fulfillment order](/apps/fulfillment/fulfillment-service-apps/manage-fulfillments#webhooks) and [order](/api/admin-rest/latest/resources/webhook) webhooks.

Was this section helpful?

YesNo

#

## Endpoints

  * [post/admin/api/latest/fulfillment_services.json](/docs/api/admin-rest/latest/resources/fulfillmentservice#post-fulfillment-services)

Create a new FulfillmentService

[fulfillmentServiceCreate](/docs/api/admin-graphql/latest/mutations/fulfillmentServiceCreate?example=create-a-new-fulfillmentservice)

  * [get/admin/api/latest/fulfillment_services.json?scope=all](/docs/api/admin-rest/latest/resources/fulfillmentservice#get-fulfillment-services?scope=all)

Receive a list of all FulfillmentServices

[shop](/docs/api/admin-graphql/latest/queries/shop?example=receive-a-list-of-all-fulfillmentservices)

  * [get/admin/api/latest/fulfillment_services/{fulfillment_service_id}.json](/docs/api/admin-rest/latest/resources/fulfillmentservice#get-fulfillment-services-fulfillment-service-id)

Receive a single FulfillmentService

[fulfillmentService](/docs/api/admin-graphql/latest/queries/fulfillmentService?example=receive-a-single-fulfillmentservice)

  * [put/admin/api/latest/fulfillment_services/{fulfillment_service_id}.json](/docs/api/admin-rest/latest/resources/fulfillmentservice#put-fulfillment-services-fulfillment-service-id)

Modify an existing FulfillmentService

[fulfillmentServiceUpdate](/docs/api/admin-graphql/latest/mutations/fulfillmentServiceUpdate?example=modify-an-existing-fulfillmentservice)

  * [del/admin/api/latest/fulfillment_services/{fulfillment_service_id}.json](/docs/api/admin-rest/latest/resources/fulfillmentservice#delete-fulfillment-services-fulfillment-service-id)

Remove an existing FulfillmentService

[fulfillmentServiceDelete](/docs/api/admin-graphql/latest/mutations/fulfillmentServiceDelete?example=remove-an-existing-fulfillmentservice)


* * *

[Anchor to ](/docs/api/admin-rest/latest/resources/fulfillmentservice#resource-object)

## The FulfillmentService resource

[Anchor to ](/docs/api/admin-rest/latest/resources/fulfillmentservice#resource-object-properties)

### Properties

* * *

admin_graphql_api_id

->[id](/docs/api/admin-graphql/latest/objects/FulfillmentService#field-FulfillmentService.fields.id)

The GraphQL GID for this fulfillment service.

* * *

callback_url

->[callbackUrl](/docs/api/admin-graphql/latest/objects/FulfillmentService#field-FulfillmentService.fields.callbackUrl)

The callback URL that the fulfillment service has registered for requests. The following considerations apply:

Show callback_url properties

  * Shopify queries the `callback_url/fetch_tracking_numbers` endpoint to retrieve tracking numbers for orders, if `tracking_support` is set to `true`.
  * Shopify queries the `callback_url/fetch_stock` endpoint to retrieve inventory levels, if `inventory_management` is set to `true`.
  * Shopify uses the `callback_url/fulfillment_order_notification` endpoint to send [ fulfillment and cancellation requests](/apps/fulfillment/fulfillment-service-apps/manage-fulfillments#step-2-receive-fulfillment-requests-and-cancellations)


* * *

fulfillment_orders_opt_in

deprecated**deprecated**

Whether the fulfillment service uses the [fulfillment order based workflow](/apps/fulfillment/fulfillment-service-apps/manage-fulfillments) for managing fulfillments.
[As of 2022-07 API version](/changelog/legacy-fulfillment-api-deprecation), the fulfillment order based workflow is the only way to manage fulfillments, and `fulfillment_orders_opt_in` must be set to `true`.
As the migration is now finished, the `fulfillment_orders_opt_in` property is [deprecated](/changelog/deprecation-of-the-fulfillmentservice-fulfillmentordersoptin-field) and is always set to `true` on correctly functioning fulfillment services.

* * *

permits_sku_sharing

deprecated**deprecated**

Whether the fulfillment service can stock inventory alongside other locations. As of version `2026-04`, this field will be removed.

* * *

handle

->[handle](/docs/api/admin-graphql/latest/objects/FulfillmentService#field-FulfillmentService.fields.handle)

Human-readable unique identifier for this fulfillment service.

* * *

inventory_management

->[inventoryManagement](/docs/api/admin-graphql/latest/objects/FulfillmentService#field-FulfillmentService.fields.inventoryManagement)

Whether the fulfillment service tracks product inventory and provides updates to Shopify. Valid values: `true` and `false`.

* * *

location_id

->[id](/docs/api/admin-graphql/latest/objects/Location#field-Location.fields.id)

The unique identifier of the location associated with the fulfillment service

* * *

name

->[serviceName](/docs/api/admin-graphql/latest/objects/FulfillmentService#field-FulfillmentService.fields.serviceName)

The name of the fulfillment service as seen by merchants.

* * *

provider_id

deprecated**deprecated**

A unique identifier for the fulfillment service provider.

* * *

requires_shipping_method

deprecated**deprecated**

Whether the fulfillment service requires products to be physically shipped. Valid values: `true` and `false`.

* * *

tracking_support

->[trackingSupport](/docs/api/admin-graphql/latest/objects/FulfillmentService#field-FulfillmentService.fields.trackingSupport)

Whether the fulfillment service provides tracking numbers for packages. Valid values: `true` and `false`.

* * *

Was this section helpful?

YesNo

{}

## The FulfillmentService resource

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

{

"admin_graphql_api_id": "gid://shopify/FulfillmentService/1",

"callback_url": "http://myapp.com",

"fulfillment_orders_opt_in": true,

"permits_sku_sharing": true,

"handle": "my-fulfillment-service",

"inventory_management": true,

"location_id": 19,

"name": "My Fulfillment Service",

"provider_id": null,

"requires_shipping_method": true,

"tracking_support": true

}

* * *

##

[Anchor to POST request, Create a new FulfillmentService](/docs/api/admin-rest/latest/resources/fulfillmentservice#post-fulfillment-services)

post

Create a new FulfillmentService

[fulfillmentServiceCreate](/docs/api/admin-graphql/latest/mutations/fulfillmentServiceCreate?example=create-a-new-fulfillmentservice)

###

[Anchor to Parameters of Create a new FulfillmentService](/docs/api/admin-rest/latest/resources/fulfillmentservice#post-fulfillment-services-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

callback_url

The callback URL that the fulfillment service has registered for requests. The following considerations apply:

Show callback_url properties

  * Shopify queries the `callback_url/fetch_tracking_numbers` endpoint to retrieve tracking numbers for orders, if `tracking_support` is set to `true`.
  * Shopify queries the `callback_url/fetch_stock` endpoint to retrieve inventory levels, if `inventory_management` is set to `true`.
  * Shopify uses the `callback_url/fulfillment_order_notification` endpoint to send [ fulfillment and cancellation requests](/apps/fulfillment/fulfillment-service-apps/manage-fulfillments#step-2-receive-fulfillment-requests-and-cancellations)


* * *

fulfillment_orders_opt_in

boolean**boolean**

default true**default true**

Whether the fulfillment service uses the [fulfillment order based workflow](/apps/fulfillment/fulfillment-service-apps/manage-fulfillments) for managing fulfillments.
As the migration is now finished, the `fulfillment_orders_opt_in` property is [deprecated](/changelog/deprecation-of-the-fulfillmentservice-fulfillmentordersoptin-field) and will be removed in the next API version. This API version defaults it to `true` for a smooth migration experience. Do not set the `fulfillment_orders_opt_in` argument, and you are ready for the next API version release.

* * *

inventory_management

boolean**boolean**

Whether the fulfillment service tracks product inventory and provides updates to Shopify. Valid values: `true` and `false`.

* * *

name

string**string**

The name of the fulfillment service as seen by merchants.

* * *

permits_sku_sharing

boolean**boolean**

default true**default true**

Whether the fulfillment service can stock inventory alongside other locations. As of API version `2025-10` this property will return an error if set to `false` and default to `true` if omitted. It will be removed in the next API version.

* * *

requires_shipping_method

boolean**boolean**

Whether the fulfillment service requires products to be physically shipped. Valid values: `true` and `false`.

* * *

tracking_support

boolean**boolean**

Whether the fulfillment service provides tracking numbers for packages. Valid values: `true` and `false`.

* * *

Was this section helpful?

YesNo

###

[Anchor to post-fulfillment-services-examples](/docs/api/admin-rest/latest/resources/fulfillmentservice#post-fulfillment-services-examples)Examples

Create a fulfillment service

Request body

fulfillment_service

Fulfillment_service resource**Fulfillment_service resource**

Show fulfillment_service properties

fulfillment_service.name:"Jupiter Fulfillment"

The name of the fulfillment service as seen by merchants.

fulfillment_service.callback_url:"http://google.com"

The callback URL that the fulfillment service has registered for requests. The following considerations apply:

Show callback_url properties

  * Shopify queries the `callback_url/fetch_tracking_numbers` endpoint to retrieve tracking numbers for orders, if `tracking_support` is set to `true`.
  * Shopify queries the `callback_url/fetch_stock` endpoint to retrieve inventory levels, if `inventory_management` is set to `true`.
  * Shopify uses the `callback_url/fulfillment_order_notification` endpoint to send [ fulfillment and cancellation requests](/apps/fulfillment/fulfillment-service-apps/manage-fulfillments#step-2-receive-fulfillment-requests-and-cancellations)


fulfillment_service.inventory_management:true

Whether the fulfillment service tracks product inventory and provides updates to Shopify. Valid values: `true` and `false`.

fulfillment_service.tracking_support:true

Whether the fulfillment service provides tracking numbers for packages. Valid values: `true` and `false`.

Was this section helpful?

YesNo

post

## /admin/api/2026-01/fulfillment_services.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{"fulfillment_service":{"name":"Jupiter Fulfillment","callback_url":"http://google.com","inventory_management":true,"tracking_support":true}}' \

-X POST "https://your-development-store.myshopify.com/admin/api/2026-01/fulfillment_services.json" \

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

HTTP/1.1 201 Created

{

"fulfillment_service": {

"id": 1061774490,

"name": "Jupiter Fulfillment",

"email": null,

"service_name": "Jupiter Fulfillment",

"handle": "jupiter-fulfillment",

"fulfillment_orders_opt_in": true,

"include_pending_stock": false,

"provider_id": null,

"location_id": 1072404547,

"callback_url": "http://google.com/",

"tracking_support": true,

"inventory_management": true,

"admin_graphql_api_id": "gid://shopify/ApiFulfillmentService/1061774490",

"permits_sku_sharing": true,

"requires_shipping_method": true

}

}

### examples

  * #### Create a fulfillment service

#####

        curl -d '{"fulfillment_service":{"name":"Jupiter Fulfillment","callback_url":"http://google.com","inventory_management":true,"tracking_support":true}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/fulfillment_services.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const fulfillment_service = new admin.rest.resources.FulfillmentService({session: session});

        fulfillment_service.name = "Jupiter Fulfillment";
        fulfillment_service.callback_url = "http://google.com";
        fulfillment_service.inventory_management = true;
        fulfillment_service.tracking_support = true;
        await fulfillment_service.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        fulfillment_service = ShopifyAPI::FulfillmentService.new(session: test_session)
        fulfillment_service.name = "Jupiter Fulfillment"
        fulfillment_service.callback_url = "http://google.com"
        fulfillment_service.inventory_management = true
        fulfillment_service.tracking_support = true
        fulfillment_service.save!

#####

        // Session is built by the OAuth process

        const fulfillment_service = new shopify.rest.FulfillmentService({session: session});
        fulfillment_service.name = "Jupiter Fulfillment";
        fulfillment_service.callback_url = "http://google.com";
        fulfillment_service.inventory_management = true;
        fulfillment_service.tracking_support = true;
        await fulfillment_service.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"fulfillment_service":{"id":1061774490,"name":"Jupiter Fulfillment","email":null,"service_name":"Jupiter Fulfillment","handle":"jupiter-fulfillment","fulfillment_orders_opt_in":true,"include_pending_stock":false,"provider_id":null,"location_id":1072404547,"callback_url":"http://google.com/","tracking_support":true,"inventory_management":true,"admin_graphql_api_id":"gid://shopify/ApiFulfillmentService/1061774490","permits_sku_sharing":true,"requires_shipping_method":true}}


* * *

##

[Anchor to GET request, Receive a list of all FulfillmentServices](/docs/api/admin-rest/latest/resources/fulfillmentservice#get-fulfillment-services?scope=all)

get

Receive a list of all FulfillmentServices

[shop](/docs/api/admin-graphql/latest/queries/shop?example=receive-a-list-of-all-fulfillmentservices)

###

[Anchor to Parameters of Receive a list of all FulfillmentServices](/docs/api/admin-rest/latest/resources/fulfillmentservice#get-fulfillment-services?scope=all-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

scope

enum**enum**

Specify which fulfillment services to retrieve.

Show scope properties

  * **current_client** : Returns fulfillment providers that have been created by the app sending the request (default)

  * **all** : Returns all the fulfillment providers


* * *

Was this section helpful?

YesNo

###

[Anchor to get-fulfillment-services?scope=all-examples](/docs/api/admin-rest/latest/resources/fulfillmentservice#get-fulfillment-services?scope=all-examples)Examples

List all of the shop's fulfillment services

Query parameters

scope=all

enum**enum**

Specify which fulfillment services to retrieve.

Show scope properties

  * **current_client** : Returns fulfillment providers that have been created by the app sending the request (default)

  * **all** : Returns all the fulfillment providers


List your app's fulfillment services

Was this section helpful?

YesNo

get

## /admin/api/2026-01/fulfillment_services.json?scope=all

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/fulfillment_services.json?scope=all" \

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

HTTP/1.1 200 OK

{

"fulfillment_services": [

{

"id": 611870435,

"name": "Venus Fulfillment",

"email": null,

"service_name": "Venus Fulfillment",

"handle": "venus-fulfillment",

"fulfillment_orders_opt_in": true,

"include_pending_stock": false,

"provider_id": null,

"location_id": 611870435,

"callback_url": "http://google.com/",

"tracking_support": false,

"inventory_management": false,

"admin_graphql_api_id": "gid://shopify/ApiFulfillmentService/611870435",

"permits_sku_sharing": false,

"requires_shipping_method": true

},

{

"id": 755357713,

"name": "Mars Fulfillment",

"email": null,

"service_name": "Mars Fulfillment",

"handle": "mars-fulfillment",

"fulfillment_orders_opt_in": true,

"include_pending_stock": false,

"provider_id": null,

"location_id": 24826418,

"callback_url": "http://google.com/",

"tracking_support": true,

"inventory_management": true,

"admin_graphql_api_id": "gid://shopify/ApiFulfillmentService/755357713",

"permits_sku_sharing": true,

"requires_shipping_method": true

}

]

}

### examples

  * #### List all of the shop's fulfillment services

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/fulfillment_services.json?scope=all" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.FulfillmentService.all({
          session: session,
          scope: "all",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::FulfillmentService.all(
          session: test_session,
          scope: "all",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.FulfillmentService.all({
          session: session,
          scope: "all",
        });

#### response

        HTTP/1.1 200 OK{"fulfillment_services":[{"id":611870435,"name":"Venus Fulfillment","email":null,"service_name":"Venus Fulfillment","handle":"venus-fulfillment","fulfillment_orders_opt_in":true,"include_pending_stock":false,"provider_id":null,"location_id":611870435,"callback_url":"http://google.com/","tracking_support":false,"inventory_management":false,"admin_graphql_api_id":"gid://shopify/ApiFulfillmentService/611870435","permits_sku_sharing":false,"requires_shipping_method":true},{"id":755357713,"name":"Mars Fulfillment","email":null,"service_name":"Mars Fulfillment","handle":"mars-fulfillment","fulfillment_orders_opt_in":true,"include_pending_stock":false,"provider_id":null,"location_id":24826418,"callback_url":"http://google.com/","tracking_support":true,"inventory_management":true,"admin_graphql_api_id":"gid://shopify/ApiFulfillmentService/755357713","permits_sku_sharing":true,"requires_shipping_method":true}]}

  * #### List your app's fulfillment services

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/fulfillment_services.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.FulfillmentService.all({
          session: session,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::FulfillmentService.all(
          session: test_session,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.FulfillmentService.all({
          session: session,
        });

#### response

        HTTP/1.1 200 OK{"fulfillment_services":[{"id":755357713,"name":"Mars Fulfillment","email":null,"service_name":"Mars Fulfillment","handle":"mars-fulfillment","fulfillment_orders_opt_in":true,"include_pending_stock":false,"provider_id":null,"location_id":24826418,"callback_url":"http://google.com/","tracking_support":true,"inventory_management":true,"admin_graphql_api_id":"gid://shopify/ApiFulfillmentService/755357713","permits_sku_sharing":true,"requires_shipping_method":true}]}


* * *

##

[Anchor to GET request, Receive a single FulfillmentService](/docs/api/admin-rest/latest/resources/fulfillmentservice#get-fulfillment-services-fulfillment-service-id)

get

Receive a single FulfillmentService

[fulfillmentService](/docs/api/admin-graphql/latest/queries/fulfillmentService?example=receive-a-single-fulfillmentservice)

###

[Anchor to Parameters of Receive a single FulfillmentService](/docs/api/admin-rest/latest/resources/fulfillmentservice#get-fulfillment-services-fulfillment-service-id-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

fulfillment_service_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to get-fulfillment-services-fulfillment-service-id-examples](/docs/api/admin-rest/latest/resources/fulfillmentservice#get-fulfillment-services-fulfillment-service-id-examples)Examples

Get a single fulfillment service by its ID

Path parameters

fulfillment_service_id=755357713

string**string**

required**required**

Was this section helpful?

YesNo

get

## /admin/api/2026-01/fulfillment_services/755357713.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/fulfillment_services/755357713.json" \

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

HTTP/1.1 200 OK

{

"fulfillment_service": {

"id": 755357713,

"name": "Mars Fulfillment",

"email": null,

"service_name": "Mars Fulfillment",

"handle": "mars-fulfillment",

"fulfillment_orders_opt_in": true,

"include_pending_stock": false,

"provider_id": null,

"location_id": 24826418,

"callback_url": "http://google.com/",

"tracking_support": true,

"inventory_management": true,

"admin_graphql_api_id": "gid://shopify/ApiFulfillmentService/755357713",

"permits_sku_sharing": true,

"requires_shipping_method": true

}

}

### examples

  * #### Get a single fulfillment service by its ID

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/fulfillment_services/755357713.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.FulfillmentService.find({
          session: session,
          id: 755357713,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::FulfillmentService.find(
          session: test_session,
          id: 755357713,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.FulfillmentService.find({
          session: session,
          id: 755357713,
        });

#### response

        HTTP/1.1 200 OK{"fulfillment_service":{"id":755357713,"name":"Mars Fulfillment","email":null,"service_name":"Mars Fulfillment","handle":"mars-fulfillment","fulfillment_orders_opt_in":true,"include_pending_stock":false,"provider_id":null,"location_id":24826418,"callback_url":"http://google.com/","tracking_support":true,"inventory_management":true,"admin_graphql_api_id":"gid://shopify/ApiFulfillmentService/755357713","permits_sku_sharing":true,"requires_shipping_method":true}}


* * *

##

[Anchor to PUT request, Modify an existing FulfillmentService](/docs/api/admin-rest/latest/resources/fulfillmentservice#put-fulfillment-services-fulfillment-service-id)

put

Modify an existing FulfillmentService

[fulfillmentServiceUpdate](/docs/api/admin-graphql/latest/mutations/fulfillmentServiceUpdate?example=modify-an-existing-fulfillmentservice)

###

[Anchor to Parameters of Modify an existing FulfillmentService](/docs/api/admin-rest/latest/resources/fulfillmentservice#put-fulfillment-services-fulfillment-service-id-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

fulfillment_service_id

string**string**

required**required**

* * *

callback_url

The callback URL that the fulfillment service has registered for requests. The following considerations apply:

Show callback_url properties

  * Shopify queries the `callback_url/fetch_tracking_numbers` endpoint to retrieve tracking numbers for orders, if `tracking_support` is set to `true`.
  * Shopify queries the `callback_url/fetch_stock` endpoint to retrieve inventory levels, if `inventory_management` is set to `true`.
  * Shopify uses the `callback_url/fulfillment_order_notification` endpoint to send [ fulfillment and cancellation requests](/apps/fulfillment/fulfillment-service-apps/manage-fulfillments#step-2-receive-fulfillment-requests-and-cancellations)


* * *

fulfillment_orders_opt_in

boolean**boolean**

Whether the fulfillment service uses the [fulfillment order based workflow](/apps/fulfillment/fulfillment-service-apps/manage-fulfillments) for managing fulfillments.
As the migration is now finished, the `fulfillment_orders_opt_in` property is [deprecated.](/changelog/deprecation-of-the-fulfillmentservice-fulfillmentordersoptin-field)

* * *

inventory_management

boolean**boolean**

Whether the fulfillment service tracks product inventory and provides updates to Shopify. Valid values: `true` and `false`.

* * *

name

string**string**

The name of the fulfillment service as seen by merchants.

* * *

permits_sku_sharing

boolean**boolean**

Whether the fulfillment service can stock inventory alongside other locations. In the next version, all new fulfillment services will support SKU sharing by default. As of version `2026-04`, this field will be removed.

* * *

requires_shipping_method

boolean**boolean**

Whether the fulfillment service requires products to be physically shipped. Valid values: `true` and `false`.

* * *

tracking_support

boolean**boolean**

Whether the fulfillment service provides tracking numbers for packages. Valid values: `true` and `false`.

* * *

Was this section helpful?

YesNo

###

[Anchor to put-fulfillment-services-fulfillment-service-id-examples](/docs/api/admin-rest/latest/resources/fulfillmentservice#put-fulfillment-services-fulfillment-service-id-examples)Examples

Update a fulfillment service

Path parameters

fulfillment_service_id=755357713

string**string**

required**required**

Request body

fulfillment_service

Fulfillment_service resource**Fulfillment_service resource**

Show fulfillment_service properties

fulfillment_service.name:"New Fulfillment Service Name"

The name of the fulfillment service as seen by merchants.

Was this section helpful?

YesNo

put

## /admin/api/2026-01/fulfillment_services/755357713.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{"fulfillment_service":{"id":755357713,"name":"New Fulfillment Service Name"}}' \

-X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/fulfillment_services/755357713.json" \

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

HTTP/1.1 200 OK

{

"fulfillment_service": {

"id": 755357713,

"name": "New Fulfillment Service Name",

"email": null,

"service_name": "New Fulfillment Service Name",

"handle": "mars-fulfillment",

"fulfillment_orders_opt_in": true,

"include_pending_stock": false,

"provider_id": null,

"location_id": 24826418,

"callback_url": "http://google.com/",

"tracking_support": true,

"inventory_management": true,

"admin_graphql_api_id": "gid://shopify/ApiFulfillmentService/755357713",

"permits_sku_sharing": true,

"requires_shipping_method": true

}

}

### examples

  * #### Update a fulfillment service

#####

        curl -d '{"fulfillment_service":{"id":755357713,"name":"New Fulfillment Service Name"}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/fulfillment_services/755357713.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const fulfillment_service = new admin.rest.resources.FulfillmentService({session: session});

        fulfillment_service.id = 755357713;
        fulfillment_service.name = "New Fulfillment Service Name";
        await fulfillment_service.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        fulfillment_service = ShopifyAPI::FulfillmentService.new(session: test_session)
        fulfillment_service.id = 755357713
        fulfillment_service.name = "New Fulfillment Service Name"
        fulfillment_service.save!

#####

        // Session is built by the OAuth process

        const fulfillment_service = new shopify.rest.FulfillmentService({session: session});
        fulfillment_service.id = 755357713;
        fulfillment_service.name = "New Fulfillment Service Name";
        await fulfillment_service.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"fulfillment_service":{"id":755357713,"name":"New Fulfillment Service Name","email":null,"service_name":"New Fulfillment Service Name","handle":"mars-fulfillment","fulfillment_orders_opt_in":true,"include_pending_stock":false,"provider_id":null,"location_id":24826418,"callback_url":"http://google.com/","tracking_support":true,"inventory_management":true,"admin_graphql_api_id":"gid://shopify/ApiFulfillmentService/755357713","permits_sku_sharing":true,"requires_shipping_method":true}}


* * *

##

[Anchor to DELETE request, Remove an existing FulfillmentService](/docs/api/admin-rest/latest/resources/fulfillmentservice#delete-fulfillment-services-fulfillment-service-id)

del

Remove an existing FulfillmentService

[fulfillmentServiceDelete](/docs/api/admin-graphql/latest/mutations/fulfillmentServiceDelete?example=remove-an-existing-fulfillmentservice)

###

[Anchor to Parameters of Remove an existing FulfillmentService](/docs/api/admin-rest/latest/resources/fulfillmentservice#delete-fulfillment-services-fulfillment-service-id-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

fulfillment_service_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to delete-fulfillment-services-fulfillment-service-id-examples](/docs/api/admin-rest/latest/resources/fulfillmentservice#delete-fulfillment-services-fulfillment-service-id-examples)Examples

Destroy a fulfillment service

Path parameters

fulfillment_service_id=755357713

string**string**

required**required**

Was this section helpful?

YesNo

del

## /admin/api/2026-01/fulfillment_services/755357713.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X DELETE "https://your-development-store.myshopify.com/admin/api/2026-01/fulfillment_services/755357713.json" \

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

  * #### Destroy a fulfillment service

#####

        curl -X DELETE "https://your-development-store.myshopify.com/admin/api/2026-01/fulfillment_services/755357713.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.FulfillmentService.delete({
          session: session,
          id: 755357713,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::FulfillmentService.delete(
          session: test_session,
          id: 755357713,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.FulfillmentService.delete({
          session: session,
          id: 755357713,
        });

#### response

        HTTP/1.1 200 OK{}