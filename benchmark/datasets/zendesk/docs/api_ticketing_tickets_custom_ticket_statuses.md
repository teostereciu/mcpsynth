# Custom Ticket Statuses

*Source: https://developer.zendesk.com/api-reference/ticketing/tickets/custom_ticket_statuses/*

---

## On this page

  * [Status categories](/api-reference/ticketing/tickets/custom_ticket_statuses/#status-categories)
  * [Limitations](/api-reference/ticketing/tickets/custom_ticket_statuses/#limitations)
  * [JSON format](/api-reference/ticketing/tickets/custom_ticket_statuses/#json-format)
  * [List Custom Ticket Statuses](/api-reference/ticketing/tickets/custom_ticket_statuses/#list-custom-ticket-statuses)
  * [Show Custom Ticket Status](/api-reference/ticketing/tickets/custom_ticket_statuses/#show-custom-ticket-status)
  * [Create Custom Ticket Status](/api-reference/ticketing/tickets/custom_ticket_statuses/#create-custom-ticket-status)
  * [Update Custom Ticket Status](/api-reference/ticketing/tickets/custom_ticket_statuses/#update-custom-ticket-status)
  * [Bulk Update Default Custom Ticket Status](/api-reference/ticketing/tickets/custom_ticket_statuses/#bulk-update-default-custom-ticket-status)
  * [Delete Custom Ticket Status](/api-reference/ticketing/tickets/custom_ticket_statuses/#delete-custom-ticket-status)
  * [Create Ticket Form Statuses for a Custom Status](/api-reference/ticketing/tickets/custom_ticket_statuses/#create-ticket-form-statuses-for-a-custom-status)


# Custom Ticket Statuses

## On this page

  * [Status categories](/api-reference/ticketing/tickets/custom_ticket_statuses/#status-categories)
  * [Limitations](/api-reference/ticketing/tickets/custom_ticket_statuses/#limitations)
  * [JSON format](/api-reference/ticketing/tickets/custom_ticket_statuses/#json-format)
  * [List Custom Ticket Statuses](/api-reference/ticketing/tickets/custom_ticket_statuses/#list-custom-ticket-statuses)
  * [Show Custom Ticket Status](/api-reference/ticketing/tickets/custom_ticket_statuses/#show-custom-ticket-status)
  * [Create Custom Ticket Status](/api-reference/ticketing/tickets/custom_ticket_statuses/#create-custom-ticket-status)
  * [Update Custom Ticket Status](/api-reference/ticketing/tickets/custom_ticket_statuses/#update-custom-ticket-status)
  * [Bulk Update Default Custom Ticket Status](/api-reference/ticketing/tickets/custom_ticket_statuses/#bulk-update-default-custom-ticket-status)
  * [Delete Custom Ticket Status](/api-reference/ticketing/tickets/custom_ticket_statuses/#delete-custom-ticket-status)
  * [Create Ticket Form Statuses for a Custom Status](/api-reference/ticketing/tickets/custom_ticket_statuses/#create-ticket-form-statuses-for-a-custom-status)


Zendesk has a default set of system ticket statuses that help you manage ticket workflows. If your account has activated custom ticket statuses, you can create additional, more-specific ticket statuses.

For more information about custom ticket statuses, see [Activating custom ticket statuses](https://support.zendesk.com/hc/en-us/articles/4412575841306) in Zendesk help.

### Status categories

Each custom ticket status belongs to a status category. Each category corresponds to one of the built-in system ticket statuses:

  * "new"
  * "open"
  * "pending"
  * "hold"
  * "solved"


**Note:** Tickets with a "Closed" status belong to the "solved" status category.

You can't create, change, or delete status categories.

#### Changing the default ticket status of a status category

Each status category has a default ticket status that's always active. When using the API, you can only change a category's default ticket status using a Bulk Update Default Custom Ticket Status request.

**Note:** The "hold" status category and its corresponding system ticket status are optional. If it's inactive, the "hold" status category doesn't require an active default ticket status.

### Limitations

Custom ticket statuses have the following limitations:

  * 300 custom ticket statuses per account
  * 100 custom ticket statuses per status category


### JSON format

Custom Ticket Statuses are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
active| boolean| false| false| If true, the custom status is set to active, If false, the custom status is set to inactive
agent_label| string| false| true| The label displayed to agents. Maximum length is 48 characters
created_at| string| true| false| The date and time the custom ticket status was created
default| boolean| false| false| If true, the custom status is set to default. If false, the custom status is set to non-default
description| string| false| false| The description of when the user should select this custom ticket status
end_user_description| string| false| false| The description displayed to end users
end_user_label| string| false| false| The label displayed to end users. Maximum length is 48 characters
id| integer| true| false| Automatically assigned when the custom ticket status is created
raw_agent_label| string| true| false| The dynamic content placeholder. If the dynamic content placeholder is not available, this is the "agent_label" value. See [Dynamic Content Items](/api-reference/ticketing/ticket-management/dynamic_content/)
raw_description| string| true| false| The dynamic content placeholder. If the dynamic content placeholder is not available, this is the "description" value. [Dynamic Content Items](/api-reference/ticketing/ticket-management/dynamic_content/)
raw_end_user_description| string| true| false| The dynamic content placeholder. If the dynamic content placeholder is not available, this is the "end_user_description" value. See [Dynamic Content Items](/api-reference/ticketing/ticket-management/dynamic_content/)
raw_end_user_label| string| true| false| The dynamic content placeholder. If the dynamic content placeholder is not available, this is the "end_user_label" value. See [Dynamic Content Items](/api-reference/ticketing/ticket-management/dynamic_content/)
status_category| string| false| true| The status category the custom ticket status belongs to. Allowed values are "new", "open", "pending", "hold", or "solved".
updated_at| string| true| false| The date and time the custom ticket status was last updated

### List Custom Ticket Statuses

  * `GET /api/v2/custom_statuses`


Lists all undeleted custom ticket statuses for the account. No pagination is provided.

#### Allowed For

  * End Users


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
active| boolean| Query| false| If true, show only active custom ticket statuses. If false, show only inactive custom ticket statuses. If the filter is not used, show all custom ticket statuses
default| boolean| Query| false| If true, show only default custom ticket statuses. If false, show only non-default custom ticket statuses. If the filter is not used, show all custom ticket statuses
status_categories| string| Query| false| Filter the list of custom ticket statuses by a comma-separated list of status categories

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/custom_statuses \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/custom_statuses?active=&default=&status_categories="	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/custom_statuses")		.newBuilder()		.addQueryParameter("active", "")		.addQueryParameter("default", "")		.addQueryParameter("status_categories", "");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/custom_statuses',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'active': '',    'default': '',    'status_categories': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/custom_statuses?active=&default=&status_categories="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/custom_statuses")uri.query = URI.encode_www_form("active": "", "default": "", "status_categories": "")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "custom_statuses": [    {      "active": true,      "agent_label": "Responding quickly",      "created_at": "2021-07-20T22:55:29Z",      "default": false,      "description": "Customer needs a response quickly",      "end_user_description": "Your ticket is being responded to",      "end_user_label": "Urgent processing",      "id": 35436,      "raw_agent_label": "Responding quickly",      "raw_description": "Customer needs a response quickly",      "raw_end_user_description": "Your ticket is being responded to",      "raw_end_user_label": "Urgent processing",      "status_category": "open",      "updated_at": "2021-07-20T22:55:29Z"    }  ]}

### Show Custom Ticket Status

  * `GET /api/v2/custom_statuses/{custom_status_id}`


Returns the custom ticket status object.

#### Allowed For

  * End Users


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
custom_status_id| integer| Path| true| The id of the custom status

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/custom_status/{custom_status_id} \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/custom_statuses/1234567"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/custom_statuses/1234567")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/custom_statuses/1234567',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/custom_statuses/1234567"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/custom_statuses/1234567")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "custom_status": {    "active": true,    "agent_label": "Responding quickly",    "created_at": "2021-07-20T22:55:29Z",    "default": false,    "description": "Customer needs a response quickly",    "end_user_description": "Your ticket is being responded to",    "end_user_label": "Urgent processing",    "id": 35436,    "raw_agent_label": "Responding quickly",    "raw_description": "Customer needs a response quickly",    "raw_end_user_description": "Your ticket is being responded to",    "raw_end_user_label": "Urgent processing",    "status_category": "open",    "updated_at": "2021-07-20T22:55:29Z"  }}

### Create Custom Ticket Status

  * `POST /api/v2/custom_statuses`


Takes a `custom_status` object that specifies the custom ticket status properties to create.

#### Allowed For

  * Admins


#### Request body format

Name| Type| Mandatory| Description
---|---|---|---
active| boolean| false| If true, the custom status is set to active. If false, the custom status is set to inactive
agent_label| string| true| The dynamic content placeholder or the label displayed to agents. Maximum length for displayed label is 48 characters
description| string| false| The description of when the user should select this custom ticket status
end_user_description| false| false| The description displayed to end users
end_user_label| string| false| The dynamic content placeholder or the label displayed to end users. Maximum length for displayed label is 48 characters
status_category| string| true| The status category the custom status belongs to. Allowed values are "new", "open", "pending", "hold", or "solved"

#### Example body


    {  "custom_status": {    "active": true,    "agent_label": "Responding quickly",    "description": "Customer needs a response quickly",    "end_user_description": "Your ticket is being responded to",    "end_user_label": "Urgent processing",    "status_category": "open"  }}

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/custom_statuses \  -d '{"custom_status": {"status_category": "open", "agent_label": "Responding quickly", "end_user_label": "Urgent processing", "description": "Responding quickly", "end_user_description": "Responding quickly"}}' \  -H "Content-Type: application/json" -v -u {email_address}/token:{api_token} -X POST

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://example.zendesk.com/api/v2/custom_statuses"	method := "POST"	payload := strings.NewReader(`{  "custom_status": {    "active": true,    "agent_label": "Responding quickly",    "description": "Customer needs a response quickly",    "end_user_description": "Your ticket is being responded to",    "end_user_label": "Urgent processing",    "status_category": "open"  }}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/custom_statuses")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"custom_status\": {    \"active\": true,    \"agent_label\": \"Responding quickly\",    \"description\": \"Customer needs a response quickly\",    \"end_user_description\": \"Your ticket is being responded to\",    \"end_user_label\": \"Urgent processing\",    \"status_category\": \"open\"  }}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "custom_status": {    "active": true,    "agent_label": "Responding quickly",    "description": "Customer needs a response quickly",    "end_user_description": "Your ticket is being responded to",    "end_user_label": "Urgent processing",    "status_category": "open"  }});
    var config = {  method: 'POST',  url: 'https://example.zendesk.com/api/v2/custom_statuses',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/custom_statuses"
    payload = json.loads("""{  "custom_status": {    "active": true,    "agent_label": "Responding quickly",    "description": "Customer needs a response quickly",    "end_user_description": "Your ticket is being responded to",    "end_user_label": "Urgent processing",    "status_category": "open"  }}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/custom_statuses")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")request.body = %q({  "custom_status": {    "active": true,    "agent_label": "Responding quickly",    "description": "Customer needs a response quickly",    "end_user_description": "Your ticket is being responded to",    "end_user_label": "Urgent processing",    "status_category": "open"  }})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**201 Created**


    // Status 201 Created
    {  "custom_status": {    "active": true,    "agent_label": "Responding quickly",    "created_at": "2021-07-20T22:55:29Z",    "default": false,    "description": "Customer needs a response quickly",    "end_user_description": "Your ticket is being responded to",    "end_user_label": "Urgent processing",    "id": 35436,    "raw_agent_label": "Responding quickly",    "raw_description": "Customer needs a response quickly",    "raw_end_user_description": "Your ticket is being responded to",    "raw_end_user_label": "Urgent processing",    "status_category": "open",    "updated_at": "2021-07-20T22:55:29Z"  }}

### Update Custom Ticket Status

  * `PUT /api/v2/custom_statuses/{custom_status_id}`


Takes a `custom_status` object that specifies the properties to update.

#### Allowed For

  * Admins


#### Request body format

Name| Type| Description
---|---|---
active| boolean| If true, the custom status is set to active. If false, the custom status is set to inactive
agent_label| string| The dynamic content placeholder or the label displayed to agents. Maximum length for displayed label is 48 characters
description| string| The description of when the user should select this custom ticket status
end_user_description| string| The description displayed to end users
end_user_label| string| The dynamic content placeholder or the label displayed to end users. Maximum length for displayed label is 48 characters

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
custom_status_id| integer| Path| true| The id of the custom status

#### Example body


    {  "custom_status": {    "active": true,    "agent_label": "Responding quickly",    "description": "Customer needs a response quickly",    "end_user_description": "Your ticket is being responded to",    "end_user_label": "Urgent processing"  }}

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/custom_statuses/{custom_status_id} \  -d '{"custom_status": {"agent_label": "{{dc.quick}}", "end_user_label": "{{dc.urgent}}"}}' \  -H "Content-Type: application/json" -v -u {email_address}/token:{api_token} -X PUT

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://example.zendesk.com/api/v2/custom_statuses/1234567"	method := "PUT"	payload := strings.NewReader(`{  "custom_status": {    "active": true,    "agent_label": "Responding quickly",    "description": "Customer needs a response quickly",    "end_user_description": "Your ticket is being responded to",    "end_user_label": "Urgent processing"  }}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/custom_statuses/1234567")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"custom_status\": {    \"active\": true,    \"agent_label\": \"Responding quickly\",    \"description\": \"Customer needs a response quickly\",    \"end_user_description\": \"Your ticket is being responded to\",    \"end_user_label\": \"Urgent processing\"  }}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "custom_status": {    "active": true,    "agent_label": "Responding quickly",    "description": "Customer needs a response quickly",    "end_user_description": "Your ticket is being responded to",    "end_user_label": "Urgent processing"  }});
    var config = {  method: 'PUT',  url: 'https://example.zendesk.com/api/v2/custom_statuses/1234567',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/custom_statuses/1234567"
    payload = json.loads("""{  "custom_status": {    "active": true,    "agent_label": "Responding quickly",    "description": "Customer needs a response quickly",    "end_user_description": "Your ticket is being responded to",    "end_user_label": "Urgent processing"  }}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/custom_statuses/1234567")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")request.body = %q({  "custom_status": {    "active": true,    "agent_label": "Responding quickly",    "description": "Customer needs a response quickly",    "end_user_description": "Your ticket is being responded to",    "end_user_label": "Urgent processing"  }})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "custom_status": {    "active": true,    "agent_label": "Responding quickly",    "created_at": "2021-07-20T22:55:29Z",    "default": false,    "description": "Customer needs a response quickly",    "end_user_description": "Your ticket is being responded to",    "end_user_label": "Urgent processing",    "id": 35436,    "raw_agent_label": "Responding quickly",    "raw_description": "Customer needs a response quickly",    "raw_end_user_description": "Your ticket is being responded to",    "raw_end_user_label": "Urgent processing",    "status_category": "open",    "updated_at": "2021-07-20T22:55:29Z"  }}

### Bulk Update Default Custom Ticket Status

  * `PUT /api/v2/custom_status/default`


Updates the default values for many custom ticket statuses at once.

#### Allowed For

  * Admins


#### Request body format

Name| Type| Description
---|---|---
ids| string| The comma-separated list of custom status ids to be set as default for their category

#### Example body


    {  "ids": "1234567,1234577"}

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/custom_status/default \  -d '{"ids": "1234567,1234577"}' \  -H "Content-Type: application/json" -v -u {email_address}/token:{api_token} -X PUT

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://example.zendesk.com/api/v2/custom_status/default"	method := "PUT"	payload := strings.NewReader(`{  "ids": "1234567,1234577"}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/custom_status/default")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"ids\": \"1234567,1234577\"}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "ids": "1234567,1234577"});
    var config = {  method: 'PUT',  url: 'https://example.zendesk.com/api/v2/custom_status/default',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/custom_status/default"
    payload = json.loads("""{  "ids": "1234567,1234577"}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/custom_status/default")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")request.body = %q({  "ids": "1234567,1234577"})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {}

### Delete Custom Ticket Status

  * `DELETE /api/v2/custom_statuses/{custom_status_id}`


Deletes the custom ticket status. The status must first be unassigned from all active (non-closed) tickets before it can be deleted.

#### Allowed For

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
custom_status_id| integer| Path| true| The id of the custom status

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/custom_statuses/{custom_status_id} \  -v -u {email_address}/token:{api_token} -X DELETE

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/custom_statuses/1234567"	method := "DELETE"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/custom_statuses/1234567")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("DELETE", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'DELETE',  url: 'https://example.zendesk.com/api/v2/custom_statuses/1234567',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/custom_statuses/1234567"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"DELETE",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/custom_statuses/1234567")request = Net::HTTP::Delete.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**204 No Content**


    // Status 204 No Content
    null

### Create Ticket Form Statuses for a Custom Status

  * `POST /api/v2/custom_statuses/{custom_status_id}/ticket_form_statuses`


Creates one or many tickets form status associations for a custom status.

#### Allowed For

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
custom_status_id| integer| Path| true| The id of the custom status

#### Example body


    {  "ticket_form_status": [    {      "ticket_form_id": 1    },    {      "ticket_form_id": 2    },    {      "ticket_form_id": 3    }  ]}

#### Code Samples

**Curl**


    curl --request POST https://example.zendesk.com/api/v2/custom_statuses/1234567/ticket_form_statuses \--header "Content-Type: application/json" \-u {email_address}/token:{api_token} \--data-raw '{  "ticket_form_status": [    {      "ticket_form_id": 1    },    {      "ticket_form_id": 2    },    {      "ticket_form_id": 3    }  ]}'

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://example.zendesk.com/api/v2/custom_statuses/1234567/ticket_form_statuses"	method := "POST"	payload := strings.NewReader(`{  "ticket_form_status": [    {      "ticket_form_id": 1    },    {      "ticket_form_id": 2    },    {      "ticket_form_id": 3    }  ]}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/custom_statuses/1234567/ticket_form_statuses")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"ticket_form_status\": [    {      \"ticket_form_id\": 1    },    {      \"ticket_form_id\": 2    },    {      \"ticket_form_id\": 3    }  ]}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "ticket_form_status": [    {      "ticket_form_id": 1    },    {      "ticket_form_id": 2    },    {      "ticket_form_id": 3    }  ]});
    var config = {  method: 'POST',  url: 'https://example.zendesk.com/api/v2/custom_statuses/1234567/ticket_form_statuses',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/custom_statuses/1234567/ticket_form_statuses"
    payload = json.loads("""{  "ticket_form_status": [    {      "ticket_form_id": 1    },    {      "ticket_form_id": 2    },    {      "ticket_form_id": 3    }  ]}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/custom_statuses/1234567/ticket_form_statuses")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")request.body = %q({  "ticket_form_status": [    {      "ticket_form_id": 1    },    {      "ticket_form_id": 2    },    {      "ticket_form_id": 3    }  ]})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "ticket_form_statuses": [    {      "custom_status_id": 7485541848574,      "id": "01HFD81Y01D65FJ7EPNNM58GPK",      "ticket_form_id": 7485506877054    }  ]}

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)