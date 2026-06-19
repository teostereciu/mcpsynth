# SLA Policies

*Source: https://developer.zendesk.com/api-reference/ticketing/business-rules/sla_policies/*

---

## On this page

  * [JSON format](/api-reference/ticketing/business-rules/sla_policies/#json-format)
  * [List SLA Policies](/api-reference/ticketing/business-rules/sla_policies/#list-sla-policies)
  * [Show SLA Policy](/api-reference/ticketing/business-rules/sla_policies/#show-sla-policy)
  * [Create SLA Policy](/api-reference/ticketing/business-rules/sla_policies/#create-sla-policy)
  * [Update SLA Policy](/api-reference/ticketing/business-rules/sla_policies/#update-sla-policy)
  * [Delete SLA Policy](/api-reference/ticketing/business-rules/sla_policies/#delete-sla-policy)
  * [Reorder SLA Policies](/api-reference/ticketing/business-rules/sla_policies/#reorder-sla-policies)
  * [Retrieve Supported Filter Definition Items](/api-reference/ticketing/business-rules/sla_policies/#retrieve-supported-filter-definition-items)


# SLA Policies

## On this page

  * [JSON format](/api-reference/ticketing/business-rules/sla_policies/#json-format)
  * [List SLA Policies](/api-reference/ticketing/business-rules/sla_policies/#list-sla-policies)
  * [Show SLA Policy](/api-reference/ticketing/business-rules/sla_policies/#show-sla-policy)
  * [Create SLA Policy](/api-reference/ticketing/business-rules/sla_policies/#create-sla-policy)
  * [Update SLA Policy](/api-reference/ticketing/business-rules/sla_policies/#update-sla-policy)
  * [Delete SLA Policy](/api-reference/ticketing/business-rules/sla_policies/#delete-sla-policy)
  * [Reorder SLA Policies](/api-reference/ticketing/business-rules/sla_policies/#reorder-sla-policies)
  * [Retrieve Supported Filter Definition Items](/api-reference/ticketing/business-rules/sla_policies/#retrieve-supported-filter-definition-items)


A Service Level Agreement is a documented agreement between a support provider and their customers that specifies performance measures for support. SLAs are often expressed as follows:

_For urgent incidents, we will respond to tickets in 10 minutes and resolve the ticket within 2 hours._ _For high priority incidents, we will respond to tickets in 30 minutes and resolved the ticket within 8 hours._

Because there may be different SLAs per customer (or group of customers) that the provider supports, the provider will define an SLA policy to support each unique SLA's requirements.

A SLA policy is the unique (not enforced) combination of criteria along with assigned metric targets for each value of the priority field. There can be multiple SLA policies per Zendesk Support account.

### JSON format

SLA Policies are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
created_at| string| true| false| The time the SLA policy was created
description| string| false| false| The description of the SLA policy
filter| object| false| true| An object that describes the conditions that a ticket must match in order for an SLA policy to be applied to that ticket. See Filter.
id| integer| true| false| Automatically assigned when created
policy_metrics| array| false| false| Array of Policy Metric objects
position| integer| false| false| Position of the SLA policy that determines the order they will be matched. If not specified, the SLA policy is added as the last position
title| string| false| true| The title of the SLA policy
updated_at| string| true| false| The time of the last update of the SLA policy
url| string| true| false| URL of the SLA policy record

#### Filter

A filter checks the value of ticket fields and selects the ticket if the conditions are met. Filter is represented as a JSON object with two arrays of one or more conditions.

**Example**


    {   "filter": {     "all": [       { "field": "type", "operator": "is", "value": "incident" },       { "field": "via_id", "operator": "is", "value": 4 }     ],     "any": [     ]   }}

The first array lists all the conditions that must be met. The second array lists any condition that must be met.

Name| Type| Description
---|---|---
`all`| array| Logical AND. Tickets must fulfill all of the conditions to be considered matching
`any`| array| Logical OR. Tickets may satisfy any of the conditions to be considered matching

Each condition in an array has the following properties:

Name| Type| Description
---|---|---
field| string| The name of a ticket field
operator| string| A comparison operator
value| string| The value of a ticket field

**Example**


    { "field": "type", "operator": "is", "value": "incident" }

See [Conditions reference](/documentation/ticketing/reference-guides/conditions-reference) for the list of fields, allowed operators, and values of the conditions.

#### Policy Metric

An object that describes the metric targets for each value of the priority field.

Policy Metrics are represented as simple flat JSON objects which have the following keys:

Name| Type| Comment
---|---|---
priority| string| Priority that a ticket must match
metric| string| The definition of the time that is being measured. See Metrics
target| integer| The total time within which the end-state for a metric should be met, measured in minutes
target_in_seconds| integer| The total time within which the end-state for a metric should be met, measured in seconds
business_hours| boolean| Whether the metric targets are being measured in business hours or calendar hours

**Example**


    {  "priority": "low",  "metric": "first_reply_time",  "target": 60,  "business_hours": false}

#### Metrics

Metric| Value
---|---
Agent Work Time| agent_work_time
First Reply Time| first_reply_time
Next Reply Time| next_reply_time
Pausable Update Time| pausable_update_time
Periodic Update Time| periodic_update_time
Requester Wait Time| requester_wait_time
Total Resolution Time| total_resolution_time

#### Example


    {  "created_at": "2015-03-17T22:50:26Z",  "description": "Organizations: Silver Plan",  "filter": {    "all": [      {        "field": "type",        "operator": "is",        "value": "incident"      },      {        "field": "via_id",        "operator": "is",        "value": "4"      },      {        "field": "custom_status_id",        "operator": "includes",        "value": [          "1",          "2"        ]      }    ],    "any": []  },  "id": 25,  "policy_metrics": [    {      "business_hours": false,      "metric": "first_reply_time",      "priority": "low",      "target": 60    }  ],  "position": 3,  "title": "Silver Plan",  "updated_at": "2015-03-17T22:50:26Z",  "url": "https://company.zendesk.com/api/v2/slas/policies/25"}

### List SLA Policies

  * `GET /api/v2/slas/policies`


#### Availability

  * Accounts on the Support Professional or Suite Growth plan or above


#### Allowed For

  * Admins


#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/slas/policies \  -H "Content-Type: application/json" \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/slas/policies"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/slas/policies")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/slas/policies',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/slas/policies"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/slas/policies")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "count": 1,  "next_page": null,  "previous_page": null,  "sla_policies": [    {      "description": "For urgent incidents, we will respond to tickets in 10 minutes",      "filter": {        "all": [          {            "field": "type",            "operator": "is",            "value": "incident"          },          {            "field": "via_id",            "operator": "is",            "value": "4"          }        ],        "any": []      },      "id": 36,      "policy_metrics": [        {          "business_hours": false,          "metric": "first_reply_time",          "priority": "low",          "target": 60        }      ],      "position": 3,      "title": "Incidents",      "url": "https://{subdomain}.zendesk.com/api/v2/slas/policies/36"    }  ]}

### Show SLA Policy

  * `GET /api/v2/slas/policies/{sla_policy_id}`


#### Availability

  * Accounts on the Support Professional or Suite Growth plan or above


#### Allowed For

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
sla_policy_id| integer| Path| true| The ID of the SLA Policy

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/slas/policies/{sla_policy_id} \  -H "Content-Type: application/json" \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/slas/policies/36"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/slas/policies/36")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/slas/policies/36',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/slas/policies/36"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/slas/policies/36")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "sla_policy": {    "description": "For urgent incidents, we will respond to tickets in 10 minutes",    "filter": {      "all": [        {          "field": "type",          "operator": "is",          "value": "incident"        },        {          "field": "via_id",          "operator": "is",          "value": "4"        }      ],      "any": []    },    "id": 36,    "policy_metrics": [      {        "business_hours": false,        "metric": "first_reply_time",        "priority": "low",        "target": 60      }    ],    "position": 3,    "title": "Incidents",    "url": "https://{subdomain}.zendesk.com/api/v2/slas/policies/36"  }}

### Create SLA Policy

  * `POST /api/v2/slas/policies`


#### Availability

  * Accounts on the Support Professional or Suite Growth plan or above


#### Allowed For

  * Admins


#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/slas/policies \  -H "Content-Type: application/json" \  -d '{        "sla_policy": {          "title": "Incidents",          "description": "For urgent incidents, we will respond to tickets in 10 minutes",          "position": 3,          "filter": {            "all": [              { "field": "type", "operator": "is", "value": "incident" }            ],            "any": []          },          "policy_metrics": [            { "priority": "normal", "metric": "first_reply_time", "target": 30, "business_hours": false },            { "priority": "urgent", "metric": "first_reply_time", "target": 10, "business_hours": false },            { "priority": "low", "metric": "requester_wait_time", "target": 180, "business_hours": false },            { "priority": "normal", "metric": "requester_wait_time", "target": 160, "business_hours": false },            { "priority": "high", "metric": "requester_wait_time", "target": 140, "business_hours": false },            { "priority": "urgent", "metric": "requester_wait_time", "target": 120, "business_hours": false }          ]        }      }' \  -v -u {email_address}/token:{api_token} -X POST

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/slas/policies"	method := "POST"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/slas/policies")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'POST',  url: 'https://example.zendesk.com/api/v2/slas/policies',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/slas/policies"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/slas/policies")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**201 Created**


    // Status 201 Created
    {  "sla_policy": {    "description": "For urgent incidents, we will respond to tickets in 10 minutes",    "filter": {      "all": [        {          "field": "type",          "operator": "is",          "value": "incident"        }      ],      "any": []    },    "id": 36,    "policy_metrics": [      {        "business_hours": false,        "metric": "first_reply_time",        "priority": "normal",        "target": 30      },      {        "business_hours": false,        "metric": "first_reply_time",        "priority": "urgent",        "target": 10      },      {        "business_hours": false,        "metric": "requester_wait_time",        "priority": "low",        "target": 180      },      {        "business_hours": false,        "metric": "requester_wait_time",        "priority": "normal",        "target": 160      },      {        "business_hours": false,        "metric": "requester_wait_time",        "priority": "high",        "target": 140      },      {        "business_hours": false,        "metric": "requester_wait_time",        "priority": "urgent",        "target": 120      }    ],    "position": 3,    "title": "Incidents",    "url": "https://{subdomain}.zendesk.com/api/v2/slas/policies/36"  }}

### Update SLA Policy

  * `PUT /api/v2/slas/policies/{sla_policy_id}`


Updates the specified policy.

#### Availability

  * Accounts on the Support Professional or Suite Growth plan or above


#### Allowed For

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
sla_policy_id| integer| Path| true| The ID of the SLA Policy

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/slas/policies/{sla_policy_id} \  -H "Content-Type: application/json" \  -d '{        "sla_policy": {          "title": "Urgent Incidents",          "description": "For urgent incidents, we will resolve the ticket within 2 hours",          "position": 3,          "filter": {            "all": [              { "field": "type", "operator": "is", "value": "incident" }            ],            "any": []          },          "policy_metrics": [            { "priority": "normal", "metric": "first_reply_time", "target": 30, "business_hours": false },            { "priority": "urgent", "metric": "first_reply_time", "target": 10, "business_hours": false },            { "priority": "low", "metric": "requester_wait_time", "target": 180, "business_hours": false },            { "priority": "normal", "metric": "requester_wait_time", "target": 160, "business_hours": false },            { "priority": "high", "metric": "requester_wait_time", "target": 140, "business_hours": false },            { "priority": "urgent", "metric": "requester_wait_time", "target": 120, "business_hours": false }          ]        }      }' \  -v -u {email_address}/token:{api_token} -X PUT

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/slas/policies/36"	method := "PUT"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/slas/policies/36")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'PUT',  url: 'https://example.zendesk.com/api/v2/slas/policies/36',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/slas/policies/36"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/slas/policies/36")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "sla_policy": {    "description": "For urgent incidents, we will resolve the ticket within 2 hours",    "filter": {      "all": [        {          "field": "type",          "operator": "is",          "value": "incident"        }      ],      "any": []    },    "id": 36,    "policy_metrics": [      {        "business_hours": false,        "metric": "first_reply_time",        "priority": "normal",        "target": 30      },      {        "business_hours": false,        "metric": "first_reply_time",        "priority": "urgent",        "target": 10      },      {        "business_hours": false,        "metric": "requester_wait_time",        "priority": "low",        "target": 180      },      {        "business_hours": false,        "metric": "requester_wait_time",        "priority": "normal",        "target": 160      },      {        "business_hours": false,        "metric": "requester_wait_time",        "priority": "high",        "target": 140      },      {        "business_hours": false,        "metric": "requester_wait_time",        "priority": "urgent",        "target": 120      }    ],    "position": 3,    "title": "Urgent Incidents",    "url": "https://{subdomain}.zendesk.com/api/v2/slas/policies/36"  }}

### Delete SLA Policy

  * `DELETE /api/v2/slas/policies/{sla_policy_id}`


#### Availability

  * Accounts on the Support Professional or Suite Growth plan or above


#### Allowed For

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
sla_policy_id| integer| Path| true| The ID of the SLA Policy

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/slas/policies/{sla_policy_id} \  -H "Content-Type: application/json" \  -v -u {email_address}/token:{api_token} -X DELETE

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/slas/policies/36"	method := "DELETE"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/slas/policies/36")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("DELETE", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'DELETE',  url: 'https://example.zendesk.com/api/v2/slas/policies/36',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/slas/policies/36"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"DELETE",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/slas/policies/36")request = Net::HTTP::Delete.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**204 No Content**


    // Status 204 No Content
    null

### Reorder SLA Policies

  * `PUT /api/v2/slas/policies/reorder`


#### Availability

  * Accounts on the Support Professional or Suite Growth plan or above


#### Allowed For

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
sla_policy_ids| array| Query| false| The IDs of the SLA Policies to reorder

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/slas/policies/reorder \  -H "Content-Type: application/json" -X PUT \  -d '{"sla_policy_ids": [12, 55]}' \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/slas/policies/reorder?sla_policy_ids="	method := "PUT"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/slas/policies/reorder")		.newBuilder()		.addQueryParameter("sla_policy_ids", "");RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'PUT',  url: 'https://example.zendesk.com/api/v2/slas/policies/reorder',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'sla_policy_ids': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/slas/policies/reorder?sla_policy_ids="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/slas/policies/reorder")uri.query = URI.encode_www_form("sla_policy_ids": "")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    null

### Retrieve Supported Filter Definition Items

  * `GET /api/v2/slas/policies/definitions`


#### Availability

  * Accounts on the Support Professional or Suite Growth plan or above


#### Allowed For

  * Admins


#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/slas/policies/definitions \  -H "Content-Type: application/json" \  -v -u {email_address}/token:{api_token} -X GET

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/slas/policies/definitions"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/slas/policies/definitions")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/slas/policies/definitions',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/slas/policies/definitions"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/slas/policies/definitions")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "definitions": {    "all": [      {        "group": "ticket",        "operators": [          {            "title": "Is",            "value": "is"          },          {            "title": "Is not",            "value": "is_not"          }        ],        "target": null,        "title": "Brand",        "value": "brand_id",        "values": {          "list": [            {              "title": "Support",              "value": "10001"            }          ],          "type": "list"        }      }    ],    "any": [      {        "group": "ticket",        "operators": [          {            "title": "Is",            "value": "is"          },          {            "title": "Is not",            "value": "is_not"          }        ],        "target": null,        "title": "Brand",        "value": "brand_id",        "values": {          "list": [            {              "title": "Support",              "value": "10001"            }          ],          "type": "list"        }      }    ]  }}

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)