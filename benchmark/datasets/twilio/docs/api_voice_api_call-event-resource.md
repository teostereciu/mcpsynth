# Events subresource

*Source: https://www.twilio.com/docs/voice/api/call-event-resource*

---

# Events subresource

Positive FeedbackNegative Feedback

* * *

Events is a subresource of [Calls](/docs/voice/api/call-resource "Calls") and shows all the requests Twilio sent to your application and how your application responded for a specific call. You can access the Call Event resource 15 minutes after a call ends.

* * *

## Event Properties

event-properties page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescriptionChild properties

request

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

Contains a dictionary representing the request of the call.

* * *

response

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

Contains a dictionary representing the call response, including a list of the call events.

### `request`

request page anchor

Positive FeedbackNegative Feedback

The `request` property represents the [request that Twilio made to your application](/docs/voice/twiml#twilios-request-to-your-application "request that Twilio made to your application"). It contains the `url`, `method`, and `parameters`.

(information)

## Info

The `parameters` property keys are presented in **snake_case** format, lower cased and words separated by underscores.

For example, the results from your [`AddOns`](/docs/marketplace) will be found under the key `add_ons`.

### `response`

response page anchor

Positive FeedbackNegative Feedback

The `response` property represents what your application sent back to Twilio. It contains `date_created`, `request_duration`, `response_code`, `content_type`, and `response_body`.

You can use this information to ensure you are producing the intended [Voice TwiML](/docs/voice/twiml "Voice TwiML").

* * *

## Retrieve a list of Events

retrieve-a-list-of-events page anchor

Positive FeedbackNegative Feedback

`GET https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/Events.json`

### Path parameters

path-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

accountSidSID<AC>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique SID identifier of the Account.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

callSidSID<CA>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique SID identifier of the Call.

Pattern: `^CA[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

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

List multiple EventsLink to code sample: List multiple Events

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

    async function listCallEvent() {


    11

      const events = await client


    12

        .calls("CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .events.list({ limit: 20 });


    14




    15

      events.forEach((e) => console.log(e.request));


    16

    }


    17




    18

    listCallEvent();

### Response

Note about this response

Copy response


    1

    {


    2

      "events": [


    3

        {


    4

          "request": {


    5

            "method": "POST",


    6

            "url": "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",


    7

            "parameters": {


    8

              "status_callback_method": "POST",


    9

              "twiml": "<Response><Say>Hi!</Say></Response>",


    10

              "trim": "trim-silence",


    11

              "timeout": "55",


    12

              "method": "POST",


    13

              "from": "+987654321",


    14

              "to": "+123456789",


    15

              "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    16

              "machine_detection_timeout": "0"


    17

            }


    18

          },


    19

          "response": {


    20

            "response_code": 201,


    21

            "request_duration": 50,


    22

            "content_type": "application/json",


    23

            "response_body": "{\"sid\": \"CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\"}",


    24

            "date_created": "Tue, 11 Aug 2020 17:44:08 +0000"


    25

          }


    26

        }


    27

      ],


    28

      "end": 0,


    29

      "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Events.json?PageSize=50&Page=0",


    30

      "next_page_uri": null,


    31

      "page": 0,


    32

      "page_size": 50,


    33

      "previous_page_uri": null,


    34

      "start": 0,


    35

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Events.json?PageSize=50&Page=0"


    36

    }