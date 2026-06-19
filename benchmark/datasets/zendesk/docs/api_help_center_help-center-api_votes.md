# Votes

*Source: https://developer.zendesk.com/api-reference/help_center/help-center-api/votes/*

---

## On this page

  * [JSON format](/api-reference/help_center/help-center-api/votes/#json-format)
  * [List Post Comment Votes](/api-reference/help_center/help-center-api/votes/#list-post-comment-votes)
  * [List Post Votes](/api-reference/help_center/help-center-api/votes/#list-post-votes)
  * [List Article Comment Votes](/api-reference/help_center/help-center-api/votes/#list-article-comment-votes)
  * [List Article Votes](/api-reference/help_center/help-center-api/votes/#list-article-votes)
  * [List Votes by User](/api-reference/help_center/help-center-api/votes/#list-votes-by-user)
  * [Show Vote](/api-reference/help_center/help-center-api/votes/#show-vote)
  * [Downvote Post Comment](/api-reference/help_center/help-center-api/votes/#downvote-post-comment)
  * [Upvote Post Comment](/api-reference/help_center/help-center-api/votes/#upvote-post-comment)
  * [Downvote Post](/api-reference/help_center/help-center-api/votes/#downvote-post)
  * [Upvote Post](/api-reference/help_center/help-center-api/votes/#upvote-post)
  * [Downvote Article Comment](/api-reference/help_center/help-center-api/votes/#downvote-article-comment)
  * [Upvote Article Comment](/api-reference/help_center/help-center-api/votes/#upvote-article-comment)
  * [Downvote Article](/api-reference/help_center/help-center-api/votes/#downvote-article)
  * [Upvote Article](/api-reference/help_center/help-center-api/votes/#upvote-article)
  * [Create Vote](/api-reference/help_center/help-center-api/votes/#create-vote)
  * [Delete Vote](/api-reference/help_center/help-center-api/votes/#delete-vote)
  * [List All Votes](/api-reference/help_center/help-center-api/votes/#list-all-votes)
  * [List Article Comment Votes by Locale](/api-reference/help_center/help-center-api/votes/#list-article-comment-votes-by-locale)
  * [List Article Votes by Locale](/api-reference/help_center/help-center-api/votes/#list-article-votes-by-locale)


# Votes

## On this page

  * [JSON format](/api-reference/help_center/help-center-api/votes/#json-format)
  * [List Post Comment Votes](/api-reference/help_center/help-center-api/votes/#list-post-comment-votes)
  * [List Post Votes](/api-reference/help_center/help-center-api/votes/#list-post-votes)
  * [List Article Comment Votes](/api-reference/help_center/help-center-api/votes/#list-article-comment-votes)
  * [List Article Votes](/api-reference/help_center/help-center-api/votes/#list-article-votes)
  * [List Votes by User](/api-reference/help_center/help-center-api/votes/#list-votes-by-user)
  * [Show Vote](/api-reference/help_center/help-center-api/votes/#show-vote)
  * [Downvote Post Comment](/api-reference/help_center/help-center-api/votes/#downvote-post-comment)
  * [Upvote Post Comment](/api-reference/help_center/help-center-api/votes/#upvote-post-comment)
  * [Downvote Post](/api-reference/help_center/help-center-api/votes/#downvote-post)
  * [Upvote Post](/api-reference/help_center/help-center-api/votes/#upvote-post)
  * [Downvote Article Comment](/api-reference/help_center/help-center-api/votes/#downvote-article-comment)
  * [Upvote Article Comment](/api-reference/help_center/help-center-api/votes/#upvote-article-comment)
  * [Downvote Article](/api-reference/help_center/help-center-api/votes/#downvote-article)
  * [Upvote Article](/api-reference/help_center/help-center-api/votes/#upvote-article)
  * [Create Vote](/api-reference/help_center/help-center-api/votes/#create-vote)
  * [Delete Vote](/api-reference/help_center/help-center-api/votes/#delete-vote)
  * [List All Votes](/api-reference/help_center/help-center-api/votes/#list-all-votes)
  * [List Article Comment Votes by Locale](/api-reference/help_center/help-center-api/votes/#list-article-comment-votes-by-locale)
  * [List Article Votes by Locale](/api-reference/help_center/help-center-api/votes/#list-article-votes-by-locale)


Votes represents positive and negative opinions of users about [articles](/api-reference/help_center/help-center-api/articles), [article comments](/api-reference/help_center/help-center-api/article_comments), [posts](/api-reference/help_center/help-center-api/posts) or [post comments](/api-reference/help_center/help-center-api/post_comments).

### JSON format

Votes are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
created_at| string| true| false| The time at which the vote was created
id| integer| true| false| Automatically assigned when the vote is created
item_id| integer| true| false| The id of the item for which this vote was cast
item_type| string| true| false| The type of the item. Can be "Article", "Comment", "Post" or "PostComment"
updated_at| string| true| false| The time at which the vote was last updated
url| string| true| false| The API url of this vote
user_id| integer| true| false| The id of the user who cast this vote
value| integer| false| true| The value of the vote

#### Example


    {  "created_at": "2012-04-04T09:14:57Z",  "id": 1635,  "item_id": 65466,  "item_type": "Article",  "user_id": 3465,  "value": 1}

### List Post Comment Votes

  * `GET /api/v2/community/posts/{post_id}/comments/{comment_id}/votes`


Lists all votes cast by all users for a given [post comment](/api-reference/help_center/help-center-api/post_comments).

#### Allowed for

  * End users


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
translations| translations of any sideloaded articles
posts| posts
comments| comments

Note that you must sideload `articles` in order to sideload `translations`.

On requests to the `/api/v2/help_center/users/{user_id}/votes.json` endpoint, article comments must be sideloaded using `article_comments`. The `comments` sideload will only return community comments.

You can also use different URL to perform this operation

Resource| URL| Required parameters
---|---|---
Article| `/api/v2/help_center{/locale}/articles/{article_id}/votes`| `article_id`: The Id of the Article
Comment| `/api/v2/help_center{/locale}/articles/{article_id}/comments/{comment_id}/votes`| `article_id`: The Id of the Article, `comment_id`: The ID of the comment
Post| `/api/v2/help_center/posts/{post_id}/votes`| `post_id`: The Id of the Post
Post Comment| `/api/v2/community/posts/{post_id}/comments/{post_comment_id}/votes`| `post_id`: The Id of the Post, `post_comment_id`: The ID of the post comment

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
comment_id| integer| Path| true| The unique ID of the comment
post_id| integer| Path| true| The unique ID of the post

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/community/posts/{post_id}/comments/{comment_id}/votes \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/community/posts/360039436873/comments/360004163994/votes"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/community/posts/360039436873/comments/360004163994/votes")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/community/posts/360039436873/comments/360004163994/votes',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/community/posts/360039436873/comments/360004163994/votes"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/community/posts/360039436873/comments/360004163994/votes")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "votes": [    {      "id": 35467,      "user_id": 888887,      "value": -1    }  ]}

### List Post Votes

  * `GET /api/v2/community/posts/{post_id}/votes`


Lists all votes cast by all users for a given [post](/api-reference/help_center/help-center-api/posts).

#### Allowed for

  * End users


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
translations| translations of any sideloaded articles
posts| posts
comments| comments

Note that you must sideload `articles` in order to sideload `translations`.

On requests to the `/api/v2/help_center/users/{user_id}/votes.json` endpoint, article comments must be sideloaded using `article_comments`. The `comments` sideload will only return community comments.

You can also use different URL to perform this operation

Resource| URL| Required parameters
---|---|---
Article| `/api/v2/help_center{/locale}/articles/{article_id}/votes`| `article_id`: The Id of the Article
Comment| `/api/v2/help_center{/locale}/articles/{article_id}/comments/{comment_id}/votes`| `article_id`: The Id of the Article, `comment_id`: The ID of the comment
Post| `/api/v2/help_center/posts/{post_id}/votes`| `post_id`: The Id of the Post
Post Comment| `/api/v2/community/posts/{post_id}/comments/{post_comment_id}/votes`| `post_id`: The Id of the Post, `post_comment_id`: The ID of the post comment

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
post_id| integer| Path| true| The unique ID of the post

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/community/posts/{post_id}/votes \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/community/posts/360039436873/votes"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/community/posts/360039436873/votes")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/community/posts/360039436873/votes',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/community/posts/360039436873/votes"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/community/posts/360039436873/votes")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "votes": [    {      "id": 35467,      "user_id": 888887,      "value": -1    }  ]}

### List Article Comment Votes

  * `GET /api/v2/help_center/articles/{article_id}/comments/{comment_id}/votes`


Lists all votes cast by all users for a given [article comment](/api-reference/help_center/help-center-api/article_comments/).

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
translations| translations of any sideloaded articles
posts| posts
comments| comments

Note that you must sideload `articles` in order to sideload `translations`.

On requests to the `/api/v2/help_center/users/{user_id}/votes.json` endpoint, article comments must be sideloaded using `article_comments`. The `comments` sideload will only return community comments.

You can also use different URL to perform this operation

Resource| URL| Required parameters
---|---|---
Article| `/api/v2/help_center{/locale}/articles/{article_id}/votes`| `article_id`: The Id of the Article
Comment| `/api/v2/help_center{/locale}/articles/{article_id}/comments/{comment_id}/votes`| `article_id`: The Id of the Article, `comment_id`: The ID of the comment
Post| `/api/v2/help_center/posts/{post_id}/votes`| `post_id`: The Id of the Post
Post Comment| `/api/v2/community/posts/{post_id}/comments/{post_comment_id}/votes`| `post_id`: The Id of the Post, `post_comment_id`: The ID of the post comment

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
article_id| integer| Path| true| The unique ID of the article
comment_id| integer| Path| true| The unique ID of the comment

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/articles/{article_id}/comments/{comment_id}/votes \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/articles/360026053753/comments/360004163994/votes"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/articles/360026053753/comments/360004163994/votes")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/help_center/articles/360026053753/comments/360004163994/votes',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/articles/360026053753/comments/360004163994/votes"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/articles/360026053753/comments/360004163994/votes")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "votes": [    {      "id": 35467,      "user_id": 888887,      "value": -1    }  ]}

### List Article Votes

  * `GET /api/v2/help_center/articles/{article_id}/votes`


Lists all votes cast by all users for a given [article](/api-reference/help_center/help-center-api/articles).

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
translations| translations of any sideloaded articles
posts| posts
comments| comments

Note that you must sideload `articles` in order to sideload `translations`.

On requests to the `/api/v2/help_center/users/{user_id}/votes.json` endpoint, article comments must be sideloaded using `article_comments`. The `comments` sideload will only return community comments.

You can also use different URL to perform this operation

Resource| URL| Required parameters
---|---|---
Article| `/api/v2/help_center{/locale}/articles/{article_id}/votes`| `article_id`: The Id of the Article
Comment| `/api/v2/help_center{/locale}/articles/{article_id}/comments/{comment_id}/votes`| `article_id`: The Id of the Article, `comment_id`: The ID of the comment
Post| `/api/v2/help_center/posts/{post_id}/votes`| `post_id`: The Id of the Post
Post Comment| `/api/v2/community/posts/{post_id}/comments/{post_comment_id}/votes`| `post_id`: The Id of the Post, `post_comment_id`: The ID of the post comment

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
article_id| integer| Path| true| The unique ID of the article

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/articles/{article_id}/votes \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/articles/360026053753/votes"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/articles/360026053753/votes")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/help_center/articles/360026053753/votes',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/articles/360026053753/votes"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/articles/360026053753/votes")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "votes": [    {      "id": 35467,      "user_id": 888887,      "value": -1    }  ]}

### List Votes by User

  * `GET /api/v2/help_center/users/{user_id}/votes`


Lists all votes cast by a given user, or all votes cast by all users for a given article, article comment, post, or post comment.

To list only your own votes, specify `me` as the user id.

The `{locale}` for article and article comment votes is required only for end users. Admins and agents can omit it.

#### Allowed for

  * End users


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
translations| translations of any sideloaded articles
posts| posts
comments| comments

Note that you must sideload `articles` in order to sideload `translations`.

On requests to the `/api/v2/help_center/users/{user_id}/votes.json` endpoint, article comments must be sideloaded using `article_comments`. The `comments` sideload will only return community comments.

You can also use different URL to perform this operation

Resource| URL| Required parameters
---|---|---
Article| `/api/v2/help_center{/locale}/articles/{article_id}/votes`| `article_id`: The Id of the Article
Comment| `/api/v2/help_center{/locale}/articles/{article_id}/comments/{comment_id}/votes`| `article_id`: The Id of the Article, `comment_id`: The ID of the comment
Post| `/api/v2/help_center/posts/{post_id}/votes`| `post_id`: The Id of the Post
Post Comment| `/api/v2/community/posts/{post_id}/comments/{post_comment_id}/votes`| `post_id`: The Id of the Post, `post_comment_id`: The ID of the post comment

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
user_id| integer| Path| true| The unique ID of the user

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/users/{user_id}/votes.json \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/users/1234/votes"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/users/1234/votes")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/help_center/users/1234/votes',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/users/1234/votes"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/users/1234/votes")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "votes": [    {      "id": 35467,      "user_id": 888887,      "value": -1    }  ]}

### Show Vote

  * `GET /api/v2/help_center/votes/{vote_id}`


#### Allowed for

  * End users


#### Sideloads

The following sideloads are supported:

Name| Will sideload
---|---
users| authors
articles| articles
translations| translations of any sideloaded articles
posts| posts
comments| comments

Note that you must sideload `articles` in order to sideload `translations`.

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
vote_id| integer| Path| true| The unique ID of the vote

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/votes/{vote_id}.json \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/votes/35467"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/votes/35467")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/help_center/votes/35467',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/votes/35467"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/votes/35467")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "vote": {    "id": 35467,    "user_id": 888887,    "value": -1  }}

### Downvote Post Comment

  * `POST /api/v2/community/posts/{post_id}/comments/{comment_id}/down`


Creates a downvote for a given [post comment](/api-reference/help_center/help-center-api/post_comments). If a vote already exists for the post comment, it's updated.

#### Allowed for

  * End users


Agents with the Help Center manager role can optionally supply a `vote` object containing a `user_id` value. If provided, the vote will be cast by the user associated with `user_id`.

Agents with the Help Center manager role can also specify `created_at` as part of the `vote` object. If it is not provided `created_at` is set to the current time.

You can also use different URL to perform this operation, depending on the object you want to vote:

Resource| Vote| URL| Required parameters
---|---|---|---
Article| Down| `/api/v2/help_center/articles/{article_id}/down`| `article_id`: The Id of the Article
Comment| Up| `/api/v2/help_center/articles/{article_id}/comments/{comment_id}/up`| `article_id`: The Id of the Article, `comment_id`: The ID of the comment
Comment| Down| `/api/v2/help_center/articles/{article_id}/comments/{comment_id}/down`| `article_id`: The Id of the Article, `comment_id`: The ID of the comment
Post| Up| `/api/v2/help_center/posts/{post_id}/up`| `post_id`: The Id of the Post
Post| Down| `/api/v2/help_center/posts/{post_id}/down`| `post_id`: The Id of the Post
Post Comment| Up| `/api/v2/community/posts/{post_id}/comments/{post_comment_id}/up`| `post_id`: The Id of the Post, `post_comment_id`: The ID of the post comment
Post Comment| Down| `/api/v2/community/posts/{post_id}/comments/{post_comment_id}/down`| `post_id`: The Id of the Post, `post_comment_id`: The ID of the post comment

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
comment_id| integer| Path| true| The unique ID of the comment
post_id| integer| Path| true| The unique ID of the post

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/community/posts/{post_id}/comments/{comment_id}/down \  -v -u {email_address}/token:{api_token} -X POST -H "Content-Type: application/json"

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/community/posts/360039436873/comments/360004163994/down"	method := "POST"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/community/posts/360039436873/comments/360004163994/down")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'POST',  url: 'https://support.zendesk.com/api/v2/community/posts/360039436873/comments/360004163994/down',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/community/posts/360039436873/comments/360004163994/down"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/community/posts/360039436873/comments/360004163994/down")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "vote": {    "id": 37486578,    "value": 1  }}

### Upvote Post Comment

  * `POST /api/v2/community/posts/{post_id}/comments/{comment_id}/up`


Creates an upvote for a given [post comment](/api-reference/help_center/help-center-api/post_comments). If a vote already exists for the post comment, it's updated.

#### Allowed for

  * End users


Agents with the Help Center manager role can optionally supply a `vote` object containing a `user_id` value. If provided, the vote will be cast by the user associated with `user_id`.

Agents with the Help Center manager role can also specify `created_at` as part of the `vote` object. If it is not provided `created_at` is set to the current time.

You can also use different URL to perform this operation, depending on the object you want to vote:

Resource| Vote| URL| Required parameters
---|---|---|---
Article| Down| `/api/v2/help_center/articles/{article_id}/down`| `article_id`: The Id of the Article
Comment| Up| `/api/v2/help_center/articles/{article_id}/comments/{comment_id}/up`| `article_id`: The Id of the Article, `comment_id`: The ID of the comment
Comment| Down| `/api/v2/help_center/articles/{article_id}/comments/{comment_id}/down`| `article_id`: The Id of the Article, `comment_id`: The ID of the comment
Post| Up| `/api/v2/help_center/posts/{post_id}/up`| `post_id`: The Id of the Post
Post| Down| `/api/v2/help_center/posts/{post_id}/down`| `post_id`: The Id of the Post
Post Comment| Up| `/api/v2/community/posts/{post_id}/comments/{post_comment_id}/up`| `post_id`: The Id of the Post, `post_comment_id`: The ID of the post comment
Post Comment| Down| `/api/v2/community/posts/{post_id}/comments/{post_comment_id}/down`| `post_id`: The Id of the Post, `post_comment_id`: The ID of the post comment

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
comment_id| integer| Path| true| The unique ID of the comment
post_id| integer| Path| true| The unique ID of the post

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/community/posts/{post_id}/comments/{comment_id}/up \  -v -u {email_address}/token:{api_token} -X POST -H "Content-Type: application/json"

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/community/posts/360039436873/comments/360004163994/up"	method := "POST"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/community/posts/360039436873/comments/360004163994/up")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'POST',  url: 'https://support.zendesk.com/api/v2/community/posts/360039436873/comments/360004163994/up',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/community/posts/360039436873/comments/360004163994/up"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/community/posts/360039436873/comments/360004163994/up")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "vote": {    "id": 37486578,    "value": 1  }}

### Downvote Post

  * `POST /api/v2/community/posts/{post_id}/down`


Creates a downvote for a given [post](/api-reference/help_center/help-center-api/posts). If a vote already exists for the post, it's updated.

#### Allowed for

  * End users


Agents with the Help Center manager role can optionally supply a `vote` object containing a `user_id` value. If provided, the vote will be cast by the user associated with `user_id`.

Agents with the Help Center manager role can also specify `created_at` as part of the `vote` object. If it is not provided `created_at` is set to the current time.

You can also use different URL to perform this operation, depending on the object you want to vote:

Resource| Vote| URL| Required parameters
---|---|---|---
Article| Down| `/api/v2/help_center/articles/{article_id}/down`| `article_id`: The Id of the Article
Comment| Up| `/api/v2/help_center/articles/{article_id}/comments/{comment_id}/up`| `article_id`: The Id of the Article, `comment_id`: The ID of the comment
Comment| Down| `/api/v2/help_center/articles/{article_id}/comments/{comment_id}/down`| `article_id`: The Id of the Article, `comment_id`: The ID of the comment
Post| Up| `/api/v2/help_center/posts/{post_id}/up`| `post_id`: The Id of the Post
Post| Down| `/api/v2/help_center/posts/{post_id}/down`| `post_id`: The Id of the Post
Post Comment| Up| `/api/v2/community/posts/{post_id}/comments/{post_comment_id}/up`| `post_id`: The Id of the Post, `post_comment_id`: The ID of the post comment
Post Comment| Down| `/api/v2/community/posts/{post_id}/comments/{post_comment_id}/down`| `post_id`: The Id of the Post, `post_comment_id`: The ID of the post comment

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
post_id| integer| Path| true| The unique ID of the post

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/community/posts/{post_id}/down \  -v -u {email_address}/token:{api_token} -X POST -H "Content-Type: application/json"

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/community/posts/360039436873/down"	method := "POST"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/community/posts/360039436873/down")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'POST',  url: 'https://support.zendesk.com/api/v2/community/posts/360039436873/down',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/community/posts/360039436873/down"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/community/posts/360039436873/down")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "vote": {    "id": 37486578,    "value": 1  }}

### Upvote Post

  * `POST /api/v2/community/posts/{post_id}/up`


Creates an upvote for a given [post](/api-reference/help_center/help-center-api/posts). If a vote already exists for the post, it's updated.

#### Allowed for

  * End users


Agents with the Help Center manager role can optionally supply a `vote` object containing a `user_id` value. If provided, the vote will be cast by the user associated with `user_id`.

Agents with the Help Center manager role can also specify `created_at` as part of the `vote` object. If it is not provided `created_at` is set to the current time.

You can also use different URL to perform this operation, depending on the object you want to vote:

Resource| Vote| URL| Required parameters
---|---|---|---
Article| Down| `/api/v2/help_center/articles/{article_id}/down`| `article_id`: The Id of the Article
Comment| Up| `/api/v2/help_center/articles/{article_id}/comments/{comment_id}/up`| `article_id`: The Id of the Article, `comment_id`: The ID of the comment
Comment| Down| `/api/v2/help_center/articles/{article_id}/comments/{comment_id}/down`| `article_id`: The Id of the Article, `comment_id`: The ID of the comment
Post| Up| `/api/v2/help_center/posts/{post_id}/up`| `post_id`: The Id of the Post
Post| Down| `/api/v2/help_center/posts/{post_id}/down`| `post_id`: The Id of the Post
Post Comment| Up| `/api/v2/community/posts/{post_id}/comments/{post_comment_id}/up`| `post_id`: The Id of the Post, `post_comment_id`: The ID of the post comment
Post Comment| Down| `/api/v2/community/posts/{post_id}/comments/{post_comment_id}/down`| `post_id`: The Id of the Post, `post_comment_id`: The ID of the post comment

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
post_id| integer| Path| true| The unique ID of the post

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/community/posts/{post_id}/up \  -v -u {email_address}/token:{api_token} -X POST -H "Content-Type: application/json"

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/community/posts/360039436873/up"	method := "POST"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/community/posts/360039436873/up")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'POST',  url: 'https://support.zendesk.com/api/v2/community/posts/360039436873/up',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/community/posts/360039436873/up"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/community/posts/360039436873/up")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "vote": {    "id": 37486578,    "value": 1  }}

### Downvote Article Comment

  * `POST /api/v2/help_center/articles/{article_id}/comments/{comment_id}/down`


Creates a downvote for a given [article comment](/api-reference/help_center/help-center-api/article_comments/). If a vote already exists for the article comment, it's updated.

#### Allowed for

  * End users


Agents with the Help Center manager role can optionally supply a `vote` object containing a `user_id` value. If provided, the vote will be cast by the user associated with `user_id`.

Agents with the Help Center manager role can also specify `created_at` as part of the `vote` object. If it is not provided `created_at` is set to the current time.

You can also use different URL to perform this operation, depending on the object you want to vote:

Resource| Vote| URL| Required parameters
---|---|---|---
Article| Down| `/api/v2/help_center/articles/{article_id}/down`| `article_id`: The Id of the Article
Comment| Up| `/api/v2/help_center/articles/{article_id}/comments/{comment_id}/up`| `article_id`: The Id of the Article, `comment_id`: The ID of the comment
Comment| Down| `/api/v2/help_center/articles/{article_id}/comments/{comment_id}/down`| `article_id`: The Id of the Article, `comment_id`: The ID of the comment
Post| Up| `/api/v2/help_center/posts/{post_id}/up`| `post_id`: The Id of the Post
Post| Down| `/api/v2/help_center/posts/{post_id}/down`| `post_id`: The Id of the Post
Post Comment| Up| `/api/v2/community/posts/{post_id}/comments/{post_comment_id}/up`| `post_id`: The Id of the Post, `post_comment_id`: The ID of the post comment
Post Comment| Down| `/api/v2/community/posts/{post_id}/comments/{post_comment_id}/down`| `post_id`: The Id of the Post, `post_comment_id`: The ID of the post comment

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
article_id| integer| Path| true| The unique ID of the article
comment_id| integer| Path| true| The unique ID of the comment

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/articles/{article_id}/comments/{comment_id}/down \  -v -u {email_address}/token:{api_token} -X POST -H "Content-Type: application/json"

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/articles/360026053753/comments/360004163994/down"	method := "POST"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/articles/360026053753/comments/360004163994/down")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'POST',  url: 'https://support.zendesk.com/api/v2/help_center/articles/360026053753/comments/360004163994/down',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/articles/360026053753/comments/360004163994/down"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/articles/360026053753/comments/360004163994/down")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "vote": {    "id": 37486578,    "value": 1  }}

### Upvote Article Comment

  * `POST /api/v2/help_center/articles/{article_id}/comments/{comment_id}/up`


Creates an upvote for a given [article comment](/api-reference/help_center/help-center-api/article_comments/). If a vote already exists for the article comment, it's updated.

#### Allowed for

  * End users


Agents with the Help Center manager role can optionally supply a `vote` object containing a `user_id` value. If provided, the vote will be cast by the user associated with `user_id`.

Agents with the Help Center manager role can also specify `created_at` as part of the `vote` object. If it is not provided `created_at` is set to the current time.

You can also use different URL to perform this operation, depending on the object you want to vote:

Resource| Vote| URL| Required parameters
---|---|---|---
Article| Down| `/api/v2/help_center/articles/{article_id}/down`| `article_id`: The Id of the Article
Comment| Up| `/api/v2/help_center/articles/{article_id}/comments/{comment_id}/up`| `article_id`: The Id of the Article, `comment_id`: The ID of the comment
Comment| Down| `/api/v2/help_center/articles/{article_id}/comments/{comment_id}/down`| `article_id`: The Id of the Article, `comment_id`: The ID of the comment
Post| Up| `/api/v2/help_center/posts/{post_id}/up`| `post_id`: The Id of the Post
Post| Down| `/api/v2/help_center/posts/{post_id}/down`| `post_id`: The Id of the Post
Post Comment| Up| `/api/v2/community/posts/{post_id}/comments/{post_comment_id}/up`| `post_id`: The Id of the Post, `post_comment_id`: The ID of the post comment
Post Comment| Down| `/api/v2/community/posts/{post_id}/comments/{post_comment_id}/down`| `post_id`: The Id of the Post, `post_comment_id`: The ID of the post comment

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
article_id| integer| Path| true| The unique ID of the article
comment_id| integer| Path| true| The unique ID of the comment

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/articles/{article_id}/comments/{comment_id}/up \  -v -u {email_address}/token:{api_token} -X POST -H "Content-Type: application/json"

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/articles/360026053753/comments/360004163994/up"	method := "POST"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/articles/360026053753/comments/360004163994/up")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'POST',  url: 'https://support.zendesk.com/api/v2/help_center/articles/360026053753/comments/360004163994/up',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/articles/360026053753/comments/360004163994/up"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/articles/360026053753/comments/360004163994/up")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "vote": {    "id": 37486578,    "value": 1  }}

### Downvote Article

  * `POST /api/v2/help_center/articles/{article_id}/down`


Creates a downvote for a given [article](/api-reference/help_center/help-center-api/articles). If a vote already exists for the article, it's updated.

#### Allowed for

  * End users


Agents with the Help Center manager role can optionally supply a `vote` object containing a `user_id` value. If provided, the vote will be cast by the user associated with `user_id`.

Agents with the Help Center manager role can also specify `created_at` as part of the `vote` object. If it is not provided `created_at` is set to the current time.

You can also use different URL to perform this operation, depending on the object you want to vote:

Resource| Vote| URL| Required parameters
---|---|---|---
Article| Down| `/api/v2/help_center/articles/{article_id}/down`| `article_id`: The Id of the Article
Comment| Up| `/api/v2/help_center/articles/{article_id}/comments/{comment_id}/up`| `article_id`: The Id of the Article, `comment_id`: The ID of the comment
Comment| Down| `/api/v2/help_center/articles/{article_id}/comments/{comment_id}/down`| `article_id`: The Id of the Article, `comment_id`: The ID of the comment
Post| Up| `/api/v2/help_center/posts/{post_id}/up`| `post_id`: The Id of the Post
Post| Down| `/api/v2/help_center/posts/{post_id}/down`| `post_id`: The Id of the Post
Post Comment| Up| `/api/v2/community/posts/{post_id}/comments/{post_comment_id}/up`| `post_id`: The Id of the Post, `post_comment_id`: The ID of the post comment
Post Comment| Down| `/api/v2/community/posts/{post_id}/comments/{post_comment_id}/down`| `post_id`: The Id of the Post, `post_comment_id`: The ID of the post comment

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
article_id| integer| Path| true| The unique ID of the article

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/articles/{article_id}/down \  -v -u {email_address}/token:{api_token} -X POST -H "Content-Type: application/json"

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/articles/360026053753/down"	method := "POST"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/articles/360026053753/down")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'POST',  url: 'https://support.zendesk.com/api/v2/help_center/articles/360026053753/down',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/articles/360026053753/down"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/articles/360026053753/down")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "vote": {    "id": 37486578,    "value": 1  }}

### Upvote Article

  * `POST /api/v2/help_center/articles/{article_id}/up`


Creates an upvote for a given [article](/api-reference/help_center/help-center-api/articles). If a vote already exists for the article, it's updated.

#### Allowed for

  * End users


Agents with the Help Center manager role can optionally supply a `vote` object containing a `user_id` value. If provided, the vote will be cast by the user associated with `user_id`.

Agents with the Help Center manager role can also specify `created_at` as part of the `vote` object. If it is not provided `created_at` is set to the current time.

You can also use different URL to perform this operation, depending on the object you want to vote:

Resource| Vote| URL| Required parameters
---|---|---|---
Article| Down| `/api/v2/help_center/articles/{article_id}/down`| `article_id`: The Id of the Article
Comment| Up| `/api/v2/help_center/articles/{article_id}/comments/{comment_id}/up`| `article_id`: The Id of the Article, `comment_id`: The ID of the comment
Comment| Down| `/api/v2/help_center/articles/{article_id}/comments/{comment_id}/down`| `article_id`: The Id of the Article, `comment_id`: The ID of the comment
Post| Up| `/api/v2/help_center/posts/{post_id}/up`| `post_id`: The Id of the Post
Post| Down| `/api/v2/help_center/posts/{post_id}/down`| `post_id`: The Id of the Post
Post Comment| Up| `/api/v2/community/posts/{post_id}/comments/{post_comment_id}/up`| `post_id`: The Id of the Post, `post_comment_id`: The ID of the post comment
Post Comment| Down| `/api/v2/community/posts/{post_id}/comments/{post_comment_id}/down`| `post_id`: The Id of the Post, `post_comment_id`: The ID of the post comment

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
article_id| integer| Path| true| The unique ID of the article

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/articles/{article_id}/up \  -v -u {email_address}/token:{api_token} -X POST -H "Content-Type: application/json"

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/articles/360026053753/up"	method := "POST"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/articles/360026053753/up")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'POST',  url: 'https://support.zendesk.com/api/v2/help_center/articles/360026053753/up',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/articles/360026053753/up"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/articles/360026053753/up")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "vote": {    "id": 37486578,    "value": 1  }}

### Create Vote

  * `POST /api/v2/help_center/{locale}/articles/{article_id}/up`


Creates an up or down vote for a given [article](/api-reference/help_center/help-center-api/articles), [article comment](/api-reference/help_center/help-center-api/article_comments/), [post](/api-reference/help_center/help-center-api/posts), or [post comment](/api-reference/help_center/help-center-api/post_comments). If a vote already exists for the source object, it's updated.

#### Allowed for

  * End users


Agents with the Help Center manager role can optionally supply a `vote` object containing a `user_id` value. If provided, the vote will be cast by the user associated with `user_id`.

Agents with the Help Center manager role can also specify `created_at` as part of the `vote` object. If it is not provided `created_at` is set to the current time.

You can also use different URL to perform this operation, depending on the object you want to vote:

Resource| Vote| URL| Required parameters
---|---|---|---
Article| Down| `/api/v2/help_center/articles/{article_id}/down`| `article_id`: The Id of the Article
Comment| Up| `/api/v2/help_center/articles/{article_id}/comments/{comment_id}/up`| `article_id`: The Id of the Article, `comment_id`: The ID of the comment
Comment| Down| `/api/v2/help_center/articles/{article_id}/comments/{comment_id}/down`| `article_id`: The Id of the Article, `comment_id`: The ID of the comment
Post| Up| `/api/v2/help_center/posts/{post_id}/up`| `post_id`: The Id of the Post
Post| Down| `/api/v2/help_center/posts/{post_id}/down`| `post_id`: The Id of the Post
Post Comment| Up| `/api/v2/community/posts/{post_id}/comments/{post_comment_id}/up`| `post_id`: The Id of the Post, `post_comment_id`: The ID of the post comment
Post Comment| Down| `/api/v2/community/posts/{post_id}/comments/{post_comment_id}/down`| `post_id`: The Id of the Post, `post_comment_id`: The ID of the post comment

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
article_id| integer| Path| true| The unique ID of the article
locale| string| Path| true| The locale the item is displayed in

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/articles/{article_id}/up.json \  -v -u {email_address}/token:{api_token} -X POST -H "Content-Type: application/json"
    curl https://{subdomain}.zendesk.com/api/v2/help_center/articles/{article_id}/comments/{comment_id}/up.json \  -v -u {email_address}/token:{api_token} -X POST -H "Content-Type: application/json"
    curl https://{subdomain}.zendesk.com/api/v2/community/posts/{post_id}/up.json \  -v -u {email_address}/token:{api_token} -X POST -H "Content-Type: application/json"
    curl https://{subdomain}.zendesk.com/api/v2/community/posts/{post_id}/comments/{post_comment_id}/up.json \  -v -u {email_address}/token:{api_token} -X POST -H "Content-Type: application/json"
    curl https://{subdomain}.zendesk.com/api/v2/help_center/articles/{article_id}/down.json \  -d '{"vote": {"user_id": 10056}}' \  -v -u {email_address}/token:{api_token} -X POST -H "Content-Type: application/json"
    curl https://{subdomain}.zendesk.com/api/v2/community/posts/{post_id}/down.json \  -d '{"vote": {"user_id": 10056}}' \  -v -u {email_address}/token:{api_token} -X POST -H "Content-Type: application/json"
    curl https://{subdomain}.zendesk.com/api/v2/community/posts/{post_id}/comments/{post_comment_id}/down.json \  -d '{"vote": {"user_id": 10056}}' \  -v -u {email_address}/token:{api_token} -X POST -H "Content-Type: application/json"

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/en-us/articles/360026053753/up"	method := "POST"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/en-us/articles/360026053753/up")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'POST',  url: 'https://support.zendesk.com/api/v2/help_center/en-us/articles/360026053753/up',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/en-us/articles/360026053753/up"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/en-us/articles/360026053753/up")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "vote": {    "id": 37486578,    "value": 1  }}

### Delete Vote

  * `DELETE /api/v2/help_center/votes/{vote_id}`


#### Allowed for

  * End users


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
vote_id| integer| Path| true| The unique ID of the vote

#### Code Samples

**Curl**


    curl --request DELETE https://support.zendesk.com/api/v2/help_center/votes/35467 \--header "Content-Type: application/json" \-u {email_address}/token:{api_token}

****


     curl https://{subdomain}.zendesk.com/api/v2/help_center/votes/{vote_id}.json \  -v -u {email_address}/token:{api_token} -X DELETE

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/votes/35467"	method := "DELETE"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/votes/35467")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("DELETE", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'DELETE',  url: 'https://support.zendesk.com/api/v2/help_center/votes/35467',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/votes/35467"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"DELETE",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/votes/35467")request = Net::HTTP::Delete.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**204 No Content**


    // Status 204 No Content
    null

### List All Votes

  * `GET /api/v2/help_center/votes`


Lists all votes.

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
translations| translations of any sideloaded articles
posts| posts
comments| comments

Note that you must sideload `articles` in order to sideload `translations`.

On requests to the `/api/v2/help_center/users/{user_id}/votes.json` endpoint, article comments must be sideloaded using `article_comments`. The `comments` sideload will only return community comments.

You can also use different URL to perform this operation

Resource| URL| Required parameters
---|---|---
Article| `/api/v2/help_center{/locale}/articles/{article_id}/votes`| `article_id`: The Id of the Article
Comment| `/api/v2/help_center{/locale}/articles/{article_id}/comments/{comment_id}/votes`| `article_id`: The Id of the Article, `comment_id`: The ID of the comment
Post| `/api/v2/help_center/posts/{post_id}/votes`| `post_id`: The Id of the Post
Post Comment| `/api/v2/community/posts/{post_id}/comments/{post_comment_id}/votes`| `post_id`: The Id of the Post, `post_comment_id`: The ID of the post comment

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/votes \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/votes"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/votes")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/help_center/votes',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/votes"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/votes")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "votes": [    {      "id": 35467,      "user_id": 888887,      "value": -1    }  ]}

### List Article Comment Votes by Locale

  * `GET /api/v2/help_center/{locale}/articles/{article_id}/comments/{comment_id}/votes`


Lists all votes cast by all users for a given [article comment](/api-reference/help_center/help-center-api/article_comments/).

The `{locale}` is required only for end users. Admins and agents can omit it.

#### Allowed for

  * End users


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
translations| translations of any sideloaded articles
posts| posts
comments| comments

Note that you must sideload `articles` in order to sideload `translations`.

On requests to the `/api/v2/help_center/users/{user_id}/votes.json` endpoint, article comments must be sideloaded using `article_comments`. The `comments` sideload will only return community comments.

You can also use different URL to perform this operation

Resource| URL| Required parameters
---|---|---
Article| `/api/v2/help_center{/locale}/articles/{article_id}/votes`| `article_id`: The Id of the Article
Comment| `/api/v2/help_center{/locale}/articles/{article_id}/comments/{comment_id}/votes`| `article_id`: The Id of the Article, `comment_id`: The ID of the comment
Post| `/api/v2/help_center/posts/{post_id}/votes`| `post_id`: The Id of the Post
Post Comment| `/api/v2/community/posts/{post_id}/comments/{post_comment_id}/votes`| `post_id`: The Id of the Post, `post_comment_id`: The ID of the post comment

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
article_id| integer| Path| true| The unique ID of the article
comment_id| integer| Path| true| The unique ID of the comment
locale| string| Path| true| The locale the item is displayed in

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/{locale}/articles/{article_id}/comments/{comment_id}/votes \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/en-us/articles/360026053753/comments/360004163994/votes"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/en-us/articles/360026053753/comments/360004163994/votes")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/help_center/en-us/articles/360026053753/comments/360004163994/votes',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/en-us/articles/360026053753/comments/360004163994/votes"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/en-us/articles/360026053753/comments/360004163994/votes")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "votes": [    {      "id": 35467,      "user_id": 888887,      "value": -1    }  ]}

### List Article Votes by Locale

  * `GET /api/v2/help_center/{locale}/articles/{article_id}/votes`


Lists all votes cast by all users for a given article.

The `{locale}` is required only for end users. Admins and agents can omit it.

#### Allowed for

  * End users


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
translations| translations of any sideloaded articles
posts| posts
comments| comments

Note that you must sideload `articles` in order to sideload `translations`.

On requests to the `/api/v2/help_center/users/{user_id}/votes.json` endpoint, article comments must be sideloaded using `article_comments`. The `comments` sideload will only return community comments.

You can also use different URL to perform this operation

Resource| URL| Required parameters
---|---|---
Article| `/api/v2/help_center{/locale}/articles/{article_id}/votes`| `article_id`: The Id of the Article
Comment| `/api/v2/help_center{/locale}/articles/{article_id}/comments/{comment_id}/votes`| `article_id`: The Id of the Article, `comment_id`: The ID of the comment
Post| `/api/v2/help_center/posts/{post_id}/votes`| `post_id`: The Id of the Post
Post Comment| `/api/v2/community/posts/{post_id}/comments/{post_comment_id}/votes`| `post_id`: The Id of the Post, `post_comment_id`: The ID of the post comment

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
article_id| integer| Path| true| The unique ID of the article
locale| string| Path| true| The locale the item is displayed in

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/{locale}/articles/{article_id}/votes \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/en-us/articles/360026053753/votes"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/en-us/articles/360026053753/votes")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/help_center/en-us/articles/360026053753/votes',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/en-us/articles/360026053753/votes"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/en-us/articles/360026053753/votes")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "votes": [    {      "id": 35467,      "user_id": 888887,      "value": -1    }  ]}

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)