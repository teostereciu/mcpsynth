# Target Failures

*Source: https://developer.zendesk.com/api-reference/ticketing/targets/target_failures/*

---

## On this page

  * [JSON format](/api-reference/ticketing/targets/target_failures/#json-format)
  * [List Target Failures](/api-reference/ticketing/targets/target_failures/#list-target-failures)
  * [Show Target Failure](/api-reference/ticketing/targets/target_failures/#show-target-failure)


# Target Failures

## On this page

  * [JSON format](/api-reference/ticketing/targets/target_failures/#json-format)
  * [List Target Failures](/api-reference/ticketing/targets/target_failures/#list-target-failures)
  * [Show Target Failure](/api-reference/ticketing/targets/target_failures/#show-target-failure)


**Important:** Zendesk is [discontinuing support for URL targets and branded targets](https://support.zendesk.com/hc/en-us/articles/6468124845210-Announcing-the-deprecation-of-URL-targets-and-branded-targets) in favor of webhooks. From October 28, 2024, the target failures endpoint will no longer function.

Targets are pointers to cloud-based applications and services, as well as to HTTP and email addresses. Targets are used with triggers and automations to send a notification to the target when a condition is met in Zendesk Support. See [Notifying external targets](https://support.zendesk.com/hc/en-us/articles/203662136). A target failure record is created when the target returns an error.

### JSON format

Target Failures are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
consecutive_failure_count| integer| true| false| Number of times the target failed consecutively
created_at| string| true| false| Time of the failure
id| integer| true| false| The ID of the target failure
raw_request| string| true| false| The raw message of the target request
raw_response| string| true| false| The raw response of the failure
status_code| integer| true| false| HTTP status code of the target failure
target_name| string| true| false| Name of the target failure
url| string| true| false| The API url of the failure record

#### Example


    {  "consecutive_failure_count": 1,  "created_at": "2017-09-05T10:38:52Z",  "id": 6001326,  "raw_request": "GET /api/v2/tickets HTTP/1.1\r\nUser-Agent: Zendesk Target\r\n ...",  "raw_response": "HTTP/1.1 401 Unauthorized\r\nServer: nginx\r\n ...",  "status_code": 401,  "target_name": "My URL Target",  "url": "https://example.zendesk.com/api/v2/target_failures/6001326"}

### List Target Failures

  * `GET /api/v2/target_failures`


Returns the 25 most recent target failures, per target.

#### Stability

  * Development


#### Allowed For

  * Admins


#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/target_failures \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/target_failures"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/target_failures")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/target_failures',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/target_failures"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/target_failures")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "target_failures": [    {      "id": 1,      "status_code": 401,      "target_name": "My URL Target"    },    {      "id": 2,      "status_code": 401,      "target_name": "My URL Target"    }  ]}

### Show Target Failure

  * `GET /api/v2/target_failures/{target_failure_id}`


#### Stability

  * Development


#### Allowed For

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
target_failure_id| integer| Path| true| The ID of the target failure

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/target_failures/{target_failure_id} \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/target_failures/1"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/target_failures/1")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/target_failures/1',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/target_failures/1"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/target_failures/1")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "target_failure": {    "id": 1,    "raw_request": "GET /api/v2/tickets HTTP/1.1\r\nUser-Agent: Zendesk Target\r\n ...",    "raw_response": "HTTP/1.1 401 Unauthorized\r\nServer: nginx\r\n ...",    "status_code": 401,    "target_name": "My URL Target"  }}

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)