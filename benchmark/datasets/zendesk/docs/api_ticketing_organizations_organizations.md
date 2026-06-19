# Organizations

*Source: https://developer.zendesk.com/api-reference/ticketing/organizations/organizations/*

---

## On this page

  * [JSON format](/api-reference/ticketing/organizations/organizations/#json-format)
  * [List Organizations](/api-reference/ticketing/organizations/organizations/#list-organizations)
  * [Count Organizations](/api-reference/ticketing/organizations/organizations/#count-organizations)
  * [Autocomplete Organizations](/api-reference/ticketing/organizations/organizations/#autocomplete-organizations)
  * [Search Organizations](/api-reference/ticketing/organizations/organizations/#search-organizations)
  * [Show Organization's Related Information](/api-reference/ticketing/organizations/organizations/#show-organizations-related-information)
  * [Show Organization](/api-reference/ticketing/organizations/organizations/#show-organization)
  * [Show Many Organizations](/api-reference/ticketing/organizations/organizations/#show-many-organizations)
  * [Create Organization](/api-reference/ticketing/organizations/organizations/#create-organization)
  * [Create Many Organizations](/api-reference/ticketing/organizations/organizations/#create-many-organizations)
  * [Create Or Update Organization](/api-reference/ticketing/organizations/organizations/#create-or-update-organization)
  * [Update Organization](/api-reference/ticketing/organizations/organizations/#update-organization)
  * [Update Many Organizations](/api-reference/ticketing/organizations/organizations/#update-many-organizations)
  * [Delete Organization](/api-reference/ticketing/organizations/organizations/#delete-organization)
  * [Bulk Delete Organizations](/api-reference/ticketing/organizations/organizations/#bulk-delete-organizations)
  * [Merge Organization With Another Organization](/api-reference/ticketing/organizations/organizations/#merge-organization-with-another-organization)
  * [Show Organization Merge](/api-reference/ticketing/organizations/organizations/#show-organization-merge)
  * [List Organization Merges](/api-reference/ticketing/organizations/organizations/#list-organization-merges)
  * [Count User's Organizations](/api-reference/ticketing/organizations/organizations/#count-users-organizations)
  * [List User Organizations](/api-reference/ticketing/organizations/organizations/#list-user-organizations)


# Organizations

## On this page

  * [JSON format](/api-reference/ticketing/organizations/organizations/#json-format)
  * [List Organizations](/api-reference/ticketing/organizations/organizations/#list-organizations)
  * [Count Organizations](/api-reference/ticketing/organizations/organizations/#count-organizations)
  * [Autocomplete Organizations](/api-reference/ticketing/organizations/organizations/#autocomplete-organizations)
  * [Search Organizations](/api-reference/ticketing/organizations/organizations/#search-organizations)
  * [Show Organization's Related Information](/api-reference/ticketing/organizations/organizations/#show-organizations-related-information)
  * [Show Organization](/api-reference/ticketing/organizations/organizations/#show-organization)
  * [Show Many Organizations](/api-reference/ticketing/organizations/organizations/#show-many-organizations)
  * [Create Organization](/api-reference/ticketing/organizations/organizations/#create-organization)
  * [Create Many Organizations](/api-reference/ticketing/organizations/organizations/#create-many-organizations)
  * [Create Or Update Organization](/api-reference/ticketing/organizations/organizations/#create-or-update-organization)
  * [Update Organization](/api-reference/ticketing/organizations/organizations/#update-organization)
  * [Update Many Organizations](/api-reference/ticketing/organizations/organizations/#update-many-organizations)
  * [Delete Organization](/api-reference/ticketing/organizations/organizations/#delete-organization)
  * [Bulk Delete Organizations](/api-reference/ticketing/organizations/organizations/#bulk-delete-organizations)
  * [Merge Organization With Another Organization](/api-reference/ticketing/organizations/organizations/#merge-organization-with-another-organization)
  * [Show Organization Merge](/api-reference/ticketing/organizations/organizations/#show-organization-merge)
  * [List Organization Merges](/api-reference/ticketing/organizations/organizations/#list-organization-merges)
  * [Count User's Organizations](/api-reference/ticketing/organizations/organizations/#count-users-organizations)
  * [List User Organizations](/api-reference/ticketing/organizations/organizations/#list-user-organizations)


Just as agents can be segmented into groups in Zendesk Support, your customers (end-users) can be segmented into organizations. You can manually assign customers to an organization or automatically assign them to an organization by their email address domain. Organizations can be used in business rules to route tickets to groups of agents or to send email notifications.

### JSON format

Organizations are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
created_at| string| true| false| The time the organization was created
details| string| false| false| Any details obout the organization, such as the address
domain_names| array| false| false| An array of domain names associated with this organization
external_id| string| false| false| A unique external id to associate organizations to an external record. The id is case-insensitive. For example, "company1" and "Company1" are considered the same
group_id| integer| false| false| New tickets from users in this organization are automatically put in this group
id| integer| false| false| Automatically assigned when the organization is created
name| string| false| true| A unique name for the organization
notes| string| false| false| Any notes you have about the organization
organization_fields| object| false| false| Custom fields for this organization. See [Custom organization fields](/api-reference/ticketing/organizations/organizations/#custom-organization-fields)
shared_comments| boolean| false| false| End users in this organization are able to comment on each other's tickets
shared_tickets| boolean| false| false| End users in this organization are able to see each other's tickets
tags| array| false| false| The tags of the organization
updated_at| string| true| false| The time of the last update of the organization
url| string| true| false| The API url of this organization

#### Custom organization fields

The examples on this page use standard fields for various requests. If you want to use custom organization fields (`organization_fields`) in your updates, see the `organization_fields` property in the following example to properly format your requests.

#### Example


    {  "created_at": "2009-07-20T22:55:29Z",  "details": "This is a kind of organization",  "domain_names": [    "example.com",    "test.com"  ],  "external_id": "ABC123",  "group_id": null,  "id": 35436,  "name": "One Organization",  "notes": "",  "organization_fields": {    "org_decimal": 5.2,    "org_dropdown": "option_1"  },  "shared_comments": true,  "shared_tickets": true,  "tags": [    "enterprise",    "other_tag"  ],  "updated_at": "2011-05-05T10:38:52Z",  "url": "https://company.zendesk.com/api/v2/organizations/35436"}

### List Organizations

  * `GET /api/v2/organizations`


#### Pagination

  * Cursor pagination (recommended)
  * Offset pagination


See [Pagination](/api-reference/introduction/pagination/).

Returns a maximum of 100 records per page.

#### Allowed For

  * Agents, with certain restrictions


If the agent has a custom agent role that restricts their access to only users in their own organization, a 403 Forbidden error is returned. See [Creating custom agent roles](https://support.zendesk.com/hc/en-us/articles/203662026-Creating-custom-roles-and-assigning-agents#topic_cxn_hig_bd) in Zendesk help.

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
include_boundary_indicators| boolean| Query| false| When true, includes `has_more` indicator in the cursor pagination response meta. Only valid with cursor pagination (page[size], page[after], page[before]).
include_item_cursors| boolean| Query| false| When true, includes cursor values for each item in the cursor pagination response. Only valid with cursor pagination (page[size], page[after], page[before]).
page| | Query| false| Pagination parameter. Supports both traditional offset and cursor-based pagination: - Traditional: `?page=2` (integer page number) - Cursor: `?page[size]=50&page[after]=cursor` (deepObject with size, after, before) These are mutually exclusive - use one format or the other, not both.
per_page| integer| Query| false| Number of records to return per page. Note: Default and maximum values vary by endpoint. Check endpoint-specific documentation for limits.
sort| string| Query| false| Field to sort results by. Prefix with `-` for descending order. When used with cursor pagination, this determines the cursor ordering. Example: `?sort=name` or `?sort=-created_at`

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/organizations \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/organizations?include_boundary_indicators=&include_item_cursors=&page=&per_page=50&sort=name"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/organizations")		.newBuilder()		.addQueryParameter("include_boundary_indicators", "")		.addQueryParameter("include_item_cursors", "")		.addQueryParameter("page", "")		.addQueryParameter("per_page", "50")		.addQueryParameter("sort", "name");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/organizations',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'include_boundary_indicators': '',    'include_item_cursors': '',    'page': '',    'per_page': '50',    'sort': 'name',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/organizations?include_boundary_indicators=&include_item_cursors=&page=&per_page=50&sort=name"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/organizations")uri.query = URI.encode_www_form("include_boundary_indicators": "", "include_item_cursors": "", "page": "", "per_page": "50", "sort": "name")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "count": 2,  "next_page": null,  "organizations": [    {      "created_at": "2018-11-14T00:14:52Z",      "details": "caterpillar =)",      "domain_names": [        "remain.com"      ],      "external_id": "ABC198",      "group_id": 1835962,      "id": 4112492,      "name": "Groablet Enterprises",      "notes": "donkey",      "organization_fields": {        "datepudding": "2018-11-04T00:00:00+00:00",        "org_field_1": "happy happy",        "org_field_2": "teapot_kettle"      },      "shared_comments": false,      "shared_tickets": false,      "tags": [        "smiley",        "teapot_kettle"      ],      "updated_at": "2018-11-14T00:54:22Z",      "url": "https://example.zendesk.com/api/v2/organizations/4112492"    },    {      "created_at": "2017-08-14T20:13:52Z",      "details": "test",      "domain_names": [        "test.com"      ],      "external_id": "TTV273",      "group_id": null,      "id": 1873,      "name": "Willy Wonkas Chocolate Factory",      "notes": "",      "organization_fields": {        "datepudding": "2018-11-02T00:00:00+00:00",        "org_field_1": "malarky",        "org_field_2": "teapot_kettle"      },      "shared_comments": false,      "shared_tickets": false,      "tags": [        "teapot_kettle"      ],      "updated_at": "2019-05-16T01:27:46Z",      "url": "https://example.zendesk.com.com/api/v2/organizations/1873"    }  ],  "previous_page": null}

### Count Organizations

  * `GET /api/v2/organizations/count`


Returns an approximate count of organizations. If the count exceeds 100,000, it is updated every 24 hours.

The `refreshed_at` property of the `count` object is a timestamp that indicates when the count was last updated.

When the count exceeds 100,000, the `refreshed_at` property may occasionally be null. This indicates that the count is being updated in the background and the `value` property of the `count` object is limited to 100,000 until the update is complete.

#### Allowed For

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
include_boundary_indicators| boolean| Query| false| When true, includes `has_more` indicator in the cursor pagination response meta. Only valid with cursor pagination (page[size], page[after], page[before]).
include_item_cursors| boolean| Query| false| When true, includes cursor values for each item in the cursor pagination response. Only valid with cursor pagination (page[size], page[after], page[before]).

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/organizations/count \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/organizations/count?include_boundary_indicators=&include_item_cursors="	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/organizations/count")		.newBuilder()		.addQueryParameter("include_boundary_indicators", "")		.addQueryParameter("include_item_cursors", "");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/organizations/count',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'include_boundary_indicators': '',    'include_item_cursors': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/organizations/count?include_boundary_indicators=&include_item_cursors="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/organizations/count")uri.query = URI.encode_www_form("include_boundary_indicators": "", "include_item_cursors": "")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "count": {    "refreshed_at": "2020-04-06T02:18:17Z",    "value": 102  }}

### Autocomplete Organizations

  * `GET /api/v2/organizations/autocomplete?name={name}`


Returns an array of organizations whose name starts with the value specified in the `name` parameter.

#### Pagination

  * Offset pagination only


See [Using Offset Pagination](/api-reference/introduction/pagination/#using-offset-pagination).

#### Allowed For

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
field_id| string| Query| false| The id of a lookup relationship field. The type of field is determined by the `source` param
include_boundary_indicators| boolean| Query| false| When true, includes `has_more` indicator in the cursor pagination response meta. Only valid with cursor pagination (page[size], page[after], page[before]).
include_item_cursors| boolean| Query| false| When true, includes cursor values for each item in the cursor pagination response. Only valid with cursor pagination (page[size], page[after], page[before]).
name| string| Query| true| A substring of an organization to search for
source| string| Query| false| If a `field_id` is provided, this specifies the type of the field. For example, if the field is on a "zen:user", it references a field on a user

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/organizations/autocomplete?name=imp \  -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/organizations/autocomplete?field_id=&include_boundary_indicators=&include_item_cursors=&name=imp&source="	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/organizations/autocomplete")		.newBuilder()		.addQueryParameter("field_id", "")		.addQueryParameter("include_boundary_indicators", "")		.addQueryParameter("include_item_cursors", "")		.addQueryParameter("name", "imp")		.addQueryParameter("source", "");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/organizations/autocomplete',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'field_id': '',    'include_boundary_indicators': '',    'include_item_cursors': '',    'name': 'imp',    'source': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/organizations/autocomplete?field_id=&include_boundary_indicators=&include_item_cursors=&name=imp&source="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/organizations/autocomplete")uri.query = URI.encode_www_form("field_id": "", "include_boundary_indicators": "", "include_item_cursors": "", "name": "imp", "source": "")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "count": 2,  "next_page": null,  "organizations": [    {      "created_at": "2018-11-14T00:14:52Z",      "details": "caterpillar =)",      "domain_names": [        "remain.com"      ],      "external_id": null,      "group_id": 1835962,      "id": 35436,      "name": "Important Customers",      "notes": "donkey",      "organization_fields": {        "datepudding": "2018-11-04T00:00:00+00:00",        "org_field_1": "happy happy",        "org_field_2": "teapot_kettle"      },      "shared_comments": false,      "shared_tickets": false,      "tags": [        "smiley",        "teapot_kettle"      ],      "updated_at": "2018-11-14T00:54:22Z",      "url": "https://example.zendesk.com/api/v2/organizations/4112492"    },    {      "created_at": "2017-08-14T20:13:52Z",      "details": "test",      "domain_names": [        "test.com"      ],      "external_id": null,      "group_id": null,      "id": 20057623,      "name": "Imperial College",      "notes": "",      "organization_fields": {        "datepudding": "2018-11-02T00:00:00+00:00",        "org_field_1": "malarky",        "org_field_2": "teapot_kettle"      },      "shared_comments": false,      "shared_tickets": false,      "tags": [        "teapot_kettle"      ],      "updated_at": "2019-05-16T01:27:46Z",      "url": "https://example.zendesk.com.com/api/v2/organizations/1873"    }  ],  "previous_page": null}

**400 Bad Request**


    // Status 400 Bad Request
    {  "errors": [    {      "code": "QueryError",      "title": "Invalid type:sample_type"    }  ]}

**429 Too Many Requests**


    // Status 429 Too Many Requests
    {  "errors": [    {      "code": "TooManyRequests",      "title": "Too many requests to autocomplete"    }  ]}

### Search Organizations

  * `GET /api/v2/organizations/search`


Returns an array of organizations matching the criteria. You may search by an organization's `external_id` or `name`, but not both:

#### Searching by `external_id`

If you set the `external_id` value of an organization to associate it to an external record, you can use it to search for the organization.

For an organization to be returned, its `external_id` must exactly match the value provided (case insensitive).

#### Searching by `name`

For an organization to be returned, its `name` must exactly match the value provided (case insensitive).

#### Allowed For:

  * Admins
  * Agents assigned to a custom role with permissions to add or modify organizations (Enterprise only)


See [Creating custom agent roles](https://support.zendesk.com/hc/en-us/articles/203662026#topic_cxn_hig_bd) in the Support Help Center.

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
external_id| integer| Query| false| The external id of an organization
name| string| Query| false| The name of an organization

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/organizations/search?external_id={external_id} \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/organizations/search?external_id=1234&name=ACME+Incorporated"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/organizations/search")		.newBuilder()		.addQueryParameter("external_id", "1234")		.addQueryParameter("name", "ACME Incorporated");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/organizations/search',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'external_id': '1234',    'name': 'ACME+Incorporated',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/organizations/search?external_id=1234&name=ACME+Incorporated"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/organizations/search")uri.query = URI.encode_www_form("external_id": "1234", "name": "ACME Incorporated")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "count": 2,  "next_page": null,  "organizations": [    {      "created_at": "2018-11-14T00:14:52Z",      "details": "caterpillar =)",      "domain_names": [        "remain.com"      ],      "external_id": "ABC198",      "group_id": 1835962,      "id": 4112492,      "name": "Groablet Enterprises",      "notes": "donkey",      "organization_fields": {        "datepudding": "2018-11-04T00:00:00+00:00",        "org_field_1": "happy happy",        "org_field_2": "teapot_kettle"      },      "shared_comments": false,      "shared_tickets": false,      "tags": [        "smiley",        "teapot_kettle"      ],      "updated_at": "2018-11-14T00:54:22Z",      "url": "https://example.zendesk.com/api/v2/organizations/4112492"    },    {      "created_at": "2017-08-14T20:13:52Z",      "details": "test",      "domain_names": [        "test.com"      ],      "external_id": "TTV273",      "group_id": null,      "id": 1873,      "name": "Willy Wonkas Chocolate Factory",      "notes": "",      "organization_fields": {        "datepudding": "2018-11-02T00:00:00+00:00",        "org_field_1": "malarky",        "org_field_2": "teapot_kettle"      },      "shared_comments": false,      "shared_tickets": false,      "tags": [        "teapot_kettle"      ],      "updated_at": "2019-05-16T01:27:46Z",      "url": "https://example.zendesk.com.com/api/v2/organizations/1873"    }  ],  "previous_page": null}

### Show Organization's Related Information

  * `GET /api/v2/organizations/{organization_id}/related`


#### Allowed For

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
organization_id| integer| Path| true| The ID of an organization

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/organizations/{organization_id}/related \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/organizations/16/related"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/organizations/16/related")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/organizations/16/related',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/organizations/16/related"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/organizations/16/related")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "organization_related": {    "tickets_count": 12,    "users_count": 4  }}

### Show Organization

  * `GET /api/v2/organizations/{organization_id}`


#### Allowed For

  * Admins
  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
include| string| Query| false| Include additional related data. Supported values: `lookup_relationship_fields`.
include_boundary_indicators| boolean| Query| false| When true, includes `has_more` indicator in the cursor pagination response meta. Only valid with cursor pagination (page[size], page[after], page[before]).
include_item_cursors| boolean| Query| false| When true, includes cursor values for each item in the cursor pagination response. Only valid with cursor pagination (page[size], page[after], page[before]).
organization_id| integer| Path| true| The ID of an organization

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/organizations/{organization_id} \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/organizations/16?include=&include_boundary_indicators=&include_item_cursors="	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/organizations/16")		.newBuilder()		.addQueryParameter("include", "")		.addQueryParameter("include_boundary_indicators", "")		.addQueryParameter("include_item_cursors", "");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/organizations/16',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'include': '',    'include_boundary_indicators': '',    'include_item_cursors': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/organizations/16?include=&include_boundary_indicators=&include_item_cursors="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/organizations/16")uri.query = URI.encode_www_form("include": "", "include_boundary_indicators": "", "include_item_cursors": "")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "organization": {    "created_at": "2018-11-14T00:14:52Z",    "details": "caterpillar =)",    "domain_names": [      "remain.com"    ],    "external_id": null,    "group_id": 1835962,    "id": 4112492,    "name": "Groablet Enterprises",    "notes": "donkey",    "organization_fields": {      "datepudding": "2018-11-04T00:00:00+00:00",      "org_field_1": "happy happy",      "org_field_2": "teapot_kettle"    },    "shared_comments": false,    "shared_tickets": false,    "tags": [      "smiley",      "teapot_kettle"    ],    "updated_at": "2018-11-14T00:54:22Z",    "url": "https://example.zendesk.com/api/v2/organizations/4112492"  }}

### Show Many Organizations

  * `GET /api/v2/organizations/show_many`


Accepts a comma-separated list of up to 100 organization ids or external ids.

#### Allowed For

  * Admins
  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
external_ids| string| Query| false| A list of external ids
ids| string| Query| false| A list of organization ids

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/organizations/show_many?ids=35436,20057623 \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/organizations/show_many?external_ids=1764%2C42156&ids=35436%2C20057623"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/organizations/show_many")		.newBuilder()		.addQueryParameter("external_ids", "1764,42156")		.addQueryParameter("ids", "35436,20057623");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/organizations/show_many',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'external_ids': '1764%2C42156',    'ids': '35436%2C20057623',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/organizations/show_many?external_ids=1764%2C42156&ids=35436%2C20057623"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/organizations/show_many")uri.query = URI.encode_www_form("external_ids": "1764,42156", "ids": "35436,20057623")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "count": 2,  "next_page": null,  "organizations": [    {      "created_at": "2018-11-14T00:14:52Z",      "details": "caterpillar =)",      "domain_names": [        "remain.com"      ],      "external_id": null,      "group_id": 1835962,      "id": 35436,      "name": "Important Customers",      "notes": "donkey",      "organization_fields": {        "datepudding": "2018-11-04T00:00:00+00:00",        "org_field_1": "happy happy",        "org_field_2": "teapot_kettle"      },      "shared_comments": false,      "shared_tickets": false,      "tags": [        "smiley",        "teapot_kettle"      ],      "updated_at": "2018-11-14T00:54:22Z",      "url": "https://example.zendesk.com/api/v2/organizations/4112492"    },    {      "created_at": "2017-08-14T20:13:52Z",      "details": "test",      "domain_names": [        "test.com"      ],      "external_id": null,      "group_id": null,      "id": 20057623,      "name": "Imperial College",      "notes": "",      "organization_fields": {        "datepudding": "2018-11-02T00:00:00+00:00",        "org_field_1": "malarky",        "org_field_2": "teapot_kettle"      },      "shared_comments": false,      "shared_tickets": false,      "tags": [        "teapot_kettle"      ],      "updated_at": "2019-05-16T01:27:46Z",      "url": "https://example.zendesk.com.com/api/v2/organizations/1873"    }  ],  "previous_page": null}

### Create Organization

  * `POST /api/v2/organizations`


You must provide a unique `name` for each organization. Normally the system doesn't allow records to be created with identical names. However, a race condition can occur if you make two or more identical POSTs very close to each other, causing the records to have identical organization names.

**Note** : Leading and trailing whitespace in `name` is automatically trimmed before validation. This means that names differing only by whitespace are treated as duplicates. For example, "API Company" and "API Company " are considered the same name.

#### Allowed For

  * Admins
  * Agents assigned to a custom role with permissions to manage organizations (Enterprise only)


#### Example body


    {  "organization": {    "name": "My Organization"  }}

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/organizations \  -H "Content-Type: application/json" -d '{"organization": {"name": "My Organization"}}' \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://example.zendesk.com/api/v2/organizations"	method := "POST"	payload := strings.NewReader(`{  "organization": {    "name": "My Organization"  }}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/organizations")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"organization\": {    \"name\": \"My Organization\"  }}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "organization": {    "name": "My Organization"  }});
    var config = {  method: 'POST',  url: 'https://example.zendesk.com/api/v2/organizations',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/organizations"
    payload = json.loads("""{  "organization": {    "name": "My Organization"  }}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/organizations")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")request.body = %q({  "organization": {    "name": "My Organization"  }})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**201 Created**


    // Status 201 Created
    {  "organization": {    "created_at": "2020-09-30T01:50:12Z",    "details": null,    "domain_names": [],    "external_id": null,    "group_id": null,    "id": 23409462,    "name": "My Organization",    "notes": null,    "organization_fields": null,    "shared_comments": false,    "shared_tickets": false,    "tags": [],    "updated_at": "2020-09-30T01:50:12Z",    "url": "https://example.zendesk.com/api/v2/organizations/23409462"  }}

### Create Many Organizations

  * `POST /api/v2/organizations/create_many`


Accepts an array of up to 100 organization objects.

#### Response

This endpoint returns a `job_status` [JSON object](/api-reference/ticketing/ticket-management/job_statuses/#json-format) and queues a background job to do the work. Use the [Show Job Status](/api-reference/ticketing/ticket-management/job_statuses/#show-job-status) endpoint to check for the job's completion. Only a certain number of jobs can be queued or running at the same time. See [Job limit](/api-reference/introduction/rate-limits/#job-limit) for more information.

#### Allowed For

  * Agents, with restrictions applying on certain actions


#### Code Samples

**curl**


    curl -v -u {email_address}/token:{api_token} https://{subdomain}.zendesk.com/api/v2/organizations/create_many \  -H "Content-Type: application/json" -X POST -d '{"organizations": [{"name": "Org1"}, {"name": "Org2"}]}'

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/organizations/create_many"	method := "POST"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/organizations/create_many")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'POST',  url: 'https://example.zendesk.com/api/v2/organizations/create_many',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/organizations/create_many"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/organizations/create_many")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "job_status": {    "id": "8b726e606741012ffc2d782bcb7848fe",    "message": "Completed at Fri Apr 13 02:51:53 +0000 2012",    "progress": 2,    "results": [      {        "action": "update",        "id": 380,        "status": "Updated",        "success": true      }    ],    "status": "completed",    "total": 2,    "url": "https://company.zendesk.com/api/v2/job_statuses/8b726e606741012ffc2d782bcb7848fe"  }}

### Create Or Update Organization

  * `POST /api/v2/organizations/create_or_update`


Creates an organization if it doesn't already exist, or updates an existing organization. Using this method means one less call to check if an organization exists before creating it. You need to specify the id or external id when updating an organization to avoid a duplicate error response. Name is not available as a matching criteria.

#### Allowed For

  * Agents, with restrictions on certain actions


#### Code Samples

**curl**

Existing organization identified by ID


    curl -v -u {email_address}/token:{api_token} https://{subdomain}.zendesk.com/api/v2/organizations/create_or_update \  -H "Content-Type: application/json" -X POST -d '{"organization": {"id": "123", "name": "My Organization"}}'

**curl**

Existing organization identified by external ID


    curl -v -u {email_address}/token:{api_token} https://{subdomain}.zendesk.com/api/v2/organizations/create_or_update \  -H "Content-Type: application/json" -X POST -d '{"organization": {"external_id": "abc_123", "name": "My Organization"}}'

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/organizations/create_or_update"	method := "POST"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/organizations/create_or_update")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'POST',  url: 'https://example.zendesk.com/api/v2/organizations/create_or_update',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/organizations/create_or_update"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/organizations/create_or_update")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "organization": {    "created_at": "2020-09-30T01:50:12Z",    "details": null,    "domain_names": [],    "external_id": null,    "group_id": null,    "id": 23409462,    "name": "My Organization",    "notes": null,    "organization_fields": null,    "shared_comments": false,    "shared_tickets": false,    "tags": [],    "updated_at": "2020-09-30T01:50:12Z",    "url": "https://example.zendesk.com/api/v2/organizations/23409462"  }}

**201 Created**


    // Status 201 Created
    {  "organization": {    "created_at": "2020-09-30T01:50:12Z",    "details": null,    "domain_names": [],    "external_id": null,    "group_id": null,    "id": 23409462,    "name": "My Organization",    "notes": null,    "organization_fields": null,    "shared_comments": false,    "shared_tickets": false,    "tags": [],    "updated_at": "2020-09-30T01:50:12Z",    "url": "https://example.zendesk.com/api/v2/organizations/23409462"  }}

### Update Organization

  * `PUT /api/v2/organizations/{organization_id}`


#### Allowed For

  * Admins
  * Agents


Agents with no permissions restrictions can only update "notes" on organizations.

**Note:** Updating an organization's `domain_names` property overwrites all existing `domain_names` values. To prevent this, submit a complete list of `domain_names` for the organization in your request.

#### Example Request


    {  "organization": {    "notes": "Something interesting"  }}

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
organization_id| integer| Path| true| The ID of an organization

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/organizations/{organization_id} \  -H "Content-Type: application/json" -d '{"organization": {"notes": "Something interesting"}}' \  -v -u {email_address}/token:{api_token} -X PUT

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/organizations/16"	method := "PUT"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/organizations/16")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'PUT',  url: 'https://example.zendesk.com/api/v2/organizations/16',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/organizations/16"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/organizations/16")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "organization": {    "created_at": "2018-11-14T00:14:52Z",    "details": "caterpillar =)",    "domain_names": [      "remain.com"    ],    "external_id": null,    "group_id": 1835962,    "id": 4112492,    "name": "Groablet Enterprises",    "notes": "Something Interesting",    "organization_fields": {      "datepudding": "2018-11-04T00:00:00+00:00",      "org_field_1": "happy happy",      "org_field_2": "teapot_kettle"    },    "shared_comments": false,    "shared_tickets": false,    "tags": [      "smiley",      "teapot_kettle"    ],    "updated_at": "2018-11-14T00:54:22Z",    "url": "https://example.zendesk.com/api/v2/organizations/4112492"  }}

**429 Too Many Requests**


    // Status 429 Too Many Requests
    {  "errors": [    {      "code": "TooManyRequests",      "title": "Too many requests to update"    }  ]}

### Update Many Organizations

  * `PUT /api/v2/organizations/update_many`


Bulk or batch updates up to 100 organizations.

#### Bulk update

To make the same change to multiple organizations, use the following endpoint and data format:

`https://{subdomain}.zendesk.com/api/v2/organizations/update_many?ids=1,2,3`


    {  "organization": {    "notes": "Priority"  }}

#### Batch update

To make different changes to multiple organizations, use the following endpoint and data format:

`https://{subdomain}.zendesk.com/api/v2/organizations/update_many`


    {  "organizations": [    { "id": 1, "notes": "Priority" },    { "id": 2, "notes": "Normal" }  ]}

#### Response

This endpoint returns a `job_status` [JSON object](/api-reference/ticketing/ticket-management/job_statuses/#json-format) and queues a background job to do the work. Use the [Show Job Status](/api-reference/ticketing/ticket-management/job_statuses/#show-job-status) endpoint to check for the job's completion. Only a certain number of jobs can be queued or running at the same time. See [Job limit](/api-reference/introduction/rate-limits/#job-limit) for more information.

#### Allowed For

  * Admins
  * Agents


Agents with no permissions restrictions can only update "notes" on organizations.

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
external_ids| string| Query| false| A list of external ids
ids| string| Query| false| A list of organization ids

#### Code Samples

**curl**

Specifying existing organizations by query parameter


    curl https://{subdomain}.zendesk.com/api/v2/organizations/update_many?ids=1,2 \  -H "Content-Type: application/json" \  -v -u {email_address}/token:{api_token} -X PUT \  -d '{"organization": {"notes": "Something interesting"}}'

**curl**

Specifying existing organizations by payload


    curl https://{subdomain}.zendesk.com/api/v2/organizations/update_many \  -H "Content-Type: application/json" \  -v -u {email_address}/token:{api_token} -X PUT \  -d '{"organizations": [{"id": "1", "notes": "Something interesting"}, {"external_id": "2", "notes": "Something even more interesting"}]}'

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/organizations/update_many?external_ids=1764%2C42156&ids=35436%2C20057623"	method := "PUT"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/organizations/update_many")		.newBuilder()		.addQueryParameter("external_ids", "1764,42156")		.addQueryParameter("ids", "35436,20057623");RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'PUT',  url: 'https://example.zendesk.com/api/v2/organizations/update_many',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'external_ids': '1764%2C42156',    'ids': '35436%2C20057623',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/organizations/update_many?external_ids=1764%2C42156&ids=35436%2C20057623"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/organizations/update_many")uri.query = URI.encode_www_form("external_ids": "1764,42156", "ids": "35436,20057623")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "job_status": {    "id": "8b726e606741012ffc2d782bcb7848fe",    "message": "Completed at Fri Apr 13 02:51:53 +0000 2012",    "progress": 2,    "results": [      {        "action": "update",        "id": 380,        "status": "Updated",        "success": true      }    ],    "status": "completed",    "total": 2,    "url": "https://company.zendesk.com/api/v2/job_statuses/8b726e606741012ffc2d782bcb7848fe"  }}

### Delete Organization

  * `DELETE /api/v2/organizations/{organization_id}`


#### Allowed For

  * Admins
  * Agents assigned to a custom role with permissions to manage organizations (Enterprise only)


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
organization_id| integer| Path| true| The ID of an organization

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/organizations/{organization_id} \  -v -u {email_address}/token:{api_token} -X DELETE

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/organizations/16"	method := "DELETE"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/organizations/16")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("DELETE", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'DELETE',  url: 'https://example.zendesk.com/api/v2/organizations/16',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/organizations/16"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"DELETE",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/organizations/16")request = Net::HTTP::Delete.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**204 No Content**


    // Status 204 No Content
    null

### Bulk Delete Organizations

  * `DELETE /api/v2/organizations/destroy_many`


Accepts a comma-separated list of up to 100 organization ids or external ids.

#### Response

This endpoint returns a `job_status` [JSON object](/api-reference/ticketing/ticket-management/job_statuses/#json-format) and queues a background job to do the work. Use the [Show Job Status](/api-reference/ticketing/ticket-management/job_statuses/#show-job-status) endpoint to check for the job's completion. Only a certain number of jobs can be queued or running at the same time. See [Job limit](/api-reference/introduction/rate-limits/#job-limit) for more information.

#### Allowed For

  * Admins
  * Agents assigned to a custom role with permissions to manage organizations (Enterprise only)


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
external_ids| string| Query| false| A list of external ids
ids| string| Query| false| A list of organization ids

#### Code Samples

**curl**

Existing organizations identified by ID


    curl https://{subdomain}.zendesk.com/api/v2/organizations/destroy_many?ids=1,2,3 \  -v -u {email_address}/token:{api_token} -X DELETE

**curl**

Existing organizations identified by external ID


    curl https://{subdomain}.zendesk.com/api/v2/organizations/destroy_many?external_ids=1,2,3 \  -v -u {email_address}/token:{api_token} -X DELETE

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/organizations/destroy_many?external_ids=1764%2C42156&ids=35436%2C20057623"	method := "DELETE"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/organizations/destroy_many")		.newBuilder()		.addQueryParameter("external_ids", "1764,42156")		.addQueryParameter("ids", "35436,20057623");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("DELETE", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'DELETE',  url: 'https://example.zendesk.com/api/v2/organizations/destroy_many',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'external_ids': '1764%2C42156',    'ids': '35436%2C20057623',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/organizations/destroy_many?external_ids=1764%2C42156&ids=35436%2C20057623"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"DELETE",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/organizations/destroy_many")uri.query = URI.encode_www_form("external_ids": "1764,42156", "ids": "35436,20057623")request = Net::HTTP::Delete.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "job_status": {    "id": "82de0b044094f0c67893ac9fe64f1a99",    "message": "Completed at 2018-03-08 10:07:04 +0000",    "progress": 2,    "results": [      {        "action": "delete",        "id": 244,        "status": "Deleted",        "success": true      },      {        "action": "delete",        "id": 245,        "status": "Deleted",        "success": true      }    ],    "status": "completed",    "total": 2,    "url": "https://example.zendesk.com/api/v2/job_statuses/82de0b0467893ac9fe64f1a99"  }}

### Merge Organization With Another Organization

  * `POST /api/v2/organizations/{organization_id}/merge`


Merges two organizations by moving all users, tickets, and domain names from the organization specified by `{organization_id}` to the organization specified by `winner_id`. After the merge:

  * The "losing" organization will be deleted.
  * Other organization fields and their values will not be carried over to the "winning" organization.
  * The merge operation creates an `Organization Merge` record which contains a status indicating the progress of the merge.


**Note** : This operation is irreversible.

#### Merge Statuses

Status| Description
---|---
new| A job has been queued to merge the two organizations.
in progress| The job to merge the two organizations has started.
error| An error occurred during the merge job. The merge can be retried by repeating the API call.
complete| The merge has been completed successfully.

#### Allowed For

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
organization_id| integer| Path| true| The ID of an organization

#### Example body


    {  "organization_merge": {    "winner_id": 54321  }}

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/organizations/{organization_id}/merge \  -H "Content-Type: application/json" -d '{"organization_merge": {"winner_id": 4321}}' \  -X POST -v -u {email_address}/token:{API_token}

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://example.zendesk.com/api/v2/organizations/16/merge"	method := "POST"	payload := strings.NewReader(`{  "organization_merge": {    "winner_id": 54321  }}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/organizations/16/merge")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"organization_merge\": {    \"winner_id\": 54321  }}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "organization_merge": {    "winner_id": 54321  }});
    var config = {  method: 'POST',  url: 'https://example.zendesk.com/api/v2/organizations/16/merge',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/organizations/16/merge"
    payload = json.loads("""{  "organization_merge": {    "winner_id": 54321  }}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/organizations/16/merge")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")request.body = %q({  "organization_merge": {    "winner_id": 54321  }})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "organization_merge": {    "id": "01HPZM6206BF4G63783E5349AD",    "loser_id": 123,    "status": "new",    "url": "https://company.zendesk.com/api/v2/organization_merges/01HPZM6206BF4G63783E5349AD",    "winner_id": 456  }}

### Show Organization Merge

  * `GET /api/v2/organization_merges/{organization_merge_id}`


Retrieves the details of a specific organization merge operation. This endpoint is useful for obtaining the status and outcome of a merge that was previously initiated. It provides information such as the winning and losing organization IDs, the status of the merge, and the associated URLs.

This endpoint can be used to determine if a merge is still in progress, has completed successfully, or has encountered an error.

#### Allowed For

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
organization_merge_id| string| Path| true| The ID of the organization merge

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/organization_merges/{id} \  -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/organization_merges/01HPZM6206BF4G63783E5349AD"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/organization_merges/01HPZM6206BF4G63783E5349AD")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/organization_merges/01HPZM6206BF4G63783E5349AD',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/organization_merges/01HPZM6206BF4G63783E5349AD"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/organization_merges/01HPZM6206BF4G63783E5349AD")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "organization_merge": {    "id": "01HPZM6206BF4G63783E5349AD",    "loser_id": 123,    "status": "new",    "url": "https://company.zendesk.com/api/v2/organization_merges/01HPZM6206BF4G63783E5349AD",    "winner_id": 456  }}

### List Organization Merges

  * `GET /api/v2/organizations/{organization_id}/merges`


Retrieves a list of all organization merge operations associated with a given organization. This endpoint allows you to track the history of merge actions for an organization, including ongoing and completed merges.

Each entry in the list contains details such as the ID of the merge, the winning and losing organization IDs, the current status of the merge, and a URL to access the `Organization Merge` record.

#### Pagination

  * Cursor pagination is used for this endpoint.
  * A maximum of 100 records can be returned per page.


See [Pagination](/api-reference/introduction/pagination/) for more details.

#### Allowed For

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
organization_id| integer| Path| true| The ID of an organization

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/organizations/{id}/merges \  -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/organizations/16/merges"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/organizations/16/merges")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/organizations/16/merges',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/organizations/16/merges"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/organizations/16/merges")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "organization_merges": [    {      "id": "01HPZM6206BF4G63783E5349AD",      "loser_id": 123,      "status": "complete",      "url": "https://company.zendesk.com/api/v2/organization_merges/01HPZM6206BF4G63783E5349AD",      "winner_id": 456    }  ]}

### Count User's Organizations

  * `GET /api/v2/users/{user_id}/organizations/count`


Returns an approximate count of organizations for a specific user. If the count exceeds 100,000, it is updated every 24 hours.

The `refreshed_at` property of the `count` object is a timestamp that indicates when the count was last updated.

When the count exceeds 100,000, the `refreshed_at` property may occasionally be null. This indicates that the count is being updated in the background and the `value` property of the `count` object is limited to 100,000 until the update is complete.

#### Allowed For

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
user_id| integer| Path| true| The id of the user

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/users/{user_id}/organizations/count \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/users/35436/organizations/count"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/users/35436/organizations/count")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/users/35436/organizations/count',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/users/35436/organizations/count"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/users/35436/organizations/count")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "count": {    "refreshed_at": "2020-04-06T02:18:17Z",    "value": 102  }}

### List User Organizations

  * `GET /api/v2/users/{user_id}/organizations`


Returns a list of organizations associated with the specified user.

#### Pagination

  * Cursor pagination (recommended)
  * Offset pagination


See [Pagination](/api-reference/introduction/pagination/).

Returns a maximum of 100 records per page.

#### Allowed For

  * Agents, with certain restrictions


If the agent has a custom agent role that restricts their access to only users in their own organization, a 403 Forbidden error is returned. See [Creating custom agent roles](https://support.zendesk.com/hc/en-us/articles/203662026-Creating-custom-roles-and-assigning-agents#topic_cxn_hig_bd) in Zendesk help.

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
include_boundary_indicators| boolean| Query| false| When true, includes `has_more` indicator in the cursor pagination response meta. Only valid with cursor pagination (page[size], page[after], page[before]).
include_item_cursors| boolean| Query| false| When true, includes cursor values for each item in the cursor pagination response. Only valid with cursor pagination (page[size], page[after], page[before]).
page| | Query| false| Pagination parameter. Supports both traditional offset and cursor-based pagination: - Traditional: `?page=2` (integer page number) - Cursor: `?page[size]=50&page[after]=cursor` (deepObject with size, after, before) These are mutually exclusive - use one format or the other, not both.
per_page| integer| Query| false| Number of records to return per page. Note: Default and maximum values vary by endpoint. Check endpoint-specific documentation for limits.
sort| string| Query| false| Field to sort results by. Prefix with `-` for descending order. When used with cursor pagination, this determines the cursor ordering. Example: `?sort=name` or `?sort=-created_at`
user_id| integer| Path| true| The id of the user

#### Code Samples

**cURL**


    curl https://{subdomain}.zendesk.com/api/v2/users/{user_id}/organizations \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/users/35436/organizations?include_boundary_indicators=&include_item_cursors=&page=&per_page=50&sort=name"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/users/35436/organizations")		.newBuilder()		.addQueryParameter("include_boundary_indicators", "")		.addQueryParameter("include_item_cursors", "")		.addQueryParameter("page", "")		.addQueryParameter("per_page", "50")		.addQueryParameter("sort", "name");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/users/35436/organizations',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'include_boundary_indicators': '',    'include_item_cursors': '',    'page': '',    'per_page': '50',    'sort': 'name',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/users/35436/organizations?include_boundary_indicators=&include_item_cursors=&page=&per_page=50&sort=name"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/users/35436/organizations")uri.query = URI.encode_www_form("include_boundary_indicators": "", "include_item_cursors": "", "page": "", "per_page": "50", "sort": "name")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "count": 2,  "next_page": null,  "organizations": [    {      "created_at": "2018-11-14T00:14:52Z",      "details": "caterpillar =)",      "domain_names": [        "remain.com"      ],      "external_id": "ABC198",      "group_id": 1835962,      "id": 4112492,      "name": "Groablet Enterprises",      "notes": "donkey",      "organization_fields": {        "datepudding": "2018-11-04T00:00:00+00:00",        "org_field_1": "happy happy",        "org_field_2": "teapot_kettle"      },      "shared_comments": false,      "shared_tickets": false,      "tags": [        "smiley",        "teapot_kettle"      ],      "updated_at": "2018-11-14T00:54:22Z",      "url": "https://example.zendesk.com/api/v2/organizations/4112492"    },    {      "created_at": "2017-08-14T20:13:52Z",      "details": "test",      "domain_names": [        "test.com"      ],      "external_id": "TTV273",      "group_id": null,      "id": 1873,      "name": "Willy Wonkas Chocolate Factory",      "notes": "",      "organization_fields": {        "datepudding": "2018-11-02T00:00:00+00:00",        "org_field_1": "malarky",        "org_field_2": "teapot_kettle"      },      "shared_comments": false,      "shared_tickets": false,      "tags": [        "teapot_kettle"      ],      "updated_at": "2019-05-16T01:27:46Z",      "url": "https://example.zendesk.com.com/api/v2/organizations/1873"    }  ],  "previous_page": null}

**403 Forbidden**


    // Status 403 Forbidden
    {  "error": "Forbidden"}

**404 Not Found**


    // Status 404 Not Found
    {  "error": "RecordNotFound"}

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)