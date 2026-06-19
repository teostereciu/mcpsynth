# Article Comments

*Source: https://developer.zendesk.com/api-reference/help_center/help-center-api/article_comments/*

---

## On this page

  * [JSON format](/api-reference/help_center/help-center-api/article_comments/#json-format)
  * [List Article Comments](/api-reference/help_center/help-center-api/article_comments/#list-article-comments)
  * [List Article Comments by User](/api-reference/help_center/help-center-api/article_comments/#list-article-comments-by-user)
  * [List Article Comments by Locale](/api-reference/help_center/help-center-api/article_comments/#list-article-comments-by-locale)
  * [Show Article Comment](/api-reference/help_center/help-center-api/article_comments/#show-article-comment)
  * [Show Article Comment by Locale](/api-reference/help_center/help-center-api/article_comments/#show-article-comment-by-locale)
  * [Create Article Comment](/api-reference/help_center/help-center-api/article_comments/#create-article-comment)
  * [Create Comment](/api-reference/help_center/help-center-api/article_comments/#create-comment)
  * [Update Article Comment](/api-reference/help_center/help-center-api/article_comments/#update-article-comment)
  * [Update Article Comment by Locale](/api-reference/help_center/help-center-api/article_comments/#update-article-comment-by-locale)
  * [Delete Article Comment](/api-reference/help_center/help-center-api/article_comments/#delete-article-comment)
  * [Delete Article Comment by Locale](/api-reference/help_center/help-center-api/article_comments/#delete-article-comment-by-locale)


# Article Comments

## On this page

  * [JSON format](/api-reference/help_center/help-center-api/article_comments/#json-format)
  * [List Article Comments](/api-reference/help_center/help-center-api/article_comments/#list-article-comments)
  * [List Article Comments by User](/api-reference/help_center/help-center-api/article_comments/#list-article-comments-by-user)
  * [List Article Comments by Locale](/api-reference/help_center/help-center-api/article_comments/#list-article-comments-by-locale)
  * [Show Article Comment](/api-reference/help_center/help-center-api/article_comments/#show-article-comment)
  * [Show Article Comment by Locale](/api-reference/help_center/help-center-api/article_comments/#show-article-comment-by-locale)
  * [Create Article Comment](/api-reference/help_center/help-center-api/article_comments/#create-article-comment)
  * [Create Comment](/api-reference/help_center/help-center-api/article_comments/#create-comment)
  * [Update Article Comment](/api-reference/help_center/help-center-api/article_comments/#update-article-comment)
  * [Update Article Comment by Locale](/api-reference/help_center/help-center-api/article_comments/#update-article-comment-by-locale)
  * [Delete Article Comment](/api-reference/help_center/help-center-api/article_comments/#delete-article-comment)
  * [Delete Article Comment by Locale](/api-reference/help_center/help-center-api/article_comments/#delete-article-comment-by-locale)


Users can provide feedback in the knowledge base by adding comments to [articles](/api-reference/help_center/help-center-api/articles/). The user must have a Zendesk account and their requests must be authenticated. Anonymous users can't add comments. For more information, see [Anatomy of the help center](https://support.zendesk.com/hc/en-us/articles/203664386#topic_kdk_srm_4k).

### JSON format

Article Comments are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
author_id| integer| false| false| The id of the author of this comment. Writable on create by Help Center managers. See Create Comment
body| string| false| true| The comment made by the author. See User content
created_at| string| false| false| The time the comment was created. Writable on create by Help Center managers. See Create Comment
html_url| string| true| false| The url at which the comment is presented in Help Center
id| integer| true| false| Automatically assigned when the comment is created
locale| string| false| true| The locale in which this comment was made
non_author_editor_id| integer| true| false| The user id of whoever performed the most recent (if any) non-author edit. A non-author edit consists of an edit make by a user other than the author that creates or updates the `body` or `author_id`. Note that only edits made after May 17, 2021 will be reflected in this field. If no non-author edits have occured since May 17, 2021, then this field will be `null`.
non_author_updated_at| string| true| false| When the comment was last edited by a non-author user
source_id| integer| true| false| The id of the item on which this comment was made
source_type| string| true| false| The type of the item on which this comment was made. Currently only supports 'Article'
updated_at| string| true| false| The time at which the comment was last updated
url| string| true| false| The API url of this comment
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


    {  "author_id": 3465,  "body": "Thanks for your help!",  "created_at": "2012-04-04T09:14:57Z",  "id": 1635,  "locale": "en-us",  "source_id": 65466,  "source_type": "Article"}

### List Article Comments

  * `GET /api/v2/help_center/articles/{article_id}/comments`


Lists all comments made by all users on a specific article.

#### Allowed for

  * Agents


End-users can only list their own comments. If listing comments by user, they must specify `me` as the id.

#### Pagination

  * Cursor pagination (recommended)
  * Offset pagination


See [Pagination](/api-reference/introduction/pagination/).

#### Sideloads

The following sideloads are supported:

Name| Will sideload
---|---
users| authors
articles| articles

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
article_id| integer| Path| true| The unique ID of the article

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/articles/{article_id}/comments \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/articles/360026053753/comments"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/articles/360026053753/comments")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/help_center/articles/360026053753/comments',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/articles/360026053753/comments"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/articles/360026053753/comments")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "comments": [    {      "author_id": 89567,      "body": "My printer is on fire",      "id": 35467,      "locale": "en"    },    {      "author_id": 89589,      "body": "My printer is on fire too!",      "id": 36221,      "locale": "en"    }  ]}

### List Article Comments by User

  * `GET /api/v2/help_center/users/{user_id}/comments`


Lists the comments created by a specific user.

#### Allowed for

  * Agents


#### Pagination

  * Cursor pagination (recommended)
  * Offset pagination


See [Pagination](/api-reference/introduction/pagination/).

#### Sideloads

The following sideloads are supported:

Name| Will sideload
---|---
users| authors
articles| articles

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
user_id| integer| Path| true| The unique ID of the user

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/users/{user_id}/comments \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/users/1234/comments"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/users/1234/comments")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/help_center/users/1234/comments',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/users/1234/comments"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/users/1234/comments")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "comments": [    {      "author_id": 89567,      "body": "My printer is on fire",      "id": 35467,      "locale": "en"    },    {      "author_id": 89589,      "body": "My printer is on fire too!",      "id": 36221,      "locale": "en"    }  ]}

### List Article Comments by Locale

  * `GET /api/v2/help_center/{locale}/articles/{article_id}/comments`


Lists the comments created by a specific user, or all comments made by all users on a specific article.

The `{locale}` for the article comments is required only for end users. Admins and agents can omit it.

#### Allowed for

  * End users


End-users can only list their own comments. If listing comments by user, they must specify `me` as the id.

#### Pagination

  * Cursor pagination (recommended)
  * Offset pagination


See [Pagination](/api-reference/introduction/pagination/).

#### Sideloads

The following sideloads are supported:

Name| Will sideload
---|---
users| authors
articles| articles

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
article_id| integer| Path| true| The unique ID of the article
locale| string| Path| true| The locale the item is displayed in

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/users/{user_id}/comments.json \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/en-us/articles/360026053753/comments"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/en-us/articles/360026053753/comments")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/help_center/en-us/articles/360026053753/comments',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/en-us/articles/360026053753/comments"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/en-us/articles/360026053753/comments")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "comments": [    {      "author_id": 89567,      "body": "My printer is on fire",      "id": 35467,      "locale": "en"    },    {      "author_id": 89589,      "body": "My printer is on fire too!",      "id": 36221,      "locale": "en"    }  ]}

### Show Article Comment

  * `GET /api/v2/help_center/articles/{article_id}/comments/{comment_id}`


Shows the properties of the specified comment.

#### Allowed for

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
article_id| integer| Path| true| The unique ID of the article
comment_id| integer| Path| true| The unique ID of the comment

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/articles/{article_id}/comments/{comment_id} \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/articles/360026053753/comments/360004163994"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/articles/360026053753/comments/360004163994")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/help_center/articles/360026053753/comments/360004163994',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/articles/360026053753/comments/360004163994"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/articles/360026053753/comments/360004163994")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "comment": {    "author_id": 89567,    "body": "Good info!",    "id": 35467,    "locale": "en"  }}

### Show Article Comment by Locale

  * `GET /api/v2/help_center/{locale}/articles/{article_id}/comments/{comment_id}`


Shows the properties of the specified comment.

The `{locale}` is required only for end users and anomynous users. Admins and agents can omit it.

#### Allowed for

  * Anonymous users


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
article_id| integer| Path| true| The unique ID of the article
comment_id| integer| Path| true| The unique ID of the comment
locale| string| Path| true| The locale the item is displayed in

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/{locale}/articles/{article_id}/comments/{comment_id}.json \-v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/en-us/articles/360026053753/comments/360004163994"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/en-us/articles/360026053753/comments/360004163994")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/help_center/en-us/articles/360026053753/comments/360004163994',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/en-us/articles/360026053753/comments/360004163994"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/en-us/articles/360026053753/comments/360004163994")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "comment": {    "author_id": 89567,    "body": "Good info!",    "id": 35467,    "locale": "en"  }}

### Create Article Comment

  * `POST /api/v2/help_center/articles/{article_id}/comments`


Adds a comment to the specified [article](/api-reference/help_center/help-center-api/articles). Because comments are associated with a specific article translation, or locale, you must specify a locale.

#### Allowed for

  * End users


Agents with the Help Center manager role can optionally supply a `created_at` as part of the `comment` object. If not provided, `created_at` is set to the current time.

Supplying a `notify_subscribers` property with a value of false will prevent subscribers to the comment's article from receiving a comment creation email notification. This can be helpful when creating many comments at a time. Specify the property in the root of the JSON object, not in the "comment" object.

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
article_id| integer| Path| true| The unique ID of the article

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/articles/{article_id}/comments \  -d '{"comment": {"body": "Good info!", "locale": "en-us"}, "notify_subscribers": false}'  -v -u {email_address}/token:{api_token} -X POST -H "Content-Type: application/json"

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/articles/360026053753/comments"	method := "POST"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/articles/360026053753/comments")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'POST',  url: 'https://support.zendesk.com/api/v2/help_center/articles/360026053753/comments',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/articles/360026053753/comments"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/articles/360026053753/comments")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "comment": {    "author_id": 89567,    "body": "Good info!",    "id": 35467,    "locale": "en"  }}

### Create Comment

  * `POST /api/v2/help_center/{locale}/articles/{article_id}/comments`


Adds a comment to the specified [article](/api-reference/help_center/help-center-api/articles). Because comments are associated with a specific article translation, or locale, you must specify a locale.

#### Allowed for

  * End users


Agents with the Help Center manager role can optionally supply a `created_at` as part of the `comment` object. If not provided, `created_at` is set to the current time.

Supplying a `notify_subscribers` property with a value of false will prevent subscribers to the comment's article from receiving a comment creation email notification. This can be helpful when creating many comments at a time. Specify the property in the root of the JSON object, not in the "comment" object.

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
article_id| integer| Path| true| The unique ID of the article
locale| string| Path| true| The locale the item is displayed in

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/articles/{article_id}/comments.json \  -d '{"comment": {"body": "Good info!", "locale": "en-us"}, "notify_subscribers": false}'  -v -u {email_address}/token:{api_token} -X POST -H "Content-Type: application/json"

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/en-us/articles/360026053753/comments"	method := "POST"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/en-us/articles/360026053753/comments")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'POST',  url: 'https://support.zendesk.com/api/v2/help_center/en-us/articles/360026053753/comments',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/en-us/articles/360026053753/comments"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/en-us/articles/360026053753/comments")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "comment": {    "author_id": 89567,    "body": "Good info!",    "id": 35467,    "locale": "en"  }}

### Update Article Comment

  * `PUT /api/v2/help_center/articles/{article_id}/comments/{comment_id}`


#### Allowed for

  * Agents
  * The end user who created the comment


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
article_id| integer| Path| true| The unique ID of the article
comment_id| integer| Path| true| The unique ID of the comment

#### Code Samples

**Curl**


    curl --request PUT https://support.zendesk.com/api/v2/help_center/articles/360026053753/comments/360004163994 \--header "Content-Type: application/json" \-u {email_address}/token:{api_token}

****


     curl https://{subdomain}.zendesk.com/api/v2/help_center/articles/{article_id}/comments/{comment_id} \  -d '{"comment": {"body": "Did not work"}}' \  -v -u {email_address}/token:{api_token} -X PUT -H "Content-Type: application/json"

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/articles/360026053753/comments/360004163994"	method := "PUT"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/articles/360026053753/comments/360004163994")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'PUT',  url: 'https://support.zendesk.com/api/v2/help_center/articles/360026053753/comments/360004163994',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/articles/360026053753/comments/360004163994"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/articles/360026053753/comments/360004163994")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "comment": {    "author_id": 89567,    "body": "Good info!",    "id": 35467,    "locale": "en"  }}

### Update Article Comment by Locale

  * `PUT /api/v2/help_center/{locale}/articles/{article_id}/comments/{comment_id}`


#### Allowed for

  * Agents
  * The end user who created the comment


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
article_id| integer| Path| true| The unique ID of the article
comment_id| integer| Path| true| The unique ID of the comment
locale| string| Path| true| The locale the item is displayed in

#### Code Samples

**Curl**


    curl --request PUT https://support.zendesk.com/api/v2/help_center/en-us/articles/360026053753/comments/360004163994 \--header "Content-Type: application/json" \-u {email_address}/token:{api_token}

****


     curl https://{subdomain}.zendesk.com/api/v2/help_center/articles/{article_id}/comments/{comment_id}.json \  -d '{"comment": {"body": "Did not work"}}' \  -v -u {email_address}/token:{api_token} -X PUT -H "Content-Type: application/json"

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/en-us/articles/360026053753/comments/360004163994"	method := "PUT"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/en-us/articles/360026053753/comments/360004163994")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'PUT',  url: 'https://support.zendesk.com/api/v2/help_center/en-us/articles/360026053753/comments/360004163994',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/en-us/articles/360026053753/comments/360004163994"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/en-us/articles/360026053753/comments/360004163994")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "comment": {    "author_id": 89567,    "body": "Good info!",    "id": 35467,    "locale": "en"  }}

### Delete Article Comment

  * `DELETE /api/v2/help_center/articles/{article_id}/comments/{comment_id}`


#### Allowed for

  * Agents
  * The end user who created the comment


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
article_id| integer| Path| true| The unique ID of the article
comment_id| integer| Path| true| The unique ID of the comment

#### Code Samples

**Curl**


    curl --request DELETE https://support.zendesk.com/api/v2/help_center/articles/360026053753/comments/360004163994 \--header "Content-Type: application/json" \-u {email_address}/token:{api_token}

****


     curl https://{subdomain}.zendesk.com/api/v2/help_center/articles/{article_id}/comments/{comment_id} \  -v -u {email_address}/token:{api_token} -X DELETE

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/articles/360026053753/comments/360004163994"	method := "DELETE"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/articles/360026053753/comments/360004163994")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("DELETE", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'DELETE',  url: 'https://support.zendesk.com/api/v2/help_center/articles/360026053753/comments/360004163994',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/articles/360026053753/comments/360004163994"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"DELETE",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/articles/360026053753/comments/360004163994")request = Net::HTTP::Delete.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**204 No Content**


    // Status 204 No Content
    null

### Delete Article Comment by Locale

  * `DELETE /api/v2/help_center/{locale}/articles/{article_id}/comments/{comment_id}`


#### Allowed for

  * Agents
  * The end user who created the comment


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
article_id| integer| Path| true| The unique ID of the article
comment_id| integer| Path| true| The unique ID of the comment
locale| string| Path| true| The locale the item is displayed in

#### Code Samples

**Curl**


    curl --request DELETE https://support.zendesk.com/api/v2/help_center/en-us/articles/360026053753/comments/360004163994 \--header "Content-Type: application/json" \-u {email_address}/token:{api_token}

****


     curl https://{subdomain}.zendesk.com/api/v2/help_center/articles/{article_id}/comments/{comment_id}.json \  -v -u {email_address}/token:{api_token} -X DELETE

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/en-us/articles/360026053753/comments/360004163994"	method := "DELETE"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/en-us/articles/360026053753/comments/360004163994")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("DELETE", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'DELETE',  url: 'https://support.zendesk.com/api/v2/help_center/en-us/articles/360026053753/comments/360004163994',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/en-us/articles/360026053753/comments/360004163994"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"DELETE",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/en-us/articles/360026053753/comments/360004163994")request = Net::HTTP::Delete.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**204 No Content**


    // Status 204 No Content
    null

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)