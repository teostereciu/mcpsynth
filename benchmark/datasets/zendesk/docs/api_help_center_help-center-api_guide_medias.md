# Guide Medias

*Source: https://developer.zendesk.com/api-reference/help_center/help-center-api/guide_medias/*

---

## On this page

  * [JSON format](/api-reference/help_center/help-center-api/guide_medias/#json-format)
  * [Search Guide Media](/api-reference/help_center/help-center-api/guide_medias/#search-guide-media)
  * [Create Guide Media](/api-reference/help_center/help-center-api/guide_medias/#create-guide-media)
  * [Create Upload URL for a Guide Media object](/api-reference/help_center/help-center-api/guide_medias/#create-upload-url-for-a-guide-media-object)
  * [Show Guide Media object](/api-reference/help_center/help-center-api/guide_medias/#show-guide-media-object)
  * [Replace Guide Media Object](/api-reference/help_center/help-center-api/guide_medias/#replace-guide-media-object)
  * [Rename Guide Media object](/api-reference/help_center/help-center-api/guide_medias/#rename-guide-media-object)
  * [Delete Guide Media object](/api-reference/help_center/help-center-api/guide_medias/#delete-guide-media-object)


# Guide Medias

## On this page

  * [JSON format](/api-reference/help_center/help-center-api/guide_medias/#json-format)
  * [Search Guide Media](/api-reference/help_center/help-center-api/guide_medias/#search-guide-media)
  * [Create Guide Media](/api-reference/help_center/help-center-api/guide_medias/#create-guide-media)
  * [Create Upload URL for a Guide Media object](/api-reference/help_center/help-center-api/guide_medias/#create-upload-url-for-a-guide-media-object)
  * [Show Guide Media object](/api-reference/help_center/help-center-api/guide_medias/#show-guide-media-object)
  * [Replace Guide Media Object](/api-reference/help_center/help-center-api/guide_medias/#replace-guide-media-object)
  * [Rename Guide Media object](/api-reference/help_center/help-center-api/guide_medias/#rename-guide-media-object)
  * [Delete Guide Media object](/api-reference/help_center/help-center-api/guide_medias/#delete-guide-media-object)


Guide Media objects are files that can be added to Guide articles either embedded in the text or as an attachment. Guide Media objects are only accessible to staff. When an article is published to Help Center, all the Guide Media objects embedded in it get automatically associated with Article Attachments, those attachments are accessible to anyone who has access to the article it is associated with.

### JSON format

Guide Medias are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
access_key| string| false| true| unique identifier used in the URL for accessing the media
content_type| string| false| true|
created_at| string| false| true|
id| string| false| true| Universally Unique Lexicographically Sortable Identifier (ULID). For more information, see the [ULID spec](https://github.com/ulid/spec) on GitHub.
name| string| false| true|
size| integer| false| true| file size in bits
updated_at| string| false| true|
url| string| false| true| path to the media to embed in html bodies
version| integer| false| true| version of the guide media

#### Example


    {  "access_key": "01E86XPM9459S78F83VH8CD69H",  "content_type": "image/png",  "created_at": "2020-05-13T11:46:19.000Z",  "id": "01E86XPPRDCNHYTSVWSRMD76R0",  "name": "hero.png",  "size": 10394,  "updated_at": "2020-05-13T11:46:19.000Z",  "url": "/guide-media/01E86XPM9459S78F83VH8CD69H",  "version": 5}

### Search Guide Media

  * `GET /api/v2/guide/medias`


Returns a paginated list of guide-media objects.

There may be a slight delay between changes to guide-media objects and the result of the search.

You can filter results using the `filter[name_prefix]` query string parameter. Requests using the parameter only show content tags with names that start with a specified prefix. If a prefix is not provided or is set to an empty string, the endpoint returns all content tags.

You can use the `sort` query string parameter to sort results by `created`, `updated`or `name`. To return results in descending order, add a `-` prefix to the sort value. Example: `?sort=-name`.

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
filter| object| Query| false| A group of query parameters for filtering search results
page| object| Query| false| A group of query parameters used for pagination. See [Pagination](/api-reference/help_center/help-center-api/introduction/#pagination)
sort| string| Query| false| Options for sorting the result set by field and direction. Values with no prefix stand for ASC order. Values with the `-` prefix stand for DESC order. Allowed values are "created", "-created", "updated", "-updated", "name", or "-name".

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/guide/medias?filter[access_keys][0]=01J2K07AK4K9XXZGWG0YAT252X&page[size]=1&sort=name \-g -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/medias?filter=&page=&sort="	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/medias")		.newBuilder()		.addQueryParameter("filter", "")		.addQueryParameter("page", "")		.addQueryParameter("sort", "");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/medias',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'filter': '',    'page': '',    'sort': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/medias?filter=&page=&sort="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/medias")uri.query = URI.encode_www_form("filter": "", "page": "", "sort": "")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "meta": {    "after_cursor": "MW",    "before_cursor": "MQ",    "has_more": true  },  "records": [    {      "access_key": "01E86XPM9459S78F83VH8CD69H",      "content_type": "image/png",      "created_at": "2020-05-13T11:46:19.000Z",      "id": "01E86XPPRDCNHYTSVWSRMD76R0",      "name": "hero.png",      "size": 10394,      "updated_at": "2020-05-13T11:46:19.000Z",      "url": "/guide-media/01E86XPM9459S78F83VH8CD69H",      "version": 5    }  ]}

**401 Unauthorized**


    // Status 401 Unauthorized
    {  "errors": [    {      "code": "Unauthorized",      "meta": {},      "status": "401",      "title": "Unauthorized to access the resource"    }  ]}

**403 Forbidden**


    // Status 403 Forbidden
    {  "errors": [    {      "code": "Forbidden",      "meta": {},      "status": "403",      "title": "Access to the resource is forbidden"    }  ]}

### Create Guide Media

  * `POST /api/v2/guide/medias`


Creates a new guide media object from the media asset that was uploaded via the upload URL. Creating a guide media is a 3-steps process:

  1. Request an upload URL.
  2. Upload the file to that URL.
  3. Create the guide-media object.


Returns the Guide media object that you can use in help center articles or to create article attachments.

You should only use this endpoint after uploading the file. See [Uploading the file with the upload URL](/api-reference/help_center/help-center-api/guide_medias/#uploading-the-file-with-the-upload-url).

The response contains `id` and `url` properties. The `id` can then be used to create article attachment. See [Create Article Attachment](/api-reference/help_center/help-center-api/article_attachments/#create-article-attachment). The `url` can be inserted directly into the body of an article translation and it will automatically create an article attachment. Example:


    <h2>Hello World</h2><p><img src="/guide_medias/ABF3G5QYUOP" alt="guide-media"></p>

#### Request Body Format

The request body must be a JSON object with the following properties:

Name| Type| Mandatory| Description
---|---|---|---
asset_upload_id| string| true| The file asset id. See [Get Guide Media Object Upload URL](/api-reference/help_center/help-center-api/guide_medias/#uploading-the-file-with-the-upload-url)
filename| string| true| The name of the file

#### Allowed for

  * Agents


#### Example body


    {  "asset_upload_id": "01J2BS9DMQFEAVJZNBEJNDS3TZ",  "filename": "Screenshot 2024-07-04 at 10.39.26.png"}

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/guide/medias \ -v -u {email_address}/token:{api_token} \ -d '{"asset_upload_id": "12J2BS9DMQFEAVJZNBEJNDS3TZ", "filename": "foo.png"}' \ -X POST

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/medias"	method := "POST"	payload := strings.NewReader(`{  "asset_upload_id": "01J2BS9DMQFEAVJZNBEJNDS3TZ",  "filename": "Screenshot 2024-07-04 at 10.39.26.png"}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/medias")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"asset_upload_id\": \"01J2BS9DMQFEAVJZNBEJNDS3TZ\",  \"filename\": \"Screenshot 2024-07-04 at 10.39.26.png\"}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "asset_upload_id": "01J2BS9DMQFEAVJZNBEJNDS3TZ",  "filename": "Screenshot 2024-07-04 at 10.39.26.png"});
    var config = {  method: 'POST',  url: 'https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/medias',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/medias"
    payload = json.loads("""{  "asset_upload_id": "01J2BS9DMQFEAVJZNBEJNDS3TZ",  "filename": "Screenshot 2024-07-04 at 10.39.26.png"}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/medias")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")request.body = %q({  "asset_upload_id": "01J2BS9DMQFEAVJZNBEJNDS3TZ",  "filename": "Screenshot 2024-07-04 at 10.39.26.png"})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "media": {    "access_key": "01E86XPM9459S78F83VH8CD69H",    "content_type": "image/png",    "created_at": "2020-05-13T11:46:19.000Z",    "id": "01E86XPPRDCNHYTSVWSRMD76R0",    "name": "hero.png",    "size": 10394,    "updated_at": "2020-05-13T11:46:19.000Z",    "url": "/guide-media/01E86XPM9459S78F83VH8CD69H",    "version": 5  }}

**400 Bad Request**


    // Status 400 Bad Request
    {  "errors": [    {      "code": "BadRequest",      "meta": {},      "status": "400",      "title": "Invalid property"    }  ]}

**401 Unauthorized**


    // Status 401 Unauthorized
    {  "errors": [    {      "code": "Unauthorized",      "meta": {},      "status": "401",      "title": "Unauthorized to access the resource"    }  ]}

**409 Conflict**


    // Status 409 Conflict
    {  "errors": [    {      "code": "Conflict",      "meta": {},      "status": "409",      "title": "The request causing a conflict"    }  ]}

### Create Upload URL for a Guide Media object

  * `POST /api/v2/guide/medias/upload_url`


Provisions an upload URL for a guide-media object from the upload service. Use the upload URL to upload the actual media file along with the headers provided in the response. Once the upload is completed, you can create the guide-media object itself by providing the asset_id from the response. Note that uploaded files that do not get associated with a guide-media object get deleted after a short while.

Returns an upload URL and `asset_upload_id`. Use the upload URL in a PUT request to upload the file to the help center. See [Uploading the file with the upload URL](/api-reference/help_center/help-center-api/guide_medias/#uploading-the-file-with-the-upload-url) below.

After uploading the file, use the `asset_upload_id` to create the Guide media object. See [Create Guide Media Object](/api-reference/help_center/help-center-api/guide_medias/#create-guide-media).

**Supported file types**

The Guide Medias API uploads files into Zendesk-hosted storage. For a list of supported image upload file types, see [Working with images in the media library](https://support.zendesk.com/hc/en-us/articles/5020384367002-Working-with-images-in-the-media-library#topic_bnm_cx5_hvb).

#### Uploading the file with the upload URL

The endpoint returns an object with the `upload_url` and `headers` properties:


    {  "headers": {    "Content-Disposition": "attachment; filename=\"01GC9JEN2X052BAKW905PH9C36.jpeg\"",    "Content-Type": "image/jpeg",    "X-Amz-Server-Side-Encryption": "AES256"  },  "upload_url": {    "url": "https://aus-uploaded-assets-production.s3-accelerate.amazonaws.com/20/13633840/01GC9JEN2X052BAKW905PH9C36?Content-Type=image%2Fjpeg&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ACCESS_KEY%2F20220906%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220906T141448Z&X-Amz-Expires=3600&X-Amz-Signature=476f8f09a97cae0bb582716d54dc58cdfbc754c5e20a2c492515d7ffce954971&X-Amz-SignedHeaders=content-disposition%3Bhost%3Bx-amz-server-side-encryption&x-amz-server-side-encryption=AES256",    "asset_upload_id": "01J69HS1J2FS4K6TK7P6JZ22NB"  }}

To upload the file, make a PUT request to the URL specified in the `url` property with the headers specified in the `headers` property. The maximum file size is 20MB.

The following curl example uploads the image:


    curl -L -X PUT 'https://aus-uploaded-assets-production.s3-accelerate.amazonaws.com/20/13633840/01GC9JEN2X052BAKW905PH9C36?Content-Type=image%2Fjpeg&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ACCESS_KEY%2F20220906%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220906T141448Z&X-Amz-Expires=3600&X-Amz-Signature=476f8f09a97cae0bb582716d54dc58cdfbc754c5e20a2c492515d7ffce954971&X-Amz-SignedHeaders=content-disposition%3Bhost%3Bx-amz-server-side-encryption&x-amz-server-side-encryption=AES256' \  -H 'Content-Disposition: attachment; filename="01GC9JEN2X052BAKW905PH9C36.jpeg"' \  -H 'Content-Type: image/jpeg' \  -H 'X-Amz-Server-Side-Encryption: AES256' \  --data-binary "@{file}"

A successful response will return:


    Status 200 OK

#### Request Body Format

The request body of POST /api/v2/guide/medias/upload_url must be a JSON object with the following properties:

Name| Type| Mandatory| Description
---|---|---|---
content_type| string| true| The content type of the file to upload
file_size| number| true| Size of the file in bytes. Max size is 20MB

#### Allowed for

  * Agents


#### Example body


    {  "content_type": "image/png",  "file_size": 12345}

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/guide/medias/upload_url \-v -u {email_address}/token:{api_token} \-d '{"content_type":"image/png", "file_size": 12345}' \-X POST

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/medias/upload_url"	method := "POST"	payload := strings.NewReader(`{  "content_type": "image/png",  "file_size": 12345}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/medias/upload_url")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"content_type\": \"image/png\",  \"file_size\": 12345}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "content_type": "image/png",  "file_size": 12345});
    var config = {  method: 'POST',  url: 'https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/medias/upload_url',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/medias/upload_url"
    payload = json.loads("""{  "content_type": "image/png",  "file_size": 12345}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/medias/upload_url")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")request.body = %q({  "content_type": "image/png",  "file_size": 12345})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "upload_url": {    "asset_upload_id": "01E86XPM9459S78F83VH8CD69H",    "headers": "{\"Content-Disposition\":\"attachment; filename=\"foo.png\"\", \\ \"Content-Type\":\"image/png\",\"X-Amz-Server-Side-Encryption\":\"AES256\"}",    "url": "https://upload-service.zendesk.com/..."  }}

**400 Bad Request**


    // Status 400 Bad Request
    {  "errors": [    {      "code": "BadRequest",      "meta": {},      "status": "400",      "title": "Invalid property"    }  ]}

**401 Unauthorized**


    // Status 401 Unauthorized
    {  "errors": [    {      "code": "Unauthorized",      "meta": {},      "status": "401",      "title": "Unauthorized to access the resource"    }  ]}

### Show Guide Media object

  * `GET /api/v2/guide/medias/{id}`


Shows information about a single the Guide Media object

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
id| string| Path| true| The guide-media id

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/guide/medias/{id} \-v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/medias/01E86XPPRDCNHYTSVWSRMD76R0"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/medias/01E86XPPRDCNHYTSVWSRMD76R0")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/medias/01E86XPPRDCNHYTSVWSRMD76R0',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/medias/01E86XPPRDCNHYTSVWSRMD76R0"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/medias/01E86XPPRDCNHYTSVWSRMD76R0")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "media": {    "access_key": "01E86XPM9459S78F83VH8CD69H",    "content_type": "image/png",    "created_at": "2020-05-13T11:46:19.000Z",    "id": "01E86XPPRDCNHYTSVWSRMD76R0",    "name": "hero.png",    "size": 10394,    "updated_at": "2020-05-13T11:46:19.000Z",    "url": "/guide-media/01E86XPM9459S78F83VH8CD69H",    "version": 5  }}

**400 Bad Request**


    // Status 400 Bad Request
    {  "errors": [    {      "code": "BadRequest",      "meta": {},      "status": "400",      "title": "Invalid property"    }  ]}

**401 Unauthorized**


    // Status 401 Unauthorized
    {  "errors": [    {      "code": "Unauthorized",      "meta": {},      "status": "401",      "title": "Unauthorized to access the resource"    }  ]}

**404 Not Found**


    // Status 404 Not Found
    {  "errors": [    {      "code": "NotFound",      "meta": {},      "status": "404",      "title": "The Resource could not be found"    }  ]}

### Replace Guide Media Object

  * `PUT /api/v2/guide/medias/{id}`


Replaces an existing object with a new one.

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
id| string| Path| true| The guide-media id

#### Example body


    {  "asset_upload_id": "01J2BS9DMQFEAVJZNBEJNDS3TZ",  "filename": "hero.png"}

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/guide/medias/{id} \ -v -u {email_address}/token:{api_token} \ -d '{"asset_upload_id": "12J2BS9DMQFEAVJZNBEJNDS3TZ", "filename": "foo.png"}' \ -X PUT

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/medias/01E86XPPRDCNHYTSVWSRMD76R0"	method := "PUT"	payload := strings.NewReader(`{  "asset_upload_id": "01J2BS9DMQFEAVJZNBEJNDS3TZ",  "filename": "hero.png"}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/medias/01E86XPPRDCNHYTSVWSRMD76R0")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"asset_upload_id\": \"01J2BS9DMQFEAVJZNBEJNDS3TZ\",  \"filename\": \"hero.png\"}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "asset_upload_id": "01J2BS9DMQFEAVJZNBEJNDS3TZ",  "filename": "hero.png"});
    var config = {  method: 'PUT',  url: 'https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/medias/01E86XPPRDCNHYTSVWSRMD76R0',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/medias/01E86XPPRDCNHYTSVWSRMD76R0"
    payload = json.loads("""{  "asset_upload_id": "01J2BS9DMQFEAVJZNBEJNDS3TZ",  "filename": "hero.png"}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/medias/01E86XPPRDCNHYTSVWSRMD76R0")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")request.body = %q({  "asset_upload_id": "01J2BS9DMQFEAVJZNBEJNDS3TZ",  "filename": "hero.png"})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "media": {    "access_key": "01E86XPM9459S78F83VH8CD69H",    "content_type": "image/png",    "created_at": "2020-05-13T11:46:19.000Z",    "id": "01E86XPPRDCNHYTSVWSRMD76R0",    "name": "hero.png",    "size": 10394,    "updated_at": "2020-05-13T11:46:19.000Z",    "url": "/guide-media/01E86XPM9459S78F83VH8CD69H",    "version": 5  }}

**400 Bad Request**


    // Status 400 Bad Request
    {  "errors": [    {      "code": "BadRequest",      "meta": {},      "status": "400",      "title": "Invalid property"    }  ]}

**401 Unauthorized**


    // Status 401 Unauthorized
    {  "errors": [    {      "code": "Unauthorized",      "meta": {},      "status": "401",      "title": "Unauthorized to access the resource"    }  ]}

**404 Not Found**


    // Status 404 Not Found
    {  "errors": [    {      "code": "NotFound",      "meta": {},      "status": "404",      "title": "The Resource could not be found"    }  ]}

**409 Conflict**


    // Status 409 Conflict
    {  "errors": [    {      "code": "Conflict",      "meta": {},      "status": "409",      "title": "The request causing a conflict"    }  ]}

### Rename Guide Media object

  * `PATCH /api/v2/guide/medias/{id}`


Renames a single Guide Media object

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
id| string| Path| true| The guide-media id

#### Example body


    {  "filename": "hero.png"}

#### Code Samples

**curl**


    curl -X PATCH https://{subdomain}.zendesk.com/api/v2/guide/medias/{id} \-v -u {email_address}/token:{api_token} \-d '{"filename":"hero.png"}' \-X PATCH

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/medias/01E86XPPRDCNHYTSVWSRMD76R0"	method := "PATCH"	payload := strings.NewReader(`{  "filename": "hero.png"}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/medias/01E86XPPRDCNHYTSVWSRMD76R0")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"filename\": \"hero.png\"}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PATCH", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "filename": "hero.png"});
    var config = {  method: 'PATCH',  url: 'https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/medias/01E86XPPRDCNHYTSVWSRMD76R0',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/medias/01E86XPPRDCNHYTSVWSRMD76R0"
    payload = json.loads("""{  "filename": "hero.png"}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PATCH",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/medias/01E86XPPRDCNHYTSVWSRMD76R0")request = Net::HTTP::Patch.new(uri, "Content-Type": "application/json")request.body = %q({  "filename": "hero.png"})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "media": {    "access_key": "01E86XPM9459S78F83VH8CD69H",    "content_type": "image/png",    "created_at": "2020-05-13T11:46:19.000Z",    "id": "01E86XPPRDCNHYTSVWSRMD76R0",    "name": "hero.png",    "size": 10394,    "updated_at": "2020-05-13T11:46:19.000Z",    "url": "/guide-media/01E86XPM9459S78F83VH8CD69H",    "version": 5  }}

**400 Bad Request**


    // Status 400 Bad Request
    {  "errors": [    {      "code": "BadRequest",      "meta": {},      "status": "400",      "title": "Invalid property"    }  ]}

**401 Unauthorized**


    // Status 401 Unauthorized
    {  "errors": [    {      "code": "Unauthorized",      "meta": {},      "status": "401",      "title": "Unauthorized to access the resource"    }  ]}

**404 Not Found**


    // Status 404 Not Found
    {  "errors": [    {      "code": "NotFound",      "meta": {},      "status": "404",      "title": "The Resource could not be found"    }  ]}

### Delete Guide Media object

  * `DELETE /api/v2/guide/medias/{id}`


Deletes a single Guide Media object

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
id| string| Path| true| The guide-media id

#### Code Samples

**curl**


    curl -X DELETE https://{subdomain}.zendesk.com/api/v2/guide/medias/{id} \ -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/medias/01E86XPPRDCNHYTSVWSRMD76R0"	method := "DELETE"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/medias/01E86XPPRDCNHYTSVWSRMD76R0")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("DELETE", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'DELETE',  url: 'https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/medias/01E86XPPRDCNHYTSVWSRMD76R0',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/medias/01E86XPPRDCNHYTSVWSRMD76R0"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"DELETE",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/medias/01E86XPPRDCNHYTSVWSRMD76R0")request = Net::HTTP::Delete.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**204 No Content**


    // Status 204 No Content
    null

**400 Bad Request**


    // Status 400 Bad Request
    {  "errors": [    {      "code": "BadRequest",      "meta": {},      "status": "400",      "title": "Invalid property"    }  ]}

**401 Unauthorized**


    // Status 401 Unauthorized
    {  "errors": [    {      "code": "Unauthorized",      "meta": {},      "status": "401",      "title": "Unauthorized to access the resource"    }  ]}

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)