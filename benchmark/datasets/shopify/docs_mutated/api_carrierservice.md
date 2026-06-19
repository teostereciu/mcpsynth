# CarrierService

*Source: https://shopify.dev/docs/api/admin-rest/2026-01/resources/carrierservice*

---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04

2026-01latest

# CarrierService

Ask assistant

Requires `shipping` access scope.

**Requires `shipping` access scope.:**

A carrier service (also known as a carrier calculated service or shipping service) provides real-time shipping rates to Shopify. Some common carrier services include Canada Post, FedEx, UPS, and USPS. The term **carrier** is often used interchangeably with the terms **shipping company** and **rate provider**.

Using the CarrierService resource, you can add a carrier service to a shop and then provide a list of applicable shipping rates at checkout. You can even use the cart data to adjust shipping rates and offer shipping discounts based on what is in the customer's cart.

## Requirements for accessing the CarrierService resource

To access the CarrierService resource, add the `write_shipping` permission to your app's requested scopes. For more information, see [_API access scopes_](/docs/admin-api/access-scopes).

Your app's request to create a carrier service will fail unless the store installing your carrier service meets one of the following requirements:

  * It's on the Advanced Shopify plan or higher.
  * It's on the Shopify plan with yearly billing, or the carrier service feature has been added to the store for a monthly fee. For more information, contact [Shopify Support](https://help.shopify.com/questions).
  * It's a development store.


Note

If a store changes its Shopify plan, then the store's association with a carrier service is deactivated if the store no long meets one of the requirements above.

**Note:**

If a store changes its Shopify plan, then the store's association with a carrier service is deactivated if the store no long meets one of the requirements above.

## Providing shipping rates to Shopify

When adding a carrier service to a store, you need to provide a POST endpoint rooted in the `callback_url` property where Shopify can retrieve applicable shipping rates. The callback URL should be a public endpoint that expects these requests from Shopify.

**A sample Shopify request for shipping rates:**


    POST

Your callback URL

Retrieves a list of applicable shipping rates

### Example shipping rate request sent to a carrier service


    {
      "rate": {
        "origin": {
          "country": "CA",
          "postal_code": "K2P1L4",
          "province": "ON",
          "city": "Ottawa",
          "name": null,
          "address1": "150 Elgin St.",
          "address2": "",
          "address3": null,
          "phone": null,
          "fax": null,
          "email": null,
          "address_type": null,
          "company_name": "Jamie D's Emporium"
        },
        "destination": {
          "country": "CA",
          "postal_code": "K1M1M4",
          "province": "ON",
          "city": "Ottawa",
          "name": "Bob Norman",
          "address1": "24 Sussex Dr.",
          "address2": "",
          "address3": null,
          "phone": null,
          "fax": null,
          "email": null,
          "address_type": null,
          "company_name": null
        },
        "items": [{
          "name": "Short Sleeve T-Shirt",
          "sku": "",
          "quantity": 1,
          "grams": 1000,
          "price": 1999,
          "vendor": "Jamie D's Emporium",
          "requires_shipping": true,
          "taxable": true,
          "fulfillment_service": "manual",
          "properties": null,
          "product_id": 48447225880,
          "variant_id": 258644705304
        }],
        "currency": "USD",
        "locale": "en"
      }
    }


View Response


    {
       "rates": [
           {
               "service_name": "canadapost-overnight",
               "service_code": "ON",
               "total_price": "1295",
               "description": "This is the fastest option by far",
               "currency": "CAD",
               "min_delivery_date": "2013-04-12 14:48:45 -0400",
               "max_delivery_date": "2013-04-12 14:48:45 -0400"
           },
           {
               "service_name": "fedex-2dayground",
               "service_code": "2D",
               "total_price": "2934",
               "currency": "USD",
               "min_delivery_date": "2013-04-12 14:48:45 -0400",
               "max_delivery_date": "2013-04-12 14:48:45 -0400"
           },
           {
               "service_name": "fedex-priorityovernight",
               "service_code": "1D",
               "total_price": "3587",
               "currency": "USD",
               "min_delivery_date": "2013-04-12 14:48:45 -0400",
               "max_delivery_date": "2013-04-12 14:48:45 -0400"
           }
       ]
    }


