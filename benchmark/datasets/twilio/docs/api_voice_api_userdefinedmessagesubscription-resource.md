# UserDefinedMessageSubscriptions subresource

*Source: https://www.twilio.com/docs/voice/api/userdefinedmessagesubscription-resource*

---

# UserDefinedMessageSubscriptions subresource

Positive FeedbackNegative Feedback

* * *

(information)

## Info

This feature is in Public Beta.

See the [Voice SDK Call Message Events page](/docs/voice/sdks/call-message-events "Voice SDK Call Message Events page") for more information.

UserDefinedMessageSubscriptions is a subresource of [Calls](/docs/voice/api/call-resource "Calls") and represents a subscription to user-defined messages sent from the Voice SDK. You must create a UserDefinedMessageSubscriptions subresource in order to receive messages from the Voice SDK.

A UserDefinedMessageSubscription subresource can only be created during an active Call associated with the Voice SDK.

Your Voice SDK application must be configured to send messages. Read more about sending and receiving Voice SDK messages on the [Voice SDK Call Message Events page](/docs/voice/sdks/call-message-events "Voice SDK Call Message Events page").

* * *

## UserDefinedMessageSubscription Properties

userdefinedmessagesubscription-properties page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescriptionChild properties

accountSidSID<AC>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that subscribed to the User Defined Messages.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

callSidSID<CA>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Call](/docs/voice/api/call-resource "Call") the User Defined Message Subscription is associated with. This refers to the Call SID that is producing the User Defined Messages.

Pattern: `^CA[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

sidSID<ZY>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID that uniquely identifies this User Defined Message Subscription.

Pattern: `^ZY[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

dateCreatedstring<date-time-rfc-2822>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date that this User Defined Message Subscription was created, given in RFC 2822 format.

* * *

uristring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URI of the User Defined Message Subscription Resource, relative to `https://api.twilio.com`.

* * *

## Create a UserDefinedMessageSubscription

create-a-userdefinedmessagesubscription page anchor

Positive FeedbackNegative Feedback

`POST https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/UserDefinedMessageSubscriptions.json`

You need to subscribe to a Call's user-defined messages in order to receive messages from the Voice SDK. You do this by creating a UserDefinedMessageSubscription subresource for that Call SID.

You must have an endpoint that can handle `POST` or `GET` requests with a `Content-Type` of `application/json`. You specify this endpoint in the `Callback` parameter when creating your UserDefinedMessageSubscription, and this is where Twilio will send requests containing the messages from the Voice SDK.

Use the appropriate Call SID in the path of your `POST` request. Use the parent Call SID if you wish to send a message to parent Call leg. Use the child Call SID if you wish to send a message to the child Call leg.

See the [Voice SDK Overview page](/docs/voice/sdks#call-legs-with-voice-sdk-calls "Voice SDK Overview page") for more information on Voice SDK Call legs.

### Path parameters

path-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

accountSidSID<AC>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that subscribed to the User Defined Messages.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

callSidSID<CA>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Call](/docs/voice/api/call-resource "Call") the User Defined Messages subscription is associated with. This refers to the Call SID that is producing the user defined messages.

Pattern: `^CA[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

### Request body parameters

request-body-parameters page anchor

Positive FeedbackNegative Feedback

Encoding type:`application/x-www-form-urlencoded`

SchemaExample

Property nameTypeRequiredPIIDescriptionChild properties

callbackstring<uri>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL we should call using the `method` to send user defined events to your application. URLs must contain a valid hostname (underscores are not permitted).

* * *

idempotencyKeystring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A unique string value to identify API call. This should be a unique string value per API call and can be a randomly generated.

* * *

methodenum<http-method>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The HTTP method Twilio will use when requesting the above `Url`. Either `GET` or `POST`. Default is `POST`.

Possible values:

`GET``POST`

Copy code block


    {


      "Callback": "http://www.example.com",


      "Method": "POST",


      "IdempotencyKey": "1"


    }

Create a UserDefinedMessageSubscription to receive user-defined messages from the Voice SDKLink to code sample: Create a UserDefinedMessageSubscription to receive user-defined messages from the Voice SDK

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

    async function createUserDefinedMessageSubscription() {


    11

      const userDefinedMessageSubscription = await client


    12

        .calls("CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .userDefinedMessageSubscriptions.create({


    14

          callback:


    15

            "https://www.example.com/your-endpoint-that-can-receive-messages",


    16

        });


    17




    18

      console.log(userDefinedMessageSubscription.accountSid);


    19

    }


    20




    21

    createUserDefinedMessageSubscription();

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

      "sid": "ZYaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

      "date_created": "Wed, 18 Dec 2019 20:02:01 +0000",


    6

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/UserDefinedMessageSubscriptions/ZYaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"


    7

    }

* * *

## Related resources

related-resources page anchor

Positive FeedbackNegative Feedback

Go to the [Voice SDK Call Message Events page](/docs/voice/sdks/call-message-events "Voice SDK Call Message Events page") to learn more.