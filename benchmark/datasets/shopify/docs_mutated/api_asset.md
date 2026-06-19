# Asset

*Source: https://shopify.dev/docs/api/admin-rest/2026-01/resources/asset*

---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04

2026-01latest

# Asset

Ask assistant

Requires `themes` access scope.

**Requires `themes` access scope.:**

Note

Starting with Admin API 2023-04, if an app distributed through the Shopify App Store uses the Asset resource to create, edit or delete a theme's asset, you need to request the required protected access scope. In most cases, you shouldn't use the Asset resource. To learn more about when you can use the Asset resource, and how to migrate, refer to the [Asset resource](/docs/apps/online-store/other-integration-methods/asset).

**Note:**

Starting with Admin API 2023-04, if an app distributed through the Shopify App Store uses the Asset resource to create, edit or delete a theme's asset, you need to request the required protected access scope. In most cases, you shouldn't use the Asset resource. To learn more about when you can use the Asset resource, and how to migrate, refer to the [Asset resource](/docs/apps/online-store/other-integration-methods/asset).

Theme assets are the individual files that make up a shop's theme.

A theme's assets include its templates, images, stylesheets, and extra snippets of code. They are arranged among the theme's directories, such as **layout** , **templates** , and **assets**. You can use the Asset resource to add, change, or remove asset files from a shop's theme. For a complete list of theme directories, refer to [_Theme architecture_](/themes/architecture).

To learn how to create your own theme, see [_Building themes_](/concepts/themes).

Was this section helpful?

YesNo

#

