# Ticket Comments

*Source: https://developer.zendesk.com/api-reference/ticketing/tickets/ticket_comments/*

---

## On this page

  * [JSON format](/api-reference/ticketing/tickets/ticket_comments/#json-format)
  * [List Comments](/api-reference/ticketing/tickets/ticket_comments/#list-comments)
  * [Count Ticket Comments](/api-reference/ticketing/tickets/ticket_comments/#count-ticket-comments)
  * [Make Comment Private](/api-reference/ticketing/tickets/ticket_comments/#make-comment-private)
  * [Redact Ticket Comment In Agent Workspace](/api-reference/ticketing/tickets/ticket_comments/#redact-ticket-comment-in-agent-workspace)
  * [Redact Chat Comment](/api-reference/ticketing/tickets/ticket_comments/#redact-chat-comment)
  * [Redact Chat Comment Attachment](/api-reference/ticketing/tickets/ticket_comments/#redact-chat-comment-attachment)
  * [Redact String in Comment](/api-reference/ticketing/tickets/ticket_comments/#redact-string-in-comment)


# Ticket Comments

## On this page

  * [JSON format](/api-reference/ticketing/tickets/ticket_comments/#json-format)
  * [List Comments](/api-reference/ticketing/tickets/ticket_comments/#list-comments)
  * [Count Ticket Comments](/api-reference/ticketing/tickets/ticket_comments/#count-ticket-comments)
  * [Make Comment Private](/api-reference/ticketing/tickets/ticket_comments/#make-comment-private)
  * [Redact Ticket Comment In Agent Workspace](/api-reference/ticketing/tickets/ticket_comments/#redact-ticket-comment-in-agent-workspace)
  * [Redact Chat Comment](/api-reference/ticketing/tickets/ticket_comments/#redact-chat-comment)
  * [Redact Chat Comment Attachment](/api-reference/ticketing/tickets/ticket_comments/#redact-chat-comment-attachment)
  * [Redact String in Comment](/api-reference/ticketing/tickets/ticket_comments/#redact-string-in-comment)


Ticket comments represent the conversation between requesters, collaborators, and agents. Comments can be public or private.

For information on comments in requests as opposed to tickets, see [Request comments](/api-reference/ticketing/tickets/ticket-requests/#request-comments).

#### Creating ticket comments

Ticket comments, including voice comments, are created with the [Tickets API](/api-reference/ticketing/tickets/tickets/), not the Ticket Comments API described in this document. The Tickets Comments API has no endpoint to create comments.

Ticket comments are created by including a `comment` object in the `ticket` object when creating or updating the ticket. Example:


    curl https://{subdomain}.zendesk.com/api/v2/tickets/{id} \  -d '{"ticket": {"comment": { "body": "The smoke is very colorful.", "author_id": 494820284 }}}' \  -H "Content-Type: application/json" \  -v -u {email_address}/token:{api_token} -X PUT

To learn more, see [Adding voice comments to tickets](/documentation/ticketing/managing-tickets/adding-voice-comments-to-tickets).

**Note** : A ticket can contain up to 5000 comments in total, including both public and private comments. Once this limit is reached, any additional attempts to add comments results in a 422 error. The ticket can still be updated in other ways, provided that no new comments are added.

See also the following reference documentation:

  * [Create Ticket](/api-reference/ticketing/tickets/tickets/#create-ticket)
  * [Update Ticket](/api-reference/ticketing/tickets/tickets/#update-ticket)


### JSON format

Ticket Comments are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
add_short_url| boolean| false| false| Internal flag for adding short URLs to the comment
attachments| array| true| false| Attachments, if any. See [Attachment](/api-reference/ticketing/tickets/ticket-attachments/)
audit_id| integer| true| false| The id of the ticket audit record. See [Show Audit](/api-reference/ticketing/tickets/ticket_audits/#show-audit)
author_id| integer| false| false| The id of the comment author. If null or omitted on create, defaults to the authenticated user. See Author id
body| string| false| false| The comment string. See Bodies
channel_back| string| false| false| Internal channel back identifier for the comment
channel_source_id| string| false| false| Internal channel source identifier for the comment
created_at| string| true| false| The time the comment was created
html_body| string| false| false| The comment formatted as HTML. See Bodies
id| integer| true| false| Automatically assigned when the comment is created
metadata| object| true| false| System information (web client, IP address, etc.) and comment flags, if any. See Comment flags
plain_body| string| true| false| The comment presented as plain text. See Bodies
public| boolean| false| false| true if a public comment; false if an internal note. The initial value set on ticket creation persists for any additional comment unless you change it
translate_to| string| false| false| The locale code to translate the comment body to.
type| string| true| false| `Comment` or `VoiceComment`. The JSON object for adding voice comments to tickets is different. See [Adding voice comments to tickets](/documentation/ticketing/managing-tickets/adding-voice-comments-to-tickets)
uploads| array| false| false| List of tokens received from [uploading files](/api-reference/ticketing/tickets/ticket-attachments/#upload-files) for comment attachments. The files are attached by creating or updating tickets with the tokens. See [Attaching files](/api-reference/ticketing/tickets/tickets/#attaching-files) in Tickets
via| object| false| false| Describes how the object was created. See the [Via object reference](/documentation/ticketing/reference-guides/via-object-reference)

#### Author id

If you set the `author_id`, the user with the id is shown as the author of the comment. However, this user is not considered the updater of the ticket. The authenticated user making the API request is the updater. This has implications for business rules and views, such as the requester updated attribute and current user conditions.

#### Bodies

To submit a ticket comment, use only `body` or `html_body` in your inbound API call. `plain_body` is not supported. If you pass a `plain_body` parameter in an API to create a comment, it is stripped out.

If you use `body`, multiple consecutive spaces are collapsed into a single space and multiple consecutive newline ("\n") characters are collapsed into a single newline. To preserve your spacing, use alternating space and non-breaking space characters (you must use the Unicode `\u00a0` and not `&nbsp;`). To preserve your line breaks, enter an extra space after "\n". For example, to generate three empty lines, use "\n \n \n".

If you use `html_body` (recommended for Agent Workspace), you can use standard HTML syntax for comment formatting, including `<br>` for line breaks.

The comment body is presented as `plain_body`, `body`, or `html_body`. `html_body` is the least sanitized option; `plain_body` is the most sanitized. Text input in `body` defaults to `plain_body` if there's an error in sanitizing.

For example, if you include HTML in the `body`, the HTML will be stripped out. Use `html_body` instead of `body` to include HTML. Example:


    "html_body": "<p>This comment uses <strong>html</strong> for formatting.</p>"

Markdown formatting is supported in `body` but not in `html_body`. Markdown formatting in `body` renders only if the comment author is an agent. To format end user comments, use `html_body` and HTML. Example:


    "body": "This comment uses **Markdown** for formatting."

You can include [ticket placeholders](https://support.zendesk.com/hc/en-us/articles/4408886858138) in the `body` or `html_body`. Example:


    "body": "This comment uses the {{ticket.id}} placeholder."

When the request is processed, the placeholder is replaced by a value if one is available. If the placeholder is not supported (example, `{{fake}}`), the placeholder is stripped out.

**Note** : If you want to display double curly brackets in the comment, use `html_body` with HTML code tags (`<code>{{fake}}</code>`). You can also escape placeholders in `body` with double backslashes (`\\{{fake}}`). Though the placeholder won't appear in the response, it will appear in the ticket in Agent Workspace.

#### Body size limits

Ticket comment bodies are limited to 64kB. Any characters exceeding this limit are truncated. No error is reported.

#### Comment flags

Each comment can be flagged by Zendesk for several reasons. If the comment is flagged, the `metadata` property will have a `flags` array with any of the following values:

Value| Reason for flag
---|---
0| Zendesk is unsure the comment should be trusted
2| The comment author was not part of the conversation. [Learn more](https://support.zendesk.com/hc/en-us/articles/203661606#topic_d32_mzc_3r)
3| The comment author was not signed in when the comment was submitted. [Learn more](https://support.zendesk.com/hc/en-us/articles/203663756#topic_nr4_4s5_cq)
4| The comment was automatically generated. Automatic email notifications have been suppressed. [Learn more](https://support.zendesk.com/hc/en-us/articles/218137678#topic_kh1_5d1_qv7)
5| The attached file was rejected because it's too big
11| This comment was submitted by the user on behalf of the author. **Note** : Flags are not added when admins comment on behalf of agents or end users, and when agents comment on behalf of end users. See [Requesters and submitters](/api-reference/ticketing/tickets/tickets/#requesters-and-submitters)
14| This message might not have been sent by the user
16| Requester's name has been truncated. Please edit the name or mark as spam
17| This is a private comment created by an end user. [Learn more](https://support.zendesk.com/hc/en-us/articles/203661606#topic_d32_mzc_3r)
18| Some email recipients were excluded from CCs due to the limit of CCs per email. View the original email for the full list. [Learn more](https://support.zendesk.com/hc/en-us/articles/203690846)
20| To protect your agents, we suspended the ability of the user in this Reply-to address to perform certain actions. [Learn more](https://support.zendesk.com/hc/en-us/articles/360057609553)
21| We flagged this comment because the From and Reply-to in the messages donât match. See [Reply-to addresses](https://support.zendesk.com/hc/en-us/articles/360057609553)
22| User has yet to confirm ownership of the address used to deliver the email. [Learn more](https://support.zendesk.com/hc/en-us/articles/4408886752410)

A `flags_options` object will also be included with additional information about the flags.

The `flags` and `flags_options` properties are omitted if there are no flags.

**Example**


    metadata: {  system: { ... },  flags: [2,5],  "flags_options": {    "2": {      "trusted": false    },    "5": {      "message": {        "file": "printer_manual.pdf",        "account_limit": "20"      },      "trusted": false    }  },  "trusted": false,  "suspension_type_id": null}

#### Example


    {  "attachments": [    {      "content_type": "text/plain",      "content_url": "https://company.zendesk.com/attachments/crash.log",      "file_name": "crash.log",      "id": 498483,      "size": 2532,      "thumbnails": []    }  ],  "author_id": 123123,  "body": "Thanks for your help!",  "created_at": "2009-07-20T22:55:29Z",  "id": 1274,  "metadata": {    "system": {      "client": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",      "ip_address": "1.1.1.1",      "latitude": -37.000000000001,      "location": "Melbourne, 07, Australia",      "longitude": 144.0000000000002    },    "via": {      "channel": "web",      "source": {        "from": {},        "rel": "web_widget",        "to": {}      }    }  },  "public": true,  "type": "Comment"}

### List Comments

  * `GET /api/v2/tickets/{ticket_id}/comments`


Returns the comments added to the ticket.

Each comment may include a `content_url` for an attachment or a `recording_url` for a voice comment that points to a file that may be hosted externally. For security reasons, take care not to inadvertently send Zendesk authentication credentials to third parties when attempting to access these files. See [Working with url properties](/documentation/api-basics/best-practices/working-with-url-properties/).

#### Pagination

  * Cursor pagination (recommended)
  * Offset pagination


See [Pagination](/api-reference/introduction/pagination/).

Returns a maximum of 100 records per page.

#### Sorting

By default, comments are sorted by creation date in ascending order.

When using cursor pagination, use the following parameter to change the sort order:

Name| Type| Required| Comments
---|---|---|---
`sort`| string| no| Possible values are "created_at" (ascending order) or "-created_at" (descending order)

When using offset pagination, use the following parameters to change the sort order:

Name| Type| Required| Comments
---|---|---|---
`sort_order`| string| no| One of `asc`, `desc`. Defaults to `asc`

#### Allowed For

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
include| string| Query| false| Accepts "users". Use this parameter to list email CCs by side-loading users. Example: `?include=users`. **Note** : If the comment source is email, a deleted user will be represented as the CCd email address. If the comment source is anything else, a deleted user will be represented as the user name.
include_inline_images| boolean| Query| false| Default is false. When true, inline images are also listed as attachments in the response
page| object| Query| false| Cursor-based pagination parameters (JSON:API style). Supports nested parameters: - `page[size]` \- Number of records per page (default varies by endpoint, typically 100) - `page[after]` \- Cursor token to fetch records after this position - `page[before]` \- Cursor token to fetch records before this position Example: `?page[size]=50&page[after]=eyJvIjoiaWQiLCJ2IjoiYVFFPSJ9`
per_page| integer| Query| false| Number of records to return per page. Note: Default and maximum values vary by endpoint. Check endpoint-specific documentation for limits.
sort_order| string| Query| false| Sort order. Defaults to "asc". Allowed values are "asc", or "desc".
ticket_id| integer| Path| true| The ID of the ticket

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/tickets/{ticket_id}/comments \  -H "Content-Type: application/json" -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/tickets/123456/comments?include=&include_inline_images=&page=&per_page=50&sort_order="	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/tickets/123456/comments")		.newBuilder()		.addQueryParameter("include", "")		.addQueryParameter("include_inline_images", "")		.addQueryParameter("page", "")		.addQueryParameter("per_page", "50")		.addQueryParameter("sort_order", "");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/tickets/123456/comments',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'include': '',    'include_inline_images': '',    'page': '',    'per_page': '50',    'sort_order': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/tickets/123456/comments?include=&include_inline_images=&page=&per_page=50&sort_order="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/tickets/123456/comments")uri.query = URI.encode_www_form("include": "", "include_inline_images": "", "page": "", "per_page": "50", "sort_order": "")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "comments": [    {      "attachments": [        {          "content_type": "text/plain",          "content_url": "https://company.zendesk.com/attachments/crash.log",          "file_name": "crash.log",          "id": 498483,          "size": 2532,          "thumbnails": []        }      ],      "audit_id": 432567,      "author_id": 123123,      "body": "Thanks for your help!",      "created_at": "2009-07-20T22:55:29Z",      "id": 1274,      "metadata": {        "system": {          "client": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",          "ip_address": "1.1.1.1",          "latitude": -37.000000000001,          "location": "Melbourne, 07, Australia",          "longitude": 144.0000000000002        },        "via": {          "channel": "web",          "source": {            "from": {},            "rel": "web_widget",            "to": {}          }        }      },      "public": true,      "type": "Comment"    }  ]}

### Count Ticket Comments

  * `GET /api/v2/tickets/{ticket_id}/comments/count`


Returns an approximate count of the comments added to the ticket. If the count exceeds 100,000, the count will return a cached result. This cached result will update every 24 hours.

The `count[refreshed_at]` property is a timestamp that indicates when the count was last updated.

**Note** : When the count exceeds 100,000, `count[refreshed_at]` may occasionally be null. This indicates that the count is being updated in the background, and `count[value]` is limited to 100,000 until the update is complete.

#### Allowed For

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
ticket_id| integer| Path| true| The ID of the ticket

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/tickets/{ticket_id}/comments/count \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/tickets/123456/comments/count"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/tickets/123456/comments/count")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/tickets/123456/comments/count',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/tickets/123456/comments/count"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/tickets/123456/comments/count")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "count": {    "refreshed_at": "2020-04-06T02:18:17Z",    "value": 12  }}

### Make Comment Private

  * `PUT /api/v2/tickets/{ticket_id}/comments/{ticket_comment_id}/make_private`


#### Allowed For

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
ticket_comment_id| integer| Path| true| The ID of the ticket comment
ticket_id| integer| Path| true| The ID of the ticket

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/tickets/{ticket_id}/comments/{ticket_comment_id}/make_private \  -v -u {email_address}/token:{api_token} -X PUT -d '{}' -H "Content-Type: application/json"

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/tickets/123456/comments/35436/make_private"	method := "PUT"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/tickets/123456/comments/35436/make_private")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'PUT',  url: 'https://example.zendesk.com/api/v2/tickets/123456/comments/35436/make_private',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/tickets/123456/comments/35436/make_private"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/tickets/123456/comments/35436/make_private")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    null

### Redact Ticket Comment In Agent Workspace

  * `PUT /api/v2/comment_redactions/{ticket_comment_id}`


Redaction allows you to permanently remove words, strings, or attachments from a ticket comment.

In the `html_body` of the comment, wrap the content you want redacted in `<redact>` tags. Example:


    {  "html_body": "<div class=\"zd-comment\" dir=\"auto\">My ID number is <redact>847564</redact>!</div>",  "ticket_id":100}

The characters in the redact tag will be replaced by the â symbol.

To redact HTML elements such inline images, anchor tags, and links, add the `redact` tag attribute to the element as well as the `<redact>` tag to inner text, if any. Example:

`<a href="http://example.com" redact><redact>some link</redact></a>`

The `redact` attribute only redacts the tag. Any inner text will be left behind if not enclosed in a `<redact>` tag.

Redaction is permanent and can not be undone. Data is permanently deleted from Zendesk servers with no way to recover it.

This endpoint provides all the same functionality that the [Redact String in Comment](/api-reference/ticketing/tickets/ticket_comments/#redact-string-in-comment) endpoint provides, plus:

  * Redaction of comments in closed tickets

  * Redaction of comments in archived tickets

  * Redaction of formatted text (bold, italics, hyperlinks)


**Limitations** : When content is redacted from an email comment, the content is also redacted from the original email through a background job. It may take a while for the changes to be completed.

**Note** : We recommend using this endpoint instead of the [Redact String in Comment](/api-reference/ticketing/tickets/ticket_comments/#redact-string-in-comment) endpoint, which will eventually be deprecated.

#### Allowed For

  * Agents


[Agent Workspace](https://support.zendesk.com/hc/en-us/articles/360024218473) must be enabled on the account. For professional accounts, deleting tickets must be enabled for agents. On Enterprise accounts, you can assign agents to a custom role with permissions to redact ticket content.

#### Request Body Properties

Name| Type| Required| Description
---|---|---|---
ticket_id| integer| true| The ID of the ticket
html_body| string| false| The `html_body` of the comment containing `<redact>` tags or `redact` attributes
external_attachment_urls| array| false| Array of attachment URLs belonging to the comment to be redacted. See [`content_url` property of Attachment](/api-reference/ticketing/tickets/ticket-attachments/)

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
ticket_comment_id| integer| Path| true| The ID of the ticket comment

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/comment_redactions/{ticket_comment_id} \  -H "Content-Type: application/json" -v -u {email_address}/token:{api_token} -X PUT \  -d '{"html_body":"<div class=\"zd-comment\" dir=\"auto\">My ID number is <redact>847564</redact>!</div>", "ticket_id": 100 }'

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/comment_redactions/35436"	method := "PUT"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/comment_redactions/35436")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'PUT',  url: 'https://example.zendesk.com/api/v2/comment_redactions/35436',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/comment_redactions/35436"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/comment_redactions/35436")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "comment": {    "attachments": [],    "author_id": 123,    "id": 100,    "plain_body": "My ID number is ââââ!",    "public": true,    "type": "Comment"  }}

### Redact Chat Comment

  * `PUT /api/v2/chat_redactions/{ticket_id}`


Permanently removes words or strings from a chat ticket's comment.

Wrap `<redact>` tags around the content in the chat comment you want redacted. Example:


    {  "text": "My ID number is <redact>847564</redact>!"}

The characters contained in the tag will be replaced by the â symbol.

**Note** : This does not work on active chats. For chat tickets that predate March 2020, consider using Redact Ticket Comment In Agent Workspace.

#### Allowed For

  * Agents


[Agent Workspace](https://support.zendesk.com/hc/en-us/articles/360024218473) must enabled for the account. Deleting tickets must be enabled for agents.

#### Request Body Properties

Name| Type| Required| Description
---|---|---|---
chat_id| string| true| The `chat_id` in the `ChatStartedEvent` event in the ticket audit. See [Ticket Audits](/api-reference/ticketing/tickets/ticket_audits)
chat_index| integer| false| The `chat_index` in the `ChatMessage` event in the ticket audit. See [Ticket Audits](/api-reference/ticketing/tickets/ticket_audits). Mandatory if `message_id` is not used
message_id| string| false| The `message_id` of the `ChatMessage` event in the ticket audit that is part of a `ChatStartedEvent` history. Used when redacting a ChatMessage that is part of a conversation history. Mandatory if `chat_index` is not used
text| string| true| The `message` in the `ChatMessage` event in the ticket audit. See [Ticket Audits](/api-reference/ticketing/tickets/ticket_audits). Wrap `message` with `<redact>` tags

To get the required body properties, make a request to the [Ticket Audit](/api-reference/ticketing/tickets/ticket_audits) endpoint. Example response:


    Status 200 OK{  "audits": [    "events": [      {        "id": 1932802680168,        "type": "ChatStartedEvent",        "value": {          "visitor_id": "10502823-16EkM3T6VNq7KMd",          "chat_id": "2109.10502823.Sjuj2YrBpXwei",          "history": [            {              "chat_index": 0,              "type": "ChatMessage",              "message": "My ID number is 847564!"            }          ]        }      }    ]  ]}

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
ticket_id| integer| Path| true| The ID of the ticket

#### Code Samples

**curl**


    # Example with chat_indexcurl https://{subdomain}.zendesk.com/api/v2/chat_redactions/{ticket_id} \  -H "Content-Type: application/json" -v -u {email_address}/token:{api_token} -X PUT \  -d '{"chat_id":"2109.10502823.Sjuj2YrBpXwei", "chat_index": 0, "text": "My ID number is <redact>847564</redact>!" }'
    # Example with message_idcurl https://{subdomain}.zendesk.com/api/v2/chat_redactions/{ticket_id} \  -H "Content-Type: application/json" -v -u {email_address}:{password} -X PUT \  -d '{"chat_id":"2109.10502823.Sjuj2YrBpXwei", "message_id": "667b72a114a0d4d5c1d26aff", "text": "My ID number is <redact>847564</redact>!" }'

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/chat_redactions/123456"	method := "PUT"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/chat_redactions/123456")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'PUT',  url: 'https://example.zendesk.com/api/v2/chat_redactions/123456',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/chat_redactions/123456"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/chat_redactions/123456")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "chat_event": {    "id": 1932802680168,    "type": "ChatStartedEvent",    "value": {      "chat_id": "2109.10502823.Sjuj2YrBpXwei",      "history": [        {          "chat_index": 0,          "message": "My ID number is ââââ!",          "type": "ChatMessage"        }      ],      "visitor_id": "10502823-16EkM3T6VNq7KMd"    }  }}

### Redact Chat Comment Attachment

  * `PUT /api/v2/chat_file_redactions/{ticket_id}`


Permanently removes one or more chat attachments from a chat ticket.

**Note** : This does not work on active chats. For chat tickets that predate March 2020, consider using Redact Ticket Comment In Agent Workspace.

#### Allowed For

  * Agents


[Agent Workspace](https://support.zendesk.com/hc/en-us/articles/360024218473) must enabled for the account. Deleting tickets must be enabled for agents.

#### Request Body Properties

Name| Type| Required| Description
---|---|---|---
chat_id| string| true| The `chat_id` in the `ChatStartedEvent` event in the ticket audit. See [Ticket Audits](/api-reference/ticketing/tickets/ticket_audits)
chat_indexes| array| false| The array of `chat_index` in the `ChatFileAttachment` event in the ticket audit. See [Ticket Audits](/api-reference/ticketing/tickets/ticket_audits). Mandatory if `message_ids` is not used
message_ids| array| false| The array of `message_id` in the `ChatFileAttachment` event in the ticket audit that is part of a `ChatStartedEvent` history. Used when redacting a ChatFileAttachment that is part of a conversation history. Mandatory if `chat_indexes` is not used

To get the required body properties, make a request to the [Ticket Audits](/api-reference/ticketing/tickets/ticket_audits) endpoint. Example response:


    Status 200 OK{  "audits": [    "events": [      {        "id": 1932802680168,        "type": "ChatStartedEvent",        "value": {          "visitor_id": "10502823-16EkM3T6VNq7KMd",          "chat_id": "2109.10502823.Sjuj2YrBpXwei",          "history": [            {              "chat_index": 0,              "type": "ChatFileAttachment",              "filename": "image1.jpg"            },            {              "chat_index": 1,              "type": "ChatFileAttachment",              "filename": "image2.jpg"            }          ]        }      }    ]  ]}

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
ticket_id| integer| Path| true| The ID of the ticket

#### Code Samples

**curl**


    # Example with chat_indexescurl https://{subdomain}.zendesk.com/api/v2/chat_file_redactions/{ticket_id} \  -H "Content-Type: application/json" -v -u {email_address}/token:{api_token} -X PUT \  -d '{"chat_id":"2109.10502823.Sjuj2YrBpXwei", "chat_indexes": [0,1] }'
    # Example with message_idscurl https://{subdomain}.zendesk.com/api/v2/chat_file_redactions/{ticket_id} \  -H "Content-Type: application/json" -v -u {email_address}/token:{api_token} -X PUT \  -d '{"chat_id":"2109.10502823.Sjuj2YrBpXwei", "message_ids": ["667b72a114a0d4d5c1d26aff", "667b72a114a0d7xbc1d26aff"] }'

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/chat_file_redactions/123456"	method := "PUT"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/chat_file_redactions/123456")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'PUT',  url: 'https://example.zendesk.com/api/v2/chat_file_redactions/123456',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/chat_file_redactions/123456"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/chat_file_redactions/123456")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "chat_event": {    "id": 1932802680168,    "type": "ChatStartedEvent",    "value": {      "chat_id": "2109.10502823.Sjuj2YrBpXwei",      "history": [        {          "chat_index": 0,          "filename": "redacted.txt",          "type": "ChatFileAttachment"        },        {          "chat_index": 1,          "filename": "redacted.txt",          "type": "ChatFileAttachment"        }      ],      "visitor_id": "10502823-16EkM3T6VNq7KMd"    }  }}

### Redact String in Comment

  * `PUT /api/v2/tickets/{ticket_id}/comments/{ticket_comment_id}/redact`


Permanently removes words or strings from a ticket comment. Specify the string to redact in an object with a `text` property. Example: `'{"text": "987-65-4320"}'`. The characters of the word or string are replaced by the â symbol.

If the comment was made by email, the endpoint also attempts to redact the string from the original email retained by Zendesk for audit purposes.

**Note** : If you use the rich text editor, support for redacting formatted text (bold, italics, hyperlinks) is limited.

Redaction is permanent. You can't undo the redaction or see _what_ was removed. Once a ticket is closed, you can no longer redact strings from its comments.

To use this endpoint, the "Agents can delete tickets" option must be enabled in the Zendesk Support admin interface at **Admin** > **Settings** > **Agents**.

#### Allowed For

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
ticket_comment_id| integer| Path| true| The ID of the ticket comment
ticket_id| integer| Path| true| The ID of the ticket

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/tickets/{ticket_id}/comments/{ticket_comment_id}/redact \  -H "Content-Type: application/json" -v -u {email_address}/token:{api_token} -X PUT \  -d '{"text": "987-65-4320"}'

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/tickets/123456/comments/35436/redact"	method := "PUT"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/tickets/123456/comments/35436/redact")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'PUT',  url: 'https://example.zendesk.com/api/v2/tickets/123456/comments/35436/redact',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/tickets/123456/comments/35436/redact"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/tickets/123456/comments/35436/redact")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "comment": {    "author_id": 1,    "id": 35436,    "plain_body": "My social security number is ââââ!",    "type": "Comment"  }}

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)