# User Segments

*Source: https://developer.zendesk.com/api-reference/help_center/help-center-api/user_segments/*

---

## On this page

  * [JSON format](/api-reference/help_center/help-center-api/user_segments/#json-format)
  * [List User Segments](/api-reference/help_center/help-center-api/user_segments/#list-user-segments)
  * [Show User Segment](/api-reference/help_center/help-center-api/user_segments/#show-user-segment)
  * [Create User Segment](/api-reference/help_center/help-center-api/user_segments/#create-user-segment)
  * [Update User Segment](/api-reference/help_center/help-center-api/user_segments/#update-user-segment)
  * [Delete User Segment](/api-reference/help_center/help-center-api/user_segments/#delete-user-segment)
  * [List Sections with User Segment](/api-reference/help_center/help-center-api/user_segments/#list-sections-with-user-segment)
  * [List Topics with User Segment](/api-reference/help_center/help-center-api/user_segments/#list-topics-with-user-segment)
  * [List Applicable User Segments](/api-reference/help_center/help-center-api/user_segments/#list-applicable-user-segments)
  * [List User Segments by User](/api-reference/help_center/help-center-api/user_segments/#list-user-segments-by-user)


# User Segments

## On this page

  * [JSON format](/api-reference/help_center/help-center-api/user_segments/#json-format)
  * [List User Segments](/api-reference/help_center/help-center-api/user_segments/#list-user-segments)
  * [Show User Segment](/api-reference/help_center/help-center-api/user_segments/#show-user-segment)
  * [Create User Segment](/api-reference/help_center/help-center-api/user_segments/#create-user-segment)
  * [Update User Segment](/api-reference/help_center/help-center-api/user_segments/#update-user-segment)
  * [Delete User Segment](/api-reference/help_center/help-center-api/user_segments/#delete-user-segment)
  * [List Sections with User Segment](/api-reference/help_center/help-center-api/user_segments/#list-sections-with-user-segment)
  * [List Topics with User Segment](/api-reference/help_center/help-center-api/user_segments/#list-topics-with-user-segment)
  * [List Applicable User Segments](/api-reference/help_center/help-center-api/user_segments/#list-applicable-user-segments)
  * [List User Segments by User](/api-reference/help_center/help-center-api/user_segments/#list-user-segments-by-user)


A user segment defines who can view the content of a section or topic. It can specify any of the following access restrictions:

  * `signed_in_users` or `staff` user types
  * [tags](/api-reference/ticketing/ticket-management/tags/)
  * [organization ids](/api-reference/ticketing/organizations/organizations/) (for signed in users)
  * [group ids](/api-reference/ticketing/groups/groups/) (for staff)


You can use this API to define or change the access restrictions of user segments. To apply user segments to content, use the [Articles](/api-reference/help_center/help-center-api/articles/) or [Topics](/api-reference/help_center/help-center-api/topics) API and set the `user_segment_id` property.

For articles, users on Enterprise plans may specify an array of ids in the `user_segment_ids` property instead. Articles can then be accessed by users with any of the user segment ids in the array.

### JSON format

User Segments are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
added_user_ids| array| false| false| The ids of users added specifically to this user segment, regardless of matching tags or other criteria
built_in| boolean| true| false| Whether the user segment is built-in. Built-in user segments cannot be modified
created_at| string| true| false| When the user segment was created
group_ids| array| false| false| The ids of the groups that have access
id| integer| true| false| Automatically assigned when the user segment is created
name| string| false| false| User segment name (localized to the locale of the current user for built-in user segments)
or_tags| array| false| false| A user must have at least one tag in the list to have access
organization_ids| array| false| false| The ids of the organizations that have access
tags| array| false| false| All the tags a user must have to have access
updated_at| string| true| false| When the user segment was last updated
user_type| string| false| true| The set of users who can view content

The `user_type` attribute takes one of the following values:

Value| Users
---|---
signed_in_users| only authenticated users
staff| only agents and Help Center managers

For `group_ids`, `organization_ids`, `tags`, and `or_tags`, an empty array means that access is not restricted by the attribute. For example, if no group ids are specified, then users don't have to be in any specific group to have access.

For `tags`, a user must have all the listed tags to have access. For `or_tags`, a user must have at least one of the listed tags to have access.

#### Example


    {  "built_in": false,  "created_at": "2017-07-20T22:55:29Z",  "group_ids": [    12  ],  "name": "VIP agents",  "organization_ids": [    42  ],  "tags": [    "vip"  ],  "updated_at": "2017-07-23T21:43:28Z",  "user_type": "staff"}

### List User Segments

  * `GET /api/v2/help_center/user_segments`


Some user segments can only be applied to sections and topics on certain Guide plans. For instance, user segments with a `user_type` of `"staff"` cannot be applied to sections and topics on accounts on the Guide Lite plan or the Suite Team plan. To request only user segments applicable on the account's current Suite plan, use the `/api/v2/help_center/user_segments/applicable.json` endpoint.

The `/api/v2/help_center/users/{user_id}/user_segments.json` endpoint returns the list of user segments that a particular user belongs to. This is the only list endpoint that agents have access to. When an agent makes a request to this endpoint with another user's id, the response only includes user segments that the requesting agent also belongs to.

These endpoints support pagination, as described in the [pagination documentation](/api-reference/introduction/pagination/).

#### Allowed for

  * Help Center managers
  * Agents


#### Pagination

  * Cursor pagination (recommended)
  * Offset pagination


See [Pagination](/api-reference/introduction/pagination/).

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
built_in| boolean| Query| false| Only built_in user segments if true, only custom user segments if false

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/user_segments.json \  -v -u {email_address}/token:{api_token}
    # Requesting only applicable user segments:curl https://{subdomain}.zendesk.com/api/v2/help_center/user_segments/applicable.json \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/user_segments?built_in="	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/user_segments")		.newBuilder()		.addQueryParameter("built_in", "");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/help_center/user_segments',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'built_in': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/user_segments?built_in="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/user_segments")uri.query = URI.encode_www_form("built_in": "")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "user_segments": [    {      "built_in": false,      "created_at": "2017-05-21T20:01:12Z",      "group_ids": [        12      ],      "id": 7284,      "name": "VIP agents",      "or_tags": [],      "organization_ids": [],      "tags": [        "vip"      ],      "updated_at": "2017-06-30T01:00:25Z",      "user_type": "staff"    },    {      "built_in": false,      "created_at": "2017-04-09T15:33:11Z",      "group_ids": [],      "id": 9930,      "name": "Privileged users",      "or_tags": [],      "organization_ids": [        42      ],      "tags": [],      "updated_at": "2017-08-10T18:41:01Z",      "user_type": "signed_in_users"    }  ]}

### Show User Segment

  * `GET /api/v2/help_center/user_segments/{user_segment_id}`


#### Allowed for

  * Help Center managers


#### Pagination

  * Cursor pagination (recommended)
  * Offset pagination


See [Pagination](/api-reference/introduction/pagination/).

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
user_segment_id| integer| Path| true| The unique ID of the user segment

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/user_segments/{user_segment_id}.json \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/user_segments/1234"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/user_segments/1234")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/help_center/user_segments/1234',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/user_segments/1234"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/user_segments/1234")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "user_segment": {    "built_in": false,    "created_at": "2017-05-21T20:01:12Z",    "group_ids": [      12    ],    "id": 7284,    "name": "VIP agents",    "or_tags": [],    "organization_ids": [],    "tags": [      "vip"    ],    "updated_at": "2017-05-21T20:01:12Z",    "user_type": "staff"  }}

### Create User Segment

  * `POST /api/v2/help_center/user_segments`


#### Allowed for

  * Help Center managers


#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/user_segments.json \  -d '{ \    "user_segment": { \      "name": "VIP agents", \      "user_type": "staff", \      "group_ids": [12, ...], \      "tags": ["vip"] \    } \  }' \  -v -u {email_address}/token:{api_token} -X POST -H "Content-Type: application/json"

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/user_segments"	method := "POST"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/user_segments")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'POST',  url: 'https://support.zendesk.com/api/v2/help_center/user_segments',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/user_segments"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/user_segments")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**201 Created**


    // Status 201 Created
    {  "user_segment": {    "built_in": false,    "created_at": "2017-05-21T20:01:12Z",    "group_ids": [      12    ],    "id": 7284,    "name": "VIP agents",    "or_tags": [],    "organization_ids": [],    "tags": [      "vip"    ],    "updated_at": "2017-05-21T20:01:12Z",    "user_type": "staff"  }}

**400 Bad Request**


    // Status 400 Bad Request
    {  "errors": {    "user_type": [      "value `foo` invalid; must be either `staff` or `signed_in_users`"    ]  }}

### Update User Segment

  * `PUT /api/v2/help_center/user_segments/{user_segment_id}`


#### Allowed for

  * Help Center managers


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
user_segment_id| integer| Path| true| The unique ID of the user segment

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/user_segments/{user_segment_id}.json \  -d '{ \    "user_segment": { \      "name": "VIP agents", \      "user_type": "staff", \      "group_ids": [12, ...], \      "organization_ids": [42, ...], \      "tags": ["vip"] \    } \  }' \  -v -u {email_address}/token:{api_token} -X PUT -H "Content-Type: application/json"

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/user_segments/1234"	method := "PUT"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/user_segments/1234")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'PUT',  url: 'https://support.zendesk.com/api/v2/help_center/user_segments/1234',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/user_segments/1234"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/user_segments/1234")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "user_segment": {    "built_in": false,    "created_at": "2017-05-21T20:01:12Z",    "group_ids": [      12    ],    "id": 7284,    "name": "VIP agents",    "or_tags": [],    "organization_ids": [],    "tags": [      "vip"    ],    "updated_at": "2017-05-21T20:01:12Z",    "user_type": "staff"  }}

**400 Bad Request**


    // Status 400 Bad Request
    {  "errors": {    "user_type": [      "value `foo` invalid; must be either `staff` or `signed_in_users`"    ]  }}

### Delete User Segment

  * `DELETE /api/v2/help_center/user_segments/{user_segment_id}`


#### Allowed for

  * Help Center managers


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
user_segment_id| integer| Path| true| The unique ID of the user segment

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/user_segments/{user_segment_id}.json \  -v -u {email_address}/token:{api_token} -X DELETE

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/user_segments/1234"	method := "DELETE"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/user_segments/1234")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("DELETE", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'DELETE',  url: 'https://support.zendesk.com/api/v2/help_center/user_segments/1234',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/user_segments/1234"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"DELETE",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/user_segments/1234")request = Net::HTTP::Delete.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**204 No Content**


    // Status 204 No Content
    null

### List Sections with User Segment

  * `GET /api/v2/help_center/user_segments/{user_segment_id}/sections`


Lists the sections that use the specified user segment.

This endpoint supports pagination as described in [Pagination](/api-reference/help_center/help-center-api/help-center-api/#pagination).

#### Allowed for

  * Help Center managers


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
user_segment_id| integer| Path| true| The unique ID of the user segment

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/user_segments/{user_segment_id}/sections.json \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/user_segments/1234/sections"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/user_segments/1234/sections")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/help_center/user_segments/1234/sections',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/user_segments/1234/sections"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/user_segments/1234/sections")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "sections": [    {      "html_url": "https://{subdomain}.zendesk.com/hc/en/sections/3242-A-section-",      "id": 3242,      "locale": "en",      "name": "A section",      "url": "https://{subdomain}.zendesk.com/api/v2/help_center/en/sections/3242-A-section-.json"    },    {      "html_url": "https://{subdomain}.zendesk.com/hc/en/sections/7352-Another-section-",      "id": 7352,      "locale": "en",      "name": "Another section",      "url": "https://{subdomain}.zendesk.com/api/v2/help_center/en/sections/7352-Another-section-.json"    }  ]}

### List Topics with User Segment

  * `GET /api/v2/help_center/user_segments/{user_segment_id}/topics`


Lists the topics that use the specified user segment.

This endpoint supports pagination as described in [Pagination](/api-reference/help_center/help-center-api/help-center-api/#pagination).

#### Allowed for

  * Help Center managers


#### Pagination

  * Cursor pagination (recommended)
  * Offset pagination


See [Pagination](/api-reference/introduction/pagination/).

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
user_segment_id| integer| Path| true| The unique ID of the user segment

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/user_segments/{user_segment_id}/topics.json \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/user_segments/1234/topics"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/user_segments/1234/topics")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/help_center/user_segments/1234/topics',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/user_segments/1234/topics"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/user_segments/1234/topics")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "topics": [    {      "html_url": "https://{subdomain}.zendesk.com/hc/en/community/topics/9273-A-topic-",      "id": 9273,      "name": "A topic",      "url": "https://{subdomain}.zendesk.com/api/v2/community/topics/9273.json"    },    {      "html_url": "https://{subdomain}.zendesk.com/hc/en/community/topics/2292-Another-topic-",      "id": 2292,      "name": "Another topic",      "url": "https://{subdomain}.zendesk.com/api/v2/community/topics/2292-Another-topic-.json"    }  ]}

### List Applicable User Segments

  * `GET /api/v2/help_center/user_segments/applicable`


Some user segments can only be applied to sections and topics on certain Guide plans. For instance, user segments with a `user_type` of `"staff"` cannot be applied to sections and topics on accounts on the Guide Lite plan or the Suite Team plan. To request only user segments applicable on the account's current Suite plan, use the `/api/v2/help_center/user_segments/applicable.json` endpoint.

The `/api/v2/help_center/users/{user_id}/user_segments.json` endpoint returns the list of user segments that a particular user belongs to. This is the only list endpoint that agents have access to. When an agent makes a request to this endpoint with another user's id, the response only includes user segments that the requesting agent also belongs to.

These endpoints support pagination, as described in the [pagination documentation](/api-reference/introduction/pagination/).

#### Allowed for

  * Help Center managers
  * Agents


#### Pagination

  * Cursor pagination (recommended)
  * Offset pagination


See [Pagination](/api-reference/introduction/pagination/).

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
built_in| boolean| Query| false| Only built_in user segments if true, only custom user segments if false

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/user_segments.json \  -v -u {email_address}/token:{api_token}
    # Requesting only applicable user segments:curl https://{subdomain}.zendesk.com/api/v2/help_center/user_segments/applicable.json \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/user_segments/applicable?built_in="	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/user_segments/applicable")		.newBuilder()		.addQueryParameter("built_in", "");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/help_center/user_segments/applicable',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'built_in': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/user_segments/applicable?built_in="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/user_segments/applicable")uri.query = URI.encode_www_form("built_in": "")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "user_segments": [    {      "built_in": false,      "created_at": "2017-05-21T20:01:12Z",      "group_ids": [        12      ],      "id": 7284,      "name": "VIP agents",      "or_tags": [],      "organization_ids": [],      "tags": [        "vip"      ],      "updated_at": "2017-06-30T01:00:25Z",      "user_type": "staff"    },    {      "built_in": false,      "created_at": "2017-04-09T15:33:11Z",      "group_ids": [],      "id": 9930,      "name": "Privileged users",      "or_tags": [],      "organization_ids": [        42      ],      "tags": [],      "updated_at": "2017-08-10T18:41:01Z",      "user_type": "signed_in_users"    }  ]}

### List User Segments by User

  * `GET /api/v2/help_center/users/{user_id}/user_segments`


Some user segments can only be applied to sections and topics on certain Guide plans. For instance, user segments with a `user_type` of `"staff"` cannot be applied to sections and topics on accounts on the Guide Lite plan or the Suite Team plan. To request only user segments applicable on the account's current Suite plan, use the `/api/v2/help_center/user_segments/applicable.json` endpoint.

The `/api/v2/help_center/users/{user_id}/user_segments` endpoint returns the list of user segments that a particular user belongs to. This is the only list endpoint that agents have access to. When an agent makes a request to this endpoint with another user's id, the response only includes user segments that the requesting agent also belongs to.

These endpoints support pagination, as described in the [pagination documentation](/api-reference/introduction/pagination/).

#### Allowed for

  * Help Center managers
  * Agents


#### Pagination

  * Cursor pagination (recommended)
  * Offset pagination


See [Pagination](/api-reference/introduction/pagination/).

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
built_in| boolean| Query| false| Only built_in user segments if true, only custom user segments if false
user_id| integer| Path| true| The unique ID of the user

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/users/{user_id}/user_segments \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/users/1234/user_segments?built_in="	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/users/1234/user_segments")		.newBuilder()		.addQueryParameter("built_in", "");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/help_center/users/1234/user_segments',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'built_in': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/users/1234/user_segments?built_in="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/users/1234/user_segments")uri.query = URI.encode_www_form("built_in": "")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "user_segments": [    {      "built_in": false,      "created_at": "2017-05-21T20:01:12Z",      "group_ids": [        12      ],      "id": 7284,      "name": "VIP agents",      "or_tags": [],      "organization_ids": [],      "tags": [        "vip"      ],      "updated_at": "2017-06-30T01:00:25Z",      "user_type": "staff"    },    {      "built_in": false,      "created_at": "2017-04-09T15:33:11Z",      "group_ids": [],      "id": 9930,      "name": "Privileged users",      "or_tags": [],      "organization_ids": [        42      ],      "tags": [],      "updated_at": "2017-08-10T18:41:01Z",      "user_type": "signed_in_users"    }  ]}

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)