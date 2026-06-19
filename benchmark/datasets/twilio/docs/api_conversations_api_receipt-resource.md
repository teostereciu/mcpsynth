# Conversation Message Receipt Resource

*Source: https://www.twilio.com/docs/conversations/api/receipt-resource*

---

# Conversation Message Receipt Resource

Positive FeedbackNegative Feedback

* * *

**Delivery Receipts** in Conversations provide visibility into the status of [Conversation Messages](/docs/conversations/api/conversation-message-resource "Conversation Messages") sent across different channels.

Using Delivery Receipts, you can verify that Messages have been sent, delivered, or even read (for OTT) by Conversations Participants.

* * *

## API Base URL

api-base-url page anchor

Positive FeedbackNegative Feedback

All URLs in the reference documentation use the following base URL:

Copy code block


    https://conversations.twilio.com/v1

### Using the shortened base URL

using-the-shortened-base-url page anchor

Positive FeedbackNegative Feedback

Using the REST API, you can interact with Conversation Message Receipt resources in the **default Conversation Service** instance via a "shortened" URL that does not include the Conversation Service instance SID ("ISXXX..."). If you are only using one Conversation Service (the default), you do not need to include the Conversation Service SID in your URL, e.g.

Copy code block


    1

    GET /v1/Conversations/CHxx/Messages/IMXXX/Receipts


    2

For Conversations applications that build on more than one Conversation Service instance, you will need to specify the Conversation Service SID in the REST API call:

Copy code block


    GET /v1/Services/ISxx/Conversations/CHxx/Messages/IMXXX/Receipts

* * *

## Receipt Properties

receipt-properties page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescriptionChild properties

accountSidSID<AC>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique ID of the [Account](/docs/iam/api/account "Account") responsible for this participant.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

conversationSidSID<CH>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique ID of the [Conversation](/docs/conversations/api/conversation-resource "Conversation") for this message.

