# RecurringApplicationCharge

*Source: https://shopify.dev/docs/api/admin-rest/2026-01/resources/recurringapplicationcharge*

---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04

2026-01latest

# RecurringApplicationCharge

Ask assistant

The RecurringApplicationCharge resource facilitates a fixed-value, 30-day recurring charge. You can create an application charge by sending a request with the name the charge should appear under, the price your app is charging, and a return URL where Shopify redirects the merchant after the charge is accepted. After you've created the charge, redirect the merchant to the confirmation URL returned by Shopify. If the charge is declined, then Shopify redirects the merchant and provides a notification message that the app charge was declined.

Note

For testing purposes you can include `"test": true` when creating the charge. This prevents the credit card from being charged. Test shops and demo shops cannot be charged.

**Note:**

For testing purposes you can include `"test": true` when creating the charge. This prevents the credit card from being charged. Test shops and demo shops cannot be charged.

### Updating an application charge

Each shop can have only one recurring charge per app. When a new recurring application charge is activated for a shop that already has one, the existing recurring charge is canceled and replaced by the new charge. The new recurring charge is then activated.

For example, if you want to offer discounted pricing to a specific merchant, then you can create a new application charge for the shop. This will prompt the shop to accept the new charge in order to continue using the app. The new charge replaces the old billing going forward.

Was this section helpful?

YesNo

#

