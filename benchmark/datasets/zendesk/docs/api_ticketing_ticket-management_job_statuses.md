# Job Statuses

*Source: https://developer.zendesk.com/api-reference/ticketing/ticket-management/job_statuses/*

---

## On this page

  * [JSON format](/api-reference/ticketing/ticket-management/job_statuses/#json-format)
  * [Results](/api-reference/ticketing/ticket-management/job_statuses/#results)
  * [List Job Statuses](/api-reference/ticketing/ticket-management/job_statuses/#list-job-statuses)
  * [Show Many Job Statuses](/api-reference/ticketing/ticket-management/job_statuses/#show-many-job-statuses)
  * [Show Job Status](/api-reference/ticketing/ticket-management/job_statuses/#show-job-status)


# Job Statuses

## On this page

  * [JSON format](/api-reference/ticketing/ticket-management/job_statuses/#json-format)
  * [Results](/api-reference/ticketing/ticket-management/job_statuses/#results)
  * [List Job Statuses](/api-reference/ticketing/ticket-management/job_statuses/#list-job-statuses)
  * [Show Many Job Statuses](/api-reference/ticketing/ticket-management/job_statuses/#show-many-job-statuses)
  * [Show Job Status](/api-reference/ticketing/ticket-management/job_statuses/#show-job-status)


A status record is created when somebody kicks off a job such as [updating multiple tickets](/api-reference/ticketing/tickets/tickets/#update-many-tickets). You can access the job status data for one day after a particular job is created, after which the data is no longer available.

### JSON format

Job Statuses are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
id| string| true| false| Automatically assigned when the job is queued
job_type| string| true| false| The type of the job
message| string| true| false| Message from the job worker, if any
progress| integer| true| false| Number of tasks that have already been completed
results| | true| false| Result data from processed tasks. See Results below
status| string| true| false| The current status. One of the following: "queued", "working", "failed", "completed"
total| integer| true| false| The total number of tasks this job is batching through
url| string| true| false| The URL to poll for status updates

### Results

The "results" array in a response lists the resources that were successfully and unsuccessfully updated or created after processing.

The results differ depending on the type of job.

#### Permanent Ticket Deletion

If the job was to permanently delete tickets, the result is an object that will only specify whether all of the tickets were successfully deleted or not (`"success": true`).


    {  "job_status": {    "id": "dd9321f29967688b27bc9499ebb4ae8d",    "url": "https://example.zendesk.com/api/v2/job_statuses/dd9321f299676c9499ebb4ae8d",    "total": null,    "progress": null,    "status": "completed",    "message": "Completed at 2018-03-08 06:07:49 +0000",    "results": {      "success": true    }  }}

#### Bulk create

If the job was to bulk create resources, each result specifies the following:

  * the id of the new resource (`"id": 245`)
  * the index number of the result (`"index": 1`)


#### Example


    {  "job_status": {    "id": "dd9321f29967688b27bc9499ebb4ae8d",    "url": "https://example.zendesk.com/api/v2/job_statuses/dd9321f299676c9499ebb4ae8d",    "total": 2,    "progress": 2,    "status": "completed",    "message": "Completed at 2018-03-08 06:07:49 +0000",    "results": [      {        "id": 244,        "index": 0      },      {        "id": 245,        "index": 1      }    ]  }}

#### Bulk update

If the job was to bulk update resources, each result specifies the following:

  * the id of the resource the job attempted to update (`"id": 255`)
  * the action the job attempted (`"action": "update"`)
  * whether the action was successful or not (`"success": true`)
  * the status (`"status": "Updated"`)


#### Example


    {  "id": "82de0b044094f0c67893ac9fe64f1a99",  "message": "Completed at 2018-03-08 10:07:04 +0000",  "progress": 2,  "results": [    {      "action": "update",      "id": 244,      "status": "Updated",      "success": true    },    {      "action": "update",      "id": 245,      "status": "Updated",      "success": true    }  ],  "status": "completed",  "total": 2,  "url": "https://example.zendesk.com/api/v2/job_statuses/82de0b0467893ac9fe64f1a99"}

### List Job Statuses

  * `GET /api/v2/job_statuses`


Shows the statuses for background jobs. Statuses are sorted first by completion date and then by creation date in descending order.

#### Allowed For:

  * Agents


#### Pagination

  * Cursor pagination


See [Pagination](/api-reference/introduction/pagination/).

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
page| object| Query| false| Cursor-based pagination parameters (JSON:API style). Supports nested parameters: - `page[size]` \- Number of records per page (default varies by endpoint, typically 100) - `page[after]` \- Cursor token to fetch records after this position - `page[before]` \- Cursor token to fetch records before this position Example: `?page[size]=50&page[after]=eyJvIjoiaWQiLCJ2IjoiYVFFPSJ9`

#### Code Samples

**cURL**


    curl https://{subdomain}.zendesk.com/api/v2/job_statuses \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/job_statuses?page="	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/job_statuses")		.newBuilder()		.addQueryParameter("page", "");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/job_statuses',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'page': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/job_statuses?page="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/job_statuses")uri.query = URI.encode_www_form("page": "")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "job_statuses": [    {      "id": "8b726e606741012ffc2d782bcb7848fe",      "status": "completed"    },    {      "id": "e7665094164c498781ebe4c8db6d2af5",      "status": "completed"    }  ]}

### Show Many Job Statuses

  * `GET /api/v2/job_statuses/show_many?ids={ids}`


Accepts a comma-separated list of job status ids.

#### Allowed For:

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
ids| string| Query| true| Comma-separated list of job status ids.

#### Code Samples

**cURL**


    curl https://{subdomain}.zendesk.com/api/v2/job_statuses/show_many?ids=8b726e606741012ffc2d782bcb7848fe,8b726e606741012ffc2d782bcb7848fe,e7665094164c498781ebe4c8db6d2af5 \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/job_statuses/show_many?ids=8b726e606741012ffc2d782bcb7848fe%2Ce7665094164c498781ebe4c8db6d2af5"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/job_statuses/show_many")		.newBuilder()		.addQueryParameter("ids", "8b726e606741012ffc2d782bcb7848fe,e7665094164c498781ebe4c8db6d2af5");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/job_statuses/show_many',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'ids': '8b726e606741012ffc2d782bcb7848fe%2Ce7665094164c498781ebe4c8db6d2af5',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/job_statuses/show_many?ids=8b726e606741012ffc2d782bcb7848fe%2Ce7665094164c498781ebe4c8db6d2af5"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/job_statuses/show_many")uri.query = URI.encode_www_form("ids": "8b726e606741012ffc2d782bcb7848fe,e7665094164c498781ebe4c8db6d2af5")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "job_statuses": [    {      "id": "8b726e606741012ffc2d782bcb7848fe",      "status": "completed"    },    {      "id": "e7665094164c498781ebe4c8db6d2af5",      "status": "completed"    }  ]}

### Show Job Status

  * `GET /api/v2/job_statuses/{job_status_id}`


Shows the status of a background job.

#### Allowed For:

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
job_status_id| string| Path| true| the Id of the Job status

#### Code Samples

**cURL**


    curl https://{subdomain}.zendesk.com/api/v2/job_statuses/{job_status_id} \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/job_statuses/8b726e606741012ffc2d782bcb7848fe"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/job_statuses/8b726e606741012ffc2d782bcb7848fe")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/job_statuses/8b726e606741012ffc2d782bcb7848fe',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/job_statuses/8b726e606741012ffc2d782bcb7848fe"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/job_statuses/8b726e606741012ffc2d782bcb7848fe")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "job_status": {    "id": "8b726e606741012ffc2d782bcb7848fe",    "message": "Completed at Fri Apr 13 02:51:53 +0000 2012",    "progress": 2,    "results": [      {        "action": "update",        "id": 380,        "status": "Updated",        "success": true      }    ],    "status": "completed",    "total": 2,    "url": "https://company.zendesk.com/api/v2/job_statuses/8b726e606741012ffc2d782bcb7848fe"  }}

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)