# Push Notification Devices

*Source: https://developer.zendesk.com/api-reference/ticketing/account-configuration/push_notification_devices/*

---

## On this page

  * [Bulk Unregister Push Notification Devices](/api-reference/ticketing/account-configuration/push_notification_devices/#bulk-unregister-push-notification-devices)


# Push Notification Devices

## On this page

  * [Bulk Unregister Push Notification Devices](/api-reference/ticketing/account-configuration/push_notification_devices/#bulk-unregister-push-notification-devices)


A push notification device is a mobile device identifier used by the Zendesk Support SDK to send push notifications.

### Bulk Unregister Push Notification Devices

  * `POST /api/v2/push_notification_devices/destroy_many`


Unregisters the mobile devices that are receiving push notifications. Specify the devices as an array of mobile device tokens.

#### Allowed for

  * Admins


#### Example body


    {  "push_notification_devices": [    "token1",    "token2"  ]}

#### Code Samples

**cURL**


    curl -X "POST" "https://{subdomain}.zendesk.com/api/v2/push_notification_devices/destroy_many" \  -u {email_address}/token:{api_token} \  -H "Content-Type: application/json" \  -H "Accept: application/json" \  -d '{ "push_notification_devices": ["token1", "token2"] }'

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://example.zendesk.com/api/v2/push_notification_devices/destroy_many"	method := "POST"	payload := strings.NewReader(`{  "push_notification_devices": [    "token1",    "token2"  ]}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/push_notification_devices/destroy_many")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"push_notification_devices\": [    \"token1\",    \"token2\"  ]}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "push_notification_devices": [    "token1",    "token2"  ]});
    var config = {  method: 'POST',  url: 'https://example.zendesk.com/api/v2/push_notification_devices/destroy_many',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/push_notification_devices/destroy_many"
    payload = json.loads("""{  "push_notification_devices": [    "token1",    "token2"  ]}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/push_notification_devices/destroy_many")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")request.body = %q({  "push_notification_devices": [    "token1",    "token2"  ]})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    null

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)