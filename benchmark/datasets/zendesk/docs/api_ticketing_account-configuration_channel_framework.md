# Channel Framework

*Source: https://developer.zendesk.com/api-reference/ticketing/account-configuration/channel_framework/*

---

## On this page

  * [Push Content to Support](/api-reference/ticketing/account-configuration/channel_framework/#push-content-to-support)
  * [Validate Token](/api-reference/ticketing/account-configuration/channel_framework/#validate-token)
  * [Report Channelback Error to Zendesk](/api-reference/ticketing/account-configuration/channel_framework/#report-channelback-error-to-zendesk)


# Channel Framework

## On this page

  * [Push Content to Support](/api-reference/ticketing/account-configuration/channel_framework/#push-content-to-support)
  * [Validate Token](/api-reference/ticketing/account-configuration/channel_framework/#validate-token)
  * [Report Channelback Error to Zendesk](/api-reference/ticketing/account-configuration/channel_framework/#report-channelback-error-to-zendesk)


The Channel framework lets you build two-way ticket-creation services between Zendesk Support and an external system such as Facebook, Twitter, or Instagram -- to give just a few examples. For more information, see the [Channel Framework](/documentation/channel_framework/) developer docs.

### Push Content to Support

  * `POST /api/v2/any_channel/push`


Pushes Channel framework content to Zendesk.

#### Allowed For

  * Admins


#### Request parameters

The POST request takes a JSON object parameter which contains data about all the resources that the client is pushing.

Name| Type| Required| Comments
---|---|---|---
instance_push_id| string| yes| The account ID where data will be pushed. This was passed to the integration service when the administrator set up the account
request_id| string| no| A unique identifier for the push request
external_resources| array| yes| The resources to push

#### external_resource object

Name| Type| Max length| Mandatory| Comments
---|---|---|---|---
external_id| string| 255| yes| Unique identifier of the external resource. Must be ASCII characters
internal_note| boolean| | no| If `true` creates a new internal note comment
message| string| 65535| yes| Text to be converted to a ticket or comment
html_message| string| 65535| no| HTML version of message
parent_id| string| 511| no| Unique identifier of the external resource for which this is a response. Used to choose the correct thread. Responses may include `parent_id` or `thread_id`, but not both. See [Conversation threads](/documentation/channel_framework/understanding-the-channel-framework/pull_endpoint/#conversation-threads)
thread_id| string| 255| no| Arbitrary identifier of the thread to which this item should belong. Responses may include `parent_id` or `thread_id`, but not both. See [Conversation threads](/documentation/channel_framework/understanding-the-channel-framework/pull_endpoint/#conversation-threads)
created_at| string| | yes| When the resource was created in the origin system, as an ISO 8601 extended format date-time. Example: '2015-09-08T22:48:09Z'
author| object| | yes| See author object below
display_info| array| | no| Array of integration-specific data used by apps to modify the agent UI. See display_info object below
allow_channelback| boolean| | no| If `false`, prevents the agent from making additional comments on the message in the Zendesk interface
fields| array| | no| Array of ticket fields to set in Zendesk and their values. See fields array
file_urls| array| 10| no| Array of files to be imported into Zendesk. See [file urls](/documentation/channel_framework/understanding-the-channel-framework/pull_endpoint/#file-urls) in the Channel framework docs

#### author object

Name| Type| Max chars| Mandatory| Comments
---|---|---|---|---
external_id| string| 255| yes| Unique identifier of the user in the origin service
name| string| 255| no| If not supplied, defaults to external id
image_url| string| 255| no| URL to an image for the user
locale| String| 255| no| The user's locale. Must be one of the supported [locales](/api-reference/ticketing/account-configuration/locales/#list-available-public-locales) in Zendesk
fields| array| | no| Array of items containing user field identifier ('id') and value of field ('value'.) For system fields ('notes' or 'details'), the identifier is the English name. For custom fields, the identifier may be the ID or the name

#### display_info object

Name| Type| Max chars| Mandatory| Comments
---|---|---|---|---
type| string| 255| yes| Globally unique type identifier defined by the integration origin service. Examples: a GUID or URI
data| string| 65535| yes| JSON data containing display hints

#### fields array

The `fields` array lists ticket fields to set in Zendesk and their values. Each item consists of a field identifier (`id`) and a value (`value`) for the field. For Zendesk system fields such as `subject`, the identifier is the English name. For custom fields, the identifier may be a field ID or a name. See [Ticket Fields](/api-reference/ticketing/tickets/ticket_fields/).

The `fields` array can only set ticket values on ticket creation, not on ticket updates.

#### Response format

The response is a JSON object containing a single key:

Name| Type| Comments
---|---|---
results| array| An array of result objects

The `results` array contains an entry for each item in the incoming `external_resources` array, in the same order. For example, if you call `push` with 3 external resources, a successful response will include `results` with three entries, corresponding to your 3 resources.

#### result object

Name| Type| Comments
---|---|---
external_resource_id| string| The external ID of the resource, as passed in
status| object| The status of the import for the indicated resource. See status object

#### status object

Name| Type| Comments
---|---|---
code| string| A code indicating the status of the import of the resource, as described in status codes
description| string| In the case of an exception, a description of the exception. Otherwise, not present.

#### status codes

Key| Description
---|---
success| The external resource was successfully converted to a ticket or comment
already_imported| Reimport of the external resource was skipped due to a pre-existing ticket or comment for the resource
could_not_locate_parent_external_resource| The parent resource, as identified by parent_id in the request, could not be found. The unrecognized parent ID is returned in the description of the status
processing_error| An internal exception occurred while processing the resource. See `description` in the status object
halted| This resource was not processed because processing of previous resources failed

#### Code Samples

**curl**


    curl -X "POST" "https://company.zendesk.com/api/v2/any_channel/push.json" \  -H "User-Agent: Zendesk SDK for Android" \  -H "Authorization: Bearer 51b8f8c894514abab0cf4705d414ffd2760589a5dcdb9d2bc812ca0635b402ec" \  -H "Content-Type: application/json" \  -H "Accept: application/json" \  -d $'{    "instance_push_id": "d448ef2f-8f51-4fbd-a5d1-9a53d2c8a3c1",    "request_id": "my_request_123",    "external_resources": [      {        "external_id": "234",        "message": "A useful comment",        "html_message": "A <b>very</b> useful comment",        "parent_id": "123",        "created_at": "2015-01-13T08:59:26Z",        "author": {          "external_id": "456",          "name": "Fred",          "locale" : "de"        },        "display_info": [          {            "type": "9ef45ff7-4aaa-4a58-8e77-a7c74dfa51c4",            "data": { "whatever": "I want" }          }        ],        "allow_channelback": true      }    ]  }'

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/any_channel/push"	method := "POST"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "username:password"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/any_channel/push")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", Credentials.basic("your-email", "your-password"))		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'POST',  url: 'https://support.zendesk.com/api/v2/any_channel/push',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "username:password"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requests
    url = "https://support.zendesk.com/api/v2/any_channel/push"headers = {	"Content-Type": "application/json",}
    response = requests.request(	"POST",	url,	auth=('<username>', '<password>'),	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"uri = URI("https://support.zendesk.com/api/v2/any_channel/push")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")request.basic_auth "username", "password"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "results": [    {      "external_resource_id": "234",      "status": {        "code": "could_not_locate_parent_external_resource",        "description": "123"      }    }  ]}

### Validate Token

  * `POST /api/v2/any_channel/validate_token`


#### Allowed For

  * Admins


#### Request parameters

The POST request takes a JSON object parameter which contains the token to be validated.

Name| Type| Required| Comments
---|---|---|---
instance_push_id| string| yes| The ID of the account to which data will be pushed. This was passed to the integration service when the administrator set up the account
request_id| string| no| A unique identifier for the push request

#### Response format

The response body is empty.

#### Code Samples

**curl**


    curl -X "POST" "https://company.zendesk.com/api/v2/any_channel/validate_token" \  -H "User-Agent: Zendesk SDK for Android" \  -H "Authorization: Bearer 51b8f8c894514abab0cf4705d414ffd2760589a5dcdb9d2bc812ca0635b402ec" \  -H "Content-Type: application/json" \  -H "Accept: application/json" \  -d $'{    "instance_push_id": "d448ef2f-8f51-4fbd-a5d1-9a53d2c8a3c1",    "request_id": "my_request_123"  }'

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/any_channel/validate_token"	method := "POST"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "username:password"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/any_channel/validate_token")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", Credentials.basic("your-email", "your-password"))		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'POST',  url: 'https://support.zendesk.com/api/v2/any_channel/validate_token',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "username:password"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requests
    url = "https://support.zendesk.com/api/v2/any_channel/validate_token"headers = {	"Content-Type": "application/json",}
    response = requests.request(	"POST",	url,	auth=('<username>', '<password>'),	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"uri = URI("https://support.zendesk.com/api/v2/any_channel/validate_token")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")request.basic_auth "username", "password"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    null

### Report Channelback Error to Zendesk

  * `POST /api/v2/any_channel/channelback/report_error`


#### Allowed For

  * Admins


#### Request parameters

The POST request takes a JSON object parameter which contains information about the problematic [channelback](/documentation/channel_framework/understanding-the-channel-framework/channelback/).

Name| Type| Required| Comments
---|---|---|---
instance_push_id| string| yes| The ID of the account to which data will be pushed. This was passed to the integration service when the administrator set up the account
external_id| string| yes| Unique identifier of the external resource from the original channelback (string)
description| string| no| A human readable description of the error
request_id| string| no| A unique identifier for the request

#### Response format

The response does not include a response body

#### Code Samples

**curl**


    curl -X "POST" "https://company.zendesk.com/api/v2/any_channel/channelback/report_error" \  -H "User-Agent: Zendesk SDK for Android" \  -H "Authorization: Bearer 51b8f8c894514abab0cf4705d414ffd2760589a5dcdb9d2bc812ca0635b402ec" \  -H "Content-Type: application/json" \  -H "Accept: application/json" \  -d $'{    "instance_push_id": "d448ef2f-8f51-4fbd-a5d1-9a53d2c8a3c1",    "external_id": "234",    "description": "HTML content is not supported",    "request_id": "my_request_123"  }'

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/any_channel/channelback/report_error"	method := "POST"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "username:password"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/any_channel/channelback/report_error")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", Credentials.basic("your-email", "your-password"))		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'POST',  url: 'https://support.zendesk.com/api/v2/any_channel/channelback/report_error',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "username:password"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requests
    url = "https://support.zendesk.com/api/v2/any_channel/channelback/report_error"headers = {	"Content-Type": "application/json",}
    response = requests.request(	"POST",	url,	auth=('<username>', '<password>'),	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"uri = URI("https://support.zendesk.com/api/v2/any_channel/channelback/report_error")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")request.basic_auth "username", "password"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    null

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)