# Ticket Import

*Source: https://developer.zendesk.com/api-reference/ticketing/tickets/ticket_import/*

---

## On this page

  * [Ticket Import](/api-reference/ticketing/tickets/ticket_import/#ticket-import)
  * [Ticket Bulk Import](/api-reference/ticketing/tickets/ticket_import/#ticket-bulk-import)


# Ticket Import

## On this page

  * [Ticket Import](/api-reference/ticketing/tickets/ticket_import/#ticket-import)
  * [Ticket Bulk Import](/api-reference/ticketing/tickets/ticket_import/#ticket-bulk-import)


You can use the imports API to move tickets in bulk from legacy systems into Zendesk Support.

Ticket imports support the normal ticket properties outlined in [Tickets](/api-reference/ticketing/tickets/tickets/#json-format), but have some additional features and restrictions.

##### Timestamps

You can set the following time stamps on the tickets: `solved_at`, `updated_at`, and `created_at`. However, providing a value for `created_at` or `updated_at` before 1970 will be automatically rounded up to 1970.

##### Comments

You can include one or more comments with a ticket. See [Ticket Comments](/api-reference/ticketing/tickets/ticket_comments/#json-format) for the properties. You can use `value`, `body`, or `html_body` for the comment body. You can also set the comment's `created_at` time stamp. However, you can't set the time stamp before 1970 or in the future.

##### Direct to archive

Ticket imports support the additional request parameter of `archive_immediately`. If true, any ticket created with a `closed` status bypasses the normal ticket lifecycle and will be created directly in your ticket archive. It's important to note that archived tickets have a handful of restrictions around their use. [You can read more about it here](https://support.zendesk.com/hc/en-us/articles/203657756-About-ticket-archiving).

You may want to explore this option if you are importing a large amount of historical data (750,000+ tickets) and don't want to impact the performance of your active tickets.

##### Attachments

Attachments are handled the same way as in the tickets API. You upload the files then supply the token in the comment parameters. See [Attaching files](/api-reference/ticketing/tickets/tickets/#attaching-files).

##### Triggers

If a ticket with a status other than closed is imported, triggers won't run on the imported ticket. However, if the ticket is updated after import, triggers will resume.

##### Metrics

Zendesk metrics and SLAs are not supported for imported tickets. Running metrics or SLAs on imported tickets will result in incomplete and inaccurate data. Zendesk recommends adding a tag to signify these tickets were imported into Zendesk Support and excluding them from any reports.

##### Notifications

No notifications are sent to users cc'ed on the imported tickets. Notifications are sent on subsequent updates to the tickets.

### Ticket Import

  * `POST /api/v2/imports/tickets`


#### Allowed For

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
archive_immediately| boolean| Query| false| If `true`, any ticket created with a `closed` status bypasses the normal ticket lifecycle and will be created directly in your ticket archive

#### Example body


    {  "ticket": {    "assignee_id": 19,    "comments": [      {        "author_id": 827,        "created_at": "2009-06-25T10:15:18Z",        "value": "This is a comment"      },      {        "author_id": 19,        "public": false,        "value": "This is a private comment"      }    ],    "description": "A description",    "requester_id": 827,    "subject": "Help",    "tags": [      "foo",      "bar"    ]  }}

#### Code Samples

**cURL**


    curl https://{subdomain}.zendesk.com/api/v2/imports/tickets \  -v -u {email_address}/token:{api_token} -X POST \  -d '{"ticket": {"subject": "Help", "comments": [{ "author_id": 19, "value": "This is a comment" }]}}' \  -H "Content-Type: application/json"

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://example.zendesk.com/api/v2/imports/tickets?archive_immediately="	method := "POST"	payload := strings.NewReader(`{  "ticket": {    "assignee_id": 19,    "comments": [      {        "author_id": 827,        "created_at": "2009-06-25T10:15:18Z",        "value": "This is a comment"      },      {        "author_id": 19,        "public": false,        "value": "This is a private comment"      }    ],    "description": "A description",    "requester_id": 827,    "subject": "Help",    "tags": [      "foo",      "bar"    ]  }}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/imports/tickets")		.newBuilder()		.addQueryParameter("archive_immediately", "");RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"ticket\": {    \"assignee_id\": 19,    \"comments\": [      {        \"author_id\": 827,        \"created_at\": \"2009-06-25T10:15:18Z\",        \"value\": \"This is a comment\"      },      {        \"author_id\": 19,        \"public\": false,        \"value\": \"This is a private comment\"      }    ],    \"description\": \"A description\",    \"requester_id\": 827,    \"subject\": \"Help\",    \"tags\": [      \"foo\",      \"bar\"    ]  }}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "ticket": {    "assignee_id": 19,    "comments": [      {        "author_id": 827,        "created_at": "2009-06-25T10:15:18Z",        "value": "This is a comment"      },      {        "author_id": 19,        "public": false,        "value": "This is a private comment"      }    ],    "description": "A description",    "requester_id": 827,    "subject": "Help",    "tags": [      "foo",      "bar"    ]  }});
    var config = {  method: 'POST',  url: 'https://example.zendesk.com/api/v2/imports/tickets',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'archive_immediately': '',  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/imports/tickets?archive_immediately="
    payload = json.loads("""{  "ticket": {    "assignee_id": 19,    "comments": [      {        "author_id": 827,        "created_at": "2009-06-25T10:15:18Z",        "value": "This is a comment"      },      {        "author_id": 19,        "public": false,        "value": "This is a private comment"      }    ],    "description": "A description",    "requester_id": 827,    "subject": "Help",    "tags": [      "foo",      "bar"    ]  }}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/imports/tickets")uri.query = URI.encode_www_form("archive_immediately": "")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")request.body = %q({  "ticket": {    "assignee_id": 19,    "comments": [      {        "author_id": 827,        "created_at": "2009-06-25T10:15:18Z",        "value": "This is a comment"      },      {        "author_id": 19,        "public": false,        "value": "This is a private comment"      }    ],    "description": "A description",    "requester_id": 827,    "subject": "Help",    "tags": [      "foo",      "bar"    ]  }})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**201 Created**


    // Status 201 Created
    {  "ticket": {    "assignee_id": 235323,    "collaborator_ids": [      35334,      234    ],    "created_at": "2009-07-20T22:55:29Z",    "custom_fields": [      {        "id": 27642,        "value": "745"      },      {        "id": 27648,        "value": "yes"      }    ],    "custom_status_id": 123,    "description": "The fire is very colorful.",    "due_at": null,    "external_id": "ahg35h3jh",    "follower_ids": [      35334,      234    ],    "from_messaging_channel": false,    "generated_timestamp": 1304553600,    "group_id": 98738,    "has_incidents": false,    "id": 35436,    "organization_id": 509974,    "priority": "high",    "problem_id": 9873764,    "raw_subject": "{{dc.printer_on_fire}}",    "recipient": "[[email protected]](/cdn-cgi/l/email-protection)",    "requester_id": 20978392,    "satisfaction_rating": {      "comment": "Great support!",      "id": 1234,      "score": "good"    },    "sharing_agreement_ids": [      84432    ],    "status": "open",    "subject": "Help, my printer is on fire!",    "submitter_id": 76872,    "tags": [      "enterprise",      "other_tag"    ],    "type": "incident",    "updated_at": "2011-05-05T10:38:52Z",    "url": "https://company.zendesk.com/api/v2/tickets/35436",    "via": {      "channel": "web"    }  }}

### Ticket Bulk Import

  * `POST /api/v2/imports/tickets/create_many`


Accepts an array of up to 100 ticket objects.

#### Allowed For

  * Admins


#### Example Response

This endpoint returns a `job_status` [JSON object](/api-reference/ticketing/ticket-management/job_statuses/#json-format) and queues a background job to do the work. Use the [Show Job Status](/api-reference/ticketing/ticket-management/job_statuses/#show-job-status) endpoint to check for the job's completion.

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
archive_immediately| boolean| Query| false| If `true`, any ticket created with a `closed` status bypasses the normal ticket lifecycle and will be created directly in your ticket archive

#### Example body


    {  "tickets": [    {      "assignee_id": 19,      "comments": [        {          "author_id": 827,          "created_at": "2009-06-25T10:15:18Z",          "value": "This is a comment"        },        {          "author_id": 19,          "public": false,          "value": "This is a private comment"        }      ],      "description": "A description",      "requester_id": 827,      "subject": "Help",      "tags": [        "foo",        "bar"      ]    },    {      "assignee_id": 21,      "comments": [        {          "author_id": 830,          "created_at": "2009-06-25T10:15:18Z",          "value": "This is a comment"        },        {          "author_id": 21,          "public": false,          "value": "This is a private comment"        }      ],      "description": "A description",      "requester_id": 830,      "subject": "Missing Item",      "tags": [        "foo",        "bar"      ]    }  ]}

#### Code Samples

**cURL**


    curl https://{subdomain}.zendesk.com/api/v2/imports/tickets/create_many \  -v -u {email_address}/token:{api_token} -X POST \  -d '{"tickets": [{"subject": "Help!", "comments": [{ "author_id": 19, "value": "This is a comment" }]}, {"subject": "Help!!", "comments": [{ "author_id": 21, "value": "This is a comment" }]}]}' \  -H "Content-Type: application/json"

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://example.zendesk.com/api/v2/imports/tickets/create_many?archive_immediately="	method := "POST"	payload := strings.NewReader(`{  "tickets": [    {      "assignee_id": 19,      "comments": [        {          "author_id": 827,          "created_at": "2009-06-25T10:15:18Z",          "value": "This is a comment"        },        {          "author_id": 19,          "public": false,          "value": "This is a private comment"        }      ],      "description": "A description",      "requester_id": 827,      "subject": "Help",      "tags": [        "foo",        "bar"      ]    },    {      "assignee_id": 21,      "comments": [        {          "author_id": 830,          "created_at": "2009-06-25T10:15:18Z",          "value": "This is a comment"        },        {          "author_id": 21,          "public": false,          "value": "This is a private comment"        }      ],      "description": "A description",      "requester_id": 830,      "subject": "Missing Item",      "tags": [        "foo",        "bar"      ]    }  ]}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/imports/tickets/create_many")		.newBuilder()		.addQueryParameter("archive_immediately", "");RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"tickets\": [    {      \"assignee_id\": 19,      \"comments\": [        {          \"author_id\": 827,          \"created_at\": \"2009-06-25T10:15:18Z\",          \"value\": \"This is a comment\"        },        {          \"author_id\": 19,          \"public\": false,          \"value\": \"This is a private comment\"        }      ],      \"description\": \"A description\",      \"requester_id\": 827,      \"subject\": \"Help\",      \"tags\": [        \"foo\",        \"bar\"      ]    },    {      \"assignee_id\": 21,      \"comments\": [        {          \"author_id\": 830,          \"created_at\": \"2009-06-25T10:15:18Z\",          \"value\": \"This is a comment\"        },        {          \"author_id\": 21,          \"public\": false,          \"value\": \"This is a private comment\"        }      ],      \"description\": \"A description\",      \"requester_id\": 830,      \"subject\": \"Missing Item\",      \"tags\": [        \"foo\",        \"bar\"      ]    }  ]}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "tickets": [    {      "assignee_id": 19,      "comments": [        {          "author_id": 827,          "created_at": "2009-06-25T10:15:18Z",          "value": "This is a comment"        },        {          "author_id": 19,          "public": false,          "value": "This is a private comment"        }      ],      "description": "A description",      "requester_id": 827,      "subject": "Help",      "tags": [        "foo",        "bar"      ]    },    {      "assignee_id": 21,      "comments": [        {          "author_id": 830,          "created_at": "2009-06-25T10:15:18Z",          "value": "This is a comment"        },        {          "author_id": 21,          "public": false,          "value": "This is a private comment"        }      ],      "description": "A description",      "requester_id": 830,      "subject": "Missing Item",      "tags": [        "foo",        "bar"      ]    }  ]});
    var config = {  method: 'POST',  url: 'https://example.zendesk.com/api/v2/imports/tickets/create_many',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'archive_immediately': '',  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/imports/tickets/create_many?archive_immediately="
    payload = json.loads("""{  "tickets": [    {      "assignee_id": 19,      "comments": [        {          "author_id": 827,          "created_at": "2009-06-25T10:15:18Z",          "value": "This is a comment"        },        {          "author_id": 19,          "public": false,          "value": "This is a private comment"        }      ],      "description": "A description",      "requester_id": 827,      "subject": "Help",      "tags": [        "foo",        "bar"      ]    },    {      "assignee_id": 21,      "comments": [        {          "author_id": 830,          "created_at": "2009-06-25T10:15:18Z",          "value": "This is a comment"        },        {          "author_id": 21,          "public": false,          "value": "This is a private comment"        }      ],      "description": "A description",      "requester_id": 830,      "subject": "Missing Item",      "tags": [        "foo",        "bar"      ]    }  ]}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/imports/tickets/create_many")uri.query = URI.encode_www_form("archive_immediately": "")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")request.body = %q({  "tickets": [    {      "assignee_id": 19,      "comments": [        {          "author_id": 827,          "created_at": "2009-06-25T10:15:18Z",          "value": "This is a comment"        },        {          "author_id": 19,          "public": false,          "value": "This is a private comment"        }      ],      "description": "A description",      "requester_id": 827,      "subject": "Help",      "tags": [        "foo",        "bar"      ]    },    {      "assignee_id": 21,      "comments": [        {          "author_id": 830,          "created_at": "2009-06-25T10:15:18Z",          "value": "This is a comment"        },        {          "author_id": 21,          "public": false,          "value": "This is a private comment"        }      ],      "description": "A description",      "requester_id": 830,      "subject": "Missing Item",      "tags": [        "foo",        "bar"      ]    }  ]})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "job_status": {    "id": "82de0b044094f0c67893ac9fe64f1a99",    "message": "Completed at 2018-03-08 10:07:04 +0000",    "progress": 2,    "results": [      {        "action": "update",        "id": 244,        "status": "Updated",        "success": true      },      {        "action": "update",        "id": 245,        "status": "Updated",        "success": true      }    ],    "status": "completed",    "total": 2,    "url": "https://example.zendesk.com/api/v2/job_statuses/82de0b0467893ac9fe64f1a99"  }}

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)