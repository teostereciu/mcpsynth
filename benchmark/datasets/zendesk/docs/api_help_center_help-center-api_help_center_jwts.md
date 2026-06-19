# Help Center JWTs

*Source: https://developer.zendesk.com/api-reference/help_center/help-center-api/help_center_jwts/*

---

## On this page

  * [New Token](/api-reference/help_center/help-center-api/help_center_jwts/#new-token)
  * [List Public Keys](/api-reference/help_center/help-center-api/help_center_jwts/#list-public-keys)


# Help Center JWTs

## On this page

  * [New Token](/api-reference/help_center/help-center-api/help_center_jwts/#new-token)
  * [List Public Keys](/api-reference/help_center/help-center-api/help_center_jwts/#list-public-keys)


A Zendesk help center theme can include client-side JavaScript that makes REST API calls and other HTTP requests from the browser. When making client-side requests to third-party APIs from a help center, you can include a signed help center JSON Web Token (JWT) in the request.

The server that receives the request can then use a related JSON Web Key (JWK) to verify the JWT's signature. This verification ensures the request is legitimate and originated from the help center.

The help center JWT's payload includes the user's Zendesk email address, Zendesk user id, and external user id. The JWT's payload can be extended to include extra information via the [account custom claims](/api-reference/help_center/help-center-api/account_custom_claims/) feature.

The server receiving the JWT can use these identifiers to access and return related data for the user.

Help center JWTs are supported on Guide Enterprise and Suite Enterprise plans. If you are on any other plan, you will receive a 404 error.

For more information, see [Making third-party API requests with help center JWTs](/documentation/help_center/help-center-api/using-the-help-center-api/secured-requests/#making-third-party-api-requests-with-help-center-jwts).

### New Token

  * `GET /api/v2/help_center/integration/token`


Returns a signed help center JWT for the Zendesk user making the request. You typically make calls to this endpoint in the browser from a help center.

For information about the JWT's structure and data, see [JWT structure](/documentation/help_center/help-center-api/using-the-help-center-api/secured-requests/#jwt-structure).

#### JSON format

Help center JWTs are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
token| string| true| false| Signed help center JWT for the Zendesk user making the request

#### Allowed for

  * End users


#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/integration/token.json \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/integration/token"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/integration/token")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/help_center/integration/token',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/integration/token"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/integration/token")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "token": "eyJ0eXAi..."}

### List Public Keys

  * `GET /api/v2/help_center/integration/keys`


Returns a set of help center JSON web keys (JWKs) for the Zendesk account.

Each JWK contains the components needed to construct the public signing key for the matching help center JWT's signature. Use the `kid` in the JWT's header to find the matching JWK.

#### JSON format

Help center JWKs are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
kty| string| true| false| The type of cryptographic algorithms used to sign JWTs. For help center JWKs, the value is "RSA"
n| string| true| false| The modulus for the RSA public key used to sign the matching JWT. Used to construct the public signing key for the JWT's signature
e| string| true| false| The exponent for the RSA public key used to sign the matching JWT. Used to construct the public signing key for the JWT's signature
kid| string| true| false| Unique identifier for the key. Matches the `kid` property in the matching JWT's header

#### Allowed for

  * Anonymous


#### Code Samples

**curl**


    curl -v https://{subdomain}.zendesk.com/api/v2/help_center/integration/keys.json

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/integration/keys"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/integration/keys")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/help_center/integration/keys',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/integration/keys"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/integration/keys")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "keys": [    {      "e": "AQAB",      "kid": "deeee01d5023d9b44c5b5ab2583be9354620249652a48568ed2cb5bff8d86841",      "kty": "RSA",      "n": "yaiTIWA7vCbzoEEBAyV_dMd2Ao-IP8tSNSVxgZLyLiVorWtSdH7Vcp4qbTwiTWimDbjWZEZFUcbNDg_wLjv3efLcjE1eVrF_ewQOoR3C-dskNE_QyxC-aVvKDCGj-kMXnuHGvvZZmvt0CBeNZUSSbhGnqVta46O5hijoYCpNJOxwj8Ml84CnpBhgMllcyFUT7_Mx_I-w6_8CkSS-5XZMJXqaDZ3xljXMoIW5jTMfLU5_1X8sgv_Pn45yzACJHsyPIx0moEoL2lasI-jLPJt8G3aj8pcjwLTTa5cIT4s0tlZlMC2m4Kz0ictVqyMvCaJTxf6YIFa63KN7IiHJqu_ULmWxtIFb90X6hurNvyUqTfBbY-gKYX-i8TjG2x96Zec7-5PQ6OCzuz6fu7Xq56B_IVCkkQKTWAVHGapP1wZXWRLZB7AyZMhQ3ug5-ISIC4ySE8bIhuo82HDZy-m2dSnG4BU9sHFPlCRAyp5UzNDJofrc_aGW_3nRgPJ0eiC12ig_"    }  ]}

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)