# Dialing Permissions - HighRiskSpecialPrefixes subresource

*Source: https://www.twilio.com/docs/voice/api/dialingpermissions-highriskspecialprefix-resource*

---

# Dialing Permissions - HighRiskSpecialPrefixes subresource

Positive FeedbackNegative Feedback

* * *

HighRiskSpecialPrefixes is a subresource of [Countries](/docs/voice/api/dialingpermissions-country-resource "Countries") and represents a list of high-risk prefixes for a specific country.

* * *

## HighRiskSpecialPrefixes properties

highriskspecialprefixes-properties page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescriptionChild properties

prefixstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A prefix is a contiguous number range for a block of E.164 numbers that includes the E.164 assigned country code. For example, a North American Numbering Plan prefix like `+1510720` written like `+1(510) 720` matches all numbers inclusive from `+1(510) 720-0000` to `+1(510) 720-9999`.

* * *

## Retrieve a list of HighRiskSpecialPrefixes

retrieve-a-list-of-highriskspecialprefixes page anchor

Positive FeedbackNegative Feedback

`GET https://voice.twilio.com/v1/DialingPermissions/Countries/{IsoCode}/HighRiskSpecialPrefixes`

### Path parameters

path-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

isoCodestring<iso-country-code>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The [ISO 3166-1 country code(link takes you to an external page)](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2 "ISO 3166-1 country code") to identify the country permissions from which high-risk special service number prefixes are fetched

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

Read multiple DialingPermissions HighRiskSpecialPrefix resourcesLink to code sample: Read multiple DialingPermissions HighRiskSpecialPrefix resources

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

    async function listDialingPermissionsHrsPrefixes() {


    11

      const highriskSpecialPrefixes = await client.voice.v1.dialingPermissions


    12

        .countries("LV")


    13

        .highriskSpecialPrefixes.list({ limit: 20 });


    14




    15

      highriskSpecialPrefixes.forEach((h) => console.log(h.prefix));


    16

    }


    17




    18

    listDialingPermissionsHrsPrefixes();

### Response

Note about this response

Copy response


    1

    {


    2

      "content": [


    3

        {


    4

          "prefix": "+37181"


    5

        },


    6

        {


    7

          "prefix": "+3719000"


    8

        }


    9

      ],


    10

      "meta": {


    11

        "first_page_url": "https://voice.twilio.com/v1/DialingPermissions/Countries/LV/HighRiskSpecialPrefixes?PageSize=50&Page=0",


    12

        "key": "content",


    13

        "next_page_url": null,


    14

        "page": 0,


    15

        "page_size": 50,


    16

        "previous_page_url": null,


    17

        "url": "https://voice.twilio.com/v1/DialingPermissions/Countries/LV/HighRiskSpecialPrefixes?PageSize=50&Page=0"


    18

      }


    19

    }