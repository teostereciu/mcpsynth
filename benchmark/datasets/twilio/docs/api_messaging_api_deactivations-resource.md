# Deactivations resource

*Source: https://www.twilio.com/docs/messaging/api/deactivations-resource*

---

# Deactivations resource

Positive FeedbackNegative Feedback

* * *

The Deactivations resource retrieves a list of United States phone numbers that have been deactivated by mobile carriers. These phone numbers are no longer in service for the subscriber who used to own that number. Twilio updates the set of available reports daily.

These reports should be used periodically to remove deactivated phone numbers from your opted-in subscriber list. For more information how to use these reports, see the ["Handling Deactivated Phone Numbers" Help Center article(link takes you to an external page)](https://help.twilio.com/hc/en-us/articles/360042744973-Handling-Deactivated-Phone-Numbers ""Handling Deactivated Phone Numbers" Help Center article").

API requests to the Deactivations resource are free of charge.

* * *

## Deactivation Properties

deactivation-properties page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescriptionChild properties

redirectTostring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Returns an authenticated url that redirects to a file containing the deactivated numbers for the requested day. This url is valid for up to two minutes.

* * *

## Retrieve a list of Deactivations

retrieve-a-list-of-deactivations page anchor

Positive FeedbackNegative Feedback

`GET https://messaging.twilio.com/v1/Deactivations`

Retrieve a list of deactivated numbers for a specific date.

You must include the Date parameter with a date value in `YYYY-MM-DD` format.

Twilio's response contains a `redirect_to` property with a signed URL for the requested date's deactivations list in `.txt` format.

### Query parameters

query-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

datestring<date>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The request will return a list of all United States Phone Numbers that were deactivated on the day specified by this parameter. This date should be specified in YYYY-MM-DD format.

Fetch deactivations for August 13, 2023Link to code sample: Fetch deactivations for August 13, 2023

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

    async function fetchDeactivation() {


    11

      const deactivation = await client.messaging.v1


    12

        .deactivations()


    13

        .fetch({ date: "2023-08-13" });


    14




    15

      console.log(deactivation.redirectTo);


    16

    }


    17




    18

    fetchDeactivation();

### Response

Note about this response

Copy response


    1

    {


    2

      "redirect_to": "https://com-twilio-dev-messaging-deactivations.s3.amazonaws.com"


    3

    }