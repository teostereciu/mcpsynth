# External Content Types

*Source: https://developer.zendesk.com/api-reference/help_center/federated-search/external_content_types/*

---

## On this page

  * [JSON format](/api-reference/help_center/federated-search/external_content_types/#json-format)
  * [List External Content Types](/api-reference/help_center/federated-search/external_content_types/#list-external-content-types)
  * [Show External Content Type](/api-reference/help_center/federated-search/external_content_types/#show-external-content-type)
  * [Create External Content Type](/api-reference/help_center/federated-search/external_content_types/#create-external-content-type)
  * [Update External Content Type](/api-reference/help_center/federated-search/external_content_types/#update-external-content-type)
  * [Delete External Content Type](/api-reference/help_center/federated-search/external_content_types/#delete-external-content-type)


# External Content Types

## On this page

  * [JSON format](/api-reference/help_center/federated-search/external_content_types/#json-format)
  * [List External Content Types](/api-reference/help_center/federated-search/external_content_types/#list-external-content-types)
  * [Show External Content Type](/api-reference/help_center/federated-search/external_content_types/#show-external-content-type)
  * [Create External Content Type](/api-reference/help_center/federated-search/external_content_types/#create-external-content-type)
  * [Update External Content Type](/api-reference/help_center/federated-search/external_content_types/#update-external-content-type)
  * [Delete External Content Type](/api-reference/help_center/federated-search/external_content_types/#delete-external-content-type)


Use this API to define and manage external content types. A type refers to a kind of content, such as blog posts, tech notes, or bug reports. Because end users can filter help center search results by content type, use descriptive names to help them understand and navigate your content.

For more information on federated search, see [Introduction](/api-reference/help_center/federated-search/introduction/) and [About Zendesk Federated Search](https://support.zendesk.com/hc/en-us/articles/4408830243482) in Zendesk help.

### JSON format

Types are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
created_at| string| false| false| ISO-8601 compliant date-time reflecting the time the event was created. If not set, the API sets the value when it receives the event
id| string| true| false| Universally Unique Lexicographically Sortable Identifier. See <https://github.com/ulid/spec>[](https://github.com/ulid/spec)
name| string| false| true| The name of the type to be displayed in the help center
updated_at| string| false| false| ISO-8601 compliant date-time reflecting the time the event was last updated

### List External Content Types

  * `GET /api/v2/guide/external_content/types`


Returns a list of the external content types created for this account.

#### Allowed for

  * Help Center managers


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
page| object| Query| false| Paginate query

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/guide/external_content/types \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/guide/external_content/types?page="	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/guide/external_content/types")		.newBuilder()		.addQueryParameter("page", "");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/guide/external_content/types',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'page': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/guide/external_content/types?page="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/guide/external_content/types")uri.query = URI.encode_www_form("page": "")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "meta": {    "after_cursor": "MG",    "before_cursor": "MQ",    "has_more": true  },  "types": [    {      "created_at": "2020-05-01T09:12:20Z",      "id": "01EBDWWC98ZF7DK9YQF3DK9Y77",      "name": "Book",      "updated_at": "2020-05-26T09:11:30Z"    }  ]}

### Show External Content Type

  * `GET /api/v2/guide/external_content/types/{id}`


Returns the specified content type.

#### Allowed for

  * Help Center managers


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
id| string| Path| true| ULID for the object

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/guide/external_content/types/{id} \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/guide/external_content/types/01E7GZVZHBWYD50V00XDMYCMYP"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/guide/external_content/types/01E7GZVZHBWYD50V00XDMYCMYP")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/guide/external_content/types/01E7GZVZHBWYD50V00XDMYCMYP',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/guide/external_content/types/01E7GZVZHBWYD50V00XDMYCMYP"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/guide/external_content/types/01E7GZVZHBWYD50V00XDMYCMYP")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "type": {    "created_at": "2020-05-01T09:12:20Z",    "id": "01E7H2DC2EDTK45NZTFGFAAA1N",    "name": "Book",    "updated_at": "2020-05-26T09:11:30Z"  }}

### Create External Content Type

  * `POST /api/v2/guide/external_content/types`


Creates an external content type.

#### Allowed for

  * Help Center managers


#### Example body


    {  "type": {    "name": "Book"  }}

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/guide/external_content/types \  -d '{"type": { "name": "Book" }}' \  -H "Content-Type: application/json" \  -v -u {email_address}/token:{api_token} -X POST

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://support.zendesk.com/api/v2/guide/external_content/types"	method := "POST"	payload := strings.NewReader(`{  "type": {    "name": "Book"  }}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/guide/external_content/types")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"type\": {    \"name\": \"Book\"  }}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "type": {    "name": "Book"  }});
    var config = {  method: 'POST',  url: 'https://support.zendesk.com/api/v2/guide/external_content/types',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/guide/external_content/types"
    payload = json.loads("""{  "type": {    "name": "Book"  }}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/guide/external_content/types")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")request.body = %q({  "type": {    "name": "Book"  }})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**201 Created**


    // Status 201 Created
    {  "type": {    "created_at": "2020-05-01T09:12:20Z",    "id": "01E7H2DC2EDTK45NZTFGFAAA1N",    "name": "Book",    "updated_at": "2020-05-26T09:11:30Z"  }}

### Update External Content Type

  * `PUT /api/v2/guide/external_content/types/{id}`


Updates the specified external content type with the request body.

#### Allowed for

  * Help Center managers


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
id| string| Path| true| ULID for the object

#### Example body


    {  "type": {    "name": "Book"  }}

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/guide/external_content/types/{id} \  -d '{"type": { "name": "Book" }}' \  -H "Content-Type: application/json" \  -v -u {email_address}/token:{api_token} -X PUT

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://support.zendesk.com/api/v2/guide/external_content/types/01E7GZVZHBWYD50V00XDMYCMYP"	method := "PUT"	payload := strings.NewReader(`{  "type": {    "name": "Book"  }}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/guide/external_content/types/01E7GZVZHBWYD50V00XDMYCMYP")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"type\": {    \"name\": \"Book\"  }}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "type": {    "name": "Book"  }});
    var config = {  method: 'PUT',  url: 'https://support.zendesk.com/api/v2/guide/external_content/types/01E7GZVZHBWYD50V00XDMYCMYP',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/guide/external_content/types/01E7GZVZHBWYD50V00XDMYCMYP"
    payload = json.loads("""{  "type": {    "name": "Book"  }}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/guide/external_content/types/01E7GZVZHBWYD50V00XDMYCMYP")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")request.body = %q({  "type": {    "name": "Book"  }})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "type": {    "created_at": "2020-05-01T09:12:20Z",    "id": "01E7H2DC2EDTK45NZTFGFAAA1N",    "name": "Book",    "updated_at": "2020-05-26T09:11:30Z"  }}

### Delete External Content Type

  * `DELETE /api/v2/guide/external_content/types/{id}`


Deletes the specified external content type. Will also delete any crawler or record associated with this type.

#### Allowed for

  * Help Center managers


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
id| string| Path| true| ULID for the object

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/guide/external_content/types/{id} \  -v -u {email_address}/token:{api_token} -X DELETE

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/guide/external_content/types/01E7GZVZHBWYD50V00XDMYCMYP"	method := "DELETE"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/guide/external_content/types/01E7GZVZHBWYD50V00XDMYCMYP")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("DELETE", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'DELETE',  url: 'https://support.zendesk.com/api/v2/guide/external_content/types/01E7GZVZHBWYD50V00XDMYCMYP',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/guide/external_content/types/01E7GZVZHBWYD50V00XDMYCMYP"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"DELETE",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/guide/external_content/types/01E7GZVZHBWYD50V00XDMYCMYP")request = Net::HTTP::Delete.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**204 No Content**


    // Status 204 No Content
    null

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)