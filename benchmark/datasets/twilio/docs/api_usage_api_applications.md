# REST API: Applications

*Source: https://www.twilio.com/docs/usage/api/applications*

---

# REST API: Applications

Positive FeedbackNegative Feedback

* * *

An Application Resource (also referred to as a "TwiML Application" or "TwiML App") represents a collection of endpoints that return TwiML instructions to Twilio. TwiML Applications are most commonly used for the [Voice SDKs](/docs/voice/sdks#twiml-apps "Voice SDKs") to handle outbound calls, but can also be used to configure multiple phone numbers with the same set of TwiML endpoints. TwiML Applications can be configured via the Applications Resource or via the Console on the [TwiML Apps(link takes you to an external page)](https://console.twilio.com/?frameUrl=/console/voice/twiml/apps "TwiML Apps") page.

The Applications list resource represents the set of an account's Twilio applications. You can `POST` to the list resource to create a new application. Note that accounts can contain at most 1000 applications.

Applications are useful for encapsulating configuration information that you need to distribute across multiple phone numbers. You can assign an ApplicationSid to an IncomingPhoneNumber to tell Twilio to use the application's URLs instead of the ones set directly on the IncomingPhoneNumber. So if you create an application with its VoiceUrl set to [http://myapp.com/answer(link takes you to an external page)](http://myapp.com/answer "http://myapp.com/answer"), you can assign that application to all of your phone numbers and Twilio will make a request to that URL whenever a call comes in.

* * *

## Application Properties

application-properties page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescriptionChild properties

accountSidSID<AC>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that created the Application resource.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

apiVersionstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The API version used to start a new TwiML session.

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

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The string that you assigned to describe the resource.

* * *

messageStatusCallbackstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL we call using a POST method to send message status information to your application.

* * *

sidSID<AP>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique string that that we created to identify the Application resource.

Pattern: `^AP[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

smsFallbackMethodenum<http-method>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The HTTP method we use to call `sms_fallback_url`. Can be: `GET` or `POST`.

Possible values:

`GET``POST`

* * *

smsFallbackUrlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL that we call when an error occurs while retrieving or executing the TwiML from `sms_url`.

* * *

smsMethodenum<http-method>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The HTTP method we use to call `sms_url`. Can be: `GET` or `POST`.

Possible values:

`GET``POST`

* * *

smsStatusCallbackstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL we call using a POST method to send status information to your application about SMS messages that refer to the application.

* * *

smsUrlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL we call when the phone number receives an incoming SMS message.

* * *

statusCallbackstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL we call using the `status_callback_method` to send status information to your application.

* * *

statusCallbackMethodenum<http-method>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The HTTP method we use to call `status_callback`. Can be: `GET` or `POST`.

Possible values:

`GET``POST`

* * *

uristring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URI of the resource, relative to `https://api.twilio.com`.

* * *

voiceCallerIdLookupboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether we look up the caller's caller-ID name from the CNAM database (additional charges apply). Can be: `true` or `false`.

* * *

voiceFallbackMethodenum<http-method>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The HTTP method we use to call `voice_fallback_url`. Can be: `GET` or `POST`.

Possible values:

`GET``POST`

* * *

voiceFallbackUrlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL that we call when an error occurs retrieving or executing the TwiML requested by `url`.

* * *

voiceMethodenum<http-method>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The HTTP method we use to call `voice_url`. Can be: `GET` or `POST`.

Possible values:

`GET``POST`

* * *

voiceUrlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL we call when the phone number assigned to this application receives a call.

* * *

publicApplicationConnectEnabledboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether to allow other Twilio accounts to dial this applicaton using Dial verb. Can be: `true` or `false`.

* * *

## Create an Application resource

create-an-application-resource page anchor

Positive FeedbackNegative Feedback

`POST https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Applications.json`

Creates a new application within your account.

If successful, Twilio responds with a representation of the new application.

### Path parameters

path-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

accountSidSID<AC>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that will create the resource.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

### Request body parameters

request-body-parameters page anchor

Positive FeedbackNegative Feedback

Encoding type:`application/x-www-form-urlencoded`

SchemaExample

Property nameTypeRequiredPIIDescriptionChild properties

apiVersionstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The API version to use to start a new TwiML session. Can be: `2010-04-01` or `2008-08-01`. The default value is the account's default API version.

* * *

voiceUrlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL we should call when the phone number assigned to this application receives a call.

* * *

voiceMethodenum<http-method>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The HTTP method we should use to call `voice_url`. Can be: `GET` or `POST`.

Possible values:

`GET``POST`

* * *

voiceFallbackUrlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL that we should call when an error occurs retrieving or executing the TwiML requested by `url`.

* * *

voiceFallbackMethodenum<http-method>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The HTTP method we should use to call `voice_fallback_url`. Can be: `GET` or `POST`.

Possible values:

`GET``POST`

* * *

statusCallbackstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL we should call using the `status_callback_method` to send status information to your application.

* * *

statusCallbackMethodenum<http-method>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The HTTP method we should use to call `status_callback`. Can be: `GET` or `POST`.

Possible values:

`GET``POST`

* * *

voiceCallerIdLookupboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether we should look up the caller's caller-ID name from the CNAM database (additional charges apply). Can be: `true` or `false`.

* * *

smsUrlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL we should call when the phone number receives an incoming SMS message.

* * *

smsMethodenum<http-method>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The HTTP method we should use to call `sms_url`. Can be: `GET` or `POST`.

Possible values:

`GET``POST`

* * *

smsFallbackUrlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL that we should call when an error occurs while retrieving or executing the TwiML from `sms_url`.

* * *

smsFallbackMethodenum<http-method>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The HTTP method we should use to call `sms_fallback_url`. Can be: `GET` or `POST`.

Possible values:

`GET``POST`

* * *

smsStatusCallbackstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL we should call using a POST method to send status information about SMS messages sent by the application.

* * *

messageStatusCallbackstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL we should call using a POST method to send message status information to your application.

* * *

friendlyNamestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A descriptive string that you create to describe the new application. It can be up to 64 characters long.

* * *

publicApplicationConnectEnabledboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether to allow other Twilio accounts to dial this applicaton using Dial verb. Can be: `true` or `false`.

Copy code block


    {


      "FriendlyName": "friendly_name",


      "MessageStatusCallback": "https://example.com",


      "SmsFallbackMethod": "GET",


      "SmsFallbackUrl": "https://example.com",


      "SmsMethod": "GET",


      "SmsStatusCallback": "https://example.com",


      "SmsUrl": "https://example.com",


      "StatusCallback": "https://example.com",


      "StatusCallbackMethod": "GET",


      "VoiceCallerIdLookup": true,


      "VoiceFallbackMethod": "GET",


      "VoiceFallbackUrl": "https://example.com",


      "VoiceMethod": "GET",


      "VoiceUrl": "https://example.com",


      "PublicApplicationConnectEnabled": true


    }

Create a New Application Within Your AccountLink to code sample: Create a New Application Within Your Account

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

    async function createApplication() {


    11

      const application = await client.applications.create({


    12

        friendlyName: "Phone Me",


    13

        voiceMethod: "GET",


    14

        voiceUrl: "http://demo.twilio.com/docs/voice.xml",


    15

      });


    16




    17

      console.log(application.accountSid);


    18

    }


    19




    20

    createApplication();

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

      "date_created": "Mon, 22 Aug 2011 20:59:45 +0000",


    5

      "date_updated": "Tue, 18 Aug 2015 16:48:57 +0000",


    6

      "friendly_name": "Phone Me",


    7

      "message_status_callback": "http://www.example.com/sms-status-callback",


    8

      "sid": "APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    9

      "sms_fallback_method": "GET",


    10

      "sms_fallback_url": "http://www.example.com/sms-fallback",


    11

      "sms_method": "GET",


    12

      "sms_status_callback": "http://www.example.com/sms-status-callback",


    13

      "sms_url": "http://example.com",


    14

      "status_callback": "http://example.com",


    15

      "status_callback_method": "GET",


    16

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Applications/APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",


    17

      "voice_caller_id_lookup": false,


    18

      "voice_fallback_method": "GET",


    19

      "voice_fallback_url": "http://www.example.com/voice-callback",


    20

      "voice_method": "GET",


    21

      "voice_url": "http://demo.twilio.com/docs/voice.xml",


    22

      "public_application_connect_enabled": true


    23

    }

