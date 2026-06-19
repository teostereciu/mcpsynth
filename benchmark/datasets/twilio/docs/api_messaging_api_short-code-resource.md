# ShortCodes resource

*Source: https://www.twilio.com/docs/messaging/api/short-code-resource*

---

# ShortCodes resource

Positive FeedbackNegative Feedback

* * *

A [short code](/docs/glossary/what-is-a-short-code "short code") is a 5 or 6-digit number that can send and receive messages with mobile phones. These high-throughput numbers are perfect for apps that need to send messages to lots of users or need to send time-sensitive messages. You can [buy short codes from Twilio(link takes you to an external page)](https://www.twilio.com/console/sms/short-codes "buy short codes from Twilio") or [port existing short codes to Twilio(link takes you to an external page)](https://www.twilio.com/console/phone-numbers/porting-requests/port "port existing short codes to Twilio").

To send messages from your short code, see the [Sending Messages](/docs/messaging/quickstart "Sending Messages") documentation.

* * *

## ShortCode Properties

shortcode-properties page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescriptionChild properties

accountSidSID<AC>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that created this ShortCode resource.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

apiVersionstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The API version used to start a new TwiML session when an SMS message is sent to this short code.

* * *

dateCreatedstring<date-time-rfc-2822>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date and time in GMT that this resource was created specified in [RFC 2822(link takes you to an external page)](https://www.ietf.org/rfc/rfc2822.txt "RFC 2822") format.

* * *

dateUpdatedstring<date-time-rfc-2822>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date and time in GMT that this resource was last updated, specified in [RFC 2822(link takes you to an external page)](https://www.ietf.org/rfc/rfc2822.txt "RFC 2822") format.

* * *

friendlyNamestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A string that you assigned to describe this resource. By default, the `FriendlyName` is the short code.

* * *

shortCodestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The short code. e.g., 894546.

* * *

sidSID<SC>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique string that that we created to identify this ShortCode resource.

Pattern: `^SC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

smsFallbackMethodenum<http-method>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The HTTP method we use to call the `sms_fallback_url`. Can be: `GET` or `POST`.

Possible values:

`GET``POST`

* * *

smsFallbackUrlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL that we call if an error occurs while retrieving or executing the TwiML from `sms_url`.

* * *

smsMethodenum<http-method>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The HTTP method we use to call the `sms_url`. Can be: `GET` or `POST`.

Possible values:

`GET``POST`

* * *

smsUrlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL we call when receiving an incoming SMS message to this short code.

* * *

uristring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URI of this resource, relative to `https://api.twilio.com`.

* * *

## Retrieve a ShortCode

retrieve-a-shortcode page anchor

Positive FeedbackNegative Feedback

`GET https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/SMS/ShortCodes/{Sid}.json`

### Path parameters

path-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

accountSidSID<AC>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that created the ShortCode resource(s) to fetch.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

sidSID<SC>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The Twilio-provided string that uniquely identifies the ShortCode resource to fetch

Pattern: `^SC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

Fetch a ShortCodeLink to code sample: Fetch a ShortCode

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

      const shortCode = await client


    12

        .shortCodes("SCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .fetch();


    14




    15

      console.log(shortCode.accountSid);


    16

    }


    17




    18

    fetchShortCode();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "api_version": "2010-04-01",


    4

      "date_created": "Thu, 01 Apr 2010 00:00:00 +0000",


    5

      "date_updated": "Thu, 01 Apr 2010 00:00:00 +0000",


    6

      "friendly_name": "API_CLUSTER_TEST_SHORT_CODE",


    7

      "short_code": "99990",


    8

      "sid": "SCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    9

      "sms_fallback_method": "POST",


    10

      "sms_fallback_url": null,


    11

      "sms_method": "POST",


    12

      "sms_url": null,


    13

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/ShortCodes/SCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"


    14

    }

* * *

## Retrieve a list of ShortCodes

retrieve-a-list-of-shortcodes page anchor

Positive FeedbackNegative Feedback

`GET https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/SMS/ShortCodes.json`

Returns a list of ShortCodes, each representing a short code within your account. This list includes [paging information](/docs/usage/twilios-response "paging information").

### Filter the list Twilio returns

filter-the-list-twilio-returns page anchor

Positive FeedbackNegative Feedback

The following query string parameters allow you to limit the list returned.

### Path parameters

path-parameters-1 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

accountSidSID<AC>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that created the ShortCode resource(s) to read.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

### Query parameters

query-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

friendlyNamestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The string that identifies the ShortCode resources to read.

* * *

shortCodestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Only show the ShortCode resources that match this pattern. You can specify partial numbers and use '*' as a wildcard for any digit.

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

Retrieve a list of ShortCodes from your AccountLink to code sample: Retrieve a list of ShortCodes from your Account

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

      const shortCodes = await client.shortCodes.list({ limit: 20 });


    12




    13

      shortCodes.forEach((s) => console.log(s.accountSid));


    14

    }


    15




    16

    listShortCode();

### Response

Note about this response

Copy response


    1

    {


    2

      "end": 0,


    3

      "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/ShortCodes.json?FriendlyName=friendly_name&ShortCode=short_code&PageSize=50&Page=0",


    4

      "next_page_uri": null,


    5

      "page": 0,


    6

      "page_size": 50,


    7

      "previous_page_uri": null,


    8

      "short_codes": [


    9

        {


    10

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    11

          "api_version": "2010-04-01",


    12

          "date_created": "Thu, 01 Apr 2010 00:00:00 +0000",


    13

          "date_updated": "Thu, 01 Apr 2010 00:00:00 +0000",


    14

          "friendly_name": "API_CLUSTER_TEST_SHORT_CODE",


    15

          "short_code": "99990",


    16

          "sid": "SCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    17

          "sms_fallback_method": "POST",


    18

          "sms_fallback_url": null,


    19

          "sms_method": "POST",


    20

          "sms_url": null,


    21

          "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/ShortCodes/SCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"


    22

        }


    23

      ],


    24

      "start": 0,


    25

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/ShortCodes.json?FriendlyName=friendly_name&ShortCode=short_code&PageSize=50&Page=0"


    26

    }

Retrieve a list of ShortCodes with an exact matchLink to code sample: Retrieve a list of ShortCodes with an exact match

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

      const shortCodes = await client.shortCodes.list({


    12

        shortCode: "67898",


    13

        limit: 20,


    14

      });


    15




    16

      shortCodes.forEach((s) => console.log(s.accountSid));


    17

    }


    18




    19

    listShortCode();

### Response

Note about this response

Copy response


    1

    {


    2

      "end": 0,


    3

      "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/ShortCodes.json?FriendlyName=friendly_name&ShortCode=short_code&PageSize=50&Page=0",


    4

      "next_page_uri": null,


    5

      "page": 0,


    6

      "page_size": 50,


    7

      "previous_page_uri": null,


    8

      "short_codes": [


    9

        {


    10

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    11

          "api_version": "2010-04-01",


    12

          "date_created": "Thu, 01 Apr 2010 00:00:00 +0000",


    13

          "date_updated": "Thu, 01 Apr 2010 00:00:00 +0000",


    14

          "friendly_name": "API_CLUSTER_TEST_SHORT_CODE",


    15

          "short_code": "99990",


    16

          "sid": "SCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    17

          "sms_fallback_method": "POST",


    18

          "sms_fallback_url": null,


    19

          "sms_method": "POST",


    20

          "sms_url": null,


    21

          "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/ShortCodes/SCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"


    22

        }


    23

      ],


    24

      "start": 0,


    25

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/ShortCodes.json?FriendlyName=friendly_name&ShortCode=short_code&PageSize=50&Page=0"


    26

    }

Retrieve a list of ShortCodes resources with a partial matchLink to code sample: Retrieve a list of ShortCodes resources with a partial match

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

      const shortCodes = await client.shortCodes.list({


    12

        shortCode: "898",


    13

        limit: 20,


    14

      });


    15




    16

      shortCodes.forEach((s) => console.log(s.accountSid));


    17

    }


    18




    19

    listShortCode();

### Response

Note about this response

Copy response


    1

    {


    2

      "end": 0,


    3

      "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/ShortCodes.json?FriendlyName=friendly_name&ShortCode=short_code&PageSize=50&Page=0",


    4

      "next_page_uri": null,


    5

      "page": 0,


    6

      "page_size": 50,


    7

      "previous_page_uri": null,


    8

      "short_codes": [


    9

        {


    10

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    11

          "api_version": "2010-04-01",


    12

          "date_created": "Thu, 01 Apr 2010 00:00:00 +0000",


    13

          "date_updated": "Thu, 01 Apr 2010 00:00:00 +0000",


    14

          "friendly_name": "API_CLUSTER_TEST_SHORT_CODE",


    15

          "short_code": "99990",


    16

          "sid": "SCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    17

          "sms_fallback_method": "POST",


    18

          "sms_fallback_url": null,


    19

          "sms_method": "POST",


    20

          "sms_url": null,


    21

          "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/ShortCodes/SCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"


    22

        }


    23

      ],


    24

      "start": 0,


    25

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/ShortCodes.json?FriendlyName=friendly_name&ShortCode=short_code&PageSize=50&Page=0"


    26

    }

* * *

## Update a ShortCode

update-a-shortcode page anchor

Positive FeedbackNegative Feedback

`POST https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/SMS/ShortCodes/{Sid}.json`

Tries to update the short code's properties. This API call returns the updated resource representation if it is successful. The returned response is identical to that returned when making a `GET` request.

### Path parameters

path-parameters-2 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

accountSidSID<AC>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that created the ShortCode resource(s) to update.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

sidSID<SC>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The Twilio-provided string that uniquely identifies the ShortCode resource to update

Pattern: `^SC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

### Request body parameters

request-body-parameters page anchor

Positive FeedbackNegative Feedback

Encoding type:`application/x-www-form-urlencoded`

SchemaExample

Property nameTypeRequiredPIIDescriptionChild properties

friendlyNamestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A descriptive string that you created to describe this resource. It can be up to 64 characters long. By default, the `FriendlyName` is the short code.

* * *

apiVersionstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The API version to use to start a new TwiML session. Can be: `2010-04-01` or `2008-08-01`.

* * *

smsUrlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL we should call when receiving an incoming SMS message to this short code.

* * *

smsMethodenum<http-method>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The HTTP method we should use when calling the `sms_url`. Can be: `GET` or `POST`.

Possible values:

`GET``POST`

* * *

smsFallbackUrlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL that we should call if an error occurs while retrieving or executing the TwiML from `sms_url`.

* * *

smsFallbackMethodenum<http-method>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The HTTP method that we should use to call the `sms_fallback_url`. Can be: `GET` or `POST`.

Possible values:

`GET``POST`

Copy code block


    {


      "ApiVersion": "2010-04-01",


      "FriendlyName": "friendly_name",


      "SmsFallbackMethod": "POST",


      "SmsFallbackUrl": "https://example.com",


      "SmsMethod": "POST",


      "SmsUrl": "https://example.com"


    }

Update a ShortCodeLink to code sample: Update a ShortCode

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

    async function updateShortCode() {


    11

      const shortCode = await client


    12

        .shortCodes("SC6b20cb705c1e8f00210049b20b70fce3")


    13

        .update({ smsUrl: "http://demo.twilio.com/docs/sms.xml" });


    14




    15

      console.log(shortCode.accountSid);


    16

    }


    17




    18

    updateShortCode();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    3

      "api_version": "2010-04-01",


    4

      "date_created": "Thu, 01 Apr 2010 00:00:00 +0000",


    5

      "date_updated": "Thu, 01 Apr 2010 00:00:00 +0000",


    6

      "friendly_name": "API_CLUSTER_TEST_SHORT_CODE",


    7

      "short_code": "99990",


    8

      "sid": "SC6b20cb705c1e8f00210049b20b70fce3",


    9

      "sms_fallback_method": "POST",


    10

      "sms_fallback_url": null,


    11

      "sms_method": "POST",


    12

      "sms_url": "http://demo.twilio.com/docs/sms.xml",


    13

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/ShortCodes/SCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"


    14

    }