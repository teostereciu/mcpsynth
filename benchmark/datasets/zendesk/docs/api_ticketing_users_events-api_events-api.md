# Events API

*Source: https://developer.zendesk.com/api-reference/ticketing/users/events-api/events-api/*

---

## On this page

  * [JSON format](/api-reference/ticketing/users/events-api/events-api/#json-format)
  * [Get Zendesk User Events](/api-reference/ticketing/users/events-api/events-api/#get-zendesk-user-events)
  * [Get Events by Sunshine Profile](/api-reference/ticketing/users/events-api/events-api/#get-events-by-sunshine-profile)
  * [Get Events by Sunshine Profile ID](/api-reference/ticketing/users/events-api/events-api/#get-events-by-sunshine-profile-id)
  * [Track Event Against Zendesk User and Given Profile](/api-reference/ticketing/users/events-api/events-api/#track-event-against-zendesk-user-and-given-profile)
  * [Track Event Against a Sunshine Profile](/api-reference/ticketing/users/events-api/events-api/#track-event-against-a-sunshine-profile)
  * [Track Event Against a Sunshine Profile by Profile ID](/api-reference/ticketing/users/events-api/events-api/#track-event-against-a-sunshine-profile-by-profile-id)


# Events API

## On this page

  * [JSON format](/api-reference/ticketing/users/events-api/events-api/#json-format)
  * [Get Zendesk User Events](/api-reference/ticketing/users/events-api/events-api/#get-zendesk-user-events)
  * [Get Events by Sunshine Profile](/api-reference/ticketing/users/events-api/events-api/#get-events-by-sunshine-profile)
  * [Get Events by Sunshine Profile ID](/api-reference/ticketing/users/events-api/events-api/#get-events-by-sunshine-profile-id)
  * [Track Event Against Zendesk User and Given Profile](/api-reference/ticketing/users/events-api/events-api/#track-event-against-zendesk-user-and-given-profile)
  * [Track Event Against a Sunshine Profile](/api-reference/ticketing/users/events-api/events-api/#track-event-against-a-sunshine-profile)
  * [Track Event Against a Sunshine Profile by Profile ID](/api-reference/ticketing/users/events-api/events-api/#track-event-against-a-sunshine-profile-by-profile-id)


The Events API lets you build a timeline of all your customers' interactions from any source. An event can be any programmatic event that your application or system can associate with a user. Examples include purchase transactions, website visits, or customer service interactions.

Each event is associated with a customer who triggered the event.

The Events API is available on the Suite Team plan and above. It is activated in the Admin Center by an admin.

In addition to this API reference, the following resources are available in the Develop Help Center:

  * To get started, see [Getting started with Sunshine user events](/documentation/ticketing/events/getting-started-with-events) in the Develop Help Center
  * To learn more about using the API, see the [Events API developer guide](/documentation/ticketing/events/about-the-events-api/)
  * To ask questions, provide answers, and join discussions, visit the [Zendesk APIs community](https://support.zendesk.com/hc/en-us/community/topics/1260801854210)


### Run in Postman

If you use Postman, you can import the Sunshine Events API endpoints as a collection into your Postman app, then try out different requests to learn how the API works. Click the following button to get started:

[](https://god.gw.postman.com/run-collection/19931619-678e0310-0069-43b1-a7af-6c9414c45f48?action=collection/fork&collection-url=entityId=19931619-678e0310-0069-43b1-a7af-6c9414c45f48&entityType=collection&workspaceId=cfe0e8e6-42d1-4f46-a048-90e2caae5a05)

If you don't use Postman, you can sign up for a free account on the [Postman website](https://identity.getpostman.com/signup) and download the app. For more information about using Postman with Zendesk APIs, see [Exploring Zendesk APIs with Postman](/documentation/api-basics/working-with-the-zendesk-apis/exploring-zendesk-apis-with-postman/).

### JSON format

Events are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
created_at| string| false| false| ISO-8601 compliant date-time reflecting the time the event was created. If not set, the API sets the value when it receives the event
description| string| false| false| An event description
id| string| true| false| ID of the event
properties| object| false| true| A custom JSON object with details about the event. Must comply with the JSON Schema specification
received_at| string| true| false| ISO-8601 compliant date-time reflecting the time the event was received
source| string| false| true| Application which sent the event. Note: 'zendesk' is a protected source name for Zendesk standard events. Any attempts to use this source when creating an event results in an error
type| string| false| true| Event name

An event consists of a JSON object describing both the event and the user who triggered the event.

Name| Type| Required| Description
---|---|---|---
profile| object| yes| The user who triggered the event. For more information, see [profile object](/api-reference/ticketing/users/events-api/events-api/#profile-object)
event| object| yes| The event triggered by the user. For more information, see the [event object](/api-reference/ticketing/users/events-api/events-api/#json-format)

#### Profile Object

A profile object describes a user associated with an application or system. The object has the following properties:

Name| Type| Required| Description
---|---|---|---
source| string| yes| The product or service associated with the profile. For example, "Support", "Salesforce", or "Chat"
type| string| yes| The type of profile. For example, "Contact" or "Lead"
identifiers| object| yes| One or more user identities. See the [identifiers array](/api-reference/ticketing/users/profiles_api/profiles_api/#identifiers-array)

#### Example


    {  "profile": {    "source": "shoppingnow",    "type": "customer",    "identifiers": [      {        "type": "shoppingnow_id",        "value": "361959350832"      },      {       "type": "external_id",       "value": "0987654321"     }    ]  },  "event": {    "source": "shoppingnow",    "type": "order_completed",    "created_at": "2018-11-05T22:26:00Z",    "description": "Added item to cart",    "properties": {      "item": {        "name": "Canon 429 EOS HD",        "query": "camera",        "price": "499.99"      },      "shipping": {        "eta_date": "2019/01/02",        "address": {          "address1": "1019 Market Street",          "city": "San Francisco",          "state": "CA",          "zipcode": "94103"        }      }    }  }}

### Get Zendesk User Events

  * `GET /api/v2/users/{user_id}/events`


Returns events for a given Zendesk user.

#### Allowed For

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
filter[end_time]| string| Query| false| Include events equal to or before the `created_at` time
filter[source]| string| Query| false| Include events of the specified source
filter[start_time]| string| Query| false| Include events equal to or later than the `created_at` time
filter[type]| string| Query| false| Include events of the specified type for the given event source. The `filter[source]` parameter must be included
page[size]| string| Query| false| Include the specified number of events
user_id| string| Path| true| Zendesk user ID

#### Code Samples

**curl**


    curl "https://{subdomain}.zendesk.com/api/v2/users/{user_id}/events" \  -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/users/120077332/events?filter[end_time]=&filter[source]=&filter[start_time]=&filter[type]=&page[size]="	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/users/120077332/events")		.newBuilder()		.addQueryParameter("filter[end_time]", "")		.addQueryParameter("filter[source]", "")		.addQueryParameter("filter[start_time]", "")		.addQueryParameter("filter[type]", "")		.addQueryParameter("page[size]", "");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/users/120077332/events',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'filter[end_time]': '',    'filter[source]': '',    'filter[start_time]': '',    'filter[type]': '',    'page[size]': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/users/120077332/events?filter[end_time]=&filter[source]=&filter[start_time]=&filter[type]=&page[size]="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/users/120077332/events")uri.query = URI.encode_www_form("filter[end_time]": "", "filter[source]": "", "filter[start_time]": "", "filter[type]": "", "page[size]": "")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "events": [    {      "created_at": "2020-01-31T00:44:07+00:00",      "description": "Order complete",      "properties": {        "billing": {          "address1": "1019 Market St",          "city": "San Francisco",          "state": "CA",          "zipcode": "94103"        },        "item": {          "name": "Zendesk Swag"        }      },      "source": "shoppingnow",      "type": "checkout"    }  ],  "links": [    {      "next": "https://yoursubdomain.zendesk.com/api/v2/user_profiles/1/events?page[after]=hkjhdjk"    }  ],  "meta": {    "after_cursor": "hkjhdjk",    "has_more": true  }}

**400 Bad Request**


    // Status 400 Bad Request
    {  "error": {    "message": "You passed an invalid value for the id attribute. Invalid parameter: id must be an integer from api/v2/users/show",    "title": "Invalid attribute"  }}

### Get Events by Sunshine Profile

  * `GET /api/v2/user_profiles/events?identifier={identifier}`


Returns events for a Sunshine profile.

To locate the specific profile, you must specify an identifier query as a URL parameter in a request. For more information, see [Identifier queries](/api-reference/ticketing/users/profiles_api/profiles_api/#identifier-queries).

You can also include any of the following optional query string parameters in the format of `filter[{optional parameter}]=`:

  * **source** \- Include only events of the specified source. For example, `filter[source]=amazon`
  * **type** \- Include only events of the specified type for a given event source. For example, `filter[source]=amazon&filter[type]=checkout`
  * **start_time** \- Include only events with a later or equal to `filter[created_at]` time
  * **end_time** \- Include only events with an earlier or equal to `filter[created_at]` time


`page[size]` specifies the number of events. Note, it is a parameter in itself and not a `filter[]` parameter value.

To understand how to use the optional `filter[]` path parameter, see [Filtering Sunshine events](/documentation/custom-data/events/filtering-events).

The query string must be url-encoded before sending the request. In cURL, use the `--data-urlencode` option with the `-G` flag. The `-G` flag forces the command to make a GET request instead of a default POST request.

#### Allowed For

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
filter[end_time]| string| Query| false| Include events equal to or before the `created_at` time
filter[source]| string| Query| false| Include events of the specified source
filter[start_time]| string| Query| false| Include events equal to or later than the `created_at` time
filter[type]| string| Query| false| Include events of the specified type for the given event source. The `filter[source]` parameter must be included
identifier| string| Query| true| Pass a profile identifier query to filter for a specific profile in the format `source:type:identifier_type:identifier_value`. For more information, see [Identifier queries](/api-reference/ticketing/users/profiles_api/profiles_api/#identifier-queries)
page[size]| string| Query| false| Include the specified number of events

#### Code Samples

**curl**


    curl "https://{subdomain}.zendesk.com/api/v2/user_profiles/events?identifier={identifier_query}" \  -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/user_profiles/events?filter[end_time]=&filter[source]=&filter[start_time]=&filter[type]=&identifier=shoppingnow%3Acustomer%3Aemail%3Aexample%40example.com&page[size]="	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/user_profiles/events")		.newBuilder()		.addQueryParameter("filter[end_time]", "")		.addQueryParameter("filter[source]", "")		.addQueryParameter("filter[start_time]", "")		.addQueryParameter("filter[type]", "")		.addQueryParameter("identifier", "shoppingnow:customer:email:[[email protected]](/cdn-cgi/l/email-protection)")		.addQueryParameter("page[size]", "");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/user_profiles/events',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'filter[end_time]': '',    'filter[source]': '',    'filter[start_time]': '',    'filter[type]': '',    'identifier': 'shoppingnow%3Acustomer%3Aemail%3Aexample%40example.com',    'page[size]': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/user_profiles/events?filter[end_time]=&filter[source]=&filter[start_time]=&filter[type]=&identifier=shoppingnow%3Acustomer%3Aemail%3Aexample%40example.com&page[size]="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/user_profiles/events")uri.query = URI.encode_www_form("filter[end_time]": "", "filter[source]": "", "filter[start_time]": "", "filter[type]": "", "identifier": "shoppingnow:customer:email:[[email protected]](/cdn-cgi/l/email-protection)", "page[size]": "")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "events": [    {      "created_at": "2020-01-31T00:44:07+00:00",      "description": "Order complete",      "properties": {        "billing": {          "address1": "1019 Market St",          "city": "San Francisco",          "state": "CA",          "zipcode": "94103"        },        "item": {          "name": "Zendesk Swag"        }      },      "source": "shoppingnow",      "type": "checkout"    }  ],  "links": [    {      "next": "https://yoursubdomain.zendesk.com/api/v2/user_profiles/1/events?page[after]=hkjhdjk"    }  ],  "meta": {    "after_cursor": "hkjhdjk",    "has_more": true  }}

**400 Bad Request**


    // Status 400 Bad Request
    {  "errors": [    {      "code": "StartTimestampNotValid",      "id": "c21d8981-8940-419b-907b-7f7a2ba22cca",      "title": "Start Timestamp not valid"    }  ]}

**404 Not Found**


    // Status 404 Not Found
    {  "errors": [    {      "code": "StartTimestampNotValid",      "id": "c21d8981-8940-419b-907b-7f7a2ba22cca",      "title": "Start Timestamp not valid"    }  ]}

### Get Events by Sunshine Profile ID

  * `GET /api/v2/user_profiles/{profile_id}/events`


Returns events for a given Sunshine profile. To retrieve a profile ID, see [Get profile by identifier](/api-reference/custom-data/profiles_api/profiles_api/#get-profile-by-identifier).

#### Allowed For

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
filter[end_time]| string| Query| false| Include events equal to or before the `created_at` time
filter[source]| string| Query| false| Include events of the specified source
filter[start_time]| string| Query| false| Include events equal to or later than the `created_at` time
filter[type]| string| Query| false| Include events of the specified type for the given event source. This requires the `filter[source]` parameter to be included
page[size]| string| Query| false| Include the specified number of events
profile_id| string| Path| true| Sunshine profile ID

#### Code Samples

**curl**


    curl "https://{subdomain}.zendesk.com/api/v2/user_profiles/{profile_id}/events" \  -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/user_profiles//events?filter[end_time]=&filter[source]=&filter[start_time]=&filter[type]=&page[size]="	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/user_profiles//events")		.newBuilder()		.addQueryParameter("filter[end_time]", "")		.addQueryParameter("filter[source]", "")		.addQueryParameter("filter[start_time]", "")		.addQueryParameter("filter[type]", "")		.addQueryParameter("page[size]", "");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/user_profiles//events',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'filter[end_time]': '',    'filter[source]': '',    'filter[start_time]': '',    'filter[type]': '',    'page[size]': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/user_profiles//events?filter[end_time]=&filter[source]=&filter[start_time]=&filter[type]=&page[size]="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/user_profiles//events")uri.query = URI.encode_www_form("filter[end_time]": "", "filter[source]": "", "filter[start_time]": "", "filter[type]": "", "page[size]": "")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "events": [    {      "created_at": "2020-01-31T00:44:07+00:00",      "description": "Order complete",      "properties": {        "billing": {          "address1": "1019 Market St",          "city": "San Francisco",          "state": "CA",          "zipcode": "94103"        },        "item": {          "name": "Zendesk Swag"        }      },      "source": "shoppingnow",      "type": "checkout"    }  ],  "links": [    {      "next": "https://yoursubdomain.zendesk.com/api/v2/user_profiles/1/events?page[after]=hkjhdjk"    }  ],  "meta": {    "after_cursor": "hkjhdjk",    "has_more": true  }}

**400 Bad Request**


    // Status 400 Bad Request
    {  "errors": [    {      "code": "StartTimestampNotValid",      "id": "c21d8981-8940-419b-907b-7f7a2ba22cca",      "title": "Start Timestamp not valid"    }  ]}

**404 Not Found**


    // Status 404 Not Found
    {  "errors": [    {      "code": "StartTimestampNotValid",      "id": "c21d8981-8940-419b-907b-7f7a2ba22cca",      "title": "Start Timestamp not valid"    }  ]}

### Track Event Against Zendesk User and Given Profile

  * `POST /api/v2/users/{user_id}/events`


Stores an event for a given Zendesk user and profile.

#### Allowed For

  * Agents


Access also depends on agent role permissions set in **Support** > **People** > **Roles** > **People**.

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
user_id| string| Path| true| Zendesk user ID

#### Example body


    {  "event": {    "created_at": "2020-01-31T00:44:07+00:00",    "description": "Order complete",    "properties": {      "billing": {        "address1": "1019 Market St",        "city": "San Francisco",        "state": "CA",        "zipcode": "94103"      },      "item": {        "name": "Zendesk Swag"      }    },    "source": "shoppingnow",    "type": "checkout"  },  "profile": {    "identifiers": [      {        "type": "email",        "value": "[[email protected]](/cdn-cgi/l/email-protection)"      },      {        "type": "external_id",        "value": "0987654321"      }    ],    "name": "Jane Smith",    "source": "shoppingnow",    "type": "customer"  }}

#### Code Samples

**curl**


    curl "https://{subdomain}.zendesk.com/api/v2/users/{user_id}/events" \  -d {"profile":{"name": "Jane Smith", "source":"shoppingnow","type":"customer","identifiers":[{"type":"email","value":"[[email protected]](/cdn-cgi/l/email-protection)"}]},"event":{"source":"shoppingnow","type":"checkout","description":"Order complete","created_at":"2020-01-31T00:44:07.000Z","properties":{"item":{"name":"Zendesk Swag"},"billing":{"address1":"1019 Market St","city":"San Francisco","state":"CA","zipcode":"94103"}}}} \  -H "Content-Type: application/json" \  -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://support.zendesk.com/api/v2/users/120077332/events"	method := "POST"	payload := strings.NewReader(`{  "event": {    "created_at": "2020-01-31T00:44:07+00:00",    "description": "Order complete",    "properties": {      "billing": {        "address1": "1019 Market St",        "city": "San Francisco",        "state": "CA",        "zipcode": "94103"      },      "item": {        "name": "Zendesk Swag"      }    },    "source": "shoppingnow",    "type": "checkout"  },  "profile": {    "identifiers": [      {        "type": "email",        "value": "[[email protected]](/cdn-cgi/l/email-protection)"      },      {        "type": "external_id",        "value": "0987654321"      }    ],    "name": "Jane Smith",    "source": "shoppingnow",    "type": "customer"  }}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/users/120077332/events")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"event\": {    \"created_at\": \"2020-01-31T00:44:07+00:00\",    \"description\": \"Order complete\",    \"properties\": {      \"billing\": {        \"address1\": \"1019 Market St\",        \"city\": \"San Francisco\",        \"state\": \"CA\",        \"zipcode\": \"94103\"      },      \"item\": {        \"name\": \"Zendesk Swag\"      }    },    \"source\": \"shoppingnow\",    \"type\": \"checkout\"  },  \"profile\": {    \"identifiers\": [      {        \"type\": \"email\",        \"value\": \"jane@example.com\"      },      {        \"type\": \"external_id\",        \"value\": \"0987654321\"      }    ],    \"name\": \"Jane Smith\",    \"source\": \"shoppingnow\",    \"type\": \"customer\"  }}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "event": {    "created_at": "2020-01-31T00:44:07+00:00",    "description": "Order complete",    "properties": {      "billing": {        "address1": "1019 Market St",        "city": "San Francisco",        "state": "CA",        "zipcode": "94103"      },      "item": {        "name": "Zendesk Swag"      }    },    "source": "shoppingnow",    "type": "checkout"  },  "profile": {    "identifiers": [      {        "type": "email",        "value": "[[email protected]](/cdn-cgi/l/email-protection)"      },      {        "type": "external_id",        "value": "0987654321"      }    ],    "name": "Jane Smith",    "source": "shoppingnow",    "type": "customer"  }});
    var config = {  method: 'POST',  url: 'https://support.zendesk.com/api/v2/users/120077332/events',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/users/120077332/events"
    payload = json.loads("""{  "event": {    "created_at": "2020-01-31T00:44:07+00:00",    "description": "Order complete",    "properties": {      "billing": {        "address1": "1019 Market St",        "city": "San Francisco",        "state": "CA",        "zipcode": "94103"      },      "item": {        "name": "Zendesk Swag"      }    },    "source": "shoppingnow",    "type": "checkout"  },  "profile": {    "identifiers": [      {        "type": "email",        "value": "[[email protected]](/cdn-cgi/l/email-protection)"      },      {        "type": "external_id",        "value": "0987654321"      }    ],    "name": "Jane Smith",    "source": "shoppingnow",    "type": "customer"  }}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/users/120077332/events")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")request.body = %q({  "event": {    "created_at": "2020-01-31T00:44:07+00:00",    "description": "Order complete",    "properties": {      "billing": {        "address1": "1019 Market St",        "city": "San Francisco",        "state": "CA",        "zipcode": "94103"      },      "item": {        "name": "Zendesk Swag"      }    },    "source": "shoppingnow",    "type": "checkout"  },  "profile": {    "identifiers": [      {        "type": "email",        "value": "[[email protected]](/cdn-cgi/l/email-protection)"      },      {        "type": "external_id",        "value": "0987654321"      }    ],    "name": "Jane Smith",    "source": "shoppingnow",    "type": "customer"  }})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**202 Accepted**


    // Status 202 Accepted
    {  "profile_id": "01E1DPYAA7HW7645KMJEY9CXRJ",  "status": "received",  "user_id": "123456"}

**400 Bad Request**


    // Status 400 Bad Request
    {  "errors": [    {      "code": "StartTimestampNotValid",      "id": "c21d8981-8940-419b-907b-7f7a2ba22cca",      "title": "Start Timestamp not valid"    }  ]}

**404 Not Found**


    // Status 404 Not Found
    {  "errors": [    {      "code": "StartTimestampNotValid",      "id": "c21d8981-8940-419b-907b-7f7a2ba22cca",      "title": "Start Timestamp not valid"    }  ]}

### Track Event Against a Sunshine Profile

  * `POST /api/v2/user_profiles/events`


Stores an event against the given Sunshine profile. If the profile does not exist, it will be created. Any additional identifier information provided is added to the profile.

#### Allowed For

  * Agents


Access also depends on agent role permissions set in **Support** > **People** > **Roles** > **People**.

#### Example body


    {  "event": {    "created_at": "2020-01-31T00:44:07+00:00",    "description": "Order complete",    "properties": {      "billing": {        "address1": "1019 Market St",        "city": "San Francisco",        "state": "CA",        "zipcode": "94103"      },      "item": {        "name": "Zendesk Swag"      }    },    "source": "shoppingnow",    "type": "checkout"  },  "profile": {    "identifiers": [      {        "type": "email",        "value": "[[email protected]](/cdn-cgi/l/email-protection)"      },      {        "type": "external_id",        "value": "0987654321"      }    ],    "name": "Jane Smith",    "source": "shoppingnow",    "type": "customer"  }}

#### Code Samples

**curl**


    curl "https://{subdomain}.zendesk.com/api/v2/user_profiles/events" \  -d {"profile":{"name": "Jane Smith", "source":"shoppingnow","type":"customer","identifiers":[{"type":"email","value":"[[email protected]](/cdn-cgi/l/email-protection)"},{"type":"external_id","value":"0987654321"}]},"event":{"source":"shoppingnow","type":"checkout","description":"Order complete","created_at":"2020-01-31T00:44:07.000Z","properties":{"item":{"name":"Zendesk Swag"},"billing":{"address1":"1019 Market St","city":"San Francisco","state":"CA","zipcode":"94103"}}}} \  -H "Content-Type: application/json" \  -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://support.zendesk.com/api/v2/user_profiles/events"	method := "POST"	payload := strings.NewReader(`{  "event": {    "created_at": "2020-01-31T00:44:07+00:00",    "description": "Order complete",    "properties": {      "billing": {        "address1": "1019 Market St",        "city": "San Francisco",        "state": "CA",        "zipcode": "94103"      },      "item": {        "name": "Zendesk Swag"      }    },    "source": "shoppingnow",    "type": "checkout"  },  "profile": {    "identifiers": [      {        "type": "email",        "value": "[[email protected]](/cdn-cgi/l/email-protection)"      },      {        "type": "external_id",        "value": "0987654321"      }    ],    "name": "Jane Smith",    "source": "shoppingnow",    "type": "customer"  }}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/user_profiles/events")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"event\": {    \"created_at\": \"2020-01-31T00:44:07+00:00\",    \"description\": \"Order complete\",    \"properties\": {      \"billing\": {        \"address1\": \"1019 Market St\",        \"city\": \"San Francisco\",        \"state\": \"CA\",        \"zipcode\": \"94103\"      },      \"item\": {        \"name\": \"Zendesk Swag\"      }    },    \"source\": \"shoppingnow\",    \"type\": \"checkout\"  },  \"profile\": {    \"identifiers\": [      {        \"type\": \"email\",        \"value\": \"jane@example.com\"      },      {        \"type\": \"external_id\",        \"value\": \"0987654321\"      }    ],    \"name\": \"Jane Smith\",    \"source\": \"shoppingnow\",    \"type\": \"customer\"  }}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "event": {    "created_at": "2020-01-31T00:44:07+00:00",    "description": "Order complete",    "properties": {      "billing": {        "address1": "1019 Market St",        "city": "San Francisco",        "state": "CA",        "zipcode": "94103"      },      "item": {        "name": "Zendesk Swag"      }    },    "source": "shoppingnow",    "type": "checkout"  },  "profile": {    "identifiers": [      {        "type": "email",        "value": "[[email protected]](/cdn-cgi/l/email-protection)"      },      {        "type": "external_id",        "value": "0987654321"      }    ],    "name": "Jane Smith",    "source": "shoppingnow",    "type": "customer"  }});
    var config = {  method: 'POST',  url: 'https://support.zendesk.com/api/v2/user_profiles/events',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/user_profiles/events"
    payload = json.loads("""{  "event": {    "created_at": "2020-01-31T00:44:07+00:00",    "description": "Order complete",    "properties": {      "billing": {        "address1": "1019 Market St",        "city": "San Francisco",        "state": "CA",        "zipcode": "94103"      },      "item": {        "name": "Zendesk Swag"      }    },    "source": "shoppingnow",    "type": "checkout"  },  "profile": {    "identifiers": [      {        "type": "email",        "value": "[[email protected]](/cdn-cgi/l/email-protection)"      },      {        "type": "external_id",        "value": "0987654321"      }    ],    "name": "Jane Smith",    "source": "shoppingnow",    "type": "customer"  }}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/user_profiles/events")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")request.body = %q({  "event": {    "created_at": "2020-01-31T00:44:07+00:00",    "description": "Order complete",    "properties": {      "billing": {        "address1": "1019 Market St",        "city": "San Francisco",        "state": "CA",        "zipcode": "94103"      },      "item": {        "name": "Zendesk Swag"      }    },    "source": "shoppingnow",    "type": "checkout"  },  "profile": {    "identifiers": [      {        "type": "email",        "value": "[[email protected]](/cdn-cgi/l/email-protection)"      },      {        "type": "external_id",        "value": "0987654321"      }    ],    "name": "Jane Smith",    "source": "shoppingnow",    "type": "customer"  }})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**202 Accepted**


    // Status 202 Accepted
    {  "profile_id": "01E1DPYAA7HW7645KMJEY9CXRJ",  "status": "received",  "user_id": "123456"}

**400 Bad Request**


    // Status 400 Bad Request
    {  "errors": [    {      "code": "StartTimestampNotValid",      "id": "c21d8981-8940-419b-907b-7f7a2ba22cca",      "title": "Start Timestamp not valid"    }  ]}

### Track Event Against a Sunshine Profile by Profile ID

  * `POST /api/v2/user_profiles/{profile_id}/events`


Stores an event against the given Sunshine profile. If the profile does not exist, it will return an error.

#### Allowed For

  * Agents


Access also depends on agent role permissions set in **Support** > **People** > **Roles** > **People**.

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
profile_id| string| Path| true| Sunshine profile ID

#### Example body


    {  "event": {    "created_at": "2020-01-31T00:44:07+00:00",    "description": "Order complete",    "properties": {      "billing": {        "address1": "1019 Market St",        "city": "San Francisco",        "state": "CA",        "zipcode": "94103"      },      "item": {        "name": "Zendesk Swag"      }    },    "source": "shoppingnow",    "type": "checkout"  }}

#### Code Samples

**curl**


    curl "https://{subdomain}.zendesk.com/api/v2/user_profiles/{profile_id}/events" \  -d {"profile":{"name": "Jane Smith", "source":"shoppingnow","type":"customer","identifiers":[{"type":"email","value":"[[email protected]](/cdn-cgi/l/email-protection)"},{"type":"external_id","value":"0987654321"}]},"event":{"source":"shoppingnow","type":"checkout","description":"Order complete","created_at":"2020-01-31T00:44:07.000Z","properties":{"item":{"name":"Zendesk Swag"},"billing":{"address1":"1019 Market St","city":"San Francisco","state":"CA","zipcode":"94103"}}}} \  -H "Content-Type: application/json" \  -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://support.zendesk.com/api/v2/user_profiles//events"	method := "POST"	payload := strings.NewReader(`{  "event": {    "created_at": "2020-01-31T00:44:07+00:00",    "description": "Order complete",    "properties": {      "billing": {        "address1": "1019 Market St",        "city": "San Francisco",        "state": "CA",        "zipcode": "94103"      },      "item": {        "name": "Zendesk Swag"      }    },    "source": "shoppingnow",    "type": "checkout"  }}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/user_profiles//events")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"event\": {    \"created_at\": \"2020-01-31T00:44:07+00:00\",    \"description\": \"Order complete\",    \"properties\": {      \"billing\": {        \"address1\": \"1019 Market St\",        \"city\": \"San Francisco\",        \"state\": \"CA\",        \"zipcode\": \"94103\"      },      \"item\": {        \"name\": \"Zendesk Swag\"      }    },    \"source\": \"shoppingnow\",    \"type\": \"checkout\"  }}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "event": {    "created_at": "2020-01-31T00:44:07+00:00",    "description": "Order complete",    "properties": {      "billing": {        "address1": "1019 Market St",        "city": "San Francisco",        "state": "CA",        "zipcode": "94103"      },      "item": {        "name": "Zendesk Swag"      }    },    "source": "shoppingnow",    "type": "checkout"  }});
    var config = {  method: 'POST',  url: 'https://support.zendesk.com/api/v2/user_profiles//events',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/user_profiles//events"
    payload = json.loads("""{  "event": {    "created_at": "2020-01-31T00:44:07+00:00",    "description": "Order complete",    "properties": {      "billing": {        "address1": "1019 Market St",        "city": "San Francisco",        "state": "CA",        "zipcode": "94103"      },      "item": {        "name": "Zendesk Swag"      }    },    "source": "shoppingnow",    "type": "checkout"  }}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/user_profiles//events")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")request.body = %q({  "event": {    "created_at": "2020-01-31T00:44:07+00:00",    "description": "Order complete",    "properties": {      "billing": {        "address1": "1019 Market St",        "city": "San Francisco",        "state": "CA",        "zipcode": "94103"      },      "item": {        "name": "Zendesk Swag"      }    },    "source": "shoppingnow",    "type": "checkout"  }})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**202 Accepted**


    // Status 202 Accepted
    {  "profile_id": "01E1DPYAA7HW7645KMJEY9CXRJ",  "status": "received",  "user_id": "123456"}

**400 Bad Request**


    // Status 400 Bad Request
    {  "errors": [    {      "code": "StartTimestampNotValid",      "id": "c21d8981-8940-419b-907b-7f7a2ba22cca",      "title": "Start Timestamp not valid"    }  ]}

**404 Not Found**


    // Status 404 Not Found
    {  "errors": [    {      "code": "StartTimestampNotValid",      "id": "c21d8981-8940-419b-907b-7f7a2ba22cca",      "title": "Start Timestamp not valid"    }  ]}

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)