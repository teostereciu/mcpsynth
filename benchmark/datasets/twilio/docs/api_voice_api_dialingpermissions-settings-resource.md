# Dialing Permissions - Settings resource

*Source: https://www.twilio.com/docs/voice/api/dialingpermissions-settings-resource*

---

# Dialing Permissions - Settings resource

Positive FeedbackNegative Feedback

* * *

Represents the subaccount's inheritance settings for voice dialing permissions.

* * *

## DialingPermissions Settings properties

dialingpermissions-settings-properties page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescriptionChild properties

dialingPermissionsInheritanceboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

`true` if the sub-account will inherit voice dialing permissions from the Master Project; otherwise `false`.

* * *

urlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The absolute URL of this resource.

* * *

## Retrieve DialingPermissions Settings

retrieve-dialingpermissions-settings page anchor

Positive FeedbackNegative Feedback

`GET https://voice.twilio.com/v1/Settings`

Retrieve a DialingPermissions Settings resourceLink to code sample: Retrieve a DialingPermissions Settings resource

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

    async function fetchDialingPermissionsSettings() {


    11

      const setting = await client.voice.v1.dialingPermissions.settings().fetch();


    12




    13

      console.log(setting.dialingPermissionsInheritance);


    14

    }


    15




    16

    fetchDialingPermissionsSettings();

### Response

Note about this response

Copy response


    1

    {


    2

      "dialing_permissions_inheritance": true,


    3

      "url": "https://voice.twilio.com/v1/Settings"


    4

    }

* * *

## Update DialingPermissions Settings

update-dialingpermissions-settings page anchor

Positive FeedbackNegative Feedback

`POST https://voice.twilio.com/v1/Settings`

### Request body parameters

request-body-parameters page anchor

Positive FeedbackNegative Feedback

Encoding type:`application/x-www-form-urlencoded`

SchemaExample

Property nameTypeRequiredPIIDescriptionChild properties

dialingPermissionsInheritanceboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

`true` for the sub-account to inherit voice dialing permissions from the Master Project; otherwise `false`.

Copy code block


    {


      "DialingPermissionsInheritance": true


    }

Update a DialingPermissions Settings resourceLink to code sample: Update a DialingPermissions Settings resource

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

    async function updateDialingPermissionsSettings() {


    11

      const setting = await client.voice.v1.dialingPermissions


    12

        .settings()


    13

        .update({ dialingPermissionsInheritance: false });


    14




    15

      console.log(setting.dialingPermissionsInheritance);


    16

    }


    17




    18

    updateDialingPermissionsSettings();

### Response

Note about this response

Copy response


    1

    {


    2

      "dialing_permissions_inheritance": false,


    3

      "url": "https://voice.twilio.com/v1/Settings"


    4

    }