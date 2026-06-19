# Ticket Forms

*Source: https://developer.zendesk.com/api-reference/ticketing/tickets/ticket_forms/*

---

## On this page

  * [JSON format](/api-reference/ticketing/tickets/ticket_forms/#json-format)
  * [List Ticket Forms](/api-reference/ticketing/tickets/ticket_forms/#list-ticket-forms)
  * [Show Ticket Form](/api-reference/ticketing/tickets/ticket_forms/#show-ticket-form)
  * [Show Many Ticket Forms](/api-reference/ticketing/tickets/ticket_forms/#show-many-ticket-forms)
  * [Create Ticket Form](/api-reference/ticketing/tickets/ticket_forms/#create-ticket-form)
  * [Update Ticket Form](/api-reference/ticketing/tickets/ticket_forms/#update-ticket-form)
  * [Delete Ticket Form](/api-reference/ticketing/tickets/ticket_forms/#delete-ticket-form)
  * [Clone an Already Existing Ticket Form](/api-reference/ticketing/tickets/ticket_forms/#clone-an-already-existing-ticket-form)
  * [Reorder Ticket Forms](/api-reference/ticketing/tickets/ticket_forms/#reorder-ticket-forms)
  * [List Ticket Form Statuses of a Ticket Form](/api-reference/ticketing/tickets/ticket_forms/#list-ticket-form-statuses-of-a-ticket-form)
  * [Create Ticket Form Statuses](/api-reference/ticketing/tickets/ticket_forms/#create-ticket-form-statuses)
  * [Bulk Update Ticket Form Statuses of a Ticket Form](/api-reference/ticketing/tickets/ticket_forms/#bulk-update-ticket-form-statuses-of-a-ticket-form)
  * [Update Ticket Form Status By Id](/api-reference/ticketing/tickets/ticket_forms/#update-ticket-form-status-by-id)


# Ticket Forms

## On this page

  * [JSON format](/api-reference/ticketing/tickets/ticket_forms/#json-format)
  * [List Ticket Forms](/api-reference/ticketing/tickets/ticket_forms/#list-ticket-forms)
  * [Show Ticket Form](/api-reference/ticketing/tickets/ticket_forms/#show-ticket-form)
  * [Show Many Ticket Forms](/api-reference/ticketing/tickets/ticket_forms/#show-many-ticket-forms)
  * [Create Ticket Form](/api-reference/ticketing/tickets/ticket_forms/#create-ticket-form)
  * [Update Ticket Form](/api-reference/ticketing/tickets/ticket_forms/#update-ticket-form)
  * [Delete Ticket Form](/api-reference/ticketing/tickets/ticket_forms/#delete-ticket-form)
  * [Clone an Already Existing Ticket Form](/api-reference/ticketing/tickets/ticket_forms/#clone-an-already-existing-ticket-form)
  * [Reorder Ticket Forms](/api-reference/ticketing/tickets/ticket_forms/#reorder-ticket-forms)
  * [List Ticket Form Statuses of a Ticket Form](/api-reference/ticketing/tickets/ticket_forms/#list-ticket-form-statuses-of-a-ticket-form)
  * [Create Ticket Form Statuses](/api-reference/ticketing/tickets/ticket_forms/#create-ticket-form-statuses)
  * [Bulk Update Ticket Form Statuses of a Ticket Form](/api-reference/ticketing/tickets/ticket_forms/#bulk-update-ticket-form-statuses-of-a-ticket-form)
  * [Update Ticket Form Status By Id](/api-reference/ticketing/tickets/ticket_forms/#update-ticket-form-status-by-id)


Ticket forms allow an admin to define a subset of ticket fields for display to both agents and end users. Accounts are limited to 300 ticket forms.

Ticket forms are supported on Suite Growth plans and above, as well as on Support Enterprise plans.

For legacy accounts, ticket forms are only available on Enterprise accounts or accounts with the [Productivity Pack add-on](https://support.zendesk.com/hc/en-us/articles/4408889260186).

### JSON format

Ticket Forms are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
active| boolean| false| false| If the form is set as active
agent_conditions| array| false| false| Array of condition sets for agent workspaces
created_at| string| true| false| The time the ticket form was created
default| boolean| false| false| Is the form the default form for this account
deleted_at| string| true| false| The time the ticket form was deleted
display_name| string| false| false| The name of the form that is displayed to an end user
end_user_conditions| array| false| false| Array of condition sets for end user products
end_user_visible| boolean| false| false| Is the form visible to the end user
id| integer| true| false| Automatically assigned when creating ticket form
in_all_brands| boolean| false| false| Is the form available for use in all brands on this account
name| string| false| true| The name of the form
position| integer| false| false| The position of this form among other forms in the account, i.e. dropdown
raw_display_name| string| false| false| The dynamic content placeholder, if present, or the "display_name" value, if not. See [Dynamic Content Items](/api-reference/ticketing/ticket-management/dynamic_content/)
raw_name| string| false| false| The dynamic content placeholder, if present, or the "name" value, if not. See [Dynamic Content Items](/api-reference/ticketing/ticket-management/dynamic_content/)
restricted_brand_ids| array| true| false| IDs of all brands that this ticket form is restricted to
ticket_field_ids| array| false| false| IDs of all ticket fields which are in this ticket form. The products use the order of the IDs to show the field values in the tickets
updated_at| string| true| false| The time of the last update of the ticket form
url| string| true| false| URL of the ticket form

**Warning** : Sending an empty array `[]` for `agent_conditions` or `end_user_conditions` will delete the conditions.

#### Example


    {  "active": true,  "agent_conditions": [    {      "child_fields": [        {          "id": 101,          "is_required": false,          "required_on_statuses": {            "statuses": [              "new",              "open",              "pending",              "hold"            ],            "type": "SOME_STATUSES"          }        },        {          "id": 200,          "is_required": true,          "required_on_statuses": {            "statuses": [              "solved"            ],            "type": "SOME_STATUSES"          }        }      ],      "parent_field_id": 100,      "value": "matching_value"    },    {      "child_fields": [        {          "id": 102,          "is_required": true,          "required_on_statuses": {            "type": "ALL_STATUSES"          }        },        {          "id": 200,          "is_required": false,          "required_on_statuses": {            "type": "NO_STATUSES"          }        }      ],      "parent_field_id": 101,      "value": "matching_value_2"    }  ],  "created_at": "2012-04-02T22:55:29Z",  "default": true,  "deleted_at": "2012-05-02T22:55:29Z",  "display_name": "Snowboard Damage",  "end_user_conditions": [    {      "child_fields": [        {          "id": 101,          "is_required": true        }      ],      "parent_field_id": 100,      "value": "matching_value"    },    {      "child_fields": [        {          "id": 202,          "is_required": false        }      ],      "parent_field_id": 200,      "value": "matching_value"    }  ],  "end_user_visible": true,  "id": 47,  "in_all_brands": false,  "name": "Snowboard Problem",  "position": 9999,  "raw_display_name": "{{dc.my_display_name}}",  "raw_name": "Snowboard Problem",  "restricted_brand_ids": [    47,    33,    22  ],  "ticket_field_ids": [    2,    4,    5,    10,    100,    101,    102,    200  ],  "updated_at": "2012-04-02T22:55:29Z",  "url": "https://company.zendesk.com/api/v2/ticket_forms/47"}

### List Ticket Forms

  * `GET /api/v2/ticket_forms`


Returns a list of all ticket forms for your account if accessed as an admin or agent. End users only see ticket forms that have `end_user_visible` set to true.

#### Allowed For

  * Anyone


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
active| boolean| Query| false| true returns active ticket forms; false returns inactive ticket forms. If not present, returns both
associated_to_brand| boolean| Query| false| true returns the ticket forms of the brand specified by the url's subdomain
end_user_visible| boolean| Query| false| true returns ticket forms where `end_user_visible`; false returns ticket forms that are not end-user visible. If not present, returns both
fallback_to_default| boolean| Query| false| true returns the default ticket form when the criteria defined by the parameters results in a set without active and end-user visible ticket forms
form_type| string| Query| false| Filter ticket forms by type. Use 'standard' for regular ticket forms, 'service_catalog' for service catalog forms, or 'all' to return all form types. Allowed values are "standard", "service_catalog", or "all".
include_boundary_indicators| boolean| Query| false| When true, includes `has_more` indicator in the cursor pagination response meta. Only valid with cursor pagination (page[size], page[after], page[before]).
include_item_cursors| boolean| Query| false| When true, includes cursor values for each item in the cursor pagination response. Only valid with cursor pagination (page[size], page[after], page[before]).
locale| string| Query| false| Locale to use for the ticket form names. If not specified, the default locale is used.
page| | Query| false| Pagination parameter. Supports both traditional offset and cursor-based pagination: - Traditional: `?page=2` (integer page number) - Cursor: `?page[size]=50&page[after]=cursor` (deepObject with size, after, before) These are mutually exclusive - use one format or the other, not both.
per_page| integer| Query| false| Number of records to return per page. Note: Default and maximum values vary by endpoint. Check endpoint-specific documentation for limits.
sort| string| Query| false| Field to sort results by. Prefix with `-` for descending order. When used with cursor pagination, this determines the cursor ordering. Example: `?sort=name` or `?sort=-created_at`

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/ticket_forms?active=true \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/ticket_forms?active=&associated_to_brand=&end_user_visible=&fallback_to_default=&form_type=standard&include_boundary_indicators=&include_item_cursors=&locale=&page=&per_page=50&sort=name"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/ticket_forms")		.newBuilder()		.addQueryParameter("active", "")		.addQueryParameter("associated_to_brand", "")		.addQueryParameter("end_user_visible", "")		.addQueryParameter("fallback_to_default", "")		.addQueryParameter("form_type", "standard")		.addQueryParameter("include_boundary_indicators", "")		.addQueryParameter("include_item_cursors", "")		.addQueryParameter("locale", "")		.addQueryParameter("page", "")		.addQueryParameter("per_page", "50")		.addQueryParameter("sort", "name");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/ticket_forms',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'active': '',    'associated_to_brand': '',    'end_user_visible': '',    'fallback_to_default': '',    'form_type': 'standard',    'include_boundary_indicators': '',    'include_item_cursors': '',    'locale': '',    'page': '',    'per_page': '50',    'sort': 'name',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/ticket_forms?active=&associated_to_brand=&end_user_visible=&fallback_to_default=&form_type=standard&include_boundary_indicators=&include_item_cursors=&locale=&page=&per_page=50&sort=name"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/ticket_forms")uri.query = URI.encode_www_form("active": "", "associated_to_brand": "", "end_user_visible": "", "fallback_to_default": "", "form_type": "standard", "include_boundary_indicators": "", "include_item_cursors": "", "locale": "", "page": "", "per_page": "50", "sort": "name")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "ticket_forms": [    {      "active": true,      "agent_conditions": [        {          "child_fields": [            {              "id": 44,              "is_required": false,              "required_on_statuses": {                "statuses": [                  "new",                  "open",                  "pending",                  "hold"                ],                "type": "SOME_STATUSES"              }            },            {              "id": 32,              "is_required": true,              "required_on_statuses": {                "statuses": [                  "solved"                ],                "type": "SOME_STATUSES"              }            }          ],          "parent_field_id": 5,          "value": "matching_value_1"        },        {          "child_fields": [            {              "id": 44,              "is_required": true,              "required_on_statuses": {                "type": "ALL_STATUSES"              }            },            {              "id": 32,              "is_required": false,              "required_on_statuses": {                "type": "NO_STATUSES"              }            }          ],          "parent_field_id": 32,          "value": "matching_value_2"        }      ],      "created_at": "2012-04-02T22:55:29Z",      "default": true,      "deleted_at": "2012-05-02T22:55:29Z",      "display_name": "Snowboard Damage",      "end_user_conditions": [        {          "child_fields": [            {              "id": 32,              "is_required": true            }          ],          "parent_field_id": 5,          "value": "matching_value_1"        },        {          "child_fields": [            {              "id": 44,              "is_required": false            }          ],          "parent_field_id": 32,          "value": "matching_value_2"        }      ],      "end_user_visible": true,      "id": 47,      "in_all_brands": false,      "name": "Snowboard Problem",      "position": 9999,      "raw_display_name": "{{dc.my_display_name}}",      "raw_name": "Snowboard Problem",      "restricted_brand_ids": [        1,        4,        6,        12,        34      ],      "ticket_field_ids": [        2,        4,        5,        32,        44      ],      "updated_at": "2012-04-02T22:55:29Z",      "url": "https://company.zendesk.com/api/v2/ticket_forms/47"    }  ]}

### Show Ticket Form

  * `GET /api/v2/ticket_forms/{ticket_form_id}`


#### Allowed For

  * Admins, Agents, and End Users


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
ticket_form_id| integer| Path| true| The ID of the ticket form

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/ticket_forms/{ticket_form_id} \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/ticket_forms/47"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/ticket_forms/47")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/ticket_forms/47',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/ticket_forms/47"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/ticket_forms/47")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "ticket_form": {    "active": true,    "agent_conditions": [      {        "child_fields": [          {            "id": 44,            "is_required": false,            "required_on_statuses": {              "statuses": [                "new",                "open",                "pending",                "hold"              ],              "type": "SOME_STATUSES"            }          },          {            "id": 32,            "is_required": true,            "required_on_statuses": {              "statuses": [                "solved"              ],              "type": "SOME_STATUSES"            }          }        ],        "parent_field_id": 5,        "value": "matching_value_1"      },      {        "child_fields": [          {            "id": 44,            "is_required": true,            "required_on_statuses": {              "type": "ALL_STATUSES"            }          },          {            "id": 32,            "is_required": false,            "required_on_statuses": {              "type": "NO_STATUSES"            }          }        ],        "parent_field_id": 32,        "value": "matching_value_2"      }    ],    "created_at": "2012-04-02T22:55:29Z",    "default": true,    "deleted_at": "2012-05-02T22:55:29Z",    "display_name": "Snowboard Damage",    "end_user_conditions": [      {        "child_fields": [          {            "id": 32,            "is_required": true          }        ],        "parent_field_id": 5,        "value": "matching_value_1"      },      {        "child_fields": [          {            "id": 44,            "is_required": false          }        ],        "parent_field_id": 32,        "value": "matching_value_2"      }    ],    "end_user_visible": true,    "id": 47,    "in_all_brands": false,    "name": "Snowboard Problem",    "position": 9999,    "raw_display_name": "{{dc.my_display_name}}",    "raw_name": "Snowboard Problem",    "restricted_brand_ids": [      1,      4,      6,      12,      34    ],    "ticket_field_ids": [      2,      4,      5,      32,      44    ],    "updated_at": "2012-04-02T22:55:29Z",    "url": "https://company.zendesk.com/api/v2/ticket_forms/47"  }}

### Show Many Ticket Forms

  * `GET /api/v2/ticket_forms/show_many?ids={ids}`


Takes an `ids` query parameter that accepts a comma-separated list of up to 100 ticket form ids. This endpoint is used primarily by the [mobile SDK](/documentation/classic-web-widget-sdks/) and the [Web Widget](/api-reference/widget/introduction/).

#### Allowed For

  * Anyone


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
active| boolean| Query| false| true returns active ticket forms; false returns inactive ticket forms. If not present, returns both
associated_to_brand| boolean| Query| false| true returns the ticket forms of the brand specified by the url's subdomain
end_user_visible| boolean| Query| false| true returns ticket forms where `end_user_visible`; false returns ticket forms that are not end-user visible. If not present, returns both
fallback_to_default| boolean| Query| false| true returns the default ticket form when the criteria defined by the parameters results in a set without active and end-user visible ticket forms
ids| string| Query| true| IDs of the ticket forms to be shown
include_boundary_indicators| boolean| Query| false| When true, includes `has_more` indicator in the cursor pagination response meta. Only valid with cursor pagination (page[size], page[after], page[before]).
include_item_cursors| boolean| Query| false| When true, includes cursor values for each item in the cursor pagination response. Only valid with cursor pagination (page[size], page[after], page[before]).

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/ticket_forms/show_many?ids=1,2,3 \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/ticket_forms/show_many?active=&associated_to_brand=&end_user_visible=&fallback_to_default=&ids=1%2C2%2C3&include_boundary_indicators=&include_item_cursors="	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/ticket_forms/show_many")		.newBuilder()		.addQueryParameter("active", "")		.addQueryParameter("associated_to_brand", "")		.addQueryParameter("end_user_visible", "")		.addQueryParameter("fallback_to_default", "")		.addQueryParameter("ids", "1,2,3")		.addQueryParameter("include_boundary_indicators", "")		.addQueryParameter("include_item_cursors", "");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/ticket_forms/show_many',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'active': '',    'associated_to_brand': '',    'end_user_visible': '',    'fallback_to_default': '',    'ids': '1%2C2%2C3',    'include_boundary_indicators': '',    'include_item_cursors': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/ticket_forms/show_many?active=&associated_to_brand=&end_user_visible=&fallback_to_default=&ids=1%2C2%2C3&include_boundary_indicators=&include_item_cursors="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/ticket_forms/show_many")uri.query = URI.encode_www_form("active": "", "associated_to_brand": "", "end_user_visible": "", "fallback_to_default": "", "ids": "1,2,3", "include_boundary_indicators": "", "include_item_cursors": "")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "ticket_forms": [    {      "active": true,      "agent_conditions": [        {          "child_fields": [            {              "id": 44,              "is_required": false,              "required_on_statuses": {                "statuses": [                  "new",                  "open",                  "pending",                  "hold"                ],                "type": "SOME_STATUSES"              }            },            {              "id": 32,              "is_required": true,              "required_on_statuses": {                "statuses": [                  "solved"                ],                "type": "SOME_STATUSES"              }            }          ],          "parent_field_id": 5,          "value": "matching_value_1"        },        {          "child_fields": [            {              "id": 44,              "is_required": true,              "required_on_statuses": {                "type": "ALL_STATUSES"              }            },            {              "id": 32,              "is_required": false,              "required_on_statuses": {                "type": "NO_STATUSES"              }            }          ],          "parent_field_id": 32,          "value": "matching_value_2"        }      ],      "created_at": "2012-04-02T22:55:29Z",      "default": true,      "deleted_at": "2012-05-02T22:55:29Z",      "display_name": "Snowboard Damage",      "end_user_conditions": [        {          "child_fields": [            {              "id": 32,              "is_required": true            }          ],          "parent_field_id": 5,          "value": "matching_value_1"        },        {          "child_fields": [            {              "id": 44,              "is_required": false            }          ],          "parent_field_id": 32,          "value": "matching_value_2"        }      ],      "end_user_visible": true,      "id": 47,      "in_all_brands": false,      "name": "Snowboard Problem",      "position": 9999,      "raw_display_name": "{{dc.my_display_name}}",      "raw_name": "Snowboard Problem",      "restricted_brand_ids": [        1,        4,        6,        12,        34      ],      "ticket_field_ids": [        2,        4,        5,        32,        44      ],      "updated_at": "2012-04-02T22:55:29Z",      "url": "https://company.zendesk.com/api/v2/ticket_forms/47"    }  ]}

### Create Ticket Form

  * `POST /api/v2/ticket_forms`


#### Allowed For

  * Admins


#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/ticket_forms \  -H "Content-Type: application/json" -X POST \  -d '  {    "ticket_form": {      "name": "Snowboard Problem",      "end_user_visible": true,      "display_name": "Snowboard Damage",      "position": 9999,      "active" : true,      "in_all_brands": false,      "restricted_brand_ids": [ 1,4,6,12,34 ],      "ticket_field_ids": [ 2,4,5,32,44 ],      "agent_conditions":    [                              {                                "parent_field_id": 5,                                "value": "matching_value_1",                                "child_fields": [                                  {                                    "id": 44,                                    "is_required": false,                                    "required_on_statuses": {                                      "type": "SOME_STATUSES",                                      "statuses": ["new", "open", "pending", "hold"]                                    }                                  },                                  {                                    "id": 32,                                    "is_required": true,                                    "required_on_statuses": {                                      "type": "SOME_STATUSES",                                      "statuses": ["solved"]                                    }                                  }                                ]                              },                              {                                "parent_field_id": 32,                                "value": "matching_value_2",                                "child_fields": [                                  {                                    "id": 44,                                    "is_required": true,                                    "required_on_statuses": {                                      "type": "ALL_STATUSES",                                    }                                  },                                  {                                    "id": 32,                                    "is_required": false,                                    "required_on_statuses": {                                      "type": "NO_STATUSES",                                    }                                  }                                ]                              }                            ],      "end_user_conditions": [                              {                                "parent_field_id": 5,                                "value": "matching_value_1",                                "child_fields": [ { "id": 32, "is_required": true } ]                              },                              {                                "parent_field_id": 32,                                "value": "matching_value_2",                                "child_fields": [ { "id": 44, "is_required": false } ]                              }                            ],      "default" : false    }  }' \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/ticket_forms"	method := "POST"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/ticket_forms")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'POST',  url: 'https://example.zendesk.com/api/v2/ticket_forms',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/ticket_forms"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/ticket_forms")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**201 Created**


    // Status 201 Created
    {  "ticket_form": {    "active": true,    "agent_conditions": [      {        "child_fields": [          {            "id": 44,            "is_required": false,            "required_on_statuses": {              "statuses": [                "new",                "open",                "pending",                "hold"              ],              "type": "SOME_STATUSES"            }          },          {            "id": 32,            "is_required": true,            "required_on_statuses": {              "statuses": [                "solved"              ],              "type": "SOME_STATUSES"            }          }        ],        "parent_field_id": 5,        "value": "matching_value_1"      },      {        "child_fields": [          {            "id": 44,            "is_required": true,            "required_on_statuses": {              "type": "ALL_STATUSES"            }          },          {            "id": 32,            "is_required": false,            "required_on_statuses": {              "type": "NO_STATUSES"            }          }        ],        "parent_field_id": 32,        "value": "matching_value_2"      }    ],    "created_at": "2012-04-02T22:55:29Z",    "default": false,    "deleted_at": "2012-05-02T22:55:29Z",    "display_name": "Snowboard Damage",    "end_user_conditions": [      {        "child_fields": [          {            "id": 32,            "is_required": true          }        ],        "parent_field_id": 5,        "value": "matching_value_1"      },      {        "child_fields": [          {            "id": 44,            "is_required": false          }        ],        "parent_field_id": 32,        "value": "matching_value_2"      }    ],    "end_user_visible": true,    "id": 47,    "in_all_brands": false,    "name": "Snowboard Problem",    "position": 9999,    "raw_display_name": "Snowboard Damage",    "raw_name": "Snowboard Problem",    "restricted_brand_ids": [      1,      4,      6,      12,      34    ],    "ticket_field_ids": [      2,      4,      5,      32,      44    ],    "updated_at": "2012-04-02T22:55:29Z",    "url": "https://company.zendesk.com/api/v2/ticket_forms/47"  }}

### Update Ticket Form

  * `PUT /api/v2/ticket_forms/{ticket_form_id}`


#### Allowed For

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
ticket_form_id| integer| Path| true| The ID of the ticket form

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/ticket_forms/{ticket_form_id} \  -H "Content-Type: application/json" -X PUT \  -d '{ "ticket_form": {          "name": "Snowboard Fixed",          "display_name": "Snowboard has been fixed",          "in_all_brands": true,          "restricted_brand_ids": [],          "agent_conditions": [],          "end_user_conditions": []      }}' \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/ticket_forms/47"	method := "PUT"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/ticket_forms/47")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'PUT',  url: 'https://example.zendesk.com/api/v2/ticket_forms/47',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/ticket_forms/47"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/ticket_forms/47")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "ticket_form": {    "active": true,    "agent_conditions": [],    "created_at": "2012-04-02T22:55:29Z",    "default": true,    "deleted_at": "2012-05-02T22:55:29Z",    "display_name": "Snowboard has been fixed",    "end_user_conditions": [],    "end_user_visible": true,    "id": 47,    "in_all_brands": true,    "name": "Snowboard Fixed",    "position": 9999,    "raw_display_name": "Snowboard has been fixed",    "raw_name": "Snowboard Fixed",    "restricted_brand_ids": [],    "ticket_field_ids": [      2,      4,      5,      32,      44    ],    "updated_at": "2012-04-02T22:55:29Z",    "url": "https://company.zendesk.com/api/v2/ticket_forms/47"  }}

### Delete Ticket Form

  * `DELETE /api/v2/ticket_forms/{ticket_form_id}`


#### Allowed For

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
ticket_form_id| integer| Path| true| The ID of the ticket form

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/ticket_forms/{id} \  -v -u {email_address}/token:{api_token} -X DELETE

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/ticket_forms/47"	method := "DELETE"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/ticket_forms/47")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("DELETE", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'DELETE',  url: 'https://example.zendesk.com/api/v2/ticket_forms/47',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/ticket_forms/47"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"DELETE",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/ticket_forms/47")request = Net::HTTP::Delete.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**204 No Content**


    // Status 204 No Content
    null

### Clone an Already Existing Ticket Form

  * `POST /api/v2/ticket_forms/{ticket_form_id}/clone`


#### Allowed For

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
ticket_form_id| integer| Path| true| The ID of the ticket form

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/ticket_forms/{ticket_form_id}/clone \  -H "Content-Type: application/json" -X POST \  -v -u {email_address}/token:{api_token} \  -d { "prepend_clone_title": true }

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/ticket_forms/47/clone"	method := "POST"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/ticket_forms/47/clone")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'POST',  url: 'https://example.zendesk.com/api/v2/ticket_forms/47/clone',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/ticket_forms/47/clone"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/ticket_forms/47/clone")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "ticket_form": {    "active": true,    "agent_conditions": [      {        "child_fields": [          {            "id": 44,            "is_required": false,            "required_on_statuses": {              "statuses": [                "new",                "open",                "pending",                "hold"              ],              "type": "SOME_STATUSES"            }          },          {            "id": 32,            "is_required": true,            "required_on_statuses": {              "statuses": [                "solved"              ],              "type": "SOME_STATUSES"            }          }        ],        "parent_field_id": 5,        "value": "matching_value_1"      },      {        "child_fields": [          {            "id": 44,            "is_required": true,            "required_on_statuses": {              "type": "ALL_STATUSES"            }          },          {            "id": 32,            "is_required": false,            "required_on_statuses": {              "type": "NO_STATUSES"            }          }        ],        "parent_field_id": 32,        "value": "matching_value_2"      }    ],    "created_at": "2012-04-02T22:55:29Z",    "default": true,    "deleted_at": "2012-05-02T22:55:29Z",    "display_name": "Snowboard Damage",    "end_user_conditions": [      {        "child_fields": [          {            "id": 32,            "is_required": true          }        ],        "parent_field_id": 5,        "value": "matching_value_1"      },      {        "child_fields": [          {            "id": 44,            "is_required": false          }        ],        "parent_field_id": 32,        "value": "matching_value_2"      }    ],    "end_user_visible": true,    "id": 47,    "in_all_brands": false,    "name": "Snowboard Problem",    "position": 9999,    "raw_display_name": "{{dc.my_display_name}}",    "raw_name": "Snowboard Problem",    "restricted_brand_ids": [      1,      4,      6,      12,      34    ],    "ticket_field_ids": [      2,      4,      5,      32,      44    ],    "updated_at": "2012-04-02T22:55:29Z",    "url": "https://company.zendesk.com/api/v2/ticket_forms/47"  }}

### Reorder Ticket Forms

  * `PUT /api/v2/ticket_forms/reorder`


#### Allowed For

  * Admins


#### Request Parameters

You can pass in the following parameter in the payload:

Name| Type| Comment
---|---|---
ticket_form_ids| array| An array of ticket form ids. Example: "[2, 23, 46, 50]"

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/ticket_forms/reorder \  -H "Content-Type: application/json" -X PUT \  -d '{"ticket_form_ids": [2, 23, 46, 50]}' \  -H "Content-Type: application/json" -X POST \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/ticket_forms/reorder"	method := "PUT"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/ticket_forms/reorder")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'PUT',  url: 'https://example.zendesk.com/api/v2/ticket_forms/reorder',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/ticket_forms/reorder"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/ticket_forms/reorder")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "ticket_forms": [    {      "active": true,      "agent_conditions": [        {          "child_fields": [            {              "id": 44,              "is_required": false,              "required_on_statuses": {                "statuses": [                  "new",                  "open",                  "pending",                  "hold"                ],                "type": "SOME_STATUSES"              }            },            {              "id": 32,              "is_required": true,              "required_on_statuses": {                "statuses": [                  "solved"                ],                "type": "SOME_STATUSES"              }            }          ],          "parent_field_id": 5,          "value": "matching_value_1"        },        {          "child_fields": [            {              "id": 44,              "is_required": true,              "required_on_statuses": {                "type": "ALL_STATUSES"              }            },            {              "id": 32,              "is_required": false,              "required_on_statuses": {                "type": "NO_STATUSES"              }            }          ],          "parent_field_id": 32,          "value": "matching_value_2"        }      ],      "created_at": "2012-04-02T22:55:29Z",      "default": true,      "deleted_at": "2012-05-02T22:55:29Z",      "display_name": "Snowboard Damage",      "end_user_conditions": [        {          "child_fields": [            {              "id": 32,              "is_required": true            }          ],          "parent_field_id": 5,          "value": "matching_value_1"        },        {          "child_fields": [            {              "id": 44,              "is_required": false            }          ],          "parent_field_id": 32,          "value": "matching_value_2"        }      ],      "end_user_visible": true,      "id": 47,      "in_all_brands": false,      "name": "Snowboard Problem",      "position": 9999,      "raw_display_name": "{{dc.my_display_name}}",      "raw_name": "Snowboard Problem",      "restricted_brand_ids": [        1,        4,        6,        12,        34      ],      "ticket_field_ids": [        2,        4,        5,        32,        44      ],      "updated_at": "2012-04-02T22:55:29Z",      "url": "https://company.zendesk.com/api/v2/ticket_forms/47"    }  ]}

### List Ticket Form Statuses of a Ticket Form

  * `GET /api/v2/ticket_forms/{ticket_form_id}/ticket_form_statuses`


Fetches all of the associated ticket form statuses of a ticket form.

#### Allowed For

  * Anyone


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
ticket_form_id| integer| Path| true| The ID of the ticket form

#### Code Samples

**Curl**


    curl --request GET https://example.zendesk.com/api/v2/ticket_forms/47/ticket_form_statuses \--header "Content-Type: application/json" \-u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/ticket_forms/47/ticket_form_statuses"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/ticket_forms/47/ticket_form_statuses")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/ticket_forms/47/ticket_form_statuses',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/ticket_forms/47/ticket_form_statuses"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/ticket_forms/47/ticket_form_statuses")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "ticket_form_statuses": [    {      "custom_status_id": 7485541848574,      "id": "01HFD81Y01D65FJ7EPNNM58GPK",      "ticket_form_id": 7485506877054    }  ]}

### Create Ticket Form Statuses

  * `POST /api/v2/ticket_forms/{ticket_form_id}/ticket_form_statuses`


Creates one or many ticket form status associations

#### Allowed For

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
ticket_form_id| integer| Path| true| The ID of the ticket form

#### Example body


    {  "ticket_form_status": [    {      "custom_status_id": 1234    },    {      "custom_status_id": 1235    }  ]}

#### Code Samples

**Curl**


    curl --request POST https://example.zendesk.com/api/v2/ticket_forms/47/ticket_form_statuses \--header "Content-Type: application/json" \-u {email_address}/token:{api_token} \--data-raw '{  "ticket_form_status": [    {      "custom_status_id": 1234    },    {      "custom_status_id": 1235    }  ]}'

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://example.zendesk.com/api/v2/ticket_forms/47/ticket_form_statuses"	method := "POST"	payload := strings.NewReader(`{  "ticket_form_status": [    {      "custom_status_id": 1234    },    {      "custom_status_id": 1235    }  ]}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/ticket_forms/47/ticket_form_statuses")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"ticket_form_status\": [    {      \"custom_status_id\": 1234    },    {      \"custom_status_id\": 1235    }  ]}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "ticket_form_status": [    {      "custom_status_id": 1234    },    {      "custom_status_id": 1235    }  ]});
    var config = {  method: 'POST',  url: 'https://example.zendesk.com/api/v2/ticket_forms/47/ticket_form_statuses',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/ticket_forms/47/ticket_form_statuses"
    payload = json.loads("""{  "ticket_form_status": [    {      "custom_status_id": 1234    },    {      "custom_status_id": 1235    }  ]}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/ticket_forms/47/ticket_form_statuses")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")request.body = %q({  "ticket_form_status": [    {      "custom_status_id": 1234    },    {      "custom_status_id": 1235    }  ]})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "ticket_form_statuses": [    {      "custom_status_id": 7485541848574,      "id": "01HFD81Y01D65FJ7EPNNM58GPK",      "ticket_form_id": 7485506877054    }  ]}

### Bulk Update Ticket Form Statuses of a Ticket Form

  * `PUT /api/v2/ticket_forms/{ticket_form_id}/ticket_form_statuses`


Updates or deletes ticket form status associations. This is a bulk operation that can both add and remove ticket form status associations for a form in one call.

#### Allowed For

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
ticket_form_id| integer| Path| true| The ID of the ticket form

#### Example body


    {  "ticket_form_status": [    {      "_destroy": "1",      "id": "abcdef"    },    {      "custom_status_id": 1    }  ]}

#### Code Samples

**Curl**


    curl --request PUT https://example.zendesk.com/api/v2/ticket_forms/47/ticket_form_statuses \--header "Content-Type: application/json" \-u {email_address}/token:{api_token} \--data-raw '{  "ticket_form_status": [    {      "_destroy": "1",      "id": "abcdef"    },    {      "custom_status_id": 1    }  ]}'

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://example.zendesk.com/api/v2/ticket_forms/47/ticket_form_statuses"	method := "PUT"	payload := strings.NewReader(`{  "ticket_form_status": [    {      "_destroy": "1",      "id": "abcdef"    },    {      "custom_status_id": 1    }  ]}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/ticket_forms/47/ticket_form_statuses")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"ticket_form_status\": [    {      \"_destroy\": \"1\",      \"id\": \"abcdef\"    },    {      \"custom_status_id\": 1    }  ]}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "ticket_form_status": [    {      "_destroy": "1",      "id": "abcdef"    },    {      "custom_status_id": 1    }  ]});
    var config = {  method: 'PUT',  url: 'https://example.zendesk.com/api/v2/ticket_forms/47/ticket_form_statuses',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/ticket_forms/47/ticket_form_statuses"
    payload = json.loads("""{  "ticket_form_status": [    {      "_destroy": "1",      "id": "abcdef"    },    {      "custom_status_id": 1    }  ]}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/ticket_forms/47/ticket_form_statuses")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")request.body = %q({  "ticket_form_status": [    {      "_destroy": "1",      "id": "abcdef"    },    {      "custom_status_id": 1    }  ]})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "ticket_form_statuses": [    {      "custom_status_id": 7485541848574,      "id": "01HFD81Y01D65FJ7EPNNM58GPK",      "ticket_form_id": 7485506877054    }  ]}

### Update Ticket Form Status By Id

  * `PUT /api/v2/ticket_forms/{ticket_form_id}/ticket_form_statuses/{ticket_form_status_id}`


Updates or deletes ticket form status association by id.

#### Allowed For

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
ticket_form_id| integer| Path| true| The ID of the ticket form
ticket_form_status_id| string| Path| true| The id of the ticket form status

#### Example body


    {  "ticket_form_status": [    {      "custom_status_id": 1    },    {      "custom_status_id": 2    },    {      "custom_status_id": 3    }  ]}

#### Code Samples

**Curl**


    curl --request PUT https://example.zendesk.com/api/v2/ticket_forms/47/ticket_form_statuses/abcdef \--header "Content-Type: application/json" \-u {email_address}/token:{api_token} \--data-raw '{  "ticket_form_status": [    {      "custom_status_id": 1    },    {      "custom_status_id": 2    },    {      "custom_status_id": 3    }  ]}'

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://example.zendesk.com/api/v2/ticket_forms/47/ticket_form_statuses/abcdef"	method := "PUT"	payload := strings.NewReader(`{  "ticket_form_status": [    {      "custom_status_id": 1    },    {      "custom_status_id": 2    },    {      "custom_status_id": 3    }  ]}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/ticket_forms/47/ticket_form_statuses/abcdef")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"ticket_form_status\": [    {      \"custom_status_id\": 1    },    {      \"custom_status_id\": 2    },    {      \"custom_status_id\": 3    }  ]}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "ticket_form_status": [    {      "custom_status_id": 1    },    {      "custom_status_id": 2    },    {      "custom_status_id": 3    }  ]});
    var config = {  method: 'PUT',  url: 'https://example.zendesk.com/api/v2/ticket_forms/47/ticket_form_statuses/abcdef',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/ticket_forms/47/ticket_form_statuses/abcdef"
    payload = json.loads("""{  "ticket_form_status": [    {      "custom_status_id": 1    },    {      "custom_status_id": 2    },    {      "custom_status_id": 3    }  ]}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/ticket_forms/47/ticket_form_statuses/abcdef")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")request.body = %q({  "ticket_form_status": [    {      "custom_status_id": 1    },    {      "custom_status_id": 2    },    {      "custom_status_id": 3    }  ]})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "ticket_form_statuses": [    {      "custom_status_id": 7485541848574,      "id": "01HFD81Y01D65FJ7EPNNM58GPK",      "ticket_form_id": 7485506877054    }  ]}

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)