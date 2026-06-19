# Search

*Source: https://developer.zendesk.com/api-reference/ticketing/ticket-management/search/*

---

## On this page

  * [Results limit](/api-reference/ticketing/ticket-management/search/#results-limit)
  * [Query syntax](/api-reference/ticketing/ticket-management/search/#query-syntax)
  * [JSON format](/api-reference/ticketing/ticket-management/search/#json-format)
  * [List Search Results](/api-reference/ticketing/ticket-management/search/#list-search-results)
  * [Show Results Count](/api-reference/ticketing/ticket-management/search/#show-results-count)
  * [Export Search Results](/api-reference/ticketing/ticket-management/search/#export-search-results)


# Search

## On this page

  * [Results limit](/api-reference/ticketing/ticket-management/search/#results-limit)
  * [Query syntax](/api-reference/ticketing/ticket-management/search/#query-syntax)
  * [JSON format](/api-reference/ticketing/ticket-management/search/#json-format)
  * [List Search Results](/api-reference/ticketing/ticket-management/search/#list-search-results)
  * [Show Results Count](/api-reference/ticketing/ticket-management/search/#show-results-count)
  * [Export Search Results](/api-reference/ticketing/ticket-management/search/#export-search-results)


The Search API is a unified search API that returns tickets, users, and organizations. You can define filters to narrow your search results according to resource type, dates, and object properties, such as ticket requester or tag.

To search articles in Help Center, see [Search](/api-reference/help_center/help-center-api/search/) in the Help Center API documentation.

To use the API with Python or Node.js, see [Searching with the Zendesk API](/documentation/ticketing/using-the-zendesk-api/searching-with-the-zendesk-api).

**Note** : It can take up to a few minutes for new tickets, users, and other resources to be indexed for search. If new resources don't appear in your search results, wait a few minutes and try again.

### Results limit

The Search API returns up to 1,000 results per query, with a maximum of 100 results per page. See [Pagination](/api-reference/introduction/pagination/). If you request a page past the limit (`page=11` at 100 results per page), a 422 Insufficient Resource Error is returned.

If you need to retrieve large datasets, Zendesk recommends breaking up the search into smaller chunks by limiting results to a specific date range. You can also use the [Export Search Results](/api-reference/ticketing/ticket-management/search/#export-search-results) endpoint.

Alternatively, if you only want incremental changes based on the most recent change, consider using one of the [Incremental Export](/api-reference/ticketing/ticket-management/incremental_exports/) endpoints.

The `count` property shows the actual number of results. For example, if a query has 5,000 results, the `count` value will be 5,000, even if the API only returns the first 1,000 results.

### Query syntax

The search endpoint has a `query` parameter:

`.../api/v2/search?query={search_string}`

The `query` parameter value supports a syntax that lets you specify resource types and criteria. For example, you can search for "users named Jane Doe" or "tickets with an open status".

For more information about the query syntax and examples, see [Searching with the Zendesk API](/documentation/ticketing/using-the-zendesk-api/searching-with-the-zendesk-api).

#### Side-loading

The Search API supports side-loading, which lets you retrieve related records as part of a single request. To make the request, add an `include` parameter specifying the associations you want to load.

For example, the following request searches for records that contain "help" and specifies the type `tickets` to sideload the ticket's user data.


    /api/v2/search?query=help&include=tickets(users)

For more information, see [Side-Loading](/documentation/ticketing/using-the-zendesk-api/side_loading/).

### JSON format

Search are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
count| integer| true| false| The number of resources returned by the query corresponding to this page of results in the paginated response
facets| string| true| false| The facets corresponding to the search query
next_page| string| true| false| URL to the next page of results
previous_page| string| true| false| URL to the previous page of results
results| array| true| false| May consist of tickets, users, groups, or organizations, as specified by the `result_type` property in each result object

#### Example


    {  "count": 1,  "facets": null,  "next_page": null,  "previous_page": null,  "results": [    {      "created_at": "2018-04-06T03:17:05Z",      "default": false,      "deleted": false,      "description": "",      "id": 1835972,      "name": "Ragtail",      "result_type": "group",      "updated_at": "2018-04-06T03:17:05Z",      "url": "https://example.zendesk.com/api/v2/groups/1835972"    }  ]}

### List Search Results

  * `GET /api/v2/search?query={query}`


Returns the search results. See Query syntax for details on the `query` parameter.

Use the ampersand character (&) to append the `sort_by` or `sort_order` parameters to the URL.

For examples, see [Searching with Zendesk API](/documentation/ticketing/using-the-zendesk-api/searching-with-the-zendesk-api).

This endpoint has its own rate limit. The rate limit counts towards the global API rate limit. See Limits.

#### Allowed For

  * Agents


#### Pagination

  * Offset pagination only


Offset pagination may result in duplicate results when paging. You can also use the [Export Search Results](/api-reference/ticketing/ticket-management/search/#export-search-results) endpoint, which uses cursor-based pagination and doesn't return duplicate results. See [Using cursor pagination](/api-reference/introduction/pagination/#using-cursor-pagination) for more information.

#### Errors JSON Format

Errors are represented as JSON objects which have the following keys:

Name| Type| Comment
---|---|---
error| string| The type of error. Examples: "unavailable", "invalid"
description| string|

##### Example Error


    {  "error": "unavailable",  "description": "Sorry, we could not complete your search query. Please try again in a moment."}

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
include| string| Query| false| Sideloads to include in the response. Accepts a comma-separated list of values. The available sideloads depend on the search result types.
query| string| Query| true| The search query. See Query basics above. For details on the query syntax, see the [Zendesk Support search reference](https://support.zendesk.com/hc/en-us/articles/203663226)
sort_by| string| Query| false| One of `updated_at`, `created_at`, `priority`, `status`, or `ticket_type`. Defaults to sorting by relevance
sort_order| string| Query| false| One of `asc` or `desc`. Defaults to `desc`

#### Limits

This endpoint has its own rate limit that is different from the account wide rate limit. When calls are made to this endpoint, this limit will be consumed and you will get a `429 Too Many Requests` response code if the allocation is exhausted.

##### Headers

API responses include usage limit information in the headers for this endpoint.


    Zendesk-RateLimit-search-index: total={number}; remaining={number}; resets={number}

Within this header, âTotalâ signifies the initial allocation, âRemainingâ indicates the remaining allowance for the current interval, and âResetsâ denotes the wait time in seconds before the limit refreshes. You can see the Total, and Interval values in the below table.

##### Details

Rate limit definition for the search index API.

Rate Limits| Scopes| Interval| Sandbox| Trial| Default
---|---|---|---|---|---
Standard| Account| 1 minute| N/A| N/A| 2500
With High Volume API Add On| Account| 1 minute| N/A| N/A| 2500

"Default" applies to all Zendesk suite and support plans. Please refer to the [general account limits](https://developer.zendesk.com/api-reference/introduction/rate-limits) for more information.

#### Code Samples

**curl**


    curl "https://{subdomain}.zendesk.com/api/v2/search" \  -G --data-urlencode "query=type:ticket status:open" \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/search?include=users%2Corganizations&query=https%3A%2F%2Fsubdomain.zendesk.com%2Fapi%2Fv2%2Fsearch%3Fquery%3Dtype%3Aticket+status%3Aclosed%26sort_by%3Dstatus%26sort_order%3Ddesc&sort_by=&sort_order="	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/search")		.newBuilder()		.addQueryParameter("include", "users,organizations")		.addQueryParameter("query", "https://subdomain.zendesk.com/api/v2/search?query=type:ticket status:closed&sort_by=status&sort_order=desc")		.addQueryParameter("sort_by", "")		.addQueryParameter("sort_order", "");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/search',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'include': 'users%2Corganizations',    'query': 'https%3A%2F%2Fsubdomain.zendesk.com%2Fapi%2Fv2%2Fsearch%3Fquery%3Dtype%3Aticket+status%3Aclosed%26sort_by%3Dstatus%26sort_order%3Ddesc',    'sort_by': '',    'sort_order': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/search?include=users%2Corganizations&query=https%3A%2F%2Fsubdomain.zendesk.com%2Fapi%2Fv2%2Fsearch%3Fquery%3Dtype%3Aticket+status%3Aclosed%26sort_by%3Dstatus%26sort_order%3Ddesc&sort_by=&sort_order="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/search")uri.query = URI.encode_www_form("include": "users,organizations", "query": "https://subdomain.zendesk.com/api/v2/search?query=type:ticket status:closed&sort_by=status&sort_order=desc", "sort_by": "", "sort_order": "")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "count": 1234,  "facets": null,  "next_page": "https://foo.zendesk.com/api/v2/search?query=\"type:Group hello\"&sort_by=created_at&sort_order=desc&page=2",  "previous_page": null,  "results": [    {      "created_at": "2009-05-13T00:07:08Z",      "id": 211,      "name": "Hello DJs",      "result_type": "group",      "updated_at": "2011-07-22T00:11:12Z",      "url": "https://foo.zendesk.com/api/v2/groups/211"    },    {      "created_at": "2009-08-26T00:07:08Z",      "id": 122,      "name": "Hello MCs",      "result_type": "group",      "updated_at": "2010-05-13T00:07:08Z",      "url": "https://foo.zendesk.com/api/v2/groups/122"    }  ]}

### Show Results Count

  * `GET /api/v2/search/count?query={query}`


Returns the number of items matching the query rather than the items. The search string works the same as a regular search.

#### Allowed For

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
query| string| Query| true| The search query

#### Code Samples

**curl**


    curl "https://{subdomain}.zendesk.com/api/v2/search/count" \  -G --data-urlencode "query=type:ticket status:open" \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/search/count?query=https%3A%2F%2Fsubdomain.zendesk.com%2Fapi%2Fv2%2Fsearch%3Fquery%3Dtype%3Aticket+status%3Aclosed"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/search/count")		.newBuilder()		.addQueryParameter("query", "https://subdomain.zendesk.com/api/v2/search?query=type:ticket status:closed");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/search/count',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'query': 'https%3A%2F%2Fsubdomain.zendesk.com%2Fapi%2Fv2%2Fsearch%3Fquery%3Dtype%3Aticket+status%3Aclosed',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/search/count?query=https%3A%2F%2Fsubdomain.zendesk.com%2Fapi%2Fv2%2Fsearch%3Fquery%3Dtype%3Aticket+status%3Aclosed"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/search/count")uri.query = URI.encode_www_form("query": "https://subdomain.zendesk.com/api/v2/search?query=type:ticket status:closed")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "count": 6}

### Export Search Results

  * `GET /api/v2/search/export?query={query}`


Exports a set of results. See Query syntax for the syntax of the `query` parameter.

Use this endpoint for search queries that will return more than 1000 results. The result set is ordered only by the `created_at` attribute.

The search only returns results of a single object type. The following object types are supported: ticket, organization, user, or group.

You must specify the type in the `filter[type]` parameter. Searches with type in the query string will result in an error.

#### Allowed For

  * Agents


#### Pagination

  * Cursor pagination


See [Pagination](/api-reference/introduction/pagination/).

Returns a maximum of 1000 records per page. The number of results shown in a page is determined by the `page[size]` parameter.

**Note** : You may experience a speed reduction or a timeout if you request 1000 results per page and you have many archived tickets in the results. Try reducing the number of results per page. We recommend 100 results per page.

The cursor specified by the `after_cursor` property in a response expires after one hour.

For more information on cursor-based pagination, see the following articles:

  * [Comparing cursor pagination and offset pagination](/documentation/developer-tools/pagination/comparing-cursor-pagination-and-offset-pagination)
  * [Paginating through lists using cursor pagination](/documentation/developer-tools/pagination/paginating-through-lists-using-cursor-pagination)


#### Export Search Results Limits

This API endpoint is rate-limited to 100 requests per minute per account. The limit also counts towards the global API rate limit.

#### Response Format

Name| Type| Comment
---|---|---
links[next]| string| URL to the next page of results
meta[has_more]| string| Boolean indicating if there are more results
meta[after_cursor]| string| Cursor object returned from the Search Service
results| array| May consist of tickets, users, groups, or organizations, as specified by the `filter_type` parameter

The response is similar to the response of `GET /api/v2/search?`, with a few changes:

  * `links` \- Has the following nested properties: `prev` and `next`. These replace the `next_page` and `prev_page` links. The `prev` property is always null because backward pagination is not supported. The `next` property may include an auto-generated link to the next page of results.
  * `meta` \- Has the following nested properties: `has_more` and `after_cursor`. The `has_more` property indicates whether the next page has more results. The `after_cursor` property is the cursor used to paginate to the next page. It expires after one hour.


There's no `count` property.

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
filter[type]| string| Query| false| The object type returned by the export query. Can be `ticket`, `organization`, `user`, or `group`.
include| string| Query| false| Sideloads to include in the response. Accepts a comma-separated list of values. The available sideloads depend on the search result types.
page[after]| string| Query| false| The cursor token for fetching the next page of results.
page[size]| integer| Query| false| The number of results shown in a page.
query| string| Query| true| The search query. See Query basics above. For details on the query syntax, see the [Zendesk Support search reference](https://support.zendesk.com/hc/en-us/articles/203663226)

#### Code Samples

**curl**


    curl "https://{subdomain}.zendesk.com/api/v2/search/export" -G \      --data-urlencode 'query=hello' \      --data-urlencode 'page[size]=100' \      --data-urlencode 'filter[type]=ticket' \      -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/search/export?filter[type]=&include=users%2Corganizations&page[after]=&page[size]=&query=https%3A%2F%2Fsubdomain.zendesk.com%2Fapi%2Fv2%2Fsearch%3Fquery%3Dtype%3Aticket+status%3Aclosed%26sort_by%3Dstatus%26sort_order%3Ddesc"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/search/export")		.newBuilder()		.addQueryParameter("filter[type]", "")		.addQueryParameter("include", "users,organizations")		.addQueryParameter("page[after]", "")		.addQueryParameter("page[size]", "")		.addQueryParameter("query", "https://subdomain.zendesk.com/api/v2/search?query=type:ticket status:closed&sort_by=status&sort_order=desc");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/search/export',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'filter[type]': '',    'include': 'users%2Corganizations',    'page[after]': '',    'page[size]': '',    'query': 'https%3A%2F%2Fsubdomain.zendesk.com%2Fapi%2Fv2%2Fsearch%3Fquery%3Dtype%3Aticket+status%3Aclosed%26sort_by%3Dstatus%26sort_order%3Ddesc',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/search/export?filter[type]=&include=users%2Corganizations&page[after]=&page[size]=&query=https%3A%2F%2Fsubdomain.zendesk.com%2Fapi%2Fv2%2Fsearch%3Fquery%3Dtype%3Aticket+status%3Aclosed%26sort_by%3Dstatus%26sort_order%3Ddesc"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/search/export")uri.query = URI.encode_www_form("filter[type]": "", "include": "users,organizations", "page[after]": "", "page[size]": "", "query": "https://subdomain.zendesk.com/api/v2/search?query=type:ticket status:closed&sort_by=status&sort_order=desc")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "facets": null,  "links": {    "next": "https://example.zendesk.com/api/v2/search/export?filter%5Btype%5D=ticket&page%5Bafter%5D=eyJmaWVsZCI6ImNyZWF0ZWRfYXQiLCJkZXNjIjp0cnVlLCJ0aWVCcmVha0ZpZWxkIjoiaWQiLCJ0aWVCcmVha0Rlc2MiOmZhbHNlLCJzb3J0VmFsdWVzIjpudWxsLCJleHBvcnRlZFRodXNGYXIiOjAsInNlc3Npb25TdGFydCI6MTYwNzAzOTI1Mzk4NSwiY3JlYXRlZEF0IjoxNjA3MDM5MjUzOTg1LCJzYWx0ZWRSZXF1ZXN0SGFzaCI6LTQ5ODM0ODc3LCJzYWx0ZWRDdXJzb3JIYXNoIjotMjQwMzQ4MjgwfQ%3D%3D&page%5Bsize%5D=100&query=hello%26page%5Bsize%5D%3D100%26filter%5Btype%5D%3Dticket",    "prev": null  },  "meta": {    "after_cursor": "eyJmaWVsZCI6ImNyZWF0ZWRfYXQiLCJkZXNjIjp0cnVlLCJ0aWVCcmVha0ZpZWxkIjoiaWQiLCJ0aWVCcmVha0Rlc2MiOmZhbHNlLCJzb3J0VmFsdWVzIjpudWxsLCJleHBvcnRlZFRodXNGYXIiOjAsInNlc3Npb25TdGFydCI6MTYwNzAzOTI1Mzk4NSwiY3JlYXRlZEF0IjoxNjA3MDM5MjUzOTg1LCJzYWx0ZWRSZXF1ZXN0SGFzaCI6LTQ5ODM0ODc3LCJzYWx0ZWRDdXJzb3JIYXNoIjotMjQwMzQ4MjgwfQ==",    "before_cursor": null,    "has_more": true  },  "results": []}

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)