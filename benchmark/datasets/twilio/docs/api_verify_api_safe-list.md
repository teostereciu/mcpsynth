# Safe List

*Source: https://www.twilio.com/docs/verify/api/safe-list*

---

# Safe List

Positive FeedbackNegative Feedback

* * *

(information)

## Pilot feature

This Verify feature is available as Pilot.

Verify customers who have turned on [Fraud Guard](/docs/verify/preventing-toll-fraud/sms-fraud-guard "Fraud Guard") can access the Safe List API. Fraud Guard is GA and all Verify customers can use it at no extra cost.

If you don't use Fraud Guard and want to use this API, [contact sales(link takes you to an external page)](https://www.twilio.com/en-us/help/sales "contact sales").

**Note** : Safe List API currently only supports the **SMS** channel.

Safe List API allows you to maintain a list of phone numbers that neither Verify [Fraud Guard](/docs/verify/preventing-toll-fraud/sms-fraud-guard "Fraud Guard") nor [Geo permissions](/docs/verify/preventing-toll-fraud/verify-geo-permissions "Geo permissions") block. While Twilio adapts its fraud detection model to minimize false positives, Safe List API lets you mark phone numbers as safe so they never get blocked.

This API contains three endpoints:

  1. [Add a Phone Number](/docs/verify/api/safe-list#add-a-phone-number "Add a Phone Number")
  2. [Check a Phone Number](/docs/verify/api/safe-list#check-a-phone-number "Check a Phone Number")
  3. [Remove a Phone Number](/docs/verify/api/safe-list#remove-a-phone-number "Remove a Phone Number")


Using [Verify Logs Blocked Verifications(link takes you to an external page)](https://console.twilio.com/us1/monitor/logs/verify-fraud-logs "Verify Logs Blocked Verifications") in the Twilio Console, you can add a previously blocked phone number to the Safe List. To learn more about this feature, see [Viewing Logs With Twilio Console](/docs/verify/viewing-logs-with-twilio-console "Viewing Logs With Twilio Console").

* * *

## Rate limits

rate-limits page anchor

Positive FeedbackNegative Feedback

Safe List API provides a built-in rate limit of 30 requests per minute. If you reach this limit, you will start receiving HTTP 429 "Too Many Requests" responses.

* * *

## Timeouts

timeouts page anchor

Positive FeedbackNegative Feedback

Safe List API has a timeout value of 15 seconds. However, its 99th percentile is within one second.

* * *

## Safe List Response Properties

safe-list-response-properties page anchor

Positive FeedbackNegative Feedback

The JSON response output returns these properties.

(information)

## Identifier capitalization conventions

The capitalization of the multiple-word identifiers in the parameter and property lists changes to match the [selected language's conventions(link takes you to an external page)](https://en.wikipedia.org/wiki/Naming_convention_\(programming\)#Language-specific_conventions "selected language's conventions").

Property nameTypeRequiredPIIDescriptionChild properties

sidSID<GN>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique string that we created to identify the SafeList resource.

Pattern: `^GN[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

phoneNumberstring

Optional

[PII MTL: 0 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The phone number in SafeList.

* * *

urlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The absolute URL of the SafeList resource.

* * *

## Add a Phone Number

add-a-phone-number page anchor

Positive FeedbackNegative Feedback

`POST https://verify.twilio.com/v2/SafeList/Numbers`

Adds a single phone number to the Safe List based on the provided `phone_number` parameter. Provide phone numbers in [E.164 format](/docs/glossary/what-e164 "E.164 format").

If you attempt to add a number that exists in the Safe List, the API returns a HTTP 400 status with [Error Code 60411](/docs/api/errors/60411 "Error Code 60411"). Phone numbers remain in the Safe List until explicitly removed.

### Request body parameters

request-body-parameters page anchor

Positive FeedbackNegative Feedback

Encoding type:`application/x-www-form-urlencoded`

SchemaExample

Property nameTypeRequiredPIIDescriptionChild properties

phoneNumberstring

required

[PII MTL: 0 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The phone number to be added in SafeList. Phone numbers must be in [E.164 format](/docs/glossary/what-e164 "E.164 format").

Copy code block


    {


      "PhoneNumber": "+18001234567"


    }

Add a Phone Number to the Safe ListLink to code sample: Add a Phone Number to the Safe List

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

    async function createSafelist() {


    11

      const safelist = await client.verify.v2.safelist.create({


    12

        phoneNumber: "+18001234567",


    13

      });


    14




    15

      console.log(safelist.sid);


    16

    }


    17




    18

    createSafelist();

### Response

Note about this response

Copy response


    1

    {


    2

      "sid": "GNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "phone_number": "+18001234567",


    4

      "url": "https://verify.twilio.com/v2/SafeList/Numbers/+18001234567"


    5

    }

* * *

## Check a Phone Number

check-a-phone-number page anchor

Positive FeedbackNegative Feedback

`GET https://verify.twilio.com/v2/SafeList/Numbers/{PhoneNumber}`

Checks if the provided `phone_number` parameter value exists in the Safe List. Provide phone numbers in [E.164 format](/docs/glossary/what-e164 "E.164 format").

If the provided phone number isn't in the Safe List, the API returns a HTTP 404 status.

### Path parameters

path-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

phoneNumberstring

required

[PII MTL: 0 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The phone number to be fetched from SafeList. Phone numbers must be in [E.164 format](/docs/glossary/what-e164 "E.164 format").

Check if a Phone Number is in the Safe ListLink to code sample: Check if a Phone Number is in the Safe List

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

    async function fetchSafelist() {


    11

      const safelist = await client.verify.v2.safelist("+18001234567").fetch();


    12




    13

      console.log(safelist.sid);


    14

    }


    15




    16

    fetchSafelist();

### Response

Note about this response

Copy response


    1

    {


    2

      "sid": "GNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "phone_number": "+18001234567",


    4

      "url": "https://verify.twilio.com/v2/SafeList/Numbers/+18001234567"


    5

    }

* * *

## Remove a Phone Number

remove-a-phone-number page anchor

Positive FeedbackNegative Feedback

`DELETE https://verify.twilio.com/v2/SafeList/Numbers/{PhoneNumber}`

Removes the provided `phone_number` parameter value exists in the Safe List. Provide phone numbers in [E.164 format](/docs/glossary/what-e164 "E.164 format").

If the provided phone number isn't in the Safe List, the API returns a HTTP 404 status.

### Path parameters

path-parameters-1 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

phoneNumberstring

required

[PII MTL: 0 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The phone number to be removed from SafeList. Phone numbers must be in [E.164 format](/docs/glossary/what-e164 "E.164 format").

Remove a Phone Number from the Safe ListLink to code sample: Remove a Phone Number from the Safe List

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

    async function deleteSafelist() {


    11

      await client.verify.v2.safelist("+18001234567").remove();


    12

    }


    13




    14

    deleteSafelist();