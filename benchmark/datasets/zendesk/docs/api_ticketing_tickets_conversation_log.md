# Conversation Log

*Source: https://developer.zendesk.com/api-reference/ticketing/tickets/conversation_log/*

---

## On this page

  * [JSON format](/api-reference/ticketing/tickets/conversation_log/#json-format)
  * [List Conversation log for Ticket](/api-reference/ticketing/tickets/conversation_log/#list-conversation-log-for-ticket)


# Conversation Log

## On this page

  * [JSON format](/api-reference/ticketing/tickets/conversation_log/#json-format)
  * [List Conversation log for Ticket](/api-reference/ticketing/tickets/conversation_log/#list-conversation-log-for-ticket)


The Conversation Log API provides a read-only list of all ticket and conversational events appended to a ticket.

**Conversational events** include messages sent by agents, end users, or bots.

**Ticket events** cover interactions such as adding new comments to the ticket.

For a complete list of events, see the [Conversation Log events reference](/documentation/ticketing/reference-guides/conversation-log-events-reference).

### JSON format

Conversation Log are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
attachments| array| true| true| A collection of attachments (image or file) associated with the event
author| object| false| true| Object that describes the user who created the event
content| object| true| true| Object that describes the content of the message. The inner fields depends on the record type
created_at| string| true| true| The timestamp of when this record was created
id| string| true| true| Unique record identifier
metadata| object| true| true| Various additional data that further describes this record
reference| string| true| true| A Zendesk resource name value that uniquely identifies this record. Example: `zen:ticket_event:<id>`
type| string| true| true| The type of record, representing one of the conversational ticket events. Examples: `Comment` or `Messaging::ConversationMessage`

#### Example


    {  "attachments": [    {      "content_type": "image/png",      "content_url": "https://company.zendesk.com/attachments/token/123/?name=sample.png",      "deleted": false,      "file_name": "sample.png",      "height": 128,      "id": 8639388162331,      "inline": false,      "mapped_content_url": "https://company.zendesk.com/attachments/token/h123/?name=sample.png",      "size": 20331,      "thumbnails": [        {          "content_type": "image/png",          "content_url": "https://company.zendesk.com/attachments/token/333/?name=sample_thumb.png",          "deleted": false,          "file_name": "sample_thumb.png",          "height": 80,          "id": 8639488164605,          "inline": false,          "mapped_content_url": "https://company.zendesk.com/attachments/token/333/?name=sample_thumb.png",          "size": 10173,          "url": "https://company.zendesk.com/api/v2/attachments/86395",          "width": 80        }      ],      "url": "https://company.zendesk.com/api/v2/attachments/13341",      "width": 128    }  ],  "author": {    "avatar_url": "https://static.zdassets.com/web_widget/latest/default_avatar.png",    "display_name": "Sample Owner",    "type": "agent",    "zen:sunco:user_id": "a21a91fd1234a",    "zen:support:user_id": 123111233  },  "content": {    "body": "<div class=\\\"zd-comment\\\" dir=\\\"auto\\\">big bear attachment public comment email<br></div>",    "type": "html"  },  "created_at": "2024-10-09T03:30:43Z",  "id": "01J9Q342W4DE2G1343NNTX36G",  "metadata": {    "custom": {},    "public": true,    "system": {      "client": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",      "ip_address": "123.45.67.89",      "latitude": -30.3,      "location": "Sydney, NSW, Australia",      "longitude": 100.1    },    "ticket_version": 4  },  "reference": "zen:ticket_event:8639326502654",  "type": "Comment"}

### List Conversation log for Ticket

  * `GET /api/v2/tickets/{ticket_id}/conversation_log`


Lists the conversation log events for a specified ticket.

#### Pagination

  * Cursor pagination


See [Pagination](/api-reference/introduction/pagination/).

Returns a maximum of 100 records per page.

#### Allowed for

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
page| object| Query| false| Cursor-based pagination parameters (JSON:API style). Supports nested parameters: - `page[size]` \- Number of records per page (default varies by endpoint, typically 100) - `page[after]` \- Cursor token to fetch records after this position - `page[before]` \- Cursor token to fetch records before this position Example: `?page[size]=50&page[after]=eyJvIjoiaWQiLCJ2IjoiYVFFPSJ9`
sort| string| Query| false| Field to sort results by. Prefix with `-` for descending order. When used with cursor pagination, this determines the cursor ordering. Example: `?sort=name` or `?sort=-created_at`
ticket_id| integer| Path| true| The ID of the ticket

#### Limits

This endpoint has its own rate limit that is different from the account wide rate limit. When calls are made to this endpoint, this limit will be consumed and you will get a `429 Too Many Requests` response code if the allocation is exhausted.

##### Headers

API responses include usage limit information in the headers for this endpoint.


    Zendesk-RateLimit-omnilog-index: total={number}; remaining={number}; resets={number}

Within this header, âTotalâ signifies the initial allocation, âRemainingâ indicates the remaining allowance for the current interval, and âResetsâ denotes the wait time in seconds before the limit refreshes. You can see the Total, and Interval values in the below table.

##### Details

This is the limit definition for the List Conversation Log endpoint

Rate Limits| Scopes| Interval| Sandbox| Trial| Default
---|---|---|---|---|---
Standard| Account| 1 minute| 100| 100| N/A
With High Volume API Add On| Account| 1 minute| 300| 300| N/A

"Default" applies to all Zendesk suite and support plans. Please refer to the [general account limits](https://developer.zendesk.com/api-reference/introduction/rate-limits) for more information.

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/tickets/{ticket_id}/conversation_log \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/tickets/123456/conversation_log?page=&sort=name"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/tickets/123456/conversation_log")		.newBuilder()		.addQueryParameter("page", "")		.addQueryParameter("sort", "name");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/tickets/123456/conversation_log',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'page': '',    'sort': 'name',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/tickets/123456/conversation_log?page=&sort=name"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/tickets/123456/conversation_log")uri.query = URI.encode_www_form("page": "", "sort": "name")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "events": [    {      "attachments": [],      "author": {        "avatar_url": "https://static.zdassets.com/web_widget/latest/default_avatar.png",        "display_name": "SampleBot",        "type": "bot",        "zen:sunco:user_id": "a21a91fd1234a",        "zen:support:user_id": -1      },      "content": {        "actions": [          {            "reply": {              "payload": "goto_node=01J9WVC919KKCBB0WKC42YQMCT_01J9Z7SYB9EGXNGT8DQV3KX4F2",              "text": "Talk to a human"            }          }        ],        "text": "Hey! Have a question? I'm here to assist.",        "type": "text"      },      "created_at": "2025-04-22T09:24:26Z",      "id": "02JSED093DTX4RTDRRJXN2YKB0",      "metadata": {        "custom": {},        "system": {},        "ticket_version": 0      },      "received_at": "2025-04-22T09:24:26.861Z",      "reference": "zen:sunco:conversation_message:6807603a38564290f5a086c2",      "source": {        "type": "zd:answerBot"      },      "type": "Messaging::ConversationMessage"    },    {      "attachments": [],      "author": {        "display_name": "sample user",        "type": "user",        "zen:support:user_id": 8303911923701      },      "content": {        "body": "<div class=\"zd-comment\" dir=\"auto\"><p dir=\"auto\">Conversation with wp native</p>\n\n<p dir=\"auto\">URL: None</p></div>",        "type": "html"      },      "created_at": "2025-04-22T09:24:46Z",      "id": "01JSED0VSGBJP9TJ471NTUGYYD",      "metadata": {        "custom": {},        "public": false,        "system": {},        "ticket_version": 0      },      "reference": "zen:ticket_event:8639371328313",      "type": "Comment"    }  ],  "links": {    "next": "https://company.zendesk.com/api/v2/tickets/123/conversation_log?page%5Bafter%5D=eyJvIjziaWQiLCJ2IjoiY3hvQUFBQXdNVXBUUlVSTk1WRkxXVGMxVFZSYVMwSk5SRXN8VnpRMVJ3PT0ifQ%3D%3D&sort=created_at",    "prev": "https://company.zendesk.com/api/v2/tickets/123/conversation_log?page%5Bbefore%5D=eyJvIjoiaWQiJKJ2IjoiY3hvQUFBQXdNVXBUUlVRd09UTkVWRmcwVWxSRVVsSktXRTR3V1V0Q03BPT0ifQ%3D%3D&sort=created_at"  },  "meta": {    "after_cursor": "eyJvIjoiaWQiLCJ2IjoiY3hvQUFBQXdNVXBUUlVERk1WRkxXVGMxVFZSYVMwSk5SRXN6VnpRMVJ3PT0ifQ==",    "before_cursor": "eyJvIjoiaWQiLCJ4IjoiY3hvQUFBQXdSDEBUUlVRd09UTkVWRmcwVWxSRVVsSktXRTR3V1V0Q01BPT0ifQ==",    "has_more": false  }}

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)