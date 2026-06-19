# UsageCharge

*Source: https://shopify.dev/docs/api/admin-rest/2026-01/resources/usagecharge*

---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04

2026-01latest

# UsageCharge

Ask assistant

You can use the UsageCharge resource to add variable usage fees to an existing [recurring application charge](/docs/admin-api/rest/reference/billing/recurringapplicationcharge). You can use these resources to support billing plans that vary from month to month, with or without a monthly recurring fee.

## Creating usage charges

To use the UsageCharge resource, first create a [recurring application charge](/docs/admin-api/rest/reference/billing/recurringapplicationcharge). This returns the ID that you'll need to create an associated usage charge.

To create the usage charge, send a POST request, where `{id}` represents the ID of the previously created recurring application charge.


    POST

/admin/recurring_application_charges/{id}/usage_charges.json

### Charging for usage only

A common billing scenario is to charge only usage-based fees, without a flat recurring monthly fee. To charge only usage-based fees without a recurring monthly fee, first create a [recurring application charge](/docs/admin-api/rest/reference/billing/recurringapplicationcharge/) with a price of $0.00 and then apply the usage charge.

You need to include the `capped_amount` and `terms` properties in the body of your request when you create a recurring application charge with a price of $0.00.

## Setting capped amounts

You can use the RecurringApplicationCharge resource to specify a capped amount that applies to usage-based billing. This prevents the customer from being charged for any usage over and above the capped amount. To implement capped amount billing, create a recurring application charge with the capped dollar amount, and then create the associated usage charge.

Note

The capped amount setting is applicable on a per billing cycle basis (30 days), and remains in effect unless updated.

**Note:**

The capped amount setting is applicable on a per billing cycle basis (30 days), and remains in effect unless updated.

For step-by-step guidance that walks through this flow using examples, see our [implementation guide](/apps/billing/models).

Was this section helpful?

YesNo

#

