# Satisfaction Reasons

*Source: https://developer.zendesk.com/api-reference/ticketing/ticket-management/satisfaction_reasons/*

---

## On this page

  * [JSON format](/api-reference/ticketing/ticket-management/satisfaction_reasons/#json-format)
  * [List Reasons for Satisfaction Rating](/api-reference/ticketing/ticket-management/satisfaction_reasons/#list-reasons-for-satisfaction-rating)
  * [Show Reason for Satisfaction Rating](/api-reference/ticketing/ticket-management/satisfaction_reasons/#show-reason-for-satisfaction-rating)


# Satisfaction Reasons

## On this page

  * [JSON format](/api-reference/ticketing/ticket-management/satisfaction_reasons/#json-format)
  * [List Reasons for Satisfaction Rating](/api-reference/ticketing/ticket-management/satisfaction_reasons/#list-reasons-for-satisfaction-rating)
  * [Show Reason for Satisfaction Rating](/api-reference/ticketing/ticket-management/satisfaction_reasons/#show-reason-for-satisfaction-rating)


**Note** : The endpoints listed on this page are for the [legacy CSAT feature](https://support.zendesk.com/hc/en-us/articles/4408822875034). We recommend you use survey responses for more accurate and relevant feedback. For more information, see [CSAT Survey responses](/api-reference/ticketing/ticket-management/csat_survey_responses/), [Survey offered event](/documentation/ticketing/reference-guides/ticket-audit-events-reference/#survey-offered-event), and [Survey response submitted event](/documentation/ticketing/reference-guides/ticket-audit-events-reference/#survey-response-submitted-event). See also [Setting up the CSAT survey](https://support.zendesk.com/hc/en-us/articles/7689997846554). If you are using the legacy CSAT, you must [deactivate legacy CSAT and manually deactivate any custom CSAT automations and triggers](https://support.zendesk.com/hc/en-us/articles/4408822875034#topic_lgj_cmr_w1c) before you can use survey responses. You can have only one CSAT option activated at a time.

When [satisfaction reasons](https://support.zendesk.com/hc/en-us/articles/223152967) are enabled in your Zendesk Support account, and a user gives a negative rating to a solved ticket, a follow-up question is presented to the user. The question includes a list menu of possible reasons for the negative rating. You can use this API to inspect the list of reasons.

You must use the admin interface to add or remove reasons. See [Customizing and localizing satisfaction reasons](https://support.zendesk.com/hc/en-us/articles/223152967#topic_u2m_c4b_rw) in the Support Help Center.

### JSON format

Satisfaction Reasons are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
created_at| string| true| false| The time the reason was created
deleted_at| string| true| false| The time the reason was deleted
id| integer| true| false| Automatically assigned upon creation
raw_value| string| false| false| The dynamic content placeholder, if present, or the current "value", if not. See [Dynamic Content Items](/api-reference/ticketing/ticket-management/dynamic_content/)
reason_code| integer| true| false| An account-level code for referencing the reason. Custom reasons are assigned an auto-incrementing integer (non-system reason codes begin at 1000). See Reason codes
updated_at| string| true| false| The time the reason was updated
url| string| true| false| API URL for the resource
value| string| false| true| Translated value of the reason in the account locale

#### Reason codes

The follow-up question has the following default reasons the user can select for giving a negative rating:

Code| Reason
---|---
0| No reason provided (the user didn't select a reason from the list menu)
5| The issue took too long to resolve
6| The issue was not resolved
7| The agent's knowledge is unsatisfactory
8| The agent's attitude is unsatisfactory
1000| Some other reason

An admin in Zendesk Support can create custom reasons. Any custom reason is assigned a code of 1000 or higher when the reason is created. See [Customizing and localizing satisfaction reasons](https://support.zendesk.com/hc/en-us/articles/223152967#topic_u2m_c4b_rw) in the Support Help Center.

#### Example


    {  "created_at": "2011-07-20T22:55:29Z",  "deleted_at": "2012-03-12T12:45:32Z",  "id": 35436,  "raw_value": "{{dc.reason_code_1003}}",  "reason_code": 1003,  "updated_at": "2011-07-20T22:55:29Z",  "url": "https://example.zendesk.com/api/v2/satisfaction_reasons/35436",  "value": "Agent did not respond quickly"}

### List Reasons for Satisfaction Rating

  * `GET /api/v2/satisfaction_reasons`


List all reasons for an account

#### Allowed For

  * Admins


#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/satisfaction_reasons \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/satisfaction_reasons"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/satisfaction_reasons")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/satisfaction_reasons',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/satisfaction_reasons"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/satisfaction_reasons")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "reasons": [    {      "created_at": "2011-07-20T22:55:29Z",      "id": 35436,      "raw_value": "{{dc.reason_code_1000}}",      "reason_code": 1000,      "updated_at": "2011-07-20T22:55:29Z",      "url": "https://company.zendesk.com/api/v2/satisfaction_reasons/35436",      "value": "Agent did not respond quickly."    },    {      "created_at": "2011-07-20T22:55:29Z",      "id": 120447,      "raw_value": "{{dc.reason_code_1000}}",      "reason_code": 1001,      "updated_at": "2011-07-20T22:55:29Z",      "url": "https://company.zendesk.com/api/v2/satisfaction_reasons/120447",      "value": "Issue is not resolved."    }  ]}

### Show Reason for Satisfaction Rating

  * `GET /api/v2/satisfaction_reasons/{satisfaction_reason_id}`


#### Allowed For

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
satisfaction_reason_id| integer| Path| true| The id of the satisfaction rating reason

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/satisfaction_reasons/{id} \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/satisfaction_reasons/35121"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/satisfaction_reasons/35121")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/satisfaction_reasons/35121',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/satisfaction_reasons/35121"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/satisfaction_reasons/35121")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "reason": [    {      "created_at": "2011-07-20T22:55:29Z",      "id": 35121,      "raw_value": "{{dc.reason_code_1000}}",      "reason_code": 1000,      "updated_at": "2011-07-20T22:55:29Z",      "url": "https://company.zendesk.com/api/v2/satisfaction_reason/35121",      "value": "Agent did not respond quickly."    }  ]}

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)