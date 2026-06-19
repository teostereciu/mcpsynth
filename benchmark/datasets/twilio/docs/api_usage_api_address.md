# REST API: Addresses

*Source: https://www.twilio.com/docs/usage/api/address*

---

# REST API: Addresses

Positive FeedbackNegative Feedback

* * *

An Address instance resource represents your or your customer's physical location within a country. Around the world, some local authorities require the name and address of the user to be on file with Twilio to purchase and own a phone number. Address requirements are exposed as a property on the [AvailablePhoneNumber](/docs/phone-numbers/api/availablephonenumber-resource "AvailablePhoneNumber") resource.

Addresses contain the name of your company or your customer's company in addition to location information and an optional friendly name. Each Address created on an account or subaccount can be used for any phone numbers purchased on that account. After creating an address, it can be used to satisfy the requirements for multiple phone numbers and phone numbers with address requirements can be purchased using the [IncomingPhoneNumber](/docs/phone-numbers/api/incomingphonenumber-resource "IncomingPhoneNumber") resource.

In some countries, to comply with local regulations, addresses are validated to ensure the integrity and accuracy of the data provided. In those countries, if the address you provide does not pass validation, it is not accepted as an Address and the error code [21628](/docs/api/errors/21628 "21628") is returned. If the address submitted is not an exact match but is similar to a valid address, we'll create the Address using the valid address we found, unless you include the AutoCorrectAddress=false parameter in the request. In that case, we'll provide it as a suggested address in error code [21629](/docs/api/errors/21629 "21629"). If the suggested address is indeed the address of your company or your customer's company, then use the suggested format to create a valid Address.

The Address list resource represents all of the Addresses that you have created on your account within Twilio. You can `POST` to Addresses to create a new address or modify an existing address.

* * *

## Address Properties

address-properties page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescriptionChild properties

accountSidSID<AC>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that is responsible for the Address resource.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

citystring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The city in which the address is located.

* * *

customerNamestring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The name associated with the address.This property has a maximum length of 16 4-byte characters, or 21 3-byte characters.

* * *

