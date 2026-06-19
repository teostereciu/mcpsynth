# Trigger Categories

*Source: https://developer.zendesk.com/api-reference/ticketing/business-rules/trigger_categories/*

---

## On this page

  * [JSON format](/api-reference/ticketing/business-rules/trigger_categories/#json-format)
  * [List Ticket Trigger Categories](/api-reference/ticketing/business-rules/trigger_categories/#list-ticket-trigger-categories)
  * [Create Ticket Trigger Category](/api-reference/ticketing/business-rules/trigger_categories/#create-ticket-trigger-category)
  * [Create Batch Job for Ticket Trigger Categories](/api-reference/ticketing/business-rules/trigger_categories/#create-batch-job-for-ticket-trigger-categories)
  * [Show Ticket Trigger Category](/api-reference/ticketing/business-rules/trigger_categories/#show-ticket-trigger-category)
  * [Update Ticket Trigger Category](/api-reference/ticketing/business-rules/trigger_categories/#update-ticket-trigger-category)
  * [Delete Ticket Trigger Category](/api-reference/ticketing/business-rules/trigger_categories/#delete-ticket-trigger-category)


# Trigger Categories

## On this page

  * [JSON format](/api-reference/ticketing/business-rules/trigger_categories/#json-format)
  * [List Ticket Trigger Categories](/api-reference/ticketing/business-rules/trigger_categories/#list-ticket-trigger-categories)
  * [Create Ticket Trigger Category](/api-reference/ticketing/business-rules/trigger_categories/#create-ticket-trigger-category)
  * [Create Batch Job for Ticket Trigger Categories](/api-reference/ticketing/business-rules/trigger_categories/#create-batch-job-for-ticket-trigger-categories)
  * [Show Ticket Trigger Category](/api-reference/ticketing/business-rules/trigger_categories/#show-ticket-trigger-category)
  * [Update Ticket Trigger Category](/api-reference/ticketing/business-rules/trigger_categories/#update-ticket-trigger-category)
  * [Delete Ticket Trigger Category](/api-reference/ticketing/business-rules/trigger_categories/#delete-ticket-trigger-category)


Ticket trigger categories allow Zendesk admins to visually group [ticket triggers](https://support.zendesk.com/hc/en-us/articles/203662106) and make it easier for them to organize and manage their ticket triggers. For more information, see [Creating categories to organize ticket triggers ](https://support.zendesk.com/hc/en-us/articles/360058107673) in Zendesk help.

### JSON format

Trigger Categories are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
created_at| string| true| false|
id| string| true| false|
name| string| false| false|
position| integer| false| false|
updated_at| string| true| false|

### List Ticket Trigger Categories

  * `GET /api/v2/trigger_categories`


Returns all the ticket trigger categories in the account.

#### Pagination

  * Cursor pagination (recommended)
  * Offset pagination


See [Pagination](/api-reference/introduction/pagination/).

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
include| string| Query| false| Allowed sideloads. Allowed value of "rule_counts".
page| object| Query| false| Pagination parameters
sort| string| Query| false| Sort parameters. Allowed values are "position", "-position", "name", "-name", "created_at", "-created_at", "updated_at", or "-updated_at".

#### Code Samples

**cURL**

This example provides an example query with pagination parameters with cURL.


    curl -u {email_address}/token:{api_token} -X GET \  --url https://{subdomain}.zendesk.com/api/v2/trigger_categories

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/trigger_categories?include=&page=%7B%22after%22%3A%22eyJvIjoiLXNjb3JlLGlkIiwidiI6ImFRSUFBQUFBQUFBQWFRMHBJUUVBQUFBQSJ9%22%2C%22before%22%3A%22eyJvIjoiLXNjb3JlLGlkIiwidiI6ImFRSUFBQUFBQUFBQWFRMHBJUUVBQUFBQSJ9%22%2C%22size%22%3A50%7D&sort="	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/trigger_categories")		.newBuilder()		.addQueryParameter("include", "")		.addQueryParameter("page", "{"after":"eyJvIjoiLXNjb3JlLGlkIiwidiI6ImFRSUFBQUFBQUFBQWFRMHBJUUVBQUFBQSJ9","before":"eyJvIjoiLXNjb3JlLGlkIiwidiI6ImFRSUFBQUFBQUFBQWFRMHBJUUVBQUFBQSJ9","size":50}")		.addQueryParameter("sort", "");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**JavaScript**

This example provides an example query with pagination parameters in JavaScript.


    fetch("https://{subdomain}.zendesk.com/api/v2/trigger_categories?include=rule_counts&page[size]=10&page[after]=eyJvIjoiLXNjb3JlLGlkIiwidiI6ImFRSUFBQUFBQUFBQWFRMHBJUUVBQUFBQSJ9", {  "method": "GET",  "headers": {}}).then(response => {  // do stuff with successful response}).catch(err => {  // do stuff with failed response});

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/trigger_categories',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'include': '',    'page': '%7B%22after%22%3A%22eyJvIjoiLXNjb3JlLGlkIiwidiI6ImFRSUFBQUFBQUFBQWFRMHBJUUVBQUFBQSJ9%22%2C%22before%22%3A%22eyJvIjoiLXNjb3JlLGlkIiwidiI6ImFRSUFBQUFBQUFBQWFRMHBJUUVBQUFBQSJ9%22%2C%22size%22%3A50%7D',    'sort': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/trigger_categories?include=&page=%7B%22after%22%3A%22eyJvIjoiLXNjb3JlLGlkIiwidiI6ImFRSUFBQUFBQUFBQWFRMHBJUUVBQUFBQSJ9%22%2C%22before%22%3A%22eyJvIjoiLXNjb3JlLGlkIiwidiI6ImFRSUFBQUFBQUFBQWFRMHBJUUVBQUFBQSJ9%22%2C%22size%22%3A50%7D&sort="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/trigger_categories")uri.query = URI.encode_www_form("include": "", "page": "{"after":"eyJvIjoiLXNjb3JlLGlkIiwidiI6ImFRSUFBQUFBQUFBQWFRMHBJUUVBQUFBQSJ9","before":"eyJvIjoiLXNjb3JlLGlkIiwidiI6ImFRSUFBQUFBQUFBQWFRMHBJUUVBQUFBQSJ9","size":50}", "sort": "")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "links": {    "next": "https://{subdomain}.zendesk.com/api/v2/trigger_categories?include=rule_counts&page[after]=eyJvIjoiLXNjb3JlLGlkIiwidiI6ImFRSUFBQUFBQUFBQWFRMHBJUUVBQUFBQSJ9&page[size]=2&sort=position",    "prev": "https://{subdomain}.zendesk.com/api/v2/trigger_categories?include=rule_counts&page[before]=eyJvIjoiLXNjb3JlLGlkIiwidiI6ImFRSUFBQUFBQUFBQWFRMHBJUUVBQUFBQSJ9&page[size]=2&sort=position"  },  "meta": {    "after_cursor": "eyJvIjoiLXNjb3JlLGlkIiwidiI6ImFRSUFBQUFBQUFBQWFRMHBJUUVBQUFBQSJ9",    "before_cursor": "eyJvIjoiLXNjb3JlLGlkIiwidiI6ImFRSUFBQUFBQUFBQWFRMHBJUUVBQUFBQSJ9",    "has_more": true  },  "trigger_categories": [    {      "created_at": "2020-07-17T01:30:07Z",      "id": "10001",      "name": "Email Triggers",      "position": 0,      "updated_at": "2020-07-17T01:30:07Z"    },    {      "created_at": "2020-07-17T01:30:07Z",      "id": "10002",      "name": "SMS Triggers",      "position": 1,      "updated_at": "2020-07-17T01:30:07Z"    }  ]}

**400 Bad Request**


    // Status 400 Bad Request
    {  "errors": [    {      "code": "InvalidPaginationParameter",      "title": "page[after] is not valid"    }  ]}

**403 Forbidden**


    // Status 403 Forbidden
    {  "errors": [    {      "code": "TriggerCategoriesNotEnabled",      "title": "Ticket trigger categories are not enabled for your account"    }  ]}

### Create Ticket Trigger Category

  * `POST /api/v2/trigger_categories`


Creates a ticket trigger category.

#### Example body


    {  "trigger_category": {    "name": "All Notification Triggers",    "position": 0  }}

#### Code Samples

**cURL**

This example provides an example ticket trigger category POST request with cURL.


    curl -u {email_address}/token:{api_token} -X POST \  --url https://{subdomain}.zendesk.com/api/v2/trigger_categories \  -H 'content-type: application/json' \  -d '{  "trigger_category": {    "name": "Example Category",    "position": 10  }}'

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://example.zendesk.com/api/v2/trigger_categories"	method := "POST"	payload := strings.NewReader(`{  "trigger_category": {    "name": "All Notification Triggers",    "position": 0  }}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/trigger_categories")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"trigger_category\": {    \"name\": \"All Notification Triggers\",    \"position\": 0  }}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**JavaScript**

This example provides an example ticket trigger category POST request in JavaScript.


    fetch("https://{subdomain}.zendesk.com/api/v2/trigger_categories", {  "method": "POST",  "headers": {    "content-type": "application/json"  },  "body": {    "trigger_category": {      "name": "Example Category",      "position": 10    }  }}).then(response => {  // do stuff with successful response}).catch(err => {  // do stuff with failed response});

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "trigger_category": {    "name": "All Notification Triggers",    "position": 0  }});
    var config = {  method: 'POST',  url: 'https://example.zendesk.com/api/v2/trigger_categories',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/trigger_categories"
    payload = json.loads("""{  "trigger_category": {    "name": "All Notification Triggers",    "position": 0  }}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/trigger_categories")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")request.body = %q({  "trigger_category": {    "name": "All Notification Triggers",    "position": 0  }})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "trigger_category": {    "created_at": "2020-07-17T01:30:07Z",    "id": "10001",    "name": "All Notification Triggers",    "position": 0,    "updated_at": "2020-07-17T01:30:07Z"  }}

**400 Bad Request**


    // Status 400 Bad Request
    {  "errors": [    {      "code": "InvalidTriggerCategory",      "title": "Name cannot be blank"    }  ]}

**403 Forbidden**


    // Status 403 Forbidden
    {  "errors": [    {      "code": "TriggerCategoriesNotEnabled",      "title": "Ticket trigger categories are not enabled for your account"    },    {      "code": "ProductLimitExceeded",      "title": "Your account has reached the limit of 500 ticket trigger categories."    }  ]}

### Create Batch Job for Ticket Trigger Categories

  * `POST /api/v2/trigger_categories/jobs`


Creates a job that performs a batch operation for the given ticket trigger categories.

#### Example body


    {  "job": {    "action": "patch",    "items": {      "trigger_categories": [        {          "id": "10001",          "position": 0        },        {          "id": "10002",          "position": 1        }      ],      "triggers": [        {          "active": false,          "category_id": "10001",          "id": "10011",          "position": 10        },        {          "active": true,          "category_id": "10002",          "id": "10012",          "position": 1        }      ]    }  }}

#### Code Samples

**cURL**

This example provides an example request for batch operating on existing ticket trigger categories with cURL.


    curl -u {email_address}/token:{api_token} -X POST \  --url https://{subdomain}.zendesk.com/api/v2/trigger_categories/jobs \  -H 'content-type: application/json' \  -d '{  "job": {    "action": "patch",    "items": {      "trigger_categories": [        {          "id": "10001",          "position": 20        },        {          "id": "10002",          "position": 21        }      ],      "triggers": [        {          "id": "10011",          "position": 10,          "active": false,          "category_id": "10001"        },        {          "id": "10012",          "position": 1,          "active": true,          "category_id": "10002"        }      ]    }  }}'

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://example.zendesk.com/api/v2/trigger_categories/jobs"	method := "POST"	payload := strings.NewReader(`{  "job": {    "action": "patch",    "items": {      "trigger_categories": [        {          "id": "10001",          "position": 0        },        {          "id": "10002",          "position": 1        }      ],      "triggers": [        {          "active": false,          "category_id": "10001",          "id": "10011",          "position": 10        },        {          "active": true,          "category_id": "10002",          "id": "10012",          "position": 1        }      ]    }  }}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/trigger_categories/jobs")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"job\": {    \"action\": \"patch\",    \"items\": {      \"trigger_categories\": [        {          \"id\": \"10001\",          \"position\": 0        },        {          \"id\": \"10002\",          \"position\": 1        }      ],      \"triggers\": [        {          \"active\": false,          \"category_id\": \"10001\",          \"id\": \"10011\",          \"position\": 10        },        {          \"active\": true,          \"category_id\": \"10002\",          \"id\": \"10012\",          \"position\": 1        }      ]    }  }}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**JavaScript**

This example provides an example request for batch operating on existing ticket trigger categories in JavaScript.


    fetch("https://{subdomain}.zendesk.com/api/v2/trigger_categories/jobs", {  "method": "POST",  "headers": {    "content-type": "application/json"  },  "body": {    "job": {      "action": "patch",      "items": {        "trigger_categories": [          {            "id": "10001",            "position": 20          },          {            "id": "10002",            "position": 21          }        ],        "triggers": [          {            "id": "10011",            "position": 10,            "active": false,            "category_id": "10001"          },          {            "id": "10012",            "position": 1,            "active": true,            "category_id": "10002"          }        ]      }    }  }}).then(response => {  // do stuff with successful response}).catch(err => {  // do stuff with failed response});

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "job": {    "action": "patch",    "items": {      "trigger_categories": [        {          "id": "10001",          "position": 0        },        {          "id": "10002",          "position": 1        }      ],      "triggers": [        {          "active": false,          "category_id": "10001",          "id": "10011",          "position": 10        },        {          "active": true,          "category_id": "10002",          "id": "10012",          "position": 1        }      ]    }  }});
    var config = {  method: 'POST',  url: 'https://example.zendesk.com/api/v2/trigger_categories/jobs',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/trigger_categories/jobs"
    payload = json.loads("""{  "job": {    "action": "patch",    "items": {      "trigger_categories": [        {          "id": "10001",          "position": 0        },        {          "id": "10002",          "position": 1        }      ],      "triggers": [        {          "active": false,          "category_id": "10001",          "id": "10011",          "position": 10        },        {          "active": true,          "category_id": "10002",          "id": "10012",          "position": 1        }      ]    }  }}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/trigger_categories/jobs")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")request.body = %q({  "job": {    "action": "patch",    "items": {      "trigger_categories": [        {          "id": "10001",          "position": 0        },        {          "id": "10002",          "position": 1        }      ],      "triggers": [        {          "active": false,          "category_id": "10001",          "id": "10011",          "position": 10        },        {          "active": true,          "category_id": "10002",          "id": "10012",          "position": 1        }      ]    }  }})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "results": {    "trigger_categories": [      {        "created_at": "2020-07-18T01:24:53Z",        "id": "10001",        "name": "Notifications",        "position": 0,        "updated_at": "2020-07-20T01:30:07Z"      },      {        "created_at": "2020-07-17T06:31:12Z",        "id": "10002",        "name": "Apply Tags",        "position": 1,        "updated_at": "2020-07-20T01:30:07Z"      }    ],    "triggers": [      {        "actions": [          {}        ],        "active": true,        "conditions": {},        "created_at": "2012-09-25T22:50:26Z",        "description": "Notify external target",        "id": 10012,        "position": 1,        "raw_title": "Notify target",        "title": "Notify Target",        "updated_at": "2020-07-20T01:30:07Z",        "url": "http://{subdomain}.zendesk.com/api/v2/triggers/10012"      },      {        "actions": [          {}        ],        "active": false,        "conditions": {},        "created_at": "2012-09-25T22:50:26Z",        "description": "Close and save a ticket",        "id": 10011,        "position": 10,        "raw_title": "Close and Save",        "title": "Close and Save",        "updated_at": "2020-07-20T01:30:07Z",        "url": "http://{subdomain}.zendesk.com/api/v2/triggers/10011"      }    ]  },  "status": "complete"}

**400 Bad Request**


    // Status 400 Bad Request
    {  "errors": [    {      "code": "InvalidTrigger",      "title": "category_id is not valid",      "trigger_id": "10001"    }  ],  "status": "failed"}

### Show Ticket Trigger Category

  * `GET /api/v2/trigger_categories/{trigger_category_id}`


Returns the ticket trigger category with the specified ID.

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
trigger_category_id| string| Path| true| The id of the ticket trigger category to retrieve

#### Code Samples

**cURL**

This example provides an example request for an existing ticket trigger category with cURL.


    curl -u {email_address}/token:{api_token} -X GET \  --url https://{subdomain}.zendesk.com/api/v2/trigger_categories/10001

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/trigger_categories/10001"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/trigger_categories/10001")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**JavaScript**

This example provides an example request for an existing ticket trigger category in JavaScript.


    fetch("https://{subdomain}.zendesk.com/api/v2/trigger_categories/10001", {  "method": "GET",  "headers": {}}).then(response => {  // do stuff with successful response}).catch(err => {  // do stuff with failed response});

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/trigger_categories/10001',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/trigger_categories/10001"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/trigger_categories/10001")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "trigger_category": {    "created_at": "2020-07-17T01:30:07Z",    "id": "10001",    "name": "All Notification Triggers",    "position": 0,    "updated_at": "2020-07-17T01:30:07Z"  }}

**404 Not Found**


    // Status 404 Not Found
    {  "errors": [    {      "code": "TriggerCategoryNotFound",      "title": "Category canât be found. Check the ID and try again."    }  ]}

### Update Ticket Trigger Category

  * `PATCH /api/v2/trigger_categories/{trigger_category_id}`


Updates the ticket trigger category with the specified ID.

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
trigger_category_id| string| Path| true| The id of the ticket trigger category to update

#### Example body


    {  "trigger_category": {    "name": "All Notification Triggers Updated",    "position": 10  }}

#### Code Samples

**cURL**

This example provides an example request for updating an existing ticket trigger category with cURL.


    curl -u {email_address}/token:{api_token} -X PATCH \  --url https://{subdomain}.zendesk.com/api/v2/trigger_categories/10001 \  -H 'content-type: application/json' \  -d '{  "trigger_category": {    "name": "Example Category Updated"  }}'

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://example.zendesk.com/api/v2/trigger_categories/10001"	method := "PATCH"	payload := strings.NewReader(`{  "trigger_category": {    "name": "All Notification Triggers Updated",    "position": 10  }}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/trigger_categories/10001")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"trigger_category\": {    \"name\": \"All Notification Triggers Updated\",    \"position\": 10  }}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PATCH", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**JavaScript**

This example provides an example request for updating an existing ticket trigger category in JavaScript.


    fetch("https://{subdomain}.zendesk.com/api/v2/trigger_categories/10001", {  "method": "PATCH",  "headers": {    "content-type": "application/json"  },  "body": {    "trigger_category": {      "name": "Example Category Updated"    }  }}).then(response => {  // do stuff with successful response}).catch(err => {  // do stuff with failed response});

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "trigger_category": {    "name": "All Notification Triggers Updated",    "position": 10  }});
    var config = {  method: 'PATCH',  url: 'https://example.zendesk.com/api/v2/trigger_categories/10001',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/trigger_categories/10001"
    payload = json.loads("""{  "trigger_category": {    "name": "All Notification Triggers Updated",    "position": 10  }}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PATCH",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/trigger_categories/10001")request = Net::HTTP::Patch.new(uri, "Content-Type": "application/json")request.body = %q({  "trigger_category": {    "name": "All Notification Triggers Updated",    "position": 10  }})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "trigger_category": {    "created_at": "2020-07-17T01:30:07Z",    "id": "10001",    "name": "All Notification Triggers Updated",    "position": 10,    "updated_at": "2020-07-18T05:23:32Z"  }}

**400 Bad Request**


    // Status 400 Bad Request
    {  "errors": [    {      "code": "InvalidTriggerCategory",      "title": "Name cannot be blank"    }  ]}

**404 Not Found**


    // Status 404 Not Found
    {  "errors": [    {      "code": "TriggerCategoryNotFound",      "title": "Category canât be found. Check the ID and try again."    }  ]}

### Delete Ticket Trigger Category

  * `DELETE /api/v2/trigger_categories/{trigger_category_id}`


Deletes the ticket trigger category with the specified ID.

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
trigger_category_id| string| Path| true| The id of the ticket trigger category to delete

#### Code Samples

**cURL**

This example provides an example request for deleting an existing ticket trigger category with cURL.


    curl -u {email_address}/token:{api_token} -X DELETE \  --url https://{subdomain}.zendesk.com/api/v2/trigger_categories/10001

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/trigger_categories/10001"	method := "DELETE"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/trigger_categories/10001")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("DELETE", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**JavaScript**

This example provides an example request for deleting an existing ticket trigger category in JavaScript.


    fetch("https://{subdomain}.zendesk.com/api/v2/trigger_categories/10001", {  "method": "DELETE",  "headers": {}}).then(response => {  // do stuff with successful response}).catch(err => {  // do stuff with failed response});

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'DELETE',  url: 'https://example.zendesk.com/api/v2/trigger_categories/10001',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/trigger_categories/10001"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"DELETE",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/trigger_categories/10001")request = Net::HTTP::Delete.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**204 No Content**


    // Status 204 No Content
    null

**400 Bad Request**


    // Status 400 Bad Request
    {  "errors": [    {      "code": "TriggerCategoryNotEmpty",      "title": "A category with active ticket triggers cannot be deleted."    }  ]}

**404 Not Found**


    // Status 404 Not Found
    {  "errors": [    {      "code": "TriggerCategoryNotFound",      "title": "Category canât be found. Check the ID and try again."    }  ]}

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)