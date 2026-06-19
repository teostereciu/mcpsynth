# CSAT Surveys

*Source: https://developer.zendesk.com/api-reference/ticketing/ticket-management/csat_surveys/*

---

## On this page

  * [JSON format](/api-reference/ticketing/ticket-management/csat_surveys/#json-format)
  * [List Surveys](/api-reference/ticketing/ticket-management/csat_surveys/#list-surveys)
  * [Show Survey By Id And Version](/api-reference/ticketing/ticket-management/csat_surveys/#show-survey-by-id-and-version)


# CSAT Surveys

## On this page

  * [JSON format](/api-reference/ticketing/ticket-management/csat_surveys/#json-format)
  * [List Surveys](/api-reference/ticketing/ticket-management/csat_surveys/#list-surveys)
  * [Show Survey By Id And Version](/api-reference/ticketing/ticket-management/csat_surveys/#show-survey-by-id-and-version)


A survey is an object that represents the CSAT survey. See [Sending a CSAT survey to your customers](https://support.zendesk.com/hc/en-us/articles/7689997846554) in Zendesk Help.

Surveys are available on the Support Professional plan and above, and the Zendesk Suite Growth plan and above.

### JSON format

CSAT Surveys are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
created_at| string| false| true| The date and the time when the survey was created
id| string| false| true| The id of the survey. Automatically assigned when the survey is created
questions| array| false| true| An array of survey question objects. See Question object
state| string| false| true| Whether the survey is active or deactivated. Allowed values are "enabled", or "disabled".
updated_at| string| false| true| The date and the time when the survey was most recently updated
version| integer| false| true| The version of the survey upon which the survey response was based on. Every time the survey is updated, the version is automatically incremented.

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
headline| object| false| false| A text content object representing the headline of the survey question
options| array| false| false| An array of closed-ended survey question options

###### Closed-ended option object

Name| Type| Optional| Nullable| Descriptions
---|---|---|---|---
id| string| false| false| Automatically assigned when the survey question option is created
label| object| false| false| A text content object representing the label of the option
follow_up| object| false| true| A follow up object which points to the following question

##### Open-ended question object

Name| Type| Optional| Nullable| Descriptions
---|---|---|---|---
type| string| false| false| Has the value `open_ended`
id| string| false| false| Automatically assigned when the survey question is created
headline| object| false| false| A text content object representing the headline of the survey question
follow_up| object| false| true| A follow up object which points to the following question

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
sub_type| string| false| false| One of the following values: `customer_satisfaction`, `other`
headline| string| false| false| A text content object representing the headline of the survey question
options| array| false| false| An array of custom text rating scale options

###### Custom text rating scale option object

Name| Type| Optional| Nullable| Descriptions
---|---|---|---|---
rating| integer| false| false| The numeric rating represented by this option
label| object| false| false| A text content object representing the label of this option
follow_up| object| false| true| A follow up object which points to the following question

###### Emoji rating scale question object

Name| Type| Optional| Nullable| Descriptions
---|---|---|---|---
type| string| false| false| Has the value `rating_scale_emoji`
id| string| false| false| Automatically assigned when the survey question is created
sub_type| string| false| false| One of the following values: `customer_satisfaction`, `other`
headline| string| false| false| A text content object representing the headline of the survey question
options| array| false| false| An array of emoji rating scale options

###### Emoji rating scale option object

Name| Type| Optional| Nullable| Descriptions
---|---|---|---|---
rating| integer| false| false| The numeric rating represented by this option
emoji| object| false| false| A text content object representing the emoji of this option
label| object| false| false| A text content object representing the label of this option
follow_up| object| false| true| A follow up object which points to the following question

###### Numeric rating scale question object

Name| Type| Optional| Nullable| Descriptions
---|---|---|---|---
type| string| false| false| Has the value `rating_scale_numeric`
id| string| false| false| Automatically assigned when the survey question is created
sub_type| string| false| false| One of the following values: `customer_satisfaction`, `other`
headline| string| false| false| A text content object representing the headline of the survey question
options| array| false| false| An array of numeric rating scale options

###### Numeric rating scale option object

Name| Type| Optional| Nullable| Descriptions
---|---|---|---|---
rating| integer| false| false| The numeric rating represented by this option
label| object| false| false| A text content object representing the label of this option
follow_up| object| false| true| A follow up object which points to the following question

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

##### Follow up object

Name| Type| Optional| Nullable| Descriptions
---|---|---|---|---
question_id| string| false| false| The id of the next question

#### Example


    {  "created_at": "2025-03-25T00:00:00.000Z",  "id": "01JQ6F1H5B9XSM626BT0M1R0W4",  "questions": [    {      "headline": {        "type": "static",        "value": "How would you rate the support you received?"      },      "id": "01GFYBENPDGN1R6NAA4WRDNVFR",      "options": [        {          "emoji": {            "type": "static",            "value": "ð¡"          },          "follow_up": {            "question_id": "01JQ6E6V6SSXM7796DDCYM73NC"          },          "label": {            "type": "static",            "value": "Very unsatisfied"          },          "rating": 1        },        {          "emoji": {            "type": "static",            "value": "ð"          },          "follow_up": {            "question_id": "01JQ6E6V6SSXM7796DDCYM73NC"          },          "label": {            "type": "static",            "value": "Very satisfied"          },          "rating": 2        }      ],      "sub_type": "customer_satisfaction",      "type": "rating_scale_emoji"    },    {      "headline": {        "type": "static",        "value": "Select a reason regarding your experience"      },      "id": "01JQ6E6V6SSXM7796DDCYM73NC",      "options": [        {          "follow_up": {            "question_id": "01JQ6E6V6SQ9P0KB16GFZN61VK"          },          "id": "01J5DG6N2QMGYWAZ5X7ZCJFEM6",          "label": {            "type": "static",            "value": "The issue took too long to resolve"          }        },        {          "follow_up": {            "question_id": "01JQ6E6V6SQ9P0KB16GFZN61VK"          },          "id": "01J5DGHV93SGA784ANJ0ZFVWRY",          "label": {            "type": "static",            "value": "The issue was not resolved"          }        },        {          "follow_up": {            "question_id": "01JQ6E6V6SQ9P0KB16GFZN61VK"          },          "id": "01J5DGJ0AQV900JBP73V1610AN",          "label": {            "type": "static",            "value": "The information provided was not clear or helpful"          }        }      ],      "type": "closed_ended"    },    {      "follow_up": null,      "headline": {        "type": "static",        "value": "Anything else you would like to share about your experience?"      },      "id": "01JQ6E6V6SQ9P0KB16GFZN61VK",      "type": "open_ended"    }  ],  "state": "enabled",  "updated_at": "2025-03-27T00:00:00.000Z",  "version": 3}

### List Surveys

  * `GET /api/v2/guide/{locale}/surveys`


Shows information about available CSAT surveys.

#### Allowed for

  * Agent users


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
filter| object| Query| false| filter[types] - A comma-separated list of survey types
page| object| Query| false| A group of query parameters used for pagination. See [Pagination](/api-reference/help_center/help-center-api/introduction/#pagination)
locale| string| Path| true| The locale used for the display of the corresponding survey questions and options

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/guide/{locale}/surveys \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/en-us/surveys?filter=&page="	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/en-us/surveys")		.newBuilder()		.addQueryParameter("filter", "")		.addQueryParameter("page", "");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/en-us/surveys',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'filter': '',    'page': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/en-us/surveys?filter=&page="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/en-us/surveys")uri.query = URI.encode_www_form("filter": "", "page": "")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

**curl_filter**


    curl https://{subdomain}.zendesk.com/api/v2/guide/{locale}/surveys?filter[types]=CUSTOMER_SATISFACTION \  -v -u {email_address}/token:{api_token}

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "meta": {    "after_cursor": "MW",    "before_cursor": "MQ",    "has_more": false  },  "surveys": [    {      "created_at": "2025-03-25T00:00:00.000Z",      "id": "01JQ6F1H5B9XSM626BT0M1R0W4",      "questions": [        {          "headline": {            "type": "static",            "value": "How would you rate the support you received?"          },          "id": "01GFYBENPDGN1R6NAA4WRDNVFR",          "options": [            {              "emoji": {                "type": "static",                "value": "ð¡"              },              "follow_up": {                "question_id": "01JQ6E6V6SSXM7796DDCYM73NC"              },              "label": {                "type": "static",                "value": "Very unsatisfied"              },              "rating": 1            },            {              "emoji": {                "type": "static",                "value": "ð"              },              "follow_up": {                "question_id": "01JQ6E6V6SSXM7796DDCYM73NC"              },              "label": {                "type": "static",                "value": "Very satisfied"              },              "rating": 2            }          ],          "sub_type": "customer_satisfaction",          "type": "rating_scale_emoji"        },        {          "headline": {            "type": "static",            "value": "Select a reason regarding your experience"          },          "id": "01JQ6E6V6SSXM7796DDCYM73NC",          "options": [            {              "follow_up": {                "question_id": "01JQ6E6V6SQ9P0KB16GFZN61VK"              },              "id": "01J5DG6N2QMGYWAZ5X7ZCJFEM6",              "label": {                "type": "static",                "value": "The issue took too long to resolve"              }            },            {              "follow_up": {                "question_id": "01JQ6E6V6SQ9P0KB16GFZN61VK"              },              "id": "01J5DGHV93SGA784ANJ0ZFVWRY",              "label": {                "type": "static",                "value": "The issue was not resolved"              }            },            {              "follow_up": {                "question_id": "01JQ6E6V6SQ9P0KB16GFZN61VK"              },              "id": "01J5DGJ0AQV900JBP73V1610AN",              "label": {                "type": "static",                "value": "The information provided was not clear or helpful"              }            }          ],          "type": "closed_ended"        },        {          "follow_up": null,          "headline": {            "type": "static",            "value": "Anything else you would like to share about your experience?"          },          "id": "01JQ6E6V6SQ9P0KB16GFZN61VK",          "type": "open_ended"        }      ],      "state": "enabled",      "updated_at": "2025-03-27T00:00:00.000Z",      "version": 3    }  ]}

### Show Survey By Id And Version

  * `GET /api/v2/guide/{locale}/surveys/{id}/{version}`


Shows information about the specified survey by the id and the version.

The endpoint returns the latest available version if the `version` parameter is greater than the latest available version.

#### Allowed for

  * Anonymous users


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
id| string| Path| true| The survey response id
locale| string| Path| true| The locale used for the display of the corresponding survey questions and options
version| integer| Path| true| The version of the survey upon which the survey response was based on. Every time the survey is updated, the version is automatically incremented.

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/guide/{locale}/survey/{id}/{version} \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/en-us/surveys/01JQ6F1H5B9XSM626BT0M1R0W4/3"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/en-us/surveys/01JQ6F1H5B9XSM626BT0M1R0W4/3")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/en-us/surveys/01JQ6F1H5B9XSM626BT0M1R0W4/3',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/en-us/surveys/01JQ6F1H5B9XSM626BT0M1R0W4/3"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/en-us/surveys/01JQ6F1H5B9XSM626BT0M1R0W4/3")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "survey": {    "created_at": "2025-03-25T00:00:00.000Z",    "id": "01JQ6F1H5B9XSM626BT0M1R0W4",    "questions": [      {        "headline": {          "type": "static",          "value": "How would you rate the support you received?"        },        "id": "01GFYBENPDGN1R6NAA4WRDNVFR",        "options": [          {            "emoji": {              "type": "static",              "value": "ð¡"            },            "follow_up": {              "question_id": "01JQ6E6V6SSXM7796DDCYM73NC"            },            "label": {              "type": "static",              "value": "Very unsatisfied"            },            "rating": 1          },          {            "emoji": {              "type": "static",              "value": "ð"            },            "follow_up": {              "question_id": "01JQ6E6V6SSXM7796DDCYM73NC"            },            "label": {              "type": "static",              "value": "Very satisfied"            },            "rating": 2          }        ],        "sub_type": "customer_satisfaction",        "type": "rating_scale_emoji"      },      {        "headline": {          "type": "static",          "value": "Select a reason regarding your experience"        },        "id": "01JQ6E6V6SSXM7796DDCYM73NC",        "options": [          {            "follow_up": {              "question_id": "01JQ6E6V6SQ9P0KB16GFZN61VK"            },            "id": "01J5DG6N2QMGYWAZ5X7ZCJFEM6",            "label": {              "type": "static",              "value": "The issue took too long to resolve"            }          },          {            "follow_up": {              "question_id": "01JQ6E6V6SQ9P0KB16GFZN61VK"            },            "id": "01J5DGHV93SGA784ANJ0ZFVWRY",            "label": {              "type": "static",              "value": "The issue was not resolved"            }          },          {            "follow_up": {              "question_id": "01JQ6E6V6SQ9P0KB16GFZN61VK"            },            "id": "01J5DGJ0AQV900JBP73V1610AN",            "label": {              "type": "static",              "value": "The information provided was not clear or helpful"            }          }        ],        "type": "closed_ended"      },      {        "follow_up": null,        "headline": {          "type": "static",          "value": "Anything else you would like to share about your experience?"        },        "id": "01JQ6E6V6SQ9P0KB16GFZN61VK",        "type": "open_ended"      }    ],    "state": "enabled",    "updated_at": "2025-03-27T00:00:00.000Z",    "version": 3  }}

**404 Not Found**


    // Status 404 Not Found
    {  "errors": [    {      "code": "NotFound",      "status": "404",      "title": "The survey could not be found"    }  ]}

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)