# OAuth Clients

*Source: https://developer.zendesk.com/api-reference/ticketing/oauth/oauth_clients/*

---

## On this page

  * [JSON format](/api-reference/ticketing/oauth/oauth_clients/#json-format)
  * [List Clients](/api-reference/ticketing/oauth/oauth_clients/#list-clients)
  * [Show Client](/api-reference/ticketing/oauth/oauth_clients/#show-client)
  * [Create Client](/api-reference/ticketing/oauth/oauth_clients/#create-client)
  * [Update Client](/api-reference/ticketing/oauth/oauth_clients/#update-client)
  * [Delete Client](/api-reference/ticketing/oauth/oauth_clients/#delete-client)
  * [Generate Secret](/api-reference/ticketing/oauth/oauth_clients/#generate-secret)


# OAuth Clients

## On this page

  * [JSON format](/api-reference/ticketing/oauth/oauth_clients/#json-format)
  * [List Clients](/api-reference/ticketing/oauth/oauth_clients/#list-clients)
  * [Show Client](/api-reference/ticketing/oauth/oauth_clients/#show-client)
  * [Create Client](/api-reference/ticketing/oauth/oauth_clients/#create-client)
  * [Update Client](/api-reference/ticketing/oauth/oauth_clients/#update-client)
  * [Delete Client](/api-reference/ticketing/oauth/oauth_clients/#delete-client)
  * [Generate Secret](/api-reference/ticketing/oauth/oauth_clients/#generate-secret)


### JSON format

OAuth Clients are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
company| string| false| false| The company name displayed when users are asked to grant access to your application.
created_at| string| true| false| The time the client was created
description| string| false| false| A short description of your client that is displayed to users when they are considering approving access to your application
global| boolean| true| false| Whether this client is globally accessible. See [Set up a global OAuth client](/documentation/apps/publish-your-app-or-theme/global_oauth_intro/)
id| integer| true| false| Automatically assigned upon creation
identifier| string| false| true| The unique identifier for this client
kind| string| false| false| Either "public" or "confidential". Specifies whether the OAuth client operates in a public environment where credentials cannot be securely stored, or on secure servers that can safely store credentials. See [Client types](/documentation/ticketing/working-with-oauth/oauth-pkce/#client-types)
logo_url| string| true| false| The API logo url of this record
name| string| false| true| The name of this client
redirect_uri| array| false| false| An array of the valid redirect URIs for this client
secret| string| true| false| The client secret. Generated automatically on creation and returned in full only at that time
updated_at| string| true| false| The time of the last update of the client
url| string| true| false| The API url of this record
user_id| integer| false| true| The id of the admin who created the client

#### Example


    {  "company": "Zendesk",  "created_at": "2009-05-13T00:07:08Z",  "description": "Zendesk Test Client",  "id": 1,  "identifier": "test_client",  "name": "My Test Client",  "redirect_uri": [    "https://example.com/callback"  ],  "secret": "af3t24tfj34h43s...",  "updated_at": "2011-07-22T00:11:12Z",  "url": "https://example.zendesk.com/api/v2/clients/1.json",  "user_id": 29}

### List Clients

  * `GET /api/v2/oauth/clients`
  * `GET /api/v2/users/me/oauth/clients.json`


#### Pagination

  * Cursor pagination (recommended)
  * Offset pagination


See [Pagination](/api-reference/introduction/pagination/).

Returns a maximum of 100 records per page.

#### Allowed For

  * Admins


#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/oauth/clients.json \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/oauth/clients"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/oauth/clients")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/oauth/clients',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/oauth/clients"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/oauth/clients")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "clients": [    {      "company": "Zendesk",      "created_at": "2009-05-13T00:07:08Z",      "description": "Zendesk Test Client",      "id": 223443,      "identifier": "test_client",      "name": "Stats Widget",      "redirect_uri": [        "https://example.com/callback"      ],      "secret": "af3t24tfj34h43s...",      "updated_at": "2011-07-22T00:11:12Z",      "url": "https://example.zendesk.com/api/v2/clients/223443.json",      "user_id": 29    },    {      "company": "Zendesk",      "created_at": "2009-05-13T00:07:08Z",      "description": "Zendesk Mobile Client",      "id": 8678530,      "identifier": "mobile_client",      "name": "Zendesk Mobile",      "redirect_uri": [        "https://example.com/callback"      ],      "secret": "af3t24tfj34h43s...",      "updated_at": "2011-07-22T00:11:12Z",      "url": "https://example.zendesk.com/api/v2/clients/8678530.json",      "user_id": 29    }  ]}

### Show Client

  * `GET /api/v2/oauth/clients/{oauth_client_id}`


#### Allowed for

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
oauth_client_id| integer| Path| true| The ID of the OAuth client

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/oauth/clients/{oauth_client_id}.json \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/oauth/clients/223443"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/oauth/clients/223443")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/oauth/clients/223443',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/oauth/clients/223443"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/oauth/clients/223443")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "client": {    "company": "Zendesk",    "created_at": "2009-05-13T00:07:08Z",    "description": "Zendesk Test Client",    "id": 223443,    "identifier": "test_client",    "name": "Test Client",    "redirect_uri": [      "https://example.com/callback"    ],    "secret": "af3t24tfj34h43s...",    "updated_at": "2011-07-22T00:11:12Z",    "url": "https://example.zendesk.com/api/v2/clients/223443.json",    "user_id": 29  }}

### Create Client

  * `POST /api/v2/oauth/clients`


#### Allowed For

  * Admins


#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/oauth/clients.json \  -X POST -H "Content-Type: application/json" \  -d '{"client": {"name": "Test Client", "identifier": "unique_id", "kind": "confidential"}}'  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/oauth/clients"	method := "POST"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/oauth/clients")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'POST',  url: 'https://support.zendesk.com/api/v2/oauth/clients',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/oauth/clients"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/oauth/clients")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**201 Created**


    // Status 201 Created
    {  "client": {    "company": "Zendesk",    "created_at": "2009-05-13T00:07:08Z",    "description": "Zendesk Test Client",    "id": 223443,    "identifier": "test_client",    "name": "Test Client",    "redirect_uri": [      "https://example.com/callback"    ],    "secret": "af3t24tfj34h43s...",    "updated_at": "2011-07-22T00:11:12Z",    "url": "https://example.zendesk.com/api/v2/clients/223443.json",    "user_id": 29  }}

### Update Client

  * `PUT /api/v2/oauth/clients/{oauth_client_id}`


#### Allowed for

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
oauth_client_id| integer| Path| true| The ID of the OAuth client

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/oauth/clients/{oauth_client_id}.json \  -X PUT -H "Content-Type: application/json" \  -d '{"client": {"name": "My New OAuth2 Client"}}'  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/oauth/clients/223443"	method := "PUT"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/oauth/clients/223443")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'PUT',  url: 'https://support.zendesk.com/api/v2/oauth/clients/223443',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/oauth/clients/223443"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/oauth/clients/223443")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "client": {    "company": "Zendesk",    "created_at": "2009-05-13T00:07:08Z",    "description": "Zendesk Test Client",    "id": 223443,    "identifier": "test_client",    "name": "My New OAuth2 Client",    "redirect_uri": [      "https://example.com/callback"    ],    "secret": "af3t24tfj34h43s...",    "updated_at": "2011-07-22T00:11:12Z",    "url": "https://example.zendesk.com/api/v2/clients/223443.json",    "user_id": 29  }}

### Delete Client

  * `DELETE /api/v2/oauth/clients/{oauth_client_id}`


#### Allowed for

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
oauth_client_id| integer| Path| true| The ID of the OAuth client

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/oauth/clients/{oauth_client_id}.json \  -X DELETE -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/oauth/clients/223443"	method := "DELETE"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/oauth/clients/223443")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("DELETE", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'DELETE',  url: 'https://support.zendesk.com/api/v2/oauth/clients/223443',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/oauth/clients/223443"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"DELETE",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/oauth/clients/223443")request = Net::HTTP::Delete.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**204 No Content**


    // Status 204 No Content
    null

### Generate Secret

  * `PUT /api/v2/oauth/clients/{oauth_client_id}/generate_secret`


#### Allowed for

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
oauth_client_id| integer| Path| true| The ID of the OAuth client

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/oauth/clients/{oauth_client_id}/generate_secret.json \  -X PUT -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/oauth/clients/223443/generate_secret"	method := "PUT"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/oauth/clients/223443/generate_secret")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'PUT',  url: 'https://support.zendesk.com/api/v2/oauth/clients/223443/generate_secret',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/oauth/clients/223443/generate_secret"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/oauth/clients/223443/generate_secret")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "client": {    "company": "Zendesk",    "created_at": "2009-05-13T00:07:08Z",    "description": "Zendesk Test Client",    "id": 223443,    "identifier": "test_client",    "name": "Test Client",    "redirect_uri": [      "https://example.com/callback"    ],    "secret": "af3t24tfj34h43s...",    "updated_at": "2011-07-22T00:11:12Z",    "url": "https://example.zendesk.com/api/v2/clients/223443.json",    "user_id": 29  }}

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)