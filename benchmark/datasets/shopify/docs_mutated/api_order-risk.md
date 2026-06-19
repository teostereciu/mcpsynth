# Order Risk

*Source: https://shopify.dev/docs/api/admin-rest/2026-01/resources/order-risk*

---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04

2026-01latest

# Order Risk

Ask assistant

Requires `orders` access scope.

**Requires `orders` access scope.:**

The Order Risk resource allows you to create, retrieve, update, and delete order risks. Order risks represent the results of fraud checks that have been completed for an order.

#### Usage notes

Caution

As of version 2024-04 this resource is deprecated. Risk Assessments can be queried via the [Order Risk Assessment API](https://shopify.dev/docs/api/admin-graphql/2024-04/objects/OrderRiskAssessment).

**Caution:**

As of version 2024-04 this resource is deprecated. Risk Assessments can be queried via the [Order Risk Assessment API](https://shopify.dev/docs/api/admin-graphql/2024-04/objects/OrderRiskAssessment).

  * This resource is deprecated in version 2024-04. Please refer to the GraphQL api for [Order#field-order-risk](https://shopify.dev/docs/api/admin-graphql/2024-04/objects/Order#field-order-risk)
  * When determining an order's risk level, Shopify takes into account only those order risks that have the display property set to `true`. Orders with a display set to `false` will not be returned through the Order Risk resource. It's not advised to create order risks with a display set to `false`. This property might be removed in future API versions.
  * Risk assessments will favor the most severe risk recommendation for an order. Keep this in mind when creating new order risks.


Was this section helpful?

YesNo

#

## Endpoints

  * [post/admin/api/latest/orders/{order_id}/risks.json](/docs/api/admin-rest/latest/resources/order-risk#post-orders-order-id-risks)

Creates an order risk for an order

[orderRiskAssessmentCreate](/docs/api/admin-graphql/latest/mutations/orderRiskAssessmentCreate?example=creates-an-order-risk-for-an-order)

  * [get/admin/api/latest/orders/{order_id}/risks.json](/docs/api/admin-rest/latest/resources/order-risk#get-orders-order-id-risks)

Retrieves a list of all order risks for an order

[order](/docs/api/admin-graphql/latest/queries/order)

  * [get/admin/api/latest/orders/{order_id}/risks/{risk_id}.json](/docs/api/admin-rest/latest/resources/order-risk#get-orders-order-id-risks-risk-id)

Retrieves a single order risk by its ID

deprecated

**

deprecated

**

  * [ put/admin/api/latest/orders/{order_id}/risks/{risk_id}.json](/docs/api/admin-rest/latest/resources/order-risk#put-orders-order-id-risks-risk-id)

Updates an order risk

deprecated

**

deprecated

**

  * [ del/admin/api/latest/orders/{order_id}/risks/{risk_id}.json](/docs/api/admin-rest/latest/resources/order-risk#delete-orders-order-id-risks-risk-id)

Deletes an order risk for an order

deprecated

**

deprecated

**


* * *

[ Anchor to ](/docs/api/admin-rest/latest/resources/order-risk#resource-object)

## The Order Risk resource

[Anchor to ](/docs/api/admin-rest/latest/resources/order-risk#resource-object-properties)

### Properties

* * *

cause_cancel

->[recommendation](/docs/api/admin-graphql/latest/objects/OrderRiskSummary#field-OrderRiskSummary.fields.recommendation)

Whether this order risk is severe enough to force the cancellation of the order. If `true`, then this order risk is included in the **Order canceled** message that's shown on the details page of the canceled order.

**Note:** Setting this property to `true` does not cancel the order. Use this property only if your app automatically cancels the order using the [Order](/docs/admin-api/rest/reference/orders/order/#cancel-{{ current_version }}) resource. If your app doesn't automatically cancel orders based on order risks, then leave this property set to `false`.

* * *

checkout_id

deprecated**deprecated**

The ID of the checkout that the order risk belongs to.

* * *

display

deprecated**deprecated**

Whether the order risk is displayed on the order details page in the Shopify admin. If `false`, then this order risk is ignored when Shopify determines your app's overall risk level for the order.<p>It's not advised to create order risks with a display set to `false`.

<aside class='note'><p>This property can't be changed after an order risk is created.

This property might be removed in future API versions.

* * *

id

deprecated**deprecated**

A unique numeric identifier for the order risk.

* * *

merchant_message

deprecated**deprecated**

The message that's displayed to the merchant to indicate the results of the fraud check. The message is displayed only if `display` is set to`true`.

* * *

message

->[description](/docs/api/admin-graphql/latest/objects/RiskFact#field-RiskFact.fields.description)

The message that's displayed to the merchant to indicate the results of the fraud check. The message is displayed only if `display` is set to`true`.

* * *

order_id

->[id](/docs/api/admin-graphql/latest/objects/Order#field-Order.fields.id)

The ID of the order that the order risk belongs to.

* * *

recommendation

->[recommendation](/docs/api/admin-graphql/latest/objects/OrderRiskSummary#field-OrderRiskSummary.fields.recommendation)

The recommended action given to the merchant. Valid values:

Show recommendation properties

  * **cancel** : There is a high level of risk that this order is fraudulent. The merchant should cancel the order.
  * **investigate** : There is a medium level of risk that this order is fraudulent. The merchant should investigate the order.
  * **accept** : There is a low level of risk that this order is fraudulent. The order risk found no indication of fraud.


* * *

score

string**string**

->[riskLevel](/docs/api/admin-graphql/latest/objects/OrderRiskAssessment#field-OrderRiskAssessment.fields.riskLevel)

**For internal use only**. A number between 0 and 1 that's assigned to the order. The closer the score is to 1, the more likely it is that the order is fraudulent.

Note

There is no guarantee of stability in risk scores. Scores are not probabilities. The relationship between scores and the probability of fraud can vary over time and between risk providers.

**Note:**

There is no guarantee of stability in risk scores. Scores are not probabilities. The relationship between scores and the probability of fraud can vary over time and between risk providers.

* * *

source

->[provider](/docs/api/admin-graphql/latest/objects/OrderRiskAssessment#field-OrderRiskAssessment.fields.provider)

The source of the order risk.

* * *

Was this section helpful?

YesNo

{}

## The Order Risk resource

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

{

"cause_cancel": false,

"checkout_id": 901414060,

"display": true,

"id": 284138680,

"merchant_message": "This order came from an anonymous proxy.",

"message": "This order came from an anonymous proxy.",

"order_id": 450789469,

"recommendation": "cancel",

"score": "1.0",

"source": "External"

}

* * *

##

[Anchor to POST request, Creates an order risk for an order](/docs/api/admin-rest/latest/resources/order-risk#post-orders-order-id-risks)

post

Creates an order risk for an order

[orderRiskAssessmentCreate](/docs/api/admin-graphql/latest/mutations/orderRiskAssessmentCreate?example=creates-an-order-risk-for-an-order)

Creates an order risk for an order

###

[Anchor to Parameters of Creates an order risk for an order](/docs/api/admin-rest/latest/resources/order-risk#post-orders-order-id-risks-parameters)Parameters

* * *

api_version

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

[Anchor to post-orders-order-id-risks-examples](/docs/api/admin-rest/latest/resources/order-risk#post-orders-order-id-risks-examples)Examples

Create an order risk showing a fraud risk for proxy detection

Path parameters

order_id=450789469

string**string**

required**required**

Was this section helpful?

YesNo

post

## /admin/api/2026-01/orders/450789469/risks.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{"risk":{"message":"This order came from an anonymous proxy","recommendation":"cancel","score":"1.0","source":"External","cause_cancel":true,"display":true}}' \

-X POST "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469/risks.json" \

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

HTTP/1.1 201 Created

{

"risk": {

"id": 1029151492,

"order_id": 450789469,

"checkout_id": 901414060,

"source": "External",

"score": "1.0",

"recommendation": "cancel",

"display": true,

"cause_cancel": true,

"message": "This order came from an anonymous proxy",

"merchant_message": "This order came from an anonymous proxy"

}

}

### examples

  * #### Create an order risk showing a fraud risk for proxy detection

#####

        curl -d '{"risk":{"message":"This order came from an anonymous proxy","recommendation":"cancel","score":"1.0","source":"External","cause_cancel":true,"display":true}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469/risks.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const order_risk = new admin.rest.resources.OrderRisk({session: session});

        order_risk.order_id = 450789469;
        order_risk.message = "This order came from an anonymous proxy";
        order_risk.recommendation = "cancel";
        order_risk.score = "1.0";
        order_risk.source = "External";
        order_risk.cause_cancel = true;
        order_risk.display = true;
        await order_risk.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        order_risk = ShopifyAPI::OrderRisk.new(session: test_session)
        order_risk.order_id = 450789469
        order_risk.message = "This order came from an anonymous proxy"
        order_risk.recommendation = "cancel"
        order_risk.score = "1.0"
        order_risk.source = "External"
        order_risk.cause_cancel = true
        order_risk.display = true
        order_risk.save!

#####

        // Session is built by the OAuth process

        const order_risk = new shopify.rest.OrderRisk({session: session});
        order_risk.order_id = 450789469;
        order_risk.message = "This order came from an anonymous proxy";
        order_risk.recommendation = "cancel";
        order_risk.score = "1.0";
        order_risk.source = "External";
        order_risk.cause_cancel = true;
        order_risk.display = true;
        await order_risk.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"risk":{"id":1029151492,"order_id":450789469,"checkout_id":901414060,"source":"External","score":"1.0","recommendation":"cancel","display":true,"cause_cancel":true,"message":"This order came from an anonymous proxy","merchant_message":"This order came from an anonymous proxy"}}


* * *

##

[Anchor to GET request, Retrieves a list of all order risks for an order](/docs/api/admin-rest/latest/resources/order-risk#get-orders-order-id-risks)

get

Retrieves a list of all order risks for an order

[order](/docs/api/admin-graphql/latest/queries/order)

Retrieves a list of all order risks for an order. **Note:** This endpoint implements pagination by using links that are provided in the response header. To learn more, refer to [Make paginated requests to the REST Admin API](/api/usage/pagination-rest).

###

[Anchor to Parameters of Retrieves a list of all order risks for an order](/docs/api/admin-rest/latest/resources/order-risk#get-orders-order-id-risks-parameters)Parameters

* * *

api_version

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

[Anchor to get-orders-order-id-risks-examples](/docs/api/admin-rest/latest/resources/order-risk#get-orders-order-id-risks-examples)Examples

Retrieve all order risks for an order

Path parameters

order_id=450789469

string**string**

required**required**

Was this section helpful?

YesNo

get

## /admin/api/2026-01/orders/450789469/risks.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469/risks.json" \

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

HTTP/1.1 200 OK

{

"risks": [

{

"id": 284138680,

"order_id": 450789469,

"checkout_id": null,

"source": "External",

"score": "1.0",

"recommendation": "cancel",

"display": true,

"cause_cancel": true,

"message": "This order was placed from a proxy IP",

"merchant_message": "This order was placed from a proxy IP"

},

{

"id": 1029151491,

"order_id": 450789469,

"checkout_id": 901414060,

"source": "External",

"score": "1.0",

"recommendation": "cancel",

"display": true,

"cause_cancel": true,

"message": "This order came from an anonymous proxy",

"merchant_message": "This order came from an anonymous proxy"

}

]

}

### examples

  * #### Retrieve all order risks for an order

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469/risks.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.OrderRisk.all({
          session: session,
          order_id: 450789469,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::OrderRisk.all(
          session: test_session,
          order_id: 450789469,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.OrderRisk.all({
          session: session,
          order_id: 450789469,
        });

#### response

        HTTP/1.1 200 OK{"risks":[{"id":284138680,"order_id":450789469,"checkout_id":null,"source":"External","score":"1.0","recommendation":"cancel","display":true,"cause_cancel":true,"message":"This order was placed from a proxy IP","merchant_message":"This order was placed from a proxy IP"},{"id":1029151491,"order_id":450789469,"checkout_id":901414060,"source":"External","score":"1.0","recommendation":"cancel","display":true,"cause_cancel":true,"message":"This order came from an anonymous proxy","merchant_message":"This order came from an anonymous proxy"}]}


* * *

##

[Anchor to GET request, Retrieves a single order risk by its ID](/docs/api/admin-rest/latest/resources/order-risk#get-orders-order-id-risks-risk-id)

get

Retrieves a single order risk by its ID

deprecated**deprecated**

Retrieves a single order risk by its ID

###

[Anchor to Parameters of Retrieves a single order risk by its ID](/docs/api/admin-rest/latest/resources/order-risk#get-orders-order-id-risks-risk-id-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

order_id

string**string**

required**required**

* * *

risk_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to get-orders-order-id-risks-risk-id-examples](/docs/api/admin-rest/latest/resources/order-risk#get-orders-order-id-risks-risk-id-examples)Examples

Retrieve a single order risk

Was this section helpful?

YesNo

get

## /admin/api/2026-01/orders/450789469/risks/284138680.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469/risks/284138680.json" \

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

HTTP/1.1 200 OK

{

"risk": {

"id": 284138680,

"order_id": 450789469,

"checkout_id": null,

"source": "External",

"score": "1.0",

"recommendation": "cancel",

"display": true,

"cause_cancel": true,

"message": "This order was placed from a proxy IP",

"merchant_message": "This order was placed from a proxy IP"

}

}

### examples

  * #### Retrieve a single order risk

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469/risks/284138680.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.OrderRisk.find({
          session: session,
          order_id: 450789469,
          id: 284138680,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::OrderRisk.find(
          session: test_session,
          order_id: 450789469,
          id: 284138680,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.OrderRisk.find({
          session: session,
          order_id: 450789469,
          id: 284138680,
        });

#### response

        HTTP/1.1 200 OK{"risk":{"id":284138680,"order_id":450789469,"checkout_id":null,"source":"External","score":"1.0","recommendation":"cancel","display":true,"cause_cancel":true,"message":"This order was placed from a proxy IP","merchant_message":"This order was placed from a proxy IP"}}


* * *

##

[Anchor to PUT request, Updates an order risk](/docs/api/admin-rest/latest/resources/order-risk#put-orders-order-id-risks-risk-id)

put

Updates an order risk

deprecated**deprecated**

Updates an order risk




Note

You cannot modify an order risk that was created by another application.

**Note:**

You cannot modify an order risk that was created by another application.

###

[Anchor to Parameters of Updates an order risk](/docs/api/admin-rest/latest/resources/order-risk#put-orders-order-id-risks-risk-id-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

order_id

string**string**

required**required**

* * *

risk_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to put-orders-order-id-risks-risk-id-examples](/docs/api/admin-rest/latest/resources/order-risk#put-orders-order-id-risks-risk-id-examples)Examples

Update an existing order risk for an order

Was this section helpful?

YesNo

put

## /admin/api/2026-01/orders/450789469/risks/284138680.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{"risk":{"id":284138680,"message":"After further review, this is a legitimate order","recommendation":"accept","source":"External","cause_cancel":false,"score":"0.0"}}' \

-X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469/risks/284138680.json" \

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

HTTP/1.1 200 OK

{

"risk": {

"order_id": 450789469,

"cause_cancel": false,

"message": "After further review, this is a legitimate order",

"recommendation": "accept",

"score": "0.0",

"source": "External",

"id": 284138680,

"checkout_id": null,

"display": true,

"merchant_message": "After further review, this is a legitimate order"

}

}

### examples

  * #### Update an existing order risk for an order

#####

        curl -d '{"risk":{"id":284138680,"message":"After further review, this is a legitimate order","recommendation":"accept","source":"External","cause_cancel":false,"score":"0.0"}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469/risks/284138680.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const order_risk = new admin.rest.resources.OrderRisk({session: session});

        order_risk.order_id = 450789469;
        order_risk.id = 284138680;
        order_risk.message = "After further review, this is a legitimate order";
        order_risk.recommendation = "accept";
        order_risk.source = "External";
        order_risk.cause_cancel = false;
        order_risk.score = "0.0";
        await order_risk.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        order_risk = ShopifyAPI::OrderRisk.new(session: test_session)
        order_risk.order_id = 450789469
        order_risk.id = 284138680
        order_risk.message = "After further review, this is a legitimate order"
        order_risk.recommendation = "accept"
        order_risk.source = "External"
        order_risk.cause_cancel = false
        order_risk.score = "0.0"
        order_risk.save!

#####

        // Session is built by the OAuth process

        const order_risk = new shopify.rest.OrderRisk({session: session});
        order_risk.order_id = 450789469;
        order_risk.id = 284138680;
        order_risk.message = "After further review, this is a legitimate order";
        order_risk.recommendation = "accept";
        order_risk.source = "External";
        order_risk.cause_cancel = false;
        order_risk.score = "0.0";
        await order_risk.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"risk":{"order_id":450789469,"cause_cancel":false,"message":"After further review, this is a legitimate order","recommendation":"accept","score":"0.0","source":"External","id":284138680,"checkout_id":null,"display":true,"merchant_message":"After further review, this is a legitimate order"}}


* * *

##

[Anchor to DELETE request, Deletes an order risk for an order](/docs/api/admin-rest/latest/resources/order-risk#delete-orders-order-id-risks-risk-id)

del

Deletes an order risk for an order

deprecated**deprecated**

Deletes an order risk for an order




Note

You cannot delete an order risk that was created by another application.

**Note:**

You cannot delete an order risk that was created by another application.

###

[Anchor to Parameters of Deletes an order risk for an order](/docs/api/admin-rest/latest/resources/order-risk#delete-orders-order-id-risks-risk-id-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

order_id

string**string**

required**required**

* * *

risk_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to delete-orders-order-id-risks-risk-id-examples](/docs/api/admin-rest/latest/resources/order-risk#delete-orders-order-id-risks-risk-id-examples)Examples

Delete an order risk for an order

Was this section helpful?

YesNo

del

## /admin/api/2026-01/orders/450789469/risks/284138680.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X DELETE "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469/risks/284138680.json" \

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

  * #### Delete an order risk for an order

#####

        curl -X DELETE "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469/risks/284138680.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.OrderRisk.delete({
          session: session,
          order_id: 450789469,
          id: 284138680,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::OrderRisk.delete(
          session: test_session,
          order_id: 450789469,
          id: 284138680,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.OrderRisk.delete({
          session: session,
          order_id: 450789469,
          id: 284138680,
        });

#### response

        HTTP/1.1 200 OK{}