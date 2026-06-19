# User Identities

*Source: https://developer.zendesk.com/api-reference/ticketing/users/user_identities/*

---

## On this page

  * [JSON format](/api-reference/ticketing/users/user_identities/#json-format)
  * [List End User Identities](/api-reference/ticketing/users/user_identities/#list-end-user-identities)
  * [Show End User Identity](/api-reference/ticketing/users/user_identities/#show-end-user-identity)
  * [Create End User Identity](/api-reference/ticketing/users/user_identities/#create-end-user-identity)
  * [List Identities](/api-reference/ticketing/users/user_identities/#list-identities)
  * [Show Identity](/api-reference/ticketing/users/user_identities/#show-identity)
  * [Create Identity](/api-reference/ticketing/users/user_identities/#create-identity)
  * [Update Identity](/api-reference/ticketing/users/user_identities/#update-identity)
  * [Make Identity Primary](/api-reference/ticketing/users/user_identities/#make-identity-primary)
  * [Verify Identity](/api-reference/ticketing/users/user_identities/#verify-identity)
  * [Request User Verification](/api-reference/ticketing/users/user_identities/#request-user-verification)
  * [Delete Identity](/api-reference/ticketing/users/user_identities/#delete-identity)
  * [Request End User Verification](/api-reference/ticketing/users/user_identities/#request-end-user-verification)
  * [Delete End User Identity](/api-reference/ticketing/users/user_identities/#delete-end-user-identity)
  * [Make End User Identity Primary](/api-reference/ticketing/users/user_identities/#make-end-user-identity-primary)


# User Identities

## On this page

  * [JSON format](/api-reference/ticketing/users/user_identities/#json-format)
  * [List End User Identities](/api-reference/ticketing/users/user_identities/#list-end-user-identities)
  * [Show End User Identity](/api-reference/ticketing/users/user_identities/#show-end-user-identity)
  * [Create End User Identity](/api-reference/ticketing/users/user_identities/#create-end-user-identity)
  * [List Identities](/api-reference/ticketing/users/user_identities/#list-identities)
  * [Show Identity](/api-reference/ticketing/users/user_identities/#show-identity)
  * [Create Identity](/api-reference/ticketing/users/user_identities/#create-identity)
  * [Update Identity](/api-reference/ticketing/users/user_identities/#update-identity)
  * [Make Identity Primary](/api-reference/ticketing/users/user_identities/#make-identity-primary)
  * [Verify Identity](/api-reference/ticketing/users/user_identities/#verify-identity)
  * [Request User Verification](/api-reference/ticketing/users/user_identities/#request-user-verification)
  * [Delete Identity](/api-reference/ticketing/users/user_identities/#delete-identity)
  * [Request End User Verification](/api-reference/ticketing/users/user_identities/#request-end-user-verification)
  * [Delete End User Identity](/api-reference/ticketing/users/user_identities/#delete-end-user-identity)
  * [Make End User Identity Primary](/api-reference/ticketing/users/user_identities/#make-end-user-identity-primary)


A user identity is something that can be used to identify an individual. Most likely, it's an email address, an X (formerly Twitter) handle, or a phone number. Zendesk Support supports a series of different such identities.

This API does not support OAuth tokens scoped for "users:write" or "users:read". See [Scopes](/api-reference/ticketing/oauth/oauth_tokens/#scopes).

### JSON format

User Identities are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
created_at| string| true| false| The time the identity was created
deliverable_state| string| true| false| Email identity type only. Indicates if Zendesk sends notifications to the email address. See Deliverable state
id| integer| true| false| Automatically assigned on creation
primary| boolean| false| false| If the identity is the primary identity. *Writable only when creating, not when updating. Use the Make Identity Primary endpoint instead
type| string| true| true| The type of this identity. Allowed values are "email", "twitter", "facebook", "google", "phone_number", "agent_forwarding", "any_channel", "foreign", "sdk", or "messaging".
undeliverable_count| integer| true| false| The number of times a soft-bounce response was received at that address
updated_at| string| true| false| The time the identity was updated
url| string| true| false| The API url of this identity
user_id| integer| true| true| The id of the user
value| string| true| true| The identifier for this identity, such as an email address
verification_method| string| false| false| Indicates the state of user identity verification. See Verification method. Allowed values are "none", "low", "sso", "embed", or "full".
verified| boolean| false| false| (Deprecated). If the identity has been verified. Deprecated. Use `verification_method` as a more accurate representation of a user's state of verification.
verified_at| string| true| false| The last time a full verification flow was completed for the identity

If the identity is of type "phone_number", the phone number must be a direct line, not a shared phone number. See [Phone Number](/api-reference/ticketing/users/users/#phone-number) in the Users API.

#### Deliverable state

When a user has multiple email addresses, Zendesk will choose the best one to deliver email notifications. The `deliverable_state` property helps to determine that identity. If the value is "deliverable", Zendesk will likely use that identity over other email addresses; in the same way, Zendesk will not choose an email address that will likely fail to receive an email.

Value| Description
---|---
deliverable| Email address marked as deliverable
undeliverable| Email address marked as undeliverable
ticket_sharing_partner| Email address used by a Ticket Sharing Partner integration between two Zendesk instances. Considered undeliverable to prevent email loops
mailing_list| Email address used for mailing lists with multiple individual recipients. Considered undeliverable to prevent email loops
reserved_example| Email address used for documentation and testing only. Includes @example.com, @example.net, @example.org, and @example.edu. Considered undeliverable because it's a reserved example domain
machine| Email address used by other providers to deliver machine-generated emails (like automatic responses, marketing campaigns). Considered undeliverable to prevent email loops
mailer_daemon| Email address reserved for delivery notifications agents. Includes [[email protected]](/cdn-cgi/l/email-protection#abc6cac2c7ced986cfcacec6c4c5ebcfc4c6cac2c585c8c4c6) and @mailer-daemon.domain.com. Considered undeliverable because it's a machine address
mandatory| Email address marked as mandatory. Zendesk will prefer this address in some situations when the user switches identities

#### Verification method

Email verification settles a trusted connection of ownership between a specific Zendesk user and an email identity. The `verification` property indicates whether or not a full email verification has taken place.

The `verification_method` property can have any of the following values:

Value| Description
---|---
none| The user has provided an email address
low| An individual agent has marked the email as verified
sso| The identity provider has included the email as a SAML assertion or claim, as part of SSO login flow
embed| The email was provided in a JWT as part of an embedded Web Widget or SDK login flow. See [Setting up user authentication](https://support.zendesk.com/hc/en-us/articles/4411666638746)
full| Zendesk has run an email verification flow first hand

The API only allows the `verification_method` property to be directly set to the values "none" or "low". For example, the only way to get the value to "full" would be to have the end user complete an email verification flow. An attempt to set "sso", "embed" or "full" `verification_method` states directly is rejected with a 400 Bad Request error.

#### Example


    {  "created_at": "2011-07-20T22:55:29Z",  "deliverable_state": "deliverable",  "id": 35436,  "primary": true,  "type": "email",  "updated_at": "2011-07-20T22:55:29Z",  "url": "https://company.zendesk.com/api/v2/users/135/identities/35436",  "user_id": 135,  "value": "[[email protected]](/cdn-cgi/l/email-protection)",  "verification_method": "full",  "verified": true,  "verified_at": "2011-07-20T22:55:29Z"}

### List End User Identities

  * `GET /api/v2/end_users/{user_id}/identities`


Returns a list of identities for the given end user.

End users can only list email and phone number identities.

#### Pagination

  * Cursor pagination (recommended)
  * Offset pagination


See [Pagination](/api-reference/introduction/pagination/).

Returns a maximum of 100 records per page for cursor pagination.

#### Allowed For

  * Verified end users


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
type[]| string| Query| false| Filters results by one or more identity types using the format `?type[]={type}&type[]={type}`. Allowed values are "email", or "phone_number".
user_id| integer| Path| true| The id of the user

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/end_users/{user_id}/identities \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/end_users/35436/identities?type[]="	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/end_users/35436/identities")		.newBuilder()		.addQueryParameter("type[]", "");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/end_users/35436/identities',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'type[]': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/end_users/35436/identities?type[]="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/end_users/35436/identities")uri.query = URI.encode_www_form("type[]": "")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "identities": [    {      "created_at": "2011-07-20T22:55:29Z",      "id": 35436,      "primary": true,      "type": "email",      "updated_at": "2011-07-20T22:55:29Z",      "user_id": 135,      "value": "[[email protected]](/cdn-cgi/l/email-protection)",      "verification_method": "low",      "verified": true    },    {      "created_at": "2012-02-12T14:25:21Z",      "id": 77136,      "primary": false,      "type": "twitter",      "updated_at": "2012-02-12T14:25:21Z",      "user_id": 135,      "value": "didgeridooboy",      "verification_method": "low",      "verified": true    },    {      "created_at": "2012-02-12T14:25:21Z",      "id": 88136,      "primary": true,      "type": "phone_number",      "updated_at": "2012-02-12T14:25:21Z",      "user_id": 135,      "value": "+1 555-123-4567",      "verification_method": "low",      "verified": true    }  ]}

### Show End User Identity

  * `GET /api/v2/end_users/{user_id}/identities/{user_identity_id}`


Shows the identity with the given id for a given end user.

End users can only view email or phone number identity.

#### Allowed For

  * Verified end users


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
user_id| integer| Path| true| The id of the user
user_identity_id| integer| Path| true| The ID of the user identity

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/end_users/{user_id}/identities/{user_identity_id} \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/end_users/35436/identities/77938"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/end_users/35436/identities/77938")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/end_users/35436/identities/77938',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/end_users/35436/identities/77938"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/end_users/35436/identities/77938")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "identity": {    "created_at": "2012-02-12T14:25:21Z",    "id": 77938,    "primary": false,    "type": "twitter",    "updated_at": "2012-02-12T14:25:21Z",    "user_id": 13531,    "value": "cabanaboy",    "verified": false  }}

### Create End User Identity

  * `POST /api/v2/end_users/{user_id}/identities`


Adds an identity to an end user's profile.

Supported identity types for end users:

Type| Example
---|---
email| `{ "type" : "email", "value" : "[[email protected]](/cdn-cgi/l/email-protection)" }`
phone_number| `{ "type" : "phone_number", "value" : "+1 555-123-4567" }`

#### Allowed For

  * Verified end users


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
type[]| string| Query| false| Filters results by one or more identity types using the format `?type[]={type}&type[]={type}`. Allowed values are "email", or "phone_number".
user_id| integer| Path| true| The id of the user

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/end_users/{user_id}/identities \  -H "Content-Type: application/json" -X POST \  -d '{"identity": {"type": "email", "value": "[[email protected]](/cdn-cgi/l/email-protection)"}}' -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/end_users/35436/identities?type[]="	method := "POST"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/end_users/35436/identities")		.newBuilder()		.addQueryParameter("type[]", "");RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'POST',  url: 'https://example.zendesk.com/api/v2/end_users/35436/identities',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'type[]': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/end_users/35436/identities?type[]="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/end_users/35436/identities")uri.query = URI.encode_www_form("type[]": "")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**201 Created**


    // Status 201 Created
    {  "identity": {    "created_at": "2012-02-12T14:25:21Z",    "id": 77938,    "primary": false,    "type": "twitter",    "updated_at": "2012-02-12T14:25:21Z",    "user_id": 13531,    "value": "cabanaboy",    "verification_method": "none",    "verified": false  }}

### List Identities

  * `GET /api/v2/users/{user_id}/identities`


Returns a list of identities for the given user.

Use the first endpoint if authenticating as an agent. Use the second if authenticating as an end user. End users can only list email and phone number identities.

#### Pagination

  * Cursor pagination (recommended)
  * Offset pagination


See [Pagination](/api-reference/introduction/pagination/).

Returns a maximum of 100 records per page for cursor pagination.

#### Allowed For

  * Agents
  * Verified end users


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
include_boundary_indicators| boolean| Query| false| When true, includes `has_more` indicator in the cursor pagination response meta. Only valid with cursor pagination (page[size], page[after], page[before]).
include_item_cursors| boolean| Query| false| When true, includes cursor values for each item in the cursor pagination response. Only valid with cursor pagination (page[size], page[after], page[before]).
page| object| Query| false| Cursor-based pagination parameters (JSON:API style). Supports nested parameters: - `page[size]` \- Number of records per page (default varies by endpoint, typically 100) - `page[after]` \- Cursor token to fetch records after this position - `page[before]` \- Cursor token to fetch records before this position Example: `?page[size]=50&page[after]=eyJvIjoiaWQiLCJ2IjoiYVFFPSJ9`
sort| string| Query| false| Field to sort results by. Prefix with `-` for descending order. When used with cursor pagination, this determines the cursor ordering. Example: `?sort=name` or `?sort=-created_at`
user_id| integer| Path| true| The id of the user

#### Code Samples

**curl**

Agents only


    curl https://{subdomain}.zendesk.com/api/v2/users/{user_id}/identities \  -v -u {email_address}/token:{api_token}

**curl**

Filtering to only `email` and `phone_number` types


    curl https://{subdomain}.zendesk.com/api/v2/users/{user_id}/identities?type[]=email&type[]=phone_number \  -v -u {email_address}/token:{api_token}

**curl**

Verified end users only


    curl https://{subdomain}.zendesk.com/api/v2/end_users/{user_id}/identities \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/users/35436/identities?include_boundary_indicators=&include_item_cursors=&page=&sort=name"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/users/35436/identities")		.newBuilder()		.addQueryParameter("include_boundary_indicators", "")		.addQueryParameter("include_item_cursors", "")		.addQueryParameter("page", "")		.addQueryParameter("sort", "name");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/users/35436/identities',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'include_boundary_indicators': '',    'include_item_cursors': '',    'page': '',    'sort': 'name',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/users/35436/identities?include_boundary_indicators=&include_item_cursors=&page=&sort=name"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/users/35436/identities")uri.query = URI.encode_www_form("include_boundary_indicators": "", "include_item_cursors": "", "page": "", "sort": "name")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "identities": [    {      "created_at": "2011-07-20T22:55:29Z",      "id": 35436,      "primary": true,      "type": "email",      "updated_at": "2011-07-20T22:55:29Z",      "user_id": 135,      "value": "[[email protected]](/cdn-cgi/l/email-protection)",      "verification_method": "low",      "verified": true    },    {      "created_at": "2012-02-12T14:25:21Z",      "id": 77136,      "primary": false,      "type": "twitter",      "updated_at": "2012-02-12T14:25:21Z",      "user_id": 135,      "value": "didgeridooboy",      "verification_method": "low",      "verified": true    },    {      "created_at": "2012-02-12T14:25:21Z",      "id": 88136,      "primary": true,      "type": "phone_number",      "updated_at": "2012-02-12T14:25:21Z",      "user_id": 135,      "value": "+1 555-123-4567",      "verification_method": "low",      "verified": true    }  ]}

### Show Identity

  * `GET /api/v2/users/{user_id}/identities/{user_identity_id}`


Shows the identity with the given id for a given user.

Use the first endpoint if authenticating as an agent. Use the second if authenticating as an end user. End users can only view email or phone number identity.

#### Allowed For

  * Agents
  * Verified end users


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
user_id| integer| Path| true| The id of the user
user_identity_id| integer| Path| true| The ID of the user identity

#### Code Samples

**curl**

Agents only


    curl https://{subdomain}.zendesk.com/api/v2/users/{user_id}/identities/{user_identity_id} \  -v -u {email_address}/token:{api_token}

**curl**

Verified end users only


    curl https://{subdomain}.zendesk.com/api/v2/end_users/{user_id}/identities/{user_identity_id} \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/users/35436/identities/77938"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/users/35436/identities/77938")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/users/35436/identities/77938',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/users/35436/identities/77938"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/users/35436/identities/77938")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "identity": {    "created_at": "2012-02-12T14:25:21Z",    "id": 77938,    "primary": false,    "type": "twitter",    "updated_at": "2012-02-12T14:25:21Z",    "user_id": 13531,    "value": "cabanaboy",    "verified": false  }}

### Create Identity

  * `POST /api/v2/users/{user_id}/identities`


Adds an identity to a user's profile. An agent can add an identity to any user profile.

Supported identity types:

Type| Example
---|---
email| `{ "type" : "email", "value" : "[[email protected]](/cdn-cgi/l/email-protection)" }`
twitter| `{ "type" : "twitter", "value" : "screen_name" }`
facebook| `{ "type" : "facebook", "value" : "855769377321" }`
google| `{ "type" : "google", "value" : "[[email protected]](/cdn-cgi/l/email-protection)" }`
agent_forwarding| `{ "type" : "agent_forwarding", "value" : "+1 555-123-4567" }`
phone_number| `{ "type" : "phone_number", "value" : "+1 555-123-4567" }`

To create an identity without sending out a verification email, include a `"skip_verify_email": true` property. The `"skip_verify_email": true` property does not apply when updating your own agent profile. A welcome or verification email will be sent regardless of this setting.

#### Allowed For

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
user_id| integer| Path| true| The id of the user

#### Code Samples

**curl**

Agents only


    curl https://{subdomain}.zendesk.com/api/v2/users/{user_id}/identities \  -H "Content-Type: application/json" -X POST \  -d '{"identity": {"type": "email", "value": "[[email protected]](/cdn-cgi/l/email-protection)"}}' -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/users/35436/identities"	method := "POST"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/users/35436/identities")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'POST',  url: 'https://example.zendesk.com/api/v2/users/35436/identities',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/users/35436/identities"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/users/35436/identities")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**201 Created**


    // Status 201 Created
    {  "identity": {    "created_at": "2012-02-12T14:25:21Z",    "id": 77938,    "primary": false,    "type": "twitter",    "updated_at": "2012-02-12T14:25:21Z",    "user_id": 13531,    "value": "cabanaboy",    "verification_method": "none",    "verified": false  }}

### Update Identity

  * `PUT /api/v2/users/{user_id}/identities/{user_identity_id}`


This endpoint allows you to:

  * Set the specified identity as verified (by setting `verified` to "true" or `verification_method` to "low")
  * Unverify a verified identity (by setting `verified` to "false" or `verification_method` to "none")
  * Update the `value` property of the specified identity


You can't change an identity's `primary` attribute with this endpoint. You must use the Make Identity Primary endpoint instead.

#### Allowed For

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
user_id| integer| Path| true| The id of the user
user_identity_id| integer| Path| true| The ID of the user identity

#### Code Samples

**curl**

To update `verification_method`


    curl https://{subdomain}.zendesk.com/api/v2/users/{user_id}/identities/{user_identity_id} \  -H "Content-Type: application/json" -X PUT \  -d '{"identity": {"verification_method": "low"}}' -v -u {email_address}/token:{api_token}

**curl**

To update `verified`


    curl https://{subdomain}.zendesk.com/api/v2/users/{user_id}/identities/{user_identity_id} \  -H "Content-Type: application/json" -X PUT \  -d '{"identity": {"verified": true}}' -v -u {email_address}/token:{api_token}

**curl**

To update `value`


    curl https://{subdomain}.zendesk.com/api/v2/users/{user_id}/identities/{user_identity_id} \  -H "Content-Type: application/json" -X PUT \  -d '{"identity": {"value": "[[email protected]](/cdn-cgi/l/email-protection)"}}' -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/users/35436/identities/77938"	method := "PUT"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/users/35436/identities/77938")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'PUT',  url: 'https://example.zendesk.com/api/v2/users/35436/identities/77938',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/users/35436/identities/77938"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/users/35436/identities/77938")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "identity": {    "created_at": "2011-07-20T22:55:29Z",    "deliverable_state": "deliverable",    "id": 35436,    "primary": true,    "type": "email",    "updated_at": "2011-07-20T22:55:29Z",    "user_id": 135,    "value": "[[email protected]](/cdn-cgi/l/email-protection)",    "verification_method": "low",    "verified": true  }}

### Make Identity Primary

  * `PUT /api/v2/users/{user_id}/identities/{user_identity_id}/make_primary`


Sets the specified identity as primary. To change other attributes, use the Update Identity endpoint. This is a collection-level operation and the correct behavior for an API client is to subsequently reload the entire collection.

The first endpoint is the preferred option if authenticating as an agent. If authenticating as an end user, you can only use the second endpoint. In addition, an end user can only make an email identity primary if the email is verified.

#### Allowed For

  * Agents
  * Verified end users


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
user_id| integer| Path| true| The id of the user
user_identity_id| integer| Path| true| The ID of the user identity

#### Code Samples

**curl**

Agents only


    curl https://{subdomain}.zendesk.com/api/v2/users/{user_id}/identities/{user_identity_id}/make_primary \  -X PUT -v -u {email_address}/token:{api_token} -d '{}' -H "Content-Type: application/json"

**curl**

Verified end users only


    curl https://{subdomain}.zendesk.com/api/v2/end_users/{user_id}/identities/{user_identity_id}/make_primary \  -X PUT -v -u {email_address}/token:{api_token} -d '{}' -H "Content-Type: application/json"

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/users/35436/identities/77938/make_primary"	method := "PUT"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/users/35436/identities/77938/make_primary")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'PUT',  url: 'https://example.zendesk.com/api/v2/users/35436/identities/77938/make_primary',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/users/35436/identities/77938/make_primary"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/users/35436/identities/77938/make_primary")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "identities": [    {      "created_at": "2011-07-20T22:55:29Z",      "id": 35436,      "primary": true,      "type": "email",      "updated_at": "2011-07-20T22:55:29Z",      "user_id": 135,      "value": "[[email protected]](/cdn-cgi/l/email-protection)",      "verification_method": "low",      "verified": true    },    {      "created_at": "2012-02-12T14:25:21Z",      "id": 77136,      "primary": false,      "type": "twitter",      "updated_at": "2012-02-12T14:25:21Z",      "user_id": 135,      "value": "didgeridooboy",      "verification_method": "low",      "verified": true    },    {      "created_at": "2012-02-12T14:25:21Z",      "id": 88136,      "primary": true,      "type": "phone_number",      "updated_at": "2012-02-12T14:25:21Z",      "user_id": 135,      "value": "+1 555-123-4567",      "verification_method": "low",      "verified": true    }  ]}

### Verify Identity

  * `PUT /api/v2/users/{user_id}/identities/{user_identity_id}/verify`


Sets the specified identity as verified.

For security reasons, you can't use this endpoint to update the email identity of the account owner. To verify the person's identity, send a verification email. See [Verifying the account owner's email address](https://support.zendesk.com/hc/en-us/articles/4408828975130) in Zendesk help.

If [automatic mapping of users to organizations using the email domain](https://support.zendesk.com/hc/en-us/articles/4408882246298-Creating-organizations#topic_nxl_vdt_bc) is enabled and the user is not already a member of an organization, they will be automatically added to the organization associated with the email domain once the email identity is verified.

#### Allowed For

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
user_id| integer| Path| true| The id of the user
user_identity_id| integer| Path| true| The ID of the user identity

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/users/{user_id}/identities/{user_identity_id}/verify \  -X PUT -v -u {email_address}/token:{api_token} -d '{}' -H "Content-Type: application/json"

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/users/35436/identities/77938/verify"	method := "PUT"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/users/35436/identities/77938/verify")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'PUT',  url: 'https://example.zendesk.com/api/v2/users/35436/identities/77938/verify',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/users/35436/identities/77938/verify"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/users/35436/identities/77938/verify")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "identity": {    "created_at": "2012-02-12T14:25:21Z",    "id": 77938,    "primary": false,    "type": "twitter",    "updated_at": "2012-02-12T14:25:21Z",    "user_id": 13531,    "value": "cabanaboy",    "verified": false  }}

### Request User Verification

  * `PUT /api/v2/users/{user_id}/identities/{user_identity_id}/request_verification`


Sends the user a verification email with a link to verify ownership of the email address.

#### Allowed For

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
user_id| integer| Path| true| The id of the user
user_identity_id| integer| Path| true| The ID of the user identity

#### Code Samples

**curl**

Agents only


    curl https://{subdomain}.zendesk.com/api/v2/users/{user_id}/identities/{user_identity_id}/request_verification \  -X PUT -v -u {email_address}/token:{api_token} -d '{}' -H "Content-Type: application/json"

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/users/35436/identities/77938/request_verification"	method := "PUT"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/users/35436/identities/77938/request_verification")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'PUT',  url: 'https://example.zendesk.com/api/v2/users/35436/identities/77938/request_verification',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/users/35436/identities/77938/request_verification"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/users/35436/identities/77938/request_verification")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    null

### Delete Identity

  * `DELETE /api/v2/users/{user_id}/identities/{user_identity_id}`


Deletes the identity for a given user. In certain cases, a phone number associated with an identity is still visible on the user profile after the identity has been deleted via API. You can remove the phone number from the user profile by updating the `phone` attribute of the user to an empty string. See [Update User via API](/api-reference/ticketing/users/users/#update-user) for details and examples.

Deleting identities with type `messaging` could break messaging functionality. For example, an agent may stop being able to send messages via the messaging channel.

#### Allowed For

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
user_id| integer| Path| true| The id of the user
user_identity_id| integer| Path| true| The ID of the user identity

#### Code Samples

**curl**

Agents only


    curl https://{subdomain}.zendesk.com/api/v2/users/{user_id}/identities/{user_identity_id} \  -X DELETE -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/users/35436/identities/77938"	method := "DELETE"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/users/35436/identities/77938")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("DELETE", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'DELETE',  url: 'https://example.zendesk.com/api/v2/users/35436/identities/77938',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/users/35436/identities/77938"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"DELETE",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/users/35436/identities/77938")request = Net::HTTP::Delete.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**204 No Content**


    // Status 204 No Content
    null

### Request End User Verification

  * `PUT /api/v2/end_users/{user_id}/identities/{user_identity_id}/request_verification`


Sends the end user a verification email with a link to verify ownership of the email address.

#### Allowed For

  * Verified end users


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
user_id| integer| Path| true| The id of the user
user_identity_id| integer| Path| true| The ID of the user identity

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/end_users/{user_id}/identities/{user_identity_id}/request_verification \  -X PUT -v -u {email_address}/token:{api_token} -d '{}' -H "Content-Type: application/json"

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/end_users/35436/identities/77938/request_verification"	method := "PUT"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/end_users/35436/identities/77938/request_verification")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'PUT',  url: 'https://example.zendesk.com/api/v2/end_users/35436/identities/77938/request_verification',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/end_users/35436/identities/77938/request_verification"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/end_users/35436/identities/77938/request_verification")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    null

### Delete End User Identity

  * `DELETE /api/v2/end_users/{user_id}/identities/{user_identity_id}`


Deletes the identity for a given end user.

In certain cases, a phone number associated with an identity is still visible on the user profile after the identity has been deleted via API.

#### Allowed For

  * Verified end users


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
user_id| integer| Path| true| The id of the user
user_identity_id| integer| Path| true| The ID of the user identity

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/end_users/{user_id}/identities/{user_identity_id} \  -X DELETE -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/end_users/35436/identities/77938"	method := "DELETE"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/end_users/35436/identities/77938")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("DELETE", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'DELETE',  url: 'https://example.zendesk.com/api/v2/end_users/35436/identities/77938',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/end_users/35436/identities/77938"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"DELETE",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/end_users/35436/identities/77938")request = Net::HTTP::Delete.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**204 No Content**


    // Status 204 No Content
    null

### Make End User Identity Primary

  * `PUT /api/v2/end_users/{user_id}/identities/{user_identity_id}/make_primary`


Sets the specified identity as primary for the end user. This is a collection-level operation and the correct behavior for an API client is to subsequently reload the entire collection.

An end user can only make an email identity primary if the email is verified.

#### Allowed For

  * Verified end users


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
user_id| integer| Path| true| The id of the user
user_identity_id| integer| Path| true| The ID of the user identity

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/end_users/{user_id}/identities/{user_identity_id}/make_primary \  -X PUT -v -u {email_address}/token:{api_token} -d '{}' -H "Content-Type: application/json"

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/end_users/35436/identities/77938/make_primary"	method := "PUT"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/end_users/35436/identities/77938/make_primary")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'PUT',  url: 'https://example.zendesk.com/api/v2/end_users/35436/identities/77938/make_primary',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/end_users/35436/identities/77938/make_primary"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/end_users/35436/identities/77938/make_primary")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "identities": [    {      "created_at": "2011-07-20T22:55:29Z",      "id": 35436,      "primary": true,      "type": "email",      "updated_at": "2011-07-20T22:55:29Z",      "user_id": 135,      "value": "[[email protected]](/cdn-cgi/l/email-protection)",      "verification_method": "low",      "verified": true    },    {      "created_at": "2012-02-12T14:25:21Z",      "id": 77136,      "primary": false,      "type": "twitter",      "updated_at": "2012-02-12T14:25:21Z",      "user_id": 135,      "value": "didgeridooboy",      "verification_method": "low",      "verified": true    },    {      "created_at": "2012-02-12T14:25:21Z",      "id": 88136,      "primary": true,      "type": "phone_number",      "updated_at": "2012-02-12T14:25:21Z",      "user_id": 135,      "value": "+1 555-123-4567",      "verification_method": "low",      "verified": true    }  ]}

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)