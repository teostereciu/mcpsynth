# User Subscriptions

*Source: https://developer.zendesk.com/api-reference/help_center/help-center-api/user_subscriptions/*

---

## On this page

  * [JSON format](/api-reference/help_center/help-center-api/user_subscriptions/#json-format)
  * [List User Subscriptions By User](/api-reference/help_center/help-center-api/user_subscriptions/#list-user-subscriptions-by-user)


# User Subscriptions

## On this page

  * [JSON format](/api-reference/help_center/help-center-api/user_subscriptions/#json-format)
  * [List User Subscriptions By User](/api-reference/help_center/help-center-api/user_subscriptions/#list-user-subscriptions-by-user)


Users can subscribe to other users. The subscriber is notified when the other user adds an article to a section, adds a comment to an article or a post, or adds a post to a topic.

### JSON format

User Subscriptions are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
followed_id| integer| true| true| The id of the user being followed
follower_id| integer| true| true| The id of the user doing the following
id| integer| true| true| Automatically assigned when the subscription is created

#### Example


    {  "followed_id": 65466,  "follower_id": 98354,  "id": 1635}

### List User Subscriptions By User

  * `GET /api/v2/help_center/users/{user_id}/user_subscriptions`


Lists the user subscriptions of a given user. To list your own subscriptions, specify `me` as the user id.

#### Allowed for

  * End users


#### Pagination

  * Cursor pagination (recommended)
  * Offset pagination


See [Pagination](/api-reference/introduction/pagination/).

#### Sideloads

The following sideloads are supported:

Name| Will sideload| For
---|---|---
users| users| all

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
type| string| Query| false| Selects whether to find who the given user is following ("followings") or who is following the given user ("followers"). The default is "followers". Allowed values are "followings", or "followers".
user_id| integer| Path| true| The unique ID of the user

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/help_center/users/{user_id}/user_subscriptions.json \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/help_center/users/1234/user_subscriptions?type="	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/help_center/users/1234/user_subscriptions")		.newBuilder()		.addQueryParameter("type", "");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/api/v2/help_center/users/1234/user_subscriptions',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'type': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/help_center/users/1234/user_subscriptions?type="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/help_center/users/1234/user_subscriptions")uri.query = URI.encode_www_form("type": "")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "user_subscriptions": [    {      "followed_id": 8748733,      "follower_id": 398452,      "id": 35467    }  ]}

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)