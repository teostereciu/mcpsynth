# Side Conversation Events

*Source: https://developer.zendesk.com/api-reference/ticketing/side_conversation/side_conversation_event/*

---

## On this page

  * [JSON format](/api-reference/ticketing/side_conversation/side_conversation_event/#json-format)
  * [List Side Conversation Events](/api-reference/ticketing/side_conversation/side_conversation_event/#list-side-conversation-events)
  * [Incremental Side Conversation Event Export](/api-reference/ticketing/side_conversation/side_conversation_event/#incremental-side-conversation-event-export)


# Side Conversation Events

## On this page

  * [JSON format](/api-reference/ticketing/side_conversation/side_conversation_event/#json-format)
  * [List Side Conversation Events](/api-reference/ticketing/side_conversation/side_conversation_event/#list-side-conversation-events)
  * [Incremental Side Conversation Event Export](/api-reference/ticketing/side_conversation/side_conversation_event/#incremental-side-conversation-event-export)


The messages that make up a [side conversation](/api-reference/ticketing/side_conversation/side_conversation/) are recorded as events.

### JSON format

Side Conversation Events are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
actor| object| true| false| The participant who created the event. See [Participants](/api-reference/ticketing/side_conversation/side_conversation/#participants)
created_at| string| true| false| The time the side converation event was created
id| string| true| false| Automatically assigned when the event is created
message| object| true| false| Events of type "create" and "reply" have a message. See Messages
side_conversation_id| string| true| false| The id of the side conversation the event belongs to
ticket_id| integer| true| false| The parent ticket id of the side conversation
type| string| true| false| The type of event
updates| object| true| false| Events of type "update" have fields here. See Updates
url| string| true| false| The API url of the side conversation
via| string| true| false| The channel used when creating the event. See the [Via object reference](/documentation/ticketing/reference-guides/via-object-reference/)

#### Messages

The `message` object has the following properties:

Name| Type| Mandatory| Comment
---|---|---|---
subject| string| no| The subject of the message
preview_text| string| no| A plain text string describing the message
body| string| no| The plain text version of the body of the message
html_body| string| no| The HTML version of the body of the message
from| object| no| The participant who sent the message. See [Participants](/api-reference/ticketing/side_conversation/side_conversation/#participants)
to| array| yes| The list of participants the message was sent to. See [Participants](/api-reference/ticketing/side_conversation/side_conversation/#participants)
external_ids| object| no| A key-value object where all values are strings. Used for metadata

#### Updates

The `updates` object has the following properties:

Name| Type| Comment
---|---|---
state| string| The state of the side conversation. Possible values: "open", "closed"
subject| string| The subject of the side conversation

#### Example


    {  "actor": {    "email": "[[email protected]](/cdn-cgi/l/email-protection)",    "name": "Johnny Agent",    "user_id": 35436  },  "created_at": "2018-11-20T16:58:36.453+00:00",  "id": "8566255a-ece5-11e8-857d-493066fa7b17",  "message": {    "body": "I was trying to print an email when the printer suddenly started burning",    "from": {      "email": "[[email protected]](/cdn-cgi/l/email-protection)",      "name": "Johnny Agent",      "user_id": 35436    },    "html_body": "I was trying to print an email when the printer suddenly started <strong>burning</strong>",    "preview_text": "I was trying to print an email when the printer suddenly",    "subject": "Help, my printer is on fire!",    "to": [      {        "email": "[[email protected]](/cdn-cgi/l/email-protection)",        "name": null,        "user_id": null      }    ],    "via": "support"  },  "side_conversation_id": "8566255a-ece5-11e8-857d-493066fa7b17",  "type": "reply",  "via": "support"}

### List Side Conversation Events

  * `GET /api/v2/tickets/{ticket_id}/side_conversations/{side_conversation_id}/events`


Returns a list of side conversation events on the side conversation.

You can sideload [side conversations](/api-reference/ticketing/side_conversation/side_conversation/).

#### Allowed For

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
side_conversation_id| string| Path| true| The id of the side conversation
ticket_id| integer| Path| true| The id of the ticket

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/tickets/{ticket_id}/side_conversations/{side_conversation_id}/events.json \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/tickets/1/side_conversations/e9ad3991-35e8-445e-a8cc-3d56862cb1f7/events"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/tickets/1/side_conversations/e9ad3991-35e8-445e-a8cc-3d56862cb1f7/events")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/tickets/1/side_conversations/e9ad3991-35e8-445e-a8cc-3d56862cb1f7/events',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/tickets/1/side_conversations/e9ad3991-35e8-445e-a8cc-3d56862cb1f7/events"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/tickets/1/side_conversations/e9ad3991-35e8-445e-a8cc-3d56862cb1f7/events")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "count": 1,  "events": [    {      "actor": {        "email": "[[email protected]](/cdn-cgi/l/email-protection)",        "name": "Johnny Agent",        "user_id": 35436      },      "created_at": "2018-11-20T16:58:36.453+00:00",      "id": "8566255a-ece5-11e8-857d-493066fa7b17",      "message": {        "body": "I was trying to print an email when the printer suddenly started burning",        "from": {          "email": "[[email protected]](/cdn-cgi/l/email-protection)",          "name": "Johnny Agent",          "user_id": 35436        },        "html_body": "I was trying to print an email when the printer suddenly started <strong>burning</strong>",        "preview_text": "I was trying to print an email when the printer suddenly",        "subject": "Help, my printer is on fire!",        "to": [          {            "email": "[[email protected]](/cdn-cgi/l/email-protection)",            "name": null,            "user_id": null          }        ],        "via": "support"      },      "side_conversation_id": "8566255a-ece5-11e8-857d-493066fa7b17",      "type": "reply",      "via": "support"    }  ],  "next_page": null,  "previous_page": null}

### Incremental Side Conversation Event Export

  * `GET /api/v2/tickets/side_conversations/events?start_time={start_time}`


Returns the side conversation events created since the start time. See [start_time](/api-reference/ticketing/ticket-management/incremental_exports/#start_time).

#### Allowed for

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
start_time| integer| Query| true| A query start time for incremental exports

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/tickets/side_conversations/events.json?start_time=1332034771 \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/tickets/side_conversations/events?start_time=1383685952"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/tickets/side_conversations/events")		.newBuilder()		.addQueryParameter("start_time", "1383685952");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/tickets/side_conversations/events',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'start_time': '1383685952',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/tickets/side_conversations/events?start_time=1383685952"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/tickets/side_conversations/events")uri.query = URI.encode_www_form("start_time": "1383685952")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "count": 1,  "end_time": 1383685952,  "events": [    {      "actor": {        "email": "[[email protected]](/cdn-cgi/l/email-protection)",        "name": "Johnny Agent",        "user_id": 35436      },      "created_at": "2018-11-20T16:58:36.453+00:00",      "id": "8566255a-ece5-11e8-857d-493066fa7b17",      "message": {        "body": "I was trying to print an email when the printer suddenly started burning",        "from": {          "email": "[[email protected]](/cdn-cgi/l/email-protection)",          "name": "Johnny Agent",          "user_id": 35436        },        "html_body": "I was trying to print an email when the printer suddenly started <strong>burning</strong>",        "preview_text": "I was trying to print an email when the printer suddenly",        "subject": "Help, my printer is on fire!",        "to": [          {            "email": "[[email protected]](/cdn-cgi/l/email-protection)",            "name": null,            "user_id": null          }        ],        "via": "support"      },      "side_conversation_id": "8566255a-ece5-11e8-857d-493066fa7b17",      "type": "reply",      "via": "support"    }  ],  "next_page": "https://{subdomain}.zendesk.com/api/v2/tickets/side_conversations/events.json?start_time=1383685952"}

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)