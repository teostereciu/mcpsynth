# ApplicationCredit

*Source: https://shopify.dev/docs/api/admin-rest/2026-01/resources/applicationcredit*

---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04

2026-01latest

# ApplicationCredit

Ask assistant

Important

Creating application credits through this resource is being deprecated. App credits can continue to be created using the [appCreditCreate mutation](https://shopify.dev/docs/api/partner/unstable/mutations/appCreditCreate) in the Partner API.

**Important:**

Creating application credits through this resource is being deprecated. App credits can continue to be created using the [appCreditCreate mutation](https://shopify.dev/docs/api/partner/unstable/mutations/appCreditCreate) in the Partner API.

The ApplicationCredit resource is used to issue credits to merchants that can be used towards future app purchases in Shopify. You can create an application credit by sending a request that includes the credit amount and a description explaining the reason for the credit. A corresponding deduction based on your revenue share is entered in your Partner account by Shopify. For example, if you create a credit for $10.00, then a deduction of $8.00 is applied.

The total amount of all application credits requested by an app must not exceed the total amount the shop owner was charged in the last 30 days, or the total amount of pending payouts in the app's Partner account.

Note

The ApplicationCredit resource can be used only by apps that use Shopify's Billing API ([ApplicationCharge](/docs/admin-api/rest/reference/billing/applicationcharge), [RecurringApplicationCharge](/docs/admin-api/rest/reference/billing/recurringapplicationcharge), or [UsageCharge](/docs/admin-api/rest/reference/billing/usagecharge)).

**Note:**

The ApplicationCredit resource can be used only by apps that use Shopify's Billing API ([ApplicationCharge](/docs/admin-api/rest/reference/billing/applicationcharge), [RecurringApplicationCharge](/docs/admin-api/rest/reference/billing/recurringapplicationcharge), or [UsageCharge](/docs/admin-api/rest/reference/billing/usagecharge)).

Was this section helpful?

YesNo

#

## Endpoints

  * [get/admin/api/latest/application_credits.json](/docs/api/admin-rest/latest/resources/applicationcredit#get-application-credits)

Retrieves all application credits

[appInstallation](/docs/api/admin-graphql/latest/queries/appInstallation?example=retrieves-all-application-credits)

  * [get/admin/api/latest/application_credits/{application_credit_id}.json](/docs/api/admin-rest/latest/resources/applicationcredit#get-application-credits-application-credit-id)

Retrieves a single application credit


* * *

[Anchor to ](/docs/api/admin-rest/latest/resources/applicationcredit#resource-object)

## The ApplicationCredit resource

[Anchor to ](/docs/api/admin-rest/latest/resources/applicationcredit#resource-object-properties)

### Properties

* * *

description

->[description](/docs/api/admin-graphql/latest/objects/AppCredit#field-AppCredit.fields.description)

The description of the application credit.

* * *

id

->[id](/docs/api/admin-graphql/latest/objects/AppCredit#field-AppCredit.fields.id)

The ID of the application credit.

* * *

amount

string**string**

->[amount](/docs/api/admin-graphql/latest/objects/AppCredit#field-AppCredit.fields.amount)

The amount refunded by the application credit.

* * *

test

->[test](/docs/api/admin-graphql/latest/objects/AppCredit#field-AppCredit.fields.test)

Whether the application credit is a test transaction. Valid values: `true`,`null`

* * *

currency

->[amount](/docs/api/admin-graphql/latest/objects/AppCredit#field-AppCredit.fields.amount)

The currency of the application credit amount.

* * *

Was this section helpful?

YesNo

{}

## The ApplicationCredit resource

9

1

2

3

4

5

6

7

{

"description": "Super Mega Plan 1000 emails",

"id": 675931192,

"amount": "10",

"test": null,

"currency": "USD"

}

* * *

##

[Anchor to GET request, Retrieves all application credits](/docs/api/admin-rest/latest/resources/applicationcredit#get-application-credits)

get

Retrieves all application credits

[appInstallation](/docs/api/admin-graphql/latest/queries/appInstallation?example=retrieves-all-application-credits)

Retrieves all application credits

###

[Anchor to Parameters of Retrieves all application credits](/docs/api/admin-rest/latest/resources/applicationcredit#get-application-credits-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

fields

A comma-separated list of fields to include in the response.

* * *

Was this section helpful?

YesNo

###

[Anchor to get-application-credits-examples](/docs/api/admin-rest/latest/resources/applicationcredit#get-application-credits-examples)Examples

Retrieve all application credits

Was this section helpful?

YesNo

get

## /admin/api/2026-01/application_credits.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/application_credits.json" \

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

HTTP/1.1 200 OK

{

"application_credits": [

{

"id": 140583599,

"amount": "5.00",

"description": "credit for application refund",

"test": null,

"currency": "USD"

}

]

}

### examples

  * #### Retrieve all application credits

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/application_credits.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.ApplicationCredit.all({
          session: session,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::ApplicationCredit.all(
          session: test_session,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.ApplicationCredit.all({
          session: session,
        });

#### response

        HTTP/1.1 200 OK{"application_credits":[{"id":140583599,"amount":"5.00","description":"credit for application refund","test":null,"currency":"USD"}]}


* * *

##

[Anchor to GET request, Retrieves a single application credit](/docs/api/admin-rest/latest/resources/applicationcredit#get-application-credits-application-credit-id)

get

Retrieves a single application credit

Retrieves a single application credit

###

[Anchor to Parameters of Retrieves a single application credit](/docs/api/admin-rest/latest/resources/applicationcredit#get-application-credits-application-credit-id-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

application_credit_id

string**string**

required**required**

* * *

fields

A comma-separated list of fields to include in the response.

* * *

Was this section helpful?

YesNo

###

[Anchor to get-application-credits-application-credit-id-examples](/docs/api/admin-rest/latest/resources/applicationcredit#get-application-credits-application-credit-id-examples)Examples

Retrieve a single application credit

Path parameters

application_credit_id=140583599

string**string**

required**required**

Was this section helpful?

YesNo

get

## /admin/api/2026-01/application_credits/140583599.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/application_credits/140583599.json" \

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

HTTP/1.1 200 OK

{

"application_credit": {

"id": 140583599,

"amount": "5.00",

"description": "credit for application refund",

"test": null,

"currency": "USD"

}

}

### examples

  * #### Retrieve a single application credit

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/application_credits/140583599.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.ApplicationCredit.find({
          session: session,
          id: 140583599,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::ApplicationCredit.find(
          session: test_session,
          id: 140583599,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.ApplicationCredit.find({
          session: session,
          id: 140583599,
        });

#### response

        HTTP/1.1 200 OK{"application_credit":{"id":140583599,"amount":"5.00","description":"credit for application refund","test":null,"currency":"USD"}}