# Services resource

*Source: https://www.twilio.com/docs/messaging/api/service-resource*

---

# Services resource

Positive FeedbackNegative Feedback

* * *

(new)

## Public Beta

The Services resource is currently available as a Public Beta product. This means that some features for configuring your Messaging Service via the REST API are not yet implemented, and others may be changed before the product is declared Generally Available. Messaging Service Configuration through the [Twilio Console(link takes you to an external page)](https://www.twilio.com/console "Twilio Console") is Generally Available.

Public Beta products are [not covered by a Twilio SLA(link takes you to an external page)](https://help.twilio.com/hc/en-us/articles/115002413087-Twilio-Beta-product-support "not covered by a Twilio SLA").

The resources for sending Messages with a Messaging Service are Generally Available.

When sending a message with a Messaging Service, you can improve message performance by enabling the [included features](/docs/messaging/services "included features").

Developers can associate [phone numbers](/docs/messaging/api/phonenumber-resource "phone numbers"), [short codes](/docs/messaging/api/services-shortcode-resource "short codes"), and [alpha sender IDs](/docs/messaging/api/alphasender-resource "alpha sender IDs") to an instance of a Messaging Service. The Service handles all inbound and outbound behaviors for the phone numbers and shortcodes.

**Twilio Console**

You can manage your Messaging Services through the [Twilio Console when logged in.(link takes you to an external page)](https://www.twilio.com/console/sms/services "Twilio Console when logged in.")

* * *

## Messaging Services Resource

messaging-services-resource page anchor

Positive FeedbackNegative Feedback

The Services resource represents a set of configurable behavior for sending and receiving Messages.

### Subresources

subresources page anchor

Positive FeedbackNegative Feedback

The Services resource also has PhoneNumbers, ShortCodes, and AlphaSenders subresources for managing the phone numbers, short codes, and alpha sender IDs associated with the Service.

  * [PhoneNumbers](/docs/messaging/api/phonenumber-resource "PhoneNumbers")
  * [ShortCodes](/docs/messaging/api/services-shortcode-resource "ShortCodes")
  * [AlphaSenders](/docs/messaging/api/alphasender-resource "AlphaSenders")


### Resource URI

resource-uri page anchor

Positive FeedbackNegative Feedback

All URLs in this documentation use the following base URL:

Copy code block


    https://messaging.twilio.com/v1

* * *

## Service Properties

service-properties page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescriptionChild properties

sidSID<MG>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique string that we created to identify the Service resource.

Pattern: `^MG[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

accountSidSID<AC>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that created the Service resource.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

friendlyNamestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The string that you assigned to describe the resource.

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

inboundRequestUrlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL we call using `inbound_method` when a message is received by any phone number or short code in the Service. When this property is `null`, receiving inbound messages is disabled. All messages sent to the Twilio phone number or short code will not be logged and received on the Account. If the `use_inbound_webhook_on_number` field is enabled then the webhook url defined on the phone number will override the `inbound_request_url` defined for the Messaging Service.

* * *

inboundMethodenum<http-method>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The HTTP method we use to call `inbound_request_url`. Can be `GET` or `POST`.

Possible values:

`GET``POST`

* * *

fallbackUrlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL that we call using `fallback_method` if an error occurs while retrieving or executing the TwiML from the Inbound Request URL. If the `use_inbound_webhook_on_number` field is enabled then the webhook url defined on the phone number will override the `fallback_url` defined for the Messaging Service.

* * *

fallbackMethodenum<http-method>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The HTTP method we use to call `fallback_url`. Can be: `GET` or `POST`.

Possible values:

`GET``POST`

* * *

statusCallbackstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL we call to [pass status updates](/docs/sms/api/message-resource#message-status-values "pass status updates") about message delivery.

* * *

stickySenderboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether to enable [Sticky Sender](/docs/messaging/services#sticky-sender "Sticky Sender") on the Service instance.

* * *

mmsConverterboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether to enable the [MMS Converter](/docs/messaging/services#mms-converter "MMS Converter") for messages sent through the Service instance.

* * *

smartEncodingboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether to enable [Smart Encoding](/docs/messaging/services#smart-encoding "Smart Encoding") for messages sent through the Service instance.

* * *

scanMessageContentenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Reserved.

Possible values:

`inherit``enable``disable`

* * *

fallbackToLongCodeboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

[OBSOLETE] Former feature used to fallback to long code sender after certain short code message failures.

* * *

areaCodeGeomatchboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether to enable [Area Code Geomatch](/docs/messaging/services#area-code-geomatch "Area Code Geomatch") on the Service Instance.

* * *

synchronousValidationboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Reserved.

* * *

validityPeriodinteger

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

How long, in seconds, messages sent from the Service are valid. Can be an integer from `1` to `36,000`. Default value is `36,000`.

Default: `0`

* * *

urlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The absolute URL of the Service resource.

* * *

linksobject<uri-map>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The absolute URLs of related resources.

* * *

usecasestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A string that describes the scenario in which the Messaging Service will be used. Possible values are `notifications`, `marketing`, `verification`, `discussion`, `poll`, `undeclared`.

* * *

usAppToPersonRegisteredboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether US A2P campaign is registered for this Service.

* * *

useInboundWebhookOnNumberboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A boolean value that indicates either the webhook url configured on the phone number will be used or `inbound_request_url`/`fallback_url` url will be called when a message is received from the phone number. If this field is enabled then the webhook url defined on the phone number will override the `inbound_request_url`/`fallback_url` defined for the Messaging Service.

* * *

## Create a Service

create-a-service page anchor

Positive FeedbackNegative Feedback

`POST https://messaging.twilio.com/v1/Services`

### Request body parameters

request-body-parameters page anchor

Positive FeedbackNegative Feedback

Encoding type:`application/x-www-form-urlencoded`

SchemaExample

Property nameTypeRequiredPIIDescriptionChild properties

friendlyNamestring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A descriptive string that you create to describe the resource. It can be up to 64 characters long.

* * *

inboundRequestUrlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL we call using `inbound_method` when a message is received by any phone number or short code in the Service. When this property is `null`, receiving inbound messages is disabled. All messages sent to the Twilio phone number or short code will not be logged and received on the Account. If the `use_inbound_webhook_on_number` field is enabled then the webhook url defined on the phone number will override the `inbound_request_url` defined for the Messaging Service.

* * *

inboundMethodenum<http-method>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The HTTP method we should use to call `inbound_request_url`. Can be `GET` or `POST` and the default is `POST`.

Possible values:

`GET``POST`

* * *

fallbackUrlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL that we call using `fallback_method` if an error occurs while retrieving or executing the TwiML from the Inbound Request URL. If the `use_inbound_webhook_on_number` field is enabled then the webhook url defined on the phone number will override the `fallback_url` defined for the Messaging Service.

* * *

fallbackMethodenum<http-method>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The HTTP method we should use to call `fallback_url`. Can be: `GET` or `POST`.

Possible values:

`GET``POST`

* * *

statusCallbackstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL we should call to [pass status updates](/docs/sms/api/message-resource#message-status-values "pass status updates") about message delivery.

* * *

stickySenderboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether to enable [Sticky Sender](/docs/messaging/services#sticky-sender "Sticky Sender") on the Service instance.

* * *

mmsConverterboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether to enable the [MMS Converter](/docs/messaging/services#mms-converter "MMS Converter") for messages sent through the Service instance.

* * *

smartEncodingboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether to enable [Smart Encoding](/docs/messaging/services#smart-encoding "Smart Encoding") for messages sent through the Service instance.

* * *

scanMessageContentenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Reserved.

Possible values:

`inherit``enable``disable`

* * *

fallbackToLongCodeboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

[OBSOLETE] Former feature used to fallback to long code sender after certain short code message failures.

* * *

areaCodeGeomatchboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether to enable [Area Code Geomatch](/docs/messaging/services#area-code-geomatch "Area Code Geomatch") on the Service Instance.

* * *

validityPeriodinteger

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

How long, in seconds, messages sent from the Service are valid. Can be an integer from `1` to `36,000`. Default value is `36,000`.

* * *

synchronousValidationboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Reserved.

* * *

usecasestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A string that describes the scenario in which the Messaging Service will be used. Possible values are `notifications`, `marketing`, `verification`, `discussion`, `poll`, `undeclared`.

* * *

useInboundWebhookOnNumberboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A boolean value that indicates either the webhook url configured on the phone number will be used or `inbound_request_url`/`fallback_url` url will be called when a message is received from the phone number. If this field is enabled then the webhook url defined on the phone number will override the `inbound_request_url`/`fallback_url` defined for the Messaging Service.

Copy code block


    {


      "FriendlyName": "My Service!",


      "StickySender": true,


      "MmsConverter": true,


      "SmartEncoding": false,


      "FallbackToLongCode": true,


      "InboundRequestUrl": "https://www.example.com",


      "InboundMethod": "POST",


      "FallbackMethod": "GET",


      "FallbackUrl": "https://www.example.com",


      "StatusCallback": "https://www.example.com",


      "ScanMessageContent": "inherit",


      "AreaCodeGeomatch": true,


      "ValidityPeriod": 600,


      "SynchronousValidation": true,


      "Usecase": "marketing",


      "UseInboundWebhookOnNumber": true


    }

Create a ServiceLink to code sample: Create a Service

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

    async function createService() {


    11

      const service = await client.messaging.v1.services.create({


    12

        friendlyName: "FriendlyName",


    13

      });


    14




    15

      console.log(service.sid);


    16

    }


    17




    18

    createService();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "sid": "MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "date_created": "2015-07-30T20:12:31Z",


    5

      "date_updated": "2015-07-30T20:12:33Z",


    6

      "friendly_name": "FriendlyName",


    7

      "inbound_request_url": "https://www.example.com/",


    8

      "inbound_method": "POST",


    9

      "fallback_url": "https://www.example.com",


    10

      "fallback_method": "GET",


    11

      "status_callback": "https://www.example.com",


    12

      "sticky_sender": true,


    13

      "smart_encoding": false,


    14

      "mms_converter": true,


    15

      "fallback_to_long_code": true,


    16

      "scan_message_content": "inherit",


    17

      "area_code_geomatch": true,


    18

      "validity_period": 600,


    19

      "synchronous_validation": true,


    20

      "usecase": "marketing",


    21

      "us_app_to_person_registered": false,


    22

      "use_inbound_webhook_on_number": true,


    23

      "links": {


    24

        "phone_numbers": "https://messaging.twilio.com/v1/Services/MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/PhoneNumbers",


    25

        "short_codes": "https://messaging.twilio.com/v1/Services/MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ShortCodes",


    26

        "alpha_senders": "https://messaging.twilio.com/v1/Services/MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AlphaSenders",


    27

        "messages": "https://messaging.twilio.com/v1/Services/MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages",


    28

        "us_app_to_person": "https://messaging.twilio.com/v1/Services/MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Compliance/Usa2p",


    29

        "us_app_to_person_usecases": "https://messaging.twilio.com/v1/Services/MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Compliance/Usa2p/Usecases",


    30

        "channel_senders": "https://messaging.twilio.com/v1/Services/MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ChannelSenders",


    31

        "destination_alpha_senders": "https://messaging.twilio.com/v1/Services/MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/DestinationAlphaSenders"


    32

      },


    33

      "url": "https://messaging.twilio.com/v1/Services/MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    34

    }

* * *

## Retrieve a Service

retrieve-a-service page anchor

Positive FeedbackNegative Feedback

`GET https://messaging.twilio.com/v1/Services/{Sid}`

### Path parameters

path-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

sidSID<MG>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the Service resource to fetch.

Pattern: `^MG[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

Fetch a ServiceLink to code sample: Fetch a Service

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

    async function fetchService() {


    11

      const service = await client.messaging.v1


    12

        .services("MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .fetch();


    14




    15

      console.log(service.sid);


    16

    }


    17




    18

    fetchService();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "sid": "MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "date_created": "2015-07-30T20:12:31Z",


    5

      "date_updated": "2015-07-30T20:12:33Z",


    6

      "friendly_name": "My Service!",


    7

      "inbound_request_url": "https://www.example.com/",


    8

      "inbound_method": "POST",


    9

      "fallback_url": null,


    10

      "fallback_method": "POST",


    11

      "status_callback": "https://www.example.com",


    12

      "sticky_sender": true,


    13

      "mms_converter": true,


    14

      "smart_encoding": false,


    15

      "fallback_to_long_code": true,


    16

      "area_code_geomatch": true,


    17

      "validity_period": 600,


    18

      "scan_message_content": "inherit",


    19

      "synchronous_validation": true,


    20

      "usecase": "marketing",


    21

      "us_app_to_person_registered": false,


    22

      "use_inbound_webhook_on_number": true,


    23

      "links": {


    24

        "phone_numbers": "https://messaging.twilio.com/v1/Services/MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/PhoneNumbers",


    25

        "short_codes": "https://messaging.twilio.com/v1/Services/MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ShortCodes",


    26

        "alpha_senders": "https://messaging.twilio.com/v1/Services/MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AlphaSenders",


    27

        "messages": "https://messaging.twilio.com/v1/Services/MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages",


    28

        "us_app_to_person": "https://messaging.twilio.com/v1/Services/MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Compliance/Usa2p",


    29

        "us_app_to_person_usecases": "https://messaging.twilio.com/v1/Services/MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Compliance/Usa2p/Usecases",


    30

        "channel_senders": "https://messaging.twilio.com/v1/Services/MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ChannelSenders",


    31

        "destination_alpha_senders": "https://messaging.twilio.com/v1/Services/MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/DestinationAlphaSenders"


    32

      },


    33

      "url": "https://messaging.twilio.com/v1/Services/MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    34

    }

* * *

## Retrieve a list of Services

retrieve-a-list-of-services page anchor

Positive FeedbackNegative Feedback

`GET https://messaging.twilio.com/v1/Services`

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

List multiple ServicesLink to code sample: List multiple Services

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

    async function listService() {


    11

      const services = await client.messaging.v1.services.list({ limit: 20 });


    12




    13

      services.forEach((s) => console.log(s.sid));


    14

    }


    15




    16

    listService();

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

        "first_page_url": "https://messaging.twilio.com/v1/Services?PageSize=20&Page=0",


    6

        "previous_page_url": null,


    7

        "next_page_url": null,


    8

        "key": "services",


    9

        "url": "https://messaging.twilio.com/v1/Services?PageSize=20&Page=0"


    10

      },


    11

      "services": [


    12

        {


    13

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    14

          "friendly_name": "My Service!",


    15

          "sid": "MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    16

          "date_created": "2015-07-30T20:12:31Z",


    17

          "date_updated": "2015-07-30T20:12:33Z",


    18

          "sticky_sender": true,


    19

          "mms_converter": true,


    20

          "smart_encoding": false,


    21

          "fallback_to_long_code": true,


    22

          "area_code_geomatch": true,


    23

          "validity_period": 600,


    24

          "scan_message_content": "inherit",


    25

          "synchronous_validation": true,


    26

          "inbound_request_url": "https://www.example.com/",


    27

          "inbound_method": "POST",


    28

          "fallback_url": null,


    29

          "fallback_method": "POST",


    30

          "status_callback": "https://www.example.com",


    31

          "usecase": "marketing",


    32

          "us_app_to_person_registered": false,


    33

          "use_inbound_webhook_on_number": false,


    34

          "links": {


    35

            "phone_numbers": "https://messaging.twilio.com/v1/Services/MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/PhoneNumbers",


    36

            "short_codes": "https://messaging.twilio.com/v1/Services/MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ShortCodes",


    37

            "alpha_senders": "https://messaging.twilio.com/v1/Services/MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AlphaSenders",


    38

            "messages": "https://messaging.twilio.com/v1/Services/MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages",


    39

            "us_app_to_person": "https://messaging.twilio.com/v1/Services/MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Compliance/Usa2p",


    40

            "us_app_to_person_usecases": "https://messaging.twilio.com/v1/Services/MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Compliance/Usa2p/Usecases",


    41

            "channel_senders": "https://messaging.twilio.com/v1/Services/MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ChannelSenders",


    42

            "destination_alpha_senders": "https://messaging.twilio.com/v1/Services/MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/DestinationAlphaSenders"


    43

          },


    44

          "url": "https://messaging.twilio.com/v1/Services/MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    45

        }


    46

      ]


    47

    }

* * *

## Update a Service

update-a-service page anchor

Positive FeedbackNegative Feedback

`POST https://messaging.twilio.com/v1/Services/{Sid}`

You may specify one or more of the optional parameters above to update the Service's respective properties. Parameters not specified in your request are not updated.

### Path parameters

path-parameters-1 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

sidSID<MG>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the Service resource to update.

Pattern: `^MG[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

### Request body parameters

request-body-parameters-1 page anchor

Positive FeedbackNegative Feedback

Encoding type:`application/x-www-form-urlencoded`

SchemaExample

Property nameTypeRequiredPIIDescriptionChild properties

friendlyNamestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A descriptive string that you create to describe the resource. It can be up to 64 characters long.

* * *

inboundRequestUrlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL we call using `inbound_method` when a message is received by any phone number or short code in the Service. When this property is `null`, receiving inbound messages is disabled. All messages sent to the Twilio phone number or short code will not be logged and received on the Account. If the `use_inbound_webhook_on_number` field is enabled then the webhook url defined on the phone number will override the `inbound_request_url` defined for the Messaging Service.

* * *

inboundMethodenum<http-method>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The HTTP method we should use to call `inbound_request_url`. Can be `GET` or `POST` and the default is `POST`.

Possible values:

`GET``POST`

* * *

fallbackUrlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL that we call using `fallback_method` if an error occurs while retrieving or executing the TwiML from the Inbound Request URL. If the `use_inbound_webhook_on_number` field is enabled then the webhook url defined on the phone number will override the `fallback_url` defined for the Messaging Service.

* * *

fallbackMethodenum<http-method>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The HTTP method we should use to call `fallback_url`. Can be: `GET` or `POST`.

Possible values:

`GET``POST`

* * *

statusCallbackstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL we should call to [pass status updates](/docs/sms/api/message-resource#message-status-values "pass status updates") about message delivery.

* * *

stickySenderboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether to enable [Sticky Sender](/docs/messaging/services#sticky-sender "Sticky Sender") on the Service instance.

* * *

mmsConverterboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether to enable the [MMS Converter](/docs/messaging/services#mms-converter "MMS Converter") for messages sent through the Service instance.

* * *

smartEncodingboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether to enable [Smart Encoding](/docs/messaging/services#smart-encoding "Smart Encoding") for messages sent through the Service instance.

* * *

scanMessageContentenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Reserved.

Possible values:

`inherit``enable``disable`

* * *

fallbackToLongCodeboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

[OBSOLETE] Former feature used to fallback to long code sender after certain short code message failures.

* * *

areaCodeGeomatchboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether to enable [Area Code Geomatch](/docs/messaging/services#area-code-geomatch "Area Code Geomatch") on the Service Instance.

* * *

validityPeriodinteger

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

How long, in seconds, messages sent from the Service are valid. Can be an integer from `1` to `36,000`. Default value is `36,000`.

* * *

synchronousValidationboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Reserved.

* * *

usecasestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A string that describes the scenario in which the Messaging Service will be used. Possible values are `notifications`, `marketing`, `verification`, `discussion`, `poll`, `undeclared`.

* * *

useInboundWebhookOnNumberboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A boolean value that indicates either the webhook url configured on the phone number will be used or `inbound_request_url`/`fallback_url` url will be called when a message is received from the phone number. If this field is enabled then the webhook url defined on the phone number will override the `inbound_request_url`/`fallback_url` defined for the Messaging Service.

Copy code block


    {


      "StickySender": false


    }

Update a ServiceLink to code sample: Update a Service

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

    async function updateService() {


    11

      const service = await client.messaging.v1


    12

        .services("MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .update({ friendlyName: "FriendlyName" });


    14




    15

      console.log(service.sid);


    16

    }


    17




    18

    updateService();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "friendly_name": "FriendlyName",


    4

      "sid": "MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

      "date_created": "2015-07-30T20:12:31Z",


    6

      "date_updated": "2015-07-30T20:12:33Z",


    7

      "sticky_sender": false,


    8

      "mms_converter": true,


    9

      "smart_encoding": false,


    10

      "fallback_to_long_code": true,


    11

      "scan_message_content": "inherit",


    12

      "synchronous_validation": true,


    13

      "area_code_geomatch": true,


    14

      "validity_period": 600,


    15

      "inbound_request_url": "https://www.example.com",


    16

      "inbound_method": "POST",


    17

      "fallback_url": null,


    18

      "fallback_method": "POST",


    19

      "status_callback": "https://www.example.com",


    20

      "usecase": "marketing",


    21

      "us_app_to_person_registered": false,


    22

      "use_inbound_webhook_on_number": true,


    23

      "links": {


    24

        "phone_numbers": "https://messaging.twilio.com/v1/Services/MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/PhoneNumbers",


    25

        "short_codes": "https://messaging.twilio.com/v1/Services/MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ShortCodes",


    26

        "alpha_senders": "https://messaging.twilio.com/v1/Services/MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AlphaSenders",


    27

        "messages": "https://messaging.twilio.com/v1/Services/MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages",


    28

        "us_app_to_person": "https://messaging.twilio.com/v1/Services/MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Compliance/Usa2p",


    29

        "us_app_to_person_usecases": "https://messaging.twilio.com/v1/Services/MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Compliance/Usa2p/Usecases",


    30

        "channel_senders": "https://messaging.twilio.com/v1/Services/MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ChannelSenders",


    31

        "destination_alpha_senders": "https://messaging.twilio.com/v1/Services/MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/DestinationAlphaSenders"


    32

      },


    33

      "url": "https://messaging.twilio.com/v1/Services/MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    34

    }

* * *

## Delete a Service

delete-a-service page anchor

Positive FeedbackNegative Feedback

`DELETE https://messaging.twilio.com/v1/Services/{Sid}`

When a Service is deleted, all phone numbers and short codes in the Service are returned to your Account.

(warning)

## Warning

If you are using a Messaging Service for A2P 10DLC, you should **not** delete the Messaging Service. Doing so deletes the A2P 10DLC Campaign, which immediately halts all US A2P 10DLC messaging. A new Campaign and Messaging Service must be created and re-registered. This process can take several days.

### Path parameters

path-parameters-2 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

sidSID<MG>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the Service resource to delete.

Pattern: `^MG[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

Delete a ServiceLink to code sample: Delete a Service

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

    async function deleteService() {


    11

      await client.messaging.v1


    12

        .services("MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .remove();


    14

    }


    15




    16

    deleteService();