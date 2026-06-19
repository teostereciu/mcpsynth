# Resource Collections

*Source: https://developer.zendesk.com/api-reference/ticketing/ticket-management/resource_collections/*

---

## On this page

  * [JSON format](/api-reference/ticketing/ticket-management/resource_collections/#json-format)
  * [List Resource Collections](/api-reference/ticketing/ticket-management/resource_collections/#list-resource-collections)
  * [Show Resource Collection](/api-reference/ticketing/ticket-management/resource_collections/#show-resource-collection)
  * [Create Resource Collection](/api-reference/ticketing/ticket-management/resource_collections/#create-resource-collection)
  * [Update Resource Collection](/api-reference/ticketing/ticket-management/resource_collections/#update-resource-collection)
  * [Delete Resource Collection](/api-reference/ticketing/ticket-management/resource_collections/#delete-resource-collection)


# Resource Collections

## On this page

  * [JSON format](/api-reference/ticketing/ticket-management/resource_collections/#json-format)
  * [List Resource Collections](/api-reference/ticketing/ticket-management/resource_collections/#list-resource-collections)
  * [Show Resource Collection](/api-reference/ticketing/ticket-management/resource_collections/#show-resource-collection)
  * [Create Resource Collection](/api-reference/ticketing/ticket-management/resource_collections/#create-resource-collection)
  * [Update Resource Collection](/api-reference/ticketing/ticket-management/resource_collections/#update-resource-collection)
  * [Delete Resource Collection](/api-reference/ticketing/ticket-management/resource_collections/#delete-resource-collection)


A resource collection consists of Zendesk Support resource definitions. For example, a resource collection could define two different targets and one ticket field. You specify the resource collection the same way you specify the [resource requirements](/documentation/apps/app-developer-guide/apps_requirements/) for a Zendesk app.

#### Resource objects

The [List Resource Collections](/api-reference/ticketing/ticket-management/resource_collections/#list-resource-collections) and [Show Resource Collection](/api-reference/ticketing/ticket-management/resource_collections/#show-resource-collection) endpoints return a `resources` array. Each object in the `resources` array contains metadata for a resource in a resource collection.

Objects in the `resources` array have the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
identifier| string| true| false| Descriptive name for the resource
resource_id| integer| true| false| Unique id for the resource. Automatically assigned upon creation
type| array| true| false| Resource type. Possible values are "automations", "channel_integrations", "custom_objects", "macros", "organization_fields", "targets", "ticket_fields", "triggers", "user_fields", "view", and "webhooks"
deleted| boolean| true| false| If true, the resource has been deleted

### JSON format

Resource Collections are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
created_at| string| true| false| When the resource collection was created
id| integer| true| false| id for the resource collection. Automatically assigned upon creation
resources| array| true| false| Array of resource metadata objects. See Resource objects
updated_at| string| true| false| Last time the resource collection was updated

#### Example


    {  "created_at": "2011-07-20T22:55:29Z",  "id": 35436,  "resources": [    {      "deleted": false,      "identifier": "email_on_ticket_solved",      "resource_id": 10824486485524,      "type": "triggers"    },    {      "deleted": false,      "identifier": "support_description",      "resource_id": 10824486482580,      "type": "ticket_fields"    }  ],  "updated_at": "2011-07-20T22:55:29Z"}

### List Resource Collections

  * `GET /api/v2/resource_collections`


Lists resource collections for the account.

#### Allowed for

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
per_page| integer| Query| false| Number of records to return per page. Note: Default and maximum values vary by endpoint. Check endpoint-specific documentation for limits.

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/resource_collections \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/resource_collections?per_page=50"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/resource_collections")		.newBuilder()		.addQueryParameter("per_page", "50");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/resource_collections',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'per_page': '50',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/resource_collections?per_page=50"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/resource_collections")uri.query = URI.encode_www_form("per_page": "50")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "count": 0,  "next_page": null,  "previous_page": null,  "resource_collections": [    {      "created_at": "2015-09-09T01:57:24Z",      "id": 10002,      "resources": [        {          "deleted": false,          "identifier": "email_on_ticket_solved",          "resource_id": 10824486485524,          "type": "triggers"        },        {          "deleted": false,          "identifier": "support_description",          "resource_id": 10824486482580,          "type": "ticket_fields"        }      ],      "updated_at": "2015-09-09T01:57:24Z"    },    {      "created_at": "2015-09-10T02:01:03Z",      "id": 10002,      "resources": [        {          "deleted": false,          "identifier": "an_email_target",          "resource_id": 10827267902996,          "type": "targets"        }      ],      "updated_at": "2015-09-10T02:02:15Z"    }  ]}

### Show Resource Collection

  * `GET /api/v2/resource_collections/{resource_collection_id}`


Retrieves details for a specified resource collection.

#### Allowed for

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
resource_collection_id| integer| Path| true| The id of the resource collection

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/resource_collections/{resource_collection_id} \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/resource_collections/10002"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/resource_collections/10002")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/resource_collections/10002',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/resource_collections/10002"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/resource_collections/10002")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "resource_collection": {    "created_at": "2015-09-09T01:57:24Z",    "id": 10002,    "resources": [      {        "deleted": false,        "identifier": "email_on_ticket_solved",        "resource_id": 10824486485524,        "type": "triggers"      },      {        "deleted": false,        "identifier": "support_description",        "resource_id": 10824486482580,        "type": "ticket_fields"      }    ],    "updated_at": "2015-09-09T01:57:24Z"  }}

### Create Resource Collection

  * `POST /api/v2/resource_collections`


Creates a resource collection from a provided `payload` object. The `payload` object is specified the same way as the content of a requirements.json file in a Zendesk app. See [Specifying Apps Requirements](/documentation/apps/app-developer-guide/apps_requirements/) in the Zendesk Apps framework docs.

The response includes a [job status](/api-reference/ticketing/ticket-management/job_statuses/) for creation of the specified resources.

#### Allowed for

  * Admins


#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/resource_collections \  -v -u {email_address}/token:{api_token} -X POST \  -H "Content-Type: application/json" \  -d '{  "payload": {    "ticket_fields": {      "support_description": {        "type": "text",        "title": "Support description"      }    },    "triggers": {      "email_on_ticket_solved": {        "title": "Email on ticket solved Trigger",        "all": [          {            "field": "status",            "operator": "is",            "value": "solved"          }        ],        "actions": [          {            "field": "notification_user",            "value": [              "all_agents",              "[{{ticket.account}}] {{ticket.title}}",              "A ticket (#{{ticket.id}}) by {{ticket.requester.name}} has been received. It is unassigned.\n\n{{ticket.comments_formatted}}"            ]          }        ]      }    }  }}'

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/resource_collections"	method := "POST"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/resource_collections")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'POST',  url: 'https://example.zendesk.com/api/v2/resource_collections',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/resource_collections"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/resource_collections")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "job_status": {    "id": "0a3e49b038c40133d7380242ac110031",    "message": null,    "progress": null,    "results": null,    "status": "queued",    "total": null,    "url": "https://company.zendesk.com/api/v2/job_statuses/0a3e49b038c40133d7380242ac110031"  }}

### Update Resource Collection

  * `PUT /api/v2/resource_collections/{resource_collection_id}`


Updates a resource collection using a provided `payload` object. The `payload` object is specified the same way as the content of a requirements.json file in a Zendesk app. See [Specifying Apps Requirements](/documentation/apps/app-developer-guide/apps_requirements/) in the Zendesk Apps framework docs.

The response includes a [job status](/api-reference/ticketing/ticket-management/job_statuses/) for the resource updates.

#### Allowed for

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
resource_collection_id| integer| Path| true| The id of the resource collection

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/resource_collections/{resource_collection_id} \  -v -u {email_address}/token:{api_token} -X PUT \  -H "Content-Type: application/json" \  -d '{    "payload": {      "targets": {        "an_email_target": {          "title": "Send notification email",          "type": "email_target",          "email": "[[email protected]](/cdn-cgi/l/email-protection)",          "subject": "Hey, something happened!"        }      }    }  }'

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/resource_collections/10002"	method := "PUT"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/resource_collections/10002")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'PUT',  url: 'https://example.zendesk.com/api/v2/resource_collections/10002',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/resource_collections/10002"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/resource_collections/10002")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "job_status": {    "id": "4555831038d20133d7390242ac110031",    "message": null,    "progress": null,    "results": null,    "status": "queued",    "total": null,    "url": "https://company.zendesk.com/api/v2/job_statuses/4555831038d20133d7390242ac110031"  }}

### Delete Resource Collection

  * `DELETE /api/v2/resource_collections/{resource_collection_id}`


Deletes a specified resource collection.

The response includes a [job status](/api-reference/ticketing/ticket-management/job_statuses/) for deletion of the collection's resources.

#### Allowed for

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
resource_collection_id| integer| Path| true| The id of the resource collection

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/resource_collections/{resource_collection_id} \  -v -u {email_address}/token:{api_token} -X DELETE

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/resource_collections/10002"	method := "DELETE"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/resource_collections/10002")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("DELETE", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'DELETE',  url: 'https://example.zendesk.com/api/v2/resource_collections/10002',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/resource_collections/10002"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"DELETE",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/resource_collections/10002")request = Net::HTTP::Delete.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "job_status": {    "id": "2ee570d0398e0133e26e0242ac110017",    "message": null,    "progress": null,    "results": null,    "status": "queued",    "total": null,    "url": "https://company.zendesk.com/api/v2/job_statuses/2ee570d0398e0133e26e0242ac110017"  }}

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)