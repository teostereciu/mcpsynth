# ApplicationCharge

*Source: https://shopify.dev/docs/api/admin-rest/2026-01/resources/applicationcharge*

---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04

2026-01latest

# ApplicationCharge

Ask assistant

The ApplicationCharge resource facilitates one-time charges. This type of charge is recommended for apps that aren’t billed on a recurring basis. You can create an application charge by sending a request with the name the charge should appear under, the price your app is charging, and a return URL where Shopify redirects the merchant after the charge is accepted. After you've created the charge, redirect the merchant to the confirmation URL returned by Shopify. If the charge is declined, then Shopify redirects the merchant and provides a notification message that the app charge was declined.

Note

For testing purposes you can include `"test": true` when creating the charge. This prevents the credit card from being charged. Test shops and demo shops can't be charged.

**Note:**

For testing purposes you can include `"test": true` when creating the charge. This prevents the credit card from being charged. Test shops and demo shops can't be charged.

Was this section helpful?

YesNo

#

## Endpoints

  * [post/admin/api/latest/application_charges.json](/docs/api/admin-rest/latest/resources/applicationcharge#post-application-charges)

Creates an application charge

[appPurchaseOneTimeCreate](/docs/api/admin-graphql/latest/mutations/appPurchaseOneTimeCreate?example=creates-an-application-charge)

  * [get/admin/api/latest/application_charges.json](/docs/api/admin-rest/latest/resources/applicationcharge#get-application-charges)

Retrieves a list of application charges

[currentAppInstallation](/docs/api/admin-graphql/latest/queries/currentAppInstallation?example=retrieves-a-list-of-application-charges)

  * [get/admin/api/latest/application_charges/{application_charge_id}.json](/docs/api/admin-rest/latest/resources/applicationcharge#get-application-charges-application-charge-id)

Retrieves an application charge


* * *

[Anchor to ](/docs/api/admin-rest/latest/resources/applicationcharge#resource-object)

## The ApplicationCharge resource

[Anchor to ](/docs/api/admin-rest/latest/resources/applicationcharge#resource-object-properties)

### Properties

* * *

confirmation_url

->[confirmationUrl](/docs/api/admin-graphql/latest/objects/AppPurchaseOneTimeCreatePayload#field-AppPurchaseOneTimeCreatePayload.fields.confirmationUrl)

The URL where the merchant accepts or declines the application charge.

* * *

created_at

->[createdAt](/docs/api/admin-graphql/latest/objects/AppPurchaseOneTime#field-AppPurchaseOneTime.fields.createdAt)

The date and time ([ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format) when the application charge was created.

* * *

id

->[id](/docs/api/admin-graphql/latest/objects/AppPurchaseOneTime#field-AppPurchaseOneTime.fields.id)

The ID of the application charge.

* * *

name

->[name](/docs/api/admin-graphql/latest/objects/AppPurchaseOneTime#field-AppPurchaseOneTime.fields.name)

The application charge name.

* * *

price

->[price](/docs/api/admin-graphql/latest/objects/AppPurchaseOneTime#field-AppPurchaseOneTime.fields.price)

The price of the application charge. The minimum price is 0.50, and maximum price is 10,000.

* * *

return_url

The URL where the merchant is redirected after accepting a charge.

* * *

status

->[status](/docs/api/admin-graphql/latest/objects/AppPurchaseOneTime#field-AppPurchaseOneTime.fields.status)

The status of the application charge. Valid values:

Show status properties

  * **pending** : The application charge is pending approval by the merchant.
  * **accepted** : **Removed in version 2021-01**. The application charge has been accepted by the merchant and is ready to be activated by the app. At this point it will appear on the merchant's invoice. As of API version 2021-01, when a merchant accepts a charge, the charge immediately transitions from `pending` to `active`.
  * **active** : The application charge has been activated by the app and will be paid out to the Partner.
  * **declined** : The application charge was declined by the merchant.
  * **expired** : The application charge was not accepted within 2 days of being created.


* * *

test

->[test](/docs/api/admin-graphql/latest/objects/AppPurchaseOneTime#field-AppPurchaseOneTime.fields.test)

Whether the application charge is a test transaction. Valid values:`true`,`null`.

* * *

updated_at

The date and time ([ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format) when the charge was last updated.

* * *

currency

->[price](/docs/api/admin-graphql/latest/objects/AppPurchaseOneTime#field-AppPurchaseOneTime.fields.price)

The currency of the price of the application charge.

* * *

Was this section helpful?

YesNo

{}

## The ApplicationCharge resource

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

"confirmation_url": "https://jsmith.myshopify.com/admin/charges/confirm_application_charge?id=1012637313&signature=BAhpBIGeWzw%3D--17779c1efb4688e9cfa653a3245f923b4f1eb140",

"created_at": "2013-06-27T08:48:27-04:00",

"id": 675931192,

"name": "Super Duper Expensive action",

"price": "100.00",

"return_url": "http://super-duper.shopifyapps.com",

"status": "accepted",

"test": null,

"updated_at": "2013-06-27T08:48:27-04:00",

"currency": "USD"

}

* * *

##

[Anchor to POST request, Creates an application charge](/docs/api/admin-rest/latest/resources/applicationcharge#post-application-charges)

post

Creates an application charge

[appPurchaseOneTimeCreate](/docs/api/admin-graphql/latest/mutations/appPurchaseOneTimeCreate?example=creates-an-application-charge)

Creates an application charge

###

[Anchor to Parameters of Creates an application charge](/docs/api/admin-rest/latest/resources/applicationcharge#post-application-charges-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to post-application-charges-examples](/docs/api/admin-rest/latest/resources/applicationcharge#post-application-charges-examples)Examples

Create a test charge that will not cause a credit card to be charged

Request body

application_charge

Application_charge resource**Application_charge resource**

Show application_charge properties

application_charge.name:"Super Duper Expensive action"

The application charge name.

application_charge.price:100

The price of the application charge. The minimum price is 0.50, and maximum price is 10,000.

application_charge.return_url:"http://super-duper.shopifyapps.com"

The URL where the merchant is redirected after accepting a charge.

application_charge.test:true

Whether the application charge is a test transaction. Valid values:`true`,`null`.

Create an application charge

Request body

application_charge

Application_charge resource**Application_charge resource**

Show application_charge properties

application_charge.name:"Super Duper Expensive action"

The application charge name.

application_charge.price:100

The price of the application charge. The minimum price is 0.50, and maximum price is 10,000.

application_charge.return_url:"http://super-duper.shopifyapps.com"

The URL where the merchant is redirected after accepting a charge.

Trying to create a charge with a price less than 0.50 will return an error

Request body

application_charge

Application_charge resource**Application_charge resource**

Show application_charge properties

application_charge.name:"Super Duper Expensive action"

The application charge name.

application_charge.price:0.4

The price of the application charge. The minimum price is 0.50, and maximum price is 10,000.

application_charge.return_url:"http://super-duper.shopifyapps.com"

The URL where the merchant is redirected after accepting a charge.

Trying to create a charge without a price or name will return an error

Request body

application_charge

Application_charge resource**Application_charge resource**

Show application_charge properties

application_charge.name:""

The application charge name.

Was this section helpful?

YesNo

post

## /admin/api/2026-01/application_charges.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{"application_charge":{"name":"Super Duper Expensive action","price":100.0,"return_url":"http://super-duper.shopifyapps.com","test":true}}' \

-X POST "https://your-development-store.myshopify.com/admin/api/2026-01/application_charges.json" \

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

HTTP/1.1 201 Created

{

"application_charge": {

"id": 1017262368,

"name": "Super Duper Expensive action",

"api_client_id": 755357713,

"price": "100.00",

"status": "pending",

"return_url": "http://super-duper.shopifyapps.com/",

"test": true,

"created_at": "2026-01-09T19:35:11-05:00",

"updated_at": "2026-01-09T19:35:11-05:00",

"currency": "USD",

"charge_type": null,

"decorated_return_url": "http://super-duper.shopifyapps.com/?charge_id=1017262368",

"confirmation_url": "https://jsmith.myshopify.com/admin/charges/755357713/1017262368/ApplicationCharge/confirm_application_charge?signature=BAh7BzoHaWRpBCAxojw6EmF1dG9fYWN0aXZhdGVU--cd29373fcaa37cd8a63f482b7ba4ff83cd6fe538"

}

}

### examples

  * #### Create a test charge that will not cause a credit card to be charged

#####

        curl -d '{"application_charge":{"name":"Super Duper Expensive action","price":100.0,"return_url":"http://super-duper.shopifyapps.com","test":true}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/application_charges.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const application_charge = new admin.rest.resources.ApplicationCharge({session: session});

        application_charge.name = "Super Duper Expensive action";
        application_charge.price = 100.0;
        application_charge.return_url = "http://super-duper.shopifyapps.com";
        application_charge.test = true;
        await application_charge.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        application_charge = ShopifyAPI::ApplicationCharge.new(session: test_session)
        application_charge.name = "Super Duper Expensive action"
        application_charge.price = 100.0
        application_charge.return_url = "http://super-duper.shopifyapps.com"
        application_charge.test = true
        application_charge.save!

#####

        // Session is built by the OAuth process

        const application_charge = new shopify.rest.ApplicationCharge({session: session});
        application_charge.name = "Super Duper Expensive action";
        application_charge.price = 100.0;
        application_charge.return_url = "http://super-duper.shopifyapps.com";
        application_charge.test = true;
        await application_charge.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"application_charge":{"id":1017262368,"name":"Super Duper Expensive action","api_client_id":755357713,"price":"100.00","status":"pending","return_url":"http://super-duper.shopifyapps.com/","test":true,"created_at":"2026-01-09T19:35:11-05:00","updated_at":"2026-01-09T19:35:11-05:00","currency":"USD","charge_type":null,"decorated_return_url":"http://super-duper.shopifyapps.com/?charge_id=1017262368","confirmation_url":"https://jsmith.myshopify.com/admin/charges/755357713/1017262368/ApplicationCharge/confirm_application_charge?signature=BAh7BzoHaWRpBCAxojw6EmF1dG9fYWN0aXZhdGVU--cd29373fcaa37cd8a63f482b7ba4ff83cd6fe538"}}

  * #### Create an application charge

#####

        curl -d '{"application_charge":{"name":"Super Duper Expensive action","price":100.0,"return_url":"http://super-duper.shopifyapps.com"}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/application_charges.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const application_charge = new admin.rest.resources.ApplicationCharge({session: session});

        application_charge.name = "Super Duper Expensive action";
        application_charge.price = 100.0;
        application_charge.return_url = "http://super-duper.shopifyapps.com";
        await application_charge.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        application_charge = ShopifyAPI::ApplicationCharge.new(session: test_session)
        application_charge.name = "Super Duper Expensive action"
        application_charge.price = 100.0
        application_charge.return_url = "http://super-duper.shopifyapps.com"
        application_charge.save!

#####

        // Session is built by the OAuth process

        const application_charge = new shopify.rest.ApplicationCharge({session: session});
        application_charge.name = "Super Duper Expensive action";
        application_charge.price = 100.0;
        application_charge.return_url = "http://super-duper.shopifyapps.com";
        await application_charge.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"application_charge":{"id":1017262367,"name":"Super Duper Expensive action","api_client_id":755357713,"price":"100.00","status":"pending","return_url":"http://super-duper.shopifyapps.com/","test":null,"created_at":"2026-01-09T19:35:08-05:00","updated_at":"2026-01-09T19:35:08-05:00","currency":"USD","charge_type":null,"decorated_return_url":"http://super-duper.shopifyapps.com/?charge_id=1017262367","confirmation_url":"https://jsmith.myshopify.com/admin/charges/755357713/1017262367/ApplicationCharge/confirm_application_charge?signature=BAh7BzoHaWRpBB8xojw6EmF1dG9fYWN0aXZhdGVU--2e387b390eba81ff1a159f824f79ec21b8fdb2fc"}}

  * #### Trying to create a charge with a price less than 0.50 will return an error

#####

        curl -d '{"application_charge":{"name":"Super Duper Expensive action","price":0.4,"return_url":"http://super-duper.shopifyapps.com"}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/application_charges.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const application_charge = new admin.rest.resources.ApplicationCharge({session: session});

        application_charge.name = "Super Duper Expensive action";
        application_charge.price = 0.4;
        application_charge.return_url = "http://super-duper.shopifyapps.com";
        await application_charge.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        application_charge = ShopifyAPI::ApplicationCharge.new(session: test_session)
        application_charge.name = "Super Duper Expensive action"
        application_charge.price = 0.4
        application_charge.return_url = "http://super-duper.shopifyapps.com"
        application_charge.save!

#####

        // Session is built by the OAuth process

        const application_charge = new shopify.rest.ApplicationCharge({session: session});
        application_charge.name = "Super Duper Expensive action";
        application_charge.price = 0.4;
        application_charge.return_url = "http://super-duper.shopifyapps.com";
        await application_charge.save({
          update: true,
        });

#### response

        HTTP/1.1 422 Unprocessable Entity{"errors":{"price":["must be greater than or equal to the equivalent of $0.50 USD"]}}

  * #### Trying to create a charge without a price or name will return an error

#####

        curl -d '{"application_charge":{"name":""}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/application_charges.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const application_charge = new admin.rest.resources.ApplicationCharge({session: session});

        application_charge.name = "";
        await application_charge.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        application_charge = ShopifyAPI::ApplicationCharge.new(session: test_session)
        application_charge.name = ""
        application_charge.save!

#####

        // Session is built by the OAuth process

        const application_charge = new shopify.rest.ApplicationCharge({session: session});
        application_charge.name = "";
        await application_charge.save({
          update: true,
        });

#### response

        HTTP/1.1 422 Unprocessable Entity{"errors":{"name":["can't be blank"],"price":["must be greater than or equal to the equivalent of $0.50 USD"]}}


* * *

##

[Anchor to GET request, Retrieves a list of application charges](/docs/api/admin-rest/latest/resources/applicationcharge#get-application-charges)

get

Retrieves a list of application charges

[currentAppInstallation](/docs/api/admin-graphql/latest/queries/currentAppInstallation?example=retrieves-a-list-of-application-charges)

Retrieves a list of application charges

###

[Anchor to Parameters of Retrieves a list of application charges](/docs/api/admin-rest/latest/resources/applicationcharge#get-application-charges-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

fields

A comma-separated list of fields to include in the response.

* * *

after_id

Restrict results to after the specified ID.

* * *

Was this section helpful?

YesNo

###

[Anchor to get-application-charges-examples](/docs/api/admin-rest/latest/resources/applicationcharge#get-application-charges-examples)Examples

Retrieve all application charges

Retrieve all application charges since a specified ID

Query parameters

after_id=556467234

Restrict results to after the specified ID.

Was this section helpful?

YesNo

get

## /admin/api/2026-01/application_charges.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/application_charges.json" \

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

HTTP/1.1 200 OK

{

"application_charges": [

{

"id": 556467234,

"name": "Green theme",

"api_client_id": 755357713,

"price": "120.00",

"status": "accepted",

"return_url": "http://google.com",

"test": null,

"external_id": null,

"created_at": "2026-01-09T17:04:11-05:00",

"updated_at": "2026-01-09T17:04:11-05:00",

"currency": "USD",

"charge_type": "theme",

"decorated_return_url": "http://google.com?charge_id=556467234"

},

{

"id": 675931192,

"name": "iPod Cleaning",

"api_client_id": 755357713,

"price": "5.00",

"status": "accepted",

"return_url": "http://google.com",

"test": null,

"created_at": "2026-01-09T17:04:11-05:00",

"updated_at": "2026-01-09T17:04:11-05:00",

"currency": "USD",

"charge_type": null,

"decorated_return_url": "http://google.com?charge_id=675931192"

},

{

"id": 1017262346,

"name": "Create me a logo",

"api_client_id": 755357713,

"price": "123.00",

"status": "accepted",

"return_url": "http://google.com",

"test": null,

"created_at": "2026-01-09T17:04:11-05:00",

"updated_at": "2026-01-09T17:04:11-05:00",

"currency": "USD",

"charge_type": "brokered_service",

"decorated_return_url": "http://google.com?charge_id=1017262346"

}

]

}

### examples

  * #### Retrieve all application charges

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/application_charges.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.ApplicationCharge.all({
          session: session,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::ApplicationCharge.all(
          session: test_session,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.ApplicationCharge.all({
          session: session,
        });

#### response

        HTTP/1.1 200 OK{"application_charges":[{"id":556467234,"name":"Green theme","api_client_id":755357713,"price":"120.00","status":"accepted","return_url":"http://google.com","test":null,"external_id":null,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","currency":"USD","charge_type":"theme","decorated_return_url":"http://google.com?charge_id=556467234"},{"id":675931192,"name":"iPod Cleaning","api_client_id":755357713,"price":"5.00","status":"accepted","return_url":"http://google.com","test":null,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","currency":"USD","charge_type":null,"decorated_return_url":"http://google.com?charge_id=675931192"},{"id":1017262346,"name":"Create me a logo","api_client_id":755357713,"price":"123.00","status":"accepted","return_url":"http://google.com","test":null,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","currency":"USD","charge_type":"brokered_service","decorated_return_url":"http://google.com?charge_id=1017262346"}]}

  * #### Retrieve all application charges since a specified ID

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/application_charges.json?after_id=556467234" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.ApplicationCharge.all({
          session: session,
          after_id: "556467234",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::ApplicationCharge.all(
          session: test_session,
          after_id: "556467234",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.ApplicationCharge.all({
          session: session,
          after_id: "556467234",
        });

#### response

        HTTP/1.1 200 OK{"application_charges":[{"id":675931192,"name":"iPod Cleaning","api_client_id":755357713,"price":"5.00","status":"accepted","return_url":"http://google.com","test":null,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","currency":"USD","charge_type":null,"decorated_return_url":"http://google.com?charge_id=675931192"},{"id":1017262346,"name":"Create me a logo","api_client_id":755357713,"price":"123.00","status":"accepted","return_url":"http://google.com","test":null,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","currency":"USD","charge_type":"brokered_service","decorated_return_url":"http://google.com?charge_id=1017262346"}]}


* * *

##

[Anchor to GET request, Retrieves an application charge](/docs/api/admin-rest/latest/resources/applicationcharge#get-application-charges-application-charge-id)

get

Retrieves an application charge

Retrieves an application charge

###

[Anchor to Parameters of Retrieves an application charge](/docs/api/admin-rest/latest/resources/applicationcharge#get-application-charges-application-charge-id-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

application_charge_id

string**string**

required**required**

* * *

fields

A comma-separated list of fields to include in the response.

* * *

Was this section helpful?

YesNo

###

[Anchor to get-application-charges-application-charge-id-examples](/docs/api/admin-rest/latest/resources/applicationcharge#get-application-charges-application-charge-id-examples)Examples

Retrieve an application charge

Path parameters

application_charge_id=675931192

string**string**

required**required**

Was this section helpful?

YesNo

get

## /admin/api/2026-01/application_charges/675931192.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/application_charges/675931192.json" \

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

"application_charge": {

"id": 675931192,

"name": "iPod Cleaning",

"api_client_id": 755357713,

"price": "5.00",

"status": "accepted",

"return_url": "http://google.com",

"test": null,

"created_at": "2026-01-09T17:04:11-05:00",

"updated_at": "2026-01-09T17:04:11-05:00",

"currency": "USD",

"charge_type": null,

"decorated_return_url": "http://google.com?charge_id=675931192"

}

}

### examples

  * #### Retrieve an application charge

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/application_charges/675931192.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.ApplicationCharge.find({
          session: session,
          id: 675931192,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::ApplicationCharge.find(
          session: test_session,
          id: 675931192,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.ApplicationCharge.find({
          session: session,
          id: 675931192,
        });

#### response

        HTTP/1.1 200 OK{"application_charge":{"id":675931192,"name":"iPod Cleaning","api_client_id":755357713,"price":"5.00","status":"accepted","return_url":"http://google.com","test":null,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","currency":"USD","charge_type":null,"decorated_return_url":"http://google.com?charge_id=675931192"}}