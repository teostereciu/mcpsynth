# Schedules

*Source: https://developer.zendesk.com/api-reference/ticketing/ticket-management/schedules/*

---

## On this page

  * [JSON format](/api-reference/ticketing/ticket-management/schedules/#json-format)
  * [List Schedules](/api-reference/ticketing/ticket-management/schedules/#list-schedules)
  * [Show Schedule](/api-reference/ticketing/ticket-management/schedules/#show-schedule)
  * [Create Schedule](/api-reference/ticketing/ticket-management/schedules/#create-schedule)
  * [Update Schedule](/api-reference/ticketing/ticket-management/schedules/#update-schedule)
  * [Delete Schedule](/api-reference/ticketing/ticket-management/schedules/#delete-schedule)
  * [List Holidays for Schedule](/api-reference/ticketing/ticket-management/schedules/#list-holidays-for-schedule)
  * [Show Holiday](/api-reference/ticketing/ticket-management/schedules/#show-holiday)
  * [Create Holiday](/api-reference/ticketing/ticket-management/schedules/#create-holiday)
  * [Update Holiday](/api-reference/ticketing/ticket-management/schedules/#update-holiday)
  * [Delete Holiday](/api-reference/ticketing/ticket-management/schedules/#delete-holiday)
  * [Update Intervals for a Schedule](/api-reference/ticketing/ticket-management/schedules/#update-intervals-for-a-schedule)


# Schedules

## On this page

  * [JSON format](/api-reference/ticketing/ticket-management/schedules/#json-format)
  * [List Schedules](/api-reference/ticketing/ticket-management/schedules/#list-schedules)
  * [Show Schedule](/api-reference/ticketing/ticket-management/schedules/#show-schedule)
  * [Create Schedule](/api-reference/ticketing/ticket-management/schedules/#create-schedule)
  * [Update Schedule](/api-reference/ticketing/ticket-management/schedules/#update-schedule)
  * [Delete Schedule](/api-reference/ticketing/ticket-management/schedules/#delete-schedule)
  * [List Holidays for Schedule](/api-reference/ticketing/ticket-management/schedules/#list-holidays-for-schedule)
  * [Show Holiday](/api-reference/ticketing/ticket-management/schedules/#show-holiday)
  * [Create Holiday](/api-reference/ticketing/ticket-management/schedules/#create-holiday)
  * [Update Holiday](/api-reference/ticketing/ticket-management/schedules/#update-holiday)
  * [Delete Holiday](/api-reference/ticketing/ticket-management/schedules/#delete-holiday)
  * [Update Intervals for a Schedule](/api-reference/ticketing/ticket-management/schedules/#update-intervals-for-a-schedule)


You can set a schedule in Zendesk to acknowledge your support team's availability and give customers a better sense of when they can expect a personal response to their support requests.

You can use this API to create multiple schedules with different business hours and holidays.

To learn more about schedules, see [Setting your schedule with business hours and holidays](https://support.zendesk.com/hc/en-us/articles/203662206) in Zendesk help.

### JSON format

Schedules are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
created_at| string| true| false| Time the schedule was created
id| integer| true| false| Automatically assigned upon creation
intervals| array| false| false| An array of starting and ending times for the schedule. Can't span calendar days. See intervals. Writable only when [updating intervals for a schedule](/api-reference/ticketing/ticket-management/schedules/#update-intervals-for-a-schedule)
name| string| false| true| Name of the schedule
time_zone| string| false| true| Time zone of the schedule
updated_at| string| true| false| Time the schedule was last updated

#### Intervals

An interval represents a period of business hours. Intervals are writable only when [updating intervals for a schedule](/api-reference/ticketing/ticket-management/schedules/#update-intervals-for-a-schedule). Otherwise, intervals are read-only.

Intervals are represented with the following attributes:

Name| Type| Comment
---|---|---
start_time| integer| Integer representation of the interval start time in minutes since Sunday at midnight
end_time| integer| Integer representation of the interval end time in minutes since Sunday at midnight. Can't span calendar days

The `start_time` and `end_time` values are expressed as the number of minutes since the start of the week, which is defined as Sunday at midnight. Intervals can't span calendar days.

For example, an interval might start on Monday at 9:00 a.m. and end at 17:00 (5 p.m.).


    {  "start_time": 1980,  "end_time": 3900}

If you have multiple shifts per day, an interval might start on Tuesday at 16:00 (4 p.m.) and end at 00:00 (midnight). Intervals can't span calendar days, so must end at midnight at the latest. To avoid gaps in business hours, you can use midnight as the end time for an interval and the start time for the following interval.


    {  "start_time": 3840,  "end_time": 4320}

To calculate the start and end times, use the equation: ((hours since Sunday at midnight)*60) + (minutes of incomplete hour). To help you more easily determine your start and end times, the following table lists the minutes since Sunday at midnight at 12-hour increments throughout the week.

Week time| Minute time
---|---
Sunday midnight| 0, 10080
Sunday noon| 720
Monday midnight| 1440
Monday noon| 2160
Tuesday midnight| 2880
Tuesday noon| 3600
Wednesday midnight| 4320
Wednesday noon| 5040
Thursday midnight| 5760
Thursday noon| 6480
Friday midnight| 7200
Friday noon| 7920
Saturday midnight| 8640
Saturday noon| 9360

The end of the week is defined as Saturday at 23:59 (11:59 pm). In minutes since Sunday at midnight, this is 10079. The API accepts a value of `0` or `10080` to represent midnight between Saturday and Sunday.

#### Holidays

Holidays are represented with the following attributes:

Name| Type| Comment
---|---|---
id| integer| Automatically assigned upon creation
name| string| Name of the holiday
start_date| string| ISO 8601 representation of the holiday start date
end_date| string| ISO 8601 representation of the holiday end date

Holidays can be a single day or multiple days in length.

Example


    {"id": 1, "name": "New Year's Day 2016", "start_date": "2016-01-01", "end_date": "2016-01-01"}

#### Time Zone

A `time_zone` name consists of a string such as "Eastern Time (US & Canada)". For a list of valid names, click <https://support.zendesk.com/api/v2/time_zones>[](https://support.zendesk.com/api/v2/time_zones). For details, see [Time Zones](/api-reference/introduction/data-types/#time-zones).

Example:


    {  "schedule": {    "name": "North America",    "time_zone": "Pacific Time (US & Canada)",    ...  }}

#### Example


    {  "id": 1,  "intervals": [    {      "end_time": 2460,      "start_time": 1980    },    {      "end_time": 3900,      "start_time": 3420    }  ],  "name": "North America",  "time_zone": "Pacific Time (US & Canada)"}

### List Schedules

  * `GET /api/v2/business_hours/schedules`


#### Allowed For

  * Admins


#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/business_hours/schedules.json \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/business_hours/schedules"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/business_hours/schedules")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/business_hours/schedules',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/business_hours/schedules"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/business_hours/schedules")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "schedules": [    {      "created_at": "2015-09-30T21:44:03Z",      "id": 1,      "intervals": [        {          "end_time": 2460,          "start_time": 1980        },        {          "end_time": 3900,          "start_time": 3420        }      ],      "name": "North America",      "time_zone": "Pacific Time (US & Canada)",      "updated_at": "2015-09-30T21:44:03Z"    },    {      "created_at": "2015-09-30T21:44:03Z",      "id": 2,      "intervals": [        {          "end_time": 2460,          "start_time": 1980        },        {          "end_time": 3900,          "start_time": 3420        }      ],      "name": "EMEA",      "time_zone": "London",      "updated_at": "2015-09-30T21:44:03Z"    }  ]}

### Show Schedule

  * `GET /api/v2/business_hours/schedules/{schedule_id}`


#### Allowed For

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
schedule_id| integer| Path| true| The ID of the schedule

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/business_hours/schedules/{schedule_id}.json \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/business_hours/schedules/1"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/business_hours/schedules/1")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/business_hours/schedules/1',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/business_hours/schedules/1"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/business_hours/schedules/1")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "schedule": {    "created_at": "2015-09-30T21:44:03Z",    "id": 1,    "intervals": [      {        "end_time": 2460,        "start_time": 1980      },      {        "end_time": 3900,        "start_time": 3420      }    ],    "name": "North America",    "time_zone": "Pacific Time (US & Canada)",    "updated_at": "2015-09-30T21:44:03Z"  }}

### Create Schedule

  * `POST /api/v2/business_hours/schedules`


#### Allowed For

  * Admins


#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/business_hours/schedules.json \  -v -u {email_address}/token:{api_token} \  -H "Content-Type: application/json" -X POST  -d '{"schedule": {"name": "East Coast", "time_zone": "Eastern Time (US & Canada)"}}'

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/business_hours/schedules"	method := "POST"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/business_hours/schedules")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'POST',  url: 'https://support.zendesk.com/api/v2/business_hours/schedules',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/business_hours/schedules"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/business_hours/schedules")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**201 Created**


    // Status 201 Created
    {  "schedule": {    "id": 1,    "intervals": [      {        "end_time": 2460,        "start_time": 1980      },      {        "end_time": 3900,        "start_time": 3420      },      {        "end_time": 5340,        "start_time": 4860      },      {        "end_time": 6780,        "start_time": 6300      },      {        "end_time": 8220,        "start_time": 7740      }    ],    "name": "East Coast",    "time_zone": "Eastern Time (US & Canada)"  }}

### Update Schedule

  * `PUT /api/v2/business_hours/schedules/{schedule_id}`


#### Allowed For

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
schedule_id| integer| Path| true| The ID of the schedule

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/business_hours/schedules/{schedule_id}.json \  -v -u {email_address}/token:{api_token} \  -H "Content-Type: application/json" -X PUT  -d '{"schedule": {"name": "EMEA", "time_zone": "London"}}'

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/business_hours/schedules/1"	method := "PUT"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/business_hours/schedules/1")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'PUT',  url: 'https://support.zendesk.com/api/v2/business_hours/schedules/1',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/business_hours/schedules/1"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/business_hours/schedules/1")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "schedule": {    "created_at": "2015-09-30T21:44:03Z",    "id": 1,    "intervals": [      {        "end_time": 2460,        "start_time": 1980      },      {        "end_time": 3900,        "start_time": 3420      },      {        "end_time": 5340,        "start_time": 4860      },      {        "end_time": 6780,        "start_time": 6300      },      {        "end_time": 8220,        "start_time": 7740      }    ],    "name": "EMEA",    "time_zone": "London",    "updated_at": "2015-09-30T21:44:03Z"  }}

### Delete Schedule

  * `DELETE /api/v2/business_hours/schedules/{schedule_id}`


#### Allowed For

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
schedule_id| integer| Path| true| The ID of the schedule

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/business_hours/schedules/{schedule_id}.json \  -v -u {email_address}/token:{api_token} \  -H "Content-Type: application/json" -X DELETE

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/business_hours/schedules/1"	method := "DELETE"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/business_hours/schedules/1")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("DELETE", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'DELETE',  url: 'https://support.zendesk.com/api/v2/business_hours/schedules/1',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/business_hours/schedules/1"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"DELETE",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/business_hours/schedules/1")request = Net::HTTP::Delete.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**204 No Content**


    // Status 204 No Content
    null

### List Holidays for Schedule

  * `GET /api/v2/business_hours/schedules/{schedule_id}/holidays`


The endpoint takes `start_date` and `end_date` query parameters. If you specify only a `start_date`, holidays beginning on or after that date are returned. If the `start_date` falls during a holiday, the holiday is also included. As a result the response may list some holidays that start before the `start_date`.

If you specify only an `end_date`, holidays beginning on or before that date are returned.

If you specify both a `start_date` and an `end_date`, holidays beginning between those dates are returned. If you specify neither, all holidays are returned.

#### Allowed For

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
end_date| string| Query| false| Must be in ISO 8601 date format. For example: "2021-01-01".
start_date| string| Query| false| Must be in ISO 8601 date format. For example, "2021-01-01".
schedule_id| integer| Path| true| The ID of the schedule

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/business_hours/schedules/{schedule_id}/holidays.json  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/business_hours/schedules/1/holidays?end_date=2021-01-01&start_date=2021-01-01"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/business_hours/schedules/1/holidays")		.newBuilder()		.addQueryParameter("end_date", "2021-01-01")		.addQueryParameter("start_date", "2021-01-01");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/business_hours/schedules/1/holidays',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'end_date': '2021-01-01',    'start_date': '2021-01-01',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/business_hours/schedules/1/holidays?end_date=2021-01-01&start_date=2021-01-01"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/business_hours/schedules/1/holidays")uri.query = URI.encode_www_form("end_date": "2021-01-01", "start_date": "2021-01-01")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "holidays": [    {      "end_date": "2021-07-04",      "id": 1,      "name": "Independence Day",      "start_date": "2021-07-04"    },    {      "end_date": "2021-12-25",      "id": 2,      "name": "Christmas",      "start_date": "2021-12-25"    }  ]}

### Show Holiday

  * `GET /api/v2/business_hours/schedules/{schedule_id}/holidays/{holiday_id}`


#### Allowed For

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
holiday_id| integer| Path| false| The ID of the scheduled holiday
schedule_id| integer| Path| true| The ID of the schedule

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/business_hours/schedules/{schedule_id}/holidays/{holiday_id}.json \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/business_hours/schedules/1/holidays/1"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/business_hours/schedules/1/holidays/1")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/business_hours/schedules/1/holidays/1',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/business_hours/schedules/1/holidays/1"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/business_hours/schedules/1/holidays/1")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "holiday": {    "end_date": "2021-01-02",    "id": 1,    "name": "New Year",    "start_date": "2020-12-30"  }}

### Create Holiday

  * `POST /api/v2/business_hours/schedules/{schedule_id}/holidays`


Creates a holiday defined by a start date no sooner than two years in the past and an end date no later than two years in the future.

#### Allowed For

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
schedule_id| integer| Path| true| The ID of the schedule

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/business_hours/schedules/{schedule_id}/holidays.json \  -d '{"holiday": {"name": "New Year", "start_date": "2021-12-30", "end_date": "2022-01-02"}}' \  -H "Content-Type: application/json" -X POST \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/business_hours/schedules/1/holidays"	method := "POST"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/business_hours/schedules/1/holidays")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'POST',  url: 'https://support.zendesk.com/api/v2/business_hours/schedules/1/holidays',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/business_hours/schedules/1/holidays"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/business_hours/schedules/1/holidays")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**201 Created**


    // Status 201 Created
    {  "holiday": {    "end_date": "2021-01-02",    "id": 2,    "name": "New Year",    "start_date": "2020-12-30"  }}

### Update Holiday

  * `PUT /api/v2/business_hours/schedules/{schedule_id}/holidays/{holiday_id}`


#### Allowed For

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
holiday_id| integer| Path| false| The ID of the scheduled holiday
schedule_id| integer| Path| true| The ID of the schedule

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/business_hours/schedules/{schedule_id}/holidays/{holiday_id}.json \  -d '{"holiday": {"name": "New Year", "start_date": "2021-12-30", "end_date": "2022-01-03"}}' \  -H "Content-Type: application/json" -X PUT \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/business_hours/schedules/1/holidays/1"	method := "PUT"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/business_hours/schedules/1/holidays/1")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'PUT',  url: 'https://support.zendesk.com/api/v2/business_hours/schedules/1/holidays/1',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/business_hours/schedules/1/holidays/1"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/business_hours/schedules/1/holidays/1")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "holiday": {    "end_date": "2022-01-03",    "id": 2,    "name": "New Year",    "start_date": "2021-12-30"  }}

### Delete Holiday

  * `DELETE /api/v2/business_hours/schedules/{schedule_id}/holidays/{holiday_id}`


#### Allowed For

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
holiday_id| integer| Path| false| The ID of the scheduled holiday
schedule_id| integer| Path| true| The ID of the schedule

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/business_hours/schedules/{schedule_id}/holidays/{holiday_id}.json \  -H "Content-Type: application/json" -X DELETE \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/business_hours/schedules/1/holidays/1"	method := "DELETE"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/business_hours/schedules/1/holidays/1")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("DELETE", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'DELETE',  url: 'https://support.zendesk.com/api/v2/business_hours/schedules/1/holidays/1',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/business_hours/schedules/1/holidays/1"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"DELETE",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/business_hours/schedules/1/holidays/1")request = Net::HTTP::Delete.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**204 No Content**


    // Status 204 No Content
    null

### Update Intervals for a Schedule

  * `PUT /api/v2/business_hours/schedules/{schedule_id}/workweek`


#### Allowed For

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
schedule_id| integer| Path| true| The ID of the schedule

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/business_hours/schedules/{schedule_id}/workweek.json \  -v -u {email_address}/token:{api_token} \  -H "Content-Type: application/json" -X PUT \  -d '{"workweek": {"intervals": [{"start_time": 3420, "end_time": 3900}]}}'

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/business_hours/schedules/1/workweek"	method := "PUT"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/business_hours/schedules/1/workweek")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'PUT',  url: 'https://support.zendesk.com/api/v2/business_hours/schedules/1/workweek',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/business_hours/schedules/1/workweek"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/business_hours/schedules/1/workweek")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "workweek": {    "intervals": [      {        "end_time": 3900,        "start_time": 3420      }    ]  }}

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)