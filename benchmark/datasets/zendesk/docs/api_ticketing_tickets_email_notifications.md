# Email Notifications

*Source: https://developer.zendesk.com/api-reference/ticketing/tickets/email_notifications/*

---

## On this page

  * [Delivery Status Reference](/api-reference/ticketing/tickets/email_notifications/#delivery-status-reference)
  * [JSON format](/api-reference/ticketing/tickets/email_notifications/#json-format)
  * [List Email Notifications](/api-reference/ticketing/tickets/email_notifications/#list-email-notifications)
  * [Show Email Notification](/api-reference/ticketing/tickets/email_notifications/#show-email-notification)
  * [Show Many Email Notifications](/api-reference/ticketing/tickets/email_notifications/#show-many-email-notifications)


# Email Notifications

## On this page

  * [Delivery Status Reference](/api-reference/ticketing/tickets/email_notifications/#delivery-status-reference)
  * [JSON format](/api-reference/ticketing/tickets/email_notifications/#json-format)
  * [List Email Notifications](/api-reference/ticketing/tickets/email_notifications/#list-email-notifications)
  * [Show Email Notification](/api-reference/ticketing/tickets/email_notifications/#show-email-notification)
  * [Show Many Email Notifications](/api-reference/ticketing/tickets/email_notifications/#show-many-email-notifications)


Use the Email Notifications API to find out what happened after an email was sent to its recipients. For example, you can use the API to determine if an outbound email was actually delivered and, if not, understand why based on the delivery status codes returned by the email service providers upon request; For more information about email notifications, see [Understanding email delivery failures in the Zendesk Agent Workspace](https://support.zendesk.com/hc/en-us/articles/7917145637530) in Zendesk help.

### Delivery Status Reference

Every recipient from an email notification includes a delivery status information, with "id", "name", "code", and "message" properties. This provides more information directly from the email service providers during the email delivery transaction.

The following table contains for possible values for delivery status:

Id| Name| SMTP Status Code| Description
---|---|---|---
0| NONE| 0| No delivery failure responses received
1| UNRECOGNIZED_INTERNAL_ERROR| 1| Email failed to deliver. Try sending again
2| UNRECOGNIZED_EXTERNAL_ERROR| 2| Email failed to deliver. Try sending again
3| NET_SMTP_SYNTAX_ERROR| 3| Email failed to deliver. Try sending again
4| ACTIVE_RECORD_NOT_FOUND_ERROR| 4| Email failed to deliver. Try sending again
6| SYNTAX_ERROR_COMMAND_UNRECOGNIZED| 500| Email failed to deliver. The SMTP command used was not recognized due to a syntax error, or is not supported by the given protocol or SMTP server implementation
7| AUTHENTICATION_EXCHANGE_LINE_TOO_LONG| 500 5.5.6| Email failed to deliver. Authentication exchange line is too long
8| SYNTAX_ERROR_IN_ARGUMENTS| 501| Recipient server rejected email. Syntax error in parameters or arguments
9| CANNOT_BASE64_DECODE_CLIENT_RESPONSES| 501 5.5.2| Recipient server rejected email. Cannot base64-decode client responses
10| CLIENT_INITIATED_AUTHENTICATION_EXCHANGE| 501 5.7.0| Recipient server rejected email. Client initiated authentication exchange
11| COMMAND_NOT_IMPLEMENTED| 502| Email failed to deliver. Command not implemented
12| BAD_SEQUENCE_OF_COMMANDS| 503| Email failed to deliver. Bad sequence of commands
13| COMMAND_PARAMETER_NOT_IMPLEMENTED| 504| Email failed to deliver. Command parameter is not implemented
14| UNRECOGNIZED_AUTHENTICATION_TYPE| 504 5.5.4| Email failed to deliver. Unrecognized authentication type
15| SMTP_SERVICE_NOT_AVAILABLE| 505| Recipient server rejected email. SMTP service not available
16| BAD_EMAIL_ADDRESS| 510| Recipient server rejected email. Email address rejected due to bad email address. Email does not exist or was misspelled. Check the recipient's email for typos
17| RECIPIENT_EMAIL_ADDRESS_INVALID| 511| Recipient server rejected email. Recipient's email address is incorrect or invalid
18| SENDER_EMAIL_ADDRESS_BLOCKED_OR_SUSPENDED| 517| Email failed to deliver.
19| IP_AND_SPF_RECORD_DO_NOT_MATCH| 520| Email failed to deliver. IP and SPF record do not match
20| SERVER_DOES_NOT_ACCEPT_MAIL| 521| Recipient server rejected email. The server does not accept mail
21| SENDER_IP_ON_BLOCKLIST| 522| Email failed to deliver
22| ENCRYPTION_NEEDED_OR_EMAIL_TOO_LARGE| 523| Recipient server rejected email. Encryption needed or email size exceeds the recipient's email server limits. These limits are set by the email server and only allow emails of a specific size to be accepted
23| DISABLED_RECIPIENT_ADDRESS| 525| Recipient server rejected email. Email address disabled. The recipient address is disabled
24| AUTHENTICATION_REQUIRED| 530| Email failed to deliver. Authentication is required
26| AUTHENTICATION_CREDENTIALS_INVALID| 534 5.7.8| Email failed to deliver. The authentication credentials are invalid
25| AUTHENTICATION_MECHANISM_WEAK| 534 5.7.9| Email failed to deliver. The authentication mechanism is too weak
27| ENCRYPTION_REQUIRED| 538 5.7.11| Email failed to deliver. Encryption is required for the requested authentication mechanism
28| RECIPIENT_ADDRESS_REJECTED_INACTIVE| 540| Recipient server rejected email. The recipient address was rejected
29| MAILBOX_UNAVAILABLE| 550| Recipient server rejected email. Requested action not taken: mailbox unavailable (for example, the mailbox was not found or unavailable, no access is permitted, or a command was rejected for policy reasons)
38| MAILBOX_INVALID| 550 5.0.0| Recipient server rejected email. Invalid mailbox; recommend rechecking email address and domain. Invalid mailbox. Re-check the email address and domain
39| USER_DOES_NOT_EXIST| 550 5.1.1| Recipient server rejected email. User does not exist; recommend checking for typos. User does not exist. Check for typos in the email address
40| RECIPIENT_IS_INACTIVE| 550 5.2.1| Recipient server rejected email. Inactive email address. The email address is inactive
30| USER_NOT_LOCAL| 551| Recipient server rejected email. User not local; please try forward-path
31| MAILBOX_FULL| 552| Recipient server rejected email. Recipient's inbox is full
32| MAILBOX_NAME_NOT_ALLOWED| 553| Recipient server rejected email. Requested action not taken: mailbox name not allowed
33| TRANSACTION_FAILED| 554| Recipient server rejected email. Transaction has failed (or, in the case of a connection-opening response, no SMTP service here)
34| MESSAGE_TOO_BIG| 554 5.3.4| Recipient server rejected email. Message too large
35| DOMAIN_DOES_NOT_ACCEPT_MAIL| 556| Recipient server rejected email. The domain does not accept email
36| MESSAGE_REJECTED_SUSPECTED_SPAM| 558| Recipient server rejected email. The message content was rejected due to suspected spam
37| RECIPIENT_ADDRESS_REJECTED| 577| Recipient server rejected email. The recipient address was rejected. This could be due to an undeliverable address or the user is unknown in the relay recipient table
41| RECIPIENT_REJECTED_ADDRESS| 541| Recipient server rejected email.
42| HEADER_SIZE_EXCEEDS_FIXED_MAXIMUM_SIZE| 552 5.3.4| Recipient server rejected email. Message too large
43| FILE_TYPES_BLOCKED| 552 5.7.0| Recipient server rejected email. Potential security risk. The email includes insecure executable files or certain links
44| AUTHENTICATION_INVALID| 535| Recipient server rejected email. Authentication credentials invalid. The recipient server denied authentication preventing email delivery
45| AUTHENTICATION_UNSUCCESSFUL| 535 5.7.139| Recipient server rejected email. Authentication unsuccessful due to expiring passwords, forced resets, or policy restrictions
46| EC_INTEGRATION_ERROR| EC-001| The email delivery failed because the Microsoft Exchange connection is inactive or restricted
47| EC_INSUFFICIENT_STORAGE| EC-002| Microsoft Exchange rejected the handoff of this email to its server due to insufficient storage
48| EC_ERROR| EC-003| Microsoft Exchange rejected the handoff of this email to its server
49| EC_INVALID_RECIPIENT| EC-004| Recipient server rejected email. Email address rejected due to bad email address. Email does not exist or was misspelled. Check the recipient's email for typos
50| EC_THROTTLED| EC-005| Microsoft Exchange rejected the handoff of this email to its server due to Microsoft API limits and Zendesk retry limits being reached
51| EC_AUTHENTICATION_INVALID| EC-006| Microsoft Exchange rejected the handoff of this email to its server. Authentication issue
52| INCORRECT_AUTHENTICATION_LEVEL| 550 5.7.515| Recipient server rejected email. Authentication unsuccessful. From address doesn't meet the required authentication level requirements defined by the recipient
53| NO_SUCH_USER| 585 5.1.1| Recipient server rejected email. User does not exist. Check for typos in the email address
54| NOT_ALLOWED_TO_RECEIVE_EMAIL| 542 5.0.0| Recipient server rejected email. Account is not allowed to receive email

### JSON format

Email Notifications are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
comment_id| integer| true| false| The comment ID associated to this email notification
created_at| string| true| false| When this email notification was created
email_id| string| true| false| The email ID of this email notification
message_id| string| true| false| The value of the Message-Id header of the email
notification_id| integer| true| false| The notification id of this email notification
recipients| array| true| false| The list of recipients associated to this email notification
ticket_id| integer| true| false| The ticket ID associated to this email notification
updated_at| string| true| false| When this email notification was last updated
url| string| true| false| The API url of this email notification

#### Example


    {  "comment_id": 7824075373565,  "created_at": "2024-02-21T23:13:07Z",  "email_id": "01HQ6Z3DE28F34XBFCYH0SRM95",  "message_id": "<[[email protected]](/cdn-cgi/l/email-protection)>",  "notification_id": 7824075373693,  "recipients": [    {      "delivery_status": {        "code": "530 5.7.0",        "id": 24,        "message": "Email failed to deliver. Status code: 530",        "name": "authentication_required"      },      "email_address": "[[email protected]](/cdn-cgi/l/email-protection)",      "user_id": 7612709251581    }  ],  "ticket_id": 623,  "updated_at": "2024-02-21T23:13:07Z",  "url": "https://example.zendesk.com/api/v2/email_notifications/7824075373693"}

### List Email Notifications

  * `GET /api/v2/email_notifications?filter={filter}`


#### Allowed For

  * Agents


#### Request parameters

##### Filters

**Important** : You must specify a `filter` query parameter to narrow the scope of the search for this endpoint.

  * By notification: `api/v2/email_notifications?filter[notification_id]=7824075373693`
  * By comment: `api/v2/email_notifications?filter[comment_id]=782407`
  * By ticket: `api/v2/email_notifications?filter[ticket_id]=623`


##### Pagination

By default, a maximum of 100 email notifications are included per page. Use cursor-based pagination parameters (`page[after]` and `page[before]`) to navigate the records (can't be used together in the same request). See [Pagination](/api-reference/introduction/pagination/) for more details.

##### Sorting

By default, email notifications are sorted by creation time (newest first). The query parameter is not supported for this endpoint.

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
filter| object| Query| true| Filters the email notifications by ticket, comment, or notification id.
per_page| integer| Query| false| The number of records to return per page
sort| string| Query| false| The field to sort the list. Possible values are "created_at", "updated_at" (ascending order) or "-created_at", "-updated_at" (descending order)

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/email_notifications \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/email_notifications?filter=&per_page=&sort=updated_at"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/email_notifications")		.newBuilder()		.addQueryParameter("filter", "")		.addQueryParameter("per_page", "")		.addQueryParameter("sort", "updated_at");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/email_notifications',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'filter': '',    'per_page': '',    'sort': 'updated_at',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/email_notifications?filter=&per_page=&sort=updated_at"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/email_notifications")uri.query = URI.encode_www_form("filter": "", "per_page": "", "sort": "updated_at")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "email_notifications": [    {      "comment_id": 7824075373565,      "created_at": "2024-02-21T23:13:07Z",      "email_id": "01HQ6Z3DE28F34XBFCYH0SRM95",      "message_id": "<[[email protected]](/cdn-cgi/l/email-protection)>",      "notification_id": 7824075373693,      "recipients": [        {          "delivery_status": {            "code": "530 5.7.0",            "id": 24,            "message": "Email failed to deliver. Status code: 530",            "name": "authentication_required"          },          "email_address": "[[email protected]](/cdn-cgi/l/email-protection)",          "user_id": 7612709251581        }      ],      "ticket_id": 623,      "updated_at": "2024-02-21T23:13:07Z",      "url": "https://example.zendesk.com/api/v2/email_notifications/7824075373693"    },    {      "comment_id": 7975134672637,      "created_at": "2024-05-16T20:15:20Z",      "email_id": "01HY1GPZVDQAQK3CKWD3MFPX7Z",      "message_id": "<[[email protected]](/cdn-cgi/l/email-protection)>",      "notification_id": 7975134674301,      "recipients": [        {          "delivery_status": {            "code": "538 5.7.11",            "id": 27,            "message": "Email failed to deliver. Status code: 538 5.7.11",            "name": "encryption_required"          },          "email_address": "[[email protected]](/cdn-cgi/l/email-protection)",          "user_id": 1100021780374        },        {          "delivery_status": {            "code": "200",            "id": 5,            "message": "Email was delivered.",            "name": "delivered"          },          "email_address": "[[email protected]](/cdn-cgi/l/email-protection)",          "user_id": 6020924697213        }      ],      "ticket_id": 626,      "updated_at": "2024-05-16T20:15:20Z",      "url": "https://example.zendesk.com/api/v2/email_notifications/7975134674301"    },    {      "comment_id": 7975121425149,      "created_at": "2024-05-16T20:15:58Z",      "email_id": "01HY1GR2T8VKSPZ73TMCWAFWS3",      "message_id": "<[[email protected]](/cdn-cgi/l/email-protection)>",      "notification_id": 7975121425661,      "recipients": [        {          "delivery_status": {            "code": "0",            "id": 0,            "message": "No delivery response has been received.",            "name": "none"          },          "email_address": "[[email protected]](/cdn-cgi/l/email-protection)",          "user_id": 1100021780374        },        {          "delivery_status": {            "code": "501",            "id": 8,            "message": "Recipient server rejected email. Status code: 501",            "name": "syntax_error_in_arguments"          },          "email_address": "[[email protected]](/cdn-cgi/l/email-protection)",          "user_id": 6020924697213        }      ],      "ticket_id": 626,      "updated_at": "2024-05-16T20:15:58Z",      "url": "https://example.zendesk.com/api/v2/email_notifications/7975121425661"    }  ]}

### Show Email Notification

  * `GET /api/v2/email_notifications/{notification_id}`


Shows details on an email notification. You can get the value of the `notification_id` parameter by listing the ticket's outbound emails.

#### Allowed For

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
notification_id| integer| Path| true| The id of the email notification

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/email_notifications/{notification_id} \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/email_notifications/7824075373693"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/email_notifications/7824075373693")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/email_notifications/7824075373693',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/email_notifications/7824075373693"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/email_notifications/7824075373693")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "email_notification": {    "comment_id": 7824075373565,    "created_at": "2024-02-21T23:13:07Z",    "email_id": "01HQ6Z3DE28F34XBFCYH0SRM95",    "message_id": "<[[email protected]](/cdn-cgi/l/email-protection)>",    "notification_id": 7824075373693,    "recipients": [      {        "delivery_status": {          "code": "530 5.7.0",          "id": 24,          "message": "Email failed to deliver. Status code: 530",          "name": "authentication_required"        },        "email_address": "[[email protected]](/cdn-cgi/l/email-protection)",        "user_id": 7612709251581      }    ],    "ticket_id": 623,    "updated_at": "2024-02-21T23:13:07Z",    "url": "https://example.zendesk.com/api/v2/email_notifications/7824075373693"  }}

### Show Many Email Notifications

  * `GET /api/v2/email_notifications/show_many`


Shows details of many email notifications. Allows you to query by providing a list of notifications, comments, or tickets IDs.

#### Allowed For

  * Agents


#### Filters

  * By notification: `?ids=8433702508541,8433348111869`
  * By comment: `?comment_ids=8433348111741,8433544226045,8433702508413`
  * By ticket: `?ticket_ids=730,723`


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
comment_ids| string| Query| false| Comma-separated list of comment ids. One of ids, comment_ids, or ticket_ids is required.
ids| string| Query| false| Comma-separated list of notification ids. One of ids, comment_ids, or ticket_ids is required.
ticket_ids| string| Query| false| Comma-separated list of ticket ids. One of ids, comment_ids, or ticket_ids is required.

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/email_notifications/show_many?ids={ids} \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/email_notifications/show_many?comment_ids=8433348111741%2C8433544226045%2C8433702508413&ids=8433702508541%2C8433348111869&ticket_ids=35436%2C35437"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/email_notifications/show_many")		.newBuilder()		.addQueryParameter("comment_ids", "8433348111741,8433544226045,8433702508413")		.addQueryParameter("ids", "8433702508541,8433348111869")		.addQueryParameter("ticket_ids", "35436,35437");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/email_notifications/show_many',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'comment_ids': '8433348111741%2C8433544226045%2C8433702508413',    'ids': '8433702508541%2C8433348111869',    'ticket_ids': '35436%2C35437',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/email_notifications/show_many?comment_ids=8433348111741%2C8433544226045%2C8433702508413&ids=8433702508541%2C8433348111869&ticket_ids=35436%2C35437"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/email_notifications/show_many")uri.query = URI.encode_www_form("comment_ids": "8433348111741,8433544226045,8433702508413", "ids": "8433702508541,8433348111869", "ticket_ids": "35436,35437")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "email_notification": {    "comment_id": 7824075373565,    "created_at": "2024-02-21T23:13:07Z",    "email_id": "01HQ6Z3DE28F34XBFCYH0SRM95",    "message_id": "<[[email protected]](/cdn-cgi/l/email-protection)>",    "notification_id": 7824075373693,    "recipients": [      {        "delivery_status": {          "code": "530 5.7.0",          "id": 24,          "message": "Email failed to deliver. Status code: 530",          "name": "authentication_required"        },        "email_address": "[[email protected]](/cdn-cgi/l/email-protection)",        "user_id": 7612709251581      }    ],    "ticket_id": 623,    "updated_at": "2024-02-21T23:13:07Z",    "url": "https://example.zendesk.com/api/v2/email_notifications/7824075373693"  }}

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)