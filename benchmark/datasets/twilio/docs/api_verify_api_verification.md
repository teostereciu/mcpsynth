# Verifications

*Source: https://www.twilio.com/docs/verify/api/verification*

---

# Verifications

Positive FeedbackNegative Feedback

* * *

The Twilio Verify REST API verifies that a user has a claimed device, phone number, or email address in their possession. You can start a new Verification for a user and check that the Verification was successful.

* * *

## Prerequisites

prerequisites page anchor

Positive FeedbackNegative Feedback

Before you begin, complete the following:

  1. [Create a Verification Service](/docs/verify/api/service "Create a Verification Service").
  2. If you're using a Twilio Trial Account, you need to [verify any non-Twilio phone numbers](/docs/usage/tutorials/how-to-use-your-free-trial-account "verify any non-Twilio phone numbers") you want to send SMS, Voice, or WhatsApp OTP messages.


* * *

## Verification Response Properties

verification-response-properties page anchor

Positive FeedbackNegative Feedback

These fields are returned in the output JSON response. The type `SID<VE>` is a unique ID starting with the letters VE.

Property nameTypeRequiredPIIDescriptionChild properties

sidSID<VE>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique string that we created to identify the Verification resource.

Pattern: `^VE[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

serviceSidSID<VA>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Service](/docs/verify/api/service "Service") the resource is associated with.

Pattern: `^VA[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

accountSidSID<AC>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that created the Verification resource.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

tostring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The phone number or [email](/docs/verify/email "email") being verified. Phone numbers must be in [E.164 format](/docs/glossary/what-e164 "E.164 format").

* * *

channelenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The verification method used. One of: [`email`](/docs/verify/email), `sms`, `whatsapp`, `call`, `sna`, or `rcs`.

Possible values:

`sms``call``email``whatsapp``sna`

* * *

statusstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The status of the verification. Can be: `pending`, `approved`, `canceled`, `max_attempts_reached`, `deleted`, `failed` or `expired`.

* * *

validboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Use "status" instead. Legacy property indicating whether the verification was successful.

* * *

lookup

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Information about the phone number being verified.

* * *

amountstring

Optional

[PII MTL: 1 day](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The amount of the associated PSD2 compliant transaction. Requires the PSD2 Service flag enabled.

* * *

payeestring

Optional

[PII MTL: 1 day](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The payee of the associated PSD2 compliant transaction. Requires the PSD2 Service flag enabled.

* * *

sendCodeAttemptsarray

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

An array of verification attempt objects containing the channel attempted and the channel-specific transaction SID.

* * *

dateCreatedstring<date-time>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date and time in GMT when the resource was created specified in [RFC 2822(link takes you to an external page)](https://www.ietf.org/rfc/rfc2822.txt "RFC 2822") format.

* * *

dateUpdatedstring<date-time>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date and time in GMT when the resource was last updated specified in [RFC 2822(link takes you to an external page)](https://www.ietf.org/rfc/rfc2822.txt "RFC 2822") format.

* * *

sna

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The set of fields used for a silent network auth (`sna`) verification. Contains a single field with the URL to be invoked to verify the phone number.

* * *

urlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The absolute URL of the Verification resource.

* * *

## Start New Verification

start-new-verification page anchor

Positive FeedbackNegative Feedback

`POST https://verify.twilio.com/v2/Services/{ServiceSid}/Verifications`

To verify a user's phone number or email, start by requesting to send a verification code to their device, or use the Silent Network Auth channel to perform the verification without sending a code.

These are the available input parameters for starting a verification. The type `SID<VE>` is a unique ID starting with the letters VE.

Phone numbers must be in [E.164 format](/docs/glossary/what-e164 "E.164 format"). Learn more about how to turn [phone number input into E.164 format(link takes you to an external page)](https://www.twilio.com/blog/international-phone-number-input-html-javascript "phone number input into E.164 format").

### Path parameters

path-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

serviceSidSID<VA>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the verification [Service](/docs/verify/api/service "Service") to create the resource under.

Pattern: `^VA[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

### Request body parameters

request-body-parameters page anchor

Positive FeedbackNegative Feedback

Encoding type:`application/x-www-form-urlencoded`

SchemaExample

Property nameTypeRequiredPIIDescriptionChild properties

tostring

required

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The phone number or [email](/docs/verify/email "email") to verify. Phone numbers must be in [E.164 format](/docs/glossary/what-e164 "E.164 format").

* * *

channelstring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The verification method to use. One of: [`email`](/docs/verify/email), `sms`, `whatsapp`, `call`, `sna` or `auto`.

* * *

customFriendlyNamestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A custom user defined friendly name that overwrites the existing one in the verification message

* * *

customMessagestring

deprecated

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The text of a custom message to use for the verification [DEPRECATED].

* * *

sendDigitsstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The digits to send after a phone call is answered, for example, to dial an extension. For more information, see the Programmable Voice documentation of [sendDigits](/docs/voice/twiml/number#attributes-sendDigits "sendDigits").

* * *

localestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Locale will automatically resolve based on phone number country code for SMS, WhatsApp, and call channel verifications. It will fallback to English or the template’s default translation if the selected translation is not available. This parameter will override the automatic locale resolution. [See supported languages and more information here](/docs/verify/supported-languages "See supported languages and more information here").

* * *

customCodestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A pre-generated code to use for verification. The code can be between 4 and 10 characters, inclusive.

* * *

amountstring

Optional

[PII MTL: 1 day](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The amount of the associated PSD2 compliant transaction. Requires the PSD2 Service flag enabled.

* * *

payeestring

Optional

[PII MTL: 1 day](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The payee of the associated PSD2 compliant transaction. Requires the PSD2 Service flag enabled.

* * *

rateLimits

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The custom key-value pairs of Programmable Rate Limits. Keys correspond to `unique_name` fields defined when [creating your Rate Limit](/docs/verify/api/service-rate-limits "creating your Rate Limit"). Associated value pairs represent values in the request that you are rate limiting on. You may include multiple Rate Limit values in each request.

* * *

channelConfiguration

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

[`email`](/docs/verify/email) channel configuration in json format. The fields 'from' and 'from_name' are optional but if included the 'from' field must have a valid email address.

* * *

appHashstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Your [App Hash(link takes you to an external page)](https://developers.google.com/identity/sms-retriever/verify#computing_your_apps_hash_string "App Hash") to be appended at the end of your verification SMS body. Applies only to SMS. Example SMS body: `<#> Your AppName verification code is: 1234 He42w354ol9`.

* * *

templateSidSID<HJ>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The message [template](/docs/verify/api/templates "template"). If provided, will override the default template for the Service. SMS and Voice channels only.

Pattern: `^HJ[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

templateCustomSubstitutionsstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A stringified JSON object in which the keys are the template's special variables and the values are the variables substitutions.

* * *

deviceIpstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Strongly encouraged if using the auto channel. The IP address of the client's device. If provided, it has to be a valid IPv4 or IPv6 address.

* * *

enableSnaClientTokenboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

An optional Boolean value to indicate the requirement of sna client token in the SNA URL invocation response for added security. This token must match in the Verification Check request to confirm phone number verification.

* * *

riskCheckenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Risk_check overrides Fraud Prevention measures like Fraud Guard, Geo Permissions etc per verification attempt basis, allowing Verify to block traffic considered fraudulent if enabled or bypass active protections if disabled. Can be: `enable`(default) or `disable`. For SMS channel only.

Possible values:

`enable``disable`

* * *

tagsstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A string containing a JSON map of key value pairs of tags to be recorded as metadata for the message. The object may contain up to 10 tags. Keys and values can each be up to 128 characters in length.

Select from available examples

Copy code block


    {


      "To": "+15017122661",


      "Channel": "sms",


      "CustomCode": "custom_code",


      "CustomFriendlyName": "custom_friendly_name",


      "CustomMessage": "custom_message",


      "SendDigits": "ww1",


      "Locale": "en",


      "Amount": "€39.99",


      "Payee": "Acme Inc.",


      "AppHash": "AAAAAAAAAAA",


      "TemplateSid": "HJaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


      "TemplateCustomSubstitutions": "{\"AppName\": \"MyApp\", \"Contact\":\"12345689\"}",


      "RiskCheck": "enable",


      "Tags": "{\"tenant_id\": \"12345\"}"


    }

Start a Verification with SMSLink to code sample: Start a Verification with SMS

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

    async function createVerification() {


    11

      const verification = await client.verify.v2


    12

        .services("VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .verifications.create({


    14

          channel: "sms",


    15

          to: "+15017122661",


    16

        });


    17




    18

      console.log(verification.sid);


    19

    }


    20




    21

    createVerification();

### Response

Note about this response

Copy response


    1

    {


    2

      "sid": "VEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "service_sid": "VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

      "to": "+15017122661",


    6

      "channel": "sms",


    7

      "status": "pending",


    8

      "valid": false,


    9

      "date_created": "2015-07-30T20:00:00Z",


    10

      "date_updated": "2015-07-30T20:00:00Z",


    11

      "lookup": {},


    12

      "amount": null,


    13

      "payee": null,


    14

      "send_code_attempts": [


    15

        {


    16

          "time": "2015-07-30T20:00:00Z",


    17

          "channel": "SMS",


    18

          "attempt_sid": "VLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    19

        }


    20

      ],


    21

      "sna": null,


    22

      "url": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Verifications/VEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    23

    }

Start a Verification with WhatsAppLink to code sample: Start a Verification with WhatsApp

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

    async function createVerification() {


    11

      const verification = await client.verify.v2


    12

        .services("VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .verifications.create({


    14

          channel: "whatsapp",


    15

          to: "+15017122661",


    16

        });


    17




    18

      console.log(verification.sid);


    19

    }


    20




    21

    createVerification();

### Response

Note about this response

Copy response


    1

    {


    2

      "sid": "VEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "service_sid": "VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

      "to": "+15017122661",


    6

      "channel": "whatsapp",


    7

      "status": "pending",


    8

      "valid": false,


    9

      "date_created": "2015-07-30T20:00:00Z",


    10

      "date_updated": "2015-07-30T20:00:00Z",


    11

      "lookup": {},


    12

      "amount": null,


    13

      "payee": null,


    14

      "send_code_attempts": [


    15

        {


    16

          "time": "2015-07-30T20:00:00Z",


    17

          "channel": "whatsapp",


    18

          "attempt_sid": "VLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    19

        }


    20

      ],


    21

      "sna": null,


    22

      "url": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Verifications/VEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    23

    }

Start a Verification with VoiceLink to code sample: Start a Verification with Voice

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

    async function createVerification() {


    11

      const verification = await client.verify.v2


    12

        .services("VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .verifications.create({


    14

          channel: "call",


    15

          to: "+15017122661",


    16

        });


    17




    18

      console.log(verification.sid);


    19

    }


    20




    21

    createVerification();

### Response

Note about this response

Copy response


    1

    {


    2

      "sid": "VEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "service_sid": "VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

      "to": "+15017122661",


    6

      "channel": "call",


    7

      "status": "pending",


    8

      "valid": false,


    9

      "date_created": "2015-07-30T20:00:00Z",


    10

      "date_updated": "2015-07-30T20:00:00Z",


    11

      "lookup": {},


    12

      "amount": null,


    13

      "payee": null,


    14

      "send_code_attempts": [


    15

        {


    16

          "time": "2015-07-30T20:00:00Z",


    17

          "channel": "SMS",


    18

          "attempt_sid": "VLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    19

        }


    20

      ],


    21

      "sna": null,


    22

      "url": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Verifications/VEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    23

    }

Start a Verification with Voice to an extensionLink to code sample: Start a Verification with Voice to an extension

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

    async function createVerification() {


    11

      const verification = await client.verify.v2


    12

        .services("VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .verifications.create({


    14

          channel: "call",


    15

          sendDigits: "350",


    16

          to: "+15017122661",


    17

        });


    18




    19

      console.log(verification.sid);


    20

    }


    21




    22

    createVerification();

### Response

Note about this response

Copy response


    1

    {


    2

      "sid": "VEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "service_sid": "VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

      "to": "+15017122661",


    6

      "channel": "call",


    7

      "status": "pending",


    8

      "valid": false,


    9

      "date_created": "2015-07-30T20:00:00Z",


    10

      "date_updated": "2015-07-30T20:00:00Z",


    11

      "lookup": {},


    12

      "amount": null,


    13

      "payee": null,


    14

      "send_code_attempts": [


    15

        {


    16

          "time": "2015-07-30T20:00:00Z",


    17

          "channel": "SMS",


    18

          "attempt_sid": "VLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    19

        }


    20

      ],


    21

      "sna": null,


    22

      "url": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Verifications/VEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    23

    }

* * *

## Start a new Verification with Silent Network Auth

start-a-new-verification-with-silent-network-auth page anchor

Positive FeedbackNegative Feedback

(information)

## Info

Verify Silent Network Auth (SNA) is currently in the beta release stage, [talk to an expert(link takes you to an external page)](https://interactive.twilio.com/silent-network-auth-sales-1?_ga=2.37177440.1944479737.1659912854-303184958.1630969149 "talk to an expert") to request access to this feature.

Silent Network Auth (SNA) is a secure verification channel that verifies user possession of a mobile number without explicit user intervention. It uses the built-in connectivity to the mobile network operator (carrier). In the background, Twilio verifies the phone number by confirming directly from the carrier that the number corresponds to the SIM card located in the device requesting the authentication. This all happens without one-time password (OTP) prompts or visible redirects for the end user.

See [Verify Silent Network Auth Overview](/docs/verify/sna "Verify Silent Network Auth Overview") to learn more about this exciting feature.

To use SNA, complete the following steps:

  1. Start a new Verification with the `sna` channel using Verifications API.
  2. Send `POST` request to response property `sna.url` from client device that's connected to a mobile network.
  3. Check that the Verification was successful using [Verification Check API](/docs/verify/api/verification-check "Verification Check API").


To begin, use the [Start New Verification](/docs/verify/api/verification#start-new-verification "Start New Verification") endpoint with the parameter `channel=sna`.

Start a Verification With Silent Network AuthLink to code sample: Start a Verification With Silent Network Auth

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

    async function createVerification() {


    11

      const verification = await client.verify.v2


    12

        .services("VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .verifications.create({


    14

          channel: "sna",


    15

          to: "+15017122661",


    16

        });


    17




    18

      console.log(verification.sid);


    19

    }


    20




    21

    createVerification();

### Response

Note about this response

Copy response


    1

    {


    2

      "sid": "VEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "service_sid": "VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

      "to": "+15017122661",


    6

      "channel": "sna",


    7

      "status": "pending",


    8

      "valid": false,


    9

      "date_created": "2015-07-30T20:00:00Z",


    10

      "date_updated": "2015-07-30T20:00:00Z",


    11

      "lookup": {


    12

        "carrier": {


    13

          "mobile_country_code": "311",


    14

          "type": "mobile",


    15

          "error_code": null,


    16

          "mobile_network_code": "180",


    17

          "name": "T-Mobile USA, Inc."


    18

        }


    19

      },


    20

      "amount": null,


    21

      "payee": null,


    22

      "send_code_attempts": [


    23

        {


    24

          "time": "2015-07-30T20:00:00Z",


    25

          "channel": "sna",


    26

          "attempt_sid": "VLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    27

        }


    28

      ],


    29

      "sna": {


    30

        "url": "https://mi.dnlsrv.com/m/id/ANBByzx7?data=AAAglRRdNn02iTFWfDWwdTjOzM8o%2F6JB86fH%2Bt%2FFftUPj0pFA0u8%2FibWuYwzmMeMOtdTwYlsO8V%2FXF%2BJmngMhbeGKYhHeTOF2H9VrGEYKcEEklPxHgb5GgL3XtYa33j3lIU%2By6InvoV%2FowWHBzA0QeFPBh6vmJ8LoUPJqGE7q0PRz618Z4ym1AGq%2BaomSq9PlP4rCduv9Cmtxu%2FrvPSBwocs0GCWDE8seK8t9epmPQW7gwODxkAiKr9UxhJd9KvmBVuAQPf%2BoFQVo86USXkhXqTvUzB2bNUYY9FCy3CWgZFTOa1D3H1CVxf1eHzYIswNA7SmOzP%2FBX8g6%2B0hkzwMRkcit3gBNs4evAVJiqAgYvUlrtGwwv9bFx4X7jWSHY4%3D&cipherSalt=yANeDq09bwM38SJs"


    31

      },


    32

      "url": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Verifications/VEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    33

    }

### Send POST request to response property sna.url

send-post-request-to-response-property-snaurl page anchor

Positive FeedbackNegative Feedback

Check your response from the [Start New Verification](/docs/verify/api/verification#start-new-verification "Start New Verification") endpoint for the `sna.url` property:

Copy code block


    1

    "sna": {


    2

         "url": "https://mi.dnlsrv.com/m/id/ANBByzx7?data=AAAglRRdNn02iTFWfDWwdTjOzM8o%2F6JB86fH%2Bt%2FFftUPj0pFA0u8%2FibWuYwzmMeMOtdTwYlsO8V%2FXF%2BJmngMhbeGKYhHeTOF2H9VrGEYKcEEklPxHgb5GgL3XtYa33j3lIU%2By6InvoV%2FowWHBzA0QeFPBh6vmJ8LoUPJqGE7q0PRz618Z4ym1AGq%2BaomSq9PlP4rCduv9Cmtxu%2FrvPSBwocs0GCWDE8seK8t9epmPQW7gwODxkAiKr9UxhJd9KvmBVuAQPf%2BoFQVo86USXkhXqTvUzB2bNUYY9FCy3CWgZFTOa1D3H1CVxf1eHzYIswNA7SmOzP%2FBX8g6%2B0hkzwMRkcit3gBNs4evAVJiqAgYvUlrtGwwv9bFx4X7jWSHY4%3D&cipherSalt=yANeDq09bwM38SJs"


    3

    }

Then do an `HTTP POST` request to `sna.url` over the end user's mobile network to continue the authentication process. Note that `sna.url` is unique for every Verification Attempt, has a defined time-to-live of 10 minutes, and can only be processed once.

Copy code block


    curl -X POST https://mi.dnlsrv.com/m/id/ANBByzx7?data=AAAglRRdNn02iTFWfDWwdTjOzM8o%2F6JB86fH%2Bt%2FFftUPj0pFA0u8%2FibWuYwzmMeMOtdTwYlsO8V%2FXF%2BJmngMhbeGKYhHeTOF2H9VrGEYKcEEklPxHgb5GgL3XtYa33j3lIU%2By6InvoV%2FowWHBzA0QeFPBh6vmJ8LoUPJqGE7q0PRz618Z4ym1AGq%2BaomSq9PlP4rCduv9Cmtxu%2FrvPSBwocs0GCWDE8seK8t9epmPQW7gwODxkAiKr9UxhJd9KvmBVuAQPf%2BoFQVo86USXkhXqTvUzB2bNUYY9FCy3CWgZFTOa1D3H1CVxf1eHzYIswNA7SmOzP%2FBX8g6%2B0hkzwMRkcit3gBNs4evAVJiqAgYvUlrtGwwv9bFx4X7jWSHY4%3D&cipherSalt=yANeDq09bwM38SJs

This `POST` request will prompt multiple redirects behind the scenes, including contacting the carrier to confirm phone number ownership. You can expect to receive a `200` response from this request in under four seconds.

Next, use [Verification Check API](/docs/verify/api/verification-check "Verification Check API") to confirm that the `POST` request and Verification Attempt was successful.

* * *

## Start a new Verification with AutomaticSMS fallback

start-a-new-verification-with-automaticsms-fallback page anchor

Positive FeedbackNegative Feedback

(information)

## Info

Verify Automatic SMS Fallback is currently in the Pilot maturity stage, please [contact sales(link takes you to an external page)](https://www.twilio.com/en-us/help/sales "contact sales") to request access to this feature.

Setting the `channel` parameter to `auto` will attempt a verification using [Silent Network Auth](/docs/verify/authentication-channels#silent-network-auth "Silent Network Auth") (SNA) with a fallback to [SMS](/docs/verify/authentication-channels#sms-with-rcs-upgrade "SMS") if needed. Learn more about [Automatic SMS Fallback](/docs/verify/automatic-channel-selection "Automatic SMS Fallback").

To use Automatic SMS Fallback, complete the following steps:

  1. Start a new Verification with the `auto` channel using Verifications API, including the optional parameter `device_ip`.
  2. Check the response for the `channel` property to see if `sna` or `sms` was used.
     * If `sna` was used: Continue following the SNA Verification process, see [Send `POST` request to response property sna.url](/docs/verify/api/verification#send-post-request-to-response-property-snaurl) for instructions.
     * If `sms` was used: No further actions required, skip to step 3.
  3. Check that the Verification was successful using [Verification Check API](/docs/verify/api/verification-check "Verification Check API").


Start a Verification With Automatic SMS FallbackLink to code sample: Start a Verification With Automatic SMS Fallback

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

    async function createVerification() {


    11

      const verification = await client.verify.v2


    12

        .services("VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .verifications.create({


    14

          channel: "auto",


    15

          deviceIp: "0.000.00.000",


    16

          to: "+15017122661",


    17

        });


    18




    19

      console.log(verification.sid);


    20

    }


    21




    22

    createVerification();

### Response

Note about this response

Copy response


    1

    {


    2

      "sid": "VEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "service_sid": "VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

      "to": "+15017122661",


    6

      "channel": "auto",


    7

      "status": "pending",


    8

      "valid": false,


    9

      "date_created": "2015-07-30T20:00:00Z",


    10

      "date_updated": "2015-07-30T20:00:00Z",


    11

      "lookup": {


    12

        "carrier": {


    13

          "mobile_country_code": "311",


    14

          "type": "mobile",


    15

          "error_code": null,


    16

          "mobile_network_code": "180",


    17

          "name": "T-Mobile USA, Inc."


    18

        }


    19

      },


    20

      "amount": null,


    21

      "payee": null,


    22

      "send_code_attempts": [


    23

        {


    24

          "time": "2015-07-30T20:00:00Z",


    25

          "channel": "sna",


    26

          "attempt_sid": "VLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    27

        }


    28

      ],


    29

      "sna": {


    30

        "url": "https://mi.dnlsrv.com/m/id/ANBByzx7?data=AAAglRRdNn02iTFWfDWwdTjOzM8o%2F6JB86fH%2Bt%2FFftUPj0pFA0u8%2FibWuYwzmMeMOtdTwYlsO8V%2FXF%2BJmngMhbeGKYhHeTOF2H9VrGEYKcEEklPxHgb5GgL3XtYa33j3lIU%2By6InvoV%2FowWHBzA0QeFPBh6vmJ8LoUPJqGE7q0PRz618Z4ym1AGq%2BaomSq9PlP4rCduv9Cmtxu%2FrvPSBwocs0GCWDE8seK8t9epmPQW7gwODxkAiKr9UxhJd9KvmBVuAQPf%2BoFQVo86USXkhXqTvUzB2bNUYY9FCy3CWgZFTOa1D3H1CVxf1eHzYIswNA7SmOzP%2FBX8g6%2B0hkzwMRkcit3gBNs4evAVJiqAgYvUlrtGwwv9bFx4X7jWSHY4%3D&cipherSalt=yANeDq09bwM38SJs"


    31

      },


    32

      "url": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Verifications/VEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    33

    }

* * *

## Start a new Verification with a pre-defined template

start-a-new-verification-with-a-pre-defined-template page anchor

Positive FeedbackNegative Feedback

The message body of an SMS or Voice Verification can be overridden by using a template. To do so, the template `SID<HJ>` must be sent as a parameter in the Start Verification request.
The template `SID<HJ>` is a unique ID starting with the letters `HJ`. A complete list of the available templates for the account can be obtained by querying the Templates API.

Start a Verification using a templateLink to code sample: Start a Verification using a template

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

    async function createVerification() {


    11

      const verification = await client.verify.v2


    12

        .services("VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .verifications.create({


    14

          channel: "sms",


    15

          templateSid: "HJXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    16

          to: "+15017122661",


    17

        });


    18




    19

      console.log(verification.status);


    20

    }


    21




    22

    createVerification();

### Response

Note about this response

Copy response


    1

    {


    2

      "sid": "VEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "service_sid": "VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

      "to": "+15017122661",


    6

      "channel": "sms",


    7

      "status": "pending",


    8

      "valid": false,


    9

      "date_created": "2015-07-30T20:00:00Z",


    10

      "date_updated": "2015-07-30T20:00:00Z",


    11

      "lookup": {},


    12

      "amount": null,


    13

      "payee": null,


    14

      "send_code_attempts": [


    15

        {


    16

          "time": "2015-07-30T20:00:00Z",


    17

          "channel": "SMS",


    18

          "attempt_sid": "VLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    19

        }


    20

      ],


    21

      "sna": null,


    22

      "url": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Verifications/VEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    23

    }

Start a Verification with EmailLink to code sample: Start a Verification with Email

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

    async function createVerification() {


    11

      const verification = await client.verify.v2


    12

        .services("VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .verifications.create({


    14

          channel: "email",


    15

          to: "customer@example.com",


    16

        });


    17




    18

      console.log(verification.sid);


    19

    }


    20




    21

    createVerification();

### Response

Note about this response

Copy response


    1

    {


    2

      "sid": "VEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "service_sid": "VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

      "to": "customer@example.com",


    6

      "channel": "email",


    7

      "status": "pending",


    8

      "valid": false,


    9

      "date_created": "2015-07-30T20:00:00Z",


    10

      "date_updated": "2015-07-30T20:00:00Z",


    11

      "lookup": {},


    12

      "amount": null,


    13

      "payee": null,


    14

      "send_code_attempts": [


    15

        {


    16

          "time": "2015-07-30T20:00:00Z",


    17

          "channel": "SMS",


    18

          "attempt_sid": "VLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    19

        }


    20

      ],


    21

      "sna": null,


    22

      "url": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Verifications/VEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    23

    }

### Email Channel Configuration

email-channel-configuration page anchor

Positive FeedbackNegative Feedback

(information)

## Info

Verify's email channel requires additional Service configuration. Please refer to the [email channel setup documentation](/docs/verify/email "email channel setup documentation") for detailed instructions.

The email `ChannelConfiguration` parameter is an object that supports the following keys for customizing email verifications:

Key| Data type| Description
---|---|---
`from`| string| Optional parameter. If included must be a valid email address.
`from_name`| string| Optional parameter. Name of the sender.
`template_id`| string| Override the default template from the Verify Service email integration. Create a new template in the [SendGrid dashboard(link takes you to an external page)](https://mc.sendgrid.com/dynamic-templates "SendGrid dashboard") or learn more in the [SendGrid docs(link takes you to an external page)](https://sendgrid.com/docs/ui/sending-email/how-to-send-an-email-with-dynamic-transactional-templates/ "SendGrid docs").
`substitutions`| object| Variable substitution for dynamic email templates. See code sample below. Learn more about [substitution and section tags(link takes you to an external page)](https://sendgrid.com/docs/ui/sending-email/substitution-and-section-tags/ "substitution and section tags").

#### Substitutions code sample

substitutions-code-sample page anchor

Copy code block


    1

    {


    2

      "substitutions": {


    3

        "username": "jdoe321",


    4

        "first_name": "Jane",


    5

        "last_name": "Doe"


    6

      }


    7

    }

### Localization and supported languages

localization-and-supported-languages page anchor

Positive FeedbackNegative Feedback

Verify supports delivering verification codes in more than 30 languages over SMS, Voice, and WhatsApp. The language for a verification message resolves based on the country code of the phone number provided, with English as the fallback language. To find out more about which languages are supported, visit our page on [Supported Languages](/docs/verify/supported-languages "Supported Languages").

(information)

## Canadian Carrier Data Support

By default, Verify will not return carrier data for Canadian phone numbers. If you need carrier data on Canadian phone numbers, please visit our [support site(link takes you to an external page)](https://help.twilio.com/hc/en-us/articles/360004563433-Twilio-Lookups-API-is-Not-Returning-Carrier-Data-for-Canadian-Phone-Numbers "support site") to enable this feature.

* * *

## Fetch a Verification

fetch-a-verification page anchor

Positive FeedbackNegative Feedback

`GET https://verify.twilio.com/v2/Services/{ServiceSid}/Verifications/{Sid}`

### Path parameters

path-parameters-1 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

serviceSidSID<VA>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the verification [Service](/docs/verify/api/service "Service") to fetch the resource from.

Pattern: `^VA[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

sidstring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The Twilio-provided string that uniquely identifies the Verification resource to fetch.

Fetch a Verification by SIDLink to code sample: Fetch a Verification by SID

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

    async function fetchVerification() {


    11

      const verification = await client.verify.v2


    12

        .services("VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .verifications("VEXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")


    14

        .fetch();


    15




    16

      console.log(verification.status);


    17

    }


    18




    19

    fetchVerification();

### Response

Note about this response

Copy response


    1

    {


    2

      "sid": "VEXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    3

      "service_sid": "VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

      "to": "+15017122661",


    6

      "channel": "sms",


    7

      "status": "pending",


    8

      "valid": false,


    9

      "date_created": "2015-07-30T20:00:00Z",


    10

      "date_updated": "2015-07-30T20:00:00Z",


    11

      "lookup": {},


    12

      "amount": null,


    13

      "payee": null,


    14

      "send_code_attempts": [


    15

        {


    16

          "time": "2015-07-30T20:00:00Z",


    17

          "channel": "SMS",


    18

          "attempt_sid": "VLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    19

        }


    20

      ],


    21

      "sna": null,


    22

      "url": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Verifications/VEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    23

    }

* * *

## Update a Verification Status

update-a-verification-status page anchor

Positive FeedbackNegative Feedback

`POST https://verify.twilio.com/v2/Services/{ServiceSid}/Verifications/{Sid}`

Mark the verification as `approved` after your application had validated the verification code.

Mark the verification as `canceled` to start a new verification session with a different code before the previous code expires (10 minutes). Only recommended during [testing(link takes you to an external page)](https://www.twilio.com/blog/test-verify-no-rate-limits "testing") or if you're using [custom verification codes](/docs/verify/api/customization-options "custom verification codes").

For most other use cases, Verify is able to manage the complete lifecycle of a verification with the [Verification Check Resource](/docs/verify/api/verification-check "Verification Check Resource").

### Path parameters

path-parameters-2 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

serviceSidSID<VA>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the verification [Service](/docs/verify/api/service "Service") to update the resource from.

Pattern: `^VA[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

sidstring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The Twilio-provided string that uniquely identifies the Verification resource to update.

### Request body parameters

request-body-parameters-1 page anchor

Positive FeedbackNegative Feedback

Encoding type:`application/x-www-form-urlencoded`

SchemaExample

Property nameTypeRequiredPIIDescriptionChild properties

statusenum<string>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The status of the verification. Can be: `pending`, `approved`, `canceled`, `max_attempts_reached`, `deleted`, `failed` or `expired`.

Possible values:

`canceled``approved`

Select from available examples

Copy code block


    {


      "Status": "canceled"


    }

Manually Approve Verification using SIDLink to code sample: Manually Approve Verification using SID

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

    async function updateVerification() {


    11

      const verification = await client.verify.v2


    12

        .services("VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .verifications("VEXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")


    14

        .update({ status: "approved" });


    15




    16

      console.log(verification.status);


    17

    }


    18




    19

    updateVerification();

### Response

Note about this response

Copy response


    1

    {


    2

      "sid": "VEXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    3

      "service_sid": "VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

      "to": "+15017122661",


    6

      "channel": "sms",


    7

      "status": "approved",


    8

      "valid": false,


    9

      "date_created": "2015-07-30T20:00:00Z",


    10

      "date_updated": "2015-07-30T20:00:00Z",


    11

      "lookup": {},


    12

      "amount": null,


    13

      "payee": null,


    14

      "send_code_attempts": [


    15

        {


    16

          "time": "2015-07-30T20:00:00Z",


    17

          "channel": "SMS",


    18

          "attempt_sid": "VLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    19

        }


    20

      ],


    21

      "sna": null,


    22

      "url": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Verifications/VEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    23

    }

Manually Approve Verification using Phone NumberLink to code sample: Manually Approve Verification using Phone Number

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

    async function updateVerification() {


    11

      const verification = await client.verify.v2


    12

        .services("VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .verifications("+15017122661")


    14

        .update({ status: "approved" });


    15




    16

      console.log(verification.status);


    17

    }


    18




    19

    updateVerification();

### Response

Note about this response

Copy response


    1

    {


    2

      "sid": "+15017122661",


    3

      "service_sid": "VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

      "to": "+15017122661",


    6

      "channel": "sms",


    7

      "status": "approved",


    8

      "valid": true,


    9

      "date_created": "2015-07-30T20:00:00Z",


    10

      "date_updated": "2015-07-30T20:00:00Z",


    11

      "lookup": {},


    12

      "amount": null,


    13

      "payee": null,


    14

      "send_code_attempts": [


    15

        {


    16

          "time": "2015-07-30T20:00:00Z",


    17

          "channel": "SMS",


    18

          "attempt_sid": "VLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    19

        }


    20

      ],


    21

      "sna": null,


    22

      "url": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Verifications/VEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    23

    }

Manually Cancel a VerificationLink to code sample: Manually Cancel a Verification

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

    async function updateVerification() {


    11

      const verification = await client.verify.v2


    12

        .services("VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .verifications("VEXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")


    14

        .update({ status: "canceled" });


    15




    16

      console.log(verification.status);


    17

    }


    18




    19

    updateVerification();

### Response

Note about this response

Copy response


    1

    {


    2

      "sid": "VEXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    3

      "service_sid": "VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

      "to": "+15017122661",


    6

      "channel": "sms",


    7

      "status": "canceled",


    8

      "valid": false,


    9

      "date_created": "2015-07-30T20:00:00Z",


    10

      "date_updated": "2015-07-30T20:00:00Z",


    11

      "lookup": {},


    12

      "amount": null,


    13

      "payee": null,


    14

      "send_code_attempts": [


    15

        {


    16

          "time": "2015-07-30T20:00:00Z",


    17

          "channel": "SMS",


    18

          "attempt_sid": "VLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    19

        }


    20

      ],


    21

      "sna": null,


    22

      "url": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Verifications/VEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    23

    }

* * *

## Next steps

next-steps page anchor

Positive FeedbackNegative Feedback

After you know how to start a verification, explore these resources:

  * Use the [Verification Check API](/docs/verify/api/verification-check "Verification Check API") to validate if the code a user provided was correct or that the Silent Network Auth (SNA) process was successful.
  * Learn more about [Verify authentication channels](/docs/verify/authentication-channels "Verify authentication channels") to understand all available verification methods.
  * Explore [customization options](/docs/verify/api/customization-options "customization options") to tailor verifications to your brand.