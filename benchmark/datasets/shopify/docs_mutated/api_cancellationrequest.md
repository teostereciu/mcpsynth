# CancellationRequest

*Source: https://shopify.dev/docs/api/admin-rest/2026-01/resources/cancellationrequest*

---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04

2026-01latest

# CancellationRequest

Ask assistant

Multiple access scopes needed — refer to each endpoint for access scope requirements.

**Multiple access scopes needed — refer to each endpoint for access scope requirements.:**

The `CancellationRequest` resource represents a cancellation request made by the merchant or an order management app to a [fulfillment service](/docs/admin-api/rest/reference/shipping-and-fulfillment/fulfillmentservice) for a [fulfillment order](/docs/admin-api/rest/reference/shipping-and-fulfillment/fulfillmentorder). A fulfillment service can accept or reject the cancellation request.

## Retrieving cancellation request details

The `FulfillmentOrder` resource and the `merchant_requests` field can be used to retrieve the merchant requests which have been made. The overall status of these requests is also available using the `request_status` field of the fulfillment order.

To learn more about the cancellation request process in the fulfillment workflow, refer to [Manage fulfillments as a fulfillment service app](/apps/fulfillment/fulfillment-service-apps/manage-fulfillments) guide.

Was this section helpful?

YesNo

#

## Endpoints

  * [post/admin/api/latest/fulfillment_orders/{fulfillment_order_id}/cancellation_request.json](/docs/api/admin-rest/latest/resources/cancellationrequest#post-fulfillment-orders-fulfillment-order-id-cancellation-request)

Sends a cancellation request

[fulfillmentOrderSubmitCancellationRequest](/docs/api/admin-graphql/latest/mutations/fulfillmentOrderSubmitCancellationRequest?example=sends-a-cancellation-request)

  * [post/admin/api/latest/fulfillment_orders/{fulfillment_order_id}/cancellation_request/accept.json](/docs/api/admin-rest/latest/resources/cancellationrequest#post-fulfillment-orders-fulfillment-order-id-cancellation-request-accept)

Accepts a cancellation request

[fulfillmentOrderAcceptCancellationRequest](/docs/api/admin-graphql/latest/mutations/fulfillmentOrderAcceptCancellationRequest?example=accepts-a-cancellation-request)

  * [post/admin/api/latest/fulfillment_orders/{fulfillment_order_id}/cancellation_request/reject.json](/docs/api/admin-rest/latest/resources/cancellationrequest#post-fulfillment-orders-fulfillment-order-id-cancellation-request-reject)

Rejects a cancellation request

[fulfillmentOrderRejectCancellationRequest](/docs/api/admin-graphql/latest/mutations/fulfillmentOrderRejectCancellationRequest?example=rejects-a-cancellation-request)


* * *

[Anchor to ](/docs/api/admin-rest/latest/resources/cancellationrequest#resource-object)

## The CancellationRequest resource

[Anchor to ](/docs/api/admin-rest/latest/resources/cancellationrequest#resource-object-properties)

### Properties

* * *

Was this section helpful?

YesNo

{}

## The CancellationRequest resource

9

1

{}

* * *

##

[Anchor to POST request, Sends a cancellation request](/docs/api/admin-rest/latest/resources/cancellationrequest#post-fulfillment-orders-fulfillment-order-id-cancellation-request)

post

Sends a cancellation request

[fulfillmentOrderSubmitCancellationRequest](/docs/api/admin-graphql/latest/mutations/fulfillmentOrderSubmitCancellationRequest?example=sends-a-cancellation-request)

Requires `third_party_fulfillment_orders` access scope.

**Requires `third_party_fulfillment_orders` access scope.:**

Sends a cancellation request to the fulfillment service of a fulfillment order.

###

[Anchor to Parameters of Sends a cancellation request](/docs/api/admin-rest/latest/resources/cancellationrequest#post-fulfillment-orders-fulfillment-order-id-cancellation-request-parameters)Parameters

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

An optional reason for the cancellation request.

* * *

Was this section helpful?

YesNo

###

[Anchor to post-fulfillment-orders-fulfillment-order-id-cancellation-request-examples](/docs/api/admin-rest/latest/resources/cancellationrequest#post-fulfillment-orders-fulfillment-order-id-cancellation-request-examples)Examples

Sends a cancellation request to the fulfillment service of a fulfillment order and updates the fulfillment order

Path parameters

fulfillment_order_id=1046000842

string**string**

required**required**

Was this section helpful?

YesNo

post

## /admin/api/2026-01/fulfillment_orders/1046000842/cancellation_request.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{"cancellation_request":{"message":"The customer changed his mind."}}' \

-X POST "https://your-development-store.myshopify.com/admin/api/2026-01/fulfillment_orders/1046000842/cancellation_request.json" \

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

"fulfillment_order": {

"id": 1046000842,

"created_at": "2026-01-09T17:34:28-05:00",

"updated_at": "2026-01-09T17:34:28-05:00",

"shop_id": 548380009,

"order_id": 450789469,

"assigned_location_id": 24826418,

"request_status": "cancellation_requested",

"status": "in_progress",

"fulfill_at": null,

"fulfill_by": null,

"supported_actions": [

"create_fulfillment",

"cancel_fulfillment_order"

],

"destination": {

"id": 1042572165,

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

"id": 1072503353,

"shop_id": 548380009,

"fulfillment_order_id": 1046000842,

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

  * #### Sends a cancellation request to the fulfillment service of a fulfillment order and updates the fulfillment order

#####

        curl -d '{"cancellation_request":{"message":"The customer changed his mind."}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/fulfillment_orders/1046000842/cancellation_request.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const cancellation_request = new admin.rest.resources.CancellationRequest({session: session});

        cancellation_request.fulfillment_order_id = 1046000842;
        cancellation_request.message = "The customer changed his mind.";
        await cancellation_request.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        cancellation_request = ShopifyAPI::CancellationRequest.new(session: test_session)
        cancellation_request.fulfillment_order_id = 1046000842
        cancellation_request.message = "The customer changed his mind."
        cancellation_request.save!

#####

        // Session is built by the OAuth process

        const cancellation_request = new shopify.rest.CancellationRequest({session: session});
        cancellation_request.fulfillment_order_id = 1046000842;
        cancellation_request.message = "The customer changed his mind.";
        await cancellation_request.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"fulfillment_order":{"id":1046000842,"created_at":"2026-01-09T17:34:28-05:00","updated_at":"2026-01-09T17:34:28-05:00","shop_id":548380009,"order_id":450789469,"assigned_location_id":24826418,"request_status":"cancellation_requested","status":"in_progress","fulfill_at":null,"fulfill_by":null,"supported_actions":["create_fulfillment","cancel_fulfillment_order"],"destination":{"id":1042572165,"address1":"Chestnut Street 92","address2":"","city":"Louisville","company":null,"country":"United States","email":"bob.norman@mail.example.com","first_name":"Bob","last_name":"Norman","phone":"+1(502)-459-2181","province":"Kentucky","zip":"40202"},"origin":{"address1":null,"address2":null,"city":null,"country_code":"DE","location_id":24826418,"name":"Apple Api Shipwire","phone":null,"province":null,"zip":null},"line_items":[{"id":1072503353,"shop_id":548380009,"fulfillment_order_id":1046000842,"quantity":1,"line_item_id":518995019,"inventory_item_id":49148385,"fulfillable_quantity":1,"variant_id":49148385}],"outgoing_requests":[],"international_duties":null,"fulfillment_holds":[],"delivery_method":null}}


* * *

##

[Anchor to POST request, Accepts a cancellation request](/docs/api/admin-rest/latest/resources/cancellationrequest#post-fulfillment-orders-fulfillment-order-id-cancellation-request-accept)

post

Accepts a cancellation request

[fulfillmentOrderAcceptCancellationRequest](/docs/api/admin-graphql/latest/mutations/fulfillmentOrderAcceptCancellationRequest?example=accepts-a-cancellation-request)

Requires `assigned_fulfillment_orders` access scope.

**Requires `assigned_fulfillment_orders` access scope.:**

Accepts a cancellation request sent to a fulfillment service for a fulfillment order.

###

[Anchor to Parameters of Accepts a cancellation request](/docs/api/admin-rest/latest/resources/cancellationrequest#post-fulfillment-orders-fulfillment-order-id-cancellation-request-accept-parameters)Parameters

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

An optional reason for accepting the cancellation request.

* * *

Was this section helpful?

YesNo

###

[Anchor to post-fulfillment-orders-fulfillment-order-id-cancellation-request-accept-examples](/docs/api/admin-rest/latest/resources/cancellationrequest#post-fulfillment-orders-fulfillment-order-id-cancellation-request-accept-examples)Examples

Accepts a cancellation request sent to a fulfillment service and updates the fulfillment order

Path parameters

fulfillment_order_id=1046000843

string**string**

required**required**

Was this section helpful?

YesNo

post

## /admin/api/2026-01/fulfillment_orders/1046000843/cancellation_request/accept.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{"cancellation_request":{"message":"We had not started any processing yet."}}' \

-X POST "https://your-development-store.myshopify.com/admin/api/2026-01/fulfillment_orders/1046000843/cancellation_request/accept.json" \

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

"id": 1046000843,

"created_at": "2026-01-09T17:34:29-05:00",

"updated_at": "2026-01-09T17:34:30-05:00",

"shop_id": 548380009,

"order_id": 450789469,

"assigned_location_id": 24826418,

"request_status": "cancellation_accepted",

"status": "cancelled",

"fulfill_at": null,

"fulfill_by": null,

"supported_actions": [

"request_fulfillment",

"create_fulfillment",

"hold"

],

"destination": {

"id": 1042572166,

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

"id": 1072503354,

"shop_id": 548380009,

"fulfillment_order_id": 1046000843,

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

  * #### Accepts a cancellation request sent to a fulfillment service and updates the fulfillment order

#####

        curl -d '{"cancellation_request":{"message":"We had not started any processing yet."}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/fulfillment_orders/1046000843/cancellation_request/accept.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const cancellation_request = new admin.rest.resources.CancellationRequest({session: session});

        cancellation_request.fulfillment_order_id = 1046000843;
        await cancellation_request.accept({
          body: {"cancellation_request": {"message": "We had not started any processing yet."}},
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        cancellation_request = ShopifyAPI::CancellationRequest.new(session: test_session)
        cancellation_request.fulfillment_order_id = 1046000843
        cancellation_request.accept(
          session: test_session,
          body: {"cancellation_request" => {"message" => "We had not started any processing yet."}},
        )

#####

        // Session is built by the OAuth process

        const cancellation_request = new shopify.rest.CancellationRequest({session: session});
        cancellation_request.fulfillment_order_id = 1046000843;
        await cancellation_request.accept({
          body: {"cancellation_request": {"message": "We had not started any processing yet."}},
        });

#### response

        HTTP/1.1 200 OK{"fulfillment_order":{"id":1046000843,"created_at":"2026-01-09T17:34:29-05:00","updated_at":"2026-01-09T17:34:30-05:00","shop_id":548380009,"order_id":450789469,"assigned_location_id":24826418,"request_status":"cancellation_accepted","status":"cancelled","fulfill_at":null,"fulfill_by":null,"supported_actions":["request_fulfillment","create_fulfillment","hold"],"destination":{"id":1042572166,"address1":"Chestnut Street 92","address2":"","city":"Louisville","company":null,"country":"United States","email":"bob.norman@mail.example.com","first_name":"Bob","last_name":"Norman","phone":"+1(502)-459-2181","province":"Kentucky","zip":"40202"},"origin":{"address1":null,"address2":null,"city":null,"country_code":"DE","location_id":24826418,"name":"Apple Api Shipwire","phone":null,"province":null,"zip":null},"line_items":[{"id":1072503354,"shop_id":548380009,"fulfillment_order_id":1046000843,"quantity":1,"line_item_id":518995019,"inventory_item_id":49148385,"fulfillable_quantity":1,"variant_id":49148385}],"outgoing_requests":[],"international_duties":null,"fulfillment_holds":[],"delivery_method":null}}


* * *

##

[Anchor to POST request, Rejects a cancellation request](/docs/api/admin-rest/latest/resources/cancellationrequest#post-fulfillment-orders-fulfillment-order-id-cancellation-request-reject)

post

Rejects a cancellation request

[fulfillmentOrderRejectCancellationRequest](/docs/api/admin-graphql/latest/mutations/fulfillmentOrderRejectCancellationRequest?example=rejects-a-cancellation-request)

Requires `assigned_fulfillment_orders` access scope.

**Requires `assigned_fulfillment_orders` access scope.:**

Rejects a cancellation request sent to a fulfillment service for a fulfillment order.

###

[Anchor to Parameters of Rejects a cancellation request](/docs/api/admin-rest/latest/resources/cancellationrequest#post-fulfillment-orders-fulfillment-order-id-cancellation-request-reject-parameters)Parameters

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

An optional reason for rejecting the cancellation request.

* * *

Was this section helpful?

YesNo

###

[Anchor to post-fulfillment-orders-fulfillment-order-id-cancellation-request-reject-examples](/docs/api/admin-rest/latest/resources/cancellationrequest#post-fulfillment-orders-fulfillment-order-id-cancellation-request-reject-examples)Examples

Rejects a cancellation request sent to a fulfillment service and updates the fulfillment order

Path parameters

fulfillment_order_id=1046000841

string**string**

required**required**

Was this section helpful?

YesNo

post

## /admin/api/2026-01/fulfillment_orders/1046000841/cancellation_request/reject.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{"cancellation_request":{"message":"We have already sent the shipment out."}}' \

-X POST "https://your-development-store.myshopify.com/admin/api/2026-01/fulfillment_orders/1046000841/cancellation_request/reject.json" \

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

"id": 1046000841,

"created_at": "2026-01-09T17:34:27-05:00",

"updated_at": "2026-01-09T17:34:28-05:00",

"shop_id": 548380009,

"order_id": 450789469,

"assigned_location_id": 24826418,

"request_status": "cancellation_rejected",

"status": "in_progress",

"fulfill_at": null,

"fulfill_by": null,

"supported_actions": [

"create_fulfillment"

],

"destination": {

"id": 1042572164,

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

"id": 1072503352,

"shop_id": 548380009,

"fulfillment_order_id": 1046000841,

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

  * #### Rejects a cancellation request sent to a fulfillment service and updates the fulfillment order

#####

        curl -d '{"cancellation_request":{"message":"We have already sent the shipment out."}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/fulfillment_orders/1046000841/cancellation_request/reject.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const cancellation_request = new admin.rest.resources.CancellationRequest({session: session});

        cancellation_request.fulfillment_order_id = 1046000841;
        await cancellation_request.reject({
          body: {"cancellation_request": {"message": "We have already sent the shipment out."}},
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        cancellation_request = ShopifyAPI::CancellationRequest.new(session: test_session)
        cancellation_request.fulfillment_order_id = 1046000841
        cancellation_request.reject(
          session: test_session,
          body: {"cancellation_request" => {"message" => "We have already sent the shipment out."}},
        )

#####

        // Session is built by the OAuth process

        const cancellation_request = new shopify.rest.CancellationRequest({session: session});
        cancellation_request.fulfillment_order_id = 1046000841;
        await cancellation_request.reject({
          body: {"cancellation_request": {"message": "We have already sent the shipment out."}},
        });

#### response

        HTTP/1.1 200 OK{"fulfillment_order":{"id":1046000841,"created_at":"2026-01-09T17:34:27-05:00","updated_at":"2026-01-09T17:34:28-05:00","shop_id":548380009,"order_id":450789469,"assigned_location_id":24826418,"request_status":"cancellation_rejected","status":"in_progress","fulfill_at":null,"fulfill_by":null,"supported_actions":["create_fulfillment"],"destination":{"id":1042572164,"address1":"Chestnut Street 92","address2":"","city":"Louisville","company":null,"country":"United States","email":"bob.norman@mail.example.com","first_name":"Bob","last_name":"Norman","phone":"+1(502)-459-2181","province":"Kentucky","zip":"40202"},"origin":{"address1":null,"address2":null,"city":null,"country_code":"DE","location_id":24826418,"name":"Apple Api Shipwire","phone":null,"province":null,"zip":null},"line_items":[{"id":1072503352,"shop_id":548380009,"fulfillment_order_id":1046000841,"quantity":1,"line_item_id":518995019,"inventory_item_id":49148385,"fulfillable_quantity":1,"variant_id":49148385}],"outgoing_requests":[],"international_duties":null,"fulfillment_holds":[],"delivery_method":null}}