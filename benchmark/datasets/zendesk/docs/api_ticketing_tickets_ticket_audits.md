# Ticket Audits

*Source: https://developer.zendesk.com/api-reference/ticketing/tickets/ticket_audits/*

---

## On this page

  * [Required OAuth scope](/api-reference/ticketing/tickets/ticket_audits/#required-oauth-scope)
  * [JSON format](/api-reference/ticketing/tickets/ticket_audits/#json-format)
  * [List All Ticket Audits](/api-reference/ticketing/tickets/ticket_audits/#list-all-ticket-audits)
  * [List Audits for a Ticket](/api-reference/ticketing/tickets/ticket_audits/#list-audits-for-a-ticket)
  * [Count Audits for a Ticket](/api-reference/ticketing/tickets/ticket_audits/#count-audits-for-a-ticket)
  * [Show Audit](/api-reference/ticketing/tickets/ticket_audits/#show-audit)
  * [Change a Comment From Public To Private](/api-reference/ticketing/tickets/ticket_audits/#change-a-comment-from-public-to-private)


# Ticket Audits

## On this page

  * [Required OAuth scope](/api-reference/ticketing/tickets/ticket_audits/#required-oauth-scope)
  * [JSON format](/api-reference/ticketing/tickets/ticket_audits/#json-format)
  * [List All Ticket Audits](/api-reference/ticketing/tickets/ticket_audits/#list-all-ticket-audits)
  * [List Audits for a Ticket](/api-reference/ticketing/tickets/ticket_audits/#list-audits-for-a-ticket)
  * [Count Audits for a Ticket](/api-reference/ticketing/tickets/ticket_audits/#count-audits-for-a-ticket)
  * [Show Audit](/api-reference/ticketing/tickets/ticket_audits/#show-audit)
  * [Change a Comment From Public To Private](/api-reference/ticketing/tickets/ticket_audits/#change-a-comment-from-public-to-private)


Audits are a read-only history of all updates to a ticket. When a ticket is updated in Zendesk Support, an audit is stored. Each audit represents a single update to the ticket. An update can consist of one or more events. Examples:

  * The value of a ticket field was changed
  * A new comment was added
  * Tags were added or removed
  * A notification was sent


For a complete list, see the [Ticket Audit events reference](/documentation/ticketing/reference-guides/ticket-audit-events-reference).

### Required OAuth scope

The Ticket Audits endpoints require a global "read" scope for OAuth authentication. You can't access the endpoints using the "auditlogs:read" or "tickets:read" scopes.

### JSON format

Ticket Audits are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
author_id| integer| true| false| The user who created the audit
created_at| string| true| false| The time the audit was created
events| array| false| false| An array of the events that happened in this audit. See the [Ticket Audit events reference](/documentation/ticketing/reference-guides/ticket-audit-events-reference)
id| integer| true| false| Automatically assigned when creating audits
metadata| object| true| false| Metadata for the audit, custom and system data
ticket_id| integer| true| false| The ID of the associated ticket
via| object| false| false| Describes how the object was created. See the [Via object reference](/documentation/ticketing/reference-guides/via-object-reference)

#### Example


    {  "author_id": 35436,  "created_at": "2009-07-20T22:55:29Z",  "events": [    {      "attachments": [],      "body": "Thanks for your help!",      "id": 1564245,      "public": true,      "type": "Comment"    },    {      "body": "Ticket #47 has been updated",      "id": 1564246,      "subject": "Your ticket has been updated",      "type": "Notification"    }  ],  "id": 35436,  "metadata": {    "custom": {      "time_spent": "3m22s"    },    "system": {      "ip_address": "184.106.40.75"    }  },  "ticket_id": 47,  "via": {    "channel": "web"  }}

### List All Ticket Audits

  * `GET /api/v2/ticket_audits`


Returns ticket audits. Archived tickets are not included in the response. Use the List Audits for a Ticket endpoint to retrieve audit records for an archived ticket. To learn more about archived tickets, see [About archived tickets](https://support.zendesk.com/hc/en-us/articles/203657756).

This endpoint should not be used for capturing change data. When continually chasing the tail of a cursor, some records will be skipped. For this use case, use the [Incremental Ticket Event Export API](/api-reference/ticketing/ticket-management/incremental_exports/#incremental-ticket-event-export).

#### Allowed For

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
page[after]| string| Query| false| A [pagination cursor](/documentation/api-basics/pagination/paginating-through-lists-using-cursor-pagination) that tells the endpoint which page to start on. It should be a `meta.after_cursor` value from a previous request. Note: `page[before]` and `page[after]` can't be used together in the same request.
page[before]| string| Query| false| A [pagination cursor](/documentation/api-basics/pagination/paginating-through-lists-using-cursor-pagination) that tells the endpoint which page to start on. It should be a `meta.before_cursor` value from a previous request. Note: `page[before]` and `page[after]` can't be used together in the same request.
page[size]| integer| Query| false| Specifies how many records to be returned in the response. You can specify up to 100 records per page.

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/ticket_audits?page[size]=100 \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/ticket_audits?page[after]=&page[before]=&page[size]="	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/ticket_audits")		.newBuilder()		.addQueryParameter("page[after]", "")		.addQueryParameter("page[before]", "")		.addQueryParameter("page[size]", "");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/ticket_audits',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'page[after]': '',    'page[before]': '',    'page[size]': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/ticket_audits?page[after]=&page[before]=&page[size]="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/ticket_audits")uri.query = URI.encode_www_form("page[after]": "", "page[before]": "", "page[size]": "")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "after_cursor": "MTUwMTYwNzUyMi4wfHwxMzQ3NTMxNjcxfA==",  "after_url": "https://subdomain.zendesk.com/api/v2/ticket_audits?cursor=MTUwMTYwNzUyMi4wfHwxMzQ3NTMxNjcxfA%3D%3D&limit=1000",  "audits": [    {      "author_id": 35436,      "created_at": "2011-09-25T22:35:44Z",      "events": [        {          "attachments": [],          "body": "Thanks for your help!",          "id": 1564245,          "public": true,          "type": "Comment"        },        {          "body": "Ticket #47 has been updated",          "id": 1564246,          "subject": "Your ticket has been updated",          "type": "Notification"        },        {          "field_name": "status",          "id": 1564247,          "previous_value": "new",          "type": "Change",          "value": "open"        },        {          "field_name": "custom_status_id",          "id": 1564248,          "previous_value": 1,          "type": "Change",          "value": 123        }      ],      "id": 2127301143,      "metadata": {        "custom": {          "time_spent": "3m22s"        },        "system": {          "ip_address": "184.106.40.75"        }      },      "ticket_id": 123,      "via": {        "channel": "web"      }    }  ],  "before_cursor": "fDE1MDE1NzUxMjIuMHx8MTM0NzM0MzAxMQ==",  "before_url": "https://subdomain.zendesk.com/api/v2/ticket_audits?cursor=fDE1MDE1NzUxMjIuMHx8MTM0NzM0MzAxMQ%3D%3D&limit=1000"}

### List Audits for a Ticket

  * `GET /api/v2/tickets/{ticket_id}/audits`


Lists the audits for a specified ticket.

#### Pagination

  * Cursor pagination (recommended)
  * Offset pagination


See [Pagination](/api-reference/introduction/pagination/).

Returns a maximum of 100 records per page.

**Note** : Audits for [Archived Tickets](https://support.zendesk.com/hc/en-us/articles/4408887617050) do not support pagination for this endpoint.

#### Allowed for

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
filter_events| array| Query| false| Filter audit events by type. Use the format `filter_events[]=Type1&filter_events[]=Type2`.
include| string| Query| false| A comma-separated list of sideloads to include in the response.
include_boundary_indicators| boolean| Query| false| When true, includes `has_more` indicator in the cursor pagination response meta. Only valid with cursor pagination (page[size], page[after], page[before]).
include_item_cursors| boolean| Query| false| When true, includes cursor values for each item in the cursor pagination response. Only valid with cursor pagination (page[size], page[after], page[before]).
page| | Query| false| Pagination parameter. Supports both traditional offset and cursor-based pagination: - Traditional: `?page=2` (integer page number) - Cursor: `?page[size]=50&page[after]=cursor` (deepObject with size, after, before) These are mutually exclusive - use one format or the other, not both.
sort| string| Query| false| Field to sort results by. Prefix with `-` for descending order. When used with cursor pagination, this determines the cursor ordering. Example: `?sort=name` or `?sort=-created_at`
sort_order| string| Query| false| Sort order. Defaults to "asc". Allowed values are "asc", or "desc".
ticket_id| integer| Path| true| The ID of the ticket

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/tickets/{ticket_id}/audits \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/tickets/123456/audits?filter_events=&include=&include_boundary_indicators=&include_item_cursors=&page=&sort=name&sort_order="	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/tickets/123456/audits")		.newBuilder()		.addQueryParameter("filter_events", "")		.addQueryParameter("include", "")		.addQueryParameter("include_boundary_indicators", "")		.addQueryParameter("include_item_cursors", "")		.addQueryParameter("page", "")		.addQueryParameter("sort", "name")		.addQueryParameter("sort_order", "");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/tickets/123456/audits',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'filter_events': '',    'include': '',    'include_boundary_indicators': '',    'include_item_cursors': '',    'page': '',    'sort': 'name',    'sort_order': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/tickets/123456/audits?filter_events=&include=&include_boundary_indicators=&include_item_cursors=&page=&sort=name&sort_order="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/tickets/123456/audits")uri.query = URI.encode_www_form("filter_events": "", "include": "", "include_boundary_indicators": "", "include_item_cursors": "", "page": "", "sort": "name", "sort_order": "")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "audits": [    {      "author_id": 5246746,      "created_at": "2011-09-25T22:35:44Z",      "events": [        {          "attachments": [],          "body": "This is a new private comment",          "html_body": "<p>This is a new private comment</p>",          "id": 2127301148,          "public": false,          "type": "Comment"        },        {          "field_name": "status",          "id": 2127301163,          "previous_value": "new",          "type": "Change",          "value": "open",          "via": {            "channel": "rule",            "source": {              "from": {                "id": 35079792,                "title": "Assign to first responder"              },              "rel": "trigger",              "to": {}            }          }        },        {          "field_name": "custom_status_id",          "id": 2127301164,          "previous_value": 1,          "type": "Change",          "value": 123,          "via": {            "channel": "rule",            "source": {              "from": {                "id": 22472716,                "title": "Assign to first responder"              },              "rel": "trigger",              "to": {}            }          }        }      ],      "id": 2127301143,      "metadata": {        "custom": {},        "system": {          "client": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.186 Safari/535.1",          "ip_address": "76.218.201.212",          "location": "San Francisco, CA, United States"        }      },      "ticket_id": 666,      "via": {        "channel": "web"      }    }  ],  "count": 1,  "next_page": null,  "previous_page": null}

### Count Audits for a Ticket

  * `GET /api/v2/tickets/{ticket_id}/audits/count`


Returns an approximate count of audits for a specified ticket. If the count exceeds 100,000, the count will return a cached result. This cached result will update every 24 hours.

The `count[refreshed_at]` property is a timestamp that indicates when the count was last updated.

**Note** : If the total number of audits for a ticket exceeds 100,000, this endpoint returns a count of 100,000 with a `count[refreshed_at]` value of null. This value is cached for 24 hours, during which any requests returns the same count and timestamp. After 24 hours, the endpoint temporarily shows the same count again before providing an updated total.

#### Allowed for

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
ticket_id| integer| Path| true| The ID of the ticket

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/tickets/{ticket_id}/audits/count \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/tickets/123456/audits/count"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/tickets/123456/audits/count")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/tickets/123456/audits/count',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/tickets/123456/audits/count"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/tickets/123456/audits/count")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "count": {    "refreshed_at": "2020-04-06T02:18:17Z",    "value": 18  }}

### Show Audit

  * `GET /api/v2/tickets/{ticket_id}/audits/{ticket_audit_id}`


#### Allowed for

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
ticket_audit_id| integer| Path| true| The ID of the ticket audit
ticket_id| integer| Path| true| The ID of the ticket

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/tickets/{ticket_id}/audits \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/tickets/123456/audits/2127301143"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/tickets/123456/audits/2127301143")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/tickets/123456/audits/2127301143',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/tickets/123456/audits/2127301143"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/tickets/123456/audits/2127301143")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "audit": {    "author_id": 5246746,    "created_at": "2011-09-25T22:35:44Z",    "events": [      {        "attachments": [],        "body": "This is a new private comment",        "html_body": "<p>This is a new private comment</p>",        "id": 2127301148,        "public": false,        "type": "Comment"      },      {        "field_name": "status",        "id": 2127301163,        "previous_value": "new",        "type": "Change",        "value": "open",        "via": {          "channel": "rule",          "source": {            "from": {              "id": 22472716,              "title": "Assign to first responder"            },            "rel": "trigger",            "to": {}          }        }      },      {        "field_name": "custom_status_id",        "id": 2127301164,        "previous_value": 1,        "type": "Change",        "value": 123,        "via": {          "channel": "rule",          "source": {            "from": {              "id": 22472716,              "title": "Assign to first responder"            },            "rel": "trigger",            "to": {}          }        }      }    ],    "id": 2127301143,    "metadata": {      "custom": {},      "system": {        "client": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.186 Safari/535.1",        "ip_address": "76.218.201.212",        "location": "San Francisco, CA, United States"      }    },    "ticket_id": 666,    "via": {      "channel": "web"    }  }}

### Change a Comment From Public To Private

  * `PUT /api/v2/tickets/{ticket_id}/audits/{ticket_audit_id}/make_private`


#### Allowed for

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
ticket_audit_id| integer| Path| true| The ID of the ticket audit
ticket_id| integer| Path| true| The ID of the ticket

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/tickets/{ticket_id}/audits/{ticket_audit_id}/make_private \  -v -u {email_address}/token:{api_token} -X PUT -d '{}' -H "Content-Type: application/json"

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/tickets/123456/audits/2127301143/make_private"	method := "PUT"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/tickets/123456/audits/2127301143/make_private")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'PUT',  url: 'https://example.zendesk.com/api/v2/tickets/123456/audits/2127301143/make_private',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/tickets/123456/audits/2127301143/make_private"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/tickets/123456/audits/2127301143/make_private")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    null

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)