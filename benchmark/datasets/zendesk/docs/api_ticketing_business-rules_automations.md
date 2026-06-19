# Automations

*Source: https://developer.zendesk.com/api-reference/ticketing/business-rules/automations/*

---

## On this page

  * [JSON format](/api-reference/ticketing/business-rules/automations/#json-format)
  * [List Automations](/api-reference/ticketing/business-rules/automations/#list-automations)
  * [List Active Automations](/api-reference/ticketing/business-rules/automations/#list-active-automations)
  * [Search Automations](/api-reference/ticketing/business-rules/automations/#search-automations)
  * [Show Automation](/api-reference/ticketing/business-rules/automations/#show-automation)
  * [Create Automation](/api-reference/ticketing/business-rules/automations/#create-automation)
  * [Update Automation](/api-reference/ticketing/business-rules/automations/#update-automation)
  * [Update Many Automations](/api-reference/ticketing/business-rules/automations/#update-many-automations)
  * [Delete Automation](/api-reference/ticketing/business-rules/automations/#delete-automation)
  * [Bulk Delete Automations](/api-reference/ticketing/business-rules/automations/#bulk-delete-automations)


# Automations

## On this page

  * [JSON format](/api-reference/ticketing/business-rules/automations/#json-format)
  * [List Automations](/api-reference/ticketing/business-rules/automations/#list-automations)
  * [List Active Automations](/api-reference/ticketing/business-rules/automations/#list-active-automations)
  * [Search Automations](/api-reference/ticketing/business-rules/automations/#search-automations)
  * [Show Automation](/api-reference/ticketing/business-rules/automations/#show-automation)
  * [Create Automation](/api-reference/ticketing/business-rules/automations/#create-automation)
  * [Update Automation](/api-reference/ticketing/business-rules/automations/#update-automation)
  * [Update Many Automations](/api-reference/ticketing/business-rules/automations/#update-many-automations)
  * [Delete Automation](/api-reference/ticketing/business-rules/automations/#delete-automation)
  * [Bulk Delete Automations](/api-reference/ticketing/business-rules/automations/#bulk-delete-automations)


An automation consists of one or more actions that are performed if certain conditions are met after a period of time. The conditions are checked every hour. For example, an automation can notify an agent when a ticket remains unresolved after 24 hours.

Even if the actions are performed once, they'll be performed again later if the conditions still apply. To ensure the actions are performed only once, include an action in the automation that cancels one of the conditions.

For more information, see [Creating and managing automations for time-based events](https://support.zendesk.com/hc/en-us/articles/203662126).

### JSON format

Automations are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
actions| array| false| false| An object describing what the automation will do. See [Actions reference](/documentation/ticketing/reference-guides/actions-reference)
active| boolean| false| false| Whether the automation is active
conditions| object| false| false| An object that describes the conditions under which the automation will execute. See [Conditions reference](/documentation/ticketing/reference-guides/conditions-reference)
created_at| string| true| false| The time the automation was created
default| boolean| true| false| If true, the automation is a default automation
id| integer| true| false| Automatically assigned when created
position| integer| false| false| The position of the automation which specifies the order it will be executed
raw_title| string| true| false| The raw title of the automation
title| string| false| false| The title of the automation
updated_at| string| true| false| The time of the last update of the automation

#### Example


    {  "actions": [    {      "field": "priority",      "value": "high"    }  ],  "active": true,  "conditions": {    "all": [      {        "field": "status",        "operator": "is",        "value": "open"      },      {        "field": "priority",        "operator": "less_than",        "value": "high"      }    ],    "any": []  },  "default": false,  "id": 9873843,  "position": 8,  "raw_title": "Roger Wilco",  "title": "Roger Wilco"}

### List Automations

  * `GET /api/v2/automations`


Lists all automations for the current account.

#### Allowed For

  * Agents


#### Available Parameters

You can pass in any combination of the following optional filters:

Name| Type| Comment
---|---|---
active| boolean| Only active automations if true, inactive automations if false
sort_by| string| Possible values are "alphabetical", "created_at", "updated_at", "usage_1h", "usage_24h", or "usage_7d". Defaults to "position"
sort_order| string| One of "asc" or "desc". Defaults to "asc" for alphabetical and position sort, "desc" for all others

#### Sideloads

The following sideloads are supported. The usage sideloads are only supported on the Support Professional or Suite Growth plan or above.

Name| Will sideload
---|---
app_installation| The app installation that requires each automation, if present
permissions| The permissions for each automation
usage_1h| The number of tickets processed by an automation in the past hour
usage_24h| The number of tickets processed by an automation in the past day
usage_7d| The number of tickets processed by an automation in the past week
usage_30d| The number of tickets processed by an automation in the past thirty days

#### Pagination

  * Cursor pagination (recommended)
  * Offset pagination


See [Pagination](/api-reference/introduction/pagination/).

Returns a maximum of 100 records per page.

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
active| boolean| Query| false| Filter by active automations if true or inactive automations if false
include| string| Query| false| A sideload to include in the response. See Sideloads
page| | Query| false| Pagination parameter. Supports both traditional offset and cursor-based pagination: - Traditional: `?page=2` (integer page number) - Cursor: `?page[size]=50&page[after]=cursor` (deepObject with size, after, before) These are mutually exclusive - use one format or the other, not both.
per_page| integer| Query| false| Number of records to return per page. Note: Default and maximum values vary by endpoint. Check endpoint-specific documentation for limits.
sort| string| Query| false| Field to sort results by. Prefix with `-` for descending order. When used with cursor pagination, this determines the cursor ordering. Example: `?sort=name` or `?sort=-created_at`

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/automations \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/automations?active=true&include=usage_24h&page=&per_page=50&sort=name"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/automations")		.newBuilder()		.addQueryParameter("active", "true")		.addQueryParameter("include", "usage_24h")		.addQueryParameter("page", "")		.addQueryParameter("per_page", "50")		.addQueryParameter("sort", "name");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/automations',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'active': 'true',    'include': 'usage_24h',    'page': '',    'per_page': '50',    'sort': 'name',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/automations?active=true&include=usage_24h&page=&per_page=50&sort=name"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/automations")uri.query = URI.encode_www_form("active": "true", "include": "usage_24h", "page": "", "per_page": "50", "sort": "name")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "automations": [    {      "actions": [        {          "field": "status",          "value": "open"        },        {          "field": "assignee_id",          "value": "296220096"        }      ],      "active": true,      "conditions": {        "all": [          {            "field": "status",            "operator": "less_than",            "value": "solved"          },          {            "field": "assignee_id",            "operator": "is",            "value": "296220096"          }        ],        "any": [          {            "field": "current_tags",            "operator": "includes",            "value": "hello"          }        ]      },      "id": 25,      "position": 8,      "raw_title": "Close and Save",      "title": "Close and Save"    },    {      "actions": [        {          "field": "status",          "value": "open"        },        {          "field": "assignee_id",          "value": "296220096"        }      ],      "active": false,      "conditions": {        "all": [          {            "field": "status",            "operator": "less_than",            "value": "solved"          },          {            "field": "assignee_id",            "operator": "is",            "value": "296220096"          }        ],        "any": [          {            "field": "current_tags",            "operator": "includes",            "value": "hello"          }        ]      },      "id": 26,      "position": 9,      "raw_title": "{{dc.assign_priority_tag}}",      "title": "Assign priority tag"    }  ],  "count": 2,  "next_page": null,  "previous_page": null}

### List Active Automations

  * `GET /api/v2/automations/active`


Lists all active automations.

#### Allowed For

  * Agents


#### Available Parameters

You can pass in any combination of the following optional filters:

Name| Type| Comment
---|---|---
sort_by| string| Possible values are "alphabetical", "created_at", "updated_at", "usage_1h", "usage_24h", or "usage_7d". Defaults to "position"
sort_order| string| One of "asc" or "desc". Defaults to "asc" for alphabetical and position sort, "desc" for all others

#### Sideloads

The following sideloads are supported:

Name| Will sideload
---|---
app_installation| The app installation that requires each automation, if present
permissions| The permissions for each automation
usage_1h| The number of tickets processed by an automation in the past hour
usage_24h| The number of tickets processed by an automation in the past day
usage_7d| The number of tickets processed by an automation in the past week
usage_30d| The number of tickets processed by an automation in the past thirty days

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/automations/active \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/automations/active"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/automations/active")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/automations/active',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/automations/active"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/automations/active")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "automations": [    {      "actions": [        {          "field": "status",          "value": "open"        },        {          "field": "assignee_id",          "value": "296220096"        }      ],      "active": true,      "conditions": {        "all": [          {            "field": "status",            "operator": "less_than",            "value": "solved"          },          {            "field": "assignee_id",            "operator": "is",            "value": "296220096"          }        ],        "any": [          {            "field": "current_tags",            "operator": "includes",            "value": "hello"          }        ]      },      "id": 25,      "position": 8,      "raw_title": "Close and Save",      "title": "Close and Save"    },    {      "actions": [        {          "field": "status",          "value": "open"        },        {          "field": "assignee_id",          "value": "296220096"        }      ],      "active": false,      "conditions": {        "all": [          {            "field": "status",            "operator": "less_than",            "value": "solved"          },          {            "field": "assignee_id",            "operator": "is",            "value": "296220096"          }        ],        "any": [          {            "field": "current_tags",            "operator": "includes",            "value": "hello"          }        ]      },      "id": 26,      "position": 9,      "raw_title": "{{dc.assign_priority_tag}}",      "title": "Assign priority tag"    }  ],  "count": 2,  "next_page": null,  "previous_page": null}

### Search Automations

  * `GET /api/v2/automations/search?query={query}`


#### Pagination

  * Offset pagination only


See [Using Offset Pagination](/api-reference/introduction/pagination/#using-offset-pagination).

#### Allowed For

  * Agents


#### Sideloads

The following sideloads are supported. For more information, see [Side-loading](/documentation/ticketing/using-the-zendesk-api/side_loading/).

Name| Will sideload
---|---
app_installation| The app installation that requires each automation, if present
permissions| The permissions for each automation
usage_1h| The number of tickets processed by an automation in the past hour
usage_24h| The number of tickets processed by an automation in the past day
usage_7d| The number of tickets processed by an automation in the past week
usage_30d| The number of tickets processed by an automation in the past thirty days

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
active| boolean| Query| false| Filter by active automations if true or inactive automations if false
include| string| Query| false| A sideload to include in the response. See Sideloads
query| string| Query| true| Query string used to find all automations with matching title
sort_by| string| Query| false| Possible values are "alphabetical", "created_at", "updated_at", and "position". If unspecified, the automations are sorted by relevance
sort_order| string| Query| false| One of "asc" or "desc". Defaults to "asc" for alphabetical and position sort, "desc" for all others

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/automations/search?query=close \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/automations/search?active=true&include=usage_24h&query=close&sort_by=position&sort_order=desc"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/automations/search")		.newBuilder()		.addQueryParameter("active", "true")		.addQueryParameter("include", "usage_24h")		.addQueryParameter("query", "close")		.addQueryParameter("sort_by", "position")		.addQueryParameter("sort_order", "desc");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/automations/search',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'active': 'true',    'include': 'usage_24h',    'query': 'close',    'sort_by': 'position',    'sort_order': 'desc',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/automations/search?active=true&include=usage_24h&query=close&sort_by=position&sort_order=desc"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/automations/search")uri.query = URI.encode_www_form("active": "true", "include": "usage_24h", "query": "close", "sort_by": "position", "sort_order": "desc")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "automations": [    {      "actions": [        {          "field": "status",          "value": "open"        },        {          "field": "assignee_id",          "value": "296220096"        }      ],      "active": true,      "conditions": {        "all": [          {            "field": "status",            "operator": "less_than",            "value": "solved"          },          {            "field": "assignee_id",            "operator": "is",            "value": "296220096"          }        ],        "any": [          {            "field": "current_tags",            "operator": "includes",            "value": "hello"          }        ]      },      "id": 25,      "position": 9,      "raw_title": "Close and Save",      "title": "Close and Save"    },    {      "actions": [        {          "field": "status",          "value": "open"        },        {          "field": "assignee_id",          "value": "296220096"        }      ],      "active": true,      "conditions": {        "all": [          {            "field": "status",            "operator": "less_than",            "value": "solved"          },          {            "field": "assignee_id",            "operator": "is",            "value": "296220096"          }        ],        "any": [          {            "field": "current_tags",            "operator": "includes",            "value": "hello"          }        ]      },      "id": 28,      "position": 9,      "raw_title": "{{dc.close_and_redirect}}",      "title": "Close and redirect to topics"    }  ],  "count": 2,  "next_page": null,  "previous_page": null}

### Show Automation

  * `GET /api/v2/automations/{automation_id}`


#### Allowed For

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
automation_id| integer| Path| true| The ID of the automation

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/automations/{automation_id} \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/automations/25"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/automations/25")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/automations/25',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/automations/25"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/automations/25")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "automation": {    "actions": [      {        "field": "status",        "value": "open"      },      {        "field": "assignee_id",        "value": "296220096"      }    ],    "active": true,    "conditions": {      "all": [        {          "field": "status",          "operator": "less_than",          "value": "solved"        },        {          "field": "assignee_id",          "operator": "is",          "value": "296220096"        }      ],      "any": [        {          "field": "current_tags",          "operator": "includes",          "value": "hello"        }      ]    },    "id": 25,    "position": 8,    "raw_title": "Close and Save",    "title": "Close and Save"  }}

### Create Automation

  * `POST /api/v2/automations`


Creates an automation.

New automations must be unique and have at least one condition that is true only once or an action that nullifies at least one of the conditions. Active automations can have overlapping conditions but can't be identical.

The request must include the following conditions in the `all` array:

  * At least one time-based condition
  * At least one condition that checks one of the following fields: `status`, `type`, `group_id`, `assignee_id`, or `requester_id`.


#### Allowed For

  * Agents


#### Code Samples

**curl**


    curl -u {email_address}/token:{api_token} https://{subdomain}.zendesk.com/api/v2/automations \  -H "Content-Type: application/json" -X POST -d \ '{"automation": {"title": "Roger Wilco", "all": [{ "field": "status", "operator": "is", "value": "open" }, { "field": "priority", "operator": "less_than", "value": "high" }], "actions": [{ "field": "priority", "value": "high" }]}}'

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/automations"	method := "POST"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/automations")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'POST',  url: 'https://example.zendesk.com/api/v2/automations',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/automations"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/automations")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**201 Created**


    // Status 201 Created
    {  "automation": {    "actions": [      {        "field": "priority",        "value": "high"      }    ],    "active": true,    "conditions": {      "all": [        {          "field": "status",          "operator": "is",          "value": "open"        },        {          "field": "priority",          "operator": "less_than",          "value": "high"        }      ],      "any": []    },    "id": 9873843,    "position": 8,    "raw_title": "Roger Wilco",    "title": "Roger Wilco"  }}

### Update Automation

  * `PUT /api/v2/automations/{automation_id}`


Updates an automation.

Updated automations must be unique and have at least one condition that is true only once or an action that nullifies at least one of the conditions. Active automations can have overlapping conditions but can't be identical.

The request must include the following conditions in the `all` array:

  * At least one time-based condition
  * At least one condition that checks one of the following fields: 'status', 'type', 'group_id', 'assignee_id', or 'requester_id'


**Note** : Updating a condition or action updates both the `conditions` and `actions` arrays, clearing all existing values of both arrays. Include all your conditions and actions when updating any condition or action. **Note** : You might be restricted from updating some default automations.

#### Allowed For

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
automation_id| integer| Path| true| The ID of the automation

#### Code Samples

**curl**


    curl -v -u {email_address}/token:{api_token} https://{subdomain}.zendesk.com/api/v2/automations/{automation_id} \  -H "Content-Type: application/json" -X PUT -d '{"automation": {"title": "Roger Wilco II"}}'

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/automations/25"	method := "PUT"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/automations/25")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'PUT',  url: 'https://example.zendesk.com/api/v2/automations/25',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/automations/25"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/automations/25")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "automation": {    "actions": [      {        "field": "status",        "value": "open"      },      {        "field": "assignee_id",        "value": "296220096"      }    ],    "active": true,    "conditions": {      "all": [        {          "field": "status",          "operator": "less_than",          "value": "solved"        },        {          "field": "assignee_id",          "operator": "is",          "value": "296220096"        }      ],      "any": [        {          "field": "current_tags",          "operator": "includes",          "value": "hello"        }      ]    },    "id": 25,    "position": 8,    "raw_title": "Close and Save",    "title": "Close and Save"  }}

### Update Many Automations

  * `PUT /api/v2/automations/update_many`


**Note** : You might be restricted from updating some default automations. If included in a bulk update, the unrestricted automations will be updated.

#### Allowed For

  * Agents


#### Request Parameters

The PUT request expects an `automations` object that lists the automations to update.

Each automation may have the following properties:

Name| Mandatory| Description
---|---|---
id| yes| The ID of the automation to update
position| no| The new position of the automation
active| no| The active status of the automation (true or false)

#### Example Request


    {  "automations": [    {"id": 25, "position": 3},    {"id": 23, "position": 5},    {"id": 27, "position": 9},    {"id": 22, "position": 7}  ]}

#### Code Samples

**curl**


    curl -v -u {email_address}/token:{api_token} https://{subdomain}.zendesk.com/api/v2/automations/update_many \  -H "Content-Type: application/json" -X PUT -d '{"automations": [{"id": 26, "position": 8}, {"id": 25, "position": 15}]}'

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/automations/update_many"	method := "PUT"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/automations/update_many")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'PUT',  url: 'https://example.zendesk.com/api/v2/automations/update_many',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/automations/update_many"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/automations/update_many")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "automations": [    {      "actions": [        {          "field": "status",          "value": "open"        },        {          "field": "assignee_id",          "value": "296220096"        }      ],      "active": true,      "conditions": {        "all": [          {            "field": "status",            "operator": "less_than",            "value": "solved"          },          {            "field": "assignee_id",            "operator": "is",            "value": "296220096"          }        ],        "any": [          {            "field": "current_tags",            "operator": "includes",            "value": "hello"          }        ]      },      "id": 25,      "position": 15,      "raw_title": "Close and Save",      "title": "Close and Save"    },    {      "actions": [        {          "field": "status",          "value": "open"        },        {          "field": "assignee_id",          "value": "296220096"        }      ],      "active": false,      "conditions": {        "all": [          {            "field": "status",            "operator": "less_than",            "value": "solved"          },          {            "field": "assignee_id",            "operator": "is",            "value": "296220096"          }        ],        "any": [          {            "field": "current_tags",            "operator": "includes",            "value": "hello"          }        ]      },      "id": 26,      "position": 8,      "raw_title": "{{dc.assign_priority_tag}}",      "title": "Assign priority tag"    }  ],  "count": 2,  "next_page": null,  "previous_page": null}

### Delete Automation

  * `DELETE /api/v2/automations/{automation_id}`


**Note** : You might be restricted from deleting some default automations.

#### Allowed For

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
automation_id| integer| Path| true| The ID of the automation

#### Code Samples

**curl**


    curl -v -u {email_address}/token:{api_token} https://{subdomain}.zendesk.com/api/v2/automations/{automation_id} \  -H "Content-Type: application/json" -X DELETE

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/automations/25"	method := "DELETE"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/automations/25")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("DELETE", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'DELETE',  url: 'https://example.zendesk.com/api/v2/automations/25',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/automations/25"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"DELETE",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/automations/25")request = Net::HTTP::Delete.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**204 No Content**


    // Status 204 No Content
    null

### Bulk Delete Automations

  * `DELETE /api/v2/automations/destroy_many`


Deletes the automations corresponding to the provided comma-separated list of IDs.

**Note** : You might be restricted from deleting some default automations. If included in a bulk deletion, the unrestricted automations will be deleted.

#### Allowed For

  * Agents


#### Request Parameters

The DELETE request takes one parameter, an `ids` object that lists the automations to delete.

Name| Description
---|---
ids| The IDs of the automations to delete

#### Example request


    {  "ids": "25,23,27,22"}

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
ids| array| Query| false| The IDs of the automations to delete

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/automations/destroy_many?ids=1,2,3 \  -v -u {email_address}/token:{api_token} -X DELETE

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/automations/destroy_many?ids="	method := "DELETE"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/automations/destroy_many")		.newBuilder()		.addQueryParameter("ids", "");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("DELETE", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'DELETE',  url: 'https://example.zendesk.com/api/v2/automations/destroy_many',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'ids': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/automations/destroy_many?ids="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"DELETE",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/automations/destroy_many")uri.query = URI.encode_www_form("ids": "")request = Net::HTTP::Delete.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**204 No Content**


    // Status 204 No Content
    null

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)