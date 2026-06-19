# Post Comments

*Source: https://developer.zendesk.com/api-reference/help_center/help-center-api/post_comments/*

---

## On this page

  * [JSON format](/api-reference/help_center/help-center-api/post_comments/#json-format)
  * [List Comments](/api-reference/help_center/help-center-api/post_comments/#list-comments)
  * [Show Comment](/api-reference/help_center/help-center-api/post_comments/#show-comment)
  * [Create Post Comment](/api-reference/help_center/help-center-api/post_comments/#create-post-comment)
  * [Update Comment](/api-reference/help_center/help-center-api/post_comments/#update-comment)
  * [Delete Comment](/api-reference/help_center/help-center-api/post_comments/#delete-comment)
  * [List Post Comments by User](/api-reference/help_center/help-center-api/post_comments/#list-post-comments-by-user)


# Post Comments

## On this page

  * [JSON format](/api-reference/help_center/help-center-api/post_comments/#json-format)
  * [List Comments](/api-reference/help_center/help-center-api/post_comments/#list-comments)
  * [Show Comment](/api-reference/help_center/help-center-api/post_comments/#show-comment)
  * [Create Post Comment](/api-reference/help_center/help-center-api/post_comments/#create-post-comment)
  * [Update Comment](/api-reference/help_center/help-center-api/post_comments/#update-comment)
  * [Delete Comment](/api-reference/help_center/help-center-api/post_comments/#delete-comment)
  * [List Post Comments by User](/api-reference/help_center/help-center-api/post_comments/#list-post-comments-by-user)


Users can participate in community discussions by adding comments to [community posts](/api-reference/help_center/help-center-api/posts/) in the help center. The user must have a Zendesk account and their requests must be authenticated. Anonymous users can't add comments. For more information, see [Anatomy of the help center](https://support.zendesk.com/hc/en-us/articles/203664386#ariaid-title4).

### JSON format

Post Comments are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
author_id| integer| false| false| The id of the author of the comment. Writable on create by Help Center managers. See Create Post Comment
body| string| false| true| The comment made by the author. See User content
created_at| string| false| false| When the comment was created. Writable on create by Help Center managers. See Create Post Comment
html_url| string| true| false| The community url of the comment
id| integer| true| false| Automatically assigned when the comment is created
non_author_editor_id| integer| true| false| The user id of whoever performed the most recent (if any) non-author edit. A non-author edit consists of an edit make by a user other than the author that creates or updates the `body`. Note that only edits made after May 17, 2021 will be reflected in this field. If no non-author edits have occured since May 17, 2021, then this field will be `null`.
non_author_updated_at| string| true| false| When the comment was last edited by a non-author user
official| boolean| false| false| Whether the comment is marked as official
post_id| integer| true| false| The id of the post on which the comment was made
updated_at| string| true| false| When the comment was last updated
url| string| true| false| The API url of the comment
vote_count| integer| true| false| The total number of upvotes and downvotes
vote_sum| integer| true| false| The sum of upvotes (+1) and downvotes (-1), which may be positive or negative

#### User content

End users can add their own contents in the form of community posts, post comments, or article comments. Collectively, this is called _user content_. The format of user content is HTML-based.

Content may contain the following standard HTML tags:

  * Paragraphs and blocks: `<p>`, `<div>`, `<span>`, `<br>`
  * Text formatting: `<b>`, `<i>`, `<u>`, `<strong>`, `<em>`, `<sub>`, `<sup>`
  * Links and dividers: `<a>`, `<hr>`
  * Images: `<img>` (where the `src` attribute has to reference a user-uploaded image)
  * Headers: `<h1>`, `<h2>`, `<h3>`, `<h4>`, `<h5>`, `<h6>`
  * Bullet lists: `<ul>`, `<ol>`, `<li>`
  * Description lists: `<dl>`, `<dt>`, `<dd>`
  * Tables: `<table>`, `<thead>`, `<tbody>`, `<tfoot>`, `<tr>`, `<th>`, `<td>`, `<colgroup>`, `<col>`
  * Quotes and code snippets: `<blockquote>`, `<pre>`
  * Semantics: `<abbr>`, `<acronym>`, `<cite>`, `<code>`, `<tt>`, `<samp>`, `<kbd>`, `<var>`, `<dfn>`, `<address>`


In addition, the content may contain these non-standard HTML tags:

  * @mentions: `<x-zendesk-user>`, where the contents of the tag should be the user ID of the mentioned user. Example: `<x-zendesk-user>1234</x-zendesk-user>` to mention the user whose ID is 1234.


Even if the content is validated, the body that's output may not be identical to the request body. For example, adjustments may be made for security or standards-compliance reasons.

#### Example


    {  "author_id": 89567,  "body": "My printer is on fire!",  "id": 35467,  "official": false,  "vote_count": 15,  "vote_sum": 10}

### List Comments

  * `GET /api/v2/community/posts/{post_id}/comments`


Lists all comments on a specific post or all the comments created by a specific user. When listing comments by specific user, the comments of the user making the request can be listed by specifying `me` as the id.

#### Allowed for

  * End users


#### Pagination

  * Cursor pagination (recommended)
  * Offset pagination


See [Pagination](/api-reference/introduction/pagination/).

#### Sideloads

You can sideload related records with the `include` query string parameter. The following sideloads are supported:

Name| Will sideload
---|---
users| authors
posts| posts

See [Sideloading related records](/documentation/developer-tools/working-with-data/sideloading-related-records).

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
post_id| integer| Path| true| The unique ID of the post

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/community/posts/{post_id}/comments.json \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/community/posts/360039436873/comments"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/community/posts/360039436873/comments")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/community/posts/360039436873/comments',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/community/posts/360039436873/comments"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/community/posts/360039436873/comments")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "comments": [    {      "author_id": 89567,      "body": "My printer is on fire!",      "id": 35467    },    {      "author_id": 89589,      "body": "My printer is on fire too!",      "id": 36221    }  ]}

### Show Comment

  * `GET /api/v2/community/posts/{post_id}/comments/{post_comment_id}`


Shows information about the specified comment.

#### Allowed for

  * End users


#### Sideloads

The following sideloads are supported:

Name| Will sideload
---|---
users| The comment's author
posts| The comment's post

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
post_comment_id| integer| Path| true| The unique ID of the post comment
post_id| integer| Path| true| The unique ID of the post

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/community/posts/{post_id}/comments/{post_comment_id}.json \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/community/posts/360039436873/comments/360010837133"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/community/posts/360039436873/comments/360010837133")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/community/posts/360039436873/comments/360010837133',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/community/posts/360039436873/comments/360010837133"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/community/posts/360039436873/comments/360010837133")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "comment": {    "author_id": 89567,    "body": "<p>I love my new non-flammable printer!</p>",    "id": 35467  }}

### Create Post Comment

  * `POST /api/v2/community/posts/{post_id}/comments`


Adds a comment to the specified post.

#### Allowed for

  * End users


Agents with the Help Center manager role can optionally supply an `author_id` as part of the `comment` object. If it is provided, the comment's author will be set to the value of the `author_id` key.

Supplying a `notify_subscribers` property with a value of false will prevent subscribers to the comment's post from receiving a comment creation email notification. This can be helpful when creating many comments at a time. Specify the property in the root of the JSON object, not in the "comment" object.

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
post_id| integer| Path| true| The unique ID of the post

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/community/posts/{post_id}/comments.json \  -d '{"comment": {"body": "I love my new non-flammable printer!"}, "notify_subscribers": false}' \  -v -u {email_address}/token:{api_token} -X POST -H "Content-Type: application/json"
    # Setting the comment's author:curl https://{subdomain}.zendesk.com/api/v2/community/posts/{post_id}/comments.json \  -d '{"comment": {"body": "I love my new non-flammable printer!", "author_id": 10056}}' \  -v -u {email_address}/token:{api_token} -X POST -H "Content-Type: application/json"

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/community/posts/360039436873/comments"	method := "POST"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/community/posts/360039436873/comments")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'POST',  url: 'https://support.zendesk.com/api/v2/community/posts/360039436873/comments',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/community/posts/360039436873/comments"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/community/posts/360039436873/comments")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**201 Created**


    // Status 201 Created
    {  "comment": {    "author_id": 89567,    "body": "<p>I love my new non-flammable printer!</p>",    "id": 35467  }}

### Update Comment

  * `PUT /api/v2/community/posts/{post_id}/comments/{post_comment_id}`


Updates the specified comment.

#### Allowed for

  * Agents
  * The end user who created the comment


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
post_comment_id| integer| Path| true| The unique ID of the post comment
post_id| integer| Path| true| The unique ID of the post

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/community/posts/{post_id}/comments/{post_comment_id}.json \  -d '{"comment": {"body": "The new, non-flammable printer is on fire too!"}}' \  -v -u {email_address}/token:{api_token} -X PUT -H "Content-Type: application/json"

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/community/posts/360039436873/comments/360010837133"	method := "PUT"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/community/posts/360039436873/comments/360010837133")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'PUT',  url: 'https://support.zendesk.com/api/v2/community/posts/360039436873/comments/360010837133',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/community/posts/360039436873/comments/360010837133"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/community/posts/360039436873/comments/360010837133")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "comment": {    "author_id": 89567,    "body": "<p>I love my new non-flammable printer!</p>",    "id": 35467  }}

### Delete Comment

  * `DELETE /api/v2/community/posts/{post_id}/comments/{post_comment_id}`


Deletes the specified comment.

#### Allowed for

  * Agents
  * The end user who created the comment


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
post_comment_id| integer| Path| true| The unique ID of the post comment
post_id| integer| Path| true| The unique ID of the post

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/community/posts/{post_id}/comments/{post_comment_id}.json \  -v -u {email_address}/token:{api_token} -X DELETE

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/community/posts/360039436873/comments/360010837133"	method := "DELETE"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/community/posts/360039436873/comments/360010837133")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("DELETE", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'DELETE',  url: 'https://support.zendesk.com/api/v2/community/posts/360039436873/comments/360010837133',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/community/posts/360039436873/comments/360010837133"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"DELETE",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/community/posts/360039436873/comments/360010837133")request = Net::HTTP::Delete.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**204 No Content**


    // Status 204 No Content
    null

### List Post Comments by User

  * `GET /api/v2/community/users/{user_id}/comments`


Lists all comments on a specific post or all the comments created by a specific user. When listing comments by specific user, the comments of the user making the request can be listed by specifying `me` as the id.

#### Allowed for

  * End users


#### Pagination

  * Cursor pagination (recommended)
  * Offset pagination


See [Pagination](/api-reference/introduction/pagination/).

#### Sideloads

You can sideload related records with the `include` query string parameter. The following sideloads are supported:

Name| Will sideload
---|---
users| authors
posts| posts

See [Sideloading related records](/documentation/developer-tools/working-with-data/sideloading-related-records).

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
user_id| integer| Path| true| The unique ID of the user

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/community/users/{user_id}/comments \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/community/users/1234/comments"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/community/users/1234/comments")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/community/users/1234/comments',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/community/users/1234/comments"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/community/users/1234/comments")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "comments": [    {      "author_id": 89567,      "body": "My printer is on fire!",      "id": 35467    },    {      "author_id": 89589,      "body": "My printer is on fire too!",      "id": 36221    }  ]}

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)