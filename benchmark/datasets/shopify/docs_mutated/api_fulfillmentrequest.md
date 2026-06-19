# FulfillmentRequest

*Source: https://shopify.dev/docs/api/admin-rest/2026-01/resources/fulfillmentrequest*

---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04

2026-01latest

# FulfillmentRequest

Ask assistant

Multiple access scopes needed — refer to each endpoint for access scope requirements.

**Multiple access scopes needed — refer to each endpoint for access scope requirements.:**

The `FulfillmentRequest` resource represents a fulfillment request made by the merchant or an order management app to a [fulfillment service](/docs/admin-api/rest/reference/shipping-and-fulfillment/fulfillmentservice) for a [fulfillment order](/docs/admin-api/rest/reference/shipping-and-fulfillment/fulfillmentorder). A fulfillment service can accept or reject the fulfillment request.

## Terminating a fulfillment request

A fulfillment service can stop fulfilling an accepted fulfillment request if they choose [closing the fulfillment order as incomplete](/api/admin-rest/latest/resources/fulfillmentorder#post-fulfillment-orders-fulfillment-order-id-close). The fulfillment order can be partially fulfilled when a fulfillment service chooses to stop the fulfillment.

The merchant or an order management app can notify the fulfillment service to cancel an accepted fulfillment request by sending a [cancellation request](/api/admin-rest/latest/resources/cancellationrequest#post-fulfillment-orders-fulfillment-order-id-cancellation-request). The fulfillment service can accept or reject the cancellation request. The fulfillment order can be partially fulfilled at this time.

The merchant or an order management app can also [cancel](/api/admin-rest/latest/resources/fulfillmentorder#post-fulfillment-orders-fulfillment-order-id-cancel) a fulfillment order. Calling the `cancel` endpoint results in the fulfilment order being cancelled within Shopify. This change will not be communicated to the fulfilment service. If the intention is for a fulfilment service to halt fulfilment activity, a [cancellation request](/api/admin-rest/latest/resources/cancellationrequest#post-fulfillment-orders-fulfillment-order-id-cancellation-request) should be sent to the fulfilment service instead, as described above.

## Retrieving fulfillment request details

The `FulfillmentOrder` resource and the `merchant_requests` field can be used to retrieve the merchant requests which have been made. The overall status of these requests is also available using the `request_status` field of the fulfillment order.

To learn more about the fulfillment request process in the fulfillment workflow, refer to [Manage fulfillments as a fulfillment service app](/apps/fulfillment/fulfillment-service-apps/manage-fulfillments) guide.

Was this section helpful?

YesNo

#

## Endpoints

  * [post/admin/api/latest/fulfillment_orders/{fulfillment_order_id}/fulfillment_request.json](/docs/api/admin-rest/latest/resources/fulfillmentrequest#post-fulfillment-orders-fulfillment-order-id-fulfillment-request)

Sends a fulfillment request

[fulfillmentOrderSubmitFulfillmentRequest](/docs/api/admin-graphql/latest/mutations/fulfillmentOrderSubmitFulfillmentRequest?example=sends-a-fulfillment-request)

  * [post/admin/api/latest/fulfillment_orders/{fulfillment_order_id}/fulfillment_request/accept.json](/docs/api/admin-rest/latest/resources/fulfillmentrequest#post-fulfillment-orders-fulfillment-order-id-fulfillment-request-accept)

Accepts a fulfillment request

[fulfillmentOrderAcceptFulfillmentRequest](/docs/api/admin-graphql/latest/mutations/fulfillmentOrderAcceptFulfillmentRequest?example=accepts-a-fulfillment-request)

  * [post/admin/api/latest/fulfillment_orders/{fulfillment_order_id}/fulfillment_request/reject.json](/docs/api/admin-rest/latest/resources/fulfillmentrequest#post-fulfillment-orders-fulfillment-order-id-fulfillment-request-reject)

Rejects a fulfillment request

[fulfillmentOrderRejectFulfillmentRequest](/docs/api/admin-graphql/latest/mutations/fulfillmentOrderRejectFulfillmentRequest?example=rejects-a-fulfillment-request)


* * *

[Anchor to ](/docs/api/admin-rest/latest/resources/fulfillmentrequest#resource-object)

## The FulfillmentRequest resource

[Anchor to ](/docs/api/admin-rest/latest/resources/fulfillmentrequest#resource-object-properties)

### Properties

* * *

message

->[message](/docs/api/admin-graphql/latest/objects/FulfillmentOrderMerchantRequest#field-FulfillmentOrderMerchantRequest.fields.message)

A message for the fulfillment request.

* * *

sent_at

->[sentAt](/docs/api/admin-graphql/latest/objects/FulfillmentOrderMerchantRequest#field-FulfillmentOrderMerchantRequest.fields.sentAt)

The timestamp when the request was made.

* * *

response_data

->[responseData](/docs/api/admin-graphql/latest/objects/FulfillmentOrderMerchantRequest#field-FulfillmentOrderMerchantRequest.fields.responseData)

The response from the fulfillment service.

* * *

request_options

->[requestOptions](/docs/api/admin-graphql/latest/objects/FulfillmentOrderMerchantRequest#field-FulfillmentOrderMerchantRequest.fields.requestOptions)

Whether to notify the customer about the fulfillment request.

* * *

kind

->[kind](/docs/api/admin-graphql/latest/objects/FulfillmentOrderMerchantRequest#field-FulfillmentOrderMerchantRequest.fields.kind)

The kind of request made.

* * *

Was this section helpful?

YesNo

{}

## The FulfillmentRequest resource

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

{

"message": "The optional message that the merchant included in the request.",

"sent_at": "2024-04-01T13:38:11-04:00",

"response_data": {

"response": {}

},

"request_options": {

"notify_customer": true

},

"kind": "fulfillment_request"

}

* * *

##

[Anchor to POST request, Sends a fulfillment request](/docs/api/admin-rest/latest/resources/fulfillmentrequest#post-fulfillment-orders-fulfillment-order-id-fulfillment-request)

post

Sends a fulfillment request

[fulfillmentOrderSubmitFulfillmentRequest](/docs/api/admin-graphql/latest/mutations/fulfillmentOrderSubmitFulfillmentRequest?example=sends-a-fulfillment-request)

Requires `third_party_fulfillment_orders` access scope.

**Requires `third_party_fulfillment_orders` access scope.:**

Sends a fulfillment request to the fulfillment service of a fulfillment order.

###

[Anchor to Parameters of Sends a fulfillment request](/docs/api/admin-rest/latest/resources/fulfillmentrequest#post-fulfillment-orders-fulfillment-order-id-fulfillment-request-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

fulfillment_order_id

string**string**

required**required**

* * *

fulfillment_order_line_items

The fulfillment order line items to be requested for fulfillment. If left blank, all line items of the fulfillment order are requested for fulfillment.

* * *

message

An optional message for the fulfillment request.

* * *

notify_customer

Whether to notify the customer about the fulfillment request.

* * *

Was this section helpful?

YesNo

###

[Anchor to post-fulfillment-orders-fulfillment-order-id-fulfillment-request-examples](/docs/api/admin-rest/latest/resources/fulfillmentrequest#post-fulfillment-orders-fulfillment-order-id-fulfillment-request-examples)Examples

Sends a fulfillment request to the fulfillment service for all line items on the fulfillment order if fulfillment_order_line_items is left blank

Path parameters

fulfillment_order_id=1046000849

string**string**

required**required**

Request body

fulfillment_request

Fulfillment_request resource**Fulfillment_request resource**

Show fulfillment_request properties

fulfillment_request.message:"Fulfill this ASAP please."

A message for the fulfillment request.

Sends a fulfillment request to the fulfillment service of a fulfillment order for the specified line items

Path parameters

fulfillment_order_id=1046000846

string**string**

required**required**

Request body

fulfillment_request

Fulfillment_request resource**Fulfillment_request resource**

Show fulfillment_request properties

fulfillment_request.message:"Fulfill this ASAP please."

A message for the fulfillment request.

Was this section helpful?

YesNo

post

## /admin/api/2026-01/fulfillment_orders/1046000849/fulfillment_request.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{"fulfillment_request":{"message":"Fulfill this ASAP please."}}' \

-X POST "https://your-development-store.myshopify.com/admin/api/2026-01/fulfillment_orders/1046000849/fulfillment_request.json" \

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

"original_fulfillment_order": {

"id": 1046000849,

"created_at": "2026-01-09T22:36:21-05:00",

"updated_at": "2026-01-09T22:36:22-05:00",

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

"id": 1042572171,

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

### examples

  * #### Sends a fulfillment request to the fulfillment service for all line items on the fulfillment order if fulfillment_order_line_items is left blank

#####

        curl -d '{"fulfillment_request":{"message":"Fulfill this ASAP please."}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/fulfillment_orders/1046000849/fulfillment_request.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const fulfillment_request = new admin.rest.resources.FulfillmentRequest({session: session});

        fulfillment_request.fulfillment_order_id = 1046000849;
        fulfillment_request.message = "Fulfill this ASAP please.";
        await fulfillment_request.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        fulfillment_request = ShopifyAPI::FulfillmentRequest.new(session: test_session)
        fulfillment_request.fulfillment_order_id = 1046000849
        fulfillment_request.message = "Fulfill this ASAP please."
        fulfillment_request.save!

#####

        // Session is built by the OAuth process

        const fulfillment_request = new shopify.rest.FulfillmentRequest({session: session});
        fulfillment_request.fulfillment_order_id = 1046000849;
        fulfillment_request.message = "Fulfill this ASAP please.";
        await fulfillment_request.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"original_fulfillment_order":{"id":1046000849,"created_at":"2026-01-09T22:36:21-05:00","updated_at":"2026-01-09T22:36:22-05:00","shop_id":548380009,"order_id":450789469,"assigned_location_id":24826418,"request_status":"submitted","status":"open","fulfill_at":null,"fulfill_by":null,"supported_actions":["cancel_fulfillment_order"],"destination":{"id":1042572171,"address1":"Chestnut Street 92","address2":"","city":"Louisville","company":null,"country":"United States","email":"bob.norman@mail.example.com","first_name":"Bob","last_name":"Norman","phone":"+1(502)-459-2181","province":"Kentucky","zip":"40202"},"origin":{"address1":null,"address2":null,"city":null,"country_code":"DE","location_id":24826418,"name":"Apple Api Shipwire","phone":null,"province":null,"zip":null},"line_items":[{"id":1072503362,"shop_id":548380009,"fulfillment_order_id":1046000849,"quantity":1,"line_item_id":466157049,"inventory_item_id":39072856,"fulfillable_quantity":1,"variant_id":39072856},{"id":1072503363,"shop_id":548380009,"fulfillment_order_id":1046000849,"quantity":1,"line_item_id":518995019,"inventory_item_id":49148385,"fulfillable_quantity":1,"variant_id":49148385},{"id":1072503364,"shop_id":548380009,"fulfillment_order_id":1046000849,"quantity":1,"line_item_id":703073504,"inventory_item_id":457924702,"fulfillable_quantity":1,"variant_id":457924702}],"outgoing_requests":[{"message":"Fulfill this ASAP please.","request_options":{"notify_customer":false},"sent_at":"2026-01-09T22:36:22-05:00","kind":"fulfillment_request"}],"international_duties":null,"fulfillment_holds":[],"delivery_method":{"id":989232634,"method_type":"shipping","min_delivery_date_time":null,"max_delivery_date_time":null,"additional_information":{"phone":null,"instructions":null,"failed_carriers":null,"pickup_point_id":null},"service_code":null,"detailed_branded_promise":null,"source_reference":null,"presented_name":"Expedited Shipping"}},"submitted_fulfillment_order":{"id":1046000849,"created_at":"2026-01-09T22:36:21-05:00","updated_at":"2026-01-09T22:36:22-05:00","shop_id":548380009,"order_id":450789469,"assigned_location_id":24826418,"request_status":"submitted","status":"open","fulfill_at":null,"fulfill_by":null,"supported_actions":["cancel_fulfillment_order"],"destination":{"id":1042572171,"address1":"Chestnut Street 92","address2":"","city":"Louisville","company":null,"country":"United States","email":"bob.norman@mail.example.com","first_name":"Bob","last_name":"Norman","phone":"+1(502)-459-2181","province":"Kentucky","zip":"40202"},"origin":{"address1":null,"address2":null,"city":null,"country_code":"DE","location_id":24826418,"name":"Apple Api Shipwire","phone":null,"province":null,"zip":null},"line_items":[{"id":1072503362,"shop_id":548380009,"fulfillment_order_id":1046000849,"quantity":1,"line_item_id":466157049,"inventory_item_id":39072856,"fulfillable_quantity":1,"variant_id":39072856},{"id":1072503363,"shop_id":548380009,"fulfillment_order_id":1046000849,"quantity":1,"line_item_id":518995019,"inventory_item_id":49148385,"fulfillable_quantity":1,"variant_id":49148385},{"id":1072503364,"shop_id":548380009,"fulfillment_order_id":1046000849,"quantity":1,"line_item_id":703073504,"inventory_item_id":457924702,"fulfillable_quantity":1,"variant_id":457924702}],"outgoing_requests":[{"message":"Fulfill this ASAP please.","request_options":{"notify_customer":false},"sent_at":"2026-01-09T22:36:22-05:00","kind":"fulfillment_request"}],"international_duties":null,"fulfillment_holds":[],"delivery_method":{"id":989232634,"method_type":"shipping","min_delivery_date_time":null,"max_delivery_date_time":null,"additional_information":{"phone":null,"instructions":null,"failed_carriers":null,"pickup_point_id":null},"service_code":null,"detailed_branded_promise":null,"source_reference":null,"presented_name":"Expedited Shipping"}},"unsubmitted_fulfillment_order":null}

  * #### Sends a fulfillment request to the fulfillment service of a fulfillment order for the specified line items

#####

        curl -d '{"fulfillment_request":{"message":"Fulfill this ASAP please.","fulfillment_order_line_items":[{"id":1072503356,"quantity":1},{"id":1072503357,"quantity":1}],"notify_customer":true}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/fulfillment_orders/1046000846/fulfillment_request.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const fulfillment_request = new admin.rest.resources.FulfillmentRequest({session: session});

        fulfillment_request.fulfillment_order_id = 1046000846;
        fulfillment_request.message = "Fulfill this ASAP please.";
        fulfillment_request.fulfillment_order_line_items = [
          {
            "id": 1072503356,
            "quantity": 1
          },
          {
            "id": 1072503357,
            "quantity": 1
          }
        ];
        fulfillment_request.notify_customer = true;
        await fulfillment_request.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        fulfillment_request = ShopifyAPI::FulfillmentRequest.new(session: test_session)
        fulfillment_request.fulfillment_order_id = 1046000846
        fulfillment_request.message = "Fulfill this ASAP please."
        fulfillment_request.fulfillment_order_line_items = [
          {
            "id" => 1072503356,
            "quantity" => 1
          },
          {
            "id" => 1072503357,
            "quantity" => 1
          }
        ]
        fulfillment_request.notify_customer = true
        fulfillment_request.save!

#####

        // Session is built by the OAuth process

        const fulfillment_request = new shopify.rest.FulfillmentRequest({session: session});
        fulfillment_request.fulfillment_order_id = 1046000846;
        fulfillment_request.message = "Fulfill this ASAP please.";
        fulfillment_request.fulfillment_order_line_items = [
          {
            "id": 1072503356,
            "quantity": 1
          },
          {
            "id": 1072503357,
            "quantity": 1
          }
        ];
        fulfillment_request.notify_customer = true;
        await fulfillment_request.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"original_fulfillment_order":{"id":1046000846,"created_at":"2026-01-09T22:36:16-05:00","updated_at":"2026-01-09T22:36:17-05:00","shop_id":548380009,"order_id":450789469,"assigned_location_id":24826418,"request_status":"submitted","status":"open","fulfill_at":null,"fulfill_by":null,"supported_actions":["cancel_fulfillment_order"],"destination":{"id":1042572168,"address1":"Chestnut Street 92","address2":"","city":"Louisville","company":null,"country":"United States","email":"bob.norman@mail.example.com","first_name":"Bob","last_name":"Norman","phone":"+1(502)-459-2181","province":"Kentucky","zip":"40202"},"origin":{"address1":null,"address2":null,"city":null,"country_code":"DE","location_id":24826418,"name":"Apple Api Shipwire","phone":null,"province":null,"zip":null},"line_items":[{"id":1072503356,"shop_id":548380009,"fulfillment_order_id":1046000846,"quantity":1,"line_item_id":466157049,"inventory_item_id":39072856,"fulfillable_quantity":1,"variant_id":39072856},{"id":1072503357,"shop_id":548380009,"fulfillment_order_id":1046000846,"quantity":1,"line_item_id":518995019,"inventory_item_id":49148385,"fulfillable_quantity":1,"variant_id":49148385}],"outgoing_requests":[{"message":"Fulfill this ASAP please.","request_options":{"notify_customer":true},"sent_at":"2026-01-09T22:36:17-05:00","kind":"fulfillment_request"}],"international_duties":null,"fulfillment_holds":[],"delivery_method":{"id":989232631,"method_type":"shipping","min_delivery_date_time":null,"max_delivery_date_time":null,"additional_information":{"phone":null,"instructions":null,"failed_carriers":null,"pickup_point_id":null},"service_code":null,"detailed_branded_promise":null,"source_reference":null,"presented_name":"Expedited Shipping"}},"submitted_fulfillment_order":{"id":1046000846,"created_at":"2026-01-09T22:36:16-05:00","updated_at":"2026-01-09T22:36:17-05:00","shop_id":548380009,"order_id":450789469,"assigned_location_id":24826418,"request_status":"submitted","status":"open","fulfill_at":null,"fulfill_by":null,"supported_actions":["cancel_fulfillment_order"],"destination":{"id":1042572168,"address1":"Chestnut Street 92","address2":"","city":"Louisville","company":null,"country":"United States","email":"bob.norman@mail.example.com","first_name":"Bob","last_name":"Norman","phone":"+1(502)-459-2181","province":"Kentucky","zip":"40202"},"origin":{"address1":null,"address2":null,"city":null,"country_code":"DE","location_id":24826418,"name":"Apple Api Shipwire","phone":null,"province":null,"zip":null},"line_items":[{"id":1072503356,"shop_id":548380009,"fulfillment_order_id":1046000846,"quantity":1,"line_item_id":466157049,"inventory_item_id":39072856,"fulfillable_quantity":1,"variant_id":39072856},{"id":1072503357,"shop_id":548380009,"fulfillment_order_id":1046000846,"quantity":1,"line_item_id":518995019,"inventory_item_id":49148385,"fulfillable_quantity":1,"variant_id":49148385}],"outgoing_requests":[{"message":"Fulfill this ASAP please.","request_options":{"notify_customer":true},"sent_at":"2026-01-09T22:36:17-05:00","kind":"fulfillment_request"}],"international_duties":null,"fulfillment_holds":[],"delivery_method":{"id":989232631,"method_type":"shipping","min_delivery_date_time":null,"max_delivery_date_time":null,"additional_information":{"phone":null,"instructions":null,"failed_carriers":null,"pickup_point_id":null},"service_code":null,"detailed_branded_promise":null,"source_reference":null,"presented_name":"Expedited Shipping"}},"unsubmitted_fulfillment_order":{"id":1046000847,"created_at":"2026-01-09T22:36:17-05:00","updated_at":"2026-01-09T22:36:17-05:00","shop_id":548380009,"order_id":450789469,"assigned_location_id":24826418,"request_status":"unsubmitted","status":"open","fulfill_at":null,"fulfill_by":null,"supported_actions":["request_fulfillment","create_fulfillment","hold","merge"],"destination":{"id":1042572169,"address1":"Chestnut Street 92","address2":"","city":"Louisville","company":null,"country":"United States","email":"bob.norman@mail.example.com","first_name":"Bob","last_name":"Norman","phone":"+1(502)-459-2181","province":"Kentucky","zip":"40202"},"origin":{"address1":null,"address2":null,"city":null,"country_code":"DE","location_id":24826418,"name":"Apple Api Shipwire","phone":null,"province":null,"zip":null},"line_items":[{"id":1072503358,"shop_id":548380009,"fulfillment_order_id":1046000847,"quantity":1,"line_item_id":703073504,"inventory_item_id":457924702,"fulfillable_quantity":1,"variant_id":457924702}],"outgoing_requests":[],"international_duties":null,"fulfillment_holds":[],"delivery_method":{"id":989232632,"method_type":"shipping","min_delivery_date_time":null,"max_delivery_date_time":null,"additional_information":{"phone":null,"instructions":null,"failed_carriers":null,"pickup_point_id":null},"service_code":null,"detailed_branded_promise":null,"source_reference":null,"presented_name":"Expedited Shipping"}}}


* * *

##

[Anchor to POST request, Accepts a fulfillment request](/docs/api/admin-rest/latest/resources/fulfillmentrequest#post-fulfillment-orders-fulfillment-order-id-fulfillment-request-accept)

post

Accepts a fulfillment request

[fulfillmentOrderAcceptFulfillmentRequest](/docs/api/admin-graphql/latest/mutations/fulfillmentOrderAcceptFulfillmentRequest?example=accepts-a-fulfillment-request)

Requires `assigned_fulfillment_orders` access scope.

**Requires `assigned_fulfillment_orders` access scope.:**

Accepts a fulfillment request sent to a fulfillment service for a fulfillment order.

###

[Anchor to Parameters of Accepts a fulfillment request](/docs/api/admin-rest/latest/resources/fulfillmentrequest#post-fulfillment-orders-fulfillment-order-id-fulfillment-request-accept-parameters)Parameters

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

An optional reason for accepting the fulfillment request.

* * *

Was this section helpful?

YesNo

###

[Anchor to post-fulfillment-orders-fulfillment-order-id-fulfillment-request-accept-examples](/docs/api/admin-rest/latest/resources/fulfillmentrequest#post-fulfillment-orders-fulfillment-order-id-fulfillment-request-accept-examples)Examples

Accepts a fulfillment request sent to a fulfillment service and updates the fulfillment order

Path parameters

fulfillment_order_id=1046000850

string**string**

required**required**

Request body

fulfillment_request

Fulfillment_request resource**Fulfillment_request resource**

Show fulfillment_request properties

fulfillment_request.message:"We will start processing your fulfillment on the next business day."

A message for the fulfillment request.

Was this section helpful?

YesNo

post

## /admin/api/2026-01/fulfillment_orders/1046000850/fulfillment_request/accept.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{"fulfillment_request":{"message":"We will start processing your fulfillment on the next business day."}}' \

-X POST "https://your-development-store.myshopify.com/admin/api/2026-01/fulfillment_orders/1046000850/fulfillment_request/accept.json" \

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

HTTP/1.1 200 OK

{

"fulfillment_order": {

"id": 1046000850,

"created_at": "2026-01-09T22:36:23-05:00",

"updated_at": "2026-01-09T22:36:24-05:00",

"shop_id": 548380009,

"order_id": 450789469,

"assigned_location_id": 24826418,

"request_status": "accepted",

"status": "in_progress",

"fulfill_at": null,

"fulfill_by": null,

"supported_actions": [

"create_fulfillment",

"request_cancellation"

],

"destination": {

"id": 1042572172,

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

"id": 1072503365,

"shop_id": 548380009,

"fulfillment_order_id": 1046000850,

"quantity": 1,

"line_item_id": 466157049,

"inventory_item_id": 39072856,

"fulfillable_quantity": 1,

"variant_id": 39072856

},

{

"id": 1072503366,

"shop_id": 548380009,

"fulfillment_order_id": 1046000850,

"quantity": 1,

"line_item_id": 518995019,

"inventory_item_id": 49148385,

"fulfillable_quantity": 1,

"variant_id": 49148385

},

{

"id": 1072503367,

"shop_id": 548380009,

"fulfillment_order_id": 1046000850,

"quantity": 1,

"line_item_id": 703073504,

"inventory_item_id": 457924702,

"fulfillable_quantity": 1,

"variant_id": 457924702

}

],

"outgoing_requests": [],

"international_duties": null,

"fulfillment_holds": [],

"delivery_method": {

"id": 989232635,

"method_type": "shipping",

"min_delivery_date_time": null,

"max_delivery_date_time": null,

"additional_information": {

"phone": null,

"instructions": null,

"failed_carriers": null,

"pickup_point_id": null

},

"service_code": null,

"detailed_branded_promise": null,

"source_reference": null,

"presented_name": "Expedited Shipping"

}

}

}

### examples

  * #### Accepts a fulfillment request sent to a fulfillment service and updates the fulfillment order

#####

        curl -d '{"fulfillment_request":{"message":"We will start processing your fulfillment on the next business day."}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/fulfillment_orders/1046000850/fulfillment_request/accept.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const fulfillment_request = new admin.rest.resources.FulfillmentRequest({session: session});

        fulfillment_request.fulfillment_order_id = 1046000850;
        await fulfillment_request.accept({
          body: {"fulfillment_request": {"message": "We will start processing your fulfillment on the next business day."}},
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        fulfillment_request = ShopifyAPI::FulfillmentRequest.new(session: test_session)
        fulfillment_request.fulfillment_order_id = 1046000850
        fulfillment_request.accept(
          session: test_session,
          body: {"fulfillment_request" => {"message" => "We will start processing your fulfillment on the next business day."}},
        )

#####

        // Session is built by the OAuth process

        const fulfillment_request = new shopify.rest.FulfillmentRequest({session: session});
        fulfillment_request.fulfillment_order_id = 1046000850;
        await fulfillment_request.accept({
          body: {"fulfillment_request": {"message": "We will start processing your fulfillment on the next business day."}},
        });

#### response

        HTTP/1.1 200 OK{"fulfillment_order":{"id":1046000850,"created_at":"2026-01-09T22:36:23-05:00","updated_at":"2026-01-09T22:36:24-05:00","shop_id":548380009,"order_id":450789469,"assigned_location_id":24826418,"request_status":"accepted","status":"in_progress","fulfill_at":null,"fulfill_by":null,"supported_actions":["create_fulfillment","request_cancellation"],"destination":{"id":1042572172,"address1":"Chestnut Street 92","address2":"","city":"Louisville","company":null,"country":"United States","email":"bob.norman@mail.example.com","first_name":"Bob","last_name":"Norman","phone":"+1(502)-459-2181","province":"Kentucky","zip":"40202"},"origin":{"address1":null,"address2":null,"city":null,"country_code":"DE","location_id":24826418,"name":"Apple Api Shipwire","phone":null,"province":null,"zip":null},"line_items":[{"id":1072503365,"shop_id":548380009,"fulfillment_order_id":1046000850,"quantity":1,"line_item_id":466157049,"inventory_item_id":39072856,"fulfillable_quantity":1,"variant_id":39072856},{"id":1072503366,"shop_id":548380009,"fulfillment_order_id":1046000850,"quantity":1,"line_item_id":518995019,"inventory_item_id":49148385,"fulfillable_quantity":1,"variant_id":49148385},{"id":1072503367,"shop_id":548380009,"fulfillment_order_id":1046000850,"quantity":1,"line_item_id":703073504,"inventory_item_id":457924702,"fulfillable_quantity":1,"variant_id":457924702}],"outgoing_requests":[],"international_duties":null,"fulfillment_holds":[],"delivery_method":{"id":989232635,"method_type":"shipping","min_delivery_date_time":null,"max_delivery_date_time":null,"additional_information":{"phone":null,"instructions":null,"failed_carriers":null,"pickup_point_id":null},"service_code":null,"detailed_branded_promise":null,"source_reference":null,"presented_name":"Expedited Shipping"}}}


* * *

##

[Anchor to POST request, Rejects a fulfillment request](/docs/api/admin-rest/latest/resources/fulfillmentrequest#post-fulfillment-orders-fulfillment-order-id-fulfillment-request-reject)

post

Rejects a fulfillment request

[fulfillmentOrderRejectFulfillmentRequest](/docs/api/admin-graphql/latest/mutations/fulfillmentOrderRejectFulfillmentRequest?example=rejects-a-fulfillment-request)

Requires `assigned_fulfillment_orders` access scope.

**Requires `assigned_fulfillment_orders` access scope.:**

Rejects a fulfillment request sent to a fulfillment service for a fulfillment order.

###

[Anchor to Parameters of Rejects a fulfillment request](/docs/api/admin-rest/latest/resources/fulfillmentrequest#post-fulfillment-orders-fulfillment-order-id-fulfillment-request-reject-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

fulfillment_order_id

string**string**

required**required**

* * *

line_items

array**array**

An optional array of line item rejection details. If none are provided, all line items will be assumed to be unfulfillable.

**Note** : After the fulfillment request has been rejected, none of the line items will be able to be fulfilled. This field documents which line items specifically were unable to be fulfilled and why.

Each line item has the following properties:

Show line_items properties

  * **fulfillment_order_line_item_id** : An identifier for the line item which cannot be fulfilled.
  * **message** : An optional message describing why the line item cannot be fulfilled. (150 characters maximum)


* * *

message

An optional message for rejecting the fulfillment request.

* * *

reason

enum**enum**

An optional reason for the fulfillment request rejection.

Show reason properties

  * **incorrect_address** : The fulfillment request was rejected because of an incorrect address.

  * **inventory_out_of_stock** : The fulfillment request was rejected because inventory is out of stock.

  * **ineligible_product** : The fulfillment request was rejected because of an ineligible product.

  * **undeliverable_destination** : The fulfillment request was rejected because of an undeliverable destination.

  * **other** : The fulfillment request was rejected for another reason.


* * *

Was this section helpful?

YesNo

###

[Anchor to post-fulfillment-orders-fulfillment-order-id-fulfillment-request-reject-examples](/docs/api/admin-rest/latest/resources/fulfillmentrequest#post-fulfillment-orders-fulfillment-order-id-fulfillment-request-reject-examples)Examples

Rejects a fulfillment request sent to a fulfillment service and updates the fulfillment order

Path parameters

fulfillment_order_id=1046000848

string**string**

required**required**

Request body

fulfillment_request

Fulfillment_request resource**Fulfillment_request resource**

Show fulfillment_request properties

fulfillment_request.message:"Not enough inventory on hand to complete the work."

A message for the fulfillment request.

Was this section helpful?

YesNo

post

## /admin/api/2026-01/fulfillment_orders/1046000848/fulfillment_request/reject.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{"fulfillment_request":{"message":"Not enough inventory on hand to complete the work.","reason":"inventory_out_of_stock","line_items":[{"fulfillment_order_line_item_id":1072503359,"message":"Not enough inventory."}]}}' \

-X POST "https://your-development-store.myshopify.com/admin/api/2026-01/fulfillment_orders/1046000848/fulfillment_request/reject.json" \

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

HTTP/1.1 200 OK

{

"fulfillment_order": {

"id": 1046000848,

"created_at": "2026-01-09T22:36:19-05:00",

"updated_at": "2026-01-09T22:36:20-05:00",

"shop_id": 548380009,

"order_id": 450789469,

"assigned_location_id": 24826418,

"request_status": "rejected",

"status": "open",

"fulfill_at": null,

"fulfill_by": null,

"supported_actions": [

"request_fulfillment",

"create_fulfillment",

"hold",

"split"

],

"destination": {

"id": 1042572170,

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

"id": 1072503359,

"shop_id": 548380009,

"fulfillment_order_id": 1046000848,

"quantity": 1,

"line_item_id": 466157049,

"inventory_item_id": 39072856,

"fulfillable_quantity": 1,

"variant_id": 39072856

},

{

"id": 1072503360,

"shop_id": 548380009,

"fulfillment_order_id": 1046000848,

"quantity": 1,

"line_item_id": 518995019,

"inventory_item_id": 49148385,

"fulfillable_quantity": 1,

"variant_id": 49148385

},

{

"id": 1072503361,

"shop_id": 548380009,

"fulfillment_order_id": 1046000848,

"quantity": 1,

"line_item_id": 703073504,

"inventory_item_id": 457924702,

"fulfillable_quantity": 1,

"variant_id": 457924702

}

],

"outgoing_requests": [],

"international_duties": null,

"fulfillment_holds": [],

"delivery_method": {

"id": 989232633,

"method_type": "shipping",

"min_delivery_date_time": null,

"max_delivery_date_time": null,

"additional_information": {

"phone": null,

"instructions": null,

"failed_carriers": null,

"pickup_point_id": null

},

"service_code": null,

"detailed_branded_promise": null,

"source_reference": null,

"presented_name": "Expedited Shipping"

}

}

}

### examples

  * #### Rejects a fulfillment request sent to a fulfillment service and updates the fulfillment order

#####

        curl -d '{"fulfillment_request":{"message":"Not enough inventory on hand to complete the work.","reason":"inventory_out_of_stock","line_items":[{"fulfillment_order_line_item_id":1072503359,"message":"Not enough inventory."}]}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/fulfillment_orders/1046000848/fulfillment_request/reject.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const fulfillment_request = new admin.rest.resources.FulfillmentRequest({session: session});

        fulfillment_request.fulfillment_order_id = 1046000848;
        await fulfillment_request.reject({
          body: {"fulfillment_request": {"message": "Not enough inventory on hand to complete the work.", "reason": "inventory_out_of_stock", "line_items": [{"fulfillment_order_line_item_id": 1072503359, "message": "Not enough inventory."}]}},
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        fulfillment_request = ShopifyAPI::FulfillmentRequest.new(session: test_session)
        fulfillment_request.fulfillment_order_id = 1046000848
        fulfillment_request.reject(
          session: test_session,
          body: {"fulfillment_request" => {"message" => "Not enough inventory on hand to complete the work.", "reason" => "inventory_out_of_stock", "line_items" => [{"fulfillment_order_line_item_id" => 1072503359, "message" => "Not enough inventory."}]}},
        )

#####

        // Session is built by the OAuth process

        const fulfillment_request = new shopify.rest.FulfillmentRequest({session: session});
        fulfillment_request.fulfillment_order_id = 1046000848;
        await fulfillment_request.reject({
          body: {"fulfillment_request": {"message": "Not enough inventory on hand to complete the work.", "reason": "inventory_out_of_stock", "line_items": [{"fulfillment_order_line_item_id": 1072503359, "message": "Not enough inventory."}]}},
        });

#### response

        HTTP/1.1 200 OK{"fulfillment_order":{"id":1046000848,"created_at":"2026-01-09T22:36:19-05:00","updated_at":"2026-01-09T22:36:20-05:00","shop_id":548380009,"order_id":450789469,"assigned_location_id":24826418,"request_status":"rejected","status":"open","fulfill_at":null,"fulfill_by":null,"supported_actions":["request_fulfillment","create_fulfillment","hold","split"],"destination":{"id":1042572170,"address1":"Chestnut Street 92","address2":"","city":"Louisville","company":null,"country":"United States","email":"bob.norman@mail.example.com","first_name":"Bob","last_name":"Norman","phone":"+1(502)-459-2181","province":"Kentucky","zip":"40202"},"origin":{"address1":null,"address2":null,"city":null,"country_code":"DE","location_id":24826418,"name":"Apple Api Shipwire","phone":null,"province":null,"zip":null},"line_items":[{"id":1072503359,"shop_id":548380009,"fulfillment_order_id":1046000848,"quantity":1,"line_item_id":466157049,"inventory_item_id":39072856,"fulfillable_quantity":1,"variant_id":39072856},{"id":1072503360,"shop_id":548380009,"fulfillment_order_id":1046000848,"quantity":1,"line_item_id":518995019,"inventory_item_id":49148385,"fulfillable_quantity":1,"variant_id":49148385},{"id":1072503361,"shop_id":548380009,"fulfillment_order_id":1046000848,"quantity":1,"line_item_id":703073504,"inventory_item_id":457924702,"fulfillable_quantity":1,"variant_id":457924702}],"outgoing_requests":[],"international_duties":null,"fulfillment_holds":[],"delivery_method":{"id":989232633,"method_type":"shipping","min_delivery_date_time":null,"max_delivery_date_time":null,"additional_information":{"phone":null,"instructions":null,"failed_carriers":null,"pickup_point_id":null},"service_code":null,"detailed_branded_promise":null,"source_reference":null,"presented_name":"Expedited Shipping"}}}