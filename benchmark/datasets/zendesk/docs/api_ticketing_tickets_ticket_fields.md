# Ticket Fields

*Source: https://developer.zendesk.com/api-reference/ticketing/tickets/ticket_fields/*

---

## On this page

  * [JSON format](/api-reference/ticketing/tickets/ticket_fields/#json-format)
  * [List Ticket Fields](/api-reference/ticketing/tickets/ticket_fields/#list-ticket-fields)
  * [Count Ticket Fields](/api-reference/ticketing/tickets/ticket_fields/#count-ticket-fields)
  * [Show Ticket Field](/api-reference/ticketing/tickets/ticket_fields/#show-ticket-field)
  * [Create Ticket Field](/api-reference/ticketing/tickets/ticket_fields/#create-ticket-field)
  * [Update Ticket Field](/api-reference/ticketing/tickets/ticket_fields/#update-ticket-field)
  * [Delete Ticket Field](/api-reference/ticketing/tickets/ticket_fields/#delete-ticket-field)
  * [List Ticket Field Options](/api-reference/ticketing/tickets/ticket_fields/#list-ticket-field-options)
  * [Show Ticket Field Option](/api-reference/ticketing/tickets/ticket_fields/#show-ticket-field-option)
  * [Create or Update Ticket Field Option](/api-reference/ticketing/tickets/ticket_fields/#create-or-update-ticket-field-option)
  * [Delete Ticket Field Option](/api-reference/ticketing/tickets/ticket_fields/#delete-ticket-field-option)
  * [Reorder Ticket Fields](/api-reference/ticketing/tickets/ticket_fields/#reorder-ticket-fields)
  * [Show Many Ticket Fields](/api-reference/ticketing/tickets/ticket_fields/#show-many-ticket-fields)


# Ticket Fields

## On this page

  * [JSON format](/api-reference/ticketing/tickets/ticket_fields/#json-format)
  * [List Ticket Fields](/api-reference/ticketing/tickets/ticket_fields/#list-ticket-fields)
  * [Count Ticket Fields](/api-reference/ticketing/tickets/ticket_fields/#count-ticket-fields)
  * [Show Ticket Field](/api-reference/ticketing/tickets/ticket_fields/#show-ticket-field)
  * [Create Ticket Field](/api-reference/ticketing/tickets/ticket_fields/#create-ticket-field)
  * [Update Ticket Field](/api-reference/ticketing/tickets/ticket_fields/#update-ticket-field)
  * [Delete Ticket Field](/api-reference/ticketing/tickets/ticket_fields/#delete-ticket-field)
  * [List Ticket Field Options](/api-reference/ticketing/tickets/ticket_fields/#list-ticket-field-options)
  * [Show Ticket Field Option](/api-reference/ticketing/tickets/ticket_fields/#show-ticket-field-option)
  * [Create or Update Ticket Field Option](/api-reference/ticketing/tickets/ticket_fields/#create-or-update-ticket-field-option)
  * [Delete Ticket Field Option](/api-reference/ticketing/tickets/ticket_fields/#delete-ticket-field-option)
  * [Reorder Ticket Fields](/api-reference/ticketing/tickets/ticket_fields/#reorder-ticket-fields)
  * [Show Many Ticket Fields](/api-reference/ticketing/tickets/ticket_fields/#show-many-ticket-fields)


You can use this API to get system and custom ticket fields. For a list of system fields, see [About ticket fields](https://support.zendesk.com/hc/en-us/articles/203661506) in Help Center.

You can also use the API to create custom ticket fields. See [About custom field types](https://support.zendesk.com/hc/en-us/articles/203661866) in the Zendesk Help Center. New custom ticket fields become available in the Tickets API. See [Setting custom field values](/api-reference/ticketing/tickets/tickets/#setting-custom-field-values) in Tickets.

You can make ticket fields visible on the request form in Help Center for end users. To make a ticket field visible to end users, make it both visible and editable in Help Center. Example:


    {  "visible_in_portal": true,  "editable_in_portal": true}

### JSON format

Ticket Fields are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
active| boolean| false| false| Whether this field is available
agent_can_edit| boolean| true| false| Whether this field is editable by agents
agent_description| string| false| false| A description of the ticket field that only agents can see
collapsed_for_agents| boolean| false| false| If true, the field is shown to agents by default. If false, the field is hidden alongside infrequently used fields. Classic interface only
created_at| string| true| false| The time the custom ticket field was created
creator_app_name| string| false| false| Name of the app that created the ticket field, or a null value if no app created the ticket field
creator_user_id| integer| false| false| The id of the user that created the ticket field, or a value of "-1" if an app created the ticket field
custom_field_options| array| false| false| Required and presented for a custom ticket field of type "multiselect" or "tagger"
custom_statuses| array| true| false| List of customized ticket statuses. Only presented for a system ticket field of type "custom_status"
description| string| false| false| Describes the purpose of the ticket field to users
editable_in_portal| boolean| false| false| Whether this field is editable by end users in Help Center
id| integer| true| false| Automatically assigned when created
position| integer| false| false| The relative position of the ticket field on a ticket. Note that for accounts with ticket forms, positions are controlled by the different forms
raw_description| string| false| false| The dynamic content placeholder if present, or the `description` value if not. See [Dynamic Content](/api-reference/ticketing/ticket-management/dynamic_content/)
raw_title| string| false| false| The dynamic content placeholder if present, or the `title` value if not. See [Dynamic Content](/api-reference/ticketing/ticket-management/dynamic_content/)
raw_title_in_portal| string| false| false| The dynamic content placeholder if present, or the "title_in_portal" value if not. See [Dynamic Content](/api-reference/ticketing/ticket-management/dynamic_content/)
regexp_for_validation| string| false| false| For "regexp" fields only. The validation pattern for a field value to be deemed valid
relationship_filter| object| false| false| A filter definition that allows your autocomplete to filter down results
relationship_target_type| string| false| false| A representation of what type of object the field references. Options are "zen:user", "zen:organization", "zen:ticket", or "zen:custom_object:{key}" where key is a custom object key. For example "zen:custom_object:apartment".
removable| boolean| true| false| If false, this field is a system field that must be present on all tickets
required| boolean| false| false| If true, agents must enter a value in the field to change the ticket status to solved
required_in_portal| boolean| false| false| If true, end users must enter a value in the field to create the request
sub_type_id| integer| false| false| For system ticket fields of type "priority" and "status". Defaults to 0. A "priority" sub type of 1 removes the "Low" and "Urgent" options. A "status" sub type of 1 adds the "On-Hold" option
system_field_options| array| true| false| Presented for a system ticket field of type "tickettype", "priority" or "status"
tag| string| false| false| For "checkbox" fields only. A tag added to tickets when the checkbox field is selected
title| string| false| true| The title of the ticket field
title_in_portal| string| false| false| The title of the ticket field for end users in Help Center
type| string| false| true| System or custom field type. Editable for custom field types and only on creation. See Create Ticket Field
updated_at| string| true| false| The time the custom ticket field was last updated
url| string| true| false| The URL for this resource
visible_in_portal| boolean| false| false| Whether this field is visible to end users in Help Center

#### Example


    {  "active": true,  "agent_can_edit": true,  "agent_description": "This is the agent only description for the subject field",  "collapsed_for_agents": false,  "created_at": "2009-07-20T22:55:29Z",  "description": "This is the subject field of a ticket",  "editable_in_portal": true,  "id": 34,  "position": 21,  "raw_description": "This is the subject field of a ticket",  "raw_title": "{{dc.my_title}}",  "raw_title_in_portal": "{{dc.my_title_in_portal}}",  "regexp_for_validation": null,  "removable": false,  "required": true,  "required_in_portal": true,  "tag": null,  "title": "Subject",  "title_in_portal": "Subject",  "type": "subject",  "updated_at": "2011-05-05T10:38:52Z",  "url": "https://company.zendesk.com/api/v2/ticket_fields/34",  "visible_in_portal": true}

### List Ticket Fields

  * `GET /api/v2/ticket_fields`


Returns a list of all system and custom ticket fields in your account.

For end users, only the ticket fields with visible_in_portal set to true are returned.

Cursor pagination returns a maximum of 100 records per page and fields are returned in the order specified by their id.

If the results are not paginated, every field is returned in the response and fields are returned in the order specified by the position.

You can adjust the position of ticket fields by:

  * Using the [Update Ticket Field](/api-reference/ticketing/tickets/ticket_fields/#update-ticket-field) endpoint
  * Using the [Reorder Ticket Fields](/api-reference/ticketing/tickets/ticket_fields/#reorder-ticket-fields) endpoint
  * Ticket Fields page in the Admin Center (**Admin Center** > **Manage** > **Ticket** > **Fields** > **Actions** > **Edit order**)


These adjustments determine the order in which fields are displayed in various locations. For accounts without access to multiple ticket forms, the order will also be used to display field values within tickets. However, for accounts with access to multiple ticket forms, the field order on the ticket page is defined within each form.

Consider caching this resource to use with the [Tickets](/api-reference/ticketing/tickets/tickets/#json-format) API.

#### Pagination

  * Cursor pagination (recommended)
  * No pagination


See [Pagination](/api-reference/introduction/pagination/).

#### Sideloads

The following sideloads are supported:

Name| Will sideload
---|---
users| The user or users that created the ticket field

#### Allowed For

  * Anyone


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
creator| boolean| Query| false| Displays the `creator_user_id` and `creator_app_name` properties. If the ticket field is created by an app, `creator_app_name` is the name of the app and `creator_user_id` is `-1`. If the ticket field is not created by an app, `creator_app_name` is null
include_boundary_indicators| boolean| Query| false| When true, includes `has_more` indicator in the cursor pagination response meta. Only valid with cursor pagination (page[size], page[after], page[before]).
include_item_cursors| boolean| Query| false| When true, includes cursor values for each item in the cursor pagination response. Only valid with cursor pagination (page[size], page[after], page[before]).
locale| string| Query| false| Forces the `title_in_portal` property to return a dynamic content variant for the specified locale. Only accepts [active locale ids](/api-reference/ticketing/account-configuration/locales/#list-locales). Example: `locale="de"`.
page| object| Query| false| Cursor-based pagination parameters (JSON:API style). Supports nested parameters: - `page[size]` \- Number of records per page (default varies by endpoint, typically 100) - `page[after]` \- Cursor token to fetch records after this position - `page[before]` \- Cursor token to fetch records before this position Example: `?page[size]=50&page[after]=eyJvIjoiaWQiLCJ2IjoiYVFFPSJ9`
sort| string| Query| false| Field to sort results by. Prefix with `-` for descending order. When used with cursor pagination, this determines the cursor ordering. Example: `?sort=name` or `?sort=-created_at`

#### Limits

This endpoint has its own rate limit that is different from the account wide rate limit. When calls are made to this endpoint, this limit will be consumed and you will get a `429 Too Many Requests` response code if the allocation is exhausted.

##### Headers

API responses include usage limit information in the headers for this endpoint.


    Zendesk-RateLimit-ticket-fields-index: total={number}; remaining={number}; resets={number}


    Zendesk-RateLimit-ticket-fields-index-deep-pagination: total={number}; remaining={number}; resets={number}

Within this header, âTotalâ signifies the initial allocation, âRemainingâ indicates the remaining allowance for the current interval, and âResetsâ denotes the wait time in seconds before the limit refreshes. You can see the Total, and Interval values in the below table.

##### Details

This is the limit definition for the Index action.

Rate Limits| Scopes| Interval| Sandbox| Trial| Default
---|---|---|---|---|---
Standard| Account| 1 minute| 40| 20| 300
With High Volume API Add On| Account| 1 minute| 40| 20| 450

"Default" applies to all Zendesk suite and support plans. Please refer to the [general account limits](https://developer.zendesk.com/api-reference/introduction/rate-limits) for more information.

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/ticket_fields \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/ticket_fields?creator=&include_boundary_indicators=&include_item_cursors=&locale=&page=&sort=name"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/ticket_fields")		.newBuilder()		.addQueryParameter("creator", "")		.addQueryParameter("include_boundary_indicators", "")		.addQueryParameter("include_item_cursors", "")		.addQueryParameter("locale", "")		.addQueryParameter("page", "")		.addQueryParameter("sort", "name");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/ticket_fields',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'creator': '',    'include_boundary_indicators': '',    'include_item_cursors': '',    'locale': '',    'page': '',    'sort': 'name',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/ticket_fields?creator=&include_boundary_indicators=&include_item_cursors=&locale=&page=&sort=name"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/ticket_fields")uri.query = URI.encode_www_form("creator": "", "include_boundary_indicators": "", "include_item_cursors": "", "locale": "", "page": "", "sort": "name")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "ticket_fields": [    {      "active": true,      "agent_description": "Agent only description",      "collapsed_for_agents": false,      "created_at": "2009-07-20T22:55:29Z",      "description": "This is the subject field of a ticket",      "editable_in_portal": true,      "id": 34,      "position": 21,      "raw_description": "This is the subject field of a ticket",      "raw_title": "{{dc.my_title}}",      "raw_title_in_portal": "{{dc.my_title_in_portal}}",      "regexp_for_validation": null,      "required": true,      "required_in_portal": true,      "tag": null,      "title": "Subject",      "title_in_portal": "Subject",      "type": "subject",      "updated_at": "2011-05-05T10:38:52Z",      "url": "https://company.zendesk.com/api/v2/ticket_fields/34",      "visible_in_portal": true    }  ]}

### Count Ticket Fields

  * `GET /api/v2/ticket_fields/count`


Returns an approximate count of system and custom ticket fields in the account. If the count exceeds 100,000, the count will return a cached result. This cached result will update every 24 hours.

The `count[refreshed_at]` property is a timestamp that indicates when the count was last updated.

**Note** : When the count exceeds 100,000, `count[refreshed_at]` may occasionally be null. This indicates that the count is being updated in the background, and `count[value]` is limited to 100,000 until the update is complete.

#### Allowed For

  * Agents


#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/ticket_fields/count \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/ticket_fields/count"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/ticket_fields/count")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/ticket_fields/count',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/ticket_fields/count"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/ticket_fields/count")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "count": {    "refreshed_at": "2020-04-06T02:18:17Z",    "value": 102  }}

### Show Ticket Field

  * `GET /api/v2/ticket_fields/{ticket_field_id}`


#### Allowed for

  * Agents


#### Sideloads

The following sideloads are supported:

Name| Will sideload
---|---
users| The user or users that created the ticket field

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
creator| boolean| Query| false| If true, displays the `creator_user_id` and `creator_app_name` properties. If the ticket field is created by an app, `creator_app_name` is the name of the app and `creator_user_id` is `-1`. If the ticket field is not created by an app, then `creator_app_name` is null
ticket_field_id| integer| Path| true| The ID of the ticket field

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/ticket_fields/{ticket_field_id} \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/ticket_fields/34?creator="	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/ticket_fields/34")		.newBuilder()		.addQueryParameter("creator", "");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/ticket_fields/34',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'creator': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/ticket_fields/34?creator="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/ticket_fields/34")uri.query = URI.encode_www_form("creator": "")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "ticket_field": {    "active": true,    "agent_description": "Agent only description",    "collapsed_for_agents": false,    "created_at": "2012-04-02T22:55:29Z",    "description": "Age",    "editable_in_portal": false,    "id": 89,    "position": 9999,    "raw_description": "Age",    "raw_title": "Age",    "raw_title_in_portal": "Age",    "regexp_for_validation": null,    "required": true,    "required_in_portal": false,    "tag": null,    "title": "Age",    "title_in_portal": "Age",    "type": "text",    "updated_at": "2012-04-02T22:55:29Z",    "url": "https://company.zendesk.com/api/v2/ticket_fields/89",    "visible_in_portal": false  }}

### Create Ticket Field

  * `POST /api/v2/ticket_fields`


Creates any of the following custom field types:

Custom field type| Description
---|---
text| Default custom field type when `type` is not specified
textarea| For multi-line text
checkbox| To capture a boolean value. Allowed values are true or false. Optionally, you can specify a tag to be added to the ticket when the value is true.
date| Example: 2021-04-16
integer| String composed of numbers. May contain an optional decimal point
decimal| For numbers containing decimals
regexp| Matches the Regex pattern found in the custom field settings
partialcreditcard| A credit card number. Only the last 4 digits are retained
multiselect| Enables users to choose multiple options from a dropdown menu. It contains one or more tag values belonging to the field's options.
tagger| Single-select dropdown menu. It contains one or more tag values belonging to the field's options. Example: ( {"id": 21938362, "value": ["hd_3000", "hd_5555"]})
lookup| A field to create a relationship (see [lookup relationships](/api-reference/ticketing/lookup_relationships/lookup_relationships/)) to another object such as a user, ticket, or organization

**Note** : Tags can't be re-used across custom ticket fields. For example, if you configure a tag for a checkbox field, you can't use that tag value for a dropdown (tagger) field option. The use of tags isn't validated and can prevent editing in the future.

See [About custom field types](https://support.zendesk.com/hc/en-us/articles/203661866) in the Zendesk Help Center.

#### Allowed For

  * Admins


#### Field limits

We recommend the following best practices for ticket fields limits. Creating more than these amounts can affect performance.

  * 400 ticket fields per account if your account doesn't have ticket forms
  * 400 ticket fields per ticket form if your account has ticket forms


#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/ticket_fields \  -d '{"ticket_field": {"type": "text", "title": "Age"}}' \  -H "Content-Type: application/json" -X POST \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/ticket_fields"	method := "POST"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/ticket_fields")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'POST',  url: 'https://example.zendesk.com/api/v2/ticket_fields',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/ticket_fields"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/ticket_fields")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**201 Created**


    // Status 201 Created
    {  "ticket_field": {    "active": true,    "agent_description": "Agent only description",    "collapsed_for_agents": false,    "created_at": "2012-04-02T22:55:29Z",    "description": "Age",    "editable_in_portal": false,    "id": 89,    "position": 9999,    "raw_description": "Age",    "raw_title": "Age",    "raw_title_in_portal": "Age",    "regexp_for_validation": null,    "required": true,    "required_in_portal": false,    "tag": null,    "title": "Age",    "title_in_portal": "Age",    "type": "text",    "updated_at": "2012-04-02T22:55:29Z",    "url": "https://company.zendesk.com/api/v2/ticket_fields/89",    "visible_in_portal": false  }}

### Update Ticket Field

  * `PUT /api/v2/ticket_fields/{ticket_field_id}`


#### Updating drop-down field options

You can also use the update endpoint to add, update, or remove options in a drop-down custom field. Updating field options for multi-select fields works exactly the same as drop-down field options.

**Important** : Unless you want to remove some options, you must specify all existing options in any update request. Omitting an option removes it from the drop-down field, which removes its values from any tickets or macros.

Use the `custom_field_options` attribute to update the options. The attribute consists of an array of option objects, with each object consisting of a `name`, `value` and `allow_solving` property. The properties correspond to the "Title", "Tag" and "Required to solve" boxes in the admin interface. Example request body:


    {"ticket_field": {    "custom_field_options": [      {"name": "Apple Pie", "value": "apple", "allow_solving": true},      {"name": "Pecan Pie", "value": "pecan", "allow_solving": false}    ]  }}

#### Example Request


    curl https://{subdomain}.zendesk.com/api/v2/ticket_fields/{id} \  -d '{"ticket_field": {"custom_field_options": [{"name": "Apple Pie", "value": "apple", "allow_solving": true}, {"name": "Pecan Pie", "value": "pecan", "allow_solving": false}]}}' \  -H "Content-Type: application/json" -X PUT \  -v -u {email_address}/token:{api_token}

#### Example Response


    Status: 200 OK
    {  "ticket_field": {    "id":21938362,    "type":"tagger",    "title":"Pies",    ...    "custom_field_options": [      {        "id":21029772,        "name":"Apple Pie",        "raw_name":"Apple Pie",        "value":"apple",        "default":false,        "allow_solving":true      },      ...    ]  }}

#### Allowed for

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
creator| boolean| Query| false| If true, displays the `creator_user_id` and `creator_app_name` properties. If the ticket field is created by an app, `creator_app_name` is the name of the app and `creator_user_id` is `-1`. If the ticket field is not created by an app, then `creator_app_name` is null
ticket_field_id| integer| Path| true| The ID of the ticket field

#### Limits

This endpoint has its own rate limit that is different from the account wide rate limit. When calls are made to this endpoint, this limit will be consumed and you will get a `429 Too Many Requests` response code if the allocation is exhausted.

##### Headers

API responses include usage limit information in the headers for this endpoint.


    Zendesk-RateLimit-ticket-fields-update: total={number}; remaining={number}; resets={number}

Within this header, âTotalâ signifies the initial allocation, âRemainingâ indicates the remaining allowance for the current interval, and âResetsâ denotes the wait time in seconds before the limit refreshes. You can see the Total, and Interval values in the below table.

##### Details

This is the limit definition for the update action.

Rate Limits| Scopes| Interval| Sandbox| Trial| Default
---|---|---|---|---|---
Standard| Account| 1 minute| 50| 25| 75
With High Volume API Add On| Account| 1 minute| 50| 25| 75

"Default" applies to all Zendesk suite and support plans. Please refer to the [general account limits](https://developer.zendesk.com/api-reference/introduction/rate-limits) for more information.

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/ticket_fields/{id} \  -d '{ "ticket_field": { "title": "Your age" }}' \  -H "Content-Type: application/json" -X PUT \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/ticket_fields/34?creator="	method := "PUT"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/ticket_fields/34")		.newBuilder()		.addQueryParameter("creator", "");RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'PUT',  url: 'https://example.zendesk.com/api/v2/ticket_fields/34',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'creator': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/ticket_fields/34?creator="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/ticket_fields/34")uri.query = URI.encode_www_form("creator": "")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "ticket_field": {    "active": true,    "agent_description": "Agent only description",    "collapsed_for_agents": false,    "created_at": "2012-04-02T22:55:29Z",    "description": "Your age",    "editable_in_portal": false,    "id": 89,    "position": 9999,    "raw_description": "Your age",    "raw_title": "Your age",    "raw_title_in_portal": "Your age",    "regexp_for_validation": null,    "required": true,    "required_in_portal": false,    "tag": null,    "title": "Your age",    "title_in_portal": "Your age",    "type": "text",    "updated_at": "2012-04-02T23:11:23Z",    "url": "https://company.zendesk.com/api/v2/ticket_fields/89",    "visible_in_portal": false  }}

### Delete Ticket Field

  * `DELETE /api/v2/ticket_fields/{ticket_field_id}`


#### Allowed for

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
creator| boolean| Query| false| If true, displays the `creator_user_id` and `creator_app_name` properties. If the ticket field is created by an app, `creator_app_name` is the name of the app and `creator_user_id` is `-1`. If the ticket field is not created by an app, then `creator_app_name` is null
ticket_field_id| integer| Path| true| The ID of the ticket field

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/ticket_fields/{ticket_field_id} \  -v -u {email_address}/token:{api_token} -X DELETE

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/ticket_fields/34?creator="	method := "DELETE"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/ticket_fields/34")		.newBuilder()		.addQueryParameter("creator", "");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("DELETE", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'DELETE',  url: 'https://example.zendesk.com/api/v2/ticket_fields/34',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'creator': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/ticket_fields/34?creator="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"DELETE",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/ticket_fields/34")uri.query = URI.encode_www_form("creator": "")request = Net::HTTP::Delete.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**204 No Content**


    // Status 204 No Content
    null

### List Ticket Field Options

  * `GET /api/v2/ticket_fields/{ticket_field_id}/options`


Returns a list of custom ticket field options for the given drop-down ticket field.

#### Allowed For

  * Agents


#### Pagination

  * Cursor pagination (recommended)
  * Offset pagination


See [Pagination](/api-reference/introduction/pagination/).

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
ticket_field_id| integer| Path| true| The ID of the ticket field

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/ticket_fields/{ticket_field_id}/options \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/ticket_fields/34/options"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/ticket_fields/34/options")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/ticket_fields/34/options',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/ticket_fields/34/options"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/ticket_fields/34/options")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "count": 2,  "custom_field_options": [    {      "allow_solving": true,      "id": 10000,      "name": "Apples",      "position": 0,      "raw_name": "Apples",      "url": "http://{subdomain}.zendesk.com/api/v2/ticket_fields/1/options/10000",      "value": "apple"    },    {      "allow_solving": true,      "id": 10001,      "name": "Bananas",      "position": 1,      "raw_name": "Bananas",      "url": "http://{subdomain}.zendesk.com/api/v2/ticket_fields/1/options/10001",      "value": "banana"    }  ],  "next_page": null,  "previous_page": null}

### Show Ticket Field Option

  * `GET /api/v2/ticket_fields/{ticket_field_id}/options/{ticket_field_option_id}`


#### Allowed for

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
ticket_field_id| integer| Path| true| The ID of the ticket field
ticket_field_option_id| integer| Path| true| The ID of the ticket field option

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/ticket_fields/{ticket_field_id}/options/{ticket_field_option_id} \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/ticket_fields/34/options/10001"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/ticket_fields/34/options/10001")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/ticket_fields/34/options/10001',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/ticket_fields/34/options/10001"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/ticket_fields/34/options/10001")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "custom_field_option": {    "allow_solving": true,    "id": 10001,    "name": "Bananas",    "position": 1,    "raw_name": "Bananas",    "url": "http://{subdomain}.zendesk.com/api/v2/ticket_fields/1/options/10001",    "value": "banana"  }}

### Create or Update Ticket Field Option

  * `POST /api/v2/ticket_fields/{ticket_field_id}/options`


Creates or updates an option for the given drop-down ticket field.

To update an option, include the id of the option in the `custom_field_option` object. Example:

`{"custom_field_option": {"id": 10002, "name": "Pineapples", ... }`

If an option exists for the given ID, the option will be updated. Otherwise, a new option will be created.

#### Response

Returns one of the following status codes:

  * 200 with `Location: /api/v2/ticket_fields/{ticket_field_id}/options` if the ticket field option already exists in the database
  * 201 with `Location: /api/v2/ticket_fields/{ticket_field_id}/options` if the ticket field option is new


#### Allowed For

  * Admins


#### Rate Limit

You can make 100 requests every 1 minute using this endpoint. The rate limiting mechanism behaves as described in [Monitoring your request activity](/api-reference/ticketing/account-configuration/usage_limits/#monitoring-your-request-activity) in the API introduction.

#### Field Option Limits

  * 2000 options per ticket field


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
ticket_field_id| integer| Path| true| The ID of the ticket field

#### Code Samples

**curl**

Create Ticket Field Option


    curl https://{subdomain}.zendesk.com/api/v2/ticket_fields/{ticket_field_id}/options \  -d '{"custom_field_option": {"name": "Grapes", "position": 2, "value": "grape", "allow_solving": true}}' \  -H "Content-Type: application/json" -X POST \  -v -u {email_address}/token:{api_token}

**curl**

Update Ticket Field Option


    curl https://{subdomain}.zendesk.com/api/v2/ticket_fields/{ticket_field_id}/options \  -d '{"custom_field_option": {"id": 10002, "name": "Pineapples", "position": 2, "value": "pineapple", "allow_solving": true}}' \  -H "Content-Type: application/json" -X POST \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/ticket_fields/34/options"	method := "POST"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/ticket_fields/34/options")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'POST',  url: 'https://example.zendesk.com/api/v2/ticket_fields/34/options',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/ticket_fields/34/options"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/ticket_fields/34/options")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "custom_field_option": {    "allow_solving": true,    "id": 10002,    "name": "Pineapples",    "position": 2,    "raw_name": "Pineapples",    "url": "http://{subdomain}.zendesk.com/api/v2/ticket_fields/1/options/10002",    "value": "pineapple"  }}

**201 Created**


    // Status 201 Created
    {  "custom_field_option": {    "allow_solving": true,    "id": 10002,    "name": "Grapes",    "position": 2,    "raw_name": "Grapes",    "url": "http://{subdomain}.zendesk.com/api/v2/ticket_fields/1/options/10002",    "value": "grape"  }}

### Delete Ticket Field Option

  * `DELETE /api/v2/ticket_fields/{ticket_field_id}/options/{ticket_field_option_id}`


#### Allowed for

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
ticket_field_id| integer| Path| true| The ID of the ticket field
ticket_field_option_id| integer| Path| true| The ID of the ticket field option

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/ticket_fields/{ticket_field_id}/options/{ticket_field_option_id} \  -v -u {email_address}/token:{api_token} -X DELETE

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/ticket_fields/34/options/10001"	method := "DELETE"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/ticket_fields/34/options/10001")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("DELETE", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'DELETE',  url: 'https://example.zendesk.com/api/v2/ticket_fields/34/options/10001',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/ticket_fields/34/options/10001"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"DELETE",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/ticket_fields/34/options/10001")request = Net::HTTP::Delete.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**204 No Content**


    // Status 204 No Content
    null

### Reorder Ticket Fields

  * `PUT /api/v2/ticket_fields/reorder`


#### Allowed For

  * Admins


#### Request Parameters

You can pass in the following parameter in the payload:

Name| Type| Comment
---|---|---
ticket_field_ids| array| An array of ticket field ids. Example: "[2, 23, 46, 50]". Not all ticket_field_ids are necessary in the payload; only those provided will be assigned to the first positions. Missing IDs will be assigned incremental positions automatically.

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/ticket_fields/reorder \  -H "Content-Type: application/json" -X PUT \  -d '{"ticket_field_ids": [2, 23, 46, 50]}' \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/ticket_fields/reorder"	method := "PUT"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/ticket_fields/reorder")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'PUT',  url: 'https://example.zendesk.com/api/v2/ticket_fields/reorder',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/ticket_fields/reorder"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/ticket_fields/reorder")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    null

### Show Many Ticket Fields

  * `GET /api/v2/ticket_fields/show_many`


Returns multiple ticket fields in a single request.

Provide either:

  * `ids` â a comma-separated list of ticket field IDs, or
  * `keys` â a comma-separated list of ticket field keys


Up to 100 values are accepted.

The response payload matches the List Ticket Fields [response format](/api-reference/ticketing/tickets/ticket_fields/#example-responses).

#### Sideloads

The following sideloads are supported:

Name| Will sideload
---|---
users| The user or users that created fields

#### Allowed For

  * Anyone


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
creator| boolean| Query| false| If true, includes creator information in the response.
exclude_sub_selection_options| boolean| Query| false| If true, excludes sub-selection options from dropdown fields in the response.
ids| string| Query| false| Comma-separated list of ticket field IDs to retrieve. Up to 100 values accepted. Either `ids` or `keys` can be used, but not both.
keys| string| Query| false| Comma-separated list of ticket field keys to retrieve. Up to 100 values accepted. Use field keys like 'priority', 'status', 'subject' instead of numeric IDs. Either `ids` or `keys` can be used, but not both.

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/ticket_fields/show_many?ids=1,2,3 \  -v -u {email_address}/token:{api_token}

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/ticket_fields/show_many?keys=priority,type,custom_field_12345 \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/ticket_fields/show_many?creator=&exclude_sub_selection_options=&ids=123%2C456%2C789&keys=priority%2Cstatus%2Csubject"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/ticket_fields/show_many")		.newBuilder()		.addQueryParameter("creator", "")		.addQueryParameter("exclude_sub_selection_options", "")		.addQueryParameter("ids", "123,456,789")		.addQueryParameter("keys", "priority,status,subject");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/ticket_fields/show_many',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'creator': '',    'exclude_sub_selection_options': '',    'ids': '123%2C456%2C789',    'keys': 'priority%2Cstatus%2Csubject',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/ticket_fields/show_many?creator=&exclude_sub_selection_options=&ids=123%2C456%2C789&keys=priority%2Cstatus%2Csubject"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/ticket_fields/show_many")uri.query = URI.encode_www_form("creator": "", "exclude_sub_selection_options": "", "ids": "123,456,789", "keys": "priority,status,subject")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "count": 2,  "next_page": null,  "previous_page": null,  "ticket_fields": [    {      "active": true,      "agent_description": "Agent only description",      "collapsed_for_agents": false,      "created_at": "2009-07-20T22:55:29Z",      "description": "This is the subject field of a ticket",      "editable_in_portal": true,      "id": 34,      "position": 21,      "raw_description": "This is the subject field of a ticket",      "raw_title": "{{dc.my_title}}",      "raw_title_in_portal": "{{dc.my_title_in_portal}}",      "regexp_for_validation": null,      "required": true,      "required_in_portal": true,      "tag": null,      "title": "Subject",      "title_in_portal": "Subject",      "type": "subject",      "updated_at": "2011-05-05T10:38:52Z",      "url": "https://company.zendesk.com/api/v2/ticket_fields/34",      "visible_in_portal": true    },    {      "active": true,      "agent_description": "",      "collapsed_for_agents": false,      "created_at": "2009-07-20T22:55:29Z",      "description": "Request priority",      "editable_in_portal": false,      "id": 35,      "position": 22,      "raw_description": "Request priority",      "raw_title": "Priority",      "raw_title_in_portal": "Priority",      "regexp_for_validation": null,      "required": false,      "required_in_portal": false,      "tag": null,      "title": "Priority",      "title_in_portal": "Priority",      "type": "priority",      "updated_at": "2011-05-05T10:38:52Z",      "url": "https://company.zendesk.com/api/v2/ticket_fields/35",      "visible_in_portal": true    }  ]}

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)