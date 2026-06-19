# Triggers

*Source: https://developer.zendesk.com/api-reference/ticketing/business-rules/triggers/*

---

## On this page

  * [JSON format](/api-reference/ticketing/business-rules/triggers/#json-format)
  * [List Ticket Triggers](/api-reference/ticketing/business-rules/triggers/#list-ticket-triggers)
  * [List Active Ticket Triggers](/api-reference/ticketing/business-rules/triggers/#list-active-ticket-triggers)
  * [Search Ticket Triggers](/api-reference/ticketing/business-rules/triggers/#search-ticket-triggers)
  * [Show Ticket Trigger](/api-reference/ticketing/business-rules/triggers/#show-ticket-trigger)
  * [List Ticket Trigger Action and Condition Definitions](/api-reference/ticketing/business-rules/triggers/#list-ticket-trigger-action-and-condition-definitions)
  * [List Ticket Trigger Revisions](/api-reference/ticketing/business-rules/triggers/#list-ticket-trigger-revisions)
  * [Show Ticket Trigger Revision](/api-reference/ticketing/business-rules/triggers/#show-ticket-trigger-revision)
  * [Create Trigger](/api-reference/ticketing/business-rules/triggers/#create-trigger)
  * [Update Ticket Trigger](/api-reference/ticketing/business-rules/triggers/#update-ticket-trigger)
  * [Update Many Ticket Triggers](/api-reference/ticketing/business-rules/triggers/#update-many-ticket-triggers)
  * [Reorder Ticket Triggers](/api-reference/ticketing/business-rules/triggers/#reorder-ticket-triggers)
  * [Delete Ticket Trigger](/api-reference/ticketing/business-rules/triggers/#delete-ticket-trigger)
  * [Bulk Delete Ticket Triggers](/api-reference/ticketing/business-rules/triggers/#bulk-delete-ticket-triggers)


# Triggers

## On this page

  * [JSON format](/api-reference/ticketing/business-rules/triggers/#json-format)
  * [List Ticket Triggers](/api-reference/ticketing/business-rules/triggers/#list-ticket-triggers)
  * [List Active Ticket Triggers](/api-reference/ticketing/business-rules/triggers/#list-active-ticket-triggers)
  * [Search Ticket Triggers](/api-reference/ticketing/business-rules/triggers/#search-ticket-triggers)
  * [Show Ticket Trigger](/api-reference/ticketing/business-rules/triggers/#show-ticket-trigger)
  * [List Ticket Trigger Action and Condition Definitions](/api-reference/ticketing/business-rules/triggers/#list-ticket-trigger-action-and-condition-definitions)
  * [List Ticket Trigger Revisions](/api-reference/ticketing/business-rules/triggers/#list-ticket-trigger-revisions)
  * [Show Ticket Trigger Revision](/api-reference/ticketing/business-rules/triggers/#show-ticket-trigger-revision)
  * [Create Trigger](/api-reference/ticketing/business-rules/triggers/#create-trigger)
  * [Update Ticket Trigger](/api-reference/ticketing/business-rules/triggers/#update-ticket-trigger)
  * [Update Many Ticket Triggers](/api-reference/ticketing/business-rules/triggers/#update-many-ticket-triggers)
  * [Reorder Ticket Triggers](/api-reference/ticketing/business-rules/triggers/#reorder-ticket-triggers)
  * [Delete Ticket Trigger](/api-reference/ticketing/business-rules/triggers/#delete-ticket-trigger)
  * [Bulk Delete Ticket Triggers](/api-reference/ticketing/business-rules/triggers/#bulk-delete-ticket-triggers)


A ticket trigger consists of one or more actions performed when a ticket is created or updated. The actions are performed only if certain conditions are met. For example, a ticket trigger can notify the customer when an agent changes the status of a ticket to Solved.

Ticket triggers also may depend on one or more conditions being met.

For more information on conditions and actions, see the following Help Center articles:

  * [Support API: Conditions reference](/documentation/ticketing/reference-guides/conditions-reference)
  * [Support API: Actions reference](/documentation/ticketing/reference-guides/actions-reference)


All your ticket triggers are checked from first to last each time a ticket is created or updated. The order of ticket triggers is important because the actions of one ticket trigger may affect another trigger. New ticket triggers are added in last place by default.

For more information, see [Creating ticket triggers for automatic ticket updates and notifications ](https://support.zendesk.com/hc/en-us/articles/4408886797466).

**Note** : This endpoints described on this page apply only to ticket triggers. For object trigger API documentation, see [Object Triggers](/api-reference/ticketing/business-rules/object_triggers).

### JSON format

Triggers are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
actions| array| false| true| An array of actions describing what the ticket trigger will do. See [Actions reference](/documentation/ticketing/reference-guides/actions-reference)
active| boolean| false| false| Whether the ticket trigger is active
all| array| false| false| Legacy format for conditions (deprecated). Use conditions.all instead
any| array| false| false| Legacy format for conditions (deprecated). Use conditions.any instead
brand_id| integer| false| false| The ID of the brand the ticket trigger belongs to
category| object| false| false| A category to create and assign to the trigger
category_id| string| false| false| The ID of the category the ticket trigger belongs to
conditions| object| false| false| An object that describes the circumstances under which the trigger performs its actions. See [Conditions reference](/documentation/ticketing/reference-guides/conditions-reference)
created_at| string| true| false| The time the ticket trigger was created
default| boolean| true| false| If true, the ticket trigger is a standard trigger
description| string| false| false| The description of the ticket trigger
id| integer| true| false| Automatically assigned when created
position| integer| false| false| Position of the ticket trigger, determines the order they will execute in
raw_title| string| false| false| The raw format of the title of the ticket trigger
restriction| object| false| false| Access restriction for this trigger. A null value allows unrestricted access
title| string| false| true| The title of the ticket trigger
updated_at| string| true| false| The time of the last update of the ticket trigger
url| string| true| false| The url of the ticket trigger

#### Example


    {  "actions": [    {}  ],  "active": true,  "category_id": "10026",  "conditions": {},  "created_at": "2012-09-25T22:50:26Z",  "default": false,  "description": "Close and save a ticket",  "id": 25,  "position": 8,  "raw_title": "Close and Save",  "title": "Close and Save",  "updated_at": "2012-09-25T22:50:26Z",  "url": "http://{subdomain}.zendesk.com/api/v2/triggers/25"}

### List Ticket Triggers

  * `GET /api/v2/triggers`


Lists all ticket triggers for the current account.

#### Pagination

  * Cursor pagination (recommended)
  * Offset pagination


See [Pagination](/api-reference/introduction/pagination/).

Returns a maximum of 100 records per page.

#### Allowed For

  * Agents


#### Sideloads

The following sideloads are supported. The usage sideloads are only supported on the Support Professional or Suite Growth plan or above.

Name| Will sideload
---|---
app_installation| The app installation that requires each trigger, if present
permissions| The permissions for each trigger
usage_1h| The number of times each trigger has been used in the past hour
usage_24h| The number of times each trigger has been used in the past day
usage_7d| The number of times each trigger has been used in the past week
usage_30d| The number of times each trigger has been used in the past thirty days

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
active| boolean| Query| false| Filter by active triggers if true or inactive triggers if false
category_id| string| Query| false| Filter triggers by category ID
include| string| Query| false| A sideload to include in the response. See Sideloads
page| | Query| false| Pagination parameter. Supports both traditional offset and cursor-based pagination: - Traditional: `?page=2` (integer page number) - Cursor: `?page[size]=50&page[after]=cursor` (deepObject with size, after, before) These are mutually exclusive - use one format or the other, not both.
per_page| integer| Query| false| Number of records to return per page. Note: Default and maximum values vary by endpoint. Check endpoint-specific documentation for limits.
sort| string| Query| false| Cursor-based pagination only. Possible values are "alphabetical", "created_at", "updated_at", or "position".
sort_by| string| Query| false| Offset pagination only. Possible values are "alphabetical", "created_at", "updated_at", "usage_1h", "usage_24h", or "usage_7d". Defaults to "position"
sort_order| string| Query| false| One of "asc" or "desc". Defaults to "asc" for alphabetical and position sort, "desc" for all others

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/triggers \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/triggers?active=true&category_id=10026&include=usage_24h&page=&per_page=50&sort=position&sort_by=position&sort_order=desc"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/triggers")		.newBuilder()		.addQueryParameter("active", "true")		.addQueryParameter("category_id", "10026")		.addQueryParameter("include", "usage_24h")		.addQueryParameter("page", "")		.addQueryParameter("per_page", "50")		.addQueryParameter("sort", "position")		.addQueryParameter("sort_by", "position")		.addQueryParameter("sort_order", "desc");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/triggers',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'active': 'true',    'category_id': '10026',    'include': 'usage_24h',    'page': '',    'per_page': '50',    'sort': 'position',    'sort_by': 'position',    'sort_order': 'desc',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/triggers?active=true&category_id=10026&include=usage_24h&page=&per_page=50&sort=position&sort_by=position&sort_order=desc"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/triggers")uri.query = URI.encode_www_form("active": "true", "category_id": "10026", "include": "usage_24h", "page": "", "per_page": "50", "sort": "position", "sort_by": "position", "sort_order": "desc")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "count": 2,  "next_page": null,  "previous_page": null,  "triggers": [    {      "actions": [],      "active": true,      "conditions": {},      "created_at": "2012-09-25T22:50:26Z",      "description": "Close and save a ticket",      "id": 25,      "position": 8,      "raw_title": "Close and Save",      "title": "Close and Save",      "updated_at": "2012-09-25T22:50:26Z",      "url": "http://{subdomain}.zendesk.com/api/v2/triggers/25"    },    {      "actions": [],      "active": false,      "conditions": {        "all": [          {            "field": "status",            "operator": "less_than",            "value": "solved"          },          {            "field": "assignee_id",            "operator": "is",            "value": "296220096"          }        ],        "any": [          {            "field": "status",            "operator": "less_than",            "value": "solved"          },          {            "field": "custom_status_id",            "operator": "includes",            "value": [              "1",              "2"            ]          }        ]      },      "created_at": "2012-09-25T22:50:26Z",      "description": "Assign a ticket with a priority tag",      "id": 26,      "position": 9,      "raw_title": "{{dc.assign_priority_tag}}",      "title": "Assign priority tag",      "updated_at": "2012-09-25T22:50:26Z",      "url": "http://{subdomain}.zendesk.com/api/v2/triggers/26"    }  ]}

### List Active Ticket Triggers

  * `GET /api/v2/triggers/active`


Lists all active ticket triggers.

#### Pagination

  * Cursor pagination (recommended)
  * Offset pagination


See [Pagination](/api-reference/introduction/pagination/).

Returns a maximum of 100 records per page.

#### Allowed For

  * Agents


#### Sideloads

The following sideloads are supported:

Name| Will sideload
---|---
app_installation| The app installation that requires each ticket trigger, if present
permissions| The permissions for each trigger
usage_1h| The number of times each ticket trigger has been used in the past hour
usage_24h| The number of times each ticket trigger has been used in the past day
usage_7d| The number of times each ticket trigger has been used in the past week
usage_30d| The number of times each ticket trigger has been used in the past thirty days

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
category_id| string| Query| false| Filter triggers by category ID
sort| string| Query| false| Cursor-based pagination only. Possible values are "alphabetical", "created_at", "updated_at", or "position".
sort_by| string| Query| false| Offset pagination only. Possible values are "alphabetical", "created_at", "updated_at", "usage_1h", "usage_24h", or "usage_7d". Defaults to "position"
sort_order| string| Query| false| One of "asc" or "desc". Defaults to "asc" for alphabetical and position sort, "desc" for all others

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/triggers/active \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/triggers/active?category_id=10026&sort=position&sort_by=position&sort_order=desc"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/triggers/active")		.newBuilder()		.addQueryParameter("category_id", "10026")		.addQueryParameter("sort", "position")		.addQueryParameter("sort_by", "position")		.addQueryParameter("sort_order", "desc");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/triggers/active',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'category_id': '10026',    'sort': 'position',    'sort_by': 'position',    'sort_order': 'desc',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/triggers/active?category_id=10026&sort=position&sort_by=position&sort_order=desc"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/triggers/active")uri.query = URI.encode_www_form("category_id": "10026", "sort": "position", "sort_by": "position", "sort_order": "desc")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "count": 2,  "next_page": null,  "previous_page": null,  "triggers": [    {      "actions": [],      "active": true,      "conditions": {},      "created_at": "2012-09-25T22:50:26Z",      "description": "Close and save a ticket",      "id": 25,      "position": 8,      "raw_title": "Close and Save",      "title": "Close and Save",      "updated_at": "2012-09-25T22:50:26Z",      "url": "http://{subdomain}.zendesk.com/api/v2/triggers/25"    },    {      "actions": [],      "active": true,      "conditions": {        "all": [          {            "field": "status",            "operator": "less_than",            "value": "solved"          },          {            "field": "assignee_id",            "operator": "is",            "value": "296220096"          }        ],        "any": [          {            "field": "status",            "operator": "less_than",            "value": "solved"          }        ]      },      "created_at": "2012-09-25T22:50:26Z",      "description": "Assign a ticket with a priority tag",      "id": 26,      "position": 9,      "raw_title": "{{dc.assign_priority_tag}}",      "title": "Assign priority tag",      "updated_at": "2012-09-25T22:50:26Z",      "url": "http://{subdomain}.zendesk.com/api/v2/triggers/26"    }  ]}

### Search Ticket Triggers

  * `GET /api/v2/triggers/search`


#### Pagination

  * Offset pagination only


See [Using Offset Pagination](/api-reference/introduction/pagination/#using-offset-pagination).

#### Allowed For

  * Agents


#### Sideloads

The following sideloads are supported. For more information, see [Side-loading](/documentation/ticketing/using-the-zendesk-api/side_loading/).

Name| Will sideload
---|---
app_installation| The app installation that requires each ticket trigger, if present
permissions| The permissions for each ticket trigger
usage_1h| The number of times each ticket trigger has been used in the past hour
usage_24h| The number of times each ticket trigger has been used in the past day
usage_7d| The number of times each ticket trigger has been used in the past week
usage_30d| The number of times each ticket trigger has been used in the past thirty days

#### Filter

Use the `filter` query parameter to filter a ticket trigger search by one or more attributes. For example, the following `filter` argument filters ticket triggers by the `description` attribute:


    {  "json": {    "description": "Close a ticket"  }}

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
active| boolean| Query| false| Filter by active triggers if true or inactive triggers if false
filter| string| Query| false| JSON-encoded trigger attribute filters for the search. See Filter. Example: `{"json":{"description":"Close a ticket"}}`
include| string| Query| false| A sideload to include in the response. See Sideloads
query| string| Query| false| Query string used to find all triggers with matching title
sort| string| Query| false| Cursor-based pagination only. Possible values are "alphabetical", "created_at", "updated_at", or "position".
sort_by| string| Query| false| Offset pagination only. Possible values are "alphabetical", "created_at", "updated_at", "usage_1h", "usage_24h", or "usage_7d". Defaults to "position"
sort_order| string| Query| false| One of "asc" or "desc". Defaults to "asc" for alphabetical and position sort, "desc" for all others

#### Code Samples

**curl**


    # With `query`:curl https://{subdomain}.zendesk.com/api/v2/triggers/search?query=close \  -v -u {email_address}/token:{api_token}
    # With `filter`:curl https://{subdomain}.zendesk.com/api/v2/triggers/search \  -G --data-urlencode 'filter={"json":{"description":"Close a ticket"}}' \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/triggers/search?active=true&filter=%7B%5C%22json%5C%22%3A%7B%5C%22description%5C%22%3A%5C%22Close+a+ticket%5C%22%7D%7D&include=usage_24h&query=important_trigger&sort=position&sort_by=position&sort_order=desc"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/triggers/search")		.newBuilder()		.addQueryParameter("active", "true")		.addQueryParameter("filter", "{\"json\":{\"description\":\"Close a ticket\"}}")		.addQueryParameter("include", "usage_24h")		.addQueryParameter("query", "important_trigger")		.addQueryParameter("sort", "position")		.addQueryParameter("sort_by", "position")		.addQueryParameter("sort_order", "desc");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/triggers/search',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'active': 'true',    'filter': '%7B%5C%22json%5C%22%3A%7B%5C%22description%5C%22%3A%5C%22Close+a+ticket%5C%22%7D%7D',    'include': 'usage_24h',    'query': 'important_trigger',    'sort': 'position',    'sort_by': 'position',    'sort_order': 'desc',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/triggers/search?active=true&filter=%7B%5C%22json%5C%22%3A%7B%5C%22description%5C%22%3A%5C%22Close+a+ticket%5C%22%7D%7D&include=usage_24h&query=important_trigger&sort=position&sort_by=position&sort_order=desc"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/triggers/search")uri.query = URI.encode_www_form("active": "true", "filter": "{\"json\":{\"description\":\"Close a ticket\"}}", "include": "usage_24h", "query": "important_trigger", "sort": "position", "sort_by": "position", "sort_order": "desc")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "count": 2,  "next_page": null,  "previous_page": null,  "triggers": [    {      "actions": [],      "active": true,      "conditions": {        "all": [          {            "field": "status",            "operator": "less_than",            "value": "solved"          },          {            "field": "assignee_id",            "operator": "is",            "value": "296220096"          }        ],        "any": [          {            "field": "status",            "operator": "less_than",            "value": "solved"          }        ]      },      "created_at": "2012-09-25T22:50:26Z",      "description": "Close and save a ticket",      "id": 25,      "position": 9,      "raw_title": "Close and Save",      "title": "Close and Save",      "updated_at": "2012-09-25T22:50:26Z"    },    {      "actions": [],      "active": true,      "conditions": {},      "created_at": "2012-09-25T22:50:26Z",      "id": 28,      "position": 9,      "raw_title": "{{dc.close_and_redirect}}",      "title": "Close and redirect to topics",      "updated_at": "2012-09-25T22:50:26Z"    }  ]}

### Show Ticket Trigger

  * `GET /api/v2/triggers/{trigger_id}`


#### Allowed For

  * Agents


The Via Type value is a number instead of a text string. See [Via types reference](/documentation/ticketing/reference-guides/via-types/) for the keys.

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
trigger_id| integer| Path| true| The ID of the trigger

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/triggers/{trigger_id} \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/triggers/198"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/triggers/198")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/triggers/198',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/triggers/198"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/triggers/198")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "trigger": {    "actions": [],    "active": true,    "category_id": "10026",    "conditions": {},    "created_at": "2012-09-25T22:50:26Z",    "description": "Close and save a ticket",    "id": 25,    "position": 8,    "raw_title": "Close and Save",    "title": "Close and Save",    "updated_at": "2012-09-25T22:50:26Z",    "url": "http://{subdomain}.zendesk.com/api/v2/triggers/25"  }}

### List Ticket Trigger Action and Condition Definitions

  * `GET /api/v2/triggers/definitions`


Returns the definitions of the actions a ticket trigger can perform and the definitions of the conditions under which a ticket trigger can execute. The definition of the action includes a title ("Status"), a type ("list"), and possible values. The definition of the condition includes the same fields as well as the possible operators.

For a list of supported actions, see the [Actions reference](/documentation/ticketing/reference-guides/actions-reference) For a list of supported conditions, see the [Conditions reference](/documentation/ticketing/reference-guides/conditions-reference)

#### Allowed For

  * Agents


#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/triggers/definitions \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/triggers/definitions"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/triggers/definitions")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/triggers/definitions',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/triggers/definitions"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/triggers/definitions")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "definitions": {    "actions": [      {        "group": "ticket",        "nullable": false,        "repeatable": false,        "subject": "status",        "title": "Status",        "type": "list",        "values": [          {            "enabled": true,            "title": "Open",            "value": "open"          },          {            "enabled": true,            "title": "Pending",            "value": "pending"          },          {            "enabled": true,            "title": "Solved",            "value": "solved"          },          {            "enabled": true,            "title": "Closed",            "value": "closed"          }        ]      }    ],    "conditions_all": [      {        "group": "ticket",        "nullable": false,        "operators": [          {            "terminal": false,            "title": "Is",            "value": "is"          },          {            "terminal": false,            "title": "Is not",            "value": "is_not"          },          {            "terminal": false,            "title": "Less than",            "value": "less_than"          },          {            "terminal": false,            "title": "Greater than",            "value": "greater_than"          },          {            "terminal": true,            "title": "Changed",            "value": "changed"          },          {            "terminal": false,            "title": "Changed to",            "value": "value"          },          {            "terminal": false,            "title": "Changed from",            "value": "value_previous"          },          {            "terminal": true,            "title": "Not changed",            "value": "not_changed"          },          {            "terminal": false,            "title": "Not changed to",            "value": "not_value"          },          {            "terminal": false,            "title": "Not changed from",            "value": "not_value_previous"          }        ],        "repeatable": false,        "subject": "status",        "title": "Status",        "type": "list",        "values": [          {            "enabled": true,            "title": "New",            "value": "new"          },          {            "enabled": true,            "title": "Open",            "value": "open"          },          {            "enabled": true,            "title": "Pending",            "value": "pending"          },          {            "enabled": true,            "title": "Solved",            "value": "solved"          },          {            "enabled": true,            "title": "Closed",            "value": "closed"          }        ]      }    ],    "conditions_any": [      {        "group": "ticket",        "nullable": true,        "operators": [          {            "terminal": true,            "title": "Present",            "value": "present"          },          {            "terminal": true,            "title": "Not present",            "value": "not_present"          }        ],        "repeatable": false,        "subject": "custom_fields_20513432",        "title": "Happy Gilmore",        "type": "list"      },      {        "group": "ticket",        "nullable": true,        "operators": [          {            "terminal": true,            "title": "Present",            "value": "present"          },          {            "terminal": true,            "title": "Not present",            "value": "not_present"          }        ],        "repeatable": false,        "subject": "custom_fields_86492341",        "title": "total_time_field",        "type": "list"      }    ]  }}

### List Ticket Trigger Revisions

  * `GET /api/v2/triggers/{trigger_id}/revisions`


List the revisions associated with a ticket trigger. Ticket trigger revision history is only available on Enterprise plans.

#### Allowed For

  * Agents


#### Sideloads

The following sideloads are supported:

Name| Will sideload
---|---
users| The user that authored each revision

#### Pagination

This endpoint uses cursor-based pagination. The records are ordered in descending order by the `created_at` timestamp, then by `id` on duplicate `created_at` values.

The `cursor` parameter is a non-human-readable argument you can use to move forward or backward in time.

Each JSON response will contain the following attributes to help you get more results:

  * `after_url` requests more recent results
  * `before_url` requests older results
  * `after_cursor` is the cursor to build the request yourself
  * `before_cursor` is the cursor to build the request yourself


The properties are null if no more records are available.

You can request a maximum of 1000 records using the `limit` parameter. If no `limit` parameter is supplied, it will default to 1,000.

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
trigger_id| integer| Path| true| The ID of the trigger

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/triggers/{trigger_id}/revisions?limit=20 \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/triggers/198/revisions"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/triggers/198/revisions")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/triggers/198/revisions',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/triggers/198/revisions"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/triggers/198/revisions")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "after_cursor": "MTUwMTYwNzUyMi4wfHwxMzQ3NTMxNjcxfA==",  "after_url": "https://{subdomain}.zendesk.com/api/v2/triggers/{trigger_id}/revisions?cursor=MTUwMTYwNzUyMi4wfHwxMzQ3NTMxNjcxfA%3D%3D&limit=20",  "before_cursor": "fDE1MDE1NzUxMjIuMHx8MTM0NzM0MzAxMQ==",  "before_url": "https://{subdomain}.zendesk.com/api/v2/triggers/{trigger_id}/revisions?cursor=fDE1MDE1NzUxMjIuMHx8MTM0NzM0MzAxMQ%3D%3D&limit=20",  "count": 1,  "trigger_revisions": [    {      "author_id": 2,      "created_at": "2016-08-15T16:04:06Z",      "diff": {        "actions": [],        "active": [],        "conditions": {},        "description": [],        "source_id": 1,        "target_id": 2,        "title": []      },      "id": 100,      "snapshot": {        "actions": [          {            "field": "notification_target",            "value": [              "510312",              "{}"            ]          }        ],        "active": true,        "conditions": {          "all": [],          "any": [            {              "field": "current_tags",              "operator": "includes",              "value": "fire_bulk_1"            }          ]        },        "description": "Notifies requester that a comment was updated",        "title": "Notify requester of comment update"      },      "url": "https://{subdomain}.zendesk.com/api/v2/trigger/123/revisions/100"    }  ]}

### Show Ticket Trigger Revision

  * `GET /api/v2/triggers/{trigger_id}/revisions/{trigger_revision_id}`


Fetches a revision associated with a ticket trigger. Ticket trigger revision history is only available on Enterprise plans.

#### Allowed For

  * Agents


#### Sideloads

The following sideloads are supported:

Name| Will sideload
---|---
users| The user that authored each revision

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
trigger_id| integer| Path| true| The ID of the trigger
trigger_revision_id| integer| Path| true| The ID of the revision for a particular trigger

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/triggers/{trigger_id}/revisions/{trigger_revision_id} \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/triggers/198/revisions/1"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/triggers/198/revisions/1")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/triggers/198/revisions/1',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/triggers/198/revisions/1"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/triggers/198/revisions/1")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "trigger_revision": {    "author_id": 3343,    "created_at": "2020-05-28T06:41:43Z",    "id": 1,    "snapshot": {      "actions": [        {          "field": "notification_target",          "value": [            "510312",            "{}"          ]        }      ],      "active": true,      "conditions": {        "all": [],        "any": [          {            "field": "current_tags",            "operator": "includes",            "value": "fire_bulk_1"          }        ]      },      "description": null,      "title": "bulk_test_trigger_1"    },    "url": "https://example.zendesk.com/api/v2/triggers/261303831/revisions/1"  }}

### Create Trigger

  * `POST /api/v2/triggers`


#### Allowed For

  * Agents


#### Example body


    {  "trigger": {    "actions": [      {        "field": "group_id",        "value": "20455932"      }    ],    "category_id": "10026",    "conditions": {      "all": [        {          "field": "status",          "operator": "is",          "value": "open"        },        {          "field": "priority",          "operator": "less_than",          "value": "high"        }      ]    },    "title": "Roger Wilco"  }}

#### Code Samples

**curl**


    curl -u {email_address}/token:{api_token} https://{subdomain}.zendesk.com/api/v2/triggers \  -H "Content-Type: application/json" -X POST -d \  '{"trigger": {"title": "Roger Wilco", "conditions": {"all": [{ "field": "status", \  "operator": "is", "value": "open" }, { "field": "priority", \  "operator": "less_than", "value": "high" }]}, \  "actions": [{ "field": "group_id", "value": "20455932" }],  "category_id": "10026"}}'

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://example.zendesk.com/api/v2/triggers"	method := "POST"	payload := strings.NewReader(`{  "trigger": {    "actions": [      {        "field": "group_id",        "value": "20455932"      }    ],    "category_id": "10026",    "conditions": {      "all": [        {          "field": "status",          "operator": "is",          "value": "open"        },        {          "field": "priority",          "operator": "less_than",          "value": "high"        }      ]    },    "title": "Roger Wilco"  }}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/triggers")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"trigger\": {    \"actions\": [      {        \"field\": \"group_id\",        \"value\": \"20455932\"      }    ],    \"category_id\": \"10026\",    \"conditions\": {      \"all\": [        {          \"field\": \"status\",          \"operator\": \"is\",          \"value\": \"open\"        },        {          \"field\": \"priority\",          \"operator\": \"less_than\",          \"value\": \"high\"        }      ]    },    \"title\": \"Roger Wilco\"  }}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "trigger": {    "actions": [      {        "field": "group_id",        "value": "20455932"      }    ],    "category_id": "10026",    "conditions": {      "all": [        {          "field": "status",          "operator": "is",          "value": "open"        },        {          "field": "priority",          "operator": "less_than",          "value": "high"        }      ]    },    "title": "Roger Wilco"  }});
    var config = {  method: 'POST',  url: 'https://example.zendesk.com/api/v2/triggers',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/triggers"
    payload = json.loads("""{  "trigger": {    "actions": [      {        "field": "group_id",        "value": "20455932"      }    ],    "category_id": "10026",    "conditions": {      "all": [        {          "field": "status",          "operator": "is",          "value": "open"        },        {          "field": "priority",          "operator": "less_than",          "value": "high"        }      ]    },    "title": "Roger Wilco"  }}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/triggers")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")request.body = %q({  "trigger": {    "actions": [      {        "field": "group_id",        "value": "20455932"      }    ],    "category_id": "10026",    "conditions": {      "all": [        {          "field": "status",          "operator": "is",          "value": "open"        },        {          "field": "priority",          "operator": "less_than",          "value": "high"        }      ]    },    "title": "Roger Wilco"  }})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**201 Created**


    // Status 201 Created
    {  "trigger": {    "actions": [],    "active": true,    "category_id": "10026",    "conditions": {},    "created_at": "2012-09-25T22:50:26Z",    "description": "Close and save a ticket",    "id": 25,    "position": 8,    "raw_title": "Close and Save",    "title": "Close and Save",    "updated_at": "2012-09-25T22:50:26Z",    "url": "http://{subdomain}.zendesk.com/api/v2/triggers/25"  }}

### Update Ticket Trigger

  * `PUT /api/v2/triggers/{trigger_id}`


#### Allowed For

  * Agents


#### Note

Updating a condition or action updates both the conditions and actions arrays, clearing all existing values of both arrays. Include all your conditions and actions when updating any condition or action.

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
trigger_id| integer| Path| true| The ID of the trigger

#### Example body


    {  "trigger": {    "actions": [      {        "field": "group_id",        "value": "20455932"      }    ],    "category_id": "10026",    "conditions": {      "all": [        {          "field": "status",          "operator": "is",          "value": "open"        },        {          "field": "priority",          "operator": "less_than",          "value": "high"        }      ]    },    "title": "Roger Wilco"  }}

#### Code Samples

**curl**


    curl -v -u {email_address}/token:{api_token} https://{subdomain}.zendesk.com/api/v2/triggers/{trigger_id} \  -H "Content-Type: application/json" -X PUT -d '{"trigger": {"title": "Roger Wilco II", "category_id": "10026"}}'

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://example.zendesk.com/api/v2/triggers/198"	method := "PUT"	payload := strings.NewReader(`{  "trigger": {    "actions": [      {        "field": "group_id",        "value": "20455932"      }    ],    "category_id": "10026",    "conditions": {      "all": [        {          "field": "status",          "operator": "is",          "value": "open"        },        {          "field": "priority",          "operator": "less_than",          "value": "high"        }      ]    },    "title": "Roger Wilco"  }}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/triggers/198")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"trigger\": {    \"actions\": [      {        \"field\": \"group_id\",        \"value\": \"20455932\"      }    ],    \"category_id\": \"10026\",    \"conditions\": {      \"all\": [        {          \"field\": \"status\",          \"operator\": \"is\",          \"value\": \"open\"        },        {          \"field\": \"priority\",          \"operator\": \"less_than\",          \"value\": \"high\"        }      ]    },    \"title\": \"Roger Wilco\"  }}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "trigger": {    "actions": [      {        "field": "group_id",        "value": "20455932"      }    ],    "category_id": "10026",    "conditions": {      "all": [        {          "field": "status",          "operator": "is",          "value": "open"        },        {          "field": "priority",          "operator": "less_than",          "value": "high"        }      ]    },    "title": "Roger Wilco"  }});
    var config = {  method: 'PUT',  url: 'https://example.zendesk.com/api/v2/triggers/198',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/triggers/198"
    payload = json.loads("""{  "trigger": {    "actions": [      {        "field": "group_id",        "value": "20455932"      }    ],    "category_id": "10026",    "conditions": {      "all": [        {          "field": "status",          "operator": "is",          "value": "open"        },        {          "field": "priority",          "operator": "less_than",          "value": "high"        }      ]    },    "title": "Roger Wilco"  }}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/triggers/198")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")request.body = %q({  "trigger": {    "actions": [      {        "field": "group_id",        "value": "20455932"      }    ],    "category_id": "10026",    "conditions": {      "all": [        {          "field": "status",          "operator": "is",          "value": "open"        },        {          "field": "priority",          "operator": "less_than",          "value": "high"        }      ]    },    "title": "Roger Wilco"  }})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "trigger": {    "actions": [],    "active": true,    "category_id": "10026",    "conditions": {},    "created_at": "2012-09-25T22:50:26Z",    "description": "Close and save a ticket",    "id": 25,    "position": 8,    "raw_title": "Close and Save",    "title": "Close and Save",    "updated_at": "2012-09-25T22:50:26Z",    "url": "http://{subdomain}.zendesk.com/api/v2/triggers/25"  }}

### Update Many Ticket Triggers

  * `PUT /api/v2/triggers/update_many`


Updates the position or the active status of multiple ticket triggers. Any additional properties are ignored.

#### Allowed For

  * Agents


#### Request Parameters

The PUT request expects a `triggers` object that lists the ticket triggers to update.

Each ticket trigger may have the following properties:

Name| Mandatory| Description
---|---|---
id| yes| The ID of the ticket trigger to update
position| no| The new position of the ticket trigger
active| no| The active status of the ticket trigger (true or false)
category_id| no| The ID of the new category the ticket trigger is to be moved to

#### Example Request


    {  "triggers": [    {"id": 25, "position": 3},    {"id": 23, "position": 5},    {"id": 27, "position": 9},    {"id": 22, "position": 7}  ]}

#### Example body


    {  "triggers": [    {      "id": 25,      "position": 5    },    {      "active": false,      "id": 26    },    {      "category_id": "10027",      "id": 27    }  ]}

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/triggers/update_many \  -v -u {email_address}/token:{api_token} -H "Content-Type: application/json" \  -X PUT -d '{"triggers": [{"id": 26, "position": 8}, {"id": 25, "position": 15}]}'

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://example.zendesk.com/api/v2/triggers/update_many"	method := "PUT"	payload := strings.NewReader(`{  "triggers": [    {      "id": 25,      "position": 5    },    {      "active": false,      "id": 26    },    {      "category_id": "10027",      "id": 27    }  ]}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/triggers/update_many")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"triggers\": [    {      \"id\": 25,      \"position\": 5    },    {      \"active\": false,      \"id\": 26    },    {      \"category_id\": \"10027\",      \"id\": 27    }  ]}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "triggers": [    {      "id": 25,      "position": 5    },    {      "active": false,      "id": 26    },    {      "category_id": "10027",      "id": 27    }  ]});
    var config = {  method: 'PUT',  url: 'https://example.zendesk.com/api/v2/triggers/update_many',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/triggers/update_many"
    payload = json.loads("""{  "triggers": [    {      "id": 25,      "position": 5    },    {      "active": false,      "id": 26    },    {      "category_id": "10027",      "id": 27    }  ]}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/triggers/update_many")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")request.body = %q({  "triggers": [    {      "id": 25,      "position": 5    },    {      "active": false,      "id": 26    },    {      "category_id": "10027",      "id": 27    }  ]})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "count": 2,  "next_page": null,  "previous_page": null,  "triggers": [    {      "actions": [],      "active": true,      "conditions": {},      "created_at": "2012-09-25T22:50:26Z",      "description": "Close and save a ticket",      "id": 25,      "position": 8,      "raw_title": "Close and Save",      "title": "Close and Save",      "updated_at": "2012-09-25T22:50:26Z",      "url": "http://{subdomain}.zendesk.com/api/v2/triggers/25"    },    {      "actions": [],      "active": false,      "conditions": {        "all": [          {            "field": "status",            "operator": "less_than",            "value": "solved"          },          {            "field": "assignee_id",            "operator": "is",            "value": "296220096"          }        ],        "any": [          {            "field": "status",            "operator": "less_than",            "value": "solved"          },          {            "field": "custom_status_id",            "operator": "includes",            "value": [              "1",              "2"            ]          }        ]      },      "created_at": "2012-09-25T22:50:26Z",      "description": "Assign a ticket with a priority tag",      "id": 26,      "position": 9,      "raw_title": "{{dc.assign_priority_tag}}",      "title": "Assign priority tag",      "updated_at": "2012-09-25T22:50:26Z",      "url": "http://{subdomain}.zendesk.com/api/v2/triggers/26"    }  ]}

### Reorder Ticket Triggers

  * `PUT /api/v2/triggers/reorder`


Alters the firing order of ticket triggers in the account. See [Reordering and sorting triggers](https://support.zendesk.com/hc/en-us/articles/115015696088) in the Zendesk Help Center. The firing order is set in a `trigger_ids` array in the request body.

You must include every ticket trigger id in your account to reorder the ticket triggers. If not, the endpoint will return 404 Forbidden.

Reordering ticket triggers via the API is not permitted if you have more than one ticket trigger category. If there is more than one ticket trigger category, the endpoint will return a `LimitOneCategory` error.

#### Allowed For

  * Agents


#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/triggers/reorder \  -d '{"trigger_ids": [324376, 564937, 164318]}' \  -H "Content-Type: application/json" -X PUT \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/triggers/reorder"	method := "PUT"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/triggers/reorder")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'PUT',  url: 'https://example.zendesk.com/api/v2/triggers/reorder',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/triggers/reorder"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/triggers/reorder")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "trigger": {    "actions": [],    "active": true,    "category_id": "10026",    "conditions": {},    "created_at": "2012-09-25T22:50:26Z",    "description": "Close and save a ticket",    "id": 25,    "position": 8,    "raw_title": "Close and Save",    "title": "Close and Save",    "updated_at": "2012-09-25T22:50:26Z",    "url": "http://{subdomain}.zendesk.com/api/v2/triggers/25"  }}

### Delete Ticket Trigger

  * `DELETE /api/v2/triggers/{trigger_id}`


#### Allowed For

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
trigger_id| integer| Path| true| The ID of the trigger

#### Code Samples

**curl**


    curl -v -u {email_address}/token:{api_token} https://{subdomain}.zendesk.com/api/v2/triggers/{trigger_id} \  -H "Content-Type: application/json" -X DELETE

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/triggers/198"	method := "DELETE"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/triggers/198")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("DELETE", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'DELETE',  url: 'https://example.zendesk.com/api/v2/triggers/198',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/triggers/198"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"DELETE",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/triggers/198")request = Net::HTTP::Delete.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**204 No Content**


    // Status 204 No Content
    null

### Bulk Delete Ticket Triggers

  * `DELETE /api/v2/triggers/destroy_many?ids={ids}`


Deletes the ticket triggers corresponding to the provided comma-separated list of IDs.

#### Allowed For

  * Agents


#### Request Parameters

The DELETE request takes one parameter, an `ids` object that lists the ticket triggers to delete.

Name| Description
---|---
ids| The IDs of the triggers to delete

#### Example request


    {  "ids": "25,23,27,22"}

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
ids| string| Query| true| A comma separated list of trigger IDs

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/triggers/destroy_many?ids=1,2,3 \  -v -u {email_address}/token:{api_token} -X DELETE

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/triggers/destroy_many?ids=131%2C178%2C938"	method := "DELETE"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/triggers/destroy_many")		.newBuilder()		.addQueryParameter("ids", "131,178,938");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("DELETE", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'DELETE',  url: 'https://example.zendesk.com/api/v2/triggers/destroy_many',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'ids': '131%2C178%2C938',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/triggers/destroy_many?ids=131%2C178%2C938"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"DELETE",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/triggers/destroy_many")uri.query = URI.encode_www_form("ids": "131,178,938")request = Net::HTTP::Delete.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**204 No Content**


    // Status 204 No Content
    null

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)