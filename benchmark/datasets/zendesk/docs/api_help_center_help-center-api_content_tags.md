# Content Tags

*Source: https://developer.zendesk.com/api-reference/help_center/help-center-api/content_tags/*

---

## On this page

  * [JSON format](/api-reference/help_center/help-center-api/content_tags/#json-format)
  * [Search Content Tags](/api-reference/help_center/help-center-api/content_tags/#search-content-tags)
  * [Count Content Tags](/api-reference/help_center/help-center-api/content_tags/#count-content-tags)
  * [Show Content Tag](/api-reference/help_center/help-center-api/content_tags/#show-content-tag)
  * [Create Content Tag](/api-reference/help_center/help-center-api/content_tags/#create-content-tag)
  * [Update Content Tag](/api-reference/help_center/help-center-api/content_tags/#update-content-tag)
  * [Delete Content Tag](/api-reference/help_center/help-center-api/content_tags/#delete-content-tag)
  * [Create Content Tags Job](/api-reference/help_center/help-center-api/content_tags/#create-content-tags-job)


# Content Tags

## On this page

  * [JSON format](/api-reference/help_center/help-center-api/content_tags/#json-format)
  * [Search Content Tags](/api-reference/help_center/help-center-api/content_tags/#search-content-tags)
  * [Count Content Tags](/api-reference/help_center/help-center-api/content_tags/#count-content-tags)
  * [Show Content Tag](/api-reference/help_center/help-center-api/content_tags/#show-content-tag)
  * [Create Content Tag](/api-reference/help_center/help-center-api/content_tags/#create-content-tag)
  * [Update Content Tag](/api-reference/help_center/help-center-api/content_tags/#update-content-tag)
  * [Delete Content Tag](/api-reference/help_center/help-center-api/content_tags/#delete-content-tag)
  * [Create Content Tags Job](/api-reference/help_center/help-center-api/content_tags/#create-content-tags-job)


You can assign a content tag to posts and articles to loosely group them together. For more information, see [About Content tags](https://support.zendesk.com/hc/en-us/articles/4848925672730) in Zendesk help.

### JSON format

Content Tags are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
created_at| string| false| true| When the content tag was created
id| string| false| true| Automatically assigned when the content tag is created
name| string| false| true| The name of the content tag
updated_at| string| false| true| When the content tag was last updated

#### Example


    {  "created_at": "2022-10-13T12:00:00.000Z",  "id": "01GFXGBX7YZ9ASWTCVMASTK8ZS",  "name": "feature request",  "updated_at": "2022-10-13T12:00:00.000Z"}

### Search Content Tags

  * `GET /api/v2/guide/content_tags`


Returns a paginated list of content tags.

You can filter results using the `filter[name_prefix]` query string parameter. Requests using the parameter only show content tags with names that start with a specified prefix. If a prefix is not provided or is set to an empty string, the endpoint returns all content tags.

You can use the `sort` query string parameter to sort results by `id` or `name`. To return results in descending order, add a `-` prefix to the sort value. Example: `?sort=-name`.

#### Allowed for

  * Guide managers
  * Guide agents
  * Guide end users


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
filter| object| Query| false| A group of query parameters for filtering search results
page| object| Query| false| A group of query parameters used for pagination. See [Pagination](/api-reference/help_center/help-center-api/introduction/#pagination)
sort| string| Query| false| Options for sorting the result set by field and direction. Values with no prefix stand for ASC order. Values with the `-` prefix stand for DESC order. Allowed values are "id", "-id", "name", or "-name".

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/guide/content_tags?filter[name_prefix]=feature&page[size]=1&sort=name \-g -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/content_tags?filter=&page=&sort="	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/content_tags")		.newBuilder()		.addQueryParameter("filter", "")		.addQueryParameter("page", "")		.addQueryParameter("sort", "");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/content_tags',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'filter': '',    'page': '',    'sort': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/content_tags?filter=&page=&sort="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/content_tags")uri.query = URI.encode_www_form("filter": "", "page": "", "sort": "")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "meta": {    "after_cursor": "MW",    "before_cursor": "MQ",    "has_more": true  },  "records": [    {      "created_at": "2022-10-13T12:00:00.000Z",      "id": "01GFXGBX7YZ9ASWTCVMASTK8ZS",      "name": "feature request",      "updated_at": "2022-10-13T12:00:00.000Z"    }  ]}

**403 Forbidden**


    // Status 403 Forbidden
    {  "errors": [    {      "code": "Forbidden",      "meta": {},      "status": "403",      "title": "Access to the resource is forbidden"    }  ]}

### Count Content Tags

  * `GET /api/v2/guide/content_tags/count`


Counts the number of content tags matching the filters.

#### Allowed for

  * Guide managers
  * Guide agents
  * Guide end users


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
filter| object| Query| false| A group of query parameters used to filter the available data down to a subset

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/guide/content_tags/count?filter[name_prefix]=feature \-g -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/content_tags/count?filter="	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/content_tags/count")		.newBuilder()		.addQueryParameter("filter", "");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/content_tags/count',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'filter': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/content_tags/count?filter="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/content_tags/count")uri.query = URI.encode_www_form("filter": "")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "refreshed_at": "2022-10-13T12:00:00.000Z",  "value": 42}

**403 Forbidden**


    // Status 403 Forbidden
    {  "errors": [    {      "code": "Forbidden",      "meta": {},      "status": "403",      "title": "Access to the resource is forbidden"    }  ]}

### Show Content Tag

  * `GET /api/v2/guide/content_tags/{id}`


Shows information about a single content tag.

#### Allowed for

  * Guide managers
  * Guide agents
  * Guide end users


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
id| string| Path| true| The content tag id

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/guide/content_tags/{id} \-v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/content_tags/01GFYBENPDGN1R6NAA4WRDNVFR"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/content_tags/01GFYBENPDGN1R6NAA4WRDNVFR")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/content_tags/01GFYBENPDGN1R6NAA4WRDNVFR',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/content_tags/01GFYBENPDGN1R6NAA4WRDNVFR"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/content_tags/01GFYBENPDGN1R6NAA4WRDNVFR")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "content_tag": {    "created_at": "2022-10-13T12:00:00.000Z",    "id": "01GFXGBX7YZ9ASWTCVMASTK8ZS",    "name": "feature request",    "updated_at": "2022-10-13T12:00:00.000Z"  }}

**403 Forbidden**


    // Status 403 Forbidden
    {  "errors": [    {      "code": "Forbidden",      "meta": {},      "status": "403",      "title": "Access to the resource is forbidden"    }  ]}

### Create Content Tag

  * `POST /api/v2/guide/content_tags`


#### Allowed for

  * Guide managers
  * Guide agents


#### Example body


    {  "content_tag": {    "name": "feature request"  }}

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/guide/content_tags \-d '{"content_tag": {"name": "feature request"}}' \-v -u {email_address}/token:{api_token} \-X POST -H "Content-Type: application/json"

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/content_tags"	method := "POST"	payload := strings.NewReader(`{  "content_tag": {    "name": "feature request"  }}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/content_tags")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"content_tag\": {    \"name\": \"feature request\"  }}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "content_tag": {    "name": "feature request"  }});
    var config = {  method: 'POST',  url: 'https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/content_tags',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/content_tags"
    payload = json.loads("""{  "content_tag": {    "name": "feature request"  }}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/content_tags")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")request.body = %q({  "content_tag": {    "name": "feature request"  }})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**201 Created**


    // Status 201 Created
    {  "content_tag": {    "created_at": "2022-10-13T12:00:00.000Z",    "id": "01GFXGBX7YZ9ASWTCVMASTK8ZS",    "name": "feature request",    "updated_at": "2022-10-13T12:00:00.000Z"  }}

**400 Bad Request**


    // Status 400 Bad Request
    {  "errors": [    {      "code": "BadRequest",      "meta": {},      "status": "400",      "title": "Invalid property"    }  ]}

**403 Forbidden**


    // Status 403 Forbidden
    {  "errors": [    {      "code": "Forbidden",      "meta": {},      "status": "403",      "title": "Access to the resource is forbidden"    }  ]}

**422 Unprocessable Entity**


    // Status 422 Unprocessable Entity
    {  "errors": [    {      "code": "UnprocessibleEntity",      "meta": {},      "status": "422",      "title": "The request could not be processed"    }  ]}

### Update Content Tag

  * `PUT /api/v2/guide/content_tags/{id}`


#### Allowed for

  * Guide managers


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
id| string| Path| true| The content tag id

#### Example body


    {  "content_tag": {    "name": "need help"  }}

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/guide/content_tags/{id} \-d '{"content_tag": {"name": "need help"}}' \-v -u {email_address}/token:{api_token} \-X PUT -H "Content-Type: application/json"

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/content_tags/01GFYBENPDGN1R6NAA4WRDNVFR"	method := "PUT"	payload := strings.NewReader(`{  "content_tag": {    "name": "need help"  }}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/content_tags/01GFYBENPDGN1R6NAA4WRDNVFR")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"content_tag\": {    \"name\": \"need help\"  }}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "content_tag": {    "name": "need help"  }});
    var config = {  method: 'PUT',  url: 'https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/content_tags/01GFYBENPDGN1R6NAA4WRDNVFR',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/content_tags/01GFYBENPDGN1R6NAA4WRDNVFR"
    payload = json.loads("""{  "content_tag": {    "name": "need help"  }}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/content_tags/01GFYBENPDGN1R6NAA4WRDNVFR")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")request.body = %q({  "content_tag": {    "name": "need help"  }})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "content_tag": {    "created_at": "2022-10-13T12:00:00.000Z",    "id": "01GFXGBX7YZ9ASWTCVMASTK8ZS",    "name": "need help",    "updated_at": "2022-10-13T12:00:00.000Z"  }}

**400 Bad Request**


    // Status 400 Bad Request
    {  "errors": [    {      "code": "BadRequest",      "meta": {},      "status": "400",      "title": "Invalid property"    }  ]}

**403 Forbidden**


    // Status 403 Forbidden
    {  "errors": [    {      "code": "Forbidden",      "meta": {},      "status": "403",      "title": "Access to the resource is forbidden"    }  ]}

**404 Not Found**


    // Status 404 Not Found
    {  "errors": [    {      "code": "NotFound",      "meta": {},      "status": "404",      "title": "The Resource could not be found"    }  ]}

**422 Unprocessable Entity**


    // Status 422 Unprocessable Entity
    {  "errors": [    {      "code": "UnprocessibleEntity",      "meta": {},      "status": "422",      "title": "The request could not be processed"    }  ]}

### Delete Content Tag

  * `DELETE /api/v2/guide/content_tags/{id}`


#### Allowed for

  * Guide managers


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
id| string| Path| true| The content tag id

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/guide/content_tags/{id} \-v -u {email_address}/token:{api_token} \-X DELETE"

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/content_tags/01GFYBENPDGN1R6NAA4WRDNVFR"	method := "DELETE"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/content_tags/01GFYBENPDGN1R6NAA4WRDNVFR")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("DELETE", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'DELETE',  url: 'https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/content_tags/01GFYBENPDGN1R6NAA4WRDNVFR',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/content_tags/01GFYBENPDGN1R6NAA4WRDNVFR"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"DELETE",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/content_tags/01GFYBENPDGN1R6NAA4WRDNVFR")request = Net::HTTP::Delete.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**204 No Content**


    // Status 204 No Content
    null

**400 Bad Request**


    // Status 400 Bad Request
    {  "errors": [    {      "code": "BadRequest",      "meta": {},      "status": "400",      "title": "Invalid property"    }  ]}

**403 Forbidden**


    // Status 403 Forbidden
    {  "errors": [    {      "code": "Forbidden",      "meta": {},      "status": "403",      "title": "Access to the resource is forbidden"    }  ]}

### Create Content Tags Job

  * `POST /api/v2/guide/content_tags/jobs`


Creates a job that performs one of the supported actions as a batch operation.

The `job.items` request body parameter is an array of content tag IDs. The `job.attributes.target_content_tag_id` request body parameter is only required for the `merge` action.

#### Supported actions

  * `delete`
  * `merge`


#### Allowed for

  * Guide managers


#### Example body


    {  "job": {    "action": "delete",    "items": [      "01GFXGBX7YZ9ASWTCVMASTK8ZS",      "01GFXH8B0P230ZNTNKF62MXQ5T"    ]  }}

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/guide/content_tags/jobs \-d '{"job": {"action": "delete", "items": ["01GFXGBX7YZ9ASWTCVMASTK8ZS", "01GFXH8B0P230ZNTNKF62MXQ5T"]}}' \-v -u {email_address}/token:{api_token} \-X POST -H "Content-Type: application/json"

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/content_tags/jobs"	method := "POST"	payload := strings.NewReader(`{  "job": {    "action": "delete",    "items": [      "01GFXGBX7YZ9ASWTCVMASTK8ZS",      "01GFXH8B0P230ZNTNKF62MXQ5T"    ]  }}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/content_tags/jobs")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"job\": {    \"action\": \"delete\",    \"items\": [      \"01GFXGBX7YZ9ASWTCVMASTK8ZS\",      \"01GFXH8B0P230ZNTNKF62MXQ5T\"    ]  }}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "job": {    "action": "delete",    "items": [      "01GFXGBX7YZ9ASWTCVMASTK8ZS",      "01GFXH8B0P230ZNTNKF62MXQ5T"    ]  }});
    var config = {  method: 'POST',  url: 'https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/content_tags/jobs',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/content_tags/jobs"
    payload = json.loads("""{  "job": {    "action": "delete",    "items": [      "01GFXGBX7YZ9ASWTCVMASTK8ZS",      "01GFXH8B0P230ZNTNKF62MXQ5T"    ]  }}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/content_tags/jobs")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")request.body = %q({  "job": {    "action": "delete",    "items": [      "01GFXGBX7YZ9ASWTCVMASTK8ZS",      "01GFXH8B0P230ZNTNKF62MXQ5T"    ]  }})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**201 Created**


    // Status 201 Created
    {  "job": {    "results": [      "01GFXGBX7YZ9ASWTCVMASTK8ZS",      "01GFXH8B0P230ZNTNKF62MXQ5T"    ],    "status": "completed"  }}

**400 Bad Request**


    // Status 400 Bad Request
    {  "errors": [    {      "code": "BadRequest",      "meta": {},      "status": "400",      "title": "Invalid property"    }  ]}

**403 Forbidden**


    // Status 403 Forbidden
    {  "errors": [    {      "code": "Forbidden",      "meta": {},      "status": "403",      "title": "Access to the resource is forbidden"    }  ]}

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)