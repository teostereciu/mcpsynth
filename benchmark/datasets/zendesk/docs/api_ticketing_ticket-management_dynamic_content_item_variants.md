# Dynamic Content Item Variants

*Source: https://developer.zendesk.com/api-reference/ticketing/ticket-management/dynamic_content_item_variants/*

---

## On this page

  * [JSON format](/api-reference/ticketing/ticket-management/dynamic_content_item_variants/#json-format)
  * [List Variants](/api-reference/ticketing/ticket-management/dynamic_content_item_variants/#list-variants)
  * [Show Variant](/api-reference/ticketing/ticket-management/dynamic_content_item_variants/#show-variant)
  * [Create Variant](/api-reference/ticketing/ticket-management/dynamic_content_item_variants/#create-variant)
  * [Create Many Variants](/api-reference/ticketing/ticket-management/dynamic_content_item_variants/#create-many-variants)
  * [Update Variant](/api-reference/ticketing/ticket-management/dynamic_content_item_variants/#update-variant)
  * [Update Many Variants](/api-reference/ticketing/ticket-management/dynamic_content_item_variants/#update-many-variants)
  * [Delete Variant](/api-reference/ticketing/ticket-management/dynamic_content_item_variants/#delete-variant)


# Dynamic Content Item Variants

## On this page

  * [JSON format](/api-reference/ticketing/ticket-management/dynamic_content_item_variants/#json-format)
  * [List Variants](/api-reference/ticketing/ticket-management/dynamic_content_item_variants/#list-variants)
  * [Show Variant](/api-reference/ticketing/ticket-management/dynamic_content_item_variants/#show-variant)
  * [Create Variant](/api-reference/ticketing/ticket-management/dynamic_content_item_variants/#create-variant)
  * [Create Many Variants](/api-reference/ticketing/ticket-management/dynamic_content_item_variants/#create-many-variants)
  * [Update Variant](/api-reference/ticketing/ticket-management/dynamic_content_item_variants/#update-variant)
  * [Update Many Variants](/api-reference/ticketing/ticket-management/dynamic_content_item_variants/#update-many-variants)
  * [Delete Variant](/api-reference/ticketing/ticket-management/dynamic_content_item_variants/#delete-variant)


Dynamic content item variants are locale-specific versions of a dynamic content item. To learn more, see [Dynamic Content Items](/api-reference/ticketing/ticket-management/dynamic_content/).

### JSON format

Dynamic Content Item Variants are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
active| boolean| false| false| If the variant is active and usable
content| string| false| true| The content of the variant
created_at| string| true| false| When the variant was created
default| boolean| false| false| If the variant is the default for the item it belongs to
id| integer| true| false| Automatically assigned when the variant is created
locale_id| integer| false| true| An active locale
outdated| boolean| true| false| If the variant is outdated
updated_at| string| true| false| When the variant was last updated
url| string| true| false| The API url of the variant

A few items are worth noting:

  * `locale_id` \- Must be an active locale in the account. To get a list, see [/api/v2/locales](/api-reference/ticketing/account-configuration/locales/#list-locales)

  * `default` \- Used as the fallback if Zendesk Support can't find an appropriate variant to match the locale of the user the content is being displayed for

  * `outdated`\- Indicates the default variant for this item has been updated, but the other variants were not changed. The content may be out of date

  * `active` \- If false, Zendesk Support will not use the variant even if the user's locale matches the variant


#### Example


    {  "active": true,  "content": "This is my dynamic content in English",  "created_at": "2014-04-09T19:53:23Z",  "default": true,  "id": 23,  "locale_id": 125,  "outdated": false,  "updated_at": "2014-04-09T19:53:23Z",  "url": "https://subdomain.zendesk.com/api/v2/dynamic_content/items/3/variants/23"}

### List Variants

  * `GET /api/v2/dynamic_content/items/{dynamic_content_item_id}/variants`


Returns all the variants of the specified dynamic content item.

#### Allowed For

  * Admins
  * Agents who have permission to manage dynamic content


#### Pagination

  * Cursor pagination


See [Pagination](/api-reference/introduction/pagination/).

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
page| | Query| false| Pagination parameter. Supports both traditional offset and cursor-based pagination: - Traditional: `?page=2` (integer page number) - Cursor: `?page[size]=50&page[after]=cursor` (deepObject with size, after, before) These are mutually exclusive - use one format or the other, not both.
per_page| integer| Query| false| Number of records to return per page. Note: Default and maximum values vary by endpoint. Check endpoint-specific documentation for limits.
sort| string| Query| false| Field to sort results by. Prefix with `-` for descending order. When used with cursor pagination, this determines the cursor ordering. Example: `?sort=name` or `?sort=-created_at`
dynamic_content_item_id| integer| Path| true| The ID of the dynamic content item

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/dynamic_content/items/{dynamic_content_item_id}/variants \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/dynamic_content/items/47/variants?page=&per_page=50&sort=name"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/dynamic_content/items/47/variants")		.newBuilder()		.addQueryParameter("page", "")		.addQueryParameter("per_page", "50")		.addQueryParameter("sort", "name");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/dynamic_content/items/47/variants',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'page': '',    'per_page': '50',    'sort': 'name',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/dynamic_content/items/47/variants?page=&per_page=50&sort=name"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/dynamic_content/items/47/variants")uri.query = URI.encode_www_form("page": "", "per_page": "50", "sort": "name")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "variants": [    {      "active": true,      "content": "This is my dynamic content in English",      "created_at": "2014-04-09T19:53:23Z",      "default": true,      "id": 23,      "locale_id": 125,      "outdated": false,      "updated_at": "2014-04-09T19:53:23Z",      "url": "https://subdomain.zendesk.com/api/v2/dynamic_content/items/3/variants/23"    },    {      "active": false,      "content": "Este es mi contenido dinÃ¡mico en espaÃ±ol",      "created_at": "2014-04-09T19:53:23Z",      "default": false,      "id": 24,      "locale_id": 126,      "outdated": true,      "updated_at": "2014-04-09T19:53:23Z",      "url": "https://subdomain.zendesk.com/api/v2/dynamic_content/items/3/variants/24"    }  ]}

### Show Variant

  * `GET /api/v2/dynamic_content/items/{dynamic_content_item_id}/variants/{dynamic_content_variant_id}`


#### Allowed For

  * Admins, Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
dynamic_content_item_id| integer| Path| true| The ID of the dynamic content item
dynamic_content_variant_id| integer| Path| true| The ID of the variant

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/dynamic_content/items/{dynamic_content_item_id}/variants/{dynamic_content_variant_id} \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/dynamic_content/items/47/variants/23"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/dynamic_content/items/47/variants/23")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/dynamic_content/items/47/variants/23',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/dynamic_content/items/47/variants/23"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/dynamic_content/items/47/variants/23")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "variant": {    "active": true,    "content": "C'est mon contenu dynamique en franÃ§ais",    "created_at": "2014-04-09T19:53:23Z",    "default": false,    "id": 23,    "locale_id": 127,    "outdated": false,    "updated_at": "2014-04-09T19:53:23Z",    "url": "https://subdomain.zendesk.com/api/v2/dynamic_content/items/3/variants/23"  }}

### Create Variant

  * `POST /api/v2/dynamic_content/items/{dynamic_content_item_id}/variants`


You can only create one variant for each locale id. If a locale variant already exists, the request is rejected.

#### Allowed For

  * Admins, Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
dynamic_content_item_id| integer| Path| true| The ID of the dynamic content item

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/dynamic_content/items/{dynamic_content_item_id}/variants \  -d '{"variant": {"locale_id": 127, "active": true, "default": false, "content": "C\u0027est mon contenu dynamique en franÃ§ais"}}' \  -H "Content-Type: application/json" -X POST \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/dynamic_content/items/47/variants"	method := "POST"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/dynamic_content/items/47/variants")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'POST',  url: 'https://example.zendesk.com/api/v2/dynamic_content/items/47/variants',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/dynamic_content/items/47/variants"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/dynamic_content/items/47/variants")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**201 Created**


    // Status 201 Created
    {  "variant": {    "active": true,    "content": "C'est mon contenu dynamique en franÃ§ais",    "created_at": "2014-04-09T19:53:23Z",    "default": false,    "id": 23,    "locale_id": 127,    "outdated": false,    "updated_at": "2014-04-09T19:53:23Z",    "url": "https://subdomain.zendesk.com/api/v2/dynamic_content/items/3/variants/23"  }}

### Create Many Variants

  * `POST /api/v2/dynamic_content/items/{dynamic_content_item_id}/variants/create_many`


#### Allowed For

  * Admins, Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
dynamic_content_item_id| integer| Path| true| The ID of the dynamic content item

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/dynamic_content/items/{dynamic_content_item_id}/variants/create_many \  -d '{"variants": [{"locale_id": 127, "active": true, "default": false, "content": "C\u0027est mon contenu dynamique en franÃ§ais"},{"locale_id": 126, "active": true, "default": false, "content": "Este es mi contenido dinÃ¡mico en espaÃ±ol"}]}'\  -H "Content-Type: application/json" -X POST \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/dynamic_content/items/47/variants/create_many"	method := "POST"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/dynamic_content/items/47/variants/create_many")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'POST',  url: 'https://example.zendesk.com/api/v2/dynamic_content/items/47/variants/create_many',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/dynamic_content/items/47/variants/create_many"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/dynamic_content/items/47/variants/create_many")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**201 Created**


    // Status 201 Created
    {  "variants": [    {      "active": true,      "content": "C'est mon contenu dynamique en franÃ§ais",      "created_at": "2014-04-09T19:53:23Z",      "default": false,      "id": 23,      "locale_id": 127,      "outdated": false,      "updated_at": "2014-04-09T19:53:23Z",      "url": "https://subdomain.zendesk.com/api/v2/dynamic_content/items/3/variants/23"    },    {      "active": true,      "content": "Este es mi contenido dinÃ¡mico en espaÃ±ol",      "created_at": "2014-04-09T19:53:23Z",      "default": false,      "id": 24,      "locale_id": 126,      "outdated": false,      "updated_at": "2014-04-09T19:53:23Z",      "url": "https://subdomain.zendesk.com/api/v2/dynamic_content/items/3/variants/24"    }  ]}

### Update Variant

  * `PUT /api/v2/dynamic_content/items/{dynamic_content_item_id}/variants/{dynamic_content_variant_id}`


Updates the specified variant. You don't need to include all the properties. If you just want to update content, for example, then include just that.

You can't switch the active state of the default variant of an item. Similarly, you can't switch the default to false if the variant is the default. You must make another variant default instead.

#### Allowed For

  * Admins, Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
dynamic_content_item_id| integer| Path| true| The ID of the dynamic content item
dynamic_content_variant_id| integer| Path| true| The ID of the variant

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/dynamic_content/items/{dynamic_content_item_id}/variants/{dynamic_content_variant_id} \  -d '{"variant": {"active": false, "default": false, "content": "C\u0027est mon contenu dynamique en franÃ§ais"}}'\  -H "Content-Type: application/json" \  -v -u {email_address}/token:{api_token} -X PUT

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/dynamic_content/items/47/variants/23"	method := "PUT"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/dynamic_content/items/47/variants/23")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'PUT',  url: 'https://example.zendesk.com/api/v2/dynamic_content/items/47/variants/23',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/dynamic_content/items/47/variants/23"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/dynamic_content/items/47/variants/23")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "variant": {    "active": false,    "content": "C'est mon contenu dynamique en franÃ§ais",    "created_at": "2014-04-09T19:53:23Z",    "default": false,    "id": 23,    "locale_id": 125,    "outdated": false,    "updated_at": "2014-04-09T19:53:23Z",    "url": "https://subdomain.zendesk.com/api/v2/dynamic_content/items/3/variants/23"  }}

### Update Many Variants

  * `PUT /api/v2/dynamic_content/items/{dynamic_content_item_id}/variants/update_many`


Updates one or more variants. See [Update Variant](/api-reference/ticketing/ticket-management/dynamic_content_item_variants/#update-variant).

You must specify the variants by id in the body. To get the variant ids, see [List Variants](/api-reference/ticketing/ticket-management/dynamic_content_item_variants/#list-variants).

#### Allowed For

  * Admins, Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
dynamic_content_item_id| integer| Path| true| The ID of the dynamic content item

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/dynamic_content/items/{dynamic_content_item_id}/variants/update_many \  -d '{"variants": [{"id": 2789787, "locale_id": 16, "active": true, "default": false, "content": "C\u0027est mon contenu dynamique en franÃ§ais"},{"id": 2789807, "locale_id": 2, "active": true, "default": false, "content": "Este es mi contenido dinÃ¡mico en espaÃ±ol"}]}'\  -H "Content-Type: application/json" -X POST \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/dynamic_content/items/47/variants/update_many"	method := "PUT"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/dynamic_content/items/47/variants/update_many")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'PUT',  url: 'https://example.zendesk.com/api/v2/dynamic_content/items/47/variants/update_many',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/dynamic_content/items/47/variants/update_many"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/dynamic_content/items/47/variants/update_many")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "variants": [    {      "active": true,      "content": "C'est mon contenu dynamique en franÃ§ais",      "created_at": "2014-04-09T19:53:23Z",      "default": false,      "id": 23,      "locale_id": 16,      "outdated": false,      "updated_at": "2014-04-09T19:53:23Z",      "url": "https://subdomain.zendesk.com/api/v2/dynamic_content/items/3/variants/23"    },    {      "active": true,      "content": "Este es mi contenido dinÃ¡mico en espaÃ±ol",      "created_at": "2014-04-09T19:53:23Z",      "default": false,      "id": 24,      "locale_id": 2,      "outdated": false,      "updated_at": "2014-04-09T19:53:23Z",      "url": "https://subdomain.zendesk.com/api/v2/dynamic_content/items/3/variants/24"    }  ]}

### Delete Variant

  * `DELETE /api/v2/dynamic_content/items/{dynamic_content_item_id}/variants/{dynamic_content_variant_id}`


#### Allowed For

  * Admins, Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
dynamic_content_item_id| integer| Path| true| The ID of the dynamic content item
dynamic_content_variant_id| integer| Path| true| The ID of the variant

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/dynamic_content/items/{dynamic_content_item_id}/variants/{dynamic_content_variant_id} \  -X DELETE -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/dynamic_content/items/47/variants/23"	method := "DELETE"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/dynamic_content/items/47/variants/23")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("DELETE", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'DELETE',  url: 'https://example.zendesk.com/api/v2/dynamic_content/items/47/variants/23',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/dynamic_content/items/47/variants/23"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"DELETE",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/dynamic_content/items/47/variants/23")request = Net::HTTP::Delete.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**204 No Content**


    // Status 204 No Content
    null

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)