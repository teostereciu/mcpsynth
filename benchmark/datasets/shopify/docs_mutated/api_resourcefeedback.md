# ResourceFeedback

*Source: https://shopify.dev/docs/api/admin-rest/2026-01/resources/resourcefeedback*

---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04

2026-01latest

# ResourceFeedback

Ask assistant

Requires `resource_feedbacks` access scope.

**Requires `resource_feedbacks` access scope.:**

The ResourceFeedback resource lets your app report the status of shops and their resources. For example, if your app is a marketplace channel, then you can use resource feedback to alert merchants that they need to connect their marketplace account by signing in.

Resource feedback notifications are displayed to the merchant on the home screen of their Shopify admin, and in the product details view for any products that are published to your app.

This resource should be used only in cases where you're describing steps that a merchant is required to complete. If your app offers optional or promotional set-up steps, or if it makes recommendations, then don't use resource feedback to let merchants know about them.

## Sending feedback on a shop

You can send resource feedback on a shop to let the merchant know what steps they need to take to make sure that your app is set up correctly. Feedback can have one of two states: `requires_action` or `success`. You need to send a `requires_action` feedback request for each step that the merchant is required to complete.

If there are multiple set-up steps that require merchant action, then send feedback with a state of `requires_action` as merchants complete prior steps. And to remove the feedback message from the Shopify admin, send a `success` feedback request.

Important

Sending feedback replaces previously sent feedback for the Shop. Unlike REST-style APIs, you don't need to make a PATCH or PUT request to update any previously sent feedback. Send a new POST request to push the latest state of a shop or its resources to Shopify.

**Important:**

Sending feedback replaces previously sent feedback for the Shop. Unlike REST-style APIs, you don't need to make a PATCH or PUT request to update any previously sent feedback. Send a new POST request to push the latest state of a shop or its resources to Shopify.

## Formatting the resource feedback message field

If the feedback state is `requires_action`, then you can send a string message that communicates the action to be taken by the merchant.

The string must be a single message up to 100 characters long and must end with a period. You need to adhere to the message formatting rules or your requests will fail:

* `[Explanation of the problem]. [Suggested action].`



**Examples:**

* `[Your app name]` is not connected. Connect your account to use this sales channel. `[Learn more]`
* `[Your app name]` is not configured. Agree to the terms and conditions to use this app. `[Learn more]`



Both `Your app name` and `Learn more` (a button which directs merchants to your app) are automatically populated in the Shopify admin.

## Setting feedback permissions

Add the `write_resource_feedbacks` permission to your [requested scopes](/docs/admin-api/access-scopes).

Was this section helpful?

YesNo

#