dateCreatedstring<date-time-rfc-2822>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date and time in GMT that the resource was created specified in [RFC 2822(link takes you to an external page)](https://www.ietf.org/rfc/rfc2822.txt "RFC 2822") format.

* * *

dateUpdatedstring<date-time-rfc-2822>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date and time in GMT that the resource was last updated specified in [RFC 2822(link takes you to an external page)](https://www.ietf.org/rfc/rfc2822.txt "RFC 2822") format.

* * *

friendlyNamestring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The string that you assigned to describe the resource.

* * *

isoCountrystring<iso-country-code>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The ISO country code of the address.

* * *

postalCodestring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The postal code of the address.

* * *

regionstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The state or region of the address.

* * *

sidSID<AD>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique string that that we created to identify the Address resource.

Pattern: `^AD[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

streetstring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The number and street address of the address.

* * *

uristring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URI of the resource, relative to `https://api.twilio.com`.

* * *

emergencyEnabledboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether emergency calling has been enabled on this number.

* * *

validatedboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether the address has been validated to comply with local regulation. In countries that require valid addresses, an invalid address will not be accepted. `true` indicates the Address has been validated. `false` indicate the country doesn't require validation or the Address is not valid.

* * *

verifiedboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether the address has been verified to comply with regulation. In countries that require valid addresses, an invalid address will not be accepted. `true` indicates the Address has been verified. `false` indicate the country doesn't require verified or the Address is not valid.

* * *

streetSecondarystring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The additional number and street address of the address.

* * *

## Create an Address resource

create-an-address-resource page anchor

Positive FeedbackNegative Feedback

`POST https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Addresses.json`

Creates a new Address within your account.

### Path parameters

path-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

accountSidSID<AC>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that will be responsible for the new Address resource.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

### Request body parameters

request-body-parameters page anchor

Positive FeedbackNegative Feedback

Encoding type:`application/x-www-form-urlencoded`

SchemaExample

Property nameTypeRequiredPIIDescriptionChild properties

customerNamestring

required

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The name to associate with the new address.

* * *

streetstring

required

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The number and street address of the new address.

* * *

citystring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The city of the new address.

* * *

regionstring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The state or region of the new address.

* * *

postalCodestring

required

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The postal code of the new address.

* * *

isoCountrystring<iso-country-code>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The ISO country code of the new address.

* * *

friendlyNamestring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

A descriptive string that you create to describe the new address. It can be up to 64 characters long for Regulatory Compliance addresses and 32 characters long for Emergency addresses.

* * *

emergencyEnabledboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether to enable emergency calling on the new address. Can be: `true` or `false`.

* * *

autoCorrectAddressboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether we should automatically correct the address. Can be: `true` or `false` and the default is `true`. If empty or `true`, we will correct the address you provide if necessary. If `false`, we won't alter the address you provide.

* * *

streetSecondarystring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The additional number and street address of the address.

Copy code block


    {


      "City": "city",


      "CustomerName": "customer_name",


      "FriendlyName": "friendly_name",


      "IsoCountry": "US",


      "PostalCode": "postal_code",


      "Region": "region",


      "Street": "street"


    }

Create an AddressLink to code sample: Create an Address

Report code block

Copy code block


    1

    // Download the helper library from https://www.twilio.com/docs/node/install


    2

    const twilio = require("twilio"); // Or, for ESM: import twilio from "twilio";


    3




    4

    // Find your Account SID and Auth Token at twilio.com/console


    5

    // and set the environment variables. See http://twil.io/secure


    6

    const accountSid = process.env.TWILIO_ACCOUNT_SID;


    7

    const authToken = process.env.TWILIO_AUTH_TOKEN;


    8

    const client = twilio(accountSid, authToken);


    9




    10

    async function createAddress() {


    11

      const address = await client.addresses.create({


    12

        city: "city",


    13

        customerName: "customer_name",


    14

        isoCountry: "US",


    15

        postalCode: "postal_code",


    16

        region: "region",


    17

        street: "street",


    18

        streetSecondary: "street_secondary",


    19

      });


    20




    21

      console.log(address.accountSid);


    22

    }


    23




    24

    createAddress();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    3

      "city": "city",


    4

      "customer_name": "customer_name",


    5

      "date_created": "Tue, 18 Aug 2015 17:07:30 +0000",


    6

      "date_updated": "Tue, 18 Aug 2015 17:07:30 +0000",


    7

      "emergency_enabled": false,


    8

      "friendly_name": "Main Office",


    9

      "iso_country": "US",


    10

      "postal_code": "postal_code",


    11

      "region": "region",


    12

      "sid": "ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    13

      "street": "street",


    14

      "street_secondary": "street_secondary",


    15

      "validated": false,


    16

      "verified": false,


    17

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Addresses/ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"


    18

    }

If successful, Twilio will respond with a representation of the new address.

### Address Validation Related Errors

av-errors page anchor

Positive FeedbackNegative Feedback

Error Code| Error Name| Error Description
---|---|---
21615| Phone Number Requires a Local Address| To purchase this number you must have an Address on your account that satisfies the local address requirements.
21628| Address Validation Error| The address you have provided cannot be validated.
21629| Address Validation Error - Check Suggested Address| The address you have provided cannot be validated. A similar address has been found to be valid. The suggested address is included in the error message body.

* * *

## Fetch an Address resource

fetch-an-address-resource page anchor

Positive FeedbackNegative Feedback

`GET https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Addresses/{Sid}.json`

### Path parameters

path-parameters-1 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

accountSidSID<AC>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that is responsible for the Address resource to fetch.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

sidSID<AD>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The Twilio-provided string that uniquely identifies the Address resource to fetch.

Pattern: `^AD[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

Fetch an AddressLink to code sample: Fetch an Address

Report code block

Copy code block


    1

    // Download the helper library from https://www.twilio.com/docs/node/install


    2

    const twilio = require("twilio"); // Or, for ESM: import twilio from "twilio";


    3




    4

    // Find your Account SID and Auth Token at twilio.com/console


    5

    // and set the environment variables. See http://twil.io/secure


    6

    const accountSid = process.env.TWILIO_ACCOUNT_SID;


    7

    const authToken = process.env.TWILIO_AUTH_TOKEN;


    8

    const client = twilio(accountSid, authToken);


    9




    10

    async function fetchAddress() {


    11

      const address = await client


    12

        .addresses("ADXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")


    13

        .fetch();


    14




    15

      console.log(address.accountSid);


    16

    }


    17




    18

    fetchAddress();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    3

      "city": "SF",


    4

      "customer_name": "name",


    5

      "date_created": "Tue, 18 Aug 2015 17:07:30 +0000",


    6

      "date_updated": "Tue, 18 Aug 2015 17:07:30 +0000",


    7

      "emergency_enabled": false,


    8

      "friendly_name": "Main Office",


    9

      "iso_country": "US",


    10

      "postal_code": "94019",


    11

      "region": "CA",


    12

      "sid": "ADXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    13

      "street": "4th",


    14

      "street_secondary": null,


    15

      "validated": false,


    16

      "verified": false,


    17

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Addresses/ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"


    18

    }

* * *

## Read multiple Address resources

read-multiple-address-resources page anchor

Positive FeedbackNegative Feedback

`GET https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Addresses.json`

Returns a list of Address resource representations, each representing an address within your account. The list includes [paging information][paging-info].

### Path parameters

path-parameters-2 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

accountSidSID<AC>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that is responsible for the Address resource to read.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

### Query parameters

query-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

customerNamestring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The `customer_name` of the Address resources to read.

* * *

friendlyNamestring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The string that identifies the Address resources to read.

* * *

emergencyEnabledboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether the address can be associated to a number for emergency calling.

* * *

isoCountrystring<iso-country-code>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The ISO country code of the Address resources to read.

* * *

pageSizeinteger<int64>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

How many resources to return in each list page. The default is 50, and the maximum is 1000.

Minimum: `1`Maximum: `1000`

* * *

pageinteger

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The page index. This value is simply for client state.

Minimum: `0`

* * *

pageTokenstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The page token. This is provided by the API.

Show all addressesLink to code sample: Show all addresses

Report code block

Copy code block


    1

    // Download the helper library from https://www.twilio.com/docs/node/install


    2

    const twilio = require("twilio"); // Or, for ESM: import twilio from "twilio";


    3




    4

    // Find your Account SID and Auth Token at twilio.com/console


    5

    // and set the environment variables. See http://twil.io/secure


    6

    const accountSid = process.env.TWILIO_ACCOUNT_SID;


    7

    const authToken = process.env.TWILIO_AUTH_TOKEN;


    8

    const client = twilio(accountSid, authToken);


    9




    10

    async function listAddress() {


    11

      const addresses = await client.addresses.list({ limit: 20 });


    12




    13

      addresses.forEach((a) => console.log(a.accountSid));


    14

    }


    15




    16

    listAddress();

### Response

Note about this response

Copy response


    1

    {


    2

      "addresses": [


    3

        {


    4

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

          "city": "SF",


    6

          "customer_name": "name",


    7

          "date_created": "Tue, 18 Aug 2015 17:07:30 +0000",


    8

          "date_updated": "Tue, 18 Aug 2015 17:07:30 +0000",


    9

          "emergency_enabled": false,


    10

          "friendly_name": "Main Office",


    11

          "iso_country": "US",


    12

          "postal_code": "94019",


    13

          "region": "CA",


    14

          "sid": "ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    15

          "street": "4th",


    16

          "street_secondary": null,


    17

          "validated": false,


    18

          "verified": false,


    19

          "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Addresses/ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"


    20

        }


    21

      ],


    22

      "end": 0,


    23

      "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Addresses.json?FriendlyName=friendly_name&IsoCountry=US&CustomerName=customer_name&PageSize=50&Page=0",


    24

      "next_page_uri": null,


    25

      "page": 0,


    26

      "page_size": 50,


    27

      "previous_page_uri": null,


    28

      "start": 0,


    29

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Addresses.json?FriendlyName=friendly_name&IsoCountry=US&CustomerName=customer_name&PageSize=50&Page=0"


    30

    }

Show all addresses matching the Customer Name 'Customer 123'Link to code sample: Show all addresses matching the Customer Name 'Customer 123'

Report code block

Copy code block


    1

    // Download the helper library from https://www.twilio.com/docs/node/install


    2

    const twilio = require("twilio"); // Or, for ESM: import twilio from "twilio";


    3




    4

    // Find your Account SID and Auth Token at twilio.com/console


    5

    // and set the environment variables. See http://twil.io/secure


    6

    const accountSid = process.env.TWILIO_ACCOUNT_SID;


    7

    const authToken = process.env.TWILIO_AUTH_TOKEN;


    8

    const client = twilio(accountSid, authToken);


    9




    10

    async function listAddress() {


    11

      const addresses = await client.addresses.list({


    12

        customerName: "Customer 123",


    13

        limit: 20,


    14

      });


    15




    16

      addresses.forEach((a) => console.log(a.accountSid));


    17

    }


    18




    19

    listAddress();

### Response

Note about this response

Copy response


    1

    {


    2

      "addresses": [


    3

        {


    4

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

          "city": "SF",


    6

          "customer_name": "name",


    7

          "date_created": "Tue, 18 Aug 2015 17:07:30 +0000",


    8

          "date_updated": "Tue, 18 Aug 2015 17:07:30 +0000",


    9

          "emergency_enabled": false,


    10

          "friendly_name": "Main Office",


    11

          "iso_country": "US",


    12

          "postal_code": "94019",


    13

          "region": "CA",


    14

          "sid": "ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    15

          "street": "4th",


    16

          "street_secondary": null,


    17

          "validated": false,


    18

          "verified": false,


    19

          "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Addresses/ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"


    20

        }


    21

      ],


    22

      "end": 0,


    23

      "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Addresses.json?FriendlyName=friendly_name&IsoCountry=US&CustomerName=customer_name&PageSize=50&Page=0",


    24

      "next_page_uri": null,


    25

      "page": 0,


    26

      "page_size": 50,


    27

      "previous_page_uri": null,


    28

      "start": 0,


    29

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Addresses.json?FriendlyName=friendly_name&IsoCountry=US&CustomerName=customer_name&PageSize=50&Page=0"


    30

    }

List Dependent PNS SubresourcesLink to code sample: List Dependent PNS Subresources

Report code block

Copy code block


    1

    // Download the helper library from https://www.twilio.com/docs/node/install


    2

    const twilio = require("twilio"); // Or, for ESM: import twilio from "twilio";


    3




    4

    // Find your Account SID and Auth Token at twilio.com/console


    5

    // and set the environment variables. See http://twil.io/secure


    6

    const accountSid = process.env.TWILIO_ACCOUNT_SID;


    7

    const authToken = process.env.TWILIO_AUTH_TOKEN;


    8

    const client = twilio(accountSid, authToken);


    9




    10

    async function listDependentPhoneNumber() {


    11

      const dependentPhoneNumbers = await client


    12

        .addresses("AD2a0747eba6abf96b7e3c3ff0b4530f6e")


    13

        .dependentPhoneNumbers.list({ limit: 20 });


    14




    15

      dependentPhoneNumbers.forEach((d) => console.log(d.sid));


    16

    }


    17




    18

    listDependentPhoneNumber();

### Response

Note about this response

Copy response


    1

    {


    2

      "dependent_phone_numbers": [


    3

        {


    4

          "sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    6

          "friendly_name": "3197004499318",


    7

          "phone_number": "+1111111111",


    8

          "voice_url": "https://hurl.twilio.com/welcome/voice/",


    9

          "voice_method": "POST",


    10

          "voice_fallback_url": "https://voice-fallback.twilio.com/welcome/sms/reply",


    11

          "voice_fallback_method": "POST",


    12

          "voice_caller_id_lookup": false,


    13

          "date_created": "Thu, 23 Feb 2017 18:26:31 +0000",


    14

          "date_updated": "Thu, 23 Feb 2017 18:26:31 +0000",


    15

          "sms_url": "https://demo.twilio.com/welcome/sms/reply",


    16

          "sms_method": "POST",


    17

          "sms_fallback_url": "https://sms-fallback.twilio.com/welcome/sms/reply",


    18

          "sms_fallback_method": "POST",


    19

          "address_requirements": "any",


    20

          "capabilities": {


    21

            "Voice": false,


    22

            "SMS": true,


    23

            "MMS": false


    24

          },


    25

          "status_callback": "https://status.twilio.com/welcome/sms/reply",


    26

          "status_callback_method": "POST",


    27

          "api_version": "2010-04-01",


    28

          "voice_application_sid": "APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa1",


    29

          "sms_application_sid": "APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa2",


    30

          "trunk_sid": "APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa5",


    31

          "emergency_status": "Inactive",


    32

          "emergency_address_sid": "ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    33

          "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IncomingPhoneNumbers/PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"


    34

        }


    35

      ],


    36

      "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Addresses/ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/DependentPhoneNumbers.json?PageSize=50&Page=0",


    37

      "next_page_uri": null,


    38

      "page": 0,


    39

      "page_size": 50,


    40

      "previous_page_uri": null,


    41

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Addresses/ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/DependentPhoneNumbers.json?PageSize=50&Page=0",


    42

      "start": 0,


    43

      "end": 0


    44

    }

* * *

## Read multiple Address Subresources

instance-subresources page anchor

Positive FeedbackNegative Feedback

Copy code block


    GET https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Addresses/{AddressSid}/DependentPhoneNumbers.json

Returns a list of IncomingPhoneNumbers on your account that require the specified address.

### Dependent Phone Numbers Instance Subresource

list-dependent-pns page anchor

Positive FeedbackNegative Feedback

Each Address instance resource supports a subresource for viewing which phone numbers are dependent on your existing addresses. In the case that you have two addresses that satisfy the requirement on a given phone number, this subresource will not return the phone number in the list.

#### Paging

paging page anchor

The list includes paging information. If you plan on requesting more records than will fit on a single page, you should use the provided nextpageuri rather than incrementing through the pages by page number. Using the nextpageuri helps to ensure that your next request picks up where it left off and can prevent you from retrieving duplicate data if you are actively creating addresses.

* * *

## Update an Address resource

update-an-address-resource page anchor

Positive FeedbackNegative Feedback

`POST https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Addresses/{Sid}.json`

A `POST` request attempts to update an individual Address instance and returns the updated resource representation if successful. A successful returned response is identical to that of the `HTTP GET`.

Note that all fields but `IsoCountry` can be updated using a `POST` request. To update the `IsoCountry`, a new Address must be created.

### Path parameters

path-parameters-3 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

accountSidSID<AC>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that is responsible for the Address resource to update.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

sidSID<AD>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The Twilio-provided string that uniquely identifies the Address resource to update.

Pattern: `^AD[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

### Request body parameters

request-body-parameters-1 page anchor

Positive FeedbackNegative Feedback

Encoding type:`application/x-www-form-urlencoded`

SchemaExample

Property nameTypeRequiredPIIDescriptionChild properties

friendlyNamestring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

A descriptive string that you create to describe the new address. It can be up to 64 characters long for Regulatory Compliance addresses and 32 characters long for Emergency addresses.

* * *

customerNamestring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The name to associate with the address.

* * *

streetstring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The number and street address of the address.

* * *

citystring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The city of the address.

* * *

regionstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The state or region of the address.

* * *

postalCodestring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The postal code of the address.

* * *

emergencyEnabledboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether to enable emergency calling on the address. Can be: `true` or `false`.

* * *

autoCorrectAddressboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether we should automatically correct the address. Can be: `true` or `false` and the default is `true`. If empty or `true`, we will correct the address you provide if necessary. If `false`, we won't alter the address you provide.

* * *

streetSecondarystring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The additional number and street address of the address.

Copy code block


    {


      "City": "city",


      "CustomerName": "customer_name",


      "FriendlyName": "friendly_name",


      "PostalCode": "postal_code",


      "Region": "region",


      "Street": "street"


    }

Update a customer name and street addressLink to code sample: Update a customer name and street address

Report code block

Copy code block


    1

    // Download the helper library from https://www.twilio.com/docs/node/install


    2

    const twilio = require("twilio"); // Or, for ESM: import twilio from "twilio";


    3




    4

    // Find your Account SID and Auth Token at twilio.com/console


    5

    // and set the environment variables. See http://twil.io/secure


    6

    const accountSid = process.env.TWILIO_ACCOUNT_SID;


    7

    const authToken = process.env.TWILIO_AUTH_TOKEN;


    8

    const client = twilio(accountSid, authToken);


    9




    10

    async function updateAddress() {


    11

      const address = await client


    12

        .addresses("AD2a0747eba6abf96b7e3c3ff0b4530f6e")


    13

        .update({


    14

          customerName: "Customer 456",


    15

          street: "2 Hasselhoff Lane",


    16

        });


    17




    18

      console.log(address.accountSid);


    19

    }


    20




    21

    updateAddress();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    3

      "city": "SF",


    4

      "customer_name": "Customer 456",


    5

      "date_created": "Tue, 18 Aug 2015 17:07:30 +0000",


    6

      "date_updated": "Tue, 18 Aug 2015 17:07:30 +0000",


    7

      "emergency_enabled": false,


    8

      "friendly_name": "Main Office",


    9

      "iso_country": "US",


    10

      "postal_code": "94019",


    11

      "region": "CA",


    12

      "sid": "AD2a0747eba6abf96b7e3c3ff0b4530f6e",


    13

      "street": "2 Hasselhoff Lane",


    14

      "street_secondary": null,


    15

      "validated": false,


    16

      "verified": false,


    17

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Addresses/ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"


    18

    }

* * *

## Delete an Address resource

delete-an-address-resource page anchor

Positive FeedbackNegative Feedback

`DELETE https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Addresses/{Sid}.json`

Deletes this address from your account.

If this address is required for any active IncomingPhoneNumbers, it cannot be deleted and you will receive Error [21625][21625]. However, if you have a second address that fulfills the AddressRequirement, the address will be successfully deleted. The DependentPhoneNumbers Instance Subresource will allow you to see which IncomingPhoneNumbers require a given address.

If the delete is successful, Twilio will return an HTTP 204 response with no body.

### Path parameters

path-parameters-4 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

accountSidSID<AC>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that is responsible for the Address resource to delete.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

sidSID<AD>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The Twilio-provided string that uniquely identifies the Address resource to delete.

Pattern: `^AD[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

Delete an AddressLink to code sample: Delete an Address

Report code block

Copy code block


    1

    // Download the helper library from https://www.twilio.com/docs/node/install


    2

    const twilio = require("twilio"); // Or, for ESM: import twilio from "twilio";


    3




    4

    // Find your Account SID and Auth Token at twilio.com/console


    5

    // and set the environment variables. See http://twil.io/secure


    6

    const accountSid = process.env.TWILIO_ACCOUNT_SID;


    7

    const authToken = process.env.TWILIO_AUTH_TOKEN;


    8

    const client = twilio(accountSid, authToken);


    9




    10

    async function deleteAddress() {


    11

      await client.addresses("ADXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").remove();


    12

    }


    13




    14

    deleteAddress();