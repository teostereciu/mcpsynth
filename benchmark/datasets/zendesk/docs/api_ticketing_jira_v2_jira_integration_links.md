# JIRA Integration Links

*Source: https://developer.zendesk.com/api-reference/ticketing/jira_v2/jira_integration_links/*

---

## On this page

  * [Overview](/api-reference/ticketing/jira_v2/jira_integration_links/#overview)
  * [JSON format](/api-reference/ticketing/jira_v2/jira_integration_links/#json-format)
  * [Properties](/api-reference/ticketing/jira_v2/jira_integration_links/#properties)
  * [List Links](/api-reference/ticketing/jira_v2/jira_integration_links/#list-links)
  * [Create Link](/api-reference/ticketing/jira_v2/jira_integration_links/#create-link)
  * [Get Link](/api-reference/ticketing/jira_v2/jira_integration_links/#get-link)
  * [Delete Link](/api-reference/ticketing/jira_v2/jira_integration_links/#delete-link)


# JIRA Integration Links

## On this page

  * [Overview](/api-reference/ticketing/jira_v2/jira_integration_links/#overview)
  * [JSON format](/api-reference/ticketing/jira_v2/jira_integration_links/#json-format)
  * [Properties](/api-reference/ticketing/jira_v2/jira_integration_links/#properties)
  * [List Links](/api-reference/ticketing/jira_v2/jira_integration_links/#list-links)
  * [Create Link](/api-reference/ticketing/jira_v2/jira_integration_links/#create-link)
  * [Get Link](/api-reference/ticketing/jira_v2/jira_integration_links/#get-link)
  * [Delete Link](/api-reference/ticketing/jira_v2/jira_integration_links/#delete-link)


JIRA Links represent the association between a Zendesk ticket and a Jira issue. When a link is created, updates to the linked Jira issue can be synced to the Zendesk ticket and vice versa.

### Overview

  * A Zendesk ticket can be linked to multiple Jira issues
  * A Jira issue can be linked to multiple Zendesk tickets
  * Links are bidirectional and enable data synchronization between the two systems


### JSON format

JIRA Integration Links are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
issue_id| string| false| true| The ID of the Jira issue
issue_key| string| false| true| The key of the Jira issue (e.g., "PROJ-123")
ticket_id| string| false| true| The ID of the Zendesk ticket

Represents a link between a Zendesk ticket and a Jira issue.

### Properties

Property| Type| Description
---|---|---
`ticket_id`| string| The id of the Zendesk ticket
`issue_id`| string| The id of the Jira issue
`issue_key`| string| The key for the Jira issue (e.g., "PROJ-123")
`external_id`| string| The external identifier for the link. To get this value, go to the Zendesk Admin Center, then select Apps and integrations > Integrations > Jira > Edit.

### List Links

  * `GET /api/v2/integrations/jira/{external_id}/links`


Lists the links for the specified Jira integration.

#### Allowed For

  * Admins


#### Pagination

Use cursor-based pagination with `page[after]` or `page[before]` parameters. Page size defaults to 100 and can be customized with `page[size]`.

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
issue_id| string| Query| false| Filter links by Jira issue ID
page[after]| string| Query| false| Cursor for forward pagination
page[before]| string| Query| false| Cursor for backward pagination
page[size]| integer| Query| false| Number of results per page (max 100)
ticket_id| string| Query| false| Filter links by Zendesk ticket ID
external_id| string| Path| true| The external ID of the Jira integration. To get this value, go to the Zendesk Admin Center, then select Apps and integrations > Integrations > Jira > Edit.

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/integrations/jira/{external_id}/links \  -u {email_address}/token:{api_token}
    # filter links by ticketcurl "https://{subdomain}.zendesk.com/api/v2/integrations/jira/{external_id}/links?ticket_id=5001" \  -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/integrations/jira/abc123/links?issue_id=10001&page[after]=&page[before]=&page[size]=&ticket_id=5001"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/integrations/jira/abc123/links")		.newBuilder()		.addQueryParameter("issue_id", "10001")		.addQueryParameter("page[after]", "")		.addQueryParameter("page[before]", "")		.addQueryParameter("page[size]", "")		.addQueryParameter("ticket_id", "5001");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/integrations/jira/abc123/links',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'issue_id': '10001',    'page[after]': '',    'page[before]': '',    'page[size]': '',    'ticket_id': '5001',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/integrations/jira/abc123/links?issue_id=10001&page[after]=&page[before]=&page[size]=&ticket_id=5001"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/integrations/jira/abc123/links")uri.query = URI.encode_www_form("issue_id": "10001", "page[after]": "", "page[before]": "", "page[size]": "", "ticket_id": "5001")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "count": 2,  "links": [    {      "issue_id": "10001",      "issue_key": "PROJ-123",      "ticket_id": "5001"    },    {      "issue_id": "10002",      "issue_key": "PROJ-124",      "ticket_id": "5002"    }  ],  "meta": {    "after": "eyJpZCI6MTAwMX0",    "before": "",    "has_more": true  }}

**400 Bad Request**


    // Status 400 Bad Request
    {  "errors": [    {      "code": "BadRequest",      "title": "Cannot use both page[after] and page[before] parameters"    }  ]}

**403 Forbidden**


    // Status 403 Forbidden
    {  "errors": [    {      "code": "Forbidden",      "title": "Link automation is not allowed for this integration"    }  ]}

### Create Link

  * `POST /api/v2/integrations/jira/{external_id}/links`


Creates a link between a Zendesk ticket and a Jira issue.

#### Allowed For

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
external_id| string| Path| true| The external ID of the Jira integration. To get this value, go to the Zendesk Admin Center, then select Apps and integrations > Integrations > Jira > Edit.

#### Example body


    {  "link": {    "issue_id": "10001",    "issue_key": "PROJ-123",    "ticket_id": "5001"  }}

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/integrations/jira/{external_id}/links \  -d '{"link": {"ticket_id": "5001", "issue_id": "10001", "issue_key": "PROJ-123"}}' \  -H "Content-Type: application/json" \  -u {email_address}/token:{api_token} -X POST

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://support.zendesk.com/api/v2/integrations/jira/abc123/links"	method := "POST"	payload := strings.NewReader(`{  "link": {    "issue_id": "10001",    "issue_key": "PROJ-123",    "ticket_id": "5001"  }}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/integrations/jira/abc123/links")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"link\": {    \"issue_id\": \"10001\",    \"issue_key\": \"PROJ-123\",    \"ticket_id\": \"5001\"  }}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "link": {    "issue_id": "10001",    "issue_key": "PROJ-123",    "ticket_id": "5001"  }});
    var config = {  method: 'POST',  url: 'https://support.zendesk.com/api/v2/integrations/jira/abc123/links',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/integrations/jira/abc123/links"
    payload = json.loads("""{  "link": {    "issue_id": "10001",    "issue_key": "PROJ-123",    "ticket_id": "5001"  }}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/integrations/jira/abc123/links")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")request.body = %q({  "link": {    "issue_id": "10001",    "issue_key": "PROJ-123",    "ticket_id": "5001"  }})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**201 Created**


    // Status 201 Created
    {  "link": {    "issue_id": "10001",    "issue_key": "PROJ-123",    "ticket_id": "5001"  }}

**400 Bad Request**


    // Status 400 Bad Request
    {  "errors": [    {      "code": "BadRequest",      "title": "Invalid request body"    }  ]}

**403 Forbidden**


    // Status 403 Forbidden
    {  "errors": [    {      "code": "Forbidden",      "title": "Link automation is not allowed for this integration"    }  ]}

**409 Conflict**


    // Status 409 Conflict
    {  "errors": [    {      "code": "LinkAlreadyExists",      "title": "Issue is already linked to ticket 5001"    }  ]}

### Get Link

  * `GET /api/v2/integrations/jira/{external_id}/links/ticket/{ticket_id}/issue/{issue_id}`


Retrieves a specific link between a Zendesk ticket and a Jira issue.

#### Allowed For

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
external_id| string| Path| true| The external ID of the Jira integration. To get this value, go to the Zendesk Admin Center, then select Apps and integrations > Integrations > Jira > Edit.
issue_id| string| Path| true| The Jira issue ID
ticket_id| string| Path| true| The Zendesk ticket ID

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/integrations/jira/{external_id}/links/ticket/{ticket_id}/issue/{issue_id} \  -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/integrations/jira/abc123/links/ticket/5001/issue/10001"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/integrations/jira/abc123/links/ticket/5001/issue/10001")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/integrations/jira/abc123/links/ticket/5001/issue/10001',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/integrations/jira/abc123/links/ticket/5001/issue/10001"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/integrations/jira/abc123/links/ticket/5001/issue/10001")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "link": {    "issue_id": "10001",    "issue_key": "PROJ-123",    "ticket_id": "5001"  }}

**403 Forbidden**


    // Status 403 Forbidden
    {  "errors": [    {      "code": "Forbidden",      "title": "Link automation is not allowed for this integration"    }  ]}

**404 Not Found**


    // Status 404 Not Found
    {  "errors": [    {      "code": "NotFound",      "title": "Link not found"    }  ]}

### Delete Link

  * `DELETE /api/v2/integrations/jira/{external_id}/links/ticket/{ticket_id}/issue/{issue_id}`


Removes the link between a Zendesk ticket and a Jira issue.

#### Allowed For

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
external_id| string| Path| true| The external ID of the Jira integration. To get this value, go to the Zendesk Admin Center, then select Apps and integrations > Integrations > Jira > Edit.
issue_id| string| Path| true| The Jira issue ID
ticket_id| string| Path| true| The Zendesk ticket ID

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/integrations/jira/{external_id}/links/ticket/{ticket_id}/issue/{issue_id} \  -u {email_address}/token:{api_token} -X DELETE

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/integrations/jira/abc123/links/ticket/5001/issue/10001"	method := "DELETE"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/integrations/jira/abc123/links/ticket/5001/issue/10001")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("DELETE", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'DELETE',  url: 'https://support.zendesk.com/api/v2/integrations/jira/abc123/links/ticket/5001/issue/10001',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/integrations/jira/abc123/links/ticket/5001/issue/10001"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"DELETE",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/integrations/jira/abc123/links/ticket/5001/issue/10001")request = Net::HTTP::Delete.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**204 No Content**


    // Status 204 No Content
    null

**400 Bad Request**


    // Status 400 Bad Request
    {  "errors": [    {      "code": "BadRequest",      "title": "Invalid request body"    }  ]}

**403 Forbidden**


    // Status 403 Forbidden
    {  "errors": [    {      "code": "Forbidden",      "title": "Link automation is not allowed for this integration"    }  ]}

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)