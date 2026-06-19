# Zendesk events

*Source: https://developer.zendesk.com/api-reference/ticketing/users/events-api/zendesk_events/*

---

## On this page

  * [Supported events](/api-reference/ticketing/users/events-api/zendesk_events/#supported-events)
  * [SDK Events](/api-reference/ticketing/users/events-api/zendesk_events/#sdk-events)
  * [Zendesk Guide events](/api-reference/ticketing/users/events-api/zendesk_events/#zendesk-guide-events)
  * [Zendesk Gather events](/api-reference/ticketing/users/events-api/zendesk_events/#zendesk-gather-events)
  * [Zendesk Support events](/api-reference/ticketing/users/events-api/zendesk_events/#zendesk-support-events)


# Zendesk events

## On this page

  * [Supported events](/api-reference/ticketing/users/events-api/zendesk_events/#supported-events)
  * [SDK Events](/api-reference/ticketing/users/events-api/zendesk_events/#sdk-events)
  * [Zendesk Guide events](/api-reference/ticketing/users/events-api/zendesk_events/#zendesk-guide-events)
  * [Zendesk Gather events](/api-reference/ticketing/users/events-api/zendesk_events/#zendesk-gather-events)
  * [Zendesk Support events](/api-reference/ticketing/users/events-api/zendesk_events/#zendesk-support-events)


An event is a description of an activity that has occurred, such as when a userâs name is changed, or when a support request is created. They can be retrieved using the [Events API](/api-reference/ticketing/users/events-api/events-api/), or viewed in the customer context in the [Zendesk Agent Workspace](https://support.zendesk.com/hc/en-us/articles/360001851187).

### Supported events

The following table lists the supported Zendesk events. See the sections below for event details and examples.

Event type| Zendesk product| Description
---|---|---
identity_created| Support| A new identifier was added to a user
identity_changed| Support| A userâs identifier was updated
name_changed| Support| A userâs name was updated
details_changed| Support| A userâs details were updated
notes_changed| Support| A userâs notes were updated
organization_added| Support| An organization was added to the user
organization_removed| Support| An organization was removed from the user
user_merged| Support| A user was merged with another user
user_suspension_changed| Support| A user was suspended
ticket_requested| Support| A Support ticket was requested
ticket_requester_changed| Support| A ticket requester was changed
answers_suggested| Guide| The number of articles suggested to the user while creating a support request
article_instant_search_result_clicked| Guide| The article link was clicked in the help center dropdown search results
article_search_result_clicked| Guide| The article link was clicked in the help center search results
article_viewed| Guide| The help center article was viewed
help_center_searched| Guide| A user searched the help center using the search bar
suggested_article_clicked| Guide| Article suggested to the user was clicked while submitting a support request
article_subscribed| Guide| A user subscribed to an article
article_vote_added| Guide| A user added a vote for an article
article_comment_created| Guide| A user added a comment for an article
community_post_viewed| Gather| A community post was viewed
community_search_result_clicked| Gather| A community post search result was clicked
community_post_created| Gather| A community post was created
community_post_vote_added| Gather| A user added a vote for a community post
community_post_subscribed| Gather| A user subscribed to a community post
community_comment_created| Gather| A user added a comment for a community post
community_comment_vote_added| Gather| A user added a vote for a community post comment
page_view| SDKs| A page was viewed where the Web Widget or SDK is installed

### SDK Events

#### Page viewed

A page was viewed where the Web Widget or SDK is installed. Page views are displayed to agents in the [customer context panel](https://support.zendesk.com/hc/en-us/articles/4408829170458#topic_ehg_1qz_vkb) for Zendesk messaging customers.

##### Rate limits

Page view events are limited to 1,000 events per minute. Any additional page views beyond this limit will not be recorded.

**Example**


    Status 200 OK


    {            "id": "01FY8J3D3X6GWKGR9M14PP6D1Q",            "type": "page_view",            "source": "zendesk",            "description": "",            "created_at": "2022-03-16T05:09:39.328Z",            "received_at": "2022-03-16T05:09:39.593225847Z",            "properties": {                "channel": "web_messenger",                "device_id": "7e124a8b13a24635881812ah6f5188ce",                "referrer": "https://some-website.com/en-us/articles/How-do-I-publish-my-content",                "session_id": "2e40d024khsa498b81452a70bb693b1e9",                "title": "What are these sections?",                "url": "https://some-website.com/en-us/articles/5179514369534-What-are-these-sections",                "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"            }}

The event contains the following unique attributes in the `properties` object:

  * `channel` \- The channel where the event occurred. Values can be "mobile_sdk", "web_widget", "support_sdk" or "web_messenger"
  * `device_id` \- The ID that identifies the end userâs device
  * `referrer` \- The value of the [HTTP Referer header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referer) on the viewed page (if set)
  * `session_id` \- A unique identifier for the user's browsing session. This will be reset when the browser tab is closed or after 30 minutes of inactivity, whichever occurs first.
  * `title` \- The title of the viewed page
  * `url` \- The URL of the viewed page
  * `user_agent` \- The value of the [User-Agent header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent), which is an identifier for the user's browser.


### Zendesk Guide events

#### Answers suggested

Article suggestions when a user submitted a new support request. The support request subject field is used to query suggested articles.

**Example**


    {            "id": "01EADX8ZHNC53NCWV38RWPMPJQ",            "type": "answers_suggested",            "source": "zendesk",            "description": "",            "created_at": "2020-06-10T01:24:53.941314392Z",            "received_at": "2020-06-10T01:24:58.143324138Z",            "properties": {                "result_count": 5,                "search_query": "help"            } }

The event contains the following unique attributes in the `properties` object:

  * `result_count` \- The number of articles suggested to the user when submitting a new support request
  * `search_query` \- The query used to provide suggested articles


#### Article instant search result clicked

A user clicked an article link in the instant search result drop down on the help center page.

**Example**


    {            "id": "01EAGBS4MPC53NCWV38RWPMPJQ",            "type": "article_instant_search_result_clicked",            "source": "zendesk",            "description": "",            "created_at": "2020-06-11T00:16:52.374269872Z",            "received_at": "2020-06-11T00:16:54.973520585Z",            "properties": {                "article_id": 360044308092,                "article": {                    "display_name": "Refund options",                    "url": "url"                 },                "locale": "en-us"            }}

The event contains the following unique attributes in the `properties` object:

  * `article_id` \- The help center article identifier
  * `article.display_name` \- The help center article title
  * `article.url` \- The help center article URL
  * `locale` \- The language used to view the article


#### Article search result clicked

A user clicked on an article appearing in a search result in the help center.

**Example**


    {            "id": "01EADYGJDKC53NCWV38RWPMPJQ",            "type": "article_search_result_clicked",            "source": "zendesk",            "description": "",            "created_at": "2020-06-10T01:46:31.219738419Z",            "received_at": "2020-06-10T01:46:40.114502688Z",            "properties": {                "article_id": 360043980132,                "article": {                    "display_name": "Refund options",                    "url": "url"                 },                "locale": "en-us"            }}

The event contains the following unique attributes in the `properties` object:

  * `article_id` \- The help center article identifier
  * `article.display_name` \- The help center article title
  * `article.url` \- The help center article URL
  * `locale` \- The language used to view the article


#### Article viewed

A user viewed a help center article. Triggered from the help center or mobile SDK.

**Example**


    {            "id": "01EADW2Q2AC53NCWV38RWPMPJQ",            "type": "article_viewed",            "source": "zendesk",            "description": "",            "created_at": "2020-06-10T01:04:00.074320469Z",            "received_at": "2020-06-10T01:04:01.908815098Z",            "properties": {                "article_id": 360043980092,                "article": {                    "display_name": "Refund options",                    "url": "url"                 },                "locale": "en-us",                "channel": "help_center"            }}

The event contains the following unique attributes in the `properties` object:

  * `article_id` \- The help center article identifier
  * `article.display_name` \- The help center article title
  * `article.url` \- The help center article URL
  * `locale` \- The language used to view the article
  * `channel` \- The channel where the event occurred. Values can be "help_center" or "support_sdk"


#### Help center searched

A user searched the help center using the search field. Triggered from the help center or mobile SDK.

**Example**


    {            "id": "01EADXRV4QC53NCWV38RWPMPJQ",            "type": "help_center_searched",            "source": "zendesk",            "description": "",            "created_at": "2020-06-10T01:33:33.71951541Z",            "received_at": "2020-06-10T01:33:41.173895146Z",            "properties": {                "result_count": 5,                "search_query": {                    "locale": "en-us",                    "page": 1,                    "page_size": 10,                    "query": "Help",                    "search_id": "8a8a5a55-df2c-445f-9bbd-eacff9bf83b9",                    "channel": "help_center"                }            }}

The event contains the following unique attributes in the `properties` object:

  * `result_count` \- The number of articles returned from the search request. Applicable to events in the help center.

  * `Search query`:

    * `locale` \- The language used by the user
    * `page` \- The page viewed. Applicable to events in the help center
    * `page_size` \- The number of results displayed on the page. Applicable to events in the help center
    * `query` \- The query entered
    * `search_id` \- A unique identifier of the search query
    * `channel` \- The channel where the event occurred. Values can be "help_center" or "support_sdk"


#### Suggested article clicked

A user clicked on a suggested article while submitting a new support request.

**Example**


    {            "id": "01EADX96YRC53NCWV38RWPMPJQ",            "type": "suggested_article_clicked",            "source": "zendesk",            "description": "",            "created_at": "2020-06-10T01:25:01.528358417Z",            "received_at": "2020-06-10T01:25:06.714429248Z",            "properties": {                "article_id": 360043980132,                "article": {                    "display_name": "Refund options",                    "url": "url"                 },                "locale": "en-us",            }}

The event contains the following unique attributes in the `properties` object:

  * `article_id` \- The help center article identifier
  * `article.display_name` \- The help center article title
  * `article.url` \- The help center article URL
  * `locale` \- The language used to view the article


### Zendesk Gather events

#### Community post viewed

A user clicked on a community post in the help center.

**Example**


    {            "id": "01EADZ7FQRC53NCWV38RWPMPJQ",            "type": "community_post_viewed",            "source": "zendesk",            "description": "",            "created_at": "2020-06-10T01:59:02.135901062Z",            "received_at": "2020-06-10T01:59:07.029595427Z",            "properties": {                "community_post_id": 360067836832            }}

The event contains the following unique attributes in the `properties` object:

  * `community_post_id` \- The community post identifier


#### Community search result clicked

A user clicked on a community post appearing in a search result in the help center.

**Example**


    {            "id": "01EADZ7EPSC53NCWV38RWPMPJQ",            "type": "community_search_result_clicked",            "source": "zendesk",            "description": "",            "created_at": "2020-06-10T01:59:01.08124078Z",            "received_at": "2020-06-10T01:59:06.394860314Z",            "properties": {                "community_post_id": 360067836832            }}

The event contains the following unique attributes in the `properties` object:

  * `community_post_id` \- The community post identifier


### Zendesk Support events

#### Identity created

A userâs identifier was created. The following example shows the userâs phone number as the identifier.

**Example**


    {            "id": "01EAE0WQWZC9BMCD3469B76RJ8",            "type": "identity_created",            "source": "zendesk",            "description": "",            "created_at": "2020-06-10T02:28:07Z",            "received_at": "2020-06-10T02:28:07.201012928Z",            "properties": {                "identity_type": "phone_number",                "value": "0412 123 456"            }}

The event contains the following unique attributes in the `properties` object:

  * `identity_type` \- The type of identifier. Examples include "phone_number" and "email"
  * `value` \- The current assigned identifier value


#### Identity changed

A userâs identifier was updated. The following example shows the userâs email address as the identifier.

**Example**


    {            "id": "01EADVYAW4C9BMCD3469B76RJ8",            "type": "identity_changed",            "source": "zendesk",            "description": "",            "created_at": "2020-06-10T01:01:36Z",            "received_at": "2020-06-10T01:01:36.536097818Z",            "properties": {                "current_value": "janesmith@**Example**.com",                "identity_type": "email",                "previous_value": "johnsmith@**Example**.com"            }        }

The event contains the following unique attributes in the `properties` object:

  * `current_value` \- The previous assigned identifier value
  * `identity_type` \- The type of identifier. Examples include "phone_number" and "email"
  * `previous_value` \- The current assigned identifier value


#### Name changed

A userâs name was updated by the user or by an agent.

**Example**


    {            "id": "01E8XD4VK9C9BMCD3469B76RJ8",            "type": "name_changed",            "source": "zendesk",            "description": "",            "created_at": "2020-05-22T05:19:28Z",            "received_at": "2020-05-22T05:19:28.986762787Z",            "properties": {                "current_value": "Jane Smith",                "previous_value": "John Smith"            }}

The event contains the following unique attributes in the `properties` object:

  * `current_value` \- The current assigned name
  * `previous_value` \- The previous assigned name


#### Details changed

A userâs details was updated.

**Example**


    {            "id": "01E8XD4VK9C9BMCD3469B76RJ8",            "type": "details_changed",            "source": "zendesk",            "description": "",            "created_at": "2020-05-22T05:19:28Z",            "received_at": "2020-05-22T05:19:28.986762787Z",            "properties": {                "current_value": "Jane Smith",                "previous_value": "John Smith"            }}

The event contains the following unique attributes in the `properties` object:

  * `current_value` \- The current assigned details
  * `previous_value` \- The previous assigned details


#### Notes changed

A userâs notes was updated.

**Example**


    {            "id": "01E8XD4VK9C9BMCD3469B76RJ8",            "type": "notes_changed",            "source": "zendesk",            "description": "",            "created_at": "2020-05-22T05:19:28Z",            "received_at": "2020-05-22T05:19:28.986762787Z",            "properties": {                "current_value": "Jane Smith",                "previous_value": "John Smith"            }}

The event contains the following unique attributes in the `properties` object:

  * `current_value` \- The current assigned notes
  * `previous_value` \- The previous assigned notes


#### Organization added

An organization is added to the user

**Example**


    {            "id": "01E8XD4VK9C9BMCD3469B76RJ8",            "type": "organization_added",            "source": "zendesk",            "description": "",            "created_at": "2020-05-22T05:19:28Z",            "received_at": "2020-05-22T05:19:28.986762787Z",            "properties": {                "organization": "BigCo",            }}

The event contains the following unique attributes in the `properties` object:

  * `organization` \- The organization added to the user


#### Organization removed

An organization is removed from the user

**Example**


    {            "id": "01E8XD4VK9C9BMCD3469B76RJ8",            "type": "organization_removed",            "source": "zendesk",            "description": "",            "created_at": "2020-05-22T05:19:28Z",            "received_at": "2020-05-22T05:19:28.986762787Z",            "properties": {                "organization": "BigCo",            }}

The event contains the following unique attributes in the `properties` object:

  * `organization` \- The organization removed from the user


#### User merged

A user is merged with another user

**Example**


    {            "id": "01E8XD4VK9C9BMCD3469B76RJ8",            "type": "user_merged",            "source": "zendesk",            "description": "",            "created_at": "2020-05-22T05:19:28Z",            "received_at": "2020-05-22T05:19:28.986762787Z",            "properties": {                "winner": "Some User",            }}

The event contains the following unique attributes in the `properties` object:

  * `winner` \- The user that the other user was merged with.


#### User suspension changed

A [user's suspension](https://support.zendesk.com/hc/en-us/articles/4408889293978) status changed

**Example**


    {            "id": "01E8XD4VK9C9BMCD3469B76RJ8",            "type": "user_suspension_changed",            "source": "zendesk",            "description": "",            "created_at": "2020-05-22T05:19:28Z",            "received_at": "2020-05-22T05:19:28.986762787Z",            "properties": {                "current_value": "TRUE",                "previous_value": "FALSE"            }}

The event contains the following unique attributes in the `properties` object:

  * `current_value` \- The current suspension status
  * `previous_value` \- The previous suspension status


Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)