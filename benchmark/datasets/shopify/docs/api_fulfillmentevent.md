# FulfillmentEvent

*Source: https://shopify.dev/docs/api/admin-rest/2026-01/resources/fulfillmentevent*

---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04

2026-01latest

# FulfillmentEvent

Ask assistant

Requires `orders` access scope.

**Requires `orders` access scope.:**

The FulfillmentEvent resource represents tracking events that belong to a [fulfillment](/docs/admin-api/rest/reference/shipping-and-fulfillment/fulfillment) of one or more items in an [order](/docs/admin-api/rest/reference/orders/order). Fulfillment events are displayed on the [order status page](https://help.shopify.com/manual/orders/status-tracking) to update customers on the status of their shipment.

Was this section helpful?

YesNo

#

## Endpoints

  * [post/admin/api/latest/orders/{order_id}/fulfillments/{fulfillment_id}/events.json](/docs/api/admin-rest/latest/resources/fulfillmentevent#post-orders-order-id-fulfillments-fulfillment-id-events)

Creates a fulfillment event

[fulfillmentEventCreate](/docs/api/admin-graphql/latest/mutations/fulfillmentEventCreate?example=creates-a-fulfillment-event)

  * [get/admin/api/latest/orders/{order_id}/fulfillments/{fulfillment_id}/events.json](/docs/api/admin-rest/latest/resources/fulfillmentevent#get-orders-order-id-fulfillments-fulfillment-id-events)

Retrieves a list of fulfillment events for a specific fulfillment

[fulfillment](/docs/api/admin-graphql/latest/queries/fulfillment?example=retrieves-a-list-of-fulfillment-events-for-a-specific-fulfillment)

  * [get/admin/api/latest/orders/{order_id}/fulfillments/{fulfillment_id}/events/{event_id}.json](/docs/api/admin-rest/latest/resources/fulfillmentevent#get-orders-order-id-fulfillments-fulfillment-id-events-event-id)

Retrieves a specific fulfillment event

deprecated

**

deprecated

**

  * [ del/admin/api/latest/orders/{order_id}/fulfillments/{fulfillment_id}/events/{event_id}.json](/docs/api/admin-rest/latest/resources/fulfillmentevent#delete-orders-order-id-fulfillments-fulfillment-id-events-event-id)

Deletes a fulfillment event

deprecated

**

deprecated

**


* * *

[ Anchor to ](/docs/api/admin-rest/latest/resources/fulfillmentevent#resource-object)

## The FulfillmentEvent resource

[Anchor to ](/docs/api/admin-rest/latest/resources/fulfillmentevent#resource-object-properties)

### Properties

* * *

address1

->[address1](/docs/api/admin-graphql/latest/objects/FulfillmentEvent#field-FulfillmentEvent.fields.address1)

The street address where the fulfillment event occurred.

* * *

city

->[city](/docs/api/admin-graphql/latest/objects/FulfillmentEvent#field-FulfillmentEvent.fields.city)

The city where the fulfillment event occurred.

* * *

country

->[country](/docs/api/admin-graphql/latest/objects/FulfillmentEvent#field-FulfillmentEvent.fields.country)

The country where the fulfillment event occurred.

* * *

created_at

->[createdAt](/docs/api/admin-graphql/latest/objects/FulfillmentEvent#field-FulfillmentEvent.fields.createdAt)

The date and time ([ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) format) when the fulfillment event was created.

* * *

estimated_delivery_at

->[estimatedDeliveryAt](/docs/api/admin-graphql/latest/objects/FulfillmentEvent#field-FulfillmentEvent.fields.estimatedDeliveryAt)

The estimated delivery date based on the fulfillment's tracking number, as long as it's provided by one of the following carriers: USPS, FedEx, UPS, or Canada Post (Canada only). Value is `null` if no tracking number is available or if the tracking number is from an unsupported carrier. This property is available only when [carrier calculated rates](https://help.shopify.com/manual/shipping/rates-and-methods/custom-calculated-rates) are in use.'

* * *

fulfillment_id

An ID for the fulfillment that's associated with the fulfillment event.

* * *

happened_at

->[happenedAt](/docs/api/admin-graphql/latest/objects/FulfillmentEvent#field-FulfillmentEvent.fields.happenedAt)

The date and time ([ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) format) when the fulfillment event occurred.

* * *

id

->[id](/docs/api/admin-graphql/latest/objects/FulfillmentEvent#field-FulfillmentEvent.fields.id)

An ID for the fulfillment event.

* * *

latitude

->[latitude](/docs/api/admin-graphql/latest/objects/FulfillmentEvent#field-FulfillmentEvent.fields.latitude)

A geographic coordinate specifying the latitude of the fulfillment event.

* * *

longitude

->[longitude](/docs/api/admin-graphql/latest/objects/FulfillmentEvent#field-FulfillmentEvent.fields.longitude)

A geographic coordinate specifying the longitude of the fulfillment event.

* * *

message

->[message](/docs/api/admin-graphql/latest/objects/FulfillmentEvent#field-FulfillmentEvent.fields.message)

An arbitrary message describing the status. Can be provided by a shipping carrier.

* * *

order_id

deprecated**deprecated**

The ID of the order that's associated with the fulfillment event.

* * *

Show 5 hidden fields

Was this section helpful?

YesNo

{}

## The FulfillmentEvent resource

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

{

"address1": "3575 Boul. Saint-Laurent",

"city": "Montreal",

"country": "Canada",

"created_at": "2012-03-13T16:09:54-04:00",

"estimated_delivery_at": "2014-04-13T16:09:54-04:00",

"fulfillment_id": 450789469,

"happened_at": "2012-03-13T16:09:54-04:00",

"id": 255858046,

"latitude": 45.5017,

"longitude": 73.5673,

"message": "IN_TRANSIT",

"order_id": 3183479,

"province": "QC",

"shop_id": 255858046,

"status": "in_transit",

"updated_at": "2012-03-15T16:09:54-04:00",

"zip": "H2X 2R7"

}

* * *

##

[Anchor to POST request, Creates a fulfillment event](/docs/api/admin-rest/latest/resources/fulfillmentevent#post-orders-order-id-fulfillments-fulfillment-id-events)

post

Creates a fulfillment event

[fulfillmentEventCreate](/docs/api/admin-graphql/latest/mutations/fulfillmentEventCreate?example=creates-a-fulfillment-event)

Creates a fulfillment event

###

[Anchor to Parameters of Creates a fulfillment event](/docs/api/admin-rest/latest/resources/fulfillmentevent#post-orders-order-id-fulfillments-fulfillment-id-events-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

fulfillment_id

string**string**

required**required**

* * *

order_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to post-orders-order-id-fulfillments-fulfillment-id-events-examples](/docs/api/admin-rest/latest/resources/fulfillmentevent#post-orders-order-id-fulfillments-fulfillment-id-events-examples)Examples

Create a fulfillment event

Was this section helpful?

YesNo

post

## /admin/api/2026-01/orders/450789469/fulfillments/255858046/events.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{"event":{"status":"in_transit"}}' \

-X POST "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469/fulfillments/255858046/events.json" \

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

HTTP/1.1 201 Created

{

"fulfillment_event": {

"id": 944956398,

"fulfillment_id": 255858046,

"status": "in_transit",

"message": null,

"happened_at": "2026-01-09T19:38:04-05:00",

"city": null,

"province": null,

"country": null,

"zip": null,

"address1": null,

"latitude": null,

"longitude": null,

"shop_id": 548380009,

"created_at": "2026-01-09T19:38:04-05:00",

"updated_at": "2026-01-09T19:38:04-05:00",

"estimated_delivery_at": null,

"order_id": 450789469,

"admin_graphql_api_id": "gid://shopify/FulfillmentEvent/944956398"

}

}

### examples

  * #### Create a fulfillment event

#####

        curl -d '{"event":{"status":"in_transit"}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469/fulfillments/255858046/events.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const fulfillment_event = new admin.rest.resources.FulfillmentEvent({session: session});

        fulfillment_event.order_id = 450789469;
        fulfillment_event.fulfillment_id = 255858046;
        fulfillment_event.status = "in_transit";
        await fulfillment_event.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        fulfillment_event = ShopifyAPI::FulfillmentEvent.new(session: test_session)
        fulfillment_event.order_id = 450789469
        fulfillment_event.fulfillment_id = 255858046
        fulfillment_event.status = "in_transit"
        fulfillment_event.save!

#####

        // Session is built by the OAuth process

        const fulfillment_event = new shopify.rest.FulfillmentEvent({session: session});
        fulfillment_event.order_id = 450789469;
        fulfillment_event.fulfillment_id = 255858046;
        fulfillment_event.status = "in_transit";
        await fulfillment_event.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"fulfillment_event":{"id":944956398,"fulfillment_id":255858046,"status":"in_transit","message":null,"happened_at":"2026-01-09T19:38:04-05:00","city":null,"province":null,"country":null,"zip":null,"address1":null,"latitude":null,"longitude":null,"shop_id":548380009,"created_at":"2026-01-09T19:38:04-05:00","updated_at":"2026-01-09T19:38:04-05:00","estimated_delivery_at":null,"order_id":450789469,"admin_graphql_api_id":"gid://shopify/FulfillmentEvent/944956398"}}


* * *

##

[Anchor to GET request, Retrieves a list of fulfillment events for a specific fulfillment](/docs/api/admin-rest/latest/resources/fulfillmentevent#get-orders-order-id-fulfillments-fulfillment-id-events)

get

Retrieves a list of fulfillment events for a specific fulfillment

[fulfillment](/docs/api/admin-graphql/latest/queries/fulfillment?example=retrieves-a-list-of-fulfillment-events-for-a-specific-fulfillment)

Retrieves a list of fulfillment events for a specific fulfillment

###

[Anchor to Parameters of Retrieves a list of fulfillment events for a specific fulfillment](/docs/api/admin-rest/latest/resources/fulfillmentevent#get-orders-order-id-fulfillments-fulfillment-id-events-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

fulfillment_id

string**string**

required**required**

* * *

order_id

string**string**

required**required**

* * *

fulfillment_id

The ID of the fulfillment that's associated with the fulfillment event.

* * *

order_id

The ID of the order that's associated with the fulfillment event.

* * *

Was this section helpful?

YesNo

###

[Anchor to get-orders-order-id-fulfillments-fulfillment-id-events-examples](/docs/api/admin-rest/latest/resources/fulfillmentevent#get-orders-order-id-fulfillments-fulfillment-id-events-examples)Examples

Retrieve a list of all the fulfillment events that are associated with a specific fulfillment

Was this section helpful?

YesNo

get

## /admin/api/2026-01/orders/450789469/fulfillments/255858046/events.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469/fulfillments/255858046/events.json" \

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

HTTP/1.1 200 OK

{

"fulfillment_events": [

{

"id": 944956397,

"fulfillment_id": 255858046,

"status": "in_transit",

"message": null,

"happened_at": "2026-01-09T19:38:02-05:00",

"city": null,

"province": null,

"country": null,

"zip": null,

"address1": null,

"latitude": null,

"longitude": null,

"shop_id": 548380009,

"created_at": "2026-01-09T19:38:02-05:00",

"updated_at": "2026-01-09T19:38:02-05:00",

"estimated_delivery_at": null,

"order_id": 450789469,

"admin_graphql_api_id": "gid://shopify/FulfillmentEvent/944956397"

}

]

}

### examples

  * #### Retrieve a list of all the fulfillment events that are associated with a specific fulfillment

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469/fulfillments/255858046/events.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.FulfillmentEvent.all({
          session: session,
          order_id: 450789469,
          fulfillment_id: 255858046,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::FulfillmentEvent.all(
          session: test_session,
          order_id: 450789469,
          fulfillment_id: 255858046,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.FulfillmentEvent.all({
          session: session,
          order_id: 450789469,
          fulfillment_id: 255858046,
        });

#### response

        HTTP/1.1 200 OK{"fulfillment_events":[{"id":944956397,"fulfillment_id":255858046,"status":"in_transit","message":null,"happened_at":"2026-01-09T19:38:02-05:00","city":null,"province":null,"country":null,"zip":null,"address1":null,"latitude":null,"longitude":null,"shop_id":548380009,"created_at":"2026-01-09T19:38:02-05:00","updated_at":"2026-01-09T19:38:02-05:00","estimated_delivery_at":null,"order_id":450789469,"admin_graphql_api_id":"gid://shopify/FulfillmentEvent/944956397"}]}


* * *

##

[Anchor to GET request, Retrieves a specific fulfillment event](/docs/api/admin-rest/latest/resources/fulfillmentevent#get-orders-order-id-fulfillments-fulfillment-id-events-event-id)

get

Retrieves a specific fulfillment event

deprecated**deprecated**

Retrieves a specific fulfillment event

###

[Anchor to Parameters of Retrieves a specific fulfillment event](/docs/api/admin-rest/latest/resources/fulfillmentevent#get-orders-order-id-fulfillments-fulfillment-id-events-event-id-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

event_id

string**string**

required**required**

* * *

fulfillment_id

string**string**

required**required**

* * *

order_id

string**string**

required**required**

* * *

event_id

The ID of the fulfillment event.

* * *

Was this section helpful?

YesNo

###

[Anchor to get-orders-order-id-fulfillments-fulfillment-id-events-event-id-examples](/docs/api/admin-rest/latest/resources/fulfillmentevent#get-orders-order-id-fulfillments-fulfillment-id-events-event-id-examples)Examples

Retrieve a specific fulfillment event

Was this section helpful?

YesNo

get

## /admin/api/2026-01/orders/450789469/fulfillments/255858046/events/944956396.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469/fulfillments/255858046/events/944956396.json" \

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

"fulfillment_event": {

"id": 944956396,

"fulfillment_id": 255858046,

"status": "in_transit",

"message": null,

"happened_at": "2026-01-09T19:38:01-05:00",

"city": null,

"province": null,

"country": null,

"zip": null,

"address1": null,

"latitude": null,

"longitude": null,

"shop_id": 548380009,

"created_at": "2026-01-09T19:38:01-05:00",

"updated_at": "2026-01-09T19:38:01-05:00",

"estimated_delivery_at": null,

"order_id": 450789469,

"admin_graphql_api_id": "gid://shopify/FulfillmentEvent/944956396"

}

}

### examples

  * #### Retrieve a specific fulfillment event

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469/fulfillments/255858046/events/944956396.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.FulfillmentEvent.find({
          session: session,
          order_id: 450789469,
          fulfillment_id: 255858046,
          id: 944956396,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::FulfillmentEvent.find(
          session: test_session,
          order_id: 450789469,
          fulfillment_id: 255858046,
          id: 944956396,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.FulfillmentEvent.find({
          session: session,
          order_id: 450789469,
          fulfillment_id: 255858046,
          id: 944956396,
        });

#### response

        HTTP/1.1 200 OK{"fulfillment_event":{"id":944956396,"fulfillment_id":255858046,"status":"in_transit","message":null,"happened_at":"2026-01-09T19:38:01-05:00","city":null,"province":null,"country":null,"zip":null,"address1":null,"latitude":null,"longitude":null,"shop_id":548380009,"created_at":"2026-01-09T19:38:01-05:00","updated_at":"2026-01-09T19:38:01-05:00","estimated_delivery_at":null,"order_id":450789469,"admin_graphql_api_id":"gid://shopify/FulfillmentEvent/944956396"}}


* * *

##

[Anchor to DELETE request, Deletes a fulfillment event](/docs/api/admin-rest/latest/resources/fulfillmentevent#delete-orders-order-id-fulfillments-fulfillment-id-events-event-id)

del

Deletes a fulfillment event

deprecated**deprecated**

Deletes a fulfillment event

###

[Anchor to Parameters of Deletes a fulfillment event](/docs/api/admin-rest/latest/resources/fulfillmentevent#delete-orders-order-id-fulfillments-fulfillment-id-events-event-id-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

event_id

string**string**

required**required**

* * *

fulfillment_id

string**string**

required**required**

* * *

order_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to delete-orders-order-id-fulfillments-fulfillment-id-events-event-id-examples](/docs/api/admin-rest/latest/resources/fulfillmentevent#delete-orders-order-id-fulfillments-fulfillment-id-events-event-id-examples)Examples

Delete a fulfillment event

Was this section helpful?

YesNo

del

## /admin/api/2026-01/orders/450789469/fulfillments/255858046/events/944956395.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X DELETE "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469/fulfillments/255858046/events/944956395.json" \

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

  * #### Delete a fulfillment event

#####

        curl -X DELETE "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469/fulfillments/255858046/events/944956395.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.FulfillmentEvent.delete({
          session: session,
          order_id: 450789469,
          fulfillment_id: 255858046,
          id: 944956395,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::FulfillmentEvent.delete(
          session: test_session,
          order_id: 450789469,
          fulfillment_id: 255858046,
          id: 944956395,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.FulfillmentEvent.delete({
          session: session,
          order_id: 450789469,
          fulfillment_id: 255858046,
          id: 944956395,
        });

#### response

        HTTP/1.1 200 OK{}