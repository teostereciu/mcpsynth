# Ticket Skips

*Source: https://developer.zendesk.com/api-reference/ticketing/tickets/ticket_skips/*

---

## On this page

  * [JSON format](/api-reference/ticketing/tickets/ticket_skips/#json-format)
  * [List All Skips](/api-reference/ticketing/tickets/ticket_skips/#list-all-skips)
  * [List Ticket Skips](/api-reference/ticketing/tickets/ticket_skips/#list-ticket-skips)
  * [Record a New Skip for the Current User](/api-reference/ticketing/tickets/ticket_skips/#record-a-new-skip-for-the-current-user)
  * [List Ticket Skips By Ticket](/api-reference/ticketing/tickets/ticket_skips/#list-ticket-skips-by-ticket)


# Ticket Skips

## On this page

  * [JSON format](/api-reference/ticketing/tickets/ticket_skips/#json-format)
  * [List All Skips](/api-reference/ticketing/tickets/ticket_skips/#list-all-skips)
  * [List Ticket Skips](/api-reference/ticketing/tickets/ticket_skips/#list-ticket-skips)
  * [Record a New Skip for the Current User](/api-reference/ticketing/tickets/ticket_skips/#record-a-new-skip-for-the-current-user)
  * [List Ticket Skips By Ticket](/api-reference/ticketing/tickets/ticket_skips/#list-ticket-skips-by-ticket)


A skip is a record of when an agent skips over a ticket without responding to the end user. Skips are typically recorded while a play-only agent is in Guided mode.

### JSON format

Ticket Skips are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
created_at| string| true| false| Time the skip was created
id| integer| true| false| Automatically assigned upon creation
reason| string| true| false| Reason for skipping the ticket
ticket| object| false| false| The skipped ticket. See the [Ticket object reference](/api-reference/ticketing/tickets/tickets/#json-format)
ticket_id| integer| true| false| ID of the skipped ticket
updated_at| string| true| false| Time the skip was last updated
user_id| integer| true| false| ID of the skipping agent

#### Example


    {  "created_at": "2015-09-30T21:44:03Z",  "id": 1,  "reason": "I have no idea.",  "ticket": {    "assignee_id": 235323,    "collaborator_ids": [      35334,      234    ],    "created_at": "2009-07-20T22:55:29Z",    "custom_fields": [      {        "id": 27642,        "value": "745"      },      {        "id": 27648,        "value": "yes"      }    ],    "description": "The fire is very colorful.",    "due_at": null,    "external_id": "ahg35h3jh",    "follower_ids": [      35334,      234    ],    "from_messaging_channel": false,    "generated_timestamp": 1304553600,    "group_id": 98738,    "has_incidents": false,    "id": 123,    "organization_id": 509974,    "priority": "high",    "problem_id": 9873764,    "raw_subject": "{{dc.printer_on_fire}}",    "recipient": "[[email protected]](/cdn-cgi/l/email-protection)",    "requester_id": 20978392,    "satisfaction_rating": {      "comment": "Great support!",      "id": 1234,      "score": "good"    },    "sharing_agreement_ids": [      84432    ],    "status": "open",    "subject": "Help, my printer is on fire!",    "submitter_id": 76872,    "tags": [      "enterprise",      "other_tag"    ],    "type": "incident",    "updated_at": "2011-05-05T10:38:52Z",    "url": "https://company.zendesk.com/api/v2/tickets/35436",    "via": {      "channel": "web"    }  },  "ticket_id": 123,  "updated_at": "2015-09-30T21:44:03Z",  "user_id": 456}

### List All Skips

  * `GET /api/v2/skips`


Lists all skips. Archived tickets are not included in the response. See [About archived tickets](https://support.zendesk.com/hc/en-us/articles/203657756) in the Support Help Center.

#### Pagination

  * Cursor pagination (recommended)
  * Offset pagination


See [Pagination](/api-reference/introduction/pagination/).

Returns a maximum of 100 records per page.

#### Allowed For

  * Agents with "View only" or higher reports permissions in Support. These permissions are distinct from Explore permissions.
  * Agents retrieving their own skips


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
sort_order| string| Query| false| Sort order. Defaults to "asc". Allowed values are "asc", or "desc".

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/skips \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/skips?sort_order="	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/skips")		.newBuilder()		.addQueryParameter("sort_order", "");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/skips',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'sort_order': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/skips?sort_order="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/skips")uri.query = URI.encode_www_form("sort_order": "")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "skips": [    {      "created_at": "2015-09-30T21:44:03Z",      "id": 1,      "reason": "I have no idea.",      "ticket": {        "assignee_id": 235323,        "collaborator_ids": [          35334,          234        ],        "created_at": "2009-07-20T22:55:29Z",        "custom_fields": [          {            "id": 27642,            "value": "745"          },          {            "id": 27648,            "value": "yes"          }        ],        "description": "The fire is very colorful.",        "due_at": null,        "external_id": "ahg35h3jh",        "follower_ids": [          35334,          234        ],        "from_messaging_channel": false,        "generated_timestamp": 1304553600,        "group_id": 98738,        "has_incidents": false,        "id": 123,        "organization_id": 509974,        "priority": "high",        "problem_id": 9873764,        "raw_subject": "{{dc.printer_on_fire}}",        "recipient": "[[email protected]](/cdn-cgi/l/email-protection)",        "requester_id": 20978392,        "satisfaction_rating": {          "comment": "Great support!",          "id": 1234,          "score": "good"        },        "sharing_agreement_ids": [          84432        ],        "status": "open",        "subject": "Help, my printer is on fire!",        "submitter_id": 76872,        "tags": [          "enterprise",          "other_tag"        ],        "type": "incident",        "updated_at": "2011-05-05T10:38:52Z",        "url": "https://company.zendesk.com/api/v2/tickets/35436",        "via": {          "channel": "web"        }      },      "ticket_id": 123,      "updated_at": "2015-09-30T21:44:03Z",      "user_id": 456    },    {      "created_at": "2015-10-01T21:44:03Z",      "id": 2,      "reason": "I am lost.",      "ticket": {        "assignee_id": 235323,        "collaborator_ids": [          35334,          234        ],        "created_at": "2009-07-20T22:55:29Z",        "custom_fields": [          {            "id": 27642,            "value": "745"          },          {            "id": 27648,            "value": "yes"          }        ],        "description": "The fire is very colorful.",        "due_at": null,        "external_id": "ahg35h3jh",        "follower_ids": [          35334,          234        ],        "from_messaging_channel": false,        "generated_timestamp": 1304553600,        "group_id": 98738,        "has_incidents": false,        "id": 321,        "organization_id": 509974,        "priority": "high",        "problem_id": 9873764,        "raw_subject": "{{dc.printer_on_fire}}",        "recipient": "[[email protected]](/cdn-cgi/l/email-protection)",        "requester_id": 20978392,        "satisfaction_rating": {          "comment": "Great support!",          "id": 1234,          "score": "good"        },        "sharing_agreement_ids": [          84432        ],        "status": "open",        "subject": "Help, my printer is on fire!",        "submitter_id": 76872,        "tags": [          "enterprise",          "other_tag"        ],        "type": "incident",        "updated_at": "2011-05-05T10:38:52Z",        "url": "https://company.zendesk.com/api/v2/tickets/35436",        "via": {          "channel": "web"        }      },      "ticket_id": 321,      "updated_at": "2015-10-01T21:44:03Z",      "user_id": 654    }  ]}

### List Ticket Skips

  * `GET /api/v2/users/{user_id}/skips`


Archived tickets are not included in the response. See [About archived tickets](https://support.zendesk.com/hc/en-us/articles/203657756) in the Support Help Center.

#### Pagination

  * Cursor pagination (recommended)
  * Offset pagination


See [Pagination](/api-reference/introduction/pagination/).

Returns a maximum of 100 records per page.

#### Allowed For

  * Agents with "View only" or higher reports permissions in Support. These permissions are distinct from Explore permissions.
  * Agents retrieving their own skips


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
sort_order| string| Query| false| Sort order. Defaults to "asc". Allowed values are "asc", or "desc".
user_id| integer| Path| true| User ID of an agent

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/skips \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/users/35436/skips?sort_order="	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/users/35436/skips")		.newBuilder()		.addQueryParameter("sort_order", "");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/users/35436/skips',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'sort_order': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/users/35436/skips?sort_order="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/users/35436/skips")uri.query = URI.encode_www_form("sort_order": "")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "skips": [    {      "created_at": "2015-09-30T21:44:03Z",      "id": 1,      "reason": "I have no idea.",      "ticket": {        "assignee_id": 235323,        "collaborator_ids": [          35334,          234        ],        "created_at": "2009-07-20T22:55:29Z",        "custom_fields": [          {            "id": 27642,            "value": "745"          },          {            "id": 27648,            "value": "yes"          }        ],        "description": "The fire is very colorful.",        "due_at": null,        "external_id": "ahg35h3jh",        "follower_ids": [          35334,          234        ],        "from_messaging_channel": false,        "generated_timestamp": 1304553600,        "group_id": 98738,        "has_incidents": false,        "id": 123,        "organization_id": 509974,        "priority": "high",        "problem_id": 9873764,        "raw_subject": "{{dc.printer_on_fire}}",        "recipient": "[[email protected]](/cdn-cgi/l/email-protection)",        "requester_id": 20978392,        "satisfaction_rating": {          "comment": "Great support!",          "id": 1234,          "score": "good"        },        "sharing_agreement_ids": [          84432        ],        "status": "open",        "subject": "Help, my printer is on fire!",        "submitter_id": 76872,        "tags": [          "enterprise",          "other_tag"        ],        "type": "incident",        "updated_at": "2011-05-05T10:38:52Z",        "url": "https://company.zendesk.com/api/v2/tickets/35436",        "via": {          "channel": "web"        }      },      "ticket_id": 123,      "updated_at": "2015-09-30T21:44:03Z",      "user_id": 456    },    {      "created_at": "2015-10-01T21:44:03Z",      "id": 2,      "reason": "I am lost.",      "ticket": {        "assignee_id": 235323,        "collaborator_ids": [          35334,          234        ],        "created_at": "2009-07-20T22:55:29Z",        "custom_fields": [          {            "id": 27642,            "value": "745"          },          {            "id": 27648,            "value": "yes"          }        ],        "description": "The fire is very colorful.",        "due_at": null,        "external_id": "ahg35h3jh",        "follower_ids": [          35334,          234        ],        "from_messaging_channel": false,        "generated_timestamp": 1304553600,        "group_id": 98738,        "has_incidents": false,        "id": 321,        "organization_id": 509974,        "priority": "high",        "problem_id": 9873764,        "raw_subject": "{{dc.printer_on_fire}}",        "recipient": "[[email protected]](/cdn-cgi/l/email-protection)",        "requester_id": 20978392,        "satisfaction_rating": {          "comment": "Great support!",          "id": 1234,          "score": "good"        },        "sharing_agreement_ids": [          84432        ],        "status": "open",        "subject": "Help, my printer is on fire!",        "submitter_id": 76872,        "tags": [          "enterprise",          "other_tag"        ],        "type": "incident",        "updated_at": "2011-05-05T10:38:52Z",        "url": "https://company.zendesk.com/api/v2/tickets/35436",        "via": {          "channel": "web"        }      },      "ticket_id": 321,      "updated_at": "2015-10-01T21:44:03Z",      "user_id": 654    }  ]}

### Record a New Skip for the Current User

  * `POST /api/v2/skips`


Record a new ticket skip for the current user.

#### Allowed For

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
sort_order| string| Query| false| Sort order. Defaults to "asc". Allowed values are "asc", or "desc".

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/skips \-v -u {email_address}/token:{api_token} \-H "Content-Type: application/json" -X POST \-d '{"skip": {"ticket_id": 123, "reason": "I have no idea."}}'

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/skips?sort_order="	method := "POST"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/skips")		.newBuilder()		.addQueryParameter("sort_order", "");RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'POST',  url: 'https://example.zendesk.com/api/v2/skips',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'sort_order': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/skips?sort_order="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/skips")uri.query = URI.encode_www_form("sort_order": "")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**201 Created**


    // Status 201 Created
    {  "skip": {    "created_at": "2015-09-30T21:44:03Z",    "id": 1,    "reason": "I have no idea.",    "ticket": {      "assignee_id": 235323,      "collaborator_ids": [        35334,        234      ],      "created_at": "2009-07-20T22:55:29Z",      "custom_fields": [        {          "id": 27642,          "value": "745"        },        {          "id": 27648,          "value": "yes"        }      ],      "description": "The fire is very colorful.",      "due_at": null,      "external_id": "ahg35h3jh",      "follower_ids": [        35334,        234      ],      "from_messaging_channel": false,      "generated_timestamp": 1443575048,      "group_id": 98738,      "has_incidents": false,      "id": 123,      "organization_id": 509974,      "priority": "high",      "problem_id": 9873764,      "raw_subject": "{{dc.printer_on_fire}}",      "recipient": "[[email protected]](/cdn-cgi/l/email-protection)",      "requester_id": 20978392,      "satisfaction_rating": {        "comment": "Great support!",        "id": 1234,        "score": "good"      },      "sharing_agreement_ids": [        84432      ],      "status": "open",      "subject": "Help, my printer is on fire!",      "submitter_id": 76872,      "tags": [        "enterprise",        "other_tag"      ],      "type": "incident",      "updated_at": "2011-05-05T10:38:52Z",      "url": "https://company.zendesk.com/api/v2/tickets/35436",      "via": {        "channel": "web"      }    },    "ticket_id": 123,    "updated_at": "2015-09-30T21:44:03Z",    "user_id": 456  }}

### List Ticket Skips By Ticket

  * `GET /api/v2/tickets/{ticket_id}/skips`


Returns the skips for a specific ticket.

Archived tickets are not included in the response. See [About archived tickets](https://support.zendesk.com/hc/en-us/articles/203657756) in the Support Help Center.

#### Pagination

  * Cursor pagination (recommended)
  * Offset pagination


See [Pagination](/api-reference/introduction/pagination/).

Returns a maximum of 100 records per page.

#### Allowed For

  * Agents with "View only" or higher reports permissions in Support. These permissions are distinct from Explore permissions.
  * Agents retrieving their own skips


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
sort_order| string| Query| false| Sort order. Defaults to "asc". Allowed values are "asc", or "desc".
ticket_id| integer| Path| true| The ID of the ticket

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/tickets/{ticket_id}/skips \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/tickets/123456/skips?sort_order="	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/tickets/123456/skips")		.newBuilder()		.addQueryParameter("sort_order", "");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/tickets/123456/skips',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'sort_order': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/tickets/123456/skips?sort_order="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/tickets/123456/skips")uri.query = URI.encode_www_form("sort_order": "")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "skips": [    {      "created_at": "2015-09-30T21:44:03Z",      "id": 1,      "reason": "I have no idea.",      "ticket": {        "assignee_id": 235323,        "collaborator_ids": [          35334,          234        ],        "created_at": "2009-07-20T22:55:29Z",        "custom_fields": [          {            "id": 27642,            "value": "745"          },          {            "id": 27648,            "value": "yes"          }        ],        "description": "The fire is very colorful.",        "due_at": null,        "external_id": "ahg35h3jh",        "follower_ids": [          35334,          234        ],        "from_messaging_channel": false,        "generated_timestamp": 1304553600,        "group_id": 98738,        "has_incidents": false,        "id": 123,        "organization_id": 509974,        "priority": "high",        "problem_id": 9873764,        "raw_subject": "{{dc.printer_on_fire}}",        "recipient": "[[email protected]](/cdn-cgi/l/email-protection)",        "requester_id": 20978392,        "satisfaction_rating": {          "comment": "Great support!",          "id": 1234,          "score": "good"        },        "sharing_agreement_ids": [          84432        ],        "status": "open",        "subject": "Help, my printer is on fire!",        "submitter_id": 76872,        "tags": [          "enterprise",          "other_tag"        ],        "type": "incident",        "updated_at": "2011-05-05T10:38:52Z",        "url": "https://company.zendesk.com/api/v2/tickets/35436",        "via": {          "channel": "web"        }      },      "ticket_id": 123,      "updated_at": "2015-09-30T21:44:03Z",      "user_id": 456    },    {      "created_at": "2015-10-01T21:44:03Z",      "id": 2,      "reason": "I am lost.",      "ticket": {        "assignee_id": 235323,        "collaborator_ids": [          35334,          234        ],        "created_at": "2009-07-20T22:55:29Z",        "custom_fields": [          {            "id": 27642,            "value": "745"          },          {            "id": 27648,            "value": "yes"          }        ],        "description": "The fire is very colorful.",        "due_at": null,        "external_id": "ahg35h3jh",        "follower_ids": [          35334,          234        ],        "from_messaging_channel": false,        "generated_timestamp": 1304553600,        "group_id": 98738,        "has_incidents": false,        "id": 321,        "organization_id": 509974,        "priority": "high",        "problem_id": 9873764,        "raw_subject": "{{dc.printer_on_fire}}",        "recipient": "[[email protected]](/cdn-cgi/l/email-protection)",        "requester_id": 20978392,        "satisfaction_rating": {          "comment": "Great support!",          "id": 1234,          "score": "good"        },        "sharing_agreement_ids": [          84432        ],        "status": "open",        "subject": "Help, my printer is on fire!",        "submitter_id": 76872,        "tags": [          "enterprise",          "other_tag"        ],        "type": "incident",        "updated_at": "2011-05-05T10:38:52Z",        "url": "https://company.zendesk.com/api/v2/tickets/35436",        "via": {          "channel": "web"        }      },      "ticket_id": 321,      "updated_at": "2015-10-01T21:44:03Z",      "user_id": 654    }  ]}

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)