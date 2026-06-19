# Services PhoneNumbers subresource

*Source: https://www.twilio.com/docs/messaging/api/phonenumber-resource*

---

# Services PhoneNumbers subresource

Positive FeedbackNegative Feedback

* * *

(new)

## Public Beta

The Services resource is currently available as a Public Beta product. This means that some features for configuring your Messaging Service via the REST API are not yet implemented, and others may be changed before the product is declared Generally Available. Messaging Service Configuration through the [Twilio Console(link takes you to an external page)](https://www.twilio.com/console "Twilio Console") is Generally Available.

Public Beta products are [not covered by a Twilio SLA(link takes you to an external page)](https://help.twilio.com/hc/en-us/articles/115002413087-Twilio-Beta-product-support "not covered by a Twilio SLA").

The resources for sending Messages with a Messaging Service are Generally Available.

PhoneNumbers is a subresource of [Services](/docs/messaging/api/service-resource "Services") and represents a phone number you have associated to the Service.

When sending a message with your Messaging Service, Twilio will select a phone number from the service for delivery.

Inbound messages received on any phone number associated to a Messaging Service are passed to the inbound request URL of the Service with [the TwiML parameters that describe the message](/docs/messaging/guides/webhook-request#parameters-in-twilios-request-to-your-application "the TwiML parameters that describe the message").

* * *

## PhoneNumber Properties

phonenumber-properties page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescriptionChild properties

sidSID<PN>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique string that we created to identify the PhoneNumber resource.

Pattern: `^PN[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

accountSidSID<AC>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that created the PhoneNumber resource.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

serviceSidSID<MG>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Service](/docs/chat/rest/service-resource "Service") the resource is associated with.

Pattern: `^MG[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

dateCreatedstring<date-time>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date and time in GMT when the resource was created specified in [ISO 8601(link takes you to an external page)](https://en.wikipedia.org/wiki/ISO_8601 "ISO 8601") format.

* * *

dateUpdatedstring<date-time>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date and time in GMT when the resource was last updated specified in [ISO 8601(link takes you to an external page)](https://en.wikipedia.org/wiki/ISO_8601 "ISO 8601") format.

* * *

phoneNumberstring<phone-number>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The phone number in [E.164](/docs/glossary/what-e164 "E.164") format, which consists of a + followed by the country code and subscriber number.

* * *

countryCodestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The 2-character [ISO Country Code(link takes you to an external page)](https://www.iso.org/iso-3166-country-codes.html "ISO Country Code") of the number.

* * *

capabilitiesarray[string]

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

An array of values that describe whether the number can receive calls or messages. Can be: `Voice`, `SMS`, and `MMS`.

* * *

urlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The absolute URL of the PhoneNumber resource.

* * *

## Create a PhoneNumber

create-a-phonenumber page anchor

Positive FeedbackNegative Feedback

`POST https://messaging.twilio.com/v1/Services/{ServiceSid}/PhoneNumbers`

Add a phone number to your Messaging Service.

Each Service can have no more than 400 phone numbers by default. If you think you might need a higher limit, [contact Twilio Support(link takes you to an external page)](https://www.twilio.com/console/support/tickets/create "contact Twilio Support") about a Messaging Service number limit increase, and include an explanation of your use case.

### Path parameters

path-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

serviceSidSID<MG>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Service](/docs/chat/rest/service-resource "Service") to create the resource under.

Pattern: `^MG[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

### Request body parameters

request-body-parameters page anchor

Positive FeedbackNegative Feedback

Encoding type:`application/x-www-form-urlencoded`

SchemaExample

Property nameTypeRequiredPIIDescriptionChild properties

phoneNumberSidSID<PN>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the Phone Number being added to the Service.

Pattern: `^PN[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

Select from available examples

Copy code block


    {


      "PhoneNumberSid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    }

Create a PhoneNumber for a Messaging ServiceLink to code sample: Create a PhoneNumber for a Messaging Service

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

    async function createPhoneNumber() {


    11

      const phoneNumber = await client.messaging.v1


    12

        .services("MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .phoneNumbers.create({


    14

          phoneNumberSid: "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    15

        });


    16




    17

      console.log(phoneNumber.sid);


    18

    }


    19




    20

    createPhoneNumber();

### Response

Note about this response

Copy response


    1

    {


    2

      "sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "service_sid": "MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

      "date_created": "2015-07-30T20:12:31Z",


    6

      "date_updated": "2015-07-30T20:12:33Z",


    7

      "phone_number": "+987654321",


    8

      "country_code": "US",


    9

      "capabilities": [


    10

        "MMS",


    11

        "SMS",


    12

        "Voice"


    13

      ],


    14

      "url": "https://messaging.twilio.com/v1/Services/MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/PhoneNumbers/PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    15

    }

* * *

## Retrieve a PhoneNumber

retrieve-a-phonenumber page anchor

Positive FeedbackNegative Feedback

`GET https://messaging.twilio.com/v1/Services/{ServiceSid}/PhoneNumbers/{Sid}`

### Path parameters

path-parameters-1 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

serviceSidSID<MG>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Service](/docs/chat/rest/service-resource "Service") to fetch the resource from.

Pattern: `^MG[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

sidstring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the PhoneNumber resource to fetch.

Retrieve a PhoneNumber from a Messaging ServiceLink to code sample: Retrieve a PhoneNumber from a Messaging Service

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

    async function fetchPhoneNumber() {


    11

      const phoneNumber = await client.messaging.v1


    12

        .services("MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .phoneNumbers("PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    14

        .fetch();


    15




    16

      console.log(phoneNumber.sid);


    17

    }


    18




    19

    fetchPhoneNumber();

### Response

Note about this response

Copy response


    1

    {


    2

      "sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "service_sid": "MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

      "date_created": "2015-07-30T20:12:31Z",


    6

      "date_updated": "2015-07-30T20:12:33Z",


    7

      "phone_number": "12345",


    8

      "country_code": "US",


    9

      "capabilities": [],


    10

      "url": "https://messaging.twilio.com/v1/Services/MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/PhoneNumbers/PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    11

    }

* * *

## Retrieve a list of PhoneNumbers

retrieve-a-list-of-phonenumbers page anchor

Positive FeedbackNegative Feedback

`GET https://messaging.twilio.com/v1/Services/{ServiceSid}/PhoneNumbers`

### Path parameters

path-parameters-2 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

serviceSidSID<MG>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Service](/docs/chat/rest/service-resource "Service") to read the resources from.

Pattern: `^MG[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

### Query parameters

query-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

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

Retrieve a list of PhoneNumbers from a Messaging ServiceLink to code sample: Retrieve a list of PhoneNumbers from a Messaging Service

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

    async function listPhoneNumber() {


    11

      const phoneNumbers = await client.messaging.v1


    12

        .services("MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .phoneNumbers.list({ limit: 20 });


    14




    15

      phoneNumbers.forEach((p) => console.log(p.sid));


    16

    }


    17




    18

    listPhoneNumber();

### Response

Note about this response

Copy response


    1

    {


    2

      "meta": {


    3

        "page": 0,


    4

        "page_size": 20,


    5

        "first_page_url": "https://messaging.twilio.com/v1/Services/MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/PhoneNumbers?PageSize=20&Page=0",


    6

        "previous_page_url": null,


    7

        "next_page_url": null,


    8

        "key": "phone_numbers",


    9

        "url": "https://messaging.twilio.com/v1/Services/MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/PhoneNumbers?PageSize=20&Page=0"


    10

      },


    11

      "phone_numbers": [


    12

        {


    13

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    14

          "service_sid": "MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    15

          "sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    16

          "date_created": "2015-07-30T20:12:31Z",


    17

          "date_updated": "2015-07-30T20:12:33Z",


    18

          "phone_number": "+987654321",


    19

          "country_code": "US",


    20

          "capabilities": [],


    21

          "url": "https://messaging.twilio.com/v1/Services/MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/PhoneNumbers/PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    22

        }


    23

      ]


    24

    }

* * *

## Delete a PhoneNumbers subresource

delete-a-phonenumbers-subresource page anchor

Positive FeedbackNegative Feedback

`DELETE https://messaging.twilio.com/v1/Services/{ServiceSid}/PhoneNumbers/{Sid}`

(warning)

## Warning

Removing a phone number from the Service does not release the number from your account. You must release a phone number from your Account to disassociate and delete the phone number from the Service.

Returns a "204 NO CONTENT" if the phone number was successfully removed from the service.

### Path parameters

path-parameters-3 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

serviceSidSID<MG>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Service](/docs/chat/rest/service-resource "Service") to delete the resource from.

Pattern: `^MG[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

sidstring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the PhoneNumber resource to delete.

Delete a Phone Number from a Messaging ServiceLink to code sample: Delete a Phone Number from a Messaging Service

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

    async function deletePhoneNumber() {


    11

      await client.messaging.v1


    12

        .services("MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .phoneNumbers("PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    14

        .remove();


    15

    }


    16




    17

    deletePhoneNumber();