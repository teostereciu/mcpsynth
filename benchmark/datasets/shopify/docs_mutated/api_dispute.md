# Dispute

*Source: https://shopify.dev/docs/api/admin-rest/2026-01/resources/dispute*

---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04

2026-01latest

# Dispute

Ask assistant

Requires ANY of the following access scopes: `shopify_payments_payouts`, `shopify_payments`.

**Requires ANY of the following access scopes: `shopify_payments_payouts`, `shopify_payments`.:**

Disputes occur when a buyer questions the legitimacy of a charge with their financial institution.

Was this section helpful?

YesNo

#

## Endpoints

  * [get/admin/api/latest/shopify_payments/disputes.json?initiated_at=2013-05-03](/docs/api/admin-rest/latest/resources/dispute#get-shopify-payments-disputes?initiated-at=2013-05-03)

Return a list of all disputes

[shopifyPaymentsAccount](/docs/api/admin-graphql/latest/queries/shopifyPaymentsAccount?example=return-a-list-of-all-disputes)

  * [get/admin/api/latest/shopify_payments/disputes/{dispute_id}.json](/docs/api/admin-rest/latest/resources/dispute#get-shopify-payments-disputes-dispute-id)

Return a single dispute

[dispute](/docs/api/admin-graphql/latest/queries/dispute?example=return-a-single-dispute)


* * *

[Anchor to ](/docs/api/admin-rest/latest/resources/dispute#resource-object)

## The Dispute resource

[Anchor to ](/docs/api/admin-rest/latest/resources/dispute#resource-object-properties)

### Properties

* * *

id

->[id](/docs/api/admin-graphql/latest/objects/ShopifyPaymentsDispute#field-ShopifyPaymentsDispute.fields.id)

The ID of the dispute.

* * *

order_id

->[id](/docs/api/admin-graphql/latest/objects/Order#field-Order.fields.id)

The ID of the order that the dispute belongs to.

* * *

type

->[type](/docs/api/admin-graphql/latest/objects/ShopifyPaymentsDispute#field-ShopifyPaymentsDispute.fields.type)

Whether the dispute is still in the inquiry phase or has turned into a chargeback. Valid values:

Show type properties

  * **inquiry** : The dispute is in the inquiry phase.
  * **chargeback** : The dispute has turned into a chargeback.


* * *

currency

->[currencyCode](/docs/api/admin-graphql/latest/objects/MoneyV2#field-MoneyV2.fields.currencyCode)

The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code of the dispute amount.

* * *

amount

->[amount](/docs/api/admin-graphql/latest/objects/MoneyV2#field-MoneyV2.fields.amount)

The total amount disputed by the cardholder.

* * *

reason

->[reason](/docs/api/admin-graphql/latest/objects/ShopifyPaymentsDisputeReasonDetails#field-ShopifyPaymentsDisputeReasonDetails.fields.reason)

The reason of the dispute provided by the cardholder's bank. Valid values:

Show reason properties

  * **bank_not_process** : The customer's bank cannot process the charge.
  * **credit_not_processed** : The customer claims that the purchased product was returned or the transaction was otherwise canceled, but the merchant have not yet provided a refund or credit.
  * **customer_initiated** : The customer initiated the dispute, so the merchant should contact the customer for additional details to find out why the payment was disputed.
  * **debit_not_authorized** : The customer's bank cannot proceed with the debit since it has not been authorized.
  * **duplicate** : The customer claims they were charged multiple times for the same product or service.
  * **fraudulent** : The cardholder claims that they didn't authorize the payment.
  * **general** : The dispute is uncategorized, so the merchant should contact the customer for additional details to find out why the payment was disputed.
  * **incorrect_account_details** : The customer account associated with the purchase is incorrect.
  * **insufficient_funds** : The customer's bank account has insufficient funds.
  * **product_not_received** : The customer claims they did not receive the products or services purchased.
  * **product_unacceptable** : The product or service was received but was defective, damaged, or not as described.
  * **subscription_canceled** : The customer claims that the merchant continued to charge them after a subscription was canceled.
  * **unrecognized** : The customer doesn't recognize the payment appearing on their card statement.


* * *

network_reason_code

string**string**

->[networkReasonCode](/docs/api/admin-graphql/latest/objects/ShopifyPaymentsDisputeReasonDetails#field-ShopifyPaymentsDisputeReasonDetails.fields.networkReasonCode)

The reason for the dispute provided by the cardholder's bank.

* * *

status

->[status](/docs/api/admin-graphql/latest/objects/ShopifyPaymentsDispute#field-ShopifyPaymentsDispute.fields.status)

The current state of the dispute. Valid values:

Show status properties

  * **needs_response** : The dispute has been open and needs an evidence submission.
  * **under_review** : The evidence has been submitted and is being reviewed by the cardholder's bank.
  * **charge_refunded** : The merchant refunded the inquiry amount.
  * **accepted** : The merchant has accepted the dispute as being valid.
  * **won** : The cardholder's bank reached a final decision in the merchant's favor.
  * **lost** : The cardholder's bank reached a final decision in the buyer's favor.


* * *

evidence_due_by

->[evidenceDueBy](/docs/api/admin-graphql/latest/objects/ShopifyPaymentsDispute#field-ShopifyPaymentsDispute.fields.evidenceDueBy)

The deadline for evidence submission.

* * *

evidence_sent_on

->[evidenceSentOn](/docs/api/admin-graphql/latest/objects/ShopifyPaymentsDispute#field-ShopifyPaymentsDispute.fields.evidenceSentOn)

"The date and time ([ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format) when evidence was sent. Returns `null` if evidence has not yet been sent.

* * *

finalized_on

->[finalizedOn](/docs/api/admin-graphql/latest/objects/ShopifyPaymentsDispute#field-ShopifyPaymentsDispute.fields.finalizedOn)

The date and time ([ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format) when this dispute was resolved. Returns `null` if the dispute is not yet resolved.

* * *

Was this section helpful?

YesNo

{}

## The Dispute resource

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

"id": 54534554564,

"order_id": 450789469,

"type": "inquiry",

"currency": "USD",

"amount": "102.53",

"reason": "fraudulent",

"network_reason_code": "4840",

"status": "under_review",

"evidence_due_by": "2018-01-10T11:00:00-05:00",

"evidence_sent_on": "2018-01-09T11:00:00-05:00",

"finalized_on": "2018-03-10T11:00:00-05:00"

}

* * *

##

[Anchor to GET request, Return a list of all disputes](/docs/api/admin-rest/latest/resources/dispute#get-shopify-payments-disputes?initiated-at=2013-05-03)

get

Return a list of all disputes

[shopifyPaymentsAccount](/docs/api/admin-graphql/latest/queries/shopifyPaymentsAccount?example=return-a-list-of-all-disputes)

Retrieve all disputes ordered by `initiated_at` date and time ([ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format), with the most recent being first. **Note:** This endpoint implements pagination by using links that are provided in the response header. To learn more, refer to [Make paginated requests to the REST Admin API](/api/usage/pagination-rest).

###

[Anchor to Parameters of Return a list of all disputes](/docs/api/admin-rest/latest/resources/dispute#get-shopify-payments-disputes?initiated-at=2013-05-03-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

initiated_at

Return only disputes with the specified `initiated_at` date ([ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format).

* * *

last_id

Return only disputes before the specified ID.

* * *

after_id

Return only disputes after the specified ID.

* * *

status

Return only disputes with the specified status.

* * *

Was this section helpful?

YesNo

###

[Anchor to get-shopify-payments-disputes?initiated-at=2013-05-03-examples](/docs/api/admin-rest/latest/resources/dispute#get-shopify-payments-disputes?initiated-at=2013-05-03-examples)Examples

Retrieve all disputes initiated on 2013-05-03

Query parameters

initiated_at=2013-05-03

Return only disputes with the specified `initiated_at` date ([ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format).

Retrieve all disputes ordered newest to oldest

Retrieve all won disputes

Query parameters

status=won

Return only disputes with the specified status.

Was this section helpful?

YesNo

get

## /admin/api/2026-01/shopify_payments/disputes.json?initiated_at=2013-05-03

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/shopify_payments/disputes.json?initiated_at=2013-05-03" \

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

HTTP/1.1 200 OK

{

"disputes": [

{

"id": 1052608616,

"order_id": null,

"type": "chargeback",

"amount": "100.00",

"currency": "USD",

"reason": "fraudulent",

"network_reason_code": "4827",

"status": "won",

"evidence_due_by": "2013-07-03T19:00:00-04:00",

"evidence_sent_on": "2013-07-04T07:00:00-04:00",

"finalized_on": null,

"initiated_at": "2013-05-03T20:00:00-04:00"

},

{

"id": 815713555,

"order_id": 625362839,

"type": "chargeback",

"amount": "11.50",

"currency": "USD",

"reason": "credit_not_processed",

"network_reason_code": "4827",

"status": "needs_response",

"evidence_due_by": "2099-12-29T19:00:00-05:00",

"evidence_sent_on": null,

"finalized_on": null,

"initiated_at": "2013-05-03T20:00:00-04:00"

},

{

"id": 782360659,

"order_id": 625362839,

"type": "chargeback",

"amount": "11.50",

### examples

  * #### Retrieve all disputes initiated on 2013-05-03

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/shopify_payments/disputes.json?initiated_at=2013-05-03" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Dispute.all({
          session: session,
          initiated_at: "2013-05-03",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Dispute.all(
          session: test_session,
          initiated_at: "2013-05-03",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Dispute.all({
          session: session,
          initiated_at: "2013-05-03",
        });

#### response

        HTTP/1.1 200 OK{"disputes":[{"id":1052608616,"order_id":null,"type":"chargeback","amount":"100.00","currency":"USD","reason":"fraudulent","network_reason_code":"4827","status":"won","evidence_due_by":"2013-07-03T19:00:00-04:00","evidence_sent_on":"2013-07-04T07:00:00-04:00","finalized_on":null,"initiated_at":"2013-05-03T20:00:00-04:00"},{"id":815713555,"order_id":625362839,"type":"chargeback","amount":"11.50","currency":"USD","reason":"credit_not_processed","network_reason_code":"4827","status":"needs_response","evidence_due_by":"2099-12-29T19:00:00-05:00","evidence_sent_on":null,"finalized_on":null,"initiated_at":"2013-05-03T20:00:00-04:00"},{"id":782360659,"order_id":625362839,"type":"chargeback","amount":"11.50","currency":"USD","reason":"fraudulent","network_reason_code":"4827","status":"won","evidence_due_by":"2013-07-03T19:00:00-04:00","evidence_sent_on":"2013-07-04T07:00:00-04:00","finalized_on":null,"initiated_at":"2013-05-03T20:00:00-04:00"},{"id":670893524,"order_id":625362839,"type":"inquiry","amount":"11.50","currency":"USD","reason":"fraudulent","network_reason_code":"4827","status":"needs_response","evidence_due_by":null,"evidence_sent_on":null,"finalized_on":null,"initiated_at":"2013-05-03T20:00:00-04:00"},{"id":598735659,"order_id":625362839,"type":"chargeback","amount":"11.50","currency":"USD","reason":"fraudulent","network_reason_code":"4827","status":"needs_response","evidence_due_by":"2099-12-29T19:00:00-05:00","evidence_sent_on":null,"finalized_on":null,"initiated_at":"2013-05-03T20:00:00-04:00"},{"id":428123260,"order_id":625362839,"type":"chargeback","amount":"11.50","currency":"USD","reason":"debit_not_authorized","network_reason_code":"R10","status":"lost","evidence_due_by":"2099-12-29T19:00:00-05:00","evidence_sent_on":null,"finalized_on":null,"initiated_at":"2013-05-03T20:00:00-04:00"},{"id":297752803,"order_id":625362839,"type":"chargeback","amount":"100.00","currency":"USD","reason":"fraudulent","network_reason_code":"4827","status":"lost","evidence_due_by":"2099-12-29T19:00:00-05:00","evidence_sent_on":null,"finalized_on":null,"initiated_at":"2013-05-03T20:00:00-04:00"},{"id":257169523,"order_id":625362839,"type":"chargeback","amount":"11.50","currency":"USD","reason":"fraudulent","network_reason_code":"4827","status":"needs_response","evidence_due_by":"2099-12-29T19:00:00-05:00","evidence_sent_on":null,"finalized_on":null,"initiated_at":"2013-05-03T20:00:00-04:00"},{"id":172886728,"order_id":625362839,"type":"chargeback","amount":"11.50","currency":"USD","reason":"insufficient_funds","network_reason_code":"R07","status":"lost","evidence_due_by":"2099-12-29T19:00:00-05:00","evidence_sent_on":null,"finalized_on":null,"initiated_at":"2013-05-03T20:00:00-04:00"},{"id":85190714,"order_id":625362839,"type":"chargeback","amount":"11.50","currency":"USD","reason":"fraudulent","network_reason_code":"4827","status":"under_review","evidence_due_by":"2099-12-29T19:00:00-05:00","evidence_sent_on":"2099-12-30T19:00:00-05:00","finalized_on":null,"initiated_at":"2013-05-03T20:00:00-04:00"},{"id":51858708,"order_id":1039068725,"type":"inquiry","amount":"17.50","currency":"EUR","reason":"fraudulent","network_reason_code":"4827","status":"needs_response","evidence_due_by":null,"evidence_sent_on":null,"finalized_on":null,"initiated_at":"2013-05-03T20:00:00-04:00"},{"id":46484353,"order_id":625362839,"type":"chargeback","amount":"100.00","currency":"USD","reason":"fraudulent","network_reason_code":"4827","status":"lost","evidence_due_by":"2099-12-29T19:00:00-05:00","evidence_sent_on":null,"finalized_on":null,"initiated_at":"2013-05-03T20:00:00-04:00"},{"id":35982383,"order_id":625362839,"type":"chargeback","amount":"11.50","currency":"USD","reason":"subscription_canceled","network_reason_code":"4827","status":"needs_response","evidence_due_by":"2099-12-29T19:00:00-05:00","evidence_sent_on":null,"finalized_on":null,"initiated_at":"2013-05-03T20:00:00-04:00"}]}

  * #### Retrieve all disputes ordered newest to oldest

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/shopify_payments/disputes.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Dispute.all({
          session: session,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Dispute.all(
          session: test_session,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Dispute.all({
          session: session,
        });

#### response

        HTTP/1.1 200 OK{"disputes":[{"id":1052608616,"order_id":null,"type":"chargeback","amount":"100.00","currency":"USD","reason":"fraudulent","network_reason_code":"4827","status":"won","evidence_due_by":"2013-07-03T19:00:00-04:00","evidence_sent_on":"2013-07-04T07:00:00-04:00","finalized_on":null,"initiated_at":"2013-05-03T20:00:00-04:00"},{"id":815713555,"order_id":625362839,"type":"chargeback","amount":"11.50","currency":"USD","reason":"credit_not_processed","network_reason_code":"4827","status":"needs_response","evidence_due_by":"2099-12-29T19:00:00-05:00","evidence_sent_on":null,"finalized_on":null,"initiated_at":"2013-05-03T20:00:00-04:00"},{"id":782360659,"order_id":625362839,"type":"chargeback","amount":"11.50","currency":"USD","reason":"fraudulent","network_reason_code":"4827","status":"won","evidence_due_by":"2013-07-03T19:00:00-04:00","evidence_sent_on":"2013-07-04T07:00:00-04:00","finalized_on":null,"initiated_at":"2013-05-03T20:00:00-04:00"},{"id":670893524,"order_id":625362839,"type":"inquiry","amount":"11.50","currency":"USD","reason":"fraudulent","network_reason_code":"4827","status":"needs_response","evidence_due_by":null,"evidence_sent_on":null,"finalized_on":null,"initiated_at":"2013-05-03T20:00:00-04:00"},{"id":598735659,"order_id":625362839,"type":"chargeback","amount":"11.50","currency":"USD","reason":"fraudulent","network_reason_code":"4827","status":"needs_response","evidence_due_by":"2099-12-29T19:00:00-05:00","evidence_sent_on":null,"finalized_on":null,"initiated_at":"2013-05-03T20:00:00-04:00"},{"id":428123260,"order_id":625362839,"type":"chargeback","amount":"11.50","currency":"USD","reason":"debit_not_authorized","network_reason_code":"R10","status":"lost","evidence_due_by":"2099-12-29T19:00:00-05:00","evidence_sent_on":null,"finalized_on":null,"initiated_at":"2013-05-03T20:00:00-04:00"},{"id":297752803,"order_id":625362839,"type":"chargeback","amount":"100.00","currency":"USD","reason":"fraudulent","network_reason_code":"4827","status":"lost","evidence_due_by":"2099-12-29T19:00:00-05:00","evidence_sent_on":null,"finalized_on":null,"initiated_at":"2013-05-03T20:00:00-04:00"},{"id":257169523,"order_id":625362839,"type":"chargeback","amount":"11.50","currency":"USD","reason":"fraudulent","network_reason_code":"4827","status":"needs_response","evidence_due_by":"2099-12-29T19:00:00-05:00","evidence_sent_on":null,"finalized_on":null,"initiated_at":"2013-05-03T20:00:00-04:00"},{"id":172886728,"order_id":625362839,"type":"chargeback","amount":"11.50","currency":"USD","reason":"insufficient_funds","network_reason_code":"R07","status":"lost","evidence_due_by":"2099-12-29T19:00:00-05:00","evidence_sent_on":null,"finalized_on":null,"initiated_at":"2013-05-03T20:00:00-04:00"},{"id":85190714,"order_id":625362839,"type":"chargeback","amount":"11.50","currency":"USD","reason":"fraudulent","network_reason_code":"4827","status":"under_review","evidence_due_by":"2099-12-29T19:00:00-05:00","evidence_sent_on":"2099-12-30T19:00:00-05:00","finalized_on":null,"initiated_at":"2013-05-03T20:00:00-04:00"},{"id":51858708,"order_id":1039068725,"type":"inquiry","amount":"17.50","currency":"EUR","reason":"fraudulent","network_reason_code":"4827","status":"needs_response","evidence_due_by":null,"evidence_sent_on":null,"finalized_on":null,"initiated_at":"2013-05-03T20:00:00-04:00"},{"id":46484353,"order_id":625362839,"type":"chargeback","amount":"100.00","currency":"USD","reason":"fraudulent","network_reason_code":"4827","status":"lost","evidence_due_by":"2099-12-29T19:00:00-05:00","evidence_sent_on":null,"finalized_on":null,"initiated_at":"2013-05-03T20:00:00-04:00"},{"id":35982383,"order_id":625362839,"type":"chargeback","amount":"11.50","currency":"USD","reason":"subscription_canceled","network_reason_code":"4827","status":"needs_response","evidence_due_by":"2099-12-29T19:00:00-05:00","evidence_sent_on":null,"finalized_on":null,"initiated_at":"2013-05-03T20:00:00-04:00"}]}

  * #### Retrieve all won disputes

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/shopify_payments/disputes.json?status=won" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Dispute.all({
          session: session,
          status: "won",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Dispute.all(
          session: test_session,
          status: "won",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Dispute.all({
          session: session,
          status: "won",
        });

#### response

        HTTP/1.1 200 OK{"disputes":[{"id":1052608616,"order_id":null,"type":"chargeback","amount":"100.00","currency":"USD","reason":"fraudulent","network_reason_code":"4827","status":"won","evidence_due_by":"2013-07-03T19:00:00-04:00","evidence_sent_on":"2013-07-04T07:00:00-04:00","finalized_on":null,"initiated_at":"2013-05-03T20:00:00-04:00"},{"id":782360659,"order_id":625362839,"type":"chargeback","amount":"11.50","currency":"USD","reason":"fraudulent","network_reason_code":"4827","status":"won","evidence_due_by":"2013-07-03T19:00:00-04:00","evidence_sent_on":"2013-07-04T07:00:00-04:00","finalized_on":null,"initiated_at":"2013-05-03T20:00:00-04:00"}]}


* * *

##

[Anchor to GET request, Return a single dispute](/docs/api/admin-rest/latest/resources/dispute#get-shopify-payments-disputes-dispute-id)

get

Return a single dispute

[dispute](/docs/api/admin-graphql/latest/queries/dispute?example=return-a-single-dispute)

Retrieves a single dispute by ID.

###

[Anchor to Parameters of Return a single dispute](/docs/api/admin-rest/latest/resources/dispute#get-shopify-payments-disputes-dispute-id-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

dispute_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to get-shopify-payments-disputes-dispute-id-examples](/docs/api/admin-rest/latest/resources/dispute#get-shopify-payments-disputes-dispute-id-examples)Examples

Retrieves a single dispute by ID

Path parameters

dispute_id=598735659

string**string**

required**required**

Was this section helpful?

YesNo

get

## /admin/api/2026-01/shopify_payments/disputes/598735659.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/shopify_payments/disputes/598735659.json" \

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

HTTP/1.1 200 OK

{

"dispute": {

"id": 598735659,

"order_id": 625362839,

"type": "chargeback",

"amount": "11.50",

"currency": "USD",

"reason": "fraudulent",

"network_reason_code": "4827",

"status": "needs_response",

"evidence_due_by": "2099-12-29T19:00:00-05:00",

"evidence_sent_on": null,

"finalized_on": null,

"initiated_at": "2013-05-03T20:00:00-04:00"

}

}

### examples

  * #### Retrieves a single dispute by ID

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/shopify_payments/disputes/598735659.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Dispute.find({
          session: session,
          id: 598735659,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Dispute.find(
          session: test_session,
          id: 598735659,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Dispute.find({
          session: session,
          id: 598735659,
        });

#### response

        HTTP/1.1 200 OK{"dispute":{"id":598735659,"order_id":625362839,"type":"chargeback","amount":"11.50","currency":"USD","reason":"fraudulent","network_reason_code":"4827","status":"needs_response","evidence_due_by":"2099-12-29T19:00:00-05:00","evidence_sent_on":null,"finalized_on":null,"initiated_at":"2013-05-03T20:00:00-04:00"}}