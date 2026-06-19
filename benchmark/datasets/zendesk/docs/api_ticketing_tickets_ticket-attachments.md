# Attachments

*Source: https://developer.zendesk.com/api-reference/ticketing/tickets/ticket-attachments/*

---

## On this page

  * [JSON format](/api-reference/ticketing/tickets/ticket-attachments/#json-format)
  * [Upload Files](/api-reference/ticketing/tickets/ticket-attachments/#upload-files)
  * [Delete Upload](/api-reference/ticketing/tickets/ticket-attachments/#delete-upload)
  * [Show Attachment](/api-reference/ticketing/tickets/ticket-attachments/#show-attachment)
  * [Update Attachment for Malware](/api-reference/ticketing/tickets/ticket-attachments/#update-attachment-for-malware)
  * [Delete Attachment](/api-reference/ticketing/tickets/ticket-attachments/#delete-attachment)
  * [Redact Comment Attachment](/api-reference/ticketing/tickets/ticket-attachments/#redact-comment-attachment)


# Attachments

## On this page

  * [JSON format](/api-reference/ticketing/tickets/ticket-attachments/#json-format)
  * [Upload Files](/api-reference/ticketing/tickets/ticket-attachments/#upload-files)
  * [Delete Upload](/api-reference/ticketing/tickets/ticket-attachments/#delete-upload)
  * [Show Attachment](/api-reference/ticketing/tickets/ticket-attachments/#show-attachment)
  * [Update Attachment for Malware](/api-reference/ticketing/tickets/ticket-attachments/#update-attachment-for-malware)
  * [Delete Attachment](/api-reference/ticketing/tickets/ticket-attachments/#delete-attachment)
  * [Redact Comment Attachment](/api-reference/ticketing/tickets/ticket-attachments/#redact-comment-attachment)


You can upload a file and attach it to a ticket comment. The attachment appears as a link in the ticket comment in the agent interface in Zendesk. If ticket notifications are enabled, the attachment appears as a link in the notification email.

Use the Attachments API to upload a file you want to attach. However, you can only attach the uploaded file to a ticket comment with the [Tickets API](/api-reference/ticketing/tickets/tickets/) when adding the comment to a ticket you're creating or updating.

For details and examples, see [Adding ticket attachments with the API](/documentation/ticketing/managing-tickets/adding-ticket-attachments-with-the-api/).

This API is for tickets attachments. To attach files to articles in your help center, see [Article Attachments](/api-reference/help_center/help-center-api/article_attachments/) in the Help Center API documentation.

### JSON format

Attachments are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
content_type| string| true| false| The content type of the image. Example value: "image/png"
content_url| string| true| false| A full URL where the attachment image file can be downloaded. The file may be hosted externally so take care not to inadvertently send Zendesk authentication credentials. See [Working with url properties](/documentation/api-basics/best-practices/working-with-url-properties/)
deleted| boolean| true| false| If true, the attachment has been deleted
file_name| string| true| false| The name of the image file
height| integer| true| false| The height of the image file in pixels. If height is unknown, returns null
id| integer| true| false| Automatically assigned when created
inline| boolean| true| false| If true, the attachment is excluded from the attachment list and the attachment's URL can be referenced within the comment of a ticket. Default is false
malware_access_override| boolean| true| false| If true, you can download an attachment flagged as malware. If false, you can't download such an attachment.
malware_scan_result| string| true| false| The result of the malware scan. There is a delay between the time the attachment is uploaded and when the malware scan is completed. Usually the scan is done within a few seconds, but high load conditions can delay the scan results. Possible values: "malware_found", "malware_not_found", "failed_to_scan", "not_scanned"
mapped_content_url| string| true| false| The URL the attachment image file has been mapped to
size| integer| true| false| The size of the image file in bytes
thumbnails| array| true| false| An array of attachment objects. Note that photo thumbnails do not have thumbnails
url| string| true| false| A URL to access the attachment details
width| integer| true| false| The width of the image file in pixels. If width is unknown, returns null

A file represented as an [Attachment](/api-reference/ticketing/tickets/ticket-attachments/) object

#### Example


    {  "content_type": "image/png",  "content_url": "https://company.zendesk.com/attachments/my_funny_profile_pic.png",  "file_name": "my_funny_profile_pic.png",  "id": 928374,  "size": 166144,  "thumbnails": [    {      "content_type": "image/png",      "content_url": "https://company.zendesk.com/attachments/my_funny_profile_pic_thumb.png",      "file_name": "my_funny_profile_pic_thumb.png",      "id": 928375,      "size": 58298    }  ]}

### Upload Files

  * `POST /api/v2/uploads?filename={filename}`


Uploads a file that can be attached to a ticket comment. It doesn't attach the file to the comment. For details and examples, see [Attaching ticket comments with the API](/documentation/ticketing/managing-tickets/adding-ticket-attachments-with-the-api/).

The endpoint has a required `filename` query parameter. The parameter specifies what the file will be named when attached to the ticket comment (to give the agent more context about the file). The parameter does not specify the file on the local system to be uploaded. While the two names can be different, their file extensions must be the same. If they don't match, the agent's browser or file reader could give an error when attempting to open the attachment.

The `Content-Type` header must contain a recognized MIME type that correctly describes the type of the uploaded file. Failing to send a recognized, correct type may cause undesired behavior. For example, in-browser audio playback may be interrupted by the browser's security mechanisms for MP3s uploaded with an incorrect type.

Adding multiple files to the same upload is handled by splitting requests and passing the API token received from the first request to each subsequent request. The token is valid for 60 minutes.

**Note** : Even if [private attachments](https://support.zendesk.com/hc/en-us/articles/204265396) are enabled in the Zendesk Support instance, uploaded files are visible to any authenticated user at the `content_URL` specified in the JSON response until the upload token is consumed. Once a file is associated with a ticket or post, visibility is restricted to users with access to the ticket or post with the attachment.

#### Allowed For

  * End users


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
filename| string| Query| true| The name to assign to the uploaded file

#### Code Samples

**curl**


    curl "https://{subdomain}.zendesk.com/api/v2/uploads?filename=user_crash.log&token={optional_token}" \  --data-binary @crash.log \  -H "Content-Type: text/plain" \  -v -u {email_address}/token:{api_token} \  -X POST

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/uploads?filename=my_document.pdf"	method := "POST"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/uploads")		.newBuilder()		.addQueryParameter("filename", "my_document.pdf");RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'POST',  url: 'https://example.zendesk.com/api/v2/uploads',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'filename': 'my_document.pdf',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/uploads?filename=my_document.pdf"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/uploads")uri.query = URI.encode_www_form("filename": "my_document.pdf")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**201 Created**


    // Status 201 Created
    {  "upload": {    "attachment": {      "content_type": "image/png",      "content_url": "https://company.zendesk.com/attachments/token/tyBq1ms40dFaHefSIigxZpwGg/?name=crash.png",      "deleted": false,      "file_name": "crash.png",      "height": 62,      "id": 1503729607981,      "inline": false,      "mapped_content_url": "https://company.zendesk.com/attachments/token/tyBq1ms40dFaHefSIigxZpwGg/?name=crash.png",      "size": 5172,      "thumbnails": [],      "url": "https://company.zendesk.com/api/v2/attachments/1503729607981",      "width": 80    },    "attachments": [      {        "content_type": "image/png",        "content_url": "https://company.zendesk.com/attachments/token/tyBq1ms40dFaHefSIigxZpwGg/?name=crash.png",        "deleted": false,        "file_name": "crash.png",        "height": 62,        "id": 1503729607981,        "inline": false,        "mapped_content_url": "https://company.zendesk.com/attachments/token/tyBq1ms40dFaHefSIigxZpwGg/?name=crash.png",        "size": 5172,        "thumbnails": [],        "url": "https://company.zendesk.com/api/v2/attachments/1503729607981",        "width": 80      }    ],    "token": "LXJdriewLBP8JrtzzkN7Ne4k6"  }}

### Delete Upload

  * `DELETE /api/v2/uploads/{token}`


#### Allowed for

  * End Users


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
token| string| Path| true| The token of the uploaded attachment

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/uploads/{token} \  -v -u {email_address}/token:{api_token} -X DELETE

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/uploads/6bk3gql82em5nmf"	method := "DELETE"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/uploads/6bk3gql82em5nmf")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("DELETE", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'DELETE',  url: 'https://example.zendesk.com/api/v2/uploads/6bk3gql82em5nmf',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/uploads/6bk3gql82em5nmf"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"DELETE",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/uploads/6bk3gql82em5nmf")request = Net::HTTP::Delete.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**204 No Content**


    // Status 204 No Content
    null

### Show Attachment

  * `GET /api/v2/attachments/{attachment_id}`


Shows attachment details. You can get the value of the `attachment_id` parameter by listing the ticket's comments. See [List Comments](/api-reference/ticketing/tickets/ticket_comments/#list-comments). Each comment in the list has an `attachments` list that specifies an `id` for each attachment.

#### Allowed for

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
attachment_id| integer| Path| true| The ID of the attachment

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/attachments/{attachment_id} \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/attachments/498483"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/attachments/498483")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/attachments/498483',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/attachments/498483"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/attachments/498483")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "attachment": {    "content_type": "application/binary",    "content_url": "https://company.zendesk.com/attachments/myfile.dat",    "file_name": "myfile.dat",    "id": 498483,    "size": 2532,    "thumbnails": [],    "url": "https://company.zendesk.com/api/v2/attachments/498483"  }}

### Update Attachment for Malware

  * `PUT /api/v2/attachments/{attachment_id}`


Toggles enabling or restricting agent access to attachments with detected malware.

#### Allowed For

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
attachment_id| integer| Path| true| The ID of the attachment

#### Example body


    {  "attachment": {    "malware_access_override": true  }}

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/attachments/{attachment_id} \  -H "Content-Type: application/json" -d '{"attachment": {"malware_access_override": true}}' \  -v -u {email_address}/token:{api_token} -X PUT

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://example.zendesk.com/api/v2/attachments/498483"	method := "PUT"	payload := strings.NewReader(`{  "attachment": {    "malware_access_override": true  }}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/attachments/498483")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"attachment\": {    \"malware_access_override\": true  }}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "attachment": {    "malware_access_override": true  }});
    var config = {  method: 'PUT',  url: 'https://example.zendesk.com/api/v2/attachments/498483',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/attachments/498483"
    payload = json.loads("""{  "attachment": {    "malware_access_override": true  }}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/attachments/498483")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")request.body = %q({  "attachment": {    "malware_access_override": true  }})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "attachment": {    "content_type": "application/binary",    "content_url": "https://company.zendesk.com/attachments/myfile.dat",    "file_name": "myfile.dat",    "id": 498483,    "size": 2532,    "thumbnails": [],    "url": "https://company.zendesk.com/api/v2/attachments/498483"  }}

### Delete Attachment

  * `DELETE /api/v2/attachments/{attachment_id}`


Deletes the attachment.

#### Allowed for

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
attachment_id| integer| Path| true| The ID of the attachment

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/attachments/{attachment_id} \  -v -u {email_address}/token:{api_token} \  -X DELETE

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/attachments/498483"	method := "DELETE"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/attachments/498483")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("DELETE", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'DELETE',  url: 'https://example.zendesk.com/api/v2/attachments/498483',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/attachments/498483"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"DELETE",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/attachments/498483")request = Net::HTTP::Delete.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**204 No Content**


    // Status 204 No Content
    null

### Redact Comment Attachment

  * `PUT /api/v2/tickets/{ticket_id}/comments/{comment_id}/attachments/{attachment_id}/redact`


Redaction allows you to permanently remove attachments from an existing comment on a ticket. Once removed from a comment, the attachment is replaced with an empty "redacted.txt" file.

The redaction is permanent. It is not possible to undo redaction or see what was removed. Once a ticket is closed, redacting its attachments is no longer possible.

Also, if you want to redact an inline attachment, you can use the `include_inline_images` parameter in the [List Comments](/api-reference/ticketing/tickets/ticket_comments/#list-comments) operation to obtain the inline attachment ID, and use it in the request URL.

#### Allowed For

  * Admins
  * Agents when [deleting tickets is enabled for agents on professional accounts](https://support.zendesk.com/hc/en-us/articles/360002128107)
  * Agents assigned to a custom role with permissions to redact ticket content (Enterprise only)


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
attachment_id| integer| Path| true| The ID of the attachment
comment_id| integer| Path| true| The ID of the comment
ticket_id| integer| Path| true| The ID of the ticket

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/tickets/{ticket_id}/comments/{comment_id}/attachments/{attachment_id}/redact \  -H "Content-Type: application/json" -v -u {email_address}/token:{api_token} -X PUT -d '{}'

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/tickets/123456/comments/654321/attachments/498483/redact"	method := "PUT"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/tickets/123456/comments/654321/attachments/498483/redact")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'PUT',  url: 'https://example.zendesk.com/api/v2/tickets/123456/comments/654321/attachments/498483/redact',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/tickets/123456/comments/654321/attachments/498483/redact"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/tickets/123456/comments/654321/attachments/498483/redact")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "attachment": {    "content_type": "application/binary",    "content_url": "https://company.zendesk.com/attachments/myfile.dat",    "file_name": "myfile.dat",    "id": 498483,    "size": 2532,    "thumbnails": [],    "url": "https://company.zendesk.com/api/v2/attachments/498483"  }}

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)