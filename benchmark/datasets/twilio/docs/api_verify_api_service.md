# Services

*Source: https://www.twilio.com/docs/verify/api/service*

---

# Services

Positive FeedbackNegative Feedback

* * *

A Verification Service is the set of common configurations used to create and check verifications. You can create a service with the API [or in the Console(link takes you to an external page)](https://www.twilio.com/console/verify/services "or in the Console"). Services include configuration for features like:

  * [Email](/docs/verify/email "Email")
  * Friendly Name (used in the Verification message templates, except in countries with [brand restrictions(link takes you to an external page)](https://help.twilio.com/hc/en-us/articles/12387480513307-Why-was-my-friendly-name-not-included-in-the-Verify-SMS- "brand restrictions"))
  * Code Length
  * Skip sending SMS to Landlines
  * Requiring DTMF Input for Voice Verifications
  * Turning on Twilio Lookup


The SMS channel example below shows different friendly names and code lengths used in our SMS message templates.

Expand image

* * *

## Email verification

email-verification page anchor

Positive FeedbackNegative Feedback

Follow along with [the instructions here](/docs/verify/email "the instructions here") to set up your service to send email verifications.

* * *

## Service Response Properties

service-response-properties page anchor

Positive FeedbackNegative Feedback

These fields are returned in the output JSON response. The type `SID<VA>` is a unique ID starting with the letters VA.

Property nameTypeRequiredPIIDescriptionChild properties

sidSID<VA>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique string that we created to identify the Service resource.

Pattern: `^VA[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

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

The name that appears in the body of your verification messages. It can be up to 30 characters long and can include letters, numbers, spaces, dashes, underscores. Phone numbers, special characters or links are NOT allowed. It cannot contain more than 4 (consecutive or non-consecutive) digits. **This value should not contain PII.**

* * *

codeLengthinteger

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The length of the verification code to generate.

Default: `0`

* * *

lookupEnabledboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether to perform a lookup with each verification started and return info about the phone number.

* * *

psd2Enabledboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether to pass PSD2 transaction parameters when starting a verification.

* * *

skipSmsToLandlinesboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether to skip sending SMS verifications to landlines. Requires `lookup_enabled`.

* * *

dtmfInputRequiredboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether to ask the user to press a number before delivering the verify code in a phone call.

* * *

ttsNamestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The name of an alternative text-to-speech service to use in phone calls. Applies only to TTS languages.

* * *

doNotShareWarningEnabledboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether to add a security warning at the end of an SMS verification body. Disabled by default and applies only to SMS. Example SMS body: `Your AppName verification code is: 1234. Don’t share this code with anyone; our employees will never ask for the code`

* * *

customCodeEnabledboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether to allow sending verifications with a custom code instead of a randomly generated one.

* * *

push

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Configurations for the Push factors (channel) created under this Service.

* * *

totp

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Configurations for the TOTP factors (channel) created under this Service.

* * *

defaultTemplateSidSID<HJ>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Pattern: `^HJ[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

whatsappnull

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

* * *

passkeysnull

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

* * *

verifyEventSubscriptionEnabledboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether to allow verifications from the service to reach the stream-events sinks if configured

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

urlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The absolute URL of the resource.

* * *

linksobject<uri-map>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URLs of related resources.

* * *

## Create a Verification Service

create-a-verification-service page anchor

Positive FeedbackNegative Feedback

`POST https://verify.twilio.com/v2/Services`

These are the available input parameters for creating a Service.

### Request body parameters

request-body-parameters page anchor

Positive FeedbackNegative Feedback

Encoding type:`application/x-www-form-urlencoded`

SchemaExample

Property nameTypeRequiredPIIDescriptionChild properties

friendlyNamestring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A descriptive string that you create to describe the verification service. It can be up to 32 characters long. **This value should not contain PII.**

* * *

codeLengthinteger

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The length of the verification code to generate. Must be an integer value between 4 and 10, inclusive.

* * *

lookupEnabledboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether to perform a lookup with each verification started and return info about the phone number.

* * *

skipSmsToLandlinesboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether to skip sending SMS verifications to landlines. Requires `lookup_enabled`.

* * *

dtmfInputRequiredboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether to ask the user to press a number before delivering the verify code in a phone call.

* * *

ttsNamestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The name of an alternative text-to-speech service to use in phone calls. Applies only to TTS languages.

* * *

psd2Enabledboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether to pass PSD2 transaction parameters when starting a verification.

* * *

doNotShareWarningEnabledboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether to add a security warning at the end of an SMS verification body. Disabled by default and applies only to SMS. Example SMS body: `Your AppName verification code is: 1234. Don’t share this code with anyone; our employees will never ask for the code`

* * *

customCodeEnabledboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether to allow sending verifications with a custom code instead of a randomly generated one.

* * *

push.includeDateboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Optional configuration for the Push factors. If true, include the date in the Challenge's response. Otherwise, the date is omitted from the response. See [Challenge](/docs/verify/api/challenge "Challenge") resource’s details parameter for more info. Default: false. **Deprecated** do not use this parameter. This timestamp value is the same one as the one found in `date_created`, please use that one instead.

* * *

push.apnCredentialSidSID<CR>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Optional configuration for the Push factors. Set the APN Credential for this service. This will allow to send push notifications to iOS devices. See [Credential Resource](/docs/notify/api/credential-resource "Credential Resource")

Pattern: `^CR[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

push.fcmCredentialSidSID<CR>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Optional configuration for the Push factors. Set the FCM Credential for this service. This will allow to send push notifications to Android devices. See [Credential Resource](/docs/notify/api/credential-resource "Credential Resource")

Pattern: `^CR[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

totp.issuerstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Optional configuration for the TOTP factors. Set TOTP Issuer for this service. This will allow to configure the issuer of the TOTP URI. Defaults to the service friendly name if not provided.

* * *

totp.timeStepinteger

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Optional configuration for the TOTP factors. Defines how often, in seconds, are TOTP codes generated. i.e, a new TOTP code is generated every time_step seconds. Must be between 20 and 60 seconds, inclusive. Defaults to 30 seconds

* * *

totp.codeLengthinteger

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Optional configuration for the TOTP factors. Number of digits for generated TOTP codes. Must be between 3 and 8, inclusive. Defaults to 6

* * *

totp.skewinteger

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Optional configuration for the TOTP factors. The number of time-steps, past and future, that are valid for validation of TOTP codes. Must be between 0 and 2, inclusive. Defaults to 1

* * *

defaultTemplateSidSID<HJ>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The default message [template](/docs/verify/api/templates "template"). Will be used for all SMS verifications unless explicitly overriden. SMS channel only.

Pattern: `^HJ[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

whatsapp.msgServiceSidSID<MG>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the Messaging Service containing WhatsApp Sender(s) that Verify will use to send WhatsApp messages to your users.

Pattern: `^MG[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

whatsapp.fromstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The number to use as the WhatsApp Sender that Verify will use to send WhatsApp messages to your users.This WhatsApp Sender must be associated with a Messaging Service SID.

* * *

passkeys.relyingParty.idstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The Relying Party ID for Passkeys. This is the domain of your application, e.g. `example.com`. It is used to identify your application when creating Passkeys.

* * *

passkeys.relyingParty.namestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The Relying Party Name for Passkeys. This is the name of your application, e.g. `Example App`. It is used to identify your application when creating Passkeys.

* * *

passkeys.relyingParty.originsstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The Relying Party Origins for Passkeys. This is the origin of your application, e.g. `login.example.com,www.example.com`. It is used to identify your application when creating Passkeys, it can have multiple origins split by `,`.

* * *

passkeys.authenticatorAttachmentstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The Authenticator Attachment for Passkeys. This is the type of authenticator that will be used to create Passkeys. It can be empty or it can have the values `platform`, `cross-platform` or `any`.

* * *

passkeys.discoverableCredentialsstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Indicates whether credentials must be discoverable by the authenticator. It can be empty or it can have the values `required`, `preferred` or `discouraged`.

* * *

passkeys.userVerificationstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The User Verification for Passkeys. This is the type of user verification that will be used to create Passkeys. It can be empty or it can have the values `required`, `preferred` or `discouraged`.

* * *

verifyEventSubscriptionEnabledboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether to allow verifications from the service to reach the stream-events sinks if configured

Copy code block


    {


      "FriendlyName": "name",


      "CodeLength": 4,


      "LookupEnabled": false,


      "Psd2Enabled": false,


      "SkipSmsToLandlines": false,


      "DtmfInputRequired": false,


      "TtsName": "name",


      "MailerSid": "MDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


      "DoNotShareWarningEnabled": false,


      "CustomCodeEnabled": true,


      "Push.ApnCredentialSid": "CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


      "Totp.Issuer": "test-issuer",


      "Totp.TimeStep": 30,


      "Totp.CodeLength": 3,


      "Totp.Skew": 2,


      "DefaultTemplateSid": "HJaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


      "VerifyEventSubscriptionEnabled": false


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

      const service = await client.verify.v2.services.create({


    12

        friendlyName: "My Verify Service",


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

      "sid": "VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "friendly_name": "My Verify Service",


    5

      "code_length": 4,


    6

      "lookup_enabled": false,


    7

      "psd2_enabled": false,


    8

      "skip_sms_to_landlines": false,


    9

      "dtmf_input_required": false,


    10

      "tts_name": "name",


    11

      "do_not_share_warning_enabled": false,


    12

      "custom_code_enabled": true,


    13

      "push": {


    14

        "include_date": false,


    15

        "apn_credential_sid": "CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    16

        "fcm_credential_sid": null


    17

      },


    18

      "totp": {


    19

        "issuer": "test-issuer",


    20

        "time_step": 30,


    21

        "code_length": 3,


    22

        "skew": 2


    23

      },


    24

      "whatsapp": {


    25

        "msg_service_sid": "MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    26

        "from": "whatsapp:+1234567890"


    27

      },


    28

      "passkeys": {


    29

        "relying_party": {


    30

          "id": "www.mydomain.com",


    31

          "name": "My domain",


    32

          "origins": [


    33

            "www.mydomain.com",


    34

            "www.login.mydomain.com"


    35

          ]


    36

        },


    37

        "authenticator_attachment": "",


    38

        "discoverable_credentials": null,


    39

        "user_verification": "discouraged"


    40

      },


    41

      "default_template_sid": "HJaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    42

      "verify_event_subscription_enabled": false,


    43

      "date_created": "2015-07-30T20:00:00Z",


    44

      "date_updated": "2015-07-30T20:00:00Z",


    45

      "url": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    46

      "links": {


    47

        "verification_checks": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/VerificationCheck",


    48

        "verifications": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Verifications",


    49

        "rate_limits": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/RateLimits",


    50

        "messaging_configurations": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/MessagingConfigurations",


    51

        "entities": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Entities",


    52

        "webhooks": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Webhooks",


    53

        "access_tokens": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AccessTokens"


    54

      }


    55

    }

* * *

## Associate a predefined template with a service

associate-a-predefined-template-with-a-service page anchor

Positive FeedbackNegative Feedback

A predefined template (public or private if there are any associated with your account) can be associated with a Verification Service by setting the `DefaultTemplateSid` attribute. By doing so, the message body of the verifications created with the service will use the text defined in the referenced template by default.

The default template `SID<HJ>` is a unique ID starting with the letters `HJ`. It's generated when the template is created.

A complete list of the available templates for the account can be obtained by querying the [Templates API](/docs/verify/api/templates "Templates API").

The template that is going to be used in the verification will be selected in the following order:

  1. If a `TemplateSid` is received in the Create Verification request, the verification will use the text defined in the template identified with that `Sid`.
  2. If a `DefaultTemplateSid` is set for the Service, the verification will use the text defined in the template identified with that `Sid`.
  3. Otherwise, the text defined in the global default template will be used.


Create a Service with a default templateLink to code sample: Create a Service with a default template

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

      const service = await client.verify.v2.services.create({


    12

        defaultTemplateSid: "HJXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    13

        friendlyName: "My Verify Service",


    14

      });


    15




    16

      console.log(service.sid);


    17

    }


    18




    19

    createService();

### Response

Note about this response

Copy response


    1

    {


    2

      "sid": "VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "friendly_name": "My Verify Service",


    5

      "code_length": 4,


    6

      "lookup_enabled": false,


    7

      "psd2_enabled": false,


    8

      "skip_sms_to_landlines": false,


    9

      "dtmf_input_required": false,


    10

      "tts_name": "name",


    11

      "do_not_share_warning_enabled": false,


    12

      "custom_code_enabled": true,


    13

      "push": {


    14

        "include_date": false,


    15

        "apn_credential_sid": "CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    16

        "fcm_credential_sid": null


    17

      },


    18

      "totp": {


    19

        "issuer": "test-issuer",


    20

        "time_step": 30,


    21

        "code_length": 3,


    22

        "skew": 2


    23

      },


    24

      "whatsapp": {


    25

        "msg_service_sid": "MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    26

        "from": "whatsapp:+1234567890"


    27

      },


    28

      "passkeys": {


    29

        "relying_party": {


    30

          "id": "www.mydomain.com",


    31

          "name": "My domain",


    32

          "origins": [


    33

            "www.mydomain.com",


    34

            "www.login.mydomain.com"


    35

          ]


    36

        },


    37

        "authenticator_attachment": "",


    38

        "discoverable_credentials": null,


    39

        "user_verification": "discouraged"


    40

      },


    41

      "default_template_sid": "HJXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    42

      "verify_event_subscription_enabled": false,


    43

      "date_created": "2015-07-30T20:00:00Z",


    44

      "date_updated": "2015-07-30T20:00:00Z",


    45

      "url": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    46

      "links": {


    47

        "verification_checks": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/VerificationCheck",


    48

        "verifications": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Verifications",


    49

        "rate_limits": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/RateLimits",


    50

        "messaging_configurations": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/MessagingConfigurations",


    51

        "entities": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Entities",


    52

        "webhooks": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Webhooks",


    53

        "access_tokens": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AccessTokens"


    54

      }


    55

    }

Create a PSD2 Enabled ServiceLink to code sample: Create a PSD2 Enabled Service

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

      const service = await client.verify.v2.services.create({


    12

        friendlyName: "Owl Banking",


    13

        psd2Enabled: true,


    14

      });


    15




    16

      console.log(service.psd2Enabled);


    17

    }


    18




    19

    createService();

### Response

Note about this response

Copy response


    1

    {


    2

      "sid": "VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "friendly_name": "Owl Banking",


    5

      "code_length": 4,


    6

      "lookup_enabled": false,


    7

      "psd2_enabled": true,


    8

      "skip_sms_to_landlines": false,


    9

      "dtmf_input_required": false,


    10

      "tts_name": "name",


    11

      "do_not_share_warning_enabled": false,


    12

      "custom_code_enabled": true,


    13

      "push": {


    14

        "include_date": false,


    15

        "apn_credential_sid": "CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    16

        "fcm_credential_sid": null


    17

      },


    18

      "totp": {


    19

        "issuer": "test-issuer",


    20

        "time_step": 30,


    21

        "code_length": 3,


    22

        "skew": 2


    23

      },


    24

      "whatsapp": {


    25

        "msg_service_sid": "MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    26

        "from": "whatsapp:+1234567890"


    27

      },


    28

      "passkeys": {


    29

        "relying_party": {


    30

          "id": "www.mydomain.com",


    31

          "name": "My domain",


    32

          "origins": [


    33

            "www.mydomain.com",


    34

            "www.login.mydomain.com"


    35

          ]


    36

        },


    37

        "authenticator_attachment": "",


    38

        "discoverable_credentials": null,


    39

        "user_verification": "discouraged"


    40

      },


    41

      "default_template_sid": "HJaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    42

      "verify_event_subscription_enabled": false,


    43

      "date_created": "2015-07-30T20:00:00Z",


    44

      "date_updated": "2015-07-30T20:00:00Z",


    45

      "url": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    46

      "links": {


    47

        "verification_checks": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/VerificationCheck",


    48

        "verifications": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Verifications",


    49

        "rate_limits": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/RateLimits",


    50

        "messaging_configurations": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/MessagingConfigurations",


    51

        "entities": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Entities",


    52

        "webhooks": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Webhooks",


    53

        "access_tokens": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AccessTokens"


    54

      }


    55

    }

See [Verifying Transactions for PSD2](/docs/verify/verifying-transactions-psd2 "Verifying Transactions for PSD2") for more information.

* * *

## Fetch a Service

fetch-a-service page anchor

Positive FeedbackNegative Feedback

`GET https://verify.twilio.com/v2/Services/{Sid}`

### Path parameters

path-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

sidSID<VA>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The Twilio-provided string that uniquely identifies the Verification Service resource to fetch.

Pattern: `^VA[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

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

      const service = await client.verify.v2


    12

        .services("VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


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

      "sid": "VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "friendly_name": "name",


    5

      "code_length": 4,


    6

      "lookup_enabled": false,


    7

      "psd2_enabled": false,


    8

      "skip_sms_to_landlines": false,


    9

      "dtmf_input_required": false,


    10

      "tts_name": "name",


    11

      "do_not_share_warning_enabled": false,


    12

      "custom_code_enabled": true,


    13

      "push": {


    14

        "include_date": false,


    15

        "apn_credential_sid": null,


    16

        "fcm_credential_sid": null


    17

      },


    18

      "totp": {


    19

        "issuer": null,


    20

        "time_step": null,


    21

        "code_length": null,


    22

        "skew": null


    23

      },


    24

      "whatsapp": {


    25

        "msg_service_sid": null,


    26

        "from": null


    27

      },


    28

      "passkeys": {


    29

        "relying_party": {


    30

          "id": null,


    31

          "name": null,


    32

          "origins": null


    33

        },


    34

        "authenticator_attachment": null,


    35

        "discoverable_credentials": null,


    36

        "user_verification": null


    37

      },


    38

      "default_template_sid": "HJaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    39

      "verify_event_subscription_enabled": false,


    40

      "date_created": "2015-07-30T20:00:00Z",


    41

      "date_updated": "2015-07-30T20:00:00Z",


    42

      "url": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    43

      "links": {


    44

        "verification_checks": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/VerificationCheck",


    45

        "verifications": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Verifications",


    46

        "rate_limits": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/RateLimits",


    47

        "messaging_configurations": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/MessagingConfigurations",


    48

        "entities": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Entities",


    49

        "webhooks": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Webhooks",


    50

        "access_tokens": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AccessTokens"


    51

      }


    52

    }

* * *

## List all Services

list-all-services page anchor

Positive FeedbackNegative Feedback

`GET https://verify.twilio.com/v2/Services`

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

List all ServicesLink to code sample: List all Services

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

      const services = await client.verify.v2.services.list({ limit: 20 });


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

        "page_size": 50,


    5

        "first_page_url": "https://verify.twilio.com/v2/Services?PageSize=50&Page=0",


    6

        "previous_page_url": null,


    7

        "next_page_url": null,


    8

        "key": "services",


    9

        "url": "https://verify.twilio.com/v2/Services?PageSize=50&Page=0"


    10

      },


    11

      "services": [


    12

        {


    13

          "sid": "VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    14

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    15

          "friendly_name": "name",


    16

          "code_length": 4,


    17

          "lookup_enabled": false,


    18

          "psd2_enabled": false,


    19

          "skip_sms_to_landlines": false,


    20

          "dtmf_input_required": false,


    21

          "tts_name": "name",


    22

          "do_not_share_warning_enabled": false,


    23

          "custom_code_enabled": true,


    24

          "push": {


    25

            "include_date": false,


    26

            "apn_credential_sid": null,


    27

            "fcm_credential_sid": null


    28

          },


    29

          "totp": {


    30

            "issuer": null,


    31

            "time_step": null,


    32

            "code_length": null,


    33

            "skew": null


    34

          },


    35

          "whatsapp": {


    36

            "msg_service_sid": null,


    37

            "from": null


    38

          },


    39

          "passkeys": {


    40

            "relying_party": {


    41

              "id": null,


    42

              "name": null,


    43

              "origins": null


    44

            },


    45

            "authenticator_attachment": null,


    46

            "discoverable_credentials": null,


    47

            "user_verification": null


    48

          },


    49

          "default_template_sid": "HJaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    50

          "verify_event_subscription_enabled": false,


    51

          "date_created": "2015-07-30T20:00:00Z",


    52

          "date_updated": "2015-07-30T20:00:00Z",


    53

          "url": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    54

          "links": {


    55

            "verification_checks": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/VerificationCheck",


    56

            "verifications": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Verifications",


    57

            "rate_limits": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/RateLimits",


    58

            "messaging_configurations": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/MessagingConfigurations",


    59

            "entities": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Entities",


    60

            "webhooks": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Webhooks",


    61

            "access_tokens": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AccessTokens"


    62

          }


    63

        }


    64

      ]


    65

    }

* * *

## Update a Service

update-a-service page anchor

Positive FeedbackNegative Feedback

`POST https://verify.twilio.com/v2/Services/{Sid}`

These are the available input parameters for updating a Service. The type `SID<VA>` is a unique ID starting with the letters VA.

### Path parameters

path-parameters-1 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

sidSID<VA>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The Twilio-provided string that uniquely identifies the Service resource to update.

Pattern: `^VA[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

### Request body parameters

request-body-parameters-1 page anchor

Positive FeedbackNegative Feedback

Encoding type:`application/x-www-form-urlencoded`

SchemaExample

Property nameTypeRequiredPIIDescriptionChild properties

friendlyNamestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A descriptive string that you create to describe the verification service. It can be up to 32 characters long. **This value should not contain PII.**

* * *

codeLengthinteger

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The length of the verification code to generate. Must be an integer value between 4 and 10, inclusive.

* * *

lookupEnabledboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether to perform a lookup with each verification started and return info about the phone number.

* * *

skipSmsToLandlinesboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether to skip sending SMS verifications to landlines. Requires `lookup_enabled`.

* * *

dtmfInputRequiredboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether to ask the user to press a number before delivering the verify code in a phone call.

* * *

ttsNamestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The name of an alternative text-to-speech service to use in phone calls. Applies only to TTS languages.

* * *

psd2Enabledboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether to pass PSD2 transaction parameters when starting a verification.

* * *

doNotShareWarningEnabledboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether to add a privacy warning at the end of an SMS. **Disabled by default and applies only for SMS.**

* * *

customCodeEnabledboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether to allow sending verifications with a custom code instead of a randomly generated one.

* * *

push.includeDateboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Optional configuration for the Push factors. If true, include the date in the Challenge's response. Otherwise, the date is omitted from the response. See [Challenge](/docs/verify/api/challenge "Challenge") resource’s details parameter for more info. Default: false. **Deprecated** do not use this parameter.

* * *

push.apnCredentialSidSID<CR>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Optional configuration for the Push factors. Set the APN Credential for this service. This will allow to send push notifications to iOS devices. See [Credential Resource](/docs/notify/api/credential-resource "Credential Resource")

Pattern: `^CR[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

push.fcmCredentialSidSID<CR>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Optional configuration for the Push factors. Set the FCM Credential for this service. This will allow to send push notifications to Android devices. See [Credential Resource](/docs/notify/api/credential-resource "Credential Resource")

Pattern: `^CR[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

totp.issuerstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Optional configuration for the TOTP factors. Set TOTP Issuer for this service. This will allow to configure the issuer of the TOTP URI.

* * *

totp.timeStepinteger

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Optional configuration for the TOTP factors. Defines how often, in seconds, are TOTP codes generated. i.e, a new TOTP code is generated every time_step seconds. Must be between 20 and 60 seconds, inclusive. Defaults to 30 seconds

* * *

totp.codeLengthinteger

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Optional configuration for the TOTP factors. Number of digits for generated TOTP codes. Must be between 3 and 8, inclusive. Defaults to 6

* * *

totp.skewinteger

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Optional configuration for the TOTP factors. The number of time-steps, past and future, that are valid for validation of TOTP codes. Must be between 0 and 2, inclusive. Defaults to 1

* * *

defaultTemplateSidSID<HJ>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The default message [template](/docs/verify/api/templates "template"). Will be used for all SMS verifications unless explicitly overriden. SMS channel only.

Pattern: `^HJ[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

whatsapp.msgServiceSidSID<MG>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Messaging Service](/docs/messaging/services "Messaging Service") to associate with the Verification Service.

Pattern: `^MG[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

whatsapp.fromstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The WhatsApp number to use as the sender of the verification messages. This number must be associated with the WhatsApp Message Service.

* * *

passkeys.relyingParty.idstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The Relying Party ID for Passkeys. This is the domain of your application, e.g. `example.com`. It is used to identify your application when creating Passkeys.

* * *

passkeys.relyingParty.namestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The Relying Party Name for Passkeys. This is the name of your application, e.g. `Example App`. It is used to identify your application when creating Passkeys.

* * *

passkeys.relyingParty.originsstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The Relying Party Origins for Passkeys. This is the origin of your application, e.g. `login.example.com,www.example.com`. It is used to identify your application when creating Passkeys, it can have multiple origins split by `,`.

* * *

passkeys.authenticatorAttachmentstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The Authenticator Attachment for Passkeys. This is the type of authenticator that will be used to create Passkeys. It can be empty or it can have the values `platform`, `cross-platform` or `any`.

* * *

passkeys.discoverableCredentialsstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Indicates whether credentials must be discoverable by the authenticator. It can be empty or it can have the values `required`, `preferred` or `discouraged`.

* * *

passkeys.userVerificationstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The User Verification for Passkeys. This is the type of user verification that will be used to create Passkeys. It can be empty or it can have the values `required`, `preferred` or `discouraged`.

* * *

verifyEventSubscriptionEnabledboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether to allow verifications from the service to reach the stream-events sinks if configured

Copy code block


    {


      "FriendlyName": "name",


      "CodeLength": 4,


      "LookupEnabled": false,


      "Psd2Enabled": false,


      "SkipSmsToLandlines": false,


      "DtmfInputRequired": false,


      "TtsName": "name",


      "MailerSid": "MDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


      "DoNotShareWarningEnabled": false,


      "CustomCodeEnabled": true,


      "Push.IncludeDate": false,


      "Push.FcmCredentialSid": "CRbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",


      "Totp.Issuer": "test-issuer",


      "Totp.TimeStep": 30,


      "Totp.CodeLength": 3,


      "Totp.Skew": 2,


      "DefaultTemplateSid": "HJaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


      "VerifyEventSubscriptionEnabled": false


    }

* * *

## Associate a template with an existing service

associate-a-template-with-an-existing-service page anchor

Positive FeedbackNegative Feedback

A predefined template can be associated with an already created Verification Service by setting the `DefaultTemplateSid` attribute. By doing so, the message body of the verifications created with the service will use by default the text defined in the template.
The default template `SID<HJ>` is a unique ID starting with the letters `HJ`. It is generated when the template is created.

A complete list of the available templates for the account can be obtained by querying the [List Templates API](/docs/verify/api/templates "List Templates API").

The template that is going to be used in the verification will be defined following this order:

  1. If a `TemplateSid` is received in the Create Verification request, the verification will use the text defined in the template identified with that `Sid`.
  2. If a `DefaultTemplateSid` is set for the Service, the verification will use the text defined in the template identified with that `Sid`.
  3. Otherwise, the text defined in the default template will be used.


Update a Service default template.Link to code sample: Update a Service default template.

Report code block

Copy code block


    1

    curl -X POST https://verify.twilio.com/v2/Services/VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX \


    2

    --data-urlencode "DefaultTemplateSid=HJXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" \


    3

    -u $TWILIO_ACCOUNT_SID:$TWILIO_AUTH_TOKEN

### Output

Copy output


    1

    {


    2

      "sid": "VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    3

      "account_sid": "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    4

      "friendly_name": "name",


    5

      "code_length": 7,


    6

      "lookup_enabled": false,


    7

      "psd2_enabled": false,


    8

      "skip_sms_to_landlines": false,


    9

      "dtmf_input_required": false,


    10

      "tts_name": "name",


    11

      "do_not_share_warning_enabled": false,


    12

      "custom_code_enabled": true,


    13

      "push": {


    14

        "include_date": true,


    15

        "apn_credential_sid": null,


    16

        "fcm_credential_sid": "CRXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"


    17

      },


    18

      "totp": {


    19

        "issuer": "test-issuer",


    20

        "time_step": 30,


    21

        "code_length": 3,


    22

        "skew": 2


    23

      },


    24

      "date_created": "2015-07-30T20:00:00Z",


    25

      "date_updated": "2015-07-30T20:00:00Z",


    26

      "url": "https://verify.twilio.com/v2/Services/VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    27

      "links": {


    28

        "verification_checks": "https://verify.twilio.com/v2/Services/VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/VerificationCheck",


    29

        "verifications": "https://verify.twilio.com/v2/Services/VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Verifications",


    30

        "rate_limits": "https://verify.twilio.com/v2/Services/VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/RateLimits",


    31

        "messaging_configurations": "https://verify.twilio.com/v2/Services/VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/MessagingConfigurations",


    32

        "entities": "https://verify.twilio.com/v2/Services/VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Entities",


    33

        "webhooks": "https://verify.twilio.com/v2/Services/VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Webhooks",


    34

        "access_tokens": "https://verify.twilio.com/v2/Services/VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/AccessTokens"


    35

      }


    36

    }

Update a Service's Code LengthLink to code sample: Update a Service's Code Length

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

      const service = await client.verify.v2


    12

        .services("VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .update({ codeLength: 7 });


    14




    15

      console.log(service.codeLength);


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

      "sid": "VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "friendly_name": "name",


    5

      "code_length": 7,


    6

      "lookup_enabled": false,


    7

      "psd2_enabled": false,


    8

      "skip_sms_to_landlines": false,


    9

      "dtmf_input_required": false,


    10

      "tts_name": "name",


    11

      "do_not_share_warning_enabled": false,


    12

      "custom_code_enabled": true,


    13

      "push": {


    14

        "include_date": false,


    15

        "apn_credential_sid": null,


    16

        "fcm_credential_sid": "CRbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"


    17

      },


    18

      "totp": {


    19

        "issuer": "test-issuer",


    20

        "time_step": 30,


    21

        "code_length": 3,


    22

        "skew": 2


    23

      },


    24

      "whatsapp": {


    25

        "msg_service_sid": "MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    26

        "from": "whatsapp:+1234567890"


    27

      },


    28

      "passkeys": {


    29

        "relying_party": {


    30

          "id": null,


    31

          "name": null,


    32

          "origins": null


    33

        },


    34

        "authenticator_attachment": null,


    35

        "discoverable_credentials": null,


    36

        "user_verification": null


    37

      },


    38

      "default_template_sid": "HJaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    39

      "verify_event_subscription_enabled": false,


    40

      "date_created": "2015-07-30T20:00:00Z",


    41

      "date_updated": "2015-07-30T20:00:00Z",


    42

      "url": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    43

      "links": {


    44

        "verification_checks": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/VerificationCheck",


    45

        "verifications": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Verifications",


    46

        "rate_limits": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/RateLimits",


    47

        "messaging_configurations": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/MessagingConfigurations",


    48

        "entities": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Entities",


    49

        "webhooks": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Webhooks",


    50

        "access_tokens": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AccessTokens"


    51

      }


    52

    }

Update a Service NameLink to code sample: Update a Service Name

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

      const service = await client.verify.v2


    12

        .services("VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .update({ friendlyName: "New and Improved Service Name" });


    14




    15

      console.log(service.friendlyName);


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

      "sid": "VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "friendly_name": "New and Improved Service Name",


    5

      "code_length": 4,


    6

      "lookup_enabled": false,


    7

      "psd2_enabled": false,


    8

      "skip_sms_to_landlines": false,


    9

      "dtmf_input_required": false,


    10

      "tts_name": "name",


    11

      "do_not_share_warning_enabled": false,


    12

      "custom_code_enabled": true,


    13

      "push": {


    14

        "include_date": false,


    15

        "apn_credential_sid": null,


    16

        "fcm_credential_sid": "CRbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"


    17

      },


    18

      "totp": {


    19

        "issuer": "test-issuer",


    20

        "time_step": 30,


    21

        "code_length": 3,


    22

        "skew": 2


    23

      },


    24

      "whatsapp": {


    25

        "msg_service_sid": "MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    26

        "from": "whatsapp:+1234567890"


    27

      },


    28

      "passkeys": {


    29

        "relying_party": {


    30

          "id": null,


    31

          "name": null,


    32

          "origins": null


    33

        },


    34

        "authenticator_attachment": null,


    35

        "discoverable_credentials": null,


    36

        "user_verification": null


    37

      },


    38

      "default_template_sid": "HJaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    39

      "verify_event_subscription_enabled": false,


    40

      "date_created": "2015-07-30T20:00:00Z",


    41

      "date_updated": "2015-07-30T20:00:00Z",


    42

      "url": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    43

      "links": {


    44

        "verification_checks": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/VerificationCheck",


    45

        "verifications": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Verifications",


    46

        "rate_limits": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/RateLimits",


    47

        "messaging_configurations": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/MessagingConfigurations",


    48

        "entities": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Entities",


    49

        "webhooks": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Webhooks",


    50

        "access_tokens": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AccessTokens"


    51

      }


    52

    }

* * *

## Delete a Service

delete-a-service page anchor

Positive FeedbackNegative Feedback

`DELETE https://verify.twilio.com/v2/Services/{Sid}`

### Path parameters

path-parameters-2 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

sidSID<VA>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The Twilio-provided string that uniquely identifies the Verification Service resource to delete.

Pattern: `^VA[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

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

      await client.verify.v2


    12

        .services("VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .remove();


    14

    }


    15




    16

    deleteService();