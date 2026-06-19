# Bookmarks

*Source: https://developer.zendesk.com/api-reference/ticketing/ticket-management/bookmarks/*

---

## On this page

  * [JSON format](/api-reference/ticketing/ticket-management/bookmarks/#json-format)
  * [List Bookmarks](/api-reference/ticketing/ticket-management/bookmarks/#list-bookmarks)
  * [Create Bookmark](/api-reference/ticketing/ticket-management/bookmarks/#create-bookmark)
  * [Delete Bookmark](/api-reference/ticketing/ticket-management/bookmarks/#delete-bookmark)


# Bookmarks

## On this page

  * [JSON format](/api-reference/ticketing/ticket-management/bookmarks/#json-format)
  * [List Bookmarks](/api-reference/ticketing/ticket-management/bookmarks/#list-bookmarks)
  * [Create Bookmark](/api-reference/ticketing/ticket-management/bookmarks/#create-bookmark)
  * [Delete Bookmark](/api-reference/ticketing/ticket-management/bookmarks/#delete-bookmark)


Use this API to bookmark tickets so you can easily return to the tickets later.

### JSON format

Bookmarks are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
created_at| string| true| false| The time the bookmark was created
id| integer| true| false| Automatically assigned when the bookmark is created
ticket| object| true| false|
url| string| true| false| The API url of this bookmark

#### Example


    {  "created_at": "2014-11-20T22:55:29Z",  "id": 35436,  "ticket": {    "description": "The fire is very colorful.",    "id": 60,    "priority": "high",    "requester_id": 156,    "subject": "Help, my printer is on fire!"  },  "url": "https://{subdomain}.zendesk.com/api/v2/bookmarks/35436"}

### List Bookmarks

  * `GET /api/v2/bookmarks`


Archived tickets are not included in the response. See [About archived tickets](https://support.zendesk.com/hc/en-us/articles/4408887617050) in Zendesk help.

#### Allowed For

  * Agents


#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/bookmarks \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/bookmarks"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/bookmarks")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/bookmarks',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/bookmarks"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/bookmarks")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "bookmarks": [    {      "created_at": "2020-10-01T08:33:45Z",      "id": 900000009567,      "ticket": {        "id": 123,        "priority": "high",        "raw_subject": "Chat with Visitor 19785128",        "requester_id": 165,        "subject": "Chat with Visitor 19785128",        "url": "https://{subdomain}.zendesk.com/api/v2/tickets/123"      },      "url": "https://{subdomain}.zendesk.com/api/v2/bookmarks/900000001111"    },    {      "created_at": "2020-09-11T10:22:45Z",      "id": 900000009568,      "ticket": {        "id": 123,        "priority": "high",        "raw_subject": "Chat with Visitor 19785128",        "requester_id": 156,        "subject": "Chat with Visitor 19785128",        "url": "https://{subdomain}.zendesk.com/api/v2/tickets/123"      },      "url": "https://{subdomain}.zendesk.com/api/v2/bookmarks/900000001112"    }  ],  "count": 1,  "next_page": null,  "previous_page": null}

### Create Bookmark

  * `POST /api/v2/bookmarks`


#### Allowed For

  * Agents


#### Example body


    {  "bookmark": {    "ticket_id": 113  }}

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/bookmarks \  -H "Content-Type: application/json" -X POST -d '{"bookmark": {"ticket_id": 123}}' \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://example.zendesk.com/api/v2/bookmarks"	method := "POST"	payload := strings.NewReader(`{  "bookmark": {    "ticket_id": 113  }}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/bookmarks")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"bookmark\": {    \"ticket_id\": 113  }}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "bookmark": {    "ticket_id": 113  }});
    var config = {  method: 'POST',  url: 'https://example.zendesk.com/api/v2/bookmarks',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/bookmarks"
    payload = json.loads("""{  "bookmark": {    "ticket_id": 113  }}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/bookmarks")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")request.body = %q({  "bookmark": {    "ticket_id": 113  }})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "bookmark": {    "created_at": "2020-10-01T08:33:45Z",    "id": 900000009567,    "ticket": {      "id": 123,      "priority": "high",      "raw_subject": "Chat with Visitor 19785128",      "requester_id": 156,      "subject": "Chat with Visitor 19785128",      "url": "https://{subdomain}.zendesk.com/api/v2/tickets/123"    },    "url": "https://{subdomain}.zendesk.com/api/v2/bookmarks/900000001111"  }}

**201 Created**


    // Status 201 Created
    {  "bookmark": {    "created_at": "2020-10-01T08:33:45Z",    "id": 900000009567,    "ticket": {      "id": 123,      "priority": "high",      "raw_subject": "Chat with Visitor 19785128",      "requester_id": 156,      "subject": "Chat with Visitor 19785128",      "url": "https://{subdomain}.zendesk.com/api/v2/tickets/123"    },    "url": "https://{subdomain}.zendesk.com/api/v2/bookmarks/900000001111"  }}

### Delete Bookmark

  * `DELETE /api/v2/bookmarks/{bookmark_id}`


#### Allowed For

  * Agents (own bookmarks only)


If the bookmark already exists with a specified ticket id, the response status will be `http Status: 200 OK`.

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
bookmark_id| integer| Path| true| The ID of the bookmark

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/bookmarks/{bookmark_id} \  -X DELETE -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/bookmarks/900000001111"	method := "DELETE"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/bookmarks/900000001111")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("DELETE", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'DELETE',  url: 'https://example.zendesk.com/api/v2/bookmarks/900000001111',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/bookmarks/900000001111"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"DELETE",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/bookmarks/900000001111")request = Net::HTTP::Delete.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**204 No Content**


    // Status 204 No Content
    null

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)