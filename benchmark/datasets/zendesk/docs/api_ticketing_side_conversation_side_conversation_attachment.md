# Side Conversation Attachment

*Source: https://developer.zendesk.com/api-reference/ticketing/side_conversation/side_conversation_attachment/*

---

## On this page

  * [JSON format](/api-reference/ticketing/side_conversation/side_conversation_attachment/#json-format)
  * [Create Side Conversation Attachments](/api-reference/ticketing/side_conversation/side_conversation_attachment/#create-side-conversation-attachments)


# Side Conversation Attachment

## On this page

  * [JSON format](/api-reference/ticketing/side_conversation/side_conversation_attachment/#json-format)
  * [Create Side Conversation Attachments](/api-reference/ticketing/side_conversation/side_conversation_attachment/#create-side-conversation-attachments)


File attachments can be included on a [side conversation](/api-reference/ticketing/side_conversation/side_conversation/).

### JSON format

Side Conversation Attachments are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
content_type| string| true| false| The content type of the attachment
height| integer| true| false| The height of the attachment image
id| string| true| false| The id of the side conversation attachment
name| string| false| false| The name of the attachment
size| integer| true| false| The size of the attachment
width| integer| true| false| The width of the attachment image

#### Example


    {  "content_type": "image/png",  "height": 214,  "id": "s3-d2a3111e-26d9-4e1c-88b4-cf7c0649d81d",  "name": "image.png",  "size": 50645,  "width": 406}

### Create Side Conversation Attachments

  * `POST /api/v2/tickets/side_conversations/attachments`


Creates a new side conversation attachment.

#### Allowed For

  * Agents


#### Request Body

Takes a file object as multipart/form-data for the uploaded attachment.

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/tickets/side_conversations/attachments.json \  -F '[[email protected]](/cdn-cgi/l/email-protection)' \  -H "Content-Type: multipart/form-data" -v -u {email_address}/token:{api_token} -X POST

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/api/v2/tickets/side_conversations/attachments"	method := "POST"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/api/v2/tickets/side_conversations/attachments")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'POST',  url: 'https://support.zendesk.com/api/v2/tickets/side_conversations/attachments',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/api/v2/tickets/side_conversations/attachments"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/api/v2/tickets/side_conversations/attachments")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**201 Created**


    // Status 201 Created
    {  "content_type": "image/png",  "height": 214,  "id": "s3-d2a3111e-26d9-4e1c-88b4-cf7c0649d81d",  "name": "image.png",  "size": 50645,  "width": 406}

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)