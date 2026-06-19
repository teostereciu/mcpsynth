# Task List Templates

*Source: https://developer.zendesk.com/api-reference/ticketing/tasks/task_list_templates/*

---

## On this page

  * [JSON format](/api-reference/ticketing/tasks/task_list_templates/#json-format)
  * [List Task List Templates](/api-reference/ticketing/tasks/task_list_templates/#list-task-list-templates)
  * [Show Task List Template](/api-reference/ticketing/tasks/task_list_templates/#show-task-list-template)
  * [Create Task List Template](/api-reference/ticketing/tasks/task_list_templates/#create-task-list-template)
  * [Update Task List Template](/api-reference/ticketing/tasks/task_list_templates/#update-task-list-template)
  * [Delete Task List Template](/api-reference/ticketing/tasks/task_list_templates/#delete-task-list-template)
  * [Get Tasks by Task List Template Id](/api-reference/ticketing/tasks/task_list_templates/#get-tasks-by-task-list-template-id)


# Task List Templates

## On this page

  * [JSON format](/api-reference/ticketing/tasks/task_list_templates/#json-format)
  * [List Task List Templates](/api-reference/ticketing/tasks/task_list_templates/#list-task-list-templates)
  * [Show Task List Template](/api-reference/ticketing/tasks/task_list_templates/#show-task-list-template)
  * [Create Task List Template](/api-reference/ticketing/tasks/task_list_templates/#create-task-list-template)
  * [Update Task List Template](/api-reference/ticketing/tasks/task_list_templates/#update-task-list-template)
  * [Delete Task List Template](/api-reference/ticketing/tasks/task_list_templates/#delete-task-list-template)
  * [Get Tasks by Task List Template Id](/api-reference/ticketing/tasks/task_list_templates/#get-tasks-by-task-list-template-id)


Task list templates are pre-defined lists of up to 20 tasks, or actions, that are required in common situations. These templates are created and maintained by admins and then agents can add an appropriate task list to tickets directly in the Agent Workspace.

Within the Task Lists API, the task lists that are defined by admins are referred to as _task list templates_ , the instances of task lists that agents add to tickets are referred to as _task lists_. The items within a task list and template are referred to as _tasks_.

### JSON format

Task List Templates are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
created_at| string| true| false| The time the task list template was created
description| string| false| false| The description of the task list template
id| string| true| false| Automatically assigned when the task list template is created
is_active| boolean| false| false| TWhether the task list template is active and available for use by agents, or inactive and unavailable for use
name| string| false| true| The name of the task list template
task_count| integer| true| false| The number of tasks in the task list template
tasks| array| false| false| The tasks for the task list template. Only present for some endpoints.
updated_at| string| true| false| The time the task list template was last updated
url| string| true| false| URL of the task list template

#### Example


    {  "created_at": "2025-08-06T17:08:40Z",  "description": "Complete HR, IT, and payroll setup for new employees.",  "id": "01K205PG0J2ET0B8AFHA106C1E",  "is_active": true,  "name": "Onboarding checklist",  "task_count": 2,  "tasks": [    {      "created_at": "2025-08-06T17:08:40Z",      "description": "Ensure the employee has signed and returned all required documents before proceeding.",      "id": "01K3KVF20JE2QNA47FY6HJWQKB",      "name": "Verify signed offer letter and contract",      "position": 1,      "required": true,      "updated_at": "2025-08-06T17:08:40Z"    },    {      "created_at": "2025-08-06T17:08:40Z",      "description": "Submit the background check request and verify employee eligibility before onboarding.",      "id": "01K3KVF23JWZ5M98BJBQHENYZ9",      "name": "Initiate background check",      "position": 2,      "required": false,      "updated_at": "2025-08-06T17:08:40Z"    }  ],  "updated_at": "2025-08-06T17:08:40Z"}

### List Task List Templates

  * `GET /api/v2/task_list_templates`


Lists all task list templates. The template's tasks aren't included in the response.

#### Allowed For

  * Agents


#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/task_list_templates.json \  -H "Content-Type: application/json" \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/task_list_templates"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/task_list_templates")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/task_list_templates',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/task_list_templates"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/task_list_templates")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "links": {    "next": "https://{subdomain}.zendesk.com/api/v2/task_list_templates?page%5Bafter%5D=eyJvIjoiLV9zY29yZSwtaWQiLCJ2IjoiYVFFQUFBQUFBQUFBY3hvQUFBQXdNVXRDUmxsWVJVc3lORUkzVVRCRVEwdEVXa1ZSTkRWQ1RRIn0",    "prev": null  },  "meta": {    "after_cursor": "eyJvIjoiLV9zY29yZSwtaWQiLCJ2IjoiYVFFQUFBQUFBQUFBY3hvQUFBQXdNVXRDUmxsWVJVc3lORUkzVVRCRVEwdEVXa1ZSTkRWQ1RRIn0",    "before_cursor": null,    "has_more": true  },  "task_list_templates": [    {      "created_at": "2025-08-06T17:08:40Z",      "description": "Complete HR, IT, and payroll setup for new employees.",      "id": "01K205PG0J2ET0B8AFHA106C1E",      "is_active": true,      "name": "Onboarding checklist",      "task_count": 2,      "updated_at": "2025-08-06T17:08:40Z",      "url": "https://{subdomain}.zendesk.com/api/v2/task_list_templates/01K205PG0J2ET0B8AFHA106C1E.json"    },    {      "created_at": "2025-08-06T17:08:40Z",      "description": "Close out access, collect all equipment, and wrap up HR steps for departing.",      "id": "01K3KV7834EFJPHQC2VFXKSYGN",      "is_active": true,      "name": "Offboarding checklist",      "task_count": 3,      "updated_at": "2026-01-12T18:31:19Z",      "url": "https://{subdomain}.zendesk.com/api/v2/task_list_templates/01K3KV7834EFJPHQC2VFXKSYGN.json"    }  ]}

### Show Task List Template

  * `GET /api/v2/task_list_templates/{task_list_template_id}`


Returns the task list template with the specified id. The template's tasks aren't included in the response.

#### Allowed For

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
task_list_template_id| string| Path| true| The id of the task list template

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/task_list_templates.json \  -H "Content-Type: application/json" \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/task_list_templates/01K205PG0J2ET0B8AFHA106C1E"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/task_list_templates/01K205PG0J2ET0B8AFHA106C1E")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/task_list_templates/01K205PG0J2ET0B8AFHA106C1E',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/task_list_templates/01K205PG0J2ET0B8AFHA106C1E"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/task_list_templates/01K205PG0J2ET0B8AFHA106C1E")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "task_list_template": {    "created_at": "2025-08-06T17:08:40Z",    "description": "Complete HR, IT, and payroll setup for new employees.",    "id": "01K205PG0J2ET0B8AFHA106C1E",    "is_active": true,    "name": "Onboarding checklist",    "task_count": 2,    "updated_at": "2025-08-06T17:08:40Z",    "url": "https://{subdomain}.zendesk.com/api/v2/task_list_templates/01K205PG0J2ET0B8AFHA106C1E.json"  }}

### Create Task List Template

  * `POST /api/v2/task_list_templates`


Creates a task list template.

#### Allowed For

  * Admins


#### Example body


    {  "task_list_template": {    "description": "Complete HR, IT, and payroll setup for new employees.",    "name": "Onboarding checklist",    "tasks": [      {        "description": "Ensure the employee has signed and returned all required documents before proceeding.",        "name": "Verify signed offer letter and contract",        "required": true      },      {        "description": "Submit the background check request and verify employee eligibility before onboarding.",        "name": "Initiate background check"      }    ]  }}

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/task_list_templates.json \  -H "Content-Type: application/json"  -d '{    "task_list_template": {      "name": "Onboarding checklist",      "description": "Complete HR, IT, and payroll setup for new employees.",      "tasks": [        { "name": "Verify signed offer letter & contract", "description": "Ensure the employee has signed and returned all required documents before proceeding." },        { "name": "Initiate background check", "description": "Submit the background check request and verify employee eligibility before onboarding."}      ]    }' \  -v -u {email_address}/token:{api_token} -X POST

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://example.zendesk.com/api/v2/task_list_templates"	method := "POST"	payload := strings.NewReader(`{  "task_list_template": {    "description": "Complete HR, IT, and payroll setup for new employees.",    "name": "Onboarding checklist",    "tasks": [      {        "description": "Ensure the employee has signed and returned all required documents before proceeding.",        "name": "Verify signed offer letter and contract",        "required": true      },      {        "description": "Submit the background check request and verify employee eligibility before onboarding.",        "name": "Initiate background check"      }    ]  }}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/task_list_templates")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"task_list_template\": {    \"description\": \"Complete HR, IT, and payroll setup for new employees.\",    \"name\": \"Onboarding checklist\",    \"tasks\": [      {        \"description\": \"Ensure the employee has signed and returned all required documents before proceeding.\",        \"name\": \"Verify signed offer letter and contract\",        \"required\": true      },      {        \"description\": \"Submit the background check request and verify employee eligibility before onboarding.\",        \"name\": \"Initiate background check\"      }    ]  }}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "task_list_template": {    "description": "Complete HR, IT, and payroll setup for new employees.",    "name": "Onboarding checklist",    "tasks": [      {        "description": "Ensure the employee has signed and returned all required documents before proceeding.",        "name": "Verify signed offer letter and contract",        "required": true      },      {        "description": "Submit the background check request and verify employee eligibility before onboarding.",        "name": "Initiate background check"      }    ]  }});
    var config = {  method: 'POST',  url: 'https://example.zendesk.com/api/v2/task_list_templates',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/task_list_templates"
    payload = json.loads("""{  "task_list_template": {    "description": "Complete HR, IT, and payroll setup for new employees.",    "name": "Onboarding checklist",    "tasks": [      {        "description": "Ensure the employee has signed and returned all required documents before proceeding.",        "name": "Verify signed offer letter and contract",        "required": true      },      {        "description": "Submit the background check request and verify employee eligibility before onboarding.",        "name": "Initiate background check"      }    ]  }}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/task_list_templates")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")request.body = %q({  "task_list_template": {    "description": "Complete HR, IT, and payroll setup for new employees.",    "name": "Onboarding checklist",    "tasks": [      {        "description": "Ensure the employee has signed and returned all required documents before proceeding.",        "name": "Verify signed offer letter and contract",        "required": true      },      {        "description": "Submit the background check request and verify employee eligibility before onboarding.",        "name": "Initiate background check"      }    ]  }})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**201 Created**


    // Status 201 Created
    {  "task_list_template": {    "created_at": "2025-08-26T18:50:21Z",    "description": "Complete HR, IT, and payroll setup for new employees.",    "id": "01K205PG0J2ET0B8AFHA106C1E",    "is_active": true,    "name": "Onboarding checklist",    "task_count": 2,    "tasks": [      {        "created_at": "2025-08-26T18:50:21Z",        "description": "Ensure the employee has signed and returned all required documents before proceeding.",        "id": "01K3KVF20JE2QNA47FY6HJWQKB",        "name": "Verify signed offer letter and contract",        "position": 1,        "required": true,        "updated_at": "2025-08-26T18:50:21Z"      },      {        "created_at": "2025-08-26T18:50:21Z",        "description": "Submit the background check request and verfiy employee elgibility before onboarding.",        "id": "01K3KVF23JWZ5M98BJBQHENYZ9",        "name": "Initiate background check",        "position": 2,        "required": false,        "updated_at": "2025-08-26T18:50:21Z"      }    ],    "updated_at": "2025-08-26T18:50:21Z",    "url": "https://{subdomain}.zendesk.com/api/v2/task_list_templates/01K205PG0J2ET0B8AFHA106C1E.json"  }}

### Update Task List Template

  * `PUT /api/v2/task_list_templates/{task_list_template_id}`


Creates, modifies, or deletes tasks in a task list template. Only the tasks included in the `task_list_template` object in the request are updated. Tasks that aren't specified in the request are unchanged.

#### Allowed For

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
task_list_template_id| string| Path| true| The id of the task list template

#### Example body


    {  "task_list_template": {    "name": "Updating a task list template",    "tasks": [      {        "description": "Updating a task's description",        "id": "01K3KVF20JE2QNA47FY6HJWQKB"      },      {        "_destroy": true,        "id": "01K3KVF23JWZ5M98BJBQHENYZ9"      },      {        "description": "A new task",        "name": "New task"      }    ]  }}

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/task_list_templates/{task_list_template_id}.json \  -H "Content-Type: application/json" \  -d '{    "task_list_template": {      "name": "Updating a task list template",      "tasks": [        { "id": "01K3KVF20JE2QNA47FY6HJWQKB", "description": "Updating a task's description" },        { "id": "01K3KVF23JWZ5M98BJBQHENYZ9", "_destroy": true },        { "name": "New task", "description": "A new task" },      ]    }' \  -v -u {email_address}/token:{api_token} -X PUT

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://example.zendesk.com/api/v2/task_list_templates/01K205PG0J2ET0B8AFHA106C1E"	method := "PUT"	payload := strings.NewReader(`{  "task_list_template": {    "name": "Updating a task list template",    "tasks": [      {        "description": "Updating a task's description",        "id": "01K3KVF20JE2QNA47FY6HJWQKB"      },      {        "_destroy": true,        "id": "01K3KVF23JWZ5M98BJBQHENYZ9"      },      {        "description": "A new task",        "name": "New task"      }    ]  }}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/task_list_templates/01K205PG0J2ET0B8AFHA106C1E")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"task_list_template\": {    \"name\": \"Updating a task list template\",    \"tasks\": [      {        \"description\": \"Updating a task's description\",        \"id\": \"01K3KVF20JE2QNA47FY6HJWQKB\"      },      {        \"_destroy\": true,        \"id\": \"01K3KVF23JWZ5M98BJBQHENYZ9\"      },      {        \"description\": \"A new task\",        \"name\": \"New task\"      }    ]  }}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "task_list_template": {    "name": "Updating a task list template",    "tasks": [      {        "description": "Updating a task's description",        "id": "01K3KVF20JE2QNA47FY6HJWQKB"      },      {        "_destroy": true,        "id": "01K3KVF23JWZ5M98BJBQHENYZ9"      },      {        "description": "A new task",        "name": "New task"      }    ]  }});
    var config = {  method: 'PUT',  url: 'https://example.zendesk.com/api/v2/task_list_templates/01K205PG0J2ET0B8AFHA106C1E',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/task_list_templates/01K205PG0J2ET0B8AFHA106C1E"
    payload = json.loads("""{  "task_list_template": {    "name": "Updating a task list template",    "tasks": [      {        "description": "Updating a task's description",        "id": "01K3KVF20JE2QNA47FY6HJWQKB"      },      {        "_destroy": true,        "id": "01K3KVF23JWZ5M98BJBQHENYZ9"      },      {        "description": "A new task",        "name": "New task"      }    ]  }}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/task_list_templates/01K205PG0J2ET0B8AFHA106C1E")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")request.body = %q({  "task_list_template": {    "name": "Updating a task list template",    "tasks": [      {        "description": "Updating a task's description",        "id": "01K3KVF20JE2QNA47FY6HJWQKB"      },      {        "_destroy": true,        "id": "01K3KVF23JWZ5M98BJBQHENYZ9"      },      {        "description": "A new task",        "name": "New task"      }    ]  }})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "task_list_template": {    "created_at": "2025-08-26T18:50:21Z",    "description": "Complete HR, IT, and payroll setup for new employees.",    "id": "01K205PG0J2ET0B8AFHA106C1E",    "is_active": true,    "name": "Onboarding checklist",    "task_count": 2,    "tasks": [      {        "created_at": "2025-08-26T18:50:21Z",        "description": "Ensure the employee has signed and returned all required documents before proceeding.",        "id": "01K3KVF20JE2QNA47FY6HJWQKB",        "name": "Verify signed offer letter and contract",        "position": 1,        "required": true,        "updated_at": "2025-08-26T18:50:21Z"      },      {        "created_at": "2025-08-26T18:50:21Z",        "description": "Submit the background check request and verfiy employee elgibility before onboarding.",        "id": "01K3KVF23JWZ5M98BJBQHENYZ9",        "name": "Initiate background check",        "position": 2,        "required": false,        "updated_at": "2025-08-26T18:50:21Z"      }    ],    "updated_at": "2025-08-26T18:50:21Z",    "url": "https://{subdomain}.zendesk.com/api/v2/task_list_templates/01K205PG0J2ET0B8AFHA106C1E.json"  }}

### Delete Task List Template

  * `DELETE /api/v2/task_list_templates/{task_list_template_id}`


Deletes a task list template with the specified id.

#### Allowed For

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
task_list_template_id| string| Path| true| The id of the task list template

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/task_list_templates/{task_list_template_id}.json \  -H "Content-Type: application/json" \  -v -u {email_address}/token:{api_token} -X DELETE

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/task_list_templates/01K205PG0J2ET0B8AFHA106C1E"	method := "DELETE"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/task_list_templates/01K205PG0J2ET0B8AFHA106C1E")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("DELETE", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'DELETE',  url: 'https://example.zendesk.com/api/v2/task_list_templates/01K205PG0J2ET0B8AFHA106C1E',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/task_list_templates/01K205PG0J2ET0B8AFHA106C1E"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"DELETE",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/task_list_templates/01K205PG0J2ET0B8AFHA106C1E")request = Net::HTTP::Delete.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**204 No Content**


    // Status 204 No Content
    null

### Get Tasks by Task List Template Id

  * `GET /api/v2/task_list_templates/{task_list_template_id}/tasks`


Returns the tasks for the specified task list template.

#### Allowed For

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
task_list_template_id| string| Path| true| The id of the task list template

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/task_list_templates/{task_list_template_id}/tasks.json \  -H "Content-Type: application/json" \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/task_list_templates/01K205PG0J2ET0B8AFHA106C1E/tasks"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/task_list_templates/01K205PG0J2ET0B8AFHA106C1E/tasks")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/task_list_templates/01K205PG0J2ET0B8AFHA106C1E/tasks',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/task_list_templates/01K205PG0J2ET0B8AFHA106C1E/tasks"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/task_list_templates/01K205PG0J2ET0B8AFHA106C1E/tasks")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "count": 2,  "next_page": null,  "previous_page": null,  "tasks": [    {      "created_at": "2025-08-26T18:50:21Z",      "description": "Ensure the employee has signed and returned all required documents before proceeding.",      "id": "01K3KVF20JE2QNA47FY6HJWQKB",      "name": "Verify signed offer letter and contract",      "position": 1,      "required": false,      "updated_at": "2025-08-26T18:50:21Z"    },    {      "created_at": "2025-08-26T18:50:21Z",      "description": "Submit the background check request and verfiy employee elgibility before onboarding.",      "id": "01K3KVF23JWZ5M98BJBQHENYZ9",      "name": "Initiate background check",      "position": 2,      "required": false,      "updated_at": "2025-08-26T18:50:21Z"    }  ]}

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)