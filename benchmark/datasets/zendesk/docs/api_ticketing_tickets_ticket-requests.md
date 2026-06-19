# Requests

*Source: https://developer.zendesk.com/api-reference/ticketing/tickets/ticket-requests/*

---

## On this page

  * [JSON format](/api-reference/ticketing/tickets/ticket-requests/#json-format)
  * [List Requests](/api-reference/ticketing/tickets/ticket-requests/#list-requests)
  * [Search Requests](/api-reference/ticketing/tickets/ticket-requests/#search-requests)
  * [Show Request](/api-reference/ticketing/tickets/ticket-requests/#show-request)
  * [Create Request](/api-reference/ticketing/tickets/ticket-requests/#create-request)
  * [Update Request](/api-reference/ticketing/tickets/ticket-requests/#update-request)
  * [Listing Comments](/api-reference/ticketing/tickets/ticket-requests/#listing-comments)
  * [Getting Comments](/api-reference/ticketing/tickets/ticket-requests/#getting-comments)
  * [List CCD Requests](/api-reference/ticketing/tickets/ticket-requests/#list-ccd-requests)
  * [List Open Requests](/api-reference/ticketing/tickets/ticket-requests/#list-open-requests)
  * [List Solved Requests](/api-reference/ticketing/tickets/ticket-requests/#list-solved-requests)
  * [List User Requests](/api-reference/ticketing/tickets/ticket-requests/#list-user-requests)
  * [List Organization Requests](/api-reference/ticketing/tickets/ticket-requests/#list-organization-requests)


# Requests

## On this page

  * [JSON format](/api-reference/ticketing/tickets/ticket-requests/#json-format)
  * [List Requests](/api-reference/ticketing/tickets/ticket-requests/#list-requests)
  * [Search Requests](/api-reference/ticketing/tickets/ticket-requests/#search-requests)
  * [Show Request](/api-reference/ticketing/tickets/ticket-requests/#show-request)
  * [Create Request](/api-reference/ticketing/tickets/ticket-requests/#create-request)
  * [Update Request](/api-reference/ticketing/tickets/ticket-requests/#update-request)
  * [Listing Comments](/api-reference/ticketing/tickets/ticket-requests/#listing-comments)
  * [Getting Comments](/api-reference/ticketing/tickets/ticket-requests/#getting-comments)
  * [List CCD Requests](/api-reference/ticketing/tickets/ticket-requests/#list-ccd-requests)
  * [List Open Requests](/api-reference/ticketing/tickets/ticket-requests/#list-open-requests)
  * [List Solved Requests](/api-reference/ticketing/tickets/ticket-requests/#list-solved-requests)
  * [List User Requests](/api-reference/ticketing/tickets/ticket-requests/#list-user-requests)
  * [List Organization Requests](/api-reference/ticketing/tickets/ticket-requests/#list-organization-requests)


A _request_ is an end user's perspective on a ticket. End users can only see public comments and certain fields of a ticket. Use this API to let end users view, update, and create tickets they have access to.

You can sideload some resources with requests. See Requests in [Supported Endpoints](/documentation/ticketing/using-the-zendesk-api/side_loading/#supported-endpoints) in Side-loading.

#### Authentication

End users can use the Requests API.

**Note** : An end user won't be able to view their requests if the end user added an email identity (an email address associated with a Zendesk profile) after September 17, 2017, and didn't verify the email address. The problem is flagged by the API with a 403 response. See [Verifying a user's email address](https://support.zendesk.com/hc/en-us/articles/203663786) in the Support Help Center.

Anonymous requests are supported for ticket creation but can be disabled by administrators. These anonymous requests have a rate limit of 5 requests per hour for [trial accounts](/documentation/developer-tools/getting-started/getting-a-trial-or-sponsored-account-for-development/). See Create Request below.

Admins and agents are treated as end users when using the Requests endpoint.

#### Multibrand accounts

On the Enterprise plan and above, a Support account can have more than one brand. See [Understanding how Multibrand works in your account](https://support.zendesk.com/hc/en-us/articles/204108983#topic_hyq_l1v_cr) in the Support Help Center.

If you have multiple brands in your account, the Requests API only returns tickets for the brand specified in the API path. It doesn't return all tickets in the account. In the API path, the brand is specified by the subdomain. For example, a GET request to `https://omniwear.zendesk.com/api/v2/requests` only returns tickets for the Omniwear brand, even if Omniwear is the default brand.

#### Status (legacy) and Custom Ticket Status

See [Status (legacy) and Custom Ticket Status in Tickets](/api-reference/ticketing/tickets/tickets/#status-\(legacy\)-and-Custom-Ticket-Status)

### JSON format

Requests are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
assignee_id| integer| true| false| The id of the assignee if the field is visible to end users
can_be_solved_by_me| boolean| true| false| If true, an end user can mark the request as solved. See [Update Request](/api-reference/ticketing/tickets/ticket-requests/#update-request)
collaborator_ids| array| true| false| The ids of users currently CC'ed on the ticket
created_at| string| true| false| When this record was created
custom_fields| array| false| false| Custom fields for the request. See [Setting custom field values](/api-reference/ticketing/tickets/tickets/#setting-custom-field-values) in the Tickets doc
custom_status_id| integer| false| false| The custom ticket status id of the ticket
description| string| true| false| Read-only first comment on the request. When creating a request, use `comment` to set the description
due_at| string| false| false| When the task is due (only applies if the request is of type "task")
email_cc_ids| array| true| false| The ids of users who are currently email CCs on the ticket. See [CCs and followers resources](https://support.zendesk.com/hc/en-us/articles/360020585233) in the Support Help Center
followup_source_id| integer| true| false| The id of the original ticket if this request is a follow-up ticket. See Create Request
group_id| integer| true| false| The id of the assigned group if the field is visible to end users
id| integer| true| false| Automatically assigned when creating requests
is_public| boolean| true| false| Is true if any comments are public, false otherwise
organization_id| integer| true| false| The organization of the requester
priority| string| false| false| The priority of the request, "low", "normal", "high", "urgent"
recipient| string| false| false| The original recipient e-mail address of the request
requester_id| integer| true| false| The id of the requester
solved| boolean| false| false| Whether or not request is solved (an end user can set this if "can_be_solved_by_me", above, is true for that user)
status| string| false| false| The state of the request, "new", "open", "pending", "hold", "solved", "closed"
subject| string| false| true| The value of the subject field for this request if the subject field is visible to end users; a truncated version of the description otherwise
ticket_form_id| integer| false| false| The numeric id of the ticket form associated with this request if the form is visible to end users - only applicable for enterprise accounts
type| string| false| false| The type of the request, "question", "incident", "problem", "task"
updated_at| string| true| false| When this record last got updated
url| string| true| false| The API url of this request
via| object| false| false| Describes how the object was created. See the [Via object reference](/documentation/ticketing/reference-guides/via-object-reference)

#### Request Comments

Comments represent the public conversation between requesters, collaborators and agents on a request.

Request comments have the following properties:

Name| Type| Read-only| Comment
---|---|---|---
id| integer| yes| Automatically assigned when the comment is created
type| string| yes| "Comment" or "VoiceComment"
request_id| integer| yes| The id of the request
body| string| no| The actual comment made by the author
html_body| string| yes| The actual comment made by the author formatted as HTML
plain_body| string| yes| The comment formatted as plain text
public| boolean| yes| If true, the comment is public
author_id| integer| yes| The id of the author
attachments| array| yes| Read-only list of attachments to the comment. See [Attaching files](/documentation/ticketing/managing-tickets/creating-and-updating-tickets#attaching-files)
uploads| array| no*| *On create only. List of tokens received after [uploading files](/api-reference/ticketing/tickets/ticket-attachments/#upload-files) to attach
created_at| date| yes| When this comment was created

#### Request Comment Example


    {  "id": 1274,  "type": "Comment",  "body": "Thanks for your help!",  "html_body": "<p>Thanks for your help!</p>",  "author_id": 1,  "attachments": [    {      "id":           498483,      "name":         "crash.log",      "content_url":  "https://company.zendesk.com/attachments/crash.log",      "content_type": "text/plain",      "size":         2532,      "thumbnails":   []    }  ],  "created_at": "2009-07-20T22:55:29Z"}

#### Example


    {  "assignee_id": 72983,  "can_be_solved_by_me": false,  "collaborator_ids": [],  "created_at": "2009-07-20T22:55:29Z",  "description": "The fire is very colorful.",  "due_at": "2011-05-24T12:00:00Z",  "group_id": 8665,  "id": 35436,  "organization_id": 509974,  "priority": "normal",  "requester_id": 1462,  "status": "open",  "subject": "Help, my printer is on fire!",  "ticket_form_id": 2,  "type": "problem",  "updated_at": "2011-05-05T10:38:52Z",  "url": "https://company.zendesk.com/api/v2/requests/35436",  "via": {    "channel": "web"  }}

### List Requests

  * `GET /api/v2/requests`


#### Allowed for

  * End Users


#### Pagination

  * Cursor pagination (recommended)
  * Offset pagination


See [Pagination](/api-reference/introduction/pagination/).

#### High volume requests

Requesting a large number of tickets may return intermittent "503 Service Unavailable" errors. Workarounds:

  * Use cursor pagination with a smaller page size. Example: GET /api/v2/requests?page[size]=100. If you continue to see timeouts, try a smaller value, such as 50 or 25.
  * Use [Search Requests](/api-reference/ticketing/tickets/ticket-requests/#search-requests) instead.


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
page| | Query| false| Pagination parameter. Supports both traditional offset and cursor-based pagination: - Traditional: `?page=2` (integer page number) - Cursor: `?page[size]=50&page[after]=cursor` (deepObject with size, after, before) These are mutually exclusive - use one format or the other, not both.
per_page| integer| Query| false| Number of records to return per page. Note: Default and maximum values vary by endpoint. Check endpoint-specific documentation for limits.
sort_by| string| Query| false| Possible values are "updated_at", "created_at"
sort_order| string| Query| false| One of "asc", "desc". Defaults to "asc"

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/requests \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/requests?page=&per_page=50&sort_by=&sort_order="	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/requests")		.newBuilder()		.addQueryParameter("page", "")		.addQueryParameter("per_page", "50")		.addQueryParameter("sort_by", "")		.addQueryParameter("sort_order", "");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/requests',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'page': '',    'per_page': '50',    'sort_by': '',    'sort_order': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/requests?page=&per_page=50&sort_by=&sort_order="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/requests")uri.query = URI.encode_www_form("page": "", "per_page": "50", "sort_by": "", "sort_order": "")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "requests": [    {      "custom_status_id": 123,      "description": "My printer is on fire!",      "id": 33,      "status": "open",      "subject": "Help!"    },    {      "custom_status_id": 234,      "description": "I can't find my keys",      "id": 34,      "status": "closed",      "subject": "Help!"    }  ]}

### Search Requests

  * `GET /api/v2/requests/search`


Examples:

  * `GET /api/v2/requests/search?query=printer`
  * `GET /api/v2/requests/search?query=printer&organization_id=1`
  * `GET /api/v2/requests/search?query=printer&cc_id=true`
  * `GET /api/v2/requests/search?query=printer&status=hold,open`


#### Pagination

  * Offset pagination only


See [Using Offset Pagination](/api-reference/introduction/pagination/#using-offset-pagination).

#### Results limit

The Search Requests endpoint returns up to 1,000 results per query, with a maximum of 100 results per page. See [Pagination](/api-reference/ticketing/introduction/#pagination). If you request a page past the limit (`page=11` at 100 results per page), a 422 Insufficient Resource Error is returned.

#### Allowed For

  * End Users


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
query| string| Query| false| The syntax and matching logic for the string is detailed in the [Zendesk Support search reference](https://support.zendesk.com/hc/en-us/articles/203663226). See also [Query basics](/api-reference/ticketing/ticket-management/search/#query-basics) in the Tickets API doc.

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/requests/search?query={search_string} \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/requests/search?query="	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/requests/search")		.newBuilder()		.addQueryParameter("query", "");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/requests/search',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'query': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/requests/search?query="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/requests/search")uri.query = URI.encode_www_form("query": "")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "requests": [    {      "custom_status_id": 123,      "description": "My printer is on fire!",      "id": 33,      "status": "open",      "subject": "Help!"    },    {      "custom_status_id": 234,      "description": "I can't find my keys",      "id": 34,      "status": "closed",      "subject": "Help!"    }  ]}

### Show Request

  * `GET /api/v2/requests/{request_id}`


#### Sideloads

The following sideloads are supported:

Name| Will sideload
---|---
users| The email ccs for a request by side-loading users

#### Allowed For

  * End Users


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
request_id| integer| Path| true| The ID of the request

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/requests/{request_id} \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/requests/33"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/requests/33")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/requests/33',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/requests/33"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/requests/33")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "request": {    "custom_status_id": 123,    "description": "My printer is on fire!",    "id": 33,    "status": "open",    "subject": "Help!"  }}

### Create Request

  * `POST /api/v2/requests`


Accepts a `request` object that sets one or more properties.

#### Allowed for

  * End users
  * Anonymous users (rate limit of 5 requests per hour for [trial accounts](/documentation/developer-tools/getting-started/getting-a-trial-or-sponsored-account-for-development/))


#### Additional properties

In addition to the writable request properties in the JSON Format table above, you can set the following properties when creating a request.

Name| Type| Mandatory| Comment
---|---|---|---
comment| object| yes| Describes the problem, incident, question, or task. See Request comments
collaborators| array| no| Adds collaborators (cc's) to the request. An email notification is sent to them when the ticket is created. See [Setting collaborators](/documentation/ticketing/managing-tickets/creating-and-managing-requests#setting-collaborators)
requester| object| yes*| *Required for anonymous requests. Specifies the requester of the anonymous request. See [Creating anonymous requests](/documentation/ticketing/managing-tickets/creating-and-managing-requests#creating-anonymous-requests)

#### Creating follow-up requests

Once a ticket is closed (as distinct from solved), it can't be reopened. However, you can create a new request that references the closed ticket. To create the follow-up request, include a `via_followup_source_id` property in the `request` object that specifies the closed ticket. The parameter only works with closed tickets. It has no effect with other tickets.

#### Code Samples

**curl**

Authenticated request


    curl https://{subdomain}.zendesk.com/api/v2/requests \  -d '{"request": {"subject": "Help!", "comment": {"body": "My printer is on fire!", "uploads": [...] }}}' \  -v -u {email_address}/token:{api_token} -X POST -H "Content-Type: application/json"

**curl**

Anonymous request


    curl https://{subdomain}.zendesk.com/api/v2/requests \  -d '{"request": {"requester": {"name": "Anonymous customer"}, "subject": "Help!", "comment": {"body": "My printer is on fire!" }}}' \  -X POST -H "Content-Type: application/json"

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/requests"	method := "POST"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/requests")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'POST',  url: 'https://example.zendesk.com/api/v2/requests',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/requests"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/requests")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**201 Created**


    // Status 201 Created
    {  "request": {    "custom_status_id": 1,    "description": "My printer is on fire!",    "id": 33,    "status": "new",    "subject": "Help!"  }}

### Update Request

  * `PUT /api/v2/requests/{request_id}`


Updates a request with a comment or collaborators (cc's). The end user who created the request can also use it to mark the request as solved. The endpoint can't be used to update other request attributes.

#### Writable properties

This endpoint can only update the following properties in the request.

Name| Type| Required| Description
---|---|---|---
comment| object| no| Adds a comment to the request. See Request comments
solved| boolean| no| Marks the request as solved. Example: `{"request": {"solved": "true"}}`. End users can mark requests as solved only if the request's `can_be_solved_by_me` property is true. The property is true only when the ticket is assigned to an agent and the ticket type is not a problem but a question, task, or incident
additional_collaborators| array| no| Adds collaborators to the request. An email notification is sent to them when the ticket is updated. See [Adding collaborators](/documentation/ticketing/managing-tickets/creating-and-managing-requests#adding-collaborators)

#### Allowed For

  * End users


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
request_id| integer| Path| true| The ID of the request

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/requests/{id} \  -d '{"request": {"comment": {"body": "Thanks!"}}}' \  -v -u {email_address}/token:{api_token} -X PUT -H "Content-Type: application/json"

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/requests/33"	method := "PUT"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/requests/33")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'PUT',  url: 'https://example.zendesk.com/api/v2/requests/33',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/requests/33"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/requests/33")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "request": {    "custom_status_id": 1,    "description": "My printer is on fire!",    "id": 33,    "status": "new",    "subject": "Help!"  }}

### Listing Comments

  * `GET /api/v2/requests/{request_id}/comments`


#### Pagination

  * Cursor pagination (recommended)
  * Offset pagination


See [Pagination](/api-reference/introduction/pagination/).

#### Sorting

By default, comments are sorted by creation date in ascending order.

When using cursor pagination, use the following parameter to change the sort order:

Name| Type| Required| Comments
---|---|---|---
`sort`| string| no| Possible values are "created_at" (ascending order) or "-created_at" (descending order)

When using offset pagination, use the following parameters to change the sort order:

Name| Type| Required| Comments
---|---|---|---
`sort_by`| string| no| One of `created_at`, `updated_at`
`sort_order`| string| no| One of `asc`, `desc`

#### Allowed For

  * End Users


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
role| string| Query| false| One of "agent", "end_user". If not specified it does not filter
since| string| Query| false| Filters the comments from the given datetime
request_id| integer| Path| true| The ID of the request

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/requests/{request_id}/comments \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/requests/33/comments?role=&since="	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/requests/33/comments")		.newBuilder()		.addQueryParameter("role", "")		.addQueryParameter("since", "");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/requests/33/comments',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'role': '',    'since': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/requests/33/comments?role=&since="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/requests/33/comments")uri.query = URI.encode_www_form("role": "", "since": "")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "comments": [    {      "body": "Thanks for your help",      "id": 43    }  ]}

### Getting Comments

  * `GET /api/v2/requests/{request_id}/comments/{ticket_comment_id}`


#### Allowed For

  * End Users


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
request_id| integer| Path| true| The ID of the request
ticket_comment_id| integer| Path| true| The ID of the ticket comment

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/requests/{request_id}/comments/{ticket_comment_id} \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/requests/33/comments/35436"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/requests/33/comments/35436")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/requests/33/comments/35436',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/requests/33/comments/35436"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/requests/33/comments/35436")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "comment": {    "body": "Thanks!",    "id": 43  }}

### List CCD Requests

  * `GET /api/v2/requests/ccd`


Lists requests where the authenticated end user is CC'd.

#### Allowed for

  * End Users


#### Pagination

  * Cursor pagination (recommended)
  * Offset pagination


See [Pagination](/api-reference/introduction/pagination/).

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
sort_by| string| Query| false| Possible values are "updated_at", "created_at"
sort_order| string| Query| false| One of "asc", "desc". Defaults to "asc"

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/requests/ccd \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/requests/ccd?sort_by=&sort_order="	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/requests/ccd")		.newBuilder()		.addQueryParameter("sort_by", "")		.addQueryParameter("sort_order", "");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/requests/ccd',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'sort_by': '',    'sort_order': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/requests/ccd?sort_by=&sort_order="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/requests/ccd")uri.query = URI.encode_www_form("sort_by": "", "sort_order": "")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "requests": [    {      "custom_status_id": 123,      "description": "My printer is on fire!",      "id": 33,      "status": "open",      "subject": "Help!"    },    {      "custom_status_id": 234,      "description": "I can't find my keys",      "id": 34,      "status": "closed",      "subject": "Help!"    }  ]}

### List Open Requests

  * `GET /api/v2/requests/open`


Lists requests with the "open" status for the authenticated end user.

#### Allowed for

  * End Users


#### Pagination

  * Cursor pagination (recommended)
  * Offset pagination


See [Pagination](/api-reference/introduction/pagination/).

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
sort_by| string| Query| false| Possible values are "updated_at", "created_at"
sort_order| string| Query| false| One of "asc", "desc". Defaults to "asc"

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/requests/open \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/requests/open?sort_by=&sort_order="	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/requests/open")		.newBuilder()		.addQueryParameter("sort_by", "")		.addQueryParameter("sort_order", "");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/requests/open',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'sort_by': '',    'sort_order': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/requests/open?sort_by=&sort_order="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/requests/open")uri.query = URI.encode_www_form("sort_by": "", "sort_order": "")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "requests": [    {      "custom_status_id": 123,      "description": "My printer is on fire!",      "id": 33,      "status": "open",      "subject": "Help!"    },    {      "custom_status_id": 234,      "description": "I can't find my keys",      "id": 34,      "status": "closed",      "subject": "Help!"    }  ]}

### List Solved Requests

  * `GET /api/v2/requests/solved`


Lists requests with the "solved" status for the authenticated end user.

#### Allowed for

  * End Users


#### Pagination

  * Cursor pagination (recommended)
  * Offset pagination


See [Pagination](/api-reference/introduction/pagination/).

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
sort_by| string| Query| false| Possible values are "updated_at", "created_at"
sort_order| string| Query| false| One of "asc", "desc". Defaults to "asc"

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/requests/solved \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/requests/solved?sort_by=&sort_order="	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/requests/solved")		.newBuilder()		.addQueryParameter("sort_by", "")		.addQueryParameter("sort_order", "");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/requests/solved',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'sort_by': '',    'sort_order': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/requests/solved?sort_by=&sort_order="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/requests/solved")uri.query = URI.encode_www_form("sort_by": "", "sort_order": "")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "requests": [    {      "custom_status_id": 123,      "description": "My printer is on fire!",      "id": 33,      "status": "open",      "subject": "Help!"    },    {      "custom_status_id": 234,      "description": "I can't find my keys",      "id": 34,      "status": "closed",      "subject": "Help!"    }  ]}

### List User Requests

  * `GET /api/v2/users/{user_id}/requests`


Lists requests for the specified user.

#### Allowed for

  * End Users


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
sort_by| string| Query| false| Possible values are "updated_at", "created_at"
sort_order| string| Query| false| One of "asc", "desc". Defaults to "asc"
user_id| integer| Path| true| The id of the user

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/users/{user_id}/requests \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/users/35436/requests?sort_by=&sort_order="	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/users/35436/requests")		.newBuilder()		.addQueryParameter("sort_by", "")		.addQueryParameter("sort_order", "");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/users/35436/requests',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'sort_by': '',    'sort_order': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/users/35436/requests?sort_by=&sort_order="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/users/35436/requests")uri.query = URI.encode_www_form("sort_by": "", "sort_order": "")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "requests": [    {      "custom_status_id": 123,      "description": "My printer is on fire!",      "id": 33,      "status": "open",      "subject": "Help!"    },    {      "custom_status_id": 234,      "description": "I can't find my keys",      "id": 34,      "status": "closed",      "subject": "Help!"    }  ]}

### List Organization Requests

  * `GET /api/v2/organizations/{organization_id}/requests`


Returns a list of requests for a specific organization.

#### Allowed for

  * End Users


#### Pagination

  * Cursor pagination (recommended)
  * Offset pagination


See [Pagination](/api-reference/introduction/pagination/).

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
sort_by| string| Query| false| Possible values are "updated_at", "created_at"
sort_order| string| Query| false| One of "asc", "desc". Defaults to "asc"
organization_id| integer| Path| true| The ID of an organization

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/organizations/{organization_id}/requests \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/organizations/16/requests?sort_by=&sort_order="	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/organizations/16/requests")		.newBuilder()		.addQueryParameter("sort_by", "")		.addQueryParameter("sort_order", "");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/organizations/16/requests',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'sort_by': '',    'sort_order': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/organizations/16/requests?sort_by=&sort_order="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/organizations/16/requests")uri.query = URI.encode_www_form("sort_by": "", "sort_order": "")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "requests": [    {      "custom_status_id": 123,      "description": "My printer is on fire!",      "id": 33,      "status": "open",      "subject": "Help!"    },    {      "custom_status_id": 234,      "description": "I can't find my keys",      "id": 34,      "status": "closed",      "subject": "Help!"    }  ]}

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)