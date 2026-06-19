# Lookup Relationships

*Source: https://developer.zendesk.com/api-reference/ticketing/lookup_relationships/lookup_relationships/*

---

## On this page

  * [Creating lookup relationship fields](/api-reference/ticketing/lookup_relationships/lookup_relationships/#creating-lookup-relationship-fields)
  * [Using dynamic filters](/api-reference/ticketing/lookup_relationships/lookup_relationships/#using-dynamic-filters)
  * [Get sources by target](/api-reference/ticketing/lookup_relationships/lookup_relationships/#get-sources-by-target)
  * [Filter Definitions](/api-reference/ticketing/lookup_relationships/lookup_relationships/#filter-definitions)


# Lookup Relationships

## On this page

  * [Creating lookup relationship fields](/api-reference/ticketing/lookup_relationships/lookup_relationships/#creating-lookup-relationship-fields)
  * [Using dynamic filters](/api-reference/ticketing/lookup_relationships/lookup_relationships/#using-dynamic-filters)
  * [Get sources by target](/api-reference/ticketing/lookup_relationships/lookup_relationships/#get-sources-by-target)
  * [Filter Definitions](/api-reference/ticketing/lookup_relationships/lookup_relationships/#filter-definitions)


A lookup relationship field is a custom field whose `type` is "lookup". This type of custom field gives you the ability to create a relationship from a source object to a target object. One example is a ticket lookup field called "Success Manager" that references a user. The source object is a ticket and the target object is a user. To learn more, see [Using lookup relationship fields](https://support.zendesk.com/hc/en-us/articles/4591924111770) in Zendesk help.

You can create `definitions` that specify what type of objects will show up in the autocomplete endpoints when populating the field. The filter is not used to validate the relationship; it's used as a convenience to filter the target records that you want to see. For example, if your field was "Success Manager", you could define a filter that says "only show users who are agents".

#### Setting lookup field values

  * To set by id, provide the target record's id. Example: `"my_lookup_field": "123"`.
  * To set by external id, provide an external id prefixed with the string `external_id:`. Example: `"my_lookup_field": "external_id:ABCDE"`. Note: The external id is used to retrieve the target record and then the id is stored as the lookup field value.
  * To set by name, provide a name prefixed with the string `name:`. The `is_unique` property on the custom object's name field must be enabled. Example: `"my_lookup_field": "name:car1"`. Note: The name is used to retrieve the target record and then the id is stored as the lookup field value.


### Creating lookup relationship fields

Use the following endpoints to create lookup relationship fields for tickets, users, and organizations:

  * [Create Ticket Field](/api-reference/ticketing/tickets/ticket_fields/#create-ticket-field)
  * [Create User Field](/api-reference/ticketing/users/user_fields/#create-user-field)
  * [Create Organization Field](/api-reference/ticketing/organizations/organization_fields/#create-organization-field)


Set the following properties to create a lookup relationship field:

  * `type` (required) - Must be "lookup".
  * `relationship_target_type` (required) - The object type that you want to store. One of "zen:user", "zen:ticket", "zen:organization", "zen:custom_object:CUSTOM_OBJECT_KEY". If the lookup field is defined in a custom object's schema, valid values also include "zen:article" or "zen:brand". For example "zen:user" will list user records or "zen:custom_object:apartment" will list apartment records. You can't change the value of this property after creating the field.
  * `relationship_filter` (optional) - A condition that defines a subset of records as the options in your lookup relationship field. See [Filtering the field's options](https://support.zendesk.com/hc/en-us/articles/4591924111770#topic_t14_w3l_5tb) in Zendesk help and [Conditions reference](/documentation/ticketing/reference-guides/conditions-reference/).


#### Using cURL

The following example creates a lookup relationship ticket field that references users.


    curl https://{subdomain}.zendesk.com/api/v2/ticket_fields \  --data-raw '{      "ticket_field": {          "type": "lookup",          "title": "Success Manager",          "relationship_target_type": "zen:user",          "relationship_filter": {              "all":[                  { "field": "role", "operator": "is", "value": "Agent" }              ]          }      }  }'  -H "Content-Type: application/json" -X POST \  -v -u {email_address}/token:{api_token}

### Using dynamic filters

Dynamic filtering enhances lookup relationships by allowing admins to define filters based on additional fields in the source object. This feature enables more granular control over the data presented in lookup relationships. The main difference from a static relationship filter compared to a dynamic filter is the value attribute.

The only valid operators for dynamic filters are `matches` and `not_matches`.

#### Values

Dynamic filters require that both the source field as well as the target field are of the same type. For example, a number field cannot be compared with a decimal field.

If both fields are lookup relationship fields, then they should both be pointing to the same target object.

Depending on the owner of the field, either the `id` or `key` attribute will be used when formatting the value. If the field belongs to a ticket, the `id` of the field is expected to be used. However, if the field belongs to an organization, user, or custom object, then the field `key` should be used.

Owner Field Type| id/key| Format example
---|---|---
Ticket| 123| `ticket_fields_123`
Organization| location| `organization.custom_fields.location`
User| team| `user.custom_fields.team`
Custom Object| brand| `custom_object.car.custom_fields.brand`

##### Pre-defined dynamic values

There are pre-defined dynamic values which only exist for ticket fields. They will appear if the target object is a `User`, `Organization`, or `Brand`.

User Value| Definition
---|---
`current_user`| The currently signed in user
`requester_id`| The id of the ticket requester
`assignee_id`| The id of the assigned user for the ticket

Organization Value| Definition
---|---
`organization`| The organization id of the ticket

Brand Value| Definition
---|---
`ticket_brand_id`| The brand of the ticket

#### Using cURL

The following example creates a lookup relationship ticket field that references another ticket field.


    curl https://{subdomain}.zendesk.com/api/v2/ticket_fields \  --data-raw '{      "ticket_field": {          "type": "lookup",          "title": "Success Manager",          "relationship_target_type": "zen:ticket",          "relationship_filter": {              "all":[                  { "field": "custom_fields_123", "operator": "matches", "value": "ticket_fields_456" }              ]          }      }  }'  -H "Content-Type: application/json" -X POST \  -v -u {email_address}/token:{api_token}

The following example creates a lookup relationship ticket field that references a custom object.


    curl https://{subdomain}.zendesk.com/api/v2/ticket_fields \  --data-raw '{      "ticket_field": {          "type": "lookup",          "title": "Car Owner",          "relationship_target_type": "zen:user",          "relationship_filter": {              "all":[                  { "field": "custom_objects.car.custom_fields.owner", "operator": "matches", "value": "current_user" }              ]          }      }  }'  -H "Content-Type: application/json" -X POST \  -v -u {email_address}/token:{api_token}

The following example creates a lookup relationship ticket field with a custom object as the target. It includes filters so that only custom object records associated with the same brand as the ticket's brand are available. The custom object must have a lookup field targeting `zen:brand`.


    curl https://{subdomain}.zendesk.com/api/v2/ticket_fields.json \  --data-raw '{      "ticket_field": {          "type": "lookup",          "title": "Product",          "relationship_target_type": "zen:custom_object:product",          "relationship_filter": {              "all":[                  { "field": "custom_object.product.custom_fields.brand", "operator": "matches", "value": "ticket_brand_id" }              ]          }      }  }'  -H "Content-Type: application/json" -X POST \  -v -u {email_address}/token:{api_token}

### Get sources by target

  * `GET /api/v2/{target_type}/{target_id}/relationship_fields/{field_id}/{source_type}`


Returns a list of source objects whose values are populated with the id of a related target object. For example, if you have a lookup field called "Success Manager" on a ticket, this endpoint can answer the question, "What tickets (sources) is this user (found by `target_type` and `target_id`) assigned as the 'Success Manager' (field referenced by `field_id`)?"

#### Allowed For

  * Agents


#### Pagination

  * Cursor pagination (recommended)
  * Offset pagination


See [Pagination](/api-reference/introduction/pagination/).

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
field_id| integer| Path| true| The id of the lookup relationship field
source_type| string| Path| true| The type of object the relationship field belongs to (example. ticket field belongs to a ticket object). The options are "zen:user", "zen:ticket", "zen:organization", and "zen:custom_object:CUSTOM_OBJECT_KEY"
target_id| integer| Path| true| The id of the object the relationship field is targeting
target_type| string| Path| true| The type of object the relationship field is targeting. The options are "zen:user", "zen:ticket", "zen:organization", and "zen:custom_object:CUSTOM_OBJECT_KEY"

#### Code Samples

**cURL**


    # Find users whose lookup relationship field of id `456` refer to ticket with id `1234`curl https://{subdomain}.zendesk.com/api/v2/zen:ticket/1234/relationship_fields/456/zen:user \  -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/zen:custom_object:apartment/1234/relationship_fields/1234/zen:custom_object:apartment"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/zen:custom_object:apartment/1234/relationship_fields/1234/zen:custom_object:apartment")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/zen:custom_object:apartment/1234/relationship_fields/1234/zen:custom_object:apartment',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/zen:custom_object:apartment/1234/relationship_fields/1234/zen:custom_object:apartment"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/zen:custom_object:apartment/1234/relationship_fields/1234/zen:custom_object:apartment")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "users": [    {      "id": 223443,      "name": "Johnny Agent"    },    {      "id": 8678530,      "name": "James A. Rosen"    }  ]}

### Filter Definitions

  * `GET /api/v2/relationships/definitions/{target_type}`


Returns filter definitions based on the given target type. Target types include users (zen:user), tickets (zen:ticket), organizations (zen:organization), or custom objects (zen:custom_object:CUSTOM_OBJECT_KEY). The returned filter definitions are the options that you can use to build a custom field or ticket field's `relationship_filter`.

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
source_type| string| Query| false| The source type for which you would like to see filter definitions. The options are "zen:user", "zen:ticket", and "zen:organization"
target_type| string| Path| true| The target type for which you would like to see filter definitions. The options are "zen:user", "zen:ticket", "zen:organization", and "zen:custom_object:CUSTOM_OBJECT_KEY"

#### Code Samples

**cURL**


    curl https://{subdomain}.zendesk.com/api/v2/relationships/definitions/zen:ticket \  -G --data-urlencode "source_type=zen:user" \  -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/relationships/definitions/zen:custom_object:apartment?source_type=zen%3Auser"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/relationships/definitions/zen:custom_object:apartment")		.newBuilder()		.addQueryParameter("source_type", "zen:user");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/relationships/definitions/zen:custom_object:apartment',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'source_type': 'zen%3Auser',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/relationships/definitions/zen:custom_object:apartment?source_type=zen%3Auser"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/relationships/definitions/zen:custom_object:apartment")uri.query = URI.encode_www_form("source_type": "zen:user")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "definitions": {    "conditions_all": [      {        "group": "ticket",        "nullable": false,        "operators": [          {            "terminal": false,            "title": "Is",            "value": "is"          },          {            "terminal": false,            "title": "Is not",            "value": "is_not"          },          {            "terminal": false,            "title": "Less than",            "value": "less_than"          },          {            "terminal": false,            "title": "Greater than",            "value": "greater_than"          },          {            "terminal": true,            "title": "Changed",            "value": "changed"          },          {            "terminal": false,            "title": "Changed to",            "value": "value"          },          {            "terminal": false,            "title": "Changed from",            "value": "value_previous"          },          {            "terminal": true,            "title": "Not changed",            "value": "not_changed"          },          {            "terminal": false,            "title": "Not changed to",            "value": "not_value"          },          {            "terminal": false,            "title": "Not changed from",            "value": "not_value_previous"          }        ],        "repeatable": false,        "subject": "status",        "title": "Status",        "type": "list",        "values": [          {            "enabled": true,            "title": "New",            "value": "new"          },          {            "enabled": true,            "title": "Open",            "value": "open"          },          {            "enabled": true,            "title": "Pending",            "value": "pending"          },          {            "enabled": true,            "title": "Solved",            "value": "solved"          },          {            "enabled": true,            "title": "Closed",            "value": "closed"          }        ]      },      {        "group": "custom_object",        "nullable": true,        "operators": [          {            "terminal": false,            "title": "Is",            "value": "is"          },          {            "terminal": false,            "title": "Is not",            "value": "is_not"          },          {            "terminal": true,            "title": "Present",            "value": "present"          },          {            "terminal": true,            "title": "Not present",            "value": "not_present"          },          {            "terminal": false,            "title": "Matches",            "value": "matches"          },          {            "terminal": false,            "title": "Does not match",            "value": "not_matches"          }        ],        "repeatable": false,        "subject": "custom_object.apartment.custom_fields.brand",        "title": "Assigned Brand",        "type": "autocomplete",        "values": [          {            "enabled": true,            "title": "(ticket's brand)",            "value": "ticket_brand_id"          }        ]      }    ],    "conditions_any": [      {        "group": "ticket",        "nullable": true,        "operators": [          {            "terminal": true,            "title": "Present",            "value": "present"          },          {            "terminal": true,            "title": "Not present",            "value": "not_present"          }        ],        "repeatable": false,        "subject": "custom_fields_20513432",        "title": "Happy Gilmore",        "type": "list"      },      {        "group": "ticket",        "nullable": true,        "operators": [          {            "terminal": true,            "title": "Present",            "value": "present"          },          {            "terminal": true,            "title": "Not present",            "value": "not_present"          }        ],        "repeatable": false,        "subject": "custom_fields_86492341",        "title": "total_time_field",        "type": "list"      }    ]  }}

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)