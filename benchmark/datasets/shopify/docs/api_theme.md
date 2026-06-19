# Theme

*Source: https://shopify.dev/docs/api/admin-rest/2026-01/resources/theme*

---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04

2026-01latest

# Theme

Ask assistant

Requires `themes` access scope.

**Requires `themes` access scope.:**

A theme controls the look and feel of a Shopify online store.

A store can have a maximum of 20 themes, one of which is the published theme that customers see when they visit the online store. Customers can't see unpublished themes. When you publish a theme, the previously published theme becomes unpublished.

To modify theme files after they're uploaded, use the [Asset](/docs/admin-api/rest/reference/online-store/asset) resource. To learn how to create your own theme, refer to [_Building themes_](/concepts/themes)

Was this section helpful?

YesNo

#

## Endpoints

  * [post/admin/api/latest/themes.json](/docs/api/admin-rest/latest/resources/theme#post-themes)

Creates a theme

[themeCreate](/docs/api/admin-graphql/latest/mutations/themeCreate?example=creates-a-theme)

  * [get/admin/api/latest/themes.json](/docs/api/admin-rest/latest/resources/theme#get-themes)

Retrieves a list of themes

[themes](/docs/api/admin-graphql/latest/queries/themes?example=retrieves-a-list-of-themes)

  * [get/admin/api/latest/themes/{theme_id}.json](/docs/api/admin-rest/latest/resources/theme#get-themes-theme-id)

Retrieves a single theme by its ID

[theme](/docs/api/admin-graphql/latest/queries/theme?example=retrieves-a-single-theme-by-its-id)

  * [put/admin/api/latest/themes/{theme_id}.json](/docs/api/admin-rest/latest/resources/theme#put-themes-theme-id)

Modify an existing Theme

[themeUpdate](/docs/api/admin-graphql/latest/mutations/themeUpdate)

[themePublish](/docs/api/admin-graphql/latest/mutations/themePublish?example=modify-an-existing-theme)

  * [del/admin/api/latest/themes/{theme_id}.json](/docs/api/admin-rest/latest/resources/theme#delete-themes-theme-id)

Remove an existing Theme

[themeDelete](/docs/api/admin-graphql/latest/mutations/themeDelete?example=remove-an-existing-theme)


* * *

[Anchor to ](/docs/api/admin-rest/latest/resources/theme#resource-object)

## The Theme resource

[Anchor to ](/docs/api/admin-rest/latest/resources/theme#resource-object-properties)

### Properties

* * *

created_at

read-only**read-only**

->[createdAt](/docs/api/admin-graphql/latest/objects/OnlineStoreTheme#field-OnlineStoreTheme.fields.createdAt)

The date and time when the theme was created. (format: 2014-04-25T16:15:47-04:00)

* * *

id

read-only**read-only**

->[id](/docs/api/admin-graphql/latest/objects/OnlineStoreTheme#field-OnlineStoreTheme.fields.id)

The unique numeric identifier for the theme.

* * *

name

->[name](/docs/api/admin-graphql/latest/objects/OnlineStoreTheme#field-OnlineStoreTheme.fields.name)

The name of the theme.

* * *

previewable

read-only**read-only**

deprecated**deprecated**

Whether the theme can currently be previewed.

* * *

processing

read-only**read-only**

->[processing](/docs/api/admin-graphql/latest/objects/OnlineStoreTheme#field-OnlineStoreTheme.fields.processing)

Whether files are still being copied into place for this theme.

* * *

role

->[role](/docs/api/admin-graphql/latest/objects/OnlineStoreTheme#field-OnlineStoreTheme.fields.role)

Specifies how the theme is being used within the shop. Valid values:

Show role properties

  * **main** : The theme is published. Customers see it when they visit the online store.
  * **unpublished** : The theme is unpublished. Customers can't see it.
  * **demo** : The theme is installed on the store as a demo. The theme can't be published until the merchant buys the full version.
  * **development** : The theme is used for development. The theme can't be published, and is temporary.


* * *

src

Specifies a public URL where Shopify can access the theme code.

* * *

theme_store_id

read-only**read-only**

->[themeStoreId](/docs/api/admin-graphql/latest/objects/OnlineStoreTheme#field-OnlineStoreTheme.fields.themeStoreId)

A unique identifier applied to Shopify-made themes that are installed from the [Shopify Theme Store](https://themes.shopify.com/) Theme Store. Not all themes available in the Theme Store are developed by Shopify. Returns `null` if the store's theme isn't made by Shopify, or if it wasn't installed from the Theme Store.

* * *

updated_at

read-only**read-only**

->[updatedAt](/docs/api/admin-graphql/latest/objects/OnlineStoreTheme#field-OnlineStoreTheme.fields.updatedAt)

The date and time of when the theme was last updated. (format: 2014-04-25T16:15:47-04:00)

* * *

Was this section helpful?

YesNo

{}

## The Theme resource

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

"created_at": "2012-08-24T14:01:47-04:00",

"id": 828155753,

"name": "Comfort",

"previewable": true,

"processing": true,

"role": "main",

"src": "http://themes.shopify.com/theme.zip",

"theme_store_id": 775,

"updated_at": "2012-08-24T14:01:47-04:00"

}

* * *

##

[Anchor to POST request, Creates a theme](/docs/api/admin-rest/latest/resources/theme#post-themes)

post

Creates a theme

[themeCreate](/docs/api/admin-graphql/latest/mutations/themeCreate?example=creates-a-theme)

Creates a theme by providing the public URL of a ZIP file that contains the theme.

A new theme is always unpublished by default. To publish a theme when you create it, include `"role": "main"` in the POST request. The theme will be published only after all of its files have been extracted and stored by Shopify, which might take a couple of minutes.

###

[Anchor to Parameters of Creates a theme](/docs/api/admin-rest/latest/resources/theme#post-themes-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to post-themes-examples](/docs/api/admin-rest/latest/resources/theme#post-themes-examples)Examples

Create a theme that has a custom name and is published

Request body

theme

Theme resource**Theme resource**

Show theme properties

theme.name:"Lemongrass"

The name of the theme.

theme.src:"http://themes.shopify.com/theme.zip"

Specifies a public URL where Shopify can access the theme code.

theme.role:"main"

Specifies how the theme is being used within the shop. Valid values:

Show role properties

  * **main** : The theme is published. Customers see it when they visit the online store.
  * **unpublished** : The theme is unpublished. Customers can't see it.
  * **demo** : The theme is installed on the store as a demo. The theme can't be published until the merchant buys the full version.
  * **development** : The theme is used for development. The theme can't be published, and is temporary.


Creating a theme without a name fails and returns an error

Was this section helpful?

YesNo

post

## /admin/api/2026-01/themes.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{"theme":{"name":"Lemongrass","src":"http://themes.shopify.com/theme.zip","role":"main"}}' \

-X POST "https://your-development-store.myshopify.com/admin/api/2026-01/themes.json" \

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

HTTP/1.1 201 Created

{

"theme": {

"id": 1049083724,

"name": "Lemongrass",

"created_at": "2026-01-09T19:36:14-05:00",

"updated_at": "2026-01-09T19:36:14-05:00",

"role": "unpublished",

"theme_store_id": null,

"previewable": false,

"processing": true,

"admin_graphql_api_id": "gid://shopify/Theme/1049083724"

}

}

### examples

  * #### Create a theme that has a custom name and is published

#####

        curl -d '{"theme":{"name":"Lemongrass","src":"http://themes.shopify.com/theme.zip","role":"main"}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/themes.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const theme = new admin.rest.resources.Theme({session: session});

        theme.name = "Lemongrass";
        theme.src = "http://themes.shopify.com/theme.zip";
        theme.role = "main";
        await theme.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        theme = ShopifyAPI::Theme.new(session: test_session)
        theme.name = "Lemongrass"
        theme.src = "http://themes.shopify.com/theme.zip"
        theme.role = "main"
        theme.save!

#####

        // Session is built by the OAuth process

        const theme = new shopify.rest.Theme({session: session});
        theme.name = "Lemongrass";
        theme.src = "http://themes.shopify.com/theme.zip";
        theme.role = "main";
        await theme.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"theme":{"id":1049083724,"name":"Lemongrass","created_at":"2026-01-09T19:36:14-05:00","updated_at":"2026-01-09T19:36:14-05:00","role":"unpublished","theme_store_id":null,"previewable":false,"processing":true,"admin_graphql_api_id":"gid://shopify/Theme/1049083724"}}

  * #### Creating a theme without a name fails and returns an error

#####

        curl -d '{"theme":{"body":"foobar"}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/themes.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const theme = new admin.rest.resources.Theme({session: session});

        theme.body = "foobar";
        await theme.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        theme = ShopifyAPI::Theme.new(session: test_session)
        theme.body = "foobar"
        theme.save!

#####

        // Session is built by the OAuth process

        const theme = new shopify.rest.Theme({session: session});
        theme.body = "foobar";
        await theme.save({
          update: true,
        });

#### response

        HTTP/1.1 422 Unprocessable Entity{"errors":{"name":["can't be blank"]}}


* * *

##

[Anchor to GET request, Retrieves a list of themes](/docs/api/admin-rest/latest/resources/theme#get-themes)

get

Retrieves a list of themes

[themes](/docs/api/admin-graphql/latest/queries/themes?example=retrieves-a-list-of-themes)

Retrieves a list of themes.

###

[Anchor to Parameters of Retrieves a list of themes](/docs/api/admin-rest/latest/resources/theme#get-themes-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

fields

Show only certain fields, specified by a comma-separated list of field names.

* * *

Was this section helpful?

YesNo

###

[Anchor to get-themes-examples](/docs/api/admin-rest/latest/resources/theme#get-themes-examples)Examples

Retrieve a list of themes

Was this section helpful?

YesNo

get

## /admin/api/2026-01/themes.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/themes.json" \

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

HTTP/1.1 200 OK

{

"themes": [

{

"id": 828155753,

"name": "Comfort",

"created_at": "2026-01-09T17:04:11-05:00",

"updated_at": "2026-01-09T17:04:11-05:00",

"role": "main",

"theme_store_id": null,

"previewable": true,

"processing": false,

"admin_graphql_api_id": "gid://shopify/Theme/828155753"

},

{

"id": 976877075,

"name": "Preview of Parallax",

"created_at": "2026-01-09T17:04:11-05:00",

"updated_at": "2026-01-09T17:04:11-05:00",

"role": "demo",

"theme_store_id": 688,

"previewable": true,

"processing": false,

"admin_graphql_api_id": "gid://shopify/Theme/976877075"

},

{

"id": 752253240,

"name": "Sandbox",

"created_at": "2026-01-09T17:04:11-05:00",

"updated_at": "2026-01-09T17:04:11-05:00",

"role": "unpublished",

"theme_store_id": null,

"previewable": true,

"processing": false,

"admin_graphql_api_id": "gid://shopify/Theme/752253240"

}

]

}

### examples

  * #### Retrieve a list of themes

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/themes.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Theme.all({
          session: session,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Theme.all(
          session: test_session,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Theme.all({
          session: session,
        });

#### response

        HTTP/1.1 200 OK{"themes":[{"id":828155753,"name":"Comfort","created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","role":"main","theme_store_id":null,"previewable":true,"processing":false,"admin_graphql_api_id":"gid://shopify/Theme/828155753"},{"id":976877075,"name":"Preview of Parallax","created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","role":"demo","theme_store_id":688,"previewable":true,"processing":false,"admin_graphql_api_id":"gid://shopify/Theme/976877075"},{"id":752253240,"name":"Sandbox","created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","role":"unpublished","theme_store_id":null,"previewable":true,"processing":false,"admin_graphql_api_id":"gid://shopify/Theme/752253240"}]}


* * *

##

[Anchor to GET request, Retrieves a single theme by its ID](/docs/api/admin-rest/latest/resources/theme#get-themes-theme-id)

get

Retrieves a single theme by its ID

[theme](/docs/api/admin-graphql/latest/queries/theme?example=retrieves-a-single-theme-by-its-id)

Retrieves a single theme by its ID.

###

[Anchor to Parameters of Retrieves a single theme by its ID](/docs/api/admin-rest/latest/resources/theme#get-themes-theme-id-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

theme_id

string**string**

required**required**

* * *

fields

Show only certain fields, specified by a comma-separated list of field names.

* * *

Was this section helpful?

YesNo

###

[Anchor to get-themes-theme-id-examples](/docs/api/admin-rest/latest/resources/theme#get-themes-theme-id-examples)Examples

Retrieve a single theme

Path parameters

theme_id=828155753

string**string**

required**required**

Was this section helpful?

YesNo

get

## /admin/api/2026-01/themes/828155753.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/themes/828155753.json" \

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

HTTP/1.1 200 OK

{

"theme": {

"id": 828155753,

"name": "Comfort",

"created_at": "2026-01-09T17:04:11-05:00",

"updated_at": "2026-01-09T17:04:11-05:00",

"role": "main",

"theme_store_id": null,

"previewable": true,

"processing": false,

"admin_graphql_api_id": "gid://shopify/Theme/828155753"

}

}

### examples

  * #### Retrieve a single theme

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/themes/828155753.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Theme.find({
          session: session,
          id: 828155753,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Theme.find(
          session: test_session,
          id: 828155753,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Theme.find({
          session: session,
          id: 828155753,
        });

#### response

        HTTP/1.1 200 OK{"theme":{"id":828155753,"name":"Comfort","created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","role":"main","theme_store_id":null,"previewable":true,"processing":false,"admin_graphql_api_id":"gid://shopify/Theme/828155753"}}


* * *

##

[Anchor to PUT request, Modify an existing Theme](/docs/api/admin-rest/latest/resources/theme#put-themes-theme-id)

put

Modify an existing Theme

[themeUpdate](/docs/api/admin-graphql/latest/mutations/themeUpdate)

[themePublish](/docs/api/admin-graphql/latest/mutations/themePublish?example=modify-an-existing-theme)

Updates an existing theme.

###

[Anchor to Parameters of Modify an existing Theme](/docs/api/admin-rest/latest/resources/theme#put-themes-theme-id-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

theme_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to put-themes-theme-id-examples](/docs/api/admin-rest/latest/resources/theme#put-themes-theme-id-examples)Examples

Publish an unpublished theme

Path parameters

theme_id=752253240

string**string**

required**required**

Request body

theme

Theme resource**Theme resource**

Show theme properties

theme.id:752253240

read-only**read-only**

The unique numeric identifier for the theme.

theme.role:"main"

Specifies how the theme is being used within the shop. Valid values:

Show role properties

  * **main** : The theme is published. Customers see it when they visit the online store.
  * **unpublished** : The theme is unpublished. Customers can't see it.
  * **demo** : The theme is installed on the store as a demo. The theme can't be published until the merchant buys the full version.
  * **development** : The theme is used for development. The theme can't be published, and is temporary.


Update a theme's name

Path parameters

theme_id=752253240

string**string**

required**required**

Request body

theme

Theme resource**Theme resource**

Show theme properties

theme.id:752253240

read-only**read-only**

The unique numeric identifier for the theme.

theme.name:"Experimental"

The name of the theme.

Was this section helpful?

YesNo

put

## /admin/api/2026-01/themes/752253240.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{"theme":{"id":752253240,"role":"main"}}' \

-X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/themes/752253240.json" \

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

HTTP/1.1 200 OK

{

"theme": {

"role": "main",

"name": "Sandbox",

"id": 752253240,

"created_at": "2026-01-09T17:04:11-05:00",

"updated_at": "2026-01-09T19:36:15-05:00",

"theme_store_id": null,

"previewable": true,

"processing": false,

"admin_graphql_api_id": "gid://shopify/Theme/752253240"

}

}

### examples

  * #### Publish an unpublished theme

#####

        curl -d '{"theme":{"id":752253240,"role":"main"}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/themes/752253240.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const theme = new admin.rest.resources.Theme({session: session});

        theme.id = 752253240;
        theme.role = "main";
        await theme.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        theme = ShopifyAPI::Theme.new(session: test_session)
        theme.id = 752253240
        theme.role = "main"
        theme.save!

#####

        // Session is built by the OAuth process

        const theme = new shopify.rest.Theme({session: session});
        theme.id = 752253240;
        theme.role = "main";
        await theme.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"theme":{"role":"main","name":"Sandbox","id":752253240,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T19:36:15-05:00","theme_store_id":null,"previewable":true,"processing":false,"admin_graphql_api_id":"gid://shopify/Theme/752253240"}}

  * #### Update a theme's name

#####

        curl -d '{"theme":{"id":752253240,"name":"Experimental"}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/themes/752253240.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const theme = new admin.rest.resources.Theme({session: session});

        theme.id = 752253240;
        theme.name = "Experimental";
        await theme.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        theme = ShopifyAPI::Theme.new(session: test_session)
        theme.id = 752253240
        theme.name = "Experimental"
        theme.save!

#####

        // Session is built by the OAuth process

        const theme = new shopify.rest.Theme({session: session});
        theme.id = 752253240;
        theme.name = "Experimental";
        await theme.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"theme":{"name":"Experimental","role":"unpublished","id":752253240,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T19:36:11-05:00","theme_store_id":null,"previewable":true,"processing":false,"admin_graphql_api_id":"gid://shopify/Theme/752253240"}}


* * *

##

[Anchor to DELETE request, Remove an existing Theme](/docs/api/admin-rest/latest/resources/theme#delete-themes-theme-id)

del

Remove an existing Theme

[themeDelete](/docs/api/admin-graphql/latest/mutations/themeDelete?example=remove-an-existing-theme)

Deletes a theme. A theme can't be deleted while it's uploading, updating, or if the theme is the last published theme.

###

[Anchor to Parameters of Remove an existing Theme](/docs/api/admin-rest/latest/resources/theme#delete-themes-theme-id-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

theme_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to delete-themes-theme-id-examples](/docs/api/admin-rest/latest/resources/theme#delete-themes-theme-id-examples)Examples

Delete a theme

Path parameters

theme_id=752253240

string**string**

required**required**

Was this section helpful?

YesNo

del

## /admin/api/2026-01/themes/752253240.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X DELETE "https://your-development-store.myshopify.com/admin/api/2026-01/themes/752253240.json" \

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

HTTP/1.1 200 OK

{

"id": 752253240,

"name": "Sandbox",

"created_at": "2026-01-09T17:04:11-05:00",

"updated_at": "2026-01-09T17:04:11-05:00",

"role": "unpublished",

"theme_store_id": null,

"previewable": true,

"processing": false,

"admin_graphql_api_id": "gid://shopify/Theme/752253240"

}

### examples

  * #### Delete a theme

#####

        curl -X DELETE "https://your-development-store.myshopify.com/admin/api/2026-01/themes/752253240.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Theme.delete({
          session: session,
          id: 752253240,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Theme.delete(
          session: test_session,
          id: 752253240,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Theme.delete({
          session: session,
          id: 752253240,
        });

#### response

        HTTP/1.1 200 OK{"id":752253240,"name":"Sandbox","created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","role":"unpublished","theme_store_id":null,"previewable":true,"processing":false,"admin_graphql_api_id":"gid://shopify/Theme/752253240"}