# Incremental Skill-based Routing

*Source: https://developer.zendesk.com/api-reference/ticketing/ticket-management/incremental_skill_based_routing/*

---

## On this page

  * [JSON Format](/api-reference/ticketing/ticket-management/incremental_skill_based_routing/#json-format)
  * [Pagination](/api-reference/ticketing/ticket-management/incremental_skill_based_routing/#pagination)
  * [JSON Format for Routing Attributes](/api-reference/ticketing/ticket-management/incremental_skill_based_routing/#json-format-for-routing-attributes)
  * [JSON Format for Routing Attribute Values](/api-reference/ticketing/ticket-management/incremental_skill_based_routing/#json-format-for-routing-attribute-values)
  * [JSON Format for Routing Instance Values](/api-reference/ticketing/ticket-management/incremental_skill_based_routing/#json-format-for-routing-instance-values)
  * [Incremental Attributes Export](/api-reference/ticketing/ticket-management/incremental_skill_based_routing/#incremental-attributes-export)
  * [Incremental Attributes Values Export](/api-reference/ticketing/ticket-management/incremental_skill_based_routing/#incremental-attributes-values-export)
  * [Incremental Instance Values Export](/api-reference/ticketing/ticket-management/incremental_skill_based_routing/#incremental-instance-values-export)


# Incremental Skill-based Routing

## On this page

  * [JSON Format](/api-reference/ticketing/ticket-management/incremental_skill_based_routing/#json-format)
  * [Pagination](/api-reference/ticketing/ticket-management/incremental_skill_based_routing/#pagination)
  * [JSON Format for Routing Attributes](/api-reference/ticketing/ticket-management/incremental_skill_based_routing/#json-format-for-routing-attributes)
  * [JSON Format for Routing Attribute Values](/api-reference/ticketing/ticket-management/incremental_skill_based_routing/#json-format-for-routing-attribute-values)
  * [JSON Format for Routing Instance Values](/api-reference/ticketing/ticket-management/incremental_skill_based_routing/#json-format-for-routing-instance-values)
  * [Incremental Attributes Export](/api-reference/ticketing/ticket-management/incremental_skill_based_routing/#incremental-attributes-export)
  * [Incremental Attributes Values Export](/api-reference/ticketing/ticket-management/incremental_skill_based_routing/#incremental-attributes-values-export)
  * [Incremental Instance Values Export](/api-reference/ticketing/ticket-management/incremental_skill_based_routing/#incremental-instance-values-export)


You can use the Incremental Skill-based Routing API to export data on the creation, update, and deletion of skill types, skills, and instance values. To learn more about the feature, see [Using skills-based routing](https://support.zendesk.com/hc/en-us/articles/360000789788) in the Support Help Center.

In this API, skill types are named _attributes_ and skills are named _attribute values_.

Skill-based routing is only available on the Enterprise plan and above.

### JSON Format

The exported items are represented as JSON objects. The format depends on the exported resource, but all have the following additional common attributes:

Name| Type| Comment
---|---|---
end_time| integer| The most recent resource creation time present in this result set in Unix epoch time
next_page| string| The URL that should be called to get the next set of results
count| integer| The number of results returned for the current request

For complete lists of attributes, see the JSON format sections below.

### Pagination

The endpoints of the skill-based routing API return a maximum of 3000 records per page.

When the response exceeds the per-page maximum, you can paginate to the next page via the `next_page` URL in the response body:


    {  "instance_values": [ ... ],  "count": 1234,  "end_time": "1535671451"  "next_page": "https://{subdomain}.zendesk.com/api/v2/incremental/routing/instance_values?cursor=cccf1b69-acab-11e8-9d65-f1b3d4e2d609"}

Stop paging when the `count` attribute is 0.

The pagination for skill-based incremental export endpoints works slightly differently from other endpoints. The `per_page` parameter doesn't apply because of the time-based way these endpoints return records. The `limit` parameter doesn't apply because of the way a single record can generate multiple events.

Unlike other endpoints, skill-based incremental export endpoints uses cursor-based pagination. The `cursor` parameter is a non-human-readable argument you can use to move forward or backward in time. The cursor is a read-only URL parameter that's only available in API responses.

### JSON Format for Routing Attributes

A routing attribute is a skill type. Routing attributes have the following format:

Name| Type| Comment
---|---|---
id| string| Automatically assigned when an attribute is created
name| string| The name of the attribute
time| date| The time the attribute was created, updated, or deleted
type| string| One of "create", "update", or "delete"

#### Example


    {  "id":   "7c43bca9-8c7b-11e8-b808-b99aed889f62",  "name": "Languages",  "time": "2018-07-21T07:17:42Z",  "type": "create"}

### JSON Format for Routing Attribute Values

A routing attribute value is a skill. Routing attribute values have the following format:

Name| Type| Comment
---|---|---
id| string| Automatically assigned when an attribute value is created
attribute_id| string| Id of the associated attribute
name| string| The name of the attribute value
time| date| The time the attribute value was created, updated, or deleted
type| string| One of "create", "update", or "delete"

#### Example


    {  "id": "19ed17fb-7326-11e8-b07e-9de44e7e7f20",  "attribute_id": "7c43bca9-8c7b-11e8-b808-b99aed889f62",  "name": "English",  "time": "2018-06-19T01:33:26Z",  "type": "create"}

### JSON Format for Routing Instance Values

Routing instance values have the following format:

Name| Type| Comment
---|---|---
id| string| Automatically assigned when an instance value is created
attribute_value_id| string| Id of the associated attribute value
instance_id| string| Id of the associated agent or ticket
time| date| The time the instance value was created or deleted
type| string| One of "associate_agent", "unassociate_agent", "associate_ticket", or "unassociate_ticket"

#### Example


    {  "id": "62055cad-7326-11e8-b07e-73653560136b",  "attribute_value_id": "19ed17fb-7326-11e8-b07e-9de44e7e7f20",  "instance_id": "10001",  "time": "2018-06-19T01:35:27Z",  "type": "associate_agent"}

### Incremental Attributes Export

  * `GET /api/v2/incremental/routing/attributes`


Returns a stream of changes that occurred on routing attributes.

#### Allowed For

  * Admins


#### Parameters

Optional

Name| Type| Comment
---|---|---
cursor| string| The `cursor` parameter is a non-human-readable argument you can use to move forward or backward in time. The cursor is a read-only URL parameter that's only available in API responses. See Pagination.

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/incremental/routing/attributes \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/incremental/routing/attributes"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/incremental/routing/attributes")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/incremental/routing/attributes',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/incremental/routing/attributes"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/incremental/routing/attributes")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "attributes": [    {      "id": "15821cba-7326-11e8-b07e-950ba849aa27",      "name": "Languages",      "time": "2018-06-19T01:33:19Z",      "type": "create"    }  ],  "count": 1200,  "end_time": 1533266020,  "next_page": "https://{subdomain}.zendesk.com/api/v2/incremental/routing/attributes?cursor=7d724c71-3911-11e8-9621-836b8c683dc6"}

### Incremental Attributes Values Export

  * `GET /api/v2/incremental/routing/attribute_values`


Returns a stream of changes that occurred on routing attribute values.

#### Allowed For

  * Admins


#### Parameters

Optional

Name| Type| Comment
---|---|---
cursor| string| The `cursor` parameter is a non-human-readable argument you can use to move forward or backward in time. The cursor is a read-only URL parameter that's only available in API responses. See Pagination.

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/incremental/routing/attribute_values \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/incremental/routing/attribute_values"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/incremental/routing/attribute_values")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/incremental/routing/attribute_values',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/incremental/routing/attribute_values"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/incremental/routing/attribute_values")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "attribute_values": [    {      "attribute_id": "15821cba-7326-11e8-b07e-950ba849aa27",      "id": "19ed17fb-7326-11e8-b07e-9de44e7e7f20",      "name": "English",      "time": "2018-06-19T01:33:26Z",      "type": "create"    }  ],  "count": 1200,  "end_time": 1533266020,  "next_page": "https://{subdomain}.zendesk.com/api/v2/incremental/routing/attribute_values?cursor=7d724c71-3911-11e8-9621-836b8c683dc6"}

### Incremental Instance Values Export

  * `GET /api/v2/incremental/routing/instance_values`


Returns a stream of changes that occurred on routing instance values. Changes are grouped by `attribute_value_id`, with associate type events listed alongside unassociate type events based on the unassociate eventâs timestamp.

#### Allowed For

  * Admins


#### Parameters

Optional

Name| Type| Comment
---|---|---
cursor| string| The `cursor` parameter is a non-human-readable argument you can use to move forward or backward in time. The cursor is a read-only URL parameter that's only available in API responses. See Pagination.

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/incremental/routing/instance_values \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/incremental/routing/instance_values"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/incremental/routing/instance_values")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/incremental/routing/instance_values',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/incremental/routing/instance_values"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/incremental/routing/instance_values")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "count": 1200,  "end_time": 1533266020,  "instance_values": [    {      "attribute_value_id": "19ed17fb-7326-11e8-b07e-9ab44e7e7f28",      "id": "62055cad-7326-11e8-b07e-73653560136b",      "instance_id": "10001",      "time": "2019-06-19T01:35:27Z",      "type": "associate_agent"    },    {      "attribute_value_id": "19ed17fb-7326-11e8-b07e-9ab44e7e7f28",      "id": "62055cad-7326-11e8-b07e-cf1082b7e6d4",      "instance_id": "11375",      "time": "2019-06-19T01:35:27Z",      "type": "associate_agent"    },    {      "attribute_value_id": "19ed17fb-7326-11e8-b07e-9ab44e7e7f28",      "id": "62055cad-7326-11e8-b07e-5b8483a47e24",      "instance_id": "14187",      "time": "2020-11-14T16:32:22Z",      "type": "unassociate_agent"    }  ],  "next_page": "https://{subdomain}.zendesk.com/api/v2/incremental/routing/instance_values?cursor=62055cad-7326-11e8-b07e-73653560136b"}

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)