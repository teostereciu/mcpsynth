# Dynamic Content Items

*Source: https://developer.zendesk.com/api-reference/ticketing/ticket-management/dynamic_content/*

---

## On this page

  * [Data hierarchy](/api-reference/ticketing/ticket-management/dynamic_content/#data-hierarchy)
  * [Paginating and sorting](/api-reference/ticketing/ticket-management/dynamic_content/#paginating-and-sorting)
  * [Specifying item variants](/api-reference/ticketing/ticket-management/dynamic_content/#specifying-item-variants)
  * [JSON format](/api-reference/ticketing/ticket-management/dynamic_content/#json-format)
  * [List Items](/api-reference/ticketing/ticket-management/dynamic_content/#list-items)
  * [Show Item](/api-reference/ticketing/ticket-management/dynamic_content/#show-item)
  * [Show Many Items](/api-reference/ticketing/ticket-management/dynamic_content/#show-many-items)
  * [Create Item](/api-reference/ticketing/ticket-management/dynamic_content/#create-item)
  * [Update Item](/api-reference/ticketing/ticket-management/dynamic_content/#update-item)
  * [Delete Item](/api-reference/ticketing/ticket-management/dynamic_content/#delete-item)


# Dynamic Content Items

## On this page

  * [Data hierarchy](/api-reference/ticketing/ticket-management/dynamic_content/#data-hierarchy)
  * [Paginating and sorting](/api-reference/ticketing/ticket-management/dynamic_content/#paginating-and-sorting)
  * [Specifying item variants](/api-reference/ticketing/ticket-management/dynamic_content/#specifying-item-variants)
  * [JSON format](/api-reference/ticketing/ticket-management/dynamic_content/#json-format)
  * [List Items](/api-reference/ticketing/ticket-management/dynamic_content/#list-items)
  * [Show Item](/api-reference/ticketing/ticket-management/dynamic_content/#show-item)
  * [Show Many Items](/api-reference/ticketing/ticket-management/dynamic_content/#show-many-items)
  * [Create Item](/api-reference/ticketing/ticket-management/dynamic_content/#create-item)
  * [Update Item](/api-reference/ticketing/ticket-management/dynamic_content/#update-item)
  * [Delete Item](/api-reference/ticketing/ticket-management/dynamic_content/#delete-item)


Dynamic content is a combination of a default version of some text and variants of the text in other languages. The combined content is represented by a placeholder such as `{{dc.my_placeholder}}`. Dynamic content is available only on the Professional plan and above. [Learn more](https://support.zendesk.com/hc/en-us/articles/203663356) in the Support Help Center.

This page contains the API reference for dynamic content items. See [Dynamic Content Item Variants](/api-reference/ticketing/ticket-management/dynamic_content_item_variants/) for the reference for variants.

You can use dynamic content with the API to set some properties of [ticket fields](/api-reference/ticketing/tickets/ticket_fields/), [ticket forms](/api-reference/ticketing/tickets/ticket_forms/), [user fields](/api-reference/ticketing/users/user_fields/), and [organization fields](/api-reference/ticketing/organizations/organization_fields/). For example, you can use dynamic content for the title of a ticket field. In that case, use the dynamic content placeholder for the value of the field's `raw_title` property and the the default version of the text as the value of the `title` property. Example:

`"title": "Flight Number", "raw_title": "{{dc.my_field_title}}", ...`

If dynamic content is not used for the property, the two values are identical:

`"title": "Flight Number", "raw_title": "Flight Number", ...`

### Data hierarchy

The data structure for dynamic content is a parent-child hierarchy where variants belong to items.

  * **Items**

These are the dynamic content placeholders defined by content creators. Each item defines a namespace for a specific piece of content, such as instructions on how to reset your password or upgrade your plan. An item's only content is the title of the item itself (defined by you) and a placeholder for that item (defined by Zendesk Support). The content itself is contained in the variants.

  * **Variants**

These are pieces of locale-specific content, where the context is based on the item they belong to. You can only have one variant per locale, per item. For example, if an item has 3 variants, they must each have a unique locale such as English, Spanish and French. They can't be English, English, and Spanish (though it is possible to have English-US and English-UK).


Each item has a unique ID and a unique dynamic content placeholder. Below each item are a number of variants, all with their unique ID and locale. Items can contain any number of variants.

### Paginating and sorting

This API uses standard pagination and sorting parameters. See [Pagination](/api-reference/introduction/pagination/).

You can sort the results of any list endpoint (both asc and desc) by the following properties: `locale`, `outdated`, `active`, `updated_at`, and `created_at`. The default sorting is by `id` in descending order.

### Specifying item variants

When creating or updating an item, specify the variants in the item's `variants` array. Each variant consists of a `locale_id`, `default`, and `content` property. See [Dynamic Content Item Variants](/api-reference/ticketing/ticket-management/dynamic_content_item_variants/) for the variants API reference.

Zendesk Support uses the `default` variant if it can't find a variant that matches the user's locale.

Example, formatted for clarity:


    {  "item": {    "name": "Snowboard Problem",    "default_locale_id": 1,    "variants": [      {"locale_id": 1, "default": true, "content": "C'est mon contenu dynamique en franÃ§ais"},      {"locale_id": 2, "default": false, "content": "Este es mi contenido dinÃ¡mico en espaÃ±ol"}    ]  }}

If you have only one variant, you can use the `content` property instead of the `variants` property:


    {  "item": {    "name": "Snowboard Problem",    "default_locale_id": 1,    "content": "C'est mon contenu dynamique en franÃ§ais"  }}

However, we recommend passing an array of variants even if you only have one variant.

### JSON format

Dynamic Content Items are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
created_at| string| true| false| When this record was created
default_locale_id| integer| false| true| The default locale for the item. Must be one of the [locales the account has active](/api-reference/ticketing/account-configuration/locales/#list-locales).
id| integer| true| false| Automatically assigned when creating items
name| string| false| true| The unique name of the item
outdated| boolean| true| false| Indicates the item has outdated variants within it
placeholder| string| true| false| Automatically generated placeholder for the item, derived from name
updated_at| string| true| false| When this record was last updated
url| string| true| false| The API url of this item
variants| array| false| true| All variants within this item. See [Dynamic Content Item Variants](/api-reference/ticketing/ticket-management/dynamic_content_item_variants/)

### List Items

  * `GET /api/v2/dynamic_content/items`


Returns a list of all dynamic content items for your account if accessed as an admin or agents who have permission to manage dynamic content.

#### Allowed For

  * Admins, Agents


#### Pagination

  * Cursor pagination (recommended)
  * Offset pagination


See [Pagination](/api-reference/introduction/pagination/).

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
page| | Query| false| Pagination parameter. Supports both traditional offset and cursor-based pagination: - Traditional: `?page=2` (integer page number) - Cursor: `?page[size]=50&page[after]=cursor` (deepObject with size, after, before) These are mutually exclusive - use one format or the other, not both.
per_page| integer| Query| false| Number of records to return per page. Note: Default and maximum values vary by endpoint. Check endpoint-specific documentation for limits.
sort| string| Query| false| Field to sort results by. Prefix with `-` for descending order. When used with cursor pagination, this determines the cursor ordering. Example: `?sort=name` or `?sort=-created_at`

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/dynamic_content/items \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/dynamic_content/items?page=&per_page=50&sort=name"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/dynamic_content/items")		.newBuilder()		.addQueryParameter("page", "")		.addQueryParameter("per_page", "50")		.addQueryParameter("sort", "name");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/dynamic_content/items',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'page': '',    'per_page': '50',    'sort': 'name',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/dynamic_content/items?page=&per_page=50&sort=name"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/dynamic_content/items")uri.query = URI.encode_www_form("page": "", "per_page": "50", "sort": "name")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "items": [    {      "created_at": "2015-05-13T22:33:12Z",      "default_locale_id": 1,      "id": 47,      "name": "Snowboard Problem",      "outdated": true,      "placeholder": "{{dc.snowboard_problem}}",      "updated_at": "2015-05-13T22:33:12Z",      "url": "https://company.zendesk.com/api/v2/dynamic_content/items/47",      "variants": [        {          "active": true,          "content": "C'est mon contenu dynamique en franÃ§ais",          "created_at": "2015-05-13T22:33:12Z",          "default": true,          "id": 47,          "locale_id": 1,          "outdated": false,          "updated_at": "2015-05-13T22:33:12Z",          "url": "https://company.zendesk.com/api/v2/dynamic_content/items/47/variants/47"        }      ]    }  ]}

### Show Item

  * `GET /api/v2/dynamic_content/items/{dynamic_content_item_id}`


#### Allowed For

  * Admins, Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
dynamic_content_item_id| integer| Path| true| The ID of the dynamic content item

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/dynamic_content/items/{dynamic_content_item_id} \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/dynamic_content/items/47"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/dynamic_content/items/47")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/dynamic_content/items/47',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/dynamic_content/items/47"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/dynamic_content/items/47")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "item": {    "created_at": "2015-05-13T22:33:12Z",    "default_locale_id": 1,    "id": 47,    "name": "Snowboard Problem",    "outdated": false,    "placeholder": "{{dc.snowboard_problem}}",    "updated_at": "2015-05-13T22:33:12Z",    "url": "https://company.zendesk.com/api/v2/dynamic_content/items/47",    "variants": [      {        "active": true,        "content": "Voici mon contenu dynamique en franÃ§ais",        "created_at": "2015-05-13T22:33:12Z",        "default": true,        "id": 47,        "locale_id": 16,        "outdated": false,        "updated_at": "2015-05-13T22:33:12Z",        "url": "https://company.zendesk.com/api/v2/dynamic_content/items/47/variants/47"      },      {        "active": true,        "content": "Este es mi contenido dinÃ¡mico en espaÃ±ol",        "created_at": "2015-05-13T22:33:12Z",        "default": false,        "id": 48,        "locale_id": 2,        "outdated": false,        "updated_at": "2015-05-13T22:33:12Z",        "url": "https://company.zendesk.com/api/v2/dynamic_content/items/47/variants/48"      }    ]  }}

### Show Many Items

  * `GET /api/v2/dynamic_content/items/show_many`


#### Stability

  * Development


#### Allowed For

  * Admins, Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
identifiers| string| Query| false| Identifiers for the dynamic contents

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/dynamic_content/items/show_many?identifiers=item_one,item_two  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/dynamic_content/items/show_many?identifiers=item1%2Citem2"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/dynamic_content/items/show_many")		.newBuilder()		.addQueryParameter("identifiers", "item1,item2");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/dynamic_content/items/show_many',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'identifiers': 'item1%2Citem2',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/dynamic_content/items/show_many?identifiers=item1%2Citem2"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/dynamic_content/items/show_many")uri.query = URI.encode_www_form("identifiers": "item1,item2")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "items": [    {      "created_at": "2015-05-13T22:33:12Z",      "default_locale_id": 1,      "id": 47,      "name": "Snowboard Problem",      "outdated": true,      "placeholder": "{{dc.snowboard_problem}}",      "updated_at": "2015-05-13T22:33:12Z",      "url": "https://company.zendesk.com/api/v2/dynamic_content/items/47",      "variants": [        {          "active": true,          "content": "C'est mon contenu dynamique en franÃ§ais",          "created_at": "2015-05-13T22:33:12Z",          "default": true,          "id": 47,          "locale_id": 1,          "outdated": false,          "updated_at": "2015-05-13T22:33:12Z",          "url": "https://company.zendesk.com/api/v2/dynamic_content/items/47/variants/47"        }      ]    }  ]}

### Create Item

  * `POST /api/v2/dynamic_content/items`


Create a new content item, with one or more variants in the item's `variants` array. See Specifying item variants.

The `default_locale_id` and variant `locale_id` values must be one of the locales the account has active. You can get the list with the [List Locales](/api-reference/ticketing/account-configuration/locales/#list-locales) endpoint.

#### Allowed For

  * Admins, Agents


#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/dynamic_content/items \  -d '{"item": {"name": "Snowboard Problem", "default_locale_id": 16, "variants": [{"locale_id": 16, "default": true, "content": "Voici mon contenu dynamique en franÃ§ais"}, {"locale_id": 2, "default": false, "content": "Este es mi contenido dinÃ¡mico en espaÃ±ol"}]}}' \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/dynamic_content/items"	method := "POST"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/dynamic_content/items")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'POST',  url: 'https://example.zendesk.com/api/v2/dynamic_content/items',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/dynamic_content/items"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/dynamic_content/items")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**201 Created**


    // Status 201 Created
    {  "item": {    "created_at": "2015-05-13T22:33:12Z",    "default_locale_id": 1,    "id": 47,    "name": "Snowboard Problem",    "outdated": false,    "placeholder": "{{dc.snowboard_problem}}",    "updated_at": "2015-05-13T22:33:12Z",    "url": "https://company.zendesk.com/api/v2/dynamic_content/items/47",    "variants": [      {        "active": true,        "content": "Voici mon contenu dynamique en franÃ§ais",        "created_at": "2015-05-13T22:33:12Z",        "default": true,        "id": 47,        "locale_id": 16,        "outdated": false,        "updated_at": "2015-05-13T22:33:12Z",        "url": "https://company.zendesk.com/api/v2/dynamic_content/items/47/variants/47"      },      {        "active": true,        "content": "Este es mi contenido dinÃ¡mico en espaÃ±ol",        "created_at": "2015-05-13T22:33:12Z",        "default": false,        "id": 48,        "locale_id": 2,        "outdated": false,        "updated_at": "2015-05-13T22:33:12Z",        "url": "https://company.zendesk.com/api/v2/dynamic_content/items/47/variants/48"      }    ]  }}

### Update Item

  * `PUT /api/v2/dynamic_content/items/{dynamic_content_item_id}`


The only attribute you can change is the name.

To add a variant to the item, or to update or delete the variants of the item, use the [Item Variants API](/api-reference/ticketing/ticket-management/dynamic_content_item_variants/#update-many-variants).

#### Allowed For

  * Admins, Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
dynamic_content_item_id| integer| Path| true| The ID of the dynamic content item

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/dynamic_content/items/{dynamic_content_item_id} \  -H "Content-Type: application/json" -d '{"item": {"name": "New name"}}'\  -v -u {email_address}/token:{api_token} -X PUT

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/dynamic_content/items/47"	method := "PUT"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/dynamic_content/items/47")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'PUT',  url: 'https://example.zendesk.com/api/v2/dynamic_content/items/47',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/dynamic_content/items/47"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/dynamic_content/items/47")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "item": {    "created_at": "2015-05-13T22:33:12Z",    "default_locale_id": 1,    "id": 47,    "name": "New name",    "outdated": false,    "placeholder": "{{dc.snowboard_problem}}",    "updated_at": "2015-05-13T22:33:12Z",    "url": "https://company.zendesk.com/api/v2/dynamic_content/items/47",    "variants": [      {        "active": true,        "content": "Voici mon contenu dynamique en franÃ§ais",        "created_at": "2015-05-13T22:33:12Z",        "default": true,        "id": 47,        "locale_id": 16,        "outdated": false,        "updated_at": "2015-05-13T22:33:12Z",        "url": "https://company.zendesk.com/api/v2/dynamic_content/items/47/variants/47"      },      {        "active": true,        "content": "Este es mi contenido dinÃ¡mico en espaÃ±ol",        "created_at": "2015-05-13T22:33:12Z",        "default": false,        "id": 48,        "locale_id": 2,        "outdated": false,        "updated_at": "2015-05-13T22:33:12Z",        "url": "https://company.zendesk.com/api/v2/dynamic_content/items/47/variants/48"      }    ]  }}

### Delete Item

  * `DELETE /api/v2/dynamic_content/items/{dynamic_content_item_id}`


#### Allowed For

  * Admins, Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
dynamic_content_item_id| integer| Path| true| The ID of the dynamic content item

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/dynamic_content/items/{dynamic_content_item_id} \  -X DELETE -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/dynamic_content/items/47"	method := "DELETE"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/dynamic_content/items/47")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("DELETE", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'DELETE',  url: 'https://example.zendesk.com/api/v2/dynamic_content/items/47',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/dynamic_content/items/47"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"DELETE",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/dynamic_content/items/47")request = Net::HTTP::Delete.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**204 No Content**


    // Status 204 No Content
    null

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)