* * *

## Fetch an Application resource

fetch-an-application-resource page anchor

Positive FeedbackNegative Feedback

`GET https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Applications/{Sid}.json`

### Path parameters

path-parameters-1 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

accountSidSID<AC>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that created the Application resource to fetch.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

sidSID<AP>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The Twilio-provided string that uniquely identifies the Application resource to fetch.

Pattern: `^AP[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

Fetch an ApplicationLink to code sample: Fetch an Application

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

    async function fetchApplication() {


    11

      const application = await client


    12

        .applications("APXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")


    13

        .fetch();


    14




    15

      console.log(application.accountSid);


    16

    }


    17




    18

    fetchApplication();

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

      "date_created": "Mon, 22 Aug 2011 20:59:45 +0000",


    5

      "date_updated": "Tue, 18 Aug 2015 16:48:57 +0000",


    6

      "friendly_name": "Application Friendly Name",


    7

      "message_status_callback": "http://www.example.com/sms-status-callback",


    8

      "sid": "APXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    9

      "sms_fallback_method": "GET",


    10

      "sms_fallback_url": "http://www.example.com/sms-fallback",


    11

      "sms_method": "GET",


    12

      "sms_status_callback": "http://www.example.com/sms-status-callback",


    13

      "sms_url": "http://example.com",


    14

      "status_callback": "http://example.com",


    15

      "status_callback_method": "GET",


    16

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Applications/APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",


    17

      "voice_caller_id_lookup": false,


    18

      "voice_fallback_method": "GET",


    19

      "voice_fallback_url": "http://www.example.com/voice-callback",


    20

      "voice_method": "GET",


    21

      "voice_url": "http://example.com",


    22

      "public_application_connect_enabled": false


    23

    }

* * *

## Read multiple Application resources

read-multiple-application-resources page anchor

Positive FeedbackNegative Feedback

`GET https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Applications.json`

Returns a list of Application resource representations, each representing an application within your account. The list includes [paging information](/docs/usage/twilios-response#pagination "paging information").

### Path parameters

path-parameters-2 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

accountSidSID<AC>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that created the Application resources to read.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

### Query parameters

query-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

friendlyNamestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The string that identifies the Application resources to read.

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

List All Application Resource RepresentationsLink to code sample: List All Application Resource Representations

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

    async function listApplication() {


    11

      const applications = await client.applications.list({ limit: 20 });


    12




    13

      applications.forEach((a) => console.log(a.accountSid));


    14

    }


    15




    16

    listApplication();

### Response

Note about this response

Copy response


    1

    {


    2

      "applications": [


    3

        {


    4

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

          "api_version": "2010-04-01",


    6

          "date_created": "Fri, 21 Aug 2015 00:07:25 +0000",


    7

          "date_updated": "Fri, 21 Aug 2015 00:07:25 +0000",


    8

          "friendly_name": "d8821fb7-4d01-48b2-bdc5-34e46252b90b",


    9

          "message_status_callback": null,


    10

          "sid": "APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    11

          "sms_fallback_method": "POST",


    12

          "sms_fallback_url": null,


    13

          "sms_method": "POST",


    14

          "sms_status_callback": null,


    15

          "sms_url": null,


    16

          "status_callback": null,


    17

          "status_callback_method": "POST",


    18

          "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Applications/APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",


    19

          "voice_caller_id_lookup": false,


    20

          "voice_fallback_method": "POST",


    21

          "voice_fallback_url": null,


    22

          "voice_method": "POST",


    23

          "voice_url": null,


    24

          "public_application_connect_enabled": false


    25

        }


    26

      ],


    27

      "end": 0,


    28

      "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Applications.json?FriendlyName=friendly_name&PageSize=1&Page=0",


    29

      "next_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Applications.json?FriendlyName=friendly_name&PageSize=1&Page=1&PageToken=PAAPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    30

      "previous_page_uri": null,


    31

      "page_size": 1,


    32

      "page": 0,


    33

      "start": 0,


    34

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Applications.json?FriendlyName=friendly_name&PageSize=1&Page=0"


    35

    }

Return the Application named 'MyApp'Link to code sample: Return the Application named 'MyApp'

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

    async function listApplication() {


    11

      const applications = await client.applications.list({


    12

        friendlyName: "MyApp",


    13

        limit: 20,


    14

      });


    15




    16

      applications.forEach((a) => console.log(a.accountSid));


    17

    }


    18




    19

    listApplication();

### Response

Note about this response

Copy response


    1

    {


    2

      "applications": [


    3

        {


    4

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

          "api_version": "2010-04-01",


    6

          "date_created": "Fri, 21 Aug 2015 00:07:25 +0000",


    7

          "date_updated": "Fri, 21 Aug 2015 00:07:25 +0000",


    8

          "friendly_name": "d8821fb7-4d01-48b2-bdc5-34e46252b90b",


    9

          "message_status_callback": null,


    10

          "sid": "APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    11

          "sms_fallback_method": "POST",


    12

          "sms_fallback_url": null,


    13

          "sms_method": "POST",


    14

          "sms_status_callback": null,


    15

          "sms_url": null,


    16

          "status_callback": null,


    17

          "status_callback_method": "POST",


    18

          "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Applications/APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",


    19

          "voice_caller_id_lookup": false,


    20

          "voice_fallback_method": "POST",


    21

          "voice_fallback_url": null,


    22

          "voice_method": "POST",


    23

          "voice_url": null,


    24

          "public_application_connect_enabled": false


    25

        }


    26

      ],


    27

      "end": 0,


    28

      "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Applications.json?FriendlyName=friendly_name&PageSize=1&Page=0",


    29

      "next_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Applications.json?FriendlyName=friendly_name&PageSize=1&Page=1&PageToken=PAAPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    30

      "previous_page_uri": null,


    31

      "page_size": 1,


    32

      "page": 0,


    33

      "start": 0,


    34

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Applications.json?FriendlyName=friendly_name&PageSize=1&Page=0"


    35

    }

* * *

## Update an Application resource

update-an-application-resource page anchor

Positive FeedbackNegative Feedback

`POST https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Applications/{Sid}.json`

Tries to update the application's properties, and returns the updated resource representation if successful. The returned response is identical to that returned above when making a `GET` request.

### Path parameters

path-parameters-3 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

accountSidSID<AC>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that created the Application resources to update.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

sidSID<AP>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The Twilio-provided string that uniquely identifies the Application resource to update.

Pattern: `^AP[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

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

apiVersionstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The API version to use to start a new TwiML session. Can be: `2010-04-01` or `2008-08-01`. The default value is your account's default API version.

* * *

voiceUrlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL we should call when the phone number assigned to this application receives a call.

* * *

voiceMethodenum<http-method>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The HTTP method we should use to call `voice_url`. Can be: `GET` or `POST`.

Possible values:

`GET``POST`

* * *

voiceFallbackUrlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL that we should call when an error occurs retrieving or executing the TwiML requested by `url`.

* * *

voiceFallbackMethodenum<http-method>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The HTTP method we should use to call `voice_fallback_url`. Can be: `GET` or `POST`.

Possible values:

`GET``POST`

* * *

statusCallbackstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL we should call using the `status_callback_method` to send status information to your application.

* * *

statusCallbackMethodenum<http-method>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The HTTP method we should use to call `status_callback`. Can be: `GET` or `POST`.

Possible values:

`GET``POST`

* * *

voiceCallerIdLookupboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether we should look up the caller's caller-ID name from the CNAM database (additional charges apply). Can be: `true` or `false`.

* * *

smsUrlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL we should call when the phone number receives an incoming SMS message.

* * *

smsMethodenum<http-method>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The HTTP method we should use to call `sms_url`. Can be: `GET` or `POST`.

Possible values:

`GET``POST`

* * *

smsFallbackUrlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL that we should call when an error occurs while retrieving or executing the TwiML from `sms_url`.

* * *

smsFallbackMethodenum<http-method>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The HTTP method we should use to call `sms_fallback_url`. Can be: `GET` or `POST`.

Possible values:

`GET``POST`

* * *

smsStatusCallbackstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Same as message_status_callback: The URL we should call using a POST method to send status information about SMS messages sent by the application. Deprecated, included for backwards compatibility.

* * *

messageStatusCallbackstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL we should call using a POST method to send message status information to your application.

* * *

publicApplicationConnectEnabledboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether to allow other Twilio accounts to dial this applicaton using Dial verb. Can be: `true` or `false`.

Copy code block


    {


      "FriendlyName": "friendly_name",


      "MessageStatusCallback": "https://example.com",


      "SmsFallbackMethod": "GET",


      "SmsFallbackUrl": "https://example.com",


      "SmsMethod": "GET",


      "SmsStatusCallback": "https://example.com",


      "SmsUrl": "https://example.com",


      "StatusCallback": "https://example.com",


      "StatusCallbackMethod": "GET",


      "VoiceCallerIdLookup": true,


      "VoiceFallbackMethod": "GET",


      "VoiceFallbackUrl": "https://example.com",


      "VoiceMethod": "GET",


      "VoiceUrl": "https://example.com",


      "PublicApplicationConnectEnabled": true


    }

Set the VoiceUrl and SmsUrl on an Application to 'http://myapp.com/awesome'Link to code sample: Set the VoiceUrl and SmsUrl on an Application to 'http://myapp.com/awesome'

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

    async function updateApplication() {


    11

      const application = await client


    12

        .applications("AP2a0747eba6abf96b7e3c3ff0b4530f6e")


    13

        .update({


    14

          smsUrl: "http://demo.twilio.com/docs/sms.xml",


    15

          voiceUrl: "http://demo.twilio.com/docs/voice.xml",


    16

        });


    17




    18

      console.log(application.accountSid);


    19

    }


    20




    21

    updateApplication();

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

      "date_created": "Mon, 22 Aug 2011 20:59:45 +0000",


    5

      "date_updated": "Tue, 18 Aug 2015 16:48:57 +0000",


    6

      "friendly_name": "Application Friendly Name",


    7

      "message_status_callback": "http://www.example.com/sms-status-callback",


    8

      "sid": "AP2a0747eba6abf96b7e3c3ff0b4530f6e",


    9

      "sms_fallback_method": "GET",


    10

      "sms_fallback_url": "http://www.example.com/sms-fallback",


    11

      "sms_method": "GET",


    12

      "sms_status_callback": "http://www.example.com/sms-status-callback",


    13

      "sms_url": "http://demo.twilio.com/docs/sms.xml",


    14

      "status_callback": "http://example.com",


    15

      "status_callback_method": "GET",


    16

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Applications/APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",


    17

      "voice_caller_id_lookup": false,


    18

      "voice_fallback_method": "GET",


    19

      "voice_fallback_url": "http://www.example.com/voice-callback",


    20

      "voice_method": "GET",


    21

      "voice_url": "http://demo.twilio.com/docs/voice.xml",


    22

      "public_application_connect_enabled": true


    23

    }

* * *

## Delete an Application resource

delete-an-application-resource page anchor

Positive FeedbackNegative Feedback

`DELETE https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Applications/{Sid}.json`

Delete this application. If this application's sid is assigned to any IncomingPhoneNumber resources as a VoiceApplicationSid or SmsApplicationSid it will be removed.

If successful, Twilio will return an HTTP 204 response with no body.

### Path parameters

path-parameters-4 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

accountSidSID<AC>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that created the Application resources to delete.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

sidSID<AP>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The Twilio-provided string that uniquely identifies the Application resource to delete.

Pattern: `^AP[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

Delete an ApplicationLink to code sample: Delete an Application

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

    async function deleteApplication() {


    11

      await client.applications("APXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").remove();


    12

    }


    13




    14

    deleteApplication();