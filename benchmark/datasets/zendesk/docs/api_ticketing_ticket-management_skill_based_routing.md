# Skill-based Routing

*Source: https://developer.zendesk.com/api-reference/ticketing/ticket-management/skill_based_routing/*

---

## On this page

  * [JSON format](/api-reference/ticketing/ticket-management/skill_based_routing/#json-format)
  * [List Account Attributes](/api-reference/ticketing/ticket-management/skill_based_routing/#list-account-attributes)
  * [List Routing Attribute Definitions](/api-reference/ticketing/ticket-management/skill_based_routing/#list-routing-attribute-definitions)
  * [Show Attribute](/api-reference/ticketing/ticket-management/skill_based_routing/#show-attribute)
  * [Create Attribute](/api-reference/ticketing/ticket-management/skill_based_routing/#create-attribute)
  * [Update Attribute](/api-reference/ticketing/ticket-management/skill_based_routing/#update-attribute)
  * [Delete Attribute](/api-reference/ticketing/ticket-management/skill_based_routing/#delete-attribute)
  * [List Attribute Values for an Attribute](/api-reference/ticketing/ticket-management/skill_based_routing/#list-attribute-values-for-an-attribute)
  * [Show Attribute Value](/api-reference/ticketing/ticket-management/skill_based_routing/#show-attribute-value)
  * [Create Attribute Value](/api-reference/ticketing/ticket-management/skill_based_routing/#create-attribute-value)
  * [Update Attribute Value](/api-reference/ticketing/ticket-management/skill_based_routing/#update-attribute-value)
  * [Delete Attribute Value](/api-reference/ticketing/ticket-management/skill_based_routing/#delete-attribute-value)
  * [List Agent Attribute Values](/api-reference/ticketing/ticket-management/skill_based_routing/#list-agent-attribute-values)
  * [List Attribute Values for Many Agents](/api-reference/ticketing/ticket-management/skill_based_routing/#list-attribute-values-for-many-agents)
  * [Set Agent Attribute Values](/api-reference/ticketing/ticket-management/skill_based_routing/#set-agent-attribute-values)
  * [Bulk Set Agent Attribute Values Jobs](/api-reference/ticketing/ticket-management/skill_based_routing/#bulk-set-agent-attribute-values-jobs)
  * [List Ticket Attribute Values](/api-reference/ticketing/ticket-management/skill_based_routing/#list-ticket-attribute-values)
  * [Set Ticket Attribute Values](/api-reference/ticketing/ticket-management/skill_based_routing/#set-ticket-attribute-values)
  * [List Tickets Fulfilled by a User](/api-reference/ticketing/ticket-management/skill_based_routing/#list-tickets-fulfilled-by-a-user)


# Skill-based Routing

## On this page

  * [JSON format](/api-reference/ticketing/ticket-management/skill_based_routing/#json-format)
  * [List Account Attributes](/api-reference/ticketing/ticket-management/skill_based_routing/#list-account-attributes)
  * [List Routing Attribute Definitions](/api-reference/ticketing/ticket-management/skill_based_routing/#list-routing-attribute-definitions)
  * [Show Attribute](/api-reference/ticketing/ticket-management/skill_based_routing/#show-attribute)
  * [Create Attribute](/api-reference/ticketing/ticket-management/skill_based_routing/#create-attribute)
  * [Update Attribute](/api-reference/ticketing/ticket-management/skill_based_routing/#update-attribute)
  * [Delete Attribute](/api-reference/ticketing/ticket-management/skill_based_routing/#delete-attribute)
  * [List Attribute Values for an Attribute](/api-reference/ticketing/ticket-management/skill_based_routing/#list-attribute-values-for-an-attribute)
  * [Show Attribute Value](/api-reference/ticketing/ticket-management/skill_based_routing/#show-attribute-value)
  * [Create Attribute Value](/api-reference/ticketing/ticket-management/skill_based_routing/#create-attribute-value)
  * [Update Attribute Value](/api-reference/ticketing/ticket-management/skill_based_routing/#update-attribute-value)
  * [Delete Attribute Value](/api-reference/ticketing/ticket-management/skill_based_routing/#delete-attribute-value)
  * [List Agent Attribute Values](/api-reference/ticketing/ticket-management/skill_based_routing/#list-agent-attribute-values)
  * [List Attribute Values for Many Agents](/api-reference/ticketing/ticket-management/skill_based_routing/#list-attribute-values-for-many-agents)
  * [Set Agent Attribute Values](/api-reference/ticketing/ticket-management/skill_based_routing/#set-agent-attribute-values)
  * [Bulk Set Agent Attribute Values Jobs](/api-reference/ticketing/ticket-management/skill_based_routing/#bulk-set-agent-attribute-values-jobs)
  * [List Ticket Attribute Values](/api-reference/ticketing/ticket-management/skill_based_routing/#list-ticket-attribute-values)
  * [Set Ticket Attribute Values](/api-reference/ticketing/ticket-management/skill_based_routing/#set-ticket-attribute-values)
  * [List Tickets Fulfilled by a User](/api-reference/ticketing/ticket-management/skill_based_routing/#list-tickets-fulfilled-by-a-user)


You can use the skill-based routing API to list skill types and skills, as well as list and set skills for tickets and agents. To learn more about the feature, see [Using skills-based routing](https://support.zendesk.com/hc/en-us/articles/360000789788) in the Support Help Center.

In this API, skill types are named _attributes_ and skills are named _attribute values_.

Skill-based routing is only available on the Enterprise plan and above.

#### Attribute

An _attribute_ in this API refers to a skill type. Skill types are categories of skills.

Name| Type| Comment
---|---|---
id| string| Automatically assigned when an attribute is created
name| string| The name of the attribute

#### Attribute Values

An _attribute value_ in this API refers to a skill. Skills are associated with an agent and determine the agent's suitability to solve a ticket.

Name| Type| Comment
---|---|---
id| string| Automatically assigned when an attribute value is created
name| string| The name of the attribute value
attribute_id| string| Id of the associated attribute

### JSON format

Skill Based Routing are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
created_at| string| true| false| When this record was created
id| string| true| false| Automatically assigned when an attribute is created
name| string| false| true| The name of the attribute
updated_at| string| true| false| When this record was last updated
url| string| true| false| URL of the attribute

#### Example


    {  "created_at": "2017-12-01T19:29:31Z",  "id": "15821cba-7326-11e8-b07e-950ba849aa27",  "name": "color",  "updated_at": "2017-12-01T19:29:31Z",  "url": "https://{subdomain}.zendesk.com/api/v2/routing/attributes/15821cba-7326-11e8-b07e-950ba849aa27"}

### List Account Attributes

  * `GET /api/v2/routing/attributes`


Returns a list of attributes for the account.

#### Sideloads

The following sideloads are supported:

Name| Will sideload
---|---
attribute_values| The attribute values available on the account

#### Allowed For

  * Agents and admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
include| string| Query| false| Sideloads to include in the response. Accepts a comma-separated list of values. See [Sideloading](/api-reference/ticketing/ticket-management/skill_based_routing/#sideloads).

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/routing/attributes \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/routing/attributes?include=attribute_values"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/routing/attributes")		.newBuilder()		.addQueryParameter("include", "attribute_values");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/routing/attributes',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'include': 'attribute_values',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/routing/attributes?include=attribute_values"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/routing/attributes")uri.query = URI.encode_www_form("include": "attribute_values")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "attributes": [    {      "created_at": "2017-12-01T19:29:31Z",      "id": "15821cba-7326-11e8-b07e-950ba849aa27",      "name": "Color",      "updated_at": "2017-12-01T19:29:31Z"    }  ],  "count": 1,  "next_page": null,  "previous_page": null}

### List Routing Attribute Definitions

  * `GET /api/v2/routing/attributes/definitions`


Returns the condition definitions that can be configured to apply attributes to a ticket.

#### Allowed For

  * Admins


#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/routing/attributes/definitions \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/routing/attributes/definitions"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/routing/attributes/definitions")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/routing/attributes/definitions',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/routing/attributes/definitions"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/routing/attributes/definitions")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "definitions": {    "conditions_all": [      {        "subject": "number_of_incidents",        "title": "Number of incidents"      }    ],    "conditions_any": [      {        "subject": "brand",        "title": "Brand"      }    ]  }}

### Show Attribute

  * `GET /api/v2/routing/attributes/{attribute_id}`


Returns an attribute.

#### Allowed For

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
attribute_id| string| Path| true| The ID of the skill-based routing attribute

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/routing/attributes/{attribute_id} \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/routing/attributes/6e279587-e930-11e8-a292-09cfcdea1b75"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/routing/attributes/6e279587-e930-11e8-a292-09cfcdea1b75")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/routing/attributes/6e279587-e930-11e8-a292-09cfcdea1b75',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/routing/attributes/6e279587-e930-11e8-a292-09cfcdea1b75"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/routing/attributes/6e279587-e930-11e8-a292-09cfcdea1b75")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "attribute": {    "created_at": "2018-11-15T23:44:45Z",    "id": "6e279587-e930-11e8-a292-09cfcdea1b75",    "name": "Language",    "updated_at": "2018-11-15T23:44:45Z",    "url": "https://{subdomain}.zendesk.com/api/v2/routing/attributes/6e279587-e930-11e8-a292-09cfcdea1b75"  }}

### Create Attribute

  * `POST /api/v2/routing/attributes`


Creates an attribute.

#### Allowed For

  * Agents


#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/routing/attributes \  -H "Content-Type: application/json" \  -d '{"attribute": { "name": "Language" }}' \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/routing/attributes"	method := "POST"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/routing/attributes")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'POST',  url: 'https://example.zendesk.com/api/v2/routing/attributes',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/routing/attributes"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/routing/attributes")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**201 Created**


    // Status 201 Created
    {  "attribute": {    "created_at": "2018-11-15T23:44:45Z",    "id": "6e279587-e930-11e8-a292-09cfcdea1b75",    "name": "Language",    "updated_at": "2018-11-15T23:44:45Z",    "url": "https://{subdomain}.zendesk.com/api/v2/routing/attributes/6e279587-e930-11e8-a292-09cfcdea1b75"  }}

### Update Attribute

  * `PUT /api/v2/routing/attributes/{attribute_id}`


Updates an attribute.

#### Allowed For

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
attribute_id| string| Path| true| The ID of the skill-based routing attribute

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/routing/attributes/{attribute_id} \  -d '{ "name": "Lingua" }' \  -X PATCH -H "Content-Type: application/json" \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/routing/attributes/6e279587-e930-11e8-a292-09cfcdea1b75"	method := "PUT"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/routing/attributes/6e279587-e930-11e8-a292-09cfcdea1b75")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'PUT',  url: 'https://example.zendesk.com/api/v2/routing/attributes/6e279587-e930-11e8-a292-09cfcdea1b75',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/routing/attributes/6e279587-e930-11e8-a292-09cfcdea1b75"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/routing/attributes/6e279587-e930-11e8-a292-09cfcdea1b75")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "attribute": {    "created_at": "2018-11-15T23:44:45Z",    "id": "6e279587-e930-11e8-a292-09cfcdea1b75",    "name": "Lingua",    "updated_at": "2018-11-15T23:44:45Z",    "url": "https://{subdomain}.zendesk.com/api/v2/routing/attributes/6e279587-e930-11e8-a292-09cfcdea1b75"  }}

### Delete Attribute

  * `DELETE /api/v2/routing/attributes/{attribute_id}`


Deletes an attribute.

#### Allowed For

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
attribute_id| string| Path| true| The ID of the skill-based routing attribute

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/routing/attributes/{attribute_id} \  -X DELETE -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/routing/attributes/6e279587-e930-11e8-a292-09cfcdea1b75"	method := "DELETE"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/routing/attributes/6e279587-e930-11e8-a292-09cfcdea1b75")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("DELETE", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'DELETE',  url: 'https://example.zendesk.com/api/v2/routing/attributes/6e279587-e930-11e8-a292-09cfcdea1b75',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/routing/attributes/6e279587-e930-11e8-a292-09cfcdea1b75"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"DELETE",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/routing/attributes/6e279587-e930-11e8-a292-09cfcdea1b75")request = Net::HTTP::Delete.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**204 No Content**


    // Status 204 No Content
    null

### List Attribute Values for an Attribute

  * `GET /api/v2/routing/attributes/{attribute_id}/values`


Returns a list of attribute values for a provided attribute.

#### Allowed For

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
attribute_id| string| Path| true| The ID of the skill-based routing attribute

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/routing/attributes/{attribute_id}/values \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/routing/attributes/6e279587-e930-11e8-a292-09cfcdea1b75/values"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/routing/attributes/6e279587-e930-11e8-a292-09cfcdea1b75/values")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/routing/attributes/6e279587-e930-11e8-a292-09cfcdea1b75/values',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/routing/attributes/6e279587-e930-11e8-a292-09cfcdea1b75/values"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/routing/attributes/6e279587-e930-11e8-a292-09cfcdea1b75/values")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "attribute_values": [    {      "created_at": "2018-11-08T19:22:58Z",      "id": "b376b35a-e38b-11e8-a292-e3b6377c5575",      "name": "French",      "updated_at": "2018-11-08T19:22:58Z",      "url": "https://{subdomain}.zendesk.com/api/v2/routing/attributes/afa31619-e38b-11e8-a292-5d17513d969b/values/b376b35a-e38b-11e8-a292-e3b6377c5575"    }  ]}

### Show Attribute Value

  * `GET /api/v2/routing/attributes/{attribute_id}/values/{attribute_value_id}`


Returns an attribute value.

#### Allowed For

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
attribute_id| string| Path| true| The ID of the skill-based routing attribute
attribute_value_id| string| Path| true| The ID of the skill-based routing attribute value

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/routing/attributes/{attribute_id}/values/{attribute_value_id} \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/routing/attributes/6e279587-e930-11e8-a292-09cfcdea1b75/values/b376b35a-e38b-11e8-a292-e3b6377c5575"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/routing/attributes/6e279587-e930-11e8-a292-09cfcdea1b75/values/b376b35a-e38b-11e8-a292-e3b6377c5575")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/routing/attributes/6e279587-e930-11e8-a292-09cfcdea1b75/values/b376b35a-e38b-11e8-a292-e3b6377c5575',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/routing/attributes/6e279587-e930-11e8-a292-09cfcdea1b75/values/b376b35a-e38b-11e8-a292-e3b6377c5575"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/routing/attributes/6e279587-e930-11e8-a292-09cfcdea1b75/values/b376b35a-e38b-11e8-a292-e3b6377c5575")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "attribute_value": {    "created_at": "2018-11-08T19:22:58Z",    "id": "b376b35a-e38b-11e8-a292-e3b6377c5575",    "name": "French",    "updated_at": "2018-11-08T19:22:58Z",    "url": "https://{subdomain}.zendesk.com/api/v2/routing/attributes/afa31619-e38b-11e8-a292-5d17513d969b/values/b376b35a-e38b-11e8-a292-e3b6377c5575"  }}

### Create Attribute Value

  * `POST /api/v2/routing/attributes/{attribute_id}/values`


Creates an attribute value.

#### Allowed For

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
attribute_id| string| Path| true| The ID of the skill-based routing attribute

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/routing/attributes/{attribute_id}/values \  -H "Content-Type: application/json" \  -d '{"attribute_value": { "name": "Japanese" }}' \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/routing/attributes/6e279587-e930-11e8-a292-09cfcdea1b75/values"	method := "POST"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/routing/attributes/6e279587-e930-11e8-a292-09cfcdea1b75/values")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'POST',  url: 'https://example.zendesk.com/api/v2/routing/attributes/6e279587-e930-11e8-a292-09cfcdea1b75/values',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/routing/attributes/6e279587-e930-11e8-a292-09cfcdea1b75/values"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/routing/attributes/6e279587-e930-11e8-a292-09cfcdea1b75/values")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**201 Created**


    // Status 201 Created
    {  "attribute_value": {    "created_at": "2018-11-08T19:22:58Z",    "id": "6ccddacf-e85e-11e8-a292-ad7686bdff67",    "name": "Japanese",    "updated_at": "2018-11-08T19:22:58Z",    "url": "https://{subdomain}.zendesk.com/api/v2/routing/attributes/afa31619-e38b-11e8-a292-5d17513d969b/values/6ccddacf-e85e-11e8-a292-ad7686bdff67"  }}

### Update Attribute Value

  * `PATCH /api/v2/routing/attributes/{attribute_id}/values/{attribute_value_id}`


Updates the name and ticket conditions of a skill. When a ticket is created, the skill is applied to a ticket if the ticket meets the specified condition or conditions. See the [Conditions reference](/documentation/ticketing/reference-guides/conditions-reference/) for more information.

#### Allowed For

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
attribute_id| string| Path| true| The ID of the skill-based routing attribute
attribute_value_id| string| Path| true| The ID of the skill-based routing attribute value

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/routing/attributes/{attribute_id}/values/{attribute_value_id} \  -X PATCH -H "Content-Type: application/json" \  -d '{ "attribute_value": { "name": "German", "conditions": {"all":[ { "subject": "locale_id", "operator": "is", "value": "8"}], "any":[]}}}' \  -v -u {email_address}/token:{password}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/routing/attributes/6e279587-e930-11e8-a292-09cfcdea1b75/values/b376b35a-e38b-11e8-a292-e3b6377c5575"	method := "PATCH"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/routing/attributes/6e279587-e930-11e8-a292-09cfcdea1b75/values/b376b35a-e38b-11e8-a292-e3b6377c5575")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PATCH", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'PATCH',  url: 'https://example.zendesk.com/api/v2/routing/attributes/6e279587-e930-11e8-a292-09cfcdea1b75/values/b376b35a-e38b-11e8-a292-e3b6377c5575',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/routing/attributes/6e279587-e930-11e8-a292-09cfcdea1b75/values/b376b35a-e38b-11e8-a292-e3b6377c5575"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PATCH",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/routing/attributes/6e279587-e930-11e8-a292-09cfcdea1b75/values/b376b35a-e38b-11e8-a292-e3b6377c5575")request = Net::HTTP::Patch.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "attribute_value": {    "created_at": "2018-11-14T22:41:28Z",    "id": "b376b35a-e38b-11e8-a292-e3b6377c5575",    "name": "German (Advanced)",    "updated_at": "2018-11-14T22:45:01Z",    "url": "https://{subdomain}.zendesk.com/api/v2/routing/attributes/afa31619-e38b-11e8-a292-5d17513d969b/values/b376b35a-e38b-11e8-a292-e3b6377c5575"  }}

### Delete Attribute Value

  * `DELETE /api/v2/routing/attributes/{attribute_id}/values/{attribute_value_id}`


Deletes an attribute value.

#### Allowed For

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
attribute_id| string| Path| true| The ID of the skill-based routing attribute
attribute_value_id| string| Path| true| The ID of the skill-based routing attribute value

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/routing/attributes/{attribute_id}/values/{attribute_value_id} \  -X DELETE -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/routing/attributes/6e279587-e930-11e8-a292-09cfcdea1b75/values/b376b35a-e38b-11e8-a292-e3b6377c5575"	method := "DELETE"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/routing/attributes/6e279587-e930-11e8-a292-09cfcdea1b75/values/b376b35a-e38b-11e8-a292-e3b6377c5575")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("DELETE", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'DELETE',  url: 'https://example.zendesk.com/api/v2/routing/attributes/6e279587-e930-11e8-a292-09cfcdea1b75/values/b376b35a-e38b-11e8-a292-e3b6377c5575',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/routing/attributes/6e279587-e930-11e8-a292-09cfcdea1b75/values/b376b35a-e38b-11e8-a292-e3b6377c5575"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"DELETE",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/routing/attributes/6e279587-e930-11e8-a292-09cfcdea1b75/values/b376b35a-e38b-11e8-a292-e3b6377c5575")request = Net::HTTP::Delete.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**204 No Content**


    // Status 204 No Content
    null

### List Agent Attribute Values

  * `GET /api/v2/routing/agents/{user_id}/instance_values`


Returns an attribute value.

#### Allowed For

  * Agents and admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
user_id| integer| Path| true| The id of the user

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/routing/agents/{user_id}/instance_values \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/routing/agents/35436/instance_values"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/routing/agents/35436/instance_values")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/routing/agents/35436/instance_values',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/routing/agents/35436/instance_values"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/routing/agents/35436/instance_values")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "attribute_values": [    {      "agent_skill_priority": "NORMAL",      "created_at": "2018-11-08T19:22:58Z",      "id": "b376b35a-e38b-11e8-a292-e3b6377c5575",      "name": "French",      "updated_at": "2018-11-08T19:22:58Z",      "url": "https://{subdomain}.zendesk.com/api/v2/routing/attributes/afa31619-e38b-11e8-a292-5d17513d969b/values/b376b35a-e38b-11e8-a292-e3b6377c5575"    }  ]}

### List Attribute Values for Many Agents

  * `GET /api/v2/routing/agents/instance_values?filter[agent_ids]={filter[agent_ids]}`


Accepts a comma-separated list of up to 100 agent ids and returns attribute values for each agent in the list.

#### Allowed For

  * Admins
  * [Agents in custom role with permission to manage skills](https://support.zendesk.com/hc/en-us/articles/4408882153882-Creating-custom-roles-and-assigning-agents)


#### Pagination

  * [Cursor pagination](/api-reference/introduction/pagination/#cursor-pagination) only.


Note: `page[before]` and `page[after]` can't be used together in the same request.

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
filter[agent_ids]| string| Query| true| A comma-separated list of agent ids
page[after]| string| Query| false| A [pagination cursor](/documentation/api-basics/pagination/paginating-through-lists-using-cursor-pagination) that tells the endpoint which page to start on. It should be a `meta.after_cursor` value from a previous request.
page[before]| string| Query| false| A [pagination cursor](/documentation/api-basics/pagination/paginating-through-lists-using-cursor-pagination) that tells the endpoint which page to start on. It should be a `meta.before_cursor` value from a previous request.
page[size]| integer| Query| false| The number of items to return per page

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/routing/agents/instance_values?filter[agent_ids]=224,225 \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/routing/agents/instance_values?filter[agent_ids]=224%2C225&page[after]=&page[before]=&page[size]="	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/routing/agents/instance_values")		.newBuilder()		.addQueryParameter("filter[agent_ids]", "224,225")		.addQueryParameter("page[after]", "")		.addQueryParameter("page[before]", "")		.addQueryParameter("page[size]", "");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/routing/agents/instance_values',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'filter[agent_ids]': '224%2C225',    'page[after]': '',    'page[before]': '',    'page[size]': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/routing/agents/instance_values?filter[agent_ids]=224%2C225&page[after]=&page[before]=&page[size]="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/routing/agents/instance_values")uri.query = URI.encode_www_form("filter[agent_ids]": "224,225", "page[after]": "", "page[before]": "", "page[size]": "")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "count": 2,  "instance_values": [    {      "agent_id": 224,      "agent_skill_priority": "NORMAL",      "attribute_id": "2e39fa8e-d88b-11ef-9229-e3c997c52841",      "attribute_value_id": "89137a1a-13e5-415a-8417-beb03e7c043e",      "created_at": "2025-01-23T02:24:00Z",      "id": "f969d6c9-f3ba-4928-9046-2c006928c1b7",      "name": "french",      "updated_at": "2025-01-23T02:24:00Z"    },    {      "agent_id": 225,      "agent_skill_priority": "HIGH",      "attribute_id": "384b95cd-e59b-4dc0-9d94-a6a76d98fb3f",      "attribute_value_id": "32ae7078-b763-441d-bc2e-5a632a0283ec",      "created_at": "2025-01-23T02:24:00Z",      "id": "19ebcf64-306f-4982-b4a9-325c6d2fecfe",      "name": "french",      "updated_at": "2025-01-23T02:24:00Z"    }  ],  "next_page": null,  "previous_page": null}

**400 Bad Request**


    // Status 400 Bad Request
    {  "error": {    "message": "You passed an invalid value for the filter attribute. Invalid parameter: filter must be present from api/v2/routing/instance_values/show_many_agent_instance_values",    "title": "Invalid attribute"  }}

### Set Agent Attribute Values

  * `POST /api/v2/routing/agents/{user_id}/instance_values`


Adds the specified attributes if no attributes exists, or replaces all existing attributes with the specified attributes.

#### Allowed For

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
user_id| integer| Path| true| The id of the user

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/routing/agents/{user_id}/instance_values \  -d "{\"attribute_value_ids\":[\"{attribute_value_id}\"]}" \  -H "Content-Type: application/json" \  -v -u {email_address}/token:{api_token} -X POST

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/routing/agents/35436/instance_values"	method := "POST"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/routing/agents/35436/instance_values")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'POST',  url: 'https://example.zendesk.com/api/v2/routing/agents/35436/instance_values',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/routing/agents/35436/instance_values"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/routing/agents/35436/instance_values")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "attribute_values": [    {      "created_at": "2018-11-08T19:22:58Z",      "id": "b376b35a-e38b-11e8-a292-e3b6377c5575",      "name": "French",      "updated_at": "2018-11-08T19:22:58Z",      "url": "https://{subdomain}.zendesk.com/api/v2/routing/attributes/afa31619-e38b-11e8-a292-5d17513d969b/values/b376b35a-e38b-11e8-a292-e3b6377c5575"    }  ]}

### Bulk Set Agent Attribute Values Jobs

  * `POST /api/v2/routing/agents/instance_values/jobs`


Adds, replaces or removes multiple attributes for up to 100 agents.

#### Allowed For

  * Admins
  * [Agents in custom role with permission to manage skills](https://support.zendesk.com/hc/en-us/articles/4408882153882-Creating-custom-roles-and-assigning-agents)


#### Available Parameters

The request takes a data object with the following properties:

Name| Type| Required| Description
---|---|---|---
action| string| true| The action to perform on the attribute values. One of the following: "upsert", "update", "delete"
attributes| object| true| The attribute values to update. See Attribute Values. `agent_skill_priority` is optional. If not provided, it keeps the current priority or defaults to `NORMAL` when adding new attribute values.
items| array| true| The list of agent ids

Action can be one of the following:

  * upsert: Adds new attribute values to the agents
  * update: Replaces all the current attribute values of the agents with the new values
  * delete: Removes specified attribute values from the agents


This endpoint returns a `job_status` [JSON object](/api-reference/ticketing/ticket-management/job_statuses/#json-format) and queues a background job to do the work. Use the [Show Job Status](/api-reference/ticketing/ticket-management/job_statuses/#show-job-status) endpoint to check for the job's completion.

#### Example body


    {  "job": {    "action": "upsert",    "attributes": {      "attribute_values": [        {          "agent_skill_priority": "NORMAL",          "id": "b376b35a-e38b-11e8-a292-e3b6377c5575"        }      ]    },    "items": [      224,      225    ]  }}

#### Code Samples

**cURL**


    curl https://{subdomain}.zendesk.com/api/v2/routing/agents/instance_values/jobs \  -d '{"job":{"action":"upsert","attributes":{"attribute_values":[{"id":"b376b35a-e38b-11e8-a292-e3b6377c5575"}]},"items":[224,225]}}' \  -H "Content-Type: application/json" -X POST \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://example.zendesk.com/api/v2/routing/agents/instance_values/jobs"	method := "POST"	payload := strings.NewReader(`{  "job": {    "action": "upsert",    "attributes": {      "attribute_values": [        {          "agent_skill_priority": "NORMAL",          "id": "b376b35a-e38b-11e8-a292-e3b6377c5575"        }      ]    },    "items": [      224,      225    ]  }}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/routing/agents/instance_values/jobs")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"job\": {    \"action\": \"upsert\",    \"attributes\": {      \"attribute_values\": [        {          \"agent_skill_priority\": \"NORMAL\",          \"id\": \"b376b35a-e38b-11e8-a292-e3b6377c5575\"        }      ]    },    \"items\": [      224,      225    ]  }}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "job": {    "action": "upsert",    "attributes": {      "attribute_values": [        {          "agent_skill_priority": "NORMAL",          "id": "b376b35a-e38b-11e8-a292-e3b6377c5575"        }      ]    },    "items": [      224,      225    ]  }});
    var config = {  method: 'POST',  url: 'https://example.zendesk.com/api/v2/routing/agents/instance_values/jobs',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/routing/agents/instance_values/jobs"
    payload = json.loads("""{  "job": {    "action": "upsert",    "attributes": {      "attribute_values": [        {          "agent_skill_priority": "NORMAL",          "id": "b376b35a-e38b-11e8-a292-e3b6377c5575"        }      ]    },    "items": [      224,      225    ]  }}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/routing/agents/instance_values/jobs")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")request.body = %q({  "job": {    "action": "upsert",    "attributes": {      "attribute_values": [        {          "agent_skill_priority": "NORMAL",          "id": "b376b35a-e38b-11e8-a292-e3b6377c5575"        }      ]    },    "items": [      224,      225    ]  }})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "job_status": {    "id": "V3-25da3dc252ff0f7b63f65d9a8c3ead61",    "job_type": "Bulk upsert/update/delete agent instance values",    "message": null,    "progress": null,    "results": null,    "status": "queued",    "total": 2,    "url": "https://example.zendesk.com/api/v2/job_statuses/82de0b0467893ac9fe64f1a99"  }}

**400 Bad Request**


    // Status 400 Bad Request
    {  "error": {    "message": "You passed an invalid value for the job.items attribute. Invalid parameter: job.items must be an integer from api/v2/routing/instance_values/update_many_agent_instance_values",    "title": "Invalid attribute"  }}

### List Ticket Attribute Values

  * `GET /api/v2/routing/tickets/{ticket_id}/instance_values`


Returns a list of attributes values for the ticket.

#### Allowed For

  * Agents and admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
ticket_id| integer| Path| true| The ID of the ticket

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/routing/tickets/{ticket_id}/instance_values \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/routing/tickets/123456/instance_values"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/routing/tickets/123456/instance_values")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/routing/tickets/123456/instance_values',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/routing/tickets/123456/instance_values"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/routing/tickets/123456/instance_values")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "attribute_values": [    {      "attribute_id": "f4a604b1-d6cd-11e7-a492-657e7928664c",      "created_at": "2017-12-01T19:29:41Z",      "id": "fa1131e2-d6cd-11e7-a492-dbdd5500c7e3",      "name": "ocean",      "updated_at": "2017-12-01T19:35:45Z"    }  ]}

### Set Ticket Attribute Values

  * `POST /api/v2/routing/tickets/{ticket_id}/instance_values`


Adds the specified attributes if no attributes exists, or replaces all existing attributes with the specified attributes.

Invalid or deleted attributes are ignored.

#### Allowed For

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
ticket_id| integer| Path| true| The ID of the ticket

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/routing/tickets/{ticket_id}/instance_values \  -d "{\"attribute_value_ids\":[\"{attribute_value_id}\"]}" \  -H "Content-Type: application/json" \  -v -u {email_address}/token:{api_token} -X POST

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/routing/tickets/123456/instance_values"	method := "POST"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/routing/tickets/123456/instance_values")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'POST',  url: 'https://example.zendesk.com/api/v2/routing/tickets/123456/instance_values',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/routing/tickets/123456/instance_values"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/routing/tickets/123456/instance_values")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "attribute_values": [    {      "attribute_id": "f4a604b1-d6cd-11e7-a492-657e7928664c",      "created_at": "2017-12-01T19:29:41Z",      "id": "fa1131e2-d6cd-11e7-a492-dbdd5500c7e3",      "name": "ocean",      "updated_at": "2017-12-01T19:35:45Z"    }  ]}

### List Tickets Fulfilled by a User

  * `GET /api/v2/routing/requirements/fulfilled?ticket_ids={ticket_ids}`


Returns a list of ticket ids that contain attributes matching the current user's attributes. Accepts a `ticket_ids` parameter for relevant tickets to check for matching attributes.

#### Allowed For

  * Agents and admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
ticket_ids| integer| Query| true| The IDs of the relevant tickets to check for matching attributes

#### Code Samples

**curl**


    curl 'https://{subdomain}.zendesk.com/api/v2/routing/requirements/fulfilled?ticket_ids\[\]=17&ticket_ids\[\]=1&ticket_ids\[\]=99' \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/routing/requirements/fulfilled?ticket_ids=1"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/routing/requirements/fulfilled")		.newBuilder()		.addQueryParameter("ticket_ids", "1");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/routing/requirements/fulfilled',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'ticket_ids': '1',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/routing/requirements/fulfilled?ticket_ids=1"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/routing/requirements/fulfilled")uri.query = URI.encode_www_form("ticket_ids": "1")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "fulfilled_ticket_ids": [    1,    17  ]}

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)