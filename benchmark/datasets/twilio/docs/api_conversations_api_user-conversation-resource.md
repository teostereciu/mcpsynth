# User Conversation Resource

*Source: https://www.twilio.com/docs/conversations/api/user-conversation-resource*

---

# User Conversation Resource

Positive FeedbackNegative Feedback

* * *

The UserConversation resource lists the [Conversations](/docs/conversations/api/conversation-resource "Conversations") in which a particular User is an active Participant. Use this resource to:

  * list a user's conversations, present or historical,
  * mute a user's push notifications for specific channels, or
  * count a user's unread messages


(information)

## Info

UnreadMessageCount returns a maximum value of 1000

* * *

## Conversation Properties

conversation-properties page anchor

Positive FeedbackNegative Feedback

Each UserConversation resource contains these properties.

Property nameTypeRequiredPIIDescriptionChild properties

accountSidSID<AC>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique ID of the [Account](/docs/iam/api/account "Account") responsible for this conversation.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

chatServiceSidSID<IS>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique ID of the [Conversation Service](/docs/conversations/api/service-resource "Conversation Service") this conversation belongs to.

Pattern: `^IS[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

conversationSidSID<CH>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique ID of the [Conversation](/docs/conversations/api/conversation-resource "Conversation") for this User Conversation.

Pattern: `^CH[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

unreadMessagesCountinteger

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The number of unread Messages in the Conversation for the Participant.

* * *

lastReadMessageIndexinteger

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The index of the last Message in the Conversation that the Participant has read.

* * *

participantSidSID<MB>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique ID of the [participant](/docs/conversations/api/conversation-participant-resource "participant") the user conversation belongs to.

Pattern: `^MB[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

userSidSID<US>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique string that identifies the [User resource](/docs/conversations/api/user-resource "User resource").

Pattern: `^US[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

friendlyNamestring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The human-readable name of this conversation, limited to 256 characters. Optional.

* * *

conversationStateenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The current state of this User Conversation. One of `inactive`, `active` or `closed`.

Possible values:

`inactive``active``closed`

* * *

timers

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Timer date values representing state update for this conversation.

* * *

attributesstring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

An optional string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified. **Note** that if the attributes are not set "{}" will be returned.

* * *

dateCreatedstring<date-time>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date that this conversation was created, given in ISO 8601 format.

* * *

dateUpdatedstring<date-time>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date that this conversation was last updated, given in ISO 8601 format.

* * *

createdBystring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Identity of the creator of this Conversation.

* * *

notificationLevelenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The Notification Level of this User Conversation. One of `default` or `muted`.

Possible values:

`default``muted`

* * *

uniqueNamestring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

An application-defined string that uniquely identifies the Conversation resource. It can be used to address the resource in place of the resource's `conversation_sid` in the URL.

* * *

urlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

* * *

linksobject<uri-map>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Contains absolute URLs to access the [participant](/docs/conversations/api/conversation-participant-resource "participant") and [conversation](/docs/conversations/api/conversation-resource "conversation") of this conversation.

* * *

## Fetch a specific conversation

fetch-a-specific-conversation page anchor

Positive FeedbackNegative Feedback

`GET https://conversations.twilio.com/v1/Users/{UserSid}/Conversations/{ConversationSid}`

The `{UserSid}` value can be either the `sid` or the `identity` of the User resource and the `{ConversationSid}` value can be either the `sid` or the `unique_name` of the Conversation to fetch.

### Path parameters

path-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

userSidstring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique SID identifier of the [User resource](/docs/conversations/api/user-resource "User resource"). This value can be either the `sid` or the `identity` of the User resource.

* * *

conversationSidstring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique SID identifier of the Conversation. This value can be either the `sid` or the `unique_name` of the [Conversation resource](/docs/conversations/api/conversation-resource "Conversation resource").

Fetch a specific conversationLink to code sample: Fetch a specific conversation

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

    async function fetchUserConversation() {


    11

      const userConversation = await client.conversations.v1


    12

        .users("USXXXXXXXXXXXXX")


    13

        .userConversations("CHXXXXXXXXXXXXX")


    14

        .fetch();


    15




    16

      console.log(userConversation.accountSid);


    17

    }


    18




    19

    fetchUserConversation();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "chat_service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "conversation_sid": "CHXXXXXXXXXXXXX",


    5

      "unread_messages_count": 100,


    6

      "last_read_message_index": 100,


    7

      "participant_sid": "MBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    8

      "user_sid": "USXXXXXXXXXXXXX",


    9

      "friendly_name": "friendly_name",


    10

      "conversation_state": "inactive",


    11

      "timers": {


    12

        "date_inactive": "2015-12-16T22:19:38Z",


    13

        "date_closed": "2015-12-16T22:28:38Z"


    14

      },


    15

      "attributes": "{}",


    16

      "date_created": "2015-07-30T20:00:00Z",


    17

      "date_updated": "2015-07-30T20:00:00Z",


    18

      "created_by": "created_by",


    19

      "notification_level": "default",


    20

      "unique_name": "unique_name",


    21

      "url": "https://conversations.twilio.com/v1/Users/USaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    22

      "links": {


    23

        "participant": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/MBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    24

        "conversation": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    25

      }


    26

    }

* * *

## List All of a User's Conversations

list-all-of-a-users-conversations page anchor

Positive FeedbackNegative Feedback

`GET https://conversations.twilio.com/v1/Users/{UserSid}/Conversations`

The `{UserSid}` value can be either the `sid` or the `identity` of the User resource to read UserConversation resources from.

### Path parameters

path-parameters-1 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

userSidstring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique SID identifier of the [User resource](/docs/conversations/api/user-resource "User resource"). This value can be either the `sid` or the `identity` of the User resource.

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

List All of a User's ConversationsLink to code sample: List All of a User's Conversations

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

    async function listUserConversation() {


    11

      const userConversations = await client.conversations.v1


    12

        .users("USXXXXXXXXXXXXX")


    13

        .userConversations.list({ limit: 20 });


    14




    15

      userConversations.forEach((u) => console.log(u.accountSid));


    16

    }


    17




    18

    listUserConversation();

### Response

Note about this response

Copy response


    1

    {


    2

      "conversations": [],


    3

      "meta": {


    4

        "page": 0,


    5

        "page_size": 50,


    6

        "first_page_url": "https://conversations.twilio.com/v1/Users/USaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations?PageSize=50&Page=0",


    7

        "previous_page_url": null,


    8

        "url": "https://conversations.twilio.com/v1/Users/USaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations?PageSize=50&Page=0",


    9

        "next_page_url": null,


    10

        "key": "conversations"


    11

      }


    12

    }

* * *

## Update a specific conversation

update-a-specific-conversation page anchor

Positive FeedbackNegative Feedback

`POST https://conversations.twilio.com/v1/Users/{UserSid}/Conversations/{ConversationSid}`

### Path parameters

path-parameters-2 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

userSidstring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique SID identifier of the [User resource](/docs/conversations/api/user-resource "User resource"). This value can be either the `sid` or the `identity` of the User resource.

* * *

conversationSidstring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique SID identifier of the Conversation. This value can be either the `sid` or the `unique_name` of the [Conversation resource](/docs/conversations/api/conversation-resource "Conversation resource").

### Request body parameters

request-body-parameters page anchor

Positive FeedbackNegative Feedback

Encoding type:`application/x-www-form-urlencoded`

SchemaExample

Property nameTypeRequiredPIIDescriptionChild properties

notificationLevelenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The Notification Level of this User Conversation. One of `default` or `muted`.

Possible values:

`default``muted`

* * *

lastReadTimestampstring<date-time>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date of the last message read in conversation by the user, given in ISO 8601 format.

* * *

lastReadMessageIndexinteger

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The index of the last Message in the Conversation that the Participant has read.

Copy code block


    {


      "NotificationLevel": "default",


      "LastReadTimestamp": "2015-07-30T20:00:00Z",


      "LastReadMessageIndex": 100


    }

Update a specific conversationLink to code sample: Update a specific conversation

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

    async function updateUserConversation() {


    11

      const userConversation = await client.conversations.v1


    12

        .users("USXXXXXXXXXXXXX")


    13

        .userConversations("CHXXXXXXXXXXXXX")


    14

        .update({ notificationLevel: "default" });


    15




    16

      console.log(userConversation.accountSid);


    17

    }


    18




    19

    updateUserConversation();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "chat_service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "conversation_sid": "CHXXXXXXXXXXXXX",


    5

      "unread_messages_count": 100,


    6

      "last_read_message_index": 100,


    7

      "participant_sid": "MBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    8

      "user_sid": "USXXXXXXXXXXXXX",


    9

      "friendly_name": "friendly_name",


    10

      "conversation_state": "inactive",


    11

      "timers": {


    12

        "date_inactive": "2015-12-16T22:19:38Z",


    13

        "date_closed": "2015-12-16T22:28:38Z"


    14

      },


    15

      "attributes": "{}",


    16

      "date_created": "2015-07-30T20:00:00Z",


    17

      "date_updated": "2015-07-30T20:00:00Z",


    18

      "created_by": "created_by",


    19

      "notification_level": "default",


    20

      "unique_name": "unique_name",


    21

      "url": "https://conversations.twilio.com/v1/Users/USaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    22

      "links": {


    23

        "participant": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/MBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    24

        "conversation": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    25

      }


    26

    }

