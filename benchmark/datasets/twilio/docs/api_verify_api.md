# Verify API

*Source: https://www.twilio.com/docs/verify/api*

---

# Verify API

Positive FeedbackNegative Feedback

* * *

As part of Twilio's account security offerings, the Twilio Verify API enables you to add user verification to your web application. The API supports the following channels:

  * SMS
  * [Passkeys](/docs/verify/passkeys "Passkeys")
  * [Silent Network Auth](/docs/verify/sna "Silent Network Auth")
  * [Automatic Channel Selection](/docs/verify/automatic-channel-selection "Automatic Channel Selection")
  * Voice
  * [WhatsApp](/docs/verify/whatsapp "WhatsApp")
  * [Email](/docs/verify/email "Email")
  * [TOTP](/docs/verify/quickstarts/totp "TOTP") (authenticator apps such as Authy or Google Authenticator)
  * [Push and Silent Device Approval](/docs/verify/push "Push and Silent Device Approval")


For more information on Verify, see the [Twilio Verify product page(link takes you to an external page)](https://www.twilio.com/en-us/trusted-activation/verify "Twilio Verify product page").

* * *

## Base URL

base-url page anchor

Positive FeedbackNegative Feedback

All URLs in this documentation use the following base URL:

Copy code block


    https://verify.twilio.com/v2/

The Twilio REST API is served over HTTPS. To ensure data privacy, unencrypted HTTP is not supported.

* * *

## Authentication

authentication page anchor

Positive FeedbackNegative Feedback

To authenticate requests to the Twilio APIs, Twilio supports [HTTP Basic authentication(link takes you to an external page)](https://en.wikipedia.org/wiki/Basic_access_authentication "HTTP Basic authentication"). Use your _API key_ as the username and your _API key secret_ as the password. You can create an API key either [in the Twilio Console](/docs/iam/api-keys/keys-in-console "in the Twilio Console") or [using the API](/docs/iam/api-keys/key-resource-v1 "using the API").

**Note** : Twilio recommends using API keys for authentication in production apps. For local testing, you can use your Account SID as the username and your Auth token as the password. You can find your Account SID and Auth Token in the [Twilio Console(link takes you to an external page)](https://www.twilio.com/console "Twilio Console").

Learn more about [Twilio API authentication](/docs/usage/requests-to-twilio "Twilio API authentication").

Copy code block


    1

    curl -X POST https://verify.twilio.com/v2/Services \


    2

        -d FriendlyName=MyServiceName \


    3

        -u $TWILIO_API_KEY:$TWILIO_API_KEY_SECRET

* * *

## User verification workflow

user-verification-workflow page anchor

Positive FeedbackNegative Feedback

This section shows the 3 steps required to complete a basic one-time passcode (OTP) verification. Follow the links for more documentation on advanced features such as [service configuration](/docs/verify/api/service "service configuration"), [custom codes](/docs/verify/api/customization-options "custom codes"), [rate limiting](/docs/verify/api/programmable-rate-limits "rate limiting"), [PSD2 compliance](/docs/verify/verifying-transactions-psd2 "PSD2 compliance"), and more.

Step 1: Create a Verification ServiceLink to code sample: Step 1: Create a Verification Service

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

        friendlyName: "My First Verify Service",


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

      "friendly_name": "My First Verify Service",


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

Create a Verification Service in one of two ways:

  1. In the [Twilio Verify Console(link takes you to an external page)](https://www.twilio.com/console/verify/services "Twilio Verify Console")
  2. By using the [Verify API](/docs/verify/api/service "Verify API")


A Verification Service is the set of common configurations used to create and check verifications. This includes features like:

  * Friendly name (used in the verification message templates, except in countries with [brand restrictions(link takes you to an external page)](https://help.twilio.com/hc/en-us/articles/12387480513307-Why-was-my-friendly-name-not-included-in-the-Verify-SMS- "brand restrictions"))
  * Code length
  * Other service-level options


One verification service can be used to send multiple verification tokens, it is not necessary to create a new service each time.

Step 2: Send a verification tokenLink to code sample: Step 2: Send a verification token

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

      console.log(verification.status);


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

This request sends a token to the end user through the specified channel. Newly created verifications have a status of `pending`. Supported channels are:

  * `sms`, see the [Verify SMS Overview](/docs/verify/sms "Verify SMS Overview")
  * `call`
  * `email`, see [Send Email Verifications with Verify and Twilio SendGrid](/docs/verify/email "Send Email Verifications with Verify and Twilio SendGrid")
  * `whatsapp`, see the [Verify WhatsApp overview](/docs/verify/whatsapp "Verify WhatsApp overview")


Learn more about how to turn [phone number input into E.164 format(link takes you to an external page)](https://www.twilio.com/blog/international-phone-number-input-html-javascript "phone number input into E.164 format") or how to [customize the verification message](/docs/verify/api/templates "customize the verification message").

For additional parameters, see the [Verification API](/docs/verify/api/verification "Verification API") reference.

Step 3: Check the verification tokenLink to code sample: Step 3: Check the verification token

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

    async function createVerificationCheck() {


    11

      const verificationCheck = await client.verify.v2


    12

        .services("VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .verificationChecks.create({


    14

          code: "123456",


    15

          to: "+15017122661",


    16

        });


    17




    18

      console.log(verificationCheck.status);


    19

    }


    20




    21

    createVerificationCheck();

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

      "status": "approved",


    8

      "valid": true,


    9

      "amount": null,


    10

      "payee": null,


    11

      "sna_attempts_error_codes": [],


    12

      "date_created": "2015-07-30T20:00:00Z",


    13

      "date_updated": "2015-07-30T20:00:00Z"


    14

    }

This request checks whether the user-provided token is correct.

**Token**| **Status in response**
---|---
Correct| `approved`
Incorrect| `pending`

See the [VerificationCheck API](/docs/verify/api/verification-check "VerificationCheck API") reference.

(information)

## Info

You made it through the Verify API Overview. To protect your service against fraud, view our guidance on [Preventing Toll Fraud](/docs/verify/preventing-toll-fraud "Preventing Toll Fraud") when using Verify.