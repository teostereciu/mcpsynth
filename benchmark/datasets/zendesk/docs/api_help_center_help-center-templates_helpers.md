# Helpers

*Source: https://developer.zendesk.com/api-reference/help_center/help-center-templates/helpers/*

---

## On this page

  * [Helpers](/api-reference/help_center/help-center-templates/helpers/#helpers)
  * [Built-in helpers](/api-reference/help_center/help-center-templates/helpers/#built-in-helpers)
  * [Global helpers](/api-reference/help_center/help-center-templates/helpers/#global-helpers)
  * [Shared helpers](/api-reference/help_center/help-center-templates/helpers/#shared-helpers)
  * [asset helper](/api-reference/help_center/help-center-templates/helpers/#asset-helper)
  * [calc helper](/api-reference/help_center/help-center-templates/helpers/#calc-helper)
  * [concat helper](/api-reference/help_center/help-center-templates/helpers/#concat-helper)
  * [contains helper](/api-reference/help_center/help-center-templates/helpers/#contains-helper)
  * [compare helper](/api-reference/help_center/help-center-templates/helpers/#compare-helper)
  * [date helper](/api-reference/help_center/help-center-templates/helpers/#date-helper)
  * [dc (dynamic content) helper](/api-reference/help_center/help-center-templates/helpers/#dc-dynamic-content-helper)
  * [excerpt helper](/api-reference/help_center/help-center-templates/helpers/#excerpt-helper)
  * [filter helper](/api-reference/help_center/help-center-templates/helpers/#filter-helper)
  * [is helper](/api-reference/help_center/help-center-templates/helpers/#is-helper)
  * [isnt helper](/api-reference/help_center/help-center-templates/helpers/#isnt-helper)
  * [json helper](/api-reference/help_center/help-center-templates/helpers/#json-helper)
  * [json_stringify helper](/api-reference/help_center/help-center-templates/helpers/#json_stringify-helper)
  * [link helper](/api-reference/help_center/help-center-templates/helpers/#link-helper)
  * [not helper](/api-reference/help_center/help-center-templates/helpers/#not-helper)
  * [page_path helper](/api-reference/help_center/help-center-templates/helpers/#page_path-helper)
  * [search helper](/api-reference/help_center/help-center-templates/helpers/#search-helper)
  * [slice helper](/api-reference/help_center/help-center-templates/helpers/#slice-helper)
  * [user_avatar helper](/api-reference/help_center/help-center-templates/helpers/#user_avatar-helper)
  * [user_name helper](/api-reference/help_center/help-center-templates/helpers/#user_name-helper)
  * [t (translation) helper](/api-reference/help_center/help-center-templates/helpers/#t-translation-helper)
  * [breadcrumbs helper](/api-reference/help_center/help-center-templates/helpers/#breadcrumbs-helper)
  * [form helper](/api-reference/help_center/help-center-templates/helpers/#form-helper)
  * [pagination helper](/api-reference/help_center/help-center-templates/helpers/#pagination-helper)
  * [share helper](/api-reference/help_center/help-center-templates/helpers/#share-helper)
  * [subscribe helper](/api-reference/help_center/help-center-templates/helpers/#subscribe-helper)
  * [vote helper](/api-reference/help_center/help-center-templates/helpers/#vote-helper)
  * [change_password helper](/api-reference/help_center/help-center-templates/helpers/#change_password-helper)
  * [my_profile helper](/api-reference/help_center/help-center-templates/helpers/#my_profile-helper)


# Helpers

## On this page

  * [Helpers](/api-reference/help_center/help-center-templates/helpers/#helpers)
  * [Built-in helpers](/api-reference/help_center/help-center-templates/helpers/#built-in-helpers)
  * [Global helpers](/api-reference/help_center/help-center-templates/helpers/#global-helpers)
  * [Shared helpers](/api-reference/help_center/help-center-templates/helpers/#shared-helpers)
  * [asset helper](/api-reference/help_center/help-center-templates/helpers/#asset-helper)
  * [calc helper](/api-reference/help_center/help-center-templates/helpers/#calc-helper)
  * [concat helper](/api-reference/help_center/help-center-templates/helpers/#concat-helper)
  * [contains helper](/api-reference/help_center/help-center-templates/helpers/#contains-helper)
  * [compare helper](/api-reference/help_center/help-center-templates/helpers/#compare-helper)
  * [date helper](/api-reference/help_center/help-center-templates/helpers/#date-helper)
  * [dc (dynamic content) helper](/api-reference/help_center/help-center-templates/helpers/#dc-dynamic-content-helper)
  * [excerpt helper](/api-reference/help_center/help-center-templates/helpers/#excerpt-helper)
  * [filter helper](/api-reference/help_center/help-center-templates/helpers/#filter-helper)
  * [is helper](/api-reference/help_center/help-center-templates/helpers/#is-helper)
  * [isnt helper](/api-reference/help_center/help-center-templates/helpers/#isnt-helper)
  * [json helper](/api-reference/help_center/help-center-templates/helpers/#json-helper)
  * [json_stringify helper](/api-reference/help_center/help-center-templates/helpers/#json_stringify-helper)
  * [link helper](/api-reference/help_center/help-center-templates/helpers/#link-helper)
  * [not helper](/api-reference/help_center/help-center-templates/helpers/#not-helper)
  * [page_path helper](/api-reference/help_center/help-center-templates/helpers/#page_path-helper)
  * [search helper](/api-reference/help_center/help-center-templates/helpers/#search-helper)
  * [slice helper](/api-reference/help_center/help-center-templates/helpers/#slice-helper)
  * [user_avatar helper](/api-reference/help_center/help-center-templates/helpers/#user_avatar-helper)
  * [user_name helper](/api-reference/help_center/help-center-templates/helpers/#user_name-helper)
  * [t (translation) helper](/api-reference/help_center/help-center-templates/helpers/#t-translation-helper)
  * [breadcrumbs helper](/api-reference/help_center/help-center-templates/helpers/#breadcrumbs-helper)
  * [form helper](/api-reference/help_center/help-center-templates/helpers/#form-helper)
  * [pagination helper](/api-reference/help_center/help-center-templates/helpers/#pagination-helper)
  * [share helper](/api-reference/help_center/help-center-templates/helpers/#share-helper)
  * [subscribe helper](/api-reference/help_center/help-center-templates/helpers/#subscribe-helper)
  * [vote helper](/api-reference/help_center/help-center-templates/helpers/#vote-helper)
  * [change_password helper](/api-reference/help_center/help-center-templates/helpers/#change_password-helper)
  * [my_profile helper](/api-reference/help_center/help-center-templates/helpers/#my_profile-helper)


## Helpers

Helpers are template expressions that perform certain actions. Help Center has the following kinds of helpers:

  * Built-in helpers \- block helpers from Handlebars available in all templates
  * Global helpers \- custom helpers available in all templates
  * Shared helpers \- custom helpers available only in specific templates
  * [Advanced helpers](/api-reference/help_center/help-center-templates/advanced_helpers) \- global and shared custom helpers that provide advanced functionality


Zendesk recommends using the most recent version of the Template API whenever possible. Unless specified otherwise, an example using a specific Templating API version is compatible with subsequent versions. For instance, if an example specifies V2, it also applies to V3 and later versions. However, if an example specifies both V2 and V3, then V3 differs from V2.

**Note:** Some helpers output different HTML based on your theme's Templating API version. These differences are noted in the helper's documentation. To check your theme's version, see [About Guide templating versions](https://support.zendesk.com/hc/en-us/articles/4408820214554) in Zendesk help.

### Built-in helpers

Help Center templates support the following built-in Handlebars block helpers:

  * `if`
  * `unless`
  * `each`
  * `with`


To learn how to use them, see [Handlebars built-in helpers](https://handlebarsjs.com/guide/builtin-helpers.html) in the Handlebars docs.

### Global helpers

In addition to the built-in Handlebars helpers listed above, Help Center provides the following custom helpers, available in all templates:

  * asset
  * calc
  * compare
  * concat
  * contains
  * date
  * dc
  * excerpt
  * filter
  * is
  * isnt
  * json
  * json_stringify
  * link
  * not
  * page_path
  * slice
  * search
  * t
  * user_avatar
  * user_name


### Shared helpers

There are also some other custom helpers that are page specific and therefore are only available in certain pages:

  * breadcrumbs
  * form
  * pagination
  * share
  * subscribe
  * vote
  * change_password
  * my_profile


### asset helper

`{{asset 'filename'}}`

Inserts the relative path of the specified asset.

#### Parameters

  * `filename` the filename of the asset


#### Attributes

  * `prefix` (optional) adds a prefix to the filename.
  * `suffix` (optional) adds a suffix to the filename.
  * `cdn="legacy"` (optional) specifies whether or not to use the legacy CDN for this asset to maintain legacy behavior for older themes. Only available for customers who migrated a theme to the new theming experience. For any new customers who created a Help Center after November 2017, this attribute is not necessary and should not be set.


#### Availability

  * All pages


#### Example


    <script src="{{asset 'jquery_plugin.js'}}"></script>
    <img src="{{asset 'background_image.png'}}" /><img src="{{asset category.id prefix='image-' suffix='.png'}}" />

#### Output


    <script src="/zendesk_cdn_path/jquery_plugin.js"></script>
    <img src="/zendesk_cdn_path/background_image.png" /><img src="/zendesk_cdn_path/image-12345.png" />

### calc helper

`(calc left "operator" right)`

[Subexpression](/api-reference/help_center/help-center-templates/introduction/#subexpressions) that returns the result of an arithmetic operation. If the operation is invalid and cannot be safely performed, `nil` is returned.

You can also use the helper in a normal expression:

`{{calc 1 "+" 1}}`

The example renders `2`.

#### Parameters

  * `left` the left operand of the arithmetic operation.
  * `operator` one of `+`, `-`, `*`, `/`, `%`, `**`.
  * `right` the right operand of the arithmetic operation.


#### Attributes

  * `float` (optional, boolean) the operation is performed with floating-point arithmetics. Default: `false`.


#### Availability

  * All pages


#### Example


    You have {{calc settings.badge_count "-" user.badges.length)}} badges left to earn.

#### Output

Given `settings.badge_count` is `25` and `user.badges.length` is `10`:


    You have 15 badges left to earn.

### concat helper

`(concat "foo" "bar")`

[Subexpression](/api-reference/help_center/help-center-templates/introduction/#subexpressions) that concatenates up to 10 string arguments. Any argument beyond the 10th string is ignored. If any of the arguments are not strings, the helper returns `nil`.

You can use the helper in a normal expression:

`{{concat "foo" "bar"}}`

The example renders `foobar`.

#### Parameters

  * `str1` (optional, string) First string to concatenate
  * `str2` (optional, string) Second string to concatenate
  * `strN` (optional, string) Nth string to concatenate


#### Attributes

None.

#### Availability

  * All pages


#### Example


    {{concat "a" "b" "c"}}

#### Output


    abc

### contains helper


    {{#contains haystack needle}}  ...{{/contains}}

Use the `contains` helper to check if one string is contained within another, and execute a template block conditionally. The expression evaluates `true` if the `needle` can be found within the `haystack`. Otherwise, it returns `false`. The check is case-sensitive.

If the expression evaluates to `true`, the `contains` block is executed, if given. Otherwise, the `else` block is executed, if given.

#### Parameters

  * `haystack` (required, string)
  * `needle` (required, string)


#### Attributes

None.

#### Availability

  * All pages


#### Example


    {{#contains article.title "Urgent"}}  <strong>{{article.title}}</strong>{{else}}  {{article.title}}{{/contains}}

### compare helper

`(compare left "operator" right)`

[Subexpression](/api-reference/help_center/help-center-templates/introduction/#subexpressions) that returns a boolean value representing the comparison result of 2 operands using a binary operator. If the operation is invalid and therefore cannot be safely performed, the helper returns `nil`.

You can also use the helper in a regular expression:

`{{compare 1 "=" 2}}`

The example renders `false`.

#### Parameters

  * `left` the left operand of the comparison.
  * `operator` one of the following: `==`, `>`, `>=`, `<`, `<=`.
  * `right` the right operand of the comparison.


#### Attributes

None.

#### Availability

  * All pages


#### Example


    {{#if (compare user.badges.length ">" 0)}}  You have earned {{user.badges.length}} badges!{{else}}  You have not earned any badges, yet.{{/if}}

#### Output

Given the user has earned 2 badges:


    You have earned 2 badges!

### date helper

`{{date timestamp}}`

Formats a timestamp into a human-friendly string. The formatted string is localized for the supported languages.

#### Parameters

  * `timestamp` an ISO8601 timestamp such as "2015-04-23T13:32:58Z", typically expressed as a Help Center datetime property such as `article.created_at`


#### Attributes

  * `format` (optional, string) displays the date in a specific format. Can be any of the following values: `short`, `medium`, `long` and `full`
  * `timeago` (optional, boolean) if `true`, inserts the date as time elapsed since the present. Example: "2 months ago". Default is `false`. Only one formatting option (either `format` or `timeago`) can be specified at a time. `format` will take precedence if both are specified
  * `class` (optional, string) the HTML class to render


#### `format` options

You can use any of the following available formats to control the display of date and time stamps. The examples are for the en-us locale, but the formats will differ based on the locale setting.

Format| Example| Description
---|---|---
`short`| 09/14/2015| A compact format only showing date
`medium`| January 2nd 2016| A date only format displaying full month name
`long`| March 3rd 2015 11:45| A long format displaying full month name and time stamp
`full`| Thursday, June 9th 2016 11:45| Same as `long`, but also shows the full name of the day

#### Availability

  * All pages


#### Example


    {{date article.created_at class='metadata'}}{{date article.created_at class='metadata' timeago=true}}{{date article.created_at class='metadata' format='short'}}

#### Output


    <!-- Text will be localized --><time datetime="2015-01-23T13:32:58Z" class="metadata">January 23, 2015 13:32</time><time datetime="2015-01-23T13:32:58Z" class="metadata">2 months ago</time><time datetime="2015-01-23T13:32:58Z" class="metadata">01/23/2015</time>

### dc (dynamic content) helper

`{{dc 'identifier'}}`

Use the `dc` helper to show dynamic content translated according to the current locale.

#### Parameters

  * `identifier` indicates the dynamic content to be inserted and translated


If `identifier` doesn't exist, a default message is shown.

See this [article](https://support.zendesk.com/hc/en-us/articles/203661426-Change-your-Help-Center-design-using-Dynamic-Content) to learn how to add new dynamic content.

#### Attributes

None.

#### Availability

  * All pages


#### Example


    {{dc 'example'}}
    {{dc 'foo'}}

#### Output

Supposing that `example` is defined as dynamic content and `foo` is not:


    <!-- 'example' was found, localized content is shown -->This is an example.
    <!-- 'foo' not found, default message is shown -->Could not find the placeholder for dynamic content named foo

### excerpt helper

`{{excerpt string}}`

Inserts the first few lines of a content item such as an article or post. If the argument contains any HTML tags, they will be stripped out before the text truncation takes place.

#### Parameters

  * `string` a content item, usually expressed as a Help Center content property such as `article.body`


#### Attributes

  * `characters` (optional, integer) the number of characters to display from the start of the item. Default is 120


#### Availability

  * All pages


#### Example


    {{excerpt article.body characters=100}}

#### Output


    <!-- First 100 characters of the article body followed by "..." -->Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqu...

### filter helper

`(filter collection on="property_name" attribute="string")`

[Subexpression](/api-reference/help_center/help-center-templates/introduction/#subexpressions) that returns a collection on the specified property, containing those items where _all_ of the specified conditions match. Returns an empty collection in case of an error. Omitting `on` or specifying an unknown property name will cause an error. Specifying an attribute not listed in Attributes below will cause an error.

#### Parameters

  * `collection` an array of Curlybars objects such as `user.badges`
  * `attribute` a condition such as `starts_with` or `contains`. See Attributes below for the full list


#### Attributes

  * `on` (required, string) a string representing the property of the objects in the collection. The value of that property is the subject to the filtering rules. You can use dot notation to access nested properties. Example: `author.name`. All the remaining attributes are interpreted as filters to be applied to the specified property.
  * `starts_with` (optional, string) a string value representing the asserted prefix of the subject.
  * `ends_with` (optional, string) a string value representing the asserted suffix of the subject.
  * `contains` (optional, string) a string value representing the asserted infix of the subject.
  * `equals` (optional, any) a value representing the asserted identity of the subject.


#### Availability

  * All pages


#### Example


    {{#each (filter user.badges on="category_slug" starts_with="abc" ends_with="cba")}}  Matching badge: {{category_slug}}{{/each}}

#### Output


    Matching badge: abc1cbaMatching badge: abc2cbaMatching badge: abc3cba

### is helper


    {{#is 'left' 'right'}}  ...{{/is}}

Use the `is` helper to execute a template block conditionally, given an expression result. If the comparison evaluates to `true` (the two values are equal), then the `is` block will be executed, if given. Otherwise, if the comparison evaluates to `false`, the `else` block will be executed, if given. The comparison is always based on the `===` JS operator.

#### Parameters

  * `left` value that will be used in the comparison. This is required and can be a path, a string, a number a boolean or a variable
  * `right` value that will be used in the comparison. This is required and can be a path, a string, a number a boolean or a variable


#### Attributes

None.

#### Availability

  * All pages


#### Example


    {{#is article.author.name 'John'}}  The author of the article is John.{{else}}  The author of the article is not John.{{/is}}

### isnt helper


    {{#isnt 'left' 'right'}}  ...{{/isnt}}

Use the `isnt` helper to execute a template block conditionally, given an expression result. If the comparison evaluates to `true` (the two values are not equal), then the `isnt` block will be executed, if given. Otherwise, if the comparison evaluates to `false`, the `else` block will be executed, if given. The comparison is always based on the `!==` JS operator.

#### Parameters

  * `left` value that will be used in the comparison. This is required and can be a path, a string, a number a boolean or a variable
  * `right` value that will be used in the comparison. This is required and can be a path, a string, a number a boolean or a variable


#### Attributes

None.

#### Availability

  * All pages


#### Example


    {{#isnt article.author.name 'John'}}  The author of the article is not John.{{else}}  The author of the article is John.{{/isnt}}

### json helper

Serializes the result of an expression to JSON. It can be used to serialize data for use in JavaScript.


    {{json 'expression'}}

#### Parameters

  * `expression` a Curlybars expression


The expression can be a property, a path expression, or a subexpression. The result of the expression is serialized to JSON. For example, a boolean value or a number is serialized as is, a string is serialized enclosed in double quotes and escaped properly, while an object or an array is serialized as JSON objects or arrays.

Some expressions are not allowed:

  * Expressions that contain a block helper (for example `{{json (#is help_center.locale 'en-us')}}`)
  * `this` keyword when targeting the page context (for example `{{json this}}` outside a block helper)
  * Subexpressions working on collections (for example `{{json (filter user.badges on="category_slug" starts_with="abc" ends_with="cba")}}`)


It is possible to serialize a helper that returns some HTML code (for example `{{json breadcrumbs}}`), but this is strongly discouraged because it is possible to introduce XSS vulnerabilities depending on how the HTML code is used from JavaScript.

#### Attributes

None.

#### Availability

  * All pages, with Templating API v4 and above


#### Example


    <script>  var signedIn = {{json signed_in}};  var locale = {{json help_center.locale}};  var articleLocationLabel = {{json (t 'article_location_with_title' title="Hello world")}};  var settings = {{json settings}};  var ticketForms = {{json ticket_forms}};</script>

#### Output


    <script>  var signedIn = true;  var locale = "en-us";  var articleLocationLabel = "Location of the article titled \"Hello world\"";  var settings = {      "brand_color": "#17494D",      "brand_text_color": "#FFFFFF",      // ... other theme settings  };  var ticketForms = [{      "id": 123,      "display_name": "First Ticket Form",      "url": "/hc/en-us/requests/new?ticket_form_id=123"  }, {      "id": 456,      "display_name": "Second Ticket Form",      "url": "/hc/en-us/requests/new?ticket_form_id=456"  }];</script>

### json_stringify helper

Converts a normal string into a JSON string that you can use in your JavaScript.


    {{json_stringify 'string'}}

#### Parameters

  * `string` a normal string with unescaped newlines, quotes, or unicode characters


#### Attributes

None.

#### Availability

  * All pages


#### Example


    <script>  var title = {{json_stringify article.title}};</script>

#### Output


    <script>  var title = "Setting the \"enduser\" value";</script>

### link helper

`{{link 'identifier'}}`

Use the `link` helper to link to other pages in Help Center. This helper is available in all page templates.

This will render both the HTML tag and link text. A default string in the proper locale is used for the link text. For example, the `new_request` identifier will render the default "Submit a Request" string as a link. You can also customize the string by using the block version of the `link` helper. Example:


    {{#link 'identifier'}}  Custom link text{{/link}}

If you only need a URL, see the page_path helper.

The link helper also takes care of hiding the link from certain users. For example, in a restricted Help Center you may want to hide the "Submit a Request" link from unregistered users. You can display alternative text when the link is hidden. Example:


    {{#link 'identifier'}}  Link text{{else}}  This link is not available for you{{/link}}

Note that the alternative text won't be wrapped in a link tag.

#### Parameters

  * `identifier` indicates the destination page to link to


You can link to the following destination pages:

Identifier| Destination page
---|---
`help_center`| Help Center Home page
`new_request`| New Request page
`my_activities`| My Activity page
`requests`| Request List page
`request`| Request page
`contributions`| Contributions page
`subscriptions`| Following page
`community`| Community main page
`topics`| Topics page
`sign_in`| Sign-in page
`sign_out`| Sign-out page
`user_profile`| User profile page for a specific user
`posts`| Posts page
`search_result`| Search results page
`survey_response`| Survey response page
`service_catalog`| Service list page
`approval_requests`| Approval requests page

#### Attributes

Varies from identifier to identifier. See below.

#### Availability

  * All pages


#### Example


    {{link 'new_request' class='submit-a-request' role='button'}}
    {{#link "my_activities" class="my-activities" role="button"}}  {{t "my_activites"}}{{else}}  <span>Activities are not available for you</span>{{/link}}

#### Output


    <a href="/new_request" class="submit-a-request" role="button">  Submit a Request</a>
    <!-- If user is not allowed to see My Activities page --><span>Activities are not available for you</span>

#### Link identifiers

##### help_center link

`{{link 'help_center'}}`

Displays a link to the Help Center home page.

###### Attributes

  * `class` (optional, string) an HTML class
  * `role` (optional, string) an HTML role
  * `selected` (optional, string) the HTML aria-selected attribute. Can be "true" or "false"
  * `target` (optional, string) the HTML target attribute


###### Availability

  * All templates


###### Example


    {{link 'help_center' class='help-center-link'}}

##### new_request link

`{{link 'new_request'}}`

Displays a link to the page for submitting a new request.

If you use [ticket forms](https://support.zendesk.com/hc/en-us/articles/203661616) (available in the Enterprise plan), you can link to a specific ticket form with the `ticket_form_id` attribute. You can get the id from the administrator interface in Zendesk Support or from the [Ticket forms API](/api-reference/ticketing/tickets/ticket_forms/#list-ticket-forms).

###### Attributes

  * `class` (optional, string) an HTML class
  * `role` (optional, string) an HTML role
  * `selected` (optional, string) the HTML aria-selected attribute. Can be "true" or "false"
  * `target` (optional, string) the HTML target attribute
  * `ticket_form_id` (optional, string) the id of the ticket form to display. Requires a ticket form that's visible to end users. Available only on the Enterprise plan.


###### Availability

  * All templates


###### Examples


    {{link 'new_request' class='submit-a-request' role='button'}}
    <!-- referencing a specific ticket form -->{{link 'new_request' ticket_form_id='1234'}}

##### my_activities link

`{{link 'my_activities'}}`

Displays a link to the page with the end user's activities. If signed in as an agent or Help Center manager, the link is not displayed.

###### Attributes

  * `class` (optional, string) an HTML class
  * `role` (optional, string) an HTML role
  * `selected` (optional, string) the HTML aria-selected attribute. Can be "true" or "false"
  * `target` (optional, string) the HTML target attribute


###### Availability

  * All templates


###### Example


    {{link 'my_activities' class='my-activities' role='button'}}

##### requests link

`{{link 'requests'}}`

Displays a link to the page listing the end user's requests. The link is not displayed if the user is anonymous.

###### Attributes

  * `class` (optional, string) an HTML class
  * `role` (optional, string) an HTML role
  * `selected` (optional, string) the HTML aria-selected attribute. Can be "true" or "false"
  * `sort_by` (optional, string) the request attribute to sort by. Valid values: `created_at` and `updated_at`.
  * `target` (optional, string) the HTML target attribute


###### Availability

  * All templates


###### Example


    {{link 'requests' class='requests-link'}}

##### request link

Displays a link to the page showing a single request.

###### Attributes

  * `id` (required, integer) the id of a request
  * `class` (optional, string) an HTML class
  * `target` (optional, string) the HTML target attribute


###### Availability

  * All templates


###### Example


    {{link 'request' id=request.id, class='followup-link'}}

##### contributions link

`{{link 'contributions'}}`

Displays a link to the page listing the end user's community contributions. The link is not displayed if the user is anonymous.

###### Attributes

  * `class` (optional, string) an HTML class
  * `role` (optional, string) an HTML role
  * `selected` (optional, string) the HTML aria-selected attribute. Can be "true" or "false"
  * `target` (optional, string) the HTML target attribute


###### Availability

  * All templates


###### Example


    {{link 'contributions' class='contributions-link'}}

##### subscriptions link

`{{link 'subscriptions'}}`

Displays a link to the page listing the content items that the end user is following. The link is not displayed if the user is anonymous.

###### Attributes

  * `class` (optional, string) an HTML class
  * `role` (optional, string) an HTML role
  * `selected` (optional, string) the HTML aria-selected attribute. Can be "true" or "false"
  * `target` (optional, string) the HTML target attribute


###### Availability

  * All templates


###### Example


    {{link 'subscriptions' class='subscriptions-link'}}

##### community link

`{{link 'community'}}`

Displays a link to the community main page. The link is not displayed if the community is disabled.

###### Attributes

  * `class` (optional, string) an HTML class
  * `role` (optional, string) an HTML role
  * `selected` (optional, string) the HTML aria-selected attribute. Can be "true" or "false"
  * `target` (optional, string) the HTML target attribute


###### Availability

  * All templates


###### Example


    {{link 'community' class='community-entrance' role='button'}}

##### topics link

`{{link 'topics'}}`

Displays a link to the page that lists all community topics. The link is not displayed if the community is disabled.

###### Attributes

  * `class` (optional, string) an HTML class
  * `role` (optional, string) an HTML role
  * `selected` (optional, string) the HTML aria-selected attribute. Can be "true" or "false"
  * `target` (optional, string) the HTML target attribute


###### Availability

  * All templates


###### Example


    {{link 'topics' class='community-topics-link' role='button'}}

##### sign_in link

`{{link 'sign_in'}}`

If your Help Center requires users to sign in and the user is not signed-in, displays a link to the page for signing-in.

###### Attributes

  * `class` (optional, string) an HTML class
  * `role` (optional, string) an HTML role
  * `selected` (optional, string) the HTML aria-selected attribute. Can be "true" or "false"
  * `target` (optional, string) the HTML target attribute


###### Availability

  * All templates


###### Example


    {{link 'sign_in' class='submit-a-request'}}

##### sign_out link

`{{link 'sign_out'}}`

Render a link to the home page for signing-out. The link will be hidden in preview mode.

###### Attributes

  * `class` (optional, string) an HTML class
  * `role` (optional, string) an HTML role
  * `selected` (optional, string) the HTML aria-selected attribute. Can be "true" or "false"
  * `target` (optional, string) the HTML target attribute


###### Availability

  * All templates


###### Example


    {{link 'sign_out' class='sign-out'}}

##### user_profile link

`{{link 'user_profile' id=user.id}}`

Displays a link to the user's profile page

  * If user profiles are enabled, links to the user's profile
  * If user profiles are disabled, links to the agent interface if the current user is an agent. Otherwise displays the body without linking


###### Attributes

  * `id` (required, id) the user's id
  * `class` (optional, string) an HTML class
  * `role` (optional, string) an HTML role
  * `selected` (optional, string) the HTML aria-selected attribute. Can be "true" or "false"
  * `target` (optional, string) the HTML target attribute


###### Availability

  * All templates


###### Example

On the User Profile page:


    {{link 'user_profile' id=user.id class='user-profile-link'}}

On the Article Page:


    {{#each comments}}  {{link 'user_profile' id=author.id class='user-profile-link'}}{{/each comments}}

##### posts link

`{{link 'posts'}}`

Displays a link to the posts page.

###### Attributes

  * `class` (optional, string) an HTML class
  * `role` (optional, string) an HTML role
  * `selected` (optional, string) the HTML aria-selected attribute. Can be "true" or "false"
  * `target` (optional, string) the HTML target attribute


###### Availability

  * All templates


###### Example


    {{link 'posts' class='posts-link'}}

##### search result link

`{{link 'search_result'}}`

Displays a link to the search results page. If the `content_tag_id` attribute is used, it links to the search page rendering the results that are tagged with the given content tag.

###### Attributes

  * `class` (optional, string) an HTML class
  * `role` (optional, string) an HTML role
  * `selected` (optional, string) the HTML aria-selected attribute. Can be "true" or "false"
  * `target` (optional, string) the HTML target attribute
  * `content_tag_id` (optional, string) the id of the content tag


###### Availability

  * All templates


###### Example


    {{link 'search_result' class='search-link'}}

##### survey response link

`{{link 'survey_response' id=satisfaction_response.id}}`

Displays a link to the survey response page.

###### Attributes

  * `id` (required, string) the id of the survey response page. There is currently only one type of survey response page, `satisfaction_response` (see example)
  * `class` (optional, string) an HTML class
  * `role` (optional, string) an HTML role
  * `selected` (optional, string) the HTML aria-selected attribute. Can be "true" or "false"
  * `target` (optional, string) the HTML target attribute


###### Availability

  * All templates


###### Example


    {{link 'survey_response' id='01HQR4A69V05DQ0THE4TXNGQHR'}}

##### service catalog link

`{{link 'service_catalog'}}`

Displays a link to the service list page. The helper doesn't return anything if the service catalog is not available.

###### Attributes

  * `class` (optional, string) an HTML class
  * `role` (optional, string) an HTML role
  * `selected` (optional, string) the HTML aria-selected attribute. Can be "true" or "false"
  * `target` (optional, string) the HTML target attribute


###### Availability

  * All templates


###### Example


    {{link 'service_catalog' class='nav-link'}}

##### approval requests link

`{{link 'approval_requests'}}`

Displays a link to the approval requests page. The helper doesn't return anything if the approval requests page is not available.

###### Attributes

  * `class` (optional, string) an HTML class
  * `role` (optional, string) an HTML role
  * `selected` (optional, string) the HTML aria-selected attribute. Can be "true" or "false"
  * `target` (optional, string) the HTML target attribute


###### Availability

  * All templates


###### Example


    {{link 'approval_requests' class='nav-link'}}

### not helper

`(not value)`

[Subexpression](/api-reference/help_center/help-center-templates/introduction/#subexpressions) that returns the negated value of the argument.

#### Parameters

  * `value` the value to be negated.


#### Attributes

None.

#### Availability

  * All pages


#### Example


    {{if (not settings.supress_warnings)}}  You have been warned.{{/if}}

#### Output

Given `settings.supress_warnings` is set to `false`:


    You have been warned.

### page_path helper

`{{page_path 'identifier'}}`

If you don't need the HTML and link text rendered by the link helper, you can use the `page_path` helper. It's available in all Help Center pages.

#### Parameters

  * `identifier` indicates the destination page to link to


The identifiers are the same as the link helper.

#### Attributes

The attributes are also the same, except for the CSS-related ones like `class`, `role` and `selected`, which aren't supported.

###### Availability

  * All pages


#### Example


    {{page_path 'new_request' ticket_form_id='1234'}}

#### Output


    /path_to_request_form

### search helper

`{{search}}`

Inserts a search box.

#### Parameters

None.

#### Attributes

  * `scoped` (optional, boolean) If `scoped` is true and the helper is on the category, section, or article page, searches only the articles in the current category. If the helper is on the topic or post page, searches only the posts in the current topic. Default is false.
  * `submit` (optional, boolean) If true, render the submit button. Default is false.
  * `instant` (optional, boolean) If true, enables [Instant Search](https://support.zendesk.com/hc/en-us/articles/216367358#topic_xqw_dd1_cw) to provide HC article suggestions while you type in the search box. Instant Search article suggestions do not respect the `scoped` parameter if it is set.
  * `class` (optional, string) class name to be added to the form
  * `placeholder` (optional, string) placeholder value for the search input element


#### Availability

  * All pages


#### Example


    {{search}}

#### Output

If inserted in the Home page:


    <form accept-charset="UTF-8" action="/hc/en-us/search" class="search" method="get" role="search">  <input name="utf8" type="hidden" value="&#x2713;" />  <input id="query" name="query" placeholder="Search" type="search" />  <input name="commit" type="submit" value="Search" /></form>

### slice helper

`(slice collection start length)`

[Subexpression](/api-reference/help_center/help-center-templates/introduction/#subexpressions) that returns a sub-array starting at the `start` index and continuing for `length` elements. Negative indices count backward from the end of the array. Returns an empty array if the starting index is out of range.

#### Parameters

  * `collection` an array of Curlybars objects such as `user.badges`.
  * `start` a number representing the start index of the array.
  * `length` a number representing the number of elements to follow after the start index.


#### Attributes

None.

#### Availability

  * All pages


#### Example


    Positive start index:{{#each (slice user.badges 0 3)}}  - Matching badge: {{name}}{{/each}}
    Negative start index:{{#each (slice user.badges -3 3)}}  - Matching badge: {{name}}{{/each}}

#### Output

Given an array of badges with the names: 1, 2, 3, 4, 5:


    Positive start index:- Matching badge: 1- Matching badge: 2- Matching badge: 3
    Negative start index:- Matching badge: 3- Matching badge: 4- Matching badge: 5

### user_avatar helper

`{{user_avatar class='user_avatar'}}`

Use the `user_avatar` helper to insert the current user avatar image. An image is always shown, anonymous users see a default fallback avatar image. For performance reasons Help Center uses a special internal data attribute in the generated HTML image element to load the actual image file using JavaScript.

#### Parameters

None.

#### Attributes

  * `class` (optional, string) a space separated list of class names that will be added to the generated `<img>` tag


#### Availability

  * All pages


#### Example


    {{user_avatar class='rounded-avatar'}}

#### Output


    <img alt="Avatar" class="rounded-avatar" src="https://secure.gravatar.com/avatar/123456" />

### user_name helper

`{{user_name}}`

Use the `user_name` helper to insert the current user name or alias. For performance reasons Help Center uses a special internal data attribute in an empty HTML span element to load the name using JavaScript.

#### Parameters

None.

#### Attributes

None

#### Availability

  * All pages


#### Example


    {{user_name}}

#### Output


    <span data-user-name="[user name or alias]">[user name or alias]</span>

### t (translation) helper

`{{t 'key'}}`

Use the `t` helper to show translated texts for each locale available in your Help Center.

#### Parameters

  * `key` the key for the translated text. See the available keys below.


#### Attributes

Some keys accept one or more of the following optional attributes.

Attribute| Type
---|---
`count`| integer
`content_tag`| string
`due_date`| string
`editor_name`| string
`name`| string
`query`| string
`request_name`| string
`request_number`| integer
`scope_name`| string
`total`| integer
`upvotes`| integer

#### Availability

  * All pages


#### Example


    {{t 'back_to_homepage'}}{{t 'post_count' count=1}}{{t 'show_all_articles' count=section.article_count}}{{t 'found_helpful' upvotes=article.upvote_count total=article.vote_count}}

#### Output


    Take me back to the home page7 postsSee all 13 articles4 out of 5 found this helpful

#### Available keys

You can use any of the following available keys to display translated strings.

Keys| English translation| Notes
---|---|---
`activity_overview`| Activity overview|
`add_comment`| Add comment|
`add_to_conversation`| Add to conversation|
`all`| All|
`all_posts`| All community posts|
`article_location_with_title`| Location of the article titled `%{title}`| Accepts a 'title' attribute.
`articles`| Articles|
`articles_in_section`| Articles in this section|
`assignee`| Assigned to|
`attachments_heading`| Attachments|
`back_to_homepage`| Take me back to the home page|
`badges`| Badges|
`badges_awarded`| Awarded|
`badges_description`| Recently awarded badges to `%{name}`| Accepts a 'name' attribute.
`browse`| browse|
`browse_community`| Community|
`browse_help_center`| Browse Help Center|
`browse_knowledge_base`| Browse Knowledge Base|
`categories`| Categories|
`ccd_requests`| Requests I'm CC'd on|
`ccs`| CCs|
`ccs_description`| The following people will also be notified when this request is updated:|
`comment`| comment/comments| The word 'comment' in singular or plural form. Accepts a 'count' attribute.
`comment_edited`| Edited by `%{editor_name}`| Accepts an 'editor_name' attribute.
`comment_location_with_author_name`| Location of the comment by `%{author_name}`| Accepts an 'author_name' attribute.
`comments`| Comments|
`comments_count`| `%{count}` comment/comments| Accepts a 'count' attribute.
`community`| Community|
`community_topics`| Community Topics|
`content_tags_description`| Add content tags to help people find related content|
`content_tags_label`| Related to|
`contributions`| Contributions|
`download`| Download|
`edited`| Edited|
`empty`| empty|
`external_content_location_with_title`| Location of the external content titled `%{title}`| Accepts a 'title' attribute.
`featured`| Featured|
`featured_posts`| Featured posts|
`filter_by_category`| By Category|
`filter_by_help_center`| By Help Center|
`filter_by_topic`| By Topic|
`filter_by_type`| By Type|
`filter_content_tag`| Related to|
`filter_source`| Source|
`filter_type`| Type|
`followed_by`| Followed by|
`follower_count`| `%{count}` followers| Accepts a 'count' attribute.
`following`| Following|
`following_users`| Following| Signifies that the subject of the subscription is a user instead of content.
`followup`| Follow-up|
`found_helpful`| `%{upvotes}` out of `%{total}` found this helpful| Show number of up votes out of the total. Accepts 'upvotes' and 'total' attributes.
`go_to_comments`| Go to comments section|
`go_to_help_center`| You can also go to the help center home page|
`group`| Group|
`home`| Home|
`home_page`| `%{name}` Help Center home page| Accepts a 'name' attribute.
`internal`| Only visible to agents and managers|
`join_conversation`| Join the conversation|
`knowledge_base`| Knowledge Base|
`mark_as_solved`| Mark as solved|
`mark_as_solved_and_submit`| Mark as solved & Submit|
`member_since`| Member since|
`logo`| Logo|
`latest_activity`| Latest activity by `%{name}`| Accepts a 'name' attribute.
`mistyped_address_or_moved_page`| You have mistyped the address or the page may have moved.|
`more_awards_to`| 1 more awarded badge for `%{name}/%{count}` more awarded badges for `%{name}`| Accepts 'count' and 'name' attributes.
`my_activities`| My activities|
`my_profile`| My profile|
`my_requests`| My requests|
`my_subscriptions`| My subscriptions|
`new_post`| New post|
`no_activity_yet`| No activity yet|
`no_articles`| Nothing here yet. Articles will appear here.|
`no_badges`| You currently have no badges.|
`no_comments`| Nothing here yet. Comments will appear here.|
`no_content`| Nothing to see here yet.|
`no_content_yet`| No content yet. Engage in the conversation to activate your profile.|
`no_contributions`| You currently have no contributions.|
`no_featured_posts`| No featured posts yet.|
`no_posts`| Nothing here yet. Posts will appear here.|
`no_posts_with_filter`| No posts for the selected filter|
`no_requests`| No requests found|
`no_results`| No results for `%{query}`| Accepts a 'query' attribute.
`no_results_unified`| Try searching another keyword.|
`no_results_unified_enter_keywords`| Enter your keywords in the search field.|
`no_results_unified_start_new_search`| Start a new search|
`no_subscriptions`| You currently have no subscriptions|
`nonexistent_page`| The page you were looking for doesn't exist|
`not_authorized`| You're not authorized to access this page.|
`not_following`| You are not following anything yet.|
`official_comment`| Official comment|
`oops`| oops.|
`open_user_in_support`| Open user in Zendesk Support|
`optional`| optional|
`organization`| Organization|
`organization_requests`| Organization requests|
`pagination_next`| Next|
`pagination_previous`| Previous|
`pagination_first`| First|
`pagination_last`| Last|
`pending_approval`| Pending approval|
`pinned`| Pinned|
`plus_more`| `+%{count}` more| Accepts a 'count' attribute.
`post`| Post|
`post_count`| `%{count}` post/posts| Accepts a 'count' attribute.
`post_location_with_title`| Location of the post titled `%{title}`| Accepts a 'title' attribute.
`posts`| Posts|
`preview_result_header`| No results for `%{query}`/Result for `%{query}`/Results for `%{query}`| Accepts a 'query' attribute.
`priority`| Priority|
`private`| Private|
`private_activity`| This user's activity is private.|
`profile`| Profile|
`promoted`| Promoted|
`promoted_articles`| Promoted articles|
`related_articles`| Related articles|
`request`| Request `#%{request_number}`| Accepts a 'request_number' attribute
`requests`| Requests|
`requests_search_results_info`| No results/1 result/`%{count}` results for `%{query}`| Accepts 'count' and 'query' attributes.
`results`| No results/One result/%`{count}` results for `%{query}`| Accepts 'count' and 'query' attributes.
`results_content_tag`| No results/One result/`%{count}` results related to `%{content_tag}`| Accepts 'count' and 'content_tag' attributes.
`results_with_scope`| No results/One result/`%{count}` results for `%{query}` in `%{scope_name}`| Accepts 'count', 'query' and 'scope_name' attributes.
`return_to_top`| Return to top|
`sign_in`| Sign in|
`search`| Search|
`search_clear`| Clear search|
`search_result_source_menu`| Search Result Source Menu|
`search_result_subfilter_menu`| Search Result Subfilters Menu|
`search_result_type_menu`| Search results|
`search_results`| Search results|
`see_all_sections`| See all sections...|
`see_more`| See more|
`see_more_community`| See 1 Community result/See all `%{count}` Community results| Accepts a 'count' attribute.
`see_more_knowledge_base`| See 1 knowledge base result/See all `%{count}` knowledge base results| Accepts a 'count' attribute.
`share`| Share|
`show_all_articles`| See all `%{count}` articles| Accepts a 'count' attribute.
`show_all_posts`| Show all posts|
`show_more_categories`| Show more categories|
`show_more_help_centers`| Show more Help Centers|
`show_more_sources`| Show more sources|
`show_more_topics`| Show more topics|
`show_topics`| Show topics|
`skip_navigation`| Skip to main content|
`sort_by`| Sort by|
`submit`| Submit|
`submit_a_request`| Submit a request|
`submitted_by`| `%{requester_name}` submitted this request| Accepts a 'requester_name' attribute.
`subscriptions`| Subscriptions|
`suggest_new_post`| Didn't find what you were looking for?|
`task_due_date`| (Due on `%{due_date}`)| Accepts a 'due_date' attribute.
`team_member`| User (`%{name}`) is a team member| Accepts a 'name' attribute.
`ticket_details`| Ticket details|
`toggle_navigation`| Toggle navigation menu|
`topics`| Topics|
`total_activity`| Total activity|
`updated`| Updated|
`users_count`| 0 users/1 user/`%{count}` users| Accepts a 'count' attribute.
`view_comment`| View comment|
`vote`| vote/votes| The word 'vote' in singular or plural form. Accepts a 'count' attribute.
`votes`| Votes|
`votes_count`| 0 votes/1 vote/`%{count}` votes| Accepts a 'count' attribute.
`votes_sum`| 0 votes/1 vote/`%{count}` votes| Accepts a 'count' attribute.
`was_this_article_helpful`| Was this article helpful?|
`what_is_your_post_about`| What is your post about?|

Available keys for table headers:

Keys| English translation
---|---
`created`| Created
`requester`| Requester
`id`| Id
`last_activity`| Last Activity
`status`| Status
`subject`| Subject
`subscription`| Following
`title`| Title
`type`| Type
`vote_sum`| Vote Sum

Available keys for form field labels:

Keys| English translation
---|---
`details_label`| Details
`title_label`| Title
`topic_label`| Topic

### breadcrumbs helper

`{{breadcrumbs}}`

Inserts a breadcrumbs navigation element to identify the location of the current page.

#### Parameters

None.

#### Attributes

None.

#### Availability

  * Article page
  * Category page
  * Contributions page
  * Request page
  * Request List page
  * Search Results page
  * Section page
  * Following page
  * New Community Post page
  * New Request page
  * Community Post page
  * Community Topic List page
  * Community Topic page
  * Community Post List page


#### Example


    {{breadcrumbs}}

#### Output

The markup the helper generates depends on several factors, including:

  * The theme's Templating API version
  * The page it's used on
  * The particular articles, sections, and categories in your help center
  * The name of your help center


For example, on the Article page, the following is the helper's output for an article within the subsection "Announcements subsection", the section "Announcements", and the category "General":

v2


    <ol class="breadcrumbs">  <li title="My Help Center">    <a href="/hc/en-us">My Help Center</a>  </li>  <li title="General">    <a href="/hc/en-us/categories/123-General">General</a>  </li>  <li title="Announcements">    <a href="/hc/en-us/sections/456-Announcements">Announcements</a>  </li>  <li title="Announcements subsection">    <a href="/hc/en-us/sections/789-Announcements-subsection">Announcements subsection</a>  </li></ol>

v3 and later


    <nav aria-label="Current location">  <ol class="breadcrumbs">    <li>      <a href="/hc/en-us">My Help Center</a>    </li>    <li>      <a href="/hc/en-us/categories/123-General">General</a>    </li>    <li>      <a href="/hc/en-us/sections/456-Announcements">Announcements</a>    </li>    <li>      <a href="/hc/en-us/sections/789-Announcements-subsection">Announcements subsection</a>    </li>  </ol></nav>

### form helper

Some pages in Help Center include one or more forms. Form helpers simplify building forms and form elements.


    {{#form form_name}}...{{/form}}

This will safely insert an HTML form in the templates. See the page-specific documentation to find out which forms you can use in each template.

You must use the form helpers like `label`, `input`, and `checkbox` to render the form fields. See more below.

#### Parameters

  * `form_name` one of the following: `comment`, `organization`, `post`, `request`, or `requests`


#### Attributes

  * `class` (optional, string) the HTML class to render
  * `id` (optional, string) the HTML id attribute to render


#### Availability

Form| Available in
---|---
comment| Article page
comment| Post page
comment| Request page
organization| Request page
requests_filter| Request List page
post| New Post page

#### Example


    {{#form 'comment' class='comment-form'}}   ...{{/form}}

#### Output

If inserted in an Article page:


    <form class="comment-form" accept-charset="UTF-8" action="/hc/articles/123456/comments" method="post">  <input name="utf8" type="hidden" value="â">  ...</form>

#### Form field helpers

Help Center provides the following form field helpers that must be used inside the form helper:

  * input
  * textarea
  * checkbox
  * label
  * select
  * multiselect
  * required
  * validate
  * error


You can also use these advanced form field helpers:

  * [wysiwyg](/api-reference/help_center/help-center-templates/advanced_helpers#wysiwyg-helper)
  * [token_field](/api-reference/help_center/help-center-templates/advanced_helpers#token_field-helper)


##### Identifiers

Identifiers distinguish similar fields inside the same form. The following identifiers are available:

Identifier| Available in| Form| Field(s)| Description
---|---|---|---|---
body| Article page, Post page and Request page| comment| textarea, wysiwyg| Identifies a text field for content (use [wysiwyg](/api-reference/help_center/help-center-templates/advanced_helpers#wysiwyg-helper) for rich content)
official| Post page| comment| label, checkbox| Identifies a checkbox field to mark a comment as official
title| New Post page| post| label, input| Identifies a text field for the post title
details| New Post page| post| label, wysiwyg| Identifies a text field for content (use [wysiwyg](/api-reference/help_center/help-center-templates/advanced_helpers#wysiwyg-helper) for rich content)
topic| New Post page| post| label, select| Identifies a drop-down to select a topic
content_tags| New Post page| post| label, multiselect| Identifies a drop-down to create or select multiple content tags
mark_as_solved| Request page| comment| label, checkbox| Identifies a checkbox to mark a request as solved
ccs| Request page| comment| token_field| Identifies an email (CC) field
organization| Request page| organization| select| Identifies a drop-down to select an organization
organization| Request List page| requests_filter| label, select| Identifies a drop-down to select an organization
query| Request List page| requests_filter| input| Identifies a search field
status| Request List page| requests_filter| label, select| Identifies a drop-down to select a status

##### input

`{{input 'identifier'}}`

Creates a textbox based on the given identifier.

###### Parameters

  * `identifier` the name of the field (optional). Depends on the page and the form that has the field. See [identifiers](/api-reference/help_center/help-center-templates/helpers#identifiers). In some cases, such as when you want to create a submit button, you don't need an identifier.


###### Attributes

  * `type` (optional, string) the type of the input, valid values are: `text`, `submit`, `email`, `number`. Default is `text`
  * `class` (optional, string) the HTML class to assign to the form
  * `id` (optional, string) the html id (only available if no identifier is given, otherwise the identifier will set this value)
  * `name` (optional, string) the HTML name. Only available if no identifier is given. Otherwise the identifier will set this value
  * `value` (optional, string) the value of the input
  * `label` (optional, string) the HTML placeholder. Only available if no identifier is given. Otherwise the identifier will set this value
  * `autofocus` (optional, boolean) whether the input field is auto-focused or not. False by default
  * `required` (optional, boolean) whether the input field is mandatory or not


###### Examples


    {{input type='submit' name='submit' id='submit-button'}}
    {{input 'first_name' type='text' class='small'}}
    {{input type='text' class='small' id='first_name' name='user[first_name]' label='Please insert your name'}}

##### textarea

`{{textarea 'identifier'}}`

Creates a textarea based on the given identifier.

###### Parameters

  * `identifier` the name of the field (required). Depends on the page and the form that has the field. See [identifiers](/api-reference/help_center/help-center-templates/helpers#identifiers).


###### Attributes

  * `class` (optional, string) the HTML class to assign to the form
  * `rows` (optional, string) specifies the visible height of a text area, in lines
  * `cols` (optional, string) specifies the visible width of a text area


###### Example


    {{textarea 'body' rows='4' class='awesome'}}

##### checkbox

`{{checkbox 'identifier'}}`

Creates a checkbox based on the given identifier.

###### Parameters

  * `identifier` the name of the field (required). Depends on the page and the form that has the field. See [identifiers](/api-reference/help_center/help-center-templates/helpers#identifiers).


###### Attributes

  * `class` (optional, string) the HTML class to assign to the form


###### Example


    {{checkbox 'mark_as_solved' class='red'}}

##### label

`{{label 'identifier'}}`

Creates a label based on the given identifier.

###### Parameters

  * `identifier` the name of the field (required). Depends on the page and the form that has the field. See [identifiers](/api-reference/help_center/help-center-templates/helpers#identifiers).


###### Attributes

  * `class` (optional, string) the HTML class to assign to the form
  * `for` (optional, string) the form element the label is bound to


###### Example


    {{label 'mark_as_solved' for='request-status-select' class='red'}}

##### select

`{{select 'identifier'}}`

Creates a select input based on the given identifier.

The markup this helper generates depends on several factors, including:

  * The identifier
  * The theme's Templating API version


###### Parameters

  * `identifier` the name of the field (required). Depends on the page and the form that has the field. See [identifiers](/api-reference/help_center/help-center-templates/helpers#identifiers).


###### Attributes

  * `class` (optional, string) the HTML class to assign to the form


###### Example


    {{select 'mark_as_solved' class='red'}}

##### multiselect

`{{multiselect 'identifier'}}`

Creates a multiselect input based on the given identifier.

###### Parameters

  * `identifier` the name of the field (required). Depends on the page and the form that has the field. See [identifiers](/api-reference/help_center/help-center-templates/helpers#identifiers).


###### Example


    {{multiselect 'content_tags'}}

##### required


    {{#required 'identifier'}}  block{{/required}}

Executes the block if the 'identifier' field is required.

###### Parameters

  * `identifier` the name of the field (required). Depends on the page and the form that has the field. See [identifiers](/api-reference/help_center/help-center-templates/helpers#identifiers).


###### Example


    {{#required 'mark_as_solved'}}  This is required.{{else}}  This is not required.{{/required}}

##### validate


    {{#validate 'identifier'}}  block{{/validate}}

Executes the block if the 'identifier' field has errors.

###### Parameters

  * `identifier` the name of the field (required). Depends on the page and the form that has the field. See [identifiers](/api-reference/help_center/help-center-templates/helpers#identifiers).


###### Example


    {{#validate 'mark_as_solved'}}  The data introduced has errors.{{else}}  The data introduced is right.{{/validate}}

##### error

`{{error 'identifier'}}`

Renders the error message associated with the given identifier, if any.

###### Parameters

  * `identifier` the name of the field (required). Depends on the page and the form that has the field. See [identifiers](/api-reference/help_center/help-center-templates/helpers#identifiers).


###### Example


    {{error 'mark_as_solved'}}

### pagination helper

`{{pagination}}`

Renders pagination elements that let a user browse more than one page.

This will only render if the number of elements is greater than the size of a page.

#### Parameters

  * `identifier` indicates the array to paginate. Only available in the section page.


The following identifiers are available:

Identifier| Available in| Description
---|---|---
section.articles| Section page| Shows pagination controls for articles of a section. Default value.
section.sections| Section page| Shows pagination controls for sections of a section.

#### Attributes

None.

#### Availability

  * Home page
  * Article page
  * Contributions page
  * Request List page
  * Search Results page
  * Section page


#### Example


    {{pagination}}

#### Output

On the second page if inserted in a Section page:


    <nav class="pagination">  <ul>    <li class="pagination-first">      <a href="/hc/en-us/sections/123-MySection">Â«</a>    </li>    <li class="pagination-prev">      <a href="/hc/en-us/sections/123-MySection" rel="prev">â¹</a>    </li>    <li>      <a href="/hc/en-us/sections/123-MySection" rel="prev">1</a>    </li>    <li class="pagination-current">      <span>2</span>    </li>    <li>      <a href="/hc/en-us/sections/123-MySection?page=3" rel="next">3</a>    </li>    <li class="pagination-next">      <a href="/hc/en-us/sections/123-MySection?page=3" rel="next">âº</a>    </li>    <li class="pagination-last">      <a href="/hc/en-us/sections/123-MySection?page=3">Â»</a>    </li>  </ul></nav>

### share helper

`{{share}}`

Adds elements for sharing content on social media.

#### Parameters

None.

#### Attributes

None.

#### Availability

  * Article page


#### Example


    {{share}}

#### Output

If inserted in an Article page:


    <ul class="share">  <li><a href="[sharing url to Facebook]" class="share-facebook">Facebook</a></li>  <li><a href="[sharing url to Twitter]" class="share-twitter">Twitter</a></li>  <li><a href="[sharing url to LinkedIn]" class="share-linkedin">LinkedIn</a></li>  <li><a href="[sharing url to Google]" class="share-googleplus">Google+</a></li></ul>

Note that the sharing urls might change in the future if the social media service changes their sharing API.

### subscribe helper

`{{subscribe}}`

Inserts a "Follow" button that gives visitors the option of receiving update notifications by email. A section follower is notified when somebody adds an article or comment. A topic follower is notified when somebody adds a post or a comment. An article or post follower is notified when somebody adds a comment. An organization follower is notified when somebody in the same organization creates a new request. A user follower is notified when the user adds an article, post, or comment.

#### Parameters

None.

#### Availability

  * Section page
  * Article page
  * Topic page
  * Post page
  * Request List page
  * User Profile page


#### Example


    {{subscribe}}

#### Output

In article page, if user is not subscribed:


    <button data-selected="false" aria-expanded="true" aria-haspopup="menu" type="button" id="[element id]">Follow</button>

In article page, if user is subscribed:


    <button data-selected="true" aria-expanded="true" aria-haspopup="menu" type="button" id="[element id]">Unfollow</button>

### vote helper

`{{vote 'element' class='element-class' selected_class='element-selected-class'}}`

Use the `vote` helper to insert vote-related elements. These elements must apply to a specific votable resource (i.e. an article). When the user is authenticated and therefore able to vote, all vote elements are synced (i.e. if user votes up in an article, its labels and counters update their values without refreshing the page). When the user is not authenticated, the 'up' and 'down' buttons act like normal links, redirecting user to the sign in page.

#### Parameters

  * `element` one of the following: `up`, `down`, `label`, `sum`, or `count`


Element| Description
---|---
`up`| renders a vote up button
`down`| renders a vote down button
`label`| renders the "X out of Y found this helpful" label
`sum`| renders the sum of all votes
`count`| renders the total number of votes

#### Attributes

  * `class` (optional, string) the class of the element
  * `selected_class` (optional, string) the class to be added to the element when it is selected (applies to 'up' and 'down' elements only)
  * `role` (optional, string) the HTML role to render. Only available in Templating API v1.


#### Availability

  * Article Page (within an [article object](/api-reference/help_center/help-center-templates/objects#article-object))
  * Article Page (within an [article comment object](/api-reference/help_center/help-center-templates/objects#article-comment-object))
  * Post Page (within a [post object](/api-reference/help_center/help-center-templates/objects#post-object))
  * Post Page (within a [post comment object](/api-reference/help_center/help-center-templates/objects#post-comment-object))


#### Example

Supported variables vary based on your Templating API version.

v1


    {{#with article}}  {{vote 'up' class='article-vote-up' selected_class='article-voted' role='button'}}  {{vote 'down' class='article-vote-down' selected_class='article-voted' role='button'}}  {{vote 'label' class='article-vote-label'}}  {{vote 'count' class='article-vote-count'}}  {{vote 'sum' class='article-vote-sum'}}{{/with}}

v2 and later


    {{#with article}}  {{vote 'up' class='article-vote-up' selected_class='article-voted'}}  {{vote 'down' class='article-vote-down' selected_class='article-voted'}}  {{vote 'label' class='article-vote-label'}}  {{vote 'count' class='article-vote-count'}}  {{vote 'sum' class='article-vote-sum'}}{{/with}}

#### Output

The rendered output varies based on your Templating API version.

v1

If user is authenticated:


    <a role="button" rel="nofollow" class="article-vote-up article-voted" aria-selected="true" title="Yes" href="#"></a><a role="button" rel="nofollow" class="article-vote-down" aria-selected="false" title="No" href="#"></a><span class="article-vote-label">2 out of 3 found this helpful</span><span class="article-vote-count">3</span><span class="article-vote-sum">1</span>

If user is not authenticated:


    <a role="button" rel="nofollow" class="article-vote-up article-voted" title="Yes" href="path_to_sign_in"></a><a role="button" rel="nofollow" class="article-vote-down" title="No" href="path_to_sign_in"></a><span class="article-vote-label">2 out of 3 found this helpful</span><span class="article-vote-count">3</span><span class="article-vote-sum">1</span>

v2 and later

The rendered HTML is the same for authenticated and unauthenticated users. After clicking the 'up' or 'down' button, unauthenticated users are redirected to the sign in page using JavaScript.


    <button type="button" class="article-vote-up article-voted" aria-pressed="true">Yes</button><button type="button" class="article-vote-down" aria-pressed="false">No</a><span class="article-vote-label">2 out of 3 found this helpful</span><span class="article-vote-count">3</span><span class="article-vote-sum">1</span>

### change_password helper

`{{change_password}}`

Inserts a button that lets end users launch the Change Password modal. The button will only appear for end users and if changing passwords is available.

#### Attributes

  * `class` (optional, string) the class of the element
  * `role` (optional, string) the HTML role to render


#### Example


    {{change_password}}

#### Output


    <button data-action="change-password" title="Opens a dialog">Change password</button>

#### Availability

  * Header
  * Footer
  * User Profile page


### my_profile helper

`{{my_profile}}`

If user profiles are enabled, the helper renders a link to the user's user profile page.

If user profiles are disabled, but endusers can edit profile data, a button to launch a Edit Profile modal is rendered.

You can also customize the string by using the block version of the `my_profile` helper.

#### Attributes

  * `class` (optional, string) an HTML class
  * `role` (optional, string) an HTML role


#### Example


    {{my_profile}}
    {{#my_profile}}  Custom My Profile text{{/my_profile}}

#### Output

if user profiles are enabled:


    <a href="[path to user profile]">My profile</a>
    <a href="[path to user profile]">Custom My Profile text</a>

if user profiles are disabled, but users can edit profile data:


    <button data-action="edit-profile">Edit my profile</button>
    <button data-action="edit-profile">Custom My Profile text</button>

#### Availability

  * Header
  * Footer


Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)