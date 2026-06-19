# Posts

*Source: https://developer.zendesk.com/api-reference/help_center/help-center-api/posts/*

---

## On this page

  * [JSON format](/api-reference/help_center/help-center-api/posts/#json-format)
  * [List Posts](/api-reference/help_center/help-center-api/posts/#list-posts)
  * [Show Post](/api-reference/help_center/help-center-api/posts/#show-post)
  * [Create Post](/api-reference/help_center/help-center-api/posts/#create-post)
  * [Update Post](/api-reference/help_center/help-center-api/posts/#update-post)
  * [Delete Post](/api-reference/help_center/help-center-api/posts/#delete-post)
  * [List Posts in Topic](/api-reference/help_center/help-center-api/posts/#list-posts-in-topic)
  * [List Posts by User](/api-reference/help_center/help-center-api/posts/#list-posts-by-user)


# Posts

## On this page

  * [JSON format](/api-reference/help_center/help-center-api/posts/#json-format)
  * [List Posts](/api-reference/help_center/help-center-api/posts/#list-posts)
  * [Show Post](/api-reference/help_center/help-center-api/posts/#show-post)
  * [Create Post](/api-reference/help_center/help-center-api/posts/#create-post)
  * [Update Post](/api-reference/help_center/help-center-api/posts/#update-post)
  * [Delete Post](/api-reference/help_center/help-center-api/posts/#delete-post)
  * [List Posts in Topic](/api-reference/help_center/help-center-api/posts/#list-posts-in-topic)
  * [List Posts by User](/api-reference/help_center/help-center-api/posts/#list-posts-by-user)


A post represents content that a user shares with the community.

### JSON format

Posts are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
author_id| integer| true| false| The id of the author of the post. *Writable on create by Help Center managers -- see Create Post
closed| boolean| false| false| Whether further comments are allowed
comment_count| integer| true| false| The number of comments on the post
content_tag_ids| array| false| false| The list of content tags attached to the post
created_at| string| true| false| When the post was created. Writable on create by Help Center managers -- see Create Post
details| string| false| false| The details of the post made by the author. See User content
featured| boolean| false| false| Whether the post is featured
follower_count| integer| true| false| The number of followers of the post
html_url| string| true| false| The community url of the post
id| integer| true| false| Automatically assigned when the post is created
non_author_editor_id| integer| true| false| The user id of whoever performed the most recent (if any) non-author edit. A non-author edit consists of an edit make by a user other than the author that creates or updates the `title` or `details`. Note that only edits made after May 17, 2021 will be reflected in this field. If no non-author edits have occured since May 17, 2021, then this field will be `null`.
non_author_updated_at| string| true| false| When the post was last edited by a non-author user
pinned| boolean| false| false| When true, pins the post to the top of its topic
status| string| false| false| The status of the post. Possible values: "planned", "not_planned" , "answered", or "completed"
title| string| false| true| The title of the post
topic_id| integer| false| false| The id of the topic that the post belongs to
updated_at| string| true| false| When the post was last updated
url| string| true| false| The API url of the post
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


    {  "author_id": 3465,  "featured": true,  "id": 1635,  "title": "The post"}

### List Posts

  * `GET /api/v2/community/posts`


Lists all posts, all posts in a given [topic](/api-reference/help_center/help-center-api/topics), or all posts by a specific user. When listing by specific user, the posts of the user making the request can be listed by specifying `me` as the id.

#### Allowed for

  * Anonymous users


#### Pagination

  * Cursor pagination (recommended)
  * Offset pagination


See [Pagination](/api-reference/introduction/pagination/).

#### Filtering

You can filter the results with the `filter_by` query string parameter.


    GET /api/v2/community/posts.json?filter_by=completed

The `filter_by` parameter can have one of the following values:

value| description
---|---
`planned`| list only posts with a status of 'Planned'
`not_planned`| list only posts with a status of 'Not planned'
`completed`| list only posts with a status of 'Completed'
`answered`| list only posts with a status of 'Answered'
`none`| list only posts with a status of 'None'

#### Sorting

You can sort the results with the `sort_by` query string parameter.


    GET /api/v2/community/posts.json?sort_by=comments

The `sort_by` parameter can have one of the following values:

value| description
---|---
`created_at`| order by creation time. Default order
`edited_at`| order by last edit time
`updated_at`| order by last update time
`recent_activity`| order by recent activity on the post
`votes`| order by vote sum
`comments`| order by comment count

#### Sideloads

You can sideload related records with the `include` query string parameter. The following sideloads are supported:

Name| Will sideload
---|---
users| authors
topics| topics

See [Sideloading related records](/documentation/developer-tools/working-with-data/sideloading-related-records).

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
filter_by| string| Query| false| Filter the results using the provided value. Allowed values are "planned", "not_planned", "completed", "answered", or "none".
sort_by| string| Query| false| Sorts the results using the provided value. Allowed values are "created_at", "edited_at", "updated_at", "recent_activity", "votes", or "comments".

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/community/users/{user_id}/posts.json \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/community/posts?filter_by=&sort_by="	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/community/posts")		.newBuilder()		.addQueryParameter("filter_by", "")		.addQueryParameter("sort_by", "");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/community/posts',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'filter_by': '',    'sort_by': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/community/posts?filter_by=&sort_by="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/community/posts")uri.query = URI.encode_www_form("filter_by": "", "sort_by": "")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "posts": [    {      "id": 35467,      "title": "How do I open the safe"    }  ]}

### Show Post

  * `GET /api/v2/community/posts/{post_id}`


Gets information about a given post.

#### Allowed for

  * Anonymous users


#### Sideloads

The following sideloads are supported:

Name| Will sideload
---|---
users| authors
topics| topics

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
post_id| integer| Path| true| The unique ID of the post

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/community/posts/{post_id}.json \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/community/posts/360039436873"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/community/posts/360039436873")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/community/posts/360039436873',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/community/posts/360039436873"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/community/posts/360039436873")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "post": {    "author_id": 888887,    "content_tag_ids": [      6776,      4545    ],    "featured": true,    "id": 35467,    "title": "Post title"  }}

### Create Post

  * `POST /api/v2/community/posts`


Adds a post to the specified [topic](/api-reference/help_center/help-center-api/topics).

#### Allowed for

  * End users


Agents with the Help Center manager role can optionally supply an `author_id` as part of the `post` object. If it is provided, the post's author will be set to the value of the `author_id` key.

Agents with the Help Center manager role can optionally supply a `created_at` as part of the `post` object. If it is not provided `created_at` is set to the current time.

Supplying a `notify_subscribers` property with a value of false will prevent subscribers to the post's topic from receiving a post creation email notification. This can be helpful when creating many posts at a time. Specify the property in the root of the JSON object, not in the "post" object. Optionally, you can attach existing [content tags](/api-reference/help_center/help-center-api/content_tags) by specifying their ids.

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/community/posts.json \  -d '{"post": {"title": "Help!", "details": "My printer is on fire!", "topic_id": 10046}, "notify_subscribers": false}' \-v -u {email_address}/token:{api_token} -X POST -H "Content-Type: application/json"
    # Setting the post's author:curl https://{subdomain}.zendesk.com/api/v2/community/posts.json \  -d '{"post": {"title": "Help!", "details": "My printer is on fire!", "author_id": 10056, "topic_id": 10046}}' \  -v -u {email_address}/token:{api_token} -X POST -H "Content-Type: application/json"
    # Attaching content tags to the post:curl https://{subdomain}.zendesk.com/api/v2/community/posts.json \  -d '{"post": {"title": "Help!", "details": "My printer is on fire!", "author_id": 10056, "topic_id": 10046, "content_tag_ids": [6776, 4545]}}' \  -v -u {email_address}/token:{api_token} -X POST -H "Content-Type: application/json"

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/community/posts"	method := "POST"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/community/posts")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'POST',  url: 'https://support.zendesk.com/api/v2/community/posts',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/community/posts"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/community/posts")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**201 Created**


    // Status 201 Created
    {  "post": {    "author_id": 888887,    "content_tag_ids": [      6776,      4545    ],    "featured": true,    "id": 35467,    "title": "Post title"  }}

### Update Post

  * `PUT /api/v2/community/posts/{post_id}`


#### Allowed for

  * Agents
  * The end user who created the post


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
post_id| integer| Path| true| The unique ID of the post

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/community/posts/{post_id}.json \  -d '{"post": {"title": "Help!", "details": "My printer is on fire!", "topic_id": 10046}}' \  -v -u {email_address}/token:{api_token} -X PUT -H "Content-Type: application/json"

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/community/posts/360039436873"	method := "PUT"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/community/posts/360039436873")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'PUT',  url: 'https://support.zendesk.com/api/v2/community/posts/360039436873',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/community/posts/360039436873"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/community/posts/360039436873")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "post": {    "author_id": 888887,    "content_tag_ids": [      6776,      4545    ],    "featured": true,    "id": 35467,    "title": "Post title"  }}

### Delete Post

  * `DELETE /api/v2/community/posts/{post_id}`


#### Allowed for

  * Agents
  * The end user who created the post


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
post_id| integer| Path| true| The unique ID of the post

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/community/posts/{post_id}.json \  -v -u {email_address}/token:{api_token} -X DELETE

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/community/posts/360039436873"	method := "DELETE"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/community/posts/360039436873")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("DELETE", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'DELETE',  url: 'https://support.zendesk.com/api/v2/community/posts/360039436873',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/community/posts/360039436873"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"DELETE",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/community/posts/360039436873")request = Net::HTTP::Delete.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**204 No Content**


    // Status 204 No Content
    null

### List Posts in Topic

  * `GET /api/v2/community/topics/{topic_id}/posts`


Lists all posts, all posts in a given [topic](/api-reference/help_center/help-center-api/topics), or all posts by a specific user. When listing by specific user, the posts of the user making the request can be listed by specifying `me` as the id.

#### Allowed for

  * Anonymous users


#### Pagination

  * Cursor pagination (recommended)
  * Offset pagination


See [Pagination](/api-reference/introduction/pagination/).

#### Filtering

You can filter the results with the `filter_by` query string parameter.


    GET /api/v2/community/posts.json?filter_by=completed

The `filter_by` parameter can have one of the following values:

value| description
---|---
`planned`| list only posts with a status of 'Planned'
`not_planned`| list only posts with a status of 'Not planned'
`completed`| list only posts with a status of 'Completed'
`answered`| list only posts with a status of 'Answered'
`none`| list only posts with a status of 'None'

#### Sorting

You can sort the results with the `sort_by` query string parameter.


    GET /api/v2/community/posts.json?sort_by=comments

The `sort_by` parameter can have one of the following values:

value| description
---|---
`created_at`| order by creation time. Default order
`edited_at`| order by last edit time
`updated_at`| order by last update time
`recent_activity`| order by recent activity on the post
`votes`| order by vote sum
`comments`| order by comment count

#### Sideloads

You can sideload related records with the `include` query string parameter. The following sideloads are supported:

Name| Will sideload
---|---
users| authors
topics| topics

See [Sideloading related records](/documentation/developer-tools/working-with-data/sideloading-related-records).

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
filter_by| string| Query| false| Filter the results using the provided value. Allowed values are "planned", "not_planned", "completed", "answered", or "none".
sort_by| string| Query| false| Sorts the results using the provided value. Allowed values are "created_at", "edited_at", "updated_at", "recent_activity", "votes", or "comments".
topic_id| integer| Path| true| The unique ID of the topic

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/community/topics/{topic_id}/posts.json \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/community/topics/360001326113/posts?filter_by=&sort_by="	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/community/topics/360001326113/posts")		.newBuilder()		.addQueryParameter("filter_by", "")		.addQueryParameter("sort_by", "");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/community/topics/360001326113/posts',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'filter_by': '',    'sort_by': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/community/topics/360001326113/posts?filter_by=&sort_by="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/community/topics/360001326113/posts")uri.query = URI.encode_www_form("filter_by": "", "sort_by": "")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "posts": [    {      "id": 35467,      "title": "How do I open the safe"    }  ]}

### List Posts by User

  * `GET /api/v2/community/users/{user_id}/posts`


Lists all posts, all posts in a given [topic](/api-reference/help_center/help-center-api/topics), or all posts by a specific user. When listing by specific user, the posts of the user making the request can be listed by specifying `me` as the id.

#### Allowed for

  * Anonymous users


#### Pagination

  * Cursor pagination (recommended)
  * Offset pagination


See [Pagination](/api-reference/introduction/pagination/).

#### Filtering

You can filter the results with the `filter_by` query string parameter.


    GET /api/v2/community/posts.json?filter_by=completed

The `filter_by` parameter can have one of the following values:

value| description
---|---
`planned`| list only posts with a status of 'Planned'
`not_planned`| list only posts with a status of 'Not planned'
`completed`| list only posts with a status of 'Completed'
`answered`| list only posts with a status of 'Answered'
`none`| list only posts with a status of 'None'

#### Sorting

You can sort the results with the `sort_by` query string parameter.


    GET /api/v2/community/posts.json?sort_by=comments

The `sort_by` parameter can have one of the following values:

value| description
---|---
`created_at`| order by creation time. Default order
`edited_at`| order by last edit time
`updated_at`| order by last update time
`recent_activity`| order by recent activity on the post
`votes`| order by vote sum
`comments`| order by comment count

#### Sideloads

You can sideload related records with the `include` query string parameter. The following sideloads are supported:

Name| Will sideload
---|---
users| authors
topics| topics

See [Sideloading related records](/documentation/developer-tools/working-with-data/sideloading-related-records).

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
filter_by| string| Query| false| Filter the results using the provided value. Allowed values are "planned", "not_planned", "completed", "answered", or "none".
sort_by| string| Query| false| Sorts the results using the provided value. Allowed values are "created_at", "edited_at", "updated_at", "recent_activity", "votes", or "comments".
user_id| integer| Path| true| The unique ID of the user

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/community/users/{user_id}/posts.json \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/community/users/1234/posts?filter_by=&sort_by="	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/community/users/1234/posts")		.newBuilder()		.addQueryParameter("filter_by", "")		.addQueryParameter("sort_by", "");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/community/users/1234/posts',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'filter_by': '',    'sort_by': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/community/users/1234/posts?filter_by=&sort_by="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/community/users/1234/posts")uri.query = URI.encode_www_form("filter_by": "", "sort_by": "")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "posts": [    {      "id": 35467,      "title": "How do I open the safe"    }  ]}

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)