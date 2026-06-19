# Task Lists

*Source: https://developer.zendesk.com/api-reference/ticketing/tasks/task_lists/*

---

## On this page

  * [JSON format](/api-reference/ticketing/tasks/task_lists/#json-format)
  * [Show Task List](/api-reference/ticketing/tasks/task_lists/#show-task-list)
  * [Create Task List](/api-reference/ticketing/tasks/task_lists/#create-task-list)


# Task Lists

## On this page

  * [JSON format](/api-reference/ticketing/tasks/task_lists/#json-format)
  * [Show Task List](/api-reference/ticketing/tasks/task_lists/#show-task-list)
  * [Create Task List](/api-reference/ticketing/tasks/task_lists/#create-task-list)


Task lists are copies of task list templates that are added to tickets directly in the Agent Workspace. The task list templates are created and maintained by admins with pre-defined lists of tasks that are required in common situations. When a task list is added to a ticket, agents can check off the tasks as they complete them without leaving the ticket interface and without affecting the task list template.

Within the Task Lists API, the task lists that are defined by admins are referred to as _task list templates_ , and the instances of task lists that agents add to tickets are referred to as _task lists_. The items within a task list and template are referred to as _tasks_.

### JSON format

Task Lists are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
created_at| string| true| false| The time the task list was created
description| string| true| false| The description of the task list
id| string| true| false| Automatically assigned when a task list template is added to a ticket, creating the task list
name| string| true| true| The name of the task list
task_count| integer| true| false| The number of tasks in the task list
task_list_template_id| string| true| true| The ID of the task list template that the task list was created from
ticket_id| string| true| true| The ID of the ticket that the task list is attached to
updated_at| string| true| false| The time the task list was last updated

#### Example


    {  "created_at": "2025-08-06T17:08:40Z",  "description": "Complete HR, IT, and payroll setup for new employees.",  "id": "01KFGZJGMQ3NA9DNX34Y5YGGYM",  "name": "Onboarding checklist",  "task_count": 2,  "task_list_template_id": "01K205PG0J2ET0B8AFHA106C1E",  "ticket_id": "1",  "updated_at": "2025-08-06T17:08:40Z"}

### Show Task List

  * `GET /api/v2/tickets/{ticket_id}/task_lists`


Returns the task list attached to the specified ticket. If the ticket doesn't have a task list, an empty array is returned.

#### Allowed For

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
ticket_id| integer| Path| true| The ID of the ticket

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/tickets/{ticket_id}/task_lists.json \  -H "Content-Type: application/json" \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/tickets/123456/task_lists"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/tickets/123456/task_lists")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/tickets/123456/task_lists',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/tickets/123456/task_lists"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/tickets/123456/task_lists")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "count": 1,  "next_page": null,  "previous_page": null,  "task_lists": [    {      "created_at": "2025-08-06T17:08:40Z",      "description": "Complete HR, IT, and payroll setup for new employees.",      "id": "01K3KVF23JWZ5M98BJBQHENYZ9",      "name": "Onboarding checklist",      "task_count": 2,      "task_list_template_id": "01K205PG0J2ET0B8AFHA106C1E",      "ticket_id": "1",      "updated_at": "2025-08-06T17:08:40Z"    }  ]}

### Create Task List

  * `POST /api/v2/tickets/{ticket_id}/task_lists`


Adds a task list to the specified ticket.

#### Allowed For

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
ticket_id| integer| Path| true| The ID of the ticket

#### Example body


    {  "task_list": {    "task_list_template_id": "01K205PG0J2ET0B8AFHA106C1E"  }}

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/tickets/{ticket_id}/task_lists.json \  -H "Content-Type: application/json" \  -d '{    "task_list": {      "task_list_template_id": "01K205PG0J2ET0B8AFHA106C1E"    }' \  -v -u {email_address}/token:{api_token} -X PUT

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://example.zendesk.com/api/v2/tickets/123456/task_lists"	method := "POST"	payload := strings.NewReader(`{  "task_list": {    "task_list_template_id": "01K205PG0J2ET0B8AFHA106C1E"  }}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/tickets/123456/task_lists")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"task_list\": {    \"task_list_template_id\": \"01K205PG0J2ET0B8AFHA106C1E\"  }}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "task_list": {    "task_list_template_id": "01K205PG0J2ET0B8AFHA106C1E"  }});
    var config = {  method: 'POST',  url: 'https://example.zendesk.com/api/v2/tickets/123456/task_lists',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/tickets/123456/task_lists"
    payload = json.loads("""{  "task_list": {    "task_list_template_id": "01K205PG0J2ET0B8AFHA106C1E"  }}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/tickets/123456/task_lists")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")request.body = %q({  "task_list": {    "task_list_template_id": "01K205PG0J2ET0B8AFHA106C1E"  }})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**201 Created**


    // Status 201 Created
    {  "count": 1,  "next_page": null,  "previous_page": null,  "task_lists": [    {      "created_at": "2025-08-06T17:08:40Z",      "description": "Complete HR, IT, and payroll setup for new employees.",      "id": "01K3KVF23JWZ5M98BJBQHENYZ9",      "name": "Onboarding checklist",      "task_count": 2,      "task_list_template_id": "01K205PG0J2ET0B8AFHA106C1E",      "ticket_id": "1",      "updated_at": "2025-08-06T17:08:40Z"    }  ]}

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)