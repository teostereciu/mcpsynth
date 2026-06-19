# zendev_horizontal

*Source: https://developer.zendesk.com/api-reference/ticketing/account-configuration/x_channel/*

---

## On this page

  * [X Channel](/api-reference/ticketing/account-configuration/x_channel/#x-channel)
  * [JSON format](/api-reference/ticketing/account-configuration/x_channel/#json-format)
  * [List Monitored X Handles](/api-reference/ticketing/account-configuration/x_channel/#list-monitored-x-handles)
  * [Show Monitored X Handle](/api-reference/ticketing/account-configuration/x_channel/#show-monitored-x-handle)
  * [Create Ticket from Tweet](/api-reference/ticketing/account-configuration/x_channel/#create-ticket-from-tweet)
  * [List Ticket statuses](/api-reference/ticketing/account-configuration/x_channel/#list-ticket-statuses)


#

## On this page

  * [X Channel](/api-reference/ticketing/account-configuration/x_channel/#x-channel)
  * [JSON format](/api-reference/ticketing/account-configuration/x_channel/#json-format)
  * [List Monitored X Handles](/api-reference/ticketing/account-configuration/x_channel/#list-monitored-x-handles)
  * [Show Monitored X Handle](/api-reference/ticketing/account-configuration/x_channel/#show-monitored-x-handle)
  * [Create Ticket from Tweet](/api-reference/ticketing/account-configuration/x_channel/#create-ticket-from-tweet)
  * [List Ticket statuses](/api-reference/ticketing/account-configuration/x_channel/#list-ticket-statuses)


## X Channel

Monitored X (formerly Twitter) handles represent the X accounts that you have configured on your account to pull new tweets into Zendesk Support as tickets.

### JSON format

Monitored X handles are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
allow_reply| boolean| true| false| If replies are allowed for this handle
avatar_url| string| true| false| The profile image url of the handle
brand_id| integer| true| false| What brand the handle is associated with
can_reply| boolean| true| false| If replies are allowed for this handle
created_at| string| true| false| The time the handle was created
id| integer| true| true| Automatically assigned upon creation
name| string| true| false| The profile name of the handle
screen_name| string| true| true| The X handle
twitter_user_id| integer| true| true| The country's code
updated_at| string| true| false| The time of the last update of the handle

#### Example


    {  "created_at": "2009-05-13T00:07:08Z",  "id": 211,  "screen_name": "@zendesk",  "twitter_user_id": 67462376832,  "updated_at": "2011-07-22T00:11:12Z"}

### List Monitored X Handles

  * `GET /api/v2/channels/twitter/monitored_twitter_handles`


#### Allowed For

  * Admins
  * Agents


#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/channels/twitter/monitored_twitter_handles.json

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "monitored_twitter_handles": [    {      "created_at": "2009-05-13T00:07:08Z",      "id": 211,      "screen_name": "@zendesk",      "twitter_user_id": 67462376832,      "updated_at": "2011-07-22T00:11:12Z"    },    {      "created_at": "2010-05-13T22:07:08Z",      "id": 431,      "screen_name": "@zendeskops",      "twitter_user_id": 67923318930,      "updated_at": "2011-07-22T00:15:19Z"    }  ]}

### Show Monitored X Handle

  * `GET /api/v2/channels/twitter/monitored_twitter_handles/{monitored_twitter_handle_id}`


#### Allowed For

  * Admins
  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
monitored_twitter_handle_id| integer| Path| true| The ID of the custom agent role

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/channels/twitter/monitored_twitter_handles/{monitored_twitter_handle_id}.json \  -v -u {email_address}:{password}

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "monitored_twitter_handle": {    "created_at": "2010-05-13T22:07:08Z",    "id": 431,    "screen_name": "@zendeskops",    "twitter_user_id": 67923318930,    "updated_at": "2011-07-22T00:15:19Z"  }}

### Create Ticket from Tweet

  * `POST /api/v2/channels/twitter/tickets`


Turns a tweet into a ticket. You must provide the tweet id as well as the id of a monitored X (formerly Twitter) handle configured for your account.

The submitter of the ticket is set to be the user submitting the API request.

#### Allowed For

  * Agents


#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/channels/twitter/tickets.json \  -H "Content-Type: application/json" \  -d '{"ticket": {"twitter_status_message_id": 8605426295771136, "monitored_twitter_handle_id": 45}}' \  -v -u {email_address}:{password} -X POST

#### Example response(s)

**201 Created**


    // Status 201 Created
    null

### List Ticket statuses

  * `GET /api/v2/channels/twitter/tickets/{comment_id}/statuses`


#### Allowed For

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
ids| string| Query| false| Optional comment ids to retrieve tweet information for only particular comments
comment_id| integer| Path| true| The ID of the comment

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/channels/twitter/tickets/{comment_id}/statuses.json \  -v -u {email_address}:{password}

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "statuses": [    {      "favorited": true,      "id": 834,      "retweeted": false,      "user_followed": true    }  ]}

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)