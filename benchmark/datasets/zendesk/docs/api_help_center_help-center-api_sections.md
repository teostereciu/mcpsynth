# Sections

*Source: https://developer.zendesk.com/api-reference/help_center/help-center-api/sections/*

---

## On this page

  * [JSON format](/api-reference/help_center/help-center-api/sections/#json-format)
  * [List Sections in Category](/api-reference/help_center/help-center-api/sections/#list-sections-in-category)
  * [List Sections](/api-reference/help_center/help-center-api/sections/#list-sections)
  * [List Sections in Category by Locale](/api-reference/help_center/help-center-api/sections/#list-sections-in-category-by-locale)
  * [List Sections by Locale](/api-reference/help_center/help-center-api/sections/#list-sections-by-locale)
  * [Show Section](/api-reference/help_center/help-center-api/sections/#show-section)
  * [Show Section by Locale](/api-reference/help_center/help-center-api/sections/#show-section-by-locale)
  * [Create Section in Category](/api-reference/help_center/help-center-api/sections/#create-section-in-category)
  * [Create Section](/api-reference/help_center/help-center-api/sections/#create-section)
  * [Update Section](/api-reference/help_center/help-center-api/sections/#update-section)
  * [Update Section by Locale](/api-reference/help_center/help-center-api/sections/#update-section-by-locale)
  * [Update Section Source Locale](/api-reference/help_center/help-center-api/sections/#update-section-source-locale)
  * [Update Section Source Locale by Locale](/api-reference/help_center/help-center-api/sections/#update-section-source-locale-by-locale)
  * [Delete Section](/api-reference/help_center/help-center-api/sections/#delete-section)
  * [Delete Section by Locale](/api-reference/help_center/help-center-api/sections/#delete-section-by-locale)


# Sections

## On this page

  * [JSON format](/api-reference/help_center/help-center-api/sections/#json-format)
  * [List Sections in Category](/api-reference/help_center/help-center-api/sections/#list-sections-in-category)
  * [List Sections](/api-reference/help_center/help-center-api/sections/#list-sections)
  * [List Sections in Category by Locale](/api-reference/help_center/help-center-api/sections/#list-sections-in-category-by-locale)
  * [List Sections by Locale](/api-reference/help_center/help-center-api/sections/#list-sections-by-locale)
  * [Show Section](/api-reference/help_center/help-center-api/sections/#show-section)
  * [Show Section by Locale](/api-reference/help_center/help-center-api/sections/#show-section-by-locale)
  * [Create Section in Category](/api-reference/help_center/help-center-api/sections/#create-section-in-category)
  * [Create Section](/api-reference/help_center/help-center-api/sections/#create-section)
  * [Update Section](/api-reference/help_center/help-center-api/sections/#update-section)
  * [Update Section by Locale](/api-reference/help_center/help-center-api/sections/#update-section-by-locale)
  * [Update Section Source Locale](/api-reference/help_center/help-center-api/sections/#update-section-source-locale)
  * [Update Section Source Locale by Locale](/api-reference/help_center/help-center-api/sections/#update-section-source-locale-by-locale)
  * [Delete Section](/api-reference/help_center/help-center-api/sections/#delete-section)
  * [Delete Section by Locale](/api-reference/help_center/help-center-api/sections/#delete-section-by-locale)


Sections contain related articles. See [Organizing knowledge base content in categories and sections](https://support.zendesk.com/hc/en-us/articles/218222877) in Zendesk help.

### JSON format

Sections are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
category_id| integer| false| false| The id of the category to which this section belongs
created_at| string| true| false| The time at which the section was created
description| string| false| false| The description of the section
html_url| string| true| false| The url of this section in HC
id| integer| true| false| Automatically assigned when creating subscriptions
locale| string| false| true| The locale in which the section is displayed
name| string| false| true| The name of the section
outdated| boolean| true| false| Whether the section is out of date
parent_section_id| integer| false| false| The id of the section to which this section belongs. Only writable for Guide Enterprise customers
position| integer| false| false| The position of this section in the section list. Used when sorting is set to Â´manualÂ´. By default the section is added to the end of the list
source_locale| string| true| false| The source (default) locale of the section
theme_template| string| false| false| The theme template name used to display this section in Help Center.
updated_at| string| true| false| The time at which the section was last updated
url| string| true| false| The API url of this section

#### Example


    {  "category_id": 3465,  "description": "This section contains tricks for the airborne",  "id": 1635,  "locale": "en-us",  "name": "Avionics"}

### List Sections in Category

  * `GET /api/v2/help_center/categories/{category_id}/sections`


Lists all the sections in a specific [category](/api-reference/help_center/help-center-api/categories).

#### Allowed for

  * Agents


The response will list only the sections that the requesting agent, end user, or anonymous user can view in the help center.

#### Pagination

  * Cursor pagination (recommended)
  * Offset pagination


See [Pagination](/api-reference/introduction/pagination/).

#### Sorting

You can sort the results with the `sort_by` and `sort_order` query string parameters.


    GET /api/v2/help_center/en-us/sections?sort_by=updated_at&sort_order=asc

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
categories| the category
translations| the section and category translations, if any

Unlike other sideloads, translations are embedded within the section because they're not shared between resources. Category translations are only sideloaded if categories are.

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
sort_by| string| Query| false| Sorts the results by one of the accepted values. Allowed values are "position", "created_at", or "updated_at".
sort_order| string| Query| false| Selects the order of the results. Allowed values are "asc", or "desc".
category_id| integer| Path| true| The unique ID of the category

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/categories/{category_id}/sections \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/categories/360002011513/sections?sort_by=&sort_order="	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/categories/360002011513/sections")		.newBuilder()		.addQueryParameter("sort_by", "")		.addQueryParameter("sort_order", "");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/help_center/categories/360002011513/sections',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'sort_by': '',    'sort_order': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/categories/360002011513/sections?sort_by=&sort_order="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/categories/360002011513/sections")uri.query = URI.encode_www_form("sort_by": "", "sort_order": "")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "sections": [    {      "category_id": 888887,      "description": "This section contains articles on flight instruments",      "id": 35467,      "locale": "en-us",      "name": "Avionics"    },    {      "category_id": 887285,      "description": "This section contains weather resources for pilots",      "id": 36169,      "locale": "en-us",      "name": "Weather"    }  ]}

### List Sections

  * `GET /api/v2/help_center/sections`


Lists all the sections in Help Center or in a specific [category](/api-reference/help_center/help-center-api/categories).

#### Allowed for

  * Agents


The response will list only the sections that the requesting agent, end user, or anonymous user can view in the help center.

#### Pagination

  * Cursor pagination (recommended)
  * Offset pagination


See [Pagination](/api-reference/introduction/pagination/).

#### Sorting

You can sort the results with the `sort_by` and `sort_order` query string parameters.


    GET /api/v2/help_center/en-us/sections?sort_by=updated_at&sort_order=asc

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
categories| the category
translations| the section and category translations, if any

Unlike other sideloads, translations are embedded within the section because they're not shared between resources. Category translations are only sideloaded if categories are.

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
sort_by| string| Query| false| Sorts the results by one of the accepted values. Allowed values are "position", "created_at", or "updated_at".
sort_order| string| Query| false| Selects the order of the results. Allowed values are "asc", or "desc".

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/sections \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/sections?sort_by=&sort_order="	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/sections")		.newBuilder()		.addQueryParameter("sort_by", "")		.addQueryParameter("sort_order", "");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/help_center/sections',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'sort_by': '',    'sort_order': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/sections?sort_by=&sort_order="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/sections")uri.query = URI.encode_www_form("sort_by": "", "sort_order": "")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "sections": [    {      "category_id": 888887,      "description": "This section contains articles on flight instruments",      "id": 35467,      "locale": "en-us",      "name": "Avionics"    },    {      "category_id": 887285,      "description": "This section contains weather resources for pilots",      "id": 36169,      "locale": "en-us",      "name": "Weather"    }  ]}

### List Sections in Category by Locale

  * `GET /api/v2/help_center/{locale}/categories/{category_id}/sections`


Lists all the sections in Help Center or in a specific [category](/api-reference/help_center/help-center-api/categories).

The `{locale}` is required only for end users and anomynous users. Admins and agents can omit it.

#### Allowed for

  * Anonymous users


The response will list only the sections that the requesting agent, end user, or anonymous user can view in the help center.

#### Pagination

  * Cursor pagination (recommended)
  * Offset pagination


See [Pagination](/api-reference/introduction/pagination/).

#### Sorting

You can sort the results with the `sort_by` and `sort_order` query string parameters.


    GET /api/v2/help_center/en-us/sections.json?sort_by=updated_at&sort_order=asc

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
categories| the category
translations| the section and category translations, if any

Unlike other sideloads, translations are embedded within the section because they're not shared between resources. Category translations are only sideloaded if categories are.

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
sort_by| string| Query| false| Sorts the results by one of the accepted values. Allowed values are "position", "created_at", or "updated_at".
sort_order| string| Query| false| Selects the order of the results. Allowed values are "asc", or "desc".
category_id| integer| Path| true| The unique ID of the category
locale| string| Path| true| The locale the item is displayed in

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/{locale}/categories/{category_id}/sections.json \-v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/en-us/categories/360002011513/sections?sort_by=&sort_order="	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/en-us/categories/360002011513/sections")		.newBuilder()		.addQueryParameter("sort_by", "")		.addQueryParameter("sort_order", "");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/help_center/en-us/categories/360002011513/sections',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'sort_by': '',    'sort_order': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/en-us/categories/360002011513/sections?sort_by=&sort_order="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/en-us/categories/360002011513/sections")uri.query = URI.encode_www_form("sort_by": "", "sort_order": "")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "sections": [    {      "category_id": 888887,      "description": "This section contains articles on flight instruments",      "id": 35467,      "locale": "en-us",      "name": "Avionics"    },    {      "category_id": 887285,      "description": "This section contains weather resources for pilots",      "id": 36169,      "locale": "en-us",      "name": "Weather"    }  ]}

### List Sections by Locale

  * `GET /api/v2/help_center/{locale}/sections`


Lists all the sections in Help Center or in a specific [category](/api-reference/help_center/help-center-api/categories).

The `{locale}` is required only for end users and anomynous users. Admins and agents can omit it.

#### Allowed for

  * Anonymous users


The response will list only the sections that the requesting agent, end user, or anonymous user can view in the help center.

#### Pagination

  * Cursor pagination (recommended)
  * Offset pagination


See [Pagination](/api-reference/introduction/pagination/).

#### Sorting

You can sort the results with the `sort_by` and `sort_order` query string parameters.


    GET /api/v2/help_center/en-us/sections.json?sort_by=updated_at&sort_order=asc

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
categories| the category
translations| the section and category translations, if any

Unlike other sideloads, translations are embedded within the section because they're not shared between resources. Category translations are only sideloaded if categories are.

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
sort_by| string| Query| false| Sorts the results by one of the accepted values. Allowed values are "position", "created_at", or "updated_at".
sort_order| string| Query| false| Selects the order of the results. Allowed values are "asc", or "desc".
locale| string| Path| true| The locale the item is displayed in

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/{locale}/sections.json \-v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/en-us/sections?sort_by=&sort_order="	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/en-us/sections")		.newBuilder()		.addQueryParameter("sort_by", "")		.addQueryParameter("sort_order", "");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/help_center/en-us/sections',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'sort_by': '',    'sort_order': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/en-us/sections?sort_by=&sort_order="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/en-us/sections")uri.query = URI.encode_www_form("sort_by": "", "sort_order": "")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "sections": [    {      "category_id": 888887,      "description": "This section contains articles on flight instruments",      "id": 35467,      "locale": "en-us",      "name": "Avionics"    },    {      "category_id": 887285,      "description": "This section contains weather resources for pilots",      "id": 36169,      "locale": "en-us",      "name": "Weather"    }  ]}

### Show Section

  * `GET /api/v2/help_center/sections/{section_id}`


#### Allowed for

  * Agents


#### Sideloads

The following sideloads are supported:

Name| Will sideload
---|---
categories| the category
translations| the section and category translations, if any

Unlike other sideloads, translations are embedded within the section since they're not shared between resources. [Category](/api-reference/help_center/help-center-api/categories) translations are only sideloaded if categories are.

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
section_id| integer| Path| true| The unique ID of the section

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/sections/{section_id} \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/sections/360004785313"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/sections/360004785313")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/help_center/sections/360004785313',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/sections/360004785313"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/sections/360004785313")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "section": {    "description": "This section contains articles on flight instruments",    "id": 3457836,    "locale": "en-us",    "name": "Avionics",    "position": 2  }}

### Show Section by Locale

  * `GET /api/v2/help_center/{locale}/sections/{section_id}`


**Note** : `{/locale}` is an optional parameter for admins and agents. End users and anonymous users must provide the parameter.

#### Allowed for

  * Anonymous users


#### Sideloads

The following sideloads are supported:

Name| Will sideload
---|---
categories| the category
translations| the section and category translations, if any

Unlike other sideloads, translations are embedded within the section since they're not shared between resources. [Category](/api-reference/help_center/help-center-api/categories) translations are only sideloaded if categories are.

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
locale| string| Path| true| The locale the item is displayed in
section_id| integer| Path| true| The unique ID of the section

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/{locale}/sections/{section_id}.json \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/en-us/sections/360004785313"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/en-us/sections/360004785313")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/help_center/en-us/sections/360004785313',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/en-us/sections/360004785313"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/en-us/sections/360004785313")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "section": {    "description": "This section contains articles on flight instruments",    "id": 3457836,    "locale": "en-us",    "name": "Avionics",    "position": 2  }}

### Create Section in Category

  * `POST /api/v2/help_center/categories/{category_id}/sections`


Creates a section in a given [category](/api-reference/help_center/help-center-api/categories). You must specify a section name and locale. The locale can be omitted if it's specified in the URL. Optionally, you can specify multiple [translations](/api-reference/help_center/help-center-api/translations) for the section. The specified locales must be enabled for the current Help Center.

#### Allowed for

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
category_id| integer| Path| true| The unique ID of the category

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/categories/{category_id}/sections \  -d '{"section": {"position": 2, "locale": "en-us", "name": "Avionics", \    "description": "This section contains articles on flight instruments"}}' \  -v -u {email_address}/token:{api_token} -X POST -H "Content-Type: application/json"
    # You can also specify multiple translations for the new section:
    curl https://{subdomain}.zendesk.com/api/v2/help_center/categories/{category_id}/sections \  -d '{"section": {"position": 2, "translations":  \    [{"locale": "en-us", "title": "Avionics", \    "body": "This section contains articles on flight instruments"}, \    {"locale": "fr", "title": "Avionique", \    "body": "Cette section contient des articles sur les instruments de vol"}]}}' \  -v -u {email_address}/token:{api_token} -X POST -H "Content-Type: application/json"

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/categories/360002011513/sections"	method := "POST"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/categories/360002011513/sections")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'POST',  url: 'https://support.zendesk.com/api/v2/help_center/categories/360002011513/sections',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/categories/360002011513/sections"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/categories/360002011513/sections")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**201 Created**


    // Status 201 Created
    {  "section": {    "description": "This section contains articles on flight instruments",    "id": 3457836,    "locale": "en-us",    "name": "Avionics",    "position": 2  }}

**400 Bad Request**


    // Status 400 Bad Request
    {  "errors": {    "parent_section_id": [      "cannot be assigned non-null value on this Guide plan"    ]  }}

### Create Section

  * `POST /api/v2/help_center/{locale}/categories/{category_id}/sections`


Creates a section in a given [category](/api-reference/help_center/help-center-api/categories). You must specify a section name and locale. The locale can be omitted if it's specified in the URL. Optionally, you can specify multiple [translations](/api-reference/help_center/help-center-api/translations) for the section. The specified locales must be enabled for the current Help Center.

#### Allowed for

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
category_id| integer| Path| true| The unique ID of the category
locale| string| Path| true| The locale the item is displayed in

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/categories/{category_id}/sections.json \  -d '{"section": {"position": 2, "locale": "en-us", "name": "Avionics", \    "description": "This section contains articles on flight instruments"}}' \  -v -u {email_address}/token:{api_token} -X POST -H "Content-Type: application/json"
    # You can also specify multiple translations for the new section:
    curl https://{subdomain}.zendesk.com/api/v2/help_center/categories/{category_id}/sections.json \  -d '{"section": {"position": 2, "translations":  \    [{"locale": "en-us", "title": "Avionics", \    "body": "This section contains articles on flight instruments"}, \    {"locale": "fr", "title": "Avionique", \    "body": "Cette section contient des articles sur les instruments de vol"}]}}' \  -v -u {email_address}/token:{api_token} -X POST -H "Content-Type: application/json"

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/en-us/categories/360002011513/sections"	method := "POST"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/en-us/categories/360002011513/sections")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'POST',  url: 'https://support.zendesk.com/api/v2/help_center/en-us/categories/360002011513/sections',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/en-us/categories/360002011513/sections"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/en-us/categories/360002011513/sections")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**201 Created**


    // Status 201 Created
    {  "section": {    "description": "This section contains articles on flight instruments",    "id": 3457836,    "locale": "en-us",    "name": "Avionics",    "position": 2  }}

**400 Bad Request**


    // Status 400 Bad Request
    {  "errors": {    "parent_section_id": [      "cannot be assigned non-null value on this Guide plan"    ]  }}

### Update Section

  * `PUT /api/v2/help_center/sections/{section_id}`


Update section. This endpoint updates section-level data, specifically:

  * name (in the source locale)
  * description (in the source locale)
  * position
  * sorting
  * category_id
  * parent_section_id
  * theme_template


To update non-source section translations, see [Translations](/api-reference/help_center/help-center-api/translations).

#### Allowed for

  * Help Center managers


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
section_id| integer| Path| true| The unique ID of the section

#### Example body


    {  "section": {    "position": 3  }}

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/sections/{section_id} \-d '{"section": {"position": 42}}' \-v -u {email_address}/token:{api_token} -X PUT -H "Content-Type: application/json"

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/sections/360004785313"	method := "PUT"	payload := strings.NewReader(`{  "section": {    "position": 3  }}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/sections/360004785313")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"section\": {    \"position\": 3  }}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "section": {    "position": 3  }});
    var config = {  method: 'PUT',  url: 'https://support.zendesk.com/api/v2/help_center/sections/360004785313',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/sections/360004785313"
    payload = json.loads("""{  "section": {    "position": 3  }}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/sections/360004785313")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")request.body = %q({  "section": {    "position": 3  }})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "section": {    "description": "This section contains articles on flight instruments",    "id": 3457836,    "locale": "en-us",    "name": "Avionics",    "position": 2  }}

**400 Bad Request**


    // Status 400 Bad Request
    {  "errors": {    "parent_section_id": [      "would result in a cycle"    ]  }}

### Update Section by Locale

  * `PUT /api/v2/help_center/{locale}/sections/{section_id}`


Update section. This endpoint updates section-level data, specifically:

  * name (in the source locale)
  * description (in the source locale)
  * position
  * sorting
  * category_id
  * parent_section_id
  * theme_template


To update non-source section translations, see [Translations](/api-reference/help_center/help-center-api/translations).

#### Allowed for

  * Help Center managers


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
locale| string| Path| true| The locale the item is displayed in
section_id| integer| Path| true| The unique ID of the section

#### Example body


    {  "section": {    "position": 3  }}

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/sections/{section_id}.json \-d '{"section": {"position": 42}}' \-v -u {email_address}/token:{api_token} -X PUT -H "Content-Type: application/json"

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/en-us/sections/360004785313"	method := "PUT"	payload := strings.NewReader(`{  "section": {    "position": 3  }}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/en-us/sections/360004785313")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"section\": {    \"position\": 3  }}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "section": {    "position": 3  }});
    var config = {  method: 'PUT',  url: 'https://support.zendesk.com/api/v2/help_center/en-us/sections/360004785313',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/en-us/sections/360004785313"
    payload = json.loads("""{  "section": {    "position": 3  }}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/en-us/sections/360004785313")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")request.body = %q({  "section": {    "position": 3  }})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "section": {    "description": "This section contains articles on flight instruments",    "id": 3457836,    "locale": "en-us",    "name": "Avionics",    "position": 2  }}

**400 Bad Request**


    // Status 400 Bad Request
    {  "errors": {    "parent_section_id": [      "would result in a cycle"    ]  }}

### Update Section Source Locale

  * `PUT /api/v2/help_center/sections/{section_id}/source_locale`


This endpoint lets you set a section's source language to something other than the default language of your Help Center. For example, if the default language of your Help Center is English but your KB has a section only for Japanese customers, you can set the section's source locale to 'ja'.

#### Allowed for

  * Help Center managers


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
section_id| integer| Path| true| The unique ID of the section

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/sections/{section_id}/source_locale.json \-d '{"section_locale": "fr"}' -v -u {email_address}/token:{api_token} -X PUT \-H "Content-Type: application/json"

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/sections/360004785313/source_locale"	method := "PUT"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/sections/360004785313/source_locale")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'PUT',  url: 'https://support.zendesk.com/api/v2/help_center/sections/360004785313/source_locale',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/sections/360004785313/source_locale"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/sections/360004785313/source_locale")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    null

### Update Section Source Locale by Locale

  * `PUT /api/v2/help_center/{locale}/sections/{section_id}/source_locale`


This endpoint lets you set a section's source language to something other than the default language of your Help Center. For example, if the default language of your Help Center is English but your KB has a section only for Japanese customers, you can set the section's source locale to 'ja'.

#### Allowed for

  * Help Center managers


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
locale| string| Path| true| The locale the item is displayed in
section_id| integer| Path| true| The unique ID of the section

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/sections/{section_id}/source_locale.json \-d '{"section_locale": "fr"}' -v -u {email_address}/token:{api_token} -X PUT \-H "Content-Type: application/json"

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/en-us/sections/360004785313/source_locale"	method := "PUT"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/en-us/sections/360004785313/source_locale")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'PUT',  url: 'https://support.zendesk.com/api/v2/help_center/en-us/sections/360004785313/source_locale',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/en-us/sections/360004785313/source_locale"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/en-us/sections/360004785313/source_locale")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    null

### Delete Section

  * `DELETE /api/v2/help_center/sections/{section_id}`


**WARNING: All articles in the section will also be deleted.**

#### Allowed for

  * Help Center managers


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
section_id| integer| Path| true| The unique ID of the section

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/sections/{section_id} \  -v -u {email_address}/token:{api_token} -X DELETE

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/sections/360004785313"	method := "DELETE"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/sections/360004785313")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("DELETE", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'DELETE',  url: 'https://support.zendesk.com/api/v2/help_center/sections/360004785313',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/sections/360004785313"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"DELETE",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/sections/360004785313")request = Net::HTTP::Delete.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**204 No Content**


    // Status 204 No Content
    null

### Delete Section by Locale

  * `DELETE /api/v2/help_center/{locale}/sections/{section_id}`


**WARNING: All articles in the section will also be deleted.**

#### Allowed for

  * Help Center managers


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
locale| string| Path| true| The locale the item is displayed in
section_id| integer| Path| true| The unique ID of the section

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/sections/{section_id}.json \  -v -u {email_address}/token:{api_token} -X DELETE

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/en-us/sections/360004785313"	method := "DELETE"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/en-us/sections/360004785313")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("DELETE", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'DELETE',  url: 'https://support.zendesk.com/api/v2/help_center/en-us/sections/360004785313',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/en-us/sections/360004785313"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"DELETE",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/en-us/sections/360004785313")request = Net::HTTP::Delete.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**204 No Content**


    // Status 204 No Content
    null

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)