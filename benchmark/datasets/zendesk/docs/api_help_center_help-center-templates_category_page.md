# Category page

*Source: https://developer.zendesk.com/api-reference/help_center/help-center-templates/category_page/*

---

## On this page

  * [Category page](/api-reference/help_center/help-center-templates/category_page/#category-page)
  * [Available properties](/api-reference/help_center/help-center-templates/category_page/#available-properties)
  * [Available helpers](/api-reference/help_center/help-center-templates/category_page/#available-helpers)
  * [Example](/api-reference/help_center/help-center-templates/category_page/#example)


# Category page

## On this page

  * [Category page](/api-reference/help_center/help-center-templates/category_page/#category-page)
  * [Available properties](/api-reference/help_center/help-center-templates/category_page/#available-properties)
  * [Available helpers](/api-reference/help_center/help-center-templates/category_page/#available-helpers)
  * [Example](/api-reference/help_center/help-center-templates/category_page/#example)


## Category page

The Category page template is rendered when a user navigates to `https://{yoursubdomain}.zendesk.com/hc/{locale}/categories/{category_id}`.

### Available properties

You can use the following properties in the Category page template.

Name| Type| Description
---|---|---
category| object| A [category](/api-reference/help_center/help-center-templates/objects#category-object) object
sections| array| An array of [section](/api-reference/help_center/help-center-templates/objects#section-object) objects
promoted_articles| array| An array of promoted [article](/api-reference/help_center/help-center-templates/objects#article-object) objects
ticket_forms| array| An array of [ticket form](/api-reference/help_center/help-center-templates/objects#ticket-form-object) objects
help_center| object| A [help_center](/api-reference/help_center/help-center-templates/objects#help_center-object) object that holds information and settings about the current help center
settings| object| A [settings](/api-reference/help_center/help-center-templates/objects#settings-object) object with custom settings for the current theme
signed_in| boolean| Whether the user is logged in or not
featured_posts| array| An array of featured [post](/api-reference/help_center/help-center-templates/objects#post-object) objects
brand| object| A [brand](/api-reference/help_center/help-center-templates/objects#brand-object) object representing the current brand
user| object| A [user](/api-reference/help_center/help-center-templates/objects#user-object) object representing the current user
path_steps| array| An array of [path_step](/api-reference/help_center/help-center-templates/objects#path_step-object) objects

### Available helpers

You can use the following helpers in this page template. You can also use any [built-in helpers](/api-reference/help_center/help-center-templates/helpers#built-in-helpers), [global helpers](/api-reference/help_center/help-center-templates/helpers#global-helpers), or [global advanced helpers](/api-reference/help_center/help-center-templates/advanced_helpers#global-advanced-helpers).

Name| Description
---|---
breadcrumbs| Breadcrumbs for the current page. See [breadcrumbs helper](/api-reference/help_center/help-center-templates/helpers#breadcrumbs-helper)

### Example


    <nav class="sub-nav sub-nav-far clearfix">  {{breadcrumbs}}  {{search}}</nav>
    <h1>{{category.name}}</h1><p class="category-description">{{category.description}}</p><ul>{{#each sections}}  <li class="section-name">    <a href="{{url}}">{{name}}</a>  </li>{{/each}}</ul>

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)