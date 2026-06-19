# Side Conversations

*Source: https://developer.zendesk.com/api-reference/ticketing/side_conversation/side_conversation/*

---

## On this page

  * [Download OpenAPI file](/api-reference/ticketing/side_conversation/side_conversation/#download-openapi-file)
  * [JSON format](/api-reference/ticketing/side_conversation/side_conversation/#json-format)
  * [List Side Conversations](/api-reference/ticketing/side_conversation/side_conversation/#list-side-conversations)
  * [Show Side Conversation](/api-reference/ticketing/side_conversation/side_conversation/#show-side-conversation)
  * [Create Side Conversation](/api-reference/ticketing/side_conversation/side_conversation/#create-side-conversation)
  * [Update Side Conversation](/api-reference/ticketing/side_conversation/side_conversation/#update-side-conversation)
  * [Reply to Side Conversation](/api-reference/ticketing/side_conversation/side_conversation/#reply-to-side-conversation)
  * [Import Side Conversation](/api-reference/ticketing/side_conversation/side_conversation/#import-side-conversation)
  * [Import Side Conversation Events](/api-reference/ticketing/side_conversation/side_conversation/#import-side-conversation-events)


# Side Conversations

## On this page

  * [Download OpenAPI file](/api-reference/ticketing/side_conversation/side_conversation/#download-openapi-file)
  * [JSON format](/api-reference/ticketing/side_conversation/side_conversation/#json-format)
  * [List Side Conversations](/api-reference/ticketing/side_conversation/side_conversation/#list-side-conversations)
  * [Show Side Conversation](/api-reference/ticketing/side_conversation/side_conversation/#show-side-conversation)
  * [Create Side Conversation](/api-reference/ticketing/side_conversation/side_conversation/#create-side-conversation)
  * [Update Side Conversation](/api-reference/ticketing/side_conversation/side_conversation/#update-side-conversation)
  * [Reply to Side Conversation](/api-reference/ticketing/side_conversation/side_conversation/#reply-to-side-conversation)
  * [Import Side Conversation](/api-reference/ticketing/side_conversation/side_conversation/#import-side-conversation)
  * [Import Side Conversation Events](/api-reference/ticketing/side_conversation/side_conversation/#import-side-conversation-events)


Side conversations allow agents to send an email to somebody outside the main conversation in a ticket and keep the email messages within the ticket. See [Using side conversations in tickets](https://support.zendesk.com/hc/en-us/articles/360001263308) in the Support Help Center.

Agents can also initiate a side conversation in Slack or Microsoft Teams and keep all the messages in the ticket. See [Using Slack in side conversations](https://support.zendesk.com/hc/en-us/articles/360002115087) or [Using Micosoft Teams in side conversations](https://support.zendesk.com/hc/en-us/articles/5191537451290).

The messages that make up a side conversation are recorded as events. See [Side Conversation Events](/api-reference/ticketing/side_conversation/side_conversation_event/).

The Collaboration add-on is required for side conversations. See [About add-ons (Professional and Enterprise)](https://support.zendesk.com/hc/en-us/articles/217547487).

### Download OpenAPI file

[Download OpenAPI file](/collaboration_api/oas.yaml)

### JSON format

Side Conversation are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
created_at| string| true| false| The time the side conversation was created
external_ids| object| false| false| A key-value store of metadata. All values must be strings
id| string| true| false| Automatically assigned when the side conversation is created
message_added_at| string| true| false| The time of the last message on the side conversation
participants| array| true| false| An array of participants in the side conversation. See [Participants](/api-reference/ticketing/side_conversation/side_conversation/#participants)
preview_text| string| true| false| A plain text text describing the side conversation
state| string| false| false| The state of the side conversation
state_updated_at| string| true| false| The time of the update of the state of the side conversation
subject| string| false| false| The subject of the side conversation
ticket_id| integer| true| false| The parent ticket id of the side conversation
updated_at| string| true| false| The time of the last update of the side conversation
url| string| true| false| The API url of the side conversation

#### Example


    {  "created_at": "2018-11-20T16:58:36.453+00:00",  "external_ids": {    "my_system_id": "abc-123-xyz"  },  "id": "8566255a-ece5-11e8-857d-493066fa7b17",  "message_added_at": "2018-11-20T16:58:36.453+00:00",  "participants": [    {      "email": "[[email protected]](/cdn-cgi/l/email-protection)",      "name": "Johnny Agent",      "user_id": 35436    },    {      "email": "[[email protected]](/cdn-cgi/l/email-protection)",      "name": null,      "user_id": null    }  ],  "preview_text": "I was trying to print an email when the printer suddenly started burning",  "state": "open",  "state_updated_at": "2018-11-20T16:58:36.453+00:00",  "subject": "Help, my printer is on fire!",  "ticket_id": 12345,  "updated_at": "2018-11-20T16:58:36.453+00:00",  "url": "https://company.zendesk.com/api/v2/tickets/1/side_conversations/8566255a-ece5-11e8-857d-493066fa7b17"}

### List Side Conversations

  * `GET /api/v2/tickets/{ticket_id}/side_conversations`


Returns a list of side conversations on the given ticket. If a side conversation is a child ticket, the `external_ids` object's `targetTicketId` property contains the child ticket's id.

You can sideload [side conversation events](/api-reference/ticketing/side_conversation/side_conversation_event/).

#### Allowed for

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
ticket_id| integer| Path| true| The id of the ticket

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/tickets/{ticket_id}/side_conversations.json \-v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/tickets/1/side_conversations"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/tickets/1/side_conversations")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/tickets/1/side_conversations',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/tickets/1/side_conversations"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/tickets/1/side_conversations")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "count": 1,  "next_page": null,  "previous_page": null,  "side_conversations": [    {      "created_at": "2018-11-20T16:58:36.453+00:00",      "external_ids": {        "my_system_id": "abc-123-xyz"      },      "id": "8566255a-ece5-11e8-857d-493066fa7b17",      "message_added_at": "2018-11-20T16:58:36.453+00:00",      "participants": [        {          "email": "[[email protected]](/cdn-cgi/l/email-protection)",          "name": "Johnny Agent",          "user_id": 35436        },        {          "email": "[[email protected]](/cdn-cgi/l/email-protection)",          "name": null,          "user_id": null        }      ],      "preview_text": "I was trying to print an email when the printer suddenly started burning",      "state": "open",      "state_updated_at": "2018-11-20T16:58:36.453+00:00",      "subject": "Help, my printer is on fire!",      "updated_at": "2018-11-20T16:58:36.453+00:00",      "url": "https://company.zendesk.com/api/v2/tickets/1/side_conversations/8566255a-ece5-11e8-857d-493066fa7b17"    }  ]}

### Show Side Conversation

  * `GET /api/v2/tickets/{ticket_id}/side_conversations/{side_conversation_id}`


Returns a side conversation. If the side conversation is a child ticket, the `external_ids` object's `targetTicketId` property contains the child ticket's id.

You can sideload [side conversation events](/api-reference/ticketing/side_conversation/side_conversation_event/).

#### Allowed for

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
side_conversation_id| string| Path| true| The id of the side conversation
ticket_id| integer| Path| true| The id of the ticket

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/tickets/{ticket_id}/side_conversation/{side_conversation_id}.json \-v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/tickets/1/side_conversations/e9ad3991-35e8-445e-a8cc-3d56862cb1f7"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/tickets/1/side_conversations/e9ad3991-35e8-445e-a8cc-3d56862cb1f7")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/tickets/1/side_conversations/e9ad3991-35e8-445e-a8cc-3d56862cb1f7',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/tickets/1/side_conversations/e9ad3991-35e8-445e-a8cc-3d56862cb1f7"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/tickets/1/side_conversations/e9ad3991-35e8-445e-a8cc-3d56862cb1f7")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "side_conversation": {    "created_at": "2018-11-20T16:58:36.453+00:00",    "external_ids": {      "my_system_id": "abc-123-xyz"    },    "id": "8566255a-ece5-11e8-857d-493066fa7b17",    "message_added_at": "2018-11-20T16:58:36.453+00:00",    "participants": [      {        "email": "[[email protected]](/cdn-cgi/l/email-protection)",        "name": "Johnny Agent",        "user_id": 35436      },      {        "email": "[[email protected]](/cdn-cgi/l/email-protection)",        "name": null,        "user_id": null      }    ],    "preview_text": "I was trying to print an email when the printer suddenly started burning",    "state": "open",    "state_updated_at": "2018-11-20T16:58:36.453+00:00",    "subject": "Help, my printer is on fire!",    "updated_at": "2018-11-20T16:58:36.453+00:00",    "url": "https://company.zendesk.com/api/v2/tickets/1/side_conversations/8566255a-ece5-11e8-857d-493066fa7b17"  }}

### Create Side Conversation

  * `POST /api/v2/tickets/{ticket_id}/side_conversations`


Creates a side conversation on the ticket.

#### Allowed for

  * Agents


#### Request Body

Takes a `message` object that specifies the initial message of the side conversation. See [Messages](/api-reference/ticketing/side_conversation/side_conversation_event/#messages).

Example:


    {  "message": {    "subject": "My printer is on fire!",    "body": "The smoke is very colorful.",    "to": [      { "email": "[[email protected]](/cdn-cgi/l/email-protection)" }    ],    "external_ids": { "message-external": "xyz" },    "attachment_ids": ["s3-d2a3111e-26d9-4e1c-88b4-cf7c0649d81d"]  },  "external_ids": { "conversation-external": "zyx" }}

#### Participants

To create a side conversation, the `message` object's `to` property must contain an array of one or more participant objects.

Participant objects support the following properties:

Name| Type| Mandatory| Description
---|---|---|---
user_id| integer| false| If the participant is an agent, the agent's user id
name| string| false| The name of the participant
email| string| false| The email address of the participant
slack_workspace_id| string| false| If the participant is a Slack user or channel, the Slack workspace id
slack_channel_id| string| false| If the participant is a Slack channel, the Slack channel id
support_group_id| string| false| If the participant is a Support ticket, the support group id
support_agent_id| string| false| If the participant is a Support ticket, the support agent id
msteams_channel_id| string| false| If the participant is a Microsoft teams channel, the Teams channel id

#### Side conversation types

The participant object's properties determine the side conversation's type. The following table lists the supported participant properties for each side conversation type.

Side conversation type| Participant object properties| Description
---|---|---
email| user_id| Create an email side conversation using an existing user's id
email| email| Create an email side conversation to an external user's email
email| email, name| Create an email side conversation specifying both email and name of an external user
slack| slack_workspace_id, slack_channel_id| Create a Slack side conversation in a specified channel of a Slack workspace
child ticket| support_group_id| Create a child ticket assigned to a support group
child ticket| support_group_id, support_agent_id| Create a child ticket assigned to a support agent belonging to a specific group
msteams| msteams_channel_id| Create a Microsoft Teams side conversation in a specified Teams channel

You can't mix participant properties from different side conversation types in the `message` object. For example, an email side conversation can't contain participant objects with the `slack_workspace_id` or `support_group_id` properties.

#### Creating an email side conversation

To create an email side conversation, use participant objects with the `user_id` property.


    {  "message": {    "subject": "My printer is on fire!",    "body": "The smoke is very colorful.",    "to": [      {        "user_id": 123      }    ]  }}

Alternatively, use participant objects with following properties:

  * `email`
OR
`email` and `name`




    {  "message": {    "subject": "My printer is on fire!",    "body": "The smoke is very colorful.",    "to": [      {        "email": "[[email protected]](/cdn-cgi/l/email-protection)",        "name": "John Doe"      }    ]  }}

#### Creating a Slack side conversation

To create a Slack side conversation, use participant objects with the `slack_workspace_id` and `slack_channel_id` properties. This creates a Slack side conversation in the specified channel of the Slack workspace.

**Note:** Slack side conversations are only available if an admin has [installed](https://support.zendesk.com/hc/en-us/articles/4408833756698) the latest version of [Slack for Zendesk Support](https://www.zendesk.com/apps/support/slack/) and [enabled side conversations](https://support.zendesk.com/hc/en-us/articles/4408832279962-Enabling-and-disabling-side-conversations).


    {  "message": {    "subject": "My printer is on fire!",    "body": "The smoke is very colorful.",    "to": [      {        "slack_workspace_id": "T123ABC",        "slack_channel_id": "C456DEF"      }    ]  }}

#### Creating a child ticket side conversation

To create a child ticket side conversation, use participant objects with the `support_group_id` property. This creates a child ticket assigned to the specified Support group.


    {  "message": {    "subject": "My printer is on fire!",    "body": "The smoke is very colorful.",    "to": [      {        "support_group_id": 123      }    ]  }}

Alternatively, use participant objects with the `support_group_id` and `support_agent_id` properties. This creates a child ticket assigned to the specified agent in the Support group.


    {  "message": {    "subject": "My printer is on fire!",    "body": "The smoke is very colorful.",    "to": [      {        "support_group_id": 123,        "support_agent_id": 456      }    ]  }}

#### Creating a Microsoft Teams side conversation

To create a Microsoft Teams side conversation, use participant objects with the `msteams_channel_id` property. This creates a Teams side conversation in the specified channel.

**Note:** Microsoft Teams side conversations are only available if a Zendesk admin has [installed](https://zendeskforteams.com/installation-guide) the latest version of [Microsoft Teams for Support](https://www.zendesk.com/marketplace/apps/support/767198/microsoft-teams-for-support/) and [enabled side conversations](https://support.zendesk.com/hc/en-us/articles/4408832279962-Enabling-and-disabling-side-conversations).


    {  "message": {    "subject": "My printer is on fire!",    "body": "The smoke is very colorful.",    "to": [      {        "msteams_channel_id": "19:[[email protected]](/cdn-cgi/l/email-protection)"      }    ]  }}

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
ticket_id| integer| Path| true| The id of the ticket

#### Example body


    {  "message": {    "body": "The smoke is very colorful.",    "subject": "My printer is on fire!",    "to": [      {        "email": "[[email protected]](/cdn-cgi/l/email-protection)"      }    ]  }}

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/tickets/42/side_conversations.json \-d '{"message": {"subject": "My printer is on fire!", "body": "The smoke is very colorful.", "to": [{"email": "[[email protected]](/cdn-cgi/l/email-protection)"}], "attachment_ids": ["s3-d2a3111e-26d9-4e1c-88b4-cf7c0649d81d"]}' \-H "Content-Type: application/json" -v -u {email_address}/token:{api_token} -X POST

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://support.zendesk.com/api/v2/tickets/1/side_conversations"	method := "POST"	payload := strings.NewReader(`{  "message": {    "body": "The smoke is very colorful.",    "subject": "My printer is on fire!",    "to": [      {        "email": "[[email protected]](/cdn-cgi/l/email-protection)"      }    ]  }}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/tickets/1/side_conversations")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"message\": {    \"body\": \"The smoke is very colorful.\",    \"subject\": \"My printer is on fire!\",    \"to\": [      {        \"email\": \"someone@example.com\"      }    ]  }}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "message": {    "body": "The smoke is very colorful.",    "subject": "My printer is on fire!",    "to": [      {        "email": "[[email protected]](/cdn-cgi/l/email-protection)"      }    ]  }});
    var config = {  method: 'POST',  url: 'https://support.zendesk.com/api/v2/tickets/1/side_conversations',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/tickets/1/side_conversations"
    payload = json.loads("""{  "message": {    "body": "The smoke is very colorful.",    "subject": "My printer is on fire!",    "to": [      {        "email": "[[email protected]](/cdn-cgi/l/email-protection)"      }    ]  }}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/tickets/1/side_conversations")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")request.body = %q({  "message": {    "body": "The smoke is very colorful.",    "subject": "My printer is on fire!",    "to": [      {        "email": "[[email protected]](/cdn-cgi/l/email-protection)"      }    ]  }})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**201 Created**


    // Status 201 Created
    {  "event": {    "actor": {      "email": "[[email protected]](/cdn-cgi/l/email-protection)",      "name": "Agent Sally",      "user_id": 2    },    "created_at": "2017-10-27T17:56:16.678Z",    "id": "9e19e100-abd5-11e8-b66e-af698c6d193c",    "message": {      "attachments": [        {          "content_type": "image/png",          "content_url": "http://www.example.com/api/v2/tickets/42/side_conversations/8566255a-ece5-11e8-857d-493066fa7b17/attachments/s3-d2a3111e-26d9-4e1c-88b4-cf7c0649d81d/download/image.png",          "file_name": "image.png",          "height": 214,          "id": "s3-d2a3111e-26d9-4e1c-88b4-cf7c0649d81d",          "inline": false,          "size": 50645,          "width": 406        }      ],      "body": "The smoke is very colorful.",      "external_ids": {        "message-external": "xyz"      },      "from": {        "email": "[[email protected]](/cdn-cgi/l/email-protection)",        "name": "Agent Sally",        "user_id": 2      },      "html_body": "<div class=\"zd-comment\"><p>The smoke is very colorful.</p></div>",      "preview_text": "My printer is on fire!",      "subject": "My printer is on fire!",      "to": [        {          "email": "[[email protected]](/cdn-cgi/l/email-protection)",          "name": null,          "user_id": null        }      ]    },    "side_conversation_id": "8566255a-ece5-11e8-857d-493066fa7b17",    "type": "create",    "via": "api"  },  "side_conversation": {    "created_at": "2018-11-20T16:58:36.453+00:00",    "external_ids": {      "my_system_id": "abc-123-xyz"    },    "id": "8566255a-ece5-11e8-857d-493066fa7b17",    "message_added_at": "2018-11-20T16:58:36.453+00:00",    "participants": [      {        "email": "[[email protected]](/cdn-cgi/l/email-protection)",        "name": "Johnny Agent",        "user_id": 35436      },      {        "email": "[[email protected]](/cdn-cgi/l/email-protection)",        "name": null,        "user_id": null      }    ],    "preview_text": "I was trying to print an email when the printer suddenly started burning",    "state": "open",    "state_updated_at": "2018-11-20T16:58:36.453+00:00",    "subject": "Help, my printer is on fire!",    "updated_at": "2018-11-20T16:58:36.453+00:00",    "url": "https://company.zendesk.com/api/v2/tickets/1/side_conversations/8566255a-ece5-11e8-857d-493066fa7b17"  },  "updates": {}}

### Update Side Conversation

  * `PUT /api/v2/tickets/{ticket_id}/side_conversations/{side_conversation_id}`


Updates the state or subject of the side conversation.

#### Allowed for

  * Agents


#### Request Body

The request takes one parameter, a `side_conversation` object that lists the values to update. All properties are optional.

Name| Description
---|---
state| The new state of the side conversation. Possible values: "open", "closed"
subject| The subject of the side conversation

Example:


    {   "side_conversation": {     "state":  "closed"   }}

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
side_conversation_id| string| Path| true| The id of the side conversation
ticket_id| integer| Path| true| The id of the ticket

#### Example body


    {  "side_conversation": {    "created_at": "2018-11-20T16:58:36.453+00:00",    "external_ids": {      "my_system_id": "abc-123-xyz"    },    "id": "8566255a-ece5-11e8-857d-493066fa7b17",    "message_added_at": "2018-11-20T16:58:36.453+00:00",    "participants": [      {        "email": "[[email protected]](/cdn-cgi/l/email-protection)",        "name": "Johnny Agent",        "user_id": 35436      },      {        "email": "[[email protected]](/cdn-cgi/l/email-protection)",        "name": null,        "user_id": null      }    ],    "preview_text": "I was trying to print an email when the printer suddenly started burning",    "state": "open",    "state_updated_at": "2018-11-20T16:58:36.453+00:00",    "subject": "Help, my printer is on fire!",    "updated_at": "2018-11-20T16:58:36.453+00:00",    "url": "https://company.zendesk.com/api/v2/tickets/1/side_conversations/8566255a-ece5-11e8-857d-493066fa7b17"  }}

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/tickets/42/side_conversations/8566255a-ece5-11e8-857d-493066fa7b17.json \  -d '{"side_conversation": {"state": "closed"}}' \  -H "Content-Type: application/json" \  -v -u {email_address}/token:{api_token} -X PUT

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://support.zendesk.com/api/v2/tickets/1/side_conversations/e9ad3991-35e8-445e-a8cc-3d56862cb1f7"	method := "PUT"	payload := strings.NewReader(`{  "side_conversation": {    "created_at": "2018-11-20T16:58:36.453+00:00",    "external_ids": {      "my_system_id": "abc-123-xyz"    },    "id": "8566255a-ece5-11e8-857d-493066fa7b17",    "message_added_at": "2018-11-20T16:58:36.453+00:00",    "participants": [      {        "email": "[[email protected]](/cdn-cgi/l/email-protection)",        "name": "Johnny Agent",        "user_id": 35436      },      {        "email": "[[email protected]](/cdn-cgi/l/email-protection)",        "name": null,        "user_id": null      }    ],    "preview_text": "I was trying to print an email when the printer suddenly started burning",    "state": "open",    "state_updated_at": "2018-11-20T16:58:36.453+00:00",    "subject": "Help, my printer is on fire!",    "updated_at": "2018-11-20T16:58:36.453+00:00",    "url": "https://company.zendesk.com/api/v2/tickets/1/side_conversations/8566255a-ece5-11e8-857d-493066fa7b17"  }}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/tickets/1/side_conversations/e9ad3991-35e8-445e-a8cc-3d56862cb1f7")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"side_conversation\": {    \"created_at\": \"2018-11-20T16:58:36.453+00:00\",    \"external_ids\": {      \"my_system_id\": \"abc-123-xyz\"    },    \"id\": \"8566255a-ece5-11e8-857d-493066fa7b17\",    \"message_added_at\": \"2018-11-20T16:58:36.453+00:00\",    \"participants\": [      {        \"email\": \"johnny@example.com\",        \"name\": \"Johnny Agent\",        \"user_id\": 35436      },      {        \"email\": \"bob@example.com\",        \"name\": null,        \"user_id\": null      }    ],    \"preview_text\": \"I was trying to print an email when the printer suddenly started burning\",    \"state\": \"open\",    \"state_updated_at\": \"2018-11-20T16:58:36.453+00:00\",    \"subject\": \"Help, my printer is on fire!\",    \"updated_at\": \"2018-11-20T16:58:36.453+00:00\",    \"url\": \"https://company.zendesk.com/api/v2/tickets/1/side_conversations/8566255a-ece5-11e8-857d-493066fa7b17\"  }}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "side_conversation": {    "created_at": "2018-11-20T16:58:36.453+00:00",    "external_ids": {      "my_system_id": "abc-123-xyz"    },    "id": "8566255a-ece5-11e8-857d-493066fa7b17",    "message_added_at": "2018-11-20T16:58:36.453+00:00",    "participants": [      {        "email": "[[email protected]](/cdn-cgi/l/email-protection)",        "name": "Johnny Agent",        "user_id": 35436      },      {        "email": "[[email protected]](/cdn-cgi/l/email-protection)",        "name": null,        "user_id": null      }    ],    "preview_text": "I was trying to print an email when the printer suddenly started burning",    "state": "open",    "state_updated_at": "2018-11-20T16:58:36.453+00:00",    "subject": "Help, my printer is on fire!",    "updated_at": "2018-11-20T16:58:36.453+00:00",    "url": "https://company.zendesk.com/api/v2/tickets/1/side_conversations/8566255a-ece5-11e8-857d-493066fa7b17"  }});
    var config = {  method: 'PUT',  url: 'https://support.zendesk.com/api/v2/tickets/1/side_conversations/e9ad3991-35e8-445e-a8cc-3d56862cb1f7',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/tickets/1/side_conversations/e9ad3991-35e8-445e-a8cc-3d56862cb1f7"
    payload = json.loads("""{  "side_conversation": {    "created_at": "2018-11-20T16:58:36.453+00:00",    "external_ids": {      "my_system_id": "abc-123-xyz"    },    "id": "8566255a-ece5-11e8-857d-493066fa7b17",    "message_added_at": "2018-11-20T16:58:36.453+00:00",    "participants": [      {        "email": "[[email protected]](/cdn-cgi/l/email-protection)",        "name": "Johnny Agent",        "user_id": 35436      },      {        "email": "[[email protected]](/cdn-cgi/l/email-protection)",        "name": null,        "user_id": null      }    ],    "preview_text": "I was trying to print an email when the printer suddenly started burning",    "state": "open",    "state_updated_at": "2018-11-20T16:58:36.453+00:00",    "subject": "Help, my printer is on fire!",    "updated_at": "2018-11-20T16:58:36.453+00:00",    "url": "https://company.zendesk.com/api/v2/tickets/1/side_conversations/8566255a-ece5-11e8-857d-493066fa7b17"  }}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/tickets/1/side_conversations/e9ad3991-35e8-445e-a8cc-3d56862cb1f7")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")request.body = %q({  "side_conversation": {    "created_at": "2018-11-20T16:58:36.453+00:00",    "external_ids": {      "my_system_id": "abc-123-xyz"    },    "id": "8566255a-ece5-11e8-857d-493066fa7b17",    "message_added_at": "2018-11-20T16:58:36.453+00:00",    "participants": [      {        "email": "[[email protected]](/cdn-cgi/l/email-protection)",        "name": "Johnny Agent",        "user_id": 35436      },      {        "email": "[[email protected]](/cdn-cgi/l/email-protection)",        "name": null,        "user_id": null      }    ],    "preview_text": "I was trying to print an email when the printer suddenly started burning",    "state": "open",    "state_updated_at": "2018-11-20T16:58:36.453+00:00",    "subject": "Help, my printer is on fire!",    "updated_at": "2018-11-20T16:58:36.453+00:00",    "url": "https://company.zendesk.com/api/v2/tickets/1/side_conversations/8566255a-ece5-11e8-857d-493066fa7b17"  }})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "side_conversation": {    "created_at": "2018-11-20T16:58:36.453+00:00",    "external_ids": {      "my_system_id": "abc-123-xyz"    },    "id": "8566255a-ece5-11e8-857d-493066fa7b17",    "message_added_at": "2018-11-20T16:58:36.453+00:00",    "participants": [      {        "email": "[[email protected]](/cdn-cgi/l/email-protection)",        "name": "Johnny Agent",        "user_id": 35436      },      {        "email": "[[email protected]](/cdn-cgi/l/email-protection)",        "name": null,        "user_id": null      }    ],    "preview_text": "I was trying to print an email when the printer suddenly started burning",    "state": "open",    "state_updated_at": "2018-11-20T16:58:36.453+00:00",    "subject": "Help, my printer is on fire!",    "updated_at": "2018-11-20T16:58:36.453+00:00",    "url": "https://company.zendesk.com/api/v2/tickets/1/side_conversations/8566255a-ece5-11e8-857d-493066fa7b17"  }}

### Reply to Side Conversation

  * `POST /api/v2/tickets/{ticket_id}/side_conversations/{side_conversation_id}/reply`


Replies to a side conversation.

#### Allowed For

  * Agents


#### Request Body

Takes a `message` object that specifies the message to add to the side conversation. See [Messages](/api-reference/ticketing/side_conversation/side_conversation_event/#messages).

Example:


    {    "message": {    "subject": "My printer is on fire!",    "body":    "The smoke is very colorful.",    "to": [      { "email": "[[email protected]](/cdn-cgi/l/email-protection)" }    ]  }}

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
side_conversation_id| string| Path| true| The id of the side conversation
ticket_id| integer| Path| true| The id of the ticket

#### Example body


    {  "message": {    "body": "The smoke is very colorful.",    "subject": "My printer is on fire!",    "to": [      {        "email": "[[email protected]](/cdn-cgi/l/email-protection)"      }    ]  }}

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/tickets/42/side_conversations/8566255a-ece5-11e8-857d-493066fa7b17/reply.json \  -d '{"message": {"subject": "My printer is on fire!", "body": "The smoke is very colorful.", "to": [{"email": "[[email protected]](/cdn-cgi/l/email-protection)"}], "attachment_ids": ["s3-d2a3111e-26d9-4e1c-88b4-cf7c0649d81d"]}' \  -H "Content-Type: application/json" -v -u {email_address}/token:{api_token} -X POST

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://support.zendesk.com/api/v2/tickets/1/side_conversations/e9ad3991-35e8-445e-a8cc-3d56862cb1f7/reply"	method := "POST"	payload := strings.NewReader(`{  "message": {    "body": "The smoke is very colorful.",    "subject": "My printer is on fire!",    "to": [      {        "email": "[[email protected]](/cdn-cgi/l/email-protection)"      }    ]  }}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/tickets/1/side_conversations/e9ad3991-35e8-445e-a8cc-3d56862cb1f7/reply")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"message\": {    \"body\": \"The smoke is very colorful.\",    \"subject\": \"My printer is on fire!\",    \"to\": [      {        \"email\": \"someone@example.com\"      }    ]  }}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "message": {    "body": "The smoke is very colorful.",    "subject": "My printer is on fire!",    "to": [      {        "email": "[[email protected]](/cdn-cgi/l/email-protection)"      }    ]  }});
    var config = {  method: 'POST',  url: 'https://support.zendesk.com/api/v2/tickets/1/side_conversations/e9ad3991-35e8-445e-a8cc-3d56862cb1f7/reply',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/tickets/1/side_conversations/e9ad3991-35e8-445e-a8cc-3d56862cb1f7/reply"
    payload = json.loads("""{  "message": {    "body": "The smoke is very colorful.",    "subject": "My printer is on fire!",    "to": [      {        "email": "[[email protected]](/cdn-cgi/l/email-protection)"      }    ]  }}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/tickets/1/side_conversations/e9ad3991-35e8-445e-a8cc-3d56862cb1f7/reply")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")request.body = %q({  "message": {    "body": "The smoke is very colorful.",    "subject": "My printer is on fire!",    "to": [      {        "email": "[[email protected]](/cdn-cgi/l/email-protection)"      }    ]  }})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "side_conversation": {    "created_at": "2018-11-20T16:58:36.453+00:00",    "external_ids": {      "my_system_id": "abc-123-xyz"    },    "id": "8566255a-ece5-11e8-857d-493066fa7b17",    "message_added_at": "2018-11-20T16:58:36.453+00:00",    "participants": [      {        "email": "[[email protected]](/cdn-cgi/l/email-protection)",        "name": "Johnny Agent",        "user_id": 35436      },      {        "email": "[[email protected]](/cdn-cgi/l/email-protection)",        "name": null,        "user_id": null      }    ],    "preview_text": "I was trying to print an email when the printer suddenly started burning",    "state": "open",    "state_updated_at": "2018-11-20T16:58:36.453+00:00",    "subject": "Help, my printer is on fire!",    "updated_at": "2018-11-20T16:58:36.453+00:00",    "url": "https://company.zendesk.com/api/v2/tickets/1/side_conversations/8566255a-ece5-11e8-857d-493066fa7b17"  }}

### Import Side Conversation

  * `POST /api/v2/tickets/{ticket_id}/side_conversations/import`


Imports a side conversation on the ticket.

#### Allowed for

  * Agents


#### Request Body

Takes a `side_conversation` object and an `events` array of [side conversation events](/api-reference/ticketing/side_conversation/side_conversation_event/).

Example:


    {  "side_conversation": {    "subject": "I have problems",    "state": "open",    "external_ids": {      "threadExternalId": "thread-external"    }  },  "events": [    {      "created_at": "2022-10-05T20:47:02.230Z",      "message": {        "subject": "My printer is on fire!",        "body": "The smoke is very colorful.",        "to": [          { "email": "[[email protected]](/cdn-cgi/l/email-protection)" }        ],        "from": { "email": "[[email protected]](/cdn-cgi/l/email-protection)" },        "external_ids": { "message-external": "xyz" },        "attachment_ids": ["s3-d2a3111e-26d9-4e1c-88b4-cf7c0649d81d"]      }    }  ]}

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
ticket_id| integer| Path| true| The id of the ticket

#### Example body


    {  "events": [    {      "created_at": "2022-10-05T20:47:02.23Z",      "message": {        "body": "The smoke is very colorful.",        "from": {          "email": "[[email protected]](/cdn-cgi/l/email-protection)"        },        "subject": "My printer is on fire!",        "to": [          {            "email": "[[email protected]](/cdn-cgi/l/email-protection)"          }        ]      }    }  ],  "side_conversation": {    "external_ids": {      "threadExternalId": "thread-external"    },    "state": "open",    "subject": "I have problems"  }}

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/tickets/{ticket_id}/side_conversations/import.json \  -v -u {email_address}/token:{api_token} -X POST \  -H "Content-Type: application/json" \  -d '{        "side_conversation": {          "subject": "My printer is on fire!",          "state": "open",          "external_ids": {            "threadExternalId": "thread-external"          }        },      "events": [        {          "created_at": "2022-10-05T20:47:02.230Z",          "message": {            "subject": "My printer is on fire!",            "body": "The smoke is very colorful.",            "to": [{ "email": "[[email protected]](/cdn-cgi/l/email-protection)" }],            "from": { "email": "[[email protected]](/cdn-cgi/l/email-protection)" }          }        }      ]    }'

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://support.zendesk.com/api/v2/tickets/1/side_conversations/import"	method := "POST"	payload := strings.NewReader(`{  "events": [    {      "created_at": "2022-10-05T20:47:02.23Z",      "message": {        "body": "The smoke is very colorful.",        "from": {          "email": "[[email protected]](/cdn-cgi/l/email-protection)"        },        "subject": "My printer is on fire!",        "to": [          {            "email": "[[email protected]](/cdn-cgi/l/email-protection)"          }        ]      }    }  ],  "side_conversation": {    "external_ids": {      "threadExternalId": "thread-external"    },    "state": "open",    "subject": "I have problems"  }}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/tickets/1/side_conversations/import")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"events\": [    {      \"created_at\": \"2022-10-05T20:47:02.23Z\",      \"message\": {        \"body\": \"The smoke is very colorful.\",        \"from\": {          \"email\": \"someone-else@example.com\"        },        \"subject\": \"My printer is on fire!\",        \"to\": [          {            \"email\": \"someone@example.com\"          }        ]      }    }  ],  \"side_conversation\": {    \"external_ids\": {      \"threadExternalId\": \"thread-external\"    },    \"state\": \"open\",    \"subject\": \"I have problems\"  }}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "events": [    {      "created_at": "2022-10-05T20:47:02.23Z",      "message": {        "body": "The smoke is very colorful.",        "from": {          "email": "[[email protected]](/cdn-cgi/l/email-protection)"        },        "subject": "My printer is on fire!",        "to": [          {            "email": "[[email protected]](/cdn-cgi/l/email-protection)"          }        ]      }    }  ],  "side_conversation": {    "external_ids": {      "threadExternalId": "thread-external"    },    "state": "open",    "subject": "I have problems"  }});
    var config = {  method: 'POST',  url: 'https://support.zendesk.com/api/v2/tickets/1/side_conversations/import',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/tickets/1/side_conversations/import"
    payload = json.loads("""{  "events": [    {      "created_at": "2022-10-05T20:47:02.23Z",      "message": {        "body": "The smoke is very colorful.",        "from": {          "email": "[[email protected]](/cdn-cgi/l/email-protection)"        },        "subject": "My printer is on fire!",        "to": [          {            "email": "[[email protected]](/cdn-cgi/l/email-protection)"          }        ]      }    }  ],  "side_conversation": {    "external_ids": {      "threadExternalId": "thread-external"    },    "state": "open",    "subject": "I have problems"  }}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/tickets/1/side_conversations/import")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")request.body = %q({  "events": [    {      "created_at": "2022-10-05T20:47:02.23Z",      "message": {        "body": "The smoke is very colorful.",        "from": {          "email": "[[email protected]](/cdn-cgi/l/email-protection)"        },        "subject": "My printer is on fire!",        "to": [          {            "email": "[[email protected]](/cdn-cgi/l/email-protection)"          }        ]      }    }  ],  "side_conversation": {    "external_ids": {      "threadExternalId": "thread-external"    },    "state": "open",    "subject": "I have problems"  }})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**201 Created**


    // Status 201 Created
    {  "event": {    "actor": {      "email": "[[email protected]](/cdn-cgi/l/email-protection)",      "name": "Agent Sally",      "user_id": 2    },    "created_at": "2017-10-27T17:56:16.678Z",    "id": "9e19e100-abd5-11e8-b66e-af698c6d193c",    "message": {      "attachments": [        {          "content_type": "image/png",          "content_url": "http://www.example.com/api/v2/tickets/42/side_conversations/8566255a-ece5-11e8-857d-493066fa7b17/attachments/s3-d2a3111e-26d9-4e1c-88b4-cf7c0649d81d/download/image.png",          "file_name": "image.png",          "height": 214,          "id": "s3-d2a3111e-26d9-4e1c-88b4-cf7c0649d81d",          "inline": false,          "size": 50645,          "width": 406        }      ],      "body": "The smoke is very colorful.",      "external_ids": {        "message-external": "xyz"      },      "from": {        "email": "[[email protected]](/cdn-cgi/l/email-protection)",        "name": "Agent Sally",        "user_id": 2      },      "html_body": "<div class=\"zd-comment\"><p>The smoke is very colorful.</p></div>",      "preview_text": "My printer is on fire!",      "subject": "My printer is on fire!",      "to": [        {          "email": "[[email protected]](/cdn-cgi/l/email-protection)",          "name": null,          "user_id": null        }      ]    },    "side_conversation_id": "8566255a-ece5-11e8-857d-493066fa7b17",    "type": "create",    "via": "api"  },  "side_conversation": {    "created_at": "2018-11-20T16:58:36.453+00:00",    "external_ids": {      "my_system_id": "abc-123-xyz"    },    "id": "8566255a-ece5-11e8-857d-493066fa7b17",    "message_added_at": "2018-11-20T16:58:36.453+00:00",    "participants": [      {        "email": "[[email protected]](/cdn-cgi/l/email-protection)",        "name": "Johnny Agent",        "user_id": 35436      },      {        "email": "[[email protected]](/cdn-cgi/l/email-protection)",        "name": null,        "user_id": null      }    ],    "preview_text": "I was trying to print an email when the printer suddenly started burning",    "state": "open",    "state_updated_at": "2018-11-20T16:58:36.453+00:00",    "subject": "Help, my printer is on fire!",    "updated_at": "2018-11-20T16:58:36.453+00:00",    "url": "https://company.zendesk.com/api/v2/tickets/1/side_conversations/8566255a-ece5-11e8-857d-493066fa7b17"  },  "updates": {}}

### Import Side Conversation Events

  * `POST /api/v2/tickets/{ticket_id}/side_conversations/{side_conversation_id}/events/import`


Imports events to an existing side conversation.

#### Allowed for

  * Agents


#### Request Body

Takes an `events` array of [side conversation events](/api-reference/ticketing/side_conversation/side_conversation_event/).

Example:


    {  "events": [    {      "message": {        "subject": "My printer is on fire!",        "body": "The smoke is very colorful.",        "to": [          { "email": "[[email protected]](/cdn-cgi/l/email-protection)" }        ],        "from": { "email": "[[email protected]](/cdn-cgi/l/email-protection)" },        "external_ids": { "message-external": "xyz" },        "attachment_ids": ["s3-d2a3111e-26d9-4e1c-88b4-cf7c0649d81d"]      },      "created_at": "2022-10-05T20:47:02.230Z"    }  ]}

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
side_conversation_id| string| Path| true| The id of the side conversation
ticket_id| integer| Path| true| The id of the ticket

#### Example body


    {  "events": [    {      "created_at": "2022-10-05T20:47:02.230Z",      "message": {        "body": "The smoke is very colorful.",        "from": {          "email": "[[email protected]](/cdn-cgi/l/email-protection)"        },        "subject": "My printer is on fire!",        "to": [          {            "email": "[[email protected]](/cdn-cgi/l/email-protection)"          }        ]      }    }  ]}

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/tickets/{ticket_id}/side_conversations/{side_conversation_id}/events/import.json \  -v -u {email_address}/token:{api_token} -X POST \  -H "Content-Type: application/json" \  -d '{    "events": [      {        "created_at": "2022-10-05T20:47:02.230Z",        "message": {          "subject": "My printer is on fire!",          "body": "The smoke is very colorful.",          "to": [{ "email": "[[email protected]](/cdn-cgi/l/email-protection)" }],          "from": { "email": "[[email protected]](/cdn-cgi/l/email-protection)" }        }      }    ]  }'

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://support.zendesk.com/api/v2/tickets/1/side_conversations/e9ad3991-35e8-445e-a8cc-3d56862cb1f7/events/import"	method := "POST"	payload := strings.NewReader(`{  "events": [    {      "created_at": "2022-10-05T20:47:02.230Z",      "message": {        "body": "The smoke is very colorful.",        "from": {          "email": "[[email protected]](/cdn-cgi/l/email-protection)"        },        "subject": "My printer is on fire!",        "to": [          {            "email": "[[email protected]](/cdn-cgi/l/email-protection)"          }        ]      }    }  ]}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/tickets/1/side_conversations/e9ad3991-35e8-445e-a8cc-3d56862cb1f7/events/import")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"events\": [    {      \"created_at\": \"2022-10-05T20:47:02.230Z\",      \"message\": {        \"body\": \"The smoke is very colorful.\",        \"from\": {          \"email\": \"someone-else@example.com\"        },        \"subject\": \"My printer is on fire!\",        \"to\": [          {            \"email\": \"someone@example.com\"          }        ]      }    }  ]}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "events": [    {      "created_at": "2022-10-05T20:47:02.230Z",      "message": {        "body": "The smoke is very colorful.",        "from": {          "email": "[[email protected]](/cdn-cgi/l/email-protection)"        },        "subject": "My printer is on fire!",        "to": [          {            "email": "[[email protected]](/cdn-cgi/l/email-protection)"          }        ]      }    }  ]});
    var config = {  method: 'POST',  url: 'https://support.zendesk.com/api/v2/tickets/1/side_conversations/e9ad3991-35e8-445e-a8cc-3d56862cb1f7/events/import',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/tickets/1/side_conversations/e9ad3991-35e8-445e-a8cc-3d56862cb1f7/events/import"
    payload = json.loads("""{  "events": [    {      "created_at": "2022-10-05T20:47:02.230Z",      "message": {        "body": "The smoke is very colorful.",        "from": {          "email": "[[email protected]](/cdn-cgi/l/email-protection)"        },        "subject": "My printer is on fire!",        "to": [          {            "email": "[[email protected]](/cdn-cgi/l/email-protection)"          }        ]      }    }  ]}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/tickets/1/side_conversations/e9ad3991-35e8-445e-a8cc-3d56862cb1f7/events/import")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")request.body = %q({  "events": [    {      "created_at": "2022-10-05T20:47:02.230Z",      "message": {        "body": "The smoke is very colorful.",        "from": {          "email": "[[email protected]](/cdn-cgi/l/email-protection)"        },        "subject": "My printer is on fire!",        "to": [          {            "email": "[[email protected]](/cdn-cgi/l/email-protection)"          }        ]      }    }  ]})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**201 Created**


    // Status 201 Created
    {  "event": {    "actor": {      "email": "[[email protected]](/cdn-cgi/l/email-protection)",      "name": "Agent Sally",      "user_id": 2    },    "created_at": "2017-10-27T17:56:16.678Z",    "id": "9e19e100-abd5-11e8-b66e-af698c6d193c",    "message": {      "attachments": [        {          "content_type": "image/png",          "content_url": "http://www.example.com/api/v2/tickets/42/side_conversations/8566255a-ece5-11e8-857d-493066fa7b17/attachments/s3-d2a3111e-26d9-4e1c-88b4-cf7c0649d81d/download/image.png",          "file_name": "image.png",          "height": 214,          "id": "s3-d2a3111e-26d9-4e1c-88b4-cf7c0649d81d",          "inline": false,          "size": 50645,          "width": 406        }      ],      "body": "The smoke is very colorful.",      "external_ids": {        "message-external": "xyz"      },      "from": {        "email": "[[email protected]](/cdn-cgi/l/email-protection)",        "name": "Agent Sally",        "user_id": 2      },      "html_body": "<div class=\"zd-comment\"><p>The smoke is very colorful.</p></div>",      "preview_text": "My printer is on fire!",      "subject": "My printer is on fire!",      "to": [        {          "email": "[[email protected]](/cdn-cgi/l/email-protection)",          "name": null,          "user_id": null        }      ]    },    "side_conversation_id": "8566255a-ece5-11e8-857d-493066fa7b17",    "type": "create",    "via": "api"  },  "side_conversation": {    "created_at": "2018-11-20T16:58:36.453+00:00",    "external_ids": {      "my_system_id": "abc-123-xyz"    },    "id": "8566255a-ece5-11e8-857d-493066fa7b17",    "message_added_at": "2018-11-20T16:58:36.453+00:00",    "participants": [      {        "email": "[[email protected]](/cdn-cgi/l/email-protection)",        "name": "Johnny Agent",        "user_id": 35436      },      {        "email": "[[email protected]](/cdn-cgi/l/email-protection)",        "name": null,        "user_id": null      }    ],    "preview_text": "I was trying to print an email when the printer suddenly started burning",    "state": "open",    "state_updated_at": "2018-11-20T16:58:36.453+00:00",    "subject": "Help, my printer is on fire!",    "updated_at": "2018-11-20T16:58:36.453+00:00",    "url": "https://company.zendesk.com/api/v2/tickets/1/side_conversations/8566255a-ece5-11e8-857d-493066fa7b17"  },  "updates": {}}

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)