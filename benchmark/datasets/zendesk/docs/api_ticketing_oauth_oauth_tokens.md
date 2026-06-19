# OAuth Tokens

*Source: https://developer.zendesk.com/api-reference/ticketing/oauth/oauth_tokens/*

---

## On this page

  * [JSON format](/api-reference/ticketing/oauth/oauth_tokens/#json-format)
  * [List Tokens](/api-reference/ticketing/oauth/oauth_tokens/#list-tokens)
  * [Show Token](/api-reference/ticketing/oauth/oauth_tokens/#show-token)
  * [Create Token](/api-reference/ticketing/oauth/oauth_tokens/#create-token)
  * [Revoke Token](/api-reference/ticketing/oauth/oauth_tokens/#revoke-token)


# OAuth Tokens

## On this page

  * [JSON format](/api-reference/ticketing/oauth/oauth_tokens/#json-format)
  * [List Tokens](/api-reference/ticketing/oauth/oauth_tokens/#list-tokens)
  * [Show Token](/api-reference/ticketing/oauth/oauth_tokens/#show-token)
  * [Create Token](/api-reference/ticketing/oauth/oauth_tokens/#create-token)
  * [Revoke Token](/api-reference/ticketing/oauth/oauth_tokens/#revoke-token)


### JSON format

OAuth Tokens are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
client_id| integer| true| false| The id of the client this token belongs to
created_at| string| true| false| The time the token was created
expires_at| string| true| false| The time the token will expire
id| integer| true| false| Automatically assigned upon creation
refresh_token| string| true| false| The refresh token, if generated
refresh_token_expires_at| string| true| false| The time the refresh token will expire
scopes| array| true| false| An array of the valid scopes for this token. See Scopes below
token| string| true| false| The access token
url| string| true| false| The API url of this record
used_at| string| true| false| The latest time this token was used for authentication
user_id| integer| true| false| The id of the user this token authenticates as

#### Example


    {  "client_id": 41,  "created_at": "2009-05-13T00:07:08Z",  "expires_at": "2011-07-22T00:11:12Z",  "id": 1,  "refresh_token": "af3t24tfj34h43s...",  "refresh_token_expires_at": "2011-07-22T00:11:12Z",  "scopes": [    "read"  ],  "token": "af3t24tfj34h43s...",  "url": "https://example.zendesk.com/api/v2/tokens/1.json",  "used_at": "2010-01-22T00:11:12Z",  "user_id": 29}

### List Tokens

  * `GET /api/v2/oauth/tokens`


Returns the properties of the tokens for the current user. Admins can view OAuth token properties for all users using the [all](/api-reference/ticketing/oauth/oauth_tokens/#parameters) parameter. To filter the list by OAuth client, use the [client_id](/api-reference/ticketing/oauth/oauth_tokens/#parameters) parameter for a local OAuth client ID, or the [global_client_id](/api-reference/ticketing/oauth/oauth_tokens/#parameters) parameter for a global OAuth client ID. For security reasons, only the first 10 characters of each access token are included.

#### Pagination

  * Cursor pagination (recommended)
  * Offset pagination


See [Pagination](/api-reference/introduction/pagination/).

Returns a maximum of 100 records per page.

#### Allowed For

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
all| boolean| Query| false| A boolean that returns all OAuth tokens in the account. Requires admin role
client_id| integer| Query| false| The id of the OAuth client
global_client_id| integer| Query| false| The id of the global OAuth client

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/oauth/tokens.json \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/oauth/tokens?all=true&client_id=223443"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/oauth/tokens")		.newBuilder()		.addQueryParameter("all", "true")		.addQueryParameter("client_id", "223443");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/oauth/tokens',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'all': 'true',    'client_id': '223443',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/oauth/tokens?all=true&client_id=223443"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/oauth/tokens")uri.query = URI.encode_www_form("all": "true", "client_id": "223443")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "tokens": [    {      "client_id": 41,      "created_at": "2009-05-13T00:07:08Z",      "expires_at": "2011-07-22T00:11:12Z",      "id": 223443,      "refresh_token": "af3t24tfj34h43s...",      "scopes": [        "read"      ],      "token": "af3345kdj3",      "url": "https://example.zendesk.com/api/v2/tokens/223443.json",      "used_at": "2010-01-22T00:11:12Z",      "user_id": 29    },    {      "client_id": 41,      "created_at": "2009-05-13T00:07:08Z",      "expires_at": "2011-07-22T00:11:12Z",      "id": 8678530,      "refresh_token": "af3t24tfj34h43s...",      "scopes": [        "read"      ],      "token": "34hjgkjas4",      "url": "https://example.zendesk.com/api/v2/tokens/8678530.json",      "used_at": "2010-01-22T00:11:12Z",      "user_id": 29    }  ]}

### Show Token

  * `GET /api/v2/oauth/tokens/{oauth_token_id}`
  * `GET /api/v2/oauth/tokens/current.json`


Returns the properties of the specified token. For security reasons, only the first 10 characters of the access token are included.

In the first endpoint, `id` is a token id, not the full token.

In the second endpoint, include an `Authorization: Bearer` header with the full token to get its associated properties. Example:


    curl https://{subdomain}.zendesk.com/api/v2/oauth/tokens/current.json \  -H 'Authorization: Bearer ${authToken}' \  -v -u {email_address}/token:{api_token}

#### Allowed for

  * Admins, Agents, End Users


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
oauth_token_id| integer| Path| true| The ID of the OAuth token

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/oauth/tokens/{oauth_token_id}.json \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/oauth/tokens/223443"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/oauth/tokens/223443")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/oauth/tokens/223443',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/oauth/tokens/223443"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/oauth/tokens/223443")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "token": {    "client_id": 1234,    "created_at": "2009-05-13T00:07:08Z",    "expires_at": "2011-07-22T00:11:12Z",    "id": 223443,    "refresh_token": "af3t24tfj34h43s...",    "scopes": [      "read",      "write"    ],    "token": "af3345kdj3",    "url": "https://example.zendesk.com/api/v2/tokens/223443.json",    "used_at": "2010-01-22T00:11:12Z",    "user_id": 29  }}

### Create Token

  * `POST /api/v2/oauth/tokens`


Returns an OAuth access token with a specified scope.

Refresh tokens aren't used. An access token doesn't expire but it can be revoked.

For a tutorial, see [Creating and using OAuth tokens with the API](/documentation/ticketing/working-with-oauth/creating-and-using-oauth-tokens-with-the-api/).

**Note** : For OAuth authorization code, use the [Create Token for Grant Type](/api-reference/ticketing/oauth/grant_type_tokens/#create-token-for-grant-type) endpoint. The two APIs don't share the same path, JSON format, or request parameters. However, both APIs return access tokens that can be used to [authenticate API requests](/api-reference/ticketing/introduction/#oauth-access-token).

#### Allowed For

  * Admins


#### Request parameters

The POST request takes a "token" object that contains an OAuth client's resource id and scopes.

Name| Type| Description
---|---|---
client_id| integer| The resource `id` of an [OAuth client](/api-reference/ticketing/oauth/oauth_clients/#json-format) (not the client's unique identifier). For the ids, see [List Clients](/api-reference/ticketing/oauth/oauth_clients/#list-clients)
scopes| array| Valid scopes for the token. See Scopes below

#### Scopes

The **scopes** parameter defines whether requests authenticated with the token can post, put, and delete data, or only get data.

**Note** : Don't confuse the **scopes** parameter (plural) with the **scope** parameter (singular) for [grant-type tokens](/api-reference/ticketing/oauth/grant_type_tokens/).

The **scopes** parameter is an array of strings, each specifying a resource name and an access setting. Access is either "read" or "write". If you don't specify a resource, access to all resources is assumed. If you don't specify the access, read and write access are assumed.

The syntax is as follows:

`"scopes": [resource:scope, ...]`

where `resource` is optional.

**Examples**

`"scopes": ["read"]`

`"scopes": ["tickets:read"]`

To give read and write access to a resource, specify both scopes:

`"scopes": ["users:read", "users:write"]`

To give write access only to one resource and read access to everything else:

`"scopes": ["organizations:write", "read"]`

**Note** : The endpoint returns an access token even if you specify an invalid scope. Any request you make with the token will return a "Forbidden" error.

**Available scopes**

  * `read` \- gives access to GET endpoints. Includes


permission to sideload related resources

  * `write` \- gives access to POST, PUT, and DELETE endpoints
  * `impersonate` \- allows Zendesk Support admins to make requests on behalf of


end users. See [Making API requests on behalf of end users](/documentation/ticketing/using-the-zendesk-api/making-api-requests-on-behalf-of-end-users/)

**Resources that can be scoped**

  * tickets
  * users
  * auditlogs (read only)
  * organizations
  * hc
  * apps
  * triggers
  * automations
  * targets
  * webhooks
  * macros
  * requests
  * satisfaction_ratings
  * dynamic_content
  * any_channel (write only)
  * web_widget (write only)
  * unrestricted (read and write)


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
all| boolean| Query| false| A boolean that returns all OAuth tokens in the account. Requires admin role
client_id| integer| Query| false| The id of the OAuth client
global_client_id| integer| Query| false| The id of the global OAuth client

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/oauth/tokens.json \ -H "Content-Type: application/json" \ -d '{"token": {"client_id": 1234, "scopes": ["read", "write"]}}' \ -X POST -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/oauth/tokens?all=true&client_id=223443"	method := "POST"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/oauth/tokens")		.newBuilder()		.addQueryParameter("all", "true")		.addQueryParameter("client_id", "223443");RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'POST',  url: 'https://support.zendesk.com/api/v2/oauth/tokens',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'all': 'true',    'client_id': '223443',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/oauth/tokens?all=true&client_id=223443"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/oauth/tokens")uri.query = URI.encode_www_form("all": "true", "client_id": "223443")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**201 Created**


    // Status 201 Created
    {  "token": {    "client_id": 1234,    "created_at": "2009-05-13T00:07:08Z",    "expires_at": "2011-07-22T00:11:12Z",    "id": 223443,    "refresh_token": "af3t24tfj34h43s...",    "scopes": [      "read",      "write"    ],    "token": "af3345kdj3",    "url": "https://example.zendesk.com/api/v2/tokens/223443.json",    "used_at": "2010-01-22T00:11:12Z",    "user_id": 29  }}

### Revoke Token

  * `DELETE /api/v2/oauth/tokens/{oauth_token_id}`
  * `DELETE /api/v2/oauth/tokens/current.json`


#### Allowed for

  * Admins, Agents, End Users


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
oauth_token_id| integer| Path| true| The ID of the OAuth token

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/oauth/tokens/{oauth_token_id}.json \  -X DELETE -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/oauth/tokens/223443"	method := "DELETE"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/oauth/tokens/223443")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("DELETE", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'DELETE',  url: 'https://support.zendesk.com/api/v2/oauth/tokens/223443',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/oauth/tokens/223443"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"DELETE",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/oauth/tokens/223443")request = Net::HTTP::Delete.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**204 No Content**


    // Status 204 No Content
    null

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)