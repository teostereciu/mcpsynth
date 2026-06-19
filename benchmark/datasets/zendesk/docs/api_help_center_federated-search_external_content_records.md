# External Content Records

*Source: https://developer.zendesk.com/api-reference/help_center/federated-search/external_content_records/*

---

## On this page

  * [JSON format](/api-reference/help_center/federated-search/external_content_records/#json-format)
  * [List External Content Records](/api-reference/help_center/federated-search/external_content_records/#list-external-content-records)
  * [Show External Content Record](/api-reference/help_center/federated-search/external_content_records/#show-external-content-record)
  * [Create External Content Record](/api-reference/help_center/federated-search/external_content_records/#create-external-content-record)
  * [Update External Content Record](/api-reference/help_center/federated-search/external_content_records/#update-external-content-record)
  * [Delete External Content Record](/api-reference/help_center/federated-search/external_content_records/#delete-external-content-record)


# External Content Records

## On this page

  * [JSON format](/api-reference/help_center/federated-search/external_content_records/#json-format)
  * [List External Content Records](/api-reference/help_center/federated-search/external_content_records/#list-external-content-records)
  * [Show External Content Record](/api-reference/help_center/federated-search/external_content_records/#show-external-content-record)
  * [Create External Content Record](/api-reference/help_center/federated-search/external_content_records/#create-external-content-record)
  * [Update External Content Record](/api-reference/help_center/federated-search/external_content_records/#update-external-content-record)
  * [Delete External Content Record](/api-reference/help_center/federated-search/external_content_records/#delete-external-content-record)


Use this API to ingest external content records for search. The help center search engine indexes and ranks the content. When an end user clicks an external content search result, they're taken to the URL of the external content record.

For more information, see [Introduction](/api-reference/help_center/federated-search/introduction/) and [About Zendesk Federated Search](https://support.zendesk.com/hc/en-us/articles/4408830243482) in Zendesk help.

### JSON format

Records are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
body| string| false| true| The body of the record. The maximum length is 10,000 characters. The body is truncated if it exceeds the limit
created_at| string| false| false| ISO-8601 compliant date-time reflecting the time the event was created. If not set, the API sets the value when it receives the event
external_id| string| false| true| A string that uniquely identifies the record in your system
id| string| true| false| Universally Unique Lexicographically Sortable Identifier. See <https://github.com/ulid/spec>[](https://github.com/ulid/spec)
locale| string| false| true| Record locale. Must match a locale already enabled in your help center to be returned in search. See [Zendesk language support by product](https://support.zendesk.com/hc/en-us/articles/4408821324826) in Zendesk help
source_id| string| false| true| Universally Unique Lexicographically Sortable Identifier. See <https://github.com/ulid/spec>[](https://github.com/ulid/spec)
title| string| false| true| The title of the record
type_id| string| false| true| Universally Unique Lexicographically Sortable Identifier. See <https://github.com/ulid/spec>[](https://github.com/ulid/spec)
updated_at| string| false| false| ISO-8601 compliant date-time reflecting the time the event was last updated
url| string| false| true| An accessible URL for the record in your system
user_segment_id| string| false| false| The id of the [user segment](/api-reference/help_center/help-center-api/user_segments/) that can view this record. To make the record visible to all users, omit setting this property or set it to null or -1

### List External Content Records

  * `GET /api/v2/guide/external_content/records`


Lists external content records.

#### Allowed for

  * Help Center managers


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
page| object| Query| false| Paginate query

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/guide/external_content/records \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/guide/external_content/records?page="	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/guide/external_content/records")		.newBuilder()		.addQueryParameter("page", "");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/guide/external_content/records',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'page': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/guide/external_content/records?page="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/guide/external_content/records")uri.query = URI.encode_www_form("page": "")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "meta": {    "after_cursor": "MW",    "before_cursor": "MQ",    "has_more": true  },  "records": [    {      "body": "We want to hear what you have to say about external content search, because ultimately we're building it for you. Below, you can find some guidelines on the best ways to let us know what you think. Right here -- this forum is the best place. With this format, we can respond to questions or comments so that everyone can see and benefit. We also encourage you to make it as social and collaborative as possible, so jump in if you have an idea that might help someone else.",      "created_at": "2020-07-08T12:27:26Z",      "external_id": "360046759835",      "id": "01EC05A5T1J4ZSDJX4Q8JGFRHP",      "locale": "en-us",      "source": {        "id": "01E77R4513SKX3AE8H20Q0KJ1K",        "name": "My Library"      },      "title": "How to leave feedback for Federated Help Center search",      "type": {        "id": "01EBDWWC98ZF7DK9YQF3DK9Y77",        "name": "Blog"      },      "updated_at": "2020-07-08T12:27:26Z",      "url": "https://support.zendesk.com/hc/en-us/community/posts/360046759834-How-to-leave-feedback-for-Federated-Help-Center-search",      "user_segment_id": "-1"    }  ]}

### Show External Content Record

  * `GET /api/v2/guide/external_content/records/{id}`


Gets the specified external content record.

#### Allowed for

  * Help Center managers


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
id| string| Path| true| ULID for the object

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/guide/external_content/records/{id} \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/guide/external_content/records/01E7GZVZHBWYD50V00XDMYCMYP"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/guide/external_content/records/01E7GZVZHBWYD50V00XDMYCMYP")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/guide/external_content/records/01E7GZVZHBWYD50V00XDMYCMYP',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/guide/external_content/records/01E7GZVZHBWYD50V00XDMYCMYP"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/guide/external_content/records/01E7GZVZHBWYD50V00XDMYCMYP")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "record": {    "body": "We want to hear what you have to say about external content search, because ultimately we're building it for you. Below, you can find some guidelines on the best ways to let us know what you think. Right here -- this forum is the best place. With this format, we can respond to questions or comments so that everyone can see and benefit. We also encourage you to make it as social and collaborative as possible, so jump in if you have an idea that might help someone else.",    "created_at": "2020-07-08T12:27:26Z",    "external_id": "360046759835",    "id": "01EC05A5T1J4ZSDJX4Q8JGFRHP",    "locale": "en-us",    "source": {      "id": "01E77R4513SKX3AE8H20Q0KJ1K",      "name": "My Library"    },    "title": "How to leave feedback for Federated Help Center search",    "type": {      "id": "01EBDWWC98ZF7DK9YQF3DK9Y77",      "name": "Blog"    },    "updated_at": "2020-07-08T12:27:26Z",    "url": "https://support.zendesk.com/hc/en-us/community/posts/360046759834-How-to-leave-feedback-for-Federated-Help-Center-search",    "user_segment_id": "-1"  }}

### Create External Content Record

  * `POST /api/v2/guide/external_content/records`


Creates an external content record. Specify a `type_id` and `source_id` for this request. You can retrieve the ids using [List External Content Types](/api-reference/help_center/federated-search/external_content_types/#list-external-content-types) and [List External Content Sources](/api-reference/help_center/federated-search/external_content_sources/#list-external-content-sources).

#### Allowed for

  * Help Center managers


#### Example body


    {  "record": {    "body": "We want to hear what you have to say about external content search, because ultimately we're building it for you. Below, you can find some guidelines on the best ways to let us know what you think. Right here -- this forum is the best place. With this format, we can respond to questions or comments so that everyone can see and benefit. We also encourage you to make it as social and collaborative as possible, so jump in if you have an idea that might help someone else.",    "external_id": "360046759835",    "locale": "en-us",    "source_id": "01E77R4513SKX3AE8H20Q0KJ1K",    "title": "How to leave feedback for Federated Help Center search",    "type_id": "01EBDWWC98ZF7DK9YQF3DK9Y77",    "url": "https://support.zendesk.com/hc/en-us/community/posts/360046759834-How-to-leave-feedback-for-Federated-Help-Center-search",    "user_segment_id": "-1"  }}

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/guide/external_content/records \  -d '{ "record": { "title": "Mansfield Park", "url": "http://www.publicbookshelf.com/regency/mansfield-park/mansfieldpark8", "locale": "en-uk", "body": "Before his return Mrs. Grant and Miss Crawford came in.", "external_id": "mansfieldpark8", "user_segment_id": null, "type_id": "01E77R7P0S8QKHPV07VKXH65S3", "source_id": "01E7GZVZHBWYD50V00XDMYCMYP" }}' \  -H "Content-Type: application/json" \  -v -u {email_address}/token:{api_token} -X POST

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://support.zendesk.com/api/v2/guide/external_content/records"	method := "POST"	payload := strings.NewReader(`{  "record": {    "body": "We want to hear what you have to say about external content search, because ultimately we're building it for you. Below, you can find some guidelines on the best ways to let us know what you think. Right here -- this forum is the best place. With this format, we can respond to questions or comments so that everyone can see and benefit. We also encourage you to make it as social and collaborative as possible, so jump in if you have an idea that might help someone else.",    "external_id": "360046759835",    "locale": "en-us",    "source_id": "01E77R4513SKX3AE8H20Q0KJ1K",    "title": "How to leave feedback for Federated Help Center search",    "type_id": "01EBDWWC98ZF7DK9YQF3DK9Y77",    "url": "https://support.zendesk.com/hc/en-us/community/posts/360046759834-How-to-leave-feedback-for-Federated-Help-Center-search",    "user_segment_id": "-1"  }}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/guide/external_content/records")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"record\": {    \"body\": \"We want to hear what you have to say about external content search, because ultimately we're building it for you. Below, you can find some guidelines on the best ways to let us know what you think. Right here -- this forum is the best place. With this format, we can respond to questions or comments so that everyone can see and benefit. We also encourage you to make it as social and collaborative as possible, so jump in if you have an idea that might help someone else.\",    \"external_id\": \"360046759835\",    \"locale\": \"en-us\",    \"source_id\": \"01E77R4513SKX3AE8H20Q0KJ1K\",    \"title\": \"How to leave feedback for Federated Help Center search\",    \"type_id\": \"01EBDWWC98ZF7DK9YQF3DK9Y77\",    \"url\": \"https://support.zendesk.com/hc/en-us/community/posts/360046759834-How-to-leave-feedback-for-Federated-Help-Center-search\",    \"user_segment_id\": \"-1\"  }}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "record": {    "body": "We want to hear what you have to say about external content search, because ultimately we're building it for you. Below, you can find some guidelines on the best ways to let us know what you think. Right here -- this forum is the best place. With this format, we can respond to questions or comments so that everyone can see and benefit. We also encourage you to make it as social and collaborative as possible, so jump in if you have an idea that might help someone else.",    "external_id": "360046759835",    "locale": "en-us",    "source_id": "01E77R4513SKX3AE8H20Q0KJ1K",    "title": "How to leave feedback for Federated Help Center search",    "type_id": "01EBDWWC98ZF7DK9YQF3DK9Y77",    "url": "https://support.zendesk.com/hc/en-us/community/posts/360046759834-How-to-leave-feedback-for-Federated-Help-Center-search",    "user_segment_id": "-1"  }});
    var config = {  method: 'POST',  url: 'https://support.zendesk.com/api/v2/guide/external_content/records',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/guide/external_content/records"
    payload = json.loads("""{  "record": {    "body": "We want to hear what you have to say about external content search, because ultimately we're building it for you. Below, you can find some guidelines on the best ways to let us know what you think. Right here -- this forum is the best place. With this format, we can respond to questions or comments so that everyone can see and benefit. We also encourage you to make it as social and collaborative as possible, so jump in if you have an idea that might help someone else.",    "external_id": "360046759835",    "locale": "en-us",    "source_id": "01E77R4513SKX3AE8H20Q0KJ1K",    "title": "How to leave feedback for Federated Help Center search",    "type_id": "01EBDWWC98ZF7DK9YQF3DK9Y77",    "url": "https://support.zendesk.com/hc/en-us/community/posts/360046759834-How-to-leave-feedback-for-Federated-Help-Center-search",    "user_segment_id": "-1"  }}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/guide/external_content/records")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")request.body = %q({  "record": {    "body": "We want to hear what you have to say about external content search, because ultimately we're building it for you. Below, you can find some guidelines on the best ways to let us know what you think. Right here -- this forum is the best place. With this format, we can respond to questions or comments so that everyone can see and benefit. We also encourage you to make it as social and collaborative as possible, so jump in if you have an idea that might help someone else.",    "external_id": "360046759835",    "locale": "en-us",    "source_id": "01E77R4513SKX3AE8H20Q0KJ1K",    "title": "How to leave feedback for Federated Help Center search",    "type_id": "01EBDWWC98ZF7DK9YQF3DK9Y77",    "url": "https://support.zendesk.com/hc/en-us/community/posts/360046759834-How-to-leave-feedback-for-Federated-Help-Center-search",    "user_segment_id": "-1"  }})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**201 Created**


    // Status 201 Created
    {  "record": {    "body": "We want to hear what you have to say about external content search, because ultimately we're building it for you. Below, you can find some guidelines on the best ways to let us know what you think. Right here -- this forum is the best place. With this format, we can respond to questions or comments so that everyone can see and benefit. We also encourage you to make it as social and collaborative as possible, so jump in if you have an idea that might help someone else.",    "created_at": "2020-07-08T12:27:26Z",    "external_id": "360046759835",    "id": "01EC05A5T1J4ZSDJX4Q8JGFRHP",    "locale": "en-us",    "source": {      "id": "01E77R4513SKX3AE8H20Q0KJ1K",      "name": "My Library"    },    "title": "How to leave feedback for Federated Help Center search",    "type": {      "id": "01EBDWWC98ZF7DK9YQF3DK9Y77",      "name": "Blog"    },    "updated_at": "2020-07-08T12:27:26Z",    "url": "https://support.zendesk.com/hc/en-us/community/posts/360046759834-How-to-leave-feedback-for-Federated-Help-Center-search",    "user_segment_id": "-1"  }}

**401 Unauthorized**


    // Status 401 Unauthorized
    {  "errors": [    {      "code": "Unauthorized",      "status": 401,      "title": "Feature not enabled"    }  ]}

**422 Unprocessable Entity**


    // Status 422 Unprocessable Entity
    {  "errors": [    {      "code": "Invalid",      "status": 422,      "title": "Validation failed: External ID has already been taken"    }  ]}

### Update External Content Record

  * `PUT /api/v2/guide/external_content/records/{id}`


Updates the specified record with the request body.

#### Allowed for

  * Help Center managers


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
id| string| Path| true| ULID for the object

#### Example body


    {  "record": {    "body": "We want to hear what you have to say about external content search, because ultimately we're building it for you. Below, you can find some guidelines on the best ways to let us know what you think. Right here -- this forum is the best place. With this format, we can respond to questions or comments so that everyone can see and benefit. We also encourage you to make it as social and collaborative as possible, so jump in if you have an idea that might help someone else.",    "external_id": "360046759835",    "locale": "en-us",    "source_id": "01E77R4513SKX3AE8H20Q0KJ1K",    "title": "How to leave feedback for Federated Help Center search",    "type_id": "01EBDWWC98ZF7DK9YQF3DK9Y77",    "url": "https://support.zendesk.com/hc/en-us/community/posts/360046759834-How-to-leave-feedback-for-Federated-Help-Center-search",    "user_segment_id": "-1"  }}

#### Code Samples

**curl**


    curl "https://{subdomain}.zendesk.com/api/v2/guide/external_content/records/{id}"  \  -d '{ "record": { "title": "Mansfield Park", "url": "http://www.publicbookshelf.com/regency/mansfield-park/mansfieldpark8", "locale": "en-uk", "body": "Before his return Mrs. Grant and Miss Crawford came in.", "external_id": "mansfieldpark8", "user_segment_id": null, "type_id": "01E77R7P0S8QKHPV07VKXH65S3", "source_id": "01E7GZVZHBWYD50V00XDMYCMYP" }}' \  -H "Content-Type: application/json" \  -v -u {email_address}/token:{api_token} -X PUT

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://support.zendesk.com/api/v2/guide/external_content/records/01E7GZVZHBWYD50V00XDMYCMYP"	method := "PUT"	payload := strings.NewReader(`{  "record": {    "body": "We want to hear what you have to say about external content search, because ultimately we're building it for you. Below, you can find some guidelines on the best ways to let us know what you think. Right here -- this forum is the best place. With this format, we can respond to questions or comments so that everyone can see and benefit. We also encourage you to make it as social and collaborative as possible, so jump in if you have an idea that might help someone else.",    "external_id": "360046759835",    "locale": "en-us",    "source_id": "01E77R4513SKX3AE8H20Q0KJ1K",    "title": "How to leave feedback for Federated Help Center search",    "type_id": "01EBDWWC98ZF7DK9YQF3DK9Y77",    "url": "https://support.zendesk.com/hc/en-us/community/posts/360046759834-How-to-leave-feedback-for-Federated-Help-Center-search",    "user_segment_id": "-1"  }}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/guide/external_content/records/01E7GZVZHBWYD50V00XDMYCMYP")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"record\": {    \"body\": \"We want to hear what you have to say about external content search, because ultimately we're building it for you. Below, you can find some guidelines on the best ways to let us know what you think. Right here -- this forum is the best place. With this format, we can respond to questions or comments so that everyone can see and benefit. We also encourage you to make it as social and collaborative as possible, so jump in if you have an idea that might help someone else.\",    \"external_id\": \"360046759835\",    \"locale\": \"en-us\",    \"source_id\": \"01E77R4513SKX3AE8H20Q0KJ1K\",    \"title\": \"How to leave feedback for Federated Help Center search\",    \"type_id\": \"01EBDWWC98ZF7DK9YQF3DK9Y77\",    \"url\": \"https://support.zendesk.com/hc/en-us/community/posts/360046759834-How-to-leave-feedback-for-Federated-Help-Center-search\",    \"user_segment_id\": \"-1\"  }}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "record": {    "body": "We want to hear what you have to say about external content search, because ultimately we're building it for you. Below, you can find some guidelines on the best ways to let us know what you think. Right here -- this forum is the best place. With this format, we can respond to questions or comments so that everyone can see and benefit. We also encourage you to make it as social and collaborative as possible, so jump in if you have an idea that might help someone else.",    "external_id": "360046759835",    "locale": "en-us",    "source_id": "01E77R4513SKX3AE8H20Q0KJ1K",    "title": "How to leave feedback for Federated Help Center search",    "type_id": "01EBDWWC98ZF7DK9YQF3DK9Y77",    "url": "https://support.zendesk.com/hc/en-us/community/posts/360046759834-How-to-leave-feedback-for-Federated-Help-Center-search",    "user_segment_id": "-1"  }});
    var config = {  method: 'PUT',  url: 'https://support.zendesk.com/api/v2/guide/external_content/records/01E7GZVZHBWYD50V00XDMYCMYP',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/guide/external_content/records/01E7GZVZHBWYD50V00XDMYCMYP"
    payload = json.loads("""{  "record": {    "body": "We want to hear what you have to say about external content search, because ultimately we're building it for you. Below, you can find some guidelines on the best ways to let us know what you think. Right here -- this forum is the best place. With this format, we can respond to questions or comments so that everyone can see and benefit. We also encourage you to make it as social and collaborative as possible, so jump in if you have an idea that might help someone else.",    "external_id": "360046759835",    "locale": "en-us",    "source_id": "01E77R4513SKX3AE8H20Q0KJ1K",    "title": "How to leave feedback for Federated Help Center search",    "type_id": "01EBDWWC98ZF7DK9YQF3DK9Y77",    "url": "https://support.zendesk.com/hc/en-us/community/posts/360046759834-How-to-leave-feedback-for-Federated-Help-Center-search",    "user_segment_id": "-1"  }}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/guide/external_content/records/01E7GZVZHBWYD50V00XDMYCMYP")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")request.body = %q({  "record": {    "body": "We want to hear what you have to say about external content search, because ultimately we're building it for you. Below, you can find some guidelines on the best ways to let us know what you think. Right here -- this forum is the best place. With this format, we can respond to questions or comments so that everyone can see and benefit. We also encourage you to make it as social and collaborative as possible, so jump in if you have an idea that might help someone else.",    "external_id": "360046759835",    "locale": "en-us",    "source_id": "01E77R4513SKX3AE8H20Q0KJ1K",    "title": "How to leave feedback for Federated Help Center search",    "type_id": "01EBDWWC98ZF7DK9YQF3DK9Y77",    "url": "https://support.zendesk.com/hc/en-us/community/posts/360046759834-How-to-leave-feedback-for-Federated-Help-Center-search",    "user_segment_id": "-1"  }})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "record": {    "body": "We want to hear what you have to say about external content search, because ultimately we're building it for you. Below, you can find some guidelines on the best ways to let us know what you think. Right here -- this forum is the best place. With this format, we can respond to questions or comments so that everyone can see and benefit. We also encourage you to make it as social and collaborative as possible, so jump in if you have an idea that might help someone else.",    "created_at": "2020-07-08T12:27:26Z",    "external_id": "360046759835",    "id": "01EC05A5T1J4ZSDJX4Q8JGFRHP",    "locale": "en-us",    "source": {      "id": "01E77R4513SKX3AE8H20Q0KJ1K",      "name": "My Library"    },    "title": "How to leave feedback for Federated Help Center search",    "type": {      "id": "01EBDWWC98ZF7DK9YQF3DK9Y77",      "name": "Blog"    },    "updated_at": "2020-07-08T12:27:26Z",    "url": "https://support.zendesk.com/hc/en-us/community/posts/360046759834-How-to-leave-feedback-for-Federated-Help-Center-search",    "user_segment_id": "-1"  }}

### Delete External Content Record

  * `DELETE /api/v2/guide/external_content/records/{id}`


Deletes the specified record.

#### Allowed for

  * Help Center managers


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
id| string| Path| true| ULID for the object

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/guide/external_content/records/{id} \  -v -u {email_address}/token:{api_token} -X DELETE

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/guide/external_content/records/01E7GZVZHBWYD50V00XDMYCMYP"	method := "DELETE"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/guide/external_content/records/01E7GZVZHBWYD50V00XDMYCMYP")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("DELETE", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'DELETE',  url: 'https://support.zendesk.com/api/v2/guide/external_content/records/01E7GZVZHBWYD50V00XDMYCMYP',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/guide/external_content/records/01E7GZVZHBWYD50V00XDMYCMYP"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"DELETE",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/guide/external_content/records/01E7GZVZHBWYD50V00XDMYCMYP")request = Net::HTTP::Delete.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**204 No Content**


    // Status 204 No Content
    null

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)