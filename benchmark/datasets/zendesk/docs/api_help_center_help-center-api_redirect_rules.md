# Redirect Rules

*Source: https://developer.zendesk.com/api-reference/help_center/help-center-api/redirect_rules/*

---

## On this page

  * [JSON format](/api-reference/help_center/help-center-api/redirect_rules/#json-format)
  * [Search Redirect Rules](/api-reference/help_center/help-center-api/redirect_rules/#search-redirect-rules)
  * [Show Redirect Rule](/api-reference/help_center/help-center-api/redirect_rules/#show-redirect-rule)
  * [Set a redirect rule](/api-reference/help_center/help-center-api/redirect_rules/#set-a-redirect-rule)
  * [Delete Redirect Rule](/api-reference/help_center/help-center-api/redirect_rules/#delete-redirect-rule)


# Redirect Rules

## On this page

  * [JSON format](/api-reference/help_center/help-center-api/redirect_rules/#json-format)
  * [Search Redirect Rules](/api-reference/help_center/help-center-api/redirect_rules/#search-redirect-rules)
  * [Show Redirect Rule](/api-reference/help_center/help-center-api/redirect_rules/#show-redirect-rule)
  * [Set a redirect rule](/api-reference/help_center/help-center-api/redirect_rules/#set-a-redirect-rule)
  * [Delete Redirect Rule](/api-reference/help_center/help-center-api/redirect_rules/#delete-redirect-rule)


The Redirect Rules API lets you create and manage page redirects for objects or URLs that return an HTTP 404 response. For example, this means that to redirect an article URL, the article must be archived or deleted. Similarly for sections, categories, community posts, etc. the object must be deleted for the redirect to take effect. The API has the following three primary use cases, each with their own URL patterns.

The Redirect Rules API is available in all Guide plans except Guide Lite Legacy. See [About the Zendesk Guide plan types](https://support.zendesk.com/hc/en-us/articles/4408823905434).

  * **Redirecting deleted objects** : If a help center article or section is deleted, you can redirect the old URL to a new article or section to prevent 404 errors and for SEO purposes. Examples:

    * /hc/en-us/articles/12345678
    * /hc/en-us/community/topics/200550545
    * /hc/en-us/sections/45678912
  * **Redirecting previous URLs when migrating to Zendesk** : If you're migrating content from a non-Zendesk product or service and you're keeping the same subdomain, you can redirect the old URLs to the corresponding Zendesk URLs to maintain SEO for your uses and crawlers. Examples:

    * /2023/01/01/blog-post-title
    * /en/support/home
    * /en/support/solutions/articles/1234

**Note** : Previous URLs that start with "/knowledge/", such as the URLs of content hosted by Hubspot, result in "Not found" errors. The "/knowledge/" path is reserved for [Knowledge admin](https://support.zendesk.com/hc/en-us/articles/9041943683354-Opening-the-help-center-and-accessing-Knowledge-admin#topic_b5q_nwn_s2c).

  * **Redirecting vanity URLs or other patterns** : There may be other reasons to set up vanity URLs or other patterns under your Zendesk subdomain or host-mapped subdomain. For example, you can create short URLs that redirect to articles or custom pages. You can set up a redirect for any non-reserved URL pattern for an active brand or host-mapped subdomain. Examples:

    * /contact-us
    * /offers
    * /videos

**Note** : There is a limit of 50,000 redirect rules per brand.


### JSON format

Redirect Rules are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
brand_id| string| false| true| ID of the brand to which this redirect rule applies
created_at| string| false| true| When the redirect rule was created
id| string| false| true| Automatically assigned when the redirect rule is created
redirect_from| string| false| true| The path to redirect from. Must begin with '/'. Omit any slug from the path
redirect_status| string| false| true| The HTTP status to use when redirecting. See [Redirections in HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Redirections) in the MDN docs. Allowed values are "301", "302", "303", "307", or "308".
redirect_to| string| false| true| The URL or path to redirect to. Must begin with 'https://', 'http://', or'/'
updated_at| string| false| true| When the redirect rule was last updated

#### Example


    {  "brand_id": "12345",  "created_at": "2022-10-13T12:00:00.000Z",  "id": "01GFXGBX7YZ9ASWTCVMASTK8ZS",  "redirect_from": "/hc/en-us/articles/7654321",  "redirect_status": "301",  "redirect_to": "https://help.example.com/account/setting-up-your-account",  "updated_at": "2022-10-13T12:00:00.000Z"}

### Search Redirect Rules

  * `GET /api/v2/guide/redirect_rules`


Lists redirect rules matching the given criteria.

#### Allowed for

  * Guide admins


#### Pagination

  * Cursor pagination only


See [Using cursor based pagination](/api-reference/introduction/pagination/#using-cursor-pagination).

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
filter| object| Query| false| A group of query parameters for filtering search results
page| object| Query| false| A group of query parameters used for pagination. See [Pagination](/api-reference/help_center/help-center-api/introduction/#pagination)
sort| string| Query| false| Options for sorting the result set by field and direction. The "-" prefix indicates DESC order. No prefix indicates ASC order. Allowed values are "id", "-id", "redirect_from", or "-redirect_from".

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/guide/redirect_rules \  --get \  --data-urlencode "filter[redirect_from_prefix]=/hc/en-us" \  --data-urlencode "sort=redirect_from" \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/redirect_rules?filter=&page=&sort="	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/redirect_rules")		.newBuilder()		.addQueryParameter("filter", "")		.addQueryParameter("page", "")		.addQueryParameter("sort", "");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/redirect_rules',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'filter': '',    'page': '',    'sort': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/redirect_rules?filter=&page=&sort="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/redirect_rules")uri.query = URI.encode_www_form("filter": "", "page": "", "sort": "")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "meta": {    "after_cursor": "Y3Vyc29yIHR3bw==",    "before_cursor": "Y3Vyc29yIG9uZQ==",    "has_more": true  },  "records": [    {      "brand_id": "12345",      "created_at": "2022-10-13T12:00:00.000Z",      "id": "01GFXGBX7YZ9ASWTCVMASTK8ZS",      "redirect_from": "/hc/en-us/articles/7654321",      "redirect_status": "301",      "redirect_to": "https://help.example.com/account/setting-up-your-account",      "updated_at": "2022-10-13T12:00:00.000Z"    }  ]}

**403 Forbidden**


    // Status 403 Forbidden
    {  "errors": [    {      "code": "Forbidden",      "meta": {},      "status": "403",      "title": "Access to the resource is forbidden"    }  ]}

### Show Redirect Rule

  * `GET /api/v2/guide/redirect_rules/{id}`


Shows information about the specified redirect rule.

#### Allowed for

  * Guide admins


#### Pagination

  * Cursor pagination only


See [Using cursor based pagination](/api-reference/introduction/pagination/#using-cursor-pagination).

By default, returns 30 redirect rules per page.

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
id| string| Path| true| The redirect rule id

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/guide/redirect_rules/{id} \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/redirect_rules/01GFYBENPDGN1R6NAA4WRDNVFR"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/redirect_rules/01GFYBENPDGN1R6NAA4WRDNVFR")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/redirect_rules/01GFYBENPDGN1R6NAA4WRDNVFR',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/redirect_rules/01GFYBENPDGN1R6NAA4WRDNVFR"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/redirect_rules/01GFYBENPDGN1R6NAA4WRDNVFR")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "redirect_rule": {    "brand_id": "12345",    "created_at": "2022-10-13T12:00:00.000Z",    "id": "01GFXGBX7YZ9ASWTCVMASTK8ZS",    "redirect_from": "/hc/en-us/articles/7654321",    "redirect_status": "301",    "redirect_to": "https://help.example.com/account/setting-up-your-account",    "updated_at": "2022-10-13T12:00:00.000Z"  }}

**403 Forbidden**


    // Status 403 Forbidden
    {  "errors": [    {      "code": "Forbidden",      "meta": {},      "status": "403",      "title": "Access to the resource is forbidden"    }  ]}

### Set a redirect rule

  * `POST /api/v2/guide/redirect_rules`


Creates or updates a redirect rule for the URL specified in `redirect_from`.

If there's already a redirect rule for the `redirect_from` URL, the request updates the `redirect_to` and `redirect_status` properties.

Some help center URLs such as for articles, topics, and posts, may have a slug appended to them. Omit the slug from the URL in `redirect_from`. For example, if the article has a URL of `/hc/en-us/articles/123456-Installation-and-setup`, then specify: `"redirect_from": "/hc/en-us/articles/123456"`

This allows you to redirect any request for that article regardless of the slug.

Read more about the [help center URL structure](https://support.zendesk.com/hc/en-us/articles/4408885974682-About-search-engine-optimization-SEO-in-your-help-center#topic_w4z_w4g_vs) in Zendesk help.

#### Allowed for

  * Guide admins


#### Example body


    {  "redirect_rule": {    "redirect_from": "/hc/en-us/articles/123",    "redirect_status": 301,    "redirect_to": "https://support.example.com/hc/en-us/456"  }}

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/guide/redirect_rules \  -X POST -d '{ "redirect_rule": { "redirect_from": "/hc/en-us/articles/9", "redirect_to": "https://example.com", "redirect_status": 301 } }' \  -H "Content-Type: application/json" \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/redirect_rules"	method := "POST"	payload := strings.NewReader(`{  "redirect_rule": {    "redirect_from": "/hc/en-us/articles/123",    "redirect_status": 301,    "redirect_to": "https://support.example.com/hc/en-us/456"  }}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/redirect_rules")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"redirect_rule\": {    \"redirect_from\": \"/hc/en-us/articles/123\",    \"redirect_status\": 301,    \"redirect_to\": \"https://support.example.com/hc/en-us/456\"  }}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "redirect_rule": {    "redirect_from": "/hc/en-us/articles/123",    "redirect_status": 301,    "redirect_to": "https://support.example.com/hc/en-us/456"  }});
    var config = {  method: 'POST',  url: 'https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/redirect_rules',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/redirect_rules"
    payload = json.loads("""{  "redirect_rule": {    "redirect_from": "/hc/en-us/articles/123",    "redirect_status": 301,    "redirect_to": "https://support.example.com/hc/en-us/456"  }}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/redirect_rules")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")request.body = %q({  "redirect_rule": {    "redirect_from": "/hc/en-us/articles/123",    "redirect_status": 301,    "redirect_to": "https://support.example.com/hc/en-us/456"  }})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**204 No Content**


    // Status 204 No Content
    null

**403 Forbidden**


    // Status 403 Forbidden
    {  "errors": [    {      "code": "Forbidden",      "meta": {},      "status": "403",      "title": "Access to the resource is forbidden"    }  ]}

### Delete Redirect Rule

  * `DELETE /api/v2/guide/redirect_rules/{id}`


Deletes the specified redirect rule.

#### Allowed for

  * Guide admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
id| string| Path| true| The redirect rule id

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/guide/redirect_rules/{id} \    -X DELETE \    -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/redirect_rules/01GFYBENPDGN1R6NAA4WRDNVFR"	method := "DELETE"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/redirect_rules/01GFYBENPDGN1R6NAA4WRDNVFR")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("DELETE", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'DELETE',  url: 'https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/redirect_rules/01GFYBENPDGN1R6NAA4WRDNVFR',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/redirect_rules/01GFYBENPDGN1R6NAA4WRDNVFR"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"DELETE",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://your_account_subdomain.zendesk.com/api/v2/api/v2/guide/redirect_rules/01GFYBENPDGN1R6NAA4WRDNVFR")request = Net::HTTP::Delete.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**204 No Content**


    // Status 204 No Content
    null

**403 Forbidden**


    // Status 403 Forbidden
    {  "errors": [    {      "code": "Forbidden",      "meta": {},      "status": "403",      "title": "Access to the resource is forbidden"    }  ]}

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)