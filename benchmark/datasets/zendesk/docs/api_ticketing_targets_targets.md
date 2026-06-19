# Targets

*Source: https://developer.zendesk.com/api-reference/ticketing/targets/targets/*

---

## On this page

  * [JSON format](/api-reference/ticketing/targets/targets/#json-format)
  * [List Targets](/api-reference/ticketing/targets/targets/#list-targets)
  * [Show Target](/api-reference/ticketing/targets/targets/#show-target)
  * [Create Target](/api-reference/ticketing/targets/targets/#create-target)
  * [Update Target](/api-reference/ticketing/targets/targets/#update-target)
  * [Delete Target](/api-reference/ticketing/targets/targets/#delete-target)


# Targets

## On this page

  * [JSON format](/api-reference/ticketing/targets/targets/#json-format)
  * [List Targets](/api-reference/ticketing/targets/targets/#list-targets)
  * [Show Target](/api-reference/ticketing/targets/targets/#show-target)
  * [Create Target](/api-reference/ticketing/targets/targets/#create-target)
  * [Update Target](/api-reference/ticketing/targets/targets/#update-target)
  * [Delete Target](/api-reference/ticketing/targets/targets/#delete-target)


**Important:** Zendesk is [discontinuing support for URL targets and branded targets](https://support.zendesk.com/hc/en-us/articles/6468124845210-Announcing-the-deprecation-of-URL-targets-and-branded-targets) in favor of webhooks. From October 28, 2024, existing URL targets and branded targets will no longer function. There will be no change to Email targets.

Targets are pointers to cloud-based applications and services such as X (formerly Twitter) and Twilio, as well as to HTTP and email addresses. You can use targets with triggers and automations to send a notification to the target when a ticket is created or updated. For a list of targets, see [Notifying external targets](https://support.zendesk.com/hc/en-us/articles/203662136).

To specify a target notification as an action for a trigger or automation, use the action's `notification_target` field. The field's value is an array of two strings specifying the numeric ID of the target and the message body. Example:


    {  "actions": [    {"field": "notification_target", "value": ["32322", "Ticket {{ticket.id}} has been updated."]}  ]}

For more information, see [Triggers](/api-reference/ticketing/business-rules/triggers/) or [Automations](/api-reference/ticketing/business-rules/automations/).

### JSON format

Targets are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
active| boolean| false| false| Whether or not the target is activated
created_at| string| true| false| The time the target was created
id| integer| true| false| Automatically assigned when created
title| string| false| true| A name for the target
type| string| false| true| A pre-defined target, such as "basecamp_target". See the additional attributes for the type that follow

Besides the common fields, the target may have extra properties depending on its type.

"basecamp_target" has the following additional attributes:

Name| Type| Mandatory| Comment
---|---|---|---
target_url| string| yes| The URL of your Basecamp account, including protocol and path
username| string| | The 37Signals username of the account you use to log in to Basecamp
password| string| | The 37Signals password for the Basecamp account (only writable)
token| string| yes| Get the API token from My info > Show your tokens > Token for feed readers or the Basecamp API in your Basecamp account
project_id| string| yes| The ID of the project in Basecamp where updates should be pushed
resource| string| yes| "todo" or "message"
message_id| string| | Can be filled if it is a "todo" resource
todo_list_id| string| | Can be filled if it is a "message" resource

"campfire_target" has the following additional attributes:

Name| Type| Mandatory| Comment
---|---|---|---
subdomain| string| yes|
ssl| boolean| |
room| string| yes|
token| string| yes|
preserve_format| boolean| |

"clickatell_target" has the following additional attributes:

Name| Type| Mandatory| Comment
---|---|---|---
target_url| string| | Read-only
method| string| | Read-only
attribute| string| | Read-only
username| string| yes|
password| string| yes| only writable
api_id| string| yes|
to| string| yes|
from| string| |
us_small_business_account| string| Possible values: "0" or "1" for false or true|

"email_target" has the following additional attributes:

Name| Type| Mandatory| Comment
---|---|---|---
email| string| yes|
subject| string| yes|

"flowdock_target" has the following additional attributes:

Name| Type| Mandatory| Comment
---|---|---|---
api_token| string| yes|

"get_satisfaction_target" has the following additional attributes:

Name| Type| Mandatory| Comment
---|---|---|---
email| string| yes|
password| string| yes| only writable
account_name| string| yes|
target_url| string| |

"jira_target" has the following additional attributes:

Name| Type| Mandatory| Comment
---|---|---|---
target_url| string| yes|
username| string| yes|
password| string| yes| only writable

"pivotal_target" has the following additional attributes:

Name| Type| Mandatory| Comment
---|---|---|---
token| string| yes|
project_id| string| yes|
story_type| string| yes|
story_title| string| yes|
requested_by| string| |
owner_by| string| |
story_labels| string| |

"twitter_target" has the following additional attributes:

Name| Type| Mandatory| Comment
---|---|---|---
token| string| |
secret| string| | only writable

"url_target" has the following additional attributes:

Name| Type| Mandatory| Comment
---|---|---|---
target_url| string| yes|
method| string| | "get"
attribute| string| yes|
username| string| |
password| string| | only writable

"yammer_target" has the following additional attributes:

Name| Type| Mandatory| Comment
---|---|---|---
group_id| string| |
token| string| |

#### Example


    {  "active": false,  "created_at": "2012-02-20T22:55:29Z",  "id": 88335,  "title": "basecamp target",  "type": "basecamp_target",  "url": "https://company.zendesk.com/api/v2/targets/88335"}

### List Targets

  * `GET /api/v2/targets`


#### Allowed For

  * Agents


#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/targets \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/targets"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/targets")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/targets',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/targets"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/targets")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "targets": [    {      "active": true,      "created_at": "2009-05-13T00:07:08Z",      "id": 211,      "title": "Fancy box",      "type": "basecamp_target"    }  ]}

### Show Target

  * `GET /api/v2/targets/{target_id}`


#### Allowed For

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
target_id| integer| Path| true| The ID of the target

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/targets/{target_id} \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/targets/211"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/targets/211")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/targets/211',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/targets/211"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/targets/211")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "target": {    "active": true,    "created_at": "2009-05-13T00:07:08Z",    "id": 211,    "title": "Fancy box",    "type": "basecamp_target"  }}

### Create Target

  * `POST /api/v2/targets`


#### Allowed For

  * Admins


#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/targets \  -H "Content-Type: application/json" -X POST \  -d '{"target": {"type": "email_target", "title": "Test Email Target", "email": "[[email protected]](/cdn-cgi/l/email-protection)", "subject": "Test Target"}}' \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/targets"	method := "POST"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/targets")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'POST',  url: 'https://example.zendesk.com/api/v2/targets',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/targets"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/targets")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**201 Created**


    // Status 201 Created
    {  "target": {    "active": true,    "created_at": "2009-05-13T00:07:08Z",    "email": "[[email protected]](/cdn-cgi/l/email-protection)",    "subject": "Test Target",    "title": "Test Email Target",    "type": "email_target"  }}

### Update Target

  * `PUT /api/v2/targets/{target_id}`


#### Allowed For

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
target_id| integer| Path| true| The ID of the target

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/targets/{target_id} \  -H "Content-Type: application/json" -X PUT \  -d '{"target": {"email": "[[email protected]](/cdn-cgi/l/email-protection)"}}' \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/targets/211"	method := "PUT"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/targets/211")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'PUT',  url: 'https://example.zendesk.com/api/v2/targets/211',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/targets/211"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/targets/211")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "target": {    "active": true,    "created_at": "2009-05-13T00:07:08Z",    "email": "[[email protected]](/cdn-cgi/l/email-protection)",    "subject": "Test Target",    "title": "Test Email Target",    "type": "email_target"  }}

### Delete Target

  * `DELETE /api/v2/targets/{target_id}`


#### Allowed For

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
target_id| integer| Path| true| The ID of the target

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/targets/{target_id} \  -H "Content-Type: application/json" -X DELETE \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/targets/211"	method := "DELETE"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/targets/211")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("DELETE", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'DELETE',  url: 'https://example.zendesk.com/api/v2/targets/211',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/targets/211"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"DELETE",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/targets/211")request = Net::HTTP::Delete.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**204 No Content**


    // Status 204 No Content
    null

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)