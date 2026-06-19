# Ticket Metrics

*Source: https://developer.zendesk.com/api-reference/ticketing/tickets/ticket_metrics/*

---

## On this page

  * [JSON format](/api-reference/ticketing/tickets/ticket_metrics/#json-format)
  * [List Ticket Metrics](/api-reference/ticketing/tickets/ticket_metrics/#list-ticket-metrics)
  * [Show Ticket Metrics](/api-reference/ticketing/tickets/ticket_metrics/#show-ticket-metrics)
  * [Show Ticket Metrics By Ticket](/api-reference/ticketing/tickets/ticket_metrics/#show-ticket-metrics-by-ticket)


# Ticket Metrics

## On this page

  * [JSON format](/api-reference/ticketing/tickets/ticket_metrics/#json-format)
  * [List Ticket Metrics](/api-reference/ticketing/tickets/ticket_metrics/#list-ticket-metrics)
  * [Show Ticket Metrics](/api-reference/ticketing/tickets/ticket_metrics/#show-ticket-metrics)
  * [Show Ticket Metrics By Ticket](/api-reference/ticketing/tickets/ticket_metrics/#show-ticket-metrics-by-ticket)


Use this API to get various metrics about one or more tickets in the Zendesk account.

### JSON format

Ticket Metrics are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
agent_wait_time_in_minutes| object| true| false| Number of minutes the agent spent waiting during calendar and business hours
assigned_at| string| true| false| When the ticket was assigned
assignee_stations| integer| true| false| Number of assignees the ticket had
assignee_updated_at| string| true| false| When the assignee last updated the ticket
created_at| string| true| false| When the record was created
custom_status_updated_at| string| true| false| The date and time the ticket's custom status was last updated
first_resolution_time_in_minutes| object| true| false| Number of minutes to the first resolution time during calendar and business hours
full_resolution_time_in_minutes| object| true| false| Number of minutes to the full resolution during calendar and business hours
group_stations| integer| true| false| Number of groups the ticket passed through
id| integer| true| false| Automatically assigned when the client is created
initially_assigned_at| string| true| false| When the ticket was initially assigned
latest_comment_added_at| string| true| false| When the latest comment was added
on_hold_time_in_minutes| object| true| false| Number of minutes on hold
reopens| integer| true| false| Total number of times the ticket was reopened
replies| integer| true| false| The number of public replies added to a ticket by an agent
reply_time_in_minutes| object| true| false| Number of minutes to the first reply during calendar and business hours
reply_time_in_seconds| object| true| false| Number of seconds to the first reply during calendar hours, only available for Messaging tickets
requester_updated_at| string| true| false| When the requester last updated the ticket
requester_wait_time_in_minutes| object| true| false| Number of minutes the requester spent waiting during calendar and business hours
solved_at| string| true| false| When the ticket was solved
status_updated_at| string| true| false| When the status of the ticket was last updated
ticket_id| integer| true| false| Id of the associated ticket
updated_at| string| true| false| When the record was last updated
url| string| true| false| The API url of the ticket metric

#### Example


    {  "agent_wait_time_in_minutes": {    "business": 737,    "calendar": 2391  },  "assigned_at": "2011-05-05T10:38:52Z",  "assignee_stations": 1,  "assignee_updated_at": "2011-05-06T10:38:52Z",  "created_at": "2009-07-20T22:55:29Z",  "custom_status_updated_at": "2011-05-09T10:38:52Z",  "first_resolution_time_in_minutes": {    "business": 737,    "calendar": 2391  },  "full_resolution_time_in_minutes": {    "business": 737,    "calendar": 2391  },  "group_stations": 7,  "id": 33,  "initially_assigned_at": "2011-05-03T10:38:52Z",  "latest_comment_added_at": "2011-05-09T10:38:52Z",  "on_hold_time_in_minutes": {    "business": 637,    "calendar": 2290  },  "reopens": 55,  "replies": 322,  "reply_time_in_minutes": {    "business": 737,    "calendar": 2391  },  "reply_time_in_seconds": {    "calendar": 143460  },  "requester_updated_at": "2011-05-07T10:38:52Z",  "requester_wait_time_in_minutes": {    "business": 737,    "calendar": 2391  },  "solved_at": "2011-05-09T10:38:52Z",  "status_updated_at": "2011-05-04T10:38:52Z",  "ticket_id": 4343,  "updated_at": "2011-05-05T10:38:52Z"}

### List Ticket Metrics

  * `GET /api/v2/ticket_metrics`


Returns a list of tickets with their metrics.

Tickets are ordered chronologically by created date, from newest to oldest. The last ticket listed may not be the absolute oldest ticket in your account due to ticket archiving.

Archived tickets are not included in the response. See [About archived tickets](https://support.zendesk.com/hc/en-us/articles/203657756) in Zendesk help.

#### Pagination

  * Cursor pagination (recommended)
  * Offset pagination


See [Pagination](/api-reference/introduction/pagination/).

Returns a maximum of 100 records per page.

#### Allowed For

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
page| object| Query| false| Cursor-based pagination parameters (JSON:API style). Supports nested parameters: - `page[size]` \- Number of records per page (default varies by endpoint, typically 100) - `page[after]` \- Cursor token to fetch records after this position - `page[before]` \- Cursor token to fetch records before this position Example: `?page[size]=50&page[after]=eyJvIjoiaWQiLCJ2IjoiYVFFPSJ9`
sort| string| Query| false| Field to sort results by. Prefix with `-` for descending order. When used with cursor pagination, this determines the cursor ordering. Example: `?sort=name` or `?sort=-created_at`

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/ticket_metrics \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/ticket_metrics?page=&sort=name"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/ticket_metrics")		.newBuilder()		.addQueryParameter("page", "")		.addQueryParameter("sort", "name");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/ticket_metrics',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'page': '',    'sort': 'name',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/ticket_metrics?page=&sort=name"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/ticket_metrics")uri.query = URI.encode_www_form("page": "", "sort": "name")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "ticket_metrics": [    {      "agent_wait_time_in_minutes": {        "business": 0,        "calendar": 0      },      "assigned_at": "2020-07-20T06:21:26Z",      "assignee_stations": 0,      "assignee_updated_at": "2020-07-20T06:21:26Z",      "created_at": "2020-07-21T01:01:42Z",      "first_resolution_time_in_minutes": {        "business": 0,        "calendar": 0      },      "full_resolution_time_in_minutes": {        "business": 0,        "calendar": 0      },      "group_stations": 0,      "id": 33,      "initially_assigned_at": "2020-07-20T06:21:26Z",      "latest_comment_added_at": "2020-07-21T01:17:16Z",      "on_hold_time_in_minutes": {        "business": 0,        "calendar": 0      },      "reopens": 0,      "replies": 1,      "reply_time_in_minutes": {        "business": 16,        "calendar": 16      },      "reply_time_in_seconds": {        "calendar": 960      },      "requester_updated_at": "2020-07-21T01:17:16Z",      "requester_wait_time_in_minutes": {        "business": 0,        "calendar": 0      },      "solved_at": "2020-07-20T06:21:26Z",      "status_updated_at": "2020-07-21T01:01:41Z",      "ticket_id": 1517,      "updated_at": "2020-07-21T01:17:16Z",      "url": "https://example.zendesk.com/api/v2/ticket_metrics/33"    },    {      "agent_wait_time_in_minutes": {        "business": 0,        "calendar": 0      },      "assigned_at": "2020-07-20T06:21:26Z",      "assignee_stations": 0,      "assignee_updated_at": "2020-07-20T06:21:26Z",      "created_at": "2020-07-20T06:21:27Z",      "first_resolution_time_in_minutes": {        "business": 0,        "calendar": 0      },      "full_resolution_time_in_minutes": {        "business": 0,        "calendar": 0      },      "group_stations": 0,      "id": 34,      "initially_assigned_at": "2020-07-20T06:21:26Z",      "latest_comment_added_at": "2020-07-20T06:21:26Z",      "on_hold_time_in_minutes": {        "business": 0,        "calendar": 0      },      "reopens": 0,      "replies": 0,      "reply_time_in_minutes": {        "business": 0,        "calendar": 0      },      "reply_time_in_seconds": {        "calendar": 0      },      "requester_updated_at": "2020-07-20T06:21:26Z",      "requester_wait_time_in_minutes": {        "business": 0,        "calendar": 0      },      "solved_at": "2020-07-20T06:21:26Z",      "status_updated_at": "2020-07-20T06:21:26Z",      "ticket_id": 1511,      "updated_at": "2020-07-20T06:21:27Z",      "url": "https://example.zendesk.com/api/v2/ticket_metrics/34"    }  ]}

### Show Ticket Metrics

  * `GET /api/v2/ticket_metrics/{ticket_metric_id}`


Returns a specific metric, or the metrics of a specific ticket.

#### Pagination

  * Cursor pagination (recommended)
  * Offset pagination


See [Pagination](/api-reference/introduction/pagination/).

Returns a maximum of 100 records per page.

#### Allowed For

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
ticket_metric_id| string| Path| true| The id of the ticket metric to retrieve

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/ticket_metrics/{ticket_metric_id} \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/ticket_metrics/10001"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/ticket_metrics/10001")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/ticket_metrics/10001',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/ticket_metrics/10001"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/ticket_metrics/10001")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "ticket_metric": [    {      "agent_wait_time_in_minutes": {        "business": 0,        "calendar": 0      },      "assigned_at": "2020-07-20T06:21:26Z",      "assignee_stations": 0,      "assignee_updated_at": "2020-07-20T06:21:26Z",      "created_at": "2020-07-21T01:01:42Z",      "first_resolution_time_in_minutes": {        "business": 0,        "calendar": 0      },      "full_resolution_time_in_minutes": {        "business": 0,        "calendar": 0      },      "group_stations": 0,      "id": 33,      "initially_assigned_at": "2020-07-20T06:21:26Z",      "latest_comment_added_at": "2020-07-21T01:17:16Z",      "on_hold_time_in_minutes": {        "business": 0,        "calendar": 0      },      "reopens": 0,      "replies": 1,      "reply_time_in_minutes": {        "business": 16,        "calendar": 16      },      "reply_time_in_seconds": {        "calendar": 960      },      "requester_updated_at": "2020-07-21T01:17:16Z",      "requester_wait_time_in_minutes": {        "business": 0,        "calendar": 0      },      "solved_at": "2020-07-20T06:21:26Z",      "status_updated_at": "2020-07-21T01:01:41Z",      "ticket_id": 1517,      "updated_at": "2020-07-21T01:17:16Z",      "url": "https://example.zendesk.com/api/v2/ticket_metrics/33"    }  ]}

### Show Ticket Metrics By Ticket

  * `GET /api/v2/tickets/{ticket_id}/metrics`


Returns the metrics for a specific ticket.

#### Allowed For

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
ticket_id| integer| Path| true| The ID of the ticket

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/tickets/{ticket_id}/metrics \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/tickets/123456/metrics"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/tickets/123456/metrics")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/tickets/123456/metrics',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/tickets/123456/metrics"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/tickets/123456/metrics")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "ticket_metric": [    {      "agent_wait_time_in_minutes": {        "business": 0,        "calendar": 0      },      "assigned_at": "2020-07-20T06:21:26Z",      "assignee_stations": 0,      "assignee_updated_at": "2020-07-20T06:21:26Z",      "created_at": "2020-07-21T01:01:42Z",      "first_resolution_time_in_minutes": {        "business": 0,        "calendar": 0      },      "full_resolution_time_in_minutes": {        "business": 0,        "calendar": 0      },      "group_stations": 0,      "id": 33,      "initially_assigned_at": "2020-07-20T06:21:26Z",      "latest_comment_added_at": "2020-07-21T01:17:16Z",      "on_hold_time_in_minutes": {        "business": 0,        "calendar": 0      },      "reopens": 0,      "replies": 1,      "reply_time_in_minutes": {        "business": 16,        "calendar": 16      },      "reply_time_in_seconds": {        "calendar": 960      },      "requester_updated_at": "2020-07-21T01:17:16Z",      "requester_wait_time_in_minutes": {        "business": 0,        "calendar": 0      },      "solved_at": "2020-07-20T06:21:26Z",      "status_updated_at": "2020-07-21T01:01:41Z",      "ticket_id": 1517,      "updated_at": "2020-07-21T01:17:16Z",      "url": "https://example.zendesk.com/api/v2/ticket_metrics/33"    }  ]}

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)