# Brands

*Source: https://developer.zendesk.com/api-reference/ticketing/account-configuration/brands/*

---

## On this page

  * [JSON format](/api-reference/ticketing/account-configuration/brands/#json-format)
  * [List Brands](/api-reference/ticketing/account-configuration/brands/#list-brands)
  * [Show a Brand](/api-reference/ticketing/account-configuration/brands/#show-a-brand)
  * [Create Brand](/api-reference/ticketing/account-configuration/brands/#create-brand)
  * [Update a Brand](/api-reference/ticketing/account-configuration/brands/#update-a-brand)
  * [Delete a Brand](/api-reference/ticketing/account-configuration/brands/#delete-a-brand)
  * [Check Host Mapping Validity](/api-reference/ticketing/account-configuration/brands/#check-host-mapping-validity)
  * [Check Host Mapping Validity for an Existing Brand](/api-reference/ticketing/account-configuration/brands/#check-host-mapping-validity-for-an-existing-brand)


# Brands

## On this page

  * [JSON format](/api-reference/ticketing/account-configuration/brands/#json-format)
  * [List Brands](/api-reference/ticketing/account-configuration/brands/#list-brands)
  * [Show a Brand](/api-reference/ticketing/account-configuration/brands/#show-a-brand)
  * [Create Brand](/api-reference/ticketing/account-configuration/brands/#create-brand)
  * [Update a Brand](/api-reference/ticketing/account-configuration/brands/#update-a-brand)
  * [Delete a Brand](/api-reference/ticketing/account-configuration/brands/#delete-a-brand)
  * [Check Host Mapping Validity](/api-reference/ticketing/account-configuration/brands/#check-host-mapping-validity)
  * [Check Host Mapping Validity for an Existing Brand](/api-reference/ticketing/account-configuration/brands/#check-host-mapping-validity-for-an-existing-brand)


Brands are your customer-facing identities. They might represent multiple products or services, or they might literally be multiple brands owned and represented by your company.

The default brand is the one that tickets get assigned to if the ticket is generated from a non-branded channel. You can update the default brand using the [Update Account Settings](/api-reference/ticketing/account-configuration/account_settings/#update-account-settings) endpoint.

### JSON format

Brands are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
active| boolean| false| false| If the brand is set as active
brand_url| string| false| false| The url of the brand
created_at| string| true| false| The time the brand was created
default| boolean| false| false| Is the brand the default brand for this account
has_help_center| boolean| false| false| If the brand has a Help Center
help_center_state| string| true| false| The state of the Help Center. Allowed values are "enabled", "disabled", or "restricted".
host_mapping| string| false| false| The hostmapping to this brand, if any. Only admins view this property.
id| integer| true| false| The ID automatically assigned when the brand is created
is_deleted| boolean| false| false| If the brand object is deleted or not
logo| object| false| false| A file represented as an [Attachment](/api-reference/ticketing/tickets/ticket-attachments/) object
name| string| false| true| The name of the brand
signature_template| string| false| false| The signature template for a brand
subdomain| string| false| true| The subdomain of the brand
ticket_form_ids| array| true| false| The ids of ticket forms that are available for use by a brand
updated_at| string| true| false| The time of the last update of the brand
url| string| true| false| The API url of this brand

#### Example


    {  "active": true,  "brand_url": "https://brand1.com",  "created_at": "2012-04-02T22:55:29Z",  "default": true,  "has_help_center": true,  "help_center_state": "enabled",  "host_mapping": "brand1.com",  "id": 47,  "logo": {    "content_type": "image/png",    "content_url": "https://company.zendesk.com/logos/brand1_logo.png",    "file_name": "brand1_logo.png",    "id": 928374,    "size": 166144,    "thumbnails": [      {        "content_type": "image/png",        "content_url": "https://company.zendesk.com/photos/brand1_logo_thumb.png",        "file_name": "brand1_logo_thumb.png",        "id": 928375,        "mapped_content_url": "https://company.com/photos/brand1_logo_thumb.png",        "size": 58298,        "url": "https://company.zendesk.com/api/v2/attachments/928375"      },      {        "content_type": "image/png",        "content_url": "https://company.zendesk.com/photos/brand1_logo_small.png",        "file_name": "brand1_logo_small.png",        "id": 928376,        "mapped_content_url": "https://company.com/photos/brand1_logo_small.png",        "size": 58298,        "url": "https://company.zendesk.com/api/v2/attachments/928376"      }    ],    "url": "https://company.zendesk.com/api/v2/attachments/928374"  },  "name": "Brand 1",  "signature_template": "{{agent.signature}}",  "subdomain": "brand1",  "ticket_form_ids": [    47,    33,    22  ],  "updated_at": "2012-04-02T22:55:29Z",  "url": "https://company.zendesk.com/api/v2/brands/47"}

### List Brands

  * `GET /api/v2/brands`


Returns a list of all brands for your account sorted by name.

#### Allowed for

  * Admins
  * Agents with the `assign_tickets_to_any_brand` permission can list all brands for the account
  * Agents without the `assign_tickets_to_any_brand` permission can only list brands they are members of


#### Pagination

  * Cursor pagination


See [Pagination](/api-reference/introduction/pagination/).

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
page| | Query| false| Cursor pagination parameters using deepObject format. Use `?page[size]=50&page[after]=cursor` to paginate through results.
sort| string| Query| false| Field to sort results by. Prefix with `-` for descending order. When used with cursor pagination, this determines the cursor ordering. Example: `?sort=name` or `?sort=-created_at`

#### Code Samples

**cURL**


    curl https://{subdomain}.zendesk.com/api/v2/brands \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/brands?page=&sort=name"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/brands")		.newBuilder()		.addQueryParameter("page", "")		.addQueryParameter("sort", "name");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/brands',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'page': '',    'sort': 'name',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/brands?page=&sort=name"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/brands")uri.query = URI.encode_www_form("page": "", "sort": "name")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "brands": [    {      "active": true,      "brand_url": "https://brand1.zendesk.com",      "created_at": "2019-08-06T02:43:39Z",      "default": true,      "has_help_center": true,      "help_center_state": "enabled",      "host_mapping": "brand1.com",      "id": 360002783572,      "is_deleted": false,      "logo": {        "content_type": "image/png",        "content_url": "https://company.zendesk.com/logos/brand1_logo.png",        "file_name": "brand1_logo.png",        "id": 928374,        "mapped_content_url": "https://company.com/logos/brand1_logo.png",        "size": 166144,        "thumbnails": [          {            "content_type": "image/png",            "content_url": "https://company.zendesk.com/photos/brand1_logo_thumb.png",            "file_name": "brand1_logo_thumb.png",            "id": 928375,            "mapped_content_url": "https://company.com/photos/brand1_logo_thumb.png",            "size": 58298,            "url": "https://company.zendesk.com/api/v2/attachments/928375"          },          {            "content_type": "image/png",            "content_url": "https://company.zendesk.com/photos/brand1_logo_small.png",            "file_name": "brand1_logo_small.png",            "id": 928376,            "mapped_content_url": "https://company.com/photos/brand1_logo_small.png",            "size": 58298,            "url": "https://company.zendesk.com/api/v2/attachments/928376"          }        ],        "url": "https://company.zendesk.com/api/v2/attachments/928374"      },      "name": "Brand 1",      "signature_template": "{{agent.signature}}",      "subdomain": "hello-world",      "ticket_form_ids": [        360000660811      ],      "updated_at": "2019-08-06T02:43:40Z",      "url": "https://company.zendesk.com/api/v2/brands/360002783572"    }  ],  "count": 1,  "next_page": null,  "previous_page": null}

### Show a Brand

  * `GET /api/v2/brands/{brand_id}`


Returns a brand for your account.

#### Allowed for

  * Admins, Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
brand_id| integer| Path| true| The ID of the brand

#### Code Samples

**cURL**


    curl https://{subdomain}.zendesk.com/api/v2/brands/{brand_id} \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/brands/360002783572"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/brands/360002783572")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/brands/360002783572',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/brands/360002783572"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/brands/360002783572")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "brand": {    "active": true,    "brand_url": "https://brand1.zendesk.com",    "created_at": "2019-08-06T02:43:39Z",    "default": true,    "has_help_center": true,    "help_center_state": "enabled",    "host_mapping": "brand1.com",    "id": 360002783572,    "is_deleted": false,    "logo": {      "content_type": "image/png",      "content_url": "https://company.zendesk.com/logos/brand1_logo.png",      "file_name": "brand1_logo.png",      "id": 928374,      "mapped_content_url": "https://company.com/logos/brand1_logo.png",      "size": 166144,      "thumbnails": [        {          "content_type": "image/png",          "content_url": "https://company.zendesk.com/photos/brand1_logo_thumb.png",          "file_name": "brand1_logo_thumb.png",          "id": 928375,          "mapped_content_url": "https://company.com/photos/brand1_logo_thumb.png",          "size": 58298,          "url": "https://company.zendesk.com/api/v2/attachments/928375"        },        {          "content_type": "image/png",          "content_url": "https://company.zendesk.com/photos/brand1_logo_small.png",          "file_name": "brand1_logo_small.png",          "id": 928376,          "mapped_content_url": "https://company.com/photos/brand1_logo_small.png",          "size": 58298,          "url": "https://company.zendesk.com/api/v2/attachments/928376"        }      ],      "url": "https://company.zendesk.com/api/v2/attachments/928374"    },    "name": "Brand 1",    "signature_template": "{{agent.signature}}",    "subdomain": "hello-world",    "ticket_form_ids": [      360000660811    ],    "updated_at": "2019-08-06T02:43:40Z",    "url": "https://company.zendesk.com/api/v2/brands/360002783572"  }}

### Create Brand

  * `POST /api/v2/brands`


#### Allowed for

  * Admins


#### Example body


    {  "brand": {    "name": "Brand 1",    "subdomain": "Brand1"  }}

#### Code Samples

**cURL**


    curl https://{subdomain}.zendesk.com/api/v2/brands \  -H "Content-Type: application/json" -X POST \  -d '{"brand": {"name": "Brand 1", "subdomain": "brand1"}}' \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://example.zendesk.com/api/v2/brands"	method := "POST"	payload := strings.NewReader(`{  "brand": {    "name": "Brand 1",    "subdomain": "Brand1"  }}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/brands")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"brand\": {    \"name\": \"Brand 1\",    \"subdomain\": \"Brand1\"  }}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "brand": {    "name": "Brand 1",    "subdomain": "Brand1"  }});
    var config = {  method: 'POST',  url: 'https://example.zendesk.com/api/v2/brands',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/brands"
    payload = json.loads("""{  "brand": {    "name": "Brand 1",    "subdomain": "Brand1"  }}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/brands")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")request.body = %q({  "brand": {    "name": "Brand 1",    "subdomain": "Brand1"  }})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**201 Created**


    // Status 201 Created
    {  "brand": {    "active": true,    "brand_url": "https://brand1.zendesk.com",    "created_at": "2019-08-06T02:43:39Z",    "default": true,    "has_help_center": true,    "help_center_state": "enabled",    "host_mapping": "brand1.com",    "id": 360002783572,    "is_deleted": false,    "logo": {      "content_type": "image/png",      "content_url": "https://company.zendesk.com/logos/brand1_logo.png",      "file_name": "brand1_logo.png",      "id": 928374,      "mapped_content_url": "https://company.com/logos/brand1_logo.png",      "size": 166144,      "thumbnails": [        {          "content_type": "image/png",          "content_url": "https://company.zendesk.com/photos/brand1_logo_thumb.png",          "file_name": "brand1_logo_thumb.png",          "id": 928375,          "mapped_content_url": "https://company.com/photos/brand1_logo_thumb.png",          "size": 58298,          "url": "https://company.zendesk.com/api/v2/attachments/928375"        },        {          "content_type": "image/png",          "content_url": "https://company.zendesk.com/photos/brand1_logo_small.png",          "file_name": "brand1_logo_small.png",          "id": 928376,          "mapped_content_url": "https://company.com/photos/brand1_logo_small.png",          "size": 58298,          "url": "https://company.zendesk.com/api/v2/attachments/928376"        }      ],      "url": "https://company.zendesk.com/api/v2/attachments/928374"    },    "name": "Brand 1",    "signature_template": "{{agent.signature}}",    "subdomain": "hello-world",    "ticket_form_ids": [      360000660811    ],    "updated_at": "2019-08-06T02:43:40Z",    "url": "https://company.zendesk.com/api/v2/brands/360002783572"  }}

### Update a Brand

  * `PUT /api/v2/brands/{brand_id}`


Returns an updated brand.

#### Allowed for

  * Admins


#### Updating a Brand's Image

A brand image can be updated by uploading a local file using the update brand endpoint. See the **Using curl** sections below for more information.

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
brand_id| integer| Path| true| The ID of the brand

#### Example body


    {  "brand": {    "active": true,    "host_mapping": "brand1.com",    "name": "Brand 1",    "subdomain": "Brand1"  }}

#### Code Samples

**cURL**

Update brand details with JSON.


    curl https://{subdomain}.zendesk.com/api/v2/brands/{brand_id} \  -H "Content-Type: application/json" -X PUT \  -d '{"brand": {"name": "Brand 1", "subdomain": "brand1", "host_mapping": "brand1.com", "active": true}}' \  -v -u {email_address}/token:{api_token}}

**cURL**

Update brand image by uploading a local image file.


    curl -v -u {email_address}/token:{api_token} -X PUT \  -F "brand[logo][uploaded_data]=@/path/to/image/image.jpg" \  https://{subdomain}.zendesk.com/api/v2/brands/{brand_id}

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://example.zendesk.com/api/v2/brands/360002783572"	method := "PUT"	payload := strings.NewReader(`{  "brand": {    "active": true,    "host_mapping": "brand1.com",    "name": "Brand 1",    "subdomain": "Brand1"  }}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/brands/360002783572")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"brand\": {    \"active\": true,    \"host_mapping\": \"brand1.com\",    \"name\": \"Brand 1\",    \"subdomain\": \"Brand1\"  }}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "brand": {    "active": true,    "host_mapping": "brand1.com",    "name": "Brand 1",    "subdomain": "Brand1"  }});
    var config = {  method: 'PUT',  url: 'https://example.zendesk.com/api/v2/brands/360002783572',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/brands/360002783572"
    payload = json.loads("""{  "brand": {    "active": true,    "host_mapping": "brand1.com",    "name": "Brand 1",    "subdomain": "Brand1"  }}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/brands/360002783572")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")request.body = %q({  "brand": {    "active": true,    "host_mapping": "brand1.com",    "name": "Brand 1",    "subdomain": "Brand1"  }})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "brand": {    "active": true,    "brand_url": "https://brand1.zendesk.com",    "created_at": "2019-08-06T02:43:39Z",    "default": true,    "has_help_center": true,    "help_center_state": "enabled",    "host_mapping": "brand1.com",    "id": 360002783572,    "is_deleted": false,    "logo": {      "content_type": "image/png",      "content_url": "https://company.zendesk.com/logos/brand1_logo.png",      "file_name": "brand1_logo.png",      "id": 928374,      "mapped_content_url": "https://company.com/logos/brand1_logo.png",      "size": 166144,      "thumbnails": [        {          "content_type": "image/png",          "content_url": "https://company.zendesk.com/photos/brand1_logo_thumb.png",          "file_name": "brand1_logo_thumb.png",          "id": 928375,          "mapped_content_url": "https://company.com/photos/brand1_logo_thumb.png",          "size": 58298,          "url": "https://company.zendesk.com/api/v2/attachments/928375"        },        {          "content_type": "image/png",          "content_url": "https://company.zendesk.com/photos/brand1_logo_small.png",          "file_name": "brand1_logo_small.png",          "id": 928376,          "mapped_content_url": "https://company.com/photos/brand1_logo_small.png",          "size": 58298,          "url": "https://company.zendesk.com/api/v2/attachments/928376"        }      ],      "url": "https://company.zendesk.com/api/v2/attachments/928374"    },    "name": "Brand 1",    "signature_template": "{{agent.signature}}",    "subdomain": "hello-world",    "ticket_form_ids": [      360000660811    ],    "updated_at": "2019-08-06T02:43:40Z",    "url": "https://company.zendesk.com/api/v2/brands/360002783572"  }}

### Delete a Brand

  * `DELETE /api/v2/brands/{brand_id}`


Deletes a brand.

#### Allowed for

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
brand_id| integer| Path| true| The ID of the brand

#### Code Samples

**cURL**


    curl https://{subdomain}.zendesk.com/api/v2/brands/{brand_id} \  -X DELETE -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/brands/360002783572"	method := "DELETE"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/brands/360002783572")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("DELETE", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'DELETE',  url: 'https://example.zendesk.com/api/v2/brands/360002783572',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/brands/360002783572"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"DELETE",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/brands/360002783572")request = Net::HTTP::Delete.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**204 No Content**


    // Status 204 No Content
    null

### Check Host Mapping Validity

  * `GET /api/v2/brands/check_host_mapping?host_mapping={host_mapping}&subdomain={subdomain}`


Returns a JSON object determining whether a host mapping is valid for a given subdomain.

#### Allowed for

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
host_mapping| string| Query| true| The hostmapping to a brand, if any (only admins view this key)
subdomain| string| Query| true| Subdomain for a given Zendesk account address

#### Code Samples

**cURL**


    curl 'https://{subdomain}.zendesk.com/api/v2/brands/check_host_mapping?host_mapping={host_mapping}&subdomain={subdomain}' \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/brands/check_host_mapping?host_mapping=brand1.com&subdomain=Brand1"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/brands/check_host_mapping")		.newBuilder()		.addQueryParameter("host_mapping", "brand1.com")		.addQueryParameter("subdomain", "Brand1");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/brands/check_host_mapping',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'host_mapping': 'brand1.com',    'subdomain': 'Brand1',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/brands/check_host_mapping?host_mapping=brand1.com&subdomain=Brand1"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/brands/check_host_mapping")uri.query = URI.encode_www_form("host_mapping": "brand1.com", "subdomain": "Brand1")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "cname": "bar.zendesk.com",  "is_valid": true}

### Check Host Mapping Validity for an Existing Brand

  * `GET /api/v2/brands/{brand_id}/check_host_mapping`


Returns a JSON object determining whether a host mapping is valid for the given brand.

#### Allowed for

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
brand_id| integer| Path| true| The ID of the brand

#### Code Samples

**cURL**


    curl "https://{subdomain}.zendesk.com/api/v2/brands/{brand_id}/check_host_mapping" \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/brands/360002783572/check_host_mapping"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/brands/360002783572/check_host_mapping")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/brands/360002783572/check_host_mapping',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/brands/360002783572/check_host_mapping"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/brands/360002783572/check_host_mapping")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "cname": "bar.zendesk.com",  "is_valid": true}

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)