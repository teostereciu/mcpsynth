# Incremental Exports

*Source: https://developer.zendesk.com/api-reference/ticketing/ticket-management/incremental_exports/*

---

## On this page

  * [JSON Format](/api-reference/ticketing/ticket-management/incremental_exports/#json-format)
  * [Query String Parameters](/api-reference/ticketing/ticket-management/incremental_exports/#query-string-parameters)
  * [Incremental Ticket Metric Event Export](/api-reference/ticketing/ticket-management/incremental_exports/#incremental-ticket-metric-event-export)
  * [Incremental Custom Object Record Export](/api-reference/ticketing/ticket-management/incremental_exports/#incremental-custom-object-record-export)
  * [Incremental Article Export](/api-reference/ticketing/ticket-management/incremental_exports/#incremental-article-export)
  * [Incremental Ticket Export, Cursor Based](/api-reference/ticketing/ticket-management/incremental_exports/#incremental-ticket-export-cursor-based)
  * [Incremental Ticket Export, Time Based](/api-reference/ticketing/ticket-management/incremental_exports/#incremental-ticket-export-time-based)
  * [Incremental Ticket Event Export](/api-reference/ticketing/ticket-management/incremental_exports/#incremental-ticket-event-export)
  * [Incremental User Export, Cursor Based](/api-reference/ticketing/ticket-management/incremental_exports/#incremental-user-export-cursor-based)
  * [Incremental User Export, Time Based](/api-reference/ticketing/ticket-management/incremental_exports/#incremental-user-export-time-based)
  * [Incremental Organization Export](/api-reference/ticketing/ticket-management/incremental_exports/#incremental-organization-export)
  * [Incremental Sample Export](/api-reference/ticketing/ticket-management/incremental_exports/#incremental-sample-export)


# Incremental Exports

## On this page

  * [JSON Format](/api-reference/ticketing/ticket-management/incremental_exports/#json-format)
  * [Query String Parameters](/api-reference/ticketing/ticket-management/incremental_exports/#query-string-parameters)
  * [Incremental Ticket Metric Event Export](/api-reference/ticketing/ticket-management/incremental_exports/#incremental-ticket-metric-event-export)
  * [Incremental Custom Object Record Export](/api-reference/ticketing/ticket-management/incremental_exports/#incremental-custom-object-record-export)
  * [Incremental Article Export](/api-reference/ticketing/ticket-management/incremental_exports/#incremental-article-export)
  * [Incremental Ticket Export, Cursor Based](/api-reference/ticketing/ticket-management/incremental_exports/#incremental-ticket-export-cursor-based)
  * [Incremental Ticket Export, Time Based](/api-reference/ticketing/ticket-management/incremental_exports/#incremental-ticket-export-time-based)
  * [Incremental Ticket Event Export](/api-reference/ticketing/ticket-management/incremental_exports/#incremental-ticket-event-export)
  * [Incremental User Export, Cursor Based](/api-reference/ticketing/ticket-management/incremental_exports/#incremental-user-export-cursor-based)
  * [Incremental User Export, Time Based](/api-reference/ticketing/ticket-management/incremental_exports/#incremental-user-export-time-based)
  * [Incremental Organization Export](/api-reference/ticketing/ticket-management/incremental_exports/#incremental-organization-export)
  * [Incremental Sample Export](/api-reference/ticketing/ticket-management/incremental_exports/#incremental-sample-export)


Use the incremental export API to get items that changed or were created in Zendesk Support since the last request. It works something like this:

  * **Request at 5pm** : "Give me all the tickets that changed since noon today."
  * **Response** : "Here are the tickets that changed since noon up until, and including, 5pm."
  * **Request at 7pm** : "Give me the tickets that changed since 5pm."
  * **Response** : "Here are the tickets that changed since 5pm up until, and including, 7pm."


To learn more, see the following topics in [Using the Incremental Export API](/documentation/ticketing/managing-tickets/using-the-incremental-export-api/):

  * [Incremental export workflow](/documentation/ticketing/managing-tickets/using-the-incremental-export-api/#incremental-export-workflow)
  * [Cursor-based incremental exports](/documentation/ticketing/managing-tickets/using-the-incremental-export-api/#cursor-based-incremental-exports)
  * [Time-based incremental exports](/documentation/ticketing/managing-tickets/using-the-incremental-export-api/#time-based-incremental-exports)
  * [Exporting tickets](/documentation/ticketing/managing-tickets/using-the-incremental-export-api/#exporting-tickets)
  * [Exporting ticket events](/documentation/ticketing/managing-tickets/using-the-incremental-export-api/#exporting-ticket-events)
  * [Excluding deleted tickets](/documentation/ticketing/managing-tickets/using-the-incremental-export-api/#excluding-deleted-tickets)


#### Rate limits

You can make up to 10 requests per minute to these endpoints.

The rate limiting mechanism behaves identically to the one described in [Rate limits](/api-reference/introduction/rate-limits/#monitoring-your-request-activity). We recommend using the `Retry-After` header value as described in [Catching errors caused by rate limiting](/documentation/ticketing/using-the-zendesk-api/best-practices-for-avoiding-rate-limiting#catch).

### JSON Format

The exported items are represented as JSON objects. The format depends on the exported resource and pagination type, but all have the following additional common attribute:

Name| Type| Comment
---|---|---
end_of_stream| boolean| true if the current request has returned all the results up to the current time; false otherwise

To test the response format of an incremental export for a specific resource, you can run a sample export that returns only up to 50 results per request. See Incremental Sample Export.

#### Cursor-based Pagination JSON Format

Name| Type| Comment
---|---|---
after_url| string| URL to fetch the next page of results
after_cursor| string| Cursor to fetch the next page of results
before_url| string| URL to fetch the previous page of results. If there's no previous page, the value is null
before_cursor| string| Cursor to fetch the previous page of results. If there's no previous page, the value is null

#### Time-based Pagination JSON Format

Name| Type| Comment
---|---|---
end_time| date| The most recent time present in the result set expressed as a Unix epoch time. Use as the `start_time` to fetch the next page of results
next_page| string| URL to fetch the next page of results
count| integer| The number of results returned for the current request

### Query String Parameters

Name| Required| Comment
---|---|---
start_time| yes| A start time expressed as a Unix epoch time. See start_time
cursor| cursor only| A cursor pointer. See cursor
per_page| no| Number of results to return per page, up to a maximum of 1,000. If the parameter is not specified, the default number is 1,000. See per_page
include| no| The name of a resource to side-load. See include
exclude_deleted| no| Whether or not you'd like to exclude deleted tickets from the response. See exclude_deleted

#### start_time

Specifies a time expressed as a [Unix epoch time](http://www.epochconverter.com/). All endpoints require a `start_time` parameter for the initial export. Example:

`GET /api/v2/incremental/tickets/cursor?start_time=1532034771`

The `start_time` of the initial export is arbitrary. The time must be more than one minute in the past to avoid missing data. To prevent race conditions, the ticket and ticket event export endpoints will not return data for the most recent minute.

When using [time-based incremental exports](/documentation/ticketing/managing-tickets/using-the-incremental-export-api#time-based-incremental-exports), subsequent pages and exports use the `start_time` parameter.

When using [cursor-based incremental exports](/documentation/ticketing/managing-tickets/using-the-incremental-export-api/#cursor-based-incremental-exports), the `start_time` parameter is only used in the initial request. Subsequent pages and exports use the `cursor` parameter.

#### cursor

Specifies a cursor pointer when using cursor-based exports. The `cursor` parameter is used to fetch the next page of results or to make the next export. The `start_time` parameter is used once to fetch the initial page of the initial export, then `cursor` is used for subsequent pages and exports.

The `cursor` parameter is only supported for incremental ticket exports.

Example:


    https://{{subdomain}}.zendesk.com/api/v2/incremental/tickets/cursor?cursor=MTU3NjYxMzUzOS4wfHw0Njd8

See [Paginating through lists using cursor pagination](/documentation/developer-tools/pagination/paginating-through-lists-using-cursor-pagination/) for more details.

#### per_page

Specifies the number of results to be returned per page, up to a maximum of 1,000. The default is 1,000. The following incremental exports support the `per_page` parameter:

  * tickets
  * ticket events
  * users (time-based)
  * users (cursor-based)
  * organizations (time-based)


Example:


    https://{subdomain}.zendesk.com/api/v2/incremental/tickets?per_page=100&start_time=1332034771

If requests are slow or begin to time out, the page size might be too large. Use the `per_page` parameter to reduce the number of results per page. We recommend progressively backing-off on the `per_page` parameter after each time out.

**Note** : In time-based exports, the system may exceed the 1000-item default return limit if items share the same timestamp. If exporting tickets, using cursor-based pagination can fix this issue.

#### include

Side-loads other resources. The following incremental exports support the `include` parameter:

  * tickets
  * ticket events
  * users
  * organizations


Add an `include` query parameter specifying the associations you want to load. Example:


    https://{subdomain}.zendesk.com/api/v2/incremental/tickets?start_time=1332034771&include=metric_sets

See [Side-Loading](/documentation/ticketing/using-the-zendesk-api/side_loading/) in the core API docs as well as any specific sideloading information in the endpoint docs below.

**Note** : The `last_audits` side-load is not supported on incremental endpoints for performance reasons.

#### exclude_deleted

If true, excludes deleted tickets from the response. By default, deletions will appear in the ticket stream. If used in combination with the Incremental Ticket Export, you can separate your deleted ticket activity from your live data.

Example:


    https://{subdomain}.zendesk.com/api/v2/incremental/tickets/cursor?exclude_deleted=true&cursor=MTU3NjYxMzUzOS4wfHw0Njd8

### Incremental Ticket Metric Event Export

See [List Ticket Metric Events](/api-reference/ticketing/tickets/ticket_metric_events/#list-ticket-metric-events).

### Incremental Custom Object Record Export

See [Incremental Custom Object Record Export, Cursor Based](/api-reference/custom-data/custom-objects/custom_object_records/#incremental-custom-object-record-export-cursor-based) in the Custom Object API docs.

### Incremental Article Export

See [List Articles](/api-reference/help_center/help-center-api/articles/#list-articles) in the Help Center API docs.

### Incremental Ticket Export, Cursor Based

  * `GET /api/v2/incremental/tickets/cursor`


Returns the tickets that changed since the start time. For more information, see [Exporting tickets](/documentation/ticketing/managing-tickets/using-the-incremental-export-api#exporting-tickets) in [Using the Incremental Exports API](/documentation/ticketing/managing-tickets/using-the-incremental-export-api).

This endpoint supports cursor-based incremental exports. Cursor-based exports are highly encouraged because they provide more consistent performance and response body sizes. For more information, see [Cursor-based incremental exports](/documentation/ticketing/managing-tickets/using-the-incremental-export-api#cursor-based-incremental-exports) in [Using the Incremental Exports API](/documentation/ticketing/managing-tickets/using-the-incremental-export-api).

#### Allowed For

  * Admins


#### Sideloading

See [Tickets sideloads](/documentation/ticketing/using-the-zendesk-api/side_loading/#supported-endpoints). For performance reasons, `last_audits` sideloads aren't supported.

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
cursor| string| Query| false| The cursor pointer to work with for all subsequent exports after the initial request
start_time| integer| Query| false| The time to start the incremental export from. Must be at least one minute in the past. Data isn't provided for the most recent minute. Required on the initial export request; not required on subsequent cursor-based pagination requests
support_type_scope| string| Query| false| Lists tickets by support type. Possible values are "all", "agent", or "ai_agent". Defaults to "agent"

#### Code Samples

**curl**

Cursor-based export


    # Cursor-based export, Initial requestcurl https://{subdomain}.zendesk.com/api/v2/incremental/tickets/cursor?start_time=1332034771 \  -v -u {email_address}/token:{api_token}
    # Cursor-based export, Subsequent requestscurl https://{subdomain}.zendesk.com/api/v2/incremental/tickets/cursor?cursor=MTU3NjYxMzUzOS4wfHw0NTF8 \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/incremental/tickets/cursor?cursor=&start_time=1332034771&support_type_scope="	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/incremental/tickets/cursor")		.newBuilder()		.addQueryParameter("cursor", "")		.addQueryParameter("start_time", "1332034771")		.addQueryParameter("support_type_scope", "");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/incremental/tickets/cursor',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'cursor': '',    'start_time': '1332034771',    'support_type_scope': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/incremental/tickets/cursor?cursor=&start_time=1332034771&support_type_scope="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/incremental/tickets/cursor")uri.query = URI.encode_www_form("cursor": "", "start_time": "1332034771", "support_type_scope": "")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "after_cursor": "MTU3NjYxMzUzOS4wfHw0Njd8",  "after_url": "https://{subdomain}.zendesk.com/api/v2/incremental/tickets/cursor?cursor=MTU3NjYxMzUzOS4wfHw0Njd8",  "before_cursor": null,  "before_url": null,  "end_of_stream": true,  "tickets": [    {      "assignee_id": 235323,      "collaborator_ids": [        35334,        234      ],      "created_at": "2009-07-20T22:55:29Z",      "custom_fields": [        {          "id": 27642,          "value": "745"        },        {          "id": 27648,          "value": "yes"        }      ],      "description": "The fire is very colorful.",      "due_at": null,      "external_id": "ahg35h3jh",      "follower_ids": [        35334,        234      ],      "from_messaging_channel": false,      "generated_timestamp": 1304553600,      "group_id": 98738,      "has_incidents": false,      "id": 35436,      "organization_id": 509974,      "priority": "high",      "problem_id": 9873764,      "raw_subject": "{{dc.printer_on_fire}}",      "recipient": "[[email protected]](/cdn-cgi/l/email-protection)",      "requester_id": 20978392,      "satisfaction_rating": {        "comment": "Great support!",        "id": 1234,        "score": "good"      },      "sharing_agreement_ids": [        84432      ],      "status": "open",      "subject": "Help, my printer is on fire!",      "submitter_id": 76872,      "tags": [        "enterprise",        "other_tag"      ],      "type": "incident",      "updated_at": "2011-05-05T10:38:52Z",      "url": "https://company.zendesk.com/api/v2/tickets/35436",      "via": {        "channel": "web"      }    }  ]}

### Incremental Ticket Export, Time Based

  * `GET /api/v2/incremental/tickets?start_time={start_time}`


Returns the tickets that changed since the start time. For more information, see [Exporting tickets](/documentation/ticketing/managing-tickets/using-the-incremental-export-api#exporting-tickets) in [Using the Incremental Exports API](/documentation/ticketing/managing-tickets/using-the-incremental-export-api).

This endpoint supports time-based incremental exports. For more information, see [Time-based incremental exports](/documentation/ticketing/managing-tickets/using-the-incremental-export-api#time-based-incremental-exports) in [Using the Incremental Exports API](/documentation/ticketing/managing-tickets/using-the-incremental-export-api). You can also return tickets using cursor-based pagination. See Incremental Ticket Export, Cursor Based.

The results include tickets that were updated by the system. See [Excluding system-updated tickets](/documentation/ticketing/managing-tickets/using-the-incremental-export-api#excluding-system-updated-tickets-time-based-exports) in [Using the Incremental Exports API](/documentation/ticketing/managing-tickets/using-the-incremental-export-api).

The endpoint can return tickets with an `updated_at` time that's earlier than the `start_time` time. The reason is that the API compares the `start_time` with the ticket's `generated_timestamp` value, not its `updated_at` value. The `updated_at` value is updated only if the update generates a ticket event. The `generated_timestamp` value is updated for all ticket updates, including system updates. If a system update occurs after a ticket event, the unchanged `updated_at` time will become earlier relative to the updated `generated_timestamp` time.

#### Allowed For

  * Admins


#### Sideloading

See [Tickets sideloads](/documentation/ticketing/using-the-zendesk-api/side_loading/#supported-endpoints). For performance reasons, `last_audits` sideloads aren't supported.

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
start_time| integer| Query| true| The time to start the incremental export from. Must be at least one minute in the past. Data isn't provided for the most recent minute
support_type_scope| string| Query| false| Lists tickets by support type. Possible values are "all", "agent", or "ai_agent". Defaults to "agent"

#### Code Samples

**curl**

Time-based export


    curl https://{subdomain}.zendesk.com/api/v2/incremental/tickets?start_time=1332034771 \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/incremental/tickets?start_time=1332034771&support_type_scope="	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/incremental/tickets")		.newBuilder()		.addQueryParameter("start_time", "1332034771")		.addQueryParameter("support_type_scope", "");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/incremental/tickets',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'start_time': '1332034771',    'support_type_scope': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/incremental/tickets?start_time=1332034771&support_type_scope="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/incremental/tickets")uri.query = URI.encode_www_form("start_time": "1332034771", "support_type_scope": "")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "count": 2,  "end_of_stream": true,  "end_time": 1390362485,  "next_page": "https://{subdomain}.zendesk.com/api/v2/incremental/tickets?per_page=3&start_time=1390362485",  "tickets": [    {      "assignee_id": 235323,      "collaborator_ids": [        35334,        234      ],      "created_at": "2009-07-20T22:55:29Z",      "custom_fields": [        {          "id": 27642,          "value": "745"        },        {          "id": 27648,          "value": "yes"        }      ],      "description": "The fire is very colorful.",      "due_at": null,      "external_id": "ahg35h3jh",      "follower_ids": [        35334,        234      ],      "from_messaging_channel": false,      "generated_timestamp": 1304553600,      "group_id": 98738,      "has_incidents": false,      "id": 35436,      "organization_id": 509974,      "priority": "high",      "problem_id": 9873764,      "raw_subject": "{{dc.printer_on_fire}}",      "recipient": "[[email protected]](/cdn-cgi/l/email-protection)",      "requester_id": 20978392,      "satisfaction_rating": {        "comment": "Great support!",        "id": 1234,        "score": "good"      },      "sharing_agreement_ids": [        84432      ],      "status": "open",      "subject": "Help, my printer is on fire!",      "submitter_id": 76872,      "tags": [        "enterprise",        "other_tag"      ],      "type": "incident",      "updated_at": "2011-05-05T10:38:52Z",      "url": "https://company.zendesk.com/api/v2/tickets/35436",      "via": {        "channel": "web"      }    }  ]}

### Incremental Ticket Event Export

  * `GET /api/v2/incremental/ticket_events?start_time={start_time}`


Returns a stream of changes that occurred on tickets, excluding events occuring within one minute of the request. Each event is tied to an update on a ticket and contains all the fields that were updated in that change. For more information, see:

  * [Exporting ticket events](/documentation/ticketing/managing-tickets/using-the-incremental-export-api#exporting-ticket-events) in [Using the Incremental Exports API](/documentation/ticketing/managing-tickets/using-the-incremental-export-api)
  * [Time-based incremental exports](/documentation/ticketing/managing-tickets/using-the-incremental-export-api#time-based-incremental-exports) in [Using the Incremental Exports API](/documentation/ticketing/managing-tickets/using-the-incremental-export-api)


You can include comments in the event stream by using the `comment_events` sideload. See Sideloading below. If you don't specify the sideload, any comment present in the ticket update is described only by Boolean `comment_present` and `comment_public` object properties in the event's `child_events` array. The comment itself is not included.

#### Allowed For

  * Admins


#### Sideloading

The endpoint supports the `comment_events` sideload. Any comment present in the ticket update is listed as an object in the event's `child_events` array. Example:


    "child_events": [  {    "id": 91048994488,    "via": {      "channel": "api",      "source": {"from":{},"to":{},"rel":null}},    "via_reference_id":null,    "type": "Comment",    "author_id": 5031726587,    "body": "This is a comment",    "html_body": "&lt;div class="zd-comment"&gt;&lt;p dir="auto"&gt;This is a comment&lt;/p&gt;",    "public": true,    "attachments": [],    "audit_id": 91048994468,    "created_at": "2009-06-25T10:15:18Z",    "event_type": "Comment"  },  ...],...

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
include| string| Query| false| Sideloads to include in the response. Accepts a comma-separated list of values. Supports `comment_events` to include full comment data in the response.
start_time| integer| Query| true| The time to start the incremental export from. Must be at least one minute in the past. Data isn't provided for the most recent minute
support_type_scope| string| Query| false| Lists tickets by support type. Possible values are "all", "agent", or "ai_agent". Defaults to "agent"

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/incremental/ticket_events?start_time=1332034771 \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/incremental/ticket_events?include=comment_events&start_time=1332034771&support_type_scope="	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/incremental/ticket_events")		.newBuilder()		.addQueryParameter("include", "comment_events")		.addQueryParameter("start_time", "1332034771")		.addQueryParameter("support_type_scope", "");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/incremental/ticket_events',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'include': 'comment_events',    'start_time': '1332034771',    'support_type_scope': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/incremental/ticket_events?include=comment_events&start_time=1332034771&support_type_scope="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/incremental/ticket_events")uri.query = URI.encode_www_form("include": "comment_events", "start_time": "1332034771", "support_type_scope": "")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "count": 1,  "end_of_stream": true,  "end_time": 1601357503,  "next_page": "https://example.zendesk.com/api/v2/incremental/ticket_events?start_time=1601357503",  "ticket_events": [    {      "id": 926256957613,      "instance_id": 1,      "metric": "agent_work_time",      "ticket_id": 155,      "time": "2020-10-26T12:53:12Z",      "type": "measure"    }  ]}

### Incremental User Export, Cursor Based

  * `GET /api/v2/incremental/users/cursor`


#### Allowed For

  * Admins


#### Sideloading

See [Users sideloads](/documentation/ticketing/using-the-zendesk-api/side_loading/#supported-endpoints).

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
cursor| string| Query| false| The cursor pointer to work with for all subsequent exports after the initial request
per_page| integer| Query| false| The number of records to return per page
start_time| integer| Query| false| The time to start the incremental export from. Must be at least one minute in the past. Data isn't provided for the most recent minute. Required on the initial export request; not required on subsequent cursor-based pagination requests

#### Limits

This endpoint has its own rate limit that is different from the account wide rate limit. When calls are made to this endpoint, this limit will be consumed and you will get a `429 Too Many Requests` response code if the allocation is exhausted.

##### Headers

API responses include usage limit information in the headers for this endpoint.


    Zendesk-RateLimit-incremental-exports-cursor: total={number}; remaining={number}; resets={number}

Within this header, âTotalâ signifies the initial allocation, âRemainingâ indicates the remaining allowance for the current interval, and âResetsâ denotes the wait time in seconds before the limit refreshes. You can see the Total, and Interval values in the below table.

##### Details

This is the limit definition for the incremental users cursor export action.

Rate Limits| Scopes| Interval| Sandbox| Trial| Default
---|---|---|---|---|---
Standard| Account| 1 minute| N/A| N/A| 20
With High Volume API Add On| Account| 1 minute| N/A| N/A| 60

"Default" applies to all Zendesk suite and support plans. Please refer to the [general account limits](https://developer.zendesk.com/api-reference/introduction/rate-limits) for more information.

#### Code Samples

**curl**

Cursor-based export


    # Cursor-based export, Initial requestcurl https://{subdomain}.zendesk.com/api/v2/incremental/users/cursor?start_time=1332034771 \  -v -u {email_address}/token:{api_token}# Cursor-based export, Subsequent requestscurl https://{subdomain}.zendesk.com/api/v2/incremental/users/cursor?cursor=MTU3NjYxMzUzOS4wfHw0NTF8 \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/incremental/users/cursor?cursor=&per_page=&start_time=1332034771"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/incremental/users/cursor")		.newBuilder()		.addQueryParameter("cursor", "")		.addQueryParameter("per_page", "")		.addQueryParameter("start_time", "1332034771");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/incremental/users/cursor',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'cursor': '',    'per_page': '',    'start_time': '1332034771',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/incremental/users/cursor?cursor=&per_page=&start_time=1332034771"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/incremental/users/cursor")uri.query = URI.encode_www_form("cursor": "", "per_page": "", "start_time": "1332034771")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "after_cursor": "MTU3NjYxMzUzOS4wfHw0Njd8",  "after_url": "https://{subdomain}.zendesk.com/api/v2/incremental/users/cursor?cursor=MTU3NjYxMzUzOS4wfHw0Njd8",  "before_cursor": null,  "before_url": null,  "end_of_stream": true,  "users": [    {      "active": true,      "alias": "Mr. Johnny",      "created_at": "2009-07-20T22:55:29Z",      "custom_role_id": 9373643,      "details": "",      "email": "[[email protected]](/cdn-cgi/l/email-protection)",      "external_id": "sai989sur98w9",      "id": 35436,      "last_login_at": "2011-05-05T10:38:52Z",      "locale": "en-US",      "locale_id": 1,      "moderator": true,      "name": "Johnny Agent",      "notes": "Johnny is a nice guy!",      "only_private_comments": false,      "organization_id": 57542,      "phone": "+15551234567",      "photo": {        "content_type": "image/png",        "content_url": "https://company.zendesk.com/photos/my_funny_profile_pic.png",        "id": 928374,        "name": "my_funny_profile_pic.png",        "size": 166144,        "thumbnails": [          {            "content_type": "image/png",            "content_url": "https://company.zendesk.com/photos/my_funny_profile_pic_thumb.png",            "id": 928375,            "name": "my_funny_profile_pic_thumb.png",            "size": 58298          }        ]      },      "restricted_agent": true,      "role": "agent",      "role_type": 0,      "shared": false,      "shared_agent": false,      "signature": "Have a nice day, Johnny",      "suspended": true,      "tags": [        "enterprise",        "other_tag"      ],      "ticket_restriction": "assigned",      "time_zone": "Copenhagen",      "updated_at": "2011-05-05T10:38:52Z",      "url": "https://company.zendesk.com/api/v2/users/35436",      "user_fields": {        "user_date": "2012-07-23T00:00:00Z",        "user_decimal": 5.1,        "user_dropdown": "option_1"      },      "verified": true    }  ]}

### Incremental User Export, Time Based

  * `GET /api/v2/incremental/users?start_time={start_time}`


#### Allowed For

  * Admins


#### Sideloading

See [Users sideloads](/documentation/ticketing/using-the-zendesk-api/side_loading/#supported-endpoints).

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
per_page| integer| Query| false| The number of records to return per page
start_time| integer| Query| true| The time to start the incremental export from. Must be at least one minute in the past. Data isn't provided for the most recent minute

#### Code Samples

**curl**

Time-based export


    curl https://{subdomain}.zendesk.com/api/v2/incremental/users?start_time=1332034771 \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/incremental/users?per_page=&start_time=1332034771"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/incremental/users")		.newBuilder()		.addQueryParameter("per_page", "")		.addQueryParameter("start_time", "1332034771");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/incremental/users',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'per_page': '',    'start_time': '1332034771',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/incremental/users?per_page=&start_time=1332034771"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/incremental/users")uri.query = URI.encode_www_form("per_page": "", "start_time": "1332034771")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "count": 1,  "end_of_stream": true,  "end_time": 1601357503,  "next_page": "https://example.zendesk.com/api/v2/incremental/ticket_events?start_time=1601357503",  "users": [    {      "active": true,      "alias": "Mr. Johnny",      "created_at": "2009-07-20T22:55:29Z",      "custom_role_id": 9373643,      "details": "",      "email": "[[email protected]](/cdn-cgi/l/email-protection)",      "external_id": "sai989sur98w9",      "id": 35436,      "last_login_at": "2011-05-05T10:38:52Z",      "locale": "en-US",      "locale_id": 1,      "moderator": true,      "name": "Johnny Agent",      "notes": "Johnny is a nice guy!",      "only_private_comments": false,      "organization_id": 57542,      "phone": "+15551234567",      "photo": {        "content_type": "image/png",        "content_url": "https://company.zendesk.com/photos/my_funny_profile_pic.png",        "id": 928374,        "name": "my_funny_profile_pic.png",        "size": 166144,        "thumbnails": [          {            "content_type": "image/png",            "content_url": "https://company.zendesk.com/photos/my_funny_profile_pic_thumb.png",            "id": 928375,            "name": "my_funny_profile_pic_thumb.png",            "size": 58298          }        ]      },      "restricted_agent": true,      "role": "agent",      "role_type": 0,      "shared": false,      "shared_agent": false,      "signature": "Have a nice day, Johnny",      "suspended": true,      "tags": [        "enterprise",        "other_tag"      ],      "ticket_restriction": "assigned",      "time_zone": "Copenhagen",      "updated_at": "2011-05-05T10:38:52Z",      "url": "https://company.zendesk.com/api/v2/users/35436",      "user_fields": {        "user_date": "2012-07-23T00:00:00Z",        "user_decimal": 5.1,        "user_dropdown": "option_1"      },      "verified": true    }  ]}

### Incremental Organization Export

  * `GET /api/v2/incremental/organizations?start_time={start_time}`


#### Allowed For

  * Admins


#### Sideloading

See [Organizations sideloads](/documentation/ticketing/using-the-zendesk-api/side_loading/#supported-endpoints).

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
per_page| integer| Query| false| The number of records to return per page
start_time| integer| Query| true| The time to start the incremental export from. Must be at least one minute in the past. Data isn't provided for the most recent minute

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/incremental/organizations?start_time=1332034771 \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/incremental/organizations?per_page=&start_time=1332034771"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/incremental/organizations")		.newBuilder()		.addQueryParameter("per_page", "")		.addQueryParameter("start_time", "1332034771");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/incremental/organizations',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'per_page': '',    'start_time': '1332034771',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/incremental/organizations?per_page=&start_time=1332034771"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/incremental/organizations")uri.query = URI.encode_www_form("per_page": "", "start_time": "1332034771")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "count": 1,  "end_of_stream": true,  "end_time": 1601357503,  "next_page": "https://example.zendesk.com/api/v2/incremental/ticket_events?start_time=1601357503",  "organizations": [    {      "created_at": "2018-11-14T00:14:52Z",      "details": "caterpillar =)",      "domain_names": [        "remain.com"      ],      "external_id": "ABC198",      "group_id": 1835962,      "id": 4112492,      "name": "Groablet Enterprises",      "notes": "donkey",      "organization_fields": {        "datepudding": "2018-11-04T00:00:00+00:00",        "org_field_1": "happy happy",        "org_field_2": "teapot_kettle"      },      "shared_comments": false,      "shared_tickets": false,      "tags": [        "smiley",        "teapot_kettle"      ],      "updated_at": "2018-11-14T00:54:22Z",      "url": "https://example.zendesk.com/api/v2/organizations/4112492"    }  ]}

### Incremental Sample Export

  * `GET /api/v2/incremental/{incremental_resource}/sample?start_time={start_time}`


Use this endpoint to test the incremental export format. It's more strict in terms of rate limiting, at 10 requests per 20 minutes instead of 10 requests per minute. It also returns only up to 50 results per request. Otherwise, it's identical to the above APIs.

Use the `incremental_resource` parameter to specify the resource. Possible values are "tickets", "ticket_events", "users", or "organizations".

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
start_time| integer| Query| true| The time to start the incremental export from. Must be at least one minute in the past. Data isn't provided for the most recent minute
incremental_resource| string| Path| true| The resource requested for incremental sample export

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/incremental/{incremental_resource}/sample?start_time={unix_time} \ -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/incremental/tickets/sample?start_time=1332034771"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/incremental/tickets/sample")		.newBuilder()		.addQueryParameter("start_time", "1332034771");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/incremental/tickets/sample',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'start_time': '1332034771',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/incremental/tickets/sample?start_time=1332034771"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/incremental/tickets/sample")uri.query = URI.encode_www_form("start_time": "1332034771")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "count": 2,  "end_of_stream": true,  "end_time": 1390362485,  "next_page": "https://{subdomain}.zendesk.com/api/v2/incremental/tickets?per_page=3&start_time=1390362485",  "tickets": [    {      "assignee_id": 235323,      "collaborator_ids": [        35334,        234      ],      "created_at": "2009-07-20T22:55:29Z",      "custom_fields": [        {          "id": 27642,          "value": "745"        },        {          "id": 27648,          "value": "yes"        }      ],      "description": "The fire is very colorful.",      "due_at": null,      "external_id": "ahg35h3jh",      "follower_ids": [        35334,        234      ],      "from_messaging_channel": false,      "generated_timestamp": 1304553600,      "group_id": 98738,      "has_incidents": false,      "id": 35436,      "organization_id": 509974,      "priority": "high",      "problem_id": 9873764,      "raw_subject": "{{dc.printer_on_fire}}",      "recipient": "[[email protected]](/cdn-cgi/l/email-protection)",      "requester_id": 20978392,      "satisfaction_rating": {        "comment": "Great support!",        "id": 1234,        "score": "good"      },      "sharing_agreement_ids": [        84432      ],      "status": "open",      "subject": "Help, my printer is on fire!",      "submitter_id": 76872,      "tags": [        "enterprise",        "other_tag"      ],      "type": "incident",      "updated_at": "2011-05-05T10:38:52Z",      "url": "https://company.zendesk.com/api/v2/tickets/35436",      "via": {        "channel": "web"      }    }  ]}

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)