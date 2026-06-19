# Ticket Activities

*Source: https://developer.zendesk.com/api-reference/ticketing/tickets/activity_stream/*

---

## On this page

  * [JSON format](/api-reference/ticketing/tickets/activity_stream/#json-format)
  * [List Activities](/api-reference/ticketing/tickets/activity_stream/#list-activities)
  * [Count Activities](/api-reference/ticketing/tickets/activity_stream/#count-activities)
  * [Show Activity](/api-reference/ticketing/tickets/activity_stream/#show-activity)


# Ticket Activities

## On this page

  * [JSON format](/api-reference/ticketing/tickets/activity_stream/#json-format)
  * [List Activities](/api-reference/ticketing/tickets/activity_stream/#list-activities)
  * [Count Activities](/api-reference/ticketing/tickets/activity_stream/#count-activities)
  * [Show Activity](/api-reference/ticketing/tickets/activity_stream/#show-activity)


The Ticket Activities API returns ticket activities by other people affecting the agent making the API request. Ticket activities include assigning a ticket to the agent, increasing the priority of a ticket assigned to the agent, or adding a comment to a ticket assigned to the agent. A possible use case for the API is building a personalized notification service for agents.

### JSON format

Ticket Activities are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
actor| object| true| false| The full user record of the user responsible for the ticket activity. See [Users](/api-reference/ticketing/users/users/)
actor_id| integer| true| false| The id of the user responsible for the ticket activity. An `actor_id` of "-1" is a Zendesk system user, such as an automations action.
created_at| string| true| false| When the record was created
id| integer| true| false| Automatically assigned on creation
object| object| true| false| The content of the activity. Can be a ticket, comment, or change.
target| object| true| false| The target of the activity, a ticket.
title| string| true| false| Description of the activity
updated_at| string| true| false| When the record was last updated
url| string| true| false| The API url of the activity
user| object| true| false| The full user record of the agent making the request. See [Users](/api-reference/ticketing/users/users/)
user_id| integer| true| false| The id of the agent making the request
verb| string| true| false| The type of activity. Can be "tickets.assignment", "tickets.comment", or "tickets.priority_increase"

#### Example


    {  "actor": {    "id": 8678530,    "name": "James A. Rosen"  },  "actor_id": 23546,  "created_at": "2019-03-05T10:38:52Z",  "id": 35,  "object": {},  "target": {},  "title": "John Hopeful assigned ticket #123 to you",  "updated_at": "2019-03-05T10:38:52Z",  "url": "https://company.zendesk.com/api/v2/activities/35",  "user": {    "id": 223443,    "name": "Johnny Agent"  },  "user_id": 29451,  "verb": "tickets.assignment"}

### List Activities

  * `GET /api/v2/activities`


Lists ticket activities in the last 30 days affecting the agent making the request. Also sideloads the following arrays of user records:

  * actors - All actors involved in the listed activities
  * users - All users involved in the listed activities


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
include| string| Query| false| A comma-separated list of sideloads to include. Supported values: `fields_metadata`.
page| | Query| false| Pagination parameter. Supports both traditional offset and cursor-based pagination: - Traditional: `?page=2` (integer page number) - Cursor: `?page[size]=50&page[after]=cursor` (deepObject with size, after, before) These are mutually exclusive - use one format or the other, not both.
per_page| integer| Query| false| Number of records to return per page. Note: Default and maximum values vary by endpoint. Check endpoint-specific documentation for limits.
since| string| Query| false| A UTC time in ISO 8601 format to return ticket activities since said date.
sort| string| Query| false| Field to sort results by. Prefix with `-` for descending order. When used with cursor pagination, this determines the cursor ordering. Example: `?sort=name` or `?sort=-created_at`

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/activities \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/activities?include=fields_metadata&page=&per_page=50&since=2013-04-03T16%3A02%3A46Z&sort=name"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/activities")		.newBuilder()		.addQueryParameter("include", "fields_metadata")		.addQueryParameter("page", "")		.addQueryParameter("per_page", "50")		.addQueryParameter("since", "2013-04-03T16:02:46Z")		.addQueryParameter("sort", "name");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/activities',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'include': 'fields_metadata',    'page': '',    'per_page': '50',    'since': '2013-04-03T16%3A02%3A46Z',    'sort': 'name',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/activities?include=fields_metadata&page=&per_page=50&since=2013-04-03T16%3A02%3A46Z&sort=name"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/activities")uri.query = URI.encode_www_form("include": "fields_metadata", "page": "", "per_page": "50", "since": "2013-04-03T16:02:46Z", "sort": "name")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "activities": [    {      "actor": {        "active": true,        "alias": "",        "created_at": "2020-11-17T00:32:12Z",        "custom_role_id": null,        "default_group_id": 1873,        "details": "",        "email": "[[email protected]](/cdn-cgi/l/email-protection)",        "external_id": null,        "iana_time_zone": "America/Juneau",        "id": 158488612,        "last_login_at": "2020-11-17T00:33:44Z",        "locale": "en-gb",        "locale_id": 5,        "moderator": true,        "name": "Tedd",        "notes": "",        "only_private_comments": false,        "organization_id": null,        "phone": null,        "photo": null,        "report_csv": true,        "restricted_agent": false,        "role": "admin",        "role_type": null,        "shared": false,        "shared_agent": false,        "shared_phone_number": null,        "signature": "",        "suspended": false,        "tags": [],        "ticket_restriction": null,        "time_zone": "Alaska",        "two_factor_auth_enabled": null,        "updated_at": "2020-11-17T00:34:38Z",        "url": "https://example.zendesk.com/api/v2/users/158488612",        "user_fields": {          "its_remember_september": null,          "skittles": null,          "user_field_1": null        },        "verified": true      },      "actor_id": 158488612,      "created_at": "2020-11-17T00:34:40Z",      "id": 29183462,      "object": {        "ticket": {          "id": 1521,          "subject": "test"        }      },      "target": {        "ticket": {          "id": 1521,          "subject": "test"        }      },      "title": "Tedd assigned ticket #1521 to you.",      "updated_at": "2020-11-17T00:34:40Z",      "url": "https://example.zendesk.com/api/v2/activities/29183462",      "user": {        "active": true,        "alias": "test",        "created_at": "2017-08-14T20:13:53Z",        "custom_role_id": null,        "default_group_id": 1873,        "details": "",        "email": "[[email protected]](/cdn-cgi/l/email-protection)",        "external_id": "oev7jj",        "iana_time_zone": "Pacific/Pago_Pago",        "id": 3343,        "last_login_at": "2020-11-16T22:57:45Z",        "locale": "en-gb",        "locale_id": 5,        "moderator": true,        "name": "Samwise Gamgee",        "notes": "test",        "only_private_comments": false,        "organization_id": 1873,        "phone": null,        "photo": {          "content_type": "image/gif",          "content_url": "https://example.zendesk.com/system/photos/8730791/1f84950b8d7949b3.gif",          "deleted": false,          "file_name": "1f84950b8d7949b3.gif",          "height": 80,          "id": 8730791,          "inline": false,          "mapped_content_url": "https://example.zendesk.com/system/photos/8730791/1f84950b8d7949b3.gif",          "size": 4566,          "thumbnails": [            {              "content_type": "image/gif",              "content_url": "https://example.zendesk.com/system/photos/8730801/1f84950b8d7949b3_thumb.gif",              "deleted": false,              "file_name": "1f84950b8d7949b3_thumb.gif",              "height": 32,              "id": 8730801,              "inline": false,              "mapped_content_url": "https://example.zendesk.com/system/photos/8730801/1f84950b8d7949b3_thumb.gif",              "size": 1517,              "url": "https://example.zendesk.com/api/v2/attachments/8730801",              "width": 32            }          ],          "url": "https://example.zendesk.com/api/v2/attachments/8730791",          "width": 80        },        "report_csv": true,        "restricted_agent": false,        "role": "admin",        "role_type": null,        "shared": false,        "shared_agent": false,        "shared_phone_number": null,        "signature": "test",        "suspended": false,        "tags": [          "101"        ],        "ticket_restriction": null,        "time_zone": "American Samoa",        "two_factor_auth_enabled": null,        "updated_at": "2020-11-17T00:33:55Z",        "url": "https://example.zendesk.com/api/v2/users/3343",        "user_fields": {          "its_remember_september": null,          "skittles": "2018-09-14T00:00:00+00:00",          "user_field_1": "101"        },        "verified": true      },      "user_id": 3343,      "verb": "tickets.assignment"    }  ],  "actors": [    {      "active": true,      "alias": "",      "created_at": "2020-11-17T00:32:12Z",      "custom_role_id": null,      "default_group_id": 1873,      "details": "",      "email": "[[email protected]](/cdn-cgi/l/email-protection)",      "external_id": null,      "iana_time_zone": "America/Juneau",      "id": 158488612,      "last_login_at": "2020-11-17T00:33:44Z",      "locale": "en-gb",      "locale_id": 5,      "moderator": true,      "name": "Tedd",      "notes": "",      "only_private_comments": false,      "organization_id": null,      "phone": null,      "photo": null,      "report_csv": true,      "restricted_agent": false,      "role": "admin",      "role_type": null,      "shared": false,      "shared_agent": false,      "shared_phone_number": null,      "signature": "",      "suspended": false,      "tags": [],      "ticket_restriction": null,      "time_zone": "Alaska",      "two_factor_auth_enabled": null,      "updated_at": "2020-11-17T00:34:38Z",      "url": "https://example.zendesk.com/api/v2/users/158488612",      "user_fields": {        "its_remember_september": null,        "skittles": null,        "user_field_1": null      },      "verified": true    }  ],  "count": 1,  "next_page": null,  "previous_page": null,  "users": [    {      "active": true,      "alias": "test",      "created_at": "2017-08-14T20:13:53Z",      "custom_role_id": null,      "default_group_id": 1873,      "details": "",      "email": "[[email protected]](/cdn-cgi/l/email-protection)",      "external_id": "oev7jj",      "iana_time_zone": "Pacific/Pago_Pago",      "id": 3343,      "last_login_at": "2020-11-16T22:57:45Z",      "locale": "en-gb",      "locale_id": 5,      "moderator": true,      "name": "Samwise Gamgee",      "notes": "test",      "only_private_comments": false,      "organization_id": 1873,      "phone": null,      "photo": {        "content_type": "image/gif",        "content_url": "https://example.zendesk.com/system/photos/8730791/1f84950b8d7949b3.gif",        "deleted": false,        "file_name": "1f84950b8d7949b3.gif",        "height": 80,        "id": 8730791,        "inline": false,        "mapped_content_url": "https://example.zendesk.com/system/photos/8730791/1f84950b8d7949b3.gif",        "size": 4566,        "thumbnails": [          {            "content_type": "image/gif",            "content_url": "https://example.zendesk.com/system/photos/8730801/1f84950b8d7949b3_thumb.gif",            "deleted": false,            "file_name": "1f84950b8d7949b3_thumb.gif",            "height": 32,            "id": 8730801,            "inline": false,            "mapped_content_url": "https://example.zendesk.com/system/photos/8730801/1f84950b8d7949b3_thumb.gif",            "size": 1517,            "url": "https://example.zendesk.com/api/v2/attachments/8730801",            "width": 32          }        ],        "url": "https://example.zendesk.com/api/v2/attachments/8730791",        "width": 80      },      "report_csv": true,      "restricted_agent": false,      "role": "admin",      "role_type": null,      "shared": false,      "shared_agent": false,      "shared_phone_number": null,      "signature": "test",      "suspended": false,      "tags": [        "101"      ],      "ticket_restriction": null,      "time_zone": "American Samoa",      "two_factor_auth_enabled": null,      "updated_at": "2020-11-17T00:33:55Z",      "url": "https://example.zendesk.com/api/v2/users/3343",      "user_fields": {        "its_remember_september": null,        "skittles": "2018-09-14T00:00:00+00:00",        "user_field_1": "101"      },      "verified": true    }  ]}

### Count Activities

  * `GET /api/v2/activities/count`


Returns an approximate count of ticket activities in the last 30 days affecting the agent making the request. If the count exceeds 100,000, the count will return a cached result. This cached result will update every 24 hours.

The `count[refreshed_at]` property is a timestamp that indicates when the count was last updated.

**Note** : When the count exceeds 100,000, `count[refreshed_at]` may occasionally be null. This indicates that the count is being updated in the background, and `count[value]` is limited to 100,000 until the update is complete.

#### Allowed For

  * Agents


#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/activities/count \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/activities/count"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/activities/count")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/activities/count',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/activities/count"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/activities/count")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "count": {    "refreshed_at": "2020-04-06T02:18:17Z",    "value": 102  }}

### Show Activity

  * `GET /api/v2/activities/{activity_id}`


Lists a specific activity.

#### Allowed For

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
activity_id| integer| Path| true| The activity ID

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/activities/{activity_id} \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/activities/29183462"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/activities/29183462")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/activities/29183462',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/activities/29183462"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/activities/29183462")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "activity": {    "actor": {      "active": true,      "alias": "",      "created_at": "2020-11-17T00:32:12Z",      "custom_role_id": null,      "default_group_id": 1873,      "details": "",      "email": "[[email protected]](/cdn-cgi/l/email-protection)",      "external_id": null,      "iana_time_zone": "America/Juneau",      "id": 158488612,      "last_login_at": "2020-11-17T00:33:44Z",      "locale": "en-gb",      "locale_id": 5,      "moderator": true,      "name": "Tedd",      "notes": "",      "only_private_comments": false,      "organization_id": null,      "phone": null,      "photo": null,      "report_csv": true,      "restricted_agent": false,      "role": "admin",      "role_type": null,      "shared": false,      "shared_agent": false,      "shared_phone_number": null,      "signature": "",      "suspended": false,      "tags": [],      "ticket_restriction": null,      "time_zone": "Alaska",      "two_factor_auth_enabled": null,      "updated_at": "2020-11-17T00:34:38Z",      "url": "https://example.zendesk.com/api/v2/users/158488612",      "user_fields": {        "its_remember_september": null,        "skittles": null,        "user_field_1": null      },      "verified": true    },    "actor_id": 158488612,    "created_at": "2020-11-17T00:34:40Z",    "id": 29183462,    "object": {      "ticket": {        "id": 1521,        "subject": "test"      }    },    "target": {      "ticket": {        "id": 1521,        "subject": "test"      }    },    "title": "Tedd assigned ticket #1521 to you.",    "updated_at": "2020-11-17T00:34:40Z",    "url": "https://example.zendesk.com/api/v2/activities/29183462",    "user": {      "active": true,      "alias": "test",      "created_at": "2017-08-14T20:13:53Z",      "custom_role_id": null,      "default_group_id": 1873,      "details": "",      "email": "[[email protected]](/cdn-cgi/l/email-protection)",      "external_id": "oev7jj",      "iana_time_zone": "Pacific/Pago_Pago",      "id": 3343,      "last_login_at": "2020-11-16T22:57:45Z",      "locale": "en-gb",      "locale_id": 5,      "moderator": true,      "name": "Samwise Gamgee",      "notes": "test",      "only_private_comments": false,      "organization_id": 1873,      "phone": null,      "photo": {        "content_type": "image/gif",        "content_url": "https://example.zendesk.com/system/photos/8730791/1f84950b8d7949b3.gif",        "deleted": false,        "file_name": "1f84950b8d7949b3.gif",        "height": 80,        "id": 8730791,        "inline": false,        "mapped_content_url": "https://example.zendesk.com/system/photos/8730791/1f84950b8d7949b3.gif",        "size": 4566,        "thumbnails": [          {            "content_type": "image/gif",            "content_url": "https://example.zendesk.com/system/photos/8730801/1f84950b8d7949b3_thumb.gif",            "deleted": false,            "file_name": "1f84950b8d7949b3_thumb.gif",            "height": 32,            "id": 8730801,            "inline": false,            "mapped_content_url": "https://example.zendesk.com/system/photos/8730801/1f84950b8d7949b3_thumb.gif",            "size": 1517,            "url": "https://example.zendesk.com/api/v2/attachments/8730801",            "width": 32          }        ],        "url": "https://example.zendesk.com/api/v2/attachments/8730791",        "width": 80      },      "report_csv": true,      "restricted_agent": false,      "role": "admin",      "role_type": null,      "shared": false,      "shared_agent": false,      "shared_phone_number": null,      "signature": "test",      "suspended": false,      "tags": [        "101"      ],      "ticket_restriction": null,      "time_zone": "American Samoa",      "two_factor_auth_enabled": null,      "updated_at": "2020-11-17T00:33:55Z",      "url": "https://example.zendesk.com/api/v2/users/3343",      "user_fields": {        "its_remember_september": null,        "skittles": "2018-09-14T00:00:00+00:00",        "user_field_1": "101"      },      "verified": true    },    "user_id": 3343,    "verb": "tickets.assignment"  }}

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)