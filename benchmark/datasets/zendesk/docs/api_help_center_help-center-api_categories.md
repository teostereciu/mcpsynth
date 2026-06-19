# Categories

*Source: https://developer.zendesk.com/api-reference/help_center/help-center-api/categories/*

---

## On this page

  * [JSON format](/api-reference/help_center/help-center-api/categories/#json-format)
  * [List Categories](/api-reference/help_center/help-center-api/categories/#list-categories)
  * [List Categories by Locale](/api-reference/help_center/help-center-api/categories/#list-categories-by-locale)
  * [Show Category](/api-reference/help_center/help-center-api/categories/#show-category)
  * [Show Category by Locale](/api-reference/help_center/help-center-api/categories/#show-category-by-locale)
  * [Create Category](/api-reference/help_center/help-center-api/categories/#create-category)
  * [Create Category by Locale](/api-reference/help_center/help-center-api/categories/#create-category-by-locale)
  * [Update Category](/api-reference/help_center/help-center-api/categories/#update-category)
  * [Update Category by Locale](/api-reference/help_center/help-center-api/categories/#update-category-by-locale)
  * [Update Category Source Locale](/api-reference/help_center/help-center-api/categories/#update-category-source-locale)
  * [Update Category Source Locale by Locale](/api-reference/help_center/help-center-api/categories/#update-category-source-locale-by-locale)
  * [Delete Category](/api-reference/help_center/help-center-api/categories/#delete-category)
  * [Delete Category by Locale](/api-reference/help_center/help-center-api/categories/#delete-category-by-locale)


# Categories

## On this page

  * [JSON format](/api-reference/help_center/help-center-api/categories/#json-format)
  * [List Categories](/api-reference/help_center/help-center-api/categories/#list-categories)
  * [List Categories by Locale](/api-reference/help_center/help-center-api/categories/#list-categories-by-locale)
  * [Show Category](/api-reference/help_center/help-center-api/categories/#show-category)
  * [Show Category by Locale](/api-reference/help_center/help-center-api/categories/#show-category-by-locale)
  * [Create Category](/api-reference/help_center/help-center-api/categories/#create-category)
  * [Create Category by Locale](/api-reference/help_center/help-center-api/categories/#create-category-by-locale)
  * [Update Category](/api-reference/help_center/help-center-api/categories/#update-category)
  * [Update Category by Locale](/api-reference/help_center/help-center-api/categories/#update-category-by-locale)
  * [Update Category Source Locale](/api-reference/help_center/help-center-api/categories/#update-category-source-locale)
  * [Update Category Source Locale by Locale](/api-reference/help_center/help-center-api/categories/#update-category-source-locale-by-locale)
  * [Delete Category](/api-reference/help_center/help-center-api/categories/#delete-category)
  * [Delete Category by Locale](/api-reference/help_center/help-center-api/categories/#delete-category-by-locale)


Categories are the top-level organizing containers of the knowledge base in the help center. Categories contain related [sections](/api-reference/help_center/help-center-api/sections/). See [Organizing knowledge base content in categories and sections](https://support.zendesk.com/hc/en-us/articles/218222877) in Zendesk help.

### JSON format

Categories are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
created_at| string| true| false| The time at which the category was created
description| string| false| false| The description of the category
html_url| string| true| false| The url of this category in Help Center
id| integer| true| true| Automatically assigned when creating categories
locale| string| false| true| The locale where the category is displayed
name| string| false| true| The name of the category
outdated| boolean| true| false| Whether the category is out of date
position| integer| false| false| The position of this category relative to other categories
source_locale| string| true| false| The source (default) locale of the category
updated_at| string| true| false| The time at which the category was last updated
url| string| true| false| The API url of this category

#### Example


    {  "description": "",  "html_url": "https://company.zendesk.com/hc/en-us/categories/354362577",  "id": 1635,  "locale": "en-us",  "name": "Self Help Articles",  "source_locale": "en-us",  "url": "https://company.zendesk.com/api/v2/help_center/categories/354362577"}

### List Categories

  * `GET /api/v2/help_center/categories`


#### Allowed for

  * Agents


The response will list only the categories that the agent, end user, or anonymous user can view in the help center.

#### Pagination

  * Cursor pagination (recommended)
  * Offset pagination


See [Pagination](/api-reference/introduction/pagination/).

#### Sorting

You can sort the results with the `sort_by` and `sort_order` query string parameters.


    GET /api/v2/help_center/en-us/categories?sort_by=updated_at&sort_order=asc

The `sort_by` parameter can have one of the following values:

value| description
---|---
`position`| order set manually using the Arrange Content page. Default order
`created_at`| order by creation time
`updated_at`| order by update time

The `sort_order` parameter can have one of the following values:

value| description
---|---
`asc`| ascending order
`desc`| descending order

#### Sideloads

The following sideloads are supported:

Name| Will sideload
---|---
translations| the category translations, if any

Translations are embedded within the category because they're not shared between resources.

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
sort_by| string| Query| false| Sorts the results by one of the accepted values. Allowed values are "position", "created_at", or "updated_at".
sort_order| string| Query| false| Selects the order of the results. Allowed values are "asc", or "desc".

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/categories \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/categories?sort_by=&sort_order="	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/categories")		.newBuilder()		.addQueryParameter("sort_by", "")		.addQueryParameter("sort_order", "");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/help_center/categories',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'sort_by': '',    'sort_order': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/categories?sort_by=&sort_order="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/categories")uri.query = URI.encode_www_form("sort_by": "", "sort_order": "")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "categories": [    {      "description": "This category contains a collection of Super Hero tricks",      "id": 37486578,      "locale": "en-us",      "name": "Super Hero Tricks"    },    {      "description": "All the cool tricks!",      "id": 354675463,      "locale": "en-us",      "name": "Tips & Tricks"    }  ]}

### List Categories by Locale

  * `GET /api/v2/help_center/{locale}/categories`


**Note** : `{/locale}` is an optional parameter for admins and agents. End users and anonymous users must provide the parameter.

#### Allowed for

  * Anonymous users


The response will list only the categories that the agent, end user, or anonymous user can view in the help center.

#### Pagination

  * Cursor pagination (recommended)
  * Offset pagination


See [Pagination](/api-reference/introduction/pagination/).

#### Sorting

You can sort the results with the `sort_by` and `sort_order` query string parameters.


    GET /api/v2/help_center/en-us/categories.json?sort_by=updated_at&sort_order=asc

The `sort_by` parameter can have one of the following values:

value| description
---|---
`position`| order set manually using the Arrange Content page. Default order
`created_at`| order by creation time
`updated_at`| order by update time

The `sort_order` parameter can have one of the following values:

value| description
---|---
`asc`| ascending order
`desc`| descending order

#### Sideloads

The following sideloads are supported:

Name| Will sideload
---|---
translations| the category translations, if any

Translations are embedded within the category because they're not shared between resources.

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
sort_by| string| Query| false| Sorts the results by one of the accepted values. Allowed values are "position", "created_at", or "updated_at".
sort_order| string| Query| false| Selects the order of the results. Allowed values are "asc", or "desc".
locale| string| Path| true| The locale the item is displayed in

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/{locale}/categories.json \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/en-us/categories?sort_by=&sort_order="	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/en-us/categories")		.newBuilder()		.addQueryParameter("sort_by", "")		.addQueryParameter("sort_order", "");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/help_center/en-us/categories',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'sort_by': '',    'sort_order': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/en-us/categories?sort_by=&sort_order="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/en-us/categories")uri.query = URI.encode_www_form("sort_by": "", "sort_order": "")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "categories": [    {      "description": "This category contains a collection of Super Hero tricks",      "id": 37486578,      "locale": "en-us",      "name": "Super Hero Tricks"    },    {      "description": "All the cool tricks!",      "id": 354675463,      "locale": "en-us",      "name": "Tips & Tricks"    }  ]}

### Show Category

  * `GET /api/v2/help_center/categories/{category_id}`


#### Allowed for

  * Agents


#### Sideloads

The following sideloads are supported:

Name| Will sideload
---|---
translations| the category translations, if any

Translations are embedded within the category because they're not shared between resources.

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
category_id| integer| Path| true| The unique ID of the category

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/categories/{category_id} \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/categories/360002011513"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/categories/360002011513")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/help_center/categories/360002011513',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/categories/360002011513"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/categories/360002011513")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "category": {    "description": "This category contains a collection of Super Hero tricks",    "id": 37486578,    "locale": "en-us",    "name": "Super Hero Tricks"  }}

### Show Category by Locale

  * `GET /api/v2/help_center/{locale}/categories/{category_id}`


**Note** : `{/locale}` is an optional parameter for admins and agents. End users and anonymous users must provide the parameter.

#### Allowed for

  * Anonymous users


#### Sideloads

The following sideloads are supported:

Name| Will sideload
---|---
translations| the category translations, if any

Translations are embedded within the category because they're not shared between resources.

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
category_id| integer| Path| true| The unique ID of the category
locale| string| Path| true| The locale the item is displayed in

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/{locale}/categories/{category_id}.json \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/en-us/categories/360002011513"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/en-us/categories/360002011513")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/help_center/en-us/categories/360002011513',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/en-us/categories/360002011513"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/en-us/categories/360002011513")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "category": {    "description": "This category contains a collection of Super Hero tricks",    "id": 37486578,    "locale": "en-us",    "name": "Super Hero Tricks"  }}

### Create Category

  * `POST /api/v2/help_center/categories`


You must specify a category name and locale. The locale can be omitted if it's specified in the URL. Optionally, you can specify multiple [translations](/api-reference/help_center/help-center-api/translations) for the category. The specified locales must be enabled for the current Help Center.

#### Allowed for

  * Help Center managers


#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/categories \  -d '{"category": {"position": 2, "locale": "en-us", "name":  "Super Hero Tricks",\  "description": "This category contains a collection of super hero tricks"}}' \  -v -u {email_address}/token:{api_token} -X POST -H "Content-Type: application/json"

**curl**


    # You can also specify multiple translations for the new category:curl https://{subdomain}.zendesk.com/api/v2/help_center/categories \  -d '{"category": {"position": 2, "translations":  \    [{"locale": "en-us", "title": "Super Hero Tricks", \    "body": "This category contains a collection of Super Hero tricks"},  \    {"locale": "fr", "title": "Trucs Super Heros", \    "body": "Cette categorie contient une collection de trucs super heros"}]}}' \  -v -u {email_address}/token:{api_token} -X POST -H "Content-Type: application/json"

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/categories"	method := "POST"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/categories")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'POST',  url: 'https://support.zendesk.com/api/v2/help_center/categories',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/categories"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/categories")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**201 Created**


    // Status 201 Created
    {  "category": {    "description": "This category contains a collection of Super Hero tricks",    "id": 37486578,    "locale": "en-us",    "name": "Super Hero Tricks"  }}

### Create Category by Locale

  * `POST /api/v2/help_center/{locale}/categories`


You must specify a category name and locale. The locale can be omitted if it's specified in the URL. Optionally, you can specify multiple [translations](/api-reference/help_center/help-center-api/translations) for the category. The specified locales must be enabled for the current Help Center.

#### Allowed for

  * Help Center managers


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
locale| string| Path| true| The locale the item is displayed in

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/categories.json \  -d '{"category": {"position": 2, "locale": "en-us", "name":  "Super Hero Tricks",\  "description": "This category contains a collection of super hero tricks"}}' \  -v -u {email_address}/token:{api_token} -X POST -H "Content-Type: application/json"

**curl**


    # You can also specify multiple translations for the new category:curl https://{subdomain}.zendesk.com/api/v2/help_center/categories.json \  -d '{"category": {"position": 2, "translations":  \    [{"locale": "en-us", "title": "Super Hero Tricks", \    "body": "This category contains a collection of Super Hero tricks"},  \    {"locale": "fr", "title": "Trucs Super Heros", \    "body": "Cette categorie contient une collection de trucs super heros"}]}}' \  -v -u {email_address}/token:{api_token} -X POST -H "Content-Type: application/json"

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/en-us/categories"	method := "POST"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/en-us/categories")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'POST',  url: 'https://support.zendesk.com/api/v2/help_center/en-us/categories',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/en-us/categories"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/en-us/categories")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**201 Created**


    // Status 201 Created
    {  "category": {    "description": "This category contains a collection of Super Hero tricks",    "id": 37486578,    "locale": "en-us",    "name": "Super Hero Tricks"  }}

### Update Category

  * `PUT /api/v2/help_center/categories/{category_id}`


These endpoints only update category-level metadata such as the sorting position. They don't update category translations.

#### Allowed for

  * Help Center managers


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
category_id| integer| Path| true| The unique ID of the category

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/categories/{category_id} \-d '{"category": {"position": 2}}' \-v -u {email_address}/token:{api_token} -X PUT -H "Content-Type: application/json"

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/categories/360002011513"	method := "PUT"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/categories/360002011513")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'PUT',  url: 'https://support.zendesk.com/api/v2/help_center/categories/360002011513',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/categories/360002011513"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/categories/360002011513")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "category": {    "description": "This category contains a collection of Super Hero tricks",    "id": 37486578,    "locale": "en-us",    "name": "Super Hero Tricks"  }}

### Update Category by Locale

  * `PUT /api/v2/help_center/{locale}/categories/{category_id}`


These endpoints only update category-level metadata such as the sorting position. They don't update category translations.

#### Allowed for

  * Help Center managers


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
category_id| integer| Path| true| The unique ID of the category
locale| string| Path| true| The locale the item is displayed in

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/categories/{category_id}.json \-d '{"category": {"position": 2}}' \-v -u {email_address}/token:{api_token} -X PUT -H "Content-Type: application/json"

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/en-us/categories/360002011513"	method := "PUT"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/en-us/categories/360002011513")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'PUT',  url: 'https://support.zendesk.com/api/v2/help_center/en-us/categories/360002011513',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/en-us/categories/360002011513"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/en-us/categories/360002011513")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "category": {    "description": "This category contains a collection of Super Hero tricks",    "id": 37486578,    "locale": "en-us",    "name": "Super Hero Tricks"  }}

### Update Category Source Locale

  * `PUT /api/v2/help_center/categories/{category_id}/source_locale`


The endpoint updates the category `source_locale` property

#### Allowed for

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
category_id| integer| Path| true| The unique ID of the category

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/categories/{category_id}/source_locale.json \-d '{"category_locale": "fr"}' -v -u {email_address}/token:{api_token} -X PUT \-H "Content-Type: application/json"

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/categories/360002011513/source_locale"	method := "PUT"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/categories/360002011513/source_locale")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'PUT',  url: 'https://support.zendesk.com/api/v2/help_center/categories/360002011513/source_locale',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/categories/360002011513/source_locale"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/categories/360002011513/source_locale")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    null

### Update Category Source Locale by Locale

  * `PUT /api/v2/help_center/{locale}/categories/{category_id}/source_locale`


The endpoint updates the category `source_locale` property

#### Allowed for

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
category_id| integer| Path| true| The unique ID of the category
locale| string| Path| true| The locale the item is displayed in

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/categories/{category_id}/source_locale.json \-d '{"category_locale": "fr"}' -v -u {email_address}/token:{api_token} -X PUT \-H "Content-Type: application/json"

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/en-us/categories/360002011513/source_locale"	method := "PUT"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/en-us/categories/360002011513/source_locale")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'PUT',  url: 'https://support.zendesk.com/api/v2/help_center/en-us/categories/360002011513/source_locale',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/en-us/categories/360002011513/source_locale"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/en-us/categories/360002011513/source_locale")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    null

### Delete Category

  * `DELETE /api/v2/help_center/categories/{category_id}`


**WARNING: Every section and all articles in the category will also be deleted.**

#### Allowed for

  * Help Center managers


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
category_id| integer| Path| true| The unique ID of the category

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/categories/{category_id} \  -v -u {email_address}/token:{api_token} -X DELETE

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/categories/360002011513"	method := "DELETE"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/categories/360002011513")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("DELETE", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'DELETE',  url: 'https://support.zendesk.com/api/v2/help_center/categories/360002011513',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/categories/360002011513"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"DELETE",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/categories/360002011513")request = Net::HTTP::Delete.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**204 No Content**


    // Status 204 No Content
    null

### Delete Category by Locale

  * `DELETE /api/v2/help_center/{locale}/categories/{category_id}`


**WARNING: Every section and all articles in the category will also be deleted.**

#### Allowed for

  * Help Center managers


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
category_id| integer| Path| true| The unique ID of the category
locale| string| Path| true| The locale the item is displayed in

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/categories/{category_id}.json \  -v -u {email_address}/token:{api_token} -X DELETE

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/en-us/categories/360002011513"	method := "DELETE"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/en-us/categories/360002011513")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("DELETE", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'DELETE',  url: 'https://support.zendesk.com/api/v2/help_center/en-us/categories/360002011513',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/en-us/categories/360002011513"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"DELETE",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/en-us/categories/360002011513")request = Net::HTTP::Delete.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**204 No Content**


    // Status 204 No Content
    null

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)