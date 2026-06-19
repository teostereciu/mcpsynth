# Dialing Permissions - Countries resource

*Source: https://www.twilio.com/docs/voice/api/dialingpermissions-country-resource*

---

# Dialing Permissions - Countries resource

Positive FeedbackNegative Feedback

* * *

Voice dialing permissions are organized by country and identified by the country's [ISO(link takes you to an external page)](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2 "ISO") code.

* * *

## Countries properties

countries-properties page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescriptionChild properties

isoCodestring<iso-country-code>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The [ISO country code(link takes you to an external page)](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2 "ISO country code").

* * *

namestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The name of the country.

* * *

continentstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The name of the continent in which the country is located.

* * *

countryCodesarray[string]

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The E.164 assigned [country codes(s)(link takes you to an external page)](https://www.itu.int/itudoc/itu-t/ob-lists/icc/e164_763.html "country codes\(s\)")

* * *

lowRiskNumbersEnabledboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether dialing to low-risk numbers is enabled.

* * *

highRiskSpecialNumbersEnabledboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether dialing to high-risk special services numbers is enabled. These prefixes include number ranges allocated by the country and include premium numbers, special services, shared cost, and others

* * *

highRiskTollfraudNumbersEnabledboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether dialing to high-risk [toll fraud(link takes you to an external page)](https://www.twilio.com/blog/how-to-protect-your-account-from-toll-fraud-with-voice-dialing-geo-permissions-html "toll fraud") numbers is enabled. These prefixes include narrow number ranges that have a high-risk of international revenue sharing fraud (IRSF) attacks, also known as [toll fraud(link takes you to an external page)](https://www.twilio.com/blog/how-to-protect-your-account-from-toll-fraud-with-voice-dialing-geo-permissions-html "toll fraud"). These prefixes are collected from anti-fraud databases and verified by analyzing calls on our network. These prefixes are not available for download and are updated frequently

* * *

urlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The absolute URL of this resource.

* * *

linksobject<uri-map>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A list of URLs related to this resource.

* * *

## Retrieve a Country

retrieve-a-country page anchor

Positive FeedbackNegative Feedback

`GET https://voice.twilio.com/v1/DialingPermissions/Countries/{IsoCode}`

### Path parameters

path-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

isoCodestring<iso-country-code>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The [ISO country code(link takes you to an external page)](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2 "ISO country code") of the DialingPermissions Country resource to fetch

Retrieve a CountryLink to code sample: Retrieve a Country

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

    async function fetchDialingPermissionsCountry() {


    11

      const country = await client.voice.v1.dialingPermissions


    12

        .countries("US")


    13

        .fetch();


    14




    15

      console.log(country.isoCode);


    16

    }


    17




    18

    fetchDialingPermissionsCountry();

### Response

Note about this response

Copy response


    1

    {


    2

      "iso_code": "US",


    3

      "name": "United States/Canada",


    4

      "country_codes": [


    5

        "+1"


    6

      ],


    7

      "continent": "NORTH_AMERICA",


    8

      "low_risk_numbers_enabled": false,


    9

      "high_risk_special_numbers_enabled": false,


    10

      "high_risk_tollfraud_numbers_enabled": false,


    11

      "url": "https://voice.twilio.com/v1/DialingPermissions/Countries/US",


    12

      "links": {


    13

        "highrisk_special_prefixes": "https://voice.twilio.com/v1/DialingPermissions/Countries/US/HighRiskSpecialPrefixes"


    14

      }


    15

    }

* * *

## Retrieve a list of Countries

retrieve-a-list-of-countries page anchor

Positive FeedbackNegative Feedback

`GET https://voice.twilio.com/v1/DialingPermissions/Countries`

### Query parameters

query-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

isoCodestring<iso-country-code>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Filter to retrieve the country permissions by specifying the [ISO country code(link takes you to an external page)](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2 "ISO country code")

* * *

continentstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Filter to retrieve the country permissions by specifying the continent

* * *

countryCodestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Filter the results by specified [country codes(link takes you to an external page)](https://www.itu.int/itudoc/itu-t/ob-lists/icc/e164_763.html "country codes")

* * *

lowRiskNumbersEnabledboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Filter to retrieve the country permissions with dialing to low-risk numbers enabled. Can be: `true` or `false`.

* * *

highRiskSpecialNumbersEnabledboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Filter to retrieve the country permissions with dialing to high-risk special service numbers enabled. Can be: `true` or `false`

* * *

highRiskTollfraudNumbersEnabledboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Filter to retrieve the country permissions with dialing to high-risk [toll fraud(link takes you to an external page)](https://www.twilio.com/blog/how-to-protect-your-account-from-toll-fraud-with-voice-dialing-geo-permissions-html "toll fraud") numbers enabled. Can be: `true` or `false`.

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

Retrieve a list of CountriesLink to code sample: Retrieve a list of Countries

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

    async function listDialingPermissionsCountry() {


    11

      const countries = await client.voice.v1.dialingPermissions.countries.list({


    12

        limit: 20,


    13

      });


    14




    15

      countries.forEach((c) => console.log(c.isoCode));


    16

    }


    17




    18

    listDialingPermissionsCountry();

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

          "iso_code": "US",


    5

          "name": "United States/Canada",


    6

          "country_codes": [


    7

            "+1"


    8

          ],


    9

          "continent": "NORTH_AMERICA",


    10

          "low_risk_numbers_enabled": false,


    11

          "high_risk_special_numbers_enabled": false,


    12

          "high_risk_tollfraud_numbers_enabled": false,


    13

          "url": "https://voice.twilio.com/v1/DialingPermissions/Countries/US",


    14

          "links": {


    15

            "highrisk_special_prefixes": "https://voice.twilio.com/v1/DialingPermissions/Countries/US/HighRiskSpecialPrefixes"


    16

          }


    17

        }


    18

      ],


    19

      "meta": {


    20

        "first_page_url": "https://voice.twilio.com/v1/DialingPermissions/Countries?IsoCode=US&PageSize=50&Page=0",


    21

        "key": "content",


    22

        "next_page_url": null,


    23

        "page": 0,


    24

        "page_size": 50,


    25

        "previous_page_url": null,


    26

        "url": "https://voice.twilio.com/v1/DialingPermissions/Countries?IsoCode=US&PageSize=50&Page=0"


    27

      }


    28

    }