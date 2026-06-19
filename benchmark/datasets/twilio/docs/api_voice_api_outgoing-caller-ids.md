# OutgoingCallerIds resource

*Source: https://www.twilio.com/docs/voice/api/outgoing-caller-ids*

---

# OutgoingCallerIds resource

Positive FeedbackNegative Feedback

* * *

The OutgoingCallerIds resource represents the set of verified phone numbers for an account. Each OutgoingCallerId represents a single verified number that you can use as a caller ID when making outgoing calls, either [via the REST API](/docs/voice/tutorials/how-to-make-outbound-phone-calls "via the REST API") or within the [TwiML <Dial> verb](/docs/voice/twiml/dial "TwiML <Dial> verb").

* * *

## OutgoingCallerIds properties

outgoingcallerids-properties page anchor

Positive FeedbackNegative Feedback

Property| Description
---|---
Sid| A 34 character string that uniquely identifies this resource.
DateCreated| The date that this resource was created, given in [RFC 2822(link takes you to an external page)](https://www.ietf.org/rfc/rfc2822.txt "RFC 2822") format.
DateUpdated| The date that this resource was last updated, given in [RFC 2822(link takes you to an external page)](https://www.ietf.org/rfc/rfc2822.txt "RFC 2822") format.
FriendlyName| A human-readable descriptive text for this resource, up to 64 characters long. By default, the `FriendlyName` is a nicely formatted version of the phone number.
AccountSid| The unique ID of the [Account](/docs/iam/api/account "Account") responsible for this Caller ID.
PhoneNumber| The incoming phone number. Formatted with a '+' and country code for example, +16175551212 ([E.164(link takes you to an external page)](https://en.wikipedia.org/wiki/E.164 "E.164") format).
Uri| The URI for this resource, relative to `https://api.twilio.com`.

* * *

## Retrieve an OutgoingCallerId

retrieve-an-outgoingcallerid page anchor

Positive FeedbackNegative Feedback

Retrieve an OutgoingCallerIdLink to code sample: Retrieve an OutgoingCallerId

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

    async function fetchOutgoingCallerId() {


    11

      const outgoingCallerId = await client


    12

        .outgoingCallerIds("PNe905d7e6b410746a0fb08c57e5a186f3")


    13

        .fetch();


    14




    15

      console.log(outgoingCallerId.sid);


    16

    }


    17




    18

    fetchOutgoingCallerId();

### Response

Note about this response

Copy response


    1

    {


    2

      "sid": "PNe905d7e6b410746a0fb08c57e5a186f3",


    3

      "account_sid": "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    4

      "friendly_name": "(415) 867-5309",


    5

      "phone_number": "+141586753096",


    6

      "date_created": "Fri, 21 Aug 2009 00:11:24 +0000",


    7

      "date_updated": "Fri, 21 Aug 2009 00:11:24 +0000",


    8

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/OutgoingCallerIds/PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"


    9

    }

* * *

## Update an OutgoingCallerId

update-an-outgoingcallerid page anchor

Positive FeedbackNegative Feedback

Updates the caller ID and returns the updated resource if successful.

### Optional parameters

optional-parameters page anchor

Positive FeedbackNegative Feedback

You can update only one field:

Parameter| Description
---|---
FriendlyName| A human readable description of a Caller ID, with maximum length of 64 characters. Defaults to a nicely formatted version of the phone number.

Update Outgoing Caller IDLink to code sample: Update Outgoing Caller ID

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

    async function updateOutgoingCallerId() {


    11

      const outgoingCallerId = await client


    12

        .outgoingCallerIds("PNe536d32a3c49700934481addd5ce1659")


    13

        .update({ friendlyName: "My Second Line" });


    14




    15

      console.log(outgoingCallerId.sid);


    16

    }


    17




    18

    updateOutgoingCallerId();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    3

      "date_created": "Fri, 21 Aug 2009 00:11:24 +0000",


    4

      "date_updated": "Fri, 21 Aug 2009 00:11:24 +0000",


    5

      "friendly_name": "My Second Line",


    6

      "phone_number": "+141586753096",


    7

      "sid": "PNe536d32a3c49700934481addd5ce1659",


    8

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/OutgoingCallerIds/PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"


    9

    }

The response format is identical to the [HTTP `GET` response](/docs/voice/api/outgoing-caller-ids) documented above.

* * *

## Delete an OutgoingCallerId

delete-an-outgoingcallerid page anchor

Positive FeedbackNegative Feedback

Deletes the caller ID from the account. Returns an HTTP 204 response if successful, with no body.

Delete Outgoing Caller IDLink to code sample: Delete Outgoing Caller ID

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

    async function deleteOutgoingCallerId() {


    11

      await client.outgoingCallerIds("PNe536d32a3c49700934481addd5ce1659").remove();


    12

    }


    13




    14

    deleteOutgoingCallerId();

* * *

## Retrieve a list of OutgoingCallerIds

retrieve-a-list-of-outgoingcallerids page anchor

Positive FeedbackNegative Feedback

Returns a list of OutgoingCallerIds, each representing a caller ID phone number that is valid for the account. The list includes [paging information](/docs/usage/twilios-response "paging information").

### Filters

filters page anchor

Positive FeedbackNegative Feedback

The following `GET` query string parameters allow you to limit the list returned. Parameters are case-sensitive:

Parameter| Description
---|---
PhoneNumber| Only show the OutgoingCallerId that exactly matches this phone number.
FriendlyName| Only show the OutgoingCallerId that exactly matches this name.

Retrieve a list of OutgoingCallerIds for an accountLink to code sample: Retrieve a list of OutgoingCallerIds for an account

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

    async function listOutgoingCallerId() {


    11

      const outgoingCallerIds = await client.outgoingCallerIds.list({ limit: 20 });


    12




    13

      outgoingCallerIds.forEach((o) => console.log(o.sid));


    14

    }


    15




    16

    listOutgoingCallerId();

### Response

Note about this response

Copy response


    1

    {


    2

      "end": 0,


    3

      "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/OutgoingCallerIds.json?PageSize=50&Page=0",


    4

      "next_page_uri": null,


    5

      "outgoing_caller_ids": [


    6

        {


    7

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    8

          "date_created": "Fri, 21 Aug 2009 00:11:24 +0000",


    9

          "date_updated": "Fri, 21 Aug 2009 00:11:24 +0000",


    10

          "friendly_name": "(415) 867-5309",


    11

          "phone_number": "+141586753096",


    12

          "sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    13

          "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/OutgoingCallerIds/PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"


    14

        }


    15

      ],


    16

      "page": 0,


    17

      "page_size": 50,


    18

      "previous_page_uri": null,


    19

      "start": 0,


    20

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/OutgoingCallerIds.json?PageSize=50&Page=0"


    21

    }

Retrieve a list of OutgoingCallerIds for a phone numberLink to code sample: Retrieve a list of OutgoingCallerIds for a phone number

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

    async function listOutgoingCallerId() {


    11

      const outgoingCallerIds = await client.outgoingCallerIds.list({


    12

        phoneNumber: "+14158675310",


    13

        limit: 20,


    14

      });


    15




    16

      outgoingCallerIds.forEach((o) => console.log(o.sid));


    17

    }


    18




    19

    listOutgoingCallerId();

### Response

Note about this response

Copy response


    1

    {


    2

      "end": 0,


    3

      "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/OutgoingCallerIds.json?PageSize=50&Page=0",


    4

      "next_page_uri": null,


    5

      "outgoing_caller_ids": [


    6

        {


    7

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    8

          "date_created": "Fri, 21 Aug 2009 00:11:24 +0000",


    9

          "date_updated": "Fri, 21 Aug 2009 00:11:24 +0000",


    10

          "friendly_name": "(415) 867-5309",


    11

          "phone_number": "+141586753096",


    12

          "sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    13

          "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/OutgoingCallerIds/PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"


    14

        }


    15

      ],


    16

      "page": 0,


    17

      "page_size": 50,


    18

      "previous_page_uri": null,


    19

      "start": 0,


    20

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/OutgoingCallerIds.json?PageSize=50&Page=0"


    21

    }

* * *

## Add an OutgoingCallerId to your account

add-an-outgoingcallerid-to-your-account page anchor

Positive FeedbackNegative Feedback

Adds an OutgoingCallerId to your account. If the request is successful, the response contains a validation code.

After you make this request, Twilio places a verification call to the provided phone number. To finish adding the OutgoingCallerId, the person who answers the call must enter the validation code. To learn more, see [Verifying Caller IDs at Scale](/docs/voice/api/verifying-caller-ids-scale "Verifying Caller IDs at Scale").

(information)

## Info

The verification call is in English. Other languages aren't supported.

The following parameters are accepted:

### Required parameters

required-parameters page anchor

Positive FeedbackNegative Feedback

Parameter| Description
---|---
PhoneNumber| The phone number to verify. Should be formatted with a '+' and country code for example, +16175551212 ([E.164(link takes you to an external page)](https://en.wikipedia.org/wiki/E.164 "E.164") format). Twilio will also accept unformatted US numbers for example, (415) 555-1212 or 415-555-1212.

### Optional parameters

optional-parameters-1 page anchor

Positive FeedbackNegative Feedback

Parameter| Description
---|---
FriendlyName| A human readable description for the new caller ID with maximum length 64 characters. Defaults to a nicely formatted version of the number.
CallDelay| The number of seconds, between 0 and 60, to delay before initiating the verification call. Defaults to 0.
Extension| Digits to dial after connecting the verification call.
StatusCallback| A URL that Twilio will request when the verification call ends to notify your app if the verification process was successful or not. See [StatusCallback parameter](/docs/voice/api/outgoing-caller-ids#statuscallback-parameter "StatusCallback parameter") below. **Note:** The StatusCallback URL is limited to 1,000 characters.
StatusCallbackMethod| The HTTP method Twilio should use when requesting the above URL. Defaults to `POST`.

This will create a new CallerID validation request within Twilio, which initiates a call to the phone number provided and listens for a validation code. The validation request is represented in the response by the following properties:

### Response properties

response-properties page anchor

Positive FeedbackNegative Feedback

Property| Description
---|---
AccountSid| The unique ID of the [Account](/docs/iam/api/account "Account") to which the Validation Request belongs.
PhoneNumber| The incoming phone number being validated, formatted with a '+' and country code e.g., +16175551212 ([E.164(link takes you to an external page)](https://en.wikipedia.org/wiki/E.164 "E.164") format).
FriendlyName| The friendly name you provided, if any.
ValidationCode| The 6-digit validation code that must be entered via the phone to validate this phone number for Caller ID.
CallSid| The unique ID of the [Call](/docs/call "Call") created for this validation attempt.

### StatusCallback parameter

statuscallback-parameter page anchor

Positive FeedbackNegative Feedback

After the verification call ends, Twilio makes an asynchronous HTTP request to the StatusCallback URL if you provided one in your API request. By capturing this request, you can determine when the call ended and whether or not the number called was successfully verified.

Twilio passes the same parameters to your application in its asynchronous request to the StatusCallback URL as it does in a typical status callback request. The full list of parameters and descriptions of each are in the [TwiML Voice: Twilio's Request](/docs/voice/twiml "TwiML Voice: Twilio's Request") documentation.

The verification status callback request also passes these additional parameters:

Parameter| Description
---|---
VerificationStatus| Describes whether or not the person called correctly entered the validation code. Possible values are `success` or `failed`.
OutgoingCallerIdSid| If the verification process was successful, the SID value of the newly-created OutgoingCallerId resource for the verified number.

### Example

example page anchor

Positive FeedbackNegative Feedback

Here are a typical request and response. Typically, you would present the validation code from the response to the user who is trying to verify their phone number. Adding an Outgoing Caller ID via the API has the same result as [verifying a number(link takes you to an external page)](https://www.twilio.com/console/phone-numbers/verified "verifying a number") via the Twilio console.

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

    async function createValidationRequest() {


    11

      const validationRequest = await client.validationRequests.create({


    12

        friendlyName: "My Home Phone Number",


    13

        phoneNumber: "+14158675310",


    14

      });


    15




    16

      console.log(validationRequest.accountSid);


    17

    }


    18




    19

    createValidationRequest();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    3

      "call_sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "friendly_name": "My Home Phone Number",


    5

      "phone_number": "+14158675310",


    6

      "validation_code": "111111"


    7

    }