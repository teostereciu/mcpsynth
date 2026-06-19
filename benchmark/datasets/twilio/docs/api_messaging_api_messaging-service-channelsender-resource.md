# ChannelSenders subresource

*Source: https://www.twilio.com/docs/messaging/api/messaging-service-channelsender-resource*

---

# ChannelSenders subresource

Positive FeedbackNegative Feedback

* * *

(new)

## Public Beta

The Services resource is currently available as a Public Beta product. This means that some features for configuring your Messaging Service via the REST API are not yet implemented, and others may be changed before the product is declared Generally Available. Messaging Service Configuration through the [Twilio Console(link takes you to an external page)](https://www.twilio.com/console "Twilio Console") is Generally Available.

Public Beta products are [not covered by a Twilio SLA(link takes you to an external page)](https://help.twilio.com/hc/en-us/articles/115002413087-Twilio-Beta-product-support "not covered by a Twilio SLA").

The resources for sending Messages with a Messaging Service are Generally Available.

ChannelSenders is subresource of [Services](/docs/messaging/api/service-resource "Services") and represents a channel sender that is associated with a Messaging Service, such as WhatsApp.

When sending a message with your Messaging Service to a channel destination, Twilio will select a channel sender of that corresponding channel from the service for delivery.

See [Twilio Channels: A New Way Reach Customers in Apps They Already Use(link takes you to an external page)](https://www.twilio.com/blog/introducing-twilio-channels-html "Twilio Channels: A New Way Reach Customers in Apps They Already Use") for more information on Twilio Channels.

* * *

## ChannelSender Properties

channelsender-properties page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescriptionChild properties

accountSidSID<AC>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that created the ChannelSender resource.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

messagingServiceSidSID<MG>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Service](/docs/messaging/services "Service") the resource is associated with.

Pattern: `^MG[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

sidSID<XE>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique string that we created to identify the ChannelSender resource.

Pattern: `^XE[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

senderstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique string that identifies the sender e.g whatsapp:+123456XXXX.

* * *

senderTypestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A string value that identifies the sender type e.g WhatsApp, Messenger.

* * *

countryCodestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The 2-character [ISO Country Code(link takes you to an external page)](https://www.iso.org/iso-3166-country-codes.html "ISO Country Code") of the number.

* * *

dateCreatedstring<date-time>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date and time in GMT when the resource was created specified in [ISO 8601(link takes you to an external page)](https://en.wikipedia.org/wiki/ISO_8601 "ISO 8601") format.

* * *

dateUpdatedstring<date-time>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date and time in GMT when the resource was last updated specified in [ISO 8601(link takes you to an external page)](https://en.wikipedia.org/wiki/ISO_8601 "ISO 8601") format.

* * *

urlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The absolute URL of the ChannelSender resource.

* * *

## Create a ChannelSender

create-a-channelsender page anchor

Positive FeedbackNegative Feedback

`POST https://messaging.twilio.com/v1/Services/{MessagingServiceSid}/ChannelSenders`

### Path parameters

path-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

messagingServiceSidSID<MG>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Service](/docs/chat/rest/service-resource "Service") to create the resource under.

Pattern: `^MG[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

### Request body parameters

request-body-parameters page anchor

Positive FeedbackNegative Feedback

Encoding type:`application/x-www-form-urlencoded`

SchemaExample

Property nameTypeRequiredPIIDescriptionChild properties

sidSID<XE>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the Channel Sender being added to the Service.

Pattern: `^XE[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

Select from available examples

Copy code block


    {


      "Sid": "XEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    }

Create a ChannelSender for a Messaging ServiceLink to code sample: Create a ChannelSender for a Messaging Service

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

    async function createChannelSender() {


    11

      const channelSender = await client.messaging.v1


    12

        .services("MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .channelSenders.create({ sid: "XEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" });


    14




    15

      console.log(channelSender.accountSid);


    16

    }


    17




    18

    createChannelSender();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "messaging_service_sid": "MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "sid": "XEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

      "sender": "whatsapp:+12487960483",


    6

      "sender_type": "WhatsApp",


    7

      "country_code": "US",


    8

      "date_created": "2023-07-30T20:12:31Z",


    9

      "date_updated": "2023-07-30T20:12:33Z",


    10

      "url": "https://messaging.twilio.com/v1/Services/MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ChannelSenders/XEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    11

    }

* * *

## Retrieve a ChannelSender

retrieve-a-channelsender page anchor

Positive FeedbackNegative Feedback

`GET https://messaging.twilio.com/v1/Services/{MessagingServiceSid}/ChannelSenders/{Sid}`

### Path parameters

path-parameters-1 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

messagingServiceSidSID<MG>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Service](/docs/chat/rest/service-resource "Service") to fetch the resource from.

Pattern: `^MG[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

sidstring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the ChannelSender resource to fetch.

Retrieve a ChannelSender from a Messaging ServiceLink to code sample: Retrieve a ChannelSender from a Messaging Service

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

    async function fetchChannelSender() {


    11

      const channelSender = await client.messaging.v1


    12

        .services("MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .channelSenders("XEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    14

        .fetch();


    15




    16

      console.log(channelSender.accountSid);


    17

    }


    18




    19

    fetchChannelSender();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "messaging_service_sid": "MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "sid": "XEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

      "sender": "whatsapp:+12487960483",


    6

      "sender_type": "WhatsApp",


    7

      "country_code": "US",


    8

      "date_created": "2023-07-30T20:12:31Z",


    9

      "date_updated": "2023-07-30T20:12:33Z",


    10

      "url": "https://messaging.twilio.com/v1/Services/MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ChannelSenders/XEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    11

    }

* * *

## Retrieve a list of ChannelSenders

retrieve-a-list-of-channelsenders page anchor

Positive FeedbackNegative Feedback

`GET https://messaging.twilio.com/v1/Services/{MessagingServiceSid}/ChannelSenders`

### Path parameters

path-parameters-2 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

messagingServiceSidSID<MG>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Service](/docs/chat/rest/service-resource "Service") to read the resources from.

Pattern: `^MG[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

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

Retrieve a list of ChannelSenders from a Messaging ServiceLink to code sample: Retrieve a list of ChannelSenders from a Messaging Service

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

    async function listChannelSender() {


    11

      const channelSenders = await client.messaging.v1


    12

        .services("MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .channelSenders.list({ limit: 20 });


    14




    15

      channelSenders.forEach((c) => console.log(c.accountSid));


    16

    }


    17




    18

    listChannelSender();

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

        "page_size": 20,


    5

        "first_page_url": "https://messaging.twilio.com/v1/Services/MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ChannelSenders?PageSize=20&Page=0",


    6

        "previous_page_url": null,


    7

        "next_page_url": null,


    8

        "key": "senders",


    9

        "url": "https://messaging.twilio.com/v1/Services/MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ChannelSenders?PageSize=20&Page=0"


    10

      },


    11

      "senders": [


    12

        {


    13

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    14

          "messaging_service_sid": "MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    15

          "sid": "XEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    16

          "sender": "whatsapp:+12487960483",


    17

          "sender_type": "WhatsApp",


    18

          "country_code": "US",


    19

          "date_created": "2023-07-30T20:12:31Z",


    20

          "date_updated": "2023-07-30T20:12:33Z",


    21

          "url": "https://messaging.twilio.com/v1/Services/MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ChannelSenders/XEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    22

        },


    23

        {


    24

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    25

          "messaging_service_sid": "MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    26

          "sid": "XEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",


    27

          "sender": "messenger:104794531907950",


    28

          "sender_type": "Messenger",


    29

          "country_code": "US",


    30

          "date_created": "2023-07-30T20:12:31Z",


    31

          "date_updated": "2023-07-30T20:12:33Z",


    32

          "url": "https://messaging.twilio.com/v1/Services/MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ChannelSenders/XEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"


    33

        },


    34

        {


    35

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    36

          "messaging_service_sid": "MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    37

          "sid": "XEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaac",


    38

          "sender": "rcs:ms_dev_ttatqler_agent",


    39

          "sender_type": "RCS",


    40

          "country_code": "US",


    41

          "date_created": "2023-07-30T20:12:31Z",


    42

          "date_updated": "2023-07-30T20:12:33Z",


    43

          "url": "https://messaging.twilio.com/v1/Services/MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ChannelSenders/XEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaac"


    44

        }


    45

      ]


    46

    }

* * *

## Delete a ChannelSender

delete-a-channelsender page anchor

Positive FeedbackNegative Feedback

`DELETE https://messaging.twilio.com/v1/Services/{MessagingServiceSid}/ChannelSenders/{Sid}`

Returns "204 NO CONTENT" if the channel sender was successfully removed from the Service.

### Path parameters

path-parameters-3 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

messagingServiceSidSID<MG>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Service](/docs/chat/rest/service-resource "Service") to delete the resource from.

Pattern: `^MG[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

sidstring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the Channel Sender resource to delete.

Remove a ChannelSender from a Messaging ServiceLink to code sample: Remove a ChannelSender from a Messaging Service

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

    async function deleteChannelSender() {


    11

      await client.messaging.v1


    12

        .services("MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .channelSenders("XEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    14

        .remove();


    15

    }


    16




    17

    deleteChannelSender();