## Endpoints

  * [post/admin/api/latest/recurring_application_charges.json](/docs/api/admin-rest/latest/resources/recurringapplicationcharge#post-recurring-application-charges)

Creates a recurring application charge

[appSubscriptionCreate](/docs/api/admin-graphql/latest/mutations/appSubscriptionCreate?example=creates-a-recurring-application-charge)

  * [get/admin/api/latest/recurring_application_charges.json](/docs/api/admin-rest/latest/resources/recurringapplicationcharge#get-recurring-application-charges)

Retrieves a list of recurring application charges

[currentAppInstallation](/docs/api/admin-graphql/latest/queries/currentAppInstallation?example=retrieves-a-list-of-recurring-application-charges)

  * [get/admin/api/latest/recurring_application_charges/{recurring_application_charge_id}.json](/docs/api/admin-rest/latest/resources/recurringapplicationcharge#get-recurring-application-charges-recurring-application-charge-id)

Retrieves a single charge

  * [put/admin/api/latest/recurring_application_charges/{recurring_application_charge_id}/customize.json?recurring_application_charge[capped_amount]=200](/docs/api/admin-rest/latest/resources/recurringapplicationcharge#put-recurring-application-charges-recurring-application-charge-id-customize?recurring-application-charge\[capped-amount\]=200)

Updates the capped amount of a recurring application charge

[appSubscriptionLineItemUpdate](/docs/api/admin-graphql/latest/mutations/appSubscriptionLineItemUpdate?example=updates-the-capped-amount-of-a-recurring-application-charge)

  * [del/admin/api/latest/recurring_application_charges/{recurring_application_charge_id}.json](/docs/api/admin-rest/latest/resources/recurringapplicationcharge#delete-recurring-application-charges-recurring-application-charge-id)

Cancels a recurring application charge

[appSubscriptionCancel](/docs/api/admin-graphql/latest/mutations/appSubscriptionCancel?example=cancels-a-recurring-application-charge)


* * *

[Anchor to ](/docs/api/admin-rest/latest/resources/recurringapplicationcharge#resource-object)

## The RecurringApplicationCharge resource

[Anchor to ](/docs/api/admin-rest/latest/resources/recurringapplicationcharge#resource-object-properties)

### Properties

* * *

activated_on

->[createdAt](/docs/api/admin-graphql/latest/objects/AppSubscription#field-AppSubscription.fields.createdAt)

The date and time ([ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format) when the customer activated the recurring application charge.
**Note:** The recurring application charge must be activated or the returned value is `null`.

* * *

billing_on

->[currentPeriodEnd](/docs/api/admin-graphql/latest/objects/AppSubscription#field-AppSubscription.fields.currentPeriodEnd)

The date and time ([ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format) when the customer is billed.
**Note:** The recurring application charge must be accepted or the returned value is `null`.

* * *

cancelled_on

deprecated**deprecated**

The date and time ([ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format) when the merchant canceled their recurring application charge.
**Note:** Returns `null` when the recurring application charge is not canceled.

* * *

capped_amount

->[cappedAmount](/docs/api/admin-graphql/latest/objects/AppUsagePricing#field-AppUsagePricing.fields.cappedAmount)

The limit a customer can be charged for usage based billing. If this property is provided, then you must also provide the `terms` property. See [usage charges](/docs/admin-api/rest/reference/billing/usagecharge) for more information.

* * *

confirmation_url

The URL where the merchant accepts or declines the recurring application charge.

* * *

created_at

->[createdAt](/docs/api/admin-graphql/latest/objects/AppSubscription#field-AppSubscription.fields.createdAt)

The date and time ([ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format) when the recurring application charge was created.

* * *

id

->[id](/docs/api/admin-graphql/latest/objects/AppSubscription#field-AppSubscription.fields.id)

The ID of the recurring application charge.

* * *

name

->[name](/docs/api/admin-graphql/latest/objects/AppSubscription#field-AppSubscription.fields.name)

The name of the recurring application charge.

* * *

price

->[price](/docs/api/admin-graphql/latest/objects/AppRecurringPricing#field-AppRecurringPricing.fields.price)

The price of the recurring application charge. The maximum price is 10,000.

* * *

return_url

->[returnUrl](/docs/api/admin-graphql/latest/objects/AppSubscription#field-AppSubscription.fields.returnUrl)

The URL where the merchant is redirected after accepting the charge.

* * *

status

->[status](/docs/api/admin-graphql/latest/objects/AppSubscription#field-AppSubscription.fields.status)

The status of the recurring charge. Valid values:

Show status properties

  * **pending** : The recurring charge is pending.
  * **accepted** : **Removed in version 2021-01**. The recurring charge has been accepted. As of API version 2021-01, when a merchant accepts a charge, the charge immediately transitions from `pending` to `active`.
  * **active** : The recurring charge is activated. This is the only status that actually causes a merchant to be charged. As of API version 2021-01, when a merchant accepts a charge, the charge immediately transitions from `pending` to `active`.
  * **declined** : The recurring charge has been declined.
  * **expired** : The recurring charge was not accepted within 2 days of being created.
  * **frozen** : The recurring charge is on hold due to a shop subscription non-payment. The charge will re-activate once subscription payments resume.
  * **cancelled** : The developer cancelled the charge.


* * *

terms

->[terms](/docs/api/admin-graphql/latest/objects/AppUsagePricing#field-AppUsagePricing.fields.terms)

The terms and conditions of usage based billing charges. Must be present in order to create usage charges, for example when the `capped_amount` property is provided. Presented to the merchant when they approve an app's usage charges.

* * *

Show 5 hidden fields

Was this section helpful?

YesNo

{}

## The RecurringApplicationCharge resource

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

"activated_on": null,

"billing_on": null,

"cancelled_on": null,

"capped_amount": "100",

"confirmation_url": "https://jsmith.myshopify.com/admin/charges/confirm_recurring_application_charge?id=654381177&signature=BAhpBHkQASc%3D--374c02da2ea0371b23f40781b8a6d5f4a520e77b",

"created_at": "2013-06-27T08:48:27-04:00",

"id": 675931192,

"name": "Super Duper Expensive action",

"price": "100.00",

"return_url": "http://super-duper.shopifyapps.com",

"status": "accepted",

"terms": "$1 for 1000 emails",

"test": null,

"trial_days": 0,

"trial_ends_on": null,

"updated_at": "2013-06-27T08:48:27-04:00",

"currency": "USD"

}

* * *

##

[Anchor to POST request, Creates a recurring application charge](/docs/api/admin-rest/latest/resources/recurringapplicationcharge#post-recurring-application-charges)

post

Creates a recurring application charge

[appSubscriptionCreate](/docs/api/admin-graphql/latest/mutations/appSubscriptionCreate?example=creates-a-recurring-application-charge)

Creates a recurring application charge. Make sure to include a valid `return_url` property to ensure the merchant is redirected after accepting the charge (an invalid or missing `return_url` property may lead to unstable behaviour in the charge approval flow).

###

[Anchor to Parameters of Creates a recurring application charge](/docs/api/admin-rest/latest/resources/recurringapplicationcharge#post-recurring-application-charges-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to post-recurring-application-charges-examples](/docs/api/admin-rest/latest/resources/recurringapplicationcharge#post-recurring-application-charges-examples)Examples

Create a new charge with a trial period. The trial period will go into effect at the time the recurring charge is activated.

Request body

recurring_application_charge

Recurring_application_charge resource**Recurring_application_charge resource**

Show recurring_application_charge properties

recurring_application_charge.name:"Super Duper Plan"

The name of the recurring application charge.

recurring_application_charge.price:10

The price of the recurring application charge. The maximum price is 10,000.

recurring_application_charge.return_url:"http://super-duper.shopifyapps.com"

The URL where the merchant is redirected after accepting the charge.

recurring_application_charge.trial_days:5

The number of days that the customer is eligible for a free trial.

Create a new charge with terms and a capped amount

Request body

recurring_application_charge

Recurring_application_charge resource**Recurring_application_charge resource**

Show recurring_application_charge properties

recurring_application_charge.name:"Super Duper Plan"

The name of the recurring application charge.

recurring_application_charge.price:10

The price of the recurring application charge. The maximum price is 10,000.

recurring_application_charge.return_url:"http://super-duper.shopifyapps.com"

The URL where the merchant is redirected after accepting the charge.

recurring_application_charge.capped_amount:100

The limit a customer can be charged for usage based billing. If this property is provided, then you must also provide the `terms` property. See [usage charges](/docs/admin-api/rest/reference/billing/usagecharge) for more information.

recurring_application_charge.terms:"$1 for 1000 emails"

The terms and conditions of usage based billing charges. Must be present in order to create usage charges, for example when the `capped_amount` property is provided. Presented to the merchant when they approve an app's usage charges.

Create a recurring application charge

Request body

recurring_application_charge

Recurring_application_charge resource**Recurring_application_charge resource**

Show recurring_application_charge properties

recurring_application_charge.name:"Super Duper Plan"

The name of the recurring application charge.

recurring_application_charge.price:10

The price of the recurring application charge. The maximum price is 10,000.

recurring_application_charge.return_url:"http://super-duper.shopifyapps.com"

The URL where the merchant is redirected after accepting the charge.

Create a recurring test charge that will not cause a credit card to be charged

Request body

recurring_application_charge

Recurring_application_charge resource**Recurring_application_charge resource**

Show recurring_application_charge properties

recurring_application_charge.name:"Super Duper Plan"

The name of the recurring application charge.

recurring_application_charge.price:10

The price of the recurring application charge. The maximum price is 10,000.

recurring_application_charge.return_url:"http://super-duper.shopifyapps.com"

The URL where the merchant is redirected after accepting the charge.

recurring_application_charge.test:true

Whether the application charge is a test transaction. Valid values: `true`,`null`.

Trying to create a charge without a price and name will return an error

Request body

recurring_application_charge

Recurring_application_charge resource**Recurring_application_charge resource**

Show recurring_application_charge properties

recurring_application_charge.name:""

The name of the recurring application charge.

Was this section helpful?

YesNo

post

## /admin/api/2026-01/recurring_application_charges.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{"recurring_application_charge":{"name":"Super Duper Plan","price":10.0,"return_url":"http://super-duper.shopifyapps.com","trial_days":5}}' \

-X POST "https://your-development-store.myshopify.com/admin/api/2026-01/recurring_application_charges.json" \

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

HTTP/1.1 201 Created

{

"recurring_application_charge": {

"id": 1029266969,

"name": "Super Duper Plan",

"price": "10.00",

"billing_on": null,

"status": "pending",

"created_at": "2026-01-09T17:29:20-05:00",

"updated_at": "2026-01-09T17:29:20-05:00",

"activated_on": null,

"return_url": "http://super-duper.shopifyapps.com/",

"test": null,

"cancelled_on": null,

"trial_days": 5,

"trial_ends_on": null,

"api_client_id": 755357713,

"decorated_return_url": "http://super-duper.shopifyapps.com/?charge_id=1029266969",

"confirmation_url": "https://jsmith.myshopify.com/admin/charges/755357713/1029266969/RecurringApplicationCharge/confirm_recurring_application_charge?signature=BAh7BzoHaWRpBBleWT06EmF1dG9fYWN0aXZhdGVU--72b5defba12e4983c745d1f804ece526ee1251db",

"currency": "USD"

}

}

### examples

  * #### Create a new charge with a trial period. The trial period will go into effect at the time the recurring charge is activated.

#####

        curl -d '{"recurring_application_charge":{"name":"Super Duper Plan","price":10.0,"return_url":"http://super-duper.shopifyapps.com","trial_days":5}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/recurring_application_charges.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const recurring_application_charge = new admin.rest.resources.RecurringApplicationCharge({session: session});

        recurring_application_charge.name = "Super Duper Plan";
        recurring_application_charge.price = 10.0;
        recurring_application_charge.return_url = "http://super-duper.shopifyapps.com";
        recurring_application_charge.trial_days = 5;
        await recurring_application_charge.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        recurring_application_charge = ShopifyAPI::RecurringApplicationCharge.new(session: test_session)
        recurring_application_charge.name = "Super Duper Plan"
        recurring_application_charge.price = 10.0
        recurring_application_charge.return_url = "http://super-duper.shopifyapps.com"
        recurring_application_charge.trial_days = 5
        recurring_application_charge.save!

#####

        // Session is built by the OAuth process

        const recurring_application_charge = new shopify.rest.RecurringApplicationCharge({session: session});
        recurring_application_charge.name = "Super Duper Plan";
        recurring_application_charge.price = 10.0;
        recurring_application_charge.return_url = "http://super-duper.shopifyapps.com";
        recurring_application_charge.trial_days = 5;
        await recurring_application_charge.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"recurring_application_charge":{"id":1029266969,"name":"Super Duper Plan","price":"10.00","billing_on":null,"status":"pending","created_at":"2026-01-09T17:29:20-05:00","updated_at":"2026-01-09T17:29:20-05:00","activated_on":null,"return_url":"http://super-duper.shopifyapps.com/","test":null,"cancelled_on":null,"trial_days":5,"trial_ends_on":null,"api_client_id":755357713,"decorated_return_url":"http://super-duper.shopifyapps.com/?charge_id=1029266969","confirmation_url":"https://jsmith.myshopify.com/admin/charges/755357713/1029266969/RecurringApplicationCharge/confirm_recurring_application_charge?signature=BAh7BzoHaWRpBBleWT06EmF1dG9fYWN0aXZhdGVU--72b5defba12e4983c745d1f804ece526ee1251db","currency":"USD"}}

  * #### Create a new charge with terms and a capped amount

#####

        curl -d '{"recurring_application_charge":{"name":"Super Duper Plan","price":10.0,"return_url":"http://super-duper.shopifyapps.com","capped_amount":100,"terms":"$1 for 1000 emails"}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/recurring_application_charges.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const recurring_application_charge = new admin.rest.resources.RecurringApplicationCharge({session: session});

        recurring_application_charge.name = "Super Duper Plan";
        recurring_application_charge.price = 10.0;
        recurring_application_charge.return_url = "http://super-duper.shopifyapps.com";
        recurring_application_charge.capped_amount = 100;
        recurring_application_charge.terms = "$1 for 1000 emails";
        await recurring_application_charge.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        recurring_application_charge = ShopifyAPI::RecurringApplicationCharge.new(session: test_session)
        recurring_application_charge.name = "Super Duper Plan"
        recurring_application_charge.price = 10.0
        recurring_application_charge.return_url = "http://super-duper.shopifyapps.com"
        recurring_application_charge.capped_amount = 100
        recurring_application_charge.terms = "$1 for 1000 emails"
        recurring_application_charge.save!

#####

        // Session is built by the OAuth process

        const recurring_application_charge = new shopify.rest.RecurringApplicationCharge({session: session});
        recurring_application_charge.name = "Super Duper Plan";
        recurring_application_charge.price = 10.0;
        recurring_application_charge.return_url = "http://super-duper.shopifyapps.com";
        recurring_application_charge.capped_amount = 100;
        recurring_application_charge.terms = "$1 for 1000 emails";
        await recurring_application_charge.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"recurring_application_charge":{"id":1029266974,"name":"Super Duper Plan","price":"10.00","billing_on":null,"status":"pending","created_at":"2026-01-09T17:29:33-05:00","updated_at":"2026-01-09T17:29:33-05:00","activated_on":null,"return_url":"http://super-duper.shopifyapps.com/","test":null,"cancelled_on":null,"trial_days":0,"trial_ends_on":null,"api_client_id":755357713,"decorated_return_url":"http://super-duper.shopifyapps.com/?charge_id=1029266974","capped_amount":"100.00","balance_used":0,"balance_remaining":"100.00","risk_level":0,"confirmation_url":"https://jsmith.myshopify.com/admin/charges/755357713/1029266974/RecurringApplicationCharge/confirm_recurring_application_charge?signature=BAh7BzoHaWRpBB5eWT06EmF1dG9fYWN0aXZhdGVU--ebccb29d40543001f606a14719fd904bde12fc9e","currency":"USD"}}

  * #### Create a recurring application charge

#####

        curl -d '{"recurring_application_charge":{"name":"Super Duper Plan","price":10.0,"return_url":"http://super-duper.shopifyapps.com"}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/recurring_application_charges.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const recurring_application_charge = new admin.rest.resources.RecurringApplicationCharge({session: session});

        recurring_application_charge.name = "Super Duper Plan";
        recurring_application_charge.price = 10.0;
        recurring_application_charge.return_url = "http://super-duper.shopifyapps.com";
        await recurring_application_charge.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        recurring_application_charge = ShopifyAPI::RecurringApplicationCharge.new(session: test_session)
        recurring_application_charge.name = "Super Duper Plan"
        recurring_application_charge.price = 10.0
        recurring_application_charge.return_url = "http://super-duper.shopifyapps.com"
        recurring_application_charge.save!

#####

        // Session is built by the OAuth process

        const recurring_application_charge = new shopify.rest.RecurringApplicationCharge({session: session});
        recurring_application_charge.name = "Super Duper Plan";
        recurring_application_charge.price = 10.0;
        recurring_application_charge.return_url = "http://super-duper.shopifyapps.com";
        await recurring_application_charge.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"recurring_application_charge":{"id":1029266972,"name":"Super Duper Plan","price":"10.00","billing_on":null,"status":"pending","created_at":"2026-01-09T17:29:29-05:00","updated_at":"2026-01-09T17:29:29-05:00","activated_on":null,"return_url":"http://super-duper.shopifyapps.com/","test":null,"cancelled_on":null,"trial_days":0,"trial_ends_on":null,"api_client_id":755357713,"decorated_return_url":"http://super-duper.shopifyapps.com/?charge_id=1029266972","confirmation_url":"https://jsmith.myshopify.com/admin/charges/755357713/1029266972/RecurringApplicationCharge/confirm_recurring_application_charge?signature=BAh7BzoHaWRpBBxeWT06EmF1dG9fYWN0aXZhdGVU--8499c501a60c28d107f614b9ba8fa347638d8175","currency":"USD"}}

  * #### Create a recurring test charge that will not cause a credit card to be charged

#####

        curl -d '{"recurring_application_charge":{"name":"Super Duper Plan","price":10.0,"return_url":"http://super-duper.shopifyapps.com","test":true}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/recurring_application_charges.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const recurring_application_charge = new admin.rest.resources.RecurringApplicationCharge({session: session});

        recurring_application_charge.name = "Super Duper Plan";
        recurring_application_charge.price = 10.0;
        recurring_application_charge.return_url = "http://super-duper.shopifyapps.com";
        recurring_application_charge.test = true;
        await recurring_application_charge.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        recurring_application_charge = ShopifyAPI::RecurringApplicationCharge.new(session: test_session)
        recurring_application_charge.name = "Super Duper Plan"
        recurring_application_charge.price = 10.0
        recurring_application_charge.return_url = "http://super-duper.shopifyapps.com"
        recurring_application_charge.test = true
        recurring_application_charge.save!

#####

        // Session is built by the OAuth process

        const recurring_application_charge = new shopify.rest.RecurringApplicationCharge({session: session});
        recurring_application_charge.name = "Super Duper Plan";
        recurring_application_charge.price = 10.0;
        recurring_application_charge.return_url = "http://super-duper.shopifyapps.com";
        recurring_application_charge.test = true;
        await recurring_application_charge.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"recurring_application_charge":{"id":1029266971,"name":"Super Duper Plan","price":"10.00","billing_on":null,"status":"pending","created_at":"2026-01-09T17:29:28-05:00","updated_at":"2026-01-09T17:29:28-05:00","activated_on":null,"return_url":"http://super-duper.shopifyapps.com/","test":true,"cancelled_on":null,"trial_days":0,"trial_ends_on":null,"api_client_id":755357713,"decorated_return_url":"http://super-duper.shopifyapps.com/?charge_id=1029266971","confirmation_url":"https://jsmith.myshopify.com/admin/charges/755357713/1029266971/RecurringApplicationCharge/confirm_recurring_application_charge?signature=BAh7BzoHaWRpBBteWT06EmF1dG9fYWN0aXZhdGVU--ac5f53ebaa0ac3c4c219ec0f6fbeda0938ee815c","currency":"USD"}}

  * #### Trying to create a charge without a price and name will return an error

#####

        curl -d '{"recurring_application_charge":{"name":""}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/recurring_application_charges.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const recurring_application_charge = new admin.rest.resources.RecurringApplicationCharge({session: session});

        recurring_application_charge.name = "";
        await recurring_application_charge.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        recurring_application_charge = ShopifyAPI::RecurringApplicationCharge.new(session: test_session)
        recurring_application_charge.name = ""
        recurring_application_charge.save!

#####

        // Session is built by the OAuth process

        const recurring_application_charge = new shopify.rest.RecurringApplicationCharge({session: session});
        recurring_application_charge.name = "";
        await recurring_application_charge.save({
          update: true,
        });

#### response

        HTTP/1.1 422 Unprocessable Entity{"errors":{"name":["can't be blank"],"price":["must be greater than zero"]}}


* * *

##

[Anchor to GET request, Retrieves a list of recurring application charges](/docs/api/admin-rest/latest/resources/recurringapplicationcharge#get-recurring-application-charges)

get

Retrieves a list of recurring application charges

[currentAppInstallation](/docs/api/admin-graphql/latest/queries/currentAppInstallation?example=retrieves-a-list-of-recurring-application-charges)

Retrieves a list of recurring application charges

###

[Anchor to Parameters of Retrieves a list of recurring application charges](/docs/api/admin-rest/latest/resources/recurringapplicationcharge#get-recurring-application-charges-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

fields

A comma-separated list of fields to include in the response.

* * *

since_id

Restrict results to after the specified ID.

* * *

Was this section helpful?

YesNo

###

[Anchor to get-recurring-application-charges-examples](/docs/api/admin-rest/latest/resources/recurringapplicationcharge#get-recurring-application-charges-examples)Examples

Retrieve all recurring application charges

Retrieve all recurring charges since a specified ID

Query parameters

since_id=455696195

Restrict results to after the specified ID.

Was this section helpful?

YesNo

get

## /admin/api/2026-01/recurring_application_charges.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/recurring_application_charges.json" \

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

"recurring_application_charges": [

{

"id": 455696195,

"name": "Super Mega Plan",

"price": "15.00",

"billing_on": "2026-01-09",

"status": "accepted",

"created_at": "2026-01-09T17:04:11-05:00",

"updated_at": "2026-01-09T17:29:26-05:00",

"activated_on": null,

"return_url": "http://yourapp.example.org",

"test": null,

"cancelled_on": null,

"trial_days": 0,

"trial_ends_on": null,

"api_client_id": 755357713,

"decorated_return_url": "http://yourapp.example.org?charge_id=455696195",

"currency": "USD"

}

]

}

### examples

  * #### Retrieve all recurring application charges

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/recurring_application_charges.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.RecurringApplicationCharge.all({
          session: session,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::RecurringApplicationCharge.all(
          session: test_session,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.RecurringApplicationCharge.all({
          session: session,
        });

#### response

        HTTP/1.1 200 OK{"recurring_application_charges":[{"id":455696195,"name":"Super Mega Plan","price":"15.00","billing_on":"2026-01-09","status":"accepted","created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:29:26-05:00","activated_on":null,"return_url":"http://yourapp.example.org","test":null,"cancelled_on":null,"trial_days":0,"trial_ends_on":null,"api_client_id":755357713,"decorated_return_url":"http://yourapp.example.org?charge_id=455696195","currency":"USD"}]}

  * #### Retrieve all recurring charges since a specified ID

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/recurring_application_charges.json?since_id=455696195" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.RecurringApplicationCharge.all({
          session: session,
          since_id: "455696195",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::RecurringApplicationCharge.all(
          session: test_session,
          since_id: "455696195",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.RecurringApplicationCharge.all({
          session: session,
          since_id: "455696195",
        });

#### response

        HTTP/1.1 200 OK{"recurring_application_charges":[{"id":1029266973,"name":"Super Duper Plan","price":"10.00","billing_on":null,"status":"pending","created_at":"2026-01-09T17:29:31-05:00","updated_at":"2026-01-09T17:29:31-05:00","activated_on":null,"return_url":"http://super-duper.shopifyapps.com/","test":null,"cancelled_on":null,"trial_days":0,"trial_ends_on":null,"api_client_id":755357713,"decorated_return_url":"http://super-duper.shopifyapps.com/?charge_id=1029266973","confirmation_url":"https://jsmith.myshopify.com/admin/charges/755357713/1029266973/RecurringApplicationCharge/confirm_recurring_application_charge?signature=BAh7BzoHaWRpBB1eWT06EmF1dG9fYWN0aXZhdGVU--5ce31ca14b289bb31eb4849490ed1c711fbdd994","currency":"USD"}]}


* * *

##

[Anchor to GET request, Retrieves a single charge](/docs/api/admin-rest/latest/resources/recurringapplicationcharge#get-recurring-application-charges-recurring-application-charge-id)

get

Retrieves a single charge

Retrieves a single charge

###

[Anchor to Parameters of Retrieves a single charge](/docs/api/admin-rest/latest/resources/recurringapplicationcharge#get-recurring-application-charges-recurring-application-charge-id-parameters)Parameters

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

[Anchor to get-recurring-application-charges-recurring-application-charge-id-examples](/docs/api/admin-rest/latest/resources/recurringapplicationcharge#get-recurring-application-charges-recurring-application-charge-id-examples)Examples

Retrieve a single charge

Path parameters

recurring_application_charge_id=455696195

string**string**

required**required**

Was this section helpful?

YesNo

get

## /admin/api/2026-01/recurring_application_charges/455696195.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/recurring_application_charges/455696195.json" \

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

"recurring_application_charge": {

"id": 455696195,

"name": "Super Mega Plan",

"price": "15.00",

"billing_on": "2026-01-09",

"status": "pending",

"created_at": "2026-01-09T17:04:11-05:00",

"updated_at": "2026-01-09T17:04:11-05:00",

"activated_on": null,

"return_url": "http://yourapp.example.org",

"test": null,

"cancelled_on": null,

"trial_days": 0,

"trial_ends_on": null,

"api_client_id": 755357713,

"decorated_return_url": "http://yourapp.example.org?charge_id=455696195",

"confirmation_url": "https://jsmith.myshopify.com/admin/charges/755357713/455696195/RecurringApplicationCharge/confirm_recurring_application_charge?signature=BAh7BzoHaWRpBENfKRs6EmF1dG9fYWN0aXZhdGVU--b5f90d04779cc5242b396e4054f2e650c5dace1c",

"currency": "USD"

}

}

### examples

  * #### Retrieve a single charge

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/recurring_application_charges/455696195.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.RecurringApplicationCharge.find({
          session: session,
          id: 455696195,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::RecurringApplicationCharge.find(
          session: test_session,
          id: 455696195,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.RecurringApplicationCharge.find({
          session: session,
          id: 455696195,
        });

#### response

        HTTP/1.1 200 OK{"recurring_application_charge":{"id":455696195,"name":"Super Mega Plan","price":"15.00","billing_on":"2026-01-09","status":"pending","created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","activated_on":null,"return_url":"http://yourapp.example.org","test":null,"cancelled_on":null,"trial_days":0,"trial_ends_on":null,"api_client_id":755357713,"decorated_return_url":"http://yourapp.example.org?charge_id=455696195","confirmation_url":"https://jsmith.myshopify.com/admin/charges/755357713/455696195/RecurringApplicationCharge/confirm_recurring_application_charge?signature=BAh7BzoHaWRpBENfKRs6EmF1dG9fYWN0aXZhdGVU--b5f90d04779cc5242b396e4054f2e650c5dace1c","currency":"USD"}}


* * *

##

[Anchor to PUT request, Updates the capped amount of a recurring application charge](/docs/api/admin-rest/latest/resources/recurringapplicationcharge#put-recurring-application-charges-recurring-application-charge-id-customize?recurring-application-charge\[capped-amount\]=200)

put

Updates the capped amount of a recurring application charge

[appSubscriptionLineItemUpdate](/docs/api/admin-graphql/latest/mutations/appSubscriptionLineItemUpdate?example=updates-the-capped-amount-of-a-recurring-application-charge)

Updates the capped amount of an active recurring application charge. Note that you cannot use this endpoint to update any other proprty on a recurring application charge or the capped amount on an [Annual subscription](https://shopify.dev/apps/billing/subscriptions/annual#limitations).

###

[Anchor to Parameters of Updates the capped amount of a recurring application charge](/docs/api/admin-rest/latest/resources/recurringapplicationcharge#put-recurring-application-charges-recurring-application-charge-id-customize?recurring-application-charge\[capped-amount\]=200-parameters)Parameters

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

[Anchor to put-recurring-application-charges-recurring-application-charge-id-customize?recurring-application-charge[capped-amount]=200-examples](/docs/api/admin-rest/latest/resources/recurringapplicationcharge#put-recurring-application-charges-recurring-application-charge-id-customize?recurring-application-charge\[capped-amount\]=200-examples)Examples

Increase the capped amount for a shop

Query parameters

Was this section helpful?

YesNo

put

## /admin/api/2026-01/recurring_application_charges/455696195/customize.json?recurring_application_charge[capped_amount]=200

cURLRemixRubyNode.js

Copy

9

1

2

curl -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/recurring_application_charges/455696195/customize.json?recurring_application_charge%5Bcapped_amount%5D=200" \

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

HTTP/1.1 200 OK

{

"recurring_application_charge": {

"id": 455696195,

"name": "Super Mega Plan",

"price": "15.00",

"billing_on": null,

"status": "active",

"created_at": "2026-01-09T17:04:11-05:00",

"updated_at": "2026-01-09T17:29:24-05:00",

"activated_on": "2026-01-09",

"return_url": "http://yourapp.example.org",

"test": null,

"cancelled_on": null,

"trial_days": 0,

"trial_ends_on": "2026-01-09",

"api_client_id": 755357713,

"decorated_return_url": "http://yourapp.example.org?charge_id=455696195",

"capped_amount": "100.00",

"balance_used": "0.0",

"balance_remaining": "100.00",

"risk_level": 0,

"update_capped_amount_url": "https://jsmith.myshopify.com/admin/charges/755357713/455696195/RecurringApplicationCharge/confirm_update_capped_amount?signature=BAh7BzoHaWRpBENfKRs6EmF1dG9fYWN0aXZhdGVG--c6b5cedaf1aa983d52c58d508f10e438a59e45e8",

"currency": "USD"

}

}

### examples

  * #### Increase the capped amount for a shop

#####

        curl -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/recurring_application_charges/455696195/customize.json?recurring_application_charge%5Bcapped_amount%5D=200" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        const { admin, session } = await authenticate.admin(request);

        const recurring_application_charge = new admin.rest.resources.RecurringApplicationCharge({session: session});

        recurring_application_charge.id = 455696195;
        await recurring_application_charge.customize({
          recurring_application_charge: {"capped_amount": "200"},
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        recurring_application_charge = ShopifyAPI::RecurringApplicationCharge.new(session: test_session)
        recurring_application_charge.id = 455696195
        recurring_application_charge.customize(
          session: test_session,
          recurring_application_charge: {"capped_amount" => "200"},
        )

#####

        // Session is built by the OAuth process

        const recurring_application_charge = new shopify.rest.RecurringApplicationCharge({session: session});
        recurring_application_charge.id = 455696195;
        await recurring_application_charge.customize({
          recurring_application_charge: {"capped_amount": "200"},
        });

#### response

        HTTP/1.1 200 OK{"recurring_application_charge":{"id":455696195,"name":"Super Mega Plan","price":"15.00","billing_on":null,"status":"active","created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:29:24-05:00","activated_on":"2026-01-09","return_url":"http://yourapp.example.org","test":null,"cancelled_on":null,"trial_days":0,"trial_ends_on":"2026-01-09","api_client_id":755357713,"decorated_return_url":"http://yourapp.example.org?charge_id=455696195","capped_amount":"100.00","balance_used":"0.0","balance_remaining":"100.00","risk_level":0,"update_capped_amount_url":"https://jsmith.myshopify.com/admin/charges/755357713/455696195/RecurringApplicationCharge/confirm_update_capped_amount?signature=BAh7BzoHaWRpBENfKRs6EmF1dG9fYWN0aXZhdGVG--c6b5cedaf1aa983d52c58d508f10e438a59e45e8","currency":"USD"}}


* * *

##

[Anchor to DELETE request, Cancels a recurring application charge](/docs/api/admin-rest/latest/resources/recurringapplicationcharge#delete-recurring-application-charges-recurring-application-charge-id)

del

Cancels a recurring application charge

[appSubscriptionCancel](/docs/api/admin-graphql/latest/mutations/appSubscriptionCancel?example=cancels-a-recurring-application-charge)

Cancels a recurring application charge

###

[Anchor to Parameters of Cancels a recurring application charge](/docs/api/admin-rest/latest/resources/recurringapplicationcharge#delete-recurring-application-charges-recurring-application-charge-id-parameters)Parameters

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

[Anchor to delete-recurring-application-charges-recurring-application-charge-id-examples](/docs/api/admin-rest/latest/resources/recurringapplicationcharge#delete-recurring-application-charges-recurring-application-charge-id-examples)Examples

Cancel the current recurring charge for a shop

Path parameters

recurring_application_charge_id=455696195

string**string**

required**required**

Was this section helpful?

YesNo

del

## /admin/api/2026-01/recurring_application_charges/455696195.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X DELETE "https://your-development-store.myshopify.com/admin/api/2026-01/recurring_application_charges/455696195.json" \

-H "X-Shopify-Access-Token: {access_token}"

{}

## Response

JSON

9

1

HTTP/1.1 200 OK

### examples

  * #### Cancel the current recurring charge for a shop

#####

        curl -X DELETE "https://your-development-store.myshopify.com/admin/api/2026-01/recurring_application_charges/455696195.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.RecurringApplicationCharge.delete({
          session: session,
          id: 455696195,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::RecurringApplicationCharge.delete(
          session: test_session,
          id: 455696195,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.RecurringApplicationCharge.delete({
          session: session,
          id: 455696195,
        });

#### response

        HTTP/1.1 200 OK