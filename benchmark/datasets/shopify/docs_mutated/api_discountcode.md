# DiscountCode

*Source: https://shopify.dev/docs/api/admin-rest/2026-01/resources/discountcode*

---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04

2026-01latest

# DiscountCode

Ask assistant

Multiple access scopes needed — refer to each endpoint for access scope requirements.

**Multiple access scopes needed — refer to each endpoint for access scope requirements.:**

Note

We recommend using the GraphQL Admin API to manage discounts. The [Discount types](/api/examples/discounts) available in the GraphQL Admin API are intended to replace the GraphQL Admin `PriceRule` object and REST Admin `PriceRule` and `DiscountCode` resources.

**Note:**

We recommend using the GraphQL Admin API to manage discounts. The [Discount types](/api/examples/discounts) available in the GraphQL Admin API are intended to replace the GraphQL Admin `PriceRule` object and REST Admin `PriceRule` and `DiscountCode` resources.

You can use the PriceRule DiscountCode resource to create discount codes that enable specific discounts to be redeemed. Merchants can distribute discount codes to their customers using a variety of means, such as an email or URL, and customers can apply these codes at checkout.

Each discount code belongs to a price rule, which holds the logic for the discount. For more information, see the [PriceRule](/docs/admin-api/rest/reference/discounts/pricerule) resource.

To create multiple discount codes that use the same price rule logic, use the batch endpoint. For example, you might allow merchants to create a batch of discount codes that belong to the same price rule but are each personalized for a different customer.

Was this section helpful?

YesNo

#

