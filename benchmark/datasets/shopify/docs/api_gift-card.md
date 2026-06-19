# Gift Card

*Source: https://shopify.dev/docs/api/admin-rest/2026-01/resources/gift-card*

---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04

2026-01latest

# Gift Card

Ask assistant

Requires `gift_cards` access scope.

**Requires `gift_cards` access scope.:**

Note

You need to contact Shopify Support to request the `write_gift_cards` and `read_gift_cards` [access scopes](/docs/admin-api/access-scopes).

**Note:**

You need to contact Shopify Support to request the `write_gift_cards` and `read_gift_cards` [access scopes](/docs/admin-api/access-scopes).

A gift card is an alternative payment method. Each gift card has a unique code that is entered during checkout. Its balance can be redeemed over multiple checkouts. Optionally, a gift card can assigned to a specific customer. Gift card codes cannot be retrieved after they're created—only the last four characters can be retrieved.

You can use the GiftCard resource to create, retrieve, and update gift cards for a store. After a gift card is created, only the expiry date, note, and template suffix can be updated.

Note

You can't delete gift cards, but you can disable them. You can't enable gift cards that were previously disabled.

**Note:**

You can't delete gift cards, but you can disable them. You can't enable gift cards that were previously disabled.

Was this section helpful?

YesNo

#

