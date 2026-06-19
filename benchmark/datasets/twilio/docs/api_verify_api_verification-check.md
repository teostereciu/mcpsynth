# Verification Check

*Source: https://www.twilio.com/docs/verify/api/verification-check*

---

# Verification Check

Positive FeedbackNegative Feedback

* * *

Use the VerificationCheck resource to validate that the user-provided token is correct.

**Prerequisites** :

  1. [Create a Verification Service](/docs/verify/api/service "Create a Verification Service")
  2. [Start a Verification](/docs/verify/api/verification "Start a Verification")


* * *

## VerificationCheck Response Properties

verificationcheck-response-properties page anchor

Positive FeedbackNegative Feedback

These fields are returned in the output JSON response. The type `SID<VE>` is a unique ID starting with the letters VE.

Property nameTypeRequiredPIIDescriptionChild properties

sidSID<VE>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique string that we created to identify the VerificationCheck resource.

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

The SID of the [Account](/docs/iam/api/account "Account") that created the VerificationCheck resource.

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

The verification method to use. One of: [`email`](/docs/verify/email), `sms`, `whatsapp`, `call`, or `sna`.

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

dateCreatedstring<date-time>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The [ISO 8601(link takes you to an external page)](https://en.wikipedia.org/wiki/ISO_8601 "ISO 8601") date and time in GMT when the Verification Check resource was created.

* * *

dateUpdatedstring<date-time>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The [ISO 8601(link takes you to an external page)](https://en.wikipedia.org/wiki/ISO_8601 "ISO 8601") date and time in GMT when the Verification Check resource was last updated.

* * *

snaAttemptsErrorCodesarray

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

List of error codes as a result of attempting a verification using the `sna` channel. The error codes are chronologically ordered, from the first attempt to the latest attempt. This will be an empty list if no errors occured or `null` if the last channel used wasn't `sna`.

* * *

## Check a Verification

check-a-verification page anchor

Positive FeedbackNegative Feedback

`POST https://verify.twilio.com/v2/Services/{ServiceSid}/VerificationCheck`

(warning)

## Warning

Twilio deletes the verification SID once it's:

  * expired (after 10 minutes)
  * approved
  * max check attempts reached


If any of these events occur, the VerificationCheck request returns a `404 Not Found` error similar to the following example:

Copy code block


    Unable to create record: The requested resource /Services/VAXXXXXXXXXXXXX/VerificationCheck was not found

To review what happened to a specific verification, use the [Verify Logs in the Twilio Console(link takes you to an external page)](https://console.twilio.com/us1/monitor/logs/verify-logs "Verify Logs in the Twilio Console").

You can pass the following input parameters. A `SID<VE>` value is a unique ID that starts with VE.

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

codestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The 4-10 character string being verified.

* * *

tostring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The phone number or [email](/docs/verify/email "email") to verify. Either this parameter or the `verification_sid` must be specified. Phone numbers must be in [E.164 format](/docs/glossary/what-e164 "E.164 format").

* * *

verificationSidSID<VE>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A SID that uniquely identifies the Verification Check. Either this parameter or the `to` phone number/[email](/docs/verify/email "email") must be specified.

Pattern: `^VE[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

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

snaClientTokenstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A sna client token received in sna url invocation response needs to be passed in Verification Check request and should match to get successful response.

Select from available examples

Copy code block


    {


      "To": "+15017122661",


      "VerificationSid": "VEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


      "Code": "1234",


      "Amount": "€39.99",


      "Payee": "Acme Inc."


    }

Check a Verification with a Phone NumberLink to code sample: Check a Verification with a Phone Number

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

          code: "1234",


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

Check a Verification with an EmailLink to code sample: Check a Verification with an Email

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

          to: "recipient@foo.com",


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

      "to": "recipient@foo.com",


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

Check a Verification with a SIDLink to code sample: Check a Verification with a SID

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

          code: "1234",


    15

          verificationSid: "VEXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


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

Check a Silent Network Auth Verification with Error CodesLink to code sample: Check a Silent Network Auth Verification with Error Codes

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

        .verificationChecks.create({ to: "+15017122661" });


    14




    15

      console.log(verificationCheck.sid);


    16

    }


    17




    18

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

An SNA VerificationCheck can display a `status` value of `approved` while still listing error codes in `sna_attempts_error_codes`. This situation occurs when an earlier SNA verification attempt fails and produces an error code, but a later attempt succeeds and approves the verification.