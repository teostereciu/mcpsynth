# Payouts

*Source: https://shopify.dev/docs/api/admin-rest/2026-01/resources/payouts*

---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04

2026-01latest

# Payouts

Ask assistant

Requires ANY of the following access scopes: `shopify_payments_payouts`, `shopify_payments`.

**Requires ANY of the following access scopes: `shopify_payments_payouts`, `shopify_payments`.:**

Payouts represent the movement of money between a Shopify Payments account balance and a connected bank account.

Was this section helpful?

YesNo

#

## Endpoints

  * [get/admin/api/latest/shopify_payments/payouts.json](/docs/api/admin-rest/latest/resources/payouts#get-shopify-payments-payouts)

Return a list of all payouts

[shopifyPaymentsAccount](/docs/api/admin-graphql/latest/queries/shopifyPaymentsAccount?example=return-a-list-of-all-payouts)

  * [get/admin/api/latest/shopify_payments/payouts/{payout_id}.json](/docs/api/admin-rest/latest/resources/payouts#get-shopify-payments-payouts-payout-id)

Return a single payout

[shopifyPaymentsAccount](/docs/api/admin-graphql/latest/queries/shopifyPaymentsAccount?example=return-a-single-payout)


* * *

[Anchor to ](/docs/api/admin-rest/latest/resources/payouts#resource-object)

## The Payouts resource

[Anchor to ](/docs/api/admin-rest/latest/resources/payouts#resource-object-properties)

### Properties

* * *

id

->[id](/docs/api/admin-graphql/latest/objects/ShopifyPaymentsPayout#field-ShopifyPaymentsPayout.fields.id)

The unique identifier of the payout

* * *

status

->[status](/docs/api/admin-graphql/latest/objects/ShopifyPaymentsPayout#field-ShopifyPaymentsPayout.fields.status)

The transfer status of the payout. The value will be one of the following:

Show status properties

  * **scheduled** : The payout has been created and had transactions assigned to it, but it has not yet been submitted to the bank.
  * **in_transit** : The payout has been submitted to the bank for processing.
  * **paid** : The payout has been successfully deposited into the bank.
  * **failed** : The payout has been declined by the bank.
  * **canceled** : The payout has been canceled by Shopify.


* * *

date

->[issuedAt](/docs/api/admin-graphql/latest/objects/ShopifyPaymentsPayout#field-ShopifyPaymentsPayout.fields.issuedAt)

The date ([ISO 8601 format](https://en.wikipedia.org/wiki/ISO_8601)) when the payout was issued.

* * *

currency

->[currencyCode](/docs/api/admin-graphql/latest/objects/MoneyV2#field-MoneyV2.fields.currencyCode)

The ISO 4217 currency code of the payout.

* * *

amount

->[amount](/docs/api/admin-graphql/latest/objects/MoneyV2#field-MoneyV2.fields.amount)

The total amount of the payout, in a decimal formatted string.

* * *

Was this section helpful?

YesNo

{}

## The Payouts resource

9

1

2

3

4

5

6

7

{

"id": 54534554564,

"status": "scheduled",

"date": "2018-03-22",

"currency": "USD",

"amount": "102.53"

}

* * *

##

[Anchor to GET request, Return a list of all payouts](/docs/api/admin-rest/latest/resources/payouts#get-shopify-payments-payouts)

get

Return a list of all payouts

[shopifyPaymentsAccount](/docs/api/admin-graphql/latest/queries/shopifyPaymentsAccount?example=return-a-list-of-all-payouts)

Retrieves a list of all payouts ordered by payout date, with the most recent being first. **Note:** This endpoint implements pagination by using links that are provided in the response header. To learn more, refer to [Make paginated requests to the REST Admin API](/api/usage/pagination-rest).

###

[Anchor to Parameters of Return a list of all payouts](/docs/api/admin-rest/latest/resources/payouts#get-shopify-payments-payouts-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

date

Filter the response to payouts made on the specified date.

* * *

date_max

Filter the response to payouts made inclusively before the specified date.

* * *

date_min

Filter the response to payouts made inclusively after the specified date.

* * *

last_id

Filter the response to payouts made before the specified ID.

* * *

since_id

Filter the response to payouts made after the specified ID.

* * *

status

Filter the response to payouts made with the specified status.

* * *

Was this section helpful?

YesNo

###

[Anchor to get-shopify-payments-payouts-examples](/docs/api/admin-rest/latest/resources/payouts#get-shopify-payments-payouts-examples)Examples

List all payouts ordered newest to oldest

List all payouts up to a specified date

Query parameters

date_max=2012-11-12

Filter the response to payouts made inclusively before the specified date.

Was this section helpful?

YesNo

get

## /admin/api/2026-01/shopify_payments/payouts.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/shopify_payments/payouts.json" \

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

"payouts": [

{

"id": 512467833,

"status": "failed",

"date": "2013-12-01",

"currency": "USD",

"amount": "43.12",

"summary": {

"adjustments_fee_amount": "0.12",

"adjustments_gross_amount": "2.13",

"charges_fee_amount": "1.32",

"charges_gross_amount": "45.52",

"refunds_fee_amount": "-0.23",

"refunds_gross_amount": "-3.54",

"reserved_funds_fee_amount": "0.00",

"reserved_funds_gross_amount": "0.00",

"retried_payouts_fee_amount": "0.00",

"retried_payouts_gross_amount": "0.00"

}

},

{

"id": 39438702,

"status": "in_transit",

"date": "2013-11-01",

"currency": "USD",

"amount": "43.12",

"summary": {

"adjustments_fee_amount": "0.12",

"adjustments_gross_amount": "2.13",

"charges_fee_amount": "1.32",

"charges_gross_amount": "45.52",

"refunds_fee_amount": "-0.23",

"refunds_gross_amount": "-3.54",

"reserved_funds_fee_amount": "0.00",

### examples

  * #### List all payouts ordered newest to oldest

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/shopify_payments/payouts.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Payout.all({
          session: session,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Payout.all(
          session: test_session,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Payout.all({
          session: session,
        });

#### response

        HTTP/1.1 200 OK{"payouts":[{"id":512467833,"status":"failed","date":"2013-12-01","currency":"USD","amount":"43.12","summary":{"adjustments_fee_amount":"0.12","adjustments_gross_amount":"2.13","charges_fee_amount":"1.32","charges_gross_amount":"45.52","refunds_fee_amount":"-0.23","refunds_gross_amount":"-3.54","reserved_funds_fee_amount":"0.00","reserved_funds_gross_amount":"0.00","retried_payouts_fee_amount":"0.00","retried_payouts_gross_amount":"0.00"}},{"id":39438702,"status":"in_transit","date":"2013-11-01","currency":"USD","amount":"43.12","summary":{"adjustments_fee_amount":"0.12","adjustments_gross_amount":"2.13","charges_fee_amount":"1.32","charges_gross_amount":"45.52","refunds_fee_amount":"-0.23","refunds_gross_amount":"-3.54","reserved_funds_fee_amount":"0.00","reserved_funds_gross_amount":"0.00","retried_payouts_fee_amount":"0.00","retried_payouts_gross_amount":"0.00"}},{"id":917000993,"status":"failed","date":"2012-11-13","currency":"USD","amount":"41.90","summary":{"adjustments_fee_amount":"0.12","adjustments_gross_amount":"2.13","charges_fee_amount":"1.32","charges_gross_amount":"44.52","refunds_fee_amount":"-0.23","refunds_gross_amount":"-3.54","reserved_funds_fee_amount":"0.00","reserved_funds_gross_amount":"0.00","retried_payouts_fee_amount":"0.00","retried_payouts_gross_amount":"0.00"}},{"id":867808544,"status":"paid","date":"2012-11-12","currency":"USD","amount":"41.90","summary":{"adjustments_fee_amount":"0.12","adjustments_gross_amount":"2.13","charges_fee_amount":"1.32","charges_gross_amount":"44.52","refunds_fee_amount":"-0.23","refunds_gross_amount":"-3.54","reserved_funds_fee_amount":"0.00","reserved_funds_gross_amount":"0.00","retried_payouts_fee_amount":"0.00","retried_payouts_gross_amount":"0.00"}},{"id":725076685,"status":"paid","date":"2012-11-12","currency":"USD","amount":"41.90","summary":{"adjustments_fee_amount":"0.12","adjustments_gross_amount":"2.13","charges_fee_amount":"1.32","charges_gross_amount":"44.52","refunds_fee_amount":"-0.23","refunds_gross_amount":"-3.54","reserved_funds_fee_amount":"0.00","reserved_funds_gross_amount":"0.00","retried_payouts_fee_amount":"0.00","retried_payouts_gross_amount":"0.00"}},{"id":714327683,"status":"failed","date":"2012-11-12","currency":"USD","amount":"41.90","summary":{"adjustments_fee_amount":"0.12","adjustments_gross_amount":"2.13","charges_fee_amount":"1.32","charges_gross_amount":"44.52","refunds_fee_amount":"-0.23","refunds_gross_amount":"-3.54","reserved_funds_fee_amount":"0.00","reserved_funds_gross_amount":"0.00","retried_payouts_fee_amount":"0.00","retried_payouts_gross_amount":"0.00"}},{"id":631321250,"status":"scheduled","date":"2012-11-12","currency":"USD","amount":"41.90","summary":{"adjustments_fee_amount":"0.12","adjustments_gross_amount":"2.13","charges_fee_amount":"1.32","charges_gross_amount":"44.52","refunds_fee_amount":"-0.23","refunds_gross_amount":"-3.54","reserved_funds_fee_amount":"0.00","reserved_funds_gross_amount":"0.00","retried_payouts_fee_amount":"0.00","retried_payouts_gross_amount":"0.00"}},{"id":623721858,"status":"paid","date":"2012-11-12","currency":"USD","amount":"41.90","summary":{"adjustments_fee_amount":"0.12","adjustments_gross_amount":"2.13","charges_fee_amount":"1.32","charges_gross_amount":"44.52","refunds_fee_amount":"-0.23","refunds_gross_amount":"-3.54","reserved_funds_fee_amount":"0.00","reserved_funds_gross_amount":"0.00","retried_payouts_fee_amount":"0.00","retried_payouts_gross_amount":"0.00"}}]}

  * #### List all payouts up to a specified date

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/shopify_payments/payouts.json?date_max=2012-11-12" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Payout.all({
          session: session,
          date_max: "2012-11-12",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Payout.all(
          session: test_session,
          date_max: "2012-11-12",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Payout.all({
          session: session,
          date_max: "2012-11-12",
        });

#### response

        HTTP/1.1 200 OK{"payouts":[{"id":867808544,"status":"paid","date":"2012-11-12","currency":"USD","amount":"41.90","summary":{"adjustments_fee_amount":"0.12","adjustments_gross_amount":"2.13","charges_fee_amount":"1.32","charges_gross_amount":"44.52","refunds_fee_amount":"-0.23","refunds_gross_amount":"-3.54","reserved_funds_fee_amount":"0.00","reserved_funds_gross_amount":"0.00","retried_payouts_fee_amount":"0.00","retried_payouts_gross_amount":"0.00"}},{"id":725076685,"status":"paid","date":"2012-11-12","currency":"USD","amount":"41.90","summary":{"adjustments_fee_amount":"0.12","adjustments_gross_amount":"2.13","charges_fee_amount":"1.32","charges_gross_amount":"44.52","refunds_fee_amount":"-0.23","refunds_gross_amount":"-3.54","reserved_funds_fee_amount":"0.00","reserved_funds_gross_amount":"0.00","retried_payouts_fee_amount":"0.00","retried_payouts_gross_amount":"0.00"}},{"id":714327683,"status":"failed","date":"2012-11-12","currency":"USD","amount":"41.90","summary":{"adjustments_fee_amount":"0.12","adjustments_gross_amount":"2.13","charges_fee_amount":"1.32","charges_gross_amount":"44.52","refunds_fee_amount":"-0.23","refunds_gross_amount":"-3.54","reserved_funds_fee_amount":"0.00","reserved_funds_gross_amount":"0.00","retried_payouts_fee_amount":"0.00","retried_payouts_gross_amount":"0.00"}},{"id":631321250,"status":"scheduled","date":"2012-11-12","currency":"USD","amount":"41.90","summary":{"adjustments_fee_amount":"0.12","adjustments_gross_amount":"2.13","charges_fee_amount":"1.32","charges_gross_amount":"44.52","refunds_fee_amount":"-0.23","refunds_gross_amount":"-3.54","reserved_funds_fee_amount":"0.00","reserved_funds_gross_amount":"0.00","retried_payouts_fee_amount":"0.00","retried_payouts_gross_amount":"0.00"}},{"id":623721858,"status":"paid","date":"2012-11-12","currency":"USD","amount":"41.90","summary":{"adjustments_fee_amount":"0.12","adjustments_gross_amount":"2.13","charges_fee_amount":"1.32","charges_gross_amount":"44.52","refunds_fee_amount":"-0.23","refunds_gross_amount":"-3.54","reserved_funds_fee_amount":"0.00","reserved_funds_gross_amount":"0.00","retried_payouts_fee_amount":"0.00","retried_payouts_gross_amount":"0.00"}}]}


* * *

##

[Anchor to GET request, Return a single payout](/docs/api/admin-rest/latest/resources/payouts#get-shopify-payments-payouts-payout-id)

get

Return a single payout

[shopifyPaymentsAccount](/docs/api/admin-graphql/latest/queries/shopifyPaymentsAccount?example=return-a-single-payout)

Retrieves a single payout by id.

###

[Anchor to Parameters of Return a single payout](/docs/api/admin-rest/latest/resources/payouts#get-shopify-payments-payouts-payout-id-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

payout_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to get-shopify-payments-payouts-payout-id-examples](/docs/api/admin-rest/latest/resources/payouts#get-shopify-payments-payouts-payout-id-examples)Examples

Retrieves a single payout by id

Path parameters

payout_id=623721858

string**string**

required**required**

Was this section helpful?

YesNo

get

## /admin/api/2026-01/shopify_payments/payouts/623721858.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/shopify_payments/payouts/623721858.json" \

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

HTTP/1.1 200 OK

{

"payout": {

"id": 623721858,

"status": "paid",

"date": "2012-11-12",

"currency": "USD",

"amount": "41.90",

"summary": {

"adjustments_fee_amount": "0.12",

"adjustments_gross_amount": "2.13",

"charges_fee_amount": "1.32",

"charges_gross_amount": "44.52",

"refunds_fee_amount": "-0.23",

"refunds_gross_amount": "-3.54",

"reserved_funds_fee_amount": "0.00",

"reserved_funds_gross_amount": "0.00",

"retried_payouts_fee_amount": "0.00",

"retried_payouts_gross_amount": "0.00"

}

}

}

### examples

  * #### Retrieves a single payout by id

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/shopify_payments/payouts/623721858.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Payout.find({
          session: session,
          id: 623721858,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Payout.find(
          session: test_session,
          id: 623721858,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Payout.find({
          session: session,
          id: 623721858,
        });

#### response

        HTTP/1.1 200 OK{"payout":{"id":623721858,"status":"paid","date":"2012-11-12","currency":"USD","amount":"41.90","summary":{"adjustments_fee_amount":"0.12","adjustments_gross_amount":"2.13","charges_fee_amount":"1.32","charges_gross_amount":"44.52","refunds_fee_amount":"-0.23","refunds_gross_amount":"-3.54","reserved_funds_fee_amount":"0.00","reserved_funds_gross_amount":"0.00","retried_payouts_fee_amount":"0.00","retried_payouts_gross_amount":"0.00"}}}