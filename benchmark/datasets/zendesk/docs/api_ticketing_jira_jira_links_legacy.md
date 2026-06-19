# JIRA Links (Legacy)

*Source: https://developer.zendesk.com/api-reference/ticketing/jira/jira_links_legacy/*

---

## On this page

  * [JSON format](/api-reference/ticketing/jira/jira_links_legacy/#json-format)
  * [List Links](/api-reference/ticketing/jira/jira_links_legacy/#list-links)
  * [Show Link](/api-reference/ticketing/jira/jira_links_legacy/#show-link)
  * [Create Link](/api-reference/ticketing/jira/jira_links_legacy/#create-link)
  * [Delete Link](/api-reference/ticketing/jira/jira_links_legacy/#delete-link)
  * [List Links (deprecated)](/api-reference/ticketing/jira/jira_links_legacy/#list-links-deprecated)


# JIRA Links (Legacy)

## On this page

  * [JSON format](/api-reference/ticketing/jira/jira_links_legacy/#json-format)
  * [List Links](/api-reference/ticketing/jira/jira_links_legacy/#list-links)
  * [Show Link](/api-reference/ticketing/jira/jira_links_legacy/#show-link)
  * [Create Link](/api-reference/ticketing/jira/jira_links_legacy/#create-link)
  * [Delete Link](/api-reference/ticketing/jira/jira_links_legacy/#delete-link)
  * [List Links (deprecated)](/api-reference/ticketing/jira/jira_links_legacy/#list-links-deprecated)


A link is the connection between a Jira issue and a Zendesk ticket. You can use this API to list, create, and delete links.

### JSON format

JIRA Links (Legacy) are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
created_at| string| true| false| The time at which the link was created
id| integer| true| false| Automatically assigned when the link is created
issue_id| string| false| true| The id of the Jira issue
issue_key| string| false| true| The key for the Jira issue
ticket_id| string| false| true| The id of the Zendesk ticket
updated_at| string| true| false| The time at which the link was last updated
url| string| false| false| An url to get the link details

The Jira integration uses `issue_id` to identify an issue. `issue_id` is used over `issue_key` because `issue_id` is immutable. An `issue_key` might change after an issue is moved to a different project. You can get an issue's ID using the instructions [here](https://confluence.atlassian.com/jirakb/how-to-get-issue-id-from-the-jira-user-interface-827341428.html) or via the Jira REST API: [Cloud](https://developer.atlassian.com/cloud/jira/platform/rest/#api-api-2-issue-issueIdOrKey-get), [Server](https://developer.atlassian.com/server/jira/platform/rest-apis/).

`issue_key` is also mandatory because it is used to support syncing issue keys to tickets. You can read more about the field sync feature [here](https://support.zendesk.com/hc/en-us/articles/115004257108-Using-the-JIRA-field-syncing-feature).

#### Example


    {  "created_at": "2017-01-01T09:30:00Z",  "id": 1234,  "issue_id": "5460",  "issue_key": "153425890A",  "ticket_id": "5000",  "updated_at": "2017-01-01T09:30:00Z"}

### List Links

  * `GET /api/v2/jira/links`


Lists the links for the current account, ordered by id.

#### Allowed For

  * Admins


#### Pagination

By default, this endpoint retrieves 1000 links per page. You can paginate through the available links and customize the page size with a combination of the `page[after]` and `page[size]` parameters.

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
filter[ticket_id]| integer| Query| false| List links for a specific Zendesk ticket or Jira issue by specifying a ticket id or issue id. Filtering by issue key is not currently supported
page[after]| integer| Query| false| When provided, the returned paginated data must have as its first item the item that is immediately after the cursor in the results list. Exception: If there are no items in the results list that fall after the cursor, the returned paginated data must be an empty array
page[size]| integer| Query| false| The number of entries that will be returned

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/jira/links \  -u {email_address}/token:{api_token}
    # filter links by ticketcurl https://{subdomain}.zendesk.com/api/v2/jira/links?filter[ticket_id]=5000 \  -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/jira/links?filter[ticket_id]=5000&page[after]=1234&page[size]=100"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/jira/links")		.newBuilder()		.addQueryParameter("filter[ticket_id]", "5000")		.addQueryParameter("page[after]", "1234")		.addQueryParameter("page[size]", "100");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/jira/links',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'filter[ticket_id]': '5000',    'page[after]': '1234',    'page[size]': '100',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/jira/links?filter[ticket_id]=5000&page[after]=1234&page[size]=100"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/jira/links")uri.query = URI.encode_www_form("filter[ticket_id]": "5000", "page[after]": "1234", "page[size]": "100")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "links": [    {      "created_at": "2017-01-01T09:30:00Z",      "id": 1234,      "issue_id": "5460",      "issue_key": "153425890A",      "ticket_id": "5000",      "updated_at": "2017-01-01T09:30:00Z"    }  ],  "meta": {    "after_cursor": "https://{subdomain}.zendesk.com/api/v2/jira/links?page[after]=5000",    "has_more": true  }}

### Show Link

  * `GET /api/services/jira/links/{link_id}`


Retrieves a single link.

#### Allowed For

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
link_id| integer| Path| true| The id of the link

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/services/jira/links/{id} \  -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/services/jira/links/1234"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/services/jira/links/1234")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/services/jira/links/1234',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/services/jira/links/1234"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/services/jira/links/1234")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "link": {    "created_at": "2017-01-01T09:30:00Z",    "id": 1234,    "issue_id": "5460",    "issue_key": "153425890A",    "ticket_id": "5000",    "updated_at": "2017-01-01T09:30:00Z",    "url": "https://subdomain.zendesk.com/api/services/jira/links/1234"  }}

### Create Link

  * `POST /api/services/jira/links`


Creates a link.

#### Allowed For

  * Admins


#### Example body


    {  "link": {    "issue_id": "5461",    "issue_key": "153425890A",    "ticket_id": "5001"  }}

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/services/jira/links \  -d '{"link": {"ticket_id": "5001", "issue_id": "5461", "issue_key": "153425890A"}}' \  -H "Content-Type: application/json" \  -u {email_address}/token:{api_token} -X POST

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://support.zendesk.com/api/services/jira/links"	method := "POST"	payload := strings.NewReader(`{  "link": {    "issue_id": "5461",    "issue_key": "153425890A",    "ticket_id": "5001"  }}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/services/jira/links")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"link\": {    \"issue_id\": \"5461\",    \"issue_key\": \"153425890A\",    \"ticket_id\": \"5001\"  }}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "link": {    "issue_id": "5461",    "issue_key": "153425890A",    "ticket_id": "5001"  }});
    var config = {  method: 'POST',  url: 'https://support.zendesk.com/api/services/jira/links',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/services/jira/links"
    payload = json.loads("""{  "link": {    "issue_id": "5461",    "issue_key": "153425890A",    "ticket_id": "5001"  }}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/services/jira/links")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")request.body = %q({  "link": {    "issue_id": "5461",    "issue_key": "153425890A",    "ticket_id": "5001"  }})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**201 Created**


    // Status 201 Created
    {  "link": {    "created_at": "2017-01-01T09:30:00Z",    "id": 1234,    "issue_id": "5460",    "issue_key": "153425890A",    "ticket_id": "5000",    "updated_at": "2017-01-01T09:30:00Z",    "url": "https://subdomain.zendesk.com/api/services/jira/links/1234"  }}

### Delete Link

  * `DELETE /api/services/jira/links/{link_id}`


Removes the given link.

#### Allowed For

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
link_id| integer| Path| true| The id of the link

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/services/jira/links/{id} \  -u {email_address}/token:{api_token} -X DELETE

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/services/jira/links/1234"	method := "DELETE"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/services/jira/links/1234")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("DELETE", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'DELETE',  url: 'https://support.zendesk.com/api/services/jira/links/1234',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/services/jira/links/1234"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"DELETE",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/services/jira/links/1234")request = Net::HTTP::Delete.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**204 No Content**


    // Status 204 No Content
    null

### List Links (deprecated)

  * `GET /api/services/jira/links`


**Note** : This endpoint is deprecated. Use the List Links endpoint (`GET /api/v2/jira/links`) instead.

Lists the links for the current account, ordered by id.

#### Pagination

By default, this endpoint retrieves 1000 links per page. You can walk through the available links and customize the page size with a combination of the `since_id` and `limit` parameters.

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
limit| integer| Query| false| The number of entries that will be returned
since_id| integer| Query| false| The start id of the collection
ticket_id| integer| Query| false| List links for a specific Zendesk Ticket or Jira issue by providing `ticket_id` and/or `issue_id` param. We currently do not support `issue_key` param.

#### Code Samples

**curl**


    curl -u {email_address}/token:{api_token} -X GET \  https://{subdomain}.zendesk.com/api/services/jira/links
    # filter links by ticketcurl -u {email_address}/token:{api_token} \  https://{subdomain}.zendesk.com/api/services/jira/links?ticket_id=5000

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/services/jira/links?limit=100&since_id=1234&ticket_id=5000"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/services/jira/links")		.newBuilder()		.addQueryParameter("limit", "100")		.addQueryParameter("since_id", "1234")		.addQueryParameter("ticket_id", "5000");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/services/jira/links',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'limit': '100',    'since_id': '1234',    'ticket_id': '5000',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/services/jira/links?limit=100&since_id=1234&ticket_id=5000"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/services/jira/links")uri.query = URI.encode_www_form("limit": "100", "since_id": "1234", "ticket_id": "5000")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "links": [    {      "created_at": "2017-01-01T09:30:00Z",      "id": 1234,      "issue_id": "5460",      "issue_key": "153425890A",      "ticket_id": "5000",      "updated_at": "2017-01-01T09:30:00Z"    }  ]}

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)