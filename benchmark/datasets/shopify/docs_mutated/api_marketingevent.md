# MarketingEvent

*Source: https://shopify.dev/docs/api/admin-rest/2026-01/resources/marketingevent*

---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04

2026-01latest

# MarketingEvent

Ask assistant

Multiple access scopes needed — refer to each endpoint for access scope requirements.

**Multiple access scopes needed — refer to each endpoint for access scope requirements.:**

Marketing events represent actions taken by your app, on behalf of the merchant, to market products, collections, discounts, pages, blog posts, and other features. These actions target multiple potential customers, rather than specific individuals. For example, you should model your marketing event at the email campaign level, rather than on a per-email basis.

Merchants get value from marketing events because they help them understand sales and traffic attribution. Implementing marketing events for your app is beneficial because it enables Shopify to surface your app in the Shopify admin in ways that are helpful to merchants. Examples of marketing events include an ad campaign that drives multiple potential customers to a product page, or an email marketing campaign advertising a discount code.

**Marketing events** can be created for email campaigns, affiliate links, advertisements, and other common marketing tactics. Marketing events include the `event_type` and `marketing_channel` properties that help Shopify to rank your app and surface it in the Shopify admin in ways that are useful to merchants. Traffic and order attribution for your app is handled by providing UTM parameters with your marketing events. The same UTM parameters are also used in the links provided in the marketing event.

**Engagements** can also be added to marketing events to give merchants more insight into how potential customers interact with your marketing events. For example, engagements for ad campaigns can include clicks, shares, and comments. Creating engagements is optional, and not all marketing events include engagements.

Was this section helpful?

YesNo

#

## Endpoints

  * [post/admin/api/latest/marketing_events.json](/docs/api/admin-rest/latest/resources/marketingevent#post-marketing-events)

Creates a marketing event

[marketingActivityCreateExternal](/docs/api/admin-graphql/latest/mutations/marketingActivityCreateExternal?example=creates-a-marketing-event)

  * [post/admin/api/latest/marketing_events/{marketing_event_id}/engagements.json](/docs/api/admin-rest/latest/resources/marketingevent#post-marketing-events-marketing-event-id-engagements)

Creates marketing engagements on a marketing event

[marketingEngagementCreate](/docs/api/admin-graphql/latest/mutations/marketingEngagementCreate?example=creates-marketing-engagements-on-a-marketing-event)

  * [get/admin/api/latest/marketing_events.json](/docs/api/admin-rest/latest/resources/marketingevent#get-marketing-events)

Retrieves a list of all marketing events

[marketingEvents](/docs/api/admin-graphql/latest/queries/marketingEvents?example=retrieves-a-list-of-all-marketing-events)

  * [get/admin/api/latest/marketing_events/{marketing_event_id}.json](/docs/api/admin-rest/latest/resources/marketingevent#get-marketing-events-marketing-event-id)

Retrieves a single marketing event

[marketingEvent](/docs/api/admin-graphql/latest/queries/marketingEvent?example=retrieves-a-single-marketing-event)

  * [get/admin/api/latest/marketing_events/count.json](/docs/api/admin-rest/latest/resources/marketingevent#get-marketing-events-count)

Retrieves a count of all marketing events

deprecated

**

deprecated

**

  * [ put/admin/api/latest/marketing_events/{marketing_event_id}.json](/docs/api/admin-rest/latest/resources/marketingevent#put-marketing-events-marketing-event-id)

Updates a marketing event

[marketingActivityUpdateExternal](/docs/api/admin-graphql/latest/mutations/marketingActivityUpdateExternal?example=updates-a-marketing-event)

  * [del/admin/api/latest/marketing_events/{marketing_event_id}.json](/docs/api/admin-rest/latest/resources/marketingevent#delete-marketing-events-marketing-event-id)

Deletes a marketing event

[marketingActivityDeleteExternal](/docs/api/admin-graphql/latest/mutations/marketingActivityDeleteExternal?example=deletes-a-marketing-event)


* * *

[Anchor to ](/docs/api/admin-rest/latest/resources/marketingevent#resource-object)

## The MarketingEvent resource

[Anchor to ](/docs/api/admin-rest/latest/resources/marketingevent#resource-object-properties)

### Properties

* * *

remote_id

->[remoteId](/docs/api/admin-graphql/latest/objects/MarketingEvent#field-MarketingEvent.fields.remoteId)

An optional remote identifier for a marketing event. The remote identifier lets Shopify validate engagement data.

* * *

event_type

->[type](/docs/api/admin-graphql/latest/objects/MarketingEvent#field-MarketingEvent.fields.type)

The type of marketing event. Valid values: `ad`, `post`, `message`, `retargeting`, `transactional`, `affiliate`, `loyalty`, `newsletter`, `abandoned_cart`.

Note

If there are values that you’d like to use for event_type that are not in the list above, then please share your request in the [Shopify Community APIs and SDKs discussion board](https://community.shopify.com/c/shopify-apis-and-sdks/bd-p/shopify-apis-and-technology) providing as much detail as possible. Our approach is to be more structured than using freeform text, but to still allow for categorization of most types of marketing actions.

**Note:**

If there are values that you’d like to use for event_type that are not in the list above, then please share your request in the [Shopify Community APIs and SDKs discussion board](https://community.shopify.com/c/shopify-apis-and-sdks/bd-p/shopify-apis-and-technology) providing as much detail as possible. Our approach is to be more structured than using freeform text, but to still allow for categorization of most types of marketing actions.

* * *

marketing_channel

->[marketingChannelType](/docs/api/admin-graphql/latest/objects/MarketingEvent#field-MarketingEvent.fields.marketingChannelType)

The channel that your marketing event will use. Valid values: `search`, `display`, `social`, `email`, `referral`.

* * *

paid

deprecated**deprecated**

Whether the event is paid or organic.

* * *

referring_domain

deprecated**deprecated**

The destination domain of the marketing event. Required if the `marketing_channel` is set to `search` or `social`.

* * *

budget

->[total](/docs/api/admin-graphql/latest/objects/MarketingBudget#field-MarketingBudget.fields.total)

The budget of the ad campaign.

* * *

currency

->[total](/docs/api/admin-graphql/latest/objects/MarketingBudget#field-MarketingBudget.fields.total)

The currency for the budget. Required if `budget` is specified.

* * *

budget_type

->[budgetType](/docs/api/admin-graphql/latest/objects/MarketingBudget#field-MarketingBudget.fields.budgetType)

The type of the budget. Required if `budget` is specified. Valid values: `daily`, `lifetime`.'

* * *

started_at

->[startedAt](/docs/api/admin-graphql/latest/objects/MarketingEvent#field-MarketingEvent.fields.startedAt)

The time when the marketing action was started.

* * *

scheduled_to_end_at

->[scheduledToEndAt](/docs/api/admin-graphql/latest/objects/MarketingEvent#field-MarketingEvent.fields.scheduledToEndAt)

For events with a duration, the time when the event was scheduled to end.

* * *

ended_at

->[endedAt](/docs/api/admin-graphql/latest/objects/MarketingEvent#field-MarketingEvent.fields.endedAt)

For events with a duration, the time when the event actually ended.

* * *

UTM parameters

->[utmCampaign](/docs/api/admin-graphql/latest/objects/MarketingEvent#field-MarketingEvent.fields.utmCampaign)

The [UTM parameters](https://en.wikipedia.org/wiki/UTM_parameters) used in the links provided in the marketing event. Values must be unique and should not be url-encoded.

To do traffic or order attribution you must at least define `utm_campaign`, `utm_source`, and `utm_medium`.

* * *

Show 4 hidden fields

Was this section helpful?

YesNo

{}

## The MarketingEvent resource

99

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

{

"remote_id": "123abc",

"event_type": "ad",

"marketing_channel": "social",

"paid": true,

"referring_domain": "facebook.com",

"budget": 10.75,

"currency": "USD",

"budget_type": "lifetime",

"started_at": "2026-01-15T11:56:18-04:00",

"scheduled_to_end_at": "2026-01-22T11:56:18-04:00",

"ended_at": "2026-01-20T11:56:18-04:00",

"UTM parameters": {

"marketing_event": {

"utm_campaign": "CanadaDay2026",

"utm_source": "facebook",

"utm_medium": "cpc"

}

},

"description": "Facebook carousel ad 2026",

"manage_url": "https://mymarketingapp.com/ad/1234",

"preview_url": "https://www.facebook.com/123456/",

"marketed_resources": [

{

"type": "product",

"id": 12345

}

]

}

* * *

##

[Anchor to POST request, Creates a marketing event](/docs/api/admin-rest/latest/resources/marketingevent#post-marketing-events)

post

Creates a marketing event

[marketingActivityCreateExternal](/docs/api/admin-graphql/latest/mutations/marketingActivityCreateExternal?example=creates-a-marketing-event)

Requires `marketing_events` access scope.

**Requires `marketing_events` access scope.:**

Marketing events can be created to track ad campaigns that target a specific time of year. For example, a marketing event can be created to track a Facebook ad campaign for Christmas 2022. When creating the marketing event, the body of the request includes the UTM parameters that must be included in the links provided in the marketing event. Each marketing event also includes the `event_type` and `marketing_channel` properties that help Shopify to rank your app and surface it within Shopify admin.




After a marketing event is created in Shopify, you can start to drive traffic to Shopify. Make sure that the links for the marketing event contain the same UTM parameters that were defined in the marketing event. For example, marketing activities for the Christmas 2022 ad campaign would use the following URL convention:




`https://storename.com/product?utm_source=facebook&utm_medium=cpc&utm_campaign=Christmas2022-12142018`

###

[Anchor to Parameters of Creates a marketing event](/docs/api/admin-rest/latest/resources/marketingevent#post-marketing-events-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to post-marketing-events-examples](/docs/api/admin-rest/latest/resources/marketingevent#post-marketing-events-examples)Examples

Create a marketing event

Request body

marketing_event

Marketing_event resource**Marketing_event resource**

Show marketing_event properties

marketing_event.started_at:"2026-12-15"

->[start](/docs/api/admin-graphql/latest/input-objects/MarketingActivityCreateExternalInput#fields-start)

The time when the marketing action was started.

marketing_event.event_type:"ad"

->[tactic](/docs/api/admin-graphql/latest/input-objects/MarketingActivityCreateExternalInput#fields-tactic)

The type of marketing event. Valid values: `ad`, `post`, `message`, `retargeting`, `transactional`, `affiliate`, `loyalty`, `newsletter`, `abandoned_cart`.

Note

If there are values that you’d like to use for event_type that are not in the list above, then please share your request in the [Shopify Community APIs and SDKs discussion board](https://community.shopify.com/c/shopify-apis-and-sdks/bd-p/shopify-apis-and-technology) providing as much detail as possible. Our approach is to be more structured than using freeform text, but to still allow for categorization of most types of marketing actions.

**Note:**

If there are values that you’d like to use for event_type that are not in the list above, then please share your request in the [Shopify Community APIs and SDKs discussion board](https://community.shopify.com/c/shopify-apis-and-sdks/bd-p/shopify-apis-and-technology) providing as much detail as possible. Our approach is to be more structured than using freeform text, but to still allow for categorization of most types of marketing actions.

marketing_event.referring_domain:"facebook.com"

deprecated**deprecated**

The destination domain of the marketing event. Required if the `marketing_channel` is set to `search` or `social`.

marketing_event.marketing_channel:"social"

->[marketingChannelType](/docs/api/admin-graphql/latest/input-objects/MarketingActivityCreateExternalInput#fields-marketingChannelType)

The channel that your marketing event will use. Valid values: `search`, `display`, `social`, `email`, `referral`.

marketing_event.paid:true

deprecated**deprecated**

Whether the event is paid or organic.

Was this section helpful?

YesNo

post

## /admin/api/2026-01/marketing_events.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{"marketing_event":{"started_at":"2026-12-15","utm_campaign":"Christmas2026","utm_source":"facebook","utm_medium":"cpc","event_type":"ad","referring_domain":"facebook.com","marketing_channel":"social","paid":true}}' \

-X POST "https://your-development-store.myshopify.com/admin/api/2026-01/marketing_events.json" \

-H "X-Shopify-Access-Token: {access_token}" \

-H "Content-Type: application/json"

{}

## Response

JSON

99

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

HTTP/1.1 201 Created

{

"marketing_event": {

"id": 1069063884,

"event_type": "ad",

"remote_id": null,

"started_at": "2026-12-15T01:00:00-05:00",

"ended_at": null,

"scheduled_to_end_at": null,

"budget": null,

"currency": null,

"manage_url": null,

"preview_url": null,

"utm_campaign": "Christmas2026",

"utm_source": "facebook",

"utm_medium": "cpc",

"budget_type": null,

"description": null,

"marketing_channel": "social",

"delivery_channel": null,

"paid": true,

"referring_domain": "facebook.com",

"breadcrumb_id": null,

"marketing_activity_id": 1063897334,

"admin_graphql_api_id": "gid://shopify/MarketingEvent/1069063884",

"marketed_resources": []

}

}

### examples

  * #### Create a marketing event

#####

        curl -d '{"marketing_event":{"started_at":"2026-12-15","utm_campaign":"Christmas2026","utm_source":"facebook","utm_medium":"cpc","event_type":"ad","referring_domain":"facebook.com","marketing_channel":"social","paid":true}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/marketing_events.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const marketing_event = new admin.rest.resources.MarketingEvent({session: session});

        marketing_event.started_at = "2026-12-15";
        marketing_event.utm_campaign = "Christmas2026";
        marketing_event.utm_source = "facebook";
        marketing_event.utm_medium = "cpc";
        marketing_event.event_type = "ad";
        marketing_event.referring_domain = "facebook.com";
        marketing_event.marketing_channel = "social";
        marketing_event.paid = true;
        await marketing_event.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        marketing_event = ShopifyAPI::MarketingEvent.new(session: test_session)
        marketing_event.started_at = "2026-12-15"
        marketing_event.utm_campaign = "Christmas2026"
        marketing_event.utm_source = "facebook"
        marketing_event.utm_medium = "cpc"
        marketing_event.event_type = "ad"
        marketing_event.referring_domain = "facebook.com"
        marketing_event.marketing_channel = "social"
        marketing_event.paid = true
        marketing_event.save!

#####

        // Session is built by the OAuth process

        const marketing_event = new shopify.rest.MarketingEvent({session: session});
        marketing_event.started_at = "2026-12-15";
        marketing_event.utm_campaign = "Christmas2026";
        marketing_event.utm_source = "facebook";
        marketing_event.utm_medium = "cpc";
        marketing_event.event_type = "ad";
        marketing_event.referring_domain = "facebook.com";
        marketing_event.marketing_channel = "social";
        marketing_event.paid = true;
        await marketing_event.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"marketing_event":{"id":1069063884,"event_type":"ad","remote_id":null,"started_at":"2026-12-15T01:00:00-05:00","ended_at":null,"scheduled_to_end_at":null,"budget":null,"currency":null,"manage_url":null,"preview_url":null,"utm_campaign":"Christmas2026","utm_source":"facebook","utm_medium":"cpc","budget_type":null,"description":null,"marketing_channel":"social","delivery_channel":null,"paid":true,"referring_domain":"facebook.com","breadcrumb_id":null,"marketing_activity_id":1063897334,"admin_graphql_api_id":"gid://shopify/MarketingEvent/1069063884","marketed_resources":[]}}


* * *

##

[Anchor to POST request, Creates marketing engagements on a marketing event](/docs/api/admin-rest/latest/resources/marketingevent#post-marketing-events-marketing-event-id-engagements)

post

Creates marketing engagements on a marketing event

[marketingEngagementCreate](/docs/api/admin-graphql/latest/mutations/marketingEngagementCreate?example=creates-marketing-engagements-on-a-marketing-event)

Engagements on marketing events represent customer activity taken on the marketing event before customers reach the shop’s website. Not all types of marketing events will necessarily have engagement, and most types of marketing events will only use a subset of the possible engagement types.




Engagements are aggregated on a daily basis. However, the data can be sent more often than once a day if the information is available. If you create an engagement with the same value for `occurred_on` as an existing engagement, then the new engagement will overwrite the previous one.

###

[Anchor to Parameters of Creates marketing engagements on a marketing event](/docs/api/admin-rest/latest/resources/marketingevent#post-marketing-events-marketing-event-id-engagements-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

marketing_event_id

string**string**

required**required**

* * *

occurred_on

required**required**

The date that these engagements occurred on, in the format “YYYY-MM-DD”.

* * *

ad_spend

The total ad spend for the day, if the marketing event is a paid ad with a daily spend.

* * *

clicks_count

The total number of clicks on the marketing event for the day.

* * *

comments_count

The total number of comments for the day.

* * *

favorites_count

The total number of favorites for the day.

* * *

impressions_count

The total number of impressions for the day. An impression occurs when the marketing event is served to a customer, either as a email or through a marketing channel.

* * *

is_cumulative

Whether the engagements are reported as lifetime values rather than daily totals.

* * *

shares_count

The total number of shares for the day.

* * *

views_count

The total number of views for the day. A view occurs when a customer reads the marketing event that was served to them, for example, if the customer opens the email or spends time looking at a Facebook post.

* * *

Was this section helpful?

YesNo

###

[Anchor to post-marketing-events-marketing-event-id-engagements-examples](/docs/api/admin-rest/latest/resources/marketingevent#post-marketing-events-marketing-event-id-engagements-examples)Examples

Add engagements to a marketing engagement

Path parameters

marketing_event_id=998730532

string**string**

required**required**

Was this section helpful?

YesNo

post

## /admin/api/2026-01/marketing_events/998730532/engagements.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{"engagements":[{"occurred_on":"2026-01-15","views_count":0,"clicks_count":0,"favorites_count":0,"ad_spend":10.0,"is_cumulative":true},{"occurred_on":"2026-01-16","views_count":100,"clicks_count":50,"is_cumulative":true},{"occurred_on":"2026-01-17","views_count":200,"clicks_count":100,"is_cumulative":true}]}' \

-X POST "https://your-development-store.myshopify.com/admin/api/2026-01/marketing_events/998730532/engagements.json" \

-H "X-Shopify-Access-Token: {access_token}" \

-H "Content-Type: application/json"

{}

## Response

JSON

99

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

30

31

32

33

34

35

36

37

38

39

40

41

42

43

44

45

46

47

48

49

50

51

52

53

54

55

56

57

58

59

60

61

62

63

64

65

HTTP/1.1 201 Created

{

"engagements": [

{

"occurred_on": "2026-01-15",

"fetched_at": null,

"views_count": 0,

"impressions_count": null,

"clicks_count": 0,

"favorites_count": 0,

"comments_count": null,

"shares_count": null,

"ad_spend": "10.0",

"currency_code": null,

"is_cumulative": true,

"unsubscribes_count": null,

"complaints_count": null,

"fails_count": null,

"sends_count": null,

"unique_views_count": null,

"unique_clicks_count": null,

"utc_offset": null

},

{

"occurred_on": "2026-01-16",

"fetched_at": null,

"views_count": 100,

"impressions_count": null,

"clicks_count": 50,

"favorites_count": null,

"comments_count": null,

"shares_count": null,

"ad_spend": null,

"currency_code": null,

"is_cumulative": true,

"unsubscribes_count": null,

"complaints_count": null,

"fails_count": null,

"sends_count": null,

"unique_views_count": null,

"unique_clicks_count": null,

"utc_offset": null

},

{

"occurred_on": "2026-01-17",

"fetched_at": null,

"views_count": 200,

"impressions_count": null,

"clicks_count": 100,

"favorites_count": null,

"comments_count": null,

"shares_count": null,

"ad_spend": null,

"currency_code": null,

"is_cumulative": true,

"unsubscribes_count": null,

"complaints_count": null,

"fails_count": null,

"sends_count": null,

"unique_views_count": null,

"unique_clicks_count": null,

"utc_offset": null

}

]

}

### examples

  * #### Add engagements to a marketing engagement

#####

        curl -d '{"engagements":[{"occurred_on":"2026-01-15","views_count":0,"clicks_count":0,"favorites_count":0,"ad_spend":10.0,"is_cumulative":true},{"occurred_on":"2026-01-16","views_count":100,"clicks_count":50,"is_cumulative":true},{"occurred_on":"2026-01-17","views_count":200,"clicks_count":100,"is_cumulative":true}]}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/marketing_events/998730532/engagements.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const marketing_event = new admin.rest.resources.MarketingEvent({session: session});

        marketing_event.id = 998730532;
        await marketing_event.engagements({
          body: {"engagements": [{"occurred_on": "2026-01-15", "views_count": 0, "clicks_count": 0, "favorites_count": 0, "ad_spend": 10.0, "is_cumulative": true}, {"occurred_on": "2026-01-16", "views_count": 100, "clicks_count": 50, "is_cumulative": true}, {"occurred_on": "2026-01-17", "views_count": 200, "clicks_count": 100, "is_cumulative": true}]},
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        marketing_event = ShopifyAPI::MarketingEvent.new(session: test_session)
        marketing_event.id = 998730532
        marketing_event.engagements(
          session: test_session,
          body: {"engagements" => [{"occurred_on" => "2026-01-15", "views_count" => 0, "clicks_count" => 0, "favorites_count" => 0, "ad_spend" => 10.0, "is_cumulative" => true}, {"occurred_on" => "2026-01-16", "views_count" => 100, "clicks_count" => 50, "is_cumulative" => true}, {"occurred_on" => "2026-01-17", "views_count" => 200, "clicks_count" => 100, "is_cumulative" => true}]},
        )

#####

        // Session is built by the OAuth process

        const marketing_event = new shopify.rest.MarketingEvent({session: session});
        marketing_event.id = 998730532;
        await marketing_event.engagements({
          body: {"engagements": [{"occurred_on": "2026-01-15", "views_count": 0, "clicks_count": 0, "favorites_count": 0, "ad_spend": 10.0, "is_cumulative": true}, {"occurred_on": "2026-01-16", "views_count": 100, "clicks_count": 50, "is_cumulative": true}, {"occurred_on": "2026-01-17", "views_count": 200, "clicks_count": 100, "is_cumulative": true}]},
        });

#### response

        HTTP/1.1 201 Created{"engagements":[{"occurred_on":"2026-01-15","fetched_at":null,"views_count":0,"impressions_count":null,"clicks_count":0,"favorites_count":0,"comments_count":null,"shares_count":null,"ad_spend":"10.0","currency_code":null,"is_cumulative":true,"unsubscribes_count":null,"complaints_count":null,"fails_count":null,"sends_count":null,"unique_views_count":null,"unique_clicks_count":null,"utc_offset":null},{"occurred_on":"2026-01-16","fetched_at":null,"views_count":100,"impressions_count":null,"clicks_count":50,"favorites_count":null,"comments_count":null,"shares_count":null,"ad_spend":null,"currency_code":null,"is_cumulative":true,"unsubscribes_count":null,"complaints_count":null,"fails_count":null,"sends_count":null,"unique_views_count":null,"unique_clicks_count":null,"utc_offset":null},{"occurred_on":"2026-01-17","fetched_at":null,"views_count":200,"impressions_count":null,"clicks_count":100,"favorites_count":null,"comments_count":null,"shares_count":null,"ad_spend":null,"currency_code":null,"is_cumulative":true,"unsubscribes_count":null,"complaints_count":null,"fails_count":null,"sends_count":null,"unique_views_count":null,"unique_clicks_count":null,"utc_offset":null}]}


* * *

##

[Anchor to GET request, Retrieves a list of all marketing events](/docs/api/admin-rest/latest/resources/marketingevent#get-marketing-events)

get

Retrieves a list of all marketing events

[marketingEvents](/docs/api/admin-graphql/latest/queries/marketingEvents?example=retrieves-a-list-of-all-marketing-events)

Requires `marketing_events` access scope.

**Requires `marketing_events` access scope.:**

Retrieves a list of all marketing events. **Note:** This endpoint implements pagination by using links that are provided in the response header. To learn more, refer to [Make paginated requests to the REST Admin API](/api/usage/pagination-rest).

###

[Anchor to Parameters of Retrieves a list of all marketing events](/docs/api/admin-rest/latest/resources/marketingevent#get-marketing-events-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

count

≤ 250**≤ 250**

default 50**default 50**

The amount of results to return.

* * *

offset

The number of marketing events to skip.

* * *

Was this section helpful?

YesNo

###

[Anchor to get-marketing-events-examples](/docs/api/admin-rest/latest/resources/marketingevent#get-marketing-events-examples)Examples

Retrieve all marketing events

Was this section helpful?

YesNo

get

## /admin/api/2026-01/marketing_events.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/marketing_events.json" \

-H "X-Shopify-Access-Token: {access_token}"

{}

## Response

JSON

99

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

30

HTTP/1.1 200 OK

{

"marketing_events": [

{

"id": 998730532,

"event_type": "post",

"remote_id": "12345678",

"started_at": "2026-01-15T10:56:18-05:00",

"ended_at": null,

"scheduled_to_end_at": null,

"budget": "10.11",

"currency": "GBP",

"manage_url": null,

"preview_url": null,

"utm_campaign": "1234567890",

"utm_source": "facebook",

"utm_medium": "facebook-post",

"budget_type": "daily",

"description": null,

"marketing_channel": "social",

"delivery_channel": null,

"paid": false,

"referring_domain": "facebook.com",

"breadcrumb_id": null,

"marketing_activity_id": null,

"admin_graphql_api_id": "gid://shopify/MarketingEvent/998730532",

"marketed_resources": []

}

]

}

### examples

  * #### Retrieve all marketing events

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/marketing_events.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.MarketingEvent.all({
          session: session,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::MarketingEvent.all(
          session: test_session,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.MarketingEvent.all({
          session: session,
        });

#### response

        HTTP/1.1 200 OK{"marketing_events":[{"id":998730532,"event_type":"post","remote_id":"12345678","started_at":"2026-01-15T10:56:18-05:00","ended_at":null,"scheduled_to_end_at":null,"budget":"10.11","currency":"GBP","manage_url":null,"preview_url":null,"utm_campaign":"1234567890","utm_source":"facebook","utm_medium":"facebook-post","budget_type":"daily","description":null,"marketing_channel":"social","delivery_channel":null,"paid":false,"referring_domain":"facebook.com","breadcrumb_id":null,"marketing_activity_id":null,"admin_graphql_api_id":"gid://shopify/MarketingEvent/998730532","marketed_resources":[]}]}


* * *

##

[Anchor to GET request, Retrieves a single marketing event](/docs/api/admin-rest/latest/resources/marketingevent#get-marketing-events-marketing-event-id)

get

Retrieves a single marketing event

[marketingEvent](/docs/api/admin-graphql/latest/queries/marketingEvent?example=retrieves-a-single-marketing-event)

Requires `marketing_events` access scope.

**Requires `marketing_events` access scope.:**

Retrieves a single marketing event

###

[Anchor to Parameters of Retrieves a single marketing event](/docs/api/admin-rest/latest/resources/marketingevent#get-marketing-events-marketing-event-id-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

marketing_event_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to get-marketing-events-marketing-event-id-examples](/docs/api/admin-rest/latest/resources/marketingevent#get-marketing-events-marketing-event-id-examples)Examples

Retrieve a single marketing event by its ID

Path parameters

marketing_event_id=998730532

string**string**

required**required**

Was this section helpful?

YesNo

get

## /admin/api/2026-01/marketing_events/998730532.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/marketing_events/998730532.json" \

-H "X-Shopify-Access-Token: {access_token}"

{}

## Response

JSON

99

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

HTTP/1.1 200 OK

{

"marketing_event": {

"id": 998730532,

"event_type": "post",

"remote_id": "12345678",

"started_at": "2026-01-15T10:56:18-05:00",

"ended_at": null,

"scheduled_to_end_at": null,

"budget": "10.11",

"currency": "GBP",

"manage_url": null,

"preview_url": null,

"utm_campaign": "1234567890",

"utm_source": "facebook",

"utm_medium": "facebook-post",

"budget_type": "daily",

"description": null,

"marketing_channel": "social",

"delivery_channel": null,

"paid": false,

"referring_domain": "facebook.com",

"breadcrumb_id": null,

"marketing_activity_id": null,

"admin_graphql_api_id": "gid://shopify/MarketingEvent/998730532",

"marketed_resources": []

}

}

### examples

  * #### Retrieve a single marketing event by its ID

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/marketing_events/998730532.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.MarketingEvent.find({
          session: session,
          id: 998730532,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::MarketingEvent.find(
          session: test_session,
          id: 998730532,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.MarketingEvent.find({
          session: session,
          id: 998730532,
        });

#### response

        HTTP/1.1 200 OK{"marketing_event":{"id":998730532,"event_type":"post","remote_id":"12345678","started_at":"2026-01-15T10:56:18-05:00","ended_at":null,"scheduled_to_end_at":null,"budget":"10.11","currency":"GBP","manage_url":null,"preview_url":null,"utm_campaign":"1234567890","utm_source":"facebook","utm_medium":"facebook-post","budget_type":"daily","description":null,"marketing_channel":"social","delivery_channel":null,"paid":false,"referring_domain":"facebook.com","breadcrumb_id":null,"marketing_activity_id":null,"admin_graphql_api_id":"gid://shopify/MarketingEvent/998730532","marketed_resources":[]}}


* * *

##

[Anchor to GET request, Retrieves a count of all marketing events](/docs/api/admin-rest/latest/resources/marketingevent#get-marketing-events-count)

get

Retrieves a count of all marketing events

deprecated**deprecated**

Requires `marketing_events` access scope.

**Requires `marketing_events` access scope.:**

Retrieves a count of all marketing events

###

[Anchor to Parameters of Retrieves a count of all marketing events](/docs/api/admin-rest/latest/resources/marketingevent#get-marketing-events-count-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to get-marketing-events-count-examples](/docs/api/admin-rest/latest/resources/marketingevent#get-marketing-events-count-examples)Examples

Retrieve a count all marketing events

Was this section helpful?

YesNo

get

## /admin/api/2026-01/marketing_events/count.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/marketing_events/count.json" \

-H "X-Shopify-Access-Token: {access_token}"

{}

## Response

JSON

9

1

2

3

4

HTTP/1.1 200 OK

{

"count": 1

}

### examples

  * #### Retrieve a count all marketing events

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/marketing_events/count.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.MarketingEvent.count({
          session: session,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::MarketingEvent.count(
          session: test_session,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.MarketingEvent.count({
          session: session,
        });

#### response

        HTTP/1.1 200 OK{"count":1}


* * *

##

[Anchor to PUT request, Updates a marketing event](/docs/api/admin-rest/latest/resources/marketingevent#put-marketing-events-marketing-event-id)

put

Updates a marketing event

[marketingActivityUpdateExternal](/docs/api/admin-graphql/latest/mutations/marketingActivityUpdateExternal?example=updates-a-marketing-event)

Requires `marketing_events` access scope.

**Requires `marketing_events` access scope.:**

Updates a marketing event

###

[Anchor to Parameters of Updates a marketing event](/docs/api/admin-rest/latest/resources/marketingevent#put-marketing-events-marketing-event-id-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

marketing_event_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to put-marketing-events-marketing-event-id-examples](/docs/api/admin-rest/latest/resources/marketingevent#put-marketing-events-marketing-event-id-examples)Examples

Update a marketing event. Can modify only timestamps, remote_id, and budget/currency.

Path parameters

marketing_event_id=998730532

string**string**

required**required**

Request body

marketing_event

Marketing_event resource**Marketing_event resource**

Show marketing_event properties

marketing_event.remote_id:"1000:2000"

An optional remote identifier for a marketing event. The remote identifier lets Shopify validate engagement data.

marketing_event.started_at:"2026-02-02T00:00 +00:00"

->[start](/docs/api/admin-graphql/latest/input-objects/MarketingActivityUpdateExternalInput#fields-start)

The time when the marketing action was started.

marketing_event.ended_at:"2026-02-03T00:00 +00:00"

->[end](/docs/api/admin-graphql/latest/input-objects/MarketingActivityUpdateExternalInput#fields-end)

For events with a duration, the time when the event actually ended.

marketing_event.scheduled_to_end_at:"2026-02-04T00:00 +00:00"

->[scheduledEnd](/docs/api/admin-graphql/latest/input-objects/MarketingActivityUpdateExternalInput#fields-scheduledEnd)

For events with a duration, the time when the event was scheduled to end.

marketing_event.budget:"11.1"

->[total](/docs/api/admin-graphql/latest/input-objects/MarketingActivityBudgetInput#fields-total)

The budget of the ad campaign.

marketing_event.budget_type:"daily"

->[budgetType](/docs/api/admin-graphql/latest/input-objects/MarketingActivityBudgetInput#fields-budgetType)

The type of the budget. Required if `budget` is specified. Valid values: `daily`, `lifetime`.'

marketing_event.currency:"CAD"

->[total](/docs/api/admin-graphql/latest/input-objects/MarketingActivityBudgetInput#fields-total)

The currency for the budget. Required if `budget` is specified.

marketing_event.event_type:"ad"

->[tactic](/docs/api/admin-graphql/latest/input-objects/MarketingActivityUpdateExternalInput#fields-tactic)

The type of marketing event. Valid values: `ad`, `post`, `message`, `retargeting`, `transactional`, `affiliate`, `loyalty`, `newsletter`, `abandoned_cart`.

Note

If there are values that you’d like to use for event_type that are not in the list above, then please share your request in the [Shopify Community APIs and SDKs discussion board](https://community.shopify.com/c/shopify-apis-and-sdks/bd-p/shopify-apis-and-technology) providing as much detail as possible. Our approach is to be more structured than using freeform text, but to still allow for categorization of most types of marketing actions.

**Note:**

If there are values that you’d like to use for event_type that are not in the list above, then please share your request in the [Shopify Community APIs and SDKs discussion board](https://community.shopify.com/c/shopify-apis-and-sdks/bd-p/shopify-apis-and-technology) providing as much detail as possible. Our approach is to be more structured than using freeform text, but to still allow for categorization of most types of marketing actions.

marketing_event.referring_domain:"instagram.com"

deprecated**deprecated**

The destination domain of the marketing event. Required if the `marketing_channel` is set to `search` or `social`.

Was this section helpful?

YesNo

put

## /admin/api/2026-01/marketing_events/998730532.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{"marketing_event":{"id":998730532,"remote_id":"1000:2000","started_at":"2026-02-02T00:00 +00:00","ended_at":"2026-02-03T00:00 +00:00","scheduled_to_end_at":"2026-02-04T00:00 +00:00","budget":"11.1","budget_type":"daily","currency":"CAD","utm_campaign":"other","utm_source":"other","utm_medium":"other","event_type":"ad","referring_domain":"instagram.com"}}' \

-X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/marketing_events/998730532.json" \

-H "X-Shopify-Access-Token: {access_token}" \

-H "Content-Type: application/json"

{}

## Response

JSON

99

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

HTTP/1.1 200 OK

{

"marketing_event": {

"started_at": "2026-02-01T19:00:00-05:00",

"ended_at": "2026-02-02T19:00:00-05:00",

"scheduled_to_end_at": "2026-02-03T19:00:00-05:00",

"remote_id": "1000:2000",

"currency": "CAD",

"budget": "11.1",

"budget_type": "daily",

"event_type": "post",

"id": 998730532,

"manage_url": null,

"preview_url": null,

"utm_campaign": "1234567890",

"utm_source": "facebook",

"utm_medium": "facebook-post",

"description": null,

"marketing_channel": "social",

"delivery_channel": null,

"paid": false,

"referring_domain": "facebook.com",

"breadcrumb_id": null,

"marketing_activity_id": null,

"admin_graphql_api_id": "gid://shopify/MarketingEvent/998730532",

"marketed_resources": []

}

}

### examples

  * #### Update a marketing event. Can modify only timestamps, remote_id, and budget/currency.

#####

        curl -d '{"marketing_event":{"id":998730532,"remote_id":"1000:2000","started_at":"2026-02-02T00:00 +00:00","ended_at":"2026-02-03T00:00 +00:00","scheduled_to_end_at":"2026-02-04T00:00 +00:00","budget":"11.1","budget_type":"daily","currency":"CAD","utm_campaign":"other","utm_source":"other","utm_medium":"other","event_type":"ad","referring_domain":"instagram.com"}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/marketing_events/998730532.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const marketing_event = new admin.rest.resources.MarketingEvent({session: session});

        marketing_event.id = 998730532;
        marketing_event.remote_id = "1000:2000";
        marketing_event.started_at = "2026-02-02T00:00 +00:00";
        marketing_event.ended_at = "2026-02-03T00:00 +00:00";
        marketing_event.scheduled_to_end_at = "2026-02-04T00:00 +00:00";
        marketing_event.budget = "11.1";
        marketing_event.budget_type = "daily";
        marketing_event.currency = "CAD";
        marketing_event.utm_campaign = "other";
        marketing_event.utm_source = "other";
        marketing_event.utm_medium = "other";
        marketing_event.event_type = "ad";
        marketing_event.referring_domain = "instagram.com";
        await marketing_event.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        marketing_event = ShopifyAPI::MarketingEvent.new(session: test_session)
        marketing_event.id = 998730532
        marketing_event.remote_id = "1000:2000"
        marketing_event.started_at = "2026-02-02T00:00 +00:00"
        marketing_event.ended_at = "2026-02-03T00:00 +00:00"
        marketing_event.scheduled_to_end_at = "2026-02-04T00:00 +00:00"
        marketing_event.budget = "11.1"
        marketing_event.budget_type = "daily"
        marketing_event.currency = "CAD"
        marketing_event.utm_campaign = "other"
        marketing_event.utm_source = "other"
        marketing_event.utm_medium = "other"
        marketing_event.event_type = "ad"
        marketing_event.referring_domain = "instagram.com"
        marketing_event.save!

#####

        // Session is built by the OAuth process

        const marketing_event = new shopify.rest.MarketingEvent({session: session});
        marketing_event.id = 998730532;
        marketing_event.remote_id = "1000:2000";
        marketing_event.started_at = "2026-02-02T00:00 +00:00";
        marketing_event.ended_at = "2026-02-03T00:00 +00:00";
        marketing_event.scheduled_to_end_at = "2026-02-04T00:00 +00:00";
        marketing_event.budget = "11.1";
        marketing_event.budget_type = "daily";
        marketing_event.currency = "CAD";
        marketing_event.utm_campaign = "other";
        marketing_event.utm_source = "other";
        marketing_event.utm_medium = "other";
        marketing_event.event_type = "ad";
        marketing_event.referring_domain = "instagram.com";
        await marketing_event.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"marketing_event":{"started_at":"2026-02-01T19:00:00-05:00","ended_at":"2026-02-02T19:00:00-05:00","scheduled_to_end_at":"2026-02-03T19:00:00-05:00","remote_id":"1000:2000","currency":"CAD","budget":"11.1","budget_type":"daily","event_type":"post","id":998730532,"manage_url":null,"preview_url":null,"utm_campaign":"1234567890","utm_source":"facebook","utm_medium":"facebook-post","description":null,"marketing_channel":"social","delivery_channel":null,"paid":false,"referring_domain":"facebook.com","breadcrumb_id":null,"marketing_activity_id":null,"admin_graphql_api_id":"gid://shopify/MarketingEvent/998730532","marketed_resources":[]}}


* * *

##

[Anchor to DELETE request, Deletes a marketing event](/docs/api/admin-rest/latest/resources/marketingevent#delete-marketing-events-marketing-event-id)

del

Deletes a marketing event

[marketingActivityDeleteExternal](/docs/api/admin-graphql/latest/mutations/marketingActivityDeleteExternal?example=deletes-a-marketing-event)

Requires `marketing_events` access scope.

**Requires `marketing_events` access scope.:**

Deletes a marketing event

###

[Anchor to Parameters of Deletes a marketing event](/docs/api/admin-rest/latest/resources/marketingevent#delete-marketing-events-marketing-event-id-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

marketing_event_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to delete-marketing-events-marketing-event-id-examples](/docs/api/admin-rest/latest/resources/marketingevent#delete-marketing-events-marketing-event-id-examples)Examples

Delete a marketing event

Path parameters

marketing_event_id=998730532

string**string**

required**required**

Was this section helpful?

YesNo

del

## /admin/api/2026-01/marketing_events/998730532.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X DELETE "https://your-development-store.myshopify.com/admin/api/2026-01/marketing_events/998730532.json" \

-H "X-Shopify-Access-Token: {access_token}"

{}

## Response

JSON

9

1

2

HTTP/1.1 200 OK

{}

### examples

  * #### Delete a marketing event

#####

        curl -X DELETE "https://your-development-store.myshopify.com/admin/api/2026-01/marketing_events/998730532.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.MarketingEvent.delete({
          session: session,
          id: 998730532,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::MarketingEvent.delete(
          session: test_session,
          id: 998730532,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.MarketingEvent.delete({
          session: session,
          id: 998730532,
        });

#### response

        HTTP/1.1 200 OK{}