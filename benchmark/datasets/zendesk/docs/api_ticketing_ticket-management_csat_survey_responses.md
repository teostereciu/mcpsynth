# CSAT Survey Responses

*Source: https://developer.zendesk.com/api-reference/ticketing/ticket-management/csat_survey_responses/*

---

## On this page

  * [JSON format for Create Survey Response](/api-reference/ticketing/ticket-management/csat_survey_responses/#json-format-for-create-survey-response)
  * [JSON format](/api-reference/ticketing/ticket-management/csat_survey_responses/#json-format)
  * [List Survey Responses](/api-reference/ticketing/ticket-management/csat_survey_responses/#list-survey-responses)
  * [Create Survey Response](/api-reference/ticketing/ticket-management/csat_survey_responses/#create-survey-response)
  * [Submit Survey Response](/api-reference/ticketing/ticket-management/csat_survey_responses/#submit-survey-response)
  * [Show Survey Response](/api-reference/ticketing/ticket-management/csat_survey_responses/#show-survey-response)


# CSAT Survey Responses

## On this page

  * [JSON format for Create Survey Response](/api-reference/ticketing/ticket-management/csat_survey_responses/#json-format-for-create-survey-response)
  * [JSON format](/api-reference/ticketing/ticket-management/csat_survey_responses/#json-format)
  * [List Survey Responses](/api-reference/ticketing/ticket-management/csat_survey_responses/#list-survey-responses)
  * [Create Survey Response](/api-reference/ticketing/ticket-management/csat_survey_responses/#create-survey-response)
  * [Submit Survey Response](/api-reference/ticketing/ticket-management/csat_survey_responses/#submit-survey-response)
  * [Show Survey Response](/api-reference/ticketing/ticket-management/csat_survey_responses/#show-survey-response)


A survey response is an object that represents the response submitted to a ticket CSAT survey. See [Sending a CSAT survey to your customers](https://support.zendesk.com/hc/en-us/articles/7689997846554) in Zendesk help.

Survey responses are available on the Support Professional plan and above, and the Zendesk Suite Growth plan and above.

### JSON format for Create Survey Response

The response to POST /api/v2/guide/survey_responses is represented as a JSON object with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
id| string| false| true| Created survey response id
links| object| false| true| A links object

#### Links object

There are three types of links objects:

  * Custom text links object
  * Emoji links object
  * Numeric links object


#### Custom text links object

Name| Type| Optional| Nullable| Description
---|---|---|---|---
type| string| false| false| Has the value `rating_link_custom_text`
url_path| string| false| false| A URL path to the survey response
rating_links| array| false| false| A rating link object

#### Emoji links object

Name| Type| Optional| Nullable| Description
---|---|---|---|---
type| string| false| false| Has the value `rating_link_emoji`
url_path| string| false| false| A URL path to the survey response
rating_links| array| false| false| A rating link object

#### Numeric links object

Name| Type| Optional| Nullable| Description
---|---|---|---|---
type| string| false| false| Has the value `rating_link_numeric`
url_path| string| false| false| A URL path to the survey response
rating_links| array| false| false| A rating link object

##### Rating link object

Name| Type| Optional| Nullable| Description
---|---|---|---|---
url_path| string| false| false| A URL path to a survey response rating option
rating| number| false| false| A rating value for the rating scale question answer
label| string| false| false| A text content object representing the label of this option
emoji| string| true| false| A text content object representing the emoji of this option

#### Example


    {  "id": "01JPHVQK3JY2RQCPWGBVCN6Y11",  "links": {    "rating_links": [      {        "emoji": {          "type": "static",          "value": "ð"        },        "label": {          "type": "static",          "value": "Very unsatisfied"        },        "rating": 1,        "url_path": "/hc/en-us/survey_responses/01JPHVQK3JY2RQCPWGBVCN6Y11?access_token=PMXFC68dx_aoluWHb_yCHPY_WQ&rating=1"      },      {        "emoji": {          "type": "static",          "value": "ð"        },        "label": {          "type": "static",          "value": "Very satisfied"        },        "rating": 5,        "url_path": "/hc/en-us/survey_responses/01JPHVQK3JY2RQCPWGBVCN6Y11?access_token=PMXFC68dx_aoluWHb_yCHPY_WQ&rating=5"      }    ],    "type": "rating_link_emoji",    "url_path": "/hc/en-us/survey_responses/01JPHVQK3JY2RQCPWGBVCN6Y11?access_token=PMXFC68dx_aoluWHb_yCHPY_WQ"  }}

### JSON format

CSAT Survey Responses are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
answers| array| false| true| An array of survey response answer objects. See Answer object
expires_at| string| false| true| The date and time of when the responder can no longer edit their survey response
id| string| false| true| Automatically assigned when the survey response is created
responder_id| integer| false| true| The id of the user the survey response belongs to
subject_zrns| array| false| true| An array of Zendesk resource names, such as ticket and conversation (zen:ticket:123, zen:conversation:4295a81b-ccdd-4998-88d9-0eff5e76dc44)
subjects| array| false| true| An array of structured objects which represent Zendesk resource names. See Subject object
survey| object| false| true| The survey object this survey response belongs to. See Survey object

#### Subject object

Name| Type| Optional| Nullable| Descriptions
---|---|---|---|---
id| string| false| false| The id of the subject this survey response belongs to
type| string| false| false| The type of the subject this survey response belongs to, such as ticket, request, conversation
zrn| string| false| false| The Zendesk resource name this survey response belongs to

#### Survey object

Name| Type| Optional| Nullable| Descriptions
---|---|---|---|---
id| string| false| false| The id of the survey this survey response belongs to. Automatically assigned when the survey is created
version| integer| false| false| The version of the survey upon which the survey response was based on. Every time the survey is updated, its version is auto-incremented
state| string| false| false| The survey state. The value has 2 options: enabled, disabled

#### Answer object

The answer object can be one of the following types:

  * Skipped answer
  * Closed-ended answer
  * Open-ended answer
  * Rating scale answer


##### Skipped answer object

Name| Type| Optional| Nullable| Descriptions
---|---|---|---|---
type| string| false| false| Has the value `skipped`
question| object| false| false| An object representing the survey question skipped during the survey response submission
created_at| string| false| false| The date when the answer was created
updated_at| string| false| false| The date when the answer was last updated

##### Closed-ended answer object

Name| Type| Optional| Nullable| Descriptions
---|---|---|---|---
type| string| false| false| Has the value `closed_ended`
selections| array| false| false| An array of options selected as the answer during the survey response submission. The selection objects are of type predefined selection
question| object| false| false| An object representing the survey question answered during the survey response submission. See Closed-ended question object
created_at| string| false| false| The date when the answer was created
updated_at| string| false| false| The date when the answer was last updated

###### Predefined selection object

Name| Type| Optional| Nullable| Descriptions
---|---|---|---|---
type| string| false| false| Has the following value `predefined`
option_id| string| false| false| The id of the closed-ended survey question option that was selected as the answer

##### Open-ended answer object

Name| Type| Optional| Nullable| Descriptions
---|---|---|---|---
type| string| false| false| Has the value `open_ended`
value| string| false| false| The plain text value of the provided answer
question| object| false| false| An object representing the survey question answered during the survey response submission. See Open ended question object
created_at| string| false| false| The date when the answer was created
updated_at| string| false| false| The date when the answer was last updated

##### Rating scale answer object

Name| Type| Optional| Nullable| Descriptions
---|---|---|---|---
type| string| false| false| Has the value `rating_scale`
rating| integer| false| false| The selected rating representing the answer
rating_category| string| false| false| Possible values: `bad`, `neutral`, `good`
question| object| false| false| An object representing the survey question answered during the survey response submission. See Rating scale question object
created_at| string| false| false| The date when the answer was created
updated_at| string| false| false| The date when the answer was last updated

#### Question object

There are three types of question objects:

  * Closed-ended question
  * Open-ended question
  * Rating scale question


##### Closed-ended question object

Name| Type| Optional| Nullable| Descriptions
---|---|---|---|---
type| string| false| false| Has the value `closed_ended`
id| string| false| false| Automatically assigned when the survey question is created
alias| string| false| false| A human-readable identifier for the survey question
headline| object| true| true| A text content object representing the headline of the survey question
options| array| true| true| An array of closed-ended survey question options

###### Closed-ended option object

Name| Type| Optional| Nullable| Descriptions
---|---|---|---|---
id| string| false| false| Automatically assigned when the survey question option is created
label| object| false| false| A text content object representing the label of this option

##### Open-ended question object

Name| Type| Optional| Nullable| Descriptions
---|---|---|---|---
type| string| false| false| Has the value `open_ended`
id| string| false| false| Automatically assigned when the survey question is created
alias| string| true| false| A human-readable identifier for the survey question
headline| object| true| true| A text content object representing the headline of the survey question

##### Rating scale question object

The rating scale question object can be one of the following types:

  * Custom text rating scale question
  * Emoji rating scale question
  * Numeric rating scale question


###### Custom text rating scale question object

Name| Type| Optional| Nullable| Descriptions
---|---|---|---|---
type| string| false| false| Has the value `rating_scale_custom_text`
id| string| false| false| Automatically assigned when the survey question is created
alias| string| true| false| A human-readable identifier for the survey question
sub_type| string| false| false| One of the following values: `customer_satisfaction`, `other`
headline| string| true| true| A text content object representing the headline of the survey question
options| array| true| true| An array of custom text rating scale options

###### Custom text rating scale option object

Name| Type| Optional| Nullable| Descriptions
---|---|---|---|---
rating| integer| false| false| The numeric rating represented by this option
label| object| false| false| A text content object representing the label of this option

###### Emoji rating scale question object

Name| Type| Optional| Nullable| Descriptions
---|---|---|---|---
type| string| false| false| Has the value `rating_scale_emoji`
id| string| false| false| Automatically assigned when the survey question is created
alias| string| true| false| A human-readable identifier for the survey question
sub_type| string| false| false| One of the following values: `customer_satisfaction`, `other`
headline| string| true| true| A text content object representing the headline of the survey question
options| array| true| true| An array of emoji rating scale options

###### Emoji rating scale option object

Name| Type| Optional| Nullable| Descriptions
---|---|---|---|---
rating| integer| false| false| The numeric rating represented by this option
emoji| object| false| false| A text content object representing the emoji of this option
label| object| false| false| A text content object representing the label of this option

###### Numeric rating scale question object

Name| Type| Optional| Nullable| Descriptions
---|---|---|---|---
type| string| false| false| Has the value `rating_scale_numeric`
id| string| false| false| Automatically assigned when the survey question is created
alias| string| true| false| A human-readable identifier for the survey question
sub_type| string| false| false| One of the following values: `customer_satisfaction`, `other`
headline| string| true| true| A text content object representing the headline of the survey question
options| array| true| true| An array of numeric rating scale options

###### Numeric rating scale option object

Name| Type| Optional| Nullable| Descriptions
---|---|---|---|---
rating| integer| false| false| The numeric rating represented by this option
label| object| false| false| A text content object representing the label of this option

##### Text content object

A text content object can be one of the following types:

  * Static text content
  * Dynamic text content


###### Static text content object

An object containing a text string that isn't translated to the user's preferred language.

Name| Type| Optional| Nullable| Descriptions
---|---|---|---|---
type| string| false| false| Has the value `static`
value| string| false| false| A static (non-translatable) plain text content

###### Dynamic text content object

An object containing a dynamic content placeholder, which returns pre-defined content that is translated to a user's preferred language. See [Dynamic content article](https://support.zendesk.com/hc/en-us/articles/4408882999066-Providing-multiple-language-support-with-dynamic-content).

Name| Type| Optional| Nullable| Descriptions
---|---|---|---|---
type| string| false| false| Has the value `dynamic`
key| string| false| false| The key of a dynamic content
value| string| false| false| The translated value of the dynamic content represented by its key for a given locale (determined by the `locale` path parameter)

#### Example


    {  "answers": [    {      "created_at": "2024-08-14T12:00:00.000Z",      "question": {        "alias": "comment",        "headline": {          "type": "static",          "value": "Anything else you would like to share about your experience?"        },        "id": "01GFYBENPDGN1R6NAA4WRDNVFR",        "type": "open_ended"      },      "type": "skipped",      "updated_at": "2024-08-14T12:00:00.000Z"    }  ],  "expires_at": "2024-08-14T12:00:00.000Z",  "id": "01J1WB51MG6HXTYWE6Q0C93RNW",  "responder_id": 4398080151295,  "subject_zrns": [    "zen:ticket:99"  ],  "subjects": [    {      "id": "99",      "type": "ticket",      "zrn": "zen:ticket:99"    }  ],  "survey": {    "id": "01J58KJ9RAE0D2EK7HRVM7Z8F2",    "state": "enabled",    "version": 3  }}

### List Survey Responses

  * `GET /api/v2/guide/survey_responses`


Shows information about survey responses.

#### Allowed for

  * Admins
  * End users (responders only)


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
filter| object| Query| false| [responder_ids] - A comma-separated list of survey responder ids
[subject_zrns] - A comma-separated list of Zendesk resource names, such as ticket and conversation (zen:ticket:123, zen:conversation:4295a81b-ccdd-4998-88d9-0eff5e76dc44)
[created_at_start] - Timestamp of the oldest survey response object in the filtered result set, expressed as [Unix epoch](https://www.epochconverter.com/) time in milliseconds
[created_at_end] - Timestamp of the most recent offered survey response object in the filtered result set, expressed as [Unix epoch](https://www.epochconverter.com/) time in milliseconds
page| object| Query| false| A group of query parameters used for pagination. See [Pagination](/api-reference/help_center/help-center-api/introduction/#pagination)
sort| string| Query| false| Options for sorting the result set by field and direction. Values with no prefix stand for ASC order. Values with the `-` prefix stand for DESC order. Allowed values are "id", or "-id".

#### Code Samples

**Curl**


    curl --request GET https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/survey_responses?filter=&page=&sort= \--header "Content-Type: application/json" \-u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/survey_responses?filter=&page=&sort="	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/survey_responses")		.newBuilder()		.addQueryParameter("filter", "")		.addQueryParameter("page", "")		.addQueryParameter("sort", "");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/survey_responses',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'filter': '',    'page': '',    'sort': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/survey_responses?filter=&page=&sort="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/survey_responses")uri.query = URI.encode_www_form("filter": "", "page": "", "sort": "")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

**curl_subject_zrns_and_responder_ids**


    curl https://{subdomain}.zendesk.com/api/v2/guide/survey_responses?filter[subject_zrns]=zen:ticket:1,zen:ticket:2&filter[responder_ids]=57919551,49284723 \  -v -u {email_address}/token:{api_token}

**curl_created_at**


    curl https://{subdomain}.zendesk.com/api/v2/guide/survey_responses?filter[created_at_start]=1741275900000&filter[created_at_end]=1741785117000 \  -v -u {email_address}/token:{api_token}

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "meta": {    "after_cursor": "MW",    "before_cursor": "MQ",    "has_more": false  },  "survey_responses": [    {      "answers": [        {          "created_at": "2024-08-14T12:00:00.000Z",          "question": {            "id": "01J1WBE8QR0YQVE373K2JDJR0F",            "sub_type": "customer_satisfaction",            "type": "rating_scale_numeric"          },          "rating": 1,          "rating_category": "bad",          "type": "rating_scale",          "updated_at": "2024-08-14T12:00:00.000Z"        },        {          "created_at": "2024-08-14T12:00:00.000Z",          "question": {            "id": "01J1WBGX1BR4ECKTS87CRJTXSF",            "type": "closed_ended"          },          "selections": [            {              "option_id": "01J1WBKRG57E6M8C1145EXJ535",              "type": "predefined"            }          ],          "type": "closed_ended",          "updated_at": "2024-08-14T12:00:00.000Z"        },        {          "created_at": "2024-08-14T12:00:00.000Z",          "question": {            "id": "01J1WBNS76ZC4TTFWP9RCNQ1S8",            "type": "open_ended"          },          "type": "open_ended",          "updated_at": "2024-08-14T12:00:00.000Z",          "value": "I had to repeatedly answer the same questions."        },        {          "created_at": "2024-08-14T12:00:00.000Z",          "question": {            "id": "01J1WBSAZWVY2XR1EFZKS3CM13",            "type": "open_ended"          },          "type": "skipped",          "updated_at": "2024-08-14T12:00:00.000Z"        }      ],      "expires_at": "2024-08-14T12:00:00.000Z",      "id": "01J1WB51MG6HXTYWE6Q0C93RNW",      "responder_id": 4398080151295,      "subject_zrns": [        "zen:ticket:99"      ],      "subjects": [        {          "id": "99",          "type": "ticket",          "zrn": "zen:ticket:99"        }      ],      "survey": {        "id": "01J58KJ9RAE0D2EK7HRVM7Z8F2",        "state": "enabled",        "version": 3      }    }  ]}

### Create Survey Response

  * `POST /api/v2/guide/survey_responses`


Creates a new survey response to be offered to a user.

The links contained in the response contain an `access_token` query parameter that allows any user to submit a survey response on behalf of a responder. As an API user, make sure to restrict access to the links to prevent the impersonation of the survey responder.

#### Allowed for

  * Admins


#### Example body


    {  "survey_response": {    "locale": "en-us",    "responder_id": "4398080151295",    "subject_zrns": [      "zen:ticket:99"    ],    "survey_id": "01JPHV4BSAH0V4552NM24FQ384"  }}

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/guide/survey_responses/ \  -v -u {email_address}/token:{api_token} \  -H "Content-Type: application/json" \|  -d '{ "survey_response": { "locale": "en-us", "survey_id": "01JPHV4BSAH0V4552NM24FQ384", "responder_id": 4398080151295, "subject_zrns": ["zen:ticket:99"] } }'

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/survey_responses"	method := "POST"	payload := strings.NewReader(`{  "survey_response": {    "locale": "en-us",    "responder_id": "4398080151295",    "subject_zrns": [      "zen:ticket:99"    ],    "survey_id": "01JPHV4BSAH0V4552NM24FQ384"  }}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/survey_responses")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"survey_response\": {    \"locale\": \"en-us\",    \"responder_id\": \"4398080151295\",    \"subject_zrns\": [      \"zen:ticket:99\"    ],    \"survey_id\": \"01JPHV4BSAH0V4552NM24FQ384\"  }}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "survey_response": {    "locale": "en-us",    "responder_id": "4398080151295",    "subject_zrns": [      "zen:ticket:99"    ],    "survey_id": "01JPHV4BSAH0V4552NM24FQ384"  }});
    var config = {  method: 'POST',  url: 'https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/survey_responses',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/survey_responses"
    payload = json.loads("""{  "survey_response": {    "locale": "en-us",    "responder_id": "4398080151295",    "subject_zrns": [      "zen:ticket:99"    ],    "survey_id": "01JPHV4BSAH0V4552NM24FQ384"  }}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/survey_responses")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")request.body = %q({  "survey_response": {    "locale": "en-us",    "responder_id": "4398080151295",    "subject_zrns": [      "zen:ticket:99"    ],    "survey_id": "01JPHV4BSAH0V4552NM24FQ384"  }})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "survey_response": {    "id": "01JPHVQK3JY2RQCPWGBVCN6Y11",    "links": {      "rating_links": [        {          "emoji": {            "type": "static",            "value": "ð"          },          "label": {            "type": "static",            "value": "Very unsatisfied"          },          "rating": 1,          "url_path": "/hc/en-us/survey_responses/01JPHVQK3JY2RQCPWGBVCN6Y11?access_token=PMXFC68dx_aoluWHb_yCHPY_WQ&rating=1"        },        {          "emoji": {            "type": "static",            "value": "ð"          },          "label": {            "type": "static",            "value": "Very satisfied"          },          "rating": 5,          "url_path": "/hc/en-us/survey_responses/01JPHVQK3JY2RQCPWGBVCN6Y11?access_token=PMXFC68dx_aoluWHb_yCHPY_WQ&rating=5"        }      ],      "type": "rating_link_emoji",      "url_path": "/hc/en-us/survey_responses/01JPHVQK3JY2RQCPWGBVCN6Y11?access_token=PMXFC68dx_aoluWHb_yCHPY_WQ"    }  }}

**401 Unauthorized**


    // Status 401 Unauthorized
    {  "errors": [    {      "code": "Unauthorized",      "status": "401",      "title": "Unauthorized to access the resource"    }  ]}

**403 Forbidden**


    // Status 403 Forbidden
    {  "errors": [    {      "code": "Forbidden",      "status": "403",      "title": "Access to the resource is forbidden"    }  ]}

**404 Not Found**


    // Status 404 Not Found
    {  "errors": [    {      "code": "NotFound",      "status": "404",      "title": "The survey is not found by provided id"    }  ]}

**409 Conflict**


    // Status 409 Conflict
    {  "errors": [    {      "code": "Conflict",      "status": "409",      "title": "The survey associated with this survey response has been disabled"    }  ]}

### Submit Survey Response

  * `POST /api/v2/guide/survey_responses/{id}`


Submit the answers for the specified survey response.

This endpoint supports signed-in users only.

The links from the Create Survey Response endpoint can be shared with the responder, who can then submit a survey response without requiring authentication.

#### Allowed for

  * Admins (responders only)
  * Agents (responders only)
  * End users (responders only)


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
id| string| Path| true| The survey response id

#### Example body


    {  "survey_response": {    "answers": [      {        "question_id": "01J1WBE8QR0YQVE373K2JDJR0F",        "rating": 1,        "type": "rating_scale"      },      {        "question_id": "01J1WBGX1BR4ECKTS87CRJTXSF",        "selections": [          {            "type": "pre_defined",            "value": "01JPHV4BSAH0V4552NM24FQ384"          }        ],        "type": "closed_ended"      },      {        "question_id": "01J1WBNS76ZC4TTFWP9RCNQ1S8",        "type": "open_ended",        "value": "Some other feedback"      },      {        "question_id": "01J1WBSAZWVY2XR1EFZKS3CM13",        "type": "skipped"      }    ],    "locale": "en-us"  }}

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/guide/survey_responses/{id} \  -v -u {email_address}/token:{api_token} \  -H "Content-Type: application/json" \  -d '{ "survey_response": { "id": "01GFYBENPDGN1R6NAA4WRDNVFR", "locale": "en-us", "access_token": "pZUS4PQl2ZFKGDwjYP-xfzhSVA", "answers": [ \  { "type": "rating_scale", "question_id": "01J1WBE8QR0YQVE373K2JDJR0F", "rating": 1 }, \  { "type": "closed_ended", "question_id": "01J1WBGX1BR4ECKTS87CRJTXSF", "selections": [ { "type": "pre_defined", "value": "01JPHV4BSAH0V4552NM24FQ384" } ] }, \  { "type": "open_ended", "question_id": "01J1WBNS76ZC4TTFWP9RCNQ1S8", "value": "I had to wait for too long" }, \   { "type": "skipped", "question_id": "01J1WBSAZWVY2XR1EFZKS3CM13" } \  ] } }'

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/survey_responses/01GFYBENPDGN1R6NAA4WRDNVFR"	method := "POST"	payload := strings.NewReader(`{  "survey_response": {    "answers": [      {        "question_id": "01J1WBE8QR0YQVE373K2JDJR0F",        "rating": 1,        "type": "rating_scale"      },      {        "question_id": "01J1WBGX1BR4ECKTS87CRJTXSF",        "selections": [          {            "type": "pre_defined",            "value": "01JPHV4BSAH0V4552NM24FQ384"          }        ],        "type": "closed_ended"      },      {        "question_id": "01J1WBNS76ZC4TTFWP9RCNQ1S8",        "type": "open_ended",        "value": "Some other feedback"      },      {        "question_id": "01J1WBSAZWVY2XR1EFZKS3CM13",        "type": "skipped"      }    ],    "locale": "en-us"  }}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/survey_responses/01GFYBENPDGN1R6NAA4WRDNVFR")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"survey_response\": {    \"answers\": [      {        \"question_id\": \"01J1WBE8QR0YQVE373K2JDJR0F\",        \"rating\": 1,        \"type\": \"rating_scale\"      },      {        \"question_id\": \"01J1WBGX1BR4ECKTS87CRJTXSF\",        \"selections\": [          {            \"type\": \"pre_defined\",            \"value\": \"01JPHV4BSAH0V4552NM24FQ384\"          }        ],        \"type\": \"closed_ended\"      },      {        \"question_id\": \"01J1WBNS76ZC4TTFWP9RCNQ1S8\",        \"type\": \"open_ended\",        \"value\": \"Some other feedback\"      },      {        \"question_id\": \"01J1WBSAZWVY2XR1EFZKS3CM13\",        \"type\": \"skipped\"      }    ],    \"locale\": \"en-us\"  }}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "survey_response": {    "answers": [      {        "question_id": "01J1WBE8QR0YQVE373K2JDJR0F",        "rating": 1,        "type": "rating_scale"      },      {        "question_id": "01J1WBGX1BR4ECKTS87CRJTXSF",        "selections": [          {            "type": "pre_defined",            "value": "01JPHV4BSAH0V4552NM24FQ384"          }        ],        "type": "closed_ended"      },      {        "question_id": "01J1WBNS76ZC4TTFWP9RCNQ1S8",        "type": "open_ended",        "value": "Some other feedback"      },      {        "question_id": "01J1WBSAZWVY2XR1EFZKS3CM13",        "type": "skipped"      }    ],    "locale": "en-us"  }});
    var config = {  method: 'POST',  url: 'https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/survey_responses/01GFYBENPDGN1R6NAA4WRDNVFR',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/survey_responses/01GFYBENPDGN1R6NAA4WRDNVFR"
    payload = json.loads("""{  "survey_response": {    "answers": [      {        "question_id": "01J1WBE8QR0YQVE373K2JDJR0F",        "rating": 1,        "type": "rating_scale"      },      {        "question_id": "01J1WBGX1BR4ECKTS87CRJTXSF",        "selections": [          {            "type": "pre_defined",            "value": "01JPHV4BSAH0V4552NM24FQ384"          }        ],        "type": "closed_ended"      },      {        "question_id": "01J1WBNS76ZC4TTFWP9RCNQ1S8",        "type": "open_ended",        "value": "Some other feedback"      },      {        "question_id": "01J1WBSAZWVY2XR1EFZKS3CM13",        "type": "skipped"      }    ],    "locale": "en-us"  }}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/survey_responses/01GFYBENPDGN1R6NAA4WRDNVFR")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")request.body = %q({  "survey_response": {    "answers": [      {        "question_id": "01J1WBE8QR0YQVE373K2JDJR0F",        "rating": 1,        "type": "rating_scale"      },      {        "question_id": "01J1WBGX1BR4ECKTS87CRJTXSF",        "selections": [          {            "type": "pre_defined",            "value": "01JPHV4BSAH0V4552NM24FQ384"          }        ],        "type": "closed_ended"      },      {        "question_id": "01J1WBNS76ZC4TTFWP9RCNQ1S8",        "type": "open_ended",        "value": "Some other feedback"      },      {        "question_id": "01J1WBSAZWVY2XR1EFZKS3CM13",        "type": "skipped"      }    ],    "locale": "en-us"  }})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "survey_response": {    "answers": [      {        "created_at": "2024-08-14T12:00:00.000Z",        "question": {          "id": "01J1WBE8QR0YQVE373K2JDJR0F",          "sub_type": "customer_satisfaction",          "type": "rating_scale_numeric"        },        "rating": 1,        "rating_category": "bad",        "type": "rating_scale",        "updated_at": "2024-08-14T12:00:00.000Z"      },      {        "created_at": "2024-08-14T12:00:00.000Z",        "question": {          "id": "01J1WBGX1BR4ECKTS87CRJTXSF",          "type": "closed_ended"        },        "selections": [          {            "option_id": "01J1WBKRG57E6M8C1145EXJ535",            "type": "predefined"          }        ],        "type": "closed_ended",        "updated_at": "2024-08-14T12:00:00.000Z"      },      {        "created_at": "2024-08-14T12:00:00.000Z",        "question": {          "id": "01J1WBNS76ZC4TTFWP9RCNQ1S8",          "type": "open_ended"        },        "type": "open_ended",        "updated_at": "2024-08-14T12:00:00.000Z",        "value": "I had to repeatedly answer the same questions."      },      {        "created_at": "2024-08-14T12:00:00.000Z",        "question": {          "id": "01J1WBSAZWVY2XR1EFZKS3CM13",          "type": "open_ended"        },        "type": "skipped",        "updated_at": "2024-08-14T12:00:00.000Z"      }    ],    "expires_at": "2024-08-14T12:00:00.000Z",    "id": "01GFYBENPDGN1R6NAA4WRDNVFR",    "responder_id": 4398080151295,    "subject_zrns": [      "zen:ticket:99"    ],    "subjects": [      {        "id": "99",        "type": "ticket",        "zrn": "zen:ticket:99"      }    ],    "survey": {      "id": "01J58KJ9RAE0D2EK7HRVM7Z8F2",      "state": "enabled",      "version": 3    }  }}

**401 Unauthorized**


    // Status 401 Unauthorized
    {  "errors": [    {      "code": "Unauthorized",      "status": "401",      "title": "Unauthorized to access the resource"    }  ]}

**403 Forbidden**


    // Status 403 Forbidden
    {  "errors": [    {      "code": "Forbidden",      "status": "403",      "title": "Access to the resource is forbidden"    }  ]}

**404 Not Found**


    // Status 404 Not Found
    {  "errors": [    {      "code": "NotFound",      "status": "404",      "title": "The survey response could not be found"    }  ]}

**409 Conflict**


    // Status 409 Conflict
    {  "errors": [    {      "code": "Conflict",      "status": "409",      "title": "The survey associated with this survey response has been disabled"    }  ]}

### Show Survey Response

  * `GET /api/v2/guide/{locale}/survey_responses/{id}`


Shows information about the specified survey response.

#### Allowed for

  * Admins
  * End users (responders only)


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
id| string| Path| true| The survey response id
locale| string| Path| true| The locale used for the display of the corresponding survey questions and options

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/guide/{locale}/survey_responses/{id} \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/en-us/survey_responses/01GFYBENPDGN1R6NAA4WRDNVFR"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/en-us/survey_responses/01GFYBENPDGN1R6NAA4WRDNVFR")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/en-us/survey_responses/01GFYBENPDGN1R6NAA4WRDNVFR',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/en-us/survey_responses/01GFYBENPDGN1R6NAA4WRDNVFR"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/en-us/survey_responses/01GFYBENPDGN1R6NAA4WRDNVFR")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "survey_response": {    "answers": [      {        "created_at": "2024-08-14T12:00:00.000Z",        "question": {          "alias": "customer satisfaction rating",          "headline": {            "key": "dc.surveys.customer_satisfaction.questions.rating",            "type": "dynamic",            "value": "How would you rate your experience?"          },          "id": "01J1WBE8QR0YQVE373K2JDJR0F",          "options": [            {              "label": {                "key": "dc.surveys.customer_satisfaction.question.rating.options.bad_rating",                "type": "dynamic",                "value": "Bad"              },              "rating": 1            },            {              "label": {                "key": "dc.surveys.customer_satisfaction.question.rating.options.good_rating",                "type": "dynamic",                "value": "Good"              },              "rating": 2            }          ],          "sub_type": "customer_satisfaction",          "type": "rating_scale_numeric"        },        "rating": 1,        "rating_category": "bad",        "type": "rating_scale",        "updated_at": "2024-08-14T12:00:00.000Z"      },      {        "created_at": "2024-08-14T12:00:00.000Z",        "question": {          "alias": "reason",          "headline": {            "key": "dc.surveys.customer_satisfaction.questions.reason",            "type": "dynamic",            "value": "Select a reason for your experience"          },          "id": "01J1WBGX1BR4ECKTS87CRJTXSF",          "options": [            {              "id": "01J1WBKRG57E6M8C1145EXJ535",              "label": {                "key": "dc.surveys.customer_satisfaction.question.reason.options.too_long",                "type": "dynamic",                "value": "The issue took too long to resolve"              }            }          ],          "type": "closed_ended"        },        "selections": [          {            "option_id": "01J1WBKRG57E6M8C1145EXJ535",            "type": "predefined"          }        ],        "type": "closed_ended",        "updated_at": "2024-08-14T12:00:00.000Z"      },      {        "created_at": "2024-08-14T12:00:00.000Z",        "question": {          "alias": "comment",          "headline": {            "key": "dc.surveys.customer_satisfaction.questions.comment",            "type": "dynamic",            "value": "Share your thoughts on the support you received"          },          "id": "01J1WBNS76ZC4TTFWP9RCNQ1S8",          "type": "open_ended"        },        "type": "open_ended",        "updated_at": "2024-08-14T12:00:00.000Z",        "value": "I had to repeatedly answer the same questions."      },      {        "created_at": "2024-08-14T12:00:00.000Z",        "question": {          "alias": "additional comment",          "headline": {            "type": "static",            "value": "A question to demonstrate a static headline"          },          "id": "01J1WBSAZWVY2XR1EFZKS3CM13",          "type": "open_ended"        },        "type": "skipped",        "updated_at": "2024-08-14T12:00:00.000Z"      }    ],    "expires_at": "2024-08-14T12:00:00.000Z",    "id": "01J1WB51MG6HXTYWE6Q0C93RNW",    "responder_id": 4398080151295,    "subject_zrns": [      "zen:ticket:99"    ],    "subjects": [      {        "id": "99",        "type": "ticket",        "zrn": "zen:ticket:99"      }    ],    "survey": {      "id": "01J58KJ9RAE0D2EK7HRVM7Z8F2",      "state": "enabled",      "version": 3    }  }}

**403 Forbidden**


    // Status 403 Forbidden
    {  "errors": [    {      "code": "Forbidden",      "status": "403",      "title": "Access to the resource is forbidden"    }  ]}

**404 Not Found**


    // Status 404 Not Found
    {  "errors": [    {      "code": "NotFound",      "status": "404",      "title": "The survey response could not be found"    }  ]}

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)