Pattern: `^CH[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

sidSID<DY>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A 34 character string that uniquely identifies this resource.

Pattern: `^DY[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

messageSidSID<IM>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the message within a [Conversation](/docs/conversations/api/conversation-resource "Conversation") the delivery receipt belongs to

Pattern: `^IM[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

channelMessageSidSID

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A messaging channel-specific identifier for the message delivered to participant e.g. `SMxx` for SMS, `WAxx` for Whatsapp etc.

Pattern: `^[a-zA-Z]{2}[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

participantSidSID<MB>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique ID of the participant the delivery receipt belongs to.

Pattern: `^MB[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

statusenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The message delivery status, can be `read`, `failed`, `delivered`, `undelivered`, `sent` or null.

Possible values:

`read``failed``delivered``undelivered``sent`

* * *

errorCodeinteger

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The message [delivery error code](/docs/sms/api/message-resource#delivery-related-errors "delivery error code") for a `failed` status,

Default: `0`

* * *

dateCreatedstring<date-time>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date that this resource was created.

* * *

dateUpdatedstring<date-time>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date that this resource was last updated. `null` if the delivery receipt has not been updated.

* * *

urlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

An absolute API resource URL for this delivery receipt.

* * *

## Fetch a ConversationMessageReceipt resource

fetch-a-conversationmessagereceipt-resource page anchor

Positive FeedbackNegative Feedback

`GET https://conversations.twilio.com/v1/Conversations/{ConversationSid}/Messages/{MessageSid}/Receipts/{Sid}`

### Path parameters

path-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

conversationSidstring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique ID of the [Conversation](/docs/conversations/api/conversation-resource "Conversation") for this message.

* * *

messageSidSID<IM>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the message within a [Conversation](/docs/conversations/api/conversation-resource "Conversation") the delivery receipt belongs to.

Pattern: `^IM[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

sidSID<DY>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A 34 character string that uniquely identifies this resource.

Pattern: `^DY[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

Fetch a ReceiptLink to code sample: Fetch a Receipt

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

    async function fetchConversationMessageReceipt() {


    11

      const deliveryReceipt = await client.conversations.v1


    12

        .conversations("ConversationSid")


    13

        .messages("IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    14

        .deliveryReceipts("DYaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    15

        .fetch();


    16




    17

      console.log(deliveryReceipt.accountSid);


    18

    }


    19




    20

    fetchConversationMessageReceipt();

### Response

Note about this response

Copy response


    1

    {


    2

      "sid": "DYaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "conversation_sid": "ConversationSid",


    5

      "message_sid": "IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    6

      "channel_message_sid": "SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    7

      "status": "failed",


    8

      "error_code": 3000,


    9

      "participant_sid": "MBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    10

      "date_created": "2016-03-24T20:37:57Z",


    11

      "date_updated": "2016-03-24T20:37:57Z",


    12

      "url": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Receipts/DYaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    13

    }

* * *

## Read multiple ConversationMessageReceipt resources

read-multiple-conversationmessagereceipt-resources page anchor

Positive FeedbackNegative Feedback

`GET https://conversations.twilio.com/v1/Conversations/{ConversationSid}/Messages/{MessageSid}/Receipts`

### Path parameters

path-parameters-1 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

conversationSidstring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique ID of the [Conversation](/docs/conversations/api/conversation-resource "Conversation") for this message.

* * *

messageSidSID<IM>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the message within a [Conversation](/docs/conversations/api/conversation-resource "Conversation") the delivery receipt belongs to.

Pattern: `^IM[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

### Query parameters

query-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

pageSizeinteger<int64>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

How many resources to return in each list page. The default is 50, and the maximum is 50.

Minimum: `1`Maximum: `50`

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

List multiple ReceiptsLink to code sample: List multiple Receipts

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

    async function listConversationMessageReceipt() {


    11

      const deliveryReceipts = await client.conversations.v1


    12

        .conversations("ConversationSid")


    13

        .messages("IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    14

        .deliveryReceipts.list({ limit: 20 });


    15




    16

      deliveryReceipts.forEach((d) => console.log(d.accountSid));


    17

    }


    18




    19

    listConversationMessageReceipt();

### Response

Note about this response

Copy response


    1

    {


    2

      "meta": {


    3

        "page": 0,


    4

        "page_size": 50,


    5

        "first_page_url": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Receipts?PageSize=50&Page=0",


    6

        "previous_page_url": null,


    7

        "url": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Receipts?PageSize=50&Page=0",


    8

        "next_page_url": null,


    9

        "key": "delivery_receipts"


    10

      },


    11

      "delivery_receipts": [


    12

        {


    13

          "sid": "DYaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    14

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    15

          "conversation_sid": "CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    16

          "message_sid": "IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    17

          "channel_message_sid": "SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    18

          "status": "failed",


    19

          "error_code": 3000,


    20

          "participant_sid": "MBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    21

          "date_created": "2016-03-24T20:37:57Z",


    22

          "date_updated": "2016-03-24T20:37:57Z",


    23

          "url": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Receipts/DYaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    24

        },


    25

        {


    26

          "sid": "DYaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    27

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    28

          "conversation_sid": "CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    29

          "message_sid": "IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    30

          "channel_message_sid": "SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    31

          "status": "failed",


    32

          "error_code": 3000,


    33

          "participant_sid": "MBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    34

          "date_created": "2016-03-24T20:37:57Z",


    35

          "date_updated": "2016-03-24T20:37:57Z",


    36

          "url": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Receipts/DYaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    37

        },


    38

        {


    39

          "sid": "DYaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    40

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    41

          "conversation_sid": "CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    42

          "message_sid": "IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    43

          "channel_message_sid": "SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    44

          "status": "failed",


    45

          "error_code": 3000,


    46

          "participant_sid": "MBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    47

          "date_created": "2016-03-24T20:37:57Z",


    48

          "date_updated": "2016-03-24T20:37:57Z",


    49

          "url": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Receipts/DYaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    50

        }


    51

      ]


    52

    }