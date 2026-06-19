# Customization Options

*Source: https://www.twilio.com/docs/verify/api/customization-options*

---

# Customization Options

Positive FeedbackNegative Feedback

* * *

**Prerequisites:**

  1. [Create a Verification Service](/docs/verify/api/service "Create a Verification Service")
  2. For an existing Service, you can enable [Custom Verification Code](/docs/verify/api/customization-options#custom-verification-codes "Custom Verification Code") in the Twilio Console by navigating to [**Verify > Services**(link takes you to an external page)](https://console.twilio.com/us1/develop/verify/services) and selecting your Service. This will open the **Service settings** page where you can select the **General tab** and select the **Enable Custom Verification Code** option for that Service. Once it is enabled on your Service, you can follow the [steps](/docs/verify/api/customization-options#custom-verification-codes "steps") listed below to submit custom verification codes.
  3. [Contact Twilio Sales(link takes you to an external page)](https://www.twilio.com/en-us/help/sales "Contact Twilio Sales") and we'll help you enable the [Custom Company Name](/docs/verify/api/customization-options#custom-company-name "Custom Company Name") option.


* * *

## Custom Verification Codes

custom-verification-codes page anchor

Positive FeedbackNegative Feedback

If you already have token generation and validation logic and would like to keep those systems in place, you can do so. We have a feature where you can submit your code to us and utilize our pre-screened message templates and localizations for both text and voice.

Please ensure that you have selected **Enable Custom Verification Code** option on the Twilio Console on your Verify service before submitting custom verification codes.

If you're using custom verification codes you must also [provide feedback](/docs/verify/api/verification#update-a-verification-status "provide feedback") that lets us know whether or not the user verified the code. This allows us to proactively monitor our global routing and stay operational.

Start a Verification with Custom CodeLink to code sample: Start a Verification with Custom Code

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

          customCode: "867530",


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

Submit Feedback by Manually Approving a VerificationLink to code sample: Submit Feedback by Manually Approving a Verification

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

      console.log(verification.sid);


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

* * *

## Custom Company Name

custom-company-name page anchor

Positive FeedbackNegative Feedback

By default, the company name that the end user sees in a verification message is set at the service level. You can programmatically override this by setting the `custom_friendly_name` parameter when creating verifications. Custom company names may be useful for Independent Software Vendors (ISVs) who own one Verify Service and need to customize the company name for each verification message.

There is a limit of 30 characters.

Start a Verification with Custom Company NameLink to code sample: Start a Verification with Custom Company Name

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

          customFriendlyName: "Sample Bank - Main Branch",


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