## Endpoints

  * [post/admin/api/latest/gift_cards.json](/docs/api/admin-rest/latest/resources/gift-card#post-gift-cards)

Creates a gift card

[giftCardCreate](/docs/api/admin-graphql/latest/mutations/giftCardCreate?example=creates-a-gift-card)

  * [post/admin/api/latest/gift_cards/{gift_card_id}/disable.json](/docs/api/admin-rest/latest/resources/gift-card#post-gift-cards-gift-card-id-disable)

Disables a gift card

[giftCardDeactivate](/docs/api/admin-graphql/latest/mutations/giftCardDeactivate?example=disables-a-gift-card)

  * [get/admin/api/latest/gift_cards.json?status=enabled](/docs/api/admin-rest/latest/resources/gift-card#get-gift-cards?status=enabled)

Retrieves a list of gift cards

[giftCards](/docs/api/admin-graphql/latest/queries/giftCards?example=retrieves-a-list-of-gift-cards)

  * [get/admin/api/latest/gift_cards/{gift_card_id}.json](/docs/api/admin-rest/latest/resources/gift-card#get-gift-cards-gift-card-id)

Retrieves a single gift card

[giftCard](/docs/api/admin-graphql/latest/queries/giftCard?example=retrieves-a-single-gift-card)

  * [get/admin/api/latest/gift_cards/count.json](/docs/api/admin-rest/latest/resources/gift-card#get-gift-cards-count)

Retrieves a count of gift cards

[giftCardsCount](/docs/api/admin-graphql/latest/queries/giftCardsCount?example=retrieves-a-count-of-gift-cards)

  * [get/admin/api/latest/gift_cards/search.json?query=last_characters:mnop](/docs/api/admin-rest/latest/resources/gift-card#get-gift-cards-search?query=last-characters:mnop)

Searches for gift cards

[giftCards](/docs/api/admin-graphql/latest/queries/giftCards?example=searches-for-gift-cards)

  * [put/admin/api/latest/gift_cards/{gift_card_id}.json](/docs/api/admin-rest/latest/resources/gift-card#put-gift-cards-gift-card-id)

Updates an existing gift card

[giftCardUpdate](/docs/api/admin-graphql/latest/mutations/giftCardUpdate)


* * *

[Anchor to ](/docs/api/admin-rest/latest/resources/gift-card#resource-object)

## The Gift Card resource

[Anchor to ](/docs/api/admin-rest/latest/resources/gift-card#resource-object-properties)

### Properties

* * *

api_client_id

deprecated**deprecated**

The ID of the client that issued the gift card.

* * *

balance

string**string**

->[balance](/docs/api/admin-graphql/latest/objects/GiftCard#field-GiftCard.fields.balance)

The balance of the gift card.

* * *

code

The gift card code, which is a string of alphanumeric characters. For security reasons, this is available only upon creation of the gift card. (minimum: 8 characters, maximum: 20 characters)

* * *

created_at

->[createdAt](/docs/api/admin-graphql/latest/objects/GiftCard#field-GiftCard.fields.createdAt)

The date and time ([ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format) when the gift card was created.

* * *

currency

string**string**

->[balance](/docs/api/admin-graphql/latest/objects/GiftCard#field-GiftCard.fields.balance)

The currency of the gift card.

* * *

customer_id

->[customer](/docs/api/admin-graphql/latest/objects/GiftCard#field-GiftCard.fields.customer)

The ID of the customer associated with this gift card.

* * *

disabled_at

->[deactivatedAt](/docs/api/admin-graphql/latest/objects/GiftCard#field-GiftCard.fields.deactivatedAt)

The date and time ([ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format) when the gift card was disabled.

* * *

expires_on

->[expiresOn](/docs/api/admin-graphql/latest/objects/GiftCard#field-GiftCard.fields.expiresOn)

The date (`YYYY-MM-DD` format) when the gift card expires. Returns `null` if the gift card doesn't have an expiration date.

* * *

id

->[id](/docs/api/admin-graphql/latest/objects/GiftCard#field-GiftCard.fields.id)

The ID of the gift card.

* * *

initial_value

string**string**

->[initialValue](/docs/api/admin-graphql/latest/objects/GiftCard#field-GiftCard.fields.initialValue)

The initial value of the gift card when it was created.

* * *

last_characters

->[lastCharacters](/docs/api/admin-graphql/latest/objects/GiftCard#field-GiftCard.fields.lastCharacters)

The last four characters of the gift card code. Because gift cards are alternative payment methods, the full code cannot be retrieved.

* * *

line_item_id

deprecated**deprecated**

The ID of the line item that initiated the creation of this gift card, if it was created by an order.

* * *

Show 5 hidden fields

Was this section helpful?

YesNo

{}

## The Gift Card resource

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

{

"api_client_id": 431223487,

"balance": "80.17",

"code": "1234 4567 8901 2ABC",

"created_at": "2008-12-31T19:00:00-05:00",

"currency": "CAD",

"customer_id": 368407052327,

"disabled_at": "2009-01-31T19:00:00-05:00",

"expires_on": "2020-01-31",

"id": 989034056,

"initial_value": "100.00",

"last_characters": "2ABC",

"line_item_id": 241253183,

"note": "A note",

"order_id": 241253183,

"template_suffix": "birthday",

"user_id": 876543210,

"updated_at": "2009-01-31T19:00:00-05:00"

}

* * *

##

[Anchor to POST request, Creates a gift card](/docs/api/admin-rest/latest/resources/gift-card#post-gift-cards)

post

Creates a gift card

[giftCardCreate](/docs/api/admin-graphql/latest/mutations/giftCardCreate?example=creates-a-gift-card)

Creates a gift card.

There are additional optional parameters that can be specified in the body of the request when creating a gift card:

###

[Anchor to Parameters of Creates a gift card](/docs/api/admin-rest/latest/resources/gift-card#post-gift-cards-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

customer_id

The ID of the customer that purchased the gift card.

* * *

recipient_id

The ID of the intended recipient of the gift card. This property should be used if the recipientis different from the purchaser. The customer with this ID must have an email address.

* * *

Was this section helpful?

YesNo

###

[Anchor to post-gift-cards-examples](/docs/api/admin-rest/latest/resources/gift-card#post-gift-cards-examples)Examples

Create a gift card with a custom code

Request body

gift_card

Gift_card resource**Gift_card resource**

Show gift_card properties

gift_card.note:"This is a note"

->[note](/docs/api/admin-graphql/latest/input-objects/GiftCardCreateInput#fields-note)

An optional note that a merchant can attach to the gift card that isn't visible to customers.

gift_card.initial_value:"100.00"

string**string**

->[initialValue](/docs/api/admin-graphql/latest/input-objects/GiftCardCreateInput#fields-initialValue)

The initial value of the gift card when it was created.

gift_card.code:"ABCD EFGH IJKL MNOP"

The gift card code, which is a string of alphanumeric characters. For security reasons, this is available only upon creation of the gift card. (minimum: 8 characters, maximum: 20 characters)

gift_card.template_suffix:"gift_cards.birthday.liquid"

->[templateSuffix](/docs/api/admin-graphql/latest/input-objects/GiftCardCreateInput#fields-templateSuffix)

The suffix of the Liquid template that's used to render the gift card online. For example, if the value is `birthday`, then the gift card is rendered using the template `gift_card.birthday.liquid`. When the value is `null`, the default `gift_card.liquid` template is used.

Create a gift card with an automatically generated code

Request body

gift_card

Gift_card resource**Gift_card resource**

Show gift_card properties

gift_card.initial_value:"25.00"

string**string**

->[initialValue](/docs/api/admin-graphql/latest/input-objects/GiftCardCreateInput#fields-initialValue)

The initial value of the gift card when it was created.

Create a scheduled gift card with a recipient and a message

Request body

gift_card

Gift_card resource**Gift_card resource**

Show gift_card properties

gift_card.initial_value:"100.00"

string**string**

->[initialValue](/docs/api/admin-graphql/latest/input-objects/GiftCardCreateInput#fields-initialValue)

The initial value of the gift card when it was created.

Was this section helpful?

YesNo

post

## /admin/api/2026-01/gift_cards.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{"gift_card":{"note":"This is a note","initial_value":"100.00","code":"ABCD EFGH IJKL MNOP","template_suffix":"gift_cards.birthday.liquid"}}' \

-X POST "https://your-development-store.myshopify.com/admin/api/2026-01/gift_cards.json" \

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

HTTP/1.1 201 Created

{

"gift_card": {

"id": 1063936327,

"balance": "100.00",

"created_at": "2026-01-09T19:00:07-05:00",

"updated_at": "2026-01-09T19:00:07-05:00",

"currency": "USD",

"initial_value": "100.00",

"disabled_at": null,

"line_item_id": null,

"api_client_id": 755357713,

"user_id": null,

"customer_id": null,

"note": "This is a note",

"expires_on": null,

"template_suffix": "gift_cards.birthday.liquid",

"last_characters": "mnop",

"order_id": null,

"code": "abcdefghijklmnop"

}

}

### examples

  * #### Create a gift card with a custom code

#####

        curl -d '{"gift_card":{"note":"This is a note","initial_value":"100.00","code":"ABCD EFGH IJKL MNOP","template_suffix":"gift_cards.birthday.liquid"}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/gift_cards.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const gift_card = new admin.rest.resources.GiftCard({session: session});

        gift_card.note = "This is a note";
        gift_card.initial_value = "100.00";
        gift_card.code = "ABCD EFGH IJKL MNOP";
        gift_card.template_suffix = "gift_cards.birthday.liquid";
        await gift_card.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        gift_card = ShopifyAPI::GiftCard.new(session: test_session)
        gift_card.note = "This is a note"
        gift_card.initial_value = "100.00"
        gift_card.code = "ABCD EFGH IJKL MNOP"
        gift_card.template_suffix = "gift_cards.birthday.liquid"
        gift_card.save!

#####

        // Session is built by the OAuth process

        const gift_card = new shopify.rest.GiftCard({session: session});
        gift_card.note = "This is a note";
        gift_card.initial_value = "100.00";
        gift_card.code = "ABCD EFGH IJKL MNOP";
        gift_card.template_suffix = "gift_cards.birthday.liquid";
        await gift_card.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"gift_card":{"id":1063936327,"balance":"100.00","created_at":"2026-01-09T19:00:07-05:00","updated_at":"2026-01-09T19:00:07-05:00","currency":"USD","initial_value":"100.00","disabled_at":null,"line_item_id":null,"api_client_id":755357713,"user_id":null,"customer_id":null,"note":"This is a note","expires_on":null,"template_suffix":"gift_cards.birthday.liquid","last_characters":"mnop","order_id":null,"code":"abcdefghijklmnop"}}

  * #### Create a gift card with an automatically generated code

#####

        curl -d '{"gift_card":{"initial_value":"25.00"}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/gift_cards.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const gift_card = new admin.rest.resources.GiftCard({session: session});

        gift_card.initial_value = "25.00";
        await gift_card.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        gift_card = ShopifyAPI::GiftCard.new(session: test_session)
        gift_card.initial_value = "25.00"
        gift_card.save!

#####

        // Session is built by the OAuth process

        const gift_card = new shopify.rest.GiftCard({session: session});
        gift_card.initial_value = "25.00";
        await gift_card.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"gift_card":{"id":1063936324,"balance":"25.00","created_at":"2026-01-09T18:59:57-05:00","updated_at":"2026-01-09T18:59:57-05:00","currency":"USD","initial_value":"25.00","disabled_at":null,"line_item_id":null,"api_client_id":755357713,"user_id":null,"customer_id":null,"note":null,"expires_on":null,"template_suffix":null,"last_characters":"5844","order_id":null,"code":"766ea5ba9hhf5844"}}

  * #### Create a scheduled gift card with a recipient and a message

#####

        curl -d '{"gift_card":{"initial_value":"100.00","recipient_id":207119551,"message":"Happy birthday!","send_on":"2023-12-31"}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/gift_cards.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const gift_card = new admin.rest.resources.GiftCard({session: session});

        gift_card.initial_value = "100.00";
        gift_card.recipient_id = 207119551;
        gift_card.message = "Happy birthday!";
        gift_card.send_on = "2023-12-31";
        await gift_card.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        gift_card = ShopifyAPI::GiftCard.new(session: test_session)
        gift_card.initial_value = "100.00"
        gift_card.recipient_id = 207119551
        gift_card.message = "Happy birthday!"
        gift_card.send_on = "2023-12-31"
        gift_card.save!

#####

        // Session is built by the OAuth process

        const gift_card = new shopify.rest.GiftCard({session: session});
        gift_card.initial_value = "100.00";
        gift_card.recipient_id = 207119551;
        gift_card.message = "Happy birthday!";
        gift_card.send_on = "2023-12-31";
        await gift_card.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"gift_card":{"id":1063936328,"balance":"100.00","created_at":"2023-11-30T19:00:00-05:00","updated_at":"2023-11-30T19:00:00-05:00","currency":"USD","initial_value":"100.00","disabled_at":null,"line_item_id":null,"api_client_id":755357713,"user_id":null,"customer_id":null,"note":null,"expires_on":null,"template_suffix":null,"last_characters":"fhea","order_id":null,"code":"ggbfc726d7fcfhea"}}


* * *

##

[Anchor to POST request, Disables a gift card](/docs/api/admin-rest/latest/resources/gift-card#post-gift-cards-gift-card-id-disable)

post

Disables a gift card

[giftCardDeactivate](/docs/api/admin-graphql/latest/mutations/giftCardDeactivate?example=disables-a-gift-card)

Disables a gift card. This action can't be undone.

###

[Anchor to Parameters of Disables a gift card](/docs/api/admin-rest/latest/resources/gift-card#post-gift-cards-gift-card-id-disable-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

gift_card_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to post-gift-cards-gift-card-id-disable-examples](/docs/api/admin-rest/latest/resources/gift-card#post-gift-cards-gift-card-id-disable-examples)Examples

Disable a gift card

Path parameters

gift_card_id=1035197676

string**string**

required**required**

Request body

gift_card

Gift_card resource**Gift_card resource**

Show gift_card properties

gift_card.id:1035197676

The ID of the gift card.

Was this section helpful?

YesNo

post

## /admin/api/2026-01/gift_cards/1035197676/disable.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{"gift_card":{"id":1035197676}}' \

-X POST "https://your-development-store.myshopify.com/admin/api/2026-01/gift_cards/1035197676/disable.json" \

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

HTTP/1.1 201 Created

{

"gift_card": {

"disabled_at": "2026-01-09T18:59:58-05:00",

"template_suffix": null,

"initial_value": "100.00",

"balance": "100.00",

"currency": "USD",

"id": 1035197676,

"created_at": "2026-01-09T17:04:11-05:00",

"updated_at": "2026-01-09T18:59:58-05:00",

"line_item_id": null,

"api_client_id": null,

"user_id": null,

"customer_id": null,

"note": null,

"expires_on": null,

"last_characters": "0d0d",

"order_id": null

}

}

### examples

  * #### Disable a gift card

#####

        curl -d '{"gift_card":{"id":1035197676}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/gift_cards/1035197676/disable.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const gift_card = new admin.rest.resources.GiftCard({session: session});

        gift_card.id = 1035197676;
        await gift_card.disable({
          body: {"gift_card": {"id": 1035197676}},
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        gift_card = ShopifyAPI::GiftCard.new(session: test_session)
        gift_card.id = 1035197676
        gift_card.disable(
          session: test_session,
          body: {"gift_card" => {"id" => 1035197676}},
        )

#####

        // Session is built by the OAuth process

        const gift_card = new shopify.rest.GiftCard({session: session});
        gift_card.id = 1035197676;
        await gift_card.disable({
          body: {"gift_card": {"id": 1035197676}},
        });

#### response

        HTTP/1.1 201 Created{"gift_card":{"disabled_at":"2026-01-09T18:59:58-05:00","template_suffix":null,"initial_value":"100.00","balance":"100.00","currency":"USD","id":1035197676,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T18:59:58-05:00","line_item_id":null,"api_client_id":null,"user_id":null,"customer_id":null,"note":null,"expires_on":null,"last_characters":"0d0d","order_id":null}}


* * *

##

[Anchor to GET request, Retrieves a list of gift cards](/docs/api/admin-rest/latest/resources/gift-card#get-gift-cards?status=enabled)

get

Retrieves a list of gift cards

[giftCards](/docs/api/admin-graphql/latest/queries/giftCards?example=retrieves-a-list-of-gift-cards)

Retrieves a list of gift cards. **Note:** This endpoint implements pagination by using links that are provided in the response header. To learn more, refer to [Make paginated requests to the REST Admin API](/api/usage/pagination-rest).

###

[Anchor to Parameters of Retrieves a list of gift cards](/docs/api/admin-rest/latest/resources/gift-card#get-gift-cards?status=enabled-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

fields

Show only certain fields, specified by a comma-separated list of field names.

* * *

limit

≤ 250**≤ 250**

default 50**default 50**

The maximum number of results to show.

* * *

since_id

Restrict results to after the specified ID.

* * *

status

Retrieve gift cards with a given status. Valid values:

Show status properties

  * **enabled** : Restrict results to only enabled gift cards

  * **disabled** : Restrict results to only disabled gift cards


* * *

Was this section helpful?

YesNo

###

[Anchor to get-gift-cards?status=enabled-examples](/docs/api/admin-rest/latest/resources/gift-card#get-gift-cards?status=enabled-examples)Examples

Retrieve a list of all enabled gift cards

Query parameters

status=enabled

Retrieve gift cards with a given status. Valid values:

Show status properties

  * **enabled** : Restrict results to only enabled gift cards

  * **disabled** : Restrict results to only disabled gift cards


Retrieve a list of all gift cards

Was this section helpful?

YesNo

get

## /admin/api/2026-01/gift_cards.json?status=enabled

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/gift_cards.json?status=enabled" \

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

HTTP/1.1 200 OK

{

"gift_cards": [

{

"id": 766118925,

"balance": "25.00",

"created_at": "2026-01-09T17:04:11-05:00",

"updated_at": "2026-01-09T17:04:11-05:00",

"currency": "USD",

"initial_value": "50.00",

"disabled_at": null,

"line_item_id": null,

"api_client_id": null,

"user_id": null,

"customer_id": null,

"note": null,

"expires_on": "2025-01-09",

"template_suffix": null,

"notify": true,

"last_characters": "0e0e",

"order_id": null

},

{

"id": 10274553,

"balance": "0.00",

"created_at": "2026-01-09T17:04:11-05:00",

"updated_at": "2026-01-09T17:04:11-05:00",

"currency": "USD",

"initial_value": "50.00",

"disabled_at": null,

"line_item_id": null,

"api_client_id": null,

"user_id": null,

"customer_id": null,

"note": null,

"expires_on": null,

"template_suffix": null,

"notify": true,

"last_characters": "0y0y",

"order_id": null

}

]

}

### examples

  * #### Retrieve a list of all enabled gift cards

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/gift_cards.json?status=enabled" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.GiftCard.all({
          session: session,
          status: "enabled",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::GiftCard.all(
          session: test_session,
          status: "enabled",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.GiftCard.all({
          session: session,
          status: "enabled",
        });

#### response

        HTTP/1.1 200 OK{"gift_cards":[{"id":766118925,"balance":"25.00","created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","currency":"USD","initial_value":"50.00","disabled_at":null,"line_item_id":null,"api_client_id":null,"user_id":null,"customer_id":null,"note":null,"expires_on":"2025-01-09","template_suffix":null,"notify":true,"last_characters":"0e0e","order_id":null},{"id":10274553,"balance":"0.00","created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","currency":"USD","initial_value":"50.00","disabled_at":null,"line_item_id":null,"api_client_id":null,"user_id":null,"customer_id":null,"note":null,"expires_on":null,"template_suffix":null,"notify":true,"last_characters":"0y0y","order_id":null}]}

  * #### Retrieve a list of all gift cards

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/gift_cards.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.GiftCard.all({
          session: session,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::GiftCard.all(
          session: test_session,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.GiftCard.all({
          session: session,
        });

#### response

        HTTP/1.1 200 OK{"gift_cards":[{"id":1035197676,"balance":"100.00","created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","currency":"USD","initial_value":"100.00","disabled_at":null,"line_item_id":null,"api_client_id":null,"user_id":null,"customer_id":null,"note":null,"expires_on":null,"template_suffix":null,"notify":true,"last_characters":"0d0d","order_id":null},{"id":766118925,"balance":"25.00","created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","currency":"USD","initial_value":"50.00","disabled_at":null,"line_item_id":null,"api_client_id":null,"user_id":null,"customer_id":null,"note":null,"expires_on":"2025-01-09","template_suffix":null,"notify":true,"last_characters":"0e0e","order_id":null},{"id":10274553,"balance":"0.00","created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","currency":"USD","initial_value":"50.00","disabled_at":null,"line_item_id":null,"api_client_id":null,"user_id":null,"customer_id":null,"note":null,"expires_on":null,"template_suffix":null,"notify":true,"last_characters":"0y0y","order_id":null}]}


* * *

##

[Anchor to GET request, Retrieves a single gift card](/docs/api/admin-rest/latest/resources/gift-card#get-gift-cards-gift-card-id)

get

Retrieves a single gift card

[giftCard](/docs/api/admin-graphql/latest/queries/giftCard?example=retrieves-a-single-gift-card)

Retrieves a single gift card by its ID

###

[Anchor to Parameters of Retrieves a single gift card](/docs/api/admin-rest/latest/resources/gift-card#get-gift-cards-gift-card-id-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

gift_card_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to get-gift-cards-gift-card-id-examples](/docs/api/admin-rest/latest/resources/gift-card#get-gift-cards-gift-card-id-examples)Examples

Retrieve a single gift card

Path parameters

gift_card_id=1035197676

string**string**

required**required**

Was this section helpful?

YesNo

get

## /admin/api/2026-01/gift_cards/1035197676.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/gift_cards/1035197676.json" \

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

HTTP/1.1 200 OK

{

"gift_card": {

"id": 1035197676,

"balance": "100.00",

"created_at": "2026-01-09T17:04:11-05:00",

"updated_at": "2026-01-09T17:04:11-05:00",

"currency": "USD",

"initial_value": "100.00",

"disabled_at": null,

"line_item_id": null,

"api_client_id": null,

"user_id": null,

"customer_id": null,

"note": null,

"expires_on": null,

"template_suffix": null,

"last_characters": "0d0d",

"order_id": null

}

}

### examples

  * #### Retrieve a single gift card

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/gift_cards/1035197676.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.GiftCard.find({
          session: session,
          id: 1035197676,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::GiftCard.find(
          session: test_session,
          id: 1035197676,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.GiftCard.find({
          session: session,
          id: 1035197676,
        });

#### response

        HTTP/1.1 200 OK{"gift_card":{"id":1035197676,"balance":"100.00","created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","currency":"USD","initial_value":"100.00","disabled_at":null,"line_item_id":null,"api_client_id":null,"user_id":null,"customer_id":null,"note":null,"expires_on":null,"template_suffix":null,"last_characters":"0d0d","order_id":null}}


* * *

##

[Anchor to GET request, Retrieves a count of gift cards](/docs/api/admin-rest/latest/resources/gift-card#get-gift-cards-count)

get

Retrieves a count of gift cards

[giftCardsCount](/docs/api/admin-graphql/latest/queries/giftCardsCount?example=retrieves-a-count-of-gift-cards)

Retrieves a count of gift cards with a given status.

###

[Anchor to Parameters of Retrieves a count of gift cards](/docs/api/admin-rest/latest/resources/gift-card#get-gift-cards-count-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

status

Count gift cards with a given status. Valid values:

Show status properties

  * **enabled** : Count only enabled gift cards

  * **disabled** : Count only disabled gift cards


* * *

Was this section helpful?

YesNo

###

[Anchor to get-gift-cards-count-examples](/docs/api/admin-rest/latest/resources/gift-card#get-gift-cards-count-examples)Examples

Retrieve a count of all gift cards

Retrieve a count of enabled gift cards

Query parameters

status=enabled

Count gift cards with a given status. Valid values:

Show status properties

  * **enabled** : Count only enabled gift cards

  * **disabled** : Count only disabled gift cards


Was this section helpful?

YesNo

get

## /admin/api/2026-01/gift_cards/count.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/gift_cards/count.json" \

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

"count": 3

}

### examples

  * #### Retrieve a count of all gift cards

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/gift_cards/count.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.GiftCard.count({
          session: session,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::GiftCard.count(
          session: test_session,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.GiftCard.count({
          session: session,
        });

#### response

        HTTP/1.1 200 OK{"count":3}

  * #### Retrieve a count of enabled gift cards

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/gift_cards/count.json?status=enabled" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.GiftCard.count({
          session: session,
          status: "enabled",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::GiftCard.count(
          session: test_session,
          status: "enabled",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.GiftCard.count({
          session: session,
          status: "enabled",
        });

#### response

        HTTP/1.1 200 OK{"count":3}


* * *

##

[Anchor to GET request, Searches for gift cards](/docs/api/admin-rest/latest/resources/gift-card#get-gift-cards-search?query=last-characters:mnop)

get

Searches for gift cards

[giftCards](/docs/api/admin-graphql/latest/queries/giftCards?example=searches-for-gift-cards)

Searches for gift cards that match a supplied query. The following fields are indexed by search:

  * `created_at`
  * `updated_at`
  * `disabled_at`
  * `balance`
  * `initial_value`
  * `amount_spent`
  * `email`
  * `last_characters`


**Note:** This endpoint implements pagination by using links that are provided in the response header. To learn more, refer to [Make paginated requests to the REST Admin API](/api/usage/pagination-rest).

###

[Anchor to Parameters of Searches for gift cards](/docs/api/admin-rest/latest/resources/gift-card#get-gift-cards-search?query=last-characters:mnop-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

created_at_max

date**date**

ISO 8601**ISO 8601**

Show gift cards created at or before date.

* * *

created_at_min

date**date**

ISO 8601**ISO 8601**

Show gift cards created at or after date.

* * *

fields

Show only certain fields, specified by a comma-separated list of field names.

* * *

limit

≤ 250**≤ 250**

default 50**default 50**

The maximum number of results to retrieve.

* * *

order

default disabled_at DESC**default disabled_at DESC**

The field and direction to order results by.

* * *

query

The text to search for.

* * *

updated_at_max

date**date**

ISO 8601**ISO 8601**

Show gift cards last updated at or before date.

* * *

updated_at_min

date**date**

ISO 8601**ISO 8601**

Show gift cards last updated at or after date.

* * *

Was this section helpful?

YesNo

###

[Anchor to get-gift-cards-search?query=last-characters:mnop-examples](/docs/api/admin-rest/latest/resources/gift-card#get-gift-cards-search?query=last-characters:mnop-examples)Examples

Retrieve all gift cards with the last characters "mnop"

Query parameters

query=last_characters:mnop

The text to search for.

Was this section helpful?

YesNo

get

## /admin/api/2026-01/gift_cards/search.json?query=last_characters:mnop

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/gift_cards/search.json?query=last_characters%3Amnop" \

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

HTTP/1.1 200 OK

{

"gift_cards": [

{

"id": 1063936325,

"balance": "10.00",

"created_at": "2026-01-09T18:59:59-05:00",

"updated_at": "2026-01-09T18:59:59-05:00",

"currency": "USD",

"initial_value": "10.00",

"disabled_at": null,

"line_item_id": null,

"api_client_id": null,

"user_id": null,

"customer_id": null,

"note": null,

"expires_on": null,

"template_suffix": null,

"notify": true,

"last_characters": "mnop",

"order_id": null

}

]

}

### examples

  * #### Retrieve all gift cards with the last characters "mnop"

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/gift_cards/search.json?query=last_characters%3Amnop" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.GiftCard.search({
          session: session,
          query: "last_characters:mnop",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::GiftCard.search(
          session: test_session,
          query: "last_characters:mnop",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.GiftCard.search({
          session: session,
          query: "last_characters:mnop",
        });

#### response

        HTTP/1.1 200 OK{"gift_cards":[{"id":1063936325,"balance":"10.00","created_at":"2026-01-09T18:59:59-05:00","updated_at":"2026-01-09T18:59:59-05:00","currency":"USD","initial_value":"10.00","disabled_at":null,"line_item_id":null,"api_client_id":null,"user_id":null,"customer_id":null,"note":null,"expires_on":null,"template_suffix":null,"notify":true,"last_characters":"mnop","order_id":null}]}


* * *

##

[Anchor to PUT request, Updates an existing gift card](/docs/api/admin-rest/latest/resources/gift-card#put-gift-cards-gift-card-id)

put

Updates an existing gift card

[giftCardUpdate](/docs/api/admin-graphql/latest/mutations/giftCardUpdate)

Updates an existing gift card.

Expiry date, note, and template suffix properties of a gift card can be changed via the API.

A customer ID can only be set if the current value is `null`.

###

[Anchor to Parameters of Updates an existing gift card](/docs/api/admin-rest/latest/resources/gift-card#put-gift-cards-gift-card-id-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

gift_card_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to put-gift-cards-gift-card-id-examples](/docs/api/admin-rest/latest/resources/gift-card#put-gift-cards-gift-card-id-examples)Examples

Update the expiry date of a gift card

Path parameters

gift_card_id=1035197676

string**string**

required**required**

Request body

gift_card

Gift_card resource**Gift_card resource**

Show gift_card properties

gift_card.id:1035197676

The ID of the gift card.

gift_card.expires_on:"2020-01-01"

->[expiresOn](/docs/api/admin-graphql/latest/input-objects/GiftCardUpdateInput#fields-expiresOn)

The date (`YYYY-MM-DD` format) when the gift card expires. Returns `null` if the gift card doesn't have an expiration date.

Update the note of a gift card

Path parameters

gift_card_id=1035197676

string**string**

required**required**

Request body

gift_card

Gift_card resource**Gift_card resource**

Show gift_card properties

gift_card.id:1035197676

The ID of the gift card.

gift_card.note:"Updating with a new note"

->[note](/docs/api/admin-graphql/latest/input-objects/GiftCardUpdateInput#fields-note)

An optional note that a merchant can attach to the gift card that isn't visible to customers.

Was this section helpful?

YesNo

put

## /admin/api/2026-01/gift_cards/1035197676.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{"gift_card":{"id":1035197676,"expires_on":"2020-01-01"}}' \

-X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/gift_cards/1035197676.json" \

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

HTTP/1.1 200 OK

{

"gift_card": {

"expires_on": "2020-01-01",

"template_suffix": null,

"initial_value": "100.00",

"balance": "100.00",

"currency": "USD",

"id": 1035197676,

"created_at": "2026-01-09T17:04:11-05:00",

"updated_at": "2026-01-09T19:00:03-05:00",

"disabled_at": null,

"line_item_id": null,

"api_client_id": null,

"user_id": null,

"customer_id": null,

"note": null,

"last_characters": "0d0d",

"order_id": null

}

}

### examples

  * #### Update the expiry date of a gift card

#####

        curl -d '{"gift_card":{"id":1035197676,"expires_on":"2020-01-01"}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/gift_cards/1035197676.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const gift_card = new admin.rest.resources.GiftCard({session: session});

        gift_card.id = 1035197676;
        gift_card.expires_on = "2020-01-01";
        await gift_card.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        gift_card = ShopifyAPI::GiftCard.new(session: test_session)
        gift_card.id = 1035197676
        gift_card.expires_on = "2020-01-01"
        gift_card.save!

#####

        // Session is built by the OAuth process

        const gift_card = new shopify.rest.GiftCard({session: session});
        gift_card.id = 1035197676;
        gift_card.expires_on = "2020-01-01";
        await gift_card.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"gift_card":{"expires_on":"2020-01-01","template_suffix":null,"initial_value":"100.00","balance":"100.00","currency":"USD","id":1035197676,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T19:00:03-05:00","disabled_at":null,"line_item_id":null,"api_client_id":null,"user_id":null,"customer_id":null,"note":null,"last_characters":"0d0d","order_id":null}}

  * #### Update the note of a gift card

#####

        curl -d '{"gift_card":{"id":1035197676,"note":"Updating with a new note"}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/gift_cards/1035197676.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const gift_card = new admin.rest.resources.GiftCard({session: session});

        gift_card.id = 1035197676;
        gift_card.note = "Updating with a new note";
        await gift_card.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        gift_card = ShopifyAPI::GiftCard.new(session: test_session)
        gift_card.id = 1035197676
        gift_card.note = "Updating with a new note"
        gift_card.save!

#####

        // Session is built by the OAuth process

        const gift_card = new shopify.rest.GiftCard({session: session});
        gift_card.id = 1035197676;
        gift_card.note = "Updating with a new note";
        await gift_card.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"gift_card":{"note":"Updating with a new note","template_suffix":null,"initial_value":"100.00","balance":"100.00","currency":"USD","id":1035197676,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T18:59:55-05:00","disabled_at":null,"line_item_id":null,"api_client_id":null,"user_id":null,"customer_id":null,"expires_on":null,"last_characters":"0d0d","order_id":null}}