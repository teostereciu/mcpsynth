# Article Attachments

*Source: https://developer.zendesk.com/api-reference/help_center/help-center-api/article_attachments/*

---

## On this page

  * [JSON format](/api-reference/help_center/help-center-api/article_attachments/#json-format)
  * [Create Unassociated Attachment](/api-reference/help_center/help-center-api/article_attachments/#create-unassociated-attachment)
  * [Show Article Attachment](/api-reference/help_center/help-center-api/article_attachments/#show-article-attachment)
  * [List Article Attachments](/api-reference/help_center/help-center-api/article_attachments/#list-article-attachments)
  * [Create Article Attachment](/api-reference/help_center/help-center-api/article_attachments/#create-article-attachment)
  * [List Article Block Attachments](/api-reference/help_center/help-center-api/article_attachments/#list-article-block-attachments)
  * [List Article Inline Attachments](/api-reference/help_center/help-center-api/article_attachments/#list-article-inline-attachments)
  * [Show Article Attachment in Article](/api-reference/help_center/help-center-api/article_attachments/#show-article-attachment-in-article)
  * [Delete Article Attachment](/api-reference/help_center/help-center-api/article_attachments/#delete-article-attachment)
  * [List Article Attachments by Locale](/api-reference/help_center/help-center-api/article_attachments/#list-article-attachments-by-locale)
  * [List Article Block Attachments by Locale](/api-reference/help_center/help-center-api/article_attachments/#list-article-block-attachments-by-locale)
  * [List Article Inline Attachments by Locale](/api-reference/help_center/help-center-api/article_attachments/#list-article-inline-attachments-by-locale)


# Article Attachments

## On this page

  * [JSON format](/api-reference/help_center/help-center-api/article_attachments/#json-format)
  * [Create Unassociated Attachment](/api-reference/help_center/help-center-api/article_attachments/#create-unassociated-attachment)
  * [Show Article Attachment](/api-reference/help_center/help-center-api/article_attachments/#show-article-attachment)
  * [List Article Attachments](/api-reference/help_center/help-center-api/article_attachments/#list-article-attachments)
  * [Create Article Attachment](/api-reference/help_center/help-center-api/article_attachments/#create-article-attachment)
  * [List Article Block Attachments](/api-reference/help_center/help-center-api/article_attachments/#list-article-block-attachments)
  * [List Article Inline Attachments](/api-reference/help_center/help-center-api/article_attachments/#list-article-inline-attachments)
  * [Show Article Attachment in Article](/api-reference/help_center/help-center-api/article_attachments/#show-article-attachment-in-article)
  * [Delete Article Attachment](/api-reference/help_center/help-center-api/article_attachments/#delete-article-attachment)
  * [List Article Attachments by Locale](/api-reference/help_center/help-center-api/article_attachments/#list-article-attachments-by-locale)
  * [List Article Block Attachments by Locale](/api-reference/help_center/help-center-api/article_attachments/#list-article-block-attachments-by-locale)
  * [List Article Inline Attachments by Locale](/api-reference/help_center/help-center-api/article_attachments/#list-article-inline-attachments-by-locale)


You can add attachments such as images and PDFs to help center articles. The file size limit is 20 MB per attachment. For more information, see [Creating and editing articles in the knowledge base](https://support.zendesk.com/hc/en-us/articles/203664366) in Zendesk help.

### JSON format

Article Attachments are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
article_id| integer| false| false| The associated article, if present
content_type| string| true| false| The file type. Example: image/png
content_url| string| true| false| URL where the attachment file can be downloaded
created_at| string| true| false| The time the article attachment was created
file| object| false| false| File to upload, applicable only during creation.
file_name| string| true| false| The file name
guide_media_id| string| false| false| Unique identifier for the guide-media to associate with this attachment, applicable only during creation.
id| integer| true| false| Assigned ID when the article attachment is created
inline| boolean| false| false| The attached file is shown in the admin interface for inline attachments. Its URL can be referenced in the article's HTML body. Inline attachments are image files directly embedded in the article body. If false, the attachment is listed in the list of attachments. The default value is false
locale| string| false| false| The locale of translation that the attachment will be attached to and can only be set on inline attachments
size| integer| true| false| The attachment file size in bytes
updated_at| string| true| false| The time the article attachment was last updated
url| string| true| false| The URL of the article attachment

#### Example


    {  "article_id": 23,  "content_type": "application/pdf",  "content_url": "https://company.zendesk.com/hc/article_attachments/200109629",  "created_at": "2012-04-04T09:14:57Z",  "file_name": "party_invitation.pdf",  "id": 1428,  "inline": false,  "locale": "en_us",  "size": 58298}

### Create Unassociated Attachment

  * `POST /api/v2/help_center/articles/attachments`


You can use this endpoint for bulk imports. It lets you upload a file without associating it to an article until later. See [Associate Attachments in Bulk to Article](/api-reference/help_center/help-center-api/articles#associate-attachments-in-bulk-to-article).

If you plan on adding attachments to article translations, import a separate article attachment for each translation and set the locale in advance. For more information on translation attachments, see [Create Article Attachment](/api-reference/help_center/help-center-api/article_attachments/#create-article-attachment).

_Notes:_

  * Zendesk recommends to first create a [Guide media object](/api-reference/help_center/help-center-api/guide_medias/#create-guide-media) and then [create an article attachment](/api-reference/help_center/help-center-api/article_attachments/#create-article-attachment) with the value of the media object's `id`. When creating the attachment, use the value of the media object's `id` as the value of the attachment's `guide_media_id` property.
  * Associate attachments to articles as soon as possible. For example, if you use the endpoint to bulk-import inline images, only signed-in end users can see the images; anonymous users don't have permission to view unassociated images. Also, from time to time, we purge old article attachments not associated to any article. To ensure you don't lose an uploaded file, associate it to an article.


#### Allowed for

  * Agents


#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/articles/attachments.json \  -F "inline=true" -F "guide_media_id=01GFXGBX7YZ9ASWTCVMASTK8ZS" \  -v -u {email_address}/token:{api_token} -X POST

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/articles/attachments"	method := "POST"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/articles/attachments")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'POST',  url: 'https://support.zendesk.com/api/v2/help_center/articles/attachments',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/articles/attachments"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/articles/attachments")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**201 Created**


    // Status 201 Created
    {  "article_attachment": {    "article_id": 23,    "content_type": "application/jpeg",    "content_url": "https://company.zendesk.com/hc/article_attachments/200109629/logo.jpg",    "file_name": "logo.jpg",    "id": 1428,    "inline": true,    "locale": "en_us",    "size": 1428  }}

### Show Article Attachment

  * `GET /api/v2/help_center/articles/attachments/{article_attachment_id}`


Shows the properties of the specified attachment.

**Note** : Omit `{/article_id}` to access unassociated article attachments.

#### Allowed for

  * Agents
  * End users, as long as they can view the associated article


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
article_attachment_id| integer| Path| true| The unique ID of the article attachment

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/articles/attachments/{article_attachment_id}.json \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/articles/attachments/1428"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/articles/attachments/1428")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/help_center/articles/attachments/1428',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/articles/attachments/1428"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/articles/attachments/1428")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "article_attachment": {    "article_id": 23,    "content_type": "application/jpeg",    "content_url": "https://company.zendesk.com/hc/article_attachments/200109629/logo.jpg",    "file_name": "logo.jpg",    "id": 1428,    "inline": true,    "locale": "en_us",    "size": 1428  }}

### List Article Attachments

  * `GET /api/v2/help_center/articles/{article_id}/attachments`


Lists all the article's attachments.

**Note** : By default the pagination returns the maximum attachments per page, which is 100.

#### Allowed for

  * Agents
  * End users, as long as they can view the associated article


#### Pagination

  * Cursor pagination (recommended)
  * Offset pagination


See [Pagination](/api-reference/introduction/pagination/).

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
article_id| integer| Path| true| The unique ID of the article

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/articles/{article_id}/attachments.json \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/articles/360026053753/attachments"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/articles/360026053753/attachments")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/help_center/articles/360026053753/attachments',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/articles/360026053753/attachments"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/articles/360026053753/attachments")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "article_attachments": [    {      "article_id": 23,      "content_type": "application/jpeg",      "content_url": "https://company.zendesk.com/hc/article_attachments/200109629/logo.jpg",      "file_name": "logo.jpg",      "id": 1428,      "inline": true,      "size": 1428    },    {      "article_id": 23,      "content_type": "application/pdf",      "content_url": "https://company.zendesk.com/hc/article_attachments/200109629/party_invitation.pdf",      "file_name": "party_invitation.pdf",      "id": 2857,      "inline": false,      "size": 58298    }  ]}

### Create Article Attachment

  * `POST /api/v2/help_center/articles/{article_id}/attachments`


Creates an attachment for the specified [article](/api-reference/help_center/help-center-api/articles). You can specify whether the attachment is inline or not. The default is false.

The `guide_media_id` parameter is required and must be submitted as multipart form data. This is the id of the media object to be attached to the article. See [Create guide media object](/api-reference/help_center/help-center-api/guide_medias/#create-guide-media). The 'inline' parameter is optional.

If your integration depends on keeping the translation body in sync with an external system, create a separate article attachment for each translation and set the locale in advance. Inline article attachments are automatically assigned a locale when they are embedded in a translation body. If the same attachment is inserted in multiple translations, it will create multiple article attachment records, all linked to the same file, and the references in the translation bodies will be updated accordingly.

_Notes:_

  * First create a [Guide media object](/api-reference/help_center/help-center-api/guide_medias/#create-guide-media) and then [create an article attachment](/api-reference/help_center/help-center-api/article_attachments/#create-article-attachment) with the value of the media object's `id`. When creating the attachment, use the value of the media object's `id` as the value of the attachment's `guide_media_id` property.
  * Inline article attachments that are no longer embedded in the translation get deleted. However the corresponding file is kept in the account's media library.


#### Allowed for

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
article_id| integer| Path| true| The unique ID of the article

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/articles/{article_id}/attachments.json \  -F "inline=true" -F "guide_media_id=01GFXGBX7YZ9ASWTCVMASTK8ZS" \  -v -u {email_address}/token:{api_token} -X POST

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/articles/360026053753/attachments"	method := "POST"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/articles/360026053753/attachments")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'POST',  url: 'https://support.zendesk.com/api/v2/help_center/articles/360026053753/attachments',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/articles/360026053753/attachments"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/articles/360026053753/attachments")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**201 Created**


    // Status 201 Created
    {  "article_attachment": {    "article_id": 23,    "content_type": "application/jpeg",    "content_url": "https://company.zendesk.com/hc/article_attachments/200109629/logo.jpg",    "file_name": "logo.jpg",    "id": 1428,    "inline": true,    "locale": "en_us",    "size": 1428  }}

### List Article Block Attachments

  * `GET /api/v2/help_center/articles/{article_id}/attachments/block`


Lists all the article's block attachments. Block attachments are those that are not inline.

#### Allowed for

  * Agents
  * End users, as long as they can view the associated article


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
article_id| integer| Path| true| The unique ID of the article

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/{locale}/articles/{article_id}/attachments/block.json \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/articles/360026053753/attachments/block"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/articles/360026053753/attachments/block")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/help_center/articles/360026053753/attachments/block',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/articles/360026053753/attachments/block"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/articles/360026053753/attachments/block")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "article_attachments": [    {      "article_id": 23,      "content_type": "application/pdf",      "content_url": "https://company.zendesk.com/hc/article_attachments/200109629/logo.pdf",      "file_name": "logo.pdf",      "id": 1428,      "inline": false,      "size": 1428    },    {      "article_id": 23,      "content_type": "application/msword",      "content_url": "https://company.zendesk.com/hc/article_attachments/200109629/results.doc",      "file_name": "results.doc",      "id": 2857,      "inline": false,      "size": 234    }  ]}

### List Article Inline Attachments

  * `GET /api/v2/help_center/articles/{article_id}/attachments/inline`


Lists all the article's inline attachments.

#### Allowed for

  * Agents
  * End users, as long as they can view the associated article


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
article_id| integer| Path| true| The unique ID of the article

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/{locale}/articles/{article_id}/attachments/inline.json \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/articles/360026053753/attachments/inline"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/articles/360026053753/attachments/inline")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/help_center/articles/360026053753/attachments/inline',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/articles/360026053753/attachments/inline"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/articles/360026053753/attachments/inline")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "article_attachments": [    {      "article_id": 23,      "content_type": "application/jpeg",      "content_url": "https://company.zendesk.com/hc/article_attachments/200109629/logo.jpg",      "file_name": "logo.jpg",      "id": 1428,      "inline": true,      "size": 1428    },    {      "article_id": 23,      "content_type": "application/gif",      "content_url": "https://company.zendesk.com/hc/article_attachments/200109629/footer.gif",      "file_name": "footer.gif",      "id": 2857,      "inline": true,      "locale": "en_us",      "size": 234    }  ]}

### Show Article Attachment in Article

  * `GET /api/v2/help_center/articles/{article_id}/attachments/{article_attachment_id}`


Shows the properties of the specified attachment.

**Note** : Omit `{/article_id}` to access unassociated article attachments.

#### Allowed for

  * Agents
  * End users, as long as they can view the associated article


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
article_attachment_id| integer| Path| true| The unique ID of the article attachment
article_id| integer| Path| true| The unique ID of the article

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/{locale}/articles/attachments/{article_attachment_id}.json \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/articles/360026053753/attachments/1428"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/articles/360026053753/attachments/1428")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/help_center/articles/360026053753/attachments/1428',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/articles/360026053753/attachments/1428"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/articles/360026053753/attachments/1428")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "article_attachment": {    "article_id": 23,    "content_type": "application/jpeg",    "content_url": "https://company.zendesk.com/hc/article_attachments/200109629/logo.jpg",    "file_name": "logo.jpg",    "id": 1428,    "inline": true,    "locale": "en_us",    "size": 1428  }}

### Delete Article Attachment

  * `DELETE /api/v2/help_center/articles/attachments/{article_attachment_id}`


#### Allowed for

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
article_attachment_id| integer| Path| true| The unique ID of the article attachment

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/articles/attachments/{article_attachment_id}.json \  -v -u {email_address}/token:{api_token} -X DELETE

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/articles/attachments/1428"	method := "DELETE"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/articles/attachments/1428")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("DELETE", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'DELETE',  url: 'https://support.zendesk.com/api/v2/help_center/articles/attachments/1428',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/articles/attachments/1428"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"DELETE",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/articles/attachments/1428")request = Net::HTTP::Delete.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**204 No Content**


    // Status 204 No Content
    null

### List Article Attachments by Locale

  * `GET /api/v2/help_center/{locale}/articles/{article_id}/attachments`


Lists all the article's attachments.

**Note** : By default the pagination returns the maximum attachments per page, which is 100.

#### Allowed for

  * Agents
  * End users, as long as they can view the associated article


#### Pagination

  * Cursor pagination (recommended)
  * Offset pagination


See [Pagination](/api-reference/introduction/pagination/).

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
article_id| integer| Path| true| The unique ID of the article
locale| string| Path| true| The locale the item is displayed in

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/{locale}/articles/{article_id}/attachments.json \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/en-us/articles/360026053753/attachments"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/en-us/articles/360026053753/attachments")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/help_center/en-us/articles/360026053753/attachments',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/en-us/articles/360026053753/attachments"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/en-us/articles/360026053753/attachments")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "article_attachments": [    {      "article_id": 23,      "content_type": "application/jpeg",      "content_url": "https://company.zendesk.com/hc/article_attachments/200109629/logo.jpg",      "file_name": "logo.jpg",      "id": 1428,      "inline": true,      "size": 1428    },    {      "article_id": 23,      "content_type": "application/pdf",      "content_url": "https://company.zendesk.com/hc/article_attachments/200109629/party_invitation.pdf",      "file_name": "party_invitation.pdf",      "id": 2857,      "inline": false,      "size": 58298    }  ]}

### List Article Block Attachments by Locale

  * `GET /api/v2/help_center/{locale}/articles/{article_id}/attachments/block`


Lists all the article's block attachments. Block attachments are those that are not inline.

#### Allowed for

  * Agents
  * End users, as long as they can view the associated article


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
article_id| integer| Path| true| The unique ID of the article
locale| string| Path| true| The locale the item is displayed in

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/{locale}/articles/{article_id}/attachments/block.json \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/en-us/articles/360026053753/attachments/block"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/en-us/articles/360026053753/attachments/block")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/help_center/en-us/articles/360026053753/attachments/block',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/en-us/articles/360026053753/attachments/block"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/en-us/articles/360026053753/attachments/block")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "article_attachments": [    {      "article_id": 23,      "content_type": "application/pdf",      "content_url": "https://company.zendesk.com/hc/article_attachments/200109629/logo.pdf",      "file_name": "logo.pdf",      "id": 1428,      "inline": false,      "size": 1428    },    {      "article_id": 23,      "content_type": "application/msword",      "content_url": "https://company.zendesk.com/hc/article_attachments/200109629/results.doc",      "file_name": "results.doc",      "id": 2857,      "inline": false,      "size": 234    }  ]}

### List Article Inline Attachments by Locale

  * `GET /api/v2/help_center/{locale}/articles/{article_id}/attachments/inline`


Lists all the article's inline attachments.

#### Allowed for

  * Agents
  * End users, as long as they can view the associated article


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
article_id| integer| Path| true| The unique ID of the article
locale| string| Path| true| The locale the item is displayed in

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/{locale}/articles/{article_id}/attachments/inline.json \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/en-us/articles/360026053753/attachments/inline"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/en-us/articles/360026053753/attachments/inline")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/help_center/en-us/articles/360026053753/attachments/inline',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/en-us/articles/360026053753/attachments/inline"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/en-us/articles/360026053753/attachments/inline")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "article_attachments": [    {      "article_id": 23,      "content_type": "application/jpeg",      "content_url": "https://company.zendesk.com/hc/article_attachments/200109629/logo.jpg",      "file_name": "logo.jpg",      "id": 1428,      "inline": true,      "size": 1428    },    {      "article_id": 23,      "content_type": "application/gif",      "content_url": "https://company.zendesk.com/hc/article_attachments/200109629/footer.gif",      "file_name": "footer.gif",      "id": 2857,      "inline": true,      "locale": "en_us",      "size": 234    }  ]}

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)