* * *

## Set the NotificationLevel for a conversation

set-the-notificationlevel-for-a-conversation page anchor

Positive FeedbackNegative Feedback

`POST https://conversations.twilio.com/v1/Users/{UserSid}/Conversations/{ConversationSid}`

The `NotificationLevel` property expresses whether a user receives pushes for this conversation or not. This can be set separately for each user/conversation pair.

### Path parameters

path-parameters-3 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

userSidstring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique SID identifier of the [User resource](/docs/conversations/api/user-resource "User resource"). This value can be either the `sid` or the `identity` of the User resource.

* * *

conversationSidstring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique SID identifier of the Conversation. This value can be either the `sid` or the `unique_name` of the [Conversation resource](/docs/conversations/api/conversation-resource "Conversation resource").

### Request body parameters

request-body-parameters-1 page anchor

Positive FeedbackNegative Feedback

Encoding type:`application/x-www-form-urlencoded`

SchemaExample

Property nameTypeRequiredPIIDescriptionChild properties

notificationLevelenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The Notification Level of this User Conversation. One of `default` or `muted`.

Possible values:

`default``muted`

* * *

lastReadTimestampstring<date-time>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date of the last message read in conversation by the user, given in ISO 8601 format.

* * *

lastReadMessageIndexinteger

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The index of the last Message in the Conversation that the Participant has read.