## Endpoints

  * [post/admin/api/latest/price_rules/{price_rule_id}/batch.json](/docs/api/admin-rest/latest/resources/discountcode#post-price-rules-price-rule-id-batch)

Creates a discount code creation job

[discountRedeemCodeBulkAdd](/docs/api/admin-graphql/latest/mutations/discountRedeemCodeBulkAdd?example=creates-a-discount-code-creation-job)

  * [post/admin/api/latest/price_rules/{price_rule_id}/discount_codes.json](/docs/api/admin-rest/latest/resources/discountcode#post-price-rules-price-rule-id-discount-codes)

Creates a discount code

[discountRedeemCodeBulkAdd](/docs/api/admin-graphql/latest/mutations/discountRedeemCodeBulkAdd?example=creates-a-discount-code)

  * [get/admin/api/latest/discount_codes/count.json](/docs/api/admin-rest/latest/resources/discountcode#get-discount-codes-count)

Retrieves a count of discount codes for a shop

[discountCodesCount](/docs/api/admin-graphql/latest/queries/discountCodesCount?example=retrieves-a-count-of-discount-codes-for-a-shop)

  * [get/admin/api/latest/discount_codes/lookup.json?code=SUMMERSALE10OFF](/docs/api/admin-rest/latest/resources/discountcode#get-discount-codes-lookup?code=SUMMERSALE10OFF)

Retrieves the location of a discount code

deprecated

**

deprecated

**

  * [ get/admin/api/latest/price_rules/{price_rule_id}/batch/{batch_id}.json](/docs/api/admin-rest/latest/resources/discountcode#get-price-rules-price-rule-id-batch-batch-id)

Retrieves a discount code creation job

[discountRedeemCodeBulkCreation](/docs/api/admin-graphql/latest/queries/discountRedeemCodeBulkCreation?example=retrieves-a-discount-code-creation-job)

  * [get/admin/api/latest/price_rules/{price_rule_id}/batch/{batch_id}/discount_codes.json](/docs/api/admin-rest/latest/resources/discountcode#get-price-rules-price-rule-id-batch-batch-id-discount-codes)

Retrieves a list of discount codes for a discount code creation job

[discountRedeemCodeBulkCreation](/docs/api/admin-graphql/latest/queries/discountRedeemCodeBulkCreation?example=retrieves-a-list-of-discount-codes-for-a-discount-code-creation-job)

  * [get/admin/api/latest/price_rules/{price_rule_id}/discount_codes.json](/docs/api/admin-rest/latest/resources/discountcode#get-price-rules-price-rule-id-discount-codes)

Retrieves a list of discount codes

[codeDiscountNode](/docs/api/admin-graphql/latest/queries/codeDiscountNode)

  * [get/admin/api/latest/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json](/docs/api/admin-rest/latest/resources/discountcode#get-price-rules-price-rule-id-discount-codes-discount-code-id)

Retrieves a single discount code

[codeDiscountNode](/docs/api/admin-graphql/latest/queries/codeDiscountNode)

  * [put/admin/api/latest/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json](/docs/api/admin-rest/latest/resources/discountcode#put-price-rules-price-rule-id-discount-codes-discount-code-id)

Updates an existing discount code

[discountCodeRedeemCodeBulkDelete](/docs/api/admin-graphql/latest/mutations/discountCodeRedeemCodeBulkDelete)

[discountRedeemCodeBulkAdd](/docs/api/admin-graphql/latest/mutations/discountRedeemCodeBulkAdd)

  * [del/admin/api/latest/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json](/docs/api/admin-rest/latest/resources/discountcode#delete-price-rules-price-rule-id-discount-codes-discount-code-id)

Deletes a discount code

[discountCodeRedeemCodeBulkDelete](/docs/api/admin-graphql/latest/mutations/discountCodeRedeemCodeBulkDelete?example=deletes-a-discount-code)


* * *

[Anchor to ](/docs/api/admin-rest/latest/resources/discountcode#resource-object)

## The DiscountCode resource

[Anchor to ](/docs/api/admin-rest/latest/resources/discountcode#resource-object-properties)

### Properties

* * *

code

->[code](/docs/api/admin-graphql/latest/objects/DiscountRedeemCode#field-DiscountRedeemCode.fields.code)

The case-insensitive discount code that customers use at checkout. (maximum: 255 characters)

Caution

Use the same value for `code` as the `title` property of the associated [price rule](/docs/admin-api/rest/reference/discounts/pricerule/#title-property).

**Caution:**

Use the same value for `code` as the `title` property of the associated [price rule](/docs/admin-api/rest/reference/discounts/pricerule/#title-property).

* * *

created_at

read-only**read-only**

->[createdAt](/docs/api/admin-graphql/latest/objects/DiscountRedeemCodeBulkCreation#field-DiscountRedeemCodeBulkCreation.fields.createdAt)

The date and time ([ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format) when the discount code was created.

* * *

updated_at

read-only**read-only**

The date and time ([ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format) when the discount code was updated.

* * *

id

read-only**read-only**

->[id](/docs/api/admin-graphql/latest/objects/DiscountRedeemCode#field-DiscountRedeemCode.fields.id)

The ID for the discount code.

* * *

price_rule_id

read-only**read-only**

->[id](/docs/api/admin-graphql/latest/objects/DiscountCodeNode#field-DiscountCodeNode.fields.id)

The ID for the price rule that this discount code belongs to.

* * *

usage_count

read-only**read-only**

->[asyncUsageCount](/docs/api/admin-graphql/latest/objects/DiscountRedeemCode#field-DiscountRedeemCode.fields.asyncUsageCount)

The number of times that the discount code has been redeemed.

* * *

errors

read-only**read-only**

->[errors](/docs/api/admin-graphql/latest/objects/DiscountRedeemCodeBulkCreationCode#field-DiscountRedeemCodeBulkCreationCode.fields.errors)

An array of errors that occurred when retrieving a list of discount codes for a discount code creation job.

* * *

Was this section helpful?

YesNo

{}

## The DiscountCode resource

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

{

"code": "SUMMERSALE10OFF",

"created_at": "2017-03-13T16:09:54-04:00",

"updated_at": "2017-03-13T16:09:54-04:00",

"id": 9808080986,

"price_rule_id": 423748927342,

"usage_count": 3,

"errors": {

"code": [

"must be unique. Please try a different code."

]

}

}

* * *

##

[Anchor to POST request, Creates a discount code creation job](/docs/api/admin-rest/latest/resources/discountcode#post-price-rules-price-rule-id-batch)

post

Creates a discount code creation job

[discountRedeemCodeBulkAdd](/docs/api/admin-graphql/latest/mutations/discountRedeemCodeBulkAdd?example=creates-a-discount-code-creation-job)

Creates a discount code creation job.

The batch endpoint can be used to asynchronously create up to 100 discount codes in a single request. It enqueues and returns a `discount_code_creation` object that can be monitored for completion. You can enqueue a single creation job per a shop and you can't enqueue more until the job completes.

The `price_rule_id` path parameter is the ID of the price rule that the discount code will belong to. This is required because each discount code must belong to a price rule.

Response fields that are specific to the batch endpoint include:

  * `status`: The state of the discount code creation job. Possible values are:
    * `queued`: The job is acknowledged, but not started.
    * `running`: The job is in process.
    * `completed`: The job has finished.
  * `codes_count`: The number of discount codes to create.
  * `imported_count`: The number of discount codes created successfully.
  * `failed_count`: The number of discount codes that were not created successfully. Unsuccessful attempts will retry up to three times.
  * `logs`: A report that specifies when no discount codes were created because the provided data was invalid. Example responses:
    * "Price rule target selection can't be blank"
    * "Price rule allocation method can't be blank"


###

[Anchor to Parameters of Creates a discount code creation job](/docs/api/admin-rest/latest/resources/discountcode#post-price-rules-price-rule-id-batch-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

price_rule_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to post-price-rules-price-rule-id-batch-examples](/docs/api/admin-rest/latest/resources/discountcode#post-price-rules-price-rule-id-batch-examples)Examples

Create a discount code creation job

Path parameters

price_rule_id=507328175

string**string**

required**required**

Was this section helpful?

YesNo

post

## /admin/api/2026-01/price_rules/507328175/batch.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{"discount_codes":[{"code":"SUMMER1"},{"code":"SUMMER2"},{"code":"SUMMER3"}]}' \

-X POST "https://your-development-store.myshopify.com/admin/api/2026-01/price_rules/507328175/batch.json" \

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

HTTP/1.1 201 Created

{

"discount_code_creation": {

"id": 989355120,

"price_rule_id": 507328175,

"started_at": null,

"completed_at": null,

"created_at": "2026-01-09T22:37:05-05:00",

"updated_at": "2026-01-09T22:37:05-05:00",

"status": "queued",

"codes_count": 3,

"imported_count": 0,

"failed_count": 0,

"logs": []

}

}

### examples

  * #### Create a discount code creation job

#####

        curl -d '{"discount_codes":[{"code":"SUMMER1"},{"code":"SUMMER2"},{"code":"SUMMER3"}]}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/price_rules/507328175/batch.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const discount_code = new admin.rest.resources.DiscountCode({session: session});

        discount_code.price_rule_id = 507328175;
        await discount_code.batch({
          body: {"discount_codes": [{"code": "SUMMER1"}, {"code": "SUMMER2"}, {"code": "SUMMER3"}]},
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        discount_code = ShopifyAPI::DiscountCode.new(session: test_session)
        discount_code.price_rule_id = 507328175
        discount_code.batch(
          session: test_session,
          body: {"discount_codes" => [{"code" => "SUMMER1"}, {"code" => "SUMMER2"}, {"code" => "SUMMER3"}]},
        )

#####

        // Session is built by the OAuth process

        const discount_code = new shopify.rest.DiscountCode({session: session});
        discount_code.price_rule_id = 507328175;
        await discount_code.batch({
          body: {"discount_codes": [{"code": "SUMMER1"}, {"code": "SUMMER2"}, {"code": "SUMMER3"}]},
        });

#### response

        HTTP/1.1 201 Created{"discount_code_creation":{"id":989355120,"price_rule_id":507328175,"started_at":null,"completed_at":null,"created_at":"2026-01-09T22:37:05-05:00","updated_at":"2026-01-09T22:37:05-05:00","status":"queued","codes_count":3,"imported_count":0,"failed_count":0,"logs":[]}}


* * *

##

[Anchor to POST request, Creates a discount code](/docs/api/admin-rest/latest/resources/discountcode#post-price-rules-price-rule-id-discount-codes)

post

Creates a discount code

[discountRedeemCodeBulkAdd](/docs/api/admin-graphql/latest/mutations/discountRedeemCodeBulkAdd?example=creates-a-discount-code)

Requires `price_rules` access scope.

**Requires `price_rules` access scope.:**

Creates a discount code.

The `price_rule_id` path parameter is the ID of the price rule that the discount code will belong to. This is required because each discount code must belong to a price rule.

###

[Anchor to Parameters of Creates a discount code](/docs/api/admin-rest/latest/resources/discountcode#post-price-rules-price-rule-id-discount-codes-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

price_rule_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to post-price-rules-price-rule-id-discount-codes-examples](/docs/api/admin-rest/latest/resources/discountcode#post-price-rules-price-rule-id-discount-codes-examples)Examples

Create a discount code

Path parameters

price_rule_id=507328175

string**string**

required**required**

Request body

discount_code

Discount_code resource**Discount_code resource**

Show discount_code properties

discount_code.code:"SUMMERSALE10OFF"

->[code](/docs/api/admin-graphql/latest/input-objects/DiscountRedeemCodeInput#fields-code)

The case-insensitive discount code that customers use at checkout. (maximum: 255 characters)

Caution

Use the same value for `code` as the `title` property of the associated [price rule](/docs/admin-api/rest/reference/discounts/pricerule/#title-property).

**Caution:**

Use the same value for `code` as the `title` property of the associated [price rule](/docs/admin-api/rest/reference/discounts/pricerule/#title-property).

Was this section helpful?

YesNo

post

## /admin/api/2026-01/price_rules/507328175/discount_codes.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{"discount_code":{"code":"SUMMERSALE10OFF"}}' \

-X POST "https://your-development-store.myshopify.com/admin/api/2026-01/price_rules/507328175/discount_codes.json" \

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

HTTP/1.1 201 Created

{

"discount_code": {

"id": 1057371197,

"price_rule_id": 507328175,

"code": "SUMMERSALE10OFF",

"usage_count": 0,

"created_at": "2026-01-09T22:37:00-05:00",

"updated_at": "2026-01-09T22:37:00-05:00"

}

}

### examples

  * #### Create a discount code

#####

        curl -d '{"discount_code":{"code":"SUMMERSALE10OFF"}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/price_rules/507328175/discount_codes.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const discount_code = new admin.rest.resources.DiscountCode({session: session});

        discount_code.price_rule_id = 507328175;
        discount_code.code = "SUMMERSALE10OFF";
        await discount_code.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        discount_code = ShopifyAPI::DiscountCode.new(session: test_session)
        discount_code.price_rule_id = 507328175
        discount_code.code = "SUMMERSALE10OFF"
        discount_code.save!

#####

        // Session is built by the OAuth process

        const discount_code = new shopify.rest.DiscountCode({session: session});
        discount_code.price_rule_id = 507328175;
        discount_code.code = "SUMMERSALE10OFF";
        await discount_code.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"discount_code":{"id":1057371197,"price_rule_id":507328175,"code":"SUMMERSALE10OFF","usage_count":0,"created_at":"2026-01-09T22:37:00-05:00","updated_at":"2026-01-09T22:37:00-05:00"}}


* * *

##

[Anchor to GET request, Retrieves a count of discount codes for a shop](/docs/api/admin-rest/latest/resources/discountcode#get-discount-codes-count)

get

Retrieves a count of discount codes for a shop

[discountCodesCount](/docs/api/admin-graphql/latest/queries/discountCodesCount?example=retrieves-a-count-of-discount-codes-for-a-shop)

Requires `price_rules` access scope.

**Requires `price_rules` access scope.:**

Retrieves a count of discount codes for a shop

###

[Anchor to Parameters of Retrieves a count of discount codes for a shop](/docs/api/admin-rest/latest/resources/discountcode#get-discount-codes-count-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

times_used

Show discount codes with times used.

* * *

times_used_max

Show discount codes used greater than or equal to this value.

* * *

times_used_min

Show discount codes used less than or equal to this value.

* * *

Was this section helpful?

YesNo

###

[Anchor to get-discount-codes-count-examples](/docs/api/admin-rest/latest/resources/discountcode#get-discount-codes-count-examples)Examples

Retrieve a count of discount codes for a shop tag:elasticsearch:true

Was this section helpful?

YesNo

get

## /admin/api/2026-01/discount_codes/count.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/discount_codes/count.json" \

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

"count": 2

}

### examples

  * #### Retrieve a count of discount codes for a shop tag:elasticsearch:true

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/discount_codes/count.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.DiscountCode.count({
          session: session,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::DiscountCode.count(
          session: test_session,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.DiscountCode.count({
          session: session,
        });

#### response

        HTTP/1.1 200 OK{"count":2}


* * *

##

[Anchor to GET request, Retrieves the location of a discount code](/docs/api/admin-rest/latest/resources/discountcode#get-discount-codes-lookup?code=SUMMERSALE10OFF)

get

Retrieves the location of a discount code

deprecated**deprecated**

Requires `price_rules` access scope.

**Requires `price_rules` access scope.:**

Retrieves the location of a discount code.

The discount code's location is returned in the location header, not in the DiscountCode object itself. Depending on your HTTP client, the location of the discount code might follow the location header automatically.

###

[Anchor to Parameters of Retrieves the location of a discount code](/docs/api/admin-rest/latest/resources/discountcode#get-discount-codes-lookup?code=SUMMERSALE10OFF-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

code

required**required**

≤ 100**≤ 100**

Retrieves the location of a discount code by code name.

* * *

Was this section helpful?

YesNo

###

[Anchor to get-discount-codes-lookup?code=SUMMERSALE10OFF-examples](/docs/api/admin-rest/latest/resources/discountcode#get-discount-codes-lookup?code=SUMMERSALE10OFF-examples)Examples

Search for a discount code

Query parameters

code=SUMMERSALE10OFF

required**required**

≤ 100**≤ 100**

Retrieves the location of a discount code by code name.

Was this section helpful?

YesNo

get

## /admin/api/2026-01/discount_codes/lookup.json?code=SUMMERSALE10OFF

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/discount_codes/lookup.json?code=SUMMERSALE10OFF" \

-H "X-Shopify-Access-Token: {access_token}"

{}

## Response

JSON

9

1

HTTP/1.1 303 See Other

### examples

  * #### Search for a discount code

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/discount_codes/lookup.json?code=SUMMERSALE10OFF" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.DiscountCode.lookup({
          session: session,
          code: "SUMMERSALE10OFF",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::DiscountCode.lookup(
          session: test_session,
          code: "SUMMERSALE10OFF",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.DiscountCode.lookup({
          session: session,
          code: "SUMMERSALE10OFF",
        });

#### response

        HTTP/1.1 303 See Other


* * *

##

[Anchor to GET request, Retrieves a discount code creation job](/docs/api/admin-rest/latest/resources/discountcode#get-price-rules-price-rule-id-batch-batch-id)

get

Retrieves a discount code creation job

[discountRedeemCodeBulkCreation](/docs/api/admin-graphql/latest/queries/discountRedeemCodeBulkCreation?example=retrieves-a-discount-code-creation-job)

Retrieves a discount code creation job

The `price_rule_id` path parameter is the ID of the price rule that the discount code creation job was ran for. This is required because each discount code creation job is associated to a price rule.

The `batch_id` path parameter is the ID of the discount code creation job for the associated price rule.

###

[Anchor to Parameters of Retrieves a discount code creation job](/docs/api/admin-rest/latest/resources/discountcode#get-price-rules-price-rule-id-batch-batch-id-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

batch_id

string**string**

required**required**

* * *

price_rule_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to get-price-rules-price-rule-id-batch-batch-id-examples](/docs/api/admin-rest/latest/resources/discountcode#get-price-rules-price-rule-id-batch-batch-id-examples)Examples

Retrieve a discount code creation job

Was this section helpful?

YesNo

get

## /admin/api/2026-01/price_rules/507328175/batch/173232803.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/price_rules/507328175/batch/173232803.json" \

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

HTTP/1.1 200 OK

{

"discount_code_creation": {

"id": 173232803,

"price_rule_id": 507328175,

"started_at": null,

"completed_at": null,

"created_at": "2026-01-09T22:32:40-05:00",

"updated_at": "2026-01-09T22:32:40-05:00",

"status": "queued",

"codes_count": 3,

"imported_count": 0,

"failed_count": 0,

"logs": []

}

}

### examples

  * #### Retrieve a discount code creation job

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/price_rules/507328175/batch/173232803.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.DiscountCode.get_all({
          session: session,
          price_rule_id: 507328175,
          batch_id: 173232803,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::DiscountCode.get_all(
          session: test_session,
          price_rule_id: 507328175,
          batch_id: 173232803,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.DiscountCode.get_all({
          session: session,
          price_rule_id: 507328175,
          batch_id: 173232803,
        });

#### response

        HTTP/1.1 200 OK{"discount_code_creation":{"id":173232803,"price_rule_id":507328175,"started_at":null,"completed_at":null,"created_at":"2026-01-09T22:32:40-05:00","updated_at":"2026-01-09T22:32:40-05:00","status":"queued","codes_count":3,"imported_count":0,"failed_count":0,"logs":[]}}


* * *

##

[Anchor to GET request, Retrieves a list of discount codes for a discount code creation job](/docs/api/admin-rest/latest/resources/discountcode#get-price-rules-price-rule-id-batch-batch-id-discount-codes)

get

Retrieves a list of discount codes for a discount code creation job

[discountRedeemCodeBulkCreation](/docs/api/admin-graphql/latest/queries/discountRedeemCodeBulkCreation?example=retrieves-a-list-of-discount-codes-for-a-discount-code-creation-job)

Retrieves a list of discount codes for a discount code creation job.

The `price_rule_id` path parameter is the ID of the price rule that the discount code creation job was ran for. This is required because each discount code creation job is associated to a price rule.

The `batch_id` path parameter is the ID of the discount code creation job for the associated price rule.

Discount codes that have been successfully created include a populated `id` field. Discount codes that encountered errors during the creation process include a populated `errors` field.

###

[Anchor to Parameters of Retrieves a list of discount codes for a discount code creation job](/docs/api/admin-rest/latest/resources/discountcode#get-price-rules-price-rule-id-batch-batch-id-discount-codes-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

batch_id

string**string**

required**required**

* * *

price_rule_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to get-price-rules-price-rule-id-batch-batch-id-discount-codes-examples](/docs/api/admin-rest/latest/resources/discountcode#get-price-rules-price-rule-id-batch-batch-id-discount-codes-examples)Examples

Retrieve a list of discount codes for a discount code creation job

Was this section helpful?

YesNo

get

## /admin/api/2026-01/price_rules/507328175/batch/173232803/discount_codes.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/price_rules/507328175/batch/173232803/discount_codes.json" \

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

HTTP/1.1 200 OK

{

"discount_codes": [

{

"id": null,

"code": "foo",

"errors": {}

},

{

"id": null,

"code": "",

"errors": {}

},

{

"id": null,

"code": "bar",

"errors": {}

}

]

}

### examples

  * #### Retrieve a list of discount codes for a discount code creation job

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/price_rules/507328175/batch/173232803/discount_codes.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.DiscountCode.all({
          session: session,
          price_rule_id: 507328175,
          batch_id: 173232803,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::DiscountCode.all(
          session: test_session,
          price_rule_id: 507328175,
          batch_id: 173232803,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.DiscountCode.all({
          session: session,
          price_rule_id: 507328175,
          batch_id: 173232803,
        });

#### response

        HTTP/1.1 200 OK{"discount_codes":[{"id":null,"code":"foo","errors":{}},{"id":null,"code":"","errors":{}},{"id":null,"code":"bar","errors":{}}]}


* * *

##

[Anchor to GET request, Retrieves a list of discount codes](/docs/api/admin-rest/latest/resources/discountcode#get-price-rules-price-rule-id-discount-codes)

get

Retrieves a list of discount codes

[codeDiscountNode](/docs/api/admin-graphql/latest/queries/codeDiscountNode)

Requires `price_rules` access scope.

**Requires `price_rules` access scope.:**

Retrieve a list of discount codes. **Note:** This endpoint implements pagination by using links that are provided in the response header. To learn more, refer to [Make paginated requests to the REST Admin API](/api/usage/pagination-rest).

The `price_rule_id` path parameter is the ID of the price rule that the discount codes belongs to.

###

[Anchor to Parameters of Retrieves a list of discount codes](/docs/api/admin-rest/latest/resources/discountcode#get-price-rules-price-rule-id-discount-codes-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

price_rule_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to get-price-rules-price-rule-id-discount-codes-examples](/docs/api/admin-rest/latest/resources/discountcode#get-price-rules-price-rule-id-discount-codes-examples)Examples

Retrieve a list of all discount codes

Path parameters

price_rule_id=507328175

string**string**

required**required**

Was this section helpful?

YesNo

get

## /admin/api/2026-01/price_rules/507328175/discount_codes.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/price_rules/507328175/discount_codes.json" \

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

HTTP/1.1 200 OK

{

"discount_codes": [

{

"id": 507328175,

"price_rule_id": 507328175,

"code": "SUMMERSALE10OFF",

"usage_count": 0,

"created_at": "2026-01-09T22:32:40-05:00",

"updated_at": "2026-01-09T22:32:40-05:00"

}

]

}

### examples

  * #### Retrieve a list of all discount codes

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/price_rules/507328175/discount_codes.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.DiscountCode.all({
          session: session,
          price_rule_id: 507328175,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::DiscountCode.all(
          session: test_session,
          price_rule_id: 507328175,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.DiscountCode.all({
          session: session,
          price_rule_id: 507328175,
        });

#### response

        HTTP/1.1 200 OK{"discount_codes":[{"id":507328175,"price_rule_id":507328175,"code":"SUMMERSALE10OFF","usage_count":0,"created_at":"2026-01-09T22:32:40-05:00","updated_at":"2026-01-09T22:32:40-05:00"}]}


* * *

##

[Anchor to GET request, Retrieves a single discount code](/docs/api/admin-rest/latest/resources/discountcode#get-price-rules-price-rule-id-discount-codes-discount-code-id)

get

Retrieves a single discount code

[codeDiscountNode](/docs/api/admin-graphql/latest/queries/codeDiscountNode)

Requires `price_rules` access scope.

**Requires `price_rules` access scope.:**

Retrieves a single discount code.

The `price_rule_id` path parameter is the ID of the price rule that the discount code belongs to. This is required because each discount code must belong to a price rule.

The `discount_code_id` path parameter is the ID of the discount code to retrieve for the associated price rule.

###

[Anchor to Parameters of Retrieves a single discount code](/docs/api/admin-rest/latest/resources/discountcode#get-price-rules-price-rule-id-discount-codes-discount-code-id-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

discount_code_id

string**string**

required**required**

* * *

price_rule_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to get-price-rules-price-rule-id-discount-codes-discount-code-id-examples](/docs/api/admin-rest/latest/resources/discountcode#get-price-rules-price-rule-id-discount-codes-discount-code-id-examples)Examples

Retrieve a single discount code

Was this section helpful?

YesNo

get

## /admin/api/2026-01/price_rules/507328175/discount_codes/507328175.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/price_rules/507328175/discount_codes/507328175.json" \

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

HTTP/1.1 200 OK

{

"discount_code": {

"id": 507328175,

"price_rule_id": 507328175,

"code": "SUMMERSALE10OFF",

"usage_count": 0,

"created_at": "2026-01-09T22:32:40-05:00",

"updated_at": "2026-01-09T22:32:40-05:00"

}

}

### examples

  * #### Retrieve a single discount code

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/price_rules/507328175/discount_codes/507328175.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.DiscountCode.find({
          session: session,
          price_rule_id: 507328175,
          id: 507328175,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::DiscountCode.find(
          session: test_session,
          price_rule_id: 507328175,
          id: 507328175,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.DiscountCode.find({
          session: session,
          price_rule_id: 507328175,
          id: 507328175,
        });

#### response

        HTTP/1.1 200 OK{"discount_code":{"id":507328175,"price_rule_id":507328175,"code":"SUMMERSALE10OFF","usage_count":0,"created_at":"2026-01-09T22:32:40-05:00","updated_at":"2026-01-09T22:32:40-05:00"}}


* * *

##

[Anchor to PUT request, Updates an existing discount code](/docs/api/admin-rest/latest/resources/discountcode#put-price-rules-price-rule-id-discount-codes-discount-code-id)

put

Updates an existing discount code

[discountCodeRedeemCodeBulkDelete](/docs/api/admin-graphql/latest/mutations/discountCodeRedeemCodeBulkDelete)

[discountRedeemCodeBulkAdd](/docs/api/admin-graphql/latest/mutations/discountRedeemCodeBulkAdd)

Requires `price_rules` access scope.

**Requires `price_rules` access scope.:**

Updates an existing discount code.

The `price_rule_id` path parameter is the ID of the price rule that the discount code belongs to. This is required because each discount code must belong to a price rule.

The `discount_code_id` path parameter is the ID of the discount code to update for the associated price rule.

###

[Anchor to Parameters of Updates an existing discount code](/docs/api/admin-rest/latest/resources/discountcode#put-price-rules-price-rule-id-discount-codes-discount-code-id-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

discount_code_id

string**string**

required**required**

* * *

price_rule_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to put-price-rules-price-rule-id-discount-codes-discount-code-id-examples](/docs/api/admin-rest/latest/resources/discountcode#put-price-rules-price-rule-id-discount-codes-discount-code-id-examples)Examples

Update the code for a discount

Request body

discount_code

Discount_code resource**Discount_code resource**

Show discount_code properties

discount_code.id:507328175

read-only**read-only**

The ID for the discount code.

discount_code.code:"WINTERSALE20OFF"

The case-insensitive discount code that customers use at checkout. (maximum: 255 characters)

Caution

Use the same value for `code` as the `title` property of the associated [price rule](/docs/admin-api/rest/reference/discounts/pricerule/#title-property).

**Caution:**

Use the same value for `code` as the `title` property of the associated [price rule](/docs/admin-api/rest/reference/discounts/pricerule/#title-property).

Was this section helpful?

YesNo

put

## /admin/api/2026-01/price_rules/507328175/discount_codes/507328175.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{"discount_code":{"id":507328175,"code":"WINTERSALE20OFF"}}' \

-X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/price_rules/507328175/discount_codes/507328175.json" \

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

HTTP/1.1 200 OK

{

"discount_code": {

"id": 507328175,

"price_rule_id": 507328175,

"code": "WINTERSALE20OFF",

"usage_count": 0,

"created_at": "2026-01-09T22:32:40-05:00",

"updated_at": "2026-01-09T22:36:53-05:00"

}

}

### examples

  * #### Update the code for a discount

#####

        curl -d '{"discount_code":{"id":507328175,"code":"WINTERSALE20OFF"}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/price_rules/507328175/discount_codes/507328175.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const discount_code = new admin.rest.resources.DiscountCode({session: session});

        discount_code.price_rule_id = 507328175;
        discount_code.id = 507328175;
        discount_code.code = "WINTERSALE20OFF";
        await discount_code.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        discount_code = ShopifyAPI::DiscountCode.new(session: test_session)
        discount_code.price_rule_id = 507328175
        discount_code.id = 507328175
        discount_code.code = "WINTERSALE20OFF"
        discount_code.save!

#####

        // Session is built by the OAuth process

        const discount_code = new shopify.rest.DiscountCode({session: session});
        discount_code.price_rule_id = 507328175;
        discount_code.id = 507328175;
        discount_code.code = "WINTERSALE20OFF";
        await discount_code.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"discount_code":{"id":507328175,"price_rule_id":507328175,"code":"WINTERSALE20OFF","usage_count":0,"created_at":"2026-01-09T22:32:40-05:00","updated_at":"2026-01-09T22:36:53-05:00"}}


* * *

##

[Anchor to DELETE request, Deletes a discount code](/docs/api/admin-rest/latest/resources/discountcode#delete-price-rules-price-rule-id-discount-codes-discount-code-id)

del

Deletes a discount code

[discountCodeRedeemCodeBulkDelete](/docs/api/admin-graphql/latest/mutations/discountCodeRedeemCodeBulkDelete?example=deletes-a-discount-code)

Requires `price_rules` access scope.

**Requires `price_rules` access scope.:**

Deletes a discount code.

The `price_rule_id` path parameter is the ID of the price rule that the discount code belongs to. This is required because each discount code must belong to a price rule.

The `discount_code_id` path parameter is the ID of the discount code to delete for the associated price rule.

###

[Anchor to Parameters of Deletes a discount code](/docs/api/admin-rest/latest/resources/discountcode#delete-price-rules-price-rule-id-discount-codes-discount-code-id-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

discount_code_id

string**string**

required**required**

* * *

price_rule_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to delete-price-rules-price-rule-id-discount-codes-discount-code-id-examples](/docs/api/admin-rest/latest/resources/discountcode#delete-price-rules-price-rule-id-discount-codes-discount-code-id-examples)Examples

Delete a discount code

Was this section helpful?

YesNo

del

## /admin/api/2026-01/price_rules/507328175/discount_codes/507328175.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X DELETE "https://your-development-store.myshopify.com/admin/api/2026-01/price_rules/507328175/discount_codes/507328175.json" \

-H "X-Shopify-Access-Token: {access_token}"

{}

## Response

JSON

9

1

HTTP/1.1 204 No Content

### examples

  * #### Delete a discount code

#####

        curl -X DELETE "https://your-development-store.myshopify.com/admin/api/2026-01/price_rules/507328175/discount_codes/507328175.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.DiscountCode.delete({
          session: session,
          price_rule_id: 507328175,
          id: 507328175,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::DiscountCode.delete(
          session: test_session,
          price_rule_id: 507328175,
          id: 507328175,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.DiscountCode.delete({
          session: session,
          price_rule_id: 507328175,
          id: 507328175,
        });

#### response

        HTTP/1.1 204 No Content