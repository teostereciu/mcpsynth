# Group SLA Policies

*Source: https://developer.zendesk.com/api-reference/ticketing/business-rules/group_sla_policies/*

---

## On this page

  * [JSON format](/api-reference/ticketing/business-rules/group_sla_policies/#json-format)
  * [List Group SLA Policies](/api-reference/ticketing/business-rules/group_sla_policies/#list-group-sla-policies)
  * [Show Group SLA Policy](/api-reference/ticketing/business-rules/group_sla_policies/#show-group-sla-policy)
  * [Create Group SLA Policy](/api-reference/ticketing/business-rules/group_sla_policies/#create-group-sla-policy)
  * [Update Group SLA Policy](/api-reference/ticketing/business-rules/group_sla_policies/#update-group-sla-policy)
  * [Delete Group SLA Policy](/api-reference/ticketing/business-rules/group_sla_policies/#delete-group-sla-policy)
  * [Reorder Group SLA Policies](/api-reference/ticketing/business-rules/group_sla_policies/#reorder-group-sla-policies)
  * [Retrieve Supported Filter Definition Items](/api-reference/ticketing/business-rules/group_sla_policies/#retrieve-supported-filter-definition-items)


# Group SLA Policies

## On this page

  * [JSON format](/api-reference/ticketing/business-rules/group_sla_policies/#json-format)
  * [List Group SLA Policies](/api-reference/ticketing/business-rules/group_sla_policies/#list-group-sla-policies)
  * [Show Group SLA Policy](/api-reference/ticketing/business-rules/group_sla_policies/#show-group-sla-policy)
  * [Create Group SLA Policy](/api-reference/ticketing/business-rules/group_sla_policies/#create-group-sla-policy)
  * [Update Group SLA Policy](/api-reference/ticketing/business-rules/group_sla_policies/#update-group-sla-policy)
  * [Delete Group SLA Policy](/api-reference/ticketing/business-rules/group_sla_policies/#delete-group-sla-policy)
  * [Reorder Group SLA Policies](/api-reference/ticketing/business-rules/group_sla_policies/#reorder-group-sla-policies)
  * [Retrieve Supported Filter Definition Items](/api-reference/ticketing/business-rules/group_sla_policies/#retrieve-supported-filter-definition-items)


A Group Service Level Agreement (SLA) is a documented agreement between a support provider and their customers that specifies support performance measures for a group of agents. Group SLAs are often expressed as follows:

*For urgent incidents, the tier 1 group solves or reassigns the ticket to another group within 10 minutes. *For high-priority incidents, the tier 3 group solves or reassign the ticket to another group the ticket within 30 minutes.

Because there may be different Group SLAs for each customer or group of customers, the support provider should define a Group SLA policy for each unique Group SLA's requirements.

All related endpoints are available on the Enterprise plans and above. Only admins are allowed to access the endpoints.

### JSON format

Group SLA Policies are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
created_at| string| true| false| The time the Group SLA policy was created
description| string| false| false| The description of the Group SLA policy
filter| object| false| true| An object that describes the conditions a ticket must match for a Group SLA policy to be applied to the ticket. See Filter.
id| string| true| false| Automatically assigned when created
policy_metrics| array| false| false| Array of policy metric objects
position| integer| false| false| Position of the Group SLA policy. This position determines the order in which policies are matched to tickets. If not specified, the Group SLA policy is added at the last position
title| string| false| true| The title of the Group SLA policy
updated_at| string| true| false| The time of the last update of the Group SLA policy
url| string| true| false| URL of the Group SLA policy record

#### Filter

A filter checks the value of ticket fields and selects the ticket if the conditions are met. The filter is represented as a JSON object with two arrays of one or more conditions. For Group SLA Policy objects, at least one filter with the field "group_id" is mandatory.

**Example**


    {   "filter": {     "all": [       { "field": "group_id", "operator": "includes", "value": [10001] },     ]   }}

The array lists all the conditions that must be met.

Name| Type| Description
---|---|---
`all`| array| Logical AND. Tickets must fulfill all of the conditions to be considered matching

Each condition in an array has the following properties:

Name| Type| Description
---|---|---
field| string| The name of a ticket field
operator| string| A comparison operator
value| string| The value of a ticket field

**Example**


    { "field": "group_id", "operator": "includes", "value": [10001] }

See [Conditions reference](/documentation/ticketing/reference-guides/conditions-reference) for the list of fields, allowed operators, and values of the conditions.

#### Policy Metric

An object that describes the metric targets for each value of the priority field.

Policy metrics are represented as simple flat JSON objects with have the following properties:

Name| Type| Comment
---|---|---
priority| string| Priority that a ticket must match
metric| string| The definition of the time that is being measured. See Metrics
target| integer| The total time within which the end-state for a metric should be met, measured in minutes
target_in_seconds| integer| The total time within which the end-state for a metric should be met, measured in seconds
business_hours| boolean| Whether the metric targets are being measured in business hours or calendar hours

**Example**


    {  "priority": "low",  "metric": "group_ownership_time",  "target": 3600,  "business_hours": false}

#### Metrics

Metric| Value
---|---
Group Ownership Time| group_ownership_time

#### Example


    {  "created_at": "2023-03-17T22:50:26Z",  "description": "Group: Tier 1",  "filter": {    "all": []  },  "id": "01H078CBDY28BZG7P6BONY09DN",  "policy_metrics": [    {      "business_hours": false,      "metric": "group_ownership_time",      "priority": "low",      "target": 3600    }  ],  "position": 3,  "title": "Tier 1",  "updated_at": "2023-03-17T22:50:26Z",  "url": "https://company.zendesk.com/api/v2/group_slas/policies/01H078CBDY28BZG7P6BONY09DN"}

### List Group SLA Policies

  * `GET /api/v2/group_slas/policies`


#### Allowed For

  * Admins


#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/group_slas/policies \  -H "Content-Type: application/json" \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/group_slas/policies"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/group_slas/policies")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/group_slas/policies',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/group_slas/policies"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/group_slas/policies")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "count": 1,  "group_sla_policies": [    {      "description": "For low priority tickets, the Tier 1 group will solve or reassign the ticket in one hour.",      "filter": {        "all": [          {            "field": "group_ownership_time",            "operator": "includes",            "value": [              6            ]          }        ]      },      "id": "01H078CBDY28BZG7P6BONY09DN",      "policy_metrics": [        {          "business_hours": false,          "metric": "group_ownership_time",          "priority": "low",          "target": 3600        }      ],      "position": 3,      "title": "Incidents",      "url": "https://{subdomain}.zendesk.com/api/v2/group_sla/policies/01H078CBDY28BZG7P6BONY09DN"    }  ],  "next_page": null,  "previous_page": null}

### Show Group SLA Policy

  * `GET /api/v2/group_slas/policies/{group_sla_policy_id}`


#### Allowed For

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
group_sla_policy_id| integer| Path| true| The id of the Group SLA policy

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/group_slas/policies/{group_sla_policy_id} \  -H "Content-Type: application/json" \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/group_slas/policies/36"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/group_slas/policies/36")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/group_slas/policies/36',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/group_slas/policies/36"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/group_slas/policies/36")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "group_sla_policy": {    "description": "Low priority tickets assigned to the group with id 6 will be completed or reassigned in one hour.",    "filter": {      "all": [        {          "field": "group_id",          "operator": "includes",          "value": [            6          ]        }      ]    },    "id": "01H078CBDY28BZG7P6BONY09DN",    "policy_metrics": [      {        "business_hours": false,        "metric": "group_ownership_time",        "priority": "low",        "target": 3600      }    ],    "position": 3,    "title": "Incidents",    "url": "https://{subdomain}.zendesk.com/api/v2/group_sla/policies/01H078CBDY28BZG7P6BONY09DN"  }}

### Create Group SLA Policy

  * `POST /api/v2/group_slas/policies`


#### Allowed For

  * Admins


#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/group_slas/policies \  -H "Content-Type: application/json" \  -d '{        "group_sla_policy": {          "title": "Tier 1 Group SLA",          "description": "Tier 1 Group SLA",          "position": 3,          "filter": {            "all": [{ "field": "group_id", "operator": "includes", "value": [6] }]          },          "policy_metrics": [            { "priority": "normal", "metric": "group_ownership_time", "target": 1800, "business_hours": true },            { "priority": "urgent", "metric": "group_ownership_time", "target": 600, "business_hours": false },          ]        }      }' \  -v -u {email_address}/token:{api_token} -X POST

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/group_slas/policies"	method := "POST"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/group_slas/policies")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'POST',  url: 'https://example.zendesk.com/api/v2/group_slas/policies',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/group_slas/policies"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/group_slas/policies")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**201 Created**


    // Status 201 Created
    {  "group_sla_policy": {    "description": "The group with id 6 will have to solve or reassign normal priority tickets in 30 minutes and urgent tickets in 10.",    "filter": {      "all": [        {          "field": "group_ownership_time",          "operator": "includes",          "value": [            6          ]        }      ]    },    "id": "01H078CBDY28BZG7P6BONY09DN",    "policy_metrics": [      {        "business_hours": false,        "metric": "group_ownership_time",        "priority": "normal",        "target": 1800      },      {        "business_hours": false,        "metric": "group_ownership_time",        "priority": "urgent",        "target": 600      }    ],    "position": 3,    "title": "Incidents",    "url": "https://{subdomain}.zendesk.com/api/v2/group_slas/policies/01H078CBDY28BZG7P6BONY09DN"  }}

### Update Group SLA Policy

  * `PUT /api/v2/group_slas/policies/{group_sla_policy_id}`


Updates the specified policy.

#### Allowed For

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
group_sla_policy_id| integer| Path| true| The id of the Group SLA policy

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/group_slas/policies/{group_sla_policy_id} \  -H "Content-Type: application/json" \  -d '{        "group_sla_policy": {          "title": "Tier 1 Group SLA",          "description": "Tier 1 Group SLA",          "position": 3,          "filter": {            "all": [{ "field": "group_id", "operator": "includes", "value": [6] }]          },          "policy_metrics": [            { "priority": "normal", "metric": "group_ownership_time", "target": 1800, "business_hours": true },            { "priority": "urgent", "metric": "group_ownership_time", "target": 600, "business_hours": false },          ]        }      }' \  -v -u {email_address}/token:{api_token} -X PUT

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/group_slas/policies/36"	method := "PUT"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/group_slas/policies/36")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'PUT',  url: 'https://example.zendesk.com/api/v2/group_slas/policies/36',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/group_slas/policies/36"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/group_slas/policies/36")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "group_sla_policy": {    "description": "Normal priority tickets assigned to the groups 6 or 7 will be completed or reassigned in 30 minutes.",    "filter": {      "all": [        {          "field": "group_id",          "operator": "includes",          "value": [            6,            7          ]        }      ]    },    "id": "01H078CBDY28BZG7P6BONY09DN",    "policy_metrics": [      {        "business_hours": false,        "metric": "group_ownership_time",        "priority": "normal",        "target": 1800      }    ],    "position": 3,    "title": "Urgent Incidents",    "url": "https://{subdomain}.zendesk.com/api/v2/group_slas/policies/01H078CBDY28BZG7P6BONY09DN"  }}

### Delete Group SLA Policy

  * `DELETE /api/v2/group_slas/policies/{group_sla_policy_id}`


#### Allowed For

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
group_sla_policy_id| integer| Path| true| The id of the Group SLA policy

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/group_slas/policies/{group_sla_policy_id} \  -H "Content-Type: application/json" \  -v -u {email_address}/token:{api_token} -X DELETE

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/group_slas/policies/36"	method := "DELETE"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/group_slas/policies/36")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("DELETE", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'DELETE',  url: 'https://example.zendesk.com/api/v2/group_slas/policies/36',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/group_slas/policies/36"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"DELETE",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/group_slas/policies/36")request = Net::HTTP::Delete.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**204 No Content**


    // Status 204 No Content
    null

### Reorder Group SLA Policies

  * `PUT /api/v2/group_slas/policies/reorder`


#### Allowed For

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
group_sla_policy_ids| array| Query| false| The ids of the Group SLA policies to reorder

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/group_slas/policies/reorder \  -H "Content-Type: application/json" -X PUT \  -d '{"group_sla_policy_ids": ["01H078CBDY28BZG7P6BONY09DN", "01K078CBDY28BZG7P9BONY09DN"]}' \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/group_slas/policies/reorder?group_sla_policy_ids="	method := "PUT"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/group_slas/policies/reorder")		.newBuilder()		.addQueryParameter("group_sla_policy_ids", "");RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'PUT',  url: 'https://example.zendesk.com/api/v2/group_slas/policies/reorder',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'group_sla_policy_ids': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/group_slas/policies/reorder?group_sla_policy_ids="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/group_slas/policies/reorder")uri.query = URI.encode_www_form("group_sla_policy_ids": "")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    null

### Retrieve Supported Filter Definition Items

  * `GET /api/v2/group_slas/policies/definitions`


#### Allowed For

  * Admins


#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/group_slas/policies/definitions \  -H "Content-Type: application/json" \  -v -u {email_address}/token:{api_token} -X GET

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/group_slas/policies/definitions"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/group_slas/policies/definitions")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/group_slas/policies/definitions',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/group_slas/policies/definitions"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/group_slas/policies/definitions")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "definitions": {    "all": [      {        "group": "ticket",        "operators": [          {            "title": "Contains at least one of the following",            "value": "includes"          },          {            "title": "Contains at least none of the following",            "value": "not_includes"          }        ],        "title": "Group ID",        "value": "group_id",        "values": {          "list": [            {              "title": "Tier 1",              "value": 6            }          ],          "type": "list"        }      }    ]  }}

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)