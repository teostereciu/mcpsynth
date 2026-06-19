# Macros

*Source: https://developer.zendesk.com/api-reference/ticketing/business-rules/macros/*

---

## On this page

  * [JSON format](/api-reference/ticketing/business-rules/macros/#json-format)
  * [List Macros](/api-reference/ticketing/business-rules/macros/#list-macros)
  * [List Active Macros](/api-reference/ticketing/business-rules/macros/#list-active-macros)
  * [Show Macro](/api-reference/ticketing/business-rules/macros/#show-macro)
  * [Create Macro](/api-reference/ticketing/business-rules/macros/#create-macro)
  * [Update Macro](/api-reference/ticketing/business-rules/macros/#update-macro)
  * [Update Many Macros](/api-reference/ticketing/business-rules/macros/#update-many-macros)
  * [Delete Macro](/api-reference/ticketing/business-rules/macros/#delete-macro)
  * [Bulk Delete Macros](/api-reference/ticketing/business-rules/macros/#bulk-delete-macros)
  * [Search Macros](/api-reference/ticketing/business-rules/macros/#search-macros)
  * [List Macro Categories](/api-reference/ticketing/business-rules/macros/#list-macro-categories)
  * [List Supported Actions for Macros](/api-reference/ticketing/business-rules/macros/#list-supported-actions-for-macros)
  * [List Macro Action Definitions](/api-reference/ticketing/business-rules/macros/#list-macro-action-definitions)
  * [Show Macro Replica](/api-reference/ticketing/business-rules/macros/#show-macro-replica)
  * [List Macro Attachments](/api-reference/ticketing/business-rules/macros/#list-macro-attachments)
  * [Show Macro Attachment](/api-reference/ticketing/business-rules/macros/#show-macro-attachment)
  * [Create Macro Attachment](/api-reference/ticketing/business-rules/macros/#create-macro-attachment)
  * [Create Unassociated Macro Attachment](/api-reference/ticketing/business-rules/macros/#create-unassociated-macro-attachment)
  * [Show Changes to Ticket](/api-reference/ticketing/business-rules/macros/#show-changes-to-ticket)
  * [Show Ticket After Changes](/api-reference/ticketing/business-rules/macros/#show-ticket-after-changes)


# Macros

## On this page

  * [JSON format](/api-reference/ticketing/business-rules/macros/#json-format)
  * [List Macros](/api-reference/ticketing/business-rules/macros/#list-macros)
  * [List Active Macros](/api-reference/ticketing/business-rules/macros/#list-active-macros)
  * [Show Macro](/api-reference/ticketing/business-rules/macros/#show-macro)
  * [Create Macro](/api-reference/ticketing/business-rules/macros/#create-macro)
  * [Update Macro](/api-reference/ticketing/business-rules/macros/#update-macro)
  * [Update Many Macros](/api-reference/ticketing/business-rules/macros/#update-many-macros)
  * [Delete Macro](/api-reference/ticketing/business-rules/macros/#delete-macro)
  * [Bulk Delete Macros](/api-reference/ticketing/business-rules/macros/#bulk-delete-macros)
  * [Search Macros](/api-reference/ticketing/business-rules/macros/#search-macros)
  * [List Macro Categories](/api-reference/ticketing/business-rules/macros/#list-macro-categories)
  * [List Supported Actions for Macros](/api-reference/ticketing/business-rules/macros/#list-supported-actions-for-macros)
  * [List Macro Action Definitions](/api-reference/ticketing/business-rules/macros/#list-macro-action-definitions)
  * [Show Macro Replica](/api-reference/ticketing/business-rules/macros/#show-macro-replica)
  * [List Macro Attachments](/api-reference/ticketing/business-rules/macros/#list-macro-attachments)
  * [Show Macro Attachment](/api-reference/ticketing/business-rules/macros/#show-macro-attachment)
  * [Create Macro Attachment](/api-reference/ticketing/business-rules/macros/#create-macro-attachment)
  * [Create Unassociated Macro Attachment](/api-reference/ticketing/business-rules/macros/#create-unassociated-macro-attachment)
  * [Show Changes to Ticket](/api-reference/ticketing/business-rules/macros/#show-changes-to-ticket)
  * [Show Ticket After Changes](/api-reference/ticketing/business-rules/macros/#show-ticket-after-changes)


A macro consists of one or more actions that modify the values of a ticket's fields. Macros are applied to tickets manually by agents. For example, you can create macros for support requests that agents can answer with a single, standard response. For more information, see [Using macros to update and add comments to tickets](https://support.zendesk.com/hc/en-us/articles/4408887656602).

### JSON format

Macros are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
actions| array| false| true| Each action describes what the macro will do. See [Actions reference](/documentation/ticketing/reference-guides/actions-reference)
active| boolean| false| false| Useful for determining if the macro should be displayed
created_at| string| true| false| The time the macro was created
default| boolean| true| false| If true, the macro is a default macro
description| string| false| false| The description of the macro
id| integer| true| false| The id automatically assigned when a macro is created
position| integer| false| false| The position of the macro
raw_title| string| false| false| The raw format of the title of the macro
restriction| object| false| false| Access to this macro. A null value allows unrestricted access for all users in the account
title| string| false| true| The title of the macro
updated_at| string| true| false| The time of the last update of the macro
url| string| true| false| A URL to access the macro's details

#### Example


    {  "actions": [    {      "field": "status",      "value": "solved"    },    {      "field": "priority",      "value": "normal"    },    {      "field": "type",      "value": "incident"    },    {      "field": "assignee_id",      "value": "current_user"    },    {      "field": "group_id",      "value": "current_groups"    },    {      "field": "comment_value",      "value": "Thanks for your request. This issue you reported is a known issue. For more information, please visit our forums. "    }  ],  "active": true,  "created_at": "2019-09-16T02:17:38Z",  "default": false,  "description": null,  "id": 360111062754,  "position": 9999,  "raw_title": "Close and redirect to topics",  "restriction": null,  "title": "Close and redirect to topics",  "updated_at": "2019-09-16T02:17:38Z",  "url": "https://subdomain.zendesk.com/api/v2/macros/360111062754"}

### List Macros

  * `GET /api/v2/macros`


Lists all shared and personal macros available to the current user. For admins, the API returns all macros for the account, including the personal macros of agents and other admins.

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
app_installation| The app installation that requires each macro, if present
categories| The macro categories
permissions| The permissions for each macro
usage_1h| The number of times each macro has been used in the past hour
usage_24h| The number of times each macro has been used in the past day
usage_7d| The number of times each macro has been used in the past week
usage_30d| The number of times each macro has been used in the past thirty days

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
access| string| Query| false| Filter macros by access. Possible values are "personal", "agents", "shared", or "account". The "agents" value returns all personal macros for the account's agents and is only available to admins.
active| boolean| Query| false| Filter by active macros if true or inactive macros if false
category| integer| Query| false| Filter macros by category
group_id| integer| Query| false| Filter macros by group
include| string| Query| false| A sideload to include in the response. See Sideloads
only_viewable| boolean| Query| false| If true, returns only macros that can be applied to tickets. If false, returns all macros the current user can manage. Default is false
page| | Query| false| Pagination parameter. Supports both traditional offset and cursor-based pagination: - Traditional: `?page=2` (integer page number) - Cursor: `?page[size]=50&page[after]=cursor` (deepObject with size, after, before) These are mutually exclusive - use one format or the other, not both.
per_page| integer| Query| false| Number of records to return per page. Note: Default and maximum values vary by endpoint. Check endpoint-specific documentation for limits.
sort_by| string| Query| false| Possible values are "alphabetical", "created_at", "updated_at", "usage_1h", "usage_24h", "usage_7d", or "usage_30d". Defaults to alphabetical
sort_order| string| Query| false| One of "asc" or "desc". Defaults to "asc" for alphabetical and position sort, "desc" for all others

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/macros \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/macros?access=personal&active=true&category=25&group_id=25&include=usage_7d&only_viewable=false&page=&per_page=50&sort_by=alphabetical&sort_order=asc"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/macros")		.newBuilder()		.addQueryParameter("access", "personal")		.addQueryParameter("active", "true")		.addQueryParameter("category", "25")		.addQueryParameter("group_id", "25")		.addQueryParameter("include", "usage_7d")		.addQueryParameter("only_viewable", "false")		.addQueryParameter("page", "")		.addQueryParameter("per_page", "50")		.addQueryParameter("sort_by", "alphabetical")		.addQueryParameter("sort_order", "asc");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/macros',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'access': 'personal',    'active': 'true',    'category': '25',    'group_id': '25',    'include': 'usage_7d',    'only_viewable': 'false',    'page': '',    'per_page': '50',    'sort_by': 'alphabetical',    'sort_order': 'asc',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/macros?access=personal&active=true&category=25&group_id=25&include=usage_7d&only_viewable=false&page=&per_page=50&sort_by=alphabetical&sort_order=asc"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/macros")uri.query = URI.encode_www_form("access": "personal", "active": "true", "category": "25", "group_id": "25", "include": "usage_7d", "only_viewable": "false", "page": "", "per_page": "50", "sort_by": "alphabetical", "sort_order": "asc")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "count": 2,  "macros": [    {      "actions": [],      "active": true,      "description": "Sets the ticket status to `solved`",      "id": 25,      "position": 42,      "restriction": {},      "title": "Close and Save"    },    {      "actions": [],      "active": false,      "description": "Adds a `priority` tag to the ticket",      "id": 26,      "restriction": {},      "title": "Assign priority tag"    }  ],  "next_page": null,  "previous_page": null}

### List Active Macros

  * `GET /api/v2/macros/active`


Lists all active shared and personal macros available to the current user.

#### Allowed For

  * Agents


#### Sideloads

The following sideloads are supported. The usage sideloads are only supported on the Support Professional or Suite Growth plan or above.

Name| Will sideload
---|---
app_installation| The app installation that requires each macro, if present
categories| The macro categories
permissions| The permissions for each macro
usage_1h| The number of times each macro has been used in the past hour
usage_24h| The number of times each macro has been used in the past day
usage_7d| The number of times each macro has been used in the past week
usage_30d| The number of times each macro has been used in the past thirty days

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
access| string| Query| false| Filter macros by access. Possible values are "personal", "agents", "shared", or "account". The "agents" value returns all personal macros for the account's agents and is only available to admins.
category| integer| Query| false| Filter macros by category
group_id| integer| Query| false| Filter macros by group
include| string| Query| false| A sideload to include in the response. See Sideloads
sort_by| string| Query| false| Possible values are "alphabetical", "created_at", "updated_at", "usage_1h", "usage_24h", "usage_7d", or "usage_30d". Defaults to alphabetical
sort_order| string| Query| false| One of "asc" or "desc". Defaults to "asc" for alphabetical and position sort, "desc" for all others

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/macros/active \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/macros/active?access=personal&category=25&group_id=25&include=usage_7d&sort_by=alphabetical&sort_order=asc"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/macros/active")		.newBuilder()		.addQueryParameter("access", "personal")		.addQueryParameter("category", "25")		.addQueryParameter("group_id", "25")		.addQueryParameter("include", "usage_7d")		.addQueryParameter("sort_by", "alphabetical")		.addQueryParameter("sort_order", "asc");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/macros/active',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'access': 'personal',    'category': '25',    'group_id': '25',    'include': 'usage_7d',    'sort_by': 'alphabetical',    'sort_order': 'asc',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/macros/active?access=personal&category=25&group_id=25&include=usage_7d&sort_by=alphabetical&sort_order=asc"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/macros/active")uri.query = URI.encode_www_form("access": "personal", "category": "25", "group_id": "25", "include": "usage_7d", "sort_by": "alphabetical", "sort_order": "asc")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "count": 2,  "macros": [    {      "actions": [],      "active": true,      "description": "Sets the ticket status to `solved`",      "id": 25,      "position": 42,      "restriction": {},      "title": "Close and Save"    },    {      "actions": [],      "active": false,      "description": "Adds a `priority` tag to the ticket",      "id": 26,      "restriction": {},      "title": "Assign priority tag"    }  ],  "next_page": null,  "previous_page": null}

### Show Macro

  * `GET /api/v2/macros/{macro_id}`


#### Allowed For

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
macro_id| integer| Path| true| The ID of the macro

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/macros/{macro_id} \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/macros/25"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/macros/25")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/macros/25',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/macros/25"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/macros/25")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "macro": {    "actions": [],    "active": true,    "description": "Sets the ticket status to `solved`",    "id": 25,    "position": 42,    "restriction": {},    "title": "Close and Save"  }}

### Create Macro

  * `POST /api/v2/macros`


#### Allowed For

  * Agents


#### Request Parameters

The POST request takes one parameter, a `macro` object that lists the values to set when the macro is created.

Name| Description
---|---
actions| Required. An object describing what the macro will do. See [Actions reference](/documentation/ticketing/reference-guides/actions-reference)
active| Allowed values are true or false. Determines if the macro is displayed or not
attachments| An array of macro attachment IDs to be associated with the macro
description| The description of the macro
position| The position of the macro
restriction| An object that describes who can access the macro. To give all agents access to the macro, omit this property
title| Required. The title of the macro

The `restriction` object has the following properties.

Name| Comment
---|---
type| Required. Allowed values are "Group" or "User"
id| The numeric ID of the group or user
ids| The numeric IDs of the groups

#### Example body


    {  "macro": {    "actions": [      {        "field": "status",        "value": "solved"      }    ],    "title": "Roger Wilco"  }}

#### Code Samples

**curl**


    curl -u {email_address}/token:{api_token} https://{subdomain}.zendesk.com/api/v2/macros \  -H "Content-Type: application/json" -X POST \  -d '{"macro": {"title": "Roger Wilco", "actions": [{"field": "status", "value": "solved"}], "restriction": {"type": "User","id": "12345"}}}'

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://example.zendesk.com/api/v2/macros"	method := "POST"	payload := strings.NewReader(`{  "macro": {    "actions": [      {        "field": "status",        "value": "solved"      }    ],    "title": "Roger Wilco"  }}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/macros")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"macro\": {    \"actions\": [      {        \"field\": \"status\",        \"value\": \"solved\"      }    ],    \"title\": \"Roger Wilco\"  }}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "macro": {    "actions": [      {        "field": "status",        "value": "solved"      }    ],    "title": "Roger Wilco"  }});
    var config = {  method: 'POST',  url: 'https://example.zendesk.com/api/v2/macros',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/macros"
    payload = json.loads("""{  "macro": {    "actions": [      {        "field": "status",        "value": "solved"      }    ],    "title": "Roger Wilco"  }}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/macros")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")request.body = %q({  "macro": {    "actions": [      {        "field": "status",        "value": "solved"      }    ],    "title": "Roger Wilco"  }})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "macro": {    "actions": [      {        "field": "status",        "value": "solved"      }    ],    "id": 25,    "restriction": {},    "title": "Roger Wilco"  }}

### Update Macro

  * `PUT /api/v2/macros/{macro_id}`


#### Allowed For

  * Agents


#### Note

Updating an action updates the containing array, clearing the other actions. Include all your actions when updating any action.

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
macro_id| integer| Path| true| The ID of the macro

#### Example body


    {  "macro": {    "actions": [      {        "field": "status",        "value": "solved"      }    ],    "title": "Sets the ticket status to `solved`"  }}

#### Code Samples

**curl**


    curl -v -u {email_address}/token:{api_token} https://{subdomain}.zendesk.com/api/v2/macros/{macro_id} \  -H "Content-Type: application/json" -X PUT -d '{"macro": {"title": "Sets the ticket status to `solved`"}}'

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://example.zendesk.com/api/v2/macros/25"	method := "PUT"	payload := strings.NewReader(`{  "macro": {    "actions": [      {        "field": "status",        "value": "solved"      }    ],    "title": "Sets the ticket status to `solved`"  }}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/macros/25")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"macro\": {    \"actions\": [      {        \"field\": \"status\",        \"value\": \"solved\"      }    ],    \"title\": \"Sets the ticket status to `solved`\"  }}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "macro": {    "actions": [      {        "field": "status",        "value": "solved"      }    ],    "title": "Sets the ticket status to `solved`"  }});
    var config = {  method: 'PUT',  url: 'https://example.zendesk.com/api/v2/macros/25',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/macros/25"
    payload = json.loads("""{  "macro": {    "actions": [      {        "field": "status",        "value": "solved"      }    ],    "title": "Sets the ticket status to `solved`"  }}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/macros/25")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")request.body = %q({  "macro": {    "actions": [      {        "field": "status",        "value": "solved"      }    ],    "title": "Sets the ticket status to `solved`"  }})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "macro": {    "actions": [      {        "field": "status",        "value": "solved"      }    ],    "active": true,    "description": "Sets the ticket status to `solved`",    "id": 25,    "position": 42,    "restriction": {},    "title": "Close and Save"  }}

### Update Many Macros

  * `PUT /api/v2/macros/update_many`


Updates the provided macros with the specified changes.

#### Allowed For

  * Agents


#### Request Parameters

The PUT request expects a `macros` object that lists the macros to update.

Each macro may have the following properties

Name| Type| Mandatory| Description
---|---|---|---
id| integer| yes| The ID of the macro to update
position| integer| no| The new position of the macro
active| boolean| no| The active status of the macro (true or false)

#### Example body


    {  "macros": [    {      "active": false,      "id": 25    },    {      "id": 23,      "position": 5    }  ]}

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/macros/update_many \  -v -u {email_address}/token:{api_token} -H "Content-Type: application/json" \  -X PUT -d '{"macros": [{"id": 123, "position": 8}]}'

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://example.zendesk.com/api/v2/macros/update_many"	method := "PUT"	payload := strings.NewReader(`{  "macros": [    {      "active": false,      "id": 25    },    {      "id": 23,      "position": 5    }  ]}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/macros/update_many")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"macros\": [    {      \"active\": false,      \"id\": 25    },    {      \"id\": 23,      \"position\": 5    }  ]}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "macros": [    {      "active": false,      "id": 25    },    {      "id": 23,      "position": 5    }  ]});
    var config = {  method: 'PUT',  url: 'https://example.zendesk.com/api/v2/macros/update_many',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/macros/update_many"
    payload = json.loads("""{  "macros": [    {      "active": false,      "id": 25    },    {      "id": 23,      "position": 5    }  ]}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/macros/update_many")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")request.body = %q({  "macros": [    {      "active": false,      "id": 25    },    {      "id": 23,      "position": 5    }  ]})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "count": 2,  "macros": [    {      "actions": [],      "active": true,      "description": "Sets the ticket status to `solved`",      "id": 25,      "position": 42,      "restriction": {},      "title": "Close and Save"    },    {      "actions": [],      "active": false,      "description": "Adds a `priority` tag to the ticket",      "id": 26,      "restriction": {},      "title": "Assign priority tag"    }  ],  "next_page": null,  "previous_page": null}

### Delete Macro

  * `DELETE /api/v2/macros/{macro_id}`


#### Allowed For

  * Agents, with restrictions applying on certain actions


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
macro_id| integer| Path| true| The ID of the macro

#### Code Samples

**curl**


    curl -v -u {email_address}/token:{api_token} https://{subdomain}.zendesk.com/api/v2/macros/{macro_id} \  -X DELETE

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/macros/25"	method := "DELETE"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/macros/25")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("DELETE", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'DELETE',  url: 'https://example.zendesk.com/api/v2/macros/25',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/macros/25"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"DELETE",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/macros/25")request = Net::HTTP::Delete.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**204 No Content**


    // Status 204 No Content
    null

### Bulk Delete Macros

  * `DELETE /api/v2/macros/destroy_many?ids={ids}`


Deletes the macros corresponding to the provided comma-separated list of IDs.

#### Allowed For

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
ids| array| Query| true| The IDs of the macros to delete

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/macros/destroy_many?ids=1,2,3 \  -v -u {email_address}/token:{api_token} -X DELETE

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/macros/destroy_many?ids=%5B1%2C2%2C3%5D"	method := "DELETE"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/macros/destroy_many")		.newBuilder()		.addQueryParameter("ids", "[1,2,3]");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("DELETE", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'DELETE',  url: 'https://example.zendesk.com/api/v2/macros/destroy_many',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'ids': '%5B1%2C2%2C3%5D',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/macros/destroy_many?ids=%5B1%2C2%2C3%5D"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"DELETE",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/macros/destroy_many")uri.query = URI.encode_www_form("ids": "[1,2,3]")request = Net::HTTP::Delete.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**204 No Content**


    // Status 204 No Content
    null

### Search Macros

  * `GET /api/v2/macros/search?query={query}`


#### Pagination

  * Offset pagination only


See [Using Offset Pagination](/api-reference/introduction/pagination/#using-offset-pagination).

#### Allowed For

  * Agents


#### Sideloads

The following sideloads are supported. The usage sideloads are only supported on the Support Professional or Suite Growth plan or above. For more information, see [Side-loading](/documentation/ticketing/using-the-zendesk-api/side_loading/).

Name| Will sideload
---|---
app_installation| The app installation that requires each macro, if present
categories| The macro categories
permissions| The permissions for each macro
usage_1h| The number of times each macro has been used in the past hour
usage_24h| The number of times each macro has been used in the past day
usage_7d| The number of times each macro has been used in the past week
usage_30d| The number of times each macro has been used in the past thirty days

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
access| string| Query| false| Filter macros by access. Possible values are "personal", "agents", "shared", or "account". The "agents" value returns all personal macros for the account's agents and is only available to admins.
active| boolean| Query| false| Filter by active macros if true or inactive macros if false
category| integer| Query| false| Filter macros by category
group_id| integer| Query| false| Filter macros by group
include| string| Query| false| A sideload to include in the response. See Sideloads
only_viewable| boolean| Query| false| If true, returns only macros that can be applied to tickets. If false, returns all macros the current user can manage. Default is false
query| string| Query| true| Query string used to find macros with matching titles
sort_by| string| Query| false| Possible values are "alphabetical", "created_at", "updated_at", or "position". Defaults to alphabetical
sort_order| string| Query| false| One of "asc" or "desc". Defaults to "asc" for alphabetical and position sort, "desc" for all others

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/macros/search?query=close&active=true  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/macros/search?access=personal&active=true&category=25&group_id=25&include=usage_7d&only_viewable=false&query=close&sort_by=alphabetical&sort_order=asc"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/macros/search")		.newBuilder()		.addQueryParameter("access", "personal")		.addQueryParameter("active", "true")		.addQueryParameter("category", "25")		.addQueryParameter("group_id", "25")		.addQueryParameter("include", "usage_7d")		.addQueryParameter("only_viewable", "false")		.addQueryParameter("query", "close")		.addQueryParameter("sort_by", "alphabetical")		.addQueryParameter("sort_order", "asc");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/macros/search',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'access': 'personal',    'active': 'true',    'category': '25',    'group_id': '25',    'include': 'usage_7d',    'only_viewable': 'false',    'query': 'close',    'sort_by': 'alphabetical',    'sort_order': 'asc',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/macros/search?access=personal&active=true&category=25&group_id=25&include=usage_7d&only_viewable=false&query=close&sort_by=alphabetical&sort_order=asc"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/macros/search")uri.query = URI.encode_www_form("access": "personal", "active": "true", "category": "25", "group_id": "25", "include": "usage_7d", "only_viewable": "false", "query": "close", "sort_by": "alphabetical", "sort_order": "asc")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "count": 2,  "macros": [    {      "actions": [],      "active": true,      "description": "Sets the ticket status to `solved`",      "id": 25,      "position": 42,      "restriction": {},      "title": "Close and Save"    },    {      "actions": [],      "active": false,      "description": "Adds a `priority` tag to the ticket",      "id": 26,      "restriction": {},      "title": "Assign priority tag"    }  ],  "next_page": null,  "previous_page": null}

### List Macro Categories

  * `GET /api/v2/macros/categories`


Lists all macro categories available to the current user.

#### Allowed For

  * Agents


#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/macros/categories \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/macros/categories"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/macros/categories")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/macros/categories',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/macros/categories"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/macros/categories")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "categories": [    "FAQ",    "Triage"  ]}

### List Supported Actions for Macros

  * `GET /api/v2/macros/actions`


#### Allowed For

  * Agents


#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/macros/actions \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/macros/actions"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/macros/actions")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/macros/actions',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/macros/actions"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/macros/actions")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "actions": [    {      "group": "ticket",      "operators": [        {          "title": "Is",          "value": "is"        }      ],      "output_key": null,      "target": null,      "title": "Set subject",      "title_for_field": "Set subject",      "value": "subject",      "values": {        "list": [],        "type": "text"      }    },    {      "group": "ticket",      "operators": [        {          "title": "Is",          "value": "is"        }      ],      "output_key": null,      "target": null,      "title": "Status",      "title_for_field": "Set subject",      "value": "subject",      "values": {        "list": [          {            "enabled": true,            "title": "Open",            "value": "open"          },          {            "enabled": true,            "title": "Pending",            "value": "pending"          },          {            "enabled": true,            "title": "Solved",            "value": "solved"          }        ],        "type": "list"      }    },    {      "field": "priority",      "group": "ticket",      "operators": [        {          "title": "Is",          "value": "is"        }      ],      "output_key": null,      "title": "Priority",      "title_for_field": "Priority",      "value": "priority",      "values": {        "list": [          {            "enabled": false,            "title": "Low",            "value": "low"          },          {            "enabled": true,            "title": "Normal",            "value": "normal"          },          {            "enabled": true,            "title": "High",            "value": "high"          },          {            "enabled": false,            "title": "Urgent",            "value": "urgent"          }        ],        "type": "list"      }    }  ]}

### List Macro Action Definitions

  * `GET /api/v2/macros/definitions`


Returns the definitions of the actions a macro can perform. For example, one action can set the status of a ticket. The definition of the action includes a title ("Status"), a type ("list"), and possible values. For a list of support actions, see [Actions reference](/documentation/ticketing/reference-guides/actions-reference).

#### Allowed For

  * Agents


#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/macros/definitions \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/macros/definitions"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/macros/definitions")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/macros/definitions',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/macros/definitions"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/macros/definitions")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "definitions": {    "actions": [      {        "group": "ticket",        "nullable": false,        "repeatable": false,        "subject": "status",        "title": "Status",        "type": "list",        "values": [          {            "enabled": true,            "title": "Open",            "value": "1"          },          {            "enabled": true,            "title": "Pending",            "value": "2"          },          {            "enabled": true,            "title": "Solved",            "value": "3"          },          {            "enabled": true,            "title": "Closed",            "value": "4"          }        ]      }    ]  }}

### Show Macro Replica

  * `GET /api/v2/macros/new?macro_id={macro_id}&ticket_id={ticket_id}`


Returns an unpersisted macro representation derived from a ticket or macro.

The endpoint takes one of the following query parameters: `macro_id` or `ticket_id`. If you include both, `macro_id` is used.

#### Allowed For

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
macro_id| integer| Query| true| The ID of the macro to replicate
ticket_id| integer| Query| true| The ID of the ticket from which to build a macro replica

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/macros/new?macro_id=123 \  -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/macros/new?macro_id=25&ticket_id=35436"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/macros/new")		.newBuilder()		.addQueryParameter("macro_id", "25")		.addQueryParameter("ticket_id", "35436");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/macros/new',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'macro_id': '25',    'ticket_id': '35436',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/macros/new?macro_id=25&ticket_id=35436"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/macros/new")uri.query = URI.encode_www_form("macro_id": "25", "ticket_id": "35436")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "macro": {    "actions": [],    "active": true,    "description": "Sets the ticket status to `solved`",    "id": 25,    "position": 42,    "restriction": {},    "title": "Close and Save"  }}

### List Macro Attachments

  * `GET /api/v2/macros/{macro_id}/attachments`


Lists the attachments associated with a macro.

#### Allowed For

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
macro_id| integer| Path| true| The ID of the macro

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/macros/{macro_id}/attachments \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/macros/25/attachments"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/macros/25/attachments")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/macros/25/attachments',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/macros/25/attachments"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/macros/25/attachments")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "macro_attachments": [    {      "content_type": "image/jpeg",      "content_url": "https://company.zendesk.com/api/v2/macros/attachments/100/content",      "created_at": "2016-08-15T16:04:06Z",      "filename": "foobar.jpg",      "id": 100,      "size": 2532    },    {      "content_type": "image/jpeg",      "content_url": "https://company.zendesk.com/api/v2/macros/attachments/342/content",      "created_at": "2016-08-16T12:42:25Z",      "filename": "bazbat.jpg",      "id": 342,      "size": 5028    }  ]}

### Show Macro Attachment

  * `GET /api/v2/macros/attachments/{attachment_id}`


Shows the properties of the specified macro attachment.

#### Allowed For

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
attachment_id| integer| Path| true| The ID of the attachment

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/macros/attachments/{id} \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/macros/attachments/498483"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/macros/attachments/498483")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/macros/attachments/498483',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/macros/attachments/498483"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/macros/attachments/498483")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "macro_attachment": {    "content_type": "image/jpeg",    "content_url": "https://company.zendesk.com/api/v2/macros/attachments/100/content",    "created_at": "2016-08-15T16:04:06Z",    "filename": "foobar.jpg",    "id": 100,    "size": 2532  }}

### Create Macro Attachment

  * `POST /api/v2/macros/{macro_id}/attachments`


Allows an attachment to be uploaded and associated with a macro at the same time.

**Note:** A macro can be associated with up to five attachments.

#### Allowed For

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
macro_id| integer| Path| true| The ID of the macro

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/macros/123/attachments \  -v -u {email_address}/token:{api_token} -F "[[email protected]](/cdn-cgi/l/email-protection)" -F "filename=foobar.jpg"

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/macros/25/attachments"	method := "POST"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/macros/25/attachments")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'POST',  url: 'https://example.zendesk.com/api/v2/macros/25/attachments',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/macros/25/attachments"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/macros/25/attachments")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**201 Created**


    // Status 201 Created
    {  "macro_attachment": {    "content_type": "image/jpeg",    "content_url": "https://company.zendesk.com/api/v2/macros/attachments/100/content",    "created_at": "2016-08-15T16:04:06Z",    "filename": "foobar.jpg",    "id": 100,    "size": 2532  }}

### Create Unassociated Macro Attachment

  * `POST /api/v2/macros/attachments`


Allows an attachment to be uploaded that can be associated with a macro at a later time.

**Note:** To ensure an uploaded attachment is not lost, associate it with a macro as soon as possible. From time to time, old attachments that are not not associated with any macro are purged.

#### Allowed For

  * Agents


#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/macros/attachments \  -v -u {email_address}/token:{api_token} -F "[[email protected]](/cdn-cgi/l/email-protection)" -F "filename=foobar.jpg"

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/macros/attachments"	method := "POST"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/macros/attachments")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'POST',  url: 'https://example.zendesk.com/api/v2/macros/attachments',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/macros/attachments"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/macros/attachments")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**201 Created**


    // Status 201 Created
    {  "macro_attachment": {    "content_type": "image/jpeg",    "content_url": "https://company.zendesk.com/api/v2/macros/attachments/100/content",    "created_at": "2016-08-15T16:04:06Z",    "filename": "foobar.jpg",    "id": 100,    "size": 2532  }}

### Show Changes to Ticket

  * `GET /api/v2/macros/{macro_id}/apply`


Returns the changes the macro would make to a ticket. It doesn't actually change a ticket. You can use the response data in a subsequent API call to the [Tickets](/api-reference/ticketing/tickets/tickets/) endpoint to update the ticket.

The response includes only the ticket fields that would be changed by the macro. To get the full ticket object after the macro is applied, see Show Ticket After Changes.

#### Allowed For

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
macro_id| integer| Path| true| The ID of the macro

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/macros/{macro_id}/apply \  -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/macros/25/apply"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/macros/25/apply")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/macros/25/apply',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/macros/25/apply"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/macros/25/apply")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "result": {    "ticket": {      "assignee_id": 235323,      "comment": {        "body": "Assigned to Agent Uno.",        "public": false,        "scoped_body": [          [            "channel:all",            "Assigned to Agent Uno."          ]        ]      },      "fields": {        "id": 27642,        "value": "745"      },      "group_id": 98738    }  }}

### Show Ticket After Changes

  * `GET /api/v2/tickets/{ticket_id}/macros/{macro_id}/apply`


Returns the full ticket object as it would be after applying the macro to the ticket. It doesn't actually change the ticket.

To get only the ticket fields that would be changed by the macro, see Show Changes to Ticket.

#### Allowed For

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
macro_id| integer| Path| true| The ID of the macro
ticket_id| integer| Path| true| The ID of the ticket

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/tickets/{ticket_id}/macros/{id}/apply \  -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/tickets/35436/macros/25/apply"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/tickets/35436/macros/25/apply")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/tickets/35436/macros/25/apply',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/tickets/35436/macros/25/apply"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/tickets/35436/macros/25/apply")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "result": {    "ticket": {      "assignee_id": 235323,      "comment": {        "body": "Assigned to Agent Uno.",        "public": false,        "scoped_body": [          [            "channel:all",            "Assigned to Agent Uno."          ]        ]      },      "fields": {        "id": 27642,        "value": "745"      },      "group_id": 98738    }  }}

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)