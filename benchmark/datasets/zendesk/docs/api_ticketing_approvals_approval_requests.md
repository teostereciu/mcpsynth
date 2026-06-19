# Approval Requests

*Source: https://developer.zendesk.com/api-reference/ticketing/approvals/approval_requests/*

---

## On this page

  * [JSON format](/api-reference/ticketing/approvals/approval_requests/#json-format)
  * [List Approval Requests](/api-reference/ticketing/approvals/approval_requests/#list-approval-requests)
  * [Create Approval Request](/api-reference/ticketing/approvals/approval_requests/#create-approval-request)


# Approval Requests

## On this page

  * [JSON format](/api-reference/ticketing/approvals/approval_requests/#json-format)
  * [List Approval Requests](/api-reference/ticketing/approvals/approval_requests/#list-approval-requests)
  * [Create Approval Request](/api-reference/ticketing/approvals/approval_requests/#create-approval-request)


Approvals are requests that agents create and assign to other agents, agent groups, or end users for review and decision-making.

For more information, see [Understanding approvals and how they work](https://support.zendesk.com/hc/en-us/articles/8481179038490-Understanding-approvals-and-how-they-work).

### JSON format

Approval Requests are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
assignee_group_id| integer| false| false| The id of the group assigned to review the request
assignee_user_id| integer| false| false| The id of the user assigned to respond to the request. Also referred to as the `approver`
created_at| string| true| false| The ISO 8601 formatted date-time when the approval request was created
created_by_id| integer| true| false| The id of the user who created the approval request
id| string| true| false| Unique identifier for the approval request (ULID format)
message| string| false| false| Details and context for the approval request
origination_type| string| true| false| How the approval request was created. Allowed values are "API_ORIGINATION", "UI_ORIGINATION", "TRIGGER_ORIGINATION", "DATA_IMPORTER_ORIGINATION", "TEMPLATE_ORIGINATION", "ACTION_FLOW_ORIGINATION", or "UNKNOWN_ORIGINATION".
status| string| true| false| Current status of the approval request
subject| string| false| false| Subject line for the approval request
ticket_id| integer| false| false| The id of the ticket this approval request is attached to

### List Approval Requests

  * `GET /api/v2/approval_requests`


Lists all approval requests for the current account with optional filtering by status and assignee.

#### Allowed For

  * Admins


#### Query Parameters

Name| Type| Description
---|---|---
filter[status]| string| Filter by a comma-separated list of one or more approval statuses. Values: active, approved, rejected, withdrawn
filter[assignee_user_id]| string| Filter by a comma-separated list of assigned user ids. Maximum 100 ids
filter[assignee_group_id]| string| Filter by a comma-separated list of assigned group ids. Maximum 100 ids

#### Filtering Logic

  * When multiple values are provided for a filter, `or` logic is used. For example, `filter[status]=active,approved` is evaluated as `status=active OR status=approved`.
  * If multiple filters are applied to a single request, `AND` logic is used. For example, `filter[status]=active AND filter[assignee_user_id]=123`.
  * Each filter parameter supports a maximum 100 values.
  * Numeric ids must be valid integers.


#### Pagination

This endpoint supports cursor-based pagination. Use `after_cursor` and `before_cursor` parameters to navigate through results.

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
after_cursor| string| Query| false| Cursor for pagination. Fetch records after this cursor
before_cursor| string| Query| false| Cursor for pagination. Fetch records before this cursor
filter[assignee_group_id]| string| Query| false| Filter by a comma-separated list of assigned group ids. Maximum 100 ids.
filter[assignee_user_id]| string| Query| false| Filter by a comma-separated list of assigned user ids. Maximum 100 ids.
filter[status]| string| Query| false| Filter by a comma-separated list of one or more approval statuses. Allowed values are active, approved, rejected, withdrawn. Maximum 100 values.

#### Code Samples

**curl**


    curl -u {email_address}/token:{api_token} https://{subdomain}.zendesk.com/api/v2/approval_requests \  -H "Content-Type: application/json"

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/approval_requests?after_cursor=&before_cursor=&filter[assignee_group_id]=&filter[assignee_user_id]=&filter[status]="	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/approval_requests")		.newBuilder()		.addQueryParameter("after_cursor", "")		.addQueryParameter("before_cursor", "")		.addQueryParameter("filter[assignee_group_id]", "")		.addQueryParameter("filter[assignee_user_id]", "")		.addQueryParameter("filter[status]", "");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/approval_requests',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'after_cursor': '',    'before_cursor': '',    'filter[assignee_group_id]': '',    'filter[assignee_user_id]': '',    'filter[status]': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/approval_requests?after_cursor=&before_cursor=&filter[assignee_group_id]=&filter[assignee_user_id]=&filter[status]="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/approval_requests")uri.query = URI.encode_www_form("after_cursor": "", "before_cursor": "", "filter[assignee_group_id]": "", "filter[assignee_user_id]": "", "filter[status]": "")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

**curl with single filter**


    curl "https://{subdomain}.zendesk.com/api/v2/approval_requests?filter[status]=active&filter[assignee_user_id]=12345" \  -v -u {email_address}:{password}

**curl with multiple filter values**


    curl "https://{subdomain}.zendesk.com/api/v2/approval_requests?filter[status]=active,approved&filter[assignee_user_id]=123,456" \  -v -u {email_address}:{password}

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "approval_requests": [    {      "assignee_user": {        "id": 12345,        "name": "Jane Approver"      },      "clarification_flow_messages": [],      "created_at": "2025-02-26T10:30:00Z",      "created_by_user": {        "id": 789,        "name": "John Requester",        "photo": {          "content_url": "https://example.zendesk.com/photos/789.jpg"        }      },      "decided_at": null,      "decisions": [],      "id": "01HX123ABC",      "message": "Please approve the software license request",      "origination_type": "API_ORIGINATION",      "status": "active",      "subject": "Software License Approval",      "ticket_id": 101,      "withdrawn_reason": null    },    {      "assignee_group": {        "id": 456,        "name": "Approval Team"      },      "clarification_flow_messages": [        {          "author": {            "avatar": "https://example.zendesk.com/avatars/999.jpg",            "email": "[[email protected]](/cdn-cgi/l/email-protection)",            "id": 999,            "name": "Mike Approver",            "role": "agent"          },          "created_at": "2025-02-25T15:00:00Z",          "id": "msg_123",          "message": "Can you provide more details about the expected ROI?"        }      ],      "created_at": "2025-02-25T14:15:00Z",      "created_by_user": {        "id": 888,        "name": "Sarah Requester",        "photo": {          "content_url": "https://example.zendesk.com/photos/888.jpg"        }      },      "decided_at": "2025-02-25T16:30:00Z",      "decisions": [        {          "decided_at": "2025-02-25T16:30:00Z",          "decided_by_user": {            "id": 999,            "name": "Mike Approver",            "photo": {              "content_url": "https://example.zendesk.com/photos/999.jpg"            }          },          "decision_notes": "Approved for Q1 budget",          "origination_type": "UI_ORIGINATION",          "status": "approved"        }      ],      "id": "01HX123DEF",      "message": "Please approve the hardware request",      "origination_type": "UI_ORIGINATION",      "status": "approved",      "subject": "Hardware Request",      "ticket_id": 102,      "withdrawn_reason": null    }  ],  "links": {    "next": null,    "prev": null  },  "meta": {    "after_cursor": null,    "before_cursor": null,    "has_more": false  }}

### Create Approval Request

  * `POST /api/v2/approval_requests`


Creates an approval request for a ticket.

When manual approval requests are turned off for the account, approval requests can still be created through this API. Approval requests created by the API have a `Sent by` value of `API`.

#### Allowed For

  * System users (flowstate)
  * Agents


#### Example body


    {  "assignee_user_id": 456,  "message": "Please approve this request for a new laptop for the engineering team",  "subject": "Laptop Purchase Approval",  "ticket_id": 123}

#### Code Samples

**Curl**


    curl --request POST https://example.zendesk.com/api/v2/approval_requests \--header "Content-Type: application/json" \-u {email_address}/token:{api_token} \--data-raw '{  "assignee_user_id": 456,  "message": "Please approve this request for a new laptop for the engineering team",  "subject": "Laptop Purchase Approval",  "ticket_id": 123}'

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://example.zendesk.com/api/v2/approval_requests"	method := "POST"	payload := strings.NewReader(`{  "assignee_user_id": 456,  "message": "Please approve this request for a new laptop for the engineering team",  "subject": "Laptop Purchase Approval",  "ticket_id": 123}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/approval_requests")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"assignee_user_id\": 456,  \"message\": \"Please approve this request for a new laptop for the engineering team\",  \"subject\": \"Laptop Purchase Approval\",  \"ticket_id\": 123}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "assignee_user_id": 456,  "message": "Please approve this request for a new laptop for the engineering team",  "subject": "Laptop Purchase Approval",  "ticket_id": 123});
    var config = {  method: 'POST',  url: 'https://example.zendesk.com/api/v2/approval_requests',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/approval_requests"
    payload = json.loads("""{  "assignee_user_id": 456,  "message": "Please approve this request for a new laptop for the engineering team",  "subject": "Laptop Purchase Approval",  "ticket_id": 123}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/approval_requests")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")request.body = %q({  "assignee_user_id": 456,  "message": "Please approve this request for a new laptop for the engineering team",  "subject": "Laptop Purchase Approval",  "ticket_id": 123})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

**curl (assign to group)**


    curl https://{subdomain}.zendesk.com/api/v2/approval_requests \  -H "Content-Type: application/json" -X POST \  -d '{"message": "approval description", "subject": "approval subject", "assignee_group_id": 789, "ticket_id": 123}' \  -v -u {email_address}/token:{api_token}

#### Example response(s)

**201 Created**


    // Status 201 Created
    {  "approval_request": {    "assignee_group_id": null,    "assignee_user_id": 456,    "created_at": "2026-01-23T19:02:36Z",    "created_by_id": 789,    "id": "01KFP3S9EVXF9CKAYY080NV98C",    "message": "Please approve this request for a new laptop for the engineering team",    "origination_type": "API_ORIGINATION",    "status": "active",    "subject": "Laptop Purchase Approval",    "ticket_id": 123  }}

**422 Unprocessable Entity**


    // Status 422 Unprocessable Entity
    {  "errors": [    {      "code": "ApprovalRequestCreationFailed",      "title": "Approval request couldn't be sent because one active, approved, or denied request already exists"    }  ]}

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)