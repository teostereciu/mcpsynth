# Templates

*Source: https://www.twilio.com/docs/verify/api/templates*

---

# Templates

Positive FeedbackNegative Feedback

* * *

(new)

## Verify Templates are in Public Beta!

Pre-approved and custom templates are currently in the Public Beta maturity stage, which means that:

We're actively looking for early-adopter customers to try it out and give us feedback. That could be you.

Pre-approved and custom templates are only supported with the **SMS and Voice** channels.

Templates are predefined and approved messages used to [send Verifications](/docs/verify/api/verification "send Verifications") that allow you to customize the Verification message. Your account can use multiple templates to accommodate different scenarios.

Verify provides three template types: Verify Default, pre-approved and custom to cover common use cases. Learn more about [getting started with Verification Templates](/docs/verify/verification-templates "getting started with Verification Templates").

* * *

## Template translations and supported languages

template-translations-and-supported-languages page anchor

Positive FeedbackNegative Feedback

Verify resolves the template message body's locale based on the phone number's country code. If it can't resolve the locale, Verify falls back to English or the custom template's default language. We recommend using this locale resolution. If you need to override the locale, pass the `Locale` parameter. [Learn more about supported languages here](/docs/verify/supported-languages "Learn more about supported languages here").

(information)

## Info

To learn about special restrictions for sending SMS, consult the issues on sending to [Singapore](/docs/verify/singapore "Singapore") or [Canada(link takes you to an external page)](https://help.twilio.com/hc/en-us/articles/12387480513307-Why-was-my-friendly-name-not-included-in-the-Verify-SMS- "Canada"). To use a template in China, [register the template with the account(link takes you to an external page)](https://help.twilio.com/articles/17024185400859 "register the template with the account").

* * *

## Template properties

template-properties page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescriptionChild properties

sidSID<HJ>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A 34 character string that uniquely identifies a Verification Template.

Pattern: `^HJ[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

accountSidSID<AC>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique SID identifier of the Account.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

friendlyNamestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A descriptive string that you create to describe a Template. It can be up to 32 characters long.

* * *

channelsarray[string]

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A list of channels that support the Template. Can include: sms, voice.

* * *

translations

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

An object that contains the different translations of the template. Every translation is identified by the language short name and contains its respective information as the approval status, text and created/modified date.

* * *

## Get a list of available templates

get-a-list-of-available-templates page anchor

Positive FeedbackNegative Feedback

`GET https://verify.twilio.com/v2/Templates`

### Query parameters

query-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

friendlyNamestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

String filter used to query templates with a given friendly name.

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

Get a list of available templatesLink to code sample: Get a list of available templates

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

    async function listVerificationTemplate() {


    11

      const templates = await client.verify.v2.templates.list({ limit: 20 });


    12




    13

      templates.forEach((t) => console.log(t.translations));


    14

    }


    15




    16

    listVerificationTemplate();

### Response

Note about this response

Copy response


    1

    {


    2

      "templates": [


    3

        {


    4

          "sid": "HJaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    6

          "friendly_name": "Base Verification Template 2 with do not share",


    7

          "channels": [


    8

            "sms"


    9

          ],


    10

          "translations": {


    11

            "en": {


    12

              "is_default_translation": true,


    13

              "status": "approved",


    14

              "locale": "en",


    15

              "text": "Your {{friendly_name}} verification code is: {{code}}. Do not share this code with anyone.",


    16

              "date_updated": "2021-07-29T20:38:28.759979905Z",


    17

              "date_created": "2021-07-29T20:38:28.165602325Z"


    18

            }


    19

          }


    20

        },


    21

        {


    22

          "sid": "HJaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",


    23

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    24

          "friendly_name": "Base Verification Template 3",


    25

          "channels": [


    26

            "sms",


    27

            "voice"


    28

          ],


    29

          "translations": {


    30

            "en": {


    31

              "is_default_translation": true,


    32

              "status": "approved",


    33

              "locale": "en",


    34

              "text": "Your verification code is: {{code}}. Do not share it.",


    35

              "date_updated": "2021-07-29T20:38:28.759979905Z",


    36

              "date_created": "2021-07-29T20:38:28.165602325Z"


    37

            }


    38

          }


    39

        }


    40

      ],


    41

      "meta": {


    42

        "page": 0,


    43

        "page_size": 50,


    44

        "first_page_url": "https://verify.twilio.com/v2/Templates?PageSize=50&Page=0",


    45

        "previous_page_url": null,


    46

        "url": "https://verify.twilio.com/v2/Templates?PageSize=50&Page=0",


    47

        "next_page_url": null,


    48

        "key": "templates"


    49

      }


    50

    }

(information)

## Tip

If you have [`jq`(link takes you to an external page)](https://jqlang.github.io/jq/) installed, you can list all English templates with the following command:

Copy code block


    1

    curl -X GET "https://verify.twilio.com/v2/Templates" \


    2

      -u $TWILIO_ACCOUNT_SID:$TWILIO_AUTH_TOKEN \


    3

      | jq '.templates[] | {sid: .sid, template: .translations.en.text}'

### Set a default template for your Verify Service

set-a-default-template-for-your-verify-service page anchor

Positive FeedbackNegative Feedback

To set a default template for a new Service, set the `default_template_sid` parameter:

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

### Start a Verification with a specific template

start-a-verification-with-a-specific-template page anchor

Positive FeedbackNegative Feedback

To send a verification with a specified template, [include the `TemplateSid` (starts with HJ) as a parameter.](/docs/verify/api/verification#start-a-new-verification-with-a-pre-defined-template)

Start a Verification with a templateLink to code sample: Start a Verification with a template

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