# Profiles API

*Source: https://developer.zendesk.com/api-reference/ticketing/users/profiles_api/profiles_api/*

---

## On this page

  * [JSON format](/api-reference/ticketing/users/profiles_api/profiles_api/#json-format)
  * [Identifier queries](/api-reference/ticketing/users/profiles_api/profiles_api/#identifier-queries)
  * [Get Profiles by User ID](/api-reference/ticketing/users/profiles_api/profiles_api/#get-profiles-by-user-id)
  * [Get Profile by Profile ID](/api-reference/ticketing/users/profiles_api/profiles_api/#get-profile-by-profile-id)
  * [Get Profile by Identifier](/api-reference/ticketing/users/profiles_api/profiles_api/#get-profile-by-identifier)
  * [Create or Update Profile by User ID](/api-reference/ticketing/users/profiles_api/profiles_api/#create-or-update-profile-by-user-id)
  * [Create or Update Profile by Identifier](/api-reference/ticketing/users/profiles_api/profiles_api/#create-or-update-profile-by-identifier)
  * [Update Profile by Profile ID](/api-reference/ticketing/users/profiles_api/profiles_api/#update-profile-by-profile-id)
  * [Partial Update Profile by Profile ID](/api-reference/ticketing/users/profiles_api/profiles_api/#partial-update-profile-by-profile-id)
  * [Partial Update Profile by Identifier](/api-reference/ticketing/users/profiles_api/profiles_api/#partial-update-profile-by-identifier)
  * [Delete Profile by Profile ID](/api-reference/ticketing/users/profiles_api/profiles_api/#delete-profile-by-profile-id)


# Profiles API

## On this page

  * [JSON format](/api-reference/ticketing/users/profiles_api/profiles_api/#json-format)
  * [Identifier queries](/api-reference/ticketing/users/profiles_api/profiles_api/#identifier-queries)
  * [Get Profiles by User ID](/api-reference/ticketing/users/profiles_api/profiles_api/#get-profiles-by-user-id)
  * [Get Profile by Profile ID](/api-reference/ticketing/users/profiles_api/profiles_api/#get-profile-by-profile-id)
  * [Get Profile by Identifier](/api-reference/ticketing/users/profiles_api/profiles_api/#get-profile-by-identifier)
  * [Create or Update Profile by User ID](/api-reference/ticketing/users/profiles_api/profiles_api/#create-or-update-profile-by-user-id)
  * [Create or Update Profile by Identifier](/api-reference/ticketing/users/profiles_api/profiles_api/#create-or-update-profile-by-identifier)
  * [Update Profile by Profile ID](/api-reference/ticketing/users/profiles_api/profiles_api/#update-profile-by-profile-id)
  * [Partial Update Profile by Profile ID](/api-reference/ticketing/users/profiles_api/profiles_api/#partial-update-profile-by-profile-id)
  * [Partial Update Profile by Identifier](/api-reference/ticketing/users/profiles_api/profiles_api/#partial-update-profile-by-identifier)
  * [Delete Profile by Profile ID](/api-reference/ticketing/users/profiles_api/profiles_api/#delete-profile-by-profile-id)


The Profiles API allows you to create a single view of a customer across applications and systems. A profile can contain the various identities of a user in different applications and systems.

This API has a direct relationship to a [Zendesk user](/api-reference/ticketing/users/users/).

The Profiles API is available on the Suite Team plan and above. It is activated in the Admin Center by an admin.

In addition to this API reference, the following resources are available:

  * To get started, see [Getting started with profiles](/documentation/ticketing/profiles/getting-started-with-profiles/) in the Develop Help Center
  * To learn more about using the API, see the [Profiles API developer guide ](/documentation/ticketing/profiles/about-the-profiles-api/)
  * To ask questions, provide answers, and join discussions, visit the [Zendesk API community](https://support.zendesk.com/hc/en-us/community/topics/1260801854210-Zendesk-APIs)


### Run in Postman

If you use Postman, you can import the Sunshine Profiles API endpoints as a collection into your Postman app, then try out different requests to learn how the API works. Click the following button to get started:

[](https://god.gw.postman.com/run-collection/19637986-6f2f6765-5cda-42d4-b46d-ef9137f12a6e?action=collection/fork&collection-url=entityId=19637986-6f2f6765-5cda-42d4-b46d-ef9137f12a6e&entityType=collection&workspaceId=cfe0e8e6-42d1-4f46-a048-90e2caae5a05)

If you don't use Postman, you can sign up for a free account on the [Postman website](https://identity.getpostman.com/signup) and download the app. For more information about using Postman with Zendesk APIs, see [Exploring Zendesk APIs with Postman](/documentation/api-basics/working-with-the-zendesk-apis/exploring-zendesk-apis-with-postman/).

### JSON format

Profiles are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
attributes| object| false| true| [JSON schema compliant](https://json-schema.org/) object containing details about the profile
created_at| string| true| false| An auto-generated datetime of when the object was updated
id| string| true| false| Profile ID
identifiers| array| false| true| The identifier for the application or system where the identity is used
name| string| false| false| The person's name for the profile
source| string| false| true| The application or system associated to the profile. Note that the value 'zendesk' is reserved for future use.
type| string| false| true| The profile type
updated_at| string| true| false| An auto-generated datetime of when the object was updated
user_id| string| false| false| Zendesk user ID that the profile belongs to

#### Identifiers array

The `identifiers` array consists of one or more values used to identify a person in an application or system. Each identifier consists of a `type` and a `value` property which are arbitrary. For example, an identifier can be of `type` "member_id" with a `value` of "0634335".

#### Standard identifiers

It is recommended to submit the identifier types email, Facebook, phone, SDK, X (formerly Twitter), or external ID as "email", "facebook", "phone_number", "sdk", "twitter", and "external_id", respectively. If a Zendesk user identity has been previously created with a "google" type property, it will be internally matched with an identifier type of "email". When the value for identifier types "email" and "twitter" are added or modified, any upper case letters are automatically converted to lower case.

Each profile is associated with a Zendesk user. When creating a profile, the API first looks for a Zendesk user who has a [Zendesk identity](/api-reference/ticketing/users/user_identities/) that matches a standard identifier in the new profile. If a match is found, it associates the profile to the Zendesk user by Zendesk user id (user_id). If no match is found, it creates an anonymous Zendesk user and associates the profile to the user by Zendesk user id.

If the `name` in the `profile` object is not provided, the value of an identifier type will be used for the profile name according to the following rules:

Identifier type used| If type not present| Profile name| Example
---|---|---|---
"email"| | email address| Â "[[email protected]](/cdn-cgi/l/email-protection#3f5950507f5d5e4d11595050)"
"external_id"| "email"| "User " + external idÂ | "User FooBar123"
"phone_number"| "external_id"| "User " + phone number| "User 0411 555 666"
"twitter"| "phone_number"| "Twitter user " + username| "Twitter user FooBar"
"facebook"| "twitter"| "Facebook user " + username| "Facebook user FooBar"
"sdk"| "facebook"| "SDK user " + sdk value| "SDK user FooBarSDK"

If none of the listed identifier types are present, the first identifier present in the `identifiers` object is used. The profile name is set as the identifier's "{`type`} user {`value`}". Example: 'Shado user FooBar'.

**Note** : Any email, phone, Facebook, SDK or X identifier added to a profile is automatically added as an identity to the user in Zendesk Support. Any external ID identifier added to a profile is automatically added as the external_id attribute on the Zendesk user. Please verify the identifier type belongs to the user before creating a profile or submitting changes.

#### Example


    {  "profile": {    "id": "01BX5ZZKBKACTAV9WEVGEMMVRY",    "name": "Jane Smith",    "source": "coolbikes",    "type": "rider",    "identifiers": [      {        "type": "email",        "value": "[[email protected]](/cdn-cgi/l/email-protection)"      },      {        "type": "external_id",        "value": "0987654321"      },      {        "type": "coolbike_id",        "value": "0987654321"      },      {        "type": "phone_number",        "value": 12345678      }    ],    "attributes": {      "favorite_color": "red",      "height": "103cm"    },    "user_id": "123456",    "updated_at": "2019-12-24T03:33:28.591Z",    "created_at": "2019-12-24T03:33:28.591Z"  }}

### Identifier queries

You can reference profile records in Zendesk using identifier queries. You specify an identifier query as a URL parameter in a request.

An identifier query contains the necessary information to find a match of profile records within our system. You must specify a profile source, profile type, identifier type, and identifier value with `:` as the delimiter:

  * `<profile_source>:<profile_type>:<identifier_key>:<identifier_value>`


#### Examples

Identifier query| Explanation| Endpoint example
---|---|---
`mysystem:customer:system_id:abc123`| `profile_source`=`mysystem`, `profile_type`=`customer`, `identifier_type`=`system_id`, `identifier_value`=`abc123`| `GET /api/v2/user_profiles?identifier=mysystem:customer:system_id:abc123`
`mycontacts:default:email:[[email protected]](/cdn-cgi/l/email-protection)`| `profile_source`=`mycontacts`, `profile_type`=`customer`, `identifier_type`=`email`, `identifier_value`=`[[email protected]](/cdn-cgi/l/email-protection)`| `GET /api/v2/user_profiles?identifier=mycontacts:customer:email:[[email protected]](/cdn-cgi/l/email-protection)`
`amazon:customer:external_id:0987654321`| `profile_source`=`amazon`, `profile_type`=`customer`, `identifier_type`=`external_id`, `identifier_value`=`0987654321`| `GET /api/v2/user_profiles?identifier=amazon:customer:external_id:0987654321`
`mywebsite:visitor:fb_id:1000098`| `profile_source`=`mywebsite`, `profile_type`=`visitor`, `identifier_type`=`fb_id`, `identifier_value`=`1000098`| `GET /api/v2/user_profiles?identifier=website:visitor:fb_id:1000098`

### Get Profiles by User ID

  * `GET /api/v2/users/{user_id}/profiles`


Retrieves the profiles of a specified Zendesk user.

#### Allowed For

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
user_id| string| Path| true| Zendesk user ID

#### Code Samples

**curl**


    curl "https://{subdomain}.zendesk.com/api/v2/users/{user_id}/profiles" \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/users/120077332/profiles"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/users/120077332/profiles")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/users/120077332/profiles',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/users/120077332/profiles"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/users/120077332/profiles")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "profiles": [    {      "attributes": {        "membership": "gold"      },      "created_at": "2020-02-03T01:37:16Z",      "id": "01ARZ3NDEKTSV4RRFFQ69G5FAV",      "identifiers": [        {          "type": "email",          "value": "[[email protected]](/cdn-cgi/l/email-protection)"        },        {          "type": "external_id",          "value": "0987654321"        },        {          "type": "phone_number",          "value": "+612345678"        }      ],      "name": "Jane Smith",      "source": "company",      "type": "contact",      "updated_at": "2020-02-03T01:37:16Z",      "user_id": "123456"    }  ]}

### Get Profile by Profile ID

  * `GET /api/v2/user_profiles/{profile_id}`


Returns a profile for a given profile ID.

#### Allowed For

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
profile_id| string| Path| true| Sunshine profile ID

#### Code Samples

**curl**


    curl  "https://{subdomain}.zendesk.com/api/v2/user_profiles/{profile_id}" \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/user_profiles/"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/user_profiles/")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/user_profiles/',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/user_profiles/"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/user_profiles/")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "profile": {    "attributes": {      "membership": "gold"    },    "created_at": "2020-02-03T01:37:16Z",    "id": "01ARZ3NDEKTSV4RRFFQ69G5FAV",    "identifiers": [      {        "type": "email",        "value": "[[email protected]](/cdn-cgi/l/email-protection)"      },      {        "type": "external_id",        "value": "0987654321"      },      {        "type": "phone_number",        "value": "+612345678"      }    ],    "name": "Jane Smith",    "source": "company",    "type": "contact",    "updated_at": "2020-02-03T01:37:16Z",    "user_id": "123456"  }}

**400 Bad Request**


    // Status 400 Bad Request
    {  "errors": [    {      "code": "ClientError",      "id": "10001",      "title": "Some client caused error"    }  ]}

**404 Not Found**


    // Status 404 Not Found
    {  "errors": [    {      "code": "ClientError",      "id": "10001",      "title": "Some client caused error"    }  ]}

### Get Profile by Identifier

  * `GET /api/v2/user_profiles?identifier={identifier}`


Returns a profile that matches the given identifier query criteria. See [Using identifier queries with profiles](/documentation/ticketing/profiles/using-identifier-queries-with-profiles/).

#### Allowed For

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
identifier| string| Query| true| An identifier query to identify the profile. Uses the format of source:type:identifier_type:identifier_value

#### Code Samples

**curl**


    curl  "https://{subdomain}.zendesk.com/api/v2/user_profiles?identifier=company:contact:email:[[email protected]](/cdn-cgi/l/email-protection)" \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/user_profiles?identifier=shoppingnow%3Acustomer%3Aemail%3Aexample%40example.com"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/user_profiles")		.newBuilder()		.addQueryParameter("identifier", "shoppingnow:customer:email:[[email protected]](/cdn-cgi/l/email-protection)");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/user_profiles',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'identifier': 'shoppingnow%3Acustomer%3Aemail%3Aexample%40example.com',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/user_profiles?identifier=shoppingnow%3Acustomer%3Aemail%3Aexample%40example.com"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/user_profiles")uri.query = URI.encode_www_form("identifier": "shoppingnow:customer:email:[[email protected]](/cdn-cgi/l/email-protection)")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "profile": {    "attributes": {      "membership": "gold"    },    "created_at": "2020-02-03T01:37:16Z",    "id": "01ARZ3NDEKTSV4RRFFQ69G5FAV",    "identifiers": [      {        "type": "email",        "value": "[[email protected]](/cdn-cgi/l/email-protection)"      },      {        "type": "external_id",        "value": "0987654321"      },      {        "type": "phone_number",        "value": "+612345678"      }    ],    "name": "Jane Smith",    "source": "company",    "type": "contact",    "updated_at": "2020-02-03T01:37:16Z",    "user_id": "123456"  }}

**400 Bad Request**


    // Status 400 Bad Request
    {  "errors": [    {      "code": "ClientError",      "id": "10001",      "title": "Some client caused error"    }  ]}

**404 Not Found**


    // Status 404 Not Found
    {  "errors": [    {      "code": "ClientError",      "id": "10001",      "title": "Some client caused error"    }  ]}

### Create or Update Profile by User ID

  * `PUT /api/v2/users/{user_id}/profiles?identifier={identifier}`


Creates or updates a profile of a Zendesk user.

The required `identifier` path parameter takes an identifier query. See [Using identifier queries with profiles](/documentation/ticketing/profiles/using-identifier-queries-with-profiles/).

When creating a new profile for a user exceeds the maximum number of profiles, the request will fail.

#### Allowed For

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
identifier| string| Query| true| An identifier query to identify the profile. Uses the format of source:type:identifier_type:identifier_value
user_id| string| Path| true| Zendesk user ID

#### Example body


    {  "profile": {    "attributes": {      "membership": "gold"    },    "identifiers": [      {        "type": "email",        "value": "[[email protected]](/cdn-cgi/l/email-protection)"      },      {        "type": "external_id",        "value": "0987654321"      },      {        "type": "phone_number",        "value": "+612345678"      }    ],    "name": "Jane Smith"  }}

#### Code Samples

**curl**


    curl  "https://{subdomain}.zendesk.com/api/v2/users/{user_id}/profiles?identifier=company:contact:email:[[email protected]](/cdn-cgi/l/email-protection)" \  -d '{"profile":{"name":"JaneSmith","source":"company","type":"contact","user_id":123456,"identifiers":[{"type":"email","value":"[[email protected]](/cdn-cgi/l/email-protection)"},{"type":"external_id","value":"0987654321"},{"type":"phone_number","value":"+612345678"}],"attributes":{"membership":"gold"}}}' \  -H "Content-Type: application/json" \  -X PUT \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://support.zendesk.com/api/v2/users/120077332/profiles?identifier=shoppingnow%3Acustomer%3Aemail%3Aexample%40example.com"	method := "PUT"	payload := strings.NewReader(`{  "profile": {    "attributes": {      "membership": "gold"    },    "identifiers": [      {        "type": "email",        "value": "[[email protected]](/cdn-cgi/l/email-protection)"      },      {        "type": "external_id",        "value": "0987654321"      },      {        "type": "phone_number",        "value": "+612345678"      }    ],    "name": "Jane Smith"  }}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/users/120077332/profiles")		.newBuilder()		.addQueryParameter("identifier", "shoppingnow:customer:email:[[email protected]](/cdn-cgi/l/email-protection)");RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"profile\": {    \"attributes\": {      \"membership\": \"gold\"    },    \"identifiers\": [      {        \"type\": \"email\",        \"value\": \"jane@example.com\"      },      {        \"type\": \"external_id\",        \"value\": \"0987654321\"      },      {        \"type\": \"phone_number\",        \"value\": \"+612345678\"      }    ],    \"name\": \"Jane Smith\"  }}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "profile": {    "attributes": {      "membership": "gold"    },    "identifiers": [      {        "type": "email",        "value": "[[email protected]](/cdn-cgi/l/email-protection)"      },      {        "type": "external_id",        "value": "0987654321"      },      {        "type": "phone_number",        "value": "+612345678"      }    ],    "name": "Jane Smith"  }});
    var config = {  method: 'PUT',  url: 'https://support.zendesk.com/api/v2/users/120077332/profiles',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'identifier': 'shoppingnow%3Acustomer%3Aemail%3Aexample%40example.com',  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/users/120077332/profiles?identifier=shoppingnow%3Acustomer%3Aemail%3Aexample%40example.com"
    payload = json.loads("""{  "profile": {    "attributes": {      "membership": "gold"    },    "identifiers": [      {        "type": "email",        "value": "[[email protected]](/cdn-cgi/l/email-protection)"      },      {        "type": "external_id",        "value": "0987654321"      },      {        "type": "phone_number",        "value": "+612345678"      }    ],    "name": "Jane Smith"  }}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/users/120077332/profiles")uri.query = URI.encode_www_form("identifier": "shoppingnow:customer:email:[[email protected]](/cdn-cgi/l/email-protection)")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")request.body = %q({  "profile": {    "attributes": {      "membership": "gold"    },    "identifiers": [      {        "type": "email",        "value": "[[email protected]](/cdn-cgi/l/email-protection)"      },      {        "type": "external_id",        "value": "0987654321"      },      {        "type": "phone_number",        "value": "+612345678"      }    ],    "name": "Jane Smith"  }})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "profile": {    "attributes": {      "membership": "gold"    },    "created_at": "2020-02-03T01:37:16Z",    "id": "01ARZ3NDEKTSV4RRFFQ69G5FAV",    "identifiers": [      {        "type": "email",        "value": "[[email protected]](/cdn-cgi/l/email-protection)"      },      {        "type": "external_id",        "value": "0987654321"      },      {        "type": "phone_number",        "value": "+612345678"      }    ],    "name": "Jane Smith",    "source": "company",    "type": "contact",    "updated_at": "2020-02-03T01:37:16Z",    "user_id": "123456"  }}

**201 Created**


    // Status 201 Created
    {  "profile": {    "attributes": {      "membership": "gold"    },    "created_at": "2020-02-03T01:37:16Z",    "id": "01ARZ3NDEKTSV4RRFFQ69G5FAV",    "identifiers": [      {        "type": "email",        "value": "[[email protected]](/cdn-cgi/l/email-protection)"      },      {        "type": "external_id",        "value": "0987654321"      },      {        "type": "phone_number",        "value": "+612345678"      }    ],    "name": "Jane Smith",    "source": "company",    "type": "contact",    "updated_at": "2020-02-03T01:37:16Z",    "user_id": "123456"  }}

**400 Bad Request**


    // Status 400 Bad Request
    {  "errors": [    {      "code": "ClientError",      "id": "10001",      "title": "Some client caused error"    }  ]}

**403 Forbidden**


    // Status 403 Forbidden
    {  "errors": [    {      "code": "ClientError",      "id": "10001",      "title": "Some client caused error"    }  ]}

### Create or Update Profile by Identifier

  * `PUT /api/v2/user_profiles?identifier={identifier}`


Creates or updates a profile. See [Creating profiles](/documentation/ticketing/profiles/creating-profiles/) for details.

The required `identifier` path parameter takes an identifier query. See [Using identifier queries with profiles](/documentation/ticketing/profiles/using-identifier-queries-with-profiles/).

If the profile has more than one identifier, all the identifiers should belong to a single user and a single profile.

When identifiers for multiple users are provided, the request will fail.

When creating a new profile for a user exceeds the maximum number of profiles, the request will fail.

Note that the source 'zendesk' is reserved and cannot be used to create a profile.

#### Allowed For

  * Agents


Access also depends on agent role permissions set in **Support** > **People** > **Roles** > **People**.

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
identifier| string| Query| true| An identifier query to identify the profile. Uses the format of source:type:identifier_type:identifier_value

#### Example body


    {  "profile": {    "attributes": {      "membership": "gold"    },    "identifiers": [      {        "type": "email",        "value": "[[email protected]](/cdn-cgi/l/email-protection)"      },      {        "type": "external_id",        "value": "0987654321"      },      {        "type": "phone_number",        "value": "+612345678"      }    ],    "name": "Jane Smith"  }}

#### Code Samples

**curl**


    curl  "https://{subdomain}.zendesk.com/api/v2/user_profiles?identifier=company:contact:email:[[email protected]](/cdn-cgi/l/email-protection)" \  -d '{"profile":{"name":"Jane Smith","source":"company","type":"contact","user_id":123456,"identifiers":[{"type":"email","value":"[[email protected]](/cdn-cgi/l/email-protection)"},{"type":"external_id","value":"0987654321"},{"type":"phone_number","value":"+612345678"}],"attributes":{"membership":"gold"}}}' \  -H "Content-Type: application/json" \  -X PUT \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://support.zendesk.com/api/v2/user_profiles?identifier=shoppingnow%3Acustomer%3Aemail%3Aexample%40example.com"	method := "PUT"	payload := strings.NewReader(`{  "profile": {    "attributes": {      "membership": "gold"    },    "identifiers": [      {        "type": "email",        "value": "[[email protected]](/cdn-cgi/l/email-protection)"      },      {        "type": "external_id",        "value": "0987654321"      },      {        "type": "phone_number",        "value": "+612345678"      }    ],    "name": "Jane Smith"  }}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/user_profiles")		.newBuilder()		.addQueryParameter("identifier", "shoppingnow:customer:email:[[email protected]](/cdn-cgi/l/email-protection)");RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"profile\": {    \"attributes\": {      \"membership\": \"gold\"    },    \"identifiers\": [      {        \"type\": \"email\",        \"value\": \"jane@example.com\"      },      {        \"type\": \"external_id\",        \"value\": \"0987654321\"      },      {        \"type\": \"phone_number\",        \"value\": \"+612345678\"      }    ],    \"name\": \"Jane Smith\"  }}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "profile": {    "attributes": {      "membership": "gold"    },    "identifiers": [      {        "type": "email",        "value": "[[email protected]](/cdn-cgi/l/email-protection)"      },      {        "type": "external_id",        "value": "0987654321"      },      {        "type": "phone_number",        "value": "+612345678"      }    ],    "name": "Jane Smith"  }});
    var config = {  method: 'PUT',  url: 'https://support.zendesk.com/api/v2/user_profiles',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'identifier': 'shoppingnow%3Acustomer%3Aemail%3Aexample%40example.com',  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/user_profiles?identifier=shoppingnow%3Acustomer%3Aemail%3Aexample%40example.com"
    payload = json.loads("""{  "profile": {    "attributes": {      "membership": "gold"    },    "identifiers": [      {        "type": "email",        "value": "[[email protected]](/cdn-cgi/l/email-protection)"      },      {        "type": "external_id",        "value": "0987654321"      },      {        "type": "phone_number",        "value": "+612345678"      }    ],    "name": "Jane Smith"  }}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/user_profiles")uri.query = URI.encode_www_form("identifier": "shoppingnow:customer:email:[[email protected]](/cdn-cgi/l/email-protection)")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")request.body = %q({  "profile": {    "attributes": {      "membership": "gold"    },    "identifiers": [      {        "type": "email",        "value": "[[email protected]](/cdn-cgi/l/email-protection)"      },      {        "type": "external_id",        "value": "0987654321"      },      {        "type": "phone_number",        "value": "+612345678"      }    ],    "name": "Jane Smith"  }})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "profile": {    "attributes": {      "membership": "gold"    },    "created_at": "2020-02-03T01:37:16Z",    "id": "01ARZ3NDEKTSV4RRFFQ69G5FAV",    "identifiers": [      {        "type": "email",        "value": "[[email protected]](/cdn-cgi/l/email-protection)"      },      {        "type": "external_id",        "value": "0987654321"      },      {        "type": "phone_number",        "value": "+612345678"      }    ],    "name": "Jane Smith",    "source": "company",    "type": "contact",    "updated_at": "2020-02-03T01:37:16Z",    "user_id": "123456"  }}

**201 Created**


    // Status 201 Created
    {  "profile": {    "attributes": {      "membership": "gold"    },    "created_at": "2020-02-03T01:37:16Z",    "id": "01ARZ3NDEKTSV4RRFFQ69G5FAV",    "identifiers": [      {        "type": "email",        "value": "[[email protected]](/cdn-cgi/l/email-protection)"      },      {        "type": "external_id",        "value": "0987654321"      },      {        "type": "phone_number",        "value": "+612345678"      }    ],    "name": "Jane Smith",    "source": "company",    "type": "contact",    "updated_at": "2020-02-03T01:37:16Z",    "user_id": "123456"  }}

**400 Bad Request**


    // Status 400 Bad Request
    {  "errors": [    {      "code": "ClientError",      "id": "10001",      "title": "Some client caused error"    }  ]}

**403 Forbidden**


    // Status 403 Forbidden
    {  "errors": [    {      "code": "ClientError",      "id": "10001",      "title": "Some client caused error"    }  ]}

### Update Profile by Profile ID

  * `PUT /api/v2/user_profiles/{profile_id}`


Updates a profile specified by a profile ID. If the profile has more than one identifier, all the identifiers should belong to a single user and a single profile. When identifiers for multiple users are provided, the request fails.

Note that the source 'zendesk' is reserved and cannot be used to create a profile.

#### Allowed For

  * Agents


Access also depends on agent role permissions set in **Support** > **People** > **Roles** > **People**.

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
profile_id| string| Path| true| Sunshine profile ID

#### Example body


    {  "profile": {    "attributes": {      "membership": "gold"    },    "identifiers": [      {        "type": "email",        "value": "[[email protected]](/cdn-cgi/l/email-protection)"      },      {        "type": "external_id",        "value": "0987654321"      },      {        "type": "phone_number",        "value": "+612345678"      }    ],    "name": "Jane Smith"  }}

#### Code Samples

**curl**


    curl "https://{subdomain}.zendesk.com/api/v2/user_profiles/{profile_id}" \  -d '{"profile":{"name":"JaneSmith","source":"company","type":"contact","user_id":123456,"identifiers":[{"type":"email","value":"[[email protected]](/cdn-cgi/l/email-protection)"},{"type":"phone_number","value":"+612345678"}],"attributes":{"membership":"gold"}}}' \  -H "Content-Type: application/json" \  -X PUT \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://support.zendesk.com/api/v2/user_profiles/"	method := "PUT"	payload := strings.NewReader(`{  "profile": {    "attributes": {      "membership": "gold"    },    "identifiers": [      {        "type": "email",        "value": "[[email protected]](/cdn-cgi/l/email-protection)"      },      {        "type": "external_id",        "value": "0987654321"      },      {        "type": "phone_number",        "value": "+612345678"      }    ],    "name": "Jane Smith"  }}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/user_profiles/")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"profile\": {    \"attributes\": {      \"membership\": \"gold\"    },    \"identifiers\": [      {        \"type\": \"email\",        \"value\": \"jane@example.com\"      },      {        \"type\": \"external_id\",        \"value\": \"0987654321\"      },      {        \"type\": \"phone_number\",        \"value\": \"+612345678\"      }    ],    \"name\": \"Jane Smith\"  }}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "profile": {    "attributes": {      "membership": "gold"    },    "identifiers": [      {        "type": "email",        "value": "[[email protected]](/cdn-cgi/l/email-protection)"      },      {        "type": "external_id",        "value": "0987654321"      },      {        "type": "phone_number",        "value": "+612345678"      }    ],    "name": "Jane Smith"  }});
    var config = {  method: 'PUT',  url: 'https://support.zendesk.com/api/v2/user_profiles/',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/user_profiles/"
    payload = json.loads("""{  "profile": {    "attributes": {      "membership": "gold"    },    "identifiers": [      {        "type": "email",        "value": "[[email protected]](/cdn-cgi/l/email-protection)"      },      {        "type": "external_id",        "value": "0987654321"      },      {        "type": "phone_number",        "value": "+612345678"      }    ],    "name": "Jane Smith"  }}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/user_profiles/")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")request.body = %q({  "profile": {    "attributes": {      "membership": "gold"    },    "identifiers": [      {        "type": "email",        "value": "[[email protected]](/cdn-cgi/l/email-protection)"      },      {        "type": "external_id",        "value": "0987654321"      },      {        "type": "phone_number",        "value": "+612345678"      }    ],    "name": "Jane Smith"  }})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "profile": {    "attributes": {      "membership": "gold"    },    "created_at": "2020-02-03T01:37:16Z",    "id": "01ARZ3NDEKTSV4RRFFQ69G5FAV",    "identifiers": [      {        "type": "email",        "value": "[[email protected]](/cdn-cgi/l/email-protection)"      },      {        "type": "external_id",        "value": "0987654321"      },      {        "type": "phone_number",        "value": "+612345678"      }    ],    "name": "Jane Smith",    "source": "company",    "type": "contact",    "updated_at": "2020-02-03T01:37:16Z",    "user_id": "123456"  }}

**400 Bad Request**


    // Status 400 Bad Request
    {  "errors": [    {      "code": "ClientError",      "id": "10001",      "title": "Some client caused error"    }  ]}

**403 Forbidden**


    // Status 403 Forbidden
    {  "errors": [    {      "code": "ClientError",      "id": "10001",      "title": "Some client caused error"    }  ]}

**404 Not Found**


    // Status 404 Not Found
    {  "errors": [    {      "code": "ClientError",      "id": "10001",      "title": "Some client caused error"    }  ]}

### Partial Update Profile by Profile ID

  * `PATCH /api/v2/user_profiles/{profile_id}`


Partially updates of a profile with profile ID using a JSON merge patch. See [Patching a profile](/documentation/ticketing/profiles/updating-profiles/#patching-a-profile).

If the profile has more than one identifier, all the identifiers should belong to a single user and a single profile. When identifiers for multiple users are provided, the request fails.

#### Allowed For

  * Agents


Access also depends on agent role permissions set in **Support** > **People** > **Roles** > **People**.

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
profile_id| string| Path| true| Sunshine profile ID

#### Example body


    {  "profile": {    "attributes": {      "membership": "gold"    },    "identifiers": [      {        "type": "email",        "value": "[[email protected]](/cdn-cgi/l/email-protection)"      },      {        "type": "external_id",        "value": "0987654321"      },      {        "type": "phone_number",        "value": "+612345678"      }    ],    "name": "Jane Smith"  }}

#### Code Samples

**curl**


    curl "https://{subdomain}.zendesk.com/api/v2/user_profiles/{profile_id}" \  -d '{"profile":{"name":"Jane Smith","source":"company","type":"contact","user_id":123456,"identifiers":[{"type":"email","value":"[[email protected]](/cdn-cgi/l/email-protection)"},{"type":"external_id","value":"0987654321"},{"type":"phone_number","value":"+612345678"}],"attributes":{"membership":"gold"}}}' \  -H "Content-Type: application/json" \  -X PATCH \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://support.zendesk.com/api/v2/user_profiles/"	method := "PATCH"	payload := strings.NewReader(`{  "profile": {    "attributes": {      "membership": "gold"    },    "identifiers": [      {        "type": "email",        "value": "[[email protected]](/cdn-cgi/l/email-protection)"      },      {        "type": "external_id",        "value": "0987654321"      },      {        "type": "phone_number",        "value": "+612345678"      }    ],    "name": "Jane Smith"  }}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/user_profiles/")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"profile\": {    \"attributes\": {      \"membership\": \"gold\"    },    \"identifiers\": [      {        \"type\": \"email\",        \"value\": \"jane@example.com\"      },      {        \"type\": \"external_id\",        \"value\": \"0987654321\"      },      {        \"type\": \"phone_number\",        \"value\": \"+612345678\"      }    ],    \"name\": \"Jane Smith\"  }}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PATCH", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "profile": {    "attributes": {      "membership": "gold"    },    "identifiers": [      {        "type": "email",        "value": "[[email protected]](/cdn-cgi/l/email-protection)"      },      {        "type": "external_id",        "value": "0987654321"      },      {        "type": "phone_number",        "value": "+612345678"      }    ],    "name": "Jane Smith"  }});
    var config = {  method: 'PATCH',  url: 'https://support.zendesk.com/api/v2/user_profiles/',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/user_profiles/"
    payload = json.loads("""{  "profile": {    "attributes": {      "membership": "gold"    },    "identifiers": [      {        "type": "email",        "value": "[[email protected]](/cdn-cgi/l/email-protection)"      },      {        "type": "external_id",        "value": "0987654321"      },      {        "type": "phone_number",        "value": "+612345678"      }    ],    "name": "Jane Smith"  }}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PATCH",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/user_profiles/")request = Net::HTTP::Patch.new(uri, "Content-Type": "application/json")request.body = %q({  "profile": {    "attributes": {      "membership": "gold"    },    "identifiers": [      {        "type": "email",        "value": "[[email protected]](/cdn-cgi/l/email-protection)"      },      {        "type": "external_id",        "value": "0987654321"      },      {        "type": "phone_number",        "value": "+612345678"      }    ],    "name": "Jane Smith"  }})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "profile": {    "attributes": {      "membership": "gold"    },    "created_at": "2020-02-03T01:37:16Z",    "id": "01ARZ3NDEKTSV4RRFFQ69G5FAV",    "identifiers": [      {        "type": "email",        "value": "[[email protected]](/cdn-cgi/l/email-protection)"      },      {        "type": "external_id",        "value": "0987654321"      },      {        "type": "phone_number",        "value": "+612345678"      }    ],    "name": "Jane Smith",    "source": "company",    "type": "contact",    "updated_at": "2020-02-03T01:37:16Z",    "user_id": "123456"  }}

**400 Bad Request**


    // Status 400 Bad Request
    {  "errors": [    {      "code": "ClientError",      "id": "10001",      "title": "Some client caused error"    }  ]}

**403 Forbidden**


    // Status 403 Forbidden
    {  "errors": [    {      "code": "ClientError",      "id": "10001",      "title": "Some client caused error"    }  ]}

### Partial Update Profile by Identifier

  * `PATCH /api/v2/user_profiles?identifier={identifier}`


Partially updates the specified profile. See [Patching a profile](/documentation/ticketing/profiles/updating-profiles/#patching-a-profile).

The required `identifier` path parameter takes an identifier query. See [Using identifier queries with profiles](/documentation/ticketing/profiles/using-identifier-queries-with-profiles/).

If the profile has more than one identifier, all the identifiers should belong to a single user and a single profile.

When identifiers for multiple users are provided, the request fails.

Note that the source 'zendesk' is reserved and cannot be used to create a profile.

#### Allowed For

  * Agents


Access also depends on agent role permissions set in **Support** > **People** > **Roles** > **People**.

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
identifier| string| Query| true| An identifier query to identify the profile. Uses the format of source:type:identifier_type:identifier_value

#### Example body


    {  "profile": {    "attributes": {      "membership": "gold"    },    "identifiers": [      {        "type": "email",        "value": "[[email protected]](/cdn-cgi/l/email-protection)"      },      {        "type": "external_id",        "value": "0987654321"      },      {        "type": "phone_number",        "value": "+612345678"      }    ],    "name": "Jane Smith"  }}

#### Code Samples

**curl**


    curl  "https://{subdomain}.zendesk.com/api/v2/user_profiles?identifier=company:contact:email:[[email protected]](/cdn-cgi/l/email-protection)" \  -d '{"profile":{"name":"JaneSmith","source":"company","type":"contact","user_id":123456,"identifiers":[{"type":"email","value":"[[email protected]](/cdn-cgi/l/email-protection)"},{"type":"external_id","value":"0987654321"},{"type":"phone_number","value":"+612345678"}],"attributes":{"membership":"gold"}}}' \  -H "Content-Type: application/json" \  -X PATCH \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://support.zendesk.com/api/v2/user_profiles?identifier=shoppingnow%3Acustomer%3Aemail%3Aexample%40example.com"	method := "PATCH"	payload := strings.NewReader(`{  "profile": {    "attributes": {      "membership": "gold"    },    "identifiers": [      {        "type": "email",        "value": "[[email protected]](/cdn-cgi/l/email-protection)"      },      {        "type": "external_id",        "value": "0987654321"      },      {        "type": "phone_number",        "value": "+612345678"      }    ],    "name": "Jane Smith"  }}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/user_profiles")		.newBuilder()		.addQueryParameter("identifier", "shoppingnow:customer:email:[[email protected]](/cdn-cgi/l/email-protection)");RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"profile\": {    \"attributes\": {      \"membership\": \"gold\"    },    \"identifiers\": [      {        \"type\": \"email\",        \"value\": \"jane@example.com\"      },      {        \"type\": \"external_id\",        \"value\": \"0987654321\"      },      {        \"type\": \"phone_number\",        \"value\": \"+612345678\"      }    ],    \"name\": \"Jane Smith\"  }}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PATCH", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "profile": {    "attributes": {      "membership": "gold"    },    "identifiers": [      {        "type": "email",        "value": "[[email protected]](/cdn-cgi/l/email-protection)"      },      {        "type": "external_id",        "value": "0987654321"      },      {        "type": "phone_number",        "value": "+612345678"      }    ],    "name": "Jane Smith"  }});
    var config = {  method: 'PATCH',  url: 'https://support.zendesk.com/api/v2/user_profiles',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'identifier': 'shoppingnow%3Acustomer%3Aemail%3Aexample%40example.com',  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/user_profiles?identifier=shoppingnow%3Acustomer%3Aemail%3Aexample%40example.com"
    payload = json.loads("""{  "profile": {    "attributes": {      "membership": "gold"    },    "identifiers": [      {        "type": "email",        "value": "[[email protected]](/cdn-cgi/l/email-protection)"      },      {        "type": "external_id",        "value": "0987654321"      },      {        "type": "phone_number",        "value": "+612345678"      }    ],    "name": "Jane Smith"  }}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PATCH",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/user_profiles")uri.query = URI.encode_www_form("identifier": "shoppingnow:customer:email:[[email protected]](/cdn-cgi/l/email-protection)")request = Net::HTTP::Patch.new(uri, "Content-Type": "application/json")request.body = %q({  "profile": {    "attributes": {      "membership": "gold"    },    "identifiers": [      {        "type": "email",        "value": "[[email protected]](/cdn-cgi/l/email-protection)"      },      {        "type": "external_id",        "value": "0987654321"      },      {        "type": "phone_number",        "value": "+612345678"      }    ],    "name": "Jane Smith"  }})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "profile": {    "attributes": {      "membership": "gold"    },    "created_at": "2020-02-03T01:37:16Z",    "id": "01ARZ3NDEKTSV4RRFFQ69G5FAV",    "identifiers": [      {        "type": "email",        "value": "[[email protected]](/cdn-cgi/l/email-protection)"      },      {        "type": "external_id",        "value": "0987654321"      },      {        "type": "phone_number",        "value": "+612345678"      }    ],    "name": "Jane Smith",    "source": "company",    "type": "contact",    "updated_at": "2020-02-03T01:37:16Z",    "user_id": "123456"  }}

**400 Bad Request**


    // Status 400 Bad Request
    {  "errors": [    {      "code": "ClientError",      "id": "10001",      "title": "Some client caused error"    }  ]}

**403 Forbidden**


    // Status 403 Forbidden
    {  "errors": [    {      "code": "ClientError",      "id": "10001",      "title": "Some client caused error"    }  ]}

### Delete Profile by Profile ID

  * `DELETE /api/v2/user_profiles/{profile_id}`


Deletes the profile specified by the profile ID.

#### Allowed For

  * Agents


Access also depends on agent role permissions set in **Support** > **People** > **Roles** > **People**.

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
profile_id| string| Path| true| Sunshine profile ID

#### Code Samples

**curl**


    curl "https://{subdomain}.zendesk.com/api/v2/user_profiles/{profile_id}" \  -X DELETE \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/user_profiles/"	method := "DELETE"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/user_profiles/")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("DELETE", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'DELETE',  url: 'https://support.zendesk.com/api/v2/user_profiles/',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/user_profiles/"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"DELETE",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/user_profiles/")request = Net::HTTP::Delete.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**204 No Content**


    // Status 204 No Content
    null

**400 Bad Request**


    // Status 400 Bad Request
    {  "errors": [    {      "code": "ClientError",      "id": "10001",      "title": "Some client caused error"    }  ]}

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)