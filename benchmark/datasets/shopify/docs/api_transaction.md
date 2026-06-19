# Transaction

*Source: https://shopify.dev/docs/api/admin-rest/2026-01/resources/transaction*

---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04

2026-01latest

# Transaction

Ask assistant

Requires ANY of the following access scopes: `orders`, `marketplace_orders`.

**Requires ANY of the following access scopes: `orders`, `marketplace_orders`.:**

Transactions are created for every order that results in an exchange of money.

There are five types of transactions:

  * **Authorization** : An amount reserved against the cardholder's funding source. Money does not change hands until the authorization is captured.
  * **Sale** : An authorization and capture performed together in a single step.
  * **Capture** : A transfer of the money that was reserved during the authorization stage.
  * **Void** : A cancellation of a pending authorization or capture.
  * **Refund** : A partial or full return of captured funds to the cardholder. A refund can happen only after a capture is processed.


Refund transactions must be created by using the [Refund resource](/docs/admin-api/rest/reference/orders/refund).

Note

An order can have more than one authorization transaction associated with it. This might happen when an order is edited or when a post-purchase upsell is added to the order. To be notified when an order is edited subscribe to the OrderEdit webhook.

If your app captures payments, you should make a `GET` request to the `/admin/api/{version}/orders/{order_id}/transactions.json` endpoint to retrieve the authorization transactions associated with an order. Then, to complete the full order payment capture, you should use the `authorization` or `parent_id` properties in separate capture `POST` requests to the same endpoint for each authorization transaction.

**Note:**

An order can have more than one authorization transaction associated with it. This might happen when an order is edited or when a post-purchase upsell is added to the order. To be notified when an order is edited subscribe to the OrderEdit webhook.

If your app captures payments, you should make a `GET` request to the `/admin/api/{version}/orders/{order_id}/transactions.json` endpoint to retrieve the authorization transactions associated with an order. Then, to complete the full order payment capture, you should use the `authorization` or `parent_id` properties in separate capture `POST` requests to the same endpoint for each authorization transaction.

Note

An order can have no more than 100 transactions associated with it.

**Note:**

An order can have no more than 100 transactions associated with it.

Was this section helpful?

YesNo

#

