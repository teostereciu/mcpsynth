# Customer Address

*Source: https://shopify.dev/docs/api/admin-rest/2026-01/resources/customer-address*

---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04

2026-01latest

# Customer Address

Ask assistant

Requires `customers` access scope.

**Requires `customers` access scope.:**

Requires access to [protected customer data](https://shopify.dev/apps/store/data-protection/protected-customer-data).

**Requires access to [protected customer data](https://shopify.dev/apps/store/data-protection/protected-customer-data).:**

The Customer Address resource represents addresses that a customer has added. Each customer can have multiple addresses associated with them.

For more information about the Customer resource, see [_Customer_](/docs/admin-api/rest/reference/customers/customer).

Was this section helpful?

YesNo

#

## Endpoints

  * [post/admin/api/latest/customers/{customer_id}/addresses.json](/docs/api/admin-rest/latest/resources/customer-address#post-customers-customer-id-addresses)

Creates a new address for a customer

[customerUpdate](/docs/api/admin-graphql/latest/mutations/customerUpdate?example=creates-a-new-address-for-a-customer)

  * [get/admin/api/latest/customers/{customer_id}/addresses.json?limit=1](/docs/api/admin-rest/latest/resources/customer-address#get-customers-customer-id-addresses?limit=1)

Retrieves a list of addresses for a customer

[customer](/docs/api/admin-graphql/latest/queries/customer?example=retrieves-a-list-of-addresses-for-a-customer)

  * [get/admin/api/latest/customers/{customer_id}/addresses/{address_id}.json](/docs/api/admin-rest/latest/resources/customer-address#get-customers-customer-id-addresses-address-id)

Retrieves details for a single customer address

[customer](/docs/api/admin-graphql/latest/queries/customer)

  * [put/admin/api/latest/customers/{customer_id}/addresses/{address_id}.json](/docs/api/admin-rest/latest/resources/customer-address#put-customers-customer-id-addresses-address-id)

Updates an existing customer address

[customerUpdateDefaultAddress](/docs/api/admin-graphql/latest/mutations/customerUpdateDefaultAddress?example=updates-an-existing-customer-address)

  * [put/admin/api/latest/customers/{customer_id}/addresses/{address_id}/default.json](/docs/api/admin-rest/latest/resources/customer-address#put-customers-customer-id-addresses-address-id-default)

Sets the default address for a customer

[customerUpdateDefaultAddress](/docs/api/admin-graphql/latest/mutations/customerUpdateDefaultAddress?example=sets-the-default-address-for-a-customer)

  * [put/admin/api/latest/customers/{customer_id}/addresses/set.json?address_ids[]=1053317346&operation=destroy](/docs/api/admin-rest/latest/resources/customer-address#put-customers-customer-id-addresses-set?address-ids\[\]=1053317346&operation=destroy)

Performs bulk operations for multiple customer addresses

[customerUpdate](/docs/api/admin-graphql/latest/mutations/customerUpdate?example=performs-bulk-operations-for-multiple-customer-addresses)

  * [del/admin/api/latest/customers/{customer_id}/addresses/{address_id}.json](/docs/api/admin-rest/latest/resources/customer-address#delete-customers-customer-id-addresses-address-id)

Removes an address from a customer’s address list


* * *

[Anchor to ](/docs/api/admin-rest/latest/resources/customer-address#resource-object)

## The Customer Address resource

[Anchor to ](/docs/api/admin-rest/latest/resources/customer-address#resource-object-properties)

### Properties

* * *

address1

->[address1](/docs/api/admin-graphql/latest/objects/MailingAddress#field-MailingAddress.fields.address1)

The customer's mailing address

* * *

address2

->[address2](/docs/api/admin-graphql/latest/objects/MailingAddress#field-MailingAddress.fields.address2)

An additional field for the customer's mailing address.

* * *

city

->[city](/docs/api/admin-graphql/latest/objects/MailingAddress#field-MailingAddress.fields.city)

The customer's city, town, or village.

* * *

country

->[country](/docs/api/admin-graphql/latest/objects/MailingAddress#field-MailingAddress.fields.country)

The customer's country.

* * *

country_code

read-only**read-only**

->[countryCodeV2](/docs/api/admin-graphql/latest/objects/MailingAddress#field-MailingAddress.fields.countryCodeV2)

The two-letter country code corresponding to the customer's country.

* * *

country_name

->[country](/docs/api/admin-graphql/latest/objects/MailingAddress#field-MailingAddress.fields.country)

The customer’s normalized country name.

* * *

company

->[company](/docs/api/admin-graphql/latest/objects/MailingAddress#field-MailingAddress.fields.company)

The customer’s company.

* * *

customer_id

deprecated**deprecated**

The unique identifier for the customer.

* * *

first_name

->[firstName](/docs/api/admin-graphql/latest/objects/MailingAddress#field-MailingAddress.fields.firstName)

The customer’s first name.

* * *

id

read-only**read-only**

->[id](/docs/api/admin-graphql/latest/objects/MailingAddress#field-MailingAddress.fields.id)

The unique identifier for the address.

* * *

last_name

->[lastName](/docs/api/admin-graphql/latest/objects/MailingAddress#field-MailingAddress.fields.lastName)

The customer’s last name.

* * *

name

->[name](/docs/api/admin-graphql/latest/objects/MailingAddress#field-MailingAddress.fields.name)

The customer’s first and last names.

* * *

Show 4 hidden fields

Was this section helpful?

YesNo

{}

## The Customer Address resource

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

{

"address1": "1 Rue des Carrieres",

"address2": "Suite 1234",

"city": "Montreal",

"country": "Canada",

"country_code": "CA",

"country_name": "Canada",

"company": "Fancy Co.",

"customer_id": {

"id": 1073339470

},

"first_name": "Samuel",

"id": 207119551,

"last_name": "de Champlain",

"name": "Samuel de Champlain",

"phone": "819-555-5555",

"province": "Quebec",

"province_code": "QC",

"zip": "G1R 4P5"

}

* * *

##

[Anchor to POST request, Creates a new address for a customer](/docs/api/admin-rest/latest/resources/customer-address#post-customers-customer-id-addresses)

post

Creates a new address for a customer

[customerUpdate](/docs/api/admin-graphql/latest/mutations/customerUpdate?example=creates-a-new-address-for-a-customer)

Creates a new address for a customer.

###

[Anchor to Parameters of Creates a new address for a customer](/docs/api/admin-rest/latest/resources/customer-address#post-customers-customer-id-addresses-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

customer_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to post-customers-customer-id-addresses-examples](/docs/api/admin-rest/latest/resources/customer-address#post-customers-customer-id-addresses-examples)Examples

Create a new address for a customer

Path parameters

customer_id=207119551

string**string**

required**required**

Was this section helpful?

YesNo

post

## /admin/api/2026-01/customers/207119551/addresses.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{"address":{"address1":"1 Rue des Carrieres","address2":"Suite 1234","city":"Montreal","company":"Fancy Co.","first_name":"Samuel","last_name":"de Champlain","phone":"819-555-5555","province":"Quebec","country":"Canada","zip":"G1R 4P5","name":"Samuel de Champlain","province_code":"QC","country_code":"CA","country_name":"Canada"}}' \

-X POST "https://your-development-store.myshopify.com/admin/api/2026-01/customers/207119551/addresses.json" \

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

"customer_address": {

"id": 1053317349,

"customer_id": 207119551,

"first_name": "Samuel",

"last_name": "de Champlain",

"company": "Fancy Co.",

"address1": "1 Rue des Carrieres",

"address2": "Suite 1234",

"city": "Montreal",

"province": "Quebec",

"country": "Canada",

"zip": "G1R 4P5",

"phone": "819-555-5555",

"name": "Samuel de Champlain",

"province_code": "QC",

"country_code": "CA",

"country_name": "Canada",

"default": false

}

}

### examples

  * #### Create a new address for a customer

#####

        curl -d '{"address":{"address1":"1 Rue des Carrieres","address2":"Suite 1234","city":"Montreal","company":"Fancy Co.","first_name":"Samuel","last_name":"de Champlain","phone":"819-555-5555","province":"Quebec","country":"Canada","zip":"G1R 4P5","name":"Samuel de Champlain","province_code":"QC","country_code":"CA","country_name":"Canada"}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/customers/207119551/addresses.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const customer_address = new admin.rest.resources.CustomerAddress({session: session});

        customer_address.customer_id = 207119551;
        customer_address.address1 = "1 Rue des Carrieres";
        customer_address.address2 = "Suite 1234";
        customer_address.city = "Montreal";
        customer_address.company = "Fancy Co.";
        customer_address.first_name = "Samuel";
        customer_address.last_name = "de Champlain";
        customer_address.phone = "819-555-5555";
        customer_address.province = "Quebec";
        customer_address.country = "Canada";
        customer_address.zip = "G1R 4P5";
        customer_address.name = "Samuel de Champlain";
        customer_address.province_code = "QC";
        customer_address.country_code = "CA";
        customer_address.country_name = "Canada";
        await customer_address.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        customer_address = ShopifyAPI::CustomerAddress.new(session: test_session)
        customer_address.customer_id = 207119551
        customer_address.address1 = "1 Rue des Carrieres"
        customer_address.address2 = "Suite 1234"
        customer_address.city = "Montreal"
        customer_address.company = "Fancy Co."
        customer_address.first_name = "Samuel"
        customer_address.last_name = "de Champlain"
        customer_address.phone = "819-555-5555"
        customer_address.province = "Quebec"
        customer_address.country = "Canada"
        customer_address.zip = "G1R 4P5"
        customer_address.name = "Samuel de Champlain"
        customer_address.province_code = "QC"
        customer_address.country_code = "CA"
        customer_address.country_name = "Canada"
        customer_address.save!

#####

        // Session is built by the OAuth process

        const customer_address = new shopify.rest.CustomerAddress({session: session});
        customer_address.customer_id = 207119551;
        customer_address.address1 = "1 Rue des Carrieres";
        customer_address.address2 = "Suite 1234";
        customer_address.city = "Montreal";
        customer_address.company = "Fancy Co.";
        customer_address.first_name = "Samuel";
        customer_address.last_name = "de Champlain";
        customer_address.phone = "819-555-5555";
        customer_address.province = "Quebec";
        customer_address.country = "Canada";
        customer_address.zip = "G1R 4P5";
        customer_address.name = "Samuel de Champlain";
        customer_address.province_code = "QC";
        customer_address.country_code = "CA";
        customer_address.country_name = "Canada";
        await customer_address.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"customer_address":{"id":1053317349,"customer_id":207119551,"first_name":"Samuel","last_name":"de Champlain","company":"Fancy Co.","address1":"1 Rue des Carrieres","address2":"Suite 1234","city":"Montreal","province":"Quebec","country":"Canada","zip":"G1R 4P5","phone":"819-555-5555","name":"Samuel de Champlain","province_code":"QC","country_code":"CA","country_name":"Canada","default":false}}


* * *

##

[Anchor to GET request, Retrieves a list of addresses for a customer](/docs/api/admin-rest/latest/resources/customer-address#get-customers-customer-id-addresses?limit=1)

get

Retrieves a list of addresses for a customer

[customer](/docs/api/admin-graphql/latest/queries/customer?example=retrieves-a-list-of-addresses-for-a-customer)

Retrieves a list of addresses for a customer. **Note:** This endpoint implements pagination by using links that are provided in the response header. To learn more, refer to [Make paginated requests to the REST Admin API](/api/usage/pagination-rest).

###

[Anchor to Parameters of Retrieves a list of addresses for a customer](/docs/api/admin-rest/latest/resources/customer-address#get-customers-customer-id-addresses?limit=1-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

customer_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to get-customers-customer-id-addresses?limit=1-examples](/docs/api/admin-rest/latest/resources/customer-address#get-customers-customer-id-addresses?limit=1-examples)Examples

Retrieve a limited number of addresses for a customer

Query parameters

Retrieve all of a customer’s addresses

Was this section helpful?

YesNo

get

## /admin/api/2026-01/customers/207119551/addresses.json?limit=1

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/customers/207119551/addresses.json?limit=1" \

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

HTTP/1.1 200 OK

{

"addresses": [

{

"id": 207119551,

"customer_id": 207119551,

"first_name": null,

"last_name": null,

"company": null,

"address1": "Chestnut Street 92",

"address2": "",

"city": "Louisville",

"province": "Kentucky",

"country": "United States",

"zip": "40202",

"phone": "555-625-1199",

"name": "",

"province_code": "KY",

"country_code": "US",

"country_name": "United States",

"default": true

}

]

}

### examples

  * #### Retrieve a limited number of addresses for a customer

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/customers/207119551/addresses.json?limit=1" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.CustomerAddress.all({
          session: session,
          customer_id: 207119551,
          limit: "1",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::CustomerAddress.all(
          session: test_session,
          customer_id: 207119551,
          limit: "1",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.CustomerAddress.all({
          session: session,
          customer_id: 207119551,
          limit: "1",
        });

#### response

        HTTP/1.1 200 OK{"addresses":[{"id":207119551,"customer_id":207119551,"first_name":null,"last_name":null,"company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"555-625-1199","name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}]}

  * #### Retrieve all of a customer’s addresses

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/customers/207119551/addresses.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.CustomerAddress.all({
          session: session,
          customer_id: 207119551,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::CustomerAddress.all(
          session: test_session,
          customer_id: 207119551,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.CustomerAddress.all({
          session: session,
          customer_id: 207119551,
        });

#### response

        HTTP/1.1 200 OK{"addresses":[{"id":207119551,"customer_id":207119551,"first_name":null,"last_name":null,"company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"555-625-1199","name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}]}


* * *

##

[Anchor to GET request, Retrieves details for a single customer address](/docs/api/admin-rest/latest/resources/customer-address#get-customers-customer-id-addresses-address-id)

get

Retrieves details for a single customer address

[customer](/docs/api/admin-graphql/latest/queries/customer)

Retrieves details for a single customer address.

###

[Anchor to Parameters of Retrieves details for a single customer address](/docs/api/admin-rest/latest/resources/customer-address#get-customers-customer-id-addresses-address-id-parameters)Parameters

* * *

address_id

string**string**

required**required**

* * *

api_version

string**string**

required**required**

* * *

customer_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to get-customers-customer-id-addresses-address-id-examples](/docs/api/admin-rest/latest/resources/customer-address#get-customers-customer-id-addresses-address-id-examples)Examples

Retrieve a single customer address

Was this section helpful?

YesNo

get

## /admin/api/2026-01/customers/207119551/addresses/207119551.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/customers/207119551/addresses/207119551.json" \

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

"customer_address": {

"id": 207119551,

"customer_id": 207119551,

"first_name": null,

"last_name": null,

"company": null,

"address1": "Chestnut Street 92",

"address2": "",

"city": "Louisville",

"province": "Kentucky",

"country": "United States",

"zip": "40202",

"phone": "555-625-1199",

"name": "",

"province_code": "KY",

"country_code": "US",

"country_name": "United States",

"default": true

}

}

### examples

  * #### Retrieve a single customer address

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/customers/207119551/addresses/207119551.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.CustomerAddress.find({
          session: session,
          customer_id: 207119551,
          id: 207119551,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::CustomerAddress.find(
          session: test_session,
          customer_id: 207119551,
          id: 207119551,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.CustomerAddress.find({
          session: session,
          customer_id: 207119551,
          id: 207119551,
        });

#### response

        HTTP/1.1 200 OK{"customer_address":{"id":207119551,"customer_id":207119551,"first_name":null,"last_name":null,"company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"555-625-1199","name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}}


* * *

##

[Anchor to PUT request, Updates an existing customer address](/docs/api/admin-rest/latest/resources/customer-address#put-customers-customer-id-addresses-address-id)

put

Updates an existing customer address

[customerUpdateDefaultAddress](/docs/api/admin-graphql/latest/mutations/customerUpdateDefaultAddress?example=updates-an-existing-customer-address)

Updates an existing customer address.

###

[Anchor to Parameters of Updates an existing customer address](/docs/api/admin-rest/latest/resources/customer-address#put-customers-customer-id-addresses-address-id-parameters)Parameters

* * *

address_id

string**string**

required**required**

* * *

api_version

string**string**

required**required**

* * *

customer_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to put-customers-customer-id-addresses-address-id-examples](/docs/api/admin-rest/latest/resources/customer-address#put-customers-customer-id-addresses-address-id-examples)Examples

Update the postal code of a customer address

Update the street address of a customer address

Was this section helpful?

YesNo

put

## /admin/api/2026-01/customers/207119551/addresses/207119551.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{"address":{"id":207119551,"zip":"90210"}}' \

-X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/customers/207119551/addresses/207119551.json" \

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

HTTP/1.1 200 OK

{

"customer_address": {

"customer_id": 207119551,

"zip": "90210",

"country": "United States",

"province": "Kentucky",

"city": "Louisville",

"address1": "Chestnut Street 92",

"address2": "",

"first_name": null,

"last_name": null,

"company": null,

"phone": "555-625-1199",

"id": 207119551,

"name": "",

"province_code": "KY",

"country_code": "US",

"country_name": "United States",

"default": true

}

}

### examples

  * #### Update the postal code of a customer address

#####

        curl -d '{"address":{"id":207119551,"zip":"90210"}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/customers/207119551/addresses/207119551.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const customer_address = new admin.rest.resources.CustomerAddress({session: session});

        customer_address.customer_id = 207119551;
        customer_address.id = 207119551;
        customer_address.zip = "90210";
        await customer_address.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        customer_address = ShopifyAPI::CustomerAddress.new(session: test_session)
        customer_address.customer_id = 207119551
        customer_address.id = 207119551
        customer_address.zip = "90210"
        customer_address.save!

#####

        // Session is built by the OAuth process

        const customer_address = new shopify.rest.CustomerAddress({session: session});
        customer_address.customer_id = 207119551;
        customer_address.id = 207119551;
        customer_address.zip = "90210";
        await customer_address.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"customer_address":{"customer_id":207119551,"zip":"90210","country":"United States","province":"Kentucky","city":"Louisville","address1":"Chestnut Street 92","address2":"","first_name":null,"last_name":null,"company":null,"phone":"555-625-1199","id":207119551,"name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}}

  * #### Update the street address of a customer address

#####

        curl -d '{"address":{"id":207119551,"address1":"Apartment 23","address2":"Chestnut Street 92"}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/customers/207119551/addresses/207119551.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const customer_address = new admin.rest.resources.CustomerAddress({session: session});

        customer_address.customer_id = 207119551;
        customer_address.id = 207119551;
        customer_address.address1 = "Apartment 23";
        customer_address.address2 = "Chestnut Street 92";
        await customer_address.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        customer_address = ShopifyAPI::CustomerAddress.new(session: test_session)
        customer_address.customer_id = 207119551
        customer_address.id = 207119551
        customer_address.address1 = "Apartment 23"
        customer_address.address2 = "Chestnut Street 92"
        customer_address.save!

#####

        // Session is built by the OAuth process

        const customer_address = new shopify.rest.CustomerAddress({session: session});
        customer_address.customer_id = 207119551;
        customer_address.id = 207119551;
        customer_address.address1 = "Apartment 23";
        customer_address.address2 = "Chestnut Street 92";
        await customer_address.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"customer_address":{"customer_id":207119551,"address1":"Apartment 23","address2":"Chestnut Street 92","country":"United States","province":"Kentucky","zip":"40202","city":"Louisville","first_name":null,"last_name":null,"company":null,"phone":"555-625-1199","id":207119551,"name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}}


* * *

##

[Anchor to PUT request, Sets the default address for a customer](/docs/api/admin-rest/latest/resources/customer-address#put-customers-customer-id-addresses-address-id-default)

put

Sets the default address for a customer

[customerUpdateDefaultAddress](/docs/api/admin-graphql/latest/mutations/customerUpdateDefaultAddress?example=sets-the-default-address-for-a-customer)

Sets the default address for a customer.

###

[Anchor to Parameters of Sets the default address for a customer](/docs/api/admin-rest/latest/resources/customer-address#put-customers-customer-id-addresses-address-id-default-parameters)Parameters

* * *

address_id

string**string**

required**required**

* * *

api_version

string**string**

required**required**

* * *

customer_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to put-customers-customer-id-addresses-address-id-default-examples](/docs/api/admin-rest/latest/resources/customer-address#put-customers-customer-id-addresses-address-id-default-examples)Examples

Set a default address for a customer

Was this section helpful?

YesNo

put

## /admin/api/2026-01/customers/207119551/addresses/1053317347/default.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/customers/207119551/addresses/1053317347/default.json" \

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

"customer_address": {

"id": 1053317347,

"customer_id": 207119551,

"first_name": null,

"last_name": null,

"company": null,

"address1": "123 Test St",

"address2": null,

"city": "Ottawa",

"province": "Ontario",

"country": "Canada",

"zip": null,

"phone": null,

"name": "",

"province_code": "ON",

"country_code": "CA",

"country_name": "Canada",

"default": true

}

}

### examples

  * #### Set a default address for a customer

#####

        curl -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/customers/207119551/addresses/1053317347/default.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        const { admin, session } = await authenticate.admin(request);

        const customer_address = new admin.rest.resources.CustomerAddress({session: session});

        customer_address.customer_id = 207119551;
        customer_address.id = 1053317347;
        await customer_address.default({});

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        customer_address = ShopifyAPI::CustomerAddress.new(session: test_session)
        customer_address.customer_id = 207119551
        customer_address.id = 1053317347
        customer_address.default(
          session: test_session,
        )

#####

        // Session is built by the OAuth process

        const customer_address = new shopify.rest.CustomerAddress({session: session});
        customer_address.customer_id = 207119551;
        customer_address.id = 1053317347;
        await customer_address.default({});

#### response

        HTTP/1.1 200 OK{"customer_address":{"id":1053317347,"customer_id":207119551,"first_name":null,"last_name":null,"company":null,"address1":"123 Test St","address2":null,"city":"Ottawa","province":"Ontario","country":"Canada","zip":null,"phone":null,"name":"","province_code":"ON","country_code":"CA","country_name":"Canada","default":true}}


* * *

##

[Anchor to PUT request, Performs bulk operations for multiple customer addresses](/docs/api/admin-rest/latest/resources/customer-address#put-customers-customer-id-addresses-set?address-ids\[\]=1053317346&operation=destroy)

put

Performs bulk operations for multiple customer addresses

[customerUpdate](/docs/api/admin-graphql/latest/mutations/customerUpdate?example=performs-bulk-operations-for-multiple-customer-addresses)

Performs bulk operations for multiple customer addresses.

###

[Anchor to Parameters of Performs bulk operations for multiple customer addresses](/docs/api/admin-rest/latest/resources/customer-address#put-customers-customer-id-addresses-set?address-ids\[\]=1053317346&operation=destroy-parameters)Parameters

* * *

address_ids[]

required**required**

Performs bulk operations on a list of customer address IDs. Format: `address_ids[]=1&address_ids[]=2&address_ids[]=3`.

* * *

api_version

string**string**

required**required**

* * *

customer_id

string**string**

required**required**

* * *

operation

required**required**

Operation to perform by keyword (for example, destroy)

* * *

Was this section helpful?

YesNo

###

[Anchor to put-customers-customer-id-addresses-set?address-ids[]=1053317346&operation=destroy-examples](/docs/api/admin-rest/latest/resources/customer-address#put-customers-customer-id-addresses-set?address-ids\[\]=1053317346&operation=destroy-examples)Examples

Destroy multiple customer addresses

Query parameters

address_ids[]=1053317346

required**required**

Performs bulk operations on a list of customer address IDs. Format: `address_ids[]=1&address_ids[]=2&address_ids[]=3`.

operation=destroy

required**required**

Operation to perform by keyword (for example, destroy)

Was this section helpful?

YesNo

put

## /admin/api/2026-01/customers/207119551/addresses/set.json?address_ids[]=1053317346&operation=destroy

cURLRemixRubyNode.js

Copy

9

1

2

curl -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/customers/207119551/addresses/set.json?address_ids%5B%5D=1053317346&operation=destroy" \

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

  * #### Destroy multiple customer addresses

#####

        curl -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/customers/207119551/addresses/set.json?address_ids%5B%5D=1053317346&operation=destroy" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        const { admin, session } = await authenticate.admin(request);

        const customer_address = new admin.rest.resources.CustomerAddress({session: session});

        customer_address.customer_id = 207119551;
        await customer_address.set({
          address_ids: ["1053317346"],
          operation: "destroy",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        customer_address = ShopifyAPI::CustomerAddress.new(session: test_session)
        customer_address.customer_id = 207119551
        customer_address.set(
          session: test_session,
          address_ids: ["1053317346"],
          operation: "destroy",
        )

#####

        // Session is built by the OAuth process

        const customer_address = new shopify.rest.CustomerAddress({session: session});
        customer_address.customer_id = 207119551;
        await customer_address.set({
          address_ids: ["1053317346"],
          operation: "destroy",
        });

#### response

        HTTP/1.1 200 OK{}


* * *

##

[Anchor to DELETE request, Removes an address from a customer’s address list](/docs/api/admin-rest/latest/resources/customer-address#delete-customers-customer-id-addresses-address-id)

del

Removes an address from a customer’s address list

Removes an address from a customer’s address list.

###

[Anchor to Parameters of Removes an address from a customer’s address list](/docs/api/admin-rest/latest/resources/customer-address#delete-customers-customer-id-addresses-address-id-parameters)Parameters

* * *

address_id

string**string**

required**required**

* * *

api_version

string**string**

required**required**

* * *

customer_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to delete-customers-customer-id-addresses-address-id-examples](/docs/api/admin-rest/latest/resources/customer-address#delete-customers-customer-id-addresses-address-id-examples)Examples

Remove a customer address

Removing a customer’s default address fails and returns an error

Was this section helpful?

YesNo

del

## /admin/api/2026-01/customers/207119551/addresses/1053317348.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X DELETE "https://your-development-store.myshopify.com/admin/api/2026-01/customers/207119551/addresses/1053317348.json" \

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

  * #### Remove a customer address

#####

        curl -X DELETE "https://your-development-store.myshopify.com/admin/api/2026-01/customers/207119551/addresses/1053317348.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.CustomerAddress.delete({
          session: session,
          customer_id: 207119551,
          id: 1053317348,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::CustomerAddress.delete(
          session: test_session,
          customer_id: 207119551,
          id: 1053317348,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.CustomerAddress.delete({
          session: session,
          customer_id: 207119551,
          id: 1053317348,
        });

#### response

        HTTP/1.1 200 OK{}

  * #### Removing a customer’s default address fails and returns an error

#####

        curl -X DELETE "https://your-development-store.myshopify.com/admin/api/2026-01/customers/207119551/addresses/207119551.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.CustomerAddress.delete({
          session: session,
          customer_id: 207119551,
          id: 207119551,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::CustomerAddress.delete(
          session: test_session,
          customer_id: 207119551,
          id: 207119551,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.CustomerAddress.delete({
          session: session,
          customer_id: 207119551,
          id: 207119551,
        });

#### response

        HTTP/1.1 422 Unprocessable Entity{"errors":{"base":["Cannot delete the customer’s default address"]}}