# Pricing: Messaging Countries resource

*Source: https://www.twilio.com/docs/messaging/api/pricing*

---

# Pricing: Messaging Countries resource

Positive FeedbackNegative Feedback

* * *

You can pull real-time, account-specific pricing for Twilio's [Messaging API](/docs/messaging "Messaging API") product using the Pricing API.

Prices can be retrieved at a country level directly via the [Countries resource](/docs/messaging/api/pricing#fetch-a-countries-resource "Countries resource") or for a specific phone number by leveraging the Lookup API and Countries resource.

You may also wish to check out our Pricing API resources for Twilio's [Voice](/docs/voice/pricing "Voice") and [Phone Number](/docs/phone-numbers/pricing "Phone Number") products.

(information)

## Info

Looking for details on pricing for Twilio products? Check out Twilio's [pricing page(link takes you to an external page)](https://www.twilio.com/en-us/pricing "pricing page").

Copy code block


    1

    curl -G https://pricing.twilio.com/v1/Messaging/Countries/US \


    2

        -u '[YOUR ACCOUNT SID]:[YOUR AUTH TOKEN]'


    3

You can find your account SID and auth token on [your Twilio Console(link takes you to an external page)](https://www.twilio.com/console "your Twilio Console").

* * *

## Countries properties

countries-properties page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescriptionChild properties

countrystring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The name of the country.

* * *

isoCountrystring<iso-country-code>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The [ISO country code(link takes you to an external page)](http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2 "ISO country code").

* * *

urlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The absolute URL of the resource.

* * *

outboundSmsPricesarray[object<outbound-sms-price>]

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The list of [OutboundSMSPrice](/docs/sms/api/pricing#outbound-sms-price "OutboundSMSPrice") records that represent the price to send a message for each MCC/MNC applicable in this country.

Show outboundSmsPrices properties

Property nameTypeRequiredPIIDescriptionChild properties

carrierstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

* * *

mccstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

* * *

mncstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

* * *

pricesarray[object]

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Show prices properties

Property nameTypeRequiredPIIDescriptionChild properties

basePricenumber

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

* * *

currentPricenumber

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

* * *

numberTypestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

* * *

inboundSmsPricesarray[object<inbound-sms-price>]

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The list of [InboundPrice](/docs/sms/api/pricing#inbound-price "InboundPrice") records that describe the price to receive an inbound SMS to the different Twilio phone number types supported in this country

Show inboundSmsPrices properties

Property nameTypeRequiredPIIDescriptionChild properties

basePricenumber

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

* * *

currentPricenumber

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

* * *

numberTypestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

* * *

priceUnitstring<currency>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The currency in which prices are measured, specified in [ISO 4127(link takes you to an external page)](http://www.iso.org/iso/home/standards/currency_codes.htm "ISO 4127") format (e.g. `usd`, `eur`, `jpy`).

* * *

## Fetch a Countries resource

fetch-a-countries-resource page anchor

Positive FeedbackNegative Feedback

`GET https://pricing.twilio.com/v1/Messaging/Countries/{IsoCountry}`

In the above API call, {IsoCountry} is the [ISO 3166-1 alpha-2 format(link takes you to an external page)](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2 "ISO 3166-1 alpha-2 format") country code.

### Path parameters

path-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

isoCountrystring<iso-country-code>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The [ISO country code(link takes you to an external page)](http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2 "ISO country code") of the pricing information to fetch.

Fetch Messaging Prices for EstoniaLink to code sample: Fetch Messaging Prices for Estonia

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

    async function fetchMessagingCountry() {


    11

      const country = await client.pricing.v1.messaging.countries("EE").fetch();


    12




    13

      console.log(country.url);


    14

    }


    15




    16

    fetchMessagingCountry();

### Response

Note about this response

Copy response


    1

    {


    2

      "country": "country",


    3

      "inbound_sms_prices": [


    4

        {


    5

          "base_price": "0.05",


    6

          "current_price": "0.05",


    7

          "number_type": "mobile"


    8

        }


    9

      ],


    10

      "iso_country": "EE",


    11

      "outbound_sms_prices": [


    12

        {


    13

          "carrier": "att",


    14

          "mcc": "foo",


    15

          "mnc": "bar",


    16

          "prices": [


    17

            {


    18

              "base_price": "0.05",


    19

              "current_price": "0.05",


    20

              "number_type": "mobile"


    21

            }


    22

          ]


    23

        }


    24

      ],


    25

      "price_unit": "USD",


    26

      "url": "https://pricing.twilio.com/v1/Messaging/Countries/US"


    27

    }

The Resource Twilio returns represents prices to send messages to phone numbers in a given country, organized by Mobile Country Code (MCC) and Mobile Network Code (MNC), and the prices to receive messages on Twilio phone numbers in this country, organized by phone number type.

A Pricing resource has the following properties attached based on the type of Price record it is ([Outbound SMS](/docs/messaging/api/pricing#outbound-sms-price "Outbound SMS"), [Outbound Price](/docs/messaging/api/pricing#outbound-price "Outbound Price"), or [Inbound Price](/docs/messaging/api/pricing#inbound-price "Inbound Price")):

### OutboundSmsPrice

outbound-sms-price page anchor

Positive FeedbackNegative Feedback

Property| Description
---|---
MCC| The Mobile Country Code
MNC| The Mobile Network Code
Carrier| The name of the carrier for this MCC/MNC combination
Prices| List of [OutboundPrice](/docs/messaging/api/pricing#outbound-price "OutboundPrice") records that represent the prices to send a message to this MCC/MNC from different Twilio phone number types

### OutboundPrice

outbound-price page anchor

Positive FeedbackNegative Feedback

Property| Description
---|---
NumberType| The type of Twilio phone number sending a message, either `mobile`, `local`, `shortcode`, or `toll free`
BasePrice| The retail price to send a message
CurrentPrice| The current price (which accounts for any volume or custom price discounts) to send a message

### InboundPrice

inbound-price page anchor

Positive FeedbackNegative Feedback

Property| Description
---|---
NumberType| The type of Twilio phone number receiving a message, either `mobile`, `local`, `shortcode`, or `toll free`
BasePrice| The retail price to receive a message
CurrentPrice| The current price (which accounts for any volume or custom price discounts) to receive a message

* * *

## Read multiple Countries resources

read-multiple-countries-resources page anchor

Positive FeedbackNegative Feedback

`GET https://pricing.twilio.com/v1/Messaging/Countries`

Returns a list of countries where Twilio Messaging Services are available along with the corresponding URL for retrieving the country-specific Messaging prices. This list includes [paging information](/docs/usage/twilios-response "paging information").

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

Read all Countries resourcesLink to code sample: Read all Countries resources

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

    async function listMessagingCountry() {


    11

      const countries = await client.pricing.v1.messaging.countries.list({


    12

        limit: 20,


    13

      });


    14




    15

      countries.forEach((c) => console.log(c.country));


    16

    }


    17




    18

    listMessagingCountry();

### Response

Note about this response

Copy response


    1

    {


    2

      "countries": [],


    3

      "meta": {


    4

        "first_page_url": "https://pricing.twilio.com/v1/Messaging/Countries?PageSize=50&Page=0",


    5

        "key": "countries",


    6

        "next_page_url": null,


    7

        "page": 0,


    8

        "page_size": 50,


    9

        "previous_page_url": null,


    10

        "url": "https://pricing.twilio.com/v1/Messaging/Countries?PageSize=50&Page=0"


    11

      }


    12

    }