The `address3`, `fax`, `address_type`, and `company_name` fields are returned by specific [ActiveShipping](https://github.com/Shopify/active_shipping) providers. For API-created carrier services, you should use only the following shipping address fields:

  * `address1`
  * `address2`
  * `city`
  * `zip`
  * `province`
  * `country`


Other values remain as `null` and are not sent to the callback URL.

### Response fields

When Shopify requests shipping rates using your callback URL, the response object `rates` must be a JSON array of objects with the following fields. Required fields must be included in the response for the carrier service integration to work properly.

**Field**| **Description**
---|---
`service_name`
required| The name of the rate, which customers see at checkout. For example: `Expedited Mail`.
`description`
required| A description of the rate, which customers see at checkout. For example: `Includes tracking and insurance`.
`service_code`
required| A unique code associated with the rate. For example: `expedited_mail`.``
`currency`
required| The currency of the shipping rate.
`total_price`
required| The total price expressed in subunits. If the currency doesn't use subunits, then the value must be multiplied by 100. For example: `"total_price": 500` for 5.00 CAD, `"total_price": 100000` for 1000 JPY.
`phone_required`| Whether the customer must provide a phone number at checkout.
`min_delivery_date`| The earliest delivery date for the displayed rate.
`max_delivery_date`| The latest delivery date for the displayed rate to still be valid.

### Special conditions

  * To indicate that this carrier service cannot handle this shipping request, return an empty array and any successful (20x) HTTP code.
  * To force backup rates instead, return a 40x or 50x HTTP code with any content. A good choice is the regular 404 Not Found code.
  * Redirects (30x codes) will only be followed for the same domain as the original callback URL. Attempting to redirect to a different domain will trigger backup rates.
  * There is no retry mechanism. The response must be successful on the first try, within the time budget listed below. Timeouts or errors will trigger backup rates.


## Response Timeouts

The read timeout for rate requests are dynamic, based on the number of requests per minute (RPM). These limits are applied to each shop-app pair. The timeout values are as follows.

**RPM Range**| **Timeout**
---|---
Under 1500| 10s
1500 to 3000| 5s
Over 3000| 3s

**Note:** These values are upper limits and should not be interpretted as a goal to develop towards. Shopify is constantly evaluating the performance of the platform and working towards improving resilience as well as app capabilities. As such, these numbers may be adjusted outside of our normal versioning timelines.

## Server-side caching of requests

Shopify provides server-side caching to reduce the number of requests it makes. Any shipping rate request that identically matches the following fields will be retrieved from Shopify's cache of the initial response:

  * variant IDs
  * default shipping box weight and dimensions
  * variant quantities
  * carrier service ID
  * origin address
  * destination address
  * item weights and signatures


If any of these fields differ, or if the cache has expired since the original request, then new shipping rates are requested. The cache expires 15 minutes after rates are successfully returned. If an error occurs, then the cache expires after 30 seconds.

Was this section helpful?

YesNo

#

## Endpoints

  * [post/admin/api/latest/carrier_services.json](/docs/api/admin-rest/latest/resources/carrierservice#post-carrier-services)

Create a new CarrierService

[carrierServiceCreate](/docs/api/admin-graphql/latest/mutations/carrierServiceCreate?example=create-a-new-carrierservice)

  * [get/admin/api/latest/carrier_services.json](/docs/api/admin-rest/latest/resources/carrierservice#get-carrier-services)

Retrieve a list of CarrierServices

[carrierServices](/docs/api/admin-graphql/latest/queries/carrierServices?example=retrieve-a-list-of-carrierservices)

  * [get/admin/api/latest/carrier_services/{carrier_service_id}.json](/docs/api/admin-rest/latest/resources/carrierservice#get-carrier-services-carrier-service-id)

Receive a single CarrierService

[carrierService](/docs/api/admin-graphql/latest/queries/carrierService?example=receive-a-single-carrierservice)

  * [put/admin/api/latest/carrier_services/{carrier_service_id}.json](/docs/api/admin-rest/latest/resources/carrierservice#put-carrier-services-carrier-service-id)

Modify an existing CarrierService

[carrierServiceUpdate](/docs/api/admin-graphql/latest/mutations/carrierServiceUpdate?example=modify-an-existing-carrierservice)

  * [del/admin/api/latest/carrier_services/{carrier_service_id}.json](/docs/api/admin-rest/latest/resources/carrierservice#delete-carrier-services-carrier-service-id)

Remove an existing CarrierService

[carrierServiceDelete](/docs/api/admin-graphql/latest/mutations/carrierServiceDelete?example=remove-an-existing-carrierservice)


* * *

[Anchor to ](/docs/api/admin-rest/latest/resources/carrierservice#resource-object)

## The CarrierService resource

[Anchor to ](/docs/api/admin-rest/latest/resources/carrierservice#resource-object-properties)

### Properties

* * *

active

->[active](/docs/api/admin-graphql/latest/objects/DeliveryCarrierService#field-DeliveryCarrierService.fields.active)

Whether this carrier service is active. If `true`, then the service will be available to serve rates in checkout.

* * *

callback_url

->[callbackUrl](/docs/api/admin-graphql/latest/objects/DeliveryCarrierService#field-DeliveryCarrierService.fields.callbackUrl)

The URL endpoint that Shopify needs to retrieve shipping rates. This must be a public URL.

* * *

carrier_service_type

deprecated**deprecated**

Distinguishes between API or legacy carrier services.

* * *

id

read-only**read-only**

->[id](/docs/api/admin-graphql/latest/objects/DeliveryCarrierService#field-DeliveryCarrierService.fields.id)

The ID of the carrier service.

* * *

format

deprecated**deprecated**

The format of the data returned by the URL endpoint. `json` is the only valid value.

* * *

name

->[name](/docs/api/admin-graphql/latest/objects/DeliveryCarrierService#field-DeliveryCarrierService.fields.name)

The name of the shipping service as seen by merchants and their customers.

* * *

service_discovery

->[supportsServiceDiscovery](/docs/api/admin-graphql/latest/objects/DeliveryCarrierService#field-DeliveryCarrierService.fields.supportsServiceDiscovery)

Whether merchants are able to send dummy data to your service through the Shopify admin to see shipping rate examples.

* * *

admin_graphql_api_id

read-only**read-only**

->[id](/docs/api/admin-graphql/latest/objects/DeliveryCarrierService#field-DeliveryCarrierService.fields.id)

The GraphQL GID for this carrier service.

* * *

Was this section helpful?

YesNo

{}

## The CarrierService resource

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

{

"active": true,

"callback_url": "http://myapp.com",

"carrier_service_type": "api",

"id": 14079244,

"format": "json",

"name": "My Carrier Service",

"service_discovery": true,

"admin_graphql_api_id": "gid://shopify/DeliveryCarrierService/1"

}

* * *

##

[Anchor to POST request, Create a new CarrierService](/docs/api/admin-rest/latest/resources/carrierservice#post-carrier-services)

post

Create a new CarrierService

[carrierServiceCreate](/docs/api/admin-graphql/latest/mutations/carrierServiceCreate?example=create-a-new-carrierservice)

###

[Anchor to Parameters of Create a new CarrierService](/docs/api/admin-rest/latest/resources/carrierservice#post-carrier-services-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to post-carrier-services-examples](/docs/api/admin-rest/latest/resources/carrierservice#post-carrier-services-examples)Examples

Create a carrier service

Request body

carrier_service

Carrier_service resource**Carrier_service resource**

Show carrier_service properties

carrier_service.name:"Shipping Rate Provider"

->[name](/docs/api/admin-graphql/latest/input-objects/DeliveryCarrierServiceCreateInput#fields-name)

The name of the shipping service as seen by merchants and their customers.

carrier_service.callback_url:"http://shipping.example.com"

->[callbackUrl](/docs/api/admin-graphql/latest/input-objects/DeliveryCarrierServiceCreateInput#fields-callbackUrl)

The URL endpoint that Shopify needs to retrieve shipping rates. This must be a public URL.

carrier_service.service_discovery:true

->[supportsServiceDiscovery](/docs/api/admin-graphql/latest/input-objects/DeliveryCarrierServiceCreateInput#fields-supportsServiceDiscovery)

Whether merchants are able to send dummy data to your service through the Shopify admin to see shipping rate examples.

Was this section helpful?

YesNo

post

## /admin/api/2026-01/carrier_services.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{"carrier_service":{"name":"Shipping Rate Provider","callback_url":"http://shipping.example.com","service_discovery":true}}' \

-X POST "https://your-development-store.myshopify.com/admin/api/2026-01/carrier_services.json" \

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

HTTP/1.1 201 Created

{

"carrier_service": {

"id": 1036894967,

"name": "Shipping Rate Provider",

"active": true,

"service_discovery": true,

"carrier_service_type": "api",

"admin_graphql_api_id": "gid://shopify/DeliveryCarrierService/1036894967",

"format": "json",

"callback_url": "http://shipping.example.com/"

}

}

### examples

  * #### Create a carrier service

#####

        curl -d '{"carrier_service":{"name":"Shipping Rate Provider","callback_url":"http://shipping.example.com","service_discovery":true}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/carrier_services.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const carrier_service = new admin.rest.resources.CarrierService({session: session});

        carrier_service.name = "Shipping Rate Provider";
        carrier_service.callback_url = "http://shipping.example.com";
        carrier_service.service_discovery = true;
        await carrier_service.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        carrier_service = ShopifyAPI::CarrierService.new(session: test_session)
        carrier_service.name = "Shipping Rate Provider"
        carrier_service.callback_url = "http://shipping.example.com"
        carrier_service.service_discovery = true
        carrier_service.save!

#####

        // Session is built by the OAuth process

        const carrier_service = new shopify.rest.CarrierService({session: session});
        carrier_service.name = "Shipping Rate Provider";
        carrier_service.callback_url = "http://shipping.example.com";
        carrier_service.service_discovery = true;
        await carrier_service.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"carrier_service":{"id":1036894967,"name":"Shipping Rate Provider","active":true,"service_discovery":true,"carrier_service_type":"api","admin_graphql_api_id":"gid://shopify/DeliveryCarrierService/1036894967","format":"json","callback_url":"http://shipping.example.com/"}}


* * *

##

[Anchor to GET request, Retrieve a list of CarrierServices](/docs/api/admin-rest/latest/resources/carrierservice#get-carrier-services)

get

Retrieve a list of CarrierServices

[carrierServices](/docs/api/admin-graphql/latest/queries/carrierServices?example=retrieve-a-list-of-carrierservices)

Retrieve a list of CarrierServices. **Note:** Only services with property `active: true` are returned.

###

[Anchor to Parameters of Retrieve a list of CarrierServices](/docs/api/admin-rest/latest/resources/carrierservice#get-carrier-services-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to get-carrier-services-examples](/docs/api/admin-rest/latest/resources/carrierservice#get-carrier-services-examples)Examples

Retrieve a list of carrier services

Was this section helpful?

YesNo

get

## /admin/api/2026-01/carrier_services.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/carrier_services.json" \

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

"carrier_services": [

{

"id": 1036894964,

"name": "Purolator",

"active": true,

"service_discovery": true,

"carrier_service_type": "api",

"admin_graphql_api_id": "gid://shopify/DeliveryCarrierService/1036894964",

"format": "json",

"callback_url": "http://example.com/"

},

{

"id": 260046840,

"name": "ups_shipping",

"active": true,

"service_discovery": true,

"carrier_service_type": "legacy",

"admin_graphql_api_id": "gid://shopify/DeliveryCarrierService/260046840"

}

]

}

### examples

  * #### Retrieve a list of carrier services

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/carrier_services.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.CarrierService.all({
          session: session,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::CarrierService.all(
          session: test_session,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.CarrierService.all({
          session: session,
        });

#### response

        HTTP/1.1 200 OK{"carrier_services":[{"id":1036894964,"name":"Purolator","active":true,"service_discovery":true,"carrier_service_type":"api","admin_graphql_api_id":"gid://shopify/DeliveryCarrierService/1036894964","format":"json","callback_url":"http://example.com/"},{"id":260046840,"name":"ups_shipping","active":true,"service_discovery":true,"carrier_service_type":"legacy","admin_graphql_api_id":"gid://shopify/DeliveryCarrierService/260046840"}]}


* * *

##

[Anchor to GET request, Receive a single CarrierService](/docs/api/admin-rest/latest/resources/carrierservice#get-carrier-services-carrier-service-id)

get

Receive a single CarrierService

[carrierService](/docs/api/admin-graphql/latest/queries/carrierService?example=receive-a-single-carrierservice)

###

[Anchor to Parameters of Receive a single CarrierService](/docs/api/admin-rest/latest/resources/carrierservice#get-carrier-services-carrier-service-id-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

carrier_service_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to get-carrier-services-carrier-service-id-examples](/docs/api/admin-rest/latest/resources/carrierservice#get-carrier-services-carrier-service-id-examples)Examples

Get a single carrier service by its ID

Path parameters

carrier_service_id=1036894965

string**string**

required**required**

Was this section helpful?

YesNo

get

## /admin/api/2026-01/carrier_services/1036894965.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/carrier_services/1036894965.json" \

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

HTTP/1.1 200 OK

{

"carrier_service": {

"id": 1036894965,

"name": "Purolator",

"active": true,

"service_discovery": true,

"carrier_service_type": "api",

"admin_graphql_api_id": "gid://shopify/DeliveryCarrierService/1036894965",

"format": "json",

"callback_url": "http://example.com/"

}

}

### examples

  * #### Get a single carrier service by its ID

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/carrier_services/1036894965.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.CarrierService.find({
          session: session,
          id: 1036894965,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::CarrierService.find(
          session: test_session,
          id: 1036894965,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.CarrierService.find({
          session: session,
          id: 1036894965,
        });

#### response

        HTTP/1.1 200 OK{"carrier_service":{"id":1036894965,"name":"Purolator","active":true,"service_discovery":true,"carrier_service_type":"api","admin_graphql_api_id":"gid://shopify/DeliveryCarrierService/1036894965","format":"json","callback_url":"http://example.com/"}}


* * *

##

[Anchor to PUT request, Modify an existing CarrierService](/docs/api/admin-rest/latest/resources/carrierservice#put-carrier-services-carrier-service-id)

put

Modify an existing CarrierService

[carrierServiceUpdate](/docs/api/admin-graphql/latest/mutations/carrierServiceUpdate?example=modify-an-existing-carrierservice)

Updates a carrier service. Only the app that creates a carrier service can update it.

###

[Anchor to Parameters of Modify an existing CarrierService](/docs/api/admin-rest/latest/resources/carrierservice#put-carrier-services-carrier-service-id-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

carrier_service_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to put-carrier-services-carrier-service-id-examples](/docs/api/admin-rest/latest/resources/carrierservice#put-carrier-services-carrier-service-id-examples)Examples

Update a carrier service

Path parameters

carrier_service_id=1036894963

string**string**

required**required**

Request body

carrier_service

Carrier_service resource**Carrier_service resource**

Show carrier_service properties

carrier_service.id:1036894963

read-only**read-only**

The ID of the carrier service.

carrier_service.name:"Some new name"

->[name](/docs/api/admin-graphql/latest/input-objects/DeliveryCarrierServiceUpdateInput#fields-name)

The name of the shipping service as seen by merchants and their customers.

carrier_service.active:false

->[active](/docs/api/admin-graphql/latest/input-objects/DeliveryCarrierServiceUpdateInput#fields-active)

Whether this carrier service is active. If `true`, then the service will be available to serve rates in checkout.

Was this section helpful?

YesNo

put

## /admin/api/2026-01/carrier_services/1036894963.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{"carrier_service":{"id":1036894963,"name":"Some new name","active":false}}' \

-X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/carrier_services/1036894963.json" \

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

HTTP/1.1 200 OK

{

"carrier_service": {

"active": false,

"id": 1036894963,

"name": "Some new name",

"service_discovery": true,

"carrier_service_type": "api",

"admin_graphql_api_id": "gid://shopify/DeliveryCarrierService/1036894963",

"format": "json",

"callback_url": "http://example.com/"

}

}

### examples

  * #### Update a carrier service

#####

        curl -d '{"carrier_service":{"id":1036894963,"name":"Some new name","active":false}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/carrier_services/1036894963.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const carrier_service = new admin.rest.resources.CarrierService({session: session});

        carrier_service.id = 1036894963;
        carrier_service.name = "Some new name";
        carrier_service.active = false;
        await carrier_service.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        carrier_service = ShopifyAPI::CarrierService.new(session: test_session)
        carrier_service.id = 1036894963
        carrier_service.name = "Some new name"
        carrier_service.active = false
        carrier_service.save!

#####

        // Session is built by the OAuth process

        const carrier_service = new shopify.rest.CarrierService({session: session});
        carrier_service.id = 1036894963;
        carrier_service.name = "Some new name";
        carrier_service.active = false;
        await carrier_service.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"carrier_service":{"active":false,"id":1036894963,"name":"Some new name","service_discovery":true,"carrier_service_type":"api","admin_graphql_api_id":"gid://shopify/DeliveryCarrierService/1036894963","format":"json","callback_url":"http://example.com/"}}


* * *

##

[Anchor to DELETE request, Remove an existing CarrierService](/docs/api/admin-rest/latest/resources/carrierservice#delete-carrier-services-carrier-service-id)

del

Remove an existing CarrierService

[carrierServiceDelete](/docs/api/admin-graphql/latest/mutations/carrierServiceDelete?example=remove-an-existing-carrierservice)

###

[Anchor to Parameters of Remove an existing CarrierService](/docs/api/admin-rest/latest/resources/carrierservice#delete-carrier-services-carrier-service-id-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

carrier_service_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to delete-carrier-services-carrier-service-id-examples](/docs/api/admin-rest/latest/resources/carrierservice#delete-carrier-services-carrier-service-id-examples)Examples

Delete a carrier service

Path parameters

carrier_service_id=1036894961

string**string**

required**required**

Was this section helpful?

YesNo

del

## /admin/api/2026-01/carrier_services/1036894961.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X DELETE "https://your-development-store.myshopify.com/admin/api/2026-01/carrier_services/1036894961.json" \

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

  * #### Delete a carrier service

#####

        curl -X DELETE "https://your-development-store.myshopify.com/admin/api/2026-01/carrier_services/1036894961.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.CarrierService.delete({
          session: session,
          id: 1036894961,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::CarrierService.delete(
          session: test_session,
          id: 1036894961,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.CarrierService.delete({
          session: session,
          id: 1036894961,
        });

#### response

        HTTP/1.1 200 OK{}