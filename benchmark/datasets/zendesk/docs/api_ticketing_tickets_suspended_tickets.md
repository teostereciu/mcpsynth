# Suspended Tickets

*Source: https://developer.zendesk.com/api-reference/ticketing/tickets/suspended_tickets/*

---

## On this page

  * [JSON format](/api-reference/ticketing/tickets/suspended_tickets/#json-format)
  * [List Suspended Tickets](/api-reference/ticketing/tickets/suspended_tickets/#list-suspended-tickets)
  * [Show Suspended Ticket](/api-reference/ticketing/tickets/suspended_tickets/#show-suspended-ticket)
  * [Recover Suspended Ticket](/api-reference/ticketing/tickets/suspended_tickets/#recover-suspended-ticket)
  * [Recover Multiple Suspended Tickets](/api-reference/ticketing/tickets/suspended_tickets/#recover-multiple-suspended-tickets)
  * [Delete Suspended Ticket](/api-reference/ticketing/tickets/suspended_tickets/#delete-suspended-ticket)
  * [Delete Multiple Suspended Tickets](/api-reference/ticketing/tickets/suspended_tickets/#delete-multiple-suspended-tickets)
  * [Suspended Ticket Attachments](/api-reference/ticketing/tickets/suspended_tickets/#suspended-ticket-attachments)
  * [Export Suspended Tickets](/api-reference/ticketing/tickets/suspended_tickets/#export-suspended-tickets)


# Suspended Tickets

## On this page

  * [JSON format](/api-reference/ticketing/tickets/suspended_tickets/#json-format)
  * [List Suspended Tickets](/api-reference/ticketing/tickets/suspended_tickets/#list-suspended-tickets)
  * [Show Suspended Ticket](/api-reference/ticketing/tickets/suspended_tickets/#show-suspended-ticket)
  * [Recover Suspended Ticket](/api-reference/ticketing/tickets/suspended_tickets/#recover-suspended-ticket)
  * [Recover Multiple Suspended Tickets](/api-reference/ticketing/tickets/suspended_tickets/#recover-multiple-suspended-tickets)
  * [Delete Suspended Ticket](/api-reference/ticketing/tickets/suspended_tickets/#delete-suspended-ticket)
  * [Delete Multiple Suspended Tickets](/api-reference/ticketing/tickets/suspended_tickets/#delete-multiple-suspended-tickets)
  * [Suspended Ticket Attachments](/api-reference/ticketing/tickets/suspended_tickets/#suspended-ticket-attachments)
  * [Export Suspended Tickets](/api-reference/ticketing/tickets/suspended_tickets/#export-suspended-tickets)


In most cases, when an end user submits a support request by email, the email becomes a new ticket or adds a comment to an existing ticket. However, in certain cases, the email becomes a suspended ticket. It remains suspended until someone reviews the email and decides whether to accept or reject it. If no one reviews it, the email is deleted after 14 days.

You can use this API to list, recover, or delete suspended tickets. For more information about suspended tickets, see [Understanding and managing suspended tickets and spam](https://support.zendesk.com/hc/en-us/articles/4408889141146) and [Guidelines for reviewing suspended tickets](https://support.zendesk.com/hc/en-us/articles/4408832102042) in Zendesk help.

### JSON format

Suspended Tickets are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
attachments| array| true| false| The attachments, if any associated to this suspended ticket. See [Attachments](/api-reference/ticketing/tickets/ticket-attachments/)
author| object| true| false| The author id (if available), name and email
brand_id| integer| true| false| The id of the brand this ticket is associated with. Only applicable for Enterprise accounts
cause| string| true| false| Why the ticket was suspended
cause_id| integer| true| false| The ID of the cause
content| string| true| false| The content that was flagged
created_at| string| true| false| The ticket ID this suspended email is associated with, if available
error_messages| array| true| false| The error messages if any associated to this suspended ticket
id| integer| true| false| Automatically assigned
message_id| string| true| false| The ID of the email, if available
recipient| string| true| false| The original recipient e-mail address of the ticket
subject| string| true| false| The value of the subject field for this ticket
ticket_id| integer| true| false| The ticket ID this suspended email is associated with, if available
updated_at| string| true| false| When the ticket was assigned
url| string| true| false| The API url of this ticket
via| object| true| false| An object explaining how the ticket was created. See the [Via object reference](/documentation/ticketing/reference-guides/via-object-reference)

#### Example


    {  "attachments": [],  "author": {    "email": "[[email protected]](/cdn-cgi/l/email-protection)",    "id": 1111,    "name": "Mr. Roboto"  },  "brand_id": 123,  "cause": "Detected as spam",  "cause_id": 0,  "content": "Out Of Office Reply",  "created_at": "2009-07-20T22:55:29Z",  "error_messages": null,  "id": 435,  "message_id": "[[email protected]](/cdn-cgi/l/email-protection)",  "recipient": "[[email protected]](/cdn-cgi/l/email-protection)",  "subject": "Help, my printer is on fire!",  "ticket_id": 67321,  "updated_at": "2011-05-05T10:38:52Z",  "url": "https://example.zendesk.com/api/v2/tickets/35436",  "via": {    "channel": "email",    "source": {      "from": {        "address": "[[email protected]](/cdn-cgi/l/email-protection)",        "name": "TotallyLegit"      },      "rel": null,      "to": {        "address": "[[email protected]](/cdn-cgi/l/email-protection)",        "name": "Example Account"      }    }  }}

### List Suspended Tickets

  * `GET /api/v2/suspended_tickets`


#### Allowed For

  * Admins and [agents in custom roles with permission](https://support.zendesk.com/hc/en-us/articles/4408882153882#topic_cxn_hig_bd) to manage suspended tickets on Enterprise plans
  * Unrestricted agents on all other plans


#### Sorting

You can sort the tickets with the `sort_by` and `sort_order` query string parameters.

#### Pagination

  * Cursor pagination


See [Pagination](/api-reference/introduction/pagination/).

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
page| | Query| false| Pagination parameter. Supports both traditional offset and cursor-based pagination: - Traditional: `?page=2` (integer page number) - Cursor: `?page[size]=50&page[after]=cursor` (deepObject with size, after, before) These are mutually exclusive - use one format or the other, not both.
per_page| integer| Query| false| Number of records to return per page. Note: Default and maximum values vary by endpoint. Check endpoint-specific documentation for limits.
sort_by| string| Query| false| The field to sort the suspended tickets by. One of "author_email", "cause", "created_at", or "subject"
sort_order| string| Query| false| The order in which to sort the suspended tickets. This can take value `asc` or `desc`.

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/suspended_tickets \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/suspended_tickets?page=&per_page=50&sort_by=author_email&sort_order=asc"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/suspended_tickets")		.newBuilder()		.addQueryParameter("page", "")		.addQueryParameter("per_page", "50")		.addQueryParameter("sort_by", "author_email")		.addQueryParameter("sort_order", "asc");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/suspended_tickets',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'page': '',    'per_page': '50',    'sort_by': 'author_email',    'sort_order': 'asc',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/suspended_tickets?page=&per_page=50&sort_by=author_email&sort_order=asc"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/suspended_tickets")uri.query = URI.encode_www_form("page": "", "per_page": "50", "sort_by": "author_email", "sort_order": "asc")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "suspended_tickets": [    {      "attachments": [],      "author": {        "email": "[[email protected]](/cdn-cgi/l/email-protection)",        "id": 1,        "name": "Mr. Roboto"      },      "brand_id": 123,      "cause": "Detected as spam",      "cause_id": 0,      "content": "Out Of Office Reply",      "created_at": "2009-07-20T22:55:29Z",      "error_messages": null,      "id": 435,      "message_id": "[[email protected]](/cdn-cgi/l/email-protection)",      "recipient": "[[email protected]](/cdn-cgi/l/email-protection)",      "subject": "Help, my printer is on fire!",      "ticket_id": 67321,      "updated_at": "2011-05-05T10:38:52Z",      "url": "https://example.zendesk.com/api/v2/tickets/35436",      "via": {        "channel": "email",        "source": {          "from": {            "address": "[[email protected]](/cdn-cgi/l/email-protection)",            "name": "TotallyLegit"          },          "rel": null,          "to": {            "address": "[[email protected]](/cdn-cgi/l/email-protection)",            "name": "Example Account"          }        }      }    },    {      "attachments": [],      "author": {        "email": "[[email protected]](/cdn-cgi/l/email-protection)",        "id": 1,        "name": "Mr. Roboto"      },      "brand_id": 123,      "cause": "Automated response mail",      "cause_id": 0,      "content": "Out Of Office Reply",      "created_at": "2009-07-20T22:55:29Z",      "error_messages": null,      "id": 207623,      "message_id": "[[email protected]](/cdn-cgi/l/email-protection)",      "recipient": "[[email protected]](/cdn-cgi/l/email-protection)",      "subject": "Not just anybody!",      "ticket_id": 67321,      "updated_at": "2011-05-05T10:38:52Z",      "url": "https://example.zendesk.com/api/v2/tickets/35436",      "via": {        "channel": "email",        "source": {          "from": {            "address": "[[email protected]](/cdn-cgi/l/email-protection)",            "name": "TotallyLegit"          },          "rel": null,          "to": {            "address": "[[email protected]](/cdn-cgi/l/email-protection)",            "name": "Example Account"          }        }      }    }  ]}

### Show Suspended Ticket

  * `GET /api/v2/suspended_tickets/{id}`


#### Allowed For

  * Admins and [agents in custom roles with permission](https://support.zendesk.com/hc/en-us/articles/4408882153882#topic_cxn_hig_bd) to manage suspended tickets on Enterprise plans
  * Unrestricted agents on all other plans


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
id| number| Path| true| id of the suspended ticket

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/suspended_tickets/{id} \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/suspended_tickets/35436"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/suspended_tickets/35436")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/suspended_tickets/35436',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/suspended_tickets/35436"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/suspended_tickets/35436")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "suspended_tickets": [    {      "attachments": [],      "author": {        "email": "[[email protected]](/cdn-cgi/l/email-protection)",        "id": 1,        "name": "Mr. Roboto"      },      "brand_id": 123,      "cause": "Detected as spam",      "cause_id": 0,      "content": "Out Of Office Reply",      "created_at": "2009-07-20T22:55:29Z",      "error_messages": null,      "id": 435,      "message_id": "[[email protected]](/cdn-cgi/l/email-protection)",      "recipient": "[[email protected]](/cdn-cgi/l/email-protection)",      "subject": "Help, my printer is on fire!",      "ticket_id": 67321,      "updated_at": "2011-05-05T10:38:52Z",      "url": "https://example.zendesk.com/api/v2/tickets/35436",      "via": {        "channel": "email",        "source": {          "from": {            "address": "[[email protected]](/cdn-cgi/l/email-protection)",            "name": "TotallyLegit"          },          "rel": null,          "to": {            "address": "[[email protected]](/cdn-cgi/l/email-protection)",            "name": "Example Account"          }        }      }    },    {      "attachments": [],      "author": {        "email": "[[email protected]](/cdn-cgi/l/email-protection)",        "id": 1,        "name": "Mr. Roboto"      },      "brand_id": 123,      "cause": "Automated response mail",      "cause_id": 0,      "content": "Out Of Office Reply",      "created_at": "2009-07-20T22:55:29Z",      "error_messages": null,      "id": 207623,      "message_id": "[[email protected]](/cdn-cgi/l/email-protection)",      "recipient": "[[email protected]](/cdn-cgi/l/email-protection)",      "subject": "Not just anybody!",      "ticket_id": 67321,      "updated_at": "2011-05-05T10:38:52Z",      "url": "https://example.zendesk.com/api/v2/tickets/35436",      "via": {        "channel": "email",        "source": {          "from": {            "address": "[[email protected]](/cdn-cgi/l/email-protection)",            "name": "TotallyLegit"          },          "rel": null,          "to": {            "address": "[[email protected]](/cdn-cgi/l/email-protection)",            "name": "Example Account"          }        }      }    }  ]}

### Recover Suspended Ticket

  * `PUT /api/v2/suspended_tickets/{id}/recover`


**Note** : During recovery, the API sets the requester to the authenticated agent who called the API, not the original requester. This prevents the ticket from being re-suspended after recovery. To preserve the original requester, use the Recover Multiple Suspended Tickets endpoint with the single ticket.

This endpoint does not queue an asynchronous job that can be tracked from [Job Statuses](/api-reference/ticketing/ticket-management/job_statuses/). Instead, it processes the request with a synchronous response.

  * If all recoveries are successful, it returns a 200 with a `tickets` array in the response.
  * If all recoveries fail, it returns a 422 with a `suspended_tickets` array in the response.
  * If there is a mixture of successes and failures in a single call, it returns a 422 with a `suspended_tickets` array of the failures in the response.


#### Allowed For

  * Admins and [agents in custom roles with permission](https://support.zendesk.com/hc/en-us/articles/4408882153882#topic_cxn_hig_bd) to manage suspended tickets on Enterprise plans
  * Unrestricted agents on all other plans


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
id| number| Path| true| id of the suspended ticket

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/suspended_tickets/{id}/recover \  -v -u {email_address}/token:{api_token} -X PUT

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/suspended_tickets/35436/recover"	method := "PUT"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/suspended_tickets/35436/recover")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'PUT',  url: 'https://example.zendesk.com/api/v2/suspended_tickets/35436/recover',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/suspended_tickets/35436/recover"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/suspended_tickets/35436/recover")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "ticket": [    {      "assignee_id": 235323,      "collaborator_ids": [        35334,        234      ],      "created_at": "2009-07-20T22:55:29Z",      "custom_fields": [        {          "id": 27642,          "value": "745"        },        {          "id": 27648,          "value": "yes"        }      ],      "custom_status_id": 123,      "description": "The fire is very colorful.",      "due_at": null,      "external_id": "ahg35h3jh",      "follower_ids": [        35334,        234      ],      "from_messaging_channel": false,      "generated_timestamp": 1304553600,      "group_id": 98738,      "has_incidents": false,      "id": 35436,      "organization_id": 509974,      "priority": "high",      "problem_id": 9873764,      "raw_subject": "{{dc.printer_on_fire}}",      "recipient": "[[email protected]](/cdn-cgi/l/email-protection)",      "requester_id": 20978392,      "satisfaction_rating": {        "comment": "Great support!",        "id": 1234,        "score": "good"      },      "sharing_agreement_ids": [        84432      ],      "status": "open",      "subject": "Help, my printer is on fire!",      "submitter_id": 76872,      "tags": [        "enterprise",        "other_tag"      ],      "type": "incident",      "updated_at": "2011-05-05T10:38:52Z",      "url": "https://company.zendesk.com/api/v2/tickets/35436",      "via": {        "channel": "web"      }    }  ]}

**422 Unprocessable Entity**


    // Status 422 Unprocessable Entity
    {  "ticket": [    {      "author": {        "email": "[[email protected]](/cdn-cgi/l/email-protection)",        "id": 1,        "name": "Help"      },      "brand_id": 123,      "cause": "Received from support address",      "cause_id": 22,      "content": "Your request has been received and is being reviewed by our support staff.",      "created_at": "2023-04-06T20:51:31Z",      "error_messages": null,      "id": 14668816692628,      "message_id": "<[[email protected]](/cdn-cgi/l/email-protection)>",      "recipient": "[[email protected]](/cdn-cgi/l/email-protection)",      "subject": "Received from support address",      "ticket_id": 14668816692628,      "updated_at": "2023-04-06T20:51:31Z",      "url": "https://example.zendesk.com/api/v2/tickets/14668816692628",      "via": {        "channel": "email",        "source": {          "from": {            "address": "[[email protected]](/cdn-cgi/l/email-protection),",            "name": "Help"          },          "rel": null,          "to": {            "address": "[[email protected]](/cdn-cgi/l/email-protection)",            "name": "Support,"          }        }      }    }  ]}

### Recover Multiple Suspended Tickets

  * `PUT /api/v2/suspended_tickets/recover_many?ids={ids}`


Accepts up to 100 ids (the auto-generated id, not the ticket id.) Note that suspended tickets that fail to be recovered are still included in the response.

#### Allowed For

  * Admins and [agents in custom roles with permission](https://support.zendesk.com/hc/en-us/articles/4408882153882#topic_cxn_hig_bd) to manage suspended tickets on Enterprise plans
  * Unrestricted agents on all other plans


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
ids| string| Query| true| A comma separated list of ids of suspended tickets to recover.

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/suspended_tickets/recover_many?ids={id1},{id2} \  -v -u {email_address}/token:{api_token} -X PUT

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/suspended_tickets/recover_many?ids=14%2C77"	method := "PUT"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/suspended_tickets/recover_many")		.newBuilder()		.addQueryParameter("ids", "14,77");RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'PUT',  url: 'https://example.zendesk.com/api/v2/suspended_tickets/recover_many',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'ids': '14%2C77',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/suspended_tickets/recover_many?ids=14%2C77"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/suspended_tickets/recover_many")uri.query = URI.encode_www_form("ids": "14,77")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "tickets": [    {      "assignee_id": 235323,      "collaborator_ids": [        35334,        234      ],      "created_at": "2009-07-20T22:55:29Z",      "custom_fields": [        {          "id": 27642,          "value": "745"        },        {          "id": 27648,          "value": "yes"        }      ],      "custom_status_id": 123,      "description": "The fire is very colorful.",      "due_at": null,      "external_id": "ahg35h3jh",      "follower_ids": [        35334,        234      ],      "from_messaging_channel": false,      "generated_timestamp": 1304553600,      "group_id": 98738,      "has_incidents": false,      "id": 3436,      "organization_id": 509974,      "priority": "high",      "problem_id": 9873764,      "raw_subject": "{{dc.printer_on_fire}}",      "recipient": "[[email protected]](/cdn-cgi/l/email-protection)",      "requester_id": 20978392,      "satisfaction_rating": {        "comment": "Great support!",        "id": 1234,        "score": "good"      },      "sharing_agreement_ids": [        84432      ],      "status": "open",      "subject": "Help, my printer is on fire!",      "submitter_id": 76872,      "tags": [        "enterprise",        "other_tag"      ],      "type": "incident",      "updated_at": "2011-05-05T10:38:52Z",      "url": "https://company.zendesk.com/api/v2/tickets/35436",      "via": {        "channel": "web"      }    },    {      "assignee_id": 235323,      "collaborator_ids": [        35334,        234      ],      "created_at": "2009-07-20T22:55:29Z",      "custom_fields": [        {          "id": 27642,          "value": "745"        },        {          "id": 27648,          "value": "yes"        }      ],      "custom_status_id": 123,      "description": "The fire is very colorful.",      "due_at": null,      "external_id": "ahg35h3jh",      "follower_ids": [        35334,        234      ],      "from_messaging_channel": false,      "generated_timestamp": 1304553600,      "group_id": 98738,      "has_incidents": false,      "id": 3437,      "organization_id": 509974,      "priority": "high",      "problem_id": 9873764,      "raw_subject": "{{dc.printer_on_fire}}",      "recipient": "[[email protected]](/cdn-cgi/l/email-protection)",      "requester_id": 20978392,      "satisfaction_rating": {        "comment": "Great support!",        "id": 1234,        "score": "good"      },      "sharing_agreement_ids": [        84432      ],      "status": "open",      "subject": "Help, my printer is on fire!",      "submitter_id": 76872,      "tags": [        "enterprise",        "other_tag"      ],      "type": "incident",      "updated_at": "2011-05-05T10:38:52Z",      "url": "https://company.zendesk.com/api/v2/tickets/35436",      "via": {        "channel": "web"      }    }  ]}

### Delete Suspended Ticket

  * `DELETE /api/v2/suspended_tickets/{id}`


#### Allowed For

  * Unrestricted agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
id| number| Path| true| id of the suspended ticket

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/suspended_tickets/{id} \  -v -u {email_address}/token:{api_token} -X DELETE

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/suspended_tickets/35436"	method := "DELETE"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/suspended_tickets/35436")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("DELETE", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'DELETE',  url: 'https://example.zendesk.com/api/v2/suspended_tickets/35436',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/suspended_tickets/35436"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"DELETE",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/suspended_tickets/35436")request = Net::HTTP::Delete.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**204 No Content**


    // Status 204 No Content
    null

### Delete Multiple Suspended Tickets

  * `DELETE /api/v2/suspended_tickets/destroy_many?ids={ids}`


Accepts up to 100 ids (the auto-generated id, not the ticket id.)

#### Allowed For

  * Admins and [agents in custom roles with permission](https://support.zendesk.com/hc/en-us/articles/4408882153882#topic_cxn_hig_bd) to manage suspended tickets on Enterprise plans
  * Unrestricted agents on all other plans


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
ids| string| Query| true| A comma separated list of ids of suspended tickets to delete.

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/suspended_tickets/destroy_many?ids={id1},{id2} \  -v -u {email_address}/token:{api_token} -X DELETE

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/suspended_tickets/destroy_many?ids=94%2C141"	method := "DELETE"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/suspended_tickets/destroy_many")		.newBuilder()		.addQueryParameter("ids", "94,141");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("DELETE", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'DELETE',  url: 'https://example.zendesk.com/api/v2/suspended_tickets/destroy_many',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'ids': '94%2C141',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/suspended_tickets/destroy_many?ids=94%2C141"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"DELETE",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/suspended_tickets/destroy_many")uri.query = URI.encode_www_form("ids": "94,141")request = Net::HTTP::Delete.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**204 No Content**


    // Status 204 No Content
    null

### Suspended Ticket Attachments

  * `POST /api/v2/suspended_tickets/attachments`


Makes copies of any attachments on a suspended ticket and returns them as [attachment tokens](/api-reference/ticketing/tickets/ticket-attachments/). If the ticket is manually recovered, you can include the attachment tokens on the new ticket.

#### Allowed For

  * Admins and [agents in custom roles with permission](https://support.zendesk.com/hc/en-us/articles/4408882153882#topic_cxn_hig_bd) to manage suspended tickets on Enterprise plans
  * Unrestricted agents on all other plans


#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/suspended_tickets/{id}/attachments \  -v -u {email_address}/token:{api_token} -X POST

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/suspended_tickets/attachments"	method := "POST"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/suspended_tickets/attachments")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'POST',  url: 'https://example.zendesk.com/api/v2/suspended_tickets/attachments',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/suspended_tickets/attachments"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/suspended_tickets/attachments")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "upload": {    "attachments": [      {        "content_type": "application/ics",        "content_url": "https://company.zendesk.com/attachments/token/tyBq1ms40dFaHefSIigxZpwGg/?name=calendar.ics",        "file_name": "calendar.ics",        "id": 367,        "size": 1166,        "thumbnails": [],        "url": "https://company.zendesk.com/api/v2/attachments/367"      }    ],    "token": "yrznqgjoa24iw2f"  }}

### Export Suspended Tickets

  * `POST /api/v2/suspended_tickets/export`


Exports a list of suspended tickets for the Zendesk Support instance. To export the list, the endpoint enqueues a job to create a CSV file with the data. When done, Zendesk sends the requester an email containing a link to the CSV file. In the CSV, tickets are sorted by the update timestamp in ascending order.

#### Allowed For

  * Admins and [agents in custom roles with permission](https://support.zendesk.com/hc/en-us/articles/4408882153882#topic_cxn_hig_bd) to manage suspended tickets on Enterprise plans
  * Unrestricted agents on all other plans


#### Rate limits

Limited to one request per minute and up to one million records in return. The rate-limiting mechanism behaves identically to the one described in [Usage limits](/api-reference/ticketing/account-configuration/usage_limits/#monitoring-your-request-activity). We recommend using the `Retry-After` header value as described in [Catching errors caused by rate limiting](/documentation/ticketing/using-the-zendesk-api/best-practices-for-avoiding-rate-limiting#catch).

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/suspended_tickets/export \  -v -u {email_address}/token:{api_token} -X POST

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/suspended_tickets/export"	method := "POST"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/suspended_tickets/export")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'POST',  url: 'https://example.zendesk.com/api/v2/suspended_tickets/export',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/suspended_tickets/export"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/suspended_tickets/export")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "export": {    "status": "enqueued",    "view_id": "suspended"  }}

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)