## Endpoints

  * [post/admin/api/latest/orders/{order_id}/transactions.json](/docs/api/admin-rest/latest/resources/transaction#post-orders-order-id-transactions)

Creates a transaction for an order

[orderCapture](/docs/api/admin-graphql/latest/mutations/orderCapture)

  * [get/admin/api/latest/orders/{order_id}/transactions.json](/docs/api/admin-rest/latest/resources/transaction#get-orders-order-id-transactions)

Retrieves a list of transactions

[order](/docs/api/admin-graphql/latest/queries/order)

  * [get/admin/api/latest/orders/{order_id}/transactions/{transaction_id}.json](/docs/api/admin-rest/latest/resources/transaction#get-orders-order-id-transactions-transaction-id)

Retrieves a specific transaction

[node](/docs/api/admin-graphql/latest/queries/node)

  * [get/admin/api/latest/orders/{order_id}/transactions/count.json](/docs/api/admin-rest/latest/resources/transaction#get-orders-order-id-transactions-count)

Retrieves a count of an order's transactions

[order](/docs/api/admin-graphql/latest/queries/order)


* * *

[Anchor to ](/docs/api/admin-rest/latest/resources/transaction#resource-object)

## The Transaction resource

[Anchor to ](/docs/api/admin-rest/latest/resources/transaction#resource-object-properties)

### Properties

* * *

amount

->[amountSet](/docs/api/admin-graphql/latest/objects/OrderTransaction#field-OrderTransaction.fields.amountSet)

The amount of money included in the transaction. If you don't provide a value for `amount`, then it defaults to the total cost of the order (even if a previous transaction has been made towards it).

* * *

amount_rounding

read-only**read-only**

->[amountSet](/docs/api/admin-graphql/latest/objects/OrderTransaction#field-OrderTransaction.fields.amountSet)

The rounding adjustment for cash payments, to be applied on the amount to get a rounded amount.

* * *

authorization

->[authorizationCode](/docs/api/admin-graphql/latest/objects/OrderTransaction#field-OrderTransaction.fields.authorizationCode)

The authorization code associated with the transaction.

* * *

authorization_expires_at

->[authorizationExpiresAt](/docs/api/admin-graphql/latest/objects/OrderTransaction#field-OrderTransaction.fields.authorizationExpiresAt)

The date and time ([ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format) when the Shopify Payments authorization expires.

* * *

created_at

read-only**read-only**

The date and time ([ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format) when the transaction was created.

* * *

currency

->[amountSet](/docs/api/admin-graphql/latest/objects/OrderTransaction#field-OrderTransaction.fields.amountSet)

The three-letter code ([ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) format) for the currency used for the payment.

* * *

device_id

read-only**read-only**

The ID for the device.

* * *

error_code

read-only**read-only**

->[errorCode](/docs/api/admin-graphql/latest/objects/OrderTransaction#field-OrderTransaction.fields.errorCode)

A standardized error code, independent of the payment provider. Valid values:

Show error_code properties

  * **incorrect_number**
  * **invalid_number**
  * **invalid_expiry_date**
  * **invalid_cvc**
  * **expired_card**
  * **incorrect_cvc**
  * **incorrect_zip**
  * **incorrect_address**
  * **card_declined**
  * **processing_error**
  * **call_issuer**
  * **pick_up_card**


* * *

extended_authorization_attributes

The attributes associated with a Shopify Payments extended authorization period. It has the following attributes:

Show extended_authorization_attributes properties

  * **standard_authorization_expires_at** : The date and time ([ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format) when the standard authorization period expires. After expiry, an extended authorization fee is applied upon capturing the payment.
  * **extended_authorization_expires_at** : The date and time ([ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format) when the extended authorization period expires. After expiry, the merchant can't capture the payment.

`extended_authorization_attributes` are available on the **Retrieve a specific transaction for an order** endpoint only if the following criteria applies:

  * The store is on a [Shopify Plus](https://www.shopify.com/plus) plan.
  * The store uses Shopify Payments.
  * The transaction being retrieved is an extended authorization, which is determined by the `capture_before` date in the charge.

If the criteria isn't met, then an empty JSON is returned for `extended_authorization_attributes`. To learn more about extended authorization periods, refer to [Payment authorization](https://help.shopify.com/en/manual/payments/payment-authorization).

* * *

gateway

->[gateway](/docs/api/admin-graphql/latest/objects/OrderTransaction#field-OrderTransaction.fields.gateway)

The name of the gateway the transaction was issued through. A list of gateways can be found on Shopify's [payment gateways page](//www.shopify.com/payment-gateways).

* * *

id

read-only**read-only**

->[id](/docs/api/admin-graphql/latest/objects/OrderTransaction#field-OrderTransaction.fields.id)

The ID for the transaction.

* * *

kind

->[kind](/docs/api/admin-graphql/latest/objects/OrderTransaction#field-OrderTransaction.fields.kind)

The transaction's type. Valid values:

Show kind properties

  * **authorization** : Money that the customer has agreed to pay. The authorization period can be between 7 and 30 days (depending on your payment service) while a store waits for a payment to be captured.
  * **capture** : A transfer of money that was reserved during the authorization of a shop.
  * **sale** : The authorization and capture of a payment performed in one single step.
  * **void** : The cancellation of a pending authorization or capture.
  * **refund** : The partial or full return of captured money to the customer.


* * *

Show 15 hidden fields

Was this section helpful?

YesNo

{}

## The Transaction resource

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

{

"amount": "10.00",

"amount_rounding": "0.02",

"authorization": "ch_1AtJu6CktlpKSclI4zjeQb2t",

"authorization_expires_at": "2021-03-13T16:09:54-04:00",

"created_at": "2012-03-13T16:09:54-04:00",

"currency": "USD",

"device_id": 1,

"error_code": "invalid_cvc",

"extended_authorization_attributes": {

"standard_authorization_expires_at": "2020-10-08T00:00:00-04:00",

"extended_authorization_expires_at": "2020-10-30T00:00:00-04:00"

},

"gateway": "shopify_payments",

"id": 999225661,

"kind": "capture",

"location_id": {

"id": 49202758

},

"message": "Marked the Stripe payment as received",

"order_id": 450789469,

"payment_details": {

"credit_card_bin": "123456",

"avs_result_code": "Y",

"cvv_result_code": "M",

"credit_card_number": "•••• •••• •••• 4242",

"credit_card_company": "Visa",

"credit_card_name": "John Smith",

"credit_card_wallet": "shopify_pay",

"credit_card_expiration_month": 10,

"credit_card_expiration_year": 2028,

"buyer_action_info": {

"multibanco": {

"Entity": "12345",

"Reference": "999999999"

}

},

"payment_method_name": "multibanco"

},

"parent_id": 584698724408,

"payments_refund_attributes": {

"status": "success",

"acquirer_reference_number": "123456789012345678901234"

},

"processed_at": "2018-01-10T11:00:00-05:00",

"receipt": {},

"source_name": "web",

"status": "success",

"total_unsettled_set": {

"presentment_money": {

"amount": "171.8",

"currency": "USD"

},

"shop_money": {

"amount": "171.8",

"currency": "USD"

}

},

"test": true,

"user_id": 106045196,

"currency_exchange_adjustment": {

"id": 1,

"adjustment": "-0.01",

"original_amount": "-53.62",

"final_amount": "-53.63",

"currency": "CAD"

},

"manual_payment_gateway": false

}

* * *

##

[Anchor to POST request, Creates a transaction for an order](/docs/api/admin-rest/latest/resources/transaction#post-orders-order-id-transactions)

post

Creates a transaction for an order

[orderCapture](/docs/api/admin-graphql/latest/mutations/orderCapture)

Caution

For multi-currency orders, the `currency` property is required when creating refund and capture transactions. The value should be the presentment currency from the order. For more information, refer to the [_Transaction resource_](/api/admin-rest/latest/resources/transaction).

**Caution:**

For multi-currency orders, the `currency` property is required when creating refund and capture transactions. The value should be the presentment currency from the order. For more information, refer to the [_Transaction resource_](/api/admin-rest/latest/resources/transaction).

Creates a transaction for an order.

###

[Anchor to Parameters of Creates a transaction for an order](/docs/api/admin-rest/latest/resources/transaction#post-orders-order-id-transactions-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

order_id

string**string**

required**required**

* * *

source

An optional origin of the transaction. Set to `external` to import a cash transaction for the associated order.

* * *

Was this section helpful?

YesNo

###

[Anchor to post-orders-order-id-transactions-examples](/docs/api/admin-rest/latest/resources/transaction#post-orders-order-id-transactions-examples)Examples

Capture a specified amount on an authorized order, and associate the capture with an authorization by including its ID

Path parameters

order_id=450789469

string**string**

required**required**

Request body

transaction

Transaction resource**Transaction resource**

Show transaction properties

transaction.currency:"USD"

->[currency](/docs/api/admin-graphql/latest/input-objects/OrderCaptureInput#fields-currency)

The three-letter code ([ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) format) for the currency used for the payment.

transaction.amount:"10.00"

->[amount](/docs/api/admin-graphql/latest/input-objects/OrderCaptureInput#fields-amount)

The amount of money included in the transaction. If you don't provide a value for `amount`, then it defaults to the total cost of the order (even if a previous transaction has been made towards it).

transaction.kind:"capture"

The transaction's type. Valid values:

Show kind properties

  * **authorization** : Money that the customer has agreed to pay. The authorization period can be between 7 and 30 days (depending on your payment service) while a store waits for a payment to be captured.
  * **capture** : A transfer of money that was reserved during the authorization of a shop.
  * **sale** : The authorization and capture of a payment performed in one single step.
  * **void** : The cancellation of a pending authorization or capture.
  * **refund** : The partial or full return of captured money to the customer.


transaction.parent_id:389404469

->[parentTransactionId](/docs/api/admin-graphql/latest/input-objects/OrderCaptureInput#fields-parentTransactionId)

The ID of an associated transaction.

Show parent_id properties

  * For `capture` transactions, the parent needs to be an `authorization` transaction.
  * For `void` transactions, the parent needs to be an `authorization` transaction.
  * For `refund` transactions, the parent needs to be a `capture` or `sale` transaction.


Capture the full amount for one authorization on an order, and associate the capture with an authorization by including its authorization code

Path parameters

order_id=450789469

string**string**

required**required**

Request body

transaction

Transaction resource**Transaction resource**

Show transaction properties

transaction.kind:"capture"

The transaction's type. Valid values:

Show kind properties

  * **authorization** : Money that the customer has agreed to pay. The authorization period can be between 7 and 30 days (depending on your payment service) while a store waits for a payment to be captured.
  * **capture** : A transfer of money that was reserved during the authorization of a shop.
  * **sale** : The authorization and capture of a payment performed in one single step.
  * **void** : The cancellation of a pending authorization or capture.
  * **refund** : The partial or full return of captured money to the customer.


transaction.authorization:"authorization-key"

The authorization code associated with the transaction.

Create a test transaction

Path parameters

order_id=450789469

string**string**

required**required**

Request body

transaction

Transaction resource**Transaction resource**

Show transaction properties

transaction.currency:"USD"

->[currency](/docs/api/admin-graphql/latest/input-objects/OrderCaptureInput#fields-currency)

The three-letter code ([ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) format) for the currency used for the payment.

transaction.amount:"10.00"

->[amount](/docs/api/admin-graphql/latest/input-objects/OrderCaptureInput#fields-amount)

The amount of money included in the transaction. If you don't provide a value for `amount`, then it defaults to the total cost of the order (even if a previous transaction has been made towards it).

transaction.kind:"capture"

The transaction's type. Valid values:

Show kind properties

  * **authorization** : Money that the customer has agreed to pay. The authorization period can be between 7 and 30 days (depending on your payment service) while a store waits for a payment to be captured.
  * **capture** : A transfer of money that was reserved during the authorization of a shop.
  * **sale** : The authorization and capture of a payment performed in one single step.
  * **void** : The cancellation of a pending authorization or capture.
  * **refund** : The partial or full return of captured money to the customer.


transaction.parent_id:389404469

->[parentTransactionId](/docs/api/admin-graphql/latest/input-objects/OrderCaptureInput#fields-parentTransactionId)

The ID of an associated transaction.

Show parent_id properties

  * For `capture` transactions, the parent needs to be an `authorization` transaction.
  * For `void` transactions, the parent needs to be an `authorization` transaction.
  * For `refund` transactions, the parent needs to be a `capture` or `sale` transaction.


transaction.test:true

Whether the transaction is a test transaction.

Void a transaction

Path parameters

order_id=450789469

string**string**

required**required**

Request body

transaction

Transaction resource**Transaction resource**

Show transaction properties

transaction.currency:"USD"

->[currency](/docs/api/admin-graphql/latest/input-objects/OrderCaptureInput#fields-currency)

The three-letter code ([ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) format) for the currency used for the payment.

transaction.amount:"10.00"

->[amount](/docs/api/admin-graphql/latest/input-objects/OrderCaptureInput#fields-amount)

The amount of money included in the transaction. If you don't provide a value for `amount`, then it defaults to the total cost of the order (even if a previous transaction has been made towards it).

transaction.kind:"void"

The transaction's type. Valid values:

Show kind properties

  * **authorization** : Money that the customer has agreed to pay. The authorization period can be between 7 and 30 days (depending on your payment service) while a store waits for a payment to be captured.
  * **capture** : A transfer of money that was reserved during the authorization of a shop.
  * **sale** : The authorization and capture of a payment performed in one single step.
  * **void** : The cancellation of a pending authorization or capture.
  * **refund** : The partial or full return of captured money to the customer.


transaction.parent_id:389404469

->[parentTransactionId](/docs/api/admin-graphql/latest/input-objects/OrderCaptureInput#fields-parentTransactionId)

The ID of an associated transaction.

Show parent_id properties

  * For `capture` transactions, the parent needs to be an `authorization` transaction.
  * For `void` transactions, the parent needs to be an `authorization` transaction.
  * For `refund` transactions, the parent needs to be a `capture` or `sale` transaction.


Was this section helpful?

YesNo

post

## /admin/api/2026-01/orders/450789469/transactions.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{"transaction":{"currency":"USD","amount":"10.00","kind":"capture","parent_id":389404469}}' \

-X POST "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469/transactions.json" \

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

HTTP/1.1 201 Created

{

"transaction": {

"id": 1068278565,

"order_id": 450789469,

"kind": "capture",

"gateway": "bogus",

"status": "success",

"message": "Bogus Gateway: Forced success",

"created_at": "2026-01-09T17:34:39-05:00",

"test": true,

"authorization": null,

"location_id": null,

"user_id": null,

"parent_id": 389404469,

"processed_at": "2026-01-09T17:34:39-05:00",

"device_id": null,

"error_code": null,

"source_name": "755357713",

"payment_details": {

"credit_card_bin": null,

"avs_result_code": null,

"cvv_result_code": null,

"credit_card_number": "•••• •••• •••• 4242",

"credit_card_company": "Visa",

"buyer_action_info": null,

"credit_card_name": null,

"credit_card_wallet": null,

"credit_card_expiration_month": null,

"credit_card_expiration_year": null,

"payment_method_name": "visa"

},

"receipt": {},

"currency_exchange_adjustment": null,

"amount": "10.00",

"currency": "USD",

"payment_id": "c901414060.1",

"total_unsettled_set": {

"presentment_money": {

"amount": "588.94",

"currency": "USD"

},

"shop_money": {

"amount": "588.94",

"currency": "USD"

}

},

"manual_payment_gateway": false,

"amount_rounding": null,

"admin_graphql_api_id": "gid://shopify/OrderTransaction/1068278565"

}

}

### examples

  * #### Capture a specified amount on an authorized order, and associate the capture with an authorization by including its ID

#####

        curl -d '{"transaction":{"currency":"USD","amount":"10.00","kind":"capture","parent_id":389404469}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469/transactions.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const transaction = new admin.rest.resources.Transaction({session: session});

        transaction.order_id = 450789469;
        transaction.currency = "USD";
        transaction.amount = "10.00";
        transaction.kind = "capture";
        transaction.parent_id = 389404469;
        await transaction.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        transaction = ShopifyAPI::Transaction.new(session: test_session)
        transaction.order_id = 450789469
        transaction.currency = "USD"
        transaction.amount = "10.00"
        transaction.kind = "capture"
        transaction.parent_id = 389404469
        transaction.save!

#####

        // Session is built by the OAuth process

        const transaction = new shopify.rest.Transaction({session: session});
        transaction.order_id = 450789469;
        transaction.currency = "USD";
        transaction.amount = "10.00";
        transaction.kind = "capture";
        transaction.parent_id = 389404469;
        await transaction.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"transaction":{"id":1068278565,"order_id":450789469,"kind":"capture","gateway":"bogus","status":"success","message":"Bogus Gateway: Forced success","created_at":"2026-01-09T17:34:39-05:00","test":true,"authorization":null,"location_id":null,"user_id":null,"parent_id":389404469,"processed_at":"2026-01-09T17:34:39-05:00","device_id":null,"error_code":null,"source_name":"755357713","payment_details":{"credit_card_bin":null,"avs_result_code":null,"cvv_result_code":null,"credit_card_number":"•••• •••• •••• 4242","credit_card_company":"Visa","buyer_action_info":null,"credit_card_name":null,"credit_card_wallet":null,"credit_card_expiration_month":null,"credit_card_expiration_year":null,"payment_method_name":"visa"},"receipt":{},"currency_exchange_adjustment":null,"amount":"10.00","currency":"USD","payment_id":"c901414060.1","total_unsettled_set":{"presentment_money":{"amount":"588.94","currency":"USD"},"shop_money":{"amount":"588.94","currency":"USD"}},"manual_payment_gateway":false,"amount_rounding":null,"admin_graphql_api_id":"gid://shopify/OrderTransaction/1068278565"}}

  * #### Capture the full amount for one authorization on an order, and associate the capture with an authorization by including its authorization code

#####

        curl -d '{"transaction":{"kind":"capture","authorization":"authorization-key"}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469/transactions.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const transaction = new admin.rest.resources.Transaction({session: session});

        transaction.order_id = 450789469;
        transaction.kind = "capture";
        transaction.authorization = "authorization-key";
        await transaction.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        transaction = ShopifyAPI::Transaction.new(session: test_session)
        transaction.order_id = 450789469
        transaction.kind = "capture"
        transaction.authorization = "authorization-key"
        transaction.save!

#####

        // Session is built by the OAuth process

        const transaction = new shopify.rest.Transaction({session: session});
        transaction.order_id = 450789469;
        transaction.kind = "capture";
        transaction.authorization = "authorization-key";
        await transaction.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"transaction":{"id":1068278569,"order_id":450789469,"kind":"capture","gateway":"bogus","status":"success","message":"Bogus Gateway: Forced success","created_at":"2026-01-09T17:34:46-05:00","test":true,"authorization":null,"location_id":null,"user_id":null,"parent_id":389404469,"processed_at":"2026-01-09T17:34:46-05:00","device_id":null,"error_code":null,"source_name":"755357713","payment_details":{"credit_card_bin":null,"avs_result_code":null,"cvv_result_code":null,"credit_card_number":"•••• •••• •••• 4242","credit_card_company":"Visa","buyer_action_info":null,"credit_card_name":null,"credit_card_wallet":null,"credit_card_expiration_month":null,"credit_card_expiration_year":null,"payment_method_name":"visa"},"receipt":{},"currency_exchange_adjustment":null,"amount":"598.94","currency":"USD","payment_id":"c901414060.1","total_unsettled_set":{"presentment_money":{"amount":"0.0","currency":"USD"},"shop_money":{"amount":"0.0","currency":"USD"}},"manual_payment_gateway":false,"amount_rounding":null,"admin_graphql_api_id":"gid://shopify/OrderTransaction/1068278569"}}

  * #### Create a test transaction

#####

        curl -d '{"transaction":{"currency":"USD","amount":"10.00","kind":"capture","parent_id":389404469,"test":true}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469/transactions.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const transaction = new admin.rest.resources.Transaction({session: session});

        transaction.order_id = 450789469;
        transaction.currency = "USD";
        transaction.amount = "10.00";
        transaction.kind = "capture";
        transaction.parent_id = 389404469;
        transaction.test = true;
        await transaction.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        transaction = ShopifyAPI::Transaction.new(session: test_session)
        transaction.order_id = 450789469
        transaction.currency = "USD"
        transaction.amount = "10.00"
        transaction.kind = "capture"
        transaction.parent_id = 389404469
        transaction.test = true
        transaction.save!

#####

        // Session is built by the OAuth process

        const transaction = new shopify.rest.Transaction({session: session});
        transaction.order_id = 450789469;
        transaction.currency = "USD";
        transaction.amount = "10.00";
        transaction.kind = "capture";
        transaction.parent_id = 389404469;
        transaction.test = true;
        await transaction.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"transaction":{"id":1068278562,"order_id":450789469,"kind":"capture","gateway":"bogus","status":"success","message":"Bogus Gateway: Forced success","created_at":"2026-01-09T17:34:33-05:00","test":true,"authorization":null,"location_id":null,"user_id":null,"parent_id":389404469,"processed_at":"2026-01-09T17:34:33-05:00","device_id":null,"error_code":null,"source_name":"755357713","payment_details":{"credit_card_bin":null,"avs_result_code":null,"cvv_result_code":null,"credit_card_number":"•••• •••• •••• 4242","credit_card_company":"Visa","buyer_action_info":null,"credit_card_name":null,"credit_card_wallet":null,"credit_card_expiration_month":null,"credit_card_expiration_year":null,"payment_method_name":"visa"},"receipt":{},"currency_exchange_adjustment":null,"amount":"10.00","currency":"USD","payment_id":"c901414060.1","total_unsettled_set":{"presentment_money":{"amount":"588.94","currency":"USD"},"shop_money":{"amount":"588.94","currency":"USD"}},"manual_payment_gateway":false,"amount_rounding":null,"admin_graphql_api_id":"gid://shopify/OrderTransaction/1068278562"}}

  * #### Void a transaction

#####

        curl -d '{"transaction":{"currency":"USD","amount":"10.00","kind":"void","parent_id":389404469}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469/transactions.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const transaction = new admin.rest.resources.Transaction({session: session});

        transaction.order_id = 450789469;
        transaction.currency = "USD";
        transaction.amount = "10.00";
        transaction.kind = "void";
        transaction.parent_id = 389404469;
        await transaction.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        transaction = ShopifyAPI::Transaction.new(session: test_session)
        transaction.order_id = 450789469
        transaction.currency = "USD"
        transaction.amount = "10.00"
        transaction.kind = "void"
        transaction.parent_id = 389404469
        transaction.save!

#####

        // Session is built by the OAuth process

        const transaction = new shopify.rest.Transaction({session: session});
        transaction.order_id = 450789469;
        transaction.currency = "USD";
        transaction.amount = "10.00";
        transaction.kind = "void";
        transaction.parent_id = 389404469;
        await transaction.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"transaction":{"id":1068278579,"order_id":450789469,"kind":"void","gateway":"bogus","status":"success","message":"Bogus Gateway: Forced success","created_at":"2026-01-09T17:35:02-05:00","test":true,"authorization":null,"location_id":null,"user_id":null,"parent_id":389404469,"processed_at":"2026-01-09T17:35:02-05:00","device_id":null,"error_code":null,"source_name":"755357713","payment_details":{"credit_card_bin":null,"avs_result_code":null,"cvv_result_code":null,"credit_card_number":"•••• •••• •••• 4242","credit_card_company":"Visa","buyer_action_info":null,"credit_card_name":null,"credit_card_wallet":null,"credit_card_expiration_month":null,"credit_card_expiration_year":null,"payment_method_name":"visa"},"receipt":{},"currency_exchange_adjustment":null,"amount":"0.00","currency":"USD","payment_id":"c901414060.1","total_unsettled_set":{"presentment_money":{"amount":"0.0","currency":"USD"},"shop_money":{"amount":"0.0","currency":"USD"}},"manual_payment_gateway":false,"amount_rounding":null,"admin_graphql_api_id":"gid://shopify/OrderTransaction/1068278579"}}


* * *

##

[Anchor to GET request, Retrieves a list of transactions](/docs/api/admin-rest/latest/resources/transaction#get-orders-order-id-transactions)

get

Retrieves a list of transactions

[order](/docs/api/admin-graphql/latest/queries/order)

Retrieves a list of transactions.

Transactions attached to multi-currency orders are in the presentment currency by default. To retrieve transactions in the shop currency, include the URL parameter `in_shop_currency=true`.

###

[Anchor to Parameters of Retrieves a list of transactions](/docs/api/admin-rest/latest/resources/transaction#get-orders-order-id-transactions-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

order_id

string**string**

required**required**

* * *

fields

Show only certain fields, specifed by a comma-separated list of fields names.

* * *

in_shop_currency

default false**default false**

Show amounts in the shop currency.

* * *

since_id

Retrieve only transactions after the specified ID.

* * *

Was this section helpful?

YesNo

###

[Anchor to get-orders-order-id-transactions-examples](/docs/api/admin-rest/latest/resources/transaction#get-orders-order-id-transactions-examples)Examples

Retrieve an order's transactions

Path parameters

order_id=450789469

string**string**

required**required**

Retrieve an order's transactions after a specified ID

Path parameters

order_id=450789469

string**string**

required**required**

Query parameters

since_id=801038806

Retrieve only transactions after the specified ID.

Was this section helpful?

YesNo

get

## /admin/api/2026-01/orders/450789469/transactions.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469/transactions.json" \

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

121

122

123

124

125

126

127

128

129

HTTP/1.1 200 OK

{

"transactions": [

{

"id": 179259969,

"order_id": 450789469,

"kind": "refund",

"gateway": "bogus",

"status": "success",

"message": null,

"created_at": "2005-08-05T12:59:12-04:00",

"test": false,

"authorization": "authorization-key",

"location_id": null,

"user_id": null,

"parent_id": 801038806,

"processed_at": "2005-08-05T12:59:12-04:00",

"device_id": null,

"error_code": null,

"source_name": "web",

"receipt": {},

"currency_exchange_adjustment": null,

"amount": "209.00",

"currency": "USD",

"payment_id": "#1001.3",

"total_unsettled_set": {

"presentment_money": {

"amount": "348.0",

"currency": "USD"

},

"shop_money": {

"amount": "348.0",

"currency": "USD"

}

},

"manual_payment_gateway": false,

"amount_rounding": null,

"admin_graphql_api_id": "gid://shopify/OrderTransaction/179259969"

},

{

"id": 389404469,

"order_id": 450789469,

"kind": "authorization",

"gateway": "bogus",

"status": "success",

"message": null,

"created_at": "2005-08-01T11:57:11-04:00",

"test": false,

"authorization": "authorization-key",

"location_id": null,

"user_id": null,

"parent_id": null,

"processed_at": "2005-08-01T11:57:11-04:00",

"device_id": null,

"error_code": null,

"source_name": "web",

"payment_details": {

"credit_card_bin": null,

"avs_result_code": null,

"cvv_result_code": null,

"credit_card_number": "•••• •••• •••• 4242",

"credit_card_company": "Visa",

"buyer_action_info": null,

"credit_card_name": null,

"credit_card_wallet": null,

"credit_card_expiration_month": null,

"credit_card_expiration_year": null,

"payment_method_name": "visa"

},

"receipt": {

"testcase": true,

"authorization": "123456"

},

"currency_exchange_adjustment": null,

"amount": "598.94",

"currency": "USD",

"payment_id": "#1001.1",

"total_unsettled_set": {

"presentment_money": {

"amount": "348.0",

"currency": "USD"

},

"shop_money": {

"amount": "348.0",

"currency": "USD"

}

},

"manual_payment_gateway": false,

"amount_rounding": null,

"admin_graphql_api_id": "gid://shopify/OrderTransaction/389404469"

},

{

"id": 801038806,

"order_id": 450789469,

"kind": "capture",

"gateway": "bogus",

"status": "success",

"message": null,

"created_at": "2005-08-05T10:22:51-04:00",

"test": false,

"authorization": "authorization-key",

"location_id": null,

"user_id": null,

"parent_id": 389404469,

"processed_at": "2005-08-05T10:22:51-04:00",

"device_id": null,

"error_code": null,

"source_name": "web",

"receipt": {},

"currency_exchange_adjustment": null,

"amount": "250.94",

"currency": "USD",

"payment_id": "#1001.2",

"total_unsettled_set": {

"presentment_money": {

"amount": "348.0",

"currency": "USD"

},

"shop_money": {

"amount": "348.0",

"currency": "USD"

}

},

"manual_payment_gateway": false,

"amount_rounding": null,

"admin_graphql_api_id": "gid://shopify/OrderTransaction/801038806"

}

]

}

### examples

  * #### Retrieve an order's transactions

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469/transactions.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Transaction.all({
          session: session,
          order_id: 450789469,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Transaction.all(
          session: test_session,
          order_id: 450789469,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Transaction.all({
          session: session,
          order_id: 450789469,
        });

#### response

        HTTP/1.1 200 OK{"transactions":[{"id":179259969,"order_id":450789469,"kind":"refund","gateway":"bogus","status":"success","message":null,"created_at":"2005-08-05T12:59:12-04:00","test":false,"authorization":"authorization-key","location_id":null,"user_id":null,"parent_id":801038806,"processed_at":"2005-08-05T12:59:12-04:00","device_id":null,"error_code":null,"source_name":"web","receipt":{},"currency_exchange_adjustment":null,"amount":"209.00","currency":"USD","payment_id":"#1001.3","total_unsettled_set":{"presentment_money":{"amount":"348.0","currency":"USD"},"shop_money":{"amount":"348.0","currency":"USD"}},"manual_payment_gateway":false,"amount_rounding":null,"admin_graphql_api_id":"gid://shopify/OrderTransaction/179259969"},{"id":389404469,"order_id":450789469,"kind":"authorization","gateway":"bogus","status":"success","message":null,"created_at":"2005-08-01T11:57:11-04:00","test":false,"authorization":"authorization-key","location_id":null,"user_id":null,"parent_id":null,"processed_at":"2005-08-01T11:57:11-04:00","device_id":null,"error_code":null,"source_name":"web","payment_details":{"credit_card_bin":null,"avs_result_code":null,"cvv_result_code":null,"credit_card_number":"•••• •••• •••• 4242","credit_card_company":"Visa","buyer_action_info":null,"credit_card_name":null,"credit_card_wallet":null,"credit_card_expiration_month":null,"credit_card_expiration_year":null,"payment_method_name":"visa"},"receipt":{"testcase":true,"authorization":"123456"},"currency_exchange_adjustment":null,"amount":"598.94","currency":"USD","payment_id":"#1001.1","total_unsettled_set":{"presentment_money":{"amount":"348.0","currency":"USD"},"shop_money":{"amount":"348.0","currency":"USD"}},"manual_payment_gateway":false,"amount_rounding":null,"admin_graphql_api_id":"gid://shopify/OrderTransaction/389404469"},{"id":801038806,"order_id":450789469,"kind":"capture","gateway":"bogus","status":"success","message":null,"created_at":"2005-08-05T10:22:51-04:00","test":false,"authorization":"authorization-key","location_id":null,"user_id":null,"parent_id":389404469,"processed_at":"2005-08-05T10:22:51-04:00","device_id":null,"error_code":null,"source_name":"web","receipt":{},"currency_exchange_adjustment":null,"amount":"250.94","currency":"USD","payment_id":"#1001.2","total_unsettled_set":{"presentment_money":{"amount":"348.0","currency":"USD"},"shop_money":{"amount":"348.0","currency":"USD"}},"manual_payment_gateway":false,"amount_rounding":null,"admin_graphql_api_id":"gid://shopify/OrderTransaction/801038806"}]}

  * #### Retrieve an order's transactions after a specified ID

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469/transactions.json?since_id=801038806" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Transaction.all({
          session: session,
          order_id: 450789469,
          since_id: "801038806",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Transaction.all(
          session: test_session,
          order_id: 450789469,
          since_id: "801038806",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Transaction.all({
          session: session,
          order_id: 450789469,
          since_id: "801038806",
        });

#### response

        HTTP/1.1 200 OK{"transactions":[{"id":1068278582,"order_id":450789469,"kind":"capture","gateway":"bogus","status":"success","message":"Bogus Gateway: Forced success","created_at":"2026-01-09T17:35:08-05:00","test":true,"authorization":null,"location_id":null,"user_id":null,"parent_id":389404469,"processed_at":"2026-01-09T17:35:08-05:00","device_id":null,"error_code":null,"source_name":"755357713","payment_details":{"credit_card_bin":null,"avs_result_code":null,"cvv_result_code":null,"credit_card_number":"•••• •••• •••• 4242","credit_card_company":"Visa","buyer_action_info":null,"credit_card_name":null,"credit_card_wallet":null,"credit_card_expiration_month":null,"credit_card_expiration_year":null,"payment_method_name":"visa"},"receipt":{},"currency_exchange_adjustment":null,"amount":"10.00","currency":"USD","payment_id":"c901414060.1","total_unsettled_set":{"presentment_money":{"amount":"338.0","currency":"USD"},"shop_money":{"amount":"338.0","currency":"USD"}},"manual_payment_gateway":false,"amount_rounding":null,"admin_graphql_api_id":"gid://shopify/OrderTransaction/1068278582"}]}


* * *

##

[Anchor to GET request, Retrieves a specific transaction](/docs/api/admin-rest/latest/resources/transaction#get-orders-order-id-transactions-transaction-id)

get

Retrieves a specific transaction

[node](/docs/api/admin-graphql/latest/queries/node)

Retrieves a specific transaction.

Transactions attached to multi-currency orders are in the presentment currency by default. To retrieve transactions in the shop currency, include the URL parameter `in_shop_currency=true`.

`extended_authorization_attributes` are available on this endpoint only to stores on the [Shopify Plus](https://www.shopify.com/plus) plan that use Shopify Payments. To learn more about extended authorization periods, refer to [Payment authorization](https://help.shopify.com/en/manual/payments/payment-authorization).

###

[Anchor to Parameters of Retrieves a specific transaction](/docs/api/admin-rest/latest/resources/transaction#get-orders-order-id-transactions-transaction-id-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

order_id

string**string**

required**required**

* * *

transaction_id

string**string**

required**required**

* * *

fields

Show only certain fields, specified by a comma-separated list of field names.

* * *

in_shop_currency

default false**default false**

Show amounts in the shop currency.

* * *

Was this section helpful?

YesNo

###

[Anchor to get-orders-order-id-transactions-transaction-id-examples](/docs/api/admin-rest/latest/resources/transaction#get-orders-order-id-transactions-transaction-id-examples)Examples

Retrieve a specific transaction for an order

Was this section helpful?

YesNo

get

## /admin/api/2026-01/orders/450789469/transactions/389404469.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469/transactions/389404469.json" \

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

HTTP/1.1 200 OK

{

"transaction": {

"id": 389404469,

"order_id": 450789469,

"kind": "authorization",

"gateway": "bogus",

"status": "success",

"message": null,

"created_at": "2005-08-01T11:57:11-04:00",

"test": false,

"authorization": "authorization-key",

"location_id": null,

"user_id": null,

"parent_id": null,

"processed_at": "2005-08-01T11:57:11-04:00",

"device_id": null,

"error_code": null,

"source_name": "web",

"payment_details": {

"credit_card_bin": null,

"avs_result_code": null,

"cvv_result_code": null,

"credit_card_number": "•••• •••• •••• 4242",

"credit_card_company": "Visa",

"buyer_action_info": null,

"credit_card_name": null,

"credit_card_wallet": null,

"credit_card_expiration_month": null,

"credit_card_expiration_year": null,

"payment_method_name": "visa"

},

"receipt": {

"testcase": true,

"authorization": "123456"

},

"currency_exchange_adjustment": null,

"amount": "598.94",

"currency": "USD",

"authorization_expires_at": null,

"extended_authorization_attributes": {},

"payment_id": "#1001.1",

"total_unsettled_set": {

"presentment_money": {

"amount": "348.0",

"currency": "USD"

},

"shop_money": {

"amount": "348.0",

"currency": "USD"

}

},

"manual_payment_gateway": false,

"amount_rounding": null,

"admin_graphql_api_id": "gid://shopify/OrderTransaction/389404469"

}

}

### examples

  * #### Retrieve a specific transaction for an order

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469/transactions/389404469.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Transaction.find({
          session: session,
          order_id: 450789469,
          id: 389404469,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Transaction.find(
          session: test_session,
          order_id: 450789469,
          id: 389404469,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Transaction.find({
          session: session,
          order_id: 450789469,
          id: 389404469,
        });

#### response

        HTTP/1.1 200 OK{"transaction":{"id":389404469,"order_id":450789469,"kind":"authorization","gateway":"bogus","status":"success","message":null,"created_at":"2005-08-01T11:57:11-04:00","test":false,"authorization":"authorization-key","location_id":null,"user_id":null,"parent_id":null,"processed_at":"2005-08-01T11:57:11-04:00","device_id":null,"error_code":null,"source_name":"web","payment_details":{"credit_card_bin":null,"avs_result_code":null,"cvv_result_code":null,"credit_card_number":"•••• •••• •••• 4242","credit_card_company":"Visa","buyer_action_info":null,"credit_card_name":null,"credit_card_wallet":null,"credit_card_expiration_month":null,"credit_card_expiration_year":null,"payment_method_name":"visa"},"receipt":{"testcase":true,"authorization":"123456"},"currency_exchange_adjustment":null,"amount":"598.94","currency":"USD","authorization_expires_at":null,"extended_authorization_attributes":{},"payment_id":"#1001.1","total_unsettled_set":{"presentment_money":{"amount":"348.0","currency":"USD"},"shop_money":{"amount":"348.0","currency":"USD"}},"manual_payment_gateway":false,"amount_rounding":null,"admin_graphql_api_id":"gid://shopify/OrderTransaction/389404469"}}


* * *

##

[Anchor to GET request, Retrieves a count of an order's transactions](/docs/api/admin-rest/latest/resources/transaction#get-orders-order-id-transactions-count)

get

Retrieves a count of an order's transactions

[order](/docs/api/admin-graphql/latest/queries/order)

Retrieves a count of an order's transactions.

###

[Anchor to Parameters of Retrieves a count of an order's transactions](/docs/api/admin-rest/latest/resources/transaction#get-orders-order-id-transactions-count-parameters)Parameters

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

[Anchor to get-orders-order-id-transactions-count-examples](/docs/api/admin-rest/latest/resources/transaction#get-orders-order-id-transactions-count-examples)Examples

Count an order's transactions

Path parameters

order_id=450789469

string**string**

required**required**

Was this section helpful?

YesNo

get

## /admin/api/2026-01/orders/450789469/transactions/count.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469/transactions/count.json" \

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

"count": 3

}

### examples

  * #### Count an order's transactions

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469/transactions/count.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Transaction.count({
          session: session,
          order_id: 450789469,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Transaction.count(
          session: test_session,
          order_id: 450789469,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Transaction.count({
          session: session,
          order_id: 450789469,
        });

#### response

        HTTP/1.1 200 OK{"count":3}