# Conversations API

*Source: https://developers.hubspot.com/docs/api/conversations/conversations*

---

Conversations

# Conversations API

Use the conversations API to manage inboxes, channels, threads, and messages.

Scope requirements

The conversations APIs enable you to manage and interact with the [conversations inbox](https://knowledge.hubspot.com/inbox/overview-of-the-conversations-inbox) and [help desk](https://knowledge.hubspot.com/help-desk/overview-of-the-help-desk-workspace), including connected channels and their associated messages. For example, you can use these APIs to:

  * Get and sort conversations inboxes, channels, threads, and messages.
  * Update thread statuses.
  * Delete and restore threads.
  * Send outbound messages via existing conversations channels.
  * Send an internal comment to an agent.
  * Retrieve conversation data to create advanced reports and analytics in external tools.

You could also use these APIs to integrate existing channels with other apps such as [Slack](https://knowledge.hubspot.com/integrations/how-do-i-use-the-slack-integration) or Microsoft Teams to send replies or receive notifications. You can also use webhooks with the conversations API. Learn more about the available webhook events.

**Please note:** If you’re planning on defining a custom channel that users can connect to their HubSpot account, check out the [custom channels API](/docs/api-reference/legacy/conversations/guide).

##

​

Scope requirements

For any requests to the `GET` endpoints, or a `POST` batch read request to the [get actors endpoint](/docs/api-reference/legacy/conversations/conversations/actors/get-actor), you must have `conversations.read` access. All other endpoints require `conversations.write` access. Learn more about authorizing [scopes](/docs/apps/developer-platform/build-apps/authentication/scopes) for your app.

##

​

Filter and sort results

When retrieving inboxes, channels, channel accounts, threads, and messages using the endpoints outlined in this article, you can use different query parameters to filter and sort your responses.

Parameter| Type| Description
---|---|---
`sort`| String| Set the sort order of the response. You can sort by multiple properties.
`after`| String| The paging cursor token of the last successfully read resource will be returned as the `paging.next.after` JSON property of a paged response containing more results.
`limit`| Integer| The maximum number of results to display per page.

You can also sort your results by any field on the channel, channel accounts, or inbox objects. For example, you could sort inboxes by name, or channel accounts by both channel ID and name.

##

​

Inboxes

To retrieve a list of inboxes set up in your account, make a `GET` request to `/conversations/v3/conversations/inboxes`. When you make a successful request, the response will include the inbox IDs of the different inboxes set up in your account. Each entry in the response will also include a `type` property, which can be either `INBOX` or `HELP_DESK`, depending on whether you connected the inbox to a [conversations inbox](https://knowledge.hubspot.com/inbox/use-the-conversations-inbox) or the [help desk workspace](https://knowledge.hubspot.com/help-desk/overview-of-the-help-desk-workspace). An example response is shown below:


    {
      "total": 3,
      "results": [
        {
          "id": "481939",
          "name": "Main website chatflow inbox",
          "createdAt": "2019-07-06T21:18:14.342Z",
          "updatedAt": "2022-08-19T20:03:44.993Z",
          "type": "INBOX",
          "archived": false
        },
        {
          "id": "273071781",
          "name": "T1 support helpdesk",
          "createdAt": "2023-05-31T21:53:12.704Z",
          "updatedAt": "2023-05-31T21:53:12.704Z",
          "type": "HELP_DESK",
          "archived": false
        }
      ]
    }


You can also retrieve details about a specific inbox by using the inbox ID to make a `GET` request to `/conversations/v3/conversations/inboxes/{inboxId}`.

##

​

Channels

You can retrieve a list of the channels connected to your inboxes by making a `GET` request to `/conversations/v3/conversations/channels`. When you make a successful request, the response will include the channel IDs for the different channels connected to your inbox. To retrieve a specific channel, use the channel ID to make a `GET` request to `/conversations/v3/conversations/channels/{channelId}`. You can also retrieve channel accounts, which are instances of a channel that are used to send and receive messages, like a specific chatflow created for one of your chat channels or a team email address connected as an email channel. To retrieve a list of channel accounts, make a `GET` request to `/conversations/v3/conversations/channel-accounts`. You can limit the results by including the following parameters in the request URL:

Parameter| Description
---|---
`channelId`| The ID of the channel type for which you’re retrieving a channel instance.
`inboxId`| The ID of the inbox that the channel is connected to.

For example, your request may look similar to the following: `https://api.hubspot.com/conversations/v3/conversations/channel-accounts?channelId=1000&inboxId=448`. When you make a successful request, the response will include an `id` property, which is the channel account ID. For example, the response may resemble the following:


    {
      "total": 1,
      "results": [
        {
          "id": "148662",
          "channelId": "1000",
          "name": "New chatflow",
          "inboxId": "481939",
          "active": false,
          "authorized": true,
          "createdAt": "2019-10-04T15:24:39.136Z",
          "archived": false
        }
      ]
    }


You can use the channel account ID to retrieve a single channel account, such as a specific chatflow. To retrieve a specific channel account, make a `GET` request to `/conversations/v3/conversations/channel-accounts/{channelAccountId}`.

##

​

Threads & messages

###

​

Retrieve threads

Threads are a group of related messages that make up a conversation in the inbox. To retrieve a list of all threads in your conversations inbox, make a `GET` request to `/conversations/v3/conversations/threads`. To filter and search your results, you can use the following query parameters in your request:

Parameter| Type| Description
---|---|---
`after`| String| The paging cursor token of the last successfully read resource will be returned as the `paging.next.after` JSON property of a paged response containing more results. Use this parameter when sorting by ID.
`archived`| Boolean| To retrieve archived threads, use the value `true`.
`associatedContactId`| String| Filter threads by a specific contact ID.
`associatedTicketId`| String| Filter threads to only include threads that are associated with the provided ticket ID.
`association`| String| If you provide `association=TICKET` as a query parameter, any threads in the response will include a `threadAssociations` object if they have a ticket association. The `threadsAssociations` property includes a single nested `associatedTicketId` field, which provides the ID of the associated ticket.
`inboxId`| String| Filter threads by a specific inbox ID. Note that you can only filter a single inbox ID (multiple instances of this query parameter are _not_ supported).
`latestMessageTimestampAfter`| String| The minimum `latestMessageTimestamp`. This is required only when sorting by `latestMessageTimestamp`.
`limit`| String| The total number of results to display per page. The maximum limit is 500.
`sort`| String| Set the sort order of the response. Valid options include `id` , which is the default, and `latestMessageTimestamp` , which requires the `latestMessageTimestampAfter` field to also be set. Results are always returned in ascending order.

When you make a successful request, the response will include the thread ID, which you can use to retrieve, update, or create a new message in a thread. For example, if you make a `GET` request to `/conversations/v3/conversations/threads?association=TICKET`, the response would resemble the following:


    {
      "results": [
        {
          "id": "176347007",
          "createdAt": "2019-11-18T18:47:59.865Z",
          "closedAt": "2019-11-18T18:50:06.872Z",
          "status": "CLOSED",
          "originalChannelId": "1000",
          "originalChannelAccountId": "148662",
          "latestMessageTimestamp": "2019-11-18T18:50:00.279Z",
          "latestMessageSentTimestamp": "2019-11-18T18:48:38.788Z",
          "latestMessageReceivedTimestamp": "2019-11-18T18:50:00.279Z",
          "assignedTo": "A-2620022",
          "spam": false,
          "inboxId": "481939",
          "associatedContactId": "1401",
          "archived": false,
          "threadAssociations": {
            "associatedTicketId": "57774743"
          }
        },
        {
          "id": "176350633",
          "createdAt": "2019-11-18T18:53:05.680Z",
          "closedAt": "2019-11-18T18:53:59.783Z",
          "status": "CLOSED",
          "originalChannelId": "1000",
          "originalChannelAccountId": "148662",
          "latestMessageTimestamp": "2019-11-18T18:53:56.694Z",
          "latestMessageSentTimestamp": "2019-11-18T18:53:56.694Z",
          "latestMessageReceivedTimestamp": "2019-11-18T18:53:52.199Z",
          "assignedTo": "A-2620022",
          "spam": false,
          "inboxId": "481939",
          "associatedContactId": "1451",
          "archived": false
        }
      ]
    }


See all 39 lines

To retrieve a specific thread by thread ID, make a `GET` request to `/conversations/v3/conversations/threads/{threadId}`. Available query parameters include:

Parameter| Type| Description
---|---|---
`archived`| Boolean| To retrieve archived threads, use the value `true`.
`association`| String| If you provide `association=TICKET` as a query parameter and the thread has an associated ticket, the response will include a `threadAssociations` object, which in turn includes a single nested `associatedTicketId` property, which provides the ID of the associated ticket.
`property`| String| A comma-separated list of properties to include (e.g., `?property=spam,inboxId`).

###

​

Retrieve messages

To get the entire message history, make a `GET` request to `/conversations/v3/conversations/threads/{threadId}/messages`. When you make a successful request, the response will include the message ID, which you can use to retrieve a specific message. To do so, make a `GET` request to `/conversations/v3/conversations/threads/{threadId}/messages/{messageId}`. For email messages, HubSpot cuts off the reply history section of an email. This is similar to how common mail clients handle reply history and longer emails.

  * When you retrieve a message, the response will include a `truncationStatus` field. The value will either be `NOT_TRUNCATED`, `TRUNCATED_TO_MOST_RECENT_REPLY`, or `TRUNCATED`.
  * If a message is truncated, you can retrieve the full version of the message by making a `GET` request to the [original content](/docs/api-reference/legacy/conversations/conversations/messages/get-conversation) endpoint.


###

​

Retrieve a subset of messages associated with a specific contact or ticket

You can also fetch messages associated with a single contact or ticket, which can be helpful if you’re creating a view where a customer can review the conversations they’ve had with your business, or you want to find all conversations associated with a specific ticket. To filter for messages associated with a contact, provide the ID of the contact as the `associatedContactId` as a query parameter in the URL of your request, along with a `threadStatus` parameter, which can be either `OPEN` or `CLOSED`. For example, to retrieve open threads associated with a contact whose ID is `53701`, you’d make a `GET` request to the following URL: `https://api.hubspot.com/conversations/v3/conversations/threads?associatedContactId=53701&threadStatus=OPEN` To filter for messages associated with a specific ticket, provide ticket ID as the `associatedTicketId` query parameter in the URL of your request. For example, to retrieve messages associated with a ticket ID of `12345`, you’d make the following `GET` request: `https://api.hubspot.com/conversations/v3/conversations/threads?associatedTicketId=53701`

###

​

Get actors

Actors are entities that interact with conversations, like a HubSpot user responding to a message or a visitor sending a message. When you make a request to retrieve threads or messages, the response will include actor IDs. All actor IDs are a single letter representing the actor type, followed by a hyphen, followed by an identifier for the actor. The identifier could be a number, a string, etc. depending on the actor type. In the table below, learn more about the different actor IDs:

Actor Type| Identifier| Description
---|---|---
`A-`| HubSpot user ID (number)| Agent actor, i.e. a user in the account.
`E-`| Email address (string)| Email actor. This is used for email addresses that HubSpot didn’t try to resolve to an agent actor or a visitor actor. For example, HubSpot will generally resolve the from email address to a contact, but if an incoming email has any additional email addresses included in the _To_ field, _CC_ field, etc., HubSpot won’t try to resolve those email addresses to contacts.
`I-`| App ID (number)| Integration actor. This is used for actions taken by an integration.
`L-`| Customer Agent ID (number)| Customer agent actor. This is used for actions taken by [Breeze Customer Agent](https://knowledge.hubspot.com/customer-agent/create-a-customer-agent).
`S-`| S-hubspot (string)| System actor. This is used for actions taken by the HubSpot system itself.
`V-`| Contact ID (number)| Visitor actor. Keep in mind that it’s possible the visitor isn’t a contact yet.

For example, if you make a `GET` request to `/conversations/v3/conversations/threads/{threadId}/messages`, the response will include a `sender` and `recipient` fields. These fields will include the actor IDs for the visitor or agent. For example, your response may look similar to the following:


    {
      "results": [
        {
          "id": "3ad3474b08dd408ca57a8454e355e942",
          "conversationsThreadId": "176347007",
          "createdAt": "2019-11-18T18:47:59.949Z",
          "updatedAt": "2019-11-18T18:47:59.949Z",
          "createdBy": "V-1401",
          "client": {
            "clientType": "SYSTEM"
          },
          "senders": [
            {
              "actorId": "V-1401",
              "deliveryIdentifier": {
                "type": "CHANNEL_SPECIFIC_OPAQUE_ID",
                "value": "0232d1661ef84248bd4923cce9d3b917"
              }
            }
          ],
          "recipients": [],
          "archived": false,
          "text": "hi yes hello",
          "richText": "<div>hi yes hello</div>",
          "attachments": [],
          "truncationStatus": "NOT_TRUNCATED",
          "status": {
            "statusType": "RECEIVED"
          },
          "direction": "INCOMING",
          "channelId": "1000",
          "channelAccountId": "148662",
          "type": "MESSAGE"
        },
        {
          "id": "0c9b86b11210479eb1ae193ec5add0b7",
          "conversationsThreadId": "176347007",
          "createdAt": "2019-11-18T18:47:59.947Z",
          "createdBy": "S-hubspot",
          "client": {
            "clientType": "SYSTEM"
          },
          "senders": [
            {
              "actorId": "S-hubspot"
            }
          ],
          "recipients": [
            {
              "actorId": "V-1401",
              "deliveryIdentifier": {
                "type": "CHANNEL_SPECIFIC_OPAQUE_ID",
                "value": "0232d1661ef84248bd4923cce9d3b917"
              }
            }
          ],
          "archived": false,
          "text": "Got any questions? I'm happy to help.",
          "channelId": "1000",
          "channelAccountId": "148662",
          "type": "WELCOME_MESSAGE"
        }
      ]
    }


To retrieve a single actor, make a `GET` request to `/conversations/v3/conversations/actors/{actorId}`. You will need the `actorId`, which is included in the response to a request to get a message or thread. The response will return details like the actor name, email address, avatar, and actor type.

###

​

Update or restore threads

You can update a thread’s status by making a `PATCH` request to `/conversations/v3/conversations/threads/{threadId}`. In the request body, include the thread properties to update.

Field| Description
---|---
`status`| The status of the thread, which can be `OPEN` or `CLOSED`.

To restore any soft-deleted threads, make a `PATCH` request to `/conversations/v3/conversations/threads/{threadId}?archived=true` to retrieve the archived thread, then in the request body set the archived property to `false`.

Field| Description
---|---
`archived`| Set to `false` to restore a thread.

**Please note:** at this time you can only update the thread’s status or restore a thread when making a `PATCH` request to this endpoint.

###

​

Archive threads

You can archive a thread by making a `DELETE` request to `/conversations/v3/conversations/threads/{threadId}`. If you use this endpoint to archive a thread, the thread will be moved to the trash and will be permanently deleted after 30 days. In the section above, learn how to restore a thread before it is permanently deleted.

###

​

Add comments to threads

To add a comment to an existing thread, make a `POST` request to `/conversations/v3/conversations/threads/{threadId}/messages`. Comments only appear in the inbox and are not sent to visitors. You can include the following fields in the request body when sending a comment:

Field| Description
---|---
`type`| The type of message you’re sending. This value can either be `MESSAGE` or `COMMENT`.
`text`| The content of the message.
`richText`| The content of the message in HTML format. This is optional.
`attachments`| Any attachments to attach to the comment, specified as an object containing a `fileId`. If you want to include a specific attachment, you can upload it using the [Files API](/docs/api-reference/legacy/files/guide) before making the call to add the comment.

For example, your request body may look similar to the following:


    {
      "type": "COMMENT",
      "text": "Can you follow up?",
      "richText": "<p>Can you follow up?</p>"
    }


###

​

Send messages to threads

Using this endpoint, an integration can send outgoing messages as a user in a HubSpot account. These messages are sent from the channel, just like if a user typed and sent a response in the inbox. To send a message to an existing thread, make a `POST` request to `/conversations/v3/conversations/threads/{threadId}/messages`.

**Please note:** sending WhatsApp messages via a [connected WhatsApp business account](https://knowledge.hubspot.com/inbox/connect-whatsapp-to-the-conversations-inbox) is _not_ supported using the conversations API.

When sending a message to a thread, you can include the following fields. You can include both the message details, as well as recipient information, in the request body.

Field| Description
---|---
`type`| The type of message you’re sending. This value can either be `MESSAGE` or `COMMENT`.
`text`| The content of the message.
`richText`| The content of the message in HTML format. This is optional.
`recipients`| An object representing the recipients of the message. This is the most important for email, where you can specify multiple recipients. This object includes the following fields:

  * `actorID`: the ID associated with the message recipient.
  * `name`: the name of the recipient.
  * `recipientField`: for email messages, this is the type of recipient. Available values are `TO`, `CC`, or `BCC`.
  * `deliveryIdentifiers`: for email messages, this indicates the email addresses used for the visitor and agent.


`senderActorId`| This must be an agent actor ID that is associated to the HubSpot user in the account who is sending the message.
`channelId`| The ID of a generic channel returned from the channels endpoint, like `1000` for live chat, `1001` for Facebook Messenger, `1002` for email, etc.
`channelAccountId`| The ID of an account that is part of the `channelId` channel. On an existing thread, it is recommended to copy the `channelId` and `channelAccountId` of the most recent message on the thread.
`subject`| The subject line of the email. This is ignored when sending a message to a non-email channel.
`attachments`| Any attachments to attach to the message, which can be specified as an object that contains a URL to a file hosted in your HubSpot account, or a list of quick replies if you’re sending a message via Facebook Messenger or LiveChat. Learn more about how to include attachments in the section below.

For example, your request body may look similar to the following:


    {
      "type": "MESSAGE",
      "text": "Hey there, following up",
      "richText": "<p>Hey there, following up</p>",
      "recipients": [
        {
          "actorId": "E-user@hubspot.com",
          "name": "Leslie Knope",
          "recipientField": "TO",
          "deliveryIdentifiers": [
            {
              "type": "HS_EMAIL_ADDRESS",
              "value": "lknope@hubspot.com"
            }
          ]
        }
      ],
      "senderActorId": "A-3892666",
      "channelId": "1002",
      "channelAccountId": "42423411",
      "subject": "Follow up"
    }


If you make a successful request, the new message will be sent to the visitor. This can appear as a message in the chat widget, an email in the thread, a message in Facebook Messenger, etc.

###

​

Assign or unassign a user to a thread

You can assign a specific user to a thread by making a `POST` request to `conversations/v3/conversations/threads/{threadId}/assignee`, then including the user’s `actorId` in the request body. For example, if you wanted to assign a user with an email address of `jdoe@hubspot.com` to a thread with an ID of `12345`, you’d make a `POST` request to `conversations/v3/conversations/threads/12345/assignee` with the following request body:


    {
      "actorId": "jdoe@hubspot.com"
    }


You can unassign a user from a thread by making a `DELETE` request to `conversations/v3/conversations/threads/{threadId}/assignee`.

##

​

Include attachments in messages

Attachments can be links to a file hosted in the HubSpot files tool, or a set of quick replies if you’re sending a message using Facebook Messenger or LiveChat. To include an attachment from a file in your HubSpot account, provide the absolute URL as the `fileId` in the `attachments` field of the request body. For example, the corresponding part of the request body is shown in lines `16-18` below:


    {
      "type": "MESSAGE",
      "text": "Hey there, following up",
      "recipients": {
        "actorID": "E-user@hubspot.com",
        "name": "Leslie Knope",
        "recipientField": "TO",
        "deliveryIdentifiers": [{ "type": "HS_EMAIL_ADDRESS", "value": "lknope@hubspot.com" }]
      },
      "senderActorId": "A-3892666",
      "channelId": "1002",
      "channelAccountId": "424232411",
      "subject": "Follow up",
      "attachments": {
        "fileId": "https://12345678.fs1.hubspotusercontent-na1.net/hubfs/12345678/doggo_video.mp4"
      }
    }


If you connected Facebook Messenger or LiveChat as a channel, you can also specify a set of quick replies within the `attachments` field, which prompt the recipient with certain options that appear as tappable buttons below a message. Once tapped, the corresponding value of that option will be recorded. Quick replies should be provided as a list of objects that each contain the following fields:

  * `label`: the visible text that appears to the recipient (e.g., _Red_)
  * `value`: the associated value of the button that you want to record (e.g., `RED`)
  * `valueType`: the type of the quick reply option, which can be either `TEXT` or `URL`.

The example request body below demonstrates how to specify two quick reply options, _Yes_ and _No_ , on lines `21-32`:


    {
      "type": "MESSAGE",
      "text": "Did that answer your question?",
      "recipients": {
        "actorID": "E-user@hubspot.com",
        "name": "Leslie Knope",
        "recipientField": "TO",
        "deliveryIdentifiers": [
          {
            "type": "HS_EMAIL_ADDRESS",
            "value": "lknope@hubspot.com"
          }
        ]
      },
      "senderActorId": "A-3892666",
      "channelId": "1002",
      "channelAccountId": "424232411",
      "subject": "Follow up",
      "attachments": [
        "type": "QUICK_REPLIES",
        "quickReplies": [
          {
            "label": "Yes",
             "value": "Yes",
             "valueType": "URL"
          },
          {
            "label": "No",
            "value": "No",
            "valueType": "TEXT"
          }
        ]
      ]
    }


##

​

Webhooks

Webhooks for conversations are also supported and can be used in tandem with the conversations API. You can use webhooks to subscribe to events about conversations, including thread creation, thread status and assignment changes, and new messages on threads. Learn more about using [webhooks](/docs/api-reference/legacy/webhooks). You must have the `conversations.read` scope to get access to following webhooks. The available conversation webhook events are:

Event| Description
---|---
`conversation.creation`| A new thread has been created.
`conversation.deletion`| A thread has been archived.
`conversation.privacyDeletion`| A thread has been permanently deleted.
`conversation.propertyChange`| A property of a thread has been updated.
`conversation.newMessage`| A new message has been posted on a thread.

The available properties included in the payload for each event type are:

Event| Properties
---|---
`All events`| `objectId`: the ID of the Conversations thread that the webhook corresponds to.
`conversation.propertyChange`|

  * `assignedTo`: a thread’s assignment has changed. The value is the user ID of the new assignee, unless the owner was removed.
  * `status`: a thread’s status has changed, either to `OPEN` or `CLOSED`.
  * `isArchived`: when a thread is restored a `conversation.propertyChange` webhook will be sent and the value will be `false`.


`conversation.newMessage`|

  * `messageId`: the ID of the new message.
  * `messageType`: the type of the new message. One of `MESSAGE`, `COMMENT`, `WELCOME_MESSAGE`.


Last modified on March 30, 2026

Was this page helpful?

YesNo

⌘I

[facebook](https://www.facebook.com/hubspot)[instagram](https://www.instagram.com/hubspot)[youtube](https://youtube.com/user/HubSpot)[x](https://x.com/HubSpot)[linkedin](https://www.linkedin.com/company/hubspot)[medium](https://medium.com/@HubSpot)