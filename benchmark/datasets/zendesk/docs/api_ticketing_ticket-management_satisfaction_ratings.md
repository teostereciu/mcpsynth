# Satisfaction Ratings

*Source: https://developer.zendesk.com/api-reference/ticketing/ticket-management/satisfaction_ratings/*

---

## On this page

  * [JSON format](/api-reference/ticketing/ticket-management/satisfaction_ratings/#json-format)
  * [List Satisfaction Ratings](/api-reference/ticketing/ticket-management/satisfaction_ratings/#list-satisfaction-ratings)
  * [Count Satisfaction Ratings](/api-reference/ticketing/ticket-management/satisfaction_ratings/#count-satisfaction-ratings)
  * [Show Satisfaction Rating](/api-reference/ticketing/ticket-management/satisfaction_ratings/#show-satisfaction-rating)
  * [Create a Satisfaction Rating](/api-reference/ticketing/ticket-management/satisfaction_ratings/#create-a-satisfaction-rating)


# Satisfaction Ratings

## On this page

  * [JSON format](/api-reference/ticketing/ticket-management/satisfaction_ratings/#json-format)
  * [List Satisfaction Ratings](/api-reference/ticketing/ticket-management/satisfaction_ratings/#list-satisfaction-ratings)
  * [Count Satisfaction Ratings](/api-reference/ticketing/ticket-management/satisfaction_ratings/#count-satisfaction-ratings)
  * [Show Satisfaction Rating](/api-reference/ticketing/ticket-management/satisfaction_ratings/#show-satisfaction-rating)
  * [Create a Satisfaction Rating](/api-reference/ticketing/ticket-management/satisfaction_ratings/#create-a-satisfaction-rating)


**Note** : The endpoints listed on this page are for the [legacy CSAT feature](https://support.zendesk.com/hc/en-us/articles/4408822875034). We recommend you use survey responses for more accurate and relevant feedback. For more information, see [CSAT Survey responses](/api-reference/ticketing/ticket-management/csat_survey_responses/), [Survey offered event](/documentation/ticketing/reference-guides/ticket-audit-events-reference/#survey-offered-event), and [Survey response submitted event](/documentation/ticketing/reference-guides/ticket-audit-events-reference/#survey-response-submitted-event). See also [Setting up the CSAT survey](https://support.zendesk.com/hc/en-us/articles/7689997846554). If you are using the legacy CSAT, you must [deactivate legacy CSAT and manually deactivate any custom CSAT automations and triggers](https://support.zendesk.com/hc/en-us/articles/4408822875034#topic_lgj_cmr_w1c) before you can use survey responses. You can have only one CSAT option activated at a time.

If you have enabled satisfaction ratings for your account, this endpoint allows you to quickly retrieve all ratings.

It supports cursor pagination and offset pagination when paginating through results. See [Pagination](/api-reference/introduction/pagination/).

### JSON format

Satisfaction Ratings are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
assignee_id| integer| true| true| The id of agent assigned to at the time of rating
comment| string| false| false| The comment received with this rating, if available
created_at| string| true| false| The time the satisfaction rating got created
group_id| integer| true| true| The id of group assigned to at the time of rating
id| integer| true| false| Automatically assigned upon creation
reason| string| false| false| The reason for a bad rating given by the requester in a follow-up question. Satisfaction reasons must be [enabled](https://support.zendesk.com/hc/en-us/articles/223152967)
reason_code| integer| false| false| The default reasons the user can select from a list menu for giving a negative rating. See [Reason codes](/api-reference/ticketing/ticket-management/satisfaction_reasons/#reason-codes) in the Satisfaction Reasons API. Can only be set on ratings with a `score` of "bad". Responses don't include this property
reason_id| integer| false| false| id for the reason the user gave a negative rating. Can only be set on ratings with a `score` of "bad". To get a descriptive value for the id, use the [Show Reason for Satisfaction Rating](/api-reference/ticketing/ticket-management/satisfaction_reasons/#show-reason-for-satisfaction-rating) endpoint
requester_id| integer| true| true| The id of ticket requester submitting the rating
score| string| false| true| The rating "offered", "unoffered", "good" or "bad". For POST requests, only "good" or "bad" are valid
ticket_id| integer| true| true| The id of ticket being rated
updated_at| string| true| false| The time the satisfaction rating got updated
url| string| true| false| The API url of this rating

#### Example


    {  "assignee_id": 135,  "created_at": "2011-07-20T22:55:29Z",  "group_id": 44,  "id": 35436,  "requester_id": 7881,  "score": "good",  "ticket_id": 208,  "updated_at": "2011-07-20T22:55:29Z",  "url": "https://company.zendesk.com/api/v2/satisfaction_ratings/62"}

### List Satisfaction Ratings

  * `GET /api/v2/satisfaction_ratings`


#### Allowed For

  * Admins


#### Pagination

  * Cursor pagination (recommended)
  * Offset pagination


See [Pagination](/api-reference/introduction/pagination/).

#### Filters

Parameter| Value
---|---
score| offered, unoffered, received, received_with_comment, received_without_comment,
good, good_with_comment, good_without_comment,
bad, bad_with_comment, bad_without_comment
start_time| Time of the oldest satisfaction rating, as a [Unix epoch time](https://www.epochconverter.com/)
end_time| Time of the most recent satisfaction rating, as a [Unix epoch time](https://www.epochconverter.com/)

If you specify an unqualified score such as `good`, the results include all the records with and without comments.

Examples:

  * `/api/v2/satisfaction_ratings?score=bad`
  * `/api/v2/satisfaction_ratings?score=bad&start_time=1498151194`
  * `/api/v2/satisfaction_ratings?start_time=1340384793&end_time=1371920793`


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
page| | Query| false| Pagination parameter. Supports both traditional offset and cursor-based pagination: - Traditional: `?page=2` (integer page number) - Cursor: `?page[size]=50&page[after]=cursor` (deepObject with size, after, before) These are mutually exclusive - use one format or the other, not both.
per_page| integer| Query| false| Number of records to return per page. Note: Default and maximum values vary by endpoint. Check endpoint-specific documentation for limits.
sort| string| Query| false| Field to sort results by. Prefix with `-` for descending order. When used with cursor pagination, this determines the cursor ordering. Example: `?sort=name` or `?sort=-created_at`

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/satisfaction_ratings \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/satisfaction_ratings?page=&per_page=50&sort=name"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/satisfaction_ratings")		.newBuilder()		.addQueryParameter("page", "")		.addQueryParameter("per_page", "50")		.addQueryParameter("sort", "name");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/satisfaction_ratings',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'page': '',    'per_page': '50',    'sort': 'name',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/satisfaction_ratings?page=&per_page=50&sort=name"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/satisfaction_ratings")uri.query = URI.encode_www_form("page": "", "per_page": "50", "sort": "name")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "satisfaction_ratings": [    {      "assignee_id": 135,      "comment": "Awesome support!",      "created_at": "2011-07-20T22:55:29Z",      "group_id": 44,      "id": 35436,      "requester_id": 7881,      "score": "good",      "ticket_id": 208,      "updated_at": "2011-07-20T22:55:29Z",      "url": "https://example.zendesk.com/api/v2/satisfaction_ratings/35436"    },    {      "assignee_id": 136,      "comment": "Awesome support!",      "created_at": "2012-02-01T04:31:29Z",      "group_id": 44,      "id": 120447,      "requester_id": 7881,      "score": "good",      "ticket_id": 209,      "updated_at": "2012-02-02T10:32:59Z",      "url": "https://example.zendesk.com/api/v2/satisfaction_ratings/120447"    }  ]}

### Count Satisfaction Ratings

  * `GET /api/v2/satisfaction_ratings/count`


Returns an approximate count of satisfaction ratings in the account. If the count exceeds 100,000, the count will return a cached result. This cached result will update every 24 hours.

The `count[refreshed_at]` property is a timestamp that indicates when the count was last updated.

**Note** : When the count exceeds 100,000, `count[refreshed_at]` may occasionally be null. This indicates that the count is being updated in the background, and `count[value]` is limited to 100,000 until the update is complete.

#### Allowed For

  * Admins


#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/satisfaction_ratings/count \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/satisfaction_ratings/count"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/satisfaction_ratings/count")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/satisfaction_ratings/count',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/satisfaction_ratings/count"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/satisfaction_ratings/count")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "count": {    "refreshed_at": "2020-04-06T02:18:17Z",    "value": 102  }}

### Show Satisfaction Rating

  * `GET /api/v2/satisfaction_ratings/{satisfaction_rating_id}`


Returns a specific satisfaction rating. You can get the id from the List Satisfaction Ratings endpoint.

#### Allowed For

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
satisfaction_rating_id| integer| Path| true| The id of the satisfaction rating to retrieve

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/satisfaction_ratings/{satisfaction_rating_id} \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/satisfaction_ratings/35436"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/satisfaction_ratings/35436")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/satisfaction_ratings/35436',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/satisfaction_ratings/35436"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/satisfaction_ratings/35436")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "satisfaction_rating": [    {      "assignee_id": 135,      "comment": "Awesome support!",      "created_at": "2011-07-20T22:55:29Z",      "group_id": 44,      "id": 35436,      "requester_id": 7881,      "score": "good",      "ticket_id": 208,      "updated_at": "2011-07-20T22:55:29Z",      "url": "https://example.zendesk.com/api/v2/satisfaction_ratings/35436"    }  ]}

### Create a Satisfaction Rating

  * `POST /api/v2/tickets/{ticket_id}/satisfaction_rating`


Creates a CSAT rating for a solved ticket, or for a ticket that was previously solved and then reopened.

Only the end user listed as the ticket requester can create a satisfaction rating for the ticket.

Only "good" and "bad" are valid values for the score when creating a rating. Other states, like "offered", are not valid and will result in a 422 error.

#### Allowed For

  * End user who requested the ticket


The end user must be a verified user.

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
ticket_id| integer| Path| true| The id of the ticket

#### Code Samples

**curl**

Good rating


    curl https://{subdomain}.zendesk.com/api/v2/tickets/{ticket_id}/satisfaction_rating \    -X POST -d '{"satisfaction_rating": {"score": "good", "comment": "Awesome support."}}' \    -v -u {email_address}/token:{api_token} -H "Content-Type: application/json"

**curl**

Bad rating


    curl https://{subdomain}.zendesk.com/api/v2/tickets/{ticket_id}/satisfaction_rating \  -X POST -d '{"satisfaction_rating": {"score": "bad", "comment": "Needed more detail.", "reason_code":100}}' \  -v -u {email_address}/token:{api_token} -H "Content-Type: application/json"

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/tickets/35436/satisfaction_rating"	method := "POST"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/tickets/35436/satisfaction_rating")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'POST',  url: 'https://example.zendesk.com/api/v2/tickets/35436/satisfaction_rating',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/tickets/35436/satisfaction_rating"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/tickets/35436/satisfaction_rating")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "satisfaction_rating": [    {      "assignee_id": 135,      "comment": "Awesome support!",      "created_at": "2011-07-20T22:55:29Z",      "group_id": 44,      "id": 35436,      "requester_id": 7881,      "score": "good",      "ticket_id": 208,      "updated_at": "2011-07-20T22:55:29Z",      "url": "https://example.zendesk.com/api/v2/satisfaction_ratings/35436"    }  ]}

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)