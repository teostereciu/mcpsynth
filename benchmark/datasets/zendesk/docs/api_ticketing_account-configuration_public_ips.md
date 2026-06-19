# Zendesk Public IPs

*Source: https://developer.zendesk.com/api-reference/ticketing/account-configuration/public_ips/*

---

## On this page

  * [JSON format](/api-reference/ticketing/account-configuration/public_ips/#json-format)
  * [List Zendesk Public IPs](/api-reference/ticketing/account-configuration/public_ips/#list-zendesk-public-ips)


# Zendesk Public IPs

## On this page

  * [JSON format](/api-reference/ticketing/account-configuration/public_ips/#json-format)
  * [List Zendesk Public IPs](/api-reference/ticketing/account-configuration/public_ips/#list-zendesk-public-ips)


This API retrieves a list of Zendeskâs main public IP ingress and egress addresses. For additional configuration for specific products, see [Configuring your firewall for use with Zendesk](https://support.zendesk.com/hc/en-us/articles/203660846-Configuring-your-firewall-for-use-with-Zendesk) in Help Center.

### JSON format

Public IPs are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
egress| object| true| false| The list of IPs Zendesk will connect to your systems. See IP List Object
ingress| object| true| false| The list of IPs you use to connect to Zendesk. See IP List Object

#### IP List Object

Name| Type| Description
---|---|---
all| array| The full list of IPs
specific| array| The specific list of IPs

A temporary key (`specific`) is also available in case your firewall can't configure all the IPs. If you use it, make sure your script expects that `specific` might disappear and reads from `all` in that case.

You can set up an alert or integration using this endpoint.

#### Example


    {  "egress": {    "all": [      "102.16.12.41/32",      "102.16.90.41/32"    ],    "specific": [      "102.16.12.41/32",      "102.16.90.41/32"    ]  },  "ingress": {    "all": [      "102.16.41.41/32",      "102.16.54.41/32",      "102.16.28.41/32"    ],    "specific": [      "104.16.41.41/32",      "104.16.54.41/32",      "104.16.28.41/32",      "104.16.12.41/32",      "104.16.90.41/32"    ]  }}

### List Zendesk Public IPs

  * `GET /ips`


Retrieves a list of Zendeskâs main public IP ingress and egress addresses.

As a best practice, set up a scheduled request (such as daily) to alert if the list changes, or to configure your firewall. This also helps Zendesk identify the customers that use this feature. Zendesk can reach out if it needs to execute emergency IP changes.

#### Allowed For

  * Anonymous


#### Code Samples

**cURL**


    curl https://{subdomain}.zendesk.com/ips

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/ips"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/ips")		.newBuilder();
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://support.zendesk.com/ips',  headers: {	'Content-Type': 'application/json',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requests
    url = "https://support.zendesk.com/ips"headers = {	"Content-Type": "application/json",}
    response = requests.request(	"GET",	url,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"uri = URI("https://support.zendesk.com/ips")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "ips": {    "egress": {      "all": [        "102.16.12.41/32",        "102.16.90.41/32"      ],      "specific": [        "102.16.12.41/32",        "102.16.90.41/32"      ]    },    "ingress": {      "all": [        "102.16.41.41/32",        "102.16.54.41/32",        "102.16.28.41/32"      ],      "specific": [        "104.16.41.41/32",        "104.16.54.41/32",        "104.16.28.41/32",        "104.16.12.41/32",        "104.16.90.41/32"      ]    }  }}

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)