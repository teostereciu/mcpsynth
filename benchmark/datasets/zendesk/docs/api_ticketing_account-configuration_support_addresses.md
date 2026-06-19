# Support Addresses

*Source: https://developer.zendesk.com/api-reference/ticketing/account-configuration/support_addresses/*

---

## On this page

  * [JSON format](/api-reference/ticketing/account-configuration/support_addresses/#json-format)
  * [List Support Addresses](/api-reference/ticketing/account-configuration/support_addresses/#list-support-addresses)
  * [Show Support Address](/api-reference/ticketing/account-configuration/support_addresses/#show-support-address)
  * [Create Support Address](/api-reference/ticketing/account-configuration/support_addresses/#create-support-address)
  * [Update Support Address](/api-reference/ticketing/account-configuration/support_addresses/#update-support-address)
  * [Delete Support Address](/api-reference/ticketing/account-configuration/support_addresses/#delete-support-address)
  * [Verify Support Address Forwarding](/api-reference/ticketing/account-configuration/support_addresses/#verify-support-address-forwarding)


# Support Addresses

## On this page

  * [JSON format](/api-reference/ticketing/account-configuration/support_addresses/#json-format)
  * [List Support Addresses](/api-reference/ticketing/account-configuration/support_addresses/#list-support-addresses)
  * [Show Support Address](/api-reference/ticketing/account-configuration/support_addresses/#show-support-address)
  * [Create Support Address](/api-reference/ticketing/account-configuration/support_addresses/#create-support-address)
  * [Update Support Address](/api-reference/ticketing/account-configuration/support_addresses/#update-support-address)
  * [Delete Support Address](/api-reference/ticketing/account-configuration/support_addresses/#delete-support-address)
  * [Verify Support Address Forwarding](/api-reference/ticketing/account-configuration/support_addresses/#verify-support-address-forwarding)


When you set up Zendesk Support, you have one email address: [[email protected]](/cdn-cgi/l/email-protection#473432373728353307223f262a372b22693d22292322342c6924282a). Emails received at this address become tickets.

You can provide your users with additional email addresses for submitting tickets. The additional addresses are called support addresses. You can add up to 3000 support addresses. They can be Zendesk addresses or external addresses. If adding external addresses, additional steps are required to set up forwarding from your email server to your Zendesk account.

Support addresses allow you to customize the "sender" address for your outgoing notifications. When an email is received at a support address, Zendesk responds from the same address. For example, if an email is sent to [[email protected]](/cdn-cgi/l/email-protection#ea828f869aaa8f928b879a868fc4908f848e8f9981c4898587), Zendesk sends a notification from [[email protected]](/cdn-cgi/l/email-protection#d6beb3baa696b3aeb7bba6bab3f8acb3b8b2b3a5bdf8b5b9bb).

For more information, see [Adding support addresses for users to submit tickets](https://support.zendesk.com/hc/en-us/articles/203663336).

### JSON format

Support Addresses are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
brand_id| integer| false| false| The ID of the [brand](/api-reference/ticketing/account-configuration/brands/)
cname_status| string| true| false| Whether all of the required CNAME records are set. Possible values: "unknown", "verified", "failed". Allowed values are "unknown", "verified", or "failed".
created_at| string| true| false| When the address was created
default| boolean| false| false| Whether the address is the account's default support address
dns_results| string| true| false| Verification statuses for the domain and CNAME records. Possible types: "verified", "failed". Allowed values are "verified", or "failed".
domain_verification_code| string| true| false| Verification string to be added as a TXT record to the domain. Possible types: string or null.
domain_verification_status| string| true| false| Whether the domain verification record is valid. Possible values: "unknown", "verified", "failed". Allowed values are "unknown", "verified", or "failed".
email| string| false| true| The email address. You can't change the email address of an existing support address.
forwarding_status| string| true| false| Status of email forwarding. Possible values: "unknown", "waiting", "verified", or "failed". Allowed values are "unknown", "waiting", "verified", or "failed".
id| integer| true| false| Automatically assigned when created
name| string| false| false| The name for the address
spf_status| string| true| false| Whether the SPF record is set up correctly. Possible values: "unknown", "verified", "failed". Allowed values are "unknown", "verified", or "failed".
updated_at| string| true| false| When the address was updated

You can also include the brand for each Support address in the JSON objects returned by GET requests by sideloading it. Example: `GET /api/v2/recipient_addresses?include=brands`

#### Example


    {  "brand_id": 123,  "cname_status": "verified",  "created_at": "2015-07-20T22:55:29Z",  "default": true,  "domain_verification_status": "verified",  "email": "[[email protected]](/cdn-cgi/l/email-protection)",  "forwarding_status": "unknown",  "id": 35436,  "name": "all",  "spf_status": "verified",  "updated_at": "2016-09-21T20:15:20Z"}

### List Support Addresses

  * `GET /api/v2/recipient_addresses`


Lists all the support addresses for the account.

#### Pagination

  * Cursor pagination (recommended)
  * Offset pagination


See [Pagination](/api-reference/introduction/pagination/).

Returns a maximum of 100 records per page.

#### Allowed For

  * Admins
  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
include| string| Query| false| A comma-separated list of sideloads to include in the response.
page| | Query| false| Pagination parameter. Supports both traditional offset and cursor-based pagination: - Traditional: `?page=2` (integer page number) - Cursor: `?page[size]=50&page[after]=cursor` (deepObject with size, after, before) These are mutually exclusive - use one format or the other, not both.
per_page| integer| Query| false| Number of records to return per page. Note: Default and maximum values vary by endpoint. Check endpoint-specific documentation for limits.
sort| string| Query| false| Field to sort results by. Prefix with `-` for descending order. When used with cursor pagination, this determines the cursor ordering. Example: `?sort=name` or `?sort=-created_at`

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/recipient_addresses \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/recipient_addresses?include=&page=&per_page=50&sort=name"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/recipient_addresses")		.newBuilder()		.addQueryParameter("include", "")		.addQueryParameter("page", "")		.addQueryParameter("per_page", "50")		.addQueryParameter("sort", "name");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/recipient_addresses',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'include': '',    'page': '',    'per_page': '50',    'sort': 'name',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/recipient_addresses?include=&page=&per_page=50&sort=name"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/recipient_addresses")uri.query = URI.encode_www_form("include": "", "page": "", "per_page": "50", "sort": "name")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "recipient_addresses": [    {      "brand_id": 123,      "cname_status": "verified",      "created_at": "2015-07-20T22:55:29Z",      "default": true,      "domain_verification_status": "verified",      "email": "[[email protected]](/cdn-cgi/l/email-protection)",      "forwarding_status": "unknown",      "id": 33,      "name": "Sales",      "spf_status": "verified",      "updated_at": "2016-09-21T20:15:20Z"    },    {      "brand_id": 123,      "cname_status": "verified",      "created_at": "2015-07-20T22:55:29Z",      "default": false,      "domain_verification_status": "verified",      "email": "[[email protected]](/cdn-cgi/l/email-protection)",      "forwarding_status": "unknown",      "id": 34,      "name": "Marketing",      "spf_status": "verified",      "updated_at": "2016-09-21T20:15:20Z"    }  ]}

### Show Support Address

  * `GET /api/v2/recipient_addresses/{support_address_id}`


#### Allowed For

  * Admins
  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
support_address_id| integer| Path| true| The ID of the support address

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/recipient_addresses/{support_address_id} \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/recipient_addresses/33"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/recipient_addresses/33")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/recipient_addresses/33',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/recipient_addresses/33"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/recipient_addresses/33")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "recipient_address": {    "brand_id": 123,    "cname_status": "unknown",    "created_at": "2017-04-02T22:55:29Z",    "default": true,    "email": "[[email protected]](/cdn-cgi/l/email-protection)",    "forwarding_status": "waiting",    "id": 33,    "name": "Sales",    "spf_status": "unknown",    "updated_at": "2017-04-02T22:55:29Z"  }}

### Create Support Address

  * `POST /api/v2/recipient_addresses`


Adds a Zendesk or external support address to your account.

To add a Zendesk address, use the following syntax: `{local-part}@{accountname}.zendesk.com`. Example: '[[email protected]](/cdn-cgi/l/email-protection#bac9dbd6dfc997cedfdbd7fadfc2dbd7cad6df94c0dfd4dedfc9d194d9d5d7)'. The [local-part](https://en.wikipedia.org/wiki/Email_address#Local-part) can be anything you like.

To add an external email address such as [[email protected]](/cdn-cgi/l/email-protection#f49c919884b49b999a9d83919586879c9b84da979b99), the email must already exist and you must set up forwarding on your email server. The exact steps depend on your mail server. See [Forwarding incoming email to Zendesk Support](https://support.zendesk.com/hc/en-us/articles/203663266). After setting up forwarding, run the Verify Support Address Forwarding endpoint. The address won't work in Zendesk Support until it's been verified.

#### Allowed For

  * Admins
  * Agents with permission to manage channels and extensions. See the system permissions in [Creating custom roles and assigning agents (Enterprise)](https://support.zendesk.com/hc/en-us/articles/203662026-Creating-custom-roles-and-assigning-agents-Enterprise-#topic_cxn_hig_bd) in the Support Help Center


#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/recipient_addresses \  -H "Content-Type: application/json" -X POST \  -d '{"recipient_address": {"name": "Sales", "email": "[[email protected]](/cdn-cgi/l/email-protection)", "default": false, "brand_id": 123 }}' \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/recipient_addresses"	method := "POST"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/recipient_addresses")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'POST',  url: 'https://example.zendesk.com/api/v2/recipient_addresses',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/recipient_addresses"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/recipient_addresses")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**201 Created**


    // Status 201 Created
    {  "recipient_address": {    "brand_id": 123,    "cname_status": "verified",    "created_at": "2017-04-02T22:55:29Z",    "default": false,    "email": "[[email protected]](/cdn-cgi/l/email-protection)",    "forwarding_status": "waiting",    "id": 33,    "name": "Sales",    "spf_status": "verified",    "updated_at": "2017-04-02T22:55:29Z"  }}

### Update Support Address

  * `PUT /api/v2/recipient_addresses/{support_address_id}`


Updates an existing support address for your account.

You can't use this endpoint to update a support address's `email` property. Instead, you can create a new address using the Create Support Address endpoint.

#### Allowed For

  * Admins
  * Agents with permission to manage channels and extensions. See the system permissions in [Creating custom roles and assigning agents (Enterprise)](https://support.zendesk.com/hc/en-us/articles/203662026-Creating-custom-roles-and-assigning-agents-Enterprise-#topic_cxn_hig_bd) in the Support Help Center


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
support_address_id| integer| Path| true| The ID of the support address

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/recipient_addresses/{support_address_id} \  -H "Content-Type: application/json" -X PUT \  -d '{"recipient_address": {"name": "Sales" }}' \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/recipient_addresses/33"	method := "PUT"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/recipient_addresses/33")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'PUT',  url: 'https://example.zendesk.com/api/v2/recipient_addresses/33',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/recipient_addresses/33"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/recipient_addresses/33")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "recipient_address": {    "brand_id": 123,    "created_at": "2017-04-02T22:55:29Z",    "default": true,    "email": "[[email protected]](/cdn-cgi/l/email-protection)",    "forwarding_status": "verified",    "id": 33,    "name": "Sales",    "updated_at": "2017-05-02T22:55:29Z"  }}

### Delete Support Address

  * `DELETE /api/v2/recipient_addresses/{support_address_id}`


Deletes a support address.

#### Allowed For

  * Admins
  * Agents with permission to manage channels and extensions. See the system permissions in [Creating custom roles and assigning agents (Enterprise)](https://support.zendesk.com/hc/en-us/articles/203662026-Creating-custom-roles-and-assigning-agents-Enterprise-#topic_cxn_hig_bd) in the Support Help Center


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
support_address_id| integer| Path| true| The ID of the support address

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/recipient_addresses/{support_address_id} \  -v -u {email_address}/token:{api_token} -X DELETE

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/recipient_addresses/33"	method := "DELETE"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/recipient_addresses/33")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("DELETE", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'DELETE',  url: 'https://example.zendesk.com/api/v2/recipient_addresses/33',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/recipient_addresses/33"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"DELETE",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/recipient_addresses/33")request = Net::HTTP::Delete.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**204 No Content**


    // Status 204 No Content
    null

### Verify Support Address Forwarding

  * `PUT /api/v2/recipient_addresses/{support_address_id}/verify`


Sends a test email to the specified support address to verify that email forwarding for the address works. An external support address won't work in Zendesk Support until it's verified.

**Note** : You don't need to verify Zendesk system support addresses.

The endpoint takes the following body: `{"type": "forwarding"}`. The value of the `type` property defaults to "forwarding" if none is specified, but the values "spf" and "dns" are also accepted.

Use this endpoint after adding an external support address to Zendesk Support and setting up forwarding on your email server. See [Forwarding incoming email to Zendesk Support](https://support.zendesk.com/hc/en-us/articles/203663266).

The endpoint doesn't return the results of the test. Instead, use the Show Support Address endpoint to check that the `forwarding_status` property is "verified".

Other verification checks can also be performed using this API. These include SPF checks and DNS checks.

When calling the endpoint with `type` set to "spf", it will queries the DNS records to check that the SPF records for Zendesk are present for outbound emails.

When calling the endpoint with `type` set to "dns", it runs checks on your CNAME records to make sure they are set up properly in your DNS.

#### Allowed For

  * Admins
  * Agents with permission to manage channels and extensions. See the system permissions in [Creating custom roles and assigning agents (Enterprise)](https://support.zendesk.com/hc/en-us/articles/203662026-Creating-custom-roles-and-assigning-agents-Enterprise-#topic_cxn_hig_bd) in the Support Help Center


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
support_address_id| integer| Path| true| The ID of the support address

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/recipient_addresses/{support_address_id}/verify \  -H "Content-Type: application/json" -X PUT \  -d '{"type": "forwarding"}' \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/recipient_addresses/33/verify"	method := "PUT"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/recipient_addresses/33/verify")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'PUT',  url: 'https://example.zendesk.com/api/v2/recipient_addresses/33/verify',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/recipient_addresses/33/verify"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/recipient_addresses/33/verify")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    null

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)