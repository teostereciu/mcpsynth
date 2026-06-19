# ShortCodes subresource

*Source: https://www.twilio.com/docs/messaging/api/services-shortcode-resource*

---

# ShortCodes subresource

Positive FeedbackNegative Feedback

* * *

(new)

## Public Beta

The Services resource is currently available as a Public Beta product. This means that some features for configuring your Messaging Service via the REST API are not yet implemented, and others may be changed before the product is declared Generally Available. Messaging Service Configuration through the [Twilio Console(link takes you to an external page)](https://www.twilio.com/console "Twilio Console") is Generally Available.

Public Beta products are [not covered by a Twilio SLA(link takes you to an external page)](https://help.twilio.com/hc/en-us/articles/115002413087-Twilio-Beta-product-support "not covered by a Twilio SLA").

The resources for sending Messages with a Messaging Service are Generally Available.

ShortCodes is a subresource of [Services](/docs/messaging/api/service-resource "Services") and represents the short codes you have associated to the Service.

When a short code has been added to the Messaging Service, Twilio always prioritizes message delivery with your short code when possible. If the short code cannot be used to reach your user, Twilio automatically [falls back to a long code](/docs/messaging/services#sender-selection "falls back to a long code") in your Messaging Service instead.

Inbound messages received on any of short codes associated with a Messaging Service are passed to the inbound request URL of the Service with [the TwiML parameters that describe the message](/docs/messaging/twiml "the TwiML parameters that describe the message").

* * *

## ShortCode Properties

shortcode-properties page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescriptionChild properties

sidSID<SC>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique string that we created to identify the ShortCode resource.

Pattern: `^SC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

accountSidSID<AC>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that created the ShortCode resource.

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

shortCodestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The [E.164](/docs/glossary/what-e164 "E.164") format of the short code.

* * *

countryCodestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The 2-character [ISO Country Code(link takes you to an external page)](https://www.iso.org/iso-3166-country-codes.html "ISO Country Code") of the number.

* * *

capabilitiesarray[string]

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

An array of values that describe whether the number can receive calls or messages. Can be: `SMS` and `MMS`.

* * *

urlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The absolute URL of the ShortCode resource.

* * *

## Create a ShortCode

create-a-shortcode page anchor

Positive FeedbackNegative Feedback

`POST https://messaging.twilio.com/v1/Services/{ServiceSid}/ShortCodes`

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

shortCodeSidSID<SC>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the ShortCode resource being added to the Service.

Pattern: `^SC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

Select from available examples

Copy code block


    {


      "ShortCodeSid": "SCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    }

Create a ShortCode for a Messaging ServiceLink to code sample: Create a ShortCode for a Messaging Service

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

    async function createShortCode() {


    11

      const shortCode = await client.messaging.v1


    12

        .services("MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .shortCodes.create({ shortCodeSid: "SCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" });


    14




    15

      console.log(shortCode.sid);


    16

    }


    17




    18

    createShortCode();

### Response

Note about this response

Copy response


    1

    {


    2

      "sid": "SCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "service_sid": "MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

      "date_created": "2015-07-30T20:12:31Z",


    6

      "date_updated": "2015-07-30T20:12:33Z",


    7

      "short_code": "12345",


    8

      "country_code": "US",


    9

      "capabilities": [


    10

        "SMS"


    11

      ],


    12

      "url": "https://messaging.twilio.com/v1/Services/MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ShortCodes/SCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    13

    }

* * *

## Retrieve a ShortCode

retrieve-a-shortcode page anchor

Positive FeedbackNegative Feedback

`GET https://messaging.twilio.com/v1/Services/{ServiceSid}/ShortCodes/{Sid}`

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

The SID of the ShortCode resource to fetch.

Retrieve a ShortCode from a Messaging ServiceLink to code sample: Retrieve a ShortCode from a Messaging Service

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

    async function fetchShortCode() {


    11

      const shortCode = await client.messaging.v1


    12

        .services("MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .shortCodes("SCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    14

        .fetch();


    15




    16

      console.log(shortCode.sid);


    17

    }


    18




    19

    fetchShortCode();

### Response

Note about this response

Copy response


    1

    {


    2

      "sid": "SCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "service_sid": "MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

      "date_created": "2015-07-30T20:12:31Z",


    6

      "date_updated": "2015-07-30T20:12:33Z",


    7

      "short_code": "12345",


    8

      "country_code": "US",


    9

      "capabilities": [


    10

        "SMS"


    11

      ],


    12

      "url": "https://messaging.twilio.com/v1/Services/MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ShortCodes/SCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    13

    }

* * *

## Retrieve a list of ShortCodes

retrieve-a-list-of-shortcodes page anchor

Positive FeedbackNegative Feedback

`GET https://messaging.twilio.com/v1/Services/{ServiceSid}/ShortCodes`

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

Retrieve a list of ShortCodes from a Messaging ServiceLink to code sample: Retrieve a list of ShortCodes from a Messaging Service

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

    async function listShortCode() {


    11

      const shortCodes = await client.messaging.v1


    12

        .services("MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .shortCodes.list({ limit: 20 });


    14




    15

      shortCodes.forEach((s) => console.log(s.sid));


    16

    }


    17




    18

    listShortCode();

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

        "first_page_url": "https://messaging.twilio.com/v1/Services/MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ShortCodes?PageSize=20&Page=0",


    6

        "previous_page_url": null,


    7

        "next_page_url": null,


    8

        "key": "short_codes",


    9

        "url": "https://messaging.twilio.com/v1/Services/MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ShortCodes?PageSize=20&Page=0"


    10

      },


    11

      "short_codes": [


    12

        {


    13

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    14

          "service_sid": "MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    15

          "sid": "SCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    16

          "date_created": "2015-07-30T20:12:31Z",


    17

          "date_updated": "2015-07-30T20:12:33Z",


    18

          "short_code": "12345",


    19

          "country_code": "US",


    20

          "capabilities": [


    21

            "SMS"


    22

          ],


    23

          "url": "https://messaging.twilio.com/v1/Services/MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ShortCodes/SCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    24

        }


    25

      ]


    26

    }

* * *

## Delete a ShortCode

delete-a-shortcode page anchor

Positive FeedbackNegative Feedback

`DELETE https://messaging.twilio.com/v1/Services/{ServiceSid}/ShortCodes/{Sid}`

(warning)

## Warning

Removing a short code from the Messaging Service does not release the short code from your account. You must cancel the short code from your Account in order to disassociate and delete the short code from your Messaging Service.

Returns a `204 NO CONTENT` if the short code was successfully removed from the service.

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

The SID of the ShortCode resource to delete.

Delete a ShortCode from a Messaging ServiceLink to code sample: Delete a ShortCode from a Messaging Service

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

    async function deleteShortCode() {


    11

      await client.messaging.v1


    12

        .services("MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .shortCodes("SCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    14

        .remove();


    15

    }


    16




    17

    deleteShortCode();