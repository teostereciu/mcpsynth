# Audit Logs

*Source: https://developer.zendesk.com/api-reference/ticketing/account-configuration/audit_logs/*

---

## On this page

  * [JSON format](/api-reference/ticketing/account-configuration/audit_logs/#json-format)
  * [List Audit Logs](/api-reference/ticketing/account-configuration/audit_logs/#list-audit-logs)
  * [Show Audit Log](/api-reference/ticketing/account-configuration/audit_logs/#show-audit-log)
  * [Export Audit Logs](/api-reference/ticketing/account-configuration/audit_logs/#export-audit-logs)


# Audit Logs

## On this page

  * [JSON format](/api-reference/ticketing/account-configuration/audit_logs/#json-format)
  * [List Audit Logs](/api-reference/ticketing/account-configuration/audit_logs/#list-audit-logs)
  * [Show Audit Log](/api-reference/ticketing/account-configuration/audit_logs/#show-audit-log)
  * [Export Audit Logs](/api-reference/ticketing/account-configuration/audit_logs/#export-audit-logs)


The audit log shows various changes in a Zendesk account since the account was created. Records of these changes are saved indefinitely and you can view the entire change history. For more information, see [Viewing the audit log for changes](https://support.zendesk.com/hc/en-us/articles/203663196-Viewing-the-audit-log-for-changes) in Zendesk help.

The Audit Logs endpoints are only available on the Enterprise plan.

### JSON format

Audit Logs are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
action| string| true| false| Type of change made. Possible values are "create", "destroy", "exported", "login", and "update"
action_label| string| true| false| Localized string of action field
actor_id| integer| true| false| id of the user or system that initiated the change
actor_name| string| true| false| Name of the user or system that initiated the change
change_description| string| true| false| The description of the change that occurred
created_at| string| true| false| The time the audit got created
id| integer| true| false| The id automatically assigned upon creation
ip_address| string| true| false| The IP address of the user doing the audit
source_id| integer| true| false| The id of the item being audited
source_label| string| true| false| The name of the item being audited
source_type| string| true| false| Item type being audited. Typically describes the system where the change was initiated. Possible values vary based on your account's Zendesk products and activity. Common values include "apitoken", "rule", "ticket", "user", and "zendesk/app_market/app". The "rule" value is used for [automations](https://support.zendesk.com/hc/en-us/articles/4408832701850), [macros](https://support.zendesk.com/hc/en-us/articles/4408844187034), [triggers](https://support.zendesk.com/hc/en-us/articles/4408822236058), [views](https://support.zendesk.com/hc/en-us/articles/4408888828570), and other automated business rules
url| string| true| false| The URL to access the audit log

#### Example


    {  "action": "update",  "action_label": "Updated",  "actor_id": 1234,  "actor_name": "Sameer Patel",  "change_description": "Role changed from Administrator to End User",  "created_at": "2012-03-05T11:32:44Z",  "id": 498483,  "ip_address": "209.119.38.228",  "source_id": 3456,  "source_label": "John Doe",  "source_type": "user",  "url": "https://company.zendesk.com/api/v2/audit_logs/498483"}

### List Audit Logs

  * `GET /api/v2/audit_logs`


#### Allowed For

  * Admins on accounts that have audit log access


#### Pagination

  * Cursor pagination (recommended)
  * Offset pagination


See [Pagination](/api-reference/introduction/pagination/).

Returns a maximum of 100 records per page.

#### Filtering by multiple values

To filter by multiple values for the same field, repeat the filter parameter and append empty square brackets "[]" to the name of each repeated parameter. For example, to return audit logs where `action` is "create", "update", or "destroy":

`/api/v2/audit_logs?filter[action][]=create&filter[action][]=update&filter[action][]=destroy`

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
filter[action]| string| Query| false| Filter audit logs by the action
filter[actor_id]| integer| Query| false| Filter audit logs by the actor id
filter[created_at]| string| Query| false| Filter audit logs by the time of creation. When used, you must specify `filter[created_at]` twice in your request, first with the start time and again with an end time
filter[ip_address]| string| Query| false| Filter audit logs by the ip address
filter[source_id]| integer| Query| false| Filter audit logs by the source id. Requires `filter[source_type]` to also be set
filter[source_type]| string| Query| false| Filter audit logs by the source type. For example, user or rule
page| object| Query| false| Cursor-based pagination parameters (JSON:API style). Supports nested parameters: - `page[size]` \- Number of records per page (default varies by endpoint, typically 100) - `page[after]` \- Cursor token to fetch records after this position - `page[before]` \- Cursor token to fetch records before this position Example: `?page[size]=50&page[after]=eyJvIjoiaWQiLCJ2IjoiYVFFPSJ9`
per_page| integer| Query| false| Number of records to return per page. Note: Default and maximum values vary by endpoint. Check endpoint-specific documentation for limits.
sort| string| Query| false| Cursor pagination only. Sort audit logs. Default is `sort=-created_at`
sort_by| string| Query| false| Offset pagination only. Sort audit logs. Default is `sort_by=created_at`
sort_order| string| Query| false| Offset pagination only. Sort audit logs. Default is `sort_order=desc`

#### Code Samples

**curl**


    curl -g 'https://helpdesk.zendesk.com/api/v2/audit_logs?filter[source_type]=user&filter[source_id]=123' \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/audit_logs?filter[action]=&filter[actor_id]=&filter[created_at]=&filter[ip_address]=&filter[source_id]=&filter[source_type]=&page=&per_page=50&sort=&sort_by=&sort_order="	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/audit_logs")		.newBuilder()		.addQueryParameter("filter[action]", "")		.addQueryParameter("filter[actor_id]", "")		.addQueryParameter("filter[created_at]", "")		.addQueryParameter("filter[ip_address]", "")		.addQueryParameter("filter[source_id]", "")		.addQueryParameter("filter[source_type]", "")		.addQueryParameter("page", "")		.addQueryParameter("per_page", "50")		.addQueryParameter("sort", "")		.addQueryParameter("sort_by", "")		.addQueryParameter("sort_order", "");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/audit_logs',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'filter[action]': '',    'filter[actor_id]': '',    'filter[created_at]': '',    'filter[ip_address]': '',    'filter[source_id]': '',    'filter[source_type]': '',    'page': '',    'per_page': '50',    'sort': '',    'sort_by': '',    'sort_order': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/audit_logs?filter[action]=&filter[actor_id]=&filter[created_at]=&filter[ip_address]=&filter[source_id]=&filter[source_type]=&page=&per_page=50&sort=&sort_by=&sort_order="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/audit_logs")uri.query = URI.encode_www_form("filter[action]": "", "filter[actor_id]": "", "filter[created_at]": "", "filter[ip_address]": "", "filter[source_id]": "", "filter[source_type]": "", "page": "", "per_page": "50", "sort": "", "sort_by": "", "sort_order": "")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "audit_logs": [    {      "action": "update",      "actor_id": 1234,      "actor_name": "Sameer Patel",      "change_description": "Role changed from Administrator to End User",      "created_at": "2012-03-05T11:32:44Z",      "id": 498483,      "ip_address": "209.119.38.228",      "source_id": 3456,      "source_label": "John Doe",      "source_type": "user",      "url": "https://company.zendesk.com/api/v2/audit_logs/498483"    }  ]}

### Show Audit Log

  * `GET /api/v2/audit_logs/{audit_log_id}`


#### Allowed For

  * Admins on accounts that have audit-log access


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
audit_log_id| integer| Path| true| The ID of the audit log

#### Code Samples

**curl**


    curl https://helpdesk.zendesk.com/api/v2/audit_logs/{audit_log_id} \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/audit_logs/498483"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/audit_logs/498483")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/audit_logs/498483',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/audit_logs/498483"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/audit_logs/498483")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "audit_log": {    "action": "update",    "actor_id": 1234,    "actor_name": "Sameer Patel",    "change_description": "Role changed from Administrator to End User",    "created_at": "2012-03-05T11:32:44Z",    "id": 498483,    "ip_address": "209.119.38.228",    "source_id": 3456,    "source_label": "John Doe",    "source_type": "user",    "url": "https://company.zendesk.com/api/v2/audit_logs/498483"  }}

### Export Audit Logs

  * `POST /api/v2/audit_logs/export`


#### Allowed For

  * Admins on accounts that have audit log access


#### Limits

This endpoint's rate limit is different from the account-wide rate limit. The rate limit is one request per minute per account. When this limit is reached, you'll get a `429 Too Many Requests` response code.

##### Headers

API responses include usage limit information in the headers for this endpoint.


    Zendesk-RateLimit-audit-logs-export: total={number}; remaining={number}; resets={number}

Within this header, âTotalâ signifies the initial allocation, âRemainingâ indicates the remaining allowance for the current interval, and âResetsâ denotes the wait time in seconds before the limit refreshes. You can see the Total, and Interval values in the below table.

##### Details

The rate limit is one request per minute per account. If you exceed this, you'll receive the following error: "Rate limit for Audit log CSV Export exceeded. Please wait 1 minute and try again."

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
filter[action]| string| Query| false| Filter audit logs by the action
filter[actor_id]| integer| Query| false| Filter audit logs by the actor id
filter[created_at]| string| Query| false| Filter audit logs by the time of creation. When used, you must specify `filter[created_at]` twice in your request, first with the start time and again with an end time
filter[ip_address]| string| Query| false| Filter audit logs by the ip address
filter[source_id]| integer| Query| false| Filter audit logs by the source id. Requires `filter[source_type]` to also be set.
filter[source_type]| string| Query| false| Filter audit logs by the source type. For example, user or rule

#### Code Samples

**curl**


    curl https://helpdesk.zendesk.com/api/v2/audit_logs/export \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/audit_logs/export?filter[action]=&filter[actor_id]=&filter[created_at]=&filter[ip_address]=&filter[source_id]=&filter[source_type]="	method := "POST"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/audit_logs/export")		.newBuilder()		.addQueryParameter("filter[action]", "")		.addQueryParameter("filter[actor_id]", "")		.addQueryParameter("filter[created_at]", "")		.addQueryParameter("filter[ip_address]", "")		.addQueryParameter("filter[source_id]", "")		.addQueryParameter("filter[source_type]", "");RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'POST',  url: 'https://example.zendesk.com/api/v2/audit_logs/export',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'filter[action]': '',    'filter[actor_id]': '',    'filter[created_at]': '',    'filter[ip_address]': '',    'filter[source_id]': '',    'filter[source_type]': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/audit_logs/export?filter[action]=&filter[actor_id]=&filter[created_at]=&filter[ip_address]=&filter[source_id]=&filter[source_type]="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/audit_logs/export")uri.query = URI.encode_www_form("filter[action]": "", "filter[actor_id]": "", "filter[created_at]": "", "filter[ip_address]": "", "filter[source_id]": "", "filter[source_type]": "")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**202 Accepted**


    // Status 202 Accepted
    null

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)