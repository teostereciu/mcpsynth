# Access Logs

*Source: https://developer.zendesk.com/api-reference/ticketing/account-configuration/access_logs/*

---

## On this page

  * [JSON format](/api-reference/ticketing/account-configuration/access_logs/#json-format)
  * [List Access Logs](/api-reference/ticketing/account-configuration/access_logs/#list-access-logs)


# Access Logs

## On this page

  * [JSON format](/api-reference/ticketing/account-configuration/access_logs/#json-format)
  * [List Access Logs](/api-reference/ticketing/account-configuration/access_logs/#list-access-logs)


The access log is a 90-day record of events that captures what an agent or admin has accessed in your account without necessarily updating, creating, or deleting anything. The access log is your record of read and write events for your account.

The [Advanced Data Privacy and Protection (ADPP)](https://support.zendesk.com/hc/en-us/articles/6119316155930) add-on is required to use this API.

The Access Logs API can return two kinds of identifiers for the resources accessed: a REST API path or a GraphQL query. The log also provides additional information, including:

  * timestamp
  * query parameters
  * the HTTP method used, such as GET or POST
  * the user id of the user who made the request
  * the IP address of the user who made the request
  * the authorization type (currently not supported for GraphQL requests)
  * the client. A characteristic string that lets servers and network peers identify the application, operating system, vendor, and version of the requesting [user agent](https://developer.mozilla.org/en-US/docs/Glossary/User_agent)
  * the browser URL (referer) from which the request originated
  * the size of the response body in bytes
  * a resource category and summary that provide human-readable descriptions of the access log entry


You can filter the access logs based on when the event happened, or based on objects or users within a specified time frame. The examples below show all filters, but that's not required. You can specify as many filters as needed.

**Filtering by objects**

`filter[start]`: UTC time stamp in the format of yyyy-mm-ddThh:mm:ssZ
`filter[end]`: UTC time stamp in the format of yyyy-mm-ddThh:mm:ssZ
`filter[path]`: URL path of the object, excluding query parameters

Example:


    https://subdomain.zendesk.com/api/v2/access_logs?filter[start]=2022-08-01T15:04:05Z&filter[end]=2022-08-02T20:04:05Z&filter[path]=/api/v2/ticket_fields

**Filtering by users**

`filter[start]`: UTC time stamp in the format of yyyy-mm-ddThh:mm:ssZ
`filter[end]`: UTC time stamp in the format of yyyy-mm-ddThh:mm:ssZ
`filter[user_id]`: User id

Example:


    https://subdomain.zendesk.com/api/v2/access_logs?filter[start]=2022-08-01T15:04:05Z&filter[end]=2022-08-01T20:04:05Z&filter[user_id]=12345678

**Filtering by time stamps**

`filter[start]`: UTC time stamp in the format of yyyy-mm-ddThh:mm:ssZ
`filter[end]`: UTC time stamp in the format of yyyy-mm-ddThh:mm:ssZ

Example:


    https://subdomain.zendesk.com/api/v2/access_logs?filter[start]=2022-08-01T15:04:05Z&filter[end]=2022-08-01T20:04:05Z

**Filtering by browser URL**

`filter[start]`: UTC time stamp in the format of yyyy-mm-ddThh:mm:ssZ
`filter[end]`: UTC time stamp in the format of yyyy-mm-ddThh:mm:ssZ
`filter[browser_url]`: The browser URL (referer) from which the request originated

Example:


    https://subdomain.zendesk.com/api/v2/access_logs?filter[start]=2022-08-01T15:04:05Z&filter[end]=2022-08-02T20:04:05Z&filter[browser_url]=/agent/tickets/123

**Filtering out GraphQL logs**

`filter[start]`: UTC time stamp in the format of yyyy-mm-ddThh:mm:ssZ
`filter[end]`: UTC time stamp in the format of yyyy-mm-ddThh:mm:ssZ
`filter[graphql]`: If set to `true`, excludes GraphQL access logs from the response. GraphQL logs track internal Zendesk component interactions.

Example:


    https://subdomain.zendesk.com/api/v2/access_logs?filter[start]=2022-08-01T15:04:05Z&filter[end]=2022-08-02T20:04:05Z&filter[graphql]=true

### JSON format

Access Logs are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
authorization_type| string| true| true| The method used for user authorization. Example: "basic", "session", "digest", "bearer"
bytes_sent| integer| true| false| The size of the response body in bytes
category| string| true| false| A translated category for the access log entry that identifies the type of resource accessed. Examples: "Users", "Tickets"
client| string| true| true| The user agent. Example: a web browser
graphql| object| true| false| Optional details if the request was a GraphQL query
id| string| true| true| Unique identifier for the access log
ip_address| string| true| true| IP address of the user who made the request
method| string| true| true| HTTP method of the request. Possible values: "GET", "POST", "PUT", "DELETE"
referer| string| true| false| The browser URL (referer) from which the request originated
status| number| true| true| HTTP status code of the response
summary| string| true| false| A translated summary description of the access log entry that provides a human-readable explanation of the action performed. Examples: "List users", "View ticket"
timestamp| string| true| true| ISO 8601 formatted string representing the time of the request
url| string| true| true| URL of the request
user_id| number| true| true| ID of the user who made the request

### List Access Logs

  * `GET /api/v2/access_logs`


Returns a list of access logs for the given query parameters.

#### Allowed For

  * Admins


#### Pagination

  * Cursor pagination


#### Rate Limits

Requests are rate limited to 50 requests per minute.

The API doesn't follow the same rate limiting conventions as other Zendesk APIs. Responses don't include `x-rate-limits` and `x-rate-limit-remaining` headers. The API does return a 429 status code when the limit is reached but doesn't include a `retry-after` header. Instead it returns a `ratelimit-reset` header that specifies a date-time.

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
filter[after]| string| Query| false| Cursor value received as part of the previous request. Used to get next set of results
filter[before]| string| Query| false| Cursor value received as part of the previous request. Used to get the previous set of results
filter[browser_url]| string| Query| false| Filter access logs by the browser URL (referer) from which the request originated
filter[end]| string| Query| false| Only return logs created before this timestamp
filter[graphql]| string| Query| false| If true, filters out GraphQL access logs from the response. GraphQL logs track internal Zendesk component interactions. Allowed value of "true".
filter[path]| string| Query| false| Specific url path excluding query params to filter by
filter[start]| string| Query| false| Only return logs created after this timestamp
filter[user_id]| number| Query| false| Specific user id to filter by
page[size]| number| Query| false| Maximum number of results to return. Default value is 1000 and the maximum allowed value is 2500
sort| string| Query| false| Sort access logs. By default, the logs are sorted in ascending order. To switch to descending order, use `sort=-created_at`.

#### Code Samples

**Curl**


    curl --request GET https://example.zendesk.com/api/v2/access_logs?filter[after]=01H6PWD1WQFC6EYJCJWFJ59EVE&filter[before]=01H6PWD1WQFC6EYJCJWFJ59EVE&filter[browser_url]=%2Fagent%2Ftickets%2F123&filter[end]=2022-03-21T00%3A00%3A00Z&filter[graphql]=true&filter[path]=%2Fapi%2Fv2%2Fusers%2Fsearch&filter[start]=2022-03-20T00%3A00%3A00Z&filter[user_id]=1234567890&page[size]=100&sort=-created_at \--header "Content-Type: application/json" \-u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/access_logs?filter[after]=01H6PWD1WQFC6EYJCJWFJ59EVE&filter[before]=01H6PWD1WQFC6EYJCJWFJ59EVE&filter[browser_url]=%2Fagent%2Ftickets%2F123&filter[end]=2022-03-21T00%3A00%3A00Z&filter[graphql]=true&filter[path]=%2Fapi%2Fv2%2Fusers%2Fsearch&filter[start]=2022-03-20T00%3A00%3A00Z&filter[user_id]=1234567890&page[size]=100&sort=-created_at"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/access_logs")		.newBuilder()		.addQueryParameter("filter[after]", "01H6PWD1WQFC6EYJCJWFJ59EVE")		.addQueryParameter("filter[before]", "01H6PWD1WQFC6EYJCJWFJ59EVE")		.addQueryParameter("filter[browser_url]", "/agent/tickets/123")		.addQueryParameter("filter[end]", "2022-03-21T00:00:00Z")		.addQueryParameter("filter[graphql]", "true")		.addQueryParameter("filter[path]", "/api/v2/users/search")		.addQueryParameter("filter[start]", "2022-03-20T00:00:00Z")		.addQueryParameter("filter[user_id]", "1234567890")		.addQueryParameter("page[size]", "100")		.addQueryParameter("sort", "-created_at");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/access_logs',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'filter[after]': '01H6PWD1WQFC6EYJCJWFJ59EVE',    'filter[before]': '01H6PWD1WQFC6EYJCJWFJ59EVE',    'filter[browser_url]': '%2Fagent%2Ftickets%2F123',    'filter[end]': '2022-03-21T00%3A00%3A00Z',    'filter[graphql]': 'true',    'filter[path]': '%2Fapi%2Fv2%2Fusers%2Fsearch',    'filter[start]': '2022-03-20T00%3A00%3A00Z',    'filter[user_id]': '1234567890',    'page[size]': '100',    'sort': '-created_at',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/access_logs?filter[after]=01H6PWD1WQFC6EYJCJWFJ59EVE&filter[before]=01H6PWD1WQFC6EYJCJWFJ59EVE&filter[browser_url]=%2Fagent%2Ftickets%2F123&filter[end]=2022-03-21T00%3A00%3A00Z&filter[graphql]=true&filter[path]=%2Fapi%2Fv2%2Fusers%2Fsearch&filter[start]=2022-03-20T00%3A00%3A00Z&filter[user_id]=1234567890&page[size]=100&sort=-created_at"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/access_logs")uri.query = URI.encode_www_form("filter[after]": "01H6PWD1WQFC6EYJCJWFJ59EVE", "filter[before]": "01H6PWD1WQFC6EYJCJWFJ59EVE", "filter[browser_url]": "/agent/tickets/123", "filter[end]": "2022-03-21T00:00:00Z", "filter[graphql]": "true", "filter[path]": "/api/v2/users/search", "filter[start]": "2022-03-20T00:00:00Z", "filter[user_id]": "1234567890", "page[size]": "100", "sort": "-created_at")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "access_logs": [    {      "authorization_type": "basic",      "bytes_sent": 1234,      "category": "Search",      "client": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",      "id": "01H6PWD1WQFC6EYJCJWFJ59EVE",      "ip_address": "127.0.0.1",      "method": "POST",      "referer": "/agent/dashboard",      "status": 200,      "summary": "Search tickets",      "timestamp": "2020-01-01T13:01:26Z",      "url": "/api/v2/search?query=foobar",      "user_id": 123    },    {      "authorization_type": "basic",      "bytes_sent": 5678,      "category": "Ticket",      "client": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",      "graphql": {        "operation_name": "ticket",        "operation_type": "QUERY",        "query": "query ticket($id: ID!, $includeSkills: Boolean = false, $includeCustomFields: Boolean = false, $includeUserCustomFields: Boolean = false, $includeConversationAuthenticated: Boolean = false) { ticket(id: $id) { id assignee { user { id name __typename }...",        "variables": "{\"id\":\"1\"}"      },      "id": "01H9KB1CDRX2RVDS7E2R4YJ0TS",      "ip_address": "127.0.0.1",      "method": "POST",      "referer": "/agent/tickets/123",      "status": 200,      "summary": "View ticket",      "timestamp": "2023-09-05T18:52:50Z",      "url": "/graphql",      "user_id": 321    }  ],  "links": {    "next": "https://<subdomain>.zendesk.com/api/v2/access_logs?filter[start]=2020-01-01T00:00:00Z&filter[end]=2020-01-02T00:00:00Z&filter[user_id]=123&page[size]=100&page[after]=xxx",    "prev": "https://<subdomain>.zendesk.com/api/v2/access_logs?filter[start]=2020-01-01T00:00:00Z&filter[end]=2020-01-02T00:00:00Z&filter[user_id]=123&page[size]=100&page[before]=xxx"  },  "meta": {    "after_cursor": "xxxxxxxxx",    "before_cursor": "xxxxxxxxx",    "has_before": true,    "has_more": true  }}

**400 Bad Request**


    // Status 400 Bad Request
    {  "errors": [    {      "detail": "max allowed page size is 2500",      "title": "Malformed query params"    }  ]}

**401 Unauthorized**


    // Status 401 Unauthorized
    {  "errors": [    {      "detail": "Please use valid credentials",      "title": "Authentication failed"    }  ]}

**403 Forbidden**


    // Status 403 Forbidden
    {  "errors": [    {      "detail": "You must have administrator privileges",      "title": "Authorization failed"    }  ]}

**429 Too Many Requests**


    // Status 429 Too Many Requests
    {  "errors": [    {      "detail": "Use RateLimit-Reset header to backoff on retries",      "title": "Too many requests"    }  ]}

**500 Internal Server Error**


    // Status 500 Internal Server Error
    {  "errors": [    {      "detail": "Failed to process request",      "title": "Internal Service Error"    }  ]}

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)