## Endpoints

  * [get/admin/api/latest/themes/{theme_id}/assets.json](/docs/api/admin-rest/latest/resources/asset#get-themes-theme-id-assets)

Retrieves a list of assets for a theme

[theme](/docs/api/admin-graphql/latest/queries/theme?example=retrieves-a-list-of-assets-for-a-theme)

  * [get/admin/api/latest/themes/{theme_id}/assets.json?asset[key]=templates/index.liquid](/docs/api/admin-rest/latest/resources/asset#get-themes-theme-id-assets?asset\[key\]=templates-index.liquid)

Retrieves a single asset for a theme

[theme](/docs/api/admin-graphql/latest/queries/theme?example=retrieves-a-single-asset-for-a-theme)

  * [put/admin/api/latest/themes/{theme_id}/assets.json](/docs/api/admin-rest/latest/resources/asset#put-themes-theme-id-assets)

Creates or updates an asset for a theme

[themeFilesUpsert](/docs/api/admin-graphql/latest/mutations/themeFilesUpsert)

[themeFilesCopy](/docs/api/admin-graphql/latest/mutations/themeFilesCopy?example=creates-or-updates-an-asset-for-a-theme)

  * [del/admin/api/latest/themes/{theme_id}/assets.json?asset[key]=assets/bg-body.gif](/docs/api/admin-rest/latest/resources/asset#delete-themes-theme-id-assets?asset\[key\]=assets-bg-body.gif)

Deletes an asset from a theme

[themeFilesDelete](/docs/api/admin-graphql/latest/mutations/themeFilesDelete?example=deletes-an-asset-from-a-theme)


* * *

[Anchor to ](/docs/api/admin-rest/latest/resources/asset#resource-object)

## The Asset resource

[Anchor to ](/docs/api/admin-rest/latest/resources/asset#resource-object-properties)

### Properties

* * *

attachment

->[contentBase64](/docs/api/admin-graphql/latest/objects/OnlineStoreThemeFileBodyBase64#field-OnlineStoreThemeFileBodyBase64.fields.contentBase64)

A base64-encoded image.

* * *

checksum

read-only**read-only**

->[checksumMd5](/docs/api/admin-graphql/latest/objects/OnlineStoreThemeFile#field-OnlineStoreThemeFile.fields.checksumMd5)

The [MD5](https://en.wikipedia.org/wiki/MD5) representation of the content, consisting of a string of 32 hexadecimal digits. May be null if an asset has not been updated recently.

* * *

content_type

read-only**read-only**

->[contentType](/docs/api/admin-graphql/latest/objects/OnlineStoreThemeFile#field-OnlineStoreThemeFile.fields.contentType)

The [MIME](https://en.wikipedia.org/wiki/Media_type) representation of the content, consisting of the type and subtype of the asset.

* * *

created_at

read-only**read-only**

->[createdAt](/docs/api/admin-graphql/latest/objects/OnlineStoreThemeFile#field-OnlineStoreThemeFile.fields.createdAt)

The date and time ([ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format) when the asset was created.

* * *

key

->[filename](/docs/api/admin-graphql/latest/objects/OnlineStoreThemeFile#field-OnlineStoreThemeFile.fields.filename)

The path to the asset within a theme. It consists of the file's directory and filename. For example, the asset `assets/bg-body-green.gif` is in the **assets** directory, so its key is `assets/bg-body-green.gif`.

* * *

public_url

read-only**read-only**

->[url](/docs/api/admin-graphql/latest/objects/OnlineStoreThemeFileBodyUrl#field-OnlineStoreThemeFileBodyUrl.fields.url)

The public-facing URL of the asset.

* * *

size

read-only**read-only**

->[size](/docs/api/admin-graphql/latest/objects/OnlineStoreThemeFile#field-OnlineStoreThemeFile.fields.size)

The asset size in bytes.

* * *

theme_id

read-only**read-only**

deprecated**deprecated**

The ID for the theme that an asset belongs to.

* * *

updated_at

read-only**read-only**

->[updatedAt](/docs/api/admin-graphql/latest/objects/OnlineStoreThemeFile#field-OnlineStoreThemeFile.fields.updatedAt)

The date and time ([ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format) when an asset was last updated.

* * *

value

->[content](/docs/api/admin-graphql/latest/objects/OnlineStoreThemeFileBodyText#field-OnlineStoreThemeFileBodyText.fields.content)

The text content of the asset, such as the HTML and Liquid markup of a template file.

* * *

Was this section helpful?

YesNo

{}

## The Asset resource

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

{

"attachment": "R0lGODlhAQABAPABAP///wAAACH5Ow==\n",

"checksum": "f69db2c563b5be32648ac7367557c09c",

"content_type": "image/gif",

"created_at": "2010-07-12T15:31:50-04:00",

"key": "assets/bg-body-green.gif",

"public_url": "http://static.shopify.com/assets/bg.gif?1",

"size": 1542,

"theme_id": 828155753,

"updated_at": "2010-07-12T15:31:50-04:00",

"value": "<div id=\"page\">\n<h1>404 Page not found</h1>\n<p>We couldn't find the page you were looking for.</p>\n</div>"

}

* * *

##

[Anchor to GET request, Retrieves a list of assets for a theme](/docs/api/admin-rest/latest/resources/asset#get-themes-theme-id-assets)

get

Retrieves a list of assets for a theme

[theme](/docs/api/admin-graphql/latest/queries/theme?example=retrieves-a-list-of-assets-for-a-theme)

Retrieves a list of assets for a theme.

**Note:** Retrieving a list of assets returns only metadata about each asset. To retrieve an asset's content, you need to retrieve the asset individually.

###

[Anchor to Parameters of Retrieves a list of assets for a theme](/docs/api/admin-rest/latest/resources/asset#get-themes-theme-id-assets-parameters)Parameters

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

Specify which fields to show using a comma-separated list of field names.

* * *

Was this section helpful?

YesNo

###

[Anchor to get-themes-theme-id-assets-examples](/docs/api/admin-rest/latest/resources/asset#get-themes-theme-id-assets-examples)Examples

Retrieve a list of all assets for a theme

Path parameters

theme_id=828155753

string**string**

required**required**

Was this section helpful?

YesNo

get

## /admin/api/2026-01/themes/828155753/assets.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/themes/828155753/assets.json" \

-H "X-Shopify-Access-Token: {access_token}"

{}

## Response

JSON

999

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

HTTP/1.1 200 OK

{

"assets": [

{

"key": "layout/theme.liquid",

"public_url": null,

"created_at": "2010-07-12T15:31:50-04:00",

"updated_at": "2010-07-12T15:31:50-04:00",

"content_type": "application/x-liquid",

"size": 3252,

"checksum": null,

"theme_id": 828155753

},

{

"key": "assets/sidebar-devider.gif",

"public_url": "https://cdn.shopify.com/s/files/1/0005/4838/0009/t/1/assets/sidebar-devider.gif?v=1278963110",

"created_at": "2010-07-12T15:31:50-04:00",

"updated_at": "2010-07-12T15:31:50-04:00",

"content_type": "image/gif",

"size": 1016,

"checksum": null,

"theme_id": 828155753

},

{

"key": "assets/bg-body-pink.gif",

"public_url": "https://cdn.shopify.com/s/files/1/0005/4838/0009/t/1/assets/bg-body-pink.gif?v=1278963110",

"created_at": "2010-07-12T15:31:50-04:00",

"updated_at": "2010-07-12T15:31:50-04:00",

"content_type": "image/gif",

"size": 1562,

"checksum": null,

"theme_id": 828155753

},

{

"key": "assets/bg-content.gif",

"public_url": "https://cdn.shopify.com/s/files/1/0005/4838/0009/t/1/assets/bg-content.gif?v=1278963110",

### examples

  * #### Retrieve a list of all assets for a theme

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/themes/828155753/assets.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Asset.all({
          session: session,
          theme_id: 828155753,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Asset.all(
          session: test_session,
          theme_id: 828155753,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Asset.all({
          session: session,
          theme_id: 828155753,
        });

#### response

        HTTP/1.1 200 OK{"assets":[{"key":"layout/theme.liquid","public_url":null,"created_at":"2010-07-12T15:31:50-04:00","updated_at":"2010-07-12T15:31:50-04:00","content_type":"application/x-liquid","size":3252,"checksum":null,"theme_id":828155753},{"key":"assets/sidebar-devider.gif","public_url":"https://cdn.shopify.com/s/files/1/0005/4838/0009/t/1/assets/sidebar-devider.gif?v=1278963110","created_at":"2010-07-12T15:31:50-04:00","updated_at":"2010-07-12T15:31:50-04:00","content_type":"image/gif","size":1016,"checksum":null,"theme_id":828155753},{"key":"assets/bg-body-pink.gif","public_url":"https://cdn.shopify.com/s/files/1/0005/4838/0009/t/1/assets/bg-body-pink.gif?v=1278963110","created_at":"2010-07-12T15:31:50-04:00","updated_at":"2010-07-12T15:31:50-04:00","content_type":"image/gif","size":1562,"checksum":null,"theme_id":828155753},{"key":"assets/bg-content.gif","public_url":"https://cdn.shopify.com/s/files/1/0005/4838/0009/t/1/assets/bg-content.gif?v=1278963110","created_at":"2010-07-12T15:31:50-04:00","updated_at":"2010-07-12T15:31:50-04:00","content_type":"image/gif","size":134,"checksum":null,"theme_id":828155753},{"key":"sections/header_section.liquid","public_url":null,"created_at":"2017-04-28T10:30:00-04:00","updated_at":"2017-04-28T10:30:00-04:00","content_type":"application/x-liquid","size":998,"checksum":null,"theme_id":828155753},{"key":"assets/shop.css.liquid","public_url":"https://cdn.shopify.com/s/files/1/0005/4838/0009/t/1/assets/shop.css.liquid?v=1278963110","created_at":"2010-07-12T15:31:50-04:00","updated_at":"2010-07-12T15:31:50-04:00","content_type":"application/x-liquid","size":14675,"checksum":null,"theme_id":828155753},{"key":"assets/shop.js","public_url":"https://cdn.shopify.com/s/files/1/0005/4838/0009/t/1/assets/shop.js?v=1278963110","created_at":"2010-07-12T15:31:50-04:00","updated_at":"2010-07-12T15:31:50-04:00","content_type":"application/javascript","size":348,"checksum":null,"theme_id":828155753},{"key":"assets/bg-main.gif","public_url":"https://cdn.shopify.com/s/files/1/0005/4838/0009/t/1/assets/bg-main.gif?v=1278963110","created_at":"2010-07-12T15:31:50-04:00","updated_at":"2010-07-12T15:31:50-04:00","content_type":"image/gif","size":297,"checksum":null,"theme_id":828155753},{"key":"sections/content_section.liquid","public_url":null,"created_at":"2016-02-11T14:31:50-05:00","updated_at":"2016-02-11T14:31:50-05:00","content_type":"application/x-liquid","size":997,"checksum":null,"theme_id":828155753},{"key":"templates/page.liquid","public_url":null,"created_at":"2010-07-12T15:31:50-04:00","updated_at":"2010-07-12T15:31:50-04:00","content_type":"application/x-liquid","size":147,"checksum":null,"theme_id":828155753},{"key":"assets/bg-body-green.gif","public_url":"https://cdn.shopify.com/s/files/1/0005/4838/0009/t/1/assets/bg-body-green.gif?v=1278963110","created_at":"2010-07-12T15:31:50-04:00","updated_at":"2010-07-12T15:31:50-04:00","content_type":"image/gif","size":1542,"checksum":null,"theme_id":828155753},{"key":"assets/shop.css","public_url":"https://cdn.shopify.com/s/files/1/0005/4838/0009/t/1/assets/shop.css?v=1278963110","created_at":"2010-07-12T15:31:50-04:00","updated_at":"2010-07-12T15:31:50-04:00","content_type":"text/css","size":14058,"checksum":null,"theme_id":828155753},{"key":"config/settings_schema.json","public_url":null,"created_at":"2010-07-12T15:31:50-04:00","updated_at":"2010-07-12T15:31:50-04:00","content_type":"application/json","size":4570,"checksum":null,"theme_id":828155753},{"key":"sections/product_section.liquid","public_url":null,"created_at":"2016-02-14T16:31:41-05:00","updated_at":"2016-02-14T16:31:41-05:00","content_type":"application/x-liquid","size":2440,"checksum":null,"theme_id":828155753},{"key":"templates/blog.liquid","public_url":null,"created_at":"2010-07-12T15:31:50-04:00","updated_at":"2010-07-12T15:31:50-04:00","content_type":"application/x-liquid","size":773,"checksum":null,"theme_id":828155753},{"key":"templates/article.liquid","public_url":null,"created_at":"2010-07-12T15:31:50-04:00","updated_at":"2010-07-12T15:31:50-04:00","content_type":"application/x-liquid","size":2486,"checksum":null,"theme_id":828155753},{"key":"templates/product.liquid","public_url":null,"created_at":"2010-07-12T15:31:50-04:00","updated_at":"2010-07-12T15:31:50-04:00","content_type":"application/x-liquid","size":2796,"checksum":null,"theme_id":828155753},{"key":"sections/footer_section.liquid","public_url":null,"created_at":"2017-04-28T10:30:00-04:00","updated_at":"2017-04-28T10:30:00-04:00","content_type":"application/x-liquid","size":999,"checksum":null,"theme_id":828155753},{"key":"assets/bg-footer.gif","public_url":"https://cdn.shopify.com/s/files/1/0005/4838/0009/t/1/assets/bg-footer.gif?v=1278963110","created_at":"2010-07-12T15:31:50-04:00","updated_at":"2010-07-12T15:31:50-04:00","content_type":"image/gif","size":1434,"checksum":null,"theme_id":828155753},{"key":"assets/bg-sidebar.gif","public_url":"https://cdn.shopify.com/s/files/1/0005/4838/0009/t/1/assets/bg-sidebar.gif?v=1278963110","created_at":"2010-07-12T15:31:50-04:00","updated_at":"2010-07-12T15:31:50-04:00","content_type":"image/gif","size":124,"checksum":null,"theme_id":828155753},{"key":"assets/bg-body-orange.gif","public_url":"https://cdn.shopify.com/s/files/1/0005/4838/0009/t/1/assets/bg-body-orange.gif?v=1278963110","created_at":"2010-07-12T15:31:50-04:00","updated_at":"2010-07-12T15:31:50-04:00","content_type":"image/gif","size":1548,"checksum":null,"theme_id":828155753},{"key":"templates/collection.liquid","public_url":null,"created_at":"2010-07-12T15:31:50-04:00","updated_at":"2010-07-12T15:31:50-04:00","content_type":"application/x-liquid","size":946,"checksum":null,"theme_id":828155753},{"key":"assets/sidebar-menu.jpg","public_url":"https://cdn.shopify.com/s/files/1/0005/4838/0009/t/1/assets/sidebar-menu.jpg?v=1278963110","created_at":"2010-07-12T15:31:50-04:00","updated_at":"2010-07-12T15:31:50-04:00","content_type":"image/jpeg","size":1609,"checksum":null,"theme_id":828155753},{"key":"templates/cart.liquid","public_url":null,"created_at":"2010-07-12T15:31:50-04:00","updated_at":"2010-07-12T15:31:50-04:00","content_type":"application/x-liquid","size":2047,"checksum":null,"theme_id":828155753},{"key":"config/settings_data.json","public_url":null,"created_at":"2010-07-12T15:31:50-04:00","updated_at":"2010-07-12T15:31:50-04:00","content_type":"application/json","size":4570,"checksum":null,"theme_id":828155753},{"key":"templates/index.liquid","public_url":null,"created_at":"2010-07-12T15:31:50-04:00","updated_at":"2010-07-12T15:31:50-04:00","content_type":"application/x-liquid","size":1068,"checksum":null,"theme_id":828155753},{"key":"assets/bg-body.gif","public_url":"https://cdn.shopify.com/s/files/1/0005/4838/0009/t/1/assets/bg-body.gif?v=1278963110","created_at":"2010-07-12T15:31:50-04:00","updated_at":"2010-07-12T15:31:50-04:00","content_type":"image/gif","size":1571,"checksum":null,"theme_id":828155753}]}


* * *

##

[Anchor to GET request, Retrieves a single asset for a theme](/docs/api/admin-rest/latest/resources/asset#get-themes-theme-id-assets?asset\[key\]=templates-index.liquid)

get

Retrieves a single asset for a theme

[theme](/docs/api/admin-graphql/latest/queries/theme?example=retrieves-a-single-asset-for-a-theme)

Retrieves a single asset for a theme by its key.

To retrieve a single asset, include `asset[key]=#{asset_key}` as a request parameter. For example, to retrieve the asset with a key of `templates/index.liquid`, the request might be `/admin/themes/828155753/assets.json?asset[key]=templates/index.liquid`.

For more information on the `key` property, refer to Asset properties.

###

[Anchor to Parameters of Retrieves a single asset for a theme](/docs/api/admin-rest/latest/resources/asset#get-themes-theme-id-assets?asset\[key\]=templates-index.liquid-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

asset[key]

required**required**

≤ 100**≤ 100**

Retrieves a single asset for a theme by specifying the asset's key.

* * *

theme_id

string**string**

required**required**

* * *

fields

Specify which fields to show using a comma-separated list of field names.

* * *

Was this section helpful?

YesNo

###

[Anchor to get-themes-theme-id-assets?asset[key]=templates-index.liquid-examples](/docs/api/admin-rest/latest/resources/asset#get-themes-theme-id-assets?asset\[key\]=templates-index.liquid-examples)Examples

Retrieve a Liquid template

Query parameters

asset[key]=templates/index.liquid

required**required**

≤ 100**≤ 100**

Retrieves a single asset for a theme by specifying the asset's key.

Was this section helpful?

YesNo

get

## /admin/api/2026-01/themes/828155753/assets.json?asset[key]=templates/index.liquid

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/themes/828155753/assets.json?asset%5Bkey%5D=templates%2Findex.liquid" \

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

"asset": {

"key": "templates/index.liquid",

"public_url": null,

"value": "<!-- LIST 3 PER ROW -->\n<h2>Featured Products</h2>\n<table id=\"products\" cellspacing=\"0\" cellpadding=\"0\">\n {% tablerow product in collections.frontpage.products cols:3 %}\n <a href=\"{{product.url}}\">{{ product.featured_image | product_img_url: 'small' | img_tag }}</a>\n <h3><a href=\"{{product.url}}\">{{product.title}}</a></h3>\n <ul class=\"attributes\">\n <li><span class=\"money\">{{product.price_min | money}}</span></li>\n </ul>\n {% endtablerow %}\n</table>\n<!-- /LIST 3 PER ROW -->\n\n{{ content_for_index }}\n\n<div id=\"articles\">\n {% assign article = pages.frontpage %}\n <div class=\"article\">\n {% if article.content != \"\" %}\n <h3>{{ article.title }}</h3>\n <div class=\"article-body textile\">\n {{ article.content }}\n </div>\n {% else %}\n <div class=\"article-body textile\">\n In <em>Admin > Blogs & Pages</em>, create a page with the handle <strong><code>frontpage</code></strong> and it will show up here.\n <br />\n  {{ \"Learn more about handles\" | link_to: \"http://wiki.shopify.com/Handle\" }}\n </div>\n {% endif %}\n </div>\n</div>\n",

"created_at": "2010-07-12T15:31:50-04:00",

"updated_at": "2010-07-12T15:31:50-04:00",

"content_type": "application/x-liquid",

"size": 1068,

"checksum": null,

"theme_id": 828155753

}

}

### examples

  * #### Retrieve a Liquid template

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/themes/828155753/assets.json?asset%5Bkey%5D=templates%2Findex.liquid" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Asset.all({
          session: session,
          theme_id: 828155753,
          asset: {"key": "templates/index.liquid"},
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Asset.all(
          session: test_session,
          theme_id: 828155753,
          asset: {"key" => "templates/index.liquid"},
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Asset.all({
          session: session,
          theme_id: 828155753,
          asset: {"key": "templates/index.liquid"},
        });

#### response

        HTTP/1.1 200 OK{"asset":{"key":"templates/index.liquid","public_url":null,"value":"<!-- LIST 3 PER ROW -->\n<h2>Featured Products</h2>\n<table id=\"products\" cellspacing=\"0\" cellpadding=\"0\">\n  {% tablerow product in collections.frontpage.products cols:3 %}\n    <a href=\"{{product.url}}\">{{ product.featured_image | product_img_url: 'small' | img_tag }}</a>\n    <h3><a href=\"{{product.url}}\">{{product.title}}</a></h3>\n    <ul class=\"attributes\">\n      <li><span class=\"money\">{{product.price_min | money}}</span></li>\n    </ul>\n  {% endtablerow %}\n</table>\n<!-- /LIST 3 PER ROW -->\n\n{{ content_for_index }}\n\n<div id=\"articles\">\n  {% assign article = pages.frontpage %}\n  <div class=\"article\">\n    {% if article.content != \"\" %}\n      <h3>{{ article.title }}</h3>\n      <div class=\"article-body textile\">\n        {{ article.content }}\n      </div>\n    {% else %}\n      <div class=\"article-body textile\">\n        In <em>Admin > Blogs & Pages</em>, create a page with the handle <strong><code>frontpage</code></strong> and it will show up here.\n        <br />\n        {{ \"Learn more about handles\" | link_to: \"http://wiki.shopify.com/Handle\" }}\n      </div>\n    {% endif %}\n  </div>\n</div>\n","created_at":"2010-07-12T15:31:50-04:00","updated_at":"2010-07-12T15:31:50-04:00","content_type":"application/x-liquid","size":1068,"checksum":null,"theme_id":828155753}}


* * *

##

[Anchor to PUT request, Creates or updates an asset for a theme](/docs/api/admin-rest/latest/resources/asset#put-themes-theme-id-assets)

put

Creates or updates an asset for a theme

[themeFilesUpsert](/docs/api/admin-graphql/latest/mutations/themeFilesUpsert)

[themeFilesCopy](/docs/api/admin-graphql/latest/mutations/themeFilesCopy?example=creates-or-updates-an-asset-for-a-theme)

Creates or updates an asset for a theme.

In the PUT request, you can include the `src` or `source_key` property to create the asset from an existing file.

###

[Anchor to Parameters of Creates or updates an asset for a theme](/docs/api/admin-rest/latest/resources/asset#put-themes-theme-id-assets-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

theme_id

string**string**

required**required**

* * *

source_key

The path within the theme to an existing asset. Include in the body of the PUT request to create a duplicate asset.

* * *

src

The source URL of an image. Include in the body of the PUT request to upload the image to Shopify.

* * *

Was this section helpful?

YesNo

###

[Anchor to put-themes-theme-id-assets-examples](/docs/api/admin-rest/latest/resources/asset#put-themes-theme-id-assets-examples)Examples

Change an existing Liquid template's value

Path parameters

theme_id=828155753

string**string**

required**required**

Request body

asset

Asset resource**Asset resource**

Show asset properties

asset.key:"templates/index.liquid"

->[filename](/docs/api/admin-graphql/latest/input-objects/OnlineStoreThemeFilesUpsertFileInput#fields-filename)

The path to the asset within a theme. It consists of the file's directory and filename. For example, the asset `assets/bg-body-green.gif` is in the **assets** directory, so its key is `assets/bg-body-green.gif`.

asset.value:"<img src='backsoon-postit.png'><p>We are busy updating the store for you and will be back within the hour.</p>"

->[value](/docs/api/admin-graphql/latest/input-objects/OnlineStoreThemeFileBodyInput#fields-value)

The text content of the asset, such as the HTML and Liquid markup of a template file.

Create an image asset by providing a base64-encoded attachment

Path parameters

theme_id=828155753

string**string**

required**required**

Request body

asset

Asset resource**Asset resource**

Show asset properties

asset.key:"assets/empty.gif"

->[filename](/docs/api/admin-graphql/latest/input-objects/OnlineStoreThemeFilesUpsertFileInput#fields-filename)

The path to the asset within a theme. It consists of the file's directory and filename. For example, the asset `assets/bg-body-green.gif` is in the **assets** directory, so its key is `assets/bg-body-green.gif`.

asset.attachment:"R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==\n"

->[value](/docs/api/admin-graphql/latest/input-objects/OnlineStoreThemeFileBodyInput#fields-value)

A base64-encoded image.

Create an image asset by providing a source URL from which to upload the image

Path parameters

theme_id=828155753

string**string**

required**required**

Request body

asset

Asset resource**Asset resource**

Show asset properties

asset.key:"assets/bg-body.gif"

->[filename](/docs/api/admin-graphql/latest/input-objects/OnlineStoreThemeFilesUpsertFileInput#fields-filename)

The path to the asset within a theme. It consists of the file's directory and filename. For example, the asset `assets/bg-body-green.gif` is in the **assets** directory, so its key is `assets/bg-body-green.gif`.

Duplicate an existing asset by providing a source key

Path parameters

theme_id=828155753

string**string**

required**required**

Request body

asset

Asset resource**Asset resource**

Show asset properties

asset.key:"layout/alternate.liquid"

->[filename](/docs/api/admin-graphql/latest/input-objects/OnlineStoreThemeFilesUpsertFileInput#fields-filename)

The path to the asset within a theme. It consists of the file's directory and filename. For example, the asset `assets/bg-body-green.gif` is in the **assets** directory, so its key is `assets/bg-body-green.gif`.

Was this section helpful?

YesNo

put

## /admin/api/2026-01/themes/828155753/assets.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{"asset":{"key":"templates/index.liquid","value":"<img src='backsoon-postit.png'><p>We are busy updating the store for you and will be back within the hour.</p>"}}' \

-X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/themes/828155753/assets.json" \

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

HTTP/1.1 200 OK

{

"asset": {

"key": "templates/index.liquid",

"public_url": null,

"created_at": "2010-07-12T15:31:50-04:00",

"updated_at": "2026-01-09T22:35:59-05:00",

"content_type": "application/x-liquid",

"size": 110,

"checksum": "cd71db2e14df976c8aa44b44c8dae77b",

"theme_id": 828155753

}

}

### examples

  * #### Change an existing Liquid template's value

#####

        curl -d '{"asset":{"key":"templates/index.liquid","value":"<img src='backsoon-postit.png'><p>We are busy updating the store for you and will be back within the hour.</p>"}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/themes/828155753/assets.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const asset = new admin.rest.resources.Asset({session: session});

        asset.theme_id = 828155753;
        asset.key = "templates/index.liquid";
        asset.value = "<img src='backsoon-postit.png'><p>We are busy updating the store for you and will be back within the hour.</p>";
        await asset.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        asset = ShopifyAPI::Asset.new(session: test_session)
        asset.theme_id = 828155753
        asset.key = "templates/index.liquid"
        asset.value = "<img src='backsoon-postit.png'><p>We are busy updating the store for you and will be back within the hour.</p>"
        asset.save!

#####

        // Session is built by the OAuth process

        const asset = new shopify.rest.Asset({session: session});
        asset.theme_id = 828155753;
        asset.key = "templates/index.liquid";
        asset.value = "<img src='backsoon-postit.png'><p>We are busy updating the store for you and will be back within the hour.</p>";
        await asset.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"asset":{"key":"templates/index.liquid","public_url":null,"created_at":"2010-07-12T15:31:50-04:00","updated_at":"2026-01-09T22:35:59-05:00","content_type":"application/x-liquid","size":110,"checksum":"cd71db2e14df976c8aa44b44c8dae77b","theme_id":828155753}}

  * #### Create an image asset by providing a base64-encoded attachment

#####

        curl -d '{"asset":{"key":"assets/empty.gif","attachment":"R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==\n"}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/themes/828155753/assets.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const asset = new admin.rest.resources.Asset({session: session});

        asset.theme_id = 828155753;
        asset.key = "assets/empty.gif";
        asset.attachment = "R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==\n";
        await asset.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        asset = ShopifyAPI::Asset.new(session: test_session)
        asset.theme_id = 828155753
        asset.key = "assets/empty.gif"
        asset.attachment = "R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==\n"
        asset.save!

#####

        // Session is built by the OAuth process

        const asset = new shopify.rest.Asset({session: session});
        asset.theme_id = 828155753;
        asset.key = "assets/empty.gif";
        asset.attachment = "R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==\n";
        await asset.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"asset":{"key":"assets/empty.gif","public_url":"https://cdn.shopify.com/s/files/1/0005/4838/0009/t/1/assets/empty.gif?v=1768016162","created_at":"2026-01-09T22:36:02-05:00","updated_at":"2026-01-09T22:36:02-05:00","content_type":"image/gif","size":43,"checksum":"45cf913e5d9d3c9b2058033056d3dd23","theme_id":828155753}}

  * #### Create an image asset by providing a source URL from which to upload the image

#####

        curl -d '{"asset":{"key":"assets/bg-body.gif","src":"http://example.com/new_bg.gif"}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/themes/828155753/assets.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const asset = new admin.rest.resources.Asset({session: session});

        asset.theme_id = 828155753;
        asset.key = "assets/bg-body.gif";
        asset.src = "http://example.com/new_bg.gif";
        await asset.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        asset = ShopifyAPI::Asset.new(session: test_session)
        asset.theme_id = 828155753
        asset.key = "assets/bg-body.gif"
        asset.src = "http://example.com/new_bg.gif"
        asset.save!

#####

        // Session is built by the OAuth process

        const asset = new shopify.rest.Asset({session: session});
        asset.theme_id = 828155753;
        asset.key = "assets/bg-body.gif";
        asset.src = "http://example.com/new_bg.gif";
        await asset.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"asset":{"key":"assets/bg-body.gif","public_url":"https://cdn.shopify.com/s/files/1/0005/4838/0009/t/1/assets/bg-body.gif?v=1768016157","created_at":"2010-07-12T15:31:50-04:00","updated_at":"2026-01-09T22:35:57-05:00","content_type":"image/gif","size":43,"checksum":"45cf913e5d9d3c9b2058033056d3dd23","theme_id":828155753}}

  * #### Duplicate an existing asset by providing a source key

#####

        curl -d '{"asset":{"key":"layout/alternate.liquid","source_key":"layout/theme.liquid"}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/themes/828155753/assets.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const asset = new admin.rest.resources.Asset({session: session});

        asset.theme_id = 828155753;
        asset.key = "layout/alternate.liquid";
        asset.source_key = "layout/theme.liquid";
        await asset.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        asset = ShopifyAPI::Asset.new(session: test_session)
        asset.theme_id = 828155753
        asset.key = "layout/alternate.liquid"
        asset.source_key = "layout/theme.liquid"
        asset.save!

#####

        // Session is built by the OAuth process

        const asset = new shopify.rest.Asset({session: session});
        asset.theme_id = 828155753;
        asset.key = "layout/alternate.liquid";
        asset.source_key = "layout/theme.liquid";
        await asset.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"asset":{"key":"layout/alternate.liquid","public_url":null,"created_at":"2026-01-09T22:36:01-05:00","updated_at":"2026-01-09T22:36:01-05:00","content_type":"application/x-liquid","size":3049,"checksum":"1879a06996941b2ff1ff485a1fe60a97","theme_id":828155753}}


* * *

##

[Anchor to DELETE request, Deletes an asset from a theme](/docs/api/admin-rest/latest/resources/asset#delete-themes-theme-id-assets?asset\[key\]=assets-bg-body.gif)

del

Deletes an asset from a theme

[themeFilesDelete](/docs/api/admin-graphql/latest/mutations/themeFilesDelete?example=deletes-an-asset-from-a-theme)

Deletes an asset from a theme.

###

[Anchor to Parameters of Deletes an asset from a theme](/docs/api/admin-rest/latest/resources/asset#delete-themes-theme-id-assets?asset\[key\]=assets-bg-body.gif-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

asset[key]

required**required**

≤ 100**≤ 100**

Deletes a single asset from a theme by specifying the asset's key.

* * *

theme_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to delete-themes-theme-id-assets?asset[key]=assets-bg-body.gif-examples](/docs/api/admin-rest/latest/resources/asset#delete-themes-theme-id-assets?asset\[key\]=assets-bg-body.gif-examples)Examples

Delete an image from a theme

Query parameters

asset[key]=assets/bg-body.gif

required**required**

≤ 100**≤ 100**

Deletes a single asset from a theme by specifying the asset's key.

Deleting an asset required by the theme fails with an error

Query parameters

asset[key]=layout/theme.liquid

required**required**

≤ 100**≤ 100**

Deletes a single asset from a theme by specifying the asset's key.

Was this section helpful?

YesNo

del

## /admin/api/2026-01/themes/828155753/assets.json?asset[key]=assets/bg-body.gif

cURLRemixRubyNode.js

Copy

9

1

2

curl -X DELETE "https://your-development-store.myshopify.com/admin/api/2026-01/themes/828155753/assets.json?asset%5Bkey%5D=assets%2Fbg-body.gif" \

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

"message": "assets/bg-body.gif was successfully deleted"

}

### examples

  * #### Delete an image from a theme

#####

        curl -X DELETE "https://your-development-store.myshopify.com/admin/api/2026-01/themes/828155753/assets.json?asset%5Bkey%5D=assets%2Fbg-body.gif" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Asset.delete({
          session: session,
          theme_id: 828155753,
          asset: {"key": "assets/bg-body.gif"},
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Asset.delete(
          session: test_session,
          theme_id: 828155753,
          asset: {"key" => "assets/bg-body.gif"},
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Asset.delete({
          session: session,
          theme_id: 828155753,
          asset: {"key": "assets/bg-body.gif"},
        });

#### response

        HTTP/1.1 200 OK{"message":"assets/bg-body.gif was successfully deleted"}

  * #### Deleting an asset required by the theme fails with an error

#####

        curl -X DELETE "https://your-development-store.myshopify.com/admin/api/2026-01/themes/828155753/assets.json?asset%5Bkey%5D=layout%2Ftheme.liquid" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Asset.delete({
          session: session,
          theme_id: 828155753,
          asset: {"key": "layout/theme.liquid"},
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Asset.delete(
          session: test_session,
          theme_id: 828155753,
          asset: {"key" => "layout/theme.liquid"},
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Asset.delete({
          session: session,
          theme_id: 828155753,
          asset: {"key": "layout/theme.liquid"},
        });

#### response

        HTTP/1.1 403 Forbidden{"message":"layout/theme.liquid could not be deleted"}