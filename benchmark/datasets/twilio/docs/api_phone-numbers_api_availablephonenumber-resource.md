# AvailablePhoneNumber resource

*Source: https://www.twilio.com/docs/phone-numbers/api/availablephonenumber-resource*

---

# AvailablePhoneNumber resource

Positive FeedbackNegative Feedback

* * *

The `AvailablePhoneNumbers` resource and its subresources let you search for local, toll-free, and mobile phone numbers that you can purchase. You can search for phone numbers that:

  * Match a specific pattern
  * Are in a specific country
  * Belong to a particular area code (NPA) or exchange (NXX)
  * Fall within a defined geographic region


To find available numbers, make a request to one of the following subresources:

  * [AvailablePhoneNumbers Local subresource](/docs/phone-numbers/api/availablephonenumberlocal-resource "AvailablePhoneNumbers Local subresource")
  * [AvailablePhoneNumbers TollFree subresource](/docs/phone-numbers/api/availablephonenumber-tollfree-resource "AvailablePhoneNumbers TollFree subresource")
  * [AvailablePhoneNumbers Mobile subresource](/docs/phone-numbers/api/availablephonenumber-mobile-resource "AvailablePhoneNumbers Mobile subresource")


(information)

## Info

After you identify a number to purchase, provision it with the [Incoming Phone Numbers API](/docs/phone-numbers/api/incomingphonenumber-resource "Incoming Phone Numbers API").

* * *

## Supported Countries and Types

supported-countries-and-types page anchor

Positive FeedbackNegative Feedback

To list the subresources available to your account in a given country, query the `AvailablePhoneNumbers` resource. For full information about our phone number support, see [Twilio phone number availability and their capabilities(link takes you to an external page)](https://help.twilio.com/articles/223183068 "Twilio phone number availability and their capabilities") and [Twilio phone number types and their capabilities(link takes you to an external page)](https://help.twilio.com/articles/223135367 "Twilio phone number types and their capabilities"). Each resource instance has the following properties.

Property nameTypeRequiredPIIDescriptionChild properties

countryCodestring<iso-country-code>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The [ISO-3166-1(link takes you to an external page)](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2 "ISO-3166-1") country code of the country.

* * *

countrystring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The name of the country.

* * *

uristring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URI of the Country resource, relative to `https://api.twilio.com`.

* * *

betaboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether all phone numbers available in the country are new to the Twilio platform. `true` if they are and `false` if all numbers are not in the Twilio Phone Number Beta program.

* * *

subresourceUrisobject<uri-map>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A list of related AvailablePhoneNumber resources identified by their URIs relative to `https://api.twilio.com`.

* * *

## Fetch a specific country

fetch-a-specific-country page anchor

Positive FeedbackNegative Feedback

`GET https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/AvailablePhoneNumbers/{CountryCode}.json`

### Path parameters

path-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

accountSidSID<AC>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") requesting the available phone number Country resource.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

countryCodestring<iso-country-code>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The [ISO-3166-1(link takes you to an external page)](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2 "ISO-3166-1") country code of the country to fetch available phone number information about.

The following example shows how to fetch information about available phone numbers in a specific country:

Fetch a specific countryLink to code sample: Fetch a specific country

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

    async function fetchAvailablePhoneNumberCountry() {


    11

      const availablePhoneNumber = await client.availablePhoneNumbers("US").fetch();


    12




    13

      console.log(availablePhoneNumber.countryCode);


    14

    }


    15




    16

    fetchAvailablePhoneNumberCountry();

### Response

Note about this response

Copy response


    1

    {


    2

      "beta": false,


    3

      "country": "United States",


    4

      "country_code": "US",


    5

      "subresource_uris": {


    6

        "local": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AvailablePhoneNumbers/US/Local.json",


    7

        "toll_free": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AvailablePhoneNumbers/US/TollFree.json"


    8

      },


    9

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AvailablePhoneNumbers/US.json"


    10

    }

* * *

## Read a list of countries

read-a-list-of-countries page anchor

Positive FeedbackNegative Feedback

`GET https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/AvailablePhoneNumbers.json`

### Path parameters

path-parameters-1 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

accountSidSID<AC>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") requesting the available phone number Country resources.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

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

The following example shows how to retrieve a list of all countries where phone numbers are available:

Read a list of countriesLink to code sample: Read a list of countries

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

    async function listAvailablePhoneNumberCountry() {


    11

      const availablePhoneNumbers = await client.availablePhoneNumbers.list({


    12

        limit: 20,


    13

      });


    14




    15

      availablePhoneNumbers.forEach((a) => console.log(a.countryCode));


    16

    }


    17




    18

    listAvailablePhoneNumberCountry();

### Response

Note about this response

Copy response


    1

    {


    2

      "countries": [


    3

        {


    4

          "beta": false,


    5

          "country": "Denmark",


    6

          "country_code": "DK",


    7

          "subresource_uris": {


    8

            "local": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AvailablePhoneNumbers/DK/Local.json",


    9

            "toll_free": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AvailablePhoneNumbers/DK/TollFree.json"


    10

          },


    11

          "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AvailablePhoneNumbers/DK.json"


    12

        },


    13

        {


    14

          "beta": false,


    15

          "country": "Australia",


    16

          "country_code": "AU",


    17

          "subresource_uris": {


    18

            "local": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AvailablePhoneNumbers/AU/Local.json",


    19

            "mobile": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AvailablePhoneNumbers/AU/Mobile.json",


    20

            "toll_free": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AvailablePhoneNumbers/AU/TollFree.json"


    21

          },


    22

          "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AvailablePhoneNumbers/AU.json"


    23

        }


    24

      ],


    25

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AvailablePhoneNumbers.json"


    26

    }