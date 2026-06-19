# Views

*Source: https://developer.zendesk.com/api-reference/ticketing/business-rules/views/*

---

## On this page

  * [JSON format](/api-reference/ticketing/business-rules/views/#json-format)
  * [Execution](/api-reference/ticketing/business-rules/views/#execution)
  * [List Views](/api-reference/ticketing/business-rules/views/#list-views)
  * [Count Views](/api-reference/ticketing/business-rules/views/#count-views)
  * [List Views By ID](/api-reference/ticketing/business-rules/views/#list-views-by-id)
  * [List Active Views](/api-reference/ticketing/business-rules/views/#list-active-views)
  * [List Views - Compact](/api-reference/ticketing/business-rules/views/#list-views---compact)
  * [Search Views](/api-reference/ticketing/business-rules/views/#search-views)
  * [Show View](/api-reference/ticketing/business-rules/views/#show-view)
  * [Create View](/api-reference/ticketing/business-rules/views/#create-view)
  * [Preview Views](/api-reference/ticketing/business-rules/views/#preview-views)
  * [Preview Ticket Count](/api-reference/ticketing/business-rules/views/#preview-ticket-count)
  * [Update View](/api-reference/ticketing/business-rules/views/#update-view)
  * [Update Many Views](/api-reference/ticketing/business-rules/views/#update-many-views)
  * [Delete View](/api-reference/ticketing/business-rules/views/#delete-view)
  * [Bulk Delete Views](/api-reference/ticketing/business-rules/views/#bulk-delete-views)
  * [Execute View](/api-reference/ticketing/business-rules/views/#execute-view)
  * [List Tickets From a View](/api-reference/ticketing/business-rules/views/#list-tickets-from-a-view)
  * [Count Tickets in View](/api-reference/ticketing/business-rules/views/#count-tickets-in-view)
  * [Count Tickets in Views](/api-reference/ticketing/business-rules/views/#count-tickets-in-views)
  * [Export View](/api-reference/ticketing/business-rules/views/#export-view)
  * [List View Filter Definitions](/api-reference/ticketing/business-rules/views/#list-view-filter-definitions)


# Views

## On this page

  * [JSON format](/api-reference/ticketing/business-rules/views/#json-format)
  * [Execution](/api-reference/ticketing/business-rules/views/#execution)
  * [List Views](/api-reference/ticketing/business-rules/views/#list-views)
  * [Count Views](/api-reference/ticketing/business-rules/views/#count-views)
  * [List Views By ID](/api-reference/ticketing/business-rules/views/#list-views-by-id)
  * [List Active Views](/api-reference/ticketing/business-rules/views/#list-active-views)
  * [List Views - Compact](/api-reference/ticketing/business-rules/views/#list-views---compact)
  * [Search Views](/api-reference/ticketing/business-rules/views/#search-views)
  * [Show View](/api-reference/ticketing/business-rules/views/#show-view)
  * [Create View](/api-reference/ticketing/business-rules/views/#create-view)
  * [Preview Views](/api-reference/ticketing/business-rules/views/#preview-views)
  * [Preview Ticket Count](/api-reference/ticketing/business-rules/views/#preview-ticket-count)
  * [Update View](/api-reference/ticketing/business-rules/views/#update-view)
  * [Update Many Views](/api-reference/ticketing/business-rules/views/#update-many-views)
  * [Delete View](/api-reference/ticketing/business-rules/views/#delete-view)
  * [Bulk Delete Views](/api-reference/ticketing/business-rules/views/#bulk-delete-views)
  * [Execute View](/api-reference/ticketing/business-rules/views/#execute-view)
  * [List Tickets From a View](/api-reference/ticketing/business-rules/views/#list-tickets-from-a-view)
  * [Count Tickets in View](/api-reference/ticketing/business-rules/views/#count-tickets-in-view)
  * [Count Tickets in Views](/api-reference/ticketing/business-rules/views/#count-tickets-in-views)
  * [Export View](/api-reference/ticketing/business-rules/views/#export-view)
  * [List View Filter Definitions](/api-reference/ticketing/business-rules/views/#list-view-filter-definitions)


A view consists of one or more conditions that define a collection of tickets to display. If the conditions are met, the ticket is included in the view. For example, a view can display all open tickets that were last updated more than 24 hours ago.

For more information, see [Creating views to manage ticket workflow](https://support.zendesk.com/hc/en-us/articles/4408888828570).

### JSON format

Views are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
active| boolean| false| false| Whether the view is active
conditions| object| false| false| Describes how the view is constructed. See [Conditions reference](/documentation/ticketing/reference-guides/conditions-reference)
created_at| string| true| false| The time the view was created
default| boolean| true| false| If true, the view is a default view
description| string| false| false| The description of the view
execution| object| false| false| Describes how the view should be executed. See Execution
id| integer| true| false| Automatically assigned when created
position| integer| false| false| The position of the view
restriction| object| false| false| Who may access this view. Is null when everyone in the account can access it
title| string| false| false| The title of the view
updated_at| string| true| false| The time the view was last updated

### Execution

A view's `execution` object is a read-only object that describes how to display a collection of tickets in the view.

Name| Type| Comment
---|---|---
group_by, sort_by| string| Sort or group the tickets by a column in the View columns table. The `subject` and `submitter` columns are not supported
group_order, sort_order| string| Either "asc" or "desc"
columns| array| The ticket fields to display. Custom fields have an id, title, type, and url referencing the [ticket field](/api-reference/ticketing/tickets/ticket_fields/)
group| object| When present, the structure indicating how the tickets are grouped
sort| object| The column structure of the field used for sorting

#### Example


    {    "execution": {      "columns": [        { "id": "status",  "title": "Status" },        { "id": "updated", "title": "Updated" },        {          "id": 5, "title": "Account", "type": "text",          "url": "https://example.zendesk.com/api/v2/ticket_fields/5"        },        ...      ]      "group": { "id": "status", "title": "Status", "order": "desc" },      "sort": { "id": "updated", "title": "Updated", "order": "desc" }    }}

#### Example


    {  "active": true,  "conditions": {    "all": [      {        "field": "status",        "operator": "less_than",        "value": "solved"      },      {        "field": "assignee_id",        "operator": "is",        "value": "296220096"      }    ],    "any": []  },  "default": false,  "description": "View for recent tickets",  "execution": {    "columns": [      {        "id": "status",        "title": "Status"      },      {        "id": "updated",        "title": "Updated"      },      {        "id": 5,        "title": "Account",        "type": "text",        "url": "https://example.zendesk.com/api/v2/ticket_fields/5"      }    ],    "group": {      "id": "status",      "order": "desc",      "title": "Status"    },    "sort": {      "id": "updated",      "order": "desc",      "title": "Updated"    }  },  "id": 25,  "position": 8,  "restriction": {    "id": 4,    "type": "User"  },  "title": "Tickets updated <12 Hours"}

### List Views

  * `GET /api/v2/views`


Lists shared and personal views available to the current user.

#### Sideloads

The following sideloads are supported:

Name| Will sideload
---|---
app_installation| The app installation that requires each view, if present
permissions| The permissions for each view

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
access| string| Query| false| Only views with given access. May be "personal", "shared", or "account"
active| boolean| Query| false| Only active views if true, inactive views if false
group_id| integer| Query| false| Only views belonging to given group
page| | Query| false| Pagination parameter. Supports both traditional offset and cursor-based pagination: - Traditional: `?page=2` (integer page number) - Cursor: `?page[size]=50&page[after]=cursor` (deepObject with size, after, before) These are mutually exclusive - use one format or the other, not both.
per_page| integer| Query| false| Number of records to return per page. Note: Default and maximum values vary by endpoint. Check endpoint-specific documentation for limits.
sort| string| Query| false| The sort parameter used with cursor pagination. Defaults to "created_at". Prefix with '-' for descending order
sort_by| string| Query| false| The sort_by parameter used with offset pagination. Possible values are "alphabetical", "created_at", or "updated_at". Defaults to "position"
sort_order| string| Query| false| The sort_order parameter used with offset pagination. One of "asc" or "desc". Defaults to "asc" for alphabetical and position sort, "desc" for all others

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/views \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/views?access=&active=&group_id=&page=&per_page=50&sort=&sort_by=&sort_order="	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/views")		.newBuilder()		.addQueryParameter("access", "")		.addQueryParameter("active", "")		.addQueryParameter("group_id", "")		.addQueryParameter("page", "")		.addQueryParameter("per_page", "50")		.addQueryParameter("sort", "")		.addQueryParameter("sort_by", "")		.addQueryParameter("sort_order", "");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/views',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'access': '',    'active': '',    'group_id': '',    'page': '',    'per_page': '50',    'sort': '',    'sort_by': '',    'sort_order': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/views?access=&active=&group_id=&page=&per_page=50&sort=&sort_by=&sort_order="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/views")uri.query = URI.encode_www_form("access": "", "active": "", "group_id": "", "page": "", "per_page": "50", "sort": "", "sort_by": "", "sort_order": "")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "count": 2,  "next_page": null,  "previous_page": null,  "views": [    {      "active": true,      "conditions": {},      "description": "View for recent tickets",      "execution": {},      "id": 25,      "position": 3,      "restriction": {},      "title": "Tickets updated less than 12 Hours"    },    {      "active": false,      "conditions": {},      "description": "View for tickets that are not assigned",      "execution": {},      "id": 23,      "position": 7,      "restriction": {},      "title": "Unassigned tickets"    }  ]}

### Count Views

  * `GET /api/v2/views/count`


Returns an approximate count of shared and personal views available to the current user. If the count exceeds 100,000, the count will return a cached result. This cached result will update every 24 hours.

The `count[refreshed_at]` property is a timestamp that indicates when the count was last updated.

**Note** : When the count exceeds 100,000, `count[refreshed_at]` may occasionally be null. This indicates that the count is being updated in the background, and `count[value]` is limited to 100,000 until the update is complete.

#### Allowed For

  * Agents


#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/views/count \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/views/count"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/views/count")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/views/count',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/views/count"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/views/count")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "count": {    "refreshed_at": "2020-04-06T02:18:17Z",    "value": 16  }}

### List Views By ID

  * `GET /api/v2/views/show_many?ids={ids}`


#### Allowed For

  * Agents


#### Sideloads

The following sideloads are supported:

Name| Will sideload
---|---
app_installation| The app installation that requires each view, if present
permissions| The permissions for each view

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
active| boolean| Query| false| Only active views if true, inactive views if false
ids| string| Query| true| List of view's ids separated by commas.

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/views/show_many?ids=25,23 \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/views/show_many?active=&ids=1%2C2%2C3"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/views/show_many")		.newBuilder()		.addQueryParameter("active", "")		.addQueryParameter("ids", "1,2,3");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/views/show_many',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'active': '',    'ids': '1%2C2%2C3',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/views/show_many?active=&ids=1%2C2%2C3"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/views/show_many")uri.query = URI.encode_www_form("active": "", "ids": "1,2,3")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "count": 2,  "next_page": null,  "previous_page": null,  "views": [    {      "active": true,      "conditions": {},      "description": "View for recent tickets",      "execution": {},      "id": 25,      "position": 3,      "restriction": {},      "title": "Tickets updated less than 12 Hours"    },    {      "active": false,      "conditions": {},      "description": "View for tickets that are not assigned",      "execution": {},      "id": 23,      "position": 7,      "restriction": {},      "title": "Unassigned tickets"    }  ]}

### List Active Views

  * `GET /api/v2/views/active`


Lists active shared and personal views available to the current user.

#### Sideloads

The following sideloads are supported:

Name| Will sideload
---|---
app_installation| The app installation that requires each view, if present
permissions| The permissions for each view

#### Pagination

  * Offset pagination


See [Pagination](/api-reference/introduction/pagination/).

Returns a maximum of 100 records per page.

#### Allowed For

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
access| string| Query| false| Only views with given access. May be "personal", "shared", or "account"
group_id| integer| Query| false| Only views belonging to given group
sort_by| string| Query| false| Possible values are "alphabetical", "created_at", or "updated_at". Defaults to "position"
sort_order| string| Query| false| One of "asc" or "desc". Defaults to "asc" for alphabetical and position sort, "desc" for all others

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/views/active \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/views/active?access=&group_id=&sort_by=&sort_order="	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/views/active")		.newBuilder()		.addQueryParameter("access", "")		.addQueryParameter("group_id", "")		.addQueryParameter("sort_by", "")		.addQueryParameter("sort_order", "");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/views/active',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'access': '',    'group_id': '',    'sort_by': '',    'sort_order': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/views/active?access=&group_id=&sort_by=&sort_order="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/views/active")uri.query = URI.encode_www_form("access": "", "group_id": "", "sort_by": "", "sort_order": "")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "count": 2,  "next_page": null,  "previous_page": null,  "views": [    {      "active": true,      "conditions": {},      "description": "View for recent tickets",      "execution": {},      "id": 25,      "position": 3,      "restriction": {},      "title": "Tickets updated less than 12 Hours"    },    {      "active": true,      "conditions": {},      "description": "View for tickets that are not assigned",      "execution": {},      "id": 23,      "position": 7,      "restriction": {},      "title": "Unassigned tickets"    }  ]}

### List Views - Compact

  * `GET /api/v2/views/compact`


A compacted list of shared and personal views available to the current user. This endpoint never returns more than 32 records and does not respect the "per_page" option.

#### Allowed For

  * Agents


#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/views/compact \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/views/compact"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/views/compact")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/views/compact',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/views/compact"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/views/compact")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "count": 2,  "next_page": null,  "previous_page": null,  "views": [    {      "active": true,      "conditions": {},      "description": "View for recent tickets",      "execution": {},      "id": 25,      "position": 3,      "restriction": {},      "title": "Tickets updated less than 12 Hours"    },    {      "active": false,      "conditions": {},      "description": "View for tickets that are not assigned",      "execution": {},      "id": 23,      "position": 7,      "restriction": {},      "title": "Unassigned tickets"    }  ]}

### Search Views

  * `GET /api/v2/views/search?query={query}`


#### Pagination

  * Offset pagination only


See [Using Offset Pagination](/api-reference/introduction/pagination/#using-offset-pagination).

#### Allowed For

  * Agents


#### Sideloads

The following sideloads are supported. For more information, see [Side-loading](/documentation/ticketing/using-the-zendesk-api/side_loading/).

Name| Will sideload
---|---
app_installation| The app installation that requires each view, if present
permissions| The permissions for each view

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
access| string| Query| false| Filter views by access. May be "personal", "shared", or "account"
active| boolean| Query| false| Filter by active views if true or inactive views if false
group_id| integer| Query| false| Filter views by group
include| string| Query| false| A sideload to include in the response. See Sideloads
query| string| Query| true| Query string used to find all views with matching title
sort_by| string| Query| false| Possible values are "alphabetical", "created_at", "updated_at", and "position". If unspecified, the views are sorted by relevance
sort_order| string| Query| false| One of "asc" or "desc". Defaults to "asc" for alphabetical and position sort, "desc" for all others

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/views/search?query=unsolved \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/views/search?access=&active=&group_id=&include=permissions&query=sales%26group_id%3D25789188&sort_by=&sort_order="	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/views/search")		.newBuilder()		.addQueryParameter("access", "")		.addQueryParameter("active", "")		.addQueryParameter("group_id", "")		.addQueryParameter("include", "permissions")		.addQueryParameter("query", "sales&group_id=25789188")		.addQueryParameter("sort_by", "")		.addQueryParameter("sort_order", "");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/views/search',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'access': '',    'active': '',    'group_id': '',    'include': 'permissions',    'query': 'sales%26group_id%3D25789188',    'sort_by': '',    'sort_order': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/views/search?access=&active=&group_id=&include=permissions&query=sales%26group_id%3D25789188&sort_by=&sort_order="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/views/search")uri.query = URI.encode_www_form("access": "", "active": "", "group_id": "", "include": "permissions", "query": "sales&group_id=25789188", "sort_by": "", "sort_order": "")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "count": 2,  "next_page": null,  "previous_page": null,  "views": [    {      "active": true,      "conditions": {},      "description": "View for recent tickets",      "execution": {},      "id": 25,      "position": 3,      "restriction": {},      "title": "Tickets updated less than 12 Hours"    },    {      "active": false,      "conditions": {},      "description": "View for tickets that are not assigned",      "execution": {},      "id": 23,      "position": 7,      "restriction": {},      "title": "Unassigned tickets"    }  ]}

### Show View

  * `GET /api/v2/views/{view_id}`


#### Allowed For

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
include| string| Query| false| A comma-separated list of sideloads to include in the response.
view_id| integer| Path| true| The ID of the view

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/views/{view_id} \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/views/25?include="	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/views/25")		.newBuilder()		.addQueryParameter("include", "");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/views/25',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'include': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/views/25?include="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/views/25")uri.query = URI.encode_www_form("include": "")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "view": {    "active": true,    "conditions": {},    "description": "View for recent tickets",    "execution": {},    "id": 25,    "position": 3,    "restriction": {},    "title": "Tickets updated less than 12 Hours"  }}

### Create View

  * `POST /api/v2/views`


#### Allowed For

  * Agents


#### JSON Format

The JSON format consists of one property, a `view` object that lists the values to set when the view is created.

**Note** : The request must include at least one condition in the `all` array that checks one of the following fields: `status`, `type`, `group_id`, `assignee_id`, or `requester_id`.

Name| Description
---|---
title| Required. The title of the view
all| Required. An array of one or more conditions. A ticket must meet all of them to be included in the view. See [Conditions reference](/documentation/ticketing/reference-guides/conditions-reference)
any| An array of one or more conditions. A ticket must meet any of them to be included in the view. See [Conditions reference](/documentation/ticketing/reference-guides/conditions-reference)
description| The description of the view
active| Allowed values are true or false. Determines if the view is displayed or not
output| An object that specifies the columns to display. Example: `"output": {"columns": ["status", "description", "priority"]}`. See View columns
restriction| An object that describes who can access the view. To give all agents access to the view, omit this property

The `restriction` object has the following properties.

Name| Comment
---|---
type| Allowed values are "Group" or "User"
id| The numeric ID of a single group or user
ids| The numeric IDs of a single or more groups. Recommended for "Group" `type`

If `type` is "Group", the `ids` property is the preferred method of specifying the group id or ids.

#### Example Request Body


    {  "view": {    "title": "Kelly's tickets",    "raw_title": "{{dc.tickets_assigned_to_kelly}}",    "description": "Tickets that are assigned to Kelly",    "active": true,    "restriction": {      "type": "User",      "id": "213977756"    },    "all": [      {        "field": "status",        "operator": "less_than",        "value": "solved"      },      {        "field": "group_id",        "operator": "is",        "value": "24000932"      },      {        "field": "custom_fields_360011872073",        "operator": "is",        "value": "Canada"      },      ...    ],    "output": {      "columns": ["status", "requester", "assignee"],      "group_by": "assignee",      "group_order": "desc",      "sort_by": "status",      "sort_order": "desc"    }  }}

#### View columns

The `output` request parameter lets you specify what columns to include in the view in the agent interface. Example: `"output": {"columns": ["status", "description", "priority"]}`. The following table lists possible columns for views in the agent UI and the corresponding values in the `columns` array.

For custom fields, specify the id of the custom field in the `columns` array.

You can specify a total of 10 columns to a view.

View column title in UI| Value
---|---
Assigned| `assigned`
Assignee| `assignee`
Due Date| `due_date`
Group| `group`
ID| `nice_id`
Updated| `updated`
Assignee updated| `updated_assignee`
Requester updated| `updated_requester`
Updater| `updated_by_type`
Organization| `organization`
Priority| `priority`
Requested| `created`
Requester| `requester`
Requester language| `locale_id`
Satisfaction| `satisfaction_score`
Solved| `solved`
Status category| `status`
Subject| `description`
Submitter| `submitter`
Ticket form| `ticket_form`
Type| `type`
Brand| `brand`
Ticket status| `custom_status_id`

#### View sorting

You can group and sort items in the view by adding items to the `output` parameter:

Attribute| Description
---|---
`group_by`, `sort_by`| Sort or group the tickets by a column in the View columns table. The `description`, `submitter` and `custom_status_id` columns are not supported
`group_order`, `sort_order`| Either "asc" or "desc"

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/views \  -d '{"view": {"title": "Roger Wilco", "all": [{"field": "status", "operator": "is", "value": "open"}, {"field": "priority", "operator": "less_than", "value": "high"}], "any": [{ "field": "current_tags", "operator": "includes", "value": "hello" }]}}' \  -H "Content-Type: application/json" \  -v -u {email_address}/token:{api_token} -X POST

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/views"	method := "POST"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/views")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'POST',  url: 'https://example.zendesk.com/api/v2/views',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/views"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/views")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "view": {    "active": true,    "conditions": {      "all": [        {          "field": "status",          "operator": "is",          "value": "open"        },        {          "field": "priority",          "operator": "less_than",          "value": "high"        }      ],      "any": [        {          "field": "current_tags",          "operator": "includes",          "value": "hello"        }      ]    },    "id": 9873843,    "title": "Roger Wilco"  }}

### Preview Views

  * `POST /api/v2/views/preview`


You can preview views by constructing the conditions in the proper format and nesting them under the `view` property. See [Conditions reference](/documentation/ticketing/reference-guides/conditions-reference/). The output can also be controlled by passing in any of the following parameters and nesting them under the `output` property.

Name| Type| Comment
---|---|---
columns| Array| The ticket fields to display. System fields are looked up by name, custom fields by title or id. See the View columns table
group_by| String| When present, the field by which the tickets are grouped
group_order| String| The direction the tickets are grouped. May be one of "asc" or "desc"
sort_order| String| The direction the tickets are sorted. May be one of "asc" or "desc"
sort_by| String| The ticket field used for sorting. This will either be a title or a custom field id.

This endpoint is rate limited to 5 requests per minute, per view, per agent.

#### Pagination

  * Cursor pagination (recommended)
  * Offset pagination


See [Pagination](/api-reference/introduction/pagination/).

#### Allowed For

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
exclude| string| Query| false| A comma-separated list of sideloads to exclude from the response.
include| string| Query| false| A comma-separated list of sideloads to include in the response.
page| | Query| false| Pagination parameter. Supports both traditional offset and cursor-based pagination: - Traditional: `?page=2` (integer page number) - Cursor: `?page[size]=50&page[after]=cursor` (deepObject with size, after, before) These are mutually exclusive - use one format or the other, not both.
per_page| integer| Query| false| Number of records to return per page. Note: Default and maximum values vary by endpoint. Check endpoint-specific documentation for limits.

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/views/preview \  -v -u {email_address}/token:{api_token} -X POST -H "Content-Type: application/json" \  -d '{"view": {"all": [{"operator": "is", "value": "open", "field": "status"}], "output": {"columns": ["subject"]}}}'

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/views/preview?exclude=&include=&page=&per_page=50"	method := "POST"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/views/preview")		.newBuilder()		.addQueryParameter("exclude", "")		.addQueryParameter("include", "")		.addQueryParameter("page", "")		.addQueryParameter("per_page", "50");RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'POST',  url: 'https://example.zendesk.com/api/v2/views/preview',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'exclude': '',    'include': '',    'page': '',    'per_page': '50',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/views/preview?exclude=&include=&page=&per_page=50"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/views/preview")uri.query = URI.encode_www_form("exclude": "", "include": "", "page": "", "per_page": "50")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "columns": [    {      "id": "subject",      "title": "Subject"    }  ],  "rows": [    {      "subject": "en-US",      "ticket": {}    }  ]}

### Preview Ticket Count

  * `POST /api/v2/views/preview/count`


Returns the ticket count for a single preview.

#### Allowed For

  * Agents


#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/views/preview/count \  -v -u {email_address}/token:{api_token} -X POST -H "Content-Type: application/json" \  -d '{"view": {"all": [{"operator": "is", "value": "open", "field": "status"}]}}'

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/views/preview/count"	method := "POST"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/views/preview/count")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'POST',  url: 'https://example.zendesk.com/api/v2/views/preview/count',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/views/preview/count"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/views/preview/count")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "view_count": {    "fresh": true,    "pretty": "~700",    "url": "https://company.zendesk.com/api/v2/views/25/count",    "value": 719,    "view_id": 25  }}

### Update View

  * `PUT /api/v2/views/{view_id}`


#### Allowed For

  * Agents


#### JSON Format

The PUT request takes one property, a `view` object that lists the values to update. All properties are optional.

**Note** : Updating a condition updates the containing array, clearing the other conditions. Include all your conditions when updating any condition.

Name| Description
---|---
title| The title of the view
all| An array of one or more conditions. A ticket must meet all the conditions to be included in the view. The PUT request replaces all existing conditions. See [Conditions reference](/documentation/ticketing/reference-guides/conditions-reference)
any| An array of one or more conditions. A ticket must meet any of them to be included in the view. At least one `all` condition must be defined with the `any` conditions. The PUT request replaces all existing `any` conditions. See [Conditions reference](/documentation/ticketing/reference-guides/conditions-reference)
active| Allowed values are true or false. Determines if the view is displayed or not
output| An object that specifies the columns to display. Example: `"output": {"columns": ["status", "description," "priority"]}`. See View columns
restriction| An object that describes who can access the view. To give all agents access to the view, omit this property

The `restriction` object has the following properties.

Name| Comment
---|---
type| Allowed values are "Group" or "User"
id| The numeric ID of a single group or user
ids| The numeric IDs of a single or more groups. Recommended for "Group" `type`

If `type` is "Group", the `ids` property is the preferred method of specifying the group id or ids.

You can also update how items are sorted and grouped. See View sorting in Create View.

#### Example Request Body


    {  "view": {    "title": "Code red tickets",    "restriction": {      "type": "Group",      "ids": [10052, 10057, 10062, 10002]    },    "all": [      {        "field": "priority",        "operator": "is",        "value": "urgent"      }    ],    "output": {      "columns": ["status", "requester", "assignee", "updated"]    }  }}

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
view_id| integer| Path| true| The ID of the view

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/views/{view_id} \  -d '{"view": {"title": "Roger Wilco II"}}' \  -H "Content-Type: application/json" \  -v -u {email_address}/token:{api_token} -X PUT

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/views/25"	method := "PUT"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/views/25")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'PUT',  url: 'https://example.zendesk.com/api/v2/views/25',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/views/25"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/views/25")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "view": {    "active": true,    "conditions": {},    "description": "View for recent tickets",    "execution": {},    "id": 25,    "position": 3,    "restriction": {},    "title": "Roger Wilco II"  }}

### Update Many Views

  * `PUT /api/v2/views/update_many`


#### Allowed For

  * Agents


#### Request Parameters

The PUT request expects a `views` object that lists the views to update.

Each view may have the following properties:

Name| Mandatory| Description
---|---|---
id| yes| The ID of the view to update
position| no| The new position of the view
active| no| The active status of the view (true or false)

#### Example Request Body


    {  "views": [    {"id": 25, "position": 3},    {"id": 23, "position": 5},    {"id": 27, "position": 9},    {"id": 22, "position": 7}  ]}

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/views/update_many \  -d '{"views": [{"id": 123, "position": 8}]}' \  -H "Content-Type: application/json" \  -v -u {email_address}/token:{api_token} -X PUT

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/views/update_many"	method := "PUT"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/views/update_many")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'PUT',  url: 'https://example.zendesk.com/api/v2/views/update_many',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/views/update_many"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/views/update_many")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "views": [    {      "active": true,      "conditions": {},      "description": "View for recent tickets",      "execution": {},      "id": 123,      "position": 8,      "restriction": {},      "title": "Tickets updated less than 12 Hours"    }  ]}

### Delete View

  * `DELETE /api/v2/views/{view_id}`


#### Allowed For

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
view_id| integer| Path| true| The ID of the view

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/views/{view_id} \  -H "Content-Type: application/json" \  -v -u {email_address}/token:{api_token} -X DELETE

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/views/25"	method := "DELETE"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/views/25")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("DELETE", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'DELETE',  url: 'https://example.zendesk.com/api/v2/views/25',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/views/25"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"DELETE",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/views/25")request = Net::HTTP::Delete.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**204 No Content**


    // Status 204 No Content
    null

### Bulk Delete Views

  * `DELETE /api/v2/views/destroy_many?ids={ids}`


Deletes the views corresponding to the provided list of IDs.

#### Allowed For

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
ids| string| Query| true| The IDs of the views to delete

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/views/destroy_many?ids=1,2,3 \  -v -u {email_address}/token:{api_token} -X DELETE

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/views/destroy_many?ids=1%2C2%2C3"	method := "DELETE"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/views/destroy_many")		.newBuilder()		.addQueryParameter("ids", "1,2,3");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("DELETE", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'DELETE',  url: 'https://example.zendesk.com/api/v2/views/destroy_many',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'ids': '1%2C2%2C3',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/views/destroy_many?ids=1%2C2%2C3"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"DELETE",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/views/destroy_many")uri.query = URI.encode_www_form("ids": "1,2,3")request = Net::HTTP::Delete.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**204 No Content**


    // Status 204 No Content
    null

### Execute View

  * `GET /api/v2/views/{view_id}/execute`


Returns the column titles and the rows of the specified view.

The `columns` array lists the view's column titles and includes only views parameters.

The `rows` array lists the values of each column for each ticket and includes parameters from both views and tickets. Though not displayed in the view, a partial ticket object is included with each row object.

**Note** : To get the full ticket objects for a specified view, use List Tickets from a View.

This endpoint is rate limited to 5 requests per minute, per view, per agent. This rate limit includes activity in Zendesk Support. An API script is more likely to encounter rate limit errors if the authenticating agent or admin is concurrently active in Zendesk Support.

The view execution system is designed for periodic rather than high-frequency API usage. In particular, views called very frequently may be cached by Zendesk. This means that the API client will still receive a result, but that result may have been computed at any time within the last 10 minutes.

Zendesk recommends using the Incremental Ticket Export endpoint to get the latest changes. You can call it more often, and it returns all the tickets that changed since the last poll. For details and rate limits, see [Incremental Exports](/api-reference/ticketing/ticket-management/incremental_exports/).

View output sorting can be controlled by passing the `sort_by` and `sort_order` parameters in the format described in the table in Preview Views.

#### Allowed For

  * Agents


#### Pagination

  * Cursor pagination (recommended)
  * Offset pagination


See [Pagination](/api-reference/introduction/pagination/).

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
exclude| string| Query| false| A comma-separated list of sideloads to exclude from the response.
group_by| string| Query| false| The ticket field used for grouping. This will either be a title or a custom field id.
include| string| Query| false| A comma-separated list of sideloads to include in the response.
page| | Query| false| Pagination parameter. Supports both traditional offset and cursor-based pagination: - Traditional: `?page=2` (integer page number) - Cursor: `?page[size]=50&page[after]=cursor` (deepObject with size, after, before) These are mutually exclusive - use one format or the other, not both.
sort_by| string| Query| false| The ticket field used for sorting. This will either be a title or a custom field id.
sort_order| string| Query| false| The direction the tickets are sorted. May be one of 'asc' or 'desc'
view_id| integer| Path| true| The ID of the view

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/views/{view_id}/execute \  -v -u {email_address}/token:{api_token}

**curl**

With sort options


    curl 'https://{subdomain}.zendesk.com/api/v2/views/{id}/execute?sort_by=id&sort_order=desc' \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/views/25/execute?exclude=&group_by=&include=&page=&sort_by=&sort_order="	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/views/25/execute")		.newBuilder()		.addQueryParameter("exclude", "")		.addQueryParameter("group_by", "")		.addQueryParameter("include", "")		.addQueryParameter("page", "")		.addQueryParameter("sort_by", "")		.addQueryParameter("sort_order", "");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/views/25/execute',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'exclude': '',    'group_by': '',    'include': '',    'page': '',    'sort_by': '',    'sort_order': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/views/25/execute?exclude=&group_by=&include=&page=&sort_by=&sort_order="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/views/25/execute")uri.query = URI.encode_www_form("exclude": "", "group_by": "", "include": "", "page": "", "sort_by": "", "sort_order": "")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "columns": [    {      "id": "locale",      "title": "Locale"    },    {      "id": 5,      "title": "Account"    }  ],  "groups": [],  "rows": [    {      "group": 1,      "locale": "en-US",      "ticket": {}    }  ],  "view": {    "id": 25  }}

### List Tickets From a View

  * `GET /api/v2/views/{view_id}/tickets`


#### Allowed For

  * Agents


#### Pagination

  * Cursor pagination (recommended)
  * Offset pagination


See [Pagination](/api-reference/introduction/pagination/).

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
sort_by| string| Query| false| Sort or group the tickets by a column in the View columns table. The `subject` and `submitter` columns are not supported
sort_order| string| Query| false| One of "asc" or "desc". Defaults to "asc" for alphabetical and position sort, "desc" for all others
view_id| integer| Path| true| The ID of the view

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/views/{view_id}/tickets \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/views/25/tickets?sort_by=&sort_order="	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/views/25/tickets")		.newBuilder()		.addQueryParameter("sort_by", "")		.addQueryParameter("sort_order", "");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/views/25/tickets',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'sort_by': '',    'sort_order': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/views/25/tickets?sort_by=&sort_order="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/views/25/tickets")uri.query = URI.encode_www_form("sort_by": "", "sort_order": "")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "tickets": [    {      "id": 35436,      "requester_id": 20978392,      "subject": "Help I need somebody!"    },    {      "id": 20057623,      "requester_id": 20978392,      "subject": "Not just anybody!"    }  ]}

### Count Tickets in View

  * `GET /api/v2/views/{view_id}/count`


Returns the ticket count for a single view.

This endpoint is rate limited to 5 requests per minute, per view, per agent.

#### View Counts

The view count endpoints, Count Tickets in View (this endpoint) and Count Tickets in Views, let you estimate how many tickets remain in a view without having to retrieve the entire view. They're designed to help estimate view size. From a business perspective, accuracy becomes less relevant as view size increases.

To ensure quality of service, these counts are cached more heavily as the number of tickets in a view grows. For a view with thousands of tickets, you can expect the count to be cached for 60-90 minutes. As a result, the count may not reflect the actual number of tickets in your view.

View counts are represented as JSON objects with the following attributes:

Name| Type| Comment
---|---|---
view_id| integer| The id of the view
url| string| The API url of the count
value| integer| The cached number of tickets in the view. Can also be null if the system is loading and caching new data. Not to be confused with 0 tickets
pretty| string| A pretty-printed text approximation of the view count
fresh| boolean| false if the cached data is stale and the system is still loading and caching new data
active| boolean| Only active views if true, inactive views if false, all views if null.

#### Example


    {  "view_count": {    "view_id": 25,    "url":     "https://company.zendesk.com/api/v2/views/25/count",    "value":   719,    "pretty":  "~700",    "fresh":   true  }}

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
view_id| integer| Path| true| The ID of the view

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/views/{view_id}/count \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/views/25/count"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/views/25/count")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/views/25/count',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/views/25/count"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/views/25/count")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "view_count": {    "fresh": true,    "pretty": "~700",    "url": "https://company.zendesk.com/api/v2/views/25/count",    "value": 719,    "view_id": 25  }}

### Count Tickets in Views

  * `GET /api/v2/views/count_many?ids={ids}`


Returns the ticket count of each view in a list of views. Accepts up to 20 view ids per request. For the ticket count of a single view, see Count Tickets in View.

Only returns values for personal and shared views accessible to the user performing the request.

_**Note:**_ Due to the asynchronous operation of computing the counts for the requested views, some of the views' counts could be null. This means that the system is still computing the count for that view. Periodically issue another request until all of the views' counts in the response are integers greater than zero.

#### Rate limiting

This endpoint is rate limited to 6 requests every 1 minute.

#### Allowed For

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
ids| string| Query| true| List of view's ids separated by commas.

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/views/count_many?ids={view_id} \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/views/count_many?ids=1%2C2%2C3"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/views/count_many")		.newBuilder()		.addQueryParameter("ids", "1,2,3");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/views/count_many',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'ids': '1%2C2%2C3',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/views/count_many?ids=1%2C2%2C3"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/views/count_many")uri.query = URI.encode_www_form("ids": "1,2,3")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "view_counts": [    {      "fresh": true,      "pretty": "~700",      "url": "https://company.zendesk.com/api/v2/views/25/count",      "value": 719,      "view_id": 25    },    {      "fresh": false,      "pretty": "...",      "url": "https://company.zendesk.com/api/v2/views/78/count",      "value": null,      "view_id": 78    }  ]}

**429 Too Many Requests**


    // Status 429 Too Many Requests
    {  "errors": [    {      "code": "TooManyRequests",      "title": "Too many requests to update"    }  ]}

### Export View

  * `GET /api/v2/views/{view_id}/export`


Returns the csv attachment of the specified view if possible. Enqueues a job to produce the csv if necessary.

#### Allowed For

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
view_id| integer| Path| true| The ID of the view

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/views/{view_id}/export \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/views/25/export"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/views/25/export")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/views/25/export',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/views/25/export"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/views/25/export")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "export": {    "status": "starting",    "view_id": 25  }}

### List View Filter Definitions

  * `GET /api/v2/views/definitions`


Returns the definitions of the conditions and actions a view can perform. The definitions include conditions, output columns, groupable fields, and sortable fields.

#### Allowed For

  * Agents


#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/views/definitions \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/views/definitions"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/views/definitions")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/views/definitions',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/views/definitions"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/views/definitions")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "definitions": {    "conditions_all": [      {        "group": "ticket",        "nullable": false,        "operators": [          {            "terminal": false,            "title": "Is",            "value": "is"          },          {            "terminal": false,            "title": "Is not",            "value": "is_not"          }        ],        "repeatable": false,        "subject": "status",        "title": "Status",        "type": "list",        "values": [          {            "enabled": true,            "title": "New",            "value": "new"          },          {            "enabled": true,            "title": "Open",            "value": "open"          }        ]      }    ],    "conditions_any": [      {        "group": "ticket",        "nullable": false,        "operators": [          {            "terminal": false,            "title": "Is",            "value": "is"          }        ],        "repeatable": false,        "subject": "status",        "title": "Status",        "type": "list",        "values": [          {            "enabled": true,            "title": "New",            "value": "new"          }        ]      }    ],    "groupables": [      {        "group": "ticket",        "title": "Status",        "type": "list",        "value": "status"      }    ],    "output": [      {        "group": "ticket",        "title": "ID",        "type": "tagger",        "value": "nice_id"      }    ],    "sortables": [      {        "group": "ticket",        "title": "ID",        "type": "number",        "value": "nice_id"      }    ]  }}

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)