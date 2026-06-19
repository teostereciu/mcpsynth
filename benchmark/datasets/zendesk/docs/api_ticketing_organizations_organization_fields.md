# Organization Fields

*Source: https://developer.zendesk.com/api-reference/ticketing/organizations/organization_fields/*

---

## On this page

  * [JSON format](/api-reference/ticketing/organizations/organization_fields/#json-format)
  * [List Organization Fields](/api-reference/ticketing/organizations/organization_fields/#list-organization-fields)
  * [Show Organization Field](/api-reference/ticketing/organizations/organization_fields/#show-organization-field)
  * [Create Organization Field](/api-reference/ticketing/organizations/organization_fields/#create-organization-field)
  * [Update Organization Field](/api-reference/ticketing/organizations/organization_fields/#update-organization-field)
  * [Delete Organization Field](/api-reference/ticketing/organizations/organization_fields/#delete-organization-field)
  * [Reorder Organization Field](/api-reference/ticketing/organizations/organization_fields/#reorder-organization-field)


# Organization Fields

## On this page

  * [JSON format](/api-reference/ticketing/organizations/organization_fields/#json-format)
  * [List Organization Fields](/api-reference/ticketing/organizations/organization_fields/#list-organization-fields)
  * [Show Organization Field](/api-reference/ticketing/organizations/organization_fields/#show-organization-field)
  * [Create Organization Field](/api-reference/ticketing/organizations/organization_fields/#create-organization-field)
  * [Update Organization Field](/api-reference/ticketing/organizations/organization_fields/#update-organization-field)
  * [Delete Organization Field](/api-reference/ticketing/organizations/organization_fields/#delete-organization-field)
  * [Reorder Organization Field](/api-reference/ticketing/organizations/organization_fields/#reorder-organization-field)


You can use this API to add fields to the Organization page in the Zendesk user interface. Basic text fields, date fields, as well as customizable drop-down and number fields are available. The fields correspond to the organization fields that admins can add using the Zendesk admin interface. See [Adding custom fields to organizations](https://support.zendesk.com/hc/en-us/articles/203662076) in Zendesk help.

The fields are only visible to agents and admins.

**About dropdown and multiselect fields**

Most custom fields let agents enter a single value such as free-form text or a date. The dropdown field lets agents choose a single value from a list of options. The multiselect field lets agents choose one or more values from a list of options. Each option has a name that's visible to the agent and an underlying value that's not visible. In the API, these options are listed in the dropdown and multiselect field's `custom_field_options` property. Each option in the list has a `name` and `value` property.

In the Zendesk admin interface, the "Value" field corresponds to the `name` property and the "Tag" field corresponds to the `value` property.

Occasionally, a `value` can be duplicated through API requests. When this happens, the field becomes uneditable until the duplicated value is removed.

### JSON format

Organization Fields are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
active| boolean| false| false| If true, this field is available for use
created_at| string| true| false| The time the field was created
custom_field_options| array| false| false| Required and presented for a custom field of type "dropdown". Each option is represented by an object with a `name` and `value` property
description| string| false| false| User-defined description of this field's purpose
id| integer| true| false| Automatically assigned upon creation
key| string| false| true| A unique key that identifies this custom field. This is used for updating the field and referencing in placeholders. The key must consist of only letters, numbers, and underscores. It can't be only numbers
position| integer| false| false| Ordering of the field relative to other fields
raw_description| string| false| false| The dynamic content placeholder, if present, or the `description` value, if not. See [Dynamic Content Items](/api-reference/ticketing/ticket-management/dynamic_content/)
raw_title| string| false| false| The dynamic content placeholder, if present, or the `title` value, if not. See [Dynamic Content Items](/api-reference/ticketing/ticket-management/dynamic_content/)
regexp_for_validation| string| false| false| Regular expression field only. The validation pattern for a field value to be deemed valid
relationship_filter| object| false| false| A filter definition that allows your autocomplete to filter down results
relationship_target_type| string| false| false| A representation of what type of object the field references. Options are "zen:user", "zen:organization", "zen:ticket", and "zen:custom_object:{key}" where key is a custom object key. For example "zen:custom_object:apartment".
system| boolean| true| false| If true, only active and position values of this field can be changed
tag| string| false| false| Optional for custom field of type "checkbox"; not presented otherwise.
title| string| false| true| The title of the custom field
type| string| false| true| The custom field type: "checkbox", "date", "decimal", "dropdown", "integer", ["lookup"](/api-reference/ticketing/lookup_relationships/lookup_relationships/), "multiselect", "regexp", "text", or "textarea"
updated_at| string| true| false| The time of the last update of the field
url| string| true| false| The URL for this resource

#### Example


    {  "active": true,  "created_at": "2012-10-16T16:04:06Z",  "description": "Description of Custom Field",  "id": 7,  "key": "custom_field_1",  "position": 9999,  "raw_description": "{{dc.my_description}}",  "raw_title": "Custom Field 1",  "regexp_for_validation": null,  "title": "Custom Field 1",  "type": "text",  "updated_at": "2012-10-16T16:04:06Z",  "url": "https://company.zendesk.com/api/v2/organization_fields/7"}

### List Organization Fields

  * `GET /api/v2/organization_fields`


Returns a list of custom organization fields in your account. Fields are returned in the order that you specify in your organization fields configuration in Zendesk Support. Clients should cache this resource for the duration of their API usage and map the key for each organization field to the values returned under the `organization_fields` attribute on the [organization](/api-reference/ticketing/organizations/organizations/) resource.

#### Pagination

  * Cursor pagination (recommended)
  * Offset pagination


See [Pagination](/api-reference/introduction/pagination/).

Returns a maximum of 100 records per page.

#### Allowed For

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
page| object| Query| false| Cursor-based pagination parameters (JSON:API style). Supports nested parameters: - `page[size]` \- Number of records per page (default varies by endpoint, typically 100) - `page[after]` \- Cursor token to fetch records after this position - `page[before]` \- Cursor token to fetch records before this position Example: `?page[size]=50&page[after]=eyJvIjoiaWQiLCJ2IjoiYVFFPSJ9`
resolve_dc| boolean| Query| false| If true, resolves dynamic content placeholders.

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/organization_fields \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/organization_fields?page=&resolve_dc="	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/organization_fields")		.newBuilder()		.addQueryParameter("page", "")		.addQueryParameter("resolve_dc", "");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/organization_fields',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'page': '',    'resolve_dc': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/organization_fields?page=&resolve_dc="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/organization_fields")uri.query = URI.encode_www_form("page": "", "resolve_dc": "")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "count": 1,  "next_page": null,  "organization_fields": [    {      "active": true,      "created_at": "2012-10-16T16:04:06Z",      "description": "Description of Custom Field",      "id": 7,      "key": "custom_field_1",      "position": 9999,      "raw_description": "{{dc.my_description}}",      "raw_title": "Custom Field 1",      "regexp_for_validation": null,      "title": "Custom Field 1",      "type": "text",      "updated_at": "2012-10-16T16:04:06Z",      "url": "https://company.zendesk.com/api/v2/organization_fields/7"    }  ],  "previous_page": null}

### Show Organization Field

  * `GET /api/v2/organization_fields/{organization_field_id}`


#### Allowed for

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
organization_field_id| | Path| true| The ID or key of the organization field

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/organization_fields/{organization_field_id} \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/organization_fields/my_text_field"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/organization_fields/my_text_field")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/organization_fields/my_text_field',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/organization_fields/my_text_field"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/organization_fields/my_text_field")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "organization_field": {    "active": true,    "created_at": "2012-10-16T16:04:06Z",    "description": "Description of Custom Field",    "id": 7,    "key": "custom_field_1",    "position": 9999,    "raw_description": "{{dc.my_description}}",    "raw_title": "Custom Field 1",    "regexp_for_validation": null,    "title": "Custom Field 1",    "type": "text",    "updated_at": "2012-10-16T16:04:06Z",    "url": "https://company.zendesk.com/api/v2/organization_fields/7"  }}

### Create Organization Field

  * `POST /api/v2/organization_fields`


Creates any of the following custom field types:

  * text (default when no "type" is specified)
  * textarea
  * checkbox
  * date
  * integer
  * decimal
  * regexp
  * dropdown
  * lookup
  * multiselect


See [About custom field types](https://support.zendesk.com/hc/en-us/articles/203661866) in Zendesk help.

#### Allowed For

  * Admins


#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/organization_fields \  -H "Content-Type: application/json" -X POST \  -d '{"organization_field": {"type": "text", "title": "Support description",      "description": "This field describes the support plan this organization has",      "position": 0, "active": true, "key": "support_description"}}' \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/organization_fields"	method := "POST"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/organization_fields")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'POST',  url: 'https://example.zendesk.com/api/v2/organization_fields',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/organization_fields"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/organization_fields")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**201 Created**


    // Status 201 Created
    {  "organization_field": {    "active": true,    "created_at": "2013-02-27T20:35:55Z",    "description": "This field describes the support plan this organization has",    "id": 75,    "key": "support_description",    "position": 0,    "raw_description": "This field describes the support plan this organization has",    "raw_title": "Support description",    "regexp_for_validation": null,    "title": "Support description",    "type": "text",    "updated_at": "2013-02-27T20:35:55Z",    "url": "https://company.zendesk.com/api/v2/organization_fields/75"  }}

### Update Organization Field

  * `PUT /api/v2/organization_fields/{organization_field_id}`


#### Updating a Dropdown (Tagger) or Multiselect Field

Dropdown and multiselect fields return an array of `custom_field_options` which specify the name, value, and order of dropdown or multiselect options. When updating a dropdown or multiselect field, note the following information:

  * All options must be passed on update. Options that are not passed will be removed. As a result, these values will be removed from any organizations
  * To create a new option, pass a null `id` along with the `name` and `value`
  * To update an existing option, pass its `id` along with the `name` and `value`
  * To reorder an option, reposition it in the `custom_field_options` array relative to the other options
  * To remove an option, omit it from the list of options upon update


#### Example Request


    curl https://{subdomain}.zendesk.com/api/v2/organization_fields/{organization_field_id} \  -H "Content-Type: application/json" -X PUT \  -d '{"organization_field": {"custom_field_options": [{"id": 124, "name": "Option 2", "value": "option_2"}, {"id": 123, "name": "Option 1", "value": "option_1"}, {"id": 125, "name": "Option 3", "value": "option_3"}]}}' \  -v -u {email_address}/token:{api_token}

#### Allowed for

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
organization_field_id| | Path| true| The ID or key of the organization field

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/organization_fields/{organization_field_id} \  -H "Content-Type: application/json" -X PUT \  -d '{ "organization_field": { "title": "Support description" }}' \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/organization_fields/my_text_field"	method := "PUT"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/organization_fields/my_text_field")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'PUT',  url: 'https://example.zendesk.com/api/v2/organization_fields/my_text_field',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/organization_fields/my_text_field"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/organization_fields/my_text_field")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "organization_field": {    "active": true,    "created_at": "2013-02-27T20:35:55Z",    "description": "This field describes the support plan this organization has",    "id": 75,    "key": "support_description",    "position": 0,    "raw_description": "This field describes the support plan this organization has",    "raw_title": "Support description",    "regexp_for_validation": null,    "title": "Support description",    "type": "text",    "updated_at": "2013-02-27T20:35:55Z",    "url": "https://company.zendesk.com/api/v2/organization_fields/75"  }}

### Delete Organization Field

  * `DELETE /api/v2/organization_fields/{organization_field_id}`


#### Allowed for

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
organization_field_id| | Path| true| The ID or key of the organization field

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/organization_fields/{organization_field_id} \  -v -u {email_address}/token:{api_token} -X DELETE

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/organization_fields/my_text_field"	method := "DELETE"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/organization_fields/my_text_field")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("DELETE", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'DELETE',  url: 'https://example.zendesk.com/api/v2/organization_fields/my_text_field',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/organization_fields/my_text_field"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"DELETE",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/organization_fields/my_text_field")request = Net::HTTP::Delete.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**204 No Content**


    // Status 204 No Content
    null

### Reorder Organization Field

  * `PUT /api/v2/organization_fields/reorder`


#### Allowed For

  * Admins


#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/organization_fields/reorder \  -v -u {email_address}/token:{api_token} -X PUT -d '{ "organization_field_ids": [3, 4] }' -H "Content-Type: application/json"

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/organization_fields/reorder"	method := "PUT"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/organization_fields/reorder")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'PUT',  url: 'https://example.zendesk.com/api/v2/organization_fields/reorder',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/organization_fields/reorder"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/organization_fields/reorder")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    null

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)