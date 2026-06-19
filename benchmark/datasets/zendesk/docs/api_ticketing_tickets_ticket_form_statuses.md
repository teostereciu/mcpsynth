# Ticket Form Statuses

*Source: https://developer.zendesk.com/api-reference/ticketing/tickets/ticket_form_statuses/*

---

## On this page

  * [JSON format](/api-reference/ticketing/tickets/ticket_form_statuses/#json-format)
  * [List Ticket Form Statuses](/api-reference/ticketing/tickets/ticket_form_statuses/#list-ticket-form-statuses)
  * [Show Many Ticket Form Statuses](/api-reference/ticketing/tickets/ticket_form_statuses/#show-many-ticket-form-statuses)
  * [Delete Ticket Form Statuses](/api-reference/ticketing/tickets/ticket_form_statuses/#delete-ticket-form-statuses)
  * [Delete Ticket Form Status By Id](/api-reference/ticketing/tickets/ticket_form_statuses/#delete-ticket-form-status-by-id)


# Ticket Form Statuses

## On this page

  * [JSON format](/api-reference/ticketing/tickets/ticket_form_statuses/#json-format)
  * [List Ticket Form Statuses](/api-reference/ticketing/tickets/ticket_form_statuses/#list-ticket-form-statuses)
  * [Show Many Ticket Form Statuses](/api-reference/ticketing/tickets/ticket_form_statuses/#show-many-ticket-form-statuses)
  * [Delete Ticket Form Statuses](/api-reference/ticketing/tickets/ticket_form_statuses/#delete-ticket-form-statuses)
  * [Delete Ticket Form Status By Id](/api-reference/ticketing/tickets/ticket_form_statuses/#delete-ticket-form-status-by-id)


Ticket form statuses define the relationship between ticket forms and custom statuses. They determine which custom statuses are available in the Agent Workspace status picker based on the current form in use.

### JSON format

Ticket Form Statuses are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
custom_status_id| integer| false| false| The id of the associated custom status
id| string| true| false| Automatically assigned when creating a ticket form
ticket_form_id| integer| false| false| The id of the associated ticket form

#### Example


    {  "custom_status_id": 7485541848574,  "id": "01HFD81Y01D65FJ7EPNNM58GPK",  "ticket_form_id": 7485506877054}

### List Ticket Form Statuses

  * `GET /api/v2/ticket_form_statuses`


Fetches all of the ticket form statuses for the account.

Supports filtering by ticket form ID and other criteria using query parameters.

#### Allowed For

  * Admins
  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
filter| object| Query| false| Additional filter criteria
ticket_form_id| string| Query| false| Filter by ticket form ID. Supports single ID or comma-separated list of IDs.

#### Code Samples

**Curl**


    curl --request GET https://example.zendesk.com/api/v2/ticket_form_statuses?filter=%7B%22custom_status_id%22%3A%22789%22%2C%22id%22%3A%22123%2C456%22%7D&ticket_form_id= \--header "Content-Type: application/json" \-u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/ticket_form_statuses?filter=%7B%22custom_status_id%22%3A%22789%22%2C%22id%22%3A%22123%2C456%22%7D&ticket_form_id="	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/ticket_form_statuses")		.newBuilder()		.addQueryParameter("filter", "{"custom_status_id":"789","id":"123,456"}")		.addQueryParameter("ticket_form_id", "");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/ticket_form_statuses',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'filter': '%7B%22custom_status_id%22%3A%22789%22%2C%22id%22%3A%22123%2C456%22%7D',    'ticket_form_id': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/ticket_form_statuses?filter=%7B%22custom_status_id%22%3A%22789%22%2C%22id%22%3A%22123%2C456%22%7D&ticket_form_id="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/ticket_form_statuses")uri.query = URI.encode_www_form("filter": "{"custom_status_id":"789","id":"123,456"}", "ticket_form_id": "")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "ticket_form_statuses": [    {      "custom_status_id": 7485541848574,      "id": "01HFD81Y01D65FJ7EPNNM58GPK",      "ticket_form_id": 7485506877054    }  ]}

### Show Many Ticket Form Statuses

  * `GET /api/v2/ticket_form_statuses/show_many?ids={ids}`


Fetches all of the ticket form statuses specified by a comma separated list of ids.

#### Allowed For

  * Anyone


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
ids| string| Query| true| Ticket form status ids to retrieve records for

#### Code Samples

**Curl**


    curl --request GET https://example.zendesk.com/api/v2/ticket_form_statuses/show_many?ids=abc%2Cdef%2Cghi \--header "Content-Type: application/json" \-u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/ticket_form_statuses/show_many?ids=abc%2Cdef%2Cghi"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/ticket_form_statuses/show_many")		.newBuilder()		.addQueryParameter("ids", "abc,def,ghi");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/ticket_form_statuses/show_many',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'ids': 'abc%2Cdef%2Cghi',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/ticket_form_statuses/show_many?ids=abc%2Cdef%2Cghi"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/ticket_form_statuses/show_many")uri.query = URI.encode_www_form("ids": "abc,def,ghi")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "ticket_form_statuses": [    {      "custom_status_id": 7485541848574,      "id": "01HFD81Y01D65FJ7EPNNM58GPK",      "ticket_form_id": 7485506877054    }  ]}

### Delete Ticket Form Statuses

  * `DELETE /api/v2/ticket_forms/{ticket_form_id}/ticket_form_statuses`


Deletes all of of the ticket form statuses by id.

#### Allowed For

  * Admins
  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
ticket_form_id| integer| Path| true| The ID of the ticket form

#### Example body


    {  "id": [    "abc",    "def",    "hij"  ]}

#### Code Samples

**Curl**


    curl --request DELETE https://example.zendesk.com/api/v2/ticket_forms/47/ticket_form_statuses \--header "Content-Type: application/json" \-u {email_address}/token:{api_token} \--data-raw '{  "id": [    "abc",    "def",    "hij"  ]}'

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://example.zendesk.com/api/v2/ticket_forms/47/ticket_form_statuses"	method := "DELETE"	payload := strings.NewReader(`{  "id": [    "abc",    "def",    "hij"  ]}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/ticket_forms/47/ticket_form_statuses")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("DELETE", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "id": [    "abc",    "def",    "hij"  ]});
    var config = {  method: 'DELETE',  url: 'https://example.zendesk.com/api/v2/ticket_forms/47/ticket_form_statuses',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/ticket_forms/47/ticket_form_statuses"
    payload = json.loads("""{  "id": [    "abc",    "def",    "hij"  ]}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"DELETE",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/ticket_forms/47/ticket_form_statuses")request = Net::HTTP::Delete.new(uri, "Content-Type": "application/json")request.body = %q({  "id": [    "abc",    "def",    "hij"  ]})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**204 No Content**


    // Status 204 No Content
    null

### Delete Ticket Form Status By Id

  * `DELETE /api/v2/ticket_forms/{ticket_form_id}/ticket_form_statuses/{ticket_form_status_id}`


Deletes a ticket form status by id.

#### Allowed For

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
ticket_form_id| integer| Path| true| The ID of the ticket form
ticket_form_status_id| string| Path| true| The id of the ticket form status

#### Code Samples

**Curl**


    curl --request DELETE https://example.zendesk.com/api/v2/ticket_forms/47/ticket_form_statuses/abcdef \--header "Content-Type: application/json" \-u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/ticket_forms/47/ticket_form_statuses/abcdef"	method := "DELETE"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/ticket_forms/47/ticket_form_statuses/abcdef")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("DELETE", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'DELETE',  url: 'https://example.zendesk.com/api/v2/ticket_forms/47/ticket_form_statuses/abcdef',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/ticket_forms/47/ticket_form_statuses/abcdef"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"DELETE",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/ticket_forms/47/ticket_form_statuses/abcdef")request = Net::HTTP::Delete.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**204 No Content**


    // Status 204 No Content
    null

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)