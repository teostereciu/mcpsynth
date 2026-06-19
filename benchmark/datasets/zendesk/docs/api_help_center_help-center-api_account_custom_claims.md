# Account Custom Claims

*Source: https://developer.zendesk.com/api-reference/help_center/help-center-api/account_custom_claims/*

---

## On this page

  * [JSON Format](/api-reference/help_center/help-center-api/account_custom_claims/#json-format)
  * [List Account Custom Claims](/api-reference/help_center/help-center-api/account_custom_claims/#list-account-custom-claims)
  * [Show Account Custom Claim](/api-reference/help_center/help-center-api/account_custom_claims/#show-account-custom-claim)
  * [Create Account Custom Claim](/api-reference/help_center/help-center-api/account_custom_claims/#create-account-custom-claim)
  * [Update Account Custom Claim](/api-reference/help_center/help-center-api/account_custom_claims/#update-account-custom-claim)
  * [Delete Account Custom Claim](/api-reference/help_center/help-center-api/account_custom_claims/#delete-account-custom-claim)


# Account Custom Claims

## On this page

  * [JSON Format](/api-reference/help_center/help-center-api/account_custom_claims/#json-format)
  * [List Account Custom Claims](/api-reference/help_center/help-center-api/account_custom_claims/#list-account-custom-claims)
  * [Show Account Custom Claim](/api-reference/help_center/help-center-api/account_custom_claims/#show-account-custom-claim)
  * [Create Account Custom Claim](/api-reference/help_center/help-center-api/account_custom_claims/#create-account-custom-claim)
  * [Update Account Custom Claim](/api-reference/help_center/help-center-api/account_custom_claims/#update-account-custom-claim)
  * [Delete Account Custom Claim](/api-reference/help_center/help-center-api/account_custom_claims/#delete-account-custom-claim)


Account custom claims enable help center admins to expand the payload of the help center JWT.

Admins can create up to five account custom claims.

### JSON Format

Account custom claims are represented as JSON objects with the following properties

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
id| string| true| false| The unique identifier (ID) for the account custom claim
account_id| integer| true| false| The id of the account to which this custom claim belongs
brand_id| integer| true| false| The id of the brand to which this custom claim belongs
claim_identifier| string| false| true| The key. For example, the string identifying the custom claim in the token payload
claim_value| string| false| true| The custom claim value in the token payload
claim_description| string| false| false| A string that provides an explanation or rationale regarding the custom claim
created_at| string| true| false| The time the custom claim was created
updated_at| string| true| false| The time the custom claim was last updated

### List Account Custom Claims

  * `GET /api/v2/help_center/integration/account_custom_claims`


Returns a set of account custom claims for the Zendesk account and brand.

#### Allowed for

  * Admins


#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/integration/account_custom_claims.json \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/integration/account_custom_claims"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/integration/account_custom_claims")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/help_center/integration/account_custom_claims',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/integration/account_custom_claims"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/integration/account_custom_claims")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "custom_claims": [    {      "account_id": 998,      "brand_id": 10001,      "claim_description": "An example of account custom claim",      "claim_identifier": "custom-claim-1",      "claim_value": "some-claim-value",      "created_at": "2012-04-04T09:14:57Z",      "id": "01HEQFZ40TR7GMPHJZBWAZKE77",      "updated_at": "2012-04-04T09:14:57Z"    },    {      "account_id": 998,      "brand_id": 10001,      "claim_description": "An example of another account custom claim",      "claim_identifier": "custom-claim-2",      "claim_value": "another-claim-value",      "created_at": "2012-04-04T09:14:57Z",      "id": "01HEQFZBW42A0MZ31VAM88DWB1",      "updated_at": "2012-04-04T09:14:57Z"    }  ]}

### Show Account Custom Claim

  * `GET /api/v2/help_center/integration/account_custom_claims/{account_custom_claim_id}`


Shows the properties of the specified account custom claim.

#### Allowed for

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
account_custom_claim_id| string| Path| true| The unique id of the account custom claim

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/integration/account_custom_claims/{account_custom_claim_id}.json \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/integration/account_custom_claims/01HEQFZ40TR7GMPHJZBWAZKE77"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/integration/account_custom_claims/01HEQFZ40TR7GMPHJZBWAZKE77")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/help_center/integration/account_custom_claims/01HEQFZ40TR7GMPHJZBWAZKE77',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/integration/account_custom_claims/01HEQFZ40TR7GMPHJZBWAZKE77"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/integration/account_custom_claims/01HEQFZ40TR7GMPHJZBWAZKE77")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "custom_claim": {    "account_id": 998,    "brand_id": 10001,    "claim_description": "An example of account custom claim",    "claim_identifier": "custom-claim-1",    "claim_value": "some-claim-value",    "created_at": "2012-04-04T09:14:57Z",    "id": "01HEQFZ40TR7GMPHJZBWAZKE77",    "updated_at": "2012-04-04T09:14:57Z"  }}

### Create Account Custom Claim

  * `POST /api/v2/help_center/integration/account_custom_claims`


Creates an account custom claims scoped by account and brand. Each pair account/brand can create up to five acccount custom claims.

#### Allowed for

  * Admins


#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/integration/account_custom_claims.json \  -d '{ \    "custom_claim": { \      "claim_identifier": "my-new-custom-claim", \      "claim_value": "my-super-value", \      "claim_description": "my claim description:" \    } \  }' \  -v -u {email_address}/token:{api_token} -X POST -H "Content-Type: application/json"

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/integration/account_custom_claims"	method := "POST"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/integration/account_custom_claims")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'POST',  url: 'https://support.zendesk.com/api/v2/help_center/integration/account_custom_claims',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/integration/account_custom_claims"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/integration/account_custom_claims")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**201 Created**


    // Status 201 Created
    {  "custom_claim": {    "account_id": 998,    "brand_id": 10001,    "claim_description": "An example of account custom claim",    "claim_identifier": "custom-claim-1",    "claim_value": "some-claim-value",    "created_at": "2012-04-04T09:14:57Z",    "id": "01HEQFZ40TR7GMPHJZBWAZKE77",    "updated_at": "2012-04-04T09:14:57Z"  }}

**400 Bad Request**


    // Status 400 Bad Request
    {  "errors": {    "claim_value": [      "can't be blank"    ]  }}

### Update Account Custom Claim

  * `PUT /api/v2/help_center/integration/account_custom_claims/{account_custom_claim_id}`


#### Allowed for

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
account_custom_claim_id| string| Path| true| The unique id of the account custom claim

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/integration/account_custom_claims/{account_custom_claim_id}.json \  -d '{ \    "custom_claim": { \      "claim_identifier": "updated-custom-claim", \      "claim_value": "updated-super-value", \      "claim_description": "updated description:" \    } \  }' \  -v -u {email_address}/token:{api_token} -X PUT -H "Content-Type: application/json"

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/integration/account_custom_claims/01HEQFZ40TR7GMPHJZBWAZKE77"	method := "PUT"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/integration/account_custom_claims/01HEQFZ40TR7GMPHJZBWAZKE77")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'PUT',  url: 'https://support.zendesk.com/api/v2/help_center/integration/account_custom_claims/01HEQFZ40TR7GMPHJZBWAZKE77',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/integration/account_custom_claims/01HEQFZ40TR7GMPHJZBWAZKE77"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/integration/account_custom_claims/01HEQFZ40TR7GMPHJZBWAZKE77")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "custom_claim": {    "account_id": 998,    "brand_id": 10001,    "claim_description": "An example of account custom claim",    "claim_identifier": "custom-claim-1",    "claim_value": "some-claim-value",    "created_at": "2012-04-04T09:14:57Z",    "id": "01HEQFZ40TR7GMPHJZBWAZKE77",    "updated_at": "2012-04-04T09:14:57Z"  }}

**400 Bad Request**


    // Status 400 Bad Request
    {  "errors": {    "claim_value": [      "can't be blank"    ]  }}

### Delete Account Custom Claim

  * `DELETE /api/v2/help_center/integration/account_custom_claims/{account_custom_claim_id}`


#### Allowed for

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
account_custom_claim_id| string| Path| true| The unique id of the account custom claim

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/integration/account_custom_claims/{account_custom_claim_id}.json \  -v -u {email_address}/token:{api_token} -X DELETE

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/integration/account_custom_claims/01HEQFZ40TR7GMPHJZBWAZKE77"	method := "DELETE"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/integration/account_custom_claims/01HEQFZ40TR7GMPHJZBWAZKE77")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("DELETE", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'DELETE',  url: 'https://support.zendesk.com/api/v2/help_center/integration/account_custom_claims/01HEQFZ40TR7GMPHJZBWAZKE77',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/integration/account_custom_claims/01HEQFZ40TR7GMPHJZBWAZKE77"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"DELETE",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/integration/account_custom_claims/01HEQFZ40TR7GMPHJZBWAZKE77")request = Net::HTTP::Delete.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**204 No Content**


    // Status 204 No Content
    null

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)