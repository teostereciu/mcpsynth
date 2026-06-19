# Workspaces

*Source: https://developer.zendesk.com/api-reference/ticketing/ticket-management/workspaces/*

---

## On this page

  * [JSON format](/api-reference/ticketing/ticket-management/workspaces/#json-format)
  * [List Workspaces](/api-reference/ticketing/ticket-management/workspaces/#list-workspaces)
  * [Show Workspace](/api-reference/ticketing/ticket-management/workspaces/#show-workspace)
  * [Create Workspace](/api-reference/ticketing/ticket-management/workspaces/#create-workspace)
  * [Update Workspace](/api-reference/ticketing/ticket-management/workspaces/#update-workspace)
  * [Reorder Workspaces](/api-reference/ticketing/ticket-management/workspaces/#reorder-workspaces)
  * [Delete Workspace](/api-reference/ticketing/ticket-management/workspaces/#delete-workspace)
  * [Bulk Delete Workspaces](/api-reference/ticketing/ticket-management/workspaces/#bulk-delete-workspaces)


# Workspaces

## On this page

  * [JSON format](/api-reference/ticketing/ticket-management/workspaces/#json-format)
  * [List Workspaces](/api-reference/ticketing/ticket-management/workspaces/#list-workspaces)
  * [Show Workspace](/api-reference/ticketing/ticket-management/workspaces/#show-workspace)
  * [Create Workspace](/api-reference/ticketing/ticket-management/workspaces/#create-workspace)
  * [Update Workspace](/api-reference/ticketing/ticket-management/workspaces/#update-workspace)
  * [Reorder Workspaces](/api-reference/ticketing/ticket-management/workspaces/#reorder-workspaces)
  * [Delete Workspace](/api-reference/ticketing/ticket-management/workspaces/#delete-workspace)
  * [Bulk Delete Workspaces](/api-reference/ticketing/ticket-management/workspaces/#bulk-delete-workspaces)


Admins in Zendesk Support can set up contextual workspaces to present ticket tools and features based on specific workflows. For more information, see [Setting up contextual workspaces (Enterprise)](https://support.zendesk.com/hc/en-us/articles/360001901487).

### JSON format

Workspaces are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
activated| boolean| false| false| If true, this workspace is available for use
apps| array| false| false| The apps associated to this workspace
conditions| object| false| false| An object that describes the conditions under which the automation will execute. See [Conditions reference](/documentation/ticketing/reference-guides/conditions-reference)
created_at| string| false| false| The time the workspace was created
description| string| false| false| User-defined description of this workspace's purpose
id| integer| false| false| Automatically assigned upon creation
macro_ids| array| false| false| The ids of the macros associated to this workspace
macros| array| false| false| The ids of the macros associated to this workspace
position| integer| false| false| Ordering of the workspace relative to other workspaces
prefer_workspace_app_order| boolean| false| false| If true, the order of apps within the workspace will be preserved
selected_macros| array| false| false| An array of the macro objects that will be used in this workspace. See [Macros](/api-reference/ticketing/business-rules/macros/)
ticket_form_id| integer| false| false| The id of the ticket web form associated to this workspace
title| string| false| false| The title of the workspace
updated_at| string| false| false| The time of the last update of the workspace
url| string| false| false| The URL for this resource

### List Workspaces

  * `GET /api/v2/workspaces`


#### Allowed For

  * Admins, Agents


#### Code Samples

**cURL**


    curl https://{subdomain}.zendesk.com/api/v2/workspacescurl https://{subdomain}.zendesk.com/api/v2/workspaces?per_page=2

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/workspaces"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/workspaces")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/workspaces',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/workspaces"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/workspaces")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "count": 1,  "next_page": null,  "previous_page": null,  "workspaces": [    {      "activated": true,      "apps": [        {          "expand": false,          "id": 360000080413,          "position": 1        }      ],      "conditions": {        "all": [          {            "field": "ticket_form_id",            "operator": "is",            "value": "360000014173"          }        ],        "any": []      },      "created_at": "2018-11-13T19:08:13Z",      "description": "Test rules",      "id": 3133,      "macro_ids": [        360005374974      ],      "position": 1,      "prefer_workspace_app_order": true,      "selected_macros": [        {          "actions": [            {              "field": "status",              "value": "solved"            }          ],          "active": true,          "created_at": "2018-02-08T23:45:30Z",          "description": null,          "id": 360005374974,          "position": 9999,          "restriction": {            "id": 360002226093,            "ids": [              360002226093            ],            "type": "Group"          },          "title": "Close and redirect to topics",          "updated_at": "2018-11-08T22:27:00Z",          "url": "https://{subdomain}.zendesk.com/api/v2/macros/360005374974",          "usage_7d": 0        }      ],      "ticket_form_id": 360000014173,      "title": "Test Workspace 1",      "updated_at": "2018-12-17T22:37:40Z",      "url": "https://{subdomain}.zendesk.com/api/v2/workspaces"    }  ]}

### Show Workspace

  * `GET /api/v2/workspaces/{workspace_id}`


#### Allowed For

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
workspace_id| integer| Path| true| The id of the workspace

#### Code Samples

**cURL**


    curl https://{subdomain}.zendesk.com/api/v2/workspaces/{id} \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/workspaces/3133"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/workspaces/3133")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/workspaces/3133',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/workspaces/3133"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/workspaces/3133")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "workspace": {    "activated": true,    "apps": [],    "conditions": {      "all": [        {          "field": "ticket_form_id",          "operator": "is",          "value": "360000014173"        }      ],      "any": []    },    "created_at": "2018-11-13T19:08:13Z",    "description": "Test rules",    "id": 3133,    "macro_ids": [      360005374974    ],    "position": 1,    "prefer_workspace_app_order": true,    "selected_macros": [      {        "actions": [          {            "field": "status",            "value": "solved"          }        ],        "active": true,        "created_at": "2018-02-08T23:45:30Z",        "description": null,        "id": 360005374974,        "position": 9999,        "restriction": {          "id": 360002226093,          "ids": [            360002226093          ],          "type": "Group"        },        "title": "Close and redirect to topics",        "updated_at": "2018-11-08T22:27:00Z",        "url": "https://{subdomain}.zendesk.com/api/v2/macros/360005374974",        "usage_7d": 0      }    ],    "ticket_form_id": 360000014173,    "title": "Test Workspace 1",    "updated_at": "2018-12-17T22:37:40Z",    "url": "https://{subdomain}.zendesk.com/api/v2/workspaces"  }}

### Create Workspace

  * `POST /api/v2/workspaces`


#### Allowed For

  * Admins


#### Example body


    {  "workspace": {    "conditions": {      "all": [        {          "field": "ticket_form_id",          "operator": "is",          "value": "360000014173"        }      ],      "any": []    },    "description": "Test rules",    "macros": [      360005374974    ],    "ticket_form_id": 360000014173,    "title": "Test Workspace 1"  }}

#### Code Samples

**cURL**


    curl https://{subdomain}.zendesk.com/api/v2/workspaces \  -H "Content-Type: application/json" -X POST \  -d '  {    "workspace": {      "title": "Test Workspace 1",      "description": "Test rules",      "ticket_form_id": 360000014173,      "macros": [360005374974],      "conditions": {        "all": [          {            "field": "ticket_form_id",            "operator": "is",            "value": "360000014173"          },        ],        "any": []      }    }  }' \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://example.zendesk.com/api/v2/workspaces"	method := "POST"	payload := strings.NewReader(`{  "workspace": {    "conditions": {      "all": [        {          "field": "ticket_form_id",          "operator": "is",          "value": "360000014173"        }      ],      "any": []    },    "description": "Test rules",    "macros": [      360005374974    ],    "ticket_form_id": 360000014173,    "title": "Test Workspace 1"  }}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/workspaces")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"workspace\": {    \"conditions\": {      \"all\": [        {          \"field\": \"ticket_form_id\",          \"operator\": \"is\",          \"value\": \"360000014173\"        }      ],      \"any\": []    },    \"description\": \"Test rules\",    \"macros\": [      360005374974    ],    \"ticket_form_id\": 360000014173,    \"title\": \"Test Workspace 1\"  }}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "workspace": {    "conditions": {      "all": [        {          "field": "ticket_form_id",          "operator": "is",          "value": "360000014173"        }      ],      "any": []    },    "description": "Test rules",    "macros": [      360005374974    ],    "ticket_form_id": 360000014173,    "title": "Test Workspace 1"  }});
    var config = {  method: 'POST',  url: 'https://example.zendesk.com/api/v2/workspaces',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/workspaces"
    payload = json.loads("""{  "workspace": {    "conditions": {      "all": [        {          "field": "ticket_form_id",          "operator": "is",          "value": "360000014173"        }      ],      "any": []    },    "description": "Test rules",    "macros": [      360005374974    ],    "ticket_form_id": 360000014173,    "title": "Test Workspace 1"  }}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/workspaces")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")request.body = %q({  "workspace": {    "conditions": {      "all": [        {          "field": "ticket_form_id",          "operator": "is",          "value": "360000014173"        }      ],      "any": []    },    "description": "Test rules",    "macros": [      360005374974    ],    "ticket_form_id": 360000014173,    "title": "Test Workspace 1"  }})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**201 Created**


    // Status 201 Created
    {  "workspace": {    "activated": true,    "apps": [],    "conditions": {      "all": [        {          "field": "ticket_form_id",          "operator": "is",          "value": "360000014173"        }      ],      "any": []    },    "created_at": "2018-11-13T19:08:13Z",    "description": "Test rules",    "id": 3133,    "macro_ids": [      360005374974    ],    "position": 1,    "prefer_workspace_app_order": true,    "selected_macros": [      {        "actions": [          {            "field": "status",            "value": "solved"          }        ],        "active": true,        "created_at": "2018-02-08T23:45:30Z",        "description": null,        "id": 360005374974,        "position": 9999,        "restriction": {          "id": 360002226093,          "ids": [            360002226093          ],          "type": "Group"        },        "title": "Close and redirect to topics",        "updated_at": "2018-11-08T22:27:00Z",        "url": "https://{subdomain}.zendesk.com/api/v2/macros/360005374974",        "usage_7d": 0      }    ],    "ticket_form_id": 360000014173,    "title": "Test Workspace 1",    "updated_at": "2018-12-17T22:37:40Z",    "url": "https://{subdomain}.zendesk.com/api/v2/workspaces"  }}

### Update Workspace

  * `PUT /api/v2/workspaces/{workspace_id}`


#### Allowed For

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
workspace_id| integer| Path| true| The id of the workspace

#### Example body


    {  "workspace": {    "conditions": {      "all": [        {          "field": "ticket_form_id",          "operator": "is",          "value": "360000014173"        }      ],      "any": []    },    "description": "Test rules",    "macros": [      360005374974    ],    "ticket_form_id": 360000014173,    "title": "Test Workspace 1"  }}

#### Code Samples

**cURL**


    curl https://{subdomain}.zendesk.com/api/v2/workspaces/{id} \  -H "Content-Type: application/json" -X PUT \  -d '{"workspace": {          "title": "Test Workspace 1",          "description": "Test rules",          "ticket_form_id": 360000014173,          "macro_ids": [360005374974],          "conditions": {            "all": [              {                "field": "status",                "operator": "is",                "value": "pending"              },            ],            "any": []          }      }}' \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://example.zendesk.com/api/v2/workspaces/3133"	method := "PUT"	payload := strings.NewReader(`{  "workspace": {    "conditions": {      "all": [        {          "field": "ticket_form_id",          "operator": "is",          "value": "360000014173"        }      ],      "any": []    },    "description": "Test rules",    "macros": [      360005374974    ],    "ticket_form_id": 360000014173,    "title": "Test Workspace 1"  }}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/workspaces/3133")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"workspace\": {    \"conditions\": {      \"all\": [        {          \"field\": \"ticket_form_id\",          \"operator\": \"is\",          \"value\": \"360000014173\"        }      ],      \"any\": []    },    \"description\": \"Test rules\",    \"macros\": [      360005374974    ],    \"ticket_form_id\": 360000014173,    \"title\": \"Test Workspace 1\"  }}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "workspace": {    "conditions": {      "all": [        {          "field": "ticket_form_id",          "operator": "is",          "value": "360000014173"        }      ],      "any": []    },    "description": "Test rules",    "macros": [      360005374974    ],    "ticket_form_id": 360000014173,    "title": "Test Workspace 1"  }});
    var config = {  method: 'PUT',  url: 'https://example.zendesk.com/api/v2/workspaces/3133',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/workspaces/3133"
    payload = json.loads("""{  "workspace": {    "conditions": {      "all": [        {          "field": "ticket_form_id",          "operator": "is",          "value": "360000014173"        }      ],      "any": []    },    "description": "Test rules",    "macros": [      360005374974    ],    "ticket_form_id": 360000014173,    "title": "Test Workspace 1"  }}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/workspaces/3133")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")request.body = %q({  "workspace": {    "conditions": {      "all": [        {          "field": "ticket_form_id",          "operator": "is",          "value": "360000014173"        }      ],      "any": []    },    "description": "Test rules",    "macros": [      360005374974    ],    "ticket_form_id": 360000014173,    "title": "Test Workspace 1"  }})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "workspace": {    "activated": true,    "apps": [],    "conditions": {      "all": [        {          "field": "ticket_form_id",          "operator": "is",          "value": "360000014173"        }      ],      "any": []    },    "created_at": "2018-11-13T19:08:13Z",    "description": "Test rules",    "id": 3133,    "macro_ids": [      360005374974    ],    "position": 1,    "prefer_workspace_app_order": true,    "selected_macros": [      {        "actions": [          {            "field": "status",            "value": "solved"          }        ],        "active": true,        "created_at": "2018-02-08T23:45:30Z",        "description": null,        "id": 360005374974,        "position": 9999,        "restriction": {          "id": 360002226093,          "ids": [            360002226093          ],          "type": "Group"        },        "title": "Close and redirect to topics",        "updated_at": "2018-11-08T22:27:00Z",        "url": "https://{subdomain}.zendesk.com/api/v2/macros/360005374974",        "usage_7d": 0      }    ],    "ticket_form_id": 360000014173,    "title": "Test Workspace 1",    "updated_at": "2018-12-17T22:37:40Z",    "url": "https://{subdomain}.zendesk.com/api/v2/workspaces"  }}

### Reorder Workspaces

  * `PUT /api/v2/workspaces/reorder`


#### Allowed For

  * Admins


#### Example body


    {  "ids": [    12,    32,    48,    60  ]}

#### Code Samples

**cURL**


    curl https://{subdomain}.zendesk.com/api/v2/workspaces/reorder \  -H "Content-Type: application/json" -X PUT \  -d '{"ids": [12, 32, 48, 60]}' \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://example.zendesk.com/api/v2/workspaces/reorder"	method := "PUT"	payload := strings.NewReader(`{  "ids": [    12,    32,    48,    60  ]}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/workspaces/reorder")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"ids\": [    12,    32,    48,    60  ]}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "ids": [    12,    32,    48,    60  ]});
    var config = {  method: 'PUT',  url: 'https://example.zendesk.com/api/v2/workspaces/reorder',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/workspaces/reorder"
    payload = json.loads("""{  "ids": [    12,    32,    48,    60  ]}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/workspaces/reorder")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")request.body = %q({  "ids": [    12,    32,    48,    60  ]})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    null

### Delete Workspace

  * `DELETE /api/v2/workspaces/{workspace_id}`


#### Allowed For

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
workspace_id| integer| Path| true| The id of the workspace

#### Code Samples

**cURL**


    curl https://{subdomain}.zendesk.com/api/v2/workspaces/{workspace_id} \  -v -u {email_address}/token:{api_token} -X DELETE

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/workspaces/3133"	method := "DELETE"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/workspaces/3133")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("DELETE", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'DELETE',  url: 'https://example.zendesk.com/api/v2/workspaces/3133',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/workspaces/3133"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"DELETE",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/workspaces/3133")request = Net::HTTP::Delete.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**204 No Content**


    // Status 204 No Content
    null

### Bulk Delete Workspaces

  * `DELETE /api/v2/workspaces/destroy_many?ids={ids}`


#### Allowed For

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
ids| array| Query| true| The ids of the workspaces to delete

#### Code Samples

**cURL**


    curl https://{subdomain}.zendesk.com/api/v2/workspaces/destroy_many?ids=1,2,3 \  -v -u {email_address}/token:{api_token} -X DELETE

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/workspaces/destroy_many?ids=%5B1%2C2%2C3%5D"	method := "DELETE"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/workspaces/destroy_many")		.newBuilder()		.addQueryParameter("ids", "[1,2,3]");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("DELETE", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'DELETE',  url: 'https://example.zendesk.com/api/v2/workspaces/destroy_many',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'ids': '%5B1%2C2%2C3%5D',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/workspaces/destroy_many?ids=%5B1%2C2%2C3%5D"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"DELETE",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/workspaces/destroy_many")uri.query = URI.encode_www_form("ids": "[1,2,3]")request = Net::HTTP::Delete.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    null

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)