## Endpoints

  * [post/admin/api/latest/recurring_application_charges/{recurring_application_charge_id}/usage_charges.json](/docs/api/admin-rest/latest/resources/usagecharge#post-recurring-application-charges-recurring-application-charge-id-usage-charges)

Creates a usage charge

[appUsageRecordCreate](/docs/api/admin-graphql/latest/mutations/appUsageRecordCreate?example=creates-a-usage-charge)

  * [get/admin/api/latest/recurring_application_charges/{recurring_application_charge_id}/usage_charges.json](/docs/api/admin-rest/latest/resources/usagecharge#get-recurring-application-charges-recurring-application-charge-id-usage-charges)

Retrieves a list of usage charges

[nodes](/docs/api/admin-graphql/latest/queries/nodes)

  * [get/admin/api/latest/recurring_application_charges/{recurring_application_charge_id}/usage_charges/{usage_charge_id}.json](/docs/api/admin-rest/latest/resources/usagecharge#get-recurring-application-charges-recurring-application-charge-id-usage-charges-usage-charge-id)

Retrieves a single charge

[node](/docs/api/admin-graphql/latest/queries/node)


* * *

[Anchor to ](/docs/api/admin-rest/latest/resources/usagecharge#resource-object)

## The UsageCharge resource

[Anchor to ](/docs/api/admin-rest/latest/resources/usagecharge#resource-object-properties)

### Properties

* * *

created_at

->[createdAt](/docs/api/admin-graphql/latest/objects/AppUsageRecord#field-AppUsageRecord.fields.createdAt)

The date and time ([ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format) when the usage charge was created.

* * *

description

->[description](/docs/api/admin-graphql/latest/objects/AppUsageRecord#field-AppUsageRecord.fields.description)

The description of the usage charge.

* * *

id

->[id](/docs/api/admin-graphql/latest/objects/AppUsageRecord#field-AppUsageRecord.fields.id)

The ID of the usage charge.

* * *

price

string**string**

->[price](/docs/api/admin-graphql/latest/objects/AppUsageRecord#field-AppUsageRecord.fields.price)

The price of the usage charge.

* * *

recurring_application_charge_id

->[subscriptionLineItem](/docs/api/admin-graphql/latest/objects/AppUsageRecord#field-AppUsageRecord.fields.subscriptionLineItem)

The ID of the recurring application charge that the usage charge belongs to.

* * *

updated_at

The date and time ([ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format) when the usage charge was last updated.

* * *

currency

->[price](/docs/api/admin-graphql/latest/objects/AppUsageRecord#field-AppUsageRecord.fields.price)

The currency of the price of the usage charge.

* * *

Was this section helpful?

YesNo

{}

## The UsageCharge resource

9

1

2

3

4

5

6

7

8

9

{

"created_at": "2013-06-27T08:48:27-04:00",

"description": "Super Mega Plan 1000 emails",

"id": 675931192,

"price": "1",

"recurring_application_charge_id": 527669426,

"updated_at": "2013-06-27T08:48:27-04:00",

"currency": "USD"

}

* * *

##

[Anchor to POST request, Creates a usage charge](/docs/api/admin-rest/latest/resources/usagecharge#post-recurring-application-charges-recurring-application-charge-id-usage-charges)

post

Creates a usage charge

[appUsageRecordCreate](/docs/api/admin-graphql/latest/mutations/appUsageRecordCreate?example=creates-a-usage-charge)

Creates a usage charge

###

[Anchor to Parameters of Creates a usage charge](/docs/api/admin-rest/latest/resources/usagecharge#post-recurring-application-charges-recurring-application-charge-id-usage-charges-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

recurring_application_charge_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to post-recurring-application-charges-recurring-application-charge-id-usage-charges-examples](/docs/api/admin-rest/latest/resources/usagecharge#post-recurring-application-charges-recurring-application-charge-id-usage-charges-examples)Examples

Create a new usage charge

Path parameters

recurring_application_charge_id=455696195

string**string**

required**required**

Request body

usage_charge

Usage_charge resource**Usage_charge resource**

Show usage_charge properties

usage_charge.description:"Super Mega Plan 1000 emails"

The description of the usage charge.

usage_charge.price:"1.00"

string**string**

The price of the usage charge.

Trying to create a charge which exceeds the remaining balance will return an error

Path parameters

recurring_application_charge_id=455696195

string**string**

required**required**

Request body

usage_charge

Usage_charge resource**Usage_charge resource**

Show usage_charge properties

usage_charge.description:"Super Mega Plan 1000 emails"

The description of the usage charge.

usage_charge.price:9999

string**string**

The price of the usage charge.

Trying to create a charge without a price or a description will return an error

Path parameters

recurring_application_charge_id=455696195

string**string**

required**required**

Request body

usage_charge

Usage_charge resource**Usage_charge resource**

Show usage_charge properties

usage_charge.description:""

The description of the usage charge.

Was this section helpful?

YesNo

post

## /admin/api/2026-01/recurring_application_charges/455696195/usage_charges.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{"usage_charge":{"description":"Super Mega Plan 1000 emails","price":"1.00"}}' \

-X POST "https://your-development-store.myshopify.com/admin/api/2026-01/recurring_application_charges/455696195/usage_charges.json" \

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

"usage_charge": {

"id": 1034618219,

"description": "Super Mega Plan 1000 emails",

"price": "1.00",

"created_at": "2026-01-09T17:26:13-05:00",

"currency": "USD",

"balance_used": "11.0",

"balance_remaining": "89.00",

"risk_level": 0

}

}

### examples

  * #### Create a new usage charge

#####

        curl -d '{"usage_charge":{"description":"Super Mega Plan 1000 emails","price":"1.00"}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/recurring_application_charges/455696195/usage_charges.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const usage_charge = new admin.rest.resources.UsageCharge({session: session});

        usage_charge.recurring_application_charge_id = 455696195;
        usage_charge.description = "Super Mega Plan 1000 emails";
        usage_charge.price = "1.00";
        await usage_charge.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        usage_charge = ShopifyAPI::UsageCharge.new(session: test_session)
        usage_charge.recurring_application_charge_id = 455696195
        usage_charge.description = "Super Mega Plan 1000 emails"
        usage_charge.price = "1.00"
        usage_charge.save!

#####

        // Session is built by the OAuth process

        const usage_charge = new shopify.rest.UsageCharge({session: session});
        usage_charge.recurring_application_charge_id = 455696195;
        usage_charge.description = "Super Mega Plan 1000 emails";
        usage_charge.price = "1.00";
        await usage_charge.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"usage_charge":{"id":1034618219,"description":"Super Mega Plan 1000 emails","price":"1.00","created_at":"2026-01-09T17:26:13-05:00","currency":"USD","balance_used":"11.0","balance_remaining":"89.00","risk_level":0}}

  * #### Trying to create a charge which exceeds the remaining balance will return an error

#####

        curl -d '{"usage_charge":{"description":"Super Mega Plan 1000 emails","price":9999}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/recurring_application_charges/455696195/usage_charges.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const usage_charge = new admin.rest.resources.UsageCharge({session: session});

        usage_charge.recurring_application_charge_id = 455696195;
        usage_charge.description = "Super Mega Plan 1000 emails";
        usage_charge.price = 9999;
        await usage_charge.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        usage_charge = ShopifyAPI::UsageCharge.new(session: test_session)
        usage_charge.recurring_application_charge_id = 455696195
        usage_charge.description = "Super Mega Plan 1000 emails"
        usage_charge.price = 9999
        usage_charge.save!

#####

        // Session is built by the OAuth process

        const usage_charge = new shopify.rest.UsageCharge({session: session});
        usage_charge.recurring_application_charge_id = 455696195;
        usage_charge.description = "Super Mega Plan 1000 emails";
        usage_charge.price = 9999;
        await usage_charge.save({
          update: true,
        });

#### response

        HTTP/1.1 422 Unprocessable Entity{"errors":{"base":["Total price exceeds balance remaining"]}}

  * #### Trying to create a charge without a price or a description will return an error

#####

        curl -d '{"usage_charge":{"description":""}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/recurring_application_charges/455696195/usage_charges.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const usage_charge = new admin.rest.resources.UsageCharge({session: session});

        usage_charge.recurring_application_charge_id = 455696195;
        usage_charge.description = "";
        await usage_charge.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        usage_charge = ShopifyAPI::UsageCharge.new(session: test_session)
        usage_charge.recurring_application_charge_id = 455696195
        usage_charge.description = ""
        usage_charge.save!

#####

        // Session is built by the OAuth process

        const usage_charge = new shopify.rest.UsageCharge({session: session});
        usage_charge.recurring_application_charge_id = 455696195;
        usage_charge.description = "";
        await usage_charge.save({
          update: true,
        });

#### response

        HTTP/1.1 422 Unprocessable Entity{"errors":{"description":["can't be blank"],"price":["must be greater than zero"]}}


* * *

##

[Anchor to GET request, Retrieves a list of usage charges](/docs/api/admin-rest/latest/resources/usagecharge#get-recurring-application-charges-recurring-application-charge-id-usage-charges)

get

Retrieves a list of usage charges

[nodes](/docs/api/admin-graphql/latest/queries/nodes)

Retrieves a list of usage charges

###

[Anchor to Parameters of Retrieves a list of usage charges](/docs/api/admin-rest/latest/resources/usagecharge#get-recurring-application-charges-recurring-application-charge-id-usage-charges-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

recurring_application_charge_id

string**string**

required**required**

* * *

fields

A comma-separated list of fields to include in the response.

* * *

Was this section helpful?

YesNo

###

[Anchor to get-recurring-application-charges-recurring-application-charge-id-usage-charges-examples](/docs/api/admin-rest/latest/resources/usagecharge#get-recurring-application-charges-recurring-application-charge-id-usage-charges-examples)Examples

Retrieve all usage charges

Path parameters

recurring_application_charge_id=455696195

string**string**

required**required**

Was this section helpful?

YesNo

get

## /admin/api/2026-01/recurring_application_charges/455696195/usage_charges.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/recurring_application_charges/455696195/usage_charges.json" \

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

"usage_charges": [

{

"id": 1034618217,

"description": "Super Mega Plan Add-ons",

"price": "10.00",

"created_at": "2026-01-09T17:26:10-05:00",

"currency": "USD",

"balance_used": "10.0",

"balance_remaining": "90.00",

"risk_level": 0

}

]

}

### examples

  * #### Retrieve all usage charges

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/recurring_application_charges/455696195/usage_charges.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.UsageCharge.all({
          session: session,
          recurring_application_charge_id: 455696195,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::UsageCharge.all(
          session: test_session,
          recurring_application_charge_id: 455696195,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.UsageCharge.all({
          session: session,
          recurring_application_charge_id: 455696195,
        });

#### response

        HTTP/1.1 200 OK{"usage_charges":[{"id":1034618217,"description":"Super Mega Plan Add-ons","price":"10.00","created_at":"2026-01-09T17:26:10-05:00","currency":"USD","balance_used":"10.0","balance_remaining":"90.00","risk_level":0}]}


* * *

##

[Anchor to GET request, Retrieves a single charge](/docs/api/admin-rest/latest/resources/usagecharge#get-recurring-application-charges-recurring-application-charge-id-usage-charges-usage-charge-id)

get

Retrieves a single charge

[node](/docs/api/admin-graphql/latest/queries/node)

Retrieves a single charge

###

[Anchor to Parameters of Retrieves a single charge](/docs/api/admin-rest/latest/resources/usagecharge#get-recurring-application-charges-recurring-application-charge-id-usage-charges-usage-charge-id-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

recurring_application_charge_id

string**string**

required**required**

* * *

usage_charge_id

string**string**

required**required**

* * *

fields

A comma-separated list of fields to include in the response.

* * *

Was this section helpful?

YesNo

###

[Anchor to get-recurring-application-charges-recurring-application-charge-id-usage-charges-usage-charge-id-examples](/docs/api/admin-rest/latest/resources/usagecharge#get-recurring-application-charges-recurring-application-charge-id-usage-charges-usage-charge-id-examples)Examples

Retrieve a single charge

Was this section helpful?

YesNo

get

## /admin/api/2026-01/recurring_application_charges/455696195/usage_charges/1034618215.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/recurring_application_charges/455696195/usage_charges/1034618215.json" \

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

"usage_charge": {

"id": 1034618215,

"description": "Super Mega Plan Add-ons",

"price": "10.00",

"created_at": "2026-01-09T17:26:08-05:00",

"currency": "USD",

"balance_used": "10.0",

"balance_remaining": "90.00",

"risk_level": 0

}

}

### examples

  * #### Retrieve a single charge

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/recurring_application_charges/455696195/usage_charges/1034618215.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.UsageCharge.find({
          session: session,
          recurring_application_charge_id: 455696195,
          id: 1034618215,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::UsageCharge.find(
          session: test_session,
          recurring_application_charge_id: 455696195,
          id: 1034618215,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.UsageCharge.find({
          session: session,
          recurring_application_charge_id: 455696195,
          id: 1034618215,
        });

#### response

        HTTP/1.1 200 OK{"usage_charge":{"id":1034618215,"description":"Super Mega Plan Add-ons","price":"10.00","created_at":"2026-01-09T17:26:08-05:00","currency":"USD","balance_used":"10.0","balance_remaining":"90.00","risk_level":0}}