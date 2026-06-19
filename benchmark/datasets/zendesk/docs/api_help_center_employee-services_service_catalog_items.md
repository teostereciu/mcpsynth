# Service Catalog Items

*Source: https://developer.zendesk.com/api-reference/help_center/employee-services/service_catalog_items/*

---

## On this page

  * [JSON format](/api-reference/help_center/employee-services/service_catalog_items/#json-format)
  * [List Service Catalog Items](/api-reference/help_center/employee-services/service_catalog_items/#list-service-catalog-items)
  * [Search Service Catalog Items](/api-reference/help_center/employee-services/service_catalog_items/#search-service-catalog-items)
  * [Show Service Catalog Item](/api-reference/help_center/employee-services/service_catalog_items/#show-service-catalog-item)


# Service Catalog Items

## On this page

  * [JSON format](/api-reference/help_center/employee-services/service_catalog_items/#json-format)
  * [List Service Catalog Items](/api-reference/help_center/employee-services/service_catalog_items/#list-service-catalog-items)
  * [Search Service Catalog Items](/api-reference/help_center/employee-services/service_catalog_items/#search-service-catalog-items)
  * [Show Service Catalog Item](/api-reference/help_center/employee-services/service_catalog_items/#show-service-catalog-item)


The service catalog is a centralized catalog that showcases available services and assets, making it easy for employees to browse, request, and access what they need with just a few clicks.

You can use the Service Catalog Items API endpoints to get the list of available items or a single one.

### JSON format

Service Catalog Items are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
description| string| false| true| The description of the service catalog item
form_id| integer| true| false| The id of the form the service catalog item is associated with
id| string| true| false| Automatically assigned when the service catalog item is created
name| string| false| true| The name of the service catalog item
thumbnail_url| string| false| false| The url of the thumbnail image for the service catalog item

### List Service Catalog Items

  * `GET /api/v2/help_center/service_catalog/items`


Lists all the service catalog items available.

#### Allowed for

  * End users


#### Pagination

  * Cursor pagination


See [Pagination](/api-reference/introduction/pagination/).

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
page[after]| string| Query| false| A string representing the cursor to the next page
page[before]| string| Query| false| A string representing the cursor to the previous page
page[size]| integer| Query| false| A numeric value to specify the number of items to return per page

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/service_catalog/items.json \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/service_catalog/items?page[after]=&page[before]=&page[size]="	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/service_catalog/items")		.newBuilder()		.addQueryParameter("page[after]", "")		.addQueryParameter("page[before]", "")		.addQueryParameter("page[size]", "");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/help_center/service_catalog/items',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'page[after]': '',    'page[before]': '',    'page[size]': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/service_catalog/items?page[after]=&page[before]=&page[size]="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/service_catalog/items")uri.query = URI.encode_www_form("page[after]": "", "page[before]": "", "page[size]": "")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "count": 2,  "links": {    "next": null,    "prev": null  },  "meta": {    "after_cursor": null,    "before_cursor": null,    "has_more": false  },  "service_catalog_items": [    {      "description": "Request a new laptop",      "form_id": 6002443386111,      "id": "01JV5G30T2JGHZDF5NSFMF3WD0",      "name": "MackBook Pro",      "thumbnail_url": "https://{subdomain}.zendesk.com/hc/service_catalog_item_attachments/01JV9G8E8QM2TTZKJTEXY58SRW/laptop.jpg"    },    {      "description": "Request a new keyboard",      "form_id": 6002443386111,      "id": "01JV9G8E8QM2TTZKJTEXY58SRW",      "name": "Keyboard",      "thumbnail_url": "https://{subdomain}.zendesk.com/hc/service_catalog_item_attachments/01JV5G30T2JGHZDF5NSFMF3WD0/keyboard.jpg"    }  ]}

### Search Service Catalog Items

  * `GET /api/v2/help_center/service_catalog/items/search`


Returns an array of service catalog item object records that meet the search criteria. Returns the records sorted by relevancy with page limits

#### Allowed for

  * End users


#### Pagination

  * Cursor pagination


See [Pagination](/api-reference/introduction/pagination/).

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
page[after]| string| Query| false| A string representing the cursor to the next page
page[before]| string| Query| false| A string representing the cursor to the previous page
page[size]| integer| Query| false| A numeric value to specify the number of items to return per page
query| string| Query| false| The query parameter allows searching for items whose names or descriptions contain the specified search criteria. The query can be multiple words or numbers.

Fuzzy search is supported. This means that the search will return results that are similar to the query, even if they do not match exactly.

For example, you might want to search for items related to laptops: `query=laptop`. In this example the API returns items that have the word 'laptop' in their name or description.

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/service_catalog/items/search.json?query={query} \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/service_catalog/items/search?page[after]=&page[before]=&page[size]=&query=laptop"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/service_catalog/items/search")		.newBuilder()		.addQueryParameter("page[after]", "")		.addQueryParameter("page[before]", "")		.addQueryParameter("page[size]", "")		.addQueryParameter("query", "laptop");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/help_center/service_catalog/items/search',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'page[after]': '',    'page[before]': '',    'page[size]': '',    'query': 'laptop',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/service_catalog/items/search?page[after]=&page[before]=&page[size]=&query=laptop"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/service_catalog/items/search")uri.query = URI.encode_www_form("page[after]": "", "page[before]": "", "page[size]": "", "query": "laptop")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "count": 2,  "links": {    "next": null,    "prev": null  },  "meta": {    "after_cursor": null,    "before_cursor": null,    "has_more": false  },  "service_catalog_items": [    {      "description": "Request a new laptop",      "form_id": 6002443386111,      "id": "01JV5G30T2JGHZDF5NSFMF3WD0",      "name": "MackBook Pro",      "thumbnail_url": "https://{subdomain}.zendesk.com/hc/service_catalog_item_attachments/01JV9G8E8QM2TTZKJTEXY58SRW/laptop.jpg"    },    {      "description": "Request a new keyboard",      "form_id": 6002443386111,      "id": "01JV9G8E8QM2TTZKJTEXY58SRW",      "name": "Keyboard",      "thumbnail_url": "https://{subdomain}.zendesk.com/hc/service_catalog_item_attachments/01JV5G30T2JGHZDF5NSFMF3WD0/keyboard.jpg"    }  ]}

### Show Service Catalog Item

  * `GET /api/v2/help_center/service_catalog/items/{item_id}`


Returns a service catalog item by its id.

#### Allowed for

  * End users


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
item_id| string| Path| true| The unique id of the service catalog item

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/service_catalog/items/{item_id}.json \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/service_catalog/items/01JV5G30T2JGHZDF5NSFMF3WD0"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/service_catalog/items/01JV5G30T2JGHZDF5NSFMF3WD0")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/help_center/service_catalog/items/01JV5G30T2JGHZDF5NSFMF3WD0',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/service_catalog/items/01JV5G30T2JGHZDF5NSFMF3WD0"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/service_catalog/items/01JV5G30T2JGHZDF5NSFMF3WD0")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "service_catalog_item": {    "description": "Request a new keyboard",    "form_id": 6002443386111,    "id": "01JV5G30T2JGHZDF5NSFMF3WD0",    "name": "Keyboard",    "thumbnail_url": "https://{subdomain}.zendesk.com/hc/service_catalog_item_attachments/01JV5G30T2JGHZDF5NSFMF3WD0/keyboard.jpg"  }}

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)