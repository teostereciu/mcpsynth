# Ticket Metric Events

*Source: https://developer.zendesk.com/api-reference/ticketing/tickets/ticket_metric_events/*

---

## On this page

  * [JSON format](/api-reference/ticketing/tickets/ticket_metric_events/#json-format)
  * [List Ticket Metric Events](/api-reference/ticketing/tickets/ticket_metric_events/#list-ticket-metric-events)


# Ticket Metric Events

## On this page

  * [JSON format](/api-reference/ticketing/tickets/ticket_metric_events/#json-format)
  * [List Ticket Metric Events](/api-reference/ticketing/tickets/ticket_metric_events/#list-ticket-metric-events)


You can use the ticket metric events API to track reply times, agent work times, and requester wait times.

For example, if you want to measure reply times, you can get the time a ticket was created and the time an agent first replied to it. If you want to measure requester wait times, you can get the time the ticket was created and the time its status was changed to solved.

The times are reported as _metric events_ , or events that are related to each of the three metrics: reply time, agent work time, and requester wait time. You can access the following six types of metric events, with different events for each type depending on the metric:

  * **activate events** , such as when a ticket is created in the case of all three metrics
  * **fulfill events** , such as when an agent first replies to a ticket for the "reply_time" metric, or when a ticket is solved for the "resolution_time" metric. A solved status change also fulfills the "requester_wait_time" metric
  * **pause events** , such as when a ticket status is changed to pending or on-hold in the case of the agent work time metric
  * **apply_sla events** , such as when a SLA policy is applied to a ticket or when an SLA policy or target is changed on a ticket
  * **apply_group_sla events** , such as when a Group SLA policy is applied to a ticket or when an Group SLA policy or target is changed on a ticket
  * **breach events** , such as when a SLA target is breached
  * **update_status events** , such as when a metric is fulfilled


For details on each type, see [Ticket metric event types reference](/documentation/ticketing/reference-guides/ticket-metric-event-types-reference).

### JSON format

Ticket Metric Events are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
deleted| boolean| true| false| If true, the event has been deleted
id| integer| true| false| Automatically assigned when the record is created
instance_id| integer| true| false| The instance of the metric associated with the event. See instance_id
metric| string| true| false| The metric being tracked. Allowed values are "agent_work_time", "pausable_update_time", "periodic_update_time", "reply_time", "requester_wait_time", "resolution_time", or "group_ownership_time".
ticket_id| integer| true| false| Id of the associated ticket
time| string| true| false| The time the event occurred
type| string| true| false| The type of the metric event. See [Ticket metric event types reference](/documentation/ticketing/reference-guides/ticket-metric-event-types-reference). Allowed values are "activate", "pause", "fulfill", "apply_sla", "apply_group_sla", "breach", "update_status", or "measure".

In addition to the general properties above, additional properties may be available depending on the event `type`:

Name| Type| Read-only| Mandatory| Comment
---|---|---|---|---
sla| object| yes| no| Available if `type` is "apply_sla". The SLA policy and target being enforced on the ticket and metric in question, if any. See sla
group_sla| object| yes| no| Available if `type` is "apply_group_sla". The Group SLA policy and target being enforced on the ticket and metric in question, if any. See group_sla
status| object| yes| no| Available if `type` is "update_status". Minutes since the metric has been open. See status

#### instance_id

Use the `instance_id` property to track each instance of a metric event that can occur more than once per ticket, such as the `reply_time` event. The value increments over the lifetime of the ticket.

#### sla

The optional `sla` property provides key information about the SLA policy and target being enforced on the ticket and metric in question. The target time is provided in minutes, along with whether the target is being measured in business or calendar hours. Policy information is also provided, including the ID, title, and description of the policy currently applied to the ticket.

#### group_sla

The optional `group_sla` property provides key information about the Group SLA policy and target being enforced on the ticket and metric in question. The target time is provided in minutes, along with whether the target is being measured in business or calendar hours. Policy information is also provided, including the id, title, and description of the policy currently applied to the ticket.

#### status

The optional `status` property provides the number of minutes in both business and calendar hours for which the metric has been open. The `status` property is only updated for a `fulfill` event. Any ticket metric that hasn't breached yet or fulfilled at least once won't have a calculated status.

#### deleted

The `deleted` property is used to indicate whether or not an event should be ignored. In general, you can ignore any event where `deleted` is true.

#### Example


    {  "id": 926256957613,  "instance_id": 1,  "metric": "agent_work_time",  "ticket_id": 155,  "time": "2020-10-26T12:53:12Z",  "type": "measure"}

### List Ticket Metric Events

  * `GET /api/v2/incremental/ticket_metric_events?start_time={start_time}`


Returns ticket metric events that occurred on or after the start time.

Cursor pagination returns a maximum of 100 records per page. Events are listed in chronological order.

If the results are not paginated, events will be returned as a time-based incremental export.

See [Time-based incremental exports](/documentation/ticketing/managing-tickets/using-the-incremental-export-api#time-based-incremental-exports).

#### Pagination

  * Cursor pagination


See [Pagination](/api-reference/introduction/pagination/).

#### Allowed For

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
exclude_deleted| boolean| Query| false| When true, excludes ticket metric events for deleted tickets. Use this to avoid receiving events for tickets that are deleted.
include_changes| boolean| Query| false| This optional parameter enhances incremental data retrieval, delivering a consistent and accurate representation of data changes.
start_time| integer| Query| true| The Unix UTC epoch time of the oldest event you're interested in. Example: 1332034771.

#### Code Samples

**cURL**


    curl https://{subdomain}.zendesk.com/api/v2/incremental/ticket_metric_events?start_time=1432155323 \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/incremental/ticket_metric_events?exclude_deleted=&include_changes=&start_time=1332034771"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/incremental/ticket_metric_events")		.newBuilder()		.addQueryParameter("exclude_deleted", "")		.addQueryParameter("include_changes", "")		.addQueryParameter("start_time", "1332034771");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/incremental/ticket_metric_events',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'exclude_deleted': '',    'include_changes': '',    'start_time': '1332034771',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/incremental/ticket_metric_events?exclude_deleted=&include_changes=&start_time=1332034771"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/incremental/ticket_metric_events")uri.query = URI.encode_www_form("exclude_deleted": "", "include_changes": "", "start_time": "1332034771")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "count": 3,  "end_time": 1603716792,  "next_page": "https://company.zendesk.com/api/v2/incremental/ticket_metric_events?start_time=1603716792",  "ticket_metric_events": [    {      "id": 926232157301,      "instance_id": 0,      "metric": "agent_work_time",      "ticket_id": 155,      "time": "2020-10-26T12:53:12Z",      "type": "measure"    },    {      "id": 926232757371,      "instance_id": 1,      "metric": "agent_work_time",      "ticket_id": 155,      "time": "2020-10-26T12:53:12Z",      "type": "activate"    },    {      "id": 926232927415,      "instance_id": 0,      "metric": "pausable_update_time",      "ticket_id": 155,      "time": "2020-10-26T12:53:12Z",      "type": "measure"    }  ]}

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)