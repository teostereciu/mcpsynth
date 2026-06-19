# User Images

*Source: https://developer.zendesk.com/api-reference/help_center/help-center-api/user_images/*

---

## On this page

  * [Create Image Upload URL and Token](/api-reference/help_center/help-center-api/user_images/#create-image-upload-url-and-token)
  * [Create Image Path](/api-reference/help_center/help-center-api/user_images/#create-image-path)


# User Images

## On this page

  * [Create Image Upload URL and Token](/api-reference/help_center/help-center-api/user_images/#create-image-upload-url-and-token)
  * [Create Image Path](/api-reference/help_center/help-center-api/user_images/#create-image-path)


You can use the User Images API to let end users upload images to a help center instance.

Uploading a user image is a three-step process:

  1. Make a request to create an image upload URL and a token. See Create Image Upload URL and Token.

  2. Make a PUT request to the image upload URL to upload the image. See Uploading the image with the upload URL.

  3. Make a request to create the image path in the help center. See Create Image Path.

You can use the path in the body of a post comment to display the image inline.


### Create Image Upload URL and Token

  * `POST /api/v2/guide/user_images/uploads`


Returns an upload URL and token. Use the upload URL in a PUT request to upload the image to the help center. See Uploading the image with the upload URL below.

After uploading the image, use the image token to create the image path. See Create Image Path.

#### Uploading the image with the upload URL

The endpoint returns an object with the `url` and `headers` properties:


    "headers": {  "Content-Disposition": "attachment; filename=\"01GC9JEN2X052BAKW905PH9C36.jpeg\"",  "Content-Type": "image/jpeg",  "X-Amz-Server-Side-Encryption": "AES256"},..."url": "https://aus-uploaded-assets-production.s3-accelerate.amazonaws.com/20/13633840/01GC9JEN2X052BAKW905PH9C36?Content-Type=image%2Fjpeg&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ACCESS_KEY%2F20220906%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220906T141448Z&X-Amz-Expires=3600&X-Amz-Signature=476f8f09a97cae0bb582716d54dc58cdfbc754c5e20a2c492515d7ffce954971&X-Amz-SignedHeaders=content-disposition%3Bhost%3Bx-amz-server-side-encryption&x-amz-server-side-encryption=AES256"

To upload the image, make a PUT request to the URL and with the specified headers. Agents, end users, or anonymous users can make the request. The maximum file size is 2MB.

The following curl example uploads the image:


    curl -L -X PUT 'https://aus-uploaded-assets-production.s3-accelerate.amazonaws.com/20/13633840/01GC9JEN2X052BAKW905PH9C36?Content-Type=image%2Fjpeg&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ACCESS_KEY%2F20220906%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220906T141448Z&X-Amz-Expires=3600&X-Amz-Signature=476f8f09a97cae0bb582716d54dc58cdfbc754c5e20a2c492515d7ffce954971&X-Amz-SignedHeaders=content-disposition%3Bhost%3Bx-amz-server-side-encryption&x-amz-server-side-encryption=AES256' \  -H 'Content-Disposition: attachment; filename="01GC9JEN2X052BAKW905PH9C36.jpeg"' \  -H 'Content-Type: image/jpeg' \  -H 'X-Amz-Server-Side-Encryption: AES256' \  --data-binary "@{file}"

A successful response will return:


    Status 200 OK

#### Request Body Format

The request body of `POST /api/v2/guide/user_images/uploads` must be a JSON object with the following properties:

Name| Type| Mandatory| Description
---|---|---|---
content_type| string| true| The content type of the file to upload
file_size| number| true| Size of the file in bytes. Max size is 2000000 (2MB).

#### Allowed for

  * Anonymous users


#### Code Samples

**curl**


    curl -X POST https://{subdomain}.zendesk.com/api/v2/guide/user_images/uploads \  -u {email_address}/token:{api_token} \  -d '{"content_type": "image/jpeg", "file_size": 169846}'

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/guide/user_images/uploads"	method := "POST"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/guide/user_images/uploads")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'POST',  url: 'https://support.zendesk.com/api/v2/guide/user_images/uploads',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/guide/user_images/uploads"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/guide/user_images/uploads")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "upload": {    "headers": {      "Content-Disposition": "attachment; filename=\"01F1D8HVJ3TK6CZH8HM51YEQRG.jpeg\"",      "Content-Type": "image/jpeg",      "X-Amz-Server-Side-Encryption": "AES256"    },    "token": "01F1D8HVJ3TK6CZH8HM51YEQRG",    "url": "https://{subdomain}.zendesk.com.com/aus-uploaded-assets/1/42/01F1D8HVJ3TK6CZH8HM51YEQRG?Content-Type=image%2Fjpeg&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ACCESSKEY%2F20210322%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210322T152346Z&X-Amz-Expires=3600&X-Amz-Signature=a5fd09fb179fe3dc3e085398423988f1c5fc5f6a6eb66a0c020905f47b72f11b&X-Amz-SignedHeaders=content-disposition%3Bhost%3Bx-amz-server-side-encryption&x-amz-server-side-encryption=AES256"  }}

### Create Image Path

  * `POST /api/v2/guide/user_images`


Returns the image path that you can use to display the image in a community post.

You should only use this endpoint after uploading the image. See Uploading the image with the upload URL.

#### Request Body Format

The request body must be a JSON object with the following properties:

Name| Type| Mandatory| Description
---|---|---|---
token| string| true| The image token. See Create Image Upload URL and Token
brand_id| string| true| The ID of the brand where this image was uploaded

#### Allowed for

  * Anonymous users


#### Code Samples

**curl**


    curl -X POST https://{subdomain}.zendesk.com/api/v2/guide/user_images \  -u {email_address}/token:{api_token} \  -d '{"token": "01GC9JEN2X052BAKW905PH9C36", "brand_id": "10016"}'

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/guide/user_images"	method := "POST"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/guide/user_images")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'POST',  url: 'https://support.zendesk.com/api/v2/guide/user_images',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/guide/user_images"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/guide/user_images")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**201 Created**


    // Status 201 Created
    {  "user_image": {    "content_type": "image/jpeg",    "path": "/hc/user_images/Bvj4bPDuRd-7d5hFVszvmQ.jpeg",    "size": 169846  }}

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)