# Customer

*Source: https://shopify.dev/docs/api/admin-rest/2026-01/resources/customer*

---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04

2026-01latest

# Customer

Ask assistant

Multiple access scopes needed — refer to each endpoint for access scope requirements.

**Multiple access scopes needed — refer to each endpoint for access scope requirements.:**

Requires access to [protected customer data](https://shopify.dev/apps/store/data-protection/protected-customer-data).

**Requires access to [protected customer data](https://shopify.dev/apps/store/data-protection/protected-customer-data).:**

The Customer resource stores information about a shop's customers, such as their contact details, their order history, and whether they've agreed to receive email marketing.

The Customer resource also holds information on the status of a customer's account. Customers with accounts save time at checkout when they're logged in because they don't need to enter their contact information. You can use the Customer API to check whether a customer has an active account, and then invite them to create one if they don't.

For security reasons, the Customer resource doesn't store credit card information. Customers always need to enter this information at checkout.

In a shop's checkout settings, there are three options for customer accounts:

  * **Accounts are disabled** : Customers can't create accounts and can check out only as guests.
  * **Accounts are optional** : Customers have the choice of either signing into their account or checking out as a guest. Customers can create accounts for themselves, and the shop owner can create an account for a customer and then invite them by email to use it.
  * **Accounts are required** : Customers can't check out unless they're logged in, and the shop owner must create their accounts.


Caution: Only use this data if it is necessary for the intended app functionality. Shopify retains the ability to restrict access to [API Access scopes](/api/usage/access-scopes) for apps not requiring legitimate use of the associated data.

Was this section helpful?

YesNo

#

## Endpoints

  * [post/admin/api/latest/customers.json](/docs/api/admin-rest/latest/resources/customer#post-customers)

Creates a customer

[customerCreate](/docs/api/admin-graphql/latest/mutations/customerCreate?example=creates-a-customer)

  * [post/admin/api/latest/customers/{customer_id}/account_activation_url.json](/docs/api/admin-rest/latest/resources/customer#post-customers-customer-id-account-activation-url)

Creates an account activation URL for a customer

[customerGenerateAccountActivationUrl](/docs/api/admin-graphql/latest/mutations/customerGenerateAccountActivationUrl?example=creates-an-account-activation-url-for-a-customer)

  * [post/admin/api/latest/customers/{customer_id}/send_invite.json](/docs/api/admin-rest/latest/resources/customer#post-customers-customer-id-send-invite)

Sends an account invite to a customer

[customerSendAccountInviteEmail](/docs/api/admin-graphql/latest/mutations/customerSendAccountInviteEmail?example=sends-an-account-invite-to-a-customer)

  * [get/admin/api/latest/customers.json?ids=207119551,562393516,688973684,1073339533](/docs/api/admin-rest/latest/resources/customer#get-customers?ids=207119551,562393516,688973684,1073339533)

Retrieves a list of customers

[customers](/docs/api/admin-graphql/latest/queries/customers)

  * [get/admin/api/latest/customers/{customer_id}/orders.json](/docs/api/admin-rest/latest/resources/customer#get-customers-customer-id-orders)

Retrieves all orders that belong to a customer

[customer](/docs/api/admin-graphql/latest/queries/customer)

  * [get/admin/api/latest/customers/count.json](/docs/api/admin-rest/latest/resources/customer#get-customers-count)

Retrieves a count of customers

[customersCount](/docs/api/admin-graphql/latest/queries/customersCount?example=retrieves-a-count-of-customers)

  * [get/admin/api/latest/customers/search.json?query=email:bob.norman@mail.example.com](/docs/api/admin-rest/latest/resources/customer#get-customers-search?query=email:bob.norman@mail.example.com)

Searches for customers that match a supplied query

[customers](/docs/api/admin-graphql/latest/queries/customers)

  * [put/admin/api/latest/customers/{customer_id}.json](/docs/api/admin-rest/latest/resources/customer#put-customers-customer-id)

Updates a customer

[customerUpdate](/docs/api/admin-graphql/latest/mutations/customerUpdate)


* * *

[Anchor to ](/docs/api/admin-rest/latest/resources/customer#resource-object)

## The Customer resource

[Anchor to ](/docs/api/admin-rest/latest/resources/customer#resource-object-properties)

### Properties

* * *

addresses

->[addresses](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.addresses)

A list of the ten most recently updated addresses for the customer. Each address has the following properties:

Show addresses properties

  * **address1** : The customer's mailing address.
  * **address2** : An additional field for the customer's mailing address.
  * **city** : The customer's city, town, or village.
  * **company** : The customer's company.
  * **country** : The customer's country.
  * **country_code** : The two-letter country code corresponding to the customer's country.
  * **country_name** : The customer's normalized country name.
  * **customer_id** : A unique identifier for the customer.
  * **default** : Whether this address is the default address for the customer.
  * **first_name** : The customer's first name.
  * **id** : A unique identifier for the address.
  * **last_name** : The customer's last name.
  * **name** : The customer's first and last names.
  * **phone** : The customer's phone number at this address.
  * **province** : The customer's region name. Typically a province, a state, or a prefecture.
  * **province_code** : The code for the region of the address, such as the province, state, or district. For example QC for Quebec, Canada.
  * **zip** : The customer's postal code, also known as zip, postcode, Eircode, etc.


* * *

currency

deprecated**deprecated**

The three-letter code ([ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) format) for the currency that the customer used when they paid for their last order. Defaults to the shop currency. Returns the shop currency for test orders.

* * *

created_at

read-only**read-only**

->[createdAt](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.createdAt)

The date and time ([ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format) when the customer was created.

* * *

default_address

read-only**read-only**

->[defaultAddress](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.defaultAddress)

The default address for the customer. The default address has the following properties:

Show default_address properties

  * **address1** : The first line of the customer's mailing address.
  * **address2** : An additional field for the customer's mailing address.
  * **city** : The customer's city, town, or village.
  * **company** : The customer's company.
  * **country** : The customer's country.
  * **country_code** : The two-letter country code corresponding to the customer's country.
  * **country_name** : The customer's normalized country name.
  * **customer_id** : A unique identifier for the customer.
  * **default** : Returns `true` for each default address.
  * **first_name** : The customer's first name.
  * **id** : A unique identifier for the address.
  * **last_name** : The customer's last name.
  * **name** : The customer's first and last names.
  * **phone** : The customer's phone number at this address.
  * **province** : The customer's region name. Typically a province, a state, or a prefecture.
  * **province_code** : The alphanumeric code for the customer's region.
  * **zip** : The customer's postal code, also known as zip, postcode, Eircode, etc.


* * *

email

->[email](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.email)

The unique email address of the customer. Attempting to assign the same email address to multiple customers returns an error.

* * *

email_marketing_consent

->[emailMarketingConsent](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.emailMarketingConsent)

The marketing consent information when the customer consented to receiving marketing material by email. The `email` property is required to create a customer with email consent information and to update a customer for email consent that doesn't have an email recorded. The customer must have a unique email address associated to the record. The email marketing consent has the following properties:

Show email_marketing_consent properties

  * **state** : The current email marketing state for the customer.
  * **opt_in_level** : The marketing subscription opt-in level, as described in the [M3AAWG Sender Best Common Practices](https://www.m3aawg.org/sites/default/files/document/M3AAWG_Senders_BCP_Ver3-2015-02.pdf), that the customer gave when they consented to receive marketing material by email.
  * **consent_updated_at** : The date and time when the customer consented to receive marketing material by email. If no date is provided, then the date and time when the consent information was sent is used.


* * *

first_name

->[firstName](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.firstName)

The customer's first name.

* * *

id

->[id](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.id)

A unique identifier for the customer.

* * *

last_name

->[lastName](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.lastName)

The customer's last name.

* * *

last_order_id

read-only**read-only**

->[lastOrder](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.lastOrder)

The ID of the customer's last order.

* * *

last_order_name

read-only**read-only**

->[lastOrder](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.lastOrder)

The name of the customer's last order. This is directly related to the `name` field on the Order resource.

* * *

metafield

->[metafield](/docs/api/admin-graphql/latest/objects/Customer#field-Customer.fields.metafield)

Attaches additional metadata to a shop's resources:

Show metafield properties

  * **key** (required): An identifier for the metafield (maximum of 30 characters).
  * **namespace**(required): A container for a set of metadata (maximum of 20 characters). Namespaces help distinguish between metadata that you created and metadata created by another individual with a similar namespace.
  * **value** (required): Information to be stored as metadata.
  * **type** (required): The type. Refer to the [full list of types](/apps/metafields/types).
  * **description** (optional): Additional information about the metafield.


* * *

Show 15 hidden fields

Was this section helpful?

YesNo

{}

## The Customer resource

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

{

"addresses": [

{

"id": 207119551,

"customer_id": 6940095564,

"first_name": "Bob",

"last_name": "Norman",

"company": null,

"address1": "Chestnut Street 92",

"address2": "Apartment 2",

"city": "Louisville",

"province": "Kentucky",

"country": "United States",

"zip": "40202",

"phone": "555-625-1199",

"province_code": "KY",

"country_code": "US",

"country_name": "United States",

"default": true

}

],

"currency": "JPY",

"created_at": "2013-06-27T08:48:27-04:00",

"default_address": {

"address1": "Chestnut Street 92",

"address2": "Apartment 2",

"city": "Louisville",

"company": null,

"country": "united states",

"first_name": "Bob",

"id": 207119551,

"last_name": "Norman",

"phone": "555-625-1199",

"province": "Kentucky",

"zip": "40202",

"province_code": "KY",

"country_code": "US",

"country_name": "United States",

"default": true

},

"email": "bob.norman@mail.example.com",

"email_marketing_consent": {

"state": "subscribed",

"opt_in_level": "confirmed_opt_in",

"consent_updated_at": "2022-04-01T11:22:06-04:00"

},

"first_name": "John",

"id": 207119551,

"last_name": "Norman",

"last_order_id": 234132602919,

"last_order_name": "#1169",

"metafield": {

"key": "new",

"namespace": "global",

"value": "newvalue",

"type": "string"

},

"marketing_opt_in_level": "confirmed_opt_in",

"multipass_identifier": null,

"note": "Placed an order that had a fraud warning",

"orders_count": 3,

"password": "password",

"password_confirmation": "password_confirmation",

"phone": "+16135551111",

"sms_marketing_consent": {

"state": "subscribed",

"opt_in_level": "single_opt_in",

"consent_updated_at": "2021-08-03T15:31:06-04:00",

"consent_collected_from": "OTHER"

},

"state": "disabled",

"tags": "loyal",

"tax_exempt": true,

"tax_exemptions": [

"CA_STATUS_CARD_EXEMPTION",

"CA_BC_RESELLER_EXEMPTION"

],

"total_spent": "375.30",

"updated_at": "2012-08-24T14:01:46-04:00",

"verified_email": true

}

* * *

##

[Anchor to POST request, Creates a customer](/docs/api/admin-rest/latest/resources/customer#post-customers)

post

Creates a customer

[customerCreate](/docs/api/admin-graphql/latest/mutations/customerCreate?example=creates-a-customer)

Requires `customers` access scope.

**Requires `customers` access scope.:**

Creates a customer.

###

[Anchor to Parameters of Creates a customer](/docs/api/admin-rest/latest/resources/customer#post-customers-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to post-customers-examples](/docs/api/admin-rest/latest/resources/customer#post-customers-examples)Examples

Create a customer with `password` and `password_confirmation` and skip sending the welcome email

Request body

customer[](/apps/store/data-protection/protected-customer-data)

Customer resource**Customer resource**

Show customer properties

customer.first_name:"Steve"

->[firstName](/docs/api/admin-graphql/latest/input-objects/CustomerInput#fields-firstName)

The customer's first name.

customer.last_name:"Lastnameson"

->[lastName](/docs/api/admin-graphql/latest/input-objects/CustomerInput#fields-lastName)

The customer's last name.

customer.email:"steve.lastnameson@example.com"

->[email](/docs/api/admin-graphql/latest/input-objects/CustomerInput#fields-email)

The unique email address of the customer. Attempting to assign the same email address to multiple customers returns an error.

customer.phone:"+15142546011"

->[phone](/docs/api/admin-graphql/latest/input-objects/CustomerInput#fields-phone)

The unique phone number ([E.164 format](https://en.wikipedia.org/wiki/E.164)) for this customer. Attempting to assign the same phone number to multiple customers returns an error. The property can be set using different formats, but each format must represent a number that can be dialed from anywhere in the world. The following formats are all valid:

Show phone properties

  * 6135551212
  * +16135551212
  * (613)555-1212
  * +1 613-555-1212


customer.verified_email:true

read-only**read-only**

Whether the customer has verified their email address.

customer.addresses:[{"address1":"123 Oak St","city":"Ottawa","province":"ON","phone":"555-1212","zip":"123 ABC","last_name":"Lastnameson","first_name":"Mother","country":"CA"}]

A list of the ten most recently updated addresses for the customer. Each address has the following properties:

Show addresses properties

  * **address1** : The customer's mailing address.
  * **address2** : An additional field for the customer's mailing address.
  * **city** : The customer's city, town, or village.
  * **company** : The customer's company.
  * **country** : The customer's country.
  * **country_code** : The two-letter country code corresponding to the customer's country.
  * **country_name** : The customer's normalized country name.
  * **customer_id** : A unique identifier for the customer.
  * **default** : Whether this address is the default address for the customer.
  * **first_name** : The customer's first name.
  * **id** : A unique identifier for the address.
  * **last_name** : The customer's last name.
  * **name** : The customer's first and last names.
  * **phone** : The customer's phone number at this address.
  * **province** : The customer's region name. Typically a province, a state, or a prefecture.
  * **province_code** : The code for the region of the address, such as the province, state, or district. For example QC for Quebec, Canada.
  * **zip** : The customer's postal code, also known as zip, postcode, Eircode, etc.


customer.password:"newpass"

deprecated**deprecated**

The customer's password.

customer.password_confirmation:"newpass"

deprecated**deprecated**

The customer's password that's confirmed.

Create a customer with `password` and `password_confirmation` and skip sending the welcome email

Request body

customer[](/apps/store/data-protection/protected-customer-data)

Customer resource**Customer resource**

Show customer properties

customer.first_name:"Steve"

->[firstName](/docs/api/admin-graphql/latest/input-objects/CustomerInput#fields-firstName)

The customer's first name.

customer.last_name:"Lastnameson"

->[lastName](/docs/api/admin-graphql/latest/input-objects/CustomerInput#fields-lastName)

The customer's last name.

customer.email:"steve.lastnameson@example.com"

->[email](/docs/api/admin-graphql/latest/input-objects/CustomerInput#fields-email)

The unique email address of the customer. Attempting to assign the same email address to multiple customers returns an error.

customer.phone:"+15142546011"

->[phone](/docs/api/admin-graphql/latest/input-objects/CustomerInput#fields-phone)

The unique phone number ([E.164 format](https://en.wikipedia.org/wiki/E.164)) for this customer. Attempting to assign the same phone number to multiple customers returns an error. The property can be set using different formats, but each format must represent a number that can be dialed from anywhere in the world. The following formats are all valid:

Show phone properties

  * 6135551212
  * +16135551212
  * (613)555-1212
  * +1 613-555-1212


customer.verified_email:true

read-only**read-only**

Whether the customer has verified their email address.

customer.addresses:[{"address1":"123 Oak St","city":"Ottawa","province":"ON","phone":"555-1212","zip":"123 ABC","last_name":"Lastnameson","first_name":"Mother","country":"CA"}]

A list of the ten most recently updated addresses for the customer. Each address has the following properties:

Show addresses properties

  * **address1** : The customer's mailing address.
  * **address2** : An additional field for the customer's mailing address.
  * **city** : The customer's city, town, or village.
  * **company** : The customer's company.
  * **country** : The customer's country.
  * **country_code** : The two-letter country code corresponding to the customer's country.
  * **country_name** : The customer's normalized country name.
  * **customer_id** : A unique identifier for the customer.
  * **default** : Whether this address is the default address for the customer.
  * **first_name** : The customer's first name.
  * **id** : A unique identifier for the address.
  * **last_name** : The customer's last name.
  * **name** : The customer's first and last names.
  * **phone** : The customer's phone number at this address.
  * **province** : The customer's region name. Typically a province, a state, or a prefecture.
  * **province_code** : The code for the region of the address, such as the province, state, or district. For example QC for Quebec, Canada.
  * **zip** : The customer's postal code, also known as zip, postcode, Eircode, etc.


customer.password:"newpass"

deprecated**deprecated**

The customer's password.

customer.password_confirmation:"newpass"

deprecated**deprecated**

The customer's password that's confirmed.

Create a customer with a metafield

Request body

customer[](/apps/store/data-protection/protected-customer-data)

Customer resource**Customer resource**

Show customer properties

customer.first_name:"Steve"

->[firstName](/docs/api/admin-graphql/latest/input-objects/CustomerInput#fields-firstName)

The customer's first name.

customer.last_name:"Lastnameson"

->[lastName](/docs/api/admin-graphql/latest/input-objects/CustomerInput#fields-lastName)

The customer's last name.

customer.email:"steve.lastnameson@example.com"

->[email](/docs/api/admin-graphql/latest/input-objects/CustomerInput#fields-email)

The unique email address of the customer. Attempting to assign the same email address to multiple customers returns an error.

customer.phone:"+15142546011"

->[phone](/docs/api/admin-graphql/latest/input-objects/CustomerInput#fields-phone)

The unique phone number ([E.164 format](https://en.wikipedia.org/wiki/E.164)) for this customer. Attempting to assign the same phone number to multiple customers returns an error. The property can be set using different formats, but each format must represent a number that can be dialed from anywhere in the world. The following formats are all valid:

Show phone properties

  * 6135551212
  * +16135551212
  * (613)555-1212
  * +1 613-555-1212


customer.verified_email:true

read-only**read-only**

Whether the customer has verified their email address.

customer.addresses:[{"address1":"123 Oak St","city":"Ottawa","province":"ON","phone":"555-1212","zip":"123 ABC","last_name":"Lastnameson","first_name":"Mother","country":"CA"}]

A list of the ten most recently updated addresses for the customer. Each address has the following properties:

Show addresses properties

  * **address1** : The customer's mailing address.
  * **address2** : An additional field for the customer's mailing address.
  * **city** : The customer's city, town, or village.
  * **company** : The customer's company.
  * **country** : The customer's country.
  * **country_code** : The two-letter country code corresponding to the customer's country.
  * **country_name** : The customer's normalized country name.
  * **customer_id** : A unique identifier for the customer.
  * **default** : Whether this address is the default address for the customer.
  * **first_name** : The customer's first name.
  * **id** : A unique identifier for the address.
  * **last_name** : The customer's last name.
  * **name** : The customer's first and last names.
  * **phone** : The customer's phone number at this address.
  * **province** : The customer's region name. Typically a province, a state, or a prefecture.
  * **province_code** : The code for the region of the address, such as the province, state, or district. For example QC for Quebec, Canada.
  * **zip** : The customer's postal code, also known as zip, postcode, Eircode, etc.


Create a new customer record

Request body

customer[](/apps/store/data-protection/protected-customer-data)

Customer resource**Customer resource**

Show customer properties

customer.first_name:"Steve"

->[firstName](/docs/api/admin-graphql/latest/input-objects/CustomerInput#fields-firstName)

The customer's first name.

customer.last_name:"Lastnameson"

->[lastName](/docs/api/admin-graphql/latest/input-objects/CustomerInput#fields-lastName)

The customer's last name.

customer.email:"steve.lastnameson@example.com"

->[email](/docs/api/admin-graphql/latest/input-objects/CustomerInput#fields-email)

The unique email address of the customer. Attempting to assign the same email address to multiple customers returns an error.

customer.phone:"+15142546011"

->[phone](/docs/api/admin-graphql/latest/input-objects/CustomerInput#fields-phone)

The unique phone number ([E.164 format](https://en.wikipedia.org/wiki/E.164)) for this customer. Attempting to assign the same phone number to multiple customers returns an error. The property can be set using different formats, but each format must represent a number that can be dialed from anywhere in the world. The following formats are all valid:

Show phone properties

  * 6135551212
  * +16135551212
  * (613)555-1212
  * +1 613-555-1212


customer.verified_email:true

read-only**read-only**

Whether the customer has verified their email address.

customer.addresses:[{"address1":"123 Oak St","city":"Ottawa","province":"ON","phone":"555-1212","zip":"123 ABC","last_name":"Lastnameson","first_name":"Mother","country":"CA"}]

A list of the ten most recently updated addresses for the customer. Each address has the following properties:

Show addresses properties

  * **address1** : The customer's mailing address.
  * **address2** : An additional field for the customer's mailing address.
  * **city** : The customer's city, town, or village.
  * **company** : The customer's company.
  * **country** : The customer's country.
  * **country_code** : The two-letter country code corresponding to the customer's country.
  * **country_name** : The customer's normalized country name.
  * **customer_id** : A unique identifier for the customer.
  * **default** : Whether this address is the default address for the customer.
  * **first_name** : The customer's first name.
  * **id** : A unique identifier for the address.
  * **last_name** : The customer's last name.
  * **name** : The customer's first and last names.
  * **phone** : The customer's phone number at this address.
  * **province** : The customer's region name. Typically a province, a state, or a prefecture.
  * **province_code** : The code for the region of the address, such as the province, state, or district. For example QC for Quebec, Canada.
  * **zip** : The customer's postal code, also known as zip, postcode, Eircode, etc.


Create a new customer record

Request body

customer[](/apps/store/data-protection/protected-customer-data)

Customer resource**Customer resource**

Show customer properties

customer.first_name:"Steve"

->[firstName](/docs/api/admin-graphql/latest/input-objects/CustomerInput#fields-firstName)

The customer's first name.

customer.last_name:"Lastnameson"

->[lastName](/docs/api/admin-graphql/latest/input-objects/CustomerInput#fields-lastName)

The customer's last name.

customer.email:"steve.lastnameson@example.com"

->[email](/docs/api/admin-graphql/latest/input-objects/CustomerInput#fields-email)

The unique email address of the customer. Attempting to assign the same email address to multiple customers returns an error.

customer.phone:"+15142546011"

->[phone](/docs/api/admin-graphql/latest/input-objects/CustomerInput#fields-phone)

The unique phone number ([E.164 format](https://en.wikipedia.org/wiki/E.164)) for this customer. Attempting to assign the same phone number to multiple customers returns an error. The property can be set using different formats, but each format must represent a number that can be dialed from anywhere in the world. The following formats are all valid:

Show phone properties

  * 6135551212
  * +16135551212
  * (613)555-1212
  * +1 613-555-1212


customer.verified_email:true

read-only**read-only**

Whether the customer has verified their email address.

customer.addresses:[{"address1":"123 Oak St","city":"Ottawa","province":"ON","phone":"555-1212","zip":"123 ABC","last_name":"Lastnameson","first_name":"Mother","country":"CA"}]

A list of the ten most recently updated addresses for the customer. Each address has the following properties:

Show addresses properties

  * **address1** : The customer's mailing address.
  * **address2** : An additional field for the customer's mailing address.
  * **city** : The customer's city, town, or village.
  * **company** : The customer's company.
  * **country** : The customer's country.
  * **country_code** : The two-letter country code corresponding to the customer's country.
  * **country_name** : The customer's normalized country name.
  * **customer_id** : A unique identifier for the customer.
  * **default** : Whether this address is the default address for the customer.
  * **first_name** : The customer's first name.
  * **id** : A unique identifier for the address.
  * **last_name** : The customer's last name.
  * **name** : The customer's first and last names.
  * **phone** : The customer's phone number at this address.
  * **province** : The customer's region name. Typically a province, a state, or a prefecture.
  * **province_code** : The code for the region of the address, such as the province, state, or district. For example QC for Quebec, Canada.
  * **zip** : The customer's postal code, also known as zip, postcode, Eircode, etc.


Create a new customer record

Request body

customer[](/apps/store/data-protection/protected-customer-data)

Customer resource**Customer resource**

Show customer properties

customer.first_name:"Steve"

->[firstName](/docs/api/admin-graphql/latest/input-objects/CustomerInput#fields-firstName)

The customer's first name.

customer.last_name:"Lastnameson"

->[lastName](/docs/api/admin-graphql/latest/input-objects/CustomerInput#fields-lastName)

The customer's last name.

customer.email:"steve.lastnameson@example.com"

->[email](/docs/api/admin-graphql/latest/input-objects/CustomerInput#fields-email)

The unique email address of the customer. Attempting to assign the same email address to multiple customers returns an error.

customer.phone:"+15142546011"

->[phone](/docs/api/admin-graphql/latest/input-objects/CustomerInput#fields-phone)

The unique phone number ([E.164 format](https://en.wikipedia.org/wiki/E.164)) for this customer. Attempting to assign the same phone number to multiple customers returns an error. The property can be set using different formats, but each format must represent a number that can be dialed from anywhere in the world. The following formats are all valid:

Show phone properties

  * 6135551212
  * +16135551212
  * (613)555-1212
  * +1 613-555-1212


customer.verified_email:true

read-only**read-only**

Whether the customer has verified their email address.

customer.addresses:[{"address1":"123 Oak St","city":"Ottawa","province":"ON","phone":"555-1212","zip":"123 ABC","last_name":"Lastnameson","first_name":"Mother","country":"CA"}]

A list of the ten most recently updated addresses for the customer. Each address has the following properties:

Show addresses properties

  * **address1** : The customer's mailing address.
  * **address2** : An additional field for the customer's mailing address.
  * **city** : The customer's city, town, or village.
  * **company** : The customer's company.
  * **country** : The customer's country.
  * **country_code** : The two-letter country code corresponding to the customer's country.
  * **country_name** : The customer's normalized country name.
  * **customer_id** : A unique identifier for the customer.
  * **default** : Whether this address is the default address for the customer.
  * **first_name** : The customer's first name.
  * **id** : A unique identifier for the address.
  * **last_name** : The customer's last name.
  * **name** : The customer's first and last names.
  * **phone** : The customer's phone number at this address.
  * **province** : The customer's region name. Typically a province, a state, or a prefecture.
  * **province_code** : The code for the region of the address, such as the province, state, or district. For example QC for Quebec, Canada.
  * **zip** : The customer's postal code, also known as zip, postcode, Eircode, etc.


Creating a customer with an email that belongs to an existing customer returns an error

Request body

customer[](/apps/store/data-protection/protected-customer-data)

Customer resource**Customer resource**

Show customer properties

customer.email:"bob.norman@mail.example.com"

->[email](/docs/api/admin-graphql/latest/input-objects/CustomerInput#fields-email)

The unique email address of the customer. Attempting to assign the same email address to multiple customers returns an error.

customer.first_name:"Tobi"

->[firstName](/docs/api/admin-graphql/latest/input-objects/CustomerInput#fields-firstName)

The customer's first name.

customer.last_name:"Lutke"

->[lastName](/docs/api/admin-graphql/latest/input-objects/CustomerInput#fields-lastName)

The customer's last name.

Creating a customer with an email that belongs to an existing customer returns an error

Request body

customer[](/apps/store/data-protection/protected-customer-data)

Customer resource**Customer resource**

Show customer properties

customer.email:"bob.norman@mail.example.com"

->[email](/docs/api/admin-graphql/latest/input-objects/CustomerInput#fields-email)

The unique email address of the customer. Attempting to assign the same email address to multiple customers returns an error.

customer.first_name:"Tobi"

->[firstName](/docs/api/admin-graphql/latest/input-objects/CustomerInput#fields-firstName)

The customer's first name.

customer.last_name:"Lutke"

->[lastName](/docs/api/admin-graphql/latest/input-objects/CustomerInput#fields-lastName)

The customer's last name.

Creating a customer without an email or name fails and returns an error

Request body

customer[](/apps/store/data-protection/protected-customer-data)

Customer resource**Customer resource**

Show customer properties

customer.email:null

->[email](/docs/api/admin-graphql/latest/input-objects/CustomerInput#fields-email)

The unique email address of the customer. Attempting to assign the same email address to multiple customers returns an error.

customer.first_name:null

->[firstName](/docs/api/admin-graphql/latest/input-objects/CustomerInput#fields-firstName)

The customer's first name.

customer.last_name:null

->[lastName](/docs/api/admin-graphql/latest/input-objects/CustomerInput#fields-lastName)

The customer's last name.

Was this section helpful?

YesNo

post

## /admin/api/2026-01/customers.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{"customer":{"first_name":"Steve","last_name":"Lastnameson","email":"steve.lastnameson@example.com","phone":"+15142546011","verified_email":true,"addresses":[{"address1":"123 Oak St","city":"Ottawa","province":"ON","phone":"555-1212","zip":"123 ABC","last_name":"Lastnameson","first_name":"Mother","country":"CA"}],"password":"newpass","password_confirmation":"newpass","send_email_welcome":false}}' \

-X POST "https://your-development-store.myshopify.com/admin/api/2026-01/customers.json" \

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

HTTP/1.1 201 Created

{

"customer": {

"first_name": "Steve",

"last_name": "Lastnameson",

"tax_exempt": false,

"id": 1073339531,

"created_at": "2026-01-09T20:48:28-05:00",

"updated_at": "2026-01-09T20:48:29-05:00",

"orders_count": 0,

"state": "enabled",

"total_spent": "0.00",

"last_order_id": null,

"note": null,

"verified_email": true,

"multipass_identifier": null,

"tags": "",

"last_order_name": null,

"email": "steve.lastnameson@example.com",

"phone": "+15142546011",

"currency": "USD",

"addresses": [

{

"id": 1053317355,

"customer_id": 1073339531,

"first_name": "Mother",

"last_name": "Lastnameson",

"company": null,

"address1": "123 Oak St",

"address2": null,

"city": "Ottawa",

"province": "Ontario",

"country": "Canada",

"zip": "123 ABC",

"phone": "555-1212",

"name": "Mother Lastnameson",

"province_code": "ON",

"country_code": "CA",

"country_name": "Canada",

"default": true

}

],

"tax_exemptions": [],

"email_marketing_consent": {

"state": "not_subscribed",

"opt_in_level": "single_opt_in",

"consent_updated_at": null

},

"sms_marketing_consent": {

"state": "not_subscribed",

"opt_in_level": "single_opt_in",

"consent_updated_at": null,

"consent_collected_from": "OTHER"

},

"admin_graphql_api_id": "gid://shopify/Customer/1073339531",

"default_address": {

"id": 1053317355,

"customer_id": 1073339531,

"first_name": "Mother",

"last_name": "Lastnameson",

"company": null,

"address1": "123 Oak St",

"address2": null,

"city": "Ottawa",

"province": "Ontario",

"country": "Canada",

"zip": "123 ABC",

"phone": "555-1212",

"name": "Mother Lastnameson",

"province_code": "ON",

"country_code": "CA",

"country_name": "Canada",

"default": true

}

}

}

### examples

  * #### Create a customer with <code>password</code> and <code>password_confirmation</code> and skip sending the welcome email

#####

        curl -d '{"customer":{"first_name":"Steve","last_name":"Lastnameson","email":"steve.lastnameson@example.com","phone":"+15142546011","verified_email":true,"addresses":[{"address1":"123 Oak St","city":"Ottawa","province":"ON","phone":"555-1212","zip":"123 ABC","last_name":"Lastnameson","first_name":"Mother","country":"CA"}],"password":"newpass","password_confirmation":"newpass","send_email_welcome":false}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/customers.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const customer = new admin.rest.resources.Customer({session: session});

        customer.first_name = "Steve";
        customer.last_name = "Lastnameson";
        customer.email = "steve.lastnameson@example.com";
        customer.phone = "+15142546011";
        customer.verified_email = true;
        customer.addresses = [
          {
            "address1": "123 Oak St",
            "city": "Ottawa",
            "province": "ON",
            "phone": "555-1212",
            "zip": "123 ABC",
            "last_name": "Lastnameson",
            "first_name": "Mother",
            "country": "CA"
          }
        ];
        customer.password = "newpass";
        customer.password_confirmation = "newpass";
        customer.send_email_welcome = false;
        await customer.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        customer = ShopifyAPI::Customer.new(session: test_session)
        customer.first_name = "Steve"
        customer.last_name = "Lastnameson"
        customer.email = "steve.lastnameson@example.com"
        customer.phone = "+15142546011"
        customer.verified_email = true
        customer.addresses = [
          {
            "address1" => "123 Oak St",
            "city" => "Ottawa",
            "province" => "ON",
            "phone" => "555-1212",
            "zip" => "123 ABC",
            "last_name" => "Lastnameson",
            "first_name" => "Mother",
            "country" => "CA"
          }
        ]
        customer.password = "newpass"
        customer.password_confirmation = "newpass"
        customer.send_email_welcome = false
        customer.save!

#####

        // Session is built by the OAuth process

        const customer = new shopify.rest.Customer({session: session});
        customer.first_name = "Steve";
        customer.last_name = "Lastnameson";
        customer.email = "steve.lastnameson@example.com";
        customer.phone = "+15142546011";
        customer.verified_email = true;
        customer.addresses = [
          {
            "address1": "123 Oak St",
            "city": "Ottawa",
            "province": "ON",
            "phone": "555-1212",
            "zip": "123 ABC",
            "last_name": "Lastnameson",
            "first_name": "Mother",
            "country": "CA"
          }
        ];
        customer.password = "newpass";
        customer.password_confirmation = "newpass";
        customer.send_email_welcome = false;
        await customer.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"customer":{"first_name":"Steve","last_name":"Lastnameson","tax_exempt":false,"id":1073339531,"created_at":"2026-01-09T20:48:28-05:00","updated_at":"2026-01-09T20:48:29-05:00","orders_count":0,"state":"enabled","total_spent":"0.00","last_order_id":null,"note":null,"verified_email":true,"multipass_identifier":null,"tags":"","last_order_name":null,"email":"steve.lastnameson@example.com","phone":"+15142546011","currency":"USD","addresses":[{"id":1053317355,"customer_id":1073339531,"first_name":"Mother","last_name":"Lastnameson","company":null,"address1":"123 Oak St","address2":null,"city":"Ottawa","province":"Ontario","country":"Canada","zip":"123 ABC","phone":"555-1212","name":"Mother Lastnameson","province_code":"ON","country_code":"CA","country_name":"Canada","default":true}],"tax_exemptions":[],"email_marketing_consent":{"state":"not_subscribed","opt_in_level":"single_opt_in","consent_updated_at":null},"sms_marketing_consent":{"state":"not_subscribed","opt_in_level":"single_opt_in","consent_updated_at":null,"consent_collected_from":"OTHER"},"admin_graphql_api_id":"gid://shopify/Customer/1073339531","default_address":{"id":1053317355,"customer_id":1073339531,"first_name":"Mother","last_name":"Lastnameson","company":null,"address1":"123 Oak St","address2":null,"city":"Ottawa","province":"Ontario","country":"Canada","zip":"123 ABC","phone":"555-1212","name":"Mother Lastnameson","province_code":"ON","country_code":"CA","country_name":"Canada","default":true}}}

  * #### Create a customer with <code>password</code> and <code>password_confirmation</code> and skip sending the welcome email

#####

        curl -d '{"customer":{"first_name":"Steve","last_name":"Lastnameson","email":"steve.lastnameson@example.com","phone":"+15142546011","verified_email":true,"addresses":[{"address1":"123 Oak St","city":"Ottawa","province":"ON","phone":"555-1212","zip":"123 ABC","last_name":"Lastnameson","first_name":"Mother","country":"CA"}],"password":"newpass","password_confirmation":"newpass","send_email_welcome":false}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/customers.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const customer = new admin.rest.resources.Customer({session: session});

        customer.first_name = "Steve";
        customer.last_name = "Lastnameson";
        customer.email = "steve.lastnameson@example.com";
        customer.phone = "+15142546011";
        customer.verified_email = true;
        customer.addresses = [
          {
            "address1": "123 Oak St",
            "city": "Ottawa",
            "province": "ON",
            "phone": "555-1212",
            "zip": "123 ABC",
            "last_name": "Lastnameson",
            "first_name": "Mother",
            "country": "CA"
          }
        ];
        customer.password = "newpass";
        customer.password_confirmation = "newpass";
        customer.send_email_welcome = false;
        await customer.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        customer = ShopifyAPI::Customer.new(session: test_session)
        customer.first_name = "Steve"
        customer.last_name = "Lastnameson"
        customer.email = "steve.lastnameson@example.com"
        customer.phone = "+15142546011"
        customer.verified_email = true
        customer.addresses = [
          {
            "address1" => "123 Oak St",
            "city" => "Ottawa",
            "province" => "ON",
            "phone" => "555-1212",
            "zip" => "123 ABC",
            "last_name" => "Lastnameson",
            "first_name" => "Mother",
            "country" => "CA"
          }
        ]
        customer.password = "newpass"
        customer.password_confirmation = "newpass"
        customer.send_email_welcome = false
        customer.save!

#####

        // Session is built by the OAuth process

        const customer = new shopify.rest.Customer({session: session});
        customer.first_name = "Steve";
        customer.last_name = "Lastnameson";
        customer.email = "steve.lastnameson@example.com";
        customer.phone = "+15142546011";
        customer.verified_email = true;
        customer.addresses = [
          {
            "address1": "123 Oak St",
            "city": "Ottawa",
            "province": "ON",
            "phone": "555-1212",
            "zip": "123 ABC",
            "last_name": "Lastnameson",
            "first_name": "Mother",
            "country": "CA"
          }
        ];
        customer.password = "newpass";
        customer.password_confirmation = "newpass";
        customer.send_email_welcome = false;
        await customer.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"customer":{"first_name":"Steve","last_name":"Lastnameson","tax_exempt":false,"updated_at":"2026-01-09T20:05:08-05:00","id":1073339525,"created_at":"2026-01-09T20:05:07-05:00","orders_count":0,"state":"enabled","total_spent":"0.00","last_order_id":null,"note":null,"verified_email":true,"multipass_identifier":null,"tags":"","last_order_name":null,"email":"steve.lastnameson@example.com","phone":"+15142546011","currency":"USD","addresses":[{"id":1053317351,"customer_id":1073339525,"first_name":"Mother","last_name":"Lastnameson","company":null,"address1":"123 Oak St","address2":null,"city":"Ottawa","province":"Ontario","country":"Canada","zip":"123 ABC","phone":"555-1212","name":"Mother Lastnameson","province_code":"ON","country_code":"CA","country_name":"Canada","default":true}],"tax_exemptions":[],"email_marketing_consent":{"state":"not_subscribed","opt_in_level":"single_opt_in","consent_updated_at":null},"sms_marketing_consent":{"state":"not_subscribed","opt_in_level":"single_opt_in","consent_updated_at":null,"consent_collected_from":"OTHER"},"admin_graphql_api_id":"gid://shopify/Customer/1073339525","default_address":{"id":1053317351,"customer_id":1073339525,"first_name":"Mother","last_name":"Lastnameson","company":null,"address1":"123 Oak St","address2":null,"city":"Ottawa","province":"Ontario","country":"Canada","zip":"123 ABC","phone":"555-1212","name":"Mother Lastnameson","province_code":"ON","country_code":"CA","country_name":"Canada","default":false}}}

  * #### Create a customer with a metafield

#####

        curl -d '{"customer":{"first_name":"Steve","last_name":"Lastnameson","email":"steve.lastnameson@example.com","phone":"+15142546011","verified_email":true,"addresses":[{"address1":"123 Oak St","city":"Ottawa","province":"ON","phone":"555-1212","zip":"123 ABC","last_name":"Lastnameson","first_name":"Mother","country":"CA"}],"metafields":[{"key":"new","value":"newvalue","type":"single_line_text_field","namespace":"global"}]}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/customers.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const customer = new admin.rest.resources.Customer({session: session});

        customer.first_name = "Steve";
        customer.last_name = "Lastnameson";
        customer.email = "steve.lastnameson@example.com";
        customer.phone = "+15142546011";
        customer.verified_email = true;
        customer.addresses = [
          {
            "address1": "123 Oak St",
            "city": "Ottawa",
            "province": "ON",
            "phone": "555-1212",
            "zip": "123 ABC",
            "last_name": "Lastnameson",
            "first_name": "Mother",
            "country": "CA"
          }
        ];
        customer.metafields = [
          {
            "key": "new",
            "value": "newvalue",
            "type": "single_line_text_field",
            "namespace": "global"
          }
        ];
        await customer.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        customer = ShopifyAPI::Customer.new(session: test_session)
        customer.first_name = "Steve"
        customer.last_name = "Lastnameson"
        customer.email = "steve.lastnameson@example.com"
        customer.phone = "+15142546011"
        customer.verified_email = true
        customer.addresses = [
          {
            "address1" => "123 Oak St",
            "city" => "Ottawa",
            "province" => "ON",
            "phone" => "555-1212",
            "zip" => "123 ABC",
            "last_name" => "Lastnameson",
            "first_name" => "Mother",
            "country" => "CA"
          }
        ]
        customer.metafields = [
          {
            "key" => "new",
            "value" => "newvalue",
            "type" => "single_line_text_field",
            "namespace" => "global"
          }
        ]
        customer.save!

#####

        // Session is built by the OAuth process

        const customer = new shopify.rest.Customer({session: session});
        customer.first_name = "Steve";
        customer.last_name = "Lastnameson";
        customer.email = "steve.lastnameson@example.com";
        customer.phone = "+15142546011";
        customer.verified_email = true;
        customer.addresses = [
          {
            "address1": "123 Oak St",
            "city": "Ottawa",
            "province": "ON",
            "phone": "555-1212",
            "zip": "123 ABC",
            "last_name": "Lastnameson",
            "first_name": "Mother",
            "country": "CA"
          }
        ];
        customer.metafields = [
          {
            "key": "new",
            "value": "newvalue",
            "type": "single_line_text_field",
            "namespace": "global"
          }
        ];
        await customer.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"customer":{"first_name":"Steve","last_name":"Lastnameson","tax_exempt":false,"id":1073339524,"created_at":"2026-01-09T19:47:31-05:00","updated_at":"2026-01-09T19:47:31-05:00","orders_count":0,"state":"disabled","total_spent":"0.00","last_order_id":null,"note":null,"verified_email":true,"multipass_identifier":null,"tags":"","last_order_name":null,"email":"steve.lastnameson@example.com","phone":"+15142546011","currency":"USD","addresses":[{"id":1053317350,"customer_id":1073339524,"first_name":"Mother","last_name":"Lastnameson","company":null,"address1":"123 Oak St","address2":null,"city":"Ottawa","province":"Ontario","country":"Canada","zip":"123 ABC","phone":"555-1212","name":"Mother Lastnameson","province_code":"ON","country_code":"CA","country_name":"Canada","default":true}],"tax_exemptions":[],"email_marketing_consent":{"state":"not_subscribed","opt_in_level":"single_opt_in","consent_updated_at":null},"sms_marketing_consent":{"state":"not_subscribed","opt_in_level":"single_opt_in","consent_updated_at":null,"consent_collected_from":"OTHER"},"admin_graphql_api_id":"gid://shopify/Customer/1073339524","default_address":{"id":1053317350,"customer_id":1073339524,"first_name":"Mother","last_name":"Lastnameson","company":null,"address1":"123 Oak St","address2":null,"city":"Ottawa","province":"Ontario","country":"Canada","zip":"123 ABC","phone":"555-1212","name":"Mother Lastnameson","province_code":"ON","country_code":"CA","country_name":"Canada","default":true}}}

  * #### Create a new customer record

#####

        curl -d '{"customer":{"first_name":"Steve","last_name":"Lastnameson","email":"steve.lastnameson@example.com","phone":"+15142546011","verified_email":true,"addresses":[{"address1":"123 Oak St","city":"Ottawa","province":"ON","phone":"555-1212","zip":"123 ABC","last_name":"Lastnameson","first_name":"Mother","country":"CA"}]}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/customers.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const customer = new admin.rest.resources.Customer({session: session});

        customer.first_name = "Steve";
        customer.last_name = "Lastnameson";
        customer.email = "steve.lastnameson@example.com";
        customer.phone = "+15142546011";
        customer.verified_email = true;
        customer.addresses = [
          {
            "address1": "123 Oak St",
            "city": "Ottawa",
            "province": "ON",
            "phone": "555-1212",
            "zip": "123 ABC",
            "last_name": "Lastnameson",
            "first_name": "Mother",
            "country": "CA"
          }
        ];
        await customer.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        customer = ShopifyAPI::Customer.new(session: test_session)
        customer.first_name = "Steve"
        customer.last_name = "Lastnameson"
        customer.email = "steve.lastnameson@example.com"
        customer.phone = "+15142546011"
        customer.verified_email = true
        customer.addresses = [
          {
            "address1" => "123 Oak St",
            "city" => "Ottawa",
            "province" => "ON",
            "phone" => "555-1212",
            "zip" => "123 ABC",
            "last_name" => "Lastnameson",
            "first_name" => "Mother",
            "country" => "CA"
          }
        ]
        customer.save!

#####

        // Session is built by the OAuth process

        const customer = new shopify.rest.Customer({session: session});
        customer.first_name = "Steve";
        customer.last_name = "Lastnameson";
        customer.email = "steve.lastnameson@example.com";
        customer.phone = "+15142546011";
        customer.verified_email = true;
        customer.addresses = [
          {
            "address1": "123 Oak St",
            "city": "Ottawa",
            "province": "ON",
            "phone": "555-1212",
            "zip": "123 ABC",
            "last_name": "Lastnameson",
            "first_name": "Mother",
            "country": "CA"
          }
        ];
        await customer.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"customer":{"first_name":"Steve","last_name":"Lastnameson","tax_exempt":false,"id":1073339534,"created_at":"2026-01-09T20:53:41-05:00","updated_at":"2026-01-09T20:53:41-05:00","orders_count":0,"state":"disabled","total_spent":"0.00","last_order_id":null,"note":null,"verified_email":true,"multipass_identifier":null,"tags":"","last_order_name":null,"email":"steve.lastnameson@example.com","phone":"+15142546011","currency":"USD","addresses":[{"id":1053317358,"customer_id":1073339534,"first_name":"Mother","last_name":"Lastnameson","company":null,"address1":"123 Oak St","address2":null,"city":"Ottawa","province":"Ontario","country":"Canada","zip":"123 ABC","phone":"555-1212","name":"Mother Lastnameson","province_code":"ON","country_code":"CA","country_name":"Canada","default":true}],"tax_exemptions":[],"email_marketing_consent":{"state":"not_subscribed","opt_in_level":"single_opt_in","consent_updated_at":null},"sms_marketing_consent":{"state":"not_subscribed","opt_in_level":"single_opt_in","consent_updated_at":null,"consent_collected_from":"OTHER"},"admin_graphql_api_id":"gid://shopify/Customer/1073339534","default_address":{"id":1053317358,"customer_id":1073339534,"first_name":"Mother","last_name":"Lastnameson","company":null,"address1":"123 Oak St","address2":null,"city":"Ottawa","province":"Ontario","country":"Canada","zip":"123 ABC","phone":"555-1212","name":"Mother Lastnameson","province_code":"ON","country_code":"CA","country_name":"Canada","default":true}}}

  * #### Create a new customer record

#####

        curl -d '{"customer":{"first_name":"Steve","last_name":"Lastnameson","email":"steve.lastnameson@example.com","phone":"+15142546011","verified_email":true,"addresses":[{"address1":"123 Oak St","city":"Ottawa","province":"ON","phone":"555-1212","zip":"123 ABC","last_name":"Lastnameson","first_name":"Mother","country":"CA"}]}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/customers.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const customer = new admin.rest.resources.Customer({session: session});

        customer.first_name = "Steve";
        customer.last_name = "Lastnameson";
        customer.email = "steve.lastnameson@example.com";
        customer.phone = "+15142546011";
        customer.verified_email = true;
        customer.addresses = [
          {
            "address1": "123 Oak St",
            "city": "Ottawa",
            "province": "ON",
            "phone": "555-1212",
            "zip": "123 ABC",
            "last_name": "Lastnameson",
            "first_name": "Mother",
            "country": "CA"
          }
        ];
        await customer.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        customer = ShopifyAPI::Customer.new(session: test_session)
        customer.first_name = "Steve"
        customer.last_name = "Lastnameson"
        customer.email = "steve.lastnameson@example.com"
        customer.phone = "+15142546011"
        customer.verified_email = true
        customer.addresses = [
          {
            "address1" => "123 Oak St",
            "city" => "Ottawa",
            "province" => "ON",
            "phone" => "555-1212",
            "zip" => "123 ABC",
            "last_name" => "Lastnameson",
            "first_name" => "Mother",
            "country" => "CA"
          }
        ]
        customer.save!

#####

        // Session is built by the OAuth process

        const customer = new shopify.rest.Customer({session: session});
        customer.first_name = "Steve";
        customer.last_name = "Lastnameson";
        customer.email = "steve.lastnameson@example.com";
        customer.phone = "+15142546011";
        customer.verified_email = true;
        customer.addresses = [
          {
            "address1": "123 Oak St",
            "city": "Ottawa",
            "province": "ON",
            "phone": "555-1212",
            "zip": "123 ABC",
            "last_name": "Lastnameson",
            "first_name": "Mother",
            "country": "CA"
          }
        ];
        await customer.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"customer":{"first_name":"Steve","last_name":"Lastnameson","tax_exempt":false,"updated_at":"2026-01-09T20:38:29-05:00","id":1073339528,"created_at":"2026-01-09T20:38:29-05:00","orders_count":0,"state":"disabled","total_spent":"0.00","last_order_id":null,"note":null,"verified_email":true,"multipass_identifier":null,"tags":"","last_order_name":null,"email":"steve.lastnameson@example.com","phone":"+15142546011","currency":"USD","addresses":[{"id":1053317353,"customer_id":1073339528,"first_name":"Mother","last_name":"Lastnameson","company":null,"address1":"123 Oak St","address2":null,"city":"Ottawa","province":"Ontario","country":"Canada","zip":"123 ABC","phone":"555-1212","name":"Mother Lastnameson","province_code":"ON","country_code":"CA","country_name":"Canada","default":true}],"tax_exemptions":[],"email_marketing_consent":{"state":"not_subscribed","opt_in_level":"single_opt_in","consent_updated_at":null},"sms_marketing_consent":{"state":"not_subscribed","opt_in_level":"single_opt_in","consent_updated_at":null,"consent_collected_from":"OTHER"},"admin_graphql_api_id":"gid://shopify/Customer/1073339528","default_address":{"id":1053317353,"customer_id":1073339528,"first_name":"Mother","last_name":"Lastnameson","company":null,"address1":"123 Oak St","address2":null,"city":"Ottawa","province":"Ontario","country":"Canada","zip":"123 ABC","phone":"555-1212","name":"Mother Lastnameson","province_code":"ON","country_code":"CA","country_name":"Canada","default":false}}}

  * #### Create a new customer record

#####

        curl -d '{"customer":{"first_name":"Steve","last_name":"Lastnameson","email":"steve.lastnameson@example.com","phone":"+15142546011","verified_email":true,"addresses":[{"address1":"123 Oak St","city":"Ottawa","province":"ON","phone":"555-1212","zip":"123 ABC","last_name":"Lastnameson","first_name":"Mother","country":"CA"}]}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/customers.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const customer = new admin.rest.resources.Customer({session: session});

        customer.first_name = "Steve";
        customer.last_name = "Lastnameson";
        customer.email = "steve.lastnameson@example.com";
        customer.phone = "+15142546011";
        customer.verified_email = true;
        customer.addresses = [
          {
            "address1": "123 Oak St",
            "city": "Ottawa",
            "province": "ON",
            "phone": "555-1212",
            "zip": "123 ABC",
            "last_name": "Lastnameson",
            "first_name": "Mother",
            "country": "CA"
          }
        ];
        await customer.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        customer = ShopifyAPI::Customer.new(session: test_session)
        customer.first_name = "Steve"
        customer.last_name = "Lastnameson"
        customer.email = "steve.lastnameson@example.com"
        customer.phone = "+15142546011"
        customer.verified_email = true
        customer.addresses = [
          {
            "address1" => "123 Oak St",
            "city" => "Ottawa",
            "province" => "ON",
            "phone" => "555-1212",
            "zip" => "123 ABC",
            "last_name" => "Lastnameson",
            "first_name" => "Mother",
            "country" => "CA"
          }
        ]
        customer.save!

#####

        // Session is built by the OAuth process

        const customer = new shopify.rest.Customer({session: session});
        customer.first_name = "Steve";
        customer.last_name = "Lastnameson";
        customer.email = "steve.lastnameson@example.com";
        customer.phone = "+15142546011";
        customer.verified_email = true;
        customer.addresses = [
          {
            "address1": "123 Oak St",
            "city": "Ottawa",
            "province": "ON",
            "phone": "555-1212",
            "zip": "123 ABC",
            "last_name": "Lastnameson",
            "first_name": "Mother",
            "country": "CA"
          }
        ];
        await customer.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"customer":{"first_name":"Steve","last_name":"Lastnameson","tax_exempt":false,"id":1073339529,"created_at":"2026-01-09T20:48:01-05:00","updated_at":"2026-01-09T20:48:01-05:00","orders_count":0,"state":"disabled","total_spent":"0.00","last_order_id":null,"note":null,"verified_email":true,"multipass_identifier":null,"tags":"","last_order_name":null,"email":"steve.lastnameson@example.com","phone":"+15142546011","currency":"USD","addresses":[{"id":1053317354,"customer_id":1073339529,"first_name":"Mother","last_name":"Lastnameson","company":null,"address1":"123 Oak St","address2":null,"city":"Ottawa","province":"Ontario","country":"Canada","zip":"123 ABC","phone":"555-1212","name":"Mother Lastnameson","province_code":"ON","country_code":"CA","country_name":"Canada","default":true}],"tax_exemptions":[],"email_marketing_consent":{"state":"not_subscribed","opt_in_level":"single_opt_in","consent_updated_at":null},"sms_marketing_consent":{"state":"not_subscribed","opt_in_level":"single_opt_in","consent_updated_at":null,"consent_collected_from":"OTHER"},"admin_graphql_api_id":"gid://shopify/Customer/1073339529","default_address":{"id":1053317354,"customer_id":1073339529,"first_name":"Mother","last_name":"Lastnameson","company":null,"address1":"123 Oak St","address2":null,"city":"Ottawa","province":"Ontario","country":"Canada","zip":"123 ABC","phone":"555-1212","name":"Mother Lastnameson","province_code":"ON","country_code":"CA","country_name":"Canada","default":true}}}

  * #### Creating a customer with an email that belongs to an existing customer returns an error

#####

        curl -d '{"customer":{"email":"bob.norman@mail.example.com","first_name":"Tobi","last_name":"Lutke"}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/customers.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const customer = new admin.rest.resources.Customer({session: session});

        customer.email = "bob.norman@mail.example.com";
        customer.first_name = "Tobi";
        customer.last_name = "Lutke";
        await customer.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        customer = ShopifyAPI::Customer.new(session: test_session)
        customer.email = "bob.norman@mail.example.com"
        customer.first_name = "Tobi"
        customer.last_name = "Lutke"
        customer.save!

#####

        // Session is built by the OAuth process

        const customer = new shopify.rest.Customer({session: session});
        customer.email = "bob.norman@mail.example.com";
        customer.first_name = "Tobi";
        customer.last_name = "Lutke";
        await customer.save({
          update: true,
        });

#### response

        HTTP/1.1 422 Unprocessable Entity{"errors":{"email":["has already been taken"]}}

  * #### Creating a customer with an email that belongs to an existing customer returns an error

#####

        curl -d '{"customer":{"email":"bob.norman@mail.example.com","first_name":"Tobi","last_name":"Lutke"}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/customers.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const customer = new admin.rest.resources.Customer({session: session});

        customer.email = "bob.norman@mail.example.com";
        customer.first_name = "Tobi";
        customer.last_name = "Lutke";
        await customer.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        customer = ShopifyAPI::Customer.new(session: test_session)
        customer.email = "bob.norman@mail.example.com"
        customer.first_name = "Tobi"
        customer.last_name = "Lutke"
        customer.save!

#####

        // Session is built by the OAuth process

        const customer = new shopify.rest.Customer({session: session});
        customer.email = "bob.norman@mail.example.com";
        customer.first_name = "Tobi";
        customer.last_name = "Lutke";
        await customer.save({
          update: true,
        });

#### response

        HTTP/1.1 422 Unprocessable Entity{"errors":{"email":["has already been taken"]}}

  * #### Creating a customer without an email or name fails and returns an error

#####

        curl -d '{"customer":{"email":null,"first_name":null,"last_name":null}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/customers.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const customer = new admin.rest.resources.Customer({session: session});

        customer.email = null;
        customer.first_name = null;
        customer.last_name = null;
        await customer.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        customer = ShopifyAPI::Customer.new(session: test_session)
        customer.email = nil
        customer.first_name = nil
        customer.last_name = nil
        customer.save!

#####

        // Session is built by the OAuth process

        const customer = new shopify.rest.Customer({session: session});
        customer.email = null;
        customer.first_name = null;
        customer.last_name = null;
        await customer.save({
          update: true,
        });

#### response

        HTTP/1.1 422 Unprocessable Entity{"errors":{"base":["A name, phone number, or email address must be present"]}}


* * *

##

[Anchor to POST request, Creates an account activation URL for a customer](/docs/api/admin-rest/latest/resources/customer#post-customers-customer-id-account-activation-url)

post

Creates an account activation URL for a customer

[customerGenerateAccountActivationUrl](/docs/api/admin-graphql/latest/mutations/customerGenerateAccountActivationUrl?example=creates-an-account-activation-url-for-a-customer)

Requires `customers` access scope.

**Requires `customers` access scope.:**

Generate an account activation URL for a customer whose account is not yet enabled. This is useful when you've imported a large number of customers and want to send them activation emails all at once. Using this approach, you'll need to generate and send the activation emails yourself.

The account activation URL generated by this endpoint is for one-time use and will expire after 30 days. If you make a new POST request to this endpoint, then a new URL will be generated. The new URL will be again valid for 30 days, but the previous URL will no longer be valid.

###

[Anchor to Parameters of Creates an account activation URL for a customer](/docs/api/admin-rest/latest/resources/customer#post-customers-customer-id-account-activation-url-parameters)Parameters

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

[Anchor to post-customers-customer-id-account-activation-url-examples](/docs/api/admin-rest/latest/resources/customer#post-customers-customer-id-account-activation-url-examples)Examples

Create an account activation URL for an invited or disabled customer

Path parameters

customer_id=207119551

string**string**

required**required**

Creating an account activation URL for an enabled customer fails and returns an error

Path parameters

customer_id=207119551

string**string**

required**required**

Creating an account activation URL for an enabled customer fails and returns an error

Path parameters

customer_id=207119551

string**string**

required**required**

Was this section helpful?

YesNo

post

## /admin/api/2026-01/customers/207119551/account_activation_url.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{}' \

-X POST "https://your-development-store.myshopify.com/admin/api/2026-01/customers/207119551/account_activation_url.json" \

-H "X-Shopify-Access-Token: {access_token}" \

-H "Content-Type: application/json"

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

"account_activation_url": "https://jsmith.myshopify.com/account/activate/207119551/535f3addaea3e52ee2617c3416c309cd-1768008075"

}

### examples

  * #### Create an account activation URL for an invited or disabled customer

#####

        curl -d '{}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/customers/207119551/account_activation_url.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const customer = new admin.rest.resources.Customer({session: session});

        customer.id = 207119551;
        await customer.account_activation_url({});

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        customer = ShopifyAPI::Customer.new(session: test_session)
        customer.id = 207119551
        customer.account_activation_url(
          session: test_session,
        )

#####

        // Session is built by the OAuth process

        const customer = new shopify.rest.Customer({session: session});
        customer.id = 207119551;
        await customer.account_activation_url({});

#### response

        HTTP/1.1 200 OK{"account_activation_url":"https://jsmith.myshopify.com/account/activate/207119551/535f3addaea3e52ee2617c3416c309cd-1768008075"}

  * #### Creating an account activation URL for an enabled customer fails and returns an error

#####

        curl -d '{}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/customers/207119551/account_activation_url.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const customer = new admin.rest.resources.Customer({session: session});

        customer.id = 207119551;
        await customer.account_activation_url({});

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        customer = ShopifyAPI::Customer.new(session: test_session)
        customer.id = 207119551
        customer.account_activation_url(
          session: test_session,
        )

#####

        // Session is built by the OAuth process

        const customer = new shopify.rest.Customer({session: session});
        customer.id = 207119551;
        await customer.account_activation_url({});

#### response

        HTTP/1.1 422 Unprocessable Entity{"errors":["account already enabled"]}

  * #### Creating an account activation URL for an enabled customer fails and returns an error

#####

        curl -d '{}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/customers/207119551/account_activation_url.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const customer = new admin.rest.resources.Customer({session: session});

        customer.id = 207119551;
        await customer.account_activation_url({});

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        customer = ShopifyAPI::Customer.new(session: test_session)
        customer.id = 207119551
        customer.account_activation_url(
          session: test_session,
        )

#####

        // Session is built by the OAuth process

        const customer = new shopify.rest.Customer({session: session});
        customer.id = 207119551;
        await customer.account_activation_url({});

#### response

        HTTP/1.1 422 Unprocessable Entity{"errors":["account already enabled"]}


* * *

##

[Anchor to POST request, Sends an account invite to a customer](/docs/api/admin-rest/latest/resources/customer#post-customers-customer-id-send-invite)

post

Sends an account invite to a customer

[customerSendAccountInviteEmail](/docs/api/admin-graphql/latest/mutations/customerSendAccountInviteEmail?example=sends-an-account-invite-to-a-customer)

Requires `customers` access scope.

**Requires `customers` access scope.:**

Sends an account invite to a customer.

###

[Anchor to Parameters of Sends an account invite to a customer](/docs/api/admin-rest/latest/resources/customer#post-customers-customer-id-send-invite-parameters)Parameters

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

[Anchor to post-customers-customer-id-send-invite-examples](/docs/api/admin-rest/latest/resources/customer#post-customers-customer-id-send-invite-examples)Examples

Send a customized invite

Path parameters

customer_id=207119551

string**string**

required**required**

Send the default invite

Path parameters

customer_id=207119551

string**string**

required**required**

Was this section helpful?

YesNo

post

## /admin/api/2026-01/customers/207119551/send_invite.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{"customer_invite":{"to":"new_test_email@shopify.com","from":"j.limited@example.com","bcc":["j.limited@example.com"],"subject":"Welcome to my new shop","custom_message":"My awesome new store"}}' \

-X POST "https://your-development-store.myshopify.com/admin/api/2026-01/customers/207119551/send_invite.json" \

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

HTTP/1.1 201 Created

{

"customer_invite": {

"to": "new_test_email@shopify.com",

"from": "j.limited@example.com",

"subject": "Welcome to my new shop",

"custom_message": "My awesome new store",

"bcc": [

"j.limited@example.com"

]

}

}

### examples

  * #### Send a customized invite

#####

        curl -d '{"customer_invite":{"to":"new_test_email@shopify.com","from":"j.limited@example.com","bcc":["j.limited@example.com"],"subject":"Welcome to my new shop","custom_message":"My awesome new store"}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/customers/207119551/send_invite.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const customer = new admin.rest.resources.Customer({session: session});

        customer.id = 207119551;
        await customer.send_invite({
          body: {"customer_invite": {"to": "new_test_email@shopify.com", "from": "j.limited@example.com", "bcc": ["j.limited@example.com"], "subject": "Welcome to my new shop", "custom_message": "My awesome new store"}},
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        customer = ShopifyAPI::Customer.new(session: test_session)
        customer.id = 207119551
        customer.send_invite(
          session: test_session,
          body: {"customer_invite" => {"to" => "new_test_email@shopify.com", "from" => "j.limited@example.com", "bcc" => ["j.limited@example.com"], "subject" => "Welcome to my new shop", "custom_message" => "My awesome new store"}},
        )

#####

        // Session is built by the OAuth process

        const customer = new shopify.rest.Customer({session: session});
        customer.id = 207119551;
        await customer.send_invite({
          body: {"customer_invite": {"to": "new_test_email@shopify.com", "from": "j.limited@example.com", "bcc": ["j.limited@example.com"], "subject": "Welcome to my new shop", "custom_message": "My awesome new store"}},
        });

#### response

        HTTP/1.1 201 Created{"customer_invite":{"to":"new_test_email@shopify.com","from":"j.limited@example.com","subject":"Welcome to my new shop","custom_message":"My awesome new store","bcc":["j.limited@example.com"]}}

  * #### Send the default invite

#####

        curl -d '{"customer_invite":{}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/customers/207119551/send_invite.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const customer = new admin.rest.resources.Customer({session: session});

        customer.id = 207119551;
        await customer.send_invite({
          body: {"customer_invite": {}},
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        customer = ShopifyAPI::Customer.new(session: test_session)
        customer.id = 207119551
        customer.send_invite(
          session: test_session,
          body: {"customer_invite" => {}},
        )

#####

        // Session is built by the OAuth process

        const customer = new shopify.rest.Customer({session: session});
        customer.id = 207119551;
        await customer.send_invite({
          body: {"customer_invite": {}},
        });

#### response

        HTTP/1.1 201 Created{"customer_invite":{"to":"bob.norman@mail.example.com","from":"j.smith@example.com","subject":"Customer account activation","custom_message":"","bcc":[]}}


* * *

##

[Anchor to GET request, Retrieves a list of customers](/docs/api/admin-rest/latest/resources/customer#get-customers?ids=207119551,562393516,688973684,1073339533)

get

Retrieves a list of customers

[customers](/docs/api/admin-graphql/latest/queries/customers)

Requires `customers` access scope.

**Requires `customers` access scope.:**

Retrieves a list of customers. **Note:** This endpoint implements pagination by using links that are provided in the response header. To learn more, refer to [Make paginated requests to the REST Admin API](/api/usage/pagination-rest).

###

[Anchor to Parameters of Retrieves a list of customers](/docs/api/admin-rest/latest/resources/customer#get-customers?ids=207119551,562393516,688973684,1073339533-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

created_at_max

Show customers created before a specified date.
(format: 2014-04-25T16:15:47-04:00)

* * *

created_after

Show customers created after a specified date.
(format: 2014-04-25T16:15:47-04:00)

* * *

fields

Show only certain fields, specified by a comma-separated list of field names.

* * *

ids

Restrict results to customers specified by a comma-separated list of IDs.

* * *

count

≤ 250**≤ 250**

default 50**default 50**

The maximum number of results to show.

* * *

after_id

Restrict results to those after the specified ID.

* * *

updated_at_max

Show customers last updated before a specified date.
(format: 2014-04-25T16:15:47-04:00)

* * *

updated_at_min

Show customers last updated after a specified date.
(format: 2014-04-25T16:15:47-04:00)

* * *

Was this section helpful?

YesNo

###

[Anchor to get-customers?ids=207119551,562393516,688973684,1073339533-examples](/docs/api/admin-rest/latest/resources/customer#get-customers?ids=207119551,562393516,688973684,1073339533-examples)Examples

Retrieve a list of specific customers

Query parameters

ids=207119551,562393516,688973684,1073339533

Restrict results to customers specified by a comma-separated list of IDs.

Retrieve all customers after a specified ID

Query parameters

after_id=207119551

Restrict results to those after the specified ID.

Retrieve all customers after a specified ID

Query parameters

after_id=207119551

Restrict results to those after the specified ID.

Retrieve all customers after a specified ID

Query parameters

after_id=207119551

Restrict results to those after the specified ID.

Retrieve all customers changed after a certain date

Query parameters

updated_at_min=2026-01-09+01:38:40

Show customers last updated after a specified date.
(format: 2014-04-25T16:15:47-04:00)

Retrieve all customers for a shop

Retrieve only the specified customer fields

Query parameters

fields=id,tags,email

Show only certain fields, specified by a comma-separated list of field names.

Was this section helpful?

YesNo

get

## /admin/api/2026-01/customers.json?ids=207119551,562393516,688973684,1073339533

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/customers.json?ids=207119551%2C562393516%2C688973684%2C1073339533" \

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

"customers": [

{

"id": 1073339533,

"created_at": "2026-01-09T20:53:29-05:00",

"updated_at": "2026-01-09T20:53:29-05:00",

"first_name": "Steve",

"last_name": "Lastnameson",

"orders_count": 0,

"state": "disabled",

"total_spent": "0.00",

"last_order_id": null,

"note": null,

"verified_email": true,

"multipass_identifier": null,

"tax_exempt": false,

"tags": "",

"last_order_name": null,

"email": "steve.lastnameson@example.com",

"phone": "+15142546011",

"currency": "USD",

"addresses": [

{

"id": 1053317357,

"customer_id": 1073339533,

"first_name": "Mother",

"last_name": "Lastnameson",

"company": null,

"address1": "123 Oak St",

"address2": null,

"city": "Ottawa",

"province": "Ontario",

"country": "Canada",

"zip": "123 ABC",

"phone": "555-1212",

### examples

  * #### Retrieve a list of specific customers

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/customers.json?ids=207119551%2C562393516%2C688973684%2C1073339533" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Customer.all({
          session: session,
          ids: "207119551,562393516,688973684,1073339533",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Customer.all(
          session: test_session,
          ids: "207119551,562393516,688973684,1073339533",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Customer.all({
          session: session,
          ids: "207119551,562393516,688973684,1073339533",
        });

#### response

        HTTP/1.1 200 OK{"customers":[{"id":1073339533,"created_at":"2026-01-09T20:53:29-05:00","updated_at":"2026-01-09T20:53:29-05:00","first_name":"Steve","last_name":"Lastnameson","orders_count":0,"state":"disabled","total_spent":"0.00","last_order_id":null,"note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"tags":"","last_order_name":null,"email":"steve.lastnameson@example.com","phone":"+15142546011","currency":"USD","addresses":[{"id":1053317357,"customer_id":1073339533,"first_name":"Mother","last_name":"Lastnameson","company":null,"address1":"123 Oak St","address2":null,"city":"Ottawa","province":"Ontario","country":"Canada","zip":"123 ABC","phone":"555-1212","name":"Mother Lastnameson","province_code":"ON","country_code":"CA","country_name":"Canada","default":true}],"tax_exemptions":[],"email_marketing_consent":{"state":"not_subscribed","opt_in_level":"single_opt_in","consent_updated_at":null},"sms_marketing_consent":{"state":"not_subscribed","opt_in_level":"single_opt_in","consent_updated_at":null,"consent_collected_from":"OTHER"},"admin_graphql_api_id":"gid://shopify/Customer/1073339533","default_address":{"id":1053317357,"customer_id":1073339533,"first_name":"Mother","last_name":"Lastnameson","company":null,"address1":"123 Oak St","address2":null,"city":"Ottawa","province":"Ontario","country":"Canada","zip":"123 ABC","phone":"555-1212","name":"Mother Lastnameson","province_code":"ON","country_code":"CA","country_name":"Canada","default":true}},{"id":688973684,"created_at":"2026-01-09T20:53:19-05:00","updated_at":"2026-01-09T20:53:19-05:00","first_name":"Bob","last_name":"Norman Invalid","orders_count":0,"state":"disabled","total_spent":"0.00","last_order_id":null,"note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"tags":"","last_order_name":null,"email":"bob.norman.invalid@mail.example.de","phone":null,"currency":"USD","addresses":[],"tax_exemptions":[],"email_marketing_consent":{"state":"invalid","opt_in_level":null,"consent_updated_at":null},"sms_marketing_consent":null,"admin_graphql_api_id":"gid://shopify/Customer/688973684"},{"id":562393516,"created_at":"2026-01-09T20:53:19-05:00","updated_at":"2026-01-09T20:53:19-05:00","first_name":"Dom","last_name":"Toretto","orders_count":0,"state":"disabled","total_spent":"199.65","last_order_id":450789469,"note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"tags":"","last_order_name":"#1001","email":"dom.toretto@mail.example.com","phone":"+12016251199","currency":"USD","addresses":[{"id":562393516,"customer_id":562393516,"first_name":"Dom","last_name":"Toretto","company":null,"address1":"Chestnut Street 93","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"+1(201)625-1199","name":"Dom Toretto","province_code":"KY","country_code":"US","country_name":"United States","default":true}],"tax_exemptions":[],"email_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null},"sms_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null,"consent_collected_from":"OTHER"},"admin_graphql_api_id":"gid://shopify/Customer/562393516","default_address":{"id":562393516,"customer_id":562393516,"first_name":"Dom","last_name":"Toretto","company":null,"address1":"Chestnut Street 93","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"+1(201)625-1199","name":"Dom Toretto","province_code":"KY","country_code":"US","country_name":"United States","default":true}},{"id":207119551,"created_at":"2026-01-09T20:53:19-05:00","updated_at":"2026-01-09T20:53:19-05:00","first_name":"Bob","last_name":"Norman","orders_count":1,"state":"disabled","total_spent":"199.65","last_order_id":450789469,"note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"tags":"Léon, Noël","last_order_name":"#1001","email":"bob.norman@mail.example.com","phone":"+16136120707","currency":"USD","addresses":[{"id":207119551,"customer_id":207119551,"first_name":null,"last_name":null,"company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"555-625-1199","name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}],"tax_exemptions":[],"email_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null},"sms_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null,"consent_collected_from":"OTHER"},"admin_graphql_api_id":"gid://shopify/Customer/207119551","default_address":{"id":207119551,"customer_id":207119551,"first_name":null,"last_name":null,"company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"555-625-1199","name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}}]}

  * #### Retrieve all customers after a specified ID

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/customers.json?after_id=207119551" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Customer.all({
          session: session,
          after_id: "207119551",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Customer.all(
          session: test_session,
          after_id: "207119551",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Customer.all({
          session: session,
          after_id: "207119551",
        });

#### response

        HTTP/1.1 200 OK{"customers":[{"id":562393516,"created_at":"2026-01-09T20:21:25-05:00","updated_at":"2026-01-09T20:21:25-05:00","first_name":"Dom","last_name":"Toretto","orders_count":0,"state":"disabled","total_spent":"199.65","last_order_id":450789469,"note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"tags":"","last_order_name":"#1001","email":"dom.toretto@mail.example.com","phone":"+12016251199","currency":"USD","addresses":[{"id":562393516,"customer_id":562393516,"first_name":"Dom","last_name":"Toretto","company":null,"address1":"Chestnut Street 93","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"+1(201)625-1199","name":"Dom Toretto","province_code":"KY","country_code":"US","country_name":"United States","default":true}],"tax_exemptions":[],"email_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null},"sms_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null,"consent_collected_from":"OTHER"},"admin_graphql_api_id":"gid://shopify/Customer/562393516","default_address":{"id":562393516,"customer_id":562393516,"first_name":"Dom","last_name":"Toretto","company":null,"address1":"Chestnut Street 93","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"+1(201)625-1199","name":"Dom Toretto","province_code":"KY","country_code":"US","country_name":"United States","default":true}},{"id":688973684,"created_at":"2026-01-09T20:21:25-05:00","updated_at":"2026-01-09T20:21:25-05:00","first_name":"Bob","last_name":"Norman Invalid","orders_count":0,"state":"disabled","total_spent":"0.00","last_order_id":null,"note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"tags":"","last_order_name":null,"email":"bob.norman.invalid@mail.example.de","phone":null,"currency":"USD","addresses":[],"tax_exemptions":[],"email_marketing_consent":{"state":"invalid","opt_in_level":null,"consent_updated_at":null},"sms_marketing_consent":null,"admin_graphql_api_id":"gid://shopify/Customer/688973684"},{"id":1073339527,"created_at":"2026-01-09T20:21:34-05:00","updated_at":"2026-01-09T20:21:34-05:00","first_name":"Steve","last_name":"Lastnameson","orders_count":0,"state":"disabled","total_spent":"0.00","last_order_id":null,"note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"tags":"","last_order_name":null,"email":"steve.lastnameson@example.com","phone":"+15142546011","currency":"USD","addresses":[{"id":1053317352,"customer_id":1073339527,"first_name":"Mother","last_name":"Lastnameson","company":null,"address1":"123 Oak St","address2":null,"city":"Ottawa","province":"Ontario","country":"Canada","zip":"123 ABC","phone":"555-1212","name":"Mother Lastnameson","province_code":"ON","country_code":"CA","country_name":"Canada","default":true}],"tax_exemptions":[],"email_marketing_consent":{"state":"not_subscribed","opt_in_level":"single_opt_in","consent_updated_at":null},"sms_marketing_consent":{"state":"not_subscribed","opt_in_level":"single_opt_in","consent_updated_at":null,"consent_collected_from":"OTHER"},"admin_graphql_api_id":"gid://shopify/Customer/1073339527","default_address":{"id":1053317352,"customer_id":1073339527,"first_name":"Mother","last_name":"Lastnameson","company":null,"address1":"123 Oak St","address2":null,"city":"Ottawa","province":"Ontario","country":"Canada","zip":"123 ABC","phone":"555-1212","name":"Mother Lastnameson","province_code":"ON","country_code":"CA","country_name":"Canada","default":true}}]}

  * #### Retrieve all customers after a specified ID

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/customers.json?after_id=207119551" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Customer.all({
          session: session,
          after_id: "207119551",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Customer.all(
          session: test_session,
          after_id: "207119551",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Customer.all({
          session: session,
          after_id: "207119551",
        });

#### response

        HTTP/1.1 200 OK{"customers":[{"id":562393516,"created_at":"2026-01-09T20:48:29-05:00","updated_at":"2026-01-09T20:48:29-05:00","first_name":"Dom","last_name":"Toretto","orders_count":0,"state":"disabled","total_spent":"199.65","last_order_id":450789469,"note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"tags":"","last_order_name":"#1001","email":"dom.toretto@mail.example.com","phone":"+12016251199","currency":"USD","addresses":[{"id":562393516,"customer_id":562393516,"first_name":"Dom","last_name":"Toretto","company":null,"address1":"Chestnut Street 93","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"+1(201)625-1199","name":"Dom Toretto","province_code":"KY","country_code":"US","country_name":"United States","default":true}],"tax_exemptions":[],"email_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null},"sms_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null,"consent_collected_from":"OTHER"},"admin_graphql_api_id":"gid://shopify/Customer/562393516","default_address":{"id":562393516,"customer_id":562393516,"first_name":"Dom","last_name":"Toretto","company":null,"address1":"Chestnut Street 93","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"+1(201)625-1199","name":"Dom Toretto","province_code":"KY","country_code":"US","country_name":"United States","default":true}},{"id":688973684,"created_at":"2026-01-09T20:48:29-05:00","updated_at":"2026-01-09T20:48:29-05:00","first_name":"Bob","last_name":"Norman Invalid","orders_count":0,"state":"disabled","total_spent":"0.00","last_order_id":null,"note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"tags":"","last_order_name":null,"email":"bob.norman.invalid@mail.example.de","phone":null,"currency":"USD","addresses":[],"tax_exemptions":[],"email_marketing_consent":{"state":"invalid","opt_in_level":null,"consent_updated_at":null},"sms_marketing_consent":null,"admin_graphql_api_id":"gid://shopify/Customer/688973684"},{"id":1073339532,"created_at":"2026-01-09T20:48:38-05:00","updated_at":"2026-01-09T20:48:38-05:00","first_name":"Steve","last_name":"Lastnameson","orders_count":0,"state":"disabled","total_spent":"0.00","last_order_id":null,"note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"tags":"","last_order_name":null,"email":"steve.lastnameson@example.com","phone":"+15142546011","currency":"USD","addresses":[{"id":1053317356,"customer_id":1073339532,"first_name":"Mother","last_name":"Lastnameson","company":null,"address1":"123 Oak St","address2":null,"city":"Ottawa","province":"Ontario","country":"Canada","zip":"123 ABC","phone":"555-1212","name":"Mother Lastnameson","province_code":"ON","country_code":"CA","country_name":"Canada","default":true}],"tax_exemptions":[],"email_marketing_consent":{"state":"not_subscribed","opt_in_level":"single_opt_in","consent_updated_at":null},"sms_marketing_consent":{"state":"not_subscribed","opt_in_level":"single_opt_in","consent_updated_at":null,"consent_collected_from":"OTHER"},"admin_graphql_api_id":"gid://shopify/Customer/1073339532","default_address":{"id":1053317356,"customer_id":1073339532,"first_name":"Mother","last_name":"Lastnameson","company":null,"address1":"123 Oak St","address2":null,"city":"Ottawa","province":"Ontario","country":"Canada","zip":"123 ABC","phone":"555-1212","name":"Mother Lastnameson","province_code":"ON","country_code":"CA","country_name":"Canada","default":true}}]}

  * #### Retrieve all customers after a specified ID

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/customers.json?after_id=207119551" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Customer.all({
          session: session,
          after_id: "207119551",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Customer.all(
          session: test_session,
          after_id: "207119551",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Customer.all({
          session: session,
          after_id: "207119551",
        });

#### response

        HTTP/1.1 200 OK{"customers":[{"id":562393516,"created_at":"2026-01-09T21:10:44-05:00","updated_at":"2026-01-09T21:10:44-05:00","first_name":"Dom","last_name":"Toretto","orders_count":0,"state":"disabled","total_spent":"199.65","last_order_id":450789469,"note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"tags":"","last_order_name":"#1001","email":"dom.toretto@mail.example.com","phone":"+12016251199","currency":"USD","addresses":[{"id":562393516,"customer_id":562393516,"first_name":"Dom","last_name":"Toretto","company":null,"address1":"Chestnut Street 93","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"+1(201)625-1199","name":"Dom Toretto","province_code":"KY","country_code":"US","country_name":"United States","default":true}],"tax_exemptions":[],"email_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null},"sms_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null,"consent_collected_from":"OTHER"},"admin_graphql_api_id":"gid://shopify/Customer/562393516","default_address":{"id":562393516,"customer_id":562393516,"first_name":"Dom","last_name":"Toretto","company":null,"address1":"Chestnut Street 93","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"+1(201)625-1199","name":"Dom Toretto","province_code":"KY","country_code":"US","country_name":"United States","default":true}},{"id":688973684,"created_at":"2026-01-09T21:10:44-05:00","updated_at":"2026-01-09T21:10:44-05:00","first_name":"Bob","last_name":"Norman Invalid","orders_count":0,"state":"disabled","total_spent":"0.00","last_order_id":null,"note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"tags":"","last_order_name":null,"email":"bob.norman.invalid@mail.example.de","phone":null,"currency":"USD","addresses":[],"tax_exemptions":[],"email_marketing_consent":{"state":"invalid","opt_in_level":null,"consent_updated_at":null},"sms_marketing_consent":null,"admin_graphql_api_id":"gid://shopify/Customer/688973684"},{"id":1073339535,"created_at":"2026-01-09T21:10:55-05:00","updated_at":"2026-01-09T21:10:55-05:00","first_name":"Steve","last_name":"Lastnameson","orders_count":0,"state":"disabled","total_spent":"0.00","last_order_id":null,"note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"tags":"","last_order_name":null,"email":"steve.lastnameson@example.com","phone":"+15142546011","currency":"USD","addresses":[{"id":1053317359,"customer_id":1073339535,"first_name":"Mother","last_name":"Lastnameson","company":null,"address1":"123 Oak St","address2":null,"city":"Ottawa","province":"Ontario","country":"Canada","zip":"123 ABC","phone":"555-1212","name":"Mother Lastnameson","province_code":"ON","country_code":"CA","country_name":"Canada","default":true}],"tax_exemptions":[],"email_marketing_consent":{"state":"not_subscribed","opt_in_level":"single_opt_in","consent_updated_at":null},"sms_marketing_consent":{"state":"not_subscribed","opt_in_level":"single_opt_in","consent_updated_at":null,"consent_collected_from":"OTHER"},"admin_graphql_api_id":"gid://shopify/Customer/1073339535","default_address":{"id":1053317359,"customer_id":1073339535,"first_name":"Mother","last_name":"Lastnameson","company":null,"address1":"123 Oak St","address2":null,"city":"Ottawa","province":"Ontario","country":"Canada","zip":"123 ABC","phone":"555-1212","name":"Mother Lastnameson","province_code":"ON","country_code":"CA","country_name":"Canada","default":true}}]}

  * #### Retrieve all customers changed after a certain date

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/customers.json?updated_at_min=2026-01-09+01%3A38%3A40" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Customer.all({
          session: session,
          updated_at_min: "2026-01-09 01:38:40",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Customer.all(
          session: test_session,
          updated_at_min: "2026-01-09 01:38:40",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Customer.all({
          session: session,
          updated_at_min: "2026-01-09 01:38:40",
        });

#### response

        HTTP/1.1 200 OK{"customers":[{"id":688973684,"created_at":"2026-01-09T20:38:29-05:00","updated_at":"2026-01-09T20:38:29-05:00","first_name":"Bob","last_name":"Norman Invalid","orders_count":0,"state":"disabled","total_spent":"0.00","last_order_id":null,"note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"tags":"","last_order_name":null,"email":"bob.norman.invalid@mail.example.de","phone":null,"currency":"USD","addresses":[],"tax_exemptions":[],"email_marketing_consent":{"state":"invalid","opt_in_level":null,"consent_updated_at":null},"sms_marketing_consent":null,"admin_graphql_api_id":"gid://shopify/Customer/688973684"},{"id":562393516,"created_at":"2026-01-09T20:38:29-05:00","updated_at":"2026-01-09T20:38:29-05:00","first_name":"Dom","last_name":"Toretto","orders_count":0,"state":"disabled","total_spent":"199.65","last_order_id":450789469,"note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"tags":"","last_order_name":"#1001","email":"dom.toretto@mail.example.com","phone":"+12016251199","currency":"USD","addresses":[{"id":562393516,"customer_id":562393516,"first_name":"Dom","last_name":"Toretto","company":null,"address1":"Chestnut Street 93","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"+1(201)625-1199","name":"Dom Toretto","province_code":"KY","country_code":"US","country_name":"United States","default":true}],"tax_exemptions":[],"email_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null},"sms_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null,"consent_collected_from":"OTHER"},"admin_graphql_api_id":"gid://shopify/Customer/562393516","default_address":{"id":562393516,"customer_id":562393516,"first_name":"Dom","last_name":"Toretto","company":null,"address1":"Chestnut Street 93","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"+1(201)625-1199","name":"Dom Toretto","province_code":"KY","country_code":"US","country_name":"United States","default":true}},{"id":207119551,"created_at":"2026-01-09T20:38:29-05:00","updated_at":"2026-01-09T20:38:29-05:00","first_name":"Bob","last_name":"Norman","orders_count":1,"state":"disabled","total_spent":"199.65","last_order_id":450789469,"note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"tags":"Léon, Noël","last_order_name":"#1001","email":"bob.norman@mail.example.com","phone":"+16136120707","currency":"USD","addresses":[{"id":207119551,"customer_id":207119551,"first_name":null,"last_name":null,"company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"555-625-1199","name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}],"tax_exemptions":[],"email_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null},"sms_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null,"consent_collected_from":"OTHER"},"admin_graphql_api_id":"gid://shopify/Customer/207119551","default_address":{"id":207119551,"customer_id":207119551,"first_name":null,"last_name":null,"company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"555-625-1199","name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}}]}

  * #### Retrieve all customers for a shop

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/customers.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Customer.all({
          session: session,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Customer.all(
          session: test_session,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Customer.all({
          session: session,
        });

#### response

        HTTP/1.1 200 OK{"customers":[{"id":688973684,"created_at":"2026-01-09T19:47:31-05:00","updated_at":"2026-01-09T19:47:31-05:00","first_name":"Bob","last_name":"Norman Invalid","orders_count":0,"state":"disabled","total_spent":"0.00","last_order_id":null,"note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"tags":"","last_order_name":null,"email":"bob.norman.invalid@mail.example.de","phone":null,"currency":"USD","addresses":[],"tax_exemptions":[],"email_marketing_consent":{"state":"invalid","opt_in_level":null,"consent_updated_at":null},"sms_marketing_consent":null,"admin_graphql_api_id":"gid://shopify/Customer/688973684"},{"id":562393516,"created_at":"2026-01-09T19:47:31-05:00","updated_at":"2026-01-09T19:47:31-05:00","first_name":"Dom","last_name":"Toretto","orders_count":0,"state":"disabled","total_spent":"199.65","last_order_id":450789469,"note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"tags":"","last_order_name":"#1001","email":"dom.toretto@mail.example.com","phone":"+12016251199","currency":"USD","addresses":[{"id":562393516,"customer_id":562393516,"first_name":"Dom","last_name":"Toretto","company":null,"address1":"Chestnut Street 93","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"+1(201)625-1199","name":"Dom Toretto","province_code":"KY","country_code":"US","country_name":"United States","default":true}],"tax_exemptions":[],"email_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null},"sms_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null,"consent_collected_from":"OTHER"},"admin_graphql_api_id":"gid://shopify/Customer/562393516","default_address":{"id":562393516,"customer_id":562393516,"first_name":"Dom","last_name":"Toretto","company":null,"address1":"Chestnut Street 93","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"+1(201)625-1199","name":"Dom Toretto","province_code":"KY","country_code":"US","country_name":"United States","default":true}},{"id":207119551,"created_at":"2026-01-09T19:47:31-05:00","updated_at":"2026-01-09T19:47:31-05:00","first_name":"Bob","last_name":"Norman","orders_count":1,"state":"disabled","total_spent":"199.65","last_order_id":450789469,"note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"tags":"Léon, Noël","last_order_name":"#1001","email":"bob.norman@mail.example.com","phone":"+16136120707","currency":"USD","addresses":[{"id":207119551,"customer_id":207119551,"first_name":null,"last_name":null,"company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"555-625-1199","name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}],"tax_exemptions":[],"email_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null},"sms_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null,"consent_collected_from":"OTHER"},"admin_graphql_api_id":"gid://shopify/Customer/207119551","default_address":{"id":207119551,"customer_id":207119551,"first_name":null,"last_name":null,"company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"555-625-1199","name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}}]}

  * #### Retrieve only the specified customer fields

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/customers.json?fields=id%2Ctags%2Cemail" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Customer.all({
          session: session,
          fields: "id,tags,email",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Customer.all(
          session: test_session,
          fields: "id,tags,email",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Customer.all({
          session: session,
          fields: "id,tags,email",
        });

#### response

        HTTP/1.1 200 OK{"customers":[{"id":688973684,"tags":"","email":"bob.norman.invalid@mail.example.de"},{"id":562393516,"tags":"","email":"dom.toretto@mail.example.com"},{"id":207119551,"tags":"Léon, Noël","email":"bob.norman@mail.example.com"}]}


* * *

##

[Anchor to GET request, Retrieves all orders that belong to a customer](/docs/api/admin-rest/latest/resources/customer#get-customers-customer-id-orders)

get

Retrieves all orders that belong to a customer

[customer](/docs/api/admin-graphql/latest/queries/customer)

Retrieves all orders that belong to a customer. By default, only open orders are returned. The query string parameters in the [ Order](/docs/admin-api/rest/reference/orders/order#endpoints-{{ current_version }}) resource are also available at this endpoint.

###

[Anchor to Parameters of Retrieves all orders that belong to a customer](/docs/api/admin-rest/latest/resources/customer#get-customers-customer-id-orders-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

customer_id

string**string**

required**required**

* * *

status

enum**enum**

default open**default open**

The status of the orders to return.

Show status properties

  * **open** : Show only open orders.

  * **closed** : Show only closed orders.

  * **cancelled** : Show only canceled orders.

  * **any** : Show orders of any status, including archived orders.


* * *

Was this section helpful?

YesNo

###

[Anchor to get-customers-customer-id-orders-examples](/docs/api/admin-rest/latest/resources/customer#get-customers-customer-id-orders-examples)Examples

Retrieve all open orders from a customer

Path parameters

customer_id=207119551

string**string**

required**required**

Retrieve all previous orders from a customer.

Path parameters

customer_id=207119551

string**string**

required**required**

Query parameters

status=any

enum**enum**

default open**default open**

The status of the orders to return.

Show status properties

  * **open** : Show only open orders.

  * **closed** : Show only closed orders.

  * **cancelled** : Show only canceled orders.

  * **any** : Show orders of any status, including archived orders.


Retrieve all previous orders from a customer.

Path parameters

customer_id=207119551

string**string**

required**required**

Query parameters

status=any

enum**enum**

default open**default open**

The status of the orders to return.

Show status properties

  * **open** : Show only open orders.

  * **closed** : Show only closed orders.

  * **cancelled** : Show only canceled orders.

  * **any** : Show orders of any status, including archived orders.


Was this section helpful?

YesNo

get

## /admin/api/2026-01/customers/207119551/orders.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/customers/207119551/orders.json" \

-H "X-Shopify-Access-Token: {access_token}"

{}

## Response

JSON

9999

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

"orders": [

{

"id": 450789469,

"admin_graphql_api_id": "gid://shopify/Order/450789469",

"app_id": null,

"browser_ip": "0.0.0.0",

"buyer_accepts_marketing": false,

"cancel_reason": null,

"cancelled_at": null,

"cart_token": "68778783ad298f1c80c3bafcddeea02f",

"checkout_id": 901414060,

"checkout_token": "bd5a8aa1ecd019dd3520ff791ee3a24c",

"client_details": {

"accept_language": null,

"browser_height": null,

"browser_ip": "0.0.0.0",

"browser_width": null,

"session_hash": null,

"user_agent": null

},

"closed_at": null,

"confirmation_number": null,

"confirmed": true,

"contact_email": "bob.norman@mail.example.com",

"created_at": "2008-01-10T11:00:00-05:00",

"currency": "USD",

"current_subtotal_price": "195.67",

"current_subtotal_price_set": {

"shop_money": {

"amount": "195.67",

"currency_code": "USD"

},

"presentment_money": {

"amount": "195.67",

### examples

  * #### Retrieve all open orders from a customer

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/customers/207119551/orders.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Customer.orders({
          session: session,
          id: 207119551,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Customer.orders(
          session: test_session,
          id: 207119551,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Customer.orders({
          session: session,
          id: 207119551,
        });

#### response

        HTTP/1.1 200 OK{"orders":[{"id":450789469,"admin_graphql_api_id":"gid://shopify/Order/450789469","app_id":null,"browser_ip":"0.0.0.0","buyer_accepts_marketing":false,"cancel_reason":null,"cancelled_at":null,"cart_token":"68778783ad298f1c80c3bafcddeea02f","checkout_id":901414060,"checkout_token":"bd5a8aa1ecd019dd3520ff791ee3a24c","client_details":{"accept_language":null,"browser_height":null,"browser_ip":"0.0.0.0","browser_width":null,"session_hash":null,"user_agent":null},"closed_at":null,"confirmation_number":null,"confirmed":true,"contact_email":"bob.norman@mail.example.com","created_at":"2008-01-10T11:00:00-05:00","currency":"USD","current_subtotal_price":"195.67","current_subtotal_price_set":{"shop_money":{"amount":"195.67","currency_code":"USD"},"presentment_money":{"amount":"195.67","currency_code":"USD"}},"current_total_additional_fees_set":null,"current_total_discounts":"3.33","current_total_discounts_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"current_total_duties_set":null,"current_total_price":"199.65","current_total_price_set":{"shop_money":{"amount":"199.65","currency_code":"USD"},"presentment_money":{"amount":"199.65","currency_code":"USD"}},"current_total_tax":"3.98","current_total_tax_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"customer_locale":null,"device_id":null,"discount_codes":[{"code":"TENOFF","amount":"10.00","type":"fixed_amount"}],"duties_included":false,"email":"bob.norman@mail.example.com","estimated_taxes":false,"payment_status":"partially_refunded","shipping_status":null,"landing_site":"http://www.example.com?source=abc","landing_site_ref":"abc","location_id":null,"merchant_business_entity_id":"MTU0ODM4MDAwOQ","merchant_of_record_app_id":null,"name":"#1001","note":null,"note_attributes":[{"name":"custom engraving","value":"Happy Birthday"},{"name":"colour","value":"green"}],"number":1,"order_number":1001,"order_status_url":"https://jsmith.myshopify.com/548380009/orders/b1946ac92492d2347c6235b4d2611184/authenticate?key=imasecretipod","original_total_additional_fees_set":null,"original_total_duties_set":null,"payment_gateway_names":["bogus"],"phone":"+557734881234","po_number":"ABC123","presentment_currency":"USD","processed_at":"2008-01-10T11:00:00-05:00","reference":"fhwdgads","referring_site":"http://www.otherexample.com","source_identifier":"fhwdgads","source_name":"web","source_url":null,"subtotal_price":"597.00","subtotal_price_set":{"shop_money":{"amount":"597.00","currency_code":"USD"},"presentment_money":{"amount":"597.00","currency_code":"USD"}},"tags":"","tax_exempt":false,"tax_lines":[{"price":"11.94","rate":0.06,"title":"State Tax","price_set":{"shop_money":{"amount":"11.94","currency_code":"USD"},"presentment_money":{"amount":"11.94","currency_code":"USD"}},"channel_liable":null}],"taxes_included":false,"test":false,"token":"b1946ac92492d2347c6235b4d2611184","total_cash_rounding_payment_adjustment_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_cash_rounding_refund_adjustment_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_discounts":"10.00","total_discounts_set":{"shop_money":{"amount":"10.00","currency_code":"USD"},"presentment_money":{"amount":"10.00","currency_code":"USD"}},"total_line_items_price":"597.00","total_line_items_price_set":{"shop_money":{"amount":"597.00","currency_code":"USD"},"presentment_money":{"amount":"597.00","currency_code":"USD"}},"total_outstanding":"0.00","total_price":"598.94","total_price_set":{"shop_money":{"amount":"598.94","currency_code":"USD"},"presentment_money":{"amount":"598.94","currency_code":"USD"}},"total_shipping_price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_tax":"11.94","total_tax_set":{"shop_money":{"amount":"11.94","currency_code":"USD"},"presentment_money":{"amount":"11.94","currency_code":"USD"}},"total_tip_received":"0.00","total_weight":0,"updated_at":"2008-01-10T11:00:00-05:00","user_id":null,"billing_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"customer":{"id":207119551,"created_at":"2026-01-09T20:48:39-05:00","updated_at":"2026-01-09T20:48:39-05:00","first_name":"Bob","last_name":"Norman","state":"disabled","note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"email_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null},"sms_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null,"consent_collected_from":"OTHER"},"tags":"Léon, Noël","email":"bob.norman@mail.example.com","phone":"+16136120707","currency":"USD","tax_exemptions":[],"admin_graphql_api_id":"gid://shopify/Customer/207119551","default_address":{"id":207119551,"customer_id":207119551,"first_name":null,"last_name":null,"company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"555-625-1199","name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}},"discount_applications":[{"target_type":"line_item","type":"discount_code","value":"10.0","value_type":"fixed_amount","allocation_method":"across","target_selection":"all","code":"TENOFF"}],"fulfillments":[{"id":255858046,"admin_graphql_api_id":"gid://shopify/Fulfillment/255858046","created_at":"2026-01-09T20:48:39-05:00","location_id":655441491,"name":"#1001.0","order_id":450789469,"origin_address":{},"receipt":{"testcase":true,"authorization":"123456"},"service":"manual","shipment_status":null,"status":"failure","tracking_company":"USPS","tracking_number":"1Z1234512345123456","tracking_numbers":["1Z1234512345123456"],"tracking_url":"https://tools.usps.com/go/TrackConfirmAction_input?qtc_tLabels1=1Z1234512345123456","tracking_urls":["https://tools.usps.com/go/TrackConfirmAction_input?qtc_tLabels1=1Z1234512345123456"],"updated_at":"2026-01-09T20:48:39-05:00","line_items":[{"id":466157049,"admin_graphql_api_id":"gid://shopify/LineItem/466157049","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - green","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"quantity":1,"requires_shipping":true,"sku":"IPOD2008GREEN","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":39072856,"variant_inventory_management":"shopify","variant_title":"green","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.34","amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}},"discount_application_index":0}]}]}],"line_items":[{"id":466157049,"admin_graphql_api_id":"gid://shopify/LineItem/466157049","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - green","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"quantity":1,"requires_shipping":true,"sku":"IPOD2008GREEN","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":39072856,"variant_inventory_management":"shopify","variant_title":"green","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.34","amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}},"discount_application_index":0}]},{"id":518995019,"admin_graphql_api_id":"gid://shopify/LineItem/518995019","attributed_staffs":[],"current_quantity":1,"fulfillable_quantity":1,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - red","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008RED","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":49148385,"variant_inventory_management":"shopify","variant_title":"red","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.33","amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"discount_application_index":0}]},{"id":703073504,"admin_graphql_api_id":"gid://shopify/LineItem/703073504","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - black","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008BLACK","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":457924702,"variant_inventory_management":"shopify","variant_title":"black","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.33","amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"discount_application_index":0}]}],"payment_terms":null,"refunds":[{"id":509562969,"admin_graphql_api_id":"gid://shopify/Refund/509562969","created_at":"2026-01-09T20:48:39-05:00","note":"it broke during shipping","order_id":450789469,"processed_at":"2026-01-09T20:48:39-05:00","restock":true,"total_additional_fees_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_duties_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"user_id":548380009,"order_adjustments":[],"transactions":[{"id":179259969,"admin_graphql_api_id":"gid://shopify/OrderTransaction/179259969","amount":"209.00","authorization":"authorization-key","created_at":"2005-08-05T12:59:12-04:00","currency":"USD","device_id":null,"error_code":null,"gateway":"bogus","kind":"refund","location_id":null,"message":null,"order_id":450789469,"parent_id":801038806,"payment_id":"#1001.3","processed_at":"2005-08-05T12:59:12-04:00","receipt":{},"source_name":"web","status":"success","test":false,"user_id":null}],"refund_line_items":[{"id":104689539,"line_item_id":703073504,"location_id":487838322,"quantity":1,"restock_type":"legacy_restock","subtotal":195.66,"subtotal_set":{"shop_money":{"amount":"195.66","currency_code":"USD"},"presentment_money":{"amount":"195.66","currency_code":"USD"}},"total_tax":3.98,"total_tax_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"line_item":{"id":703073504,"admin_graphql_api_id":"gid://shopify/LineItem/703073504","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - black","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008BLACK","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":457924702,"variant_inventory_management":"shopify","variant_title":"black","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.33","amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"discount_application_index":0}]}},{"id":709875399,"line_item_id":466157049,"location_id":487838322,"quantity":1,"restock_type":"legacy_restock","subtotal":195.67,"subtotal_set":{"shop_money":{"amount":"195.67","currency_code":"USD"},"presentment_money":{"amount":"195.67","currency_code":"USD"}},"total_tax":3.98,"total_tax_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"line_item":{"id":466157049,"admin_graphql_api_id":"gid://shopify/LineItem/466157049","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - green","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"quantity":1,"requires_shipping":true,"sku":"IPOD2008GREEN","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":39072856,"variant_inventory_management":"shopify","variant_title":"green","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.34","amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}},"discount_application_index":0}]}}],"duties":[],"additional_fees":[]}],"shipping_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"shipping_lines":[{"id":369256396,"carrier_identifier":null,"code":"Free Shipping","discounted_price":"0.00","discounted_price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"is_removed":false,"phone":null,"price":"0.00","price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"requested_fulfillment_service_id":null,"source":"shopify","title":"Free Shipping","tax_lines":[],"discount_allocations":[]}]}]}

  * #### Retrieve all previous orders from a customer.

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/customers/207119551/orders.json?status=any" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Customer.orders({
          session: session,
          id: 207119551,
          status: "any",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Customer.orders(
          session: test_session,
          id: 207119551,
          status: "any",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Customer.orders({
          session: session,
          id: 207119551,
          status: "any",
        });

#### response

        HTTP/1.1 200 OK{"orders":[{"id":450789469,"admin_graphql_api_id":"gid://shopify/Order/450789469","app_id":null,"browser_ip":"0.0.0.0","buyer_accepts_marketing":false,"cancel_reason":null,"cancelled_at":null,"cart_token":"68778783ad298f1c80c3bafcddeea02f","checkout_id":901414060,"checkout_token":"bd5a8aa1ecd019dd3520ff791ee3a24c","client_details":{"accept_language":null,"browser_height":null,"browser_ip":"0.0.0.0","browser_width":null,"session_hash":null,"user_agent":null},"closed_at":null,"confirmation_number":null,"confirmed":true,"contact_email":"bob.norman@mail.example.com","created_at":"2008-01-10T11:00:00-05:00","currency":"USD","current_subtotal_price":"195.67","current_subtotal_price_set":{"shop_money":{"amount":"195.67","currency_code":"USD"},"presentment_money":{"amount":"195.67","currency_code":"USD"}},"current_total_additional_fees_set":null,"current_total_discounts":"3.33","current_total_discounts_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"current_total_duties_set":null,"current_total_price":"199.65","current_total_price_set":{"shop_money":{"amount":"199.65","currency_code":"USD"},"presentment_money":{"amount":"199.65","currency_code":"USD"}},"current_total_tax":"3.98","current_total_tax_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"customer_locale":null,"device_id":null,"discount_codes":[{"code":"TENOFF","amount":"10.00","type":"fixed_amount"}],"duties_included":false,"email":"bob.norman@mail.example.com","estimated_taxes":false,"payment_status":"partially_refunded","shipping_status":null,"landing_site":"http://www.example.com?source=abc","landing_site_ref":"abc","location_id":null,"merchant_business_entity_id":"MTU0ODM4MDAwOQ","merchant_of_record_app_id":null,"name":"#1001","note":null,"note_attributes":[{"name":"custom engraving","value":"Happy Birthday"},{"name":"colour","value":"green"}],"number":1,"order_number":1001,"order_status_url":"https://jsmith.myshopify.com/548380009/orders/b1946ac92492d2347c6235b4d2611184/authenticate?key=imasecretipod","original_total_additional_fees_set":null,"original_total_duties_set":null,"payment_gateway_names":["bogus"],"phone":"+557734881234","po_number":"ABC123","presentment_currency":"USD","processed_at":"2008-01-10T11:00:00-05:00","reference":"fhwdgads","referring_site":"http://www.otherexample.com","source_identifier":"fhwdgads","source_name":"web","source_url":null,"subtotal_price":"597.00","subtotal_price_set":{"shop_money":{"amount":"597.00","currency_code":"USD"},"presentment_money":{"amount":"597.00","currency_code":"USD"}},"tags":"","tax_exempt":false,"tax_lines":[{"price":"11.94","rate":0.06,"title":"State Tax","price_set":{"shop_money":{"amount":"11.94","currency_code":"USD"},"presentment_money":{"amount":"11.94","currency_code":"USD"}},"channel_liable":null}],"taxes_included":false,"test":false,"token":"b1946ac92492d2347c6235b4d2611184","total_cash_rounding_payment_adjustment_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_cash_rounding_refund_adjustment_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_discounts":"10.00","total_discounts_set":{"shop_money":{"amount":"10.00","currency_code":"USD"},"presentment_money":{"amount":"10.00","currency_code":"USD"}},"total_line_items_price":"597.00","total_line_items_price_set":{"shop_money":{"amount":"597.00","currency_code":"USD"},"presentment_money":{"amount":"597.00","currency_code":"USD"}},"total_outstanding":"0.00","total_price":"598.94","total_price_set":{"shop_money":{"amount":"598.94","currency_code":"USD"},"presentment_money":{"amount":"598.94","currency_code":"USD"}},"total_shipping_price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_tax":"11.94","total_tax_set":{"shop_money":{"amount":"11.94","currency_code":"USD"},"presentment_money":{"amount":"11.94","currency_code":"USD"}},"total_tip_received":"0.00","total_weight":0,"updated_at":"2008-01-10T11:00:00-05:00","user_id":null,"billing_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"customer":{"id":207119551,"created_at":"2026-01-09T19:38:20-05:00","updated_at":"2026-01-09T19:38:20-05:00","first_name":"Bob","last_name":"Norman","state":"disabled","note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"email_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null},"sms_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null,"consent_collected_from":"OTHER"},"tags":"Léon, Noël","email":"bob.norman@mail.example.com","phone":"+16136120707","currency":"USD","tax_exemptions":[],"admin_graphql_api_id":"gid://shopify/Customer/207119551","default_address":{"id":207119551,"customer_id":207119551,"first_name":null,"last_name":null,"company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"555-625-1199","name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}},"discount_applications":[{"target_type":"line_item","type":"discount_code","value":"10.0","value_type":"fixed_amount","allocation_method":"across","target_selection":"all","code":"TENOFF"}],"fulfillments":[{"id":255858046,"admin_graphql_api_id":"gid://shopify/Fulfillment/255858046","created_at":"2026-01-09T19:38:20-05:00","location_id":655441491,"name":"#1001.0","order_id":450789469,"origin_address":{},"receipt":{"testcase":true,"authorization":"123456"},"service":"manual","shipment_status":null,"status":"failure","tracking_company":"USPS","tracking_number":"1Z1234512345123456","tracking_numbers":["1Z1234512345123456"],"tracking_url":"https://tools.usps.com/go/TrackConfirmAction_input?qtc_tLabels1=1Z1234512345123456","tracking_urls":["https://tools.usps.com/go/TrackConfirmAction_input?qtc_tLabels1=1Z1234512345123456"],"updated_at":"2026-01-09T19:38:20-05:00","line_items":[{"id":466157049,"admin_graphql_api_id":"gid://shopify/LineItem/466157049","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - green","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"quantity":1,"requires_shipping":true,"sku":"IPOD2008GREEN","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":39072856,"variant_inventory_management":"shopify","variant_title":"green","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.34","amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}},"discount_application_index":0}]}]}],"line_items":[{"id":466157049,"admin_graphql_api_id":"gid://shopify/LineItem/466157049","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - green","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"quantity":1,"requires_shipping":true,"sku":"IPOD2008GREEN","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":39072856,"variant_inventory_management":"shopify","variant_title":"green","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.34","amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}},"discount_application_index":0}]},{"id":518995019,"admin_graphql_api_id":"gid://shopify/LineItem/518995019","attributed_staffs":[],"current_quantity":1,"fulfillable_quantity":1,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - red","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008RED","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":49148385,"variant_inventory_management":"shopify","variant_title":"red","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.33","amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"discount_application_index":0}]},{"id":703073504,"admin_graphql_api_id":"gid://shopify/LineItem/703073504","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - black","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008BLACK","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":457924702,"variant_inventory_management":"shopify","variant_title":"black","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.33","amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"discount_application_index":0}]}],"payment_terms":null,"refunds":[{"id":509562969,"admin_graphql_api_id":"gid://shopify/Refund/509562969","created_at":"2026-01-09T19:38:20-05:00","note":"it broke during shipping","order_id":450789469,"processed_at":"2026-01-09T19:38:20-05:00","restock":true,"total_additional_fees_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_duties_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"user_id":548380009,"order_adjustments":[],"transactions":[{"id":179259969,"admin_graphql_api_id":"gid://shopify/OrderTransaction/179259969","amount":"209.00","authorization":"authorization-key","created_at":"2005-08-05T12:59:12-04:00","currency":"USD","device_id":null,"error_code":null,"gateway":"bogus","kind":"refund","location_id":null,"message":null,"order_id":450789469,"parent_id":801038806,"payment_id":"#1001.3","processed_at":"2005-08-05T12:59:12-04:00","receipt":{},"source_name":"web","status":"success","test":false,"user_id":null}],"refund_line_items":[{"id":104689539,"line_item_id":703073504,"location_id":487838322,"quantity":1,"restock_type":"legacy_restock","subtotal":195.66,"subtotal_set":{"shop_money":{"amount":"195.66","currency_code":"USD"},"presentment_money":{"amount":"195.66","currency_code":"USD"}},"total_tax":3.98,"total_tax_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"line_item":{"id":703073504,"admin_graphql_api_id":"gid://shopify/LineItem/703073504","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - black","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008BLACK","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":457924702,"variant_inventory_management":"shopify","variant_title":"black","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.33","amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"discount_application_index":0}]}},{"id":709875399,"line_item_id":466157049,"location_id":487838322,"quantity":1,"restock_type":"legacy_restock","subtotal":195.67,"subtotal_set":{"shop_money":{"amount":"195.67","currency_code":"USD"},"presentment_money":{"amount":"195.67","currency_code":"USD"}},"total_tax":3.98,"total_tax_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"line_item":{"id":466157049,"admin_graphql_api_id":"gid://shopify/LineItem/466157049","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - green","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"quantity":1,"requires_shipping":true,"sku":"IPOD2008GREEN","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":39072856,"variant_inventory_management":"shopify","variant_title":"green","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.34","amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}},"discount_application_index":0}]}}],"duties":[],"additional_fees":[]}],"shipping_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"shipping_lines":[{"id":369256396,"carrier_identifier":null,"code":"Free Shipping","discounted_price":"0.00","discounted_price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"is_removed":false,"phone":null,"price":"0.00","price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"requested_fulfillment_service_id":null,"source":"shopify","title":"Free Shipping","tax_lines":[],"discount_allocations":[]}]}]}

  * #### Retrieve all previous orders from a customer.

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/customers/207119551/orders.json?status=any" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Customer.orders({
          session: session,
          id: 207119551,
          status: "any",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Customer.orders(
          session: test_session,
          id: 207119551,
          status: "any",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Customer.orders({
          session: session,
          id: 207119551,
          status: "any",
        });

#### response

        HTTP/1.1 200 OK{"orders":[{"id":450789469,"admin_graphql_api_id":"gid://shopify/Order/450789469","app_id":null,"browser_ip":"0.0.0.0","buyer_accepts_marketing":false,"cancel_reason":null,"cancelled_at":null,"cart_token":"68778783ad298f1c80c3bafcddeea02f","checkout_id":901414060,"checkout_token":"bd5a8aa1ecd019dd3520ff791ee3a24c","client_details":{"accept_language":null,"browser_height":null,"browser_ip":"0.0.0.0","browser_width":null,"session_hash":null,"user_agent":null},"closed_at":null,"confirmation_number":null,"confirmed":true,"contact_email":"bob.norman@mail.example.com","created_at":"2008-01-10T11:00:00-05:00","currency":"USD","current_subtotal_price":"195.67","current_subtotal_price_set":{"shop_money":{"amount":"195.67","currency_code":"USD"},"presentment_money":{"amount":"195.67","currency_code":"USD"}},"current_total_additional_fees_set":null,"current_total_discounts":"3.33","current_total_discounts_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"current_total_duties_set":null,"current_total_price":"199.65","current_total_price_set":{"shop_money":{"amount":"199.65","currency_code":"USD"},"presentment_money":{"amount":"199.65","currency_code":"USD"}},"current_total_tax":"3.98","current_total_tax_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"customer_locale":null,"device_id":null,"discount_codes":[{"code":"TENOFF","amount":"10.00","type":"fixed_amount"}],"duties_included":false,"email":"bob.norman@mail.example.com","estimated_taxes":false,"payment_status":"partially_refunded","shipping_status":null,"landing_site":"http://www.example.com?source=abc","landing_site_ref":"abc","location_id":null,"merchant_business_entity_id":"MTU0ODM4MDAwOQ","merchant_of_record_app_id":null,"name":"#1001","note":null,"note_attributes":[{"name":"custom engraving","value":"Happy Birthday"},{"name":"colour","value":"green"}],"number":1,"order_number":1001,"order_status_url":"https://jsmith.myshopify.com/548380009/orders/b1946ac92492d2347c6235b4d2611184/authenticate?key=imasecretipod","original_total_additional_fees_set":null,"original_total_duties_set":null,"payment_gateway_names":["bogus"],"phone":"+557734881234","po_number":"ABC123","presentment_currency":"USD","processed_at":"2008-01-10T11:00:00-05:00","reference":"fhwdgads","referring_site":"http://www.otherexample.com","source_identifier":"fhwdgads","source_name":"web","source_url":null,"subtotal_price":"597.00","subtotal_price_set":{"shop_money":{"amount":"597.00","currency_code":"USD"},"presentment_money":{"amount":"597.00","currency_code":"USD"}},"tags":"","tax_exempt":false,"tax_lines":[{"price":"11.94","rate":0.06,"title":"State Tax","price_set":{"shop_money":{"amount":"11.94","currency_code":"USD"},"presentment_money":{"amount":"11.94","currency_code":"USD"}},"channel_liable":null}],"taxes_included":false,"test":false,"token":"b1946ac92492d2347c6235b4d2611184","total_cash_rounding_payment_adjustment_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_cash_rounding_refund_adjustment_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_discounts":"10.00","total_discounts_set":{"shop_money":{"amount":"10.00","currency_code":"USD"},"presentment_money":{"amount":"10.00","currency_code":"USD"}},"total_line_items_price":"597.00","total_line_items_price_set":{"shop_money":{"amount":"597.00","currency_code":"USD"},"presentment_money":{"amount":"597.00","currency_code":"USD"}},"total_outstanding":"0.00","total_price":"598.94","total_price_set":{"shop_money":{"amount":"598.94","currency_code":"USD"},"presentment_money":{"amount":"598.94","currency_code":"USD"}},"total_shipping_price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_tax":"11.94","total_tax_set":{"shop_money":{"amount":"11.94","currency_code":"USD"},"presentment_money":{"amount":"11.94","currency_code":"USD"}},"total_tip_received":"0.00","total_weight":0,"updated_at":"2008-01-10T11:00:00-05:00","user_id":null,"billing_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"customer":{"id":207119551,"created_at":"2026-01-09T20:38:41-05:00","updated_at":"2026-01-09T20:38:41-05:00","first_name":"Bob","last_name":"Norman","state":"disabled","note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"email_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null},"sms_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null,"consent_collected_from":"OTHER"},"tags":"Léon, Noël","email":"bob.norman@mail.example.com","phone":"+16136120707","currency":"USD","tax_exemptions":[],"admin_graphql_api_id":"gid://shopify/Customer/207119551","default_address":{"id":207119551,"customer_id":207119551,"first_name":null,"last_name":null,"company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"555-625-1199","name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}},"discount_applications":[{"target_type":"line_item","type":"discount_code","value":"10.0","value_type":"fixed_amount","allocation_method":"across","target_selection":"all","code":"TENOFF"}],"fulfillments":[{"id":255858046,"admin_graphql_api_id":"gid://shopify/Fulfillment/255858046","created_at":"2026-01-09T20:38:41-05:00","location_id":655441491,"name":"#1001.0","order_id":450789469,"origin_address":{},"receipt":{"testcase":true,"authorization":"123456"},"service":"manual","shipment_status":null,"status":"failure","tracking_company":"USPS","tracking_number":"1Z1234512345123456","tracking_numbers":["1Z1234512345123456"],"tracking_url":"https://tools.usps.com/go/TrackConfirmAction_input?qtc_tLabels1=1Z1234512345123456","tracking_urls":["https://tools.usps.com/go/TrackConfirmAction_input?qtc_tLabels1=1Z1234512345123456"],"updated_at":"2026-01-09T20:38:41-05:00","line_items":[{"id":466157049,"admin_graphql_api_id":"gid://shopify/LineItem/466157049","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - green","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"quantity":1,"requires_shipping":true,"sku":"IPOD2008GREEN","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":39072856,"variant_inventory_management":"shopify","variant_title":"green","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.34","amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}},"discount_application_index":0}]}]}],"line_items":[{"id":466157049,"admin_graphql_api_id":"gid://shopify/LineItem/466157049","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - green","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"quantity":1,"requires_shipping":true,"sku":"IPOD2008GREEN","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":39072856,"variant_inventory_management":"shopify","variant_title":"green","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.34","amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}},"discount_application_index":0}]},{"id":518995019,"admin_graphql_api_id":"gid://shopify/LineItem/518995019","attributed_staffs":[],"current_quantity":1,"fulfillable_quantity":1,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - red","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008RED","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":49148385,"variant_inventory_management":"shopify","variant_title":"red","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.33","amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"discount_application_index":0}]},{"id":703073504,"admin_graphql_api_id":"gid://shopify/LineItem/703073504","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - black","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008BLACK","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":457924702,"variant_inventory_management":"shopify","variant_title":"black","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.33","amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"discount_application_index":0}]}],"payment_terms":null,"refunds":[{"id":509562969,"admin_graphql_api_id":"gid://shopify/Refund/509562969","created_at":"2026-01-09T20:38:41-05:00","note":"it broke during shipping","order_id":450789469,"processed_at":"2026-01-09T20:38:41-05:00","restock":true,"total_additional_fees_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"total_duties_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"user_id":548380009,"order_adjustments":[],"transactions":[{"id":179259969,"admin_graphql_api_id":"gid://shopify/OrderTransaction/179259969","amount":"209.00","authorization":"authorization-key","created_at":"2005-08-05T12:59:12-04:00","currency":"USD","device_id":null,"error_code":null,"gateway":"bogus","kind":"refund","location_id":null,"message":null,"order_id":450789469,"parent_id":801038806,"payment_id":"#1001.3","processed_at":"2005-08-05T12:59:12-04:00","receipt":{},"source_name":"web","status":"success","test":false,"user_id":null}],"refund_line_items":[{"id":104689539,"line_item_id":703073504,"location_id":487838322,"quantity":1,"restock_type":"legacy_restock","subtotal":195.66,"subtotal_set":{"shop_money":{"amount":"195.66","currency_code":"USD"},"presentment_money":{"amount":"195.66","currency_code":"USD"}},"total_tax":3.98,"total_tax_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"line_item":{"id":703073504,"admin_graphql_api_id":"gid://shopify/LineItem/703073504","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - black","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[],"quantity":1,"requires_shipping":true,"sku":"IPOD2008BLACK","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":457924702,"variant_inventory_management":"shopify","variant_title":"black","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.33","amount_set":{"shop_money":{"amount":"3.33","currency_code":"USD"},"presentment_money":{"amount":"3.33","currency_code":"USD"}},"discount_application_index":0}]}},{"id":709875399,"line_item_id":466157049,"location_id":487838322,"quantity":1,"restock_type":"legacy_restock","subtotal":195.67,"subtotal_set":{"shop_money":{"amount":"195.67","currency_code":"USD"},"presentment_money":{"amount":"195.67","currency_code":"USD"}},"total_tax":3.98,"total_tax_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"line_item":{"id":466157049,"admin_graphql_api_id":"gid://shopify/LineItem/466157049","attributed_staffs":[],"current_quantity":0,"fulfillable_quantity":0,"fulfillment_service":"manual","shipping_status":null,"gift_card":false,"grams":200,"name":"IPod Nano - 8gb - green","price":"199.00","price_set":{"shop_money":{"amount":"199.00","currency_code":"USD"},"presentment_money":{"amount":"199.00","currency_code":"USD"}},"product_exists":true,"product_id":632910392,"properties":[{"name":"Custom Engraving Front","value":"Happy Birthday"},{"name":"Custom Engraving Back","value":"Merry Christmas"}],"quantity":1,"requires_shipping":true,"sku":"IPOD2008GREEN","taxable":true,"title":"IPod Nano - 8gb","total_discount":"0.00","total_discount_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"variant_id":39072856,"variant_inventory_management":"shopify","variant_title":"green","vendor":null,"tax_lines":[{"channel_liable":null,"price":"3.98","price_set":{"shop_money":{"amount":"3.98","currency_code":"USD"},"presentment_money":{"amount":"3.98","currency_code":"USD"}},"rate":0.06,"title":"State Tax"}],"duties":[],"discount_allocations":[{"amount":"3.34","amount_set":{"shop_money":{"amount":"3.34","currency_code":"USD"},"presentment_money":{"amount":"3.34","currency_code":"USD"}},"discount_application_index":0}]}}],"duties":[],"additional_fees":[]}],"shipping_address":{"first_name":"Bob","address1":"Chestnut Street 92","phone":"+1(502)-459-2181","city":"Louisville","zip":"40202","province":"Kentucky","country":"United States","last_name":"Norman","address2":"","company":null,"latitude":45.41634,"longitude":-75.6868,"name":"Bob Norman","country_code":"US","province_code":"KY"},"shipping_lines":[{"id":369256396,"carrier_identifier":null,"code":"Free Shipping","discounted_price":"0.00","discounted_price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"is_removed":false,"phone":null,"price":"0.00","price_set":{"shop_money":{"amount":"0.00","currency_code":"USD"},"presentment_money":{"amount":"0.00","currency_code":"USD"}},"requested_fulfillment_service_id":null,"source":"shopify","title":"Free Shipping","tax_lines":[],"discount_allocations":[]}]}]}


* * *

##

[Anchor to GET request, Retrieves a count of customers](/docs/api/admin-rest/latest/resources/customer#get-customers-count)

get

Retrieves a count of customers

[customersCount](/docs/api/admin-graphql/latest/queries/customersCount?example=retrieves-a-count-of-customers)

Requires `customers` access scope.

**Requires `customers` access scope.:**

Retrieves a count of all customers.

###

[Anchor to Parameters of Retrieves a count of customers](/docs/api/admin-rest/latest/resources/customer#get-customers-count-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

created_at_max

Count customers created before a specified date.
(format: 2014-04-25T16:15:47-04:00)

* * *

created_after

Count customers created after a specified date.
(format: 2014-04-25T16:15:47-04:00)

* * *

updated_at_max

Count customers last updated before a specified date.
(format: 2014-04-25T16:15:47-04:00)

* * *

updated_at_min

Count customers last updated after a specified date.
(format: 2014-04-25T16:15:47-04:00)

* * *

Was this section helpful?

YesNo

###

[Anchor to get-customers-count-examples](/docs/api/admin-rest/latest/resources/customer#get-customers-count-examples)Examples

Retrieve a count of all customers tag:elasticsearch:true

Retrieve a count of customers changed after a specified date tag:elasticsearch:true

Query parameters

updated_at_min=2026-01-09+01:21:24

Count customers last updated after a specified date.
(format: 2014-04-25T16:15:47-04:00)

Was this section helpful?

YesNo

get

## /admin/api/2026-01/customers/count.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/customers/count.json" \

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

  * #### Retrieve a count of all customers tag:elasticsearch:true

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/customers/count.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Customer.count({
          session: session,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Customer.count(
          session: test_session,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Customer.count({
          session: session,
        });

#### response

        HTTP/1.1 200 OK{"count":3}

  * #### Retrieve a count of customers changed after a specified date tag:elasticsearch:true

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/customers/count.json?updated_at_min=2026-01-09+01%3A21%3A24" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Customer.count({
          session: session,
          updated_at_min: "2026-01-09 01:21:24",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Customer.count(
          session: test_session,
          updated_at_min: "2026-01-09 01:21:24",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Customer.count({
          session: session,
          updated_at_min: "2026-01-09 01:21:24",
        });

#### response

        HTTP/1.1 200 OK{"count":3}


* * *

##

[Anchor to GET request, Searches for customers that match a supplied query](/docs/api/admin-rest/latest/resources/customer#get-customers-search?query=email:bob.norman@mail.example.com)

get

Searches for customers that match a supplied query

[customers](/docs/api/admin-graphql/latest/queries/customers)

Requires `customers` access scope.

**Requires `customers` access scope.:**

Searches for customers that match a supplied query. **Note:** This endpoint implements pagination by using links that are provided in the response header. To learn more, refer to [Make paginated requests to the REST Admin API](/api/usage/pagination-rest).

###

[Anchor to Parameters of Searches for customers that match a supplied query](/docs/api/admin-rest/latest/resources/customer#get-customers-search?query=email:bob.norman@mail.example.com-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

fields

Show only certain fields, specified by a comma-separated list of field names.

* * *

count

≤ 250**≤ 250**

default 50**default 50**

The maximum number of results to show.

* * *

order

default last_order_date DESC**default last_order_date DESC**

Set the field and direction by which to order results.

* * *

query

Text to search for in the shop's customer data. **Note:** Supported queries: `accepts_marketing`, `activation_date`, `address1`, `address2`, `city`, `company`, `country`, `customer_date`, `customer_first_name`, `customer_id`, `customer_last_name`, `customer_tag`, ` email`, `email_marketing_state`, `first_name`, `first_order_date`, `id`, `last_abandoned_order_date`, `last_name`, `multipass_identifier`, `orders_count`, `order_date`, `phone`, `province`, `shop_id`, `state`, `tag`, `total_spent`, `updated_at`, `verified_email`, `product_subscriber_status`. All other queries returns all customers.

* * *

Was this section helpful?

YesNo

###

[Anchor to get-customers-search?query=email:bob.norman@mail.example.com-examples](/docs/api/admin-rest/latest/resources/customer#get-customers-search?query=email:bob.norman@mail.example.com-examples)Examples

Search for a customer with a specified email address tag:elasticsearch:true

Query parameters

query=email:bob.norman@mail.example.com

Text to search for in the shop's customer data. **Note:** Supported queries: `accepts_marketing`, `activation_date`, `address1`, `address2`, `city`, `company`, `country`, `customer_date`, `customer_first_name`, `customer_id`, `customer_last_name`, `customer_tag`, ` email`, `email_marketing_state`, `first_name`, `first_order_date`, `id`, `last_abandoned_order_date`, `last_name`, `multipass_identifier`, `orders_count`, `order_date`, `phone`, `province`, `shop_id`, `state`, `tag`, `total_spent`, `updated_at`, `verified_email`, `product_subscriber_status`. All other queries returns all customers.

Search for all customers with a specified last name and show certain fields tag:elasticsearch:true

Query parameters

fields=id,+email,+first_name,+last_name

Show only certain fields, specified by a comma-separated list of field names.

query=last_name:Norman

Text to search for in the shop's customer data. **Note:** Supported queries: `accepts_marketing`, `activation_date`, `address1`, `address2`, `city`, `company`, `country`, `customer_date`, `customer_first_name`, `customer_id`, `customer_last_name`, `customer_tag`, ` email`, `email_marketing_state`, `first_name`, `first_order_date`, `id`, `last_abandoned_order_date`, `last_name`, `multipass_identifier`, `orders_count`, `order_date`, `phone`, `province`, `shop_id`, `state`, `tag`, `total_spent`, `updated_at`, `verified_email`, `product_subscriber_status`. All other queries returns all customers.

Search for all customers with a specified last name and show certain fields tag:elasticsearch:true

Query parameters

fields=id,+email,+first_name,+last_name

Show only certain fields, specified by a comma-separated list of field names.

query=last_name:Norman

Text to search for in the shop's customer data. **Note:** Supported queries: `accepts_marketing`, `activation_date`, `address1`, `address2`, `city`, `company`, `country`, `customer_date`, `customer_first_name`, `customer_id`, `customer_last_name`, `customer_tag`, ` email`, `email_marketing_state`, `first_name`, `first_order_date`, `id`, `last_abandoned_order_date`, `last_name`, `multipass_identifier`, `orders_count`, `order_date`, `phone`, `province`, `shop_id`, `state`, `tag`, `total_spent`, `updated_at`, `verified_email`, `product_subscriber_status`. All other queries returns all customers.

Search for all customers with an address in the United States and a specified first name tag:elasticsearch:true

Query parameters

query=first_name:Bob+country:United+States

Text to search for in the shop's customer data. **Note:** Supported queries: `accepts_marketing`, `activation_date`, `address1`, `address2`, `city`, `company`, `country`, `customer_date`, `customer_first_name`, `customer_id`, `customer_last_name`, `customer_tag`, ` email`, `email_marketing_state`, `first_name`, `first_order_date`, `id`, `last_abandoned_order_date`, `last_name`, `multipass_identifier`, `orders_count`, `order_date`, `phone`, `province`, `shop_id`, `state`, `tag`, `total_spent`, `updated_at`, `verified_email`, `product_subscriber_status`. All other queries returns all customers.

Search for all customers with an address in the United States and a specified first name tag:elasticsearch:true

Query parameters

query=first_name:Bob+country:United+States

Text to search for in the shop's customer data. **Note:** Supported queries: `accepts_marketing`, `activation_date`, `address1`, `address2`, `city`, `company`, `country`, `customer_date`, `customer_first_name`, `customer_id`, `customer_last_name`, `customer_tag`, ` email`, `email_marketing_state`, `first_name`, `first_order_date`, `id`, `last_abandoned_order_date`, `last_name`, `multipass_identifier`, `orders_count`, `order_date`, `phone`, `province`, `shop_id`, `state`, `tag`, `total_spent`, `updated_at`, `verified_email`, `product_subscriber_status`. All other queries returns all customers.

Search for customers matching a specified email domain tag:elasticsearch:true

Query parameters

query=email:*@mail.example.com

Text to search for in the shop's customer data. **Note:** Supported queries: `accepts_marketing`, `activation_date`, `address1`, `address2`, `city`, `company`, `country`, `customer_date`, `customer_first_name`, `customer_id`, `customer_last_name`, `customer_tag`, ` email`, `email_marketing_state`, `first_name`, `first_order_date`, `id`, `last_abandoned_order_date`, `last_name`, `multipass_identifier`, `orders_count`, `order_date`, `phone`, `province`, `shop_id`, `state`, `tag`, `total_spent`, `updated_at`, `verified_email`, `product_subscriber_status`. All other queries returns all customers.

Was this section helpful?

YesNo

get

## /admin/api/2026-01/customers/search.json?query=email:bob.norman@mail.example.com

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/customers/search.json?query=email%3Abob.norman%40mail.example.com" \

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

HTTP/1.1 200 OK

{

"customers": [

{

"id": 207119551,

"created_at": "2026-01-09T21:10:33-05:00",

"updated_at": "2026-01-09T21:10:33-05:00",

"first_name": "Bob",

"last_name": "Norman",

"orders_count": 1,

"state": "disabled",

"total_spent": "199.65",

"last_order_id": 450789469,

"note": null,

"verified_email": true,

"multipass_identifier": null,

"tax_exempt": false,

"tags": "Léon, Noël",

"last_order_name": "#1001",

"email": "bob.norman@mail.example.com",

"phone": "+16136120707",

"currency": "USD",

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

],

"tax_exemptions": [],

"email_marketing_consent": {

"state": "not_subscribed",

"opt_in_level": null,

"consent_updated_at": null

},

"sms_marketing_consent": {

"state": "not_subscribed",

"opt_in_level": null,

"consent_updated_at": null,

"consent_collected_from": "OTHER"

},

"admin_graphql_api_id": "gid://shopify/Customer/207119551",

"default_address": {

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

]

}

### examples

  * #### Search for a customer with a specified email address tag:elasticsearch:true

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/customers/search.json?query=email%3Abob.norman%40mail.example.com" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Customer.search({
          session: session,
          query: "email:bob.norman@mail.example.com",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Customer.search(
          session: test_session,
          query: "email:bob.norman@mail.example.com",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Customer.search({
          session: session,
          query: "email:bob.norman@mail.example.com",
        });

#### response

        HTTP/1.1 200 OK{"customers":[{"id":207119551,"created_at":"2026-01-09T21:10:33-05:00","updated_at":"2026-01-09T21:10:33-05:00","first_name":"Bob","last_name":"Norman","orders_count":1,"state":"disabled","total_spent":"199.65","last_order_id":450789469,"note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"tags":"Léon, Noël","last_order_name":"#1001","email":"bob.norman@mail.example.com","phone":"+16136120707","currency":"USD","addresses":[{"id":207119551,"customer_id":207119551,"first_name":null,"last_name":null,"company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"555-625-1199","name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}],"tax_exemptions":[],"email_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null},"sms_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null,"consent_collected_from":"OTHER"},"admin_graphql_api_id":"gid://shopify/Customer/207119551","default_address":{"id":207119551,"customer_id":207119551,"first_name":null,"last_name":null,"company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"555-625-1199","name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}}]}

  * #### Search for all customers with a specified last name and show certain fields tag:elasticsearch:true

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/customers/search.json?fields=id%2C+email%2C+first_name%2C+last_name&query=last_name%3ANorman" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Customer.search({
          session: session,
          fields: "id, email, first_name, last_name",
          query: "last_name:Norman",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Customer.search(
          session: test_session,
          fields: "id, email, first_name, last_name",
          query: "last_name:Norman",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Customer.search({
          session: session,
          fields: "id, email, first_name, last_name",
          query: "last_name:Norman",
        });

#### response

        HTTP/1.1 200 OK{"customers":[{"id":207119551,"first_name":"Bob","last_name":"Norman","email":"bob.norman@mail.example.com"}]}

  * #### Search for all customers with a specified last name and show certain fields tag:elasticsearch:true

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/customers/search.json?fields=id%2C+email%2C+first_name%2C+last_name&query=last_name%3ANorman" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Customer.search({
          session: session,
          fields: "id, email, first_name, last_name",
          query: "last_name:Norman",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Customer.search(
          session: test_session,
          fields: "id, email, first_name, last_name",
          query: "last_name:Norman",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Customer.search({
          session: session,
          fields: "id, email, first_name, last_name",
          query: "last_name:Norman",
        });

#### response

        HTTP/1.1 200 OK{"customers":[{"id":207119551,"first_name":"Bob","last_name":"Norman","email":"bob.norman@mail.example.com"}]}

  * #### Search for all customers with an address in the United States and a specified first name tag:elasticsearch:true

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/customers/search.json?query=first_name%3ABob+country%3AUnited+States" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Customer.search({
          session: session,
          query: "first_name:Bob country:United States",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Customer.search(
          session: test_session,
          query: "first_name:Bob country:United States",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Customer.search({
          session: session,
          query: "first_name:Bob country:United States",
        });

#### response

        HTTP/1.1 200 OK{"customers":[{"id":207119551,"created_at":"2026-01-09T20:48:10-05:00","updated_at":"2026-01-09T20:48:10-05:00","first_name":"Bob","last_name":"Norman","orders_count":1,"state":"disabled","total_spent":"199.65","last_order_id":450789469,"note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"tags":"Léon, Noël","last_order_name":"#1001","email":"bob.norman@mail.example.com","phone":"+16136120707","currency":"USD","addresses":[{"id":207119551,"customer_id":207119551,"first_name":null,"last_name":null,"company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"555-625-1199","name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}],"tax_exemptions":[],"email_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null},"sms_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null,"consent_collected_from":"OTHER"},"admin_graphql_api_id":"gid://shopify/Customer/207119551","default_address":{"id":207119551,"customer_id":207119551,"first_name":null,"last_name":null,"company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"555-625-1199","name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}}]}

  * #### Search for all customers with an address in the United States and a specified first name tag:elasticsearch:true

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/customers/search.json?query=first_name%3ABob+country%3AUnited+States" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Customer.search({
          session: session,
          query: "first_name:Bob country:United States",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Customer.search(
          session: test_session,
          query: "first_name:Bob country:United States",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Customer.search({
          session: session,
          query: "first_name:Bob country:United States",
        });

#### response

        HTTP/1.1 200 OK{"customers":[{"id":207119551,"created_at":"2026-01-09T21:10:56-05:00","updated_at":"2026-01-09T21:10:56-05:00","first_name":"Bob","last_name":"Norman","orders_count":1,"state":"disabled","total_spent":"199.65","last_order_id":450789469,"note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"tags":"Léon, Noël","last_order_name":"#1001","email":"bob.norman@mail.example.com","phone":"+16136120707","currency":"USD","addresses":[{"id":207119551,"customer_id":207119551,"first_name":null,"last_name":null,"company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"555-625-1199","name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}],"tax_exemptions":[],"email_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null},"sms_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null,"consent_collected_from":"OTHER"},"admin_graphql_api_id":"gid://shopify/Customer/207119551","default_address":{"id":207119551,"customer_id":207119551,"first_name":null,"last_name":null,"company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"555-625-1199","name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}}]}

  * #### Search for customers matching a specified email domain tag:elasticsearch:true

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/customers/search.json?query=email%3A%2A%40mail.example.com" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Customer.search({
          session: session,
          query: "email:*@mail.example.com",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Customer.search(
          session: test_session,
          query: "email:*@mail.example.com",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Customer.search({
          session: session,
          query: "email:*@mail.example.com",
        });

#### response

        HTTP/1.1 200 OK{"customers":[{"id":207119551,"created_at":"2026-01-09T20:38:52-05:00","updated_at":"2026-01-09T20:38:52-05:00","first_name":"Bob","last_name":"Norman","orders_count":1,"state":"disabled","total_spent":"199.65","last_order_id":450789469,"note":null,"verified_email":true,"multipass_identifier":null,"tax_exempt":false,"tags":"Léon, Noël","last_order_name":"#1001","email":"bob.norman@mail.example.com","phone":"+16136120707","currency":"USD","addresses":[{"id":207119551,"customer_id":207119551,"first_name":null,"last_name":null,"company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"555-625-1199","name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}],"tax_exemptions":[],"email_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null},"sms_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null,"consent_collected_from":"OTHER"},"admin_graphql_api_id":"gid://shopify/Customer/207119551","default_address":{"id":207119551,"customer_id":207119551,"first_name":null,"last_name":null,"company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"555-625-1199","name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}}]}


* * *

##

[Anchor to PUT request, Updates a customer](/docs/api/admin-rest/latest/resources/customer#put-customers-customer-id)

put

Updates a customer

[customerUpdate](/docs/api/admin-graphql/latest/mutations/customerUpdate)

Requires `customers` access scope.

**Requires `customers` access scope.:**

Updates a customer.

###

[Anchor to Parameters of Updates a customer](/docs/api/admin-rest/latest/resources/customer#put-customers-customer-id-parameters)Parameters

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

[Anchor to put-customers-customer-id-examples](/docs/api/admin-rest/latest/resources/customer#put-customers-customer-id-examples)Examples

Add metafield to an existing customer

Path parameters

customer_id=207119551

string**string**

required**required**

Request body

customer[](/apps/store/data-protection/protected-customer-data)

Customer resource**Customer resource**

Show customer properties

customer.id:207119551

A unique identifier for the customer.

Was this section helpful?

YesNo

put

## /admin/api/2026-01/customers/207119551.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{"customer":{"id":207119551,"metafields":[{"key":"new","value":"newvalue","type":"single_line_text_field","namespace":"global"}]}}' \

-X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/customers/207119551.json" \

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

HTTP/1.1 200 OK

{

"customer": {

"first_name": "Bob",

"last_name": "Norman",

"tax_exempt": false,

"id": 207119551,

"created_at": "2026-01-09T19:47:41-05:00",

"updated_at": "2026-01-09T19:47:41-05:00",

"orders_count": 1,

"state": "disabled",

"total_spent": "199.65",

"last_order_id": 450789469,

"note": null,

"verified_email": true,

"multipass_identifier": null,

"tags": "Léon, Noël",

"last_order_name": "#1001",

"email": "bob.norman@mail.example.com",

"phone": "+16136120707",

"currency": "USD",

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

],

"tax_exemptions": [],

"email_marketing_consent": {

"state": "not_subscribed",

"opt_in_level": null,

"consent_updated_at": null

},

"sms_marketing_consent": {

"state": "not_subscribed",

"opt_in_level": null,

"consent_updated_at": null,

"consent_collected_from": "OTHER"

},

"admin_graphql_api_id": "gid://shopify/Customer/207119551",

"default_address": {

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

}

### examples

  * #### Add metafield to an existing customer

#####

        curl -d '{"customer":{"id":207119551,"metafields":[{"key":"new","value":"newvalue","type":"single_line_text_field","namespace":"global"}]}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/customers/207119551.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const customer = new admin.rest.resources.Customer({session: session});

        customer.id = 207119551;
        customer.metafields = [
          {
            "key": "new",
            "value": "newvalue",
            "type": "single_line_text_field",
            "namespace": "global"
          }
        ];
        await customer.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        customer = ShopifyAPI::Customer.new(session: test_session)
        customer.id = 207119551
        customer.metafields = [
          {
            "key" => "new",
            "value" => "newvalue",
            "type" => "single_line_text_field",
            "namespace" => "global"
          }
        ]
        customer.save!

#####

        // Session is built by the OAuth process

        const customer = new shopify.rest.Customer({session: session});
        customer.id = 207119551;
        customer.metafields = [
          {
            "key": "new",
            "value": "newvalue",
            "type": "single_line_text_field",
            "namespace": "global"
          }
        ];
        await customer.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"customer":{"first_name":"Bob","last_name":"Norman","tax_exempt":false,"id":207119551,"created_at":"2026-01-09T19:47:41-05:00","updated_at":"2026-01-09T19:47:41-05:00","orders_count":1,"state":"disabled","total_spent":"199.65","last_order_id":450789469,"note":null,"verified_email":true,"multipass_identifier":null,"tags":"Léon, Noël","last_order_name":"#1001","email":"bob.norman@mail.example.com","phone":"+16136120707","currency":"USD","addresses":[{"id":207119551,"customer_id":207119551,"first_name":null,"last_name":null,"company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"555-625-1199","name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}],"tax_exemptions":[],"email_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null},"sms_marketing_consent":{"state":"not_subscribed","opt_in_level":null,"consent_updated_at":null,"consent_collected_from":"OTHER"},"admin_graphql_api_id":"gid://shopify/Customer/207119551","default_address":{"id":207119551,"customer_id":207119551,"first_name":null,"last_name":null,"company":null,"address1":"Chestnut Street 92","address2":"","city":"Louisville","province":"Kentucky","country":"United States","zip":"40202","phone":"555-625-1199","name":"","province_code":"KY","country_code":"US","country_name":"United States","default":true}}}