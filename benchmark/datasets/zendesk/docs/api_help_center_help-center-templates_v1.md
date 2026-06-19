# Upgrading from Templating API v1

*Source: https://developer.zendesk.com/api-reference/help_center/help-center-templates/v1/*

---

## On this page

  * [Upgrading from Templating API v1](/api-reference/help_center/help-center-templates/v1/#upgrading-from-templating-api-v1)
  * [New helpers](/api-reference/help_center/help-center-templates/v1/#new-helpers)
  * [Updated helpers](/api-reference/help_center/help-center-templates/v1/#updated-helpers)
  * [Removed object properties/helpers](/api-reference/help_center/help-center-templates/v1/#removed-object-propertieshelpers)
  * [Performance improvements and removed libraries](/api-reference/help_center/help-center-templates/v1/#performance-improvements-and-removed-libraries)
  * [Other updates](/api-reference/help_center/help-center-templates/v1/#other-updates)


# Upgrading from Templating API v1

## On this page

  * [Upgrading from Templating API v1](/api-reference/help_center/help-center-templates/v1/#upgrading-from-templating-api-v1)
  * [New helpers](/api-reference/help_center/help-center-templates/v1/#new-helpers)
  * [Updated helpers](/api-reference/help_center/help-center-templates/v1/#updated-helpers)
  * [Removed object properties/helpers](/api-reference/help_center/help-center-templates/v1/#removed-object-propertieshelpers)
  * [Performance improvements and removed libraries](/api-reference/help_center/help-center-templates/v1/#performance-improvements-and-removed-libraries)
  * [Other updates](/api-reference/help_center/help-center-templates/v1/#other-updates)


## Upgrading from Templating API v1

Version 2 of the Templating API is focused on providing a better foundation for building more performant and more accessible Guide Help Centers.

Find out how to check what version your theme is using and how to upgrade in [ About Guide templating](https://support.zendesk.com/hc/en-us/articles/360043187273) in Zendesk help.

This page lists what's changed from Templating API v1 to Templating API v2.

### New helpers

#### {{source_filters}}

An array of [filter](/api-reference/help_center/help-center-templates/objects#filter-object) objects. Use these filters to iterate through help centers and external sources when [searching multiple help centers and/or external content sources](https://support.zendesk.com/hc/en-us/articles/4890968422298-Managing-search-sources/#topic_f1z_s3b_w5b).

#### {{type_filters}}

An array of [filter](/api-reference/help_center/help-center-templates/objects#filter-object) objects. Use these filters to iterate through content types (articles, posts or external types) when [searching across multiple content types](https://support.zendesk.com/hc/en-us/articles/4408830243482-About-help-center-federated-search#topic_f3d_tcy_x4b).

### Updated helpers

#### `{{request_form}}`

This form will now render `(optional)` next to optional fields instead of an `*` next to required fields for improved accessibility.

#### `{{subscribe}}`

This helper has been improved for accessibility. The component is now a toggle button that no longer refreshes the page, and also does not create a notification for the user.

#### `{{related_articles}}`

This helper has been improved for accessibility.

#### `{{recent_articles}}`

This helper has been improved for accessibility.

#### `{{actions}}`

This helper has been improved for accessibility.

#### `{{share}}`

This helper has been improved for accessibility.

#### `{{recent_activity}}`

This helper has been improved for accessibility and now renders a comment bubble svg next to the comment count.

#### `{{pagination}}`

This helper has been updated to exclude page numbers in preparation for cursor-based paginated collections.

#### `{{asset}}`

If your theme was migrated to the new Customize Design experience in 2018, you might have used `{{asset "name" cdn="legacy"}}` in your theme. This would render a link to the previous asset CDN for backwards compatibility. The `cdn` attribute is no longer supported and will be ignored.

#### `{{vote}}`

To improve accessibility, the helper now renders buttons instead of anchor tags. The `role` attribute has been removed.

### Removed object properties/helpers

#### `{{logo_url}}`

The new Customize Design experience introduced in 2017 provided theme settings in a `settings` object, including the logo for the Help Center. Use `{{settings.logo}}` as a replacement for `{{logo_url}}`.

#### `{{chat}}`

This helper had previously been deprecated (rendering an empty string) and has now been removed.

#### `{{trending_questions_list}}`

This helper had previously been deprecated (rendering an empty string) and has now been removed.

#### `{{chat_about_my_ticket}}`

This helper had previously been deprecated (rendering an empty string) and has now been removed.

#### `{{section.internal}}`

This property had previously been deprecated (always returning false) and has now been removed.

#### `{{category_tree_with_article}}`

This helper would output HTML markup. This markup can be rebuilt by using the `category` object.

#### `{{section_tree_with_article}}`

This helper would output HTML markup. This markup can be rebuilt by using the `section` object.

#### `{{article_results}}`

This collection, used in the search results page, has been removed in favor of the unified results collection. You can find more details on how to upgrade your search page in the [Help Center templating cookbook](https://support.zendesk.com/hc/en-us/articles/216367358#topic_ykx_gms_y3b) in Guide Help.

#### `{{post_results}}`

This collections, used in the search results page, has been removed in favor of the unified results collection. You can find more details on how to upgrade your search page in the [Help Center templating cookbook](https://support.zendesk.com/hc/en-us/articles/216367358#topic_ykx_gms_y3b) in Guide Help.

#### `{{filter_by}}`

This property is no longer available in the user profiles page. You can replace it with `{{current_filter.identifier}}`.

#### `{{user_info}}`

This helper is no longer available in the header template. The following helpers are now available to build a corresponding menu: `{{user_avatar}}`, `{{user_name}}`, `{{my_profile}}`, `{{change_password}}`. You can find an example of the re-implemented drop-down in the Copenhagen Theme's [header template](https://github.com/zendesk/copenhagen_theme/blob/master/templates/header.hbs)

#### `{{unsubscribe}}`

This helper is no longer available in the subscription object. The `{{subscribe}}` helper now also allows to unsubscribe when content is already subscribed. The `{{following}}` attribute outputs the types of content being followed.

### Performance improvements and removed libraries

The theme's `script.js` file is now loaded at the end of the page body for improved page performance. In addition, the libraries listed in this section are no longer present in Templating API v2. If you need one or more of these libraries to customize your theme, you can still add them as theme assets. See [Using your own theme assets for Help Center](https://support.zendesk.com/hc/en-us/articles/115012399428) in Guide Help.

#### jQuery

jQuery is no longer as ubiquitous as it once was so it's no longer included by default. The Copenhagen theme is now built with plain vanilla Javascript.

If your theme still requires jQuery, you can import it in your document head template. You can either add it as an asset to your theme or load it from an external source. See more information in [Importing or upgrading jQuery](https://support.zendesk.com/hc/en-us/articles/360037983854).

Templating API v1 was using jQuery version 1.9.1. This version is no longer supported and you should consider upgrading. You can find multiple versions of jQuery at <https://cdnjs.com/libraries/jquery/>[](https://cdnjs.com/libraries/jquery/).

If you were previously using jQuery to make Zendesk API requests that require an authenticity token (also known as a CSRF token), you now need to fetch the token as part of your JavaScript code.

Example:


    $.ajax({    url: "/api/v2/users/me",    dataType: "json"  })  .done(function(data) {    authenticityToken = data.user.authenticity_token;
        // Your request goes here    $.ajax({      url: "/api/v2/requests",      method: "POST",      dataType: "json",      headers: {        "X-CSRF-Token": authenticityToken      },      data: {        "request": {          "subject": "Help!",          "comment": {            "body": "My printer is on fire!"          }        }      }    }).done(function(data) {      console.log(data)    })  });

#### moment.js

Although moment.js was not a documented API, it was available in the window object and was used by theme developers.

This is no longer possible in Templating API v2. Consider importing it in your theme if it is required.

Templating API v1 was using moment.js version 2.4.0.

#### normalize.css

Normalize.css is a small CSS library that provides cross-browser consistency in the default styling of HTML elements.

This is no longer available in Templating API v2. Consider importing it in your theme if it is required.

Templating API v1 was using normalize.css version 3.0.0.

#### entypo

Entypo is a popular icon font library which was included by default and used in the Copenhagen theme.

The theme was migrated to use inline SVGs for better page load performance and improved accessibility.

#### drop-downs

Help Center would inject drop-down functionality to the theme. This functionality is now implemented through the Copenhagen Theme's [style](https://github.com/zendesk/copenhagen_theme/blob/master/style.css) and [script](https://github.com/zendesk/copenhagen_theme/blob/master/script.js) files.

### Other updates

  * The Help Center's mobile-specific layout, originally deprecated in 2017, has been removed in Templating API v2.


Consider updating your theme to have a responsive layout if your users are accessing the Help Center from mobile.

  * Improved template validation - helpers cannot be used within conditional expressions


Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)