Copy code block


    {


      "NotificationLevel": "default",


      "LastReadTimestamp": "2015-07-30T20:00:00Z",


      "LastReadMessageIndex": 100


    }

Mute Notifications for a ConversationLink to code sample: Mute Notifications for a Conversation

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

    async function updateUserConversation() {


    11

      const userConversation = await client.conversations.v1


    12

        .users("UserSid")


    13

        .userConversations("ConversationSid")


    14

        .update({ notificationLevel: "muted" });


    15




    16

      console.log(userConversation.notificationLevel);


    17

    }


    18




    19

    updateUserConversation();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "chat_service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "conversation_sid": "ConversationSid",


    5

      "unread_messages_count": 100,


    6

      "last_read_message_index": 100,


    7

      "participant_sid": "MBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    8

      "user_sid": "UserSid",


    9

      "friendly_name": "friendly_name",


    10

      "conversation_state": "inactive",


    11

      "timers": {


    12

        "date_inactive": "2015-12-16T22:19:38Z",


    13

        "date_closed": "2015-12-16T22:28:38Z"


    14

      },


    15

      "attributes": "{}",


    16

      "date_created": "2015-07-30T20:00:00Z",


    17

      "date_updated": "2015-07-30T20:00:00Z",


    18

      "created_by": "created_by",


    19

      "notification_level": "muted",


    20

      "unique_name": "unique_name",


    21

      "url": "https://conversations.twilio.com/v1/Users/USaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    22

      "links": {


    23

        "participant": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/MBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    24

        "conversation": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    25

      }


    26

    }

* * *

## Remove a User from one of their Conversations

remove-a-user-from-one-of-their-conversations page anchor

Positive FeedbackNegative Feedback

`DELETE https://conversations.twilio.com/v1/Users/{UserSid}/Conversations/{ConversationSid}`

### Path parameters

path-parameters-4 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

userSidstring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique SID identifier of the [User resource](/docs/conversations/api/user-resource "User resource"). This value can be either the `sid` or the `identity` of the User resource.

* * *

conversationSidstring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique SID identifier of the Conversation. This value can be either the `sid` or the `unique_name` of the [Conversation resource](/docs/conversations/api/conversation-resource "Conversation resource").

Remove a User from one of their ConversationsLink to code sample: Remove a User from one of their Conversations

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

    async function deleteUserConversation() {


    11

      await client.conversations.v1


    12

        .users("USXXXXXXXXXXXXX")


    13

        .userConversations("CHXXXXXXXXXXXXX")


    14

        .remove();


    15

    }


    16




    17

    deleteUserConversation();