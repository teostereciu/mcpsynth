# Deletion Schedules

*Source: https://developer.zendesk.com/api-reference/ticketing/business-rules/deletion_schedules/*

---

## On this page

  * [JSON format](/api-reference/ticketing/business-rules/deletion_schedules/#json-format)
  * [List Deletion Schedules](/api-reference/ticketing/business-rules/deletion_schedules/#list-deletion-schedules)
  * [Create Deletion Schedule](/api-reference/ticketing/business-rules/deletion_schedules/#create-deletion-schedule)
  * [Get Deletion Schedule](/api-reference/ticketing/business-rules/deletion_schedules/#get-deletion-schedule)
  * [Update Deletion Schedule](/api-reference/ticketing/business-rules/deletion_schedules/#update-deletion-schedule)
  * [Delete Deletion Schedule](/api-reference/ticketing/business-rules/deletion_schedules/#delete-deletion-schedule)


# Deletion Schedules

## On this page

  * [JSON format](/api-reference/ticketing/business-rules/deletion_schedules/#json-format)
  * [List Deletion Schedules](/api-reference/ticketing/business-rules/deletion_schedules/#list-deletion-schedules)
  * [Create Deletion Schedule](/api-reference/ticketing/business-rules/deletion_schedules/#create-deletion-schedule)
  * [Get Deletion Schedule](/api-reference/ticketing/business-rules/deletion_schedules/#get-deletion-schedule)
  * [Update Deletion Schedule](/api-reference/ticketing/business-rules/deletion_schedules/#update-deletion-schedule)
  * [Delete Deletion Schedule](/api-reference/ticketing/business-rules/deletion_schedules/#delete-deletion-schedule)


Deletion schedules ease compliance with GDPR, CPRA, and other prominent data protection regulations by allowing the client to automatically delete data after a certain period of time. To learn more, see [Creating ticket deletion schedules for data retention policies](https://support.zendesk.com/hc/en-us/articles/6062884435866-Creating-ticket-deletion-schedules-for-data-retention-policies) in Zendesk help.

There are currently 4 types of deletion schedule. Tickets, End-users, Bot Conversations and Attachments.

### JSON format

Deletion Schedules are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
active| boolean| false| false| Whether the deletion schedule is active
conditions| object| false| false| An object that describes the conditions under which the automation will execute. See [Conditions reference](/documentation/ticketing/reference-guides/conditions-reference)
created_at| string| true| false| The time the deletion schedule was created
default| boolean| true| false| Whether the deletion schedule is the default
description| string| false| false| The description of the deletion schedule
id| integer| true| false| The id of the deletion schedule
object| string| false| false| Represents the entity the schedule will delete. Cannot be modified after schedule creation. Can be one of `'zen:ticket'`, `'zen:user'`, `'zen:attachment'`, `'zen:bot_only_conversation'`, or `'zen:custom_object:CUSTOM_OBJECT_KEY'`.
title| string| false| false| The title of the deletion schedule
updated_at| string| true| false| The time the deletion schedule was last updated
url| string| true| false| Url for obtaining the deletion schedule JSON

### List Deletion Schedules

  * `GET /api/v2/deletion_schedules`


Lists all deletion schedules for the account. Deletion schedules are used to automatically delete data from the account after a certain period of time.

#### Allowed For

  * Admins


#### Code Samples

**curl**


    curl 'https://{subdomain}.zendesk.com/api/v2/deletion_schedules' \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/deletion_schedules"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/deletion_schedules")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/deletion_schedules',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/deletion_schedules"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/deletion_schedules")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "deletion_schedules": [    {      "active": true,      "conditions": {        "all": [          {            "field": "duration_since_last_update",            "operator": "greater_than",            "value": "P1Y"          }        ],        "any": []      },      "created_at": "2021-07-20T22:55:29Z",      "default": false,      "description": "Delete tickets older than 1 year",      "id": 7772196094461,      "title": "some schedule",      "updated_at": "2021-07-20T22:55:29Z",      "url": "https://{some domain}.zendesk.com/api/v2/deletion_schedules/7772196094461"    }  ]}

### Create Deletion Schedule

  * `POST /api/v2/deletion_schedules`


Creates a new deletion schedule.

#### Allowed For

  * Admins


#### Example body


    {  "deletion_schedule": {    "active": true,    "conditions": {      "all": [        {          "field": "duration_since_last_update",          "operator": "greater_than",          "value": "P1Y"        }      ],      "any": []    },    "description": "Delete tickets older than 1 year",    "title": "some schedule"  }}

#### Code Samples

**curl**

**new_deletion_schedule.json**


    {  "deletion_schedule": {    "title": "some title",    "active": false,    "description": "some description",    "conditions": {      "all": [        {          "field": "duration_since_last_update",          "operator": "greater_than",          "value": "P1M"        }      ],      "any": []    }  }}

**curl snippet**


    curl -X POST https://{subdomain}.zendesk.com/api/v2/deletion_schedules \  -d @new_deletion_schedule.json \  -H "Content-Type: application/json" \  -v -u {email_address}/token:{api_token} -X POST

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://example.zendesk.com/api/v2/deletion_schedules"	method := "POST"	payload := strings.NewReader(`{  "deletion_schedule": {    "active": true,    "conditions": {      "all": [        {          "field": "duration_since_last_update",          "operator": "greater_than",          "value": "P1Y"        }      ],      "any": []    },    "description": "Delete tickets older than 1 year",    "title": "some schedule"  }}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/deletion_schedules")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"deletion_schedule\": {    \"active\": true,    \"conditions\": {      \"all\": [        {          \"field\": \"duration_since_last_update\",          \"operator\": \"greater_than\",          \"value\": \"P1Y\"        }      ],      \"any\": []    },    \"description\": \"Delete tickets older than 1 year\",    \"title\": \"some schedule\"  }}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "deletion_schedule": {    "active": true,    "conditions": {      "all": [        {          "field": "duration_since_last_update",          "operator": "greater_than",          "value": "P1Y"        }      ],      "any": []    },    "description": "Delete tickets older than 1 year",    "title": "some schedule"  }});
    var config = {  method: 'POST',  url: 'https://example.zendesk.com/api/v2/deletion_schedules',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/deletion_schedules"
    payload = json.loads("""{  "deletion_schedule": {    "active": true,    "conditions": {      "all": [        {          "field": "duration_since_last_update",          "operator": "greater_than",          "value": "P1Y"        }      ],      "any": []    },    "description": "Delete tickets older than 1 year",    "title": "some schedule"  }}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/deletion_schedules")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")request.body = %q({  "deletion_schedule": {    "active": true,    "conditions": {      "all": [        {          "field": "duration_since_last_update",          "operator": "greater_than",          "value": "P1Y"        }      ],      "any": []    },    "description": "Delete tickets older than 1 year",    "title": "some schedule"  }})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**201 Created**


    // Status 201 Created
    {  "deletion_schedule": {    "active": true,    "conditions": {      "all": [        {          "field": "duration_since_last_update",          "operator": "greater_than",          "value": "P1Y"        }      ],      "any": []    },    "created_at": "2021-07-20T22:55:29Z",    "default": false,    "description": "Delete tickets older than 1 year",    "id": 7772196094461,    "title": "some schedule",    "updated_at": "2021-07-20T22:55:29Z",    "url": "https://{some domain}.zendesk.com/api/v2/deletion_schedules/7772196094461"  }}

### Get Deletion Schedule

  * `GET /api/v2/deletion_schedules/{deletion_schedule_id}`


Gets a deletion schedule by its id.

#### Allowed For

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
deletion_schedule_id| integer| Path| true| The id of the deletion schedule

#### Code Samples

**curl**


    curl 'https://{subdomain}.zendesk.com/api/v2/deletion_schedules/{deletion_schedule_id}' \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/deletion_schedules/132828"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/deletion_schedules/132828")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/deletion_schedules/132828',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/deletion_schedules/132828"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/deletion_schedules/132828")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "deletion_schedule": {    "active": true,    "conditions": {      "all": [        {          "field": "duration_since_last_update",          "operator": "greater_than",          "value": "P1Y"        }      ],      "any": []    },    "created_at": "2021-07-20T22:55:29Z",    "default": false,    "description": "Delete tickets older than 1 year",    "id": 7772196094461,    "title": "some schedule",    "updated_at": "2021-07-20T22:55:29Z",    "url": "https://{some domain}.zendesk.com/api/v2/deletion_schedules/7772196094461"  }}

### Update Deletion Schedule

  * `PUT /api/v2/deletion_schedules/{deletion_schedule_id}`


Updates a deletion schedule by its id.

**Note** : Updating a condition updates the conditions array, clearing all existing values of the array. Include all your conditions when updating any condition.

#### Allowed For

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
deletion_schedule_id| integer| Path| true| The id of the deletion schedule

#### Example body


    {  "deletion_schedule": {    "active": true,    "conditions": {      "all": [        {          "field": "duration_since_last_update",          "operator": "greater_than",          "value": "P1Y"        }      ],      "any": []    },    "description": "Delete tickets older than 1 year",    "title": "some schedule"  }}

#### Code Samples

**curl**

**new_deletion_schedule.json**


    {  "deletion_schedule": {    "title": "some title",    "active": false,    "description": "some description",    "conditions": {      "all": [        {          "field": "duration_since_last_update",          "operator": "greater_than",          "value": "P1M"        }      ],      "any": []    }  }}

**curl snippet**


    curl -X PATCH https://{subdomain}.zendesk.com/api/v2/deletion_schedules/{deletion_schedule_id} \  -d @new_deletion_schedule.json \  -H "Content-Type: application/json" \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://example.zendesk.com/api/v2/deletion_schedules/132828"	method := "PUT"	payload := strings.NewReader(`{  "deletion_schedule": {    "active": true,    "conditions": {      "all": [        {          "field": "duration_since_last_update",          "operator": "greater_than",          "value": "P1Y"        }      ],      "any": []    },    "description": "Delete tickets older than 1 year",    "title": "some schedule"  }}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/deletion_schedules/132828")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"deletion_schedule\": {    \"active\": true,    \"conditions\": {      \"all\": [        {          \"field\": \"duration_since_last_update\",          \"operator\": \"greater_than\",          \"value\": \"P1Y\"        }      ],      \"any\": []    },    \"description\": \"Delete tickets older than 1 year\",    \"title\": \"some schedule\"  }}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "deletion_schedule": {    "active": true,    "conditions": {      "all": [        {          "field": "duration_since_last_update",          "operator": "greater_than",          "value": "P1Y"        }      ],      "any": []    },    "description": "Delete tickets older than 1 year",    "title": "some schedule"  }});
    var config = {  method: 'PUT',  url: 'https://example.zendesk.com/api/v2/deletion_schedules/132828',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/deletion_schedules/132828"
    payload = json.loads("""{  "deletion_schedule": {    "active": true,    "conditions": {      "all": [        {          "field": "duration_since_last_update",          "operator": "greater_than",          "value": "P1Y"        }      ],      "any": []    },    "description": "Delete tickets older than 1 year",    "title": "some schedule"  }}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/deletion_schedules/132828")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")request.body = %q({  "deletion_schedule": {    "active": true,    "conditions": {      "all": [        {          "field": "duration_since_last_update",          "operator": "greater_than",          "value": "P1Y"        }      ],      "any": []    },    "description": "Delete tickets older than 1 year",    "title": "some schedule"  }})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "deletion_schedule": {    "active": true,    "conditions": {      "all": [        {          "field": "duration_since_last_update",          "operator": "greater_than",          "value": "P1Y"        }      ],      "any": []    },    "default": false,    "description": "Delete tickets older than 1 year",    "id": 7772196094461,    "title": "some schedule",    "url": "https://{some domain}.zendesk.com/api/v2/deletion_schedules/7772196094461"  }}

### Delete Deletion Schedule

  * `DELETE /api/v2/deletion_schedules/{deletion_schedule_id}`


Deletes a deletion schedule by its id.

#### Allowed For

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
deletion_schedule_id| integer| Path| true| The id of the deletion schedule

#### Code Samples

**curl**


    curl -X DELETE 'https://{subdomain}.zendesk.com/api/v2/deletion_schedules/{deletion_schedule_id}' \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/deletion_schedules/132828"	method := "DELETE"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/deletion_schedules/132828")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("DELETE", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'DELETE',  url: 'https://example.zendesk.com/api/v2/deletion_schedules/132828',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/deletion_schedules/132828"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"DELETE",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/deletion_schedules/132828")request = Net::HTTP::Delete.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**204 No Content**


    // Status 204 No Content
    null

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)