# Apps

*Source: https://developer.zendesk.com/api-reference/ticketing/apps/apps/*

---

## On this page

  * [JSON format](/api-reference/ticketing/apps/apps/#json-format)
  * [List All Apps](/api-reference/ticketing/apps/apps/#list-all-apps)
  * [List Owned Apps](/api-reference/ticketing/apps/apps/#list-owned-apps)
  * [Get Information About App](/api-reference/ticketing/apps/apps/#get-information-about-app)
  * [Get App Public Key](/api-reference/ticketing/apps/apps/#get-app-public-key)
  * [Create App](/api-reference/ticketing/apps/apps/#create-app)
  * [Update App](/api-reference/ticketing/apps/apps/#update-app)
  * [Delete App](/api-reference/ticketing/apps/apps/#delete-app)
  * [Get job status](/api-reference/ticketing/apps/apps/#get-job-status)
  * [Upload App Package](/api-reference/ticketing/apps/apps/#upload-app-package)
  * [Send Notification to App](/api-reference/ticketing/apps/apps/#send-notification-to-app)
  * [Install App](/api-reference/ticketing/apps/apps/#install-app)
  * [List App Installations](/api-reference/ticketing/apps/apps/#list-app-installations)
  * [Show App Installation](/api-reference/ticketing/apps/apps/#show-app-installation)
  * [Update App Installation](/api-reference/ticketing/apps/apps/#update-app-installation)
  * [Remove App Installation](/api-reference/ticketing/apps/apps/#remove-app-installation)
  * [List Requirements](/api-reference/ticketing/apps/apps/#list-requirements)
  * [Get Requirements Install Status](/api-reference/ticketing/apps/apps/#get-requirements-install-status)


# Apps

## On this page

  * [JSON format](/api-reference/ticketing/apps/apps/#json-format)
  * [List All Apps](/api-reference/ticketing/apps/apps/#list-all-apps)
  * [List Owned Apps](/api-reference/ticketing/apps/apps/#list-owned-apps)
  * [Get Information About App](/api-reference/ticketing/apps/apps/#get-information-about-app)
  * [Get App Public Key](/api-reference/ticketing/apps/apps/#get-app-public-key)
  * [Create App](/api-reference/ticketing/apps/apps/#create-app)
  * [Update App](/api-reference/ticketing/apps/apps/#update-app)
  * [Delete App](/api-reference/ticketing/apps/apps/#delete-app)
  * [Get job status](/api-reference/ticketing/apps/apps/#get-job-status)
  * [Upload App Package](/api-reference/ticketing/apps/apps/#upload-app-package)
  * [Send Notification to App](/api-reference/ticketing/apps/apps/#send-notification-to-app)
  * [Install App](/api-reference/ticketing/apps/apps/#install-app)
  * [List App Installations](/api-reference/ticketing/apps/apps/#list-app-installations)
  * [Show App Installation](/api-reference/ticketing/apps/apps/#show-app-installation)
  * [Update App Installation](/api-reference/ticketing/apps/apps/#update-app-installation)
  * [Remove App Installation](/api-reference/ticketing/apps/apps/#remove-app-installation)
  * [List Requirements](/api-reference/ticketing/apps/apps/#list-requirements)
  * [Get Requirements Install Status](/api-reference/ticketing/apps/apps/#get-requirements-install-status)


This API lets you manage and interact with Zendesk apps. All actions from these endpoints are recorded in the Audit Log console of the affected Zendesk Support account.

To learn more about the process of creating and managing apps using the Apps REST API described on this page, see [Creating and managing private apps](/documentation/ticketing/using-the-zendesk-api/creating-and-managing-private-apps/)

### JSON format

Apps are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
app_organization| object| true| false| Organization that submitted the app to the Zendesk Marketplace
author_email| string| true| false| The app author's email
author_name| string| true| false| The app author's name
author_url| string| true| false| The app author's URL
categories| array| true| false| Zendesk Marketplace categories to which the app belongs
collections| array| true| false| Zendesk Marketplace collections to which the app belongs
created_at| string| true| false| When the app was created
date_published| string| true| false| When the app was published on the Zendesk Marketplace
default_locale| string| true| false| The default locale for translations for the app
deprecated| boolean| true| false| If true, the app is deprecated
feature_color| string| true| false| Hexadecimal color value used to feature the app on the Zendesk Marketplace
featured| boolean| true| false| Whether or not the app is featured in the Zendesk Marketplace
framework_version| string| true| false| The app framework version for which the app was written
google_analytics_code| string| true| false| Universal Google Analytics ("UA-") tracking id for the app's detail page on the Zendesk Marketplace
id| integer| true| false| The id of the app
installable| boolean| true| false| Whether or not the app can be installed
installation_count| integer| true| false| Current number of installations of the app
installation_instructions| string| true| false| Instructions for installing the app
large_icon| string| true| false| The large icon url for an app
locations| array| true| false| Location ids for the app. To map these ids to app locations, see the [App Locations](/api-reference/ticketing/apps/app_locations/) endpoint
long_description| string| true| false| The app's long description in the Zendesk Marketplace
marketing_only| boolean| true| false| If true, the app is an [integration app](/documentation/apps/publish-your-app-theme-or-bot/submit_your_app/#submitting-integration-apps)
name| string| true| false| The name of the app
obsolete| boolean| true| false| If true, the app is obsolete
owner_id| integer| true| false| The app developer id corresponding to the app
paid| boolean| true| false| If true, the app is a paid app
parameters| array| true| false| The parameters for the app
plans| array| true| false| Payment plans for the app
products| array| true| false| Zendesk products supported by the app
promoted| boolean| true| false| Whether or not the app is a promoted app in the Zendesk Marketplace
rating| object| true| false| The ratings of the app
raw_installation_instructions| string| true| false| The raw installation instructions
raw_long_description| string| true| false| The raw long description for the app in the Zendesk Marketplace
remote_installation_url| string| true| false| URL for the app's installation instructions
screenshots| array| true| false| Screenshots for the app when displayed in the Zendesk Marketplace
short_description| string| true| false| The short description of the app in the Zendesk Marketplace
single_install| boolean| true| false| Whether or not this app can only be installed once
small_icon| string| true| false| The url for the small logo for the app
state| string| true| false| Publication state for the app on the Zendesk Marketplace
stripe_publishable_key| string| true| false| Publishable key for the app developer's Stripe account
terms_conditions_url| string| true| false| URL for the app's terms and conditions
third_party_pricing| object| true| false| Third-party pricing information for the app
updated_at| string| true| false| When the app was last updated
version| string| true| false| The version of the app
visibility| string| true| false| The app is a private app, which is only visible to your account, or a public app. An example value is "private".

### List All Apps

  * `GET /api/v2/apps`


Lists all public apps on the Zendesk Marketplace. For authenticated agents and admins, the endpoint also lists their account's private apps.

#### Allowed For

  * Everyone


#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/apps.json \  -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/apps"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/apps")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/apps',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/apps"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/apps")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "apps": [    {      "app_organization": {        "country_code": "US",        "email": "[[email protected]](/cdn-cgi/l/email-protection)",        "id": 123,        "name": "Acme",        "stripe_account_id": null,        "website": "https://example.com"      },      "author_email": "[[email protected]](/cdn-cgi/l/email-protection)",      "author_name": "Zendesk User",      "author_url": "https://example.com",      "categories": [],      "collections": [],      "created_at": "2012-05-14T22:28:18Z",      "date_published": "2016-10-26T22:26:18Z",      "default_locale": "en",      "deprecated": false,      "feature_color": null,      "featured": false,      "framework_version": "2.0",      "google_analytics_code": null,      "id": 12345,      "installable": true,      "installation_count": 1234,      "installation_instructions": "",      "large_icon": "/api/v2/apps/12345/assets/logo.png",      "locations": [        7,        2,        1,        3,        4,        5,        6,        10,        8,        19,        17,        15,        18,        16,        25,        22,        23,        24      ],      "long_description": "",      "marketing_only": false,      "name": "Bookmarks",      "obsolete": false,      "owner_id": 1,      "paid": false,      "parameters": [        {          "app_id": 12345,          "created_at": "2012-06-14T17:31:08Z",          "default_value": null,          "id": 21,          "kind": "text",          "name": "name",          "position": 0,          "required": true,          "secure": true,          "updated_at": "2012-06-14T17:31:08Z"        }      ],      "plans": [        {          "active": true,          "amount": 0,          "app_id": 12345,          "cost_id": 1,          "cost_type": "CostFree",          "created_at": "2019-05-15T05:41:13.000Z",          "description": "<p>This is the default plan all existing apps have. You can change the description and name of this plan, or create new ones.</p>\\n",          "entity_id": 123456,          "id": 123,          "name": "Default Plan",          "plan_type": "one_off",          "service_identifier": null,          "stripe_account": null,          "stripe_plan_id": null,          "stripe_publishable_key": null,          "trial_days": 0,          "updated_at": "2019-05-15T05:41:13.000Z",          "vat_reversible": null        }      ],      "products": [        "support",        "chat",        "sell"      ],      "promoted": false,      "rating": {        "average": 3,        "count": {          "1": 2,          "2": 2,          "3": 2,          "4": 2,          "5": 2        },        "total_count": 10      },      "raw_installation_instructions": null,      "raw_long_description": null,      "remote_installation_url": null,      "screenshots": [],      "short_description": null,      "single_install": true,      "small_icon": "/api/v2/apps/12345/assets/logo-small.png",      "state": "published",      "stripe_publishable_key": null,      "terms_conditions_url": null,      "third_party_pricing": {        "has_third_party_pricing": false,        "third_party_pricing_url": null      },      "updated_at": "2014-01-21T00:32:03Z",      "version": "1.0",      "visibility": "private"    }  ]}

### List Owned Apps

  * `GET /api/v2/apps/owned`


Lists apps owned by the current account.

#### Allowed For

  * Admins


#### Sideloads

The `categories` and `parameters` objects are automatically side-loaded with each app object. However, you can exclude them from the response. Example:


    curl https://{subdomain}.zendesk.com/api/v2/apps/owned.json?exclude=parameters \ -u {email_address}/token:{api_token}

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/apps/owned.json \  -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/apps/owned"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/apps/owned")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/apps/owned',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/apps/owned"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/apps/owned")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "apps": [    {      "author_email": "[[email protected]](/cdn-cgi/l/email-protection)",      "author_name": "Zendesk User",      "author_url": "http://www.example.com",      "categories": [],      "closed_preview": false,      "created_at": "2012-05-14T22:28:18Z",      "default_locale": "en",      "deprecated": false,      "feature_color": null,      "featured": false,      "framework_version": "1.0",      "google_analytics_code": null,      "id": 12345,      "installable": true,      "installation_instructions": "",      "large_icon": "/api/v2/apps/12345/assets/logo.png",      "long_description": "",      "marketing_only": false,      "name": "Bookmarks",      "obsolete": false,      "owner_id": 1,      "paid": false,      "parameters": [        {          "app_id": 12345,          "created_at": "2012-06-14T17:31:08Z",          "default_value": null,          "id": 21,          "kind": "text",          "name": "name",          "position": 0,          "required": true,          "secure": true,          "updated_at": "2012-06-14T17:31:08Z"        }      ],      "products": [        "support",        "chat",        "sell"      ],      "promoted": false,      "raw_installation_instructions": null,      "raw_long_description": null,      "remote_installation_url": null,      "screenshots": [],      "short_description": null,      "single_install": true,      "small_icon": "/api/v2/apps/12345/assets/logo-small.png",      "state": "published",      "terms_conditions_url": null,      "updated_at": "2014-01-21T00:32:03Z",      "version": "1.0",      "visibility": "private"    }  ]}

### Get Information About App

  * `GET /api/v2/apps/{app_id}`


Retrieves information about the specified app accessible to the current user and account.

#### Allowed For

  * Everyone


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
app_id| integer| Path| true| The ID of the app to be retrieved

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/apps/{app_id}.json \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/apps/1"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/apps/1")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/apps/1',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/apps/1"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/apps/1")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "author_email": "[[email protected]](/cdn-cgi/l/email-protection)",  "author_name": "Zendesk User",  "author_url": "http://www.example.com",  "categories": [],  "closed_preview": false,  "created_at": "2012-05-14T22:28:18Z",  "default_locale": "en",  "deprecated": false,  "feature_color": null,  "featured": false,  "framework_version": "2.0",  "google_analytics_code": null,  "id": 12345,  "installable": true,  "installation_instructions": "",  "large_icon": "/api/v2/apps/12345/assets/logo.png",  "long_description": "",  "marketing_only": false,  "name": "Bookmarks",  "obsolete": false,  "owner_id": 1,  "paid": false,  "parameters": [    {      "app_id": 12345,      "created_at": "2012-06-14T17:31:08Z",      "default_value": null,      "id": 21,      "kind": "text",      "name": "name",      "position": 0,      "required": true,      "secure": true,      "updated_at": "2012-06-14T17:31:08Z"    }  ],  "products": [    "support",    "chat",    "sell"  ],  "promoted": false,  "raw_installation_instructions": null,  "raw_long_description": null,  "remote_installation_url": null,  "screenshots": [],  "short_description": null,  "single_install": true,  "small_icon": "/api/v2/apps/12345/assets/logo-small.png",  "state": "published",  "terms_conditions_url": null,  "updated_at": "2014-01-21T00:32:03Z",  "version": "1.0",  "visibility": "private"}

### Get App Public Key

  * `GET /api/v2/apps/{app_id}/public_key`


Reveals the app's public key in PEM format.

You can use it to verify that certain requests from the app are legitimate.

#### Allowed For

  * Anonymous users


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
app_id| integer| Path| true| The ID of the app

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/apps/{app_id}/public_key.pem

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/apps/1/public_key"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/apps/1/public_key")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/apps/1/public_key',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/apps/1/public_key"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/apps/1/public_key")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA6Z6U0KVY2HstBHKDiNIx\nFoxzkhhMjvyB3LiBWLqre+H1rHiqZl3Q3oQ1+61qNyBBulu+6hr1GkkIVVEHBnfe\n9OO+u2F9UAMi6JMl2L7QaaTxa+fR8ADNRNmg+5vsdKq/+nNTf2EA2ynwpwt/F5yp\nmKg6n8jhy0eqsea4qKpYLLEE6AguR04KXgQymb0Mg0PQsNowpFCoLTg3IXZGCIVE\nztOfgYaYPOVwGr3pN71L4cW5euyKPl36tpp42iHyuJ3mP3q2d7GPfLwUoLNsDZYQ\nZ8vcOkvkA7N0tZUDqIzofKGwsjk/++LYBFL04Qbj3avRHcouo70q13Lb+k4rm20u\nlwIDAQAB\n-----END PUBLIC KEY-----\n"

**404 Not Found**


    // Status 404 Not Found
    "Not Found"

### Create App

  * `POST /api/v2/apps`


Adds a build of a new app to the job queue.

You must provide an `upload_id` in the post payload to this endpoint in order to specify the uploaded app package to use for the build. See Upload App Package.

The response contains a `job_id` to check the status of the build. See Get Job Status.

#### Allowed For

  * Admins


#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/apps.json \  -d '{"name":"My App", "short_description":"My App description", "upload_id":"123"}' \  -H "Content-Type: application/json" -X POST \  -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/apps"	method := "POST"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/apps")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'POST',  url: 'https://support.zendesk.com/api/v2/apps',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/apps"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/apps")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "job_id": "fa8cac3098330130f49c14109fd02dfb"}

### Update App

  * `PUT /api/v2/apps/{app_id}`


Adds a build of an existing app to the job queue.

You must provide the id of the app you want to update. Use the [List Owned Apps](/api-reference/ticketing/apps/apps/#list-owned-apps) endpoint to get the id.

You must also provide an `upload_id` to specify the uploaded app package to use for the build. See Upload App Package.

The response contains a `job_id` to check the status of the build. See Get Job Status.

#### Allowed For

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
app_id| integer| Path| true| The ID of the app to be updated

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/apps/{app_id}.json \  -d '{"name":"My App", "short_description":"My App description", "upload_id":"123"}' \  -H "Content-Type: application/json" -X PUT \  -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/apps/1"	method := "PUT"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/apps/1")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'PUT',  url: 'https://support.zendesk.com/api/v2/apps/1',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/apps/1"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/apps/1")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "job_id": "fa8cac3098330130f49c14109fd02dfb"}

### Delete App

  * `DELETE /api/v2/apps/{app_id}`


Deletes the specified app and removes it from the My Apps page in Zendesk Support.

#### Allowed For

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
app_id| integer| Path| true| The ID of the app to be deleted

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/apps/{app_id}.json \  -u {email_address}/token:{api_token} -X DELETE

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/apps/1"	method := "DELETE"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/apps/1")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("DELETE", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'DELETE',  url: 'https://support.zendesk.com/api/v2/apps/1',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/apps/1"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"DELETE",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/apps/1")request = Net::HTTP::Delete.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**204 No Content**


    // Status 204 No Content
    null

### Get job status

  * `GET /api/v2/apps/job_statuses/{job_status_id}`


Gets the application build job status. You must provide the job id returned when the job was created.

When the job status is 'completed', the app has been built successfully. You can proceed to install the app using the app id in the response. See Install App.

If the status is 'failed', check the message for the reason.

If you're constantly getting the same error message and the error message isn't clear, try creating the app through the Zendesk Support user interface before contacting support. See [Uploading and installing your private app in Zendesk Support](/documentation/apps/getting-started/uploading-and-installing-a-private-app/#uploading-and-installing-a-private-app-in-zendesk).

For more information pertaining to Job Status objects, please see [Job Statuses](/api-reference/ticketing/ticket-management/job_statuses/).

#### Allowed For

  * Admins


#### JSON Format

App creation job statuses have the following attributes:

Name| Type| Read-only| Mandatory| Comment
---|---|---|---|---
id| string| yes| no| Automatically assigned when the job is queued
url| string| yes| no| The URL to poll for status updates
app_id| integer| yes| no| The ID of the app created by this job, if it exists
total| integer| yes| no| The total number of tasks this job is batching through
progress| integer| yes| no| Number of tasks completed
status| string| yes| no| One of "queued", "working", "failed", "completed", "killed"
message| string| yes| no| Message from the job worker, if any
retry_in| integer| yes| no| Number of seconds after which you may re-check status

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
job_status_id| string| Path| true| The ID of the job

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/apps/job_statuses/{job_status_id}.json \  -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/apps/job_statuses/fa8cac3098330130f49c14109fd02dfb"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/apps/job_statuses/fa8cac3098330130f49c14109fd02dfb")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/apps/job_statuses/fa8cac3098330130f49c14109fd02dfb',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/apps/job_statuses/fa8cac3098330130f49c14109fd02dfb"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/apps/job_statuses/fa8cac3098330130f49c14109fd02dfb")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "app_id": 123,  "app_url": "https://{subdomain}.zendesk.com/api/v2/apps/123.json",  "id": "fa8cac3098330130f49c14109fd02dfb",  "message": "Completed at 2013-05-06 15:02:40 +1000",  "progress": 126,  "retry_in": 3,  "status": "completed",  "total": 126,  "url": "https://{subdomain}.zendesk.com/api/v2/apps/job_statuses/fa8cac3098330130f49c14109fd02dfb.json"}

**404 Not Found**


    // Status 404 Not Found
    {  "id": "fa8cac3098330130f49c14109fd02dfb",  "message": "Cannot unzip the package",  "progress": null,  "retry_in": 3,  "status": "failed",  "total": null,  "url": "https://{subdomain}.zendesk.com/api/v2/apps/job_statuses/fa8cac3098330130f49c14109fd02dfb.json"}

### Upload App Package

  * `POST /api/v2/apps/uploads`


Uploads a new app package to Zendesk Support. See [Packaging and installing a private Zendesk app](/documentation/apps/app-developer-guide/zcli/#packaging-and-installing-a-private-zendesk-app).

Use the returned upload id to create or update the app in the Zendesk Support instance.

#### Allowed For

  * Admins


#### Example Response


    Status: 200
    {  "id": 123}

#### Code Samples

**curl**

If you run the curl command in the app root folder where you [packaged the app](/documentation/apps/app-developer-guide/zcli/#packaging-a-zendesk-app-for-manual-upload), the file path for the `uploaded_data` attribute should look as follows: `uploaded_data=@tmp/app-20170210150930.zip`.


    curl https://{subdomain}.zendesk.com/api/v2/apps/uploads.json \  -F uploaded_data=@/path/to/app_zip_file -X POST \  -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/apps/uploads"	method := "POST"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/apps/uploads")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'POST',  url: 'https://support.zendesk.com/api/v2/apps/uploads',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/apps/uploads"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/apps/uploads")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "id": 123}

### Send Notification to App

  * `POST /api/v2/apps/notify`


Sends messages to currently open instances of a Zendesk Apps framework (ZAF) app. The messages cause an event to fire in the app. For example, you could use this API in conjunction with a custom ZAF app to send critical product information to all signed-in agents. For information on how to set up custom event handlers, see [Notification events](/api-reference/apps/apps-support-api/all_locations/#notification-events) in the ZAF docs.

#### ZAT and ZCLI local servers

When developing Zendesk apps using the [ZAT local web server](/documentation/apps/zendesk-app-tools-zat/installing-and-using-zat/#testing-your-app-locally-in-a-browser), you can send messages to your unpublished app by setting the `app_id` parameter to `0`.

The [ZCLI local web server](/documentation/apps/app-developer-guide/zcli/#testing-your-zendesk-app-locally) can't receive messages from this endpoint. As a workaround, you can use ZCLI to install the app as a private app instead. See [Packaging and installing a private Zendesk app](/documentation/apps/app-developer-guide/zcli/#packaging-and-installing-a-private-zendesk-app).

#### Limitations

This API is rate limited. 100 requests per minute are allowed per account. For more information, see [Rate limits](/api-reference/introduction/rate-limits/).

The maximum payload for a Notify API request is 1MB (1024kB).

#### Allowed For

  * Agents


#### JSON format

Notifications sent to apps are represented as JSON objects with the following properties:

Name| Type| Mandatory| Comment
---|---|---|---
app_id| integer| yes| The id of the app you want to send the message to
event| string| yes| The name of the event you want to fire in your app
body| string| no| If it's valid JSON, it's passed to your app as a JavaScript object.
agent_id| integer| no| Send the notification to only one agent

For example, to send a user's updated phone number to agent #534 using the app with an id of 375, the request body might look something like this:


    {  "app_id": 375,  "event": "updateUsersPhoneNumber",  "body": "+61455534512",  "agent_id": 534}

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/apps/notify.json \  -d '{"event": "updateUsersPhoneNumber", "app_id": 375, "agent_id": 534, "body": "+61455534512"}' \  -H "Content-Type: application/json" -X POST \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/apps/notify"	method := "POST"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/apps/notify")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'POST',  url: 'https://support.zendesk.com/api/v2/apps/notify',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/apps/notify"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/apps/notify")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    null

**413 Request Entity Too Large**


    // Status 413 Request Entity Too Large
    "Payload too large"

### Install App

  * `POST /api/v2/apps/installations`


Installs an app in the account.

You must provide the `app_id` and a `settings` object containing properties for all required parameters for the app. You can use the List All Apps endpoint to get the id of the app you want to install.

#### Allowed For

  * Admins


#### JSON format

App installations are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
app_id| integer| false| true| id of the app
collapsible| boolean| true| false| If true, the app can be minimized in the Zendesk user interface (UI)
created_at| string| true| false| When the app installation was created
enabled| boolean| false| false| If true, the app installation is enabled
group_restrictions| array of strings| false| false| Group restrictions for the app installation
has_incomplete_subscription| boolean| true| false| If true, the app installation's Stripe payment subscription is incomplete
has_unpaid_subscription| boolean| true| false| If true, the app installation's Stripe payment subscription is unpaid
id| integer| true| false| id of the app installation
paid| boolean| true| false| If true, the app is a paid app
pending_installation| boolean| true| false| If true, the app installation is pending
pending_job_id| string| true| false| id for the app installation job. See app requirements
plan_information| object| true| false| Information about the Stripe payment plan for the app installation
product| string| true| false| Zendesk product the app is installed on
recurring_payment| boolean| false| false| If true, the app installation has a recurring Stripe payment subscription
redirect_path| boolean| true| false| URL path used to redirect admins after installing the app in the Zendesk UI
role_restrictions| array of strings| false| false| Role restrictions for the app installation
servable| boolean| true| false| If true, user making the API request can use the app installation
settings| object| false| true| Installation settings for the app, formatted as a flat object
settings_objects| array of objects| false| false| Installation settings for the app, formatted as an array of objects
stripe_account| string| true| false| App developer's Stripe account id
stripe_publishable_key| string| true| false| Publishable key for the app developer's Stripe account
stripe_subscription_id| string| true| false| Stripe subscription id for the app installation
updated| string| true| false| When the app was last updated
updated_at| string| true| false| When the app installation was last updated

#### Installation settings

All apps support the "name" installation setting. App developers can define other installation settings using the app's manifest file. For more information about defining installation settings, see [Defining installation settings](/documentation/apps/app-developer-guide/setup/#defining-installation-settings).

You specify installation setting values using the `settings` or `settings_objects` properties. `settings` formats the settings as a flat object. `settings_objects` formats the settings as an array of objects.

You must specify at least one installation setting value in `settings`. If you specify a setting value in both `settings` and `settings_objects`, only the value in `settings` is used.

#### App requirements

If the app has [requirements](/documentation/apps/app-developer-guide/apps_requirements/), the API response includes a job ID you can use to poll the installation status. See Get Requirements Install Status. Example:


    {  "id":     16,  "app_id": 82,  "settings": {    "title": "100 requirements API app"  },  "enabled":              false,  "updated":              "20141209034341",  "pending_installation": true,  "pending_job_id":       "648c47b0618d01326d443c15c2bba27e"}

#### Disabling apps on installation

By default, apps are enabled upon installation. To install an app and immediately disable it, pass `"enabled": false` in the install request.

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/apps/installations.json \  -d '{"app_id": "225", "settings": {"name": "Helpful App", "api_token": "53xjt93n6tn4321p", "use_ssl": true}}' \  -H "Content-Type: application/json" -X POST \  -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/apps/installations"	method := "POST"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/apps/installations")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'POST',  url: 'https://support.zendesk.com/api/v2/apps/installations',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/apps/installations"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/apps/installations")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "app_id": 218618,  "collapsible": true,  "created_at": "2020-06-11T06:12:48Z",  "enabled": true,  "group_restrictions": [],  "has_incomplete_subscription": false,  "has_unpaid_subscription": null,  "id": 361234573552,  "paid": null,  "pending_installation": true,  "pending_job_id": "587986abda901cde3873697585091dab",  "plan_information": {    "name": null  },  "product": "support",  "recurring_payment": false,  "redirect_path": "/support/apps/manage",  "role_restrictions": null,  "servable": true,  "settings": {    "allowlist": null,    "attachment_tag": "has_attachment",    "blocklist": null,    "items_per_page": "6",    "name": "Attachment Manager",    "new_attachment_tag": "has_new_attachment",    "title": "Attachment Manager"  },  "settings_objects": [    {      "name": "attachment_tag",      "value": "has_attachment"    },    {      "name": "blocklist",      "value": null    },    {      "name": "items_per_page",      "value": "6"    },    {      "name": "name",      "value": "Attachment Manager"    },    {      "name": "new_attachment_tag",      "value": "has_new_attachment"    },    {      "name": "title",      "value": "Attachment Manager"    },    {      "name": "allowlist",      "value": null    }  ],  "stripe_account": "acct_1CyabcGO5FKrIYc5",  "stripe_publishable_key": "pk_live_zMw5abcdYBbd6axDbyrzrRl9",  "stripe_subscription_id": null,  "updated": "20200305221223",  "updated_at": "2020-06-11T06:12:48Z"}

### List App Installations

  * `GET /api/v2/apps/installations`


Lists all app installations in the account. In the response, the `enabled` property indicates whether or not the installed app is active in the product.

#### Allowed For

  * Agents


#### Sideloads

You can pass `include=app` as a parameter to side-load the app object associated with each installation.


    curl https://{subdomain}.zendesk.com/api/v2/apps/installations.json?include=app \  -u {email_address}/token:{api_token}

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/apps/installations.json \  -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/apps/installations"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/apps/installations")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/apps/installations',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/apps/installations"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/apps/installations")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "installations": [    {      "app_id": 218618,      "collapsible": true,      "created_at": "2020-06-11T06:12:48Z",      "enabled": true,      "group_restrictions": [],      "has_incomplete_subscription": false,      "has_unpaid_subscription": null,      "id": 361234573552,      "paid": null,      "pending_installation": true,      "pending_job_id": "587986abda901cde3873697585091dab",      "plan_information": {        "name": null      },      "product": "support",      "recurring_payment": false,      "redirect_path": "/support/apps/manage",      "role_restrictions": null,      "servable": true,      "settings": {        "allowlist": null,        "attachment_tag": "has_attachment",        "blocklist": null,        "items_per_page": "6",        "name": "Attachment Manager",        "new_attachment_tag": "has_new_attachment",        "title": "Attachment Manager"      },      "settings_objects": [        {          "name": "attachment_tag",          "value": "has_attachment"        },        {          "name": "blocklist",          "value": null        },        {          "name": "items_per_page",          "value": "6"        },        {          "name": "name",          "value": "Attachment Manager"        },        {          "name": "new_attachment_tag",          "value": "has_new_attachment"        },        {          "name": "title",          "value": "Attachment Manager"        },        {          "name": "allowlist",          "value": null        }      ],      "stripe_account": "acct_1CyabcGO5FKrIYc5",      "stripe_publishable_key": "pk_live_zMw5abcdYBbd6axDbyrzrRl9",      "stripe_subscription_id": null,      "updated": "20200305221223",      "updated_at": "2020-06-11T06:12:48Z"    }  ]}

### Show App Installation

  * `GET /api/v2/apps/installations/{app_installation_id}`


Retrieves information about the specified app installation, including the installation settings.

The value of the `servable` property depends on the user making the API request. The value is true for installations that you can use.

#### Allowed For

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
app_installation_id| integer| Path| true| The ID of the app installation

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/apps/installations/{app_installation_id}.json \  -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/apps/installations/1"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/apps/installations/1")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/apps/installations/1',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/apps/installations/1"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/apps/installations/1")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "app_id": 218618,  "collapsible": true,  "created_at": "2020-06-11T06:12:48Z",  "enabled": true,  "group_restrictions": [],  "has_incomplete_subscription": false,  "has_unpaid_subscription": null,  "id": 361234573552,  "paid": null,  "pending_installation": true,  "pending_job_id": "587986abda901cde3873697585091dab",  "plan_information": {    "name": null  },  "product": "support",  "recurring_payment": false,  "redirect_path": "/support/apps/manage",  "role_restrictions": null,  "servable": true,  "settings": {    "allowlist": null,    "attachment_tag": "has_attachment",    "blocklist": null,    "items_per_page": "6",    "name": "Attachment Manager",    "new_attachment_tag": "has_new_attachment",    "title": "Attachment Manager"  },  "settings_objects": [    {      "name": "attachment_tag",      "value": "has_attachment"    },    {      "name": "blocklist",      "value": null    },    {      "name": "items_per_page",      "value": "6"    },    {      "name": "name",      "value": "Attachment Manager"    },    {      "name": "new_attachment_tag",      "value": "has_new_attachment"    },    {      "name": "title",      "value": "Attachment Manager"    },    {      "name": "allowlist",      "value": null    }  ],  "stripe_account": "acct_1CyabcGO5FKrIYc5",  "stripe_publishable_key": "pk_live_zMw5abcdYBbd6axDbyrzrRl9",  "stripe_subscription_id": null,  "updated": "20200305221223",  "updated_at": "2020-06-11T06:12:48Z"}

### Update App Installation

  * `PUT /api/v2/apps/installations/{app_installation_id}`


Updates the specified installation. Use the List App Installations endpoint to get the installation id.

#### Allowed For

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
app_installation_id| integer| Path| true| The ID of the app installation

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/apps/installations/{app_installation_id}.json \  -d '{"settings": {"name": "Helpful App - Updated", "api_token": "659323ngt4ut9an"}}' \  -H "Content-Type: application/json" -X PUT \  -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/apps/installations/1"	method := "PUT"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/apps/installations/1")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'PUT',  url: 'https://support.zendesk.com/api/v2/apps/installations/1',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/apps/installations/1"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/apps/installations/1")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "app_id": 218618,  "collapsible": true,  "created_at": "2020-06-11T06:12:48Z",  "enabled": true,  "group_restrictions": [],  "has_incomplete_subscription": false,  "has_unpaid_subscription": null,  "id": 361234573552,  "paid": null,  "pending_installation": true,  "pending_job_id": "587986abda901cde3873697585091dab",  "plan_information": {    "name": null  },  "product": "support",  "recurring_payment": false,  "redirect_path": "/support/apps/manage",  "role_restrictions": null,  "servable": true,  "settings": {    "allowlist": null,    "attachment_tag": "has_attachment",    "blocklist": null,    "items_per_page": "6",    "name": "Attachment Manager",    "new_attachment_tag": "has_new_attachment",    "title": "Attachment Manager"  },  "settings_objects": [    {      "name": "attachment_tag",      "value": "has_attachment"    },    {      "name": "blocklist",      "value": null    },    {      "name": "items_per_page",      "value": "6"    },    {      "name": "name",      "value": "Attachment Manager"    },    {      "name": "new_attachment_tag",      "value": "has_new_attachment"    },    {      "name": "title",      "value": "Attachment Manager"    },    {      "name": "allowlist",      "value": null    }  ],  "stripe_account": "acct_1CyabcGO5FKrIYc5",  "stripe_publishable_key": "pk_live_zMw5abcdYBbd6axDbyrzrRl9",  "stripe_subscription_id": null,  "updated": "20200305221223",  "updated_at": "2020-06-11T06:12:48Z"}

### Remove App Installation

  * `DELETE /api/v2/apps/installations/{app_installation_id}`


Removes an installed app. Use the List App Installations endpoint to get the installation id.

#### Allowed For

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
app_installation_id| integer| Path| true| The ID of the app installation

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/apps/installations/{app_installation_id}.json \  -u {email_address}/token:{api_token} -X DELETE

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/apps/installations/1"	method := "DELETE"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/apps/installations/1")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("DELETE", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'DELETE',  url: 'https://support.zendesk.com/api/v2/apps/installations/1',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/apps/installations/1"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"DELETE",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/apps/installations/1")request = Net::HTTP::Delete.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**204 No Content**


    // Status 204 No Content
    null

### List Requirements

  * `GET /api/v2/apps/installations/{app_installation_id}/requirements`


Lists all [app requirements](/documentation/apps/app-developer-guide/apps_requirements/) for an installation.

#### Allowed For

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
app_installation_id| integer| Path| true| The ID of the app installation

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/apps/installations/{id}/requirements.json \  -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/apps/installations/1/requirements"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/apps/installations/1/requirements")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/apps/installations/1/requirements',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/apps/installations/1/requirements"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/apps/installations/1/requirements")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "requirements": [    {      "account_id": 2,      "created_at": "2014-03-26T00:57:43Z",      "identifier": "a_basecamp_target",      "requirement_id": 302,      "requirement_type": "targets",      "updated_at": "2014-03-26T00:57:43Z"    },    {      "account_id": 2,      "created_at": "2014-03-26T00:57:43Z",      "identifier": "an_email_target",      "requirement_id": 307,      "requirement_type": "targets",      "updated_at": "2014-03-26T00:57:43Z"    },    {      "account_id": 2,      "created_at": "2014-03-26T00:57:43Z",      "identifier": "sample_ticket_field",      "requirement_id": 137,      "requirement_type": "ticket_fields",      "updated_at": "2014-03-26T00:57:43Z"    }  ]}

### Get Requirements Install Status

  * `GET /api/v2/apps/installations/job_statuses/{job_id}`


If a job has kicked off to install an app and the app has [requirements](/documentation/apps/app-developer-guide/apps_requirements/), this endpoint returns the status of the requirements installation. The job id is supplied in the response to the app installation request.

If the `status` is "completed", the installation has been created successfully with its requirements, and is available for use.

If the `status` is "failed" check the message for the reason.

If you're constantly getting the same error message and the error message isn't clear, try installing the app with the Zendesk Support user interface before contacting [Zendesk Customer Support](https://support.zendesk.com/hc/en-us/articles/360026614173). See [Uploading and installing your private app in Zendesk Support](/documentation/apps/getting-started/uploading-and-installing-a-private-app/#uploading-and-installing-a-private-app-in-zendesk).

#### Allowed For

  * Admins


#### JSON Format

Installation job statuses are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Comment
---|---|---|---|---
id| string| yes| no| Automatically assigned when job is queued
url| string| yes| no| The URL to poll for status updates
total| integer| yes| no| The total number of tasks this job is batching through
progress| integer| yes| no| Number of completed tasks
status| string| yes| no| "queued", "working", "failed", "completed", "killed"
message| string| yes| no| Message from the job worker, if any
installation_id| integer| yes| no| Unique ID of the installation

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
job_id| string| Path| true| The ID of the job

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/apps/installations/job_statuses/{job_id}.json \  -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/apps/installations/job_statuses/fa8cac3098330130f49c14109fd02dfb"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/apps/installations/job_statuses/fa8cac3098330130f49c14109fd02dfb")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/apps/installations/job_statuses/fa8cac3098330130f49c14109fd02dfb',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/apps/installations/job_statuses/fa8cac3098330130f49c14109fd02dfb"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/apps/installations/job_statuses/fa8cac3098330130f49c14109fd02dfb")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "id": "fa8cac3098330130f49c14109fd02dfb",  "installation_id": 16,  "message": "Completed at 2013-05-06 15:02:40 +1000",  "progress": 100,  "status": "completed",  "total": 100,  "url": "https://{subdomain}.zendesk.com/api/v2/apps/installations/job_statuses/fa8cac3098330130f49c14109fd02dfb.json"}

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)