## Endpoints

  * [post/admin/api/latest/resource_feedback.json](/docs/api/admin-rest/latest/resources/resourcefeedback#post-resource-feedback)

Create a new ResourceFeedback

[shopResourceFeedbackCreate](/docs/api/admin-graphql/latest/mutations/shopResourceFeedbackCreate?example=create-a-new-resourcefeedback)

  * [get/admin/api/latest/resource_feedback.json](/docs/api/admin-rest/latest/resources/resourcefeedback#get-resource-feedback)

Receive a list of all ResourceFeedbacks

[app](/docs/api/admin-graphql/latest/queries/app)


* * *

[Anchor to ](/docs/api/admin-rest/latest/resources/resourcefeedback#resource-object)

## The ResourceFeedback resource

[Anchor to ](/docs/api/admin-rest/latest/resources/resourcefeedback#resource-object-properties)

### Properties

* * *

created_at

deprecated**deprecated**

DateTime when the resource feedback record was stored by Shopify. **Type:** ISO 8601 UTC DateTime as string with year, month (or week), day, hour, minute, second, time zone.

* * *

updated_at

deprecated**deprecated**

DateTime when the resource feedback record was last updated by Shopify. **Type:** ISO 8601 UTC DateTime as string with year, month (or week), day, hour, minute, second, time zone.

* * *

resource_id

read-only**read-only**

->[id](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.id)

Unique id of the resource.

* * *

resource_type

read-only**read-only**

->[id](/docs/api/admin-graphql/latest/objects/Shop#field-Shop.fields.id)

Type of resource for which feedback is returned. eg. Shop, Product.

* * *

state

->[state](/docs/api/admin-graphql/latest/objects/AppFeedback#field-AppFeedback.fields.state)

Indicates the state that the Shop or resource is in, from the perspective of your app. Valid values are `requires_action`, or `success`.

* * *

messages

->[messages](/docs/api/admin-graphql/latest/objects/AppFeedback#field-AppFeedback.fields.messages)

A concise set of copy strings to be displayed to merchants, to guide them in resolving problems your app encounters when trying to make use of their Shop and its resources.

Required only when state is `requires_action`. Disallowed when state is `success`.

**Content restrictions for Shop feedback:** one message up to 100 characters long.

* * *

feedback_generated_at

->[feedbackGeneratedAt](/docs/api/admin-graphql/latest/objects/AppFeedback#field-AppFeedback.fields.feedbackGeneratedAt)

The time at which the payload is constructed. Used to help determine whether incoming feedback is outdated compared to feedback already received, and if it should be ignored upon arrival. **Type:** ISO 8601 UTC datetime as string with year, month [or week], day, hour, minute, second, millisecond, and time zone.

Note

If you queue a Feedback API payload for delivery at a later time, do not update this value when the API call is actually made; ensure that the current time is set when building the payload.

**Note:**

If you queue a Feedback API payload for delivery at a later time, do not update this value when the API call is actually made; ensure that the current time is set when building the payload.

* * *

Was this section helpful?

YesNo

{}

## The ResourceFeedback resource

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

{

"created_at": "2026-01-09 22:24:41 UTC",

"updated_at": "2026-01-09 22:24:41 UTC",

"resource_id": 321,

"resource_type": "Shop",

"state": "requires_action",

"messages": [

"is not connected. Connect your account to use this sales channel."

],

"feedback_generated_at": "2026-01-09T22:24:41.097862Z"

}

* * *

##

[Anchor to POST request, Create a new ResourceFeedback](/docs/api/admin-rest/latest/resources/resourcefeedback#post-resource-feedback)

post

Create a new ResourceFeedback

[shopResourceFeedbackCreate](/docs/api/admin-graphql/latest/mutations/shopResourceFeedbackCreate?example=create-a-new-resourcefeedback)

Creates shop resource feedback.

###

[Anchor to Parameters of Create a new ResourceFeedback](/docs/api/admin-rest/latest/resources/resourcefeedback#post-resource-feedback-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

feedback_generated_at

required**required**

An ISO 8601 date and time indicating when the feedback was generated by your app.

* * *

messages

required**required**

An array containing a single message. See  _Formatting the resource feedback message field_ for formatting requirements.

* * *

state

required**required**

Must be one of the following values:

Show state properties

  * **requires_action** : Indicates that your app requires the merchant to resolve an issue with their shop.

  * **success** : Indicates that the app does not have any outstanding issues with this shop.


* * *

Was this section helpful?

YesNo

###

[Anchor to post-resource-feedback-examples](/docs/api/admin-rest/latest/resources/resourcefeedback#post-resource-feedback-examples)Examples

Create a shop feedback record indicating a problem specific to your app

Request body

resource_feedback

Resource_feedback resource**Resource_feedback resource**

Show resource_feedback properties

resource_feedback.state:"requires_action"

Indicates the state that the Shop or resource is in, from the perspective of your app. Valid values are `requires_action`, or `success`.

resource_feedback.messages:["is not connected. Connect your account to use this sales channel."]

A concise set of copy strings to be displayed to merchants, to guide them in resolving problems your app encounters when trying to make use of their Shop and its resources.

Required only when state is `requires_action`. Disallowed when state is `success`.

**Content restrictions for Shop feedback:** one message up to 100 characters long.

resource_feedback.feedback_generated_at:"2026-01-10T00:35:23.828029Z"

The time at which the payload is constructed. Used to help determine whether incoming feedback is outdated compared to feedback already received, and if it should be ignored upon arrival. **Type:** ISO 8601 UTC datetime as string with year, month [or week], day, hour, minute, second, millisecond, and time zone.

Note

If you queue a Feedback API payload for delivery at a later time, do not update this value when the API call is actually made; ensure that the current time is set when building the payload.

**Note:**

If you queue a Feedback API payload for delivery at a later time, do not update this value when the API call is actually made; ensure that the current time is set when building the payload.

Create a shop feedback record indicating the Shop is usable by your app

Request body

resource_feedback

Resource_feedback resource**Resource_feedback resource**

Show resource_feedback properties

resource_feedback.state:"success"

Indicates the state that the Shop or resource is in, from the perspective of your app. Valid values are `requires_action`, or `success`.

resource_feedback.feedback_generated_at:"2026-01-10T00:35:19.887286Z"

The time at which the payload is constructed. Used to help determine whether incoming feedback is outdated compared to feedback already received, and if it should be ignored upon arrival. **Type:** ISO 8601 UTC datetime as string with year, month [or week], day, hour, minute, second, millisecond, and time zone.

Note

If you queue a Feedback API payload for delivery at a later time, do not update this value when the API call is actually made; ensure that the current time is set when building the payload.

**Note:**

If you queue a Feedback API payload for delivery at a later time, do not update this value when the API call is actually made; ensure that the current time is set when building the payload.

Sending an invalid feedback payload returns an error

Request body

resource_feedback

Resource_feedback resource**Resource_feedback resource**

Show resource_feedback properties

resource_feedback.state:"foobar"

Indicates the state that the Shop or resource is in, from the perspective of your app. Valid values are `requires_action`, or `success`.

resource_feedback.feedback_generated_at:"2026-01-10T00:35:22.943032Z"

The time at which the payload is constructed. Used to help determine whether incoming feedback is outdated compared to feedback already received, and if it should be ignored upon arrival. **Type:** ISO 8601 UTC datetime as string with year, month [or week], day, hour, minute, second, millisecond, and time zone.

Note

If you queue a Feedback API payload for delivery at a later time, do not update this value when the API call is actually made; ensure that the current time is set when building the payload.

**Note:**

If you queue a Feedback API payload for delivery at a later time, do not update this value when the API call is actually made; ensure that the current time is set when building the payload.

Sending outdated feedback (previous feedback payload has a greater resource_updated_at value) returns an error

Request body

resource_feedback

Resource_feedback resource**Resource_feedback resource**

Show resource_feedback properties

resource_feedback.state:"success"

Indicates the state that the Shop or resource is in, from the perspective of your app. Valid values are `requires_action`, or `success`.

resource_feedback.feedback_generated_at:"2026-01-10T00:35:21.912732Z"

The time at which the payload is constructed. Used to help determine whether incoming feedback is outdated compared to feedback already received, and if it should be ignored upon arrival. **Type:** ISO 8601 UTC datetime as string with year, month [or week], day, hour, minute, second, millisecond, and time zone.

Note

If you queue a Feedback API payload for delivery at a later time, do not update this value when the API call is actually made; ensure that the current time is set when building the payload.

**Note:**

If you queue a Feedback API payload for delivery at a later time, do not update this value when the API call is actually made; ensure that the current time is set when building the payload.

Was this section helpful?

YesNo

post

## /admin/api/2026-01/resource_feedback.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{"resource_feedback":{"state":"requires_action","messages":["is not connected. Connect your account to use this sales channel."],"feedback_generated_at":"2026-01-10T00:35:23.828029Z"}}' \

-X POST "https://your-development-store.myshopify.com/admin/api/2026-01/resource_feedback.json" \

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

HTTP/1.1 202 Accepted

{

"resource_feedback": {

"created_at": "2026-01-09T19:35:24-05:00",

"updated_at": "2026-01-09T19:35:24-05:00",

"resource_id": 548380009,

"resource_type": "Shop",

"resource_updated_at": null,

"messages": [

"is not connected. Connect your account to use this sales channel."

],

"feedback_generated_at": "2026-01-09T19:35:23-05:00",

"state": "requires_action"

}

}

### examples

  * #### Create a shop feedback record indicating a problem specific to your app

#####

        curl -d '{"resource_feedback":{"state":"requires_action","messages":["is not connected. Connect your account to use this sales channel."],"feedback_generated_at":"2026-01-10T00:35:23.828029Z"}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/resource_feedback.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const resource_feedback = new admin.rest.resources.ResourceFeedback({session: session});

        resource_feedback.state = "requires_action";
        resource_feedback.messages = [
          "is not connected. Connect your account to use this sales channel."
        ];
        resource_feedback.feedback_generated_at = "2026-01-10T00:35:23.828029Z";
        await resource_feedback.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        resource_feedback = ShopifyAPI::ResourceFeedback.new(session: test_session)
        resource_feedback.state = "requires_action"
        resource_feedback.messages = [
          "is not connected. Connect your account to use this sales channel."
        ]
        resource_feedback.feedback_generated_at = "2026-01-10T00:35:23.828029Z"
        resource_feedback.save!

#####

        // Session is built by the OAuth process

        const resource_feedback = new shopify.rest.ResourceFeedback({session: session});
        resource_feedback.state = "requires_action";
        resource_feedback.messages = [
          "is not connected. Connect your account to use this sales channel."
        ];
        resource_feedback.feedback_generated_at = "2026-01-10T00:35:23.828029Z";
        await resource_feedback.save({
          update: true,
        });

#### response

        HTTP/1.1 202 Accepted{"resource_feedback":{"created_at":"2026-01-09T19:35:24-05:00","updated_at":"2026-01-09T19:35:24-05:00","resource_id":548380009,"resource_type":"Shop","resource_updated_at":null,"messages":["is not connected. Connect your account to use this sales channel."],"feedback_generated_at":"2026-01-09T19:35:23-05:00","state":"requires_action"}}

  * #### Create a shop feedback record indicating the Shop is usable by your app

#####

        curl -d '{"resource_feedback":{"state":"success","feedback_generated_at":"2026-01-10T00:35:19.887286Z"}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/resource_feedback.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const resource_feedback = new admin.rest.resources.ResourceFeedback({session: session});

        resource_feedback.state = "success";
        resource_feedback.feedback_generated_at = "2026-01-10T00:35:19.887286Z";
        await resource_feedback.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        resource_feedback = ShopifyAPI::ResourceFeedback.new(session: test_session)
        resource_feedback.state = "success"
        resource_feedback.feedback_generated_at = "2026-01-10T00:35:19.887286Z"
        resource_feedback.save!

#####

        // Session is built by the OAuth process

        const resource_feedback = new shopify.rest.ResourceFeedback({session: session});
        resource_feedback.state = "success";
        resource_feedback.feedback_generated_at = "2026-01-10T00:35:19.887286Z";
        await resource_feedback.save({
          update: true,
        });

#### response

        HTTP/1.1 202 Accepted{"resource_feedback":{"created_at":"2026-01-09T19:35:20-05:00","updated_at":"2026-01-09T19:35:20-05:00","resource_id":548380009,"resource_type":"Shop","resource_updated_at":null,"messages":[],"feedback_generated_at":"2026-01-09T19:35:19-05:00","state":"success"}}

  * #### Sending an invalid feedback payload returns an error

#####

        curl -d '{"resource_feedback":{"state":"foobar","feedback_generated_at":"2026-01-10T00:35:22.943032Z"}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/resource_feedback.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const resource_feedback = new admin.rest.resources.ResourceFeedback({session: session});

        resource_feedback.state = "foobar";
        resource_feedback.feedback_generated_at = "2026-01-10T00:35:22.943032Z";
        await resource_feedback.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        resource_feedback = ShopifyAPI::ResourceFeedback.new(session: test_session)
        resource_feedback.state = "foobar"
        resource_feedback.feedback_generated_at = "2026-01-10T00:35:22.943032Z"
        resource_feedback.save!

#####

        // Session is built by the OAuth process

        const resource_feedback = new shopify.rest.ResourceFeedback({session: session});
        resource_feedback.state = "foobar";
        resource_feedback.feedback_generated_at = "2026-01-10T00:35:22.943032Z";
        await resource_feedback.save({
          update: true,
        });

#### response

        HTTP/1.1 422 Unprocessable Entity{"errors":{"messages":["State must be one of success and requires_action"]}}

  * #### Sending outdated feedback (previous feedback payload has a greater resource_updated_at value) returns an error

#####

        curl -d '{"resource_feedback":{"state":"success","feedback_generated_at":"2026-01-10T00:35:21.912732Z"}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/resource_feedback.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const resource_feedback = new admin.rest.resources.ResourceFeedback({session: session});

        resource_feedback.state = "success";
        resource_feedback.feedback_generated_at = "2026-01-10T00:35:21.912732Z";
        await resource_feedback.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        resource_feedback = ShopifyAPI::ResourceFeedback.new(session: test_session)
        resource_feedback.state = "success"
        resource_feedback.feedback_generated_at = "2026-01-10T00:35:21.912732Z"
        resource_feedback.save!

#####

        // Session is built by the OAuth process

        const resource_feedback = new shopify.rest.ResourceFeedback({session: session});
        resource_feedback.state = "success";
        resource_feedback.feedback_generated_at = "2026-01-10T00:35:21.912732Z";
        await resource_feedback.save({
          update: true,
        });

#### response

        HTTP/1.1 409 Conflict{"errors":{"messages":["Feedback request not delivered. Feedback request is older than a previously delivered feedback request."]}}


* * *

##

[Anchor to GET request, Receive a list of all ResourceFeedbacks](/docs/api/admin-rest/latest/resources/resourcefeedback#get-resource-feedback)

get

Receive a list of all ResourceFeedbacks

[app](/docs/api/admin-graphql/latest/queries/app)

Returns a list (zero or one) of resource feedback objects.

Important

Note that ids are not returned as part of this request. Records are immutable except when POST replaces them.

**Important:**

Note that ids are not returned as part of this request. Records are immutable except when POST replaces them.

###

[Anchor to Parameters of Receive a list of all ResourceFeedbacks](/docs/api/admin-rest/latest/resources/resourcefeedback#get-resource-feedback-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to get-resource-feedback-examples](/docs/api/admin-rest/latest/resources/resourcefeedback#get-resource-feedback-examples)Examples

Get a list of resource feedback records for a specific shop

Was this section helpful?

YesNo

get

## /admin/api/2026-01/resource_feedback.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/resource_feedback.json" \

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

HTTP/1.1 200 OK

{

"resource_feedback": [

{

"created_at": "2026-01-09T19:35:20-05:00",

"updated_at": "2026-01-09T19:35:20-05:00",

"resource_id": 548380009,

"resource_type": "Shop",

"resource_updated_at": null,

"messages": [

"is not connected. Connect your account to use this sales channel."

],

"feedback_generated_at": "2026-01-09T18:35:20-05:00",

"state": "requires_action"

}

]

}

### examples

  * #### Get a list of resource feedback records for a specific shop

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/resource_feedback.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.ResourceFeedback.all({
          session: session,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::ResourceFeedback.all(
          session: test_session,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.ResourceFeedback.all({
          session: session,
        });

#### response

        HTTP/1.1 200 OK{"resource_feedback":[{"created_at":"2026-01-09T19:35:20-05:00","updated_at":"2026-01-09T19:35:20-05:00","resource_id":548380009,"resource_type":"Shop","resource_updated_at":null,"messages":["is not connected. Connect your account to use this sales channel."],"feedback_generated_at":"2026-01-09T18:35:20-05:00","state":"requires_action"}]}