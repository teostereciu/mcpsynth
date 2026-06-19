# FulfillmentOrder

*Source: https://shopify.dev/docs/api/admin-rest/2026-01/resources/fulfillmentorder*

---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04

2026-01latest

# FulfillmentOrder

Ask assistant

Multiple access scopes needed — refer to each endpoint for access scope requirements.

**Multiple access scopes needed — refer to each endpoint for access scope requirements.:**

Requires access to [protected customer data](https://shopify.dev/apps/store/data-protection/protected-customer-data).

**Requires access to [protected customer data](https://shopify.dev/apps/store/data-protection/protected-customer-data).:**

The FulfillmentOrder resource represents either an item or a group of items in an [order](/docs/admin-api/rest/reference/orders/order) that are to be fulfilled from the same location. There can be more than one fulfillment order for an [order](/docs/admin-api/rest/reference/orders/order) at a given location.

Fulfillment orders represent the work which is intended to be done in relation to an order. When the fulfillment of some or all line items has started, a [Fulfillment](https://shopify.dev/api/admin-rest/latest/resources/fulfillment) is created by a merchant or third party to represent the ongoing or completed work of fulfillment. See below for more details on creating fulfillments.

Note

Shopify creates fulfillment orders automatically when an order is created. It is not possible to manually create fulfillment orders.

See below for more details on the lifecycle of a fulfillment order.

**Note:**

Shopify creates fulfillment orders automatically when an order is created. It is not possible to manually create fulfillment orders.

See below for more details on the lifecycle of a fulfillment order.

## Retrieving fulfillment orders

##

All fulfillment orders related to a given order can be retrieved with the [Get fulfillment orders by order ID](https://shopify.dev/api/admin-rest/latest/resources/fulfillmentorder#get-orders-order-id-fulfillment-orders) endpoint. API access scopes govern which fulfillments orders are returned to clients. An API client will only receive a subset of the fulfillment orders which belong to an order if they don't have the necessary access scopes to view all of the fulfillment orders.

Fulfillment service apps can retrieve the fulfillment orders which have been assigned to their locations with the [AssignedFulfillmentOrder](/docs/api/admin-rest/latest/resources/assignedfulfillmentorder) resource. The `assignment_status` parameter in the [Retrieve a list of assigned fulfillment orders](https://shopify.dev/api/admin-rest/latest/resources/assignedfulfillmentorder#get-assigned-fulfillment-orders?assignment-status=cancellation-requested&location-ids\[\]=24826418) query controls whether all assigned fulfillment orders should be returned or only those where a merchant has sent a [fulfilment request](/docs/api/admin-rest/latest/resources/fulfillmentrequest) and it has yet to be responded to. The API client must be granted the `read_assigned_fulfillment_orders` access scope to access the assigned fulfillment orders.

A specific fulfillment order can be retrieved with the [Get fulfillment order](https://shopify.dev/api/admin-rest/latest/resources/fulfillmentorder#get-orders-order-id-fulfillment-orders) endpoint.

## The lifecycle of a fulfillment order

### Fulfillment Order Creation

After an order is created, a background worker performs the order routing process which determines which locations will be responsible for fulfilling the purchased items. Once the order routing process is complete, one or more fulfillment orders will be created and assigned to these locations. It is not possible to manually create fulfillment orders.

Once a fulfillment order has been created, it will have one of two different lifecycles depending on the type of location which the fulfillment order is assigned to.

### The lifecycle of a fulfillment order at a merchant managed location

Fulfillment orders are completed by creating [fulfillments](https://shopify.dev/api/admin-rest/latest/resources/fulfillment). Fulfillments represents the work done.

For digital products a merchant or an order management app would create a fulfilment once the digital asset has been provisioned. For example, in the case of a digital gift card, a merchant would to do this once the gift card has been activated - before the email being shipped.

On the other hand, for a traditional shipped order, a merchant or an order management app would create a fulfillment after picking and packing the items relating to a fulfillment order, but before the courier has collected the goods.

[Learn about managing fulfillment orders as an order management app](https://shopify.dev/apps/fulfillment/order-management-apps/manage-fulfillments).

### The lifecycle of a fulfillment order at a location which is managed by a fulfillment service

For fulfillment orders which are assigned to a location that is managed by a fulfillment service, a merchant or an Order Management App can [send a fulfillment request](https://shopify.dev/api/admin-rest/latest/resources/fulfillmentrequest#post-fulfillment-orders-fulfillment-order-id-fulfillment-request) to the fulfillment service which operates the location to request that they fulfill the associated items. A fulfillment service has the option to [accept](https://shopify.dev/api/admin-rest/latest/resources/fulfillmentrequest#post-fulfillment-orders-fulfillment-order-id-fulfillment-request-accept) or [reject](https://shopify.dev/api/admin-rest/latest/resources/fulfillmentrequest#post-fulfillment-orders-fulfillment-order-id-fulfillment-request-accept) this fulfillment request.

Once the fulfillment service has accepted the request, the request can no longer be cancelled by the merchant or order management app and instead a [cancellation request](https://shopify.dev/api/admin-rest/latest/resources/cancellationrequest) must be submitted to the fulfillment service.

Once a fulfillment service accepts a fulfillment request, then after they are ready to pack items and send them for delivery, they create fulfillments with the [Create a fulfillment for one or many fulfillment orders](https://shopify.dev/api/admin-rest/latest/resources/fulfillment#post-fulfillments) endpoint. They can provide tracking information right away or create fulfillments without it and then [update tracking information for fulfillments](https://shopify.dev/api/admin-rest/latest/resources/fulfillment#post-fulfillments-fulfillment-id-update-tracking).

[Learn about managing fulfillment orders as a fulfillment service](https://shopify.dev/apps/fulfillment/fulfillment-service-apps/manage-fulfillments).

## API access scopes

Fulfillment orders are governed by the following API access scopes:

  * The `read_merchant_managed_fulfillment_orders` and `write_merchant_managed_fulfillment_orders` access scopes grant access to fulfillment orders assigned to merchant-managed locations.
  * The `read_assigned_fulfillment_orders` and `write_assigned_fulfillment_orders` access scopes are intended for fulfillment services. These scopes grant access to fulfillment orders assigned to locations that are being managed by fulfillment services.
  * The `read_third_party_fulfillment_orders` and `write_third_party_fulfillment_orders` access scopes grant access to fulfillment orders assigned to locations managed by other fulfillment services.


### Fulfillment service app access scopes

Usually, **fulfillment services** have the `write_assigned_fulfillment_orders` access scope and don't have the `*_third_party_fulfillment_orders` or `*_merchant_managed_fulfillment_orders` access scopes. The app will only have access to the fulfillment orders assigned to their location (or multiple locations if the app registers multiple fulfillment services on the shop). The app will not have access to fulfillment orders assigned to merchant-managed locations or locations owned by other fulfillment service apps.

### Order management app access scopes

**Order management apps** will usually request `write_merchant_managed_fulfillment_orders` and `write_third_party_fulfillment_orders` access scopes. This will allow them to manage all fulfillment orders on behalf of a merchant.

If an app combines the functions of an order management app and a fulfillment service, then the app should request all access scopes to manage all assigned and all unassigned fulfillment orders.

## Notifications about fulfillment orders

Fulfillment services are required to [register](/docs/api/admin-rest/latest/resources/fulfillmentservice) a self-hosted callback URL which has a number of uses. One of these uses is that this callback URL will be notified whenever a merchant submits a fulfillment or cancellation request.

Both merchants and apps can [subscribe](/docs/apps/fulfillment/fulfillment-service-apps/manage-fulfillments#webhooks) to [fulfillment order webhooks](/docs/api/admin-rest/latest/resources/webhook#event-topics-fulfillment-orders-cancellation-request-accepted) to be notified whenever fulfillment order related domain events occur.

[Learn about fulfillment workflows](https://shopify.dev/apps/fulfillment).

Was this section helpful?

YesNo

#

## Endpoints

  * [post/admin/api/latest/fulfillment_orders/{fulfillment_order_id}/cancel.json](/docs/api/admin-rest/latest/resources/fulfillmentorder#post-fulfillment-orders-fulfillment-order-id-cancel)

Cancel a fulfillment order

[fulfillmentOrderCancel](/docs/api/admin-graphql/latest/mutations/fulfillmentOrderCancel?example=cancel-a-fulfillment-order)

  * [post/admin/api/latest/fulfillment_orders/{fulfillment_order_id}/close.json](/docs/api/admin-rest/latest/resources/fulfillmentorder#post-fulfillment-orders-fulfillment-order-id-close)

Marks a fulfillment order as incomplete

[fulfillmentOrderClose](/docs/api/admin-graphql/latest/mutations/fulfillmentOrderClose?example=marks-a-fulfillment-order-as-incomplete)

  * [post/admin/api/latest/fulfillment_orders/{fulfillment_order_id}/hold.json](/docs/api/admin-rest/latest/resources/fulfillmentorder#post-fulfillment-orders-fulfillment-order-id-hold)

Holds fulfillment of a fulfillment order

[fulfillmentOrderHold](/docs/api/admin-graphql/latest/mutations/fulfillmentOrderHold)

  * [post/admin/api/latest/fulfillment_orders/{fulfillment_order_id}/move.json](/docs/api/admin-rest/latest/resources/fulfillmentorder#post-fulfillment-orders-fulfillment-order-id-move)

Moves a fulfillment order to a new location

[fulfillmentOrderMove](/docs/api/admin-graphql/latest/mutations/fulfillmentOrderMove?example=moves-a-fulfillment-order-to-a-new-location)

  * [post/admin/api/latest/fulfillment_orders/{fulfillment_order_id}/open.json](/docs/api/admin-rest/latest/resources/fulfillmentorder#post-fulfillment-orders-fulfillment-order-id-open)

Marks the fulfillment order as open

[fulfillmentOrderOpen](/docs/api/admin-graphql/latest/mutations/fulfillmentOrderOpen?example=marks-the-fulfillment-order-as-open)

  * [post/admin/api/latest/fulfillment_orders/{fulfillment_order_id}/release_hold.json](/docs/api/admin-rest/latest/resources/fulfillmentorder#post-fulfillment-orders-fulfillment-order-id-release-hold)

Releases all holds on a fulfillment order

[fulfillmentOrderReleaseHold](/docs/api/admin-graphql/latest/mutations/fulfillmentOrderReleaseHold)

  * [post/admin/api/latest/fulfillment_orders/{fulfillment_order_id}/reschedule.json](/docs/api/admin-rest/latest/resources/fulfillmentorder#post-fulfillment-orders-fulfillment-order-id-reschedule)

Reschedules the fulfill_at time of a scheduled fulfillment order

[fulfillmentOrderReschedule](/docs/api/admin-graphql/latest/mutations/fulfillmentOrderReschedule?example=reschedules-the-fulfill_at-time-of-a-scheduled-fulfillment-order)

  * [post/admin/api/latest/fulfillment_orders/set_fulfillment_orders_deadline.json](/docs/api/admin-rest/latest/resources/fulfillmentorder#post-fulfillment-orders-set-fulfillment-orders-deadline)

Sets deadline for fulfillment orders

[fulfillmentOrdersSetFulfillmentDeadline](/docs/api/admin-graphql/latest/mutations/fulfillmentOrdersSetFulfillmentDeadline?example=sets-deadline-for-fulfillment-orders)

  * [get/admin/api/latest/fulfillment_orders/{fulfillment_order_id}.json](/docs/api/admin-rest/latest/resources/fulfillmentorder#get-fulfillment-orders-fulfillment-order-id)

Retrieves a specific fulfillment order

[fulfillmentOrder](/docs/api/admin-graphql/latest/queries/fulfillmentOrder?example=retrieves-a-specific-fulfillment-order)

  * [get/admin/api/latest/orders/{order_id}/fulfillment_orders.json](/docs/api/admin-rest/latest/resources/fulfillmentorder#get-orders-order-id-fulfillment-orders)

Retrieves a list of fulfillment orders for a specific order

[order](/docs/api/admin-graphql/latest/queries/order)


* * *

[Anchor to ](/docs/api/admin-rest/latest/resources/fulfillmentorder#resource-object)

## The FulfillmentOrder resource

[Anchor to ](/docs/api/admin-rest/latest/resources/fulfillmentorder#resource-object-properties)

### Properties

* * *

assigned_location_id

->[id](/docs/api/admin-graphql/latest/objects/Location#field-Location.fields.id)

The ID of the location that has been assigned to do the work.

* * *

destination

->[destination](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#field-FulfillmentOrder.fields.destination)

The destination where the items should be sent.

Show destination properties

  * **id** : The ID of the fulfillment order destination.
  * **address1** : The street address of the assigned location.
  * **address2** : An optional additional field for the street address of the assigned location.
  * **city** : The city of the destination.
  * **company** : The company of the destination.
  * **country** : The country of the destination.
  * **email** : The email of the customer at the destination.
  * **first_name** : The first name of the customer at the destination.
  * **last_name** : The last name of the customer at the destination.
  * **phone** : The phone number of the customer at the destination.
  * **province** : The province of the destination.
  * **zip** : The ZIP code of the destination.


* * *

delivery_method

->[deliveryMethod](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#field-FulfillmentOrder.fields.deliveryMethod)

The type of method used to transfer a product or service to a customer.

Show delivery_method properties

  * **id** : The ID of the delivery method.
  * **method_type** : The type of delivery method. Valid values:
    * **local** : A delivery to a customer's doorstep.
    * **none** : No delivery method.
    * **pick_up** : A delivery that a customer picks up at your retail store, curbside, or any location that you choose.
    * **retail** : Items delivered immediately in a retail store.
    * **shipping** : A delivery to a customer using a shipping carrier.
  * **min_delivery_date_time** : The minimum date and time by which the delivery is expected to be completed.
  * **max_delivery_date_time** : The maximum date and time by which the delivery is expected to be completed.
  * **additional_information** : The Additional information to consider when performing the delivery. It has the following properties:
    * **instructions** : The delivery instructions to follow when performing the delivery.
    * **phone** : The phone number to contact when performing the delivery.
  * **branded_promise** : The branded promise that was presented to the buyer during checkout. For example: Shop Promise. It has the following properties:
    * **name** : The handle of the branded promise. For example: `shop_promise`.
    * **handle** : The name of the branded promise. For example: `Shop Promise`.
  * **service_code** : A reference to the shipping method.
  * **source_reference** : Source reference is promise provider specific data associated with delivery promise.
  * **presented_name** : The name of the delivery option that was presented to the buyer during checkout.


* * *

fulfill_at

->[fulfillAt](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#field-FulfillmentOrder.fields.fulfillAt)

The date and time at which the fulfillment order will be fulfillable. When this date and time is reached, a `scheduled` fulfillment order is automatically transitioned to `open`. For example, the `fulfill_at` date for a subscription order might be the 1st of each month, a pre-order `fulfill_at` date would be `nil`, and a standard order `fulfill_at` date would be the order creation date. For more information about fulfillment statuses, refer to the **status** property.

* * *

fulfill_by

->[fulfillBy](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#field-FulfillmentOrder.fields.fulfillBy)

The latest date and time by which all items in the fulfillment order need to be fulfilled.

* * *

fulfillment_holds

->[fulfillmentHolds](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#field-FulfillmentOrder.fields.fulfillmentHolds)

Represents the fulfillment holds applied on the fulfillment order.

Show fulfillment_holds properties

  * **reason** : The reason for the fulfillment hold.
  * **reason_notes** : Additional information about the fulfillment hold reason.


* * *

id

->[id](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#field-FulfillmentOrder.fields.id)

An ID for the fulfillment order.

* * *

international_duties

->[internationalDuties](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#field-FulfillmentOrder.fields.internationalDuties)

The international duties relevant to the fulfillment order.

Show international_duties properties

  * **incoterm** : The method of duties payment. Valid values:
    * **DAP** : Delivered at place.
    * **DDP** : Delivered duty paid.


* * *

line_items

->[lineItems](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#field-FulfillmentOrder.fields.lineItems)

Represents line items belonging to a fulfillment order:

Show line_items properties

  * **id** : The ID of the fulfillment order line item.
  * **shop_id** : The ID of the shop associated with the fulfillment order line item.
  * **fulfillment_order_id** : The ID of the fulfillment order associated with this line item.
  * **line_item_id** : The ID of the line item associated with this fulfillment order line item.
  * **inventory_item_id** : The ID of the inventory item associated with this fulfillment order line item.
  * **quantity** : The total number of units to be fulfilled.
  * **fulfillable_quantity** : The number of units remaining to be fulfilled.
  * **variant_id** : The ID of the variant associated with this fulfillment order line item.


* * *

order_id

->[id](/docs/api/admin-graphql/latest/objects/Order#field-Order.fields.id)

The ID of the order that's associated with the fulfillment order.

* * *

request_status

->[requestStatus](/docs/api/admin-graphql/latest/objects/FulfillmentOrder#field-FulfillmentOrder.fields.requestStatus)

The request status of the fulfillment order. Valid values:

Show request_status properties

  * **unsubmitted** : The initial request status for newly-created fulfillment orders. This is the only valid request status for fulfillment orders that aren't assigned to a fulfillment service.
  * **submitted** : The merchant requested fulfillment for this fulfillment order.
  * **accepted** : The fulfillment service accepted the merchant's fulfillment request.
  * **rejected** : The fulfillment service rejected the merchant's fulfillment request.
  * **cancellation_requested** : The merchant requested a cancellation of the fulfillment request for this fulfillment order.
  * **cancellation_accepted** : The fulfillment service accepted the merchant's fulfillment cancellation request.
  * **cancellation_rejected** : The fulfillment service rejected the merchant's fulfillment cancellation request.
  * **closed** : The fulfillment service closed the fulfillment order without completing it.


* * *

shop_id

deprecated**deprecated**

The ID of the shop that's associated with the fulfillment order.

* * *

Show 6 hidden fields

Was this section helpful?

YesNo

{}

## The FulfillmentOrder resource

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

80

81

82

83

84

85

86

87

88

89

90

91

92

{

"assigned_location_id": 3183479,

"destination": {

"id": 54433189,

"address1": "123 Amoebobacterieae St",

"address2": "Unit 806",

"city": "Ottawa",

"company": "",

"country": "Canada",

"email": "bob@example.com",

"first_name": "Bob",

"last_name": "Bobsen",

"phone": "(555)555-5555",

"province": "Ontario",

"zip": "K2P0V6"

},

"delivery_method": {

"id": 64434189,

"method_type": "local",

"min_delivery_date_time": "2022-04-20T23:59:59-04:00",

"max_delivery_date_time": "2022-04-28T23:59:59-04:00",

"additional_information": {

"instructions": "Leave at door",

"phone": "111-111-1111"

},

"service_code": "Economy",

"source_reference": "Shopify",

"branded_promise": {

"name": "Shop Promise",

"handle": "shop_promise"

},

"presented_name": "Economy"

},

"fulfill_at": "2021-01-01",

"fulfill_by": "2021-01-01",

"fulfillment_holds": [

{

"reason": "incorrect_address",

"reason_notes": "the apartment number is missing."

}

],

"id": 255858046,

"international_duties": {

"incoterm": "DAP"

},

"line_items": [

{

"id": 466157049,

"shop_id": 3998762,

"fulfillment_order_id": 1568020,

"line_item_id": 466157049,

"inventory_item_id": 6588097,

"quantity": 1,

"fulfillable_quantity": 1,

"variant_id": 2385087

}

],

"order_id": 3183479,

"request_status": "unsubmitted",

"shop_id": 255858046,

"status": "open",

"supported_actions": [

"create_fulfillment",

"request_fulfillment",

"cancel_fulfillment_order",

"request_cancellation"

],

"merchant_requests": [

{

"message": "Hello, World!",

"request_options": {

"shipping_method": "pidgeon carrier",

"note": "handle with care",

"date": "2019-08-13T16:09:58-04:00"

},

"kind": "fulfillment_request"

}

],

"assigned_location": {

"address1": "123 Amoebobacterieae St",

"address2": "Unit 806",

"city": "Ottawa",

"country_code": "CA",

"location_id": 17232953366,

"name": "Bob Bobsen",

"phone": "(555)555-5555",

"province": "Ontario",

"zip": "K2P0V6"

},

"created_at": "2022-01-01T11:00:00-01:00",

"updated_at": "2022-01-01T11:00:00-01:00"

}

* * *

##

[Anchor to POST request, Cancel a fulfillment order](/docs/api/admin-rest/latest/resources/fulfillmentorder#post-fulfillment-orders-fulfillment-order-id-cancel)

post

Cancel a fulfillment order

[fulfillmentOrderCancel](/docs/api/admin-graphql/latest/mutations/fulfillmentOrderCancel?example=cancel-a-fulfillment-order)

Marks a fulfillment order as cancelled.

###

[Anchor to Parameters of Cancel a fulfillment order](/docs/api/admin-rest/latest/resources/fulfillmentorder#post-fulfillment-orders-fulfillment-order-id-cancel-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

fulfillment_order_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to post-fulfillment-orders-fulfillment-order-id-cancel-examples](/docs/api/admin-rest/latest/resources/fulfillmentorder#post-fulfillment-orders-fulfillment-order-id-cancel-examples)Examples

Cancel a fulfillment order

Path parameters

fulfillment_order_id=1046000839

string**string**

required**required**

Was this section helpful?

YesNo

post

## /admin/api/2026-01/fulfillment_orders/1046000839/cancel.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{}' \

-X POST "https://your-development-store.myshopify.com/admin/api/2026-01/fulfillment_orders/1046000839/cancel.json" \

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

80

81

82

83

84

85

86

87

88

89

90

91

92

93

94

95

96

97

98

99

100

101

102

103

104

HTTP/1.1 200 OK

{

"fulfillment_order": {

"id": 1046000839,

"created_at": "2026-01-09T17:30:24-05:00",

"updated_at": "2026-01-09T17:30:25-05:00",

"shop_id": 548380009,

"order_id": 450789469,

"assigned_location_id": 24826418,

"request_status": "submitted",

"status": "closed",

"fulfill_at": null,

"fulfill_by": null,

"supported_actions": [],

"destination": {

"id": 1042572162,

"address1": "Chestnut Street 92",

"address2": "",

"city": "Louisville",

"company": null,

"country": "United States",

"email": "bob.norman@mail.example.com",

"first_name": "Bob",

"last_name": "Norman",

"phone": "+1(502)-459-2181",

"province": "Kentucky",

"zip": "40202"

},

"line_items": [],

"international_duties": null,

"fulfillment_holds": [],

"delivery_method": null,

"assigned_location": {

"address1": null,

"address2": null,

"city": null,

"country_code": "DE",

"location_id": 24826418,

"name": "Apple Api Shipwire",

"phone": null,

"province": null,

"zip": null

},

"merchant_requests": []

},

"replacement_fulfillment_order": {

"id": 1046000840,

"created_at": "2026-01-09T17:30:25-05:00",

"updated_at": "2026-01-09T17:30:25-05:00",

"shop_id": 548380009,

"order_id": 450789469,

"assigned_location_id": 24826418,

"request_status": "unsubmitted",

"status": "open",

"fulfill_at": null,

"fulfill_by": null,

"supported_actions": [

"request_fulfillment",

"create_fulfillment",

"hold"

],

"destination": {

"id": 1042572163,

"address1": "Chestnut Street 92",

"address2": "",

"city": "Louisville",

"company": null,

"country": "United States",

"email": "bob.norman@mail.example.com",

"first_name": "Bob",

"last_name": "Norman",

"phone": "+1(502)-459-2181",

"province": "Kentucky",

"zip": "40202"

},

"line_items": [

{

"id": 1072503351,

"shop_id": 548380009,

"fulfillment_order_id": 1046000840,

"quantity": 1,

"line_item_id": 518995019,

"inventory_item_id": 49148385,

"fulfillable_quantity": 1,

"variant_id": 49148385

}

],

"international_duties": null,

"fulfillment_holds": [],

"delivery_method": null,

"assigned_location": {

"address1": null,

"address2": null,

"city": null,

"country_code": "DE",

"location_id": 24826418,

"name": "Apple Api Shipwire",

"phone": null,

"province": null,

"zip": null

},

"merchant_requests": []

}

}

### examples

  * #### Cancel a fulfillment order

#####

        curl -d '{}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/fulfillment_orders/1046000839/cancel.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const fulfillment_order = new admin.rest.resources.FulfillmentOrder({session: session});

        fulfillment_order.id = 1046000839;
        await fulfillment_order.cancel({});

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        fulfillment_order = ShopifyAPI::FulfillmentOrder.new(session: test_session)
        fulfillment_order.id = 1046000839
        fulfillment_order.cancel(
          session: test_session,
        )

#####

        // Session is built by the OAuth process

        const fulfillment_order = new shopify.rest.FulfillmentOrder({session: session});
        fulfillment_order.id = 1046000839;
        await fulfillment_order.cancel({});

#### response

        HTTP/1.1 200 OK{"fulfillment_order":{"id":1046000839,"created_at":"2026-01-09T17:30:24-05:00","updated_at":"2026-01-09T17:30:25-05:00","shop_id":548380009,"order_id":450789469,"assigned_location_id":24826418,"request_status":"submitted","status":"closed","fulfill_at":null,"fulfill_by":null,"supported_actions":[],"destination":{"id":1042572162,"address1":"Chestnut Street 92","address2":"","city":"Louisville","company":null,"country":"United States","email":"bob.norman@mail.example.com","first_name":"Bob","last_name":"Norman","phone":"+1(502)-459-2181","province":"Kentucky","zip":"40202"},"line_items":[],"international_duties":null,"fulfillment_holds":[],"delivery_method":null,"assigned_location":{"address1":null,"address2":null,"city":null,"country_code":"DE","location_id":24826418,"name":"Apple Api Shipwire","phone":null,"province":null,"zip":null},"merchant_requests":[]},"replacement_fulfillment_order":{"id":1046000840,"created_at":"2026-01-09T17:30:25-05:00","updated_at":"2026-01-09T17:30:25-05:00","shop_id":548380009,"order_id":450789469,"assigned_location_id":24826418,"request_status":"unsubmitted","status":"open","fulfill_at":null,"fulfill_by":null,"supported_actions":["request_fulfillment","create_fulfillment","hold"],"destination":{"id":1042572163,"address1":"Chestnut Street 92","address2":"","city":"Louisville","company":null,"country":"United States","email":"bob.norman@mail.example.com","first_name":"Bob","last_name":"Norman","phone":"+1(502)-459-2181","province":"Kentucky","zip":"40202"},"line_items":[{"id":1072503351,"shop_id":548380009,"fulfillment_order_id":1046000840,"quantity":1,"line_item_id":518995019,"inventory_item_id":49148385,"fulfillable_quantity":1,"variant_id":49148385}],"international_duties":null,"fulfillment_holds":[],"delivery_method":null,"assigned_location":{"address1":null,"address2":null,"city":null,"country_code":"DE","location_id":24826418,"name":"Apple Api Shipwire","phone":null,"province":null,"zip":null},"merchant_requests":[]}}


* * *

##

[Anchor to POST request, Marks a fulfillment order as incomplete](/docs/api/admin-rest/latest/resources/fulfillmentorder#post-fulfillment-orders-fulfillment-order-id-close)

post

Marks a fulfillment order as incomplete

[fulfillmentOrderClose](/docs/api/admin-graphql/latest/mutations/fulfillmentOrderClose?example=marks-a-fulfillment-order-as-incomplete)

Requires `assigned_fulfillment_orders` access scope.

**Requires `assigned_fulfillment_orders` access scope.:**

Marks an in-progress fulfillment order as incomplete, indicating the fulfillment service is unable to ship any remaining items, and closes the fulfillment request.

This mutation can only be called for fulfillment orders that meet the following criteria:

  * Assigned to a fulfillment service location,
  * The fulfillment request has been accepted,
  * The fulfillment order status is `IN_PROGRESS`.

This mutation can only be called by the fulfillment service app that accepted the fulfillment request. Calling this mutation returns the control of the fulfillment order to the merchant, allowing them to move the fulfillment order line items to another location and fulfill from there, remove and refund the line items, or to request fulfillment from the same fulfillment service again.

Closing a fulfillment order is explained in [the fulfillment service guide](https://shopify.dev/apps/build/orders-fulfillment/fulfillment-service-apps/build-for-fulfillment-services#step-7-optional-close-a-fulfillment-order).

###

[Anchor to Parameters of Marks a fulfillment order as incomplete](/docs/api/admin-rest/latest/resources/fulfillmentorder#post-fulfillment-orders-fulfillment-order-id-close-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

fulfillment_order_id

string**string**

required**required**

* * *

message

An optional reason for marking the fulfillment order as incomplete.

* * *

Was this section helpful?

YesNo

###

[Anchor to post-fulfillment-orders-fulfillment-order-id-close-examples](/docs/api/admin-rest/latest/resources/fulfillmentorder#post-fulfillment-orders-fulfillment-order-id-close-examples)Examples

Transition a fulfillment order from in progress to incomplete

Path parameters

fulfillment_order_id=1046000831

string**string**

required**required**

Was this section helpful?

YesNo

post

## /admin/api/2026-01/fulfillment_orders/1046000831/close.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{"fulfillment_order":{"message":"Not enough inventory to complete this work."}}' \

-X POST "https://your-development-store.myshopify.com/admin/api/2026-01/fulfillment_orders/1046000831/close.json" \

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

HTTP/1.1 200 OK

{

"fulfillment_order": {

"id": 1046000831,

"created_at": "2026-01-09T17:30:06-05:00",

"updated_at": "2026-01-09T17:30:07-05:00",

"shop_id": 548380009,

"order_id": 450789469,

"assigned_location_id": 24826418,

"request_status": "closed",

"status": "incomplete",

"fulfill_at": null,

"fulfill_by": null,

"supported_actions": [

"request_fulfillment",

"create_fulfillment",

"hold"

],

"destination": {

"id": 1042572154,

"address1": "Chestnut Street 92",

"address2": "",

"city": "Louisville",

"company": null,

"country": "United States",

"email": "bob.norman@mail.example.com",

"first_name": "Bob",

"last_name": "Norman",

"phone": "+1(502)-459-2181",

"province": "Kentucky",

"zip": "40202"

},

"line_items": [

{

"id": 1072503343,

"shop_id": 548380009,

"fulfillment_order_id": 1046000831,

"quantity": 1,

"line_item_id": 518995019,

"inventory_item_id": 49148385,

"fulfillable_quantity": 1,

"variant_id": 49148385

}

],

"international_duties": null,

"fulfillment_holds": [],

"delivery_method": null,

"assigned_location": {

"address1": null,

"address2": null,

"city": null,

"country_code": "DE",

"location_id": 24826418,

"name": "Apple Api Shipwire",

"phone": null,

"province": null,

"zip": null

},

"merchant_requests": []

}

}

### examples

  * #### Transition a fulfillment order from in progress to incomplete

#####

        curl -d '{"fulfillment_order":{"message":"Not enough inventory to complete this work."}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/fulfillment_orders/1046000831/close.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const fulfillment_order = new admin.rest.resources.FulfillmentOrder({session: session});

        fulfillment_order.id = 1046000831;
        await fulfillment_order.close({
          body: {"fulfillment_order": {"message": "Not enough inventory to complete this work."}},
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        fulfillment_order = ShopifyAPI::FulfillmentOrder.new(session: test_session)
        fulfillment_order.id = 1046000831
        fulfillment_order.close(
          session: test_session,
          body: {"fulfillment_order" => {"message" => "Not enough inventory to complete this work."}},
        )

#####

        // Session is built by the OAuth process

        const fulfillment_order = new shopify.rest.FulfillmentOrder({session: session});
        fulfillment_order.id = 1046000831;
        await fulfillment_order.close({
          body: {"fulfillment_order": {"message": "Not enough inventory to complete this work."}},
        });

#### response

        HTTP/1.1 200 OK{"fulfillment_order":{"id":1046000831,"created_at":"2026-01-09T17:30:06-05:00","updated_at":"2026-01-09T17:30:07-05:00","shop_id":548380009,"order_id":450789469,"assigned_location_id":24826418,"request_status":"closed","status":"incomplete","fulfill_at":null,"fulfill_by":null,"supported_actions":["request_fulfillment","create_fulfillment","hold"],"destination":{"id":1042572154,"address1":"Chestnut Street 92","address2":"","city":"Louisville","company":null,"country":"United States","email":"bob.norman@mail.example.com","first_name":"Bob","last_name":"Norman","phone":"+1(502)-459-2181","province":"Kentucky","zip":"40202"},"line_items":[{"id":1072503343,"shop_id":548380009,"fulfillment_order_id":1046000831,"quantity":1,"line_item_id":518995019,"inventory_item_id":49148385,"fulfillable_quantity":1,"variant_id":49148385}],"international_duties":null,"fulfillment_holds":[],"delivery_method":null,"assigned_location":{"address1":null,"address2":null,"city":null,"country_code":"DE","location_id":24826418,"name":"Apple Api Shipwire","phone":null,"province":null,"zip":null},"merchant_requests":[]}}


* * *

##

[Anchor to POST request, Holds fulfillment of a fulfillment order](/docs/api/admin-rest/latest/resources/fulfillmentorder#post-fulfillment-orders-fulfillment-order-id-hold)

post

Holds fulfillment of a fulfillment order

[fulfillmentOrderHold](/docs/api/admin-graphql/latest/mutations/fulfillmentOrderHold)

Halts all fulfillment work on a fulfillment order. Changes the fulfillment order status to `ON_HOLD` and creates a fulfillment hold.

###

[Anchor to Parameters of Holds fulfillment of a fulfillment order](/docs/api/admin-rest/latest/resources/fulfillmentorder#post-fulfillment-orders-fulfillment-order-id-hold-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

fulfillment_hold

object**object**

required**required**

An object containing

Show fulfillment_hold properties

  * `reason`: (String) **required** A reason for the fulfillment hold.
    * `awaiting_payment` The fulfillment hold is applied because payment is pending.
    * `high_risk_of_fraud` The fulfillment hold is applied because of a high risk of fraud.
    * `incorrect_address` The fulfillment hold is applied because of an incorrect address.
    * `inventory_out_of_stock` The fulfillment hold is applied because inventory is out of stock.
    * `other` The fulfillment hold is applied for any other reason.
  * `reason_notes`: (String) **optional** Additional information about the fulfillment hold reason.
  * `notify_merchant`: (Boolean) **optional** Whether the merchant should receive a notification about the fulfillment hold. " "If set to true, then the merchant will be notified on the Shopify mobile app " "(if they use it to manage their store). The default value is false.
  * `fulfillment_order_line_items`: (Array) An **optional** array of fulfillment order line item ids and the quantity of each to move. **Added as of version 2023-04**


* * *

fulfillment_order_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to post-fulfillment-orders-fulfillment-order-id-hold-examples](/docs/api/admin-rest/latest/resources/fulfillmentorder#post-fulfillment-orders-fulfillment-order-id-hold-examples)Examples

Apply a fulfillment hold on a fulfillment order because some inventory is out of stock

Path parameters

fulfillment_order_id=1046000836

string**string**

required**required**

Request body

fulfillment_hold

Fulfillment_hold resource**Fulfillment_hold resource**

Show fulfillment_hold properties

fulfillment_hold:{"reason":"inventory_out_of_stock","reason_notes":"Not enough inventory to complete this work.","fulfillment_order_line_items":[{"id":1072503348,"quantity":1}]}

object**object**

required**required**

An object containing

Show fulfillment_hold properties

  * `reason`: (String) **required** A reason for the fulfillment hold.
    * `awaiting_payment` The fulfillment hold is applied because payment is pending.
    * `high_risk_of_fraud` The fulfillment hold is applied because of a high risk of fraud.
    * `incorrect_address` The fulfillment hold is applied because of an incorrect address.
    * `inventory_out_of_stock` The fulfillment hold is applied because inventory is out of stock.
    * `other` The fulfillment hold is applied for any other reason.
  * `reason_notes`: (String) **optional** Additional information about the fulfillment hold reason.
  * `notify_merchant`: (Boolean) **optional** Whether the merchant should receive a notification about the fulfillment hold. " "If set to true, then the merchant will be notified on the Shopify mobile app " "(if they use it to manage their store). The default value is false.
  * `fulfillment_order_line_items`: (Array) An **optional** array of fulfillment order line item ids and the quantity of each to move. **Added as of version 2023-04**


Was this section helpful?

YesNo

post

## /admin/api/2026-01/fulfillment_orders/1046000836/hold.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{"fulfillment_hold":{"reason":"inventory_out_of_stock","reason_notes":"Not enough inventory to complete this work.","fulfillment_order_line_items":[{"id":1072503348,"quantity":1}]}}' \

-X POST "https://your-development-store.myshopify.com/admin/api/2026-01/fulfillment_orders/1046000836/hold.json" \

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

HTTP/1.1 200 OK

{

"fulfillment_order": {

"id": 1046000836,

"created_at": "2026-01-09T17:30:16-05:00",

"updated_at": "2026-01-09T17:30:19-05:00",

"shop_id": 548380009,

"order_id": 450789469,

"assigned_location_id": 24826418,

"request_status": "unsubmitted",

"status": "on_hold",

"fulfill_at": null,

"fulfill_by": null,

"supported_actions": [

"release_hold",

"hold"

],

"destination": {

"id": 1042572159,

"address1": "Chestnut Street 92",

"address2": "",

"city": "Louisville",

"company": null,

"country": "United States",

"email": "bob.norman@mail.example.com",

"first_name": "Bob",

"last_name": "Norman",

"phone": "+1(502)-459-2181",

"province": "Kentucky",

"zip": "40202"

},

"line_items": [

{

"id": 1072503348,

"shop_id": 548380009,

"fulfillment_order_id": 1046000836,

"quantity": 1,

"line_item_id": 518995019,

"inventory_item_id": 49148385,

"fulfillable_quantity": 1,

"variant_id": 49148385

}

],

"international_duties": null,

"fulfillment_holds": [

{

"reason": "inventory_out_of_stock",

"reason_notes": "Not enough inventory to complete this work."

}

],

"delivery_method": null,

"assigned_location": {

"address1": null,

"address2": null,

"city": null,

"country_code": "DE",

"location_id": 24826418,

"name": "Apple Api Shipwire",

"phone": null,

"province": null,

"zip": null

},

"merchant_requests": []

}

}

### examples

  * #### Apply a fulfillment hold on a fulfillment order because some inventory is out of stock

#####

        curl -d '{"fulfillment_hold":{"reason":"inventory_out_of_stock","reason_notes":"Not enough inventory to complete this work.","fulfillment_order_line_items":[{"id":1072503348,"quantity":1}]}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/fulfillment_orders/1046000836/hold.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const fulfillment_order = new admin.rest.resources.FulfillmentOrder({session: session});

        fulfillment_order.id = 1046000836;
        await fulfillment_order.hold({
          body: {"fulfillment_hold": {"reason": "inventory_out_of_stock", "reason_notes": "Not enough inventory to complete this work.", "fulfillment_order_line_items": [{"id": 1072503348, "quantity": 1}]}},
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        fulfillment_order = ShopifyAPI::FulfillmentOrder.new(session: test_session)
        fulfillment_order.id = 1046000836
        fulfillment_order.hold(
          session: test_session,
          body: {"fulfillment_hold" => {"reason" => "inventory_out_of_stock", "reason_notes" => "Not enough inventory to complete this work.", "fulfillment_order_line_items" => [{"id" => 1072503348, "quantity" => 1}]}},
        )

#####

        // Session is built by the OAuth process

        const fulfillment_order = new shopify.rest.FulfillmentOrder({session: session});
        fulfillment_order.id = 1046000836;
        await fulfillment_order.hold({
          body: {"fulfillment_hold": {"reason": "inventory_out_of_stock", "reason_notes": "Not enough inventory to complete this work.", "fulfillment_order_line_items": [{"id": 1072503348, "quantity": 1}]}},
        });

#### response

        HTTP/1.1 200 OK{"fulfillment_order":{"id":1046000836,"created_at":"2026-01-09T17:30:16-05:00","updated_at":"2026-01-09T17:30:19-05:00","shop_id":548380009,"order_id":450789469,"assigned_location_id":24826418,"request_status":"unsubmitted","status":"on_hold","fulfill_at":null,"fulfill_by":null,"supported_actions":["release_hold","hold"],"destination":{"id":1042572159,"address1":"Chestnut Street 92","address2":"","city":"Louisville","company":null,"country":"United States","email":"bob.norman@mail.example.com","first_name":"Bob","last_name":"Norman","phone":"+1(502)-459-2181","province":"Kentucky","zip":"40202"},"line_items":[{"id":1072503348,"shop_id":548380009,"fulfillment_order_id":1046000836,"quantity":1,"line_item_id":518995019,"inventory_item_id":49148385,"fulfillable_quantity":1,"variant_id":49148385}],"international_duties":null,"fulfillment_holds":[{"reason":"inventory_out_of_stock","reason_notes":"Not enough inventory to complete this work."}],"delivery_method":null,"assigned_location":{"address1":null,"address2":null,"city":null,"country_code":"DE","location_id":24826418,"name":"Apple Api Shipwire","phone":null,"province":null,"zip":null},"merchant_requests":[]}}


* * *

##

[Anchor to POST request, Moves a fulfillment order to a new location](/docs/api/admin-rest/latest/resources/fulfillmentorder#post-fulfillment-orders-fulfillment-order-id-move)

post

Moves a fulfillment order to a new location

[fulfillmentOrderMove](/docs/api/admin-graphql/latest/mutations/fulfillmentOrderMove?example=moves-a-fulfillment-order-to-a-new-location)

Requires ANY of the following access scopes: `merchant_managed_fulfillment_orders`, `third_party_fulfillment_orders`.

**Requires ANY of the following access scopes: `merchant_managed_fulfillment_orders`, `third_party_fulfillment_orders`.:**

Changes the location which is assigned to fulfill a number of unfulfilled fulfillment order line items.
Moving a fulfillment order will fail in the following circumstances:

  * The fulfillment order is closed.
  * The destination location has never stocked the requested inventory item.
  * The API client doesn't have the correct permissions.


Line items which have already been fulfilled can't be re-assigned and will always remain assigned to the original location.

You can't change the assigned location while a fulfillment order has a `request_status` of `submitted`, `accepted`, `cancellation_requested`, or `cancellation_rejected`. These request statuses mean that a fulfillment order is awaiting action by a fulfillment service and can't be re-assigned without first having the fulfillment service accept a cancellation request. This behavior is intended to prevent items from being fulfilled by multiple locations or fulfillment services.

#### How re-assigning line items affects fulfillment orders

If the original fulfillment order doesn't have any line items which are fully or partially fulfilled, the original fulfillment order will be moved to the new location. However if this isn't the case, the moved fulfillment order will differ from the original one.

#### Response

  * `original_fulfillment_order` \- The final state of the original fulfillment order.
As a result of the move operation, the original fulfillment order might be moved to the new location or remain in the original location. The original fulfillment order might have the same status or be closed.
  * `moved_fulfillment_order` \- The fulfillment order which now contains the moved line items and is assigned to the destination location.
**First scenario:** All line items belonging to the original fulfillment order are re-assigned.
In this case, this will be the original fulfillment order.
**Second scenario:** A subset of the line items belonging to the original fulfillment order are re-assigned.
If the new location is already assigned to fulfill line items on the order, then this will be an existing active fulfillment order. Otherwise, this will be a new fulfillment order with the moved line items assigned.
  * `remaining_fulfillment_order` \- this field is deprecated.


###

[Anchor to Parameters of Moves a fulfillment order to a new location](/docs/api/admin-rest/latest/resources/fulfillmentorder#post-fulfillment-orders-fulfillment-order-id-move-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

fulfillment_order

[](/apps/store/data-protection/protected-customer-data)

object**object**

required**required**

An object containing

Show fulfillment_order properties

  * `new_location_id`: (integer) The ID of the location where the fulfillment order will be moved.
  * `fulfillment_order_line_items`: (Array) An **optional** array of fulfillment order line item ids and the quantity of each to move. If left blank, all unfulfilled line items belonging to the fulfillment order are moved. **Added as of version 2023-04**.


* * *

fulfillment_order_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to post-fulfillment-orders-fulfillment-order-id-move-examples](/docs/api/admin-rest/latest/resources/fulfillmentorder#post-fulfillment-orders-fulfillment-order-id-move-examples)Examples

Move a fulfillment order to a new location

Path parameters

fulfillment_order_id=1046000832

string**string**

required**required**

Request body

fulfillment_order[](/apps/store/data-protection/protected-customer-data)

Fulfillment_order resource**Fulfillment_order resource**

Show fulfillment_order properties

fulfillment_order:{"new_location_id":655441491,"fulfillment_order_line_items":[{"id":1072503344,"quantity":1}]}[](/apps/store/data-protection/protected-customer-data)

object**object**

required**required**

An object containing

Show fulfillment_order properties

  * `new_location_id`: (integer) The ID of the location where the fulfillment order will be moved.
  * `fulfillment_order_line_items`: (Array) An **optional** array of fulfillment order line item ids and the quantity of each to move. If left blank, all unfulfilled line items belonging to the fulfillment order are moved. **Added as of version 2023-04**.


Was this section helpful?

YesNo

post

## /admin/api/2026-01/fulfillment_orders/1046000832/move.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{"fulfillment_order":{"new_location_id":655441491,"fulfillment_order_line_items":[{"id":1072503344,"quantity":1}]}}' \

-X POST "https://your-development-store.myshopify.com/admin/api/2026-01/fulfillment_orders/1046000832/move.json" \

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

80

81

82

83

84

85

86

87

88

89

90

91

92

93

94

95

96

97

98

99

100

101

102

103

104

105

106

107

108

109

110

111

112

113

114

115

116

117

118

119

120

HTTP/1.1 200 OK

{

"original_fulfillment_order": {

"id": 1046000832,

"created_at": "2026-01-09T17:30:08-05:00",

"updated_at": "2026-01-09T17:30:10-05:00",

"shop_id": 548380009,

"order_id": 450789469,

"assigned_location_id": 655441491,

"request_status": "unsubmitted",

"status": "open",

"fulfill_at": null,

"fulfill_by": null,

"supported_actions": [

"create_fulfillment",

"move",

"hold"

],

"destination": {

"id": 1042572155,

"address1": "Chestnut Street 92",

"address2": "",

"city": "Louisville",

"company": null,

"country": "United States",

"email": "bob.norman@mail.example.com",

"first_name": "Bob",

"last_name": "Norman",

"phone": "+1(502)-459-2181",

"province": "Kentucky",

"zip": "40202"

},

"line_items": [

{

"id": 1072503344,

"shop_id": 548380009,

"fulfillment_order_id": 1046000832,

"quantity": 1,

"line_item_id": 518995019,

"inventory_item_id": 49148385,

"fulfillable_quantity": 1,

"variant_id": 49148385

}

],

"international_duties": null,

"fulfillment_holds": [],

"delivery_method": null,

"assigned_location": {

"address1": "50 Rideau Street",

"address2": null,

"city": "Ottawa",

"country_code": "CA",

"location_id": 655441491,

"name": "50 Rideau Street",

"phone": null,

"province": "Ontario",

"zip": "K1N 9J7"

},

"merchant_requests": []

},

"moved_fulfillment_order": {

"id": 1046000832,

"created_at": "2026-01-09T17:30:08-05:00",

"updated_at": "2026-01-09T17:30:10-05:00",

"shop_id": 548380009,

"order_id": 450789469,

"assigned_location_id": 655441491,

"request_status": "unsubmitted",

"status": "open",

"fulfill_at": null,

"fulfill_by": null,

"supported_actions": [

"create_fulfillment",

"move",

"hold"

],

"destination": {

"id": 1042572155,

"address1": "Chestnut Street 92",

"address2": "",

"city": "Louisville",

"company": null,

"country": "United States",

"email": "bob.norman@mail.example.com",

"first_name": "Bob",

"last_name": "Norman",

"phone": "+1(502)-459-2181",

"province": "Kentucky",

"zip": "40202"

},

"line_items": [

{

"id": 1072503344,

"shop_id": 548380009,

"fulfillment_order_id": 1046000832,

"quantity": 1,

"line_item_id": 518995019,

"inventory_item_id": 49148385,

"fulfillable_quantity": 1,

"variant_id": 49148385

}

],

"international_duties": null,

"fulfillment_holds": [],

"delivery_method": null,

"assigned_location": {

"address1": "50 Rideau Street",

"address2": null,

"city": "Ottawa",

"country_code": "CA",

"location_id": 655441491,

"name": "50 Rideau Street",

"phone": null,

"province": "Ontario",

"zip": "K1N 9J7"

},

"merchant_requests": []

},

"remaining_fulfillment_order": null

}

### examples

  * #### Move a fulfillment order to a new location

#####

        curl -d '{"fulfillment_order":{"new_location_id":655441491,"fulfillment_order_line_items":[{"id":1072503344,"quantity":1}]}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/fulfillment_orders/1046000832/move.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const fulfillment_order = new admin.rest.resources.FulfillmentOrder({session: session});

        fulfillment_order.id = 1046000832;
        await fulfillment_order.move({
          body: {"fulfillment_order": {"new_location_id": 655441491, "fulfillment_order_line_items": [{"id": 1072503344, "quantity": 1}]}},
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        fulfillment_order = ShopifyAPI::FulfillmentOrder.new(session: test_session)
        fulfillment_order.id = 1046000832
        fulfillment_order.move(
          session: test_session,
          body: {"fulfillment_order" => {"new_location_id" => 655441491, "fulfillment_order_line_items" => [{"id" => 1072503344, "quantity" => 1}]}},
        )

#####

        // Session is built by the OAuth process

        const fulfillment_order = new shopify.rest.FulfillmentOrder({session: session});
        fulfillment_order.id = 1046000832;
        await fulfillment_order.move({
          body: {"fulfillment_order": {"new_location_id": 655441491, "fulfillment_order_line_items": [{"id": 1072503344, "quantity": 1}]}},
        });

#### response

        HTTP/1.1 200 OK{"original_fulfillment_order":{"id":1046000832,"created_at":"2026-01-09T17:30:08-05:00","updated_at":"2026-01-09T17:30:10-05:00","shop_id":548380009,"order_id":450789469,"assigned_location_id":655441491,"request_status":"unsubmitted","status":"open","fulfill_at":null,"fulfill_by":null,"supported_actions":["create_fulfillment","move","hold"],"destination":{"id":1042572155,"address1":"Chestnut Street 92","address2":"","city":"Louisville","company":null,"country":"United States","email":"bob.norman@mail.example.com","first_name":"Bob","last_name":"Norman","phone":"+1(502)-459-2181","province":"Kentucky","zip":"40202"},"line_items":[{"id":1072503344,"shop_id":548380009,"fulfillment_order_id":1046000832,"quantity":1,"line_item_id":518995019,"inventory_item_id":49148385,"fulfillable_quantity":1,"variant_id":49148385}],"international_duties":null,"fulfillment_holds":[],"delivery_method":null,"assigned_location":{"address1":"50 Rideau Street","address2":null,"city":"Ottawa","country_code":"CA","location_id":655441491,"name":"50 Rideau Street","phone":null,"province":"Ontario","zip":"K1N 9J7"},"merchant_requests":[]},"moved_fulfillment_order":{"id":1046000832,"created_at":"2026-01-09T17:30:08-05:00","updated_at":"2026-01-09T17:30:10-05:00","shop_id":548380009,"order_id":450789469,"assigned_location_id":655441491,"request_status":"unsubmitted","status":"open","fulfill_at":null,"fulfill_by":null,"supported_actions":["create_fulfillment","move","hold"],"destination":{"id":1042572155,"address1":"Chestnut Street 92","address2":"","city":"Louisville","company":null,"country":"United States","email":"bob.norman@mail.example.com","first_name":"Bob","last_name":"Norman","phone":"+1(502)-459-2181","province":"Kentucky","zip":"40202"},"line_items":[{"id":1072503344,"shop_id":548380009,"fulfillment_order_id":1046000832,"quantity":1,"line_item_id":518995019,"inventory_item_id":49148385,"fulfillable_quantity":1,"variant_id":49148385}],"international_duties":null,"fulfillment_holds":[],"delivery_method":null,"assigned_location":{"address1":"50 Rideau Street","address2":null,"city":"Ottawa","country_code":"CA","location_id":655441491,"name":"50 Rideau Street","phone":null,"province":"Ontario","zip":"K1N 9J7"},"merchant_requests":[]},"remaining_fulfillment_order":null}


* * *

##

[Anchor to POST request, Marks the fulfillment order as open](/docs/api/admin-rest/latest/resources/fulfillmentorder#post-fulfillment-orders-fulfillment-order-id-open)

post

Marks the fulfillment order as open

[fulfillmentOrderOpen](/docs/api/admin-graphql/latest/mutations/fulfillmentOrderOpen?example=marks-the-fulfillment-order-as-open)

Requires ANY of the following access scopes: `merchant_managed_fulfillment_orders`, `third_party_fulfillment_orders`.

**Requires ANY of the following access scopes: `merchant_managed_fulfillment_orders`, `third_party_fulfillment_orders`.:**

Marks a scheduled fulfillment order as ready for fulfillment. This endpoint allows merchants to work on a scheduled fulfillment order before its expected `fulfill_at` datetime.

###

[Anchor to Parameters of Marks the fulfillment order as open](/docs/api/admin-rest/latest/resources/fulfillmentorder#post-fulfillment-orders-fulfillment-order-id-open-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

fulfillment_order_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to post-fulfillment-orders-fulfillment-order-id-open-examples](/docs/api/admin-rest/latest/resources/fulfillmentorder#post-fulfillment-orders-fulfillment-order-id-open-examples)Examples

Transition a fulfillment order from scheduled to open

Path parameters

fulfillment_order_id=1046000825

string**string**

required**required**

Was this section helpful?

YesNo

post

## /admin/api/2026-01/fulfillment_orders/1046000825/open.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{}' \

-X POST "https://your-development-store.myshopify.com/admin/api/2026-01/fulfillment_orders/1046000825/open.json" \

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

HTTP/1.1 200 OK

{

"fulfillment_order": {

"id": 1046000825,

"created_at": "2026-01-09T17:29:55-05:00",

"updated_at": "2026-01-09T17:29:57-05:00",

"shop_id": 548380009,

"order_id": 450789469,

"assigned_location_id": 24826418,

"request_status": "unsubmitted",

"status": "open",

"fulfill_at": null,

"fulfill_by": null,

"supported_actions": [

"request_fulfillment",

"create_fulfillment",

"hold"

],

"destination": {

"id": 1042572148,

"address1": "Chestnut Street 92",

"address2": "",

"city": "Louisville",

"company": null,

"country": "United States",

"email": "bob.norman@mail.example.com",

"first_name": "Bob",

"last_name": "Norman",

"phone": "+1(502)-459-2181",

"province": "Kentucky",

"zip": "40202"

},

"line_items": [

{

"id": 1072503337,

"shop_id": 548380009,

"fulfillment_order_id": 1046000825,

"quantity": 1,

"line_item_id": 518995019,

"inventory_item_id": 49148385,

"fulfillable_quantity": 1,

"variant_id": 49148385

}

],

"international_duties": null,

"fulfillment_holds": [],

"delivery_method": null,

"assigned_location": {

"address1": null,

"address2": null,

"city": null,

"country_code": "DE",

"location_id": 24826418,

"name": "Apple Api Shipwire",

"phone": null,

"province": null,

"zip": null

},

"merchant_requests": []

}

}

### examples

  * #### Transition a fulfillment order from scheduled to open

#####

        curl -d '{}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/fulfillment_orders/1046000825/open.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const fulfillment_order = new admin.rest.resources.FulfillmentOrder({session: session});

        fulfillment_order.id = 1046000825;
        await fulfillment_order.open({});

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        fulfillment_order = ShopifyAPI::FulfillmentOrder.new(session: test_session)
        fulfillment_order.id = 1046000825
        fulfillment_order.open(
          session: test_session,
        )

#####

        // Session is built by the OAuth process

        const fulfillment_order = new shopify.rest.FulfillmentOrder({session: session});
        fulfillment_order.id = 1046000825;
        await fulfillment_order.open({});

#### response

        HTTP/1.1 200 OK{"fulfillment_order":{"id":1046000825,"created_at":"2026-01-09T17:29:55-05:00","updated_at":"2026-01-09T17:29:57-05:00","shop_id":548380009,"order_id":450789469,"assigned_location_id":24826418,"request_status":"unsubmitted","status":"open","fulfill_at":null,"fulfill_by":null,"supported_actions":["request_fulfillment","create_fulfillment","hold"],"destination":{"id":1042572148,"address1":"Chestnut Street 92","address2":"","city":"Louisville","company":null,"country":"United States","email":"bob.norman@mail.example.com","first_name":"Bob","last_name":"Norman","phone":"+1(502)-459-2181","province":"Kentucky","zip":"40202"},"line_items":[{"id":1072503337,"shop_id":548380009,"fulfillment_order_id":1046000825,"quantity":1,"line_item_id":518995019,"inventory_item_id":49148385,"fulfillable_quantity":1,"variant_id":49148385}],"international_duties":null,"fulfillment_holds":[],"delivery_method":null,"assigned_location":{"address1":null,"address2":null,"city":null,"country_code":"DE","location_id":24826418,"name":"Apple Api Shipwire","phone":null,"province":null,"zip":null},"merchant_requests":[]}}


* * *

##

[Anchor to POST request, Releases all holds on a fulfillment order](/docs/api/admin-rest/latest/resources/fulfillmentorder#post-fulfillment-orders-fulfillment-order-id-release-hold)

post

Releases all holds on a fulfillment order

[fulfillmentOrderReleaseHold](/docs/api/admin-graphql/latest/mutations/fulfillmentOrderReleaseHold)

Releases the fulfillment order from all fulfillment holds and changes its status from `ON_HOLD`.
**NOTE:** It is highly recommended that apps use the [fulfillmentOrderReleaseHold GraphQL mutation](https://shopify.dev/api/admin-graphql/latest/mutations/fulfillmentOrderReleaseHold) to release specific holds by providing their IDs. Releasing all holds on a fulfillment order will result in the fulfillment order being released prematurely and items being incorrectly fulfilled.

###

[Anchor to Parameters of Releases all holds on a fulfillment order](/docs/api/admin-rest/latest/resources/fulfillmentorder#post-fulfillment-orders-fulfillment-order-id-release-hold-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

fulfillment_order_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to post-fulfillment-orders-fulfillment-order-id-release-hold-examples](/docs/api/admin-rest/latest/resources/fulfillmentorder#post-fulfillment-orders-fulfillment-order-id-release-hold-examples)Examples

Transition a fulfillment order from on_hold to open

Path parameters

fulfillment_order_id=1046000828

string**string**

required**required**

Was this section helpful?

YesNo

post

## /admin/api/2026-01/fulfillment_orders/1046000828/release_hold.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{}' \

-X POST "https://your-development-store.myshopify.com/admin/api/2026-01/fulfillment_orders/1046000828/release_hold.json" \

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

HTTP/1.1 200 OK

{

"fulfillment_order": {

"id": 1046000828,

"created_at": "2026-01-09T17:30:01-05:00",

"updated_at": "2026-01-09T17:30:02-05:00",

"shop_id": 548380009,

"order_id": 450789469,

"assigned_location_id": 24826418,

"request_status": "submitted",

"status": "open",

"fulfill_at": null,

"fulfill_by": null,

"supported_actions": [

"cancel_fulfillment_order"

],

"destination": {

"id": 1042572151,

"address1": "Chestnut Street 92",

"address2": "",

"city": "Louisville",

"company": null,

"country": "United States",

"email": "bob.norman@mail.example.com",

"first_name": "Bob",

"last_name": "Norman",

"phone": "+1(502)-459-2181",

"province": "Kentucky",

"zip": "40202"

},

"origin": {

"address1": null,

"address2": null,

"city": null,

"country_code": "DE",

"location_id": 24826418,

"name": "Apple Api Shipwire",

"phone": null,

"province": null,

"zip": null

},

"line_items": [

{

"id": 1072503340,

"shop_id": 548380009,

"fulfillment_order_id": 1046000828,

"quantity": 1,

"line_item_id": 518995019,

"inventory_item_id": 49148385,

"fulfillable_quantity": 1,

"variant_id": 49148385

}

],

"outgoing_requests": [],

"international_duties": null,

"fulfillment_holds": [],

"delivery_method": null

}

}

### examples

  * #### Transition a fulfillment order from on_hold to open

#####

        curl -d '{}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/fulfillment_orders/1046000828/release_hold.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const fulfillment_order = new admin.rest.resources.FulfillmentOrder({session: session});

        fulfillment_order.id = 1046000828;
        await fulfillment_order.release_hold({});

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        fulfillment_order = ShopifyAPI::FulfillmentOrder.new(session: test_session)
        fulfillment_order.id = 1046000828
        fulfillment_order.release_hold(
          session: test_session,
        )

#####

        // Session is built by the OAuth process

        const fulfillment_order = new shopify.rest.FulfillmentOrder({session: session});
        fulfillment_order.id = 1046000828;
        await fulfillment_order.release_hold({});

#### response

        HTTP/1.1 200 OK{"fulfillment_order":{"id":1046000828,"created_at":"2026-01-09T17:30:01-05:00","updated_at":"2026-01-09T17:30:02-05:00","shop_id":548380009,"order_id":450789469,"assigned_location_id":24826418,"request_status":"submitted","status":"open","fulfill_at":null,"fulfill_by":null,"supported_actions":["cancel_fulfillment_order"],"destination":{"id":1042572151,"address1":"Chestnut Street 92","address2":"","city":"Louisville","company":null,"country":"United States","email":"bob.norman@mail.example.com","first_name":"Bob","last_name":"Norman","phone":"+1(502)-459-2181","province":"Kentucky","zip":"40202"},"origin":{"address1":null,"address2":null,"city":null,"country_code":"DE","location_id":24826418,"name":"Apple Api Shipwire","phone":null,"province":null,"zip":null},"line_items":[{"id":1072503340,"shop_id":548380009,"fulfillment_order_id":1046000828,"quantity":1,"line_item_id":518995019,"inventory_item_id":49148385,"fulfillable_quantity":1,"variant_id":49148385}],"outgoing_requests":[],"international_duties":null,"fulfillment_holds":[],"delivery_method":null}}


* * *

##

[Anchor to POST request, Reschedules the fulfill_at time of a scheduled fulfillment order](/docs/api/admin-rest/latest/resources/fulfillmentorder#post-fulfillment-orders-fulfillment-order-id-reschedule)

post

Reschedules the fulfill_at time of a scheduled fulfillment order

[fulfillmentOrderReschedule](/docs/api/admin-graphql/latest/mutations/fulfillmentOrderReschedule?example=reschedules-the-fulfill_at-time-of-a-scheduled-fulfillment-order)

Requires ANY of the following access scopes: `merchant_managed_fulfillment_orders`, `third_party_fulfillment_orders`.

**Requires ANY of the following access scopes: `merchant_managed_fulfillment_orders`, `third_party_fulfillment_orders`.:**

Reschedules a scheduled fulfillment order.

Updates the value of the `fulfill_at` field on a scheduled fulfillment order. The fulfillment order will be marked as ready for fulfillment at this date and time.

#### Response

  * `fulfillment_order` \- a fulfillment order with the rescheduled line items.
Fulfillment orders may be merged if they have the same `fulfill_at` datetime. If the fulfillment order is merged then the resulting fulfillment order will be returned. Otherwise the original fulfillment order will be returned with an updated `fulfill_at` datetime.


###

[Anchor to Parameters of Reschedules the fulfill_at time of a scheduled fulfillment order](/docs/api/admin-rest/latest/resources/fulfillmentorder#post-fulfillment-orders-fulfillment-order-id-reschedule-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

fulfillment_order_id

string**string**

required**required**

* * *

new_fulfill_at

date**date**

ISO 8601**ISO 8601**

required**required**

The new fulfillment deadline of the fulfillment order. Must be in future.

* * *

Was this section helpful?

YesNo

###

[Anchor to post-fulfillment-orders-fulfillment-order-id-reschedule-examples](/docs/api/admin-rest/latest/resources/fulfillmentorder#post-fulfillment-orders-fulfillment-order-id-reschedule-examples)Examples

Update the fulfill_at time of a scheduled fulfillment order

Path parameters

fulfillment_order_id=1046000837

string**string**

required**required**

Was this section helpful?

YesNo

post

## /admin/api/2026-01/fulfillment_orders/1046000837/reschedule.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{"fulfillment_order":{"new_fulfill_at":"2027-02-09 22:30 UTC"}}' \

-X POST "https://your-development-store.myshopify.com/admin/api/2026-01/fulfillment_orders/1046000837/reschedule.json" \

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

HTTP/1.1 200 OK

{

"fulfillment_order": {

"id": 1046000837,

"created_at": "2026-01-09T17:30:19-05:00",

"updated_at": "2026-01-09T17:30:21-05:00",

"shop_id": 548380009,

"order_id": 450789469,

"assigned_location_id": 24826418,

"request_status": "unsubmitted",

"status": "scheduled",

"fulfill_at": "2027-02-09T17:30:00-05:00",

"fulfill_by": null,

"supported_actions": [

"mark_as_open"

],

"destination": {

"id": 1042572160,

"address1": "Chestnut Street 92",

"address2": "",

"city": "Louisville",

"company": null,

"country": "United States",

"email": "bob.norman@mail.example.com",

"first_name": "Bob",

"last_name": "Norman",

"phone": "+1(502)-459-2181",

"province": "Kentucky",

"zip": "40202"

},

"line_items": [

{

"id": 1072503349,

"shop_id": 548380009,

"fulfillment_order_id": 1046000837,

"quantity": 1,

"line_item_id": 518995019,

"inventory_item_id": 49148385,

"fulfillable_quantity": 1,

"variant_id": 49148385

}

],

"international_duties": null,

"fulfillment_holds": [],

"delivery_method": null,

"assigned_location": {

"address1": null,

"address2": null,

"city": null,

"country_code": "DE",

"location_id": 24826418,

"name": "Apple Api Shipwire",

"phone": null,

"province": null,

"zip": null

},

"merchant_requests": []

}

}

### examples

  * #### Update the fulfill_at time of a scheduled fulfillment order

#####

        curl -d '{"fulfillment_order":{"new_fulfill_at":"2027-02-09 22:30 UTC"}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/fulfillment_orders/1046000837/reschedule.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const fulfillment_order = new admin.rest.resources.FulfillmentOrder({session: session});

        fulfillment_order.id = 1046000837;
        await fulfillment_order.reschedule({
          body: {"fulfillment_order": {"new_fulfill_at": "2027-02-09 22:30 UTC"}},
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        fulfillment_order = ShopifyAPI::FulfillmentOrder.new(session: test_session)
        fulfillment_order.id = 1046000837
        fulfillment_order.reschedule(
          session: test_session,
          body: {"fulfillment_order" => {"new_fulfill_at" => "2027-02-09 22:30 UTC"}},
        )

#####

        // Session is built by the OAuth process

        const fulfillment_order = new shopify.rest.FulfillmentOrder({session: session});
        fulfillment_order.id = 1046000837;
        await fulfillment_order.reschedule({
          body: {"fulfillment_order": {"new_fulfill_at": "2027-02-09 22:30 UTC"}},
        });

#### response

        HTTP/1.1 200 OK{"fulfillment_order":{"id":1046000837,"created_at":"2026-01-09T17:30:19-05:00","updated_at":"2026-01-09T17:30:21-05:00","shop_id":548380009,"order_id":450789469,"assigned_location_id":24826418,"request_status":"unsubmitted","status":"scheduled","fulfill_at":"2027-02-09T17:30:00-05:00","fulfill_by":null,"supported_actions":["mark_as_open"],"destination":{"id":1042572160,"address1":"Chestnut Street 92","address2":"","city":"Louisville","company":null,"country":"United States","email":"bob.norman@mail.example.com","first_name":"Bob","last_name":"Norman","phone":"+1(502)-459-2181","province":"Kentucky","zip":"40202"},"line_items":[{"id":1072503349,"shop_id":548380009,"fulfillment_order_id":1046000837,"quantity":1,"line_item_id":518995019,"inventory_item_id":49148385,"fulfillable_quantity":1,"variant_id":49148385}],"international_duties":null,"fulfillment_holds":[],"delivery_method":null,"assigned_location":{"address1":null,"address2":null,"city":null,"country_code":"DE","location_id":24826418,"name":"Apple Api Shipwire","phone":null,"province":null,"zip":null},"merchant_requests":[]}}


* * *

##

[Anchor to POST request, Sets deadline for fulfillment orders](/docs/api/admin-rest/latest/resources/fulfillmentorder#post-fulfillment-orders-set-fulfillment-orders-deadline)

post

Sets deadline for fulfillment orders

[fulfillmentOrdersSetFulfillmentDeadline](/docs/api/admin-graphql/latest/mutations/fulfillmentOrdersSetFulfillmentDeadline?example=sets-deadline-for-fulfillment-orders)

Requires ANY of the following access scopes: `merchant_managed_fulfillment_orders`, `third_party_fulfillment_orders`, `marketplace_fulfillment_orders`, `orders`.

**Requires ANY of the following access scopes: `merchant_managed_fulfillment_orders`, `third_party_fulfillment_orders`, `marketplace_fulfillment_orders`, `orders`.:**

Sets the latest date and time by which the fulfillment orders need to be fulfilled.

###

[Anchor to Parameters of Sets deadline for fulfillment orders](/docs/api/admin-rest/latest/resources/fulfillmentorder#post-fulfillment-orders-set-fulfillment-orders-deadline-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

fulfillment_deadline

The new fulfillment deadline of the fulfillment orders.

* * *

fulfillment_order_ids

The IDs of the fulfillment orders for which the deadline is being set

* * *

Was this section helpful?

YesNo

###

[Anchor to post-fulfillment-orders-set-fulfillment-orders-deadline-examples](/docs/api/admin-rest/latest/resources/fulfillmentorder#post-fulfillment-orders-set-fulfillment-orders-deadline-examples)Examples

Set a fulfillment deadline for a fulfillment order

Request body

fulfillment_order_ids

Fulfillment_order_ids resource**Fulfillment_order_ids resource**

Show fulfillment_order_ids properties

fulfillment_order_ids:[1046000829]

The IDs of the fulfillment orders for which the deadline is being set

fulfillment_deadline:"2021-05-26T10:00:00-04:00"

The new fulfillment deadline of the fulfillment orders.

Was this section helpful?

YesNo

post

## /admin/api/2026-01/fulfillment_orders/set_fulfillment_orders_deadline.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{"fulfillment_order_ids":[1046000829],"fulfillment_deadline":"2021-05-26T10:00:00-04:00"}' \

-X POST "https://your-development-store.myshopify.com/admin/api/2026-01/fulfillment_orders/set_fulfillment_orders_deadline.json" \

-H "X-Shopify-Access-Token: {access_token}" \

-H "Content-Type: application/json"

{}

## Response

JSON

9

1

2

HTTP/1.1 200 OK

{}

### examples

  * #### Set a fulfillment deadline for a fulfillment order

#####

        curl -d '{"fulfillment_order_ids":[1046000829],"fulfillment_deadline":"2021-05-26T10:00:00-04:00"}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/fulfillment_orders/set_fulfillment_orders_deadline.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const fulfillment_order = new admin.rest.resources.FulfillmentOrder({session: session});

        await fulfillment_order.set_fulfillment_orders_deadline({
          body: {"fulfillment_order_ids": [1046000829], "fulfillment_deadline": "2021-05-26T10:00:00-04:00"},
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        fulfillment_order = ShopifyAPI::FulfillmentOrder.new(session: test_session)

        fulfillment_order.set_fulfillment_orders_deadline(
          session: test_session,
          body: {"fulfillment_order_ids" => [1046000829], "fulfillment_deadline" => "2021-05-26T10:00:00-04:00"},
        )

#####

        // Session is built by the OAuth process

        const fulfillment_order = new shopify.rest.FulfillmentOrder({session: session});

        await fulfillment_order.set_fulfillment_orders_deadline({
          body: {"fulfillment_order_ids": [1046000829], "fulfillment_deadline": "2021-05-26T10:00:00-04:00"},
        });

#### response

        HTTP/1.1 200 OK{}


* * *

##

[Anchor to GET request, Retrieves a specific fulfillment order](/docs/api/admin-rest/latest/resources/fulfillmentorder#get-fulfillment-orders-fulfillment-order-id)

get

Retrieves a specific fulfillment order

[fulfillmentOrder](/docs/api/admin-graphql/latest/queries/fulfillmentOrder?example=retrieves-a-specific-fulfillment-order)

Retrieves a specific fulfillment order.

###

[Anchor to Parameters of Retrieves a specific fulfillment order](/docs/api/admin-rest/latest/resources/fulfillmentorder#get-fulfillment-orders-fulfillment-order-id-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

fulfillment_order_id

string**string**

required**required**

* * *

include_financial_summaries

boolean**boolean**

default false**default false**

Include the financial summary data for each line item, if available.

* * *

include_order_reference_fields

boolean**boolean**

default false**default false**

Indicates whether the order reference fields should be returned in the result.

* * *

Was this section helpful?

YesNo

###

[Anchor to get-fulfillment-orders-fulfillment-order-id-examples](/docs/api/admin-rest/latest/resources/fulfillmentorder#get-fulfillment-orders-fulfillment-order-id-examples)Examples

Get a single fulfillment order by its ID

Path parameters

fulfillment_order_id=1046000827

string**string**

required**required**

Get a single fulfillment order by its ID and include the financial summary data

Path parameters

fulfillment_order_id=1046000830

string**string**

required**required**

Query parameters

include_financial_summaries=true

boolean**boolean**

default false**default false**

Include the financial summary data for each line item, if available.

Get a single fulfillment order by its ID and include the order reference data for each

Path parameters

fulfillment_order_id=1046000833

string**string**

required**required**

Query parameters

include_order_reference_fields=true

boolean**boolean**

default false**default false**

Indicates whether the order reference fields should be returned in the result.

Was this section helpful?

YesNo

get

## /admin/api/2026-01/fulfillment_orders/1046000827.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/fulfillment_orders/1046000827.json" \

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

HTTP/1.1 200 OK

{

"fulfillment_order": {

"id": 1046000827,

"created_at": "2026-01-09T17:29:59-05:00",

"updated_at": "2026-01-09T17:29:59-05:00",

"shop_id": 548380009,

"order_id": 450789469,

"assigned_location_id": 24826418,

"request_status": "submitted",

"status": "open",

"fulfill_at": null,

"fulfill_by": null,

"supported_actions": [

"cancel_fulfillment_order"

],

"destination": {

"id": 1042572150,

"address1": "Chestnut Street 92",

"address2": "",

"city": "Louisville",

"company": null,

"country": "United States",

"email": "bob.norman@mail.example.com",

"first_name": "Bob",

"last_name": "Norman",

"phone": "+1(502)-459-2181",

"province": "Kentucky",

"zip": "40202"

},

"line_items": [

{

"id": 1072503339,

"shop_id": 548380009,

"fulfillment_order_id": 1046000827,

"quantity": 1,

"line_item_id": 518995019,

"inventory_item_id": 49148385,

"fulfillable_quantity": 1,

"variant_id": 49148385

}

],

"international_duties": null,

"fulfillment_holds": [],

"delivery_method": null,

"assigned_location": {

"address1": null,

"address2": null,

"city": null,

"country_code": "DE",

"location_id": 24826418,

"name": "Apple Api Shipwire",

"phone": null,

"province": null,

"zip": null

},

"merchant_requests": []

}

}

### examples

  * #### Get a single fulfillment order by its ID

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/fulfillment_orders/1046000827.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.FulfillmentOrder.find({
          session: session,
          id: 1046000827,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::FulfillmentOrder.find(
          session: test_session,
          id: 1046000827,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.FulfillmentOrder.find({
          session: session,
          id: 1046000827,
        });

#### response

        HTTP/1.1 200 OK{"fulfillment_order":{"id":1046000827,"created_at":"2026-01-09T17:29:59-05:00","updated_at":"2026-01-09T17:29:59-05:00","shop_id":548380009,"order_id":450789469,"assigned_location_id":24826418,"request_status":"submitted","status":"open","fulfill_at":null,"fulfill_by":null,"supported_actions":["cancel_fulfillment_order"],"destination":{"id":1042572150,"address1":"Chestnut Street 92","address2":"","city":"Louisville","company":null,"country":"United States","email":"bob.norman@mail.example.com","first_name":"Bob","last_name":"Norman","phone":"+1(502)-459-2181","province":"Kentucky","zip":"40202"},"line_items":[{"id":1072503339,"shop_id":548380009,"fulfillment_order_id":1046000827,"quantity":1,"line_item_id":518995019,"inventory_item_id":49148385,"fulfillable_quantity":1,"variant_id":49148385}],"international_duties":null,"fulfillment_holds":[],"delivery_method":null,"assigned_location":{"address1":null,"address2":null,"city":null,"country_code":"DE","location_id":24826418,"name":"Apple Api Shipwire","phone":null,"province":null,"zip":null},"merchant_requests":[]}}

  * #### Get a single fulfillment order by its ID and include the financial summary data

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/fulfillment_orders/1046000830.json?include_financial_summaries=true" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.FulfillmentOrder.find({
          session: session,
          id: 1046000830,
          include_financial_summaries: "true",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::FulfillmentOrder.find(
          session: test_session,
          id: 1046000830,
          include_financial_summaries: "true",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.FulfillmentOrder.find({
          session: session,
          id: 1046000830,
          include_financial_summaries: "true",
        });

#### response

        HTTP/1.1 200 OK{"fulfillment_order":{"id":1046000830,"created_at":"2026-01-09T17:30:04-05:00","updated_at":"2026-01-09T17:30:04-05:00","shop_id":548380009,"order_id":450789469,"assigned_location_id":24826418,"request_status":"submitted","status":"open","fulfill_at":null,"fulfill_by":null,"supported_actions":["cancel_fulfillment_order"],"destination":{"id":1042572153,"address1":"Chestnut Street 92","address2":"","city":"Louisville","company":null,"country":"United States","email":"bob.norman@mail.example.com","first_name":"Bob","last_name":"Norman","phone":"+1(502)-459-2181","province":"Kentucky","zip":"40202"},"line_items":[{"id":1072503342,"shop_id":548380009,"fulfillment_order_id":1046000830,"quantity":1,"line_item_id":518995019,"inventory_item_id":49148385,"fulfillable_quantity":1,"variant_id":49148385,"financial_summaries":[{"quantity":1,"original_unit_price_set":"199.00","approximate_discounted_unit_price_set":"199.00","discount_allocations":[{"amount":"3.33","discount_application":{"allocation_method":"across","target_selection":"all","target_type":"line_item"}}]}]}],"international_duties":null,"fulfillment_holds":[],"delivery_method":null,"assigned_location":{"address1":null,"address2":null,"city":null,"country_code":"DE","location_id":24826418,"name":"Apple Api Shipwire","phone":null,"province":null,"zip":null},"merchant_requests":[]}}

  * #### Get a single fulfillment order by its ID and include the order reference data for each

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/fulfillment_orders/1046000833.json?include_order_reference_fields=true" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.FulfillmentOrder.find({
          session: session,
          id: 1046000833,
          include_order_reference_fields: "true",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::FulfillmentOrder.find(
          session: test_session,
          id: 1046000833,
          include_order_reference_fields: "true",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.FulfillmentOrder.find({
          session: session,
          id: 1046000833,
          include_order_reference_fields: "true",
        });

#### response

        HTTP/1.1 200 OK{"fulfillment_order":{"id":1046000833,"created_at":"2026-01-09T17:30:11-05:00","updated_at":"2026-01-09T17:30:11-05:00","shop_id":548380009,"order_id":450789469,"assigned_location_id":24826418,"request_status":"submitted","status":"open","fulfill_at":null,"fulfill_by":null,"supported_actions":["cancel_fulfillment_order"],"destination":{"id":1042572156,"address1":"Chestnut Street 92","address2":"","city":"Louisville","company":null,"country":"United States","email":"bob.norman@mail.example.com","first_name":"Bob","last_name":"Norman","phone":"+1(502)-459-2181","province":"Kentucky","zip":"40202"},"line_items":[{"id":1072503345,"shop_id":548380009,"fulfillment_order_id":1046000833,"quantity":1,"line_item_id":518995019,"inventory_item_id":49148385,"fulfillable_quantity":1,"variant_id":49148385}],"international_duties":null,"fulfillment_holds":[],"order_name":"#1001","order_processed_at":"2008-01-10T11:00:00-05:00","channel_id":null,"delivery_method":null,"assigned_location":{"address1":null,"address2":null,"city":null,"country_code":"DE","location_id":24826418,"name":"Apple Api Shipwire","phone":null,"province":null,"zip":null},"merchant_requests":[]}}


* * *

##

[Anchor to GET request, Retrieves a list of fulfillment orders for a specific order](/docs/api/admin-rest/latest/resources/fulfillmentorder#get-orders-order-id-fulfillment-orders)

get

Retrieves a list of fulfillment orders for a specific order

[order](/docs/api/admin-graphql/latest/queries/order)

Retrieves a list of fulfillment orders for a specific order.

API access scopes govern which fulfillments orders are returned. An API client will only receive a subset of the fulfillment orders which belong to an order if they don't have the necessary access scopes to view all of the fulfillment orders. In the case that an API client does not have the access scopes necessary to view any of the fulfillment orders belongs to an order, an empty array will be returned.

###

[Anchor to Parameters of Retrieves a list of fulfillment orders for a specific order](/docs/api/admin-rest/latest/resources/fulfillmentorder#get-orders-order-id-fulfillment-orders-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

order_id

string**string**

required**required**

* * *

include_financial_summaries

boolean**boolean**

default false**default false**

Include the financial summary data for each line item, if available.

* * *

include_order_reference_fields

boolean**boolean**

default false**default false**

Indicates whether the order reference fields should be returned in the result.

* * *

order_id

The ID of the order that is associated with the fulfillment orders.

* * *

Was this section helpful?

YesNo

###

[Anchor to get-orders-order-id-fulfillment-orders-examples](/docs/api/admin-rest/latest/resources/fulfillmentorder#get-orders-order-id-fulfillment-orders-examples)Examples

Retrieve a list of all fulfillment orders for an order

Retrieve a list of fulfillment orders for an order and include the financial summary data for each

Query parameters

include_financial_summaries=true

boolean**boolean**

default false**default false**

Include the financial summary data for each line item, if available.

Retrieve a list of fulfillment orders for an order and include the order reference data for each

Query parameters

include_order_reference_fields=true

boolean**boolean**

default false**default false**

Indicates whether the order reference fields should be returned in the result.

Was this section helpful?

YesNo

get

## /admin/api/2026-01/orders/450789469/fulfillment_orders.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469/fulfillment_orders.json" \

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

HTTP/1.1 200 OK

{

"fulfillment_orders": [

{

"id": 1046000838,

"created_at": "2026-01-09T17:30:22-05:00",

"updated_at": "2026-01-09T17:30:22-05:00",

"shop_id": 548380009,

"order_id": 450789469,

"assigned_location_id": 24826418,

"request_status": "submitted",

"status": "open",

"fulfill_at": null,

"fulfill_by": null,

"supported_actions": [

"cancel_fulfillment_order"

],

"destination": {

"id": 1042572161,

"address1": "Chestnut Street 92",

"address2": "",

"city": "Louisville",

"company": null,

"country": "United States",

"email": "bob.norman@mail.example.com",

"first_name": "Bob",

"last_name": "Norman",

"phone": "+1(502)-459-2181",

"province": "Kentucky",

"zip": "40202"

},

"line_items": [

{

"id": 1072503350,

"shop_id": 548380009,

"fulfillment_order_id": 1046000838,

"quantity": 1,

"line_item_id": 518995019,

"inventory_item_id": 49148385,

"fulfillable_quantity": 1,

"variant_id": 49148385

}

],

"international_duties": null,

"fulfillment_holds": [],

"delivery_method": null,

"assigned_location": {

"address1": null,

"address2": null,

"city": null,

"country_code": "DE",

"location_id": 24826418,

"name": "Apple Api Shipwire",

"phone": null,

"province": null,

"zip": null

},

"merchant_requests": []

}

]

}

### examples

  * #### Retrieve a list of all fulfillment orders for an order

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469/fulfillment_orders.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.FulfillmentOrder.all({
          session: session,
          order_id: 450789469,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::FulfillmentOrder.all(
          session: test_session,
          order_id: 450789469,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.FulfillmentOrder.all({
          session: session,
          order_id: 450789469,
        });

#### response

        HTTP/1.1 200 OK{"fulfillment_orders":[{"id":1046000838,"created_at":"2026-01-09T17:30:22-05:00","updated_at":"2026-01-09T17:30:22-05:00","shop_id":548380009,"order_id":450789469,"assigned_location_id":24826418,"request_status":"submitted","status":"open","fulfill_at":null,"fulfill_by":null,"supported_actions":["cancel_fulfillment_order"],"destination":{"id":1042572161,"address1":"Chestnut Street 92","address2":"","city":"Louisville","company":null,"country":"United States","email":"bob.norman@mail.example.com","first_name":"Bob","last_name":"Norman","phone":"+1(502)-459-2181","province":"Kentucky","zip":"40202"},"line_items":[{"id":1072503350,"shop_id":548380009,"fulfillment_order_id":1046000838,"quantity":1,"line_item_id":518995019,"inventory_item_id":49148385,"fulfillable_quantity":1,"variant_id":49148385}],"international_duties":null,"fulfillment_holds":[],"delivery_method":null,"assigned_location":{"address1":null,"address2":null,"city":null,"country_code":"DE","location_id":24826418,"name":"Apple Api Shipwire","phone":null,"province":null,"zip":null},"merchant_requests":[]}]}

  * #### Retrieve a list of fulfillment orders for an order and include the financial summary data for each

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469/fulfillment_orders.json?include_financial_summaries=true" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.FulfillmentOrder.all({
          session: session,
          order_id: 450789469,
          include_financial_summaries: "true",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::FulfillmentOrder.all(
          session: test_session,
          order_id: 450789469,
          include_financial_summaries: "true",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.FulfillmentOrder.all({
          session: session,
          order_id: 450789469,
          include_financial_summaries: "true",
        });

#### response

        HTTP/1.1 200 OK{"fulfillment_orders":[{"id":1046000835,"created_at":"2026-01-09T17:30:15-05:00","updated_at":"2026-01-09T17:30:15-05:00","shop_id":548380009,"order_id":450789469,"assigned_location_id":24826418,"request_status":"submitted","status":"open","fulfill_at":null,"fulfill_by":null,"supported_actions":["cancel_fulfillment_order"],"destination":{"id":1042572158,"address1":"Chestnut Street 92","address2":"","city":"Louisville","company":null,"country":"United States","email":"bob.norman@mail.example.com","first_name":"Bob","last_name":"Norman","phone":"+1(502)-459-2181","province":"Kentucky","zip":"40202"},"line_items":[{"id":1072503347,"shop_id":548380009,"fulfillment_order_id":1046000835,"quantity":1,"line_item_id":518995019,"inventory_item_id":49148385,"fulfillable_quantity":1,"variant_id":49148385,"financial_summaries":[{"quantity":1,"original_unit_price_set":"199.00","approximate_discounted_unit_price_set":"199.00","discount_allocations":[{"amount":"3.33","discount_application":{"allocation_method":"across","target_selection":"all","target_type":"line_item"}}]}]}],"international_duties":null,"fulfillment_holds":[],"delivery_method":null,"assigned_location":{"address1":null,"address2":null,"city":null,"country_code":"DE","location_id":24826418,"name":"Apple Api Shipwire","phone":null,"province":null,"zip":null},"merchant_requests":[]}]}

  * #### Retrieve a list of fulfillment orders for an order and include the order reference data for each

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469/fulfillment_orders.json?include_order_reference_fields=true" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.FulfillmentOrder.all({
          session: session,
          order_id: 450789469,
          include_order_reference_fields: "true",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::FulfillmentOrder.all(
          session: test_session,
          order_id: 450789469,
          include_order_reference_fields: "true",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.FulfillmentOrder.all({
          session: session,
          order_id: 450789469,
          include_order_reference_fields: "true",
        });

#### response

        HTTP/1.1 200 OK{"fulfillment_orders":[{"id":1046000826,"created_at":"2026-01-09T17:29:58-05:00","updated_at":"2026-01-09T17:29:58-05:00","shop_id":548380009,"order_id":450789469,"assigned_location_id":24826418,"request_status":"submitted","status":"open","fulfill_at":null,"fulfill_by":null,"supported_actions":["cancel_fulfillment_order"],"destination":{"id":1042572149,"address1":"Chestnut Street 92","address2":"","city":"Louisville","company":null,"country":"United States","email":"bob.norman@mail.example.com","first_name":"Bob","last_name":"Norman","phone":"+1(502)-459-2181","province":"Kentucky","zip":"40202"},"line_items":[{"id":1072503338,"shop_id":548380009,"fulfillment_order_id":1046000826,"quantity":1,"line_item_id":518995019,"inventory_item_id":49148385,"fulfillable_quantity":1,"variant_id":49148385}],"international_duties":null,"fulfillment_holds":[],"order_name":"#1001","order_processed_at":"2008-01-10T11:00:00-05:00","channel_id":null,"delivery_method":null,"assigned_location":{"address1":null,"address2":null,"city":null,"country_code":"DE","location_id":24826418,"name":"Apple Api Shipwire","phone":null,"province":null,"zip":null},"merchant_requests":[]}]}