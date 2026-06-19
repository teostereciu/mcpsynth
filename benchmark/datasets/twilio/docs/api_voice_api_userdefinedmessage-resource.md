# UserDefinedMessages subresource

*Source: https://www.twilio.com/docs/voice/api/userdefinedmessage-resource*

---

# UserDefinedMessages subresource

Positive FeedbackNegative Feedback

* * *

(information)

## Info

See the [Voice SDK Call Message Events page](/docs/voice/sdks/call-message-events "Voice SDK Call Message Events page") for more information.

UserDefinedMessages is a subresource of [Calls](/docs/voice/api/call-resource "Calls") and represents a user-defined message that is sent to a Voice SDK end user during an active call.

A UserDefinedMessage subresource can only be created during an active call associated with the Voice SDK.

Read more about the Voice SDK messaging feature on the [Voice SDK Call Message Events Page](/docs/voice/sdks/call-message-events "Voice SDK Call Message Events Page").

* * *

## UserDefinedMessages properties

userdefinedmessages-properties page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescriptionChild properties

accountSidSID<AC>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that created User Defined Message.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

callSidSID<CA>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Call](/docs/voice/api/call-resource "Call") the User Defined Message is associated with.

Pattern: `^CA[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

sidSID<KX>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID that uniquely identifies this User Defined Message.

Pattern: `^KX[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

dateCreatedstring<date-time-rfc-2822>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date that this User Defined Message was created, given in RFC 2822 format.

* * *

## Create a UserDefinedMessage

create-a-userdefinedmessage page anchor

Positive FeedbackNegative Feedback

`POST https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/UserDefinedMessages.json`

### Path parameters

path-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

accountSidSID<AC>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that created User Defined Message.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

callSidSID<CA>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Call](/docs/voice/api/call-resource "Call") the User Defined Message is associated with.

Pattern: `^CA[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

### Request body parameters

request-body-parameters page anchor

Positive FeedbackNegative Feedback

Encoding type:`application/x-www-form-urlencoded`

SchemaExample

Property nameTypeRequiredPIIDescriptionChild properties

contentstring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The User Defined Message in the form of URL-encoded JSON string.

* * *

idempotencyKeystring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A unique string value to identify API call. This should be a unique string value per API call and can be a randomly generated.

Copy code block


    {


      "Content": "{\"key\":\"value\"}",


      "IdempotencyKey": "1"


    }

Send a message from the server side to the Voice SDK by making a `POST` request to an active Call's UserDefinedMessages endpoint.

The content of your message is contained in the `Content` parameter of your request as a stringified JSON object.

Use the appropriate Call SID in the path of your `POST` request. Use the parent Call SID if you wish to send a message to parent Call leg. Use the child Call SID if you wish to send a message to the child Call leg.

See the [Voice SDK Overview page](/docs/voice/sdks#call-legs-with-voice-sdk-calls "Voice SDK Overview page") for more information on Voice SDK Call legs.

Send a UserDefinedMessage to an SDK end-userLink to code sample: Send a UserDefinedMessage to an SDK end-user

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

    async function createUserDefinedMessage() {


    11

      const userDefinedMessage = await client


    12

        .calls("CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .userDefinedMessages.create({


    14

          content: JSON.stringify({ example_key: "Hello from the server side!" }),


    15

        });


    16




    17

      console.log(userDefinedMessage.accountSid);


    18

    }


    19




    20

    createUserDefinedMessage();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "call_sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "sid": "KXaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

      "date_created": "Wed, 18 Dec 2019 20:02:01 +0000"


    6

    }

* * *

## Related resources

related-resources page anchor

Positive FeedbackNegative Feedback

Go to the [Voice SDK Call Message Events page](/docs/voice/sdks/call-message-events "Voice SDK Call Message Events page") to learn more.