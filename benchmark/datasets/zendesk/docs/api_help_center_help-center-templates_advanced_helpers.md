# Advanced helpers

*Source: https://developer.zendesk.com/api-reference/help_center/help-center-templates/advanced_helpers/*

---

## On this page

  * [Advanced helpers](/api-reference/help_center/help-center-templates/advanced_helpers/#advanced-helpers)
  * [Global advanced helpers](/api-reference/help_center/help-center-templates/advanced_helpers/#global-advanced-helpers)
  * [Shared advanced helpers](/api-reference/help_center/help-center-templates/advanced_helpers/#shared-advanced-helpers)
  * [recent_activity helper](/api-reference/help_center/help-center-templates/advanced_helpers/#recent_activity-helper)
  * [recent_articles helper](/api-reference/help_center/help-center-templates/advanced_helpers/#recent_articles-helper)
  * [actions helper](/api-reference/help_center/help-center-templates/advanced_helpers/#actions-helper)
  * [comment_callout helper](/api-reference/help_center/help-center-templates/advanced_helpers/#comment_callout-helper)
  * [follow_up helper](/api-reference/help_center/help-center-templates/advanced_helpers/#follow_up-helper)
  * [token_field helper](/api-reference/help_center/help-center-templates/advanced_helpers/#token_field-helper)
  * [related_articles helper](/api-reference/help_center/help-center-templates/advanced_helpers/#related_articles-helper)
  * [request_callout helper](/api-reference/help_center/help-center-templates/advanced_helpers/#request_callout-helper)
  * [request_form helper](/api-reference/help_center/help-center-templates/advanced_helpers/#request_form-helper)
  * [request_list helper](/api-reference/help_center/help-center-templates/advanced_helpers/#request_list-helper)
  * [satisfaction helper](/api-reference/help_center/help-center-templates/advanced_helpers/#satisfaction-helper)
  * [upload helper](/api-reference/help_center/help-center-templates/advanced_helpers/#upload-helper)
  * [wysiwyg helper](/api-reference/help_center/help-center-templates/advanced_helpers/#wysiwyg-helper)
  * [edit helper](/api-reference/help_center/help-center-templates/advanced_helpers/#edit-helper)
  * [generative_answers helper](/api-reference/help_center/help-center-templates/advanced_helpers/#generative_answers-helper)


# Advanced helpers

## On this page

  * [Advanced helpers](/api-reference/help_center/help-center-templates/advanced_helpers/#advanced-helpers)
  * [Global advanced helpers](/api-reference/help_center/help-center-templates/advanced_helpers/#global-advanced-helpers)
  * [Shared advanced helpers](/api-reference/help_center/help-center-templates/advanced_helpers/#shared-advanced-helpers)
  * [recent_activity helper](/api-reference/help_center/help-center-templates/advanced_helpers/#recent_activity-helper)
  * [recent_articles helper](/api-reference/help_center/help-center-templates/advanced_helpers/#recent_articles-helper)
  * [actions helper](/api-reference/help_center/help-center-templates/advanced_helpers/#actions-helper)
  * [comment_callout helper](/api-reference/help_center/help-center-templates/advanced_helpers/#comment_callout-helper)
  * [follow_up helper](/api-reference/help_center/help-center-templates/advanced_helpers/#follow_up-helper)
  * [token_field helper](/api-reference/help_center/help-center-templates/advanced_helpers/#token_field-helper)
  * [related_articles helper](/api-reference/help_center/help-center-templates/advanced_helpers/#related_articles-helper)
  * [request_callout helper](/api-reference/help_center/help-center-templates/advanced_helpers/#request_callout-helper)
  * [request_form helper](/api-reference/help_center/help-center-templates/advanced_helpers/#request_form-helper)
  * [request_list helper](/api-reference/help_center/help-center-templates/advanced_helpers/#request_list-helper)
  * [satisfaction helper](/api-reference/help_center/help-center-templates/advanced_helpers/#satisfaction-helper)
  * [upload helper](/api-reference/help_center/help-center-templates/advanced_helpers/#upload-helper)
  * [wysiwyg helper](/api-reference/help_center/help-center-templates/advanced_helpers/#wysiwyg-helper)
  * [edit helper](/api-reference/help_center/help-center-templates/advanced_helpers/#edit-helper)
  * [generative_answers helper](/api-reference/help_center/help-center-templates/advanced_helpers/#generative_answers-helper)


## Advanced helpers

The following helpers provide advanced functionality. We don't recommend heavily customizing the output of any of these helpers with JavaScript or CSS because their internal implementation might change in the future.

### Global advanced helpers

The following advanced helpers are available in all templates:

  * recent_activity
  * recent_articles


### Shared advanced helpers

The following advanced helpers are only available in certain pages:

  * actions
  * comment_callout
  * follow_up
  * related_articles
  * request_callout
  * request_form
  * request_list
  * satisfaction
  * token_field
  * upload
  * wysiwyg
  * edit
  * generative_answers


### recent_activity helper

`{{recent_activity}}`

A list of 5 recent activities for Help Center. Recent activities consist of the following:

  * Newly created articles
  * New translations of existing articles
  * New comments on articles


If the affected article is not visible to the user, the activity won't be displayed in the list.

If you set `scope='community'` (see below), the following activities are displayed:

  * New community posts
  * New community comments


There's no time limit for recent activity. If the most recent activity was a year ago, it will still appear at the top of the list.

#### Availability

  * All pages


#### Parameters

  * `scope` (optional, string) Can be `community`, `category`, or `section`. If set to `community`, displays the 5 most recently created community posts or post comments visible to the user. If set to `category` or `section`, displays only recent activity for a category or section. The `category` and `section` scopes only work in the Category and Section page templates respectively.


#### Example


    {{recent_activity scope='section'}}

### recent_articles helper

`{{recent_articles}}`

A list of articles recently viewed by the user in the browser.

#### Availability

  * All pages


### actions helper

`{{actions}}`

A user menu including all the available actions for the current object.

#### Availability

  * Article page (within an [article comment object](/api-reference/help_center/help-center-templates/objects#article-comment-object))
  * Post page (within a [post object](/api-reference/help_center/help-center-templates/objects#post-object) and a [post comment object](/api-reference/help_center/help-center-templates/objects#post-comment-object))
  * User Profile page


#### Example


    {{#each comments}}  ...  <span class="comment-actions">    {{actions}}  </span>{{/each}}

### comment_callout helper

`{{comment_callout}}`

A link for users to create a new comment or a follow-up ticket, if allowed.

#### Availability

  * Article page
  * Request page


#### Example


    {{comment_callout}}

#### Output

When placed in article page:


    <!-- if comments are disabled -->Article is closed for comments.
    <!-- if user not signed in -->Please <a href="/path_to_sign_in/">sign in</a> to leave a comment.
    <!-- if signed in and there is no comments yet -->Be the first to write a comment.

### follow_up helper

`{{follow_up}}`

A link to the parent request, if it exists.

#### Availability

  * New Request page


### token_field helper

`{{token_field 'identifier'}}`

An input that turns into a field with tokens, providing input validation as well as fast input deletion.

#### Availability

  * Request page (within a [comment form](/api-reference/help_center/help-center-templates/helpers#form-helper))


#### Parameters

  * `identifier` (required, string) Depends on the page and the form that has the field. See [identifiers](/api-reference/help_center/help-center-templates/helpers#identifiers).


#### Example


    {{#form 'comment' class='comment-form'}}  {{#if help_center.request_ccs_enabled}}    {{token_field 'ccs' class="ccs-input"}}  {{/if}}  {{textarea 'body' rows='4'}}  {{input type='submit'}}{{/form}}

### related_articles helper

`{{related_articles}}`

A list of up to five related articles. See [How is the Related articles list in Help Center populated?](https://support.zendesk.com/hc/en-us/articles/224934288) in the Support Help Center.

#### Availability

  * Article page


### request_callout helper

`{{request_callout}}`

A link for users to create a request, if they are allowed.

#### Availability

  * Article page


#### Example


    {{request_callout}}

#### Output


    <!-- this is only displayed if user can submit a request -->Have more questions? <a href="/path_to_new_request/">Submit a request</a>

### request_form helper

`{{request_form wysiwyg=true}}`

Displays a form to submit a support request. The form includes ticket fields as defined in the agent interface. For more information, see [Adding custom fields to your tickets and support request forms](https://support.zendesk.com/hc/en-us/articles/203661496-Adding-and-using-custom-ticket-fields) in the Support Help Center.

Note that this is a different form than the [form helper](/api-reference/help_center/help-center-templates/helpers#form-helper).

#### Attributes

  * `wysiwyg` (optional, boolean) whether or not to use a rich text editor for the `description` field of the request form. Default is `false`.


#### Availability

  * New Request page


### request_list helper

`{{request_list}}`

This helper is deprecated and will not receive updates. The helper cannot be modified with theme code. It inherits its color settings from the standard color settings in the theme.

For guidance on how to customize the request list, see the request-list part of the [Copenhagen theme repository](https://github.com/zendesk/copenhagen_theme/tree/11e8049bea05e19b5c1791ca617fc8859d428307/src/modules/request-list) code base.

Renders a list of requests.

#### Availability

  * Request List page


### satisfaction helper

`{{satisfaction}}`

The satisfaction rating of the request, if any.

#### Availability

  * Request page


### upload helper

`{{upload}}`

A file upload interface allowing visitors to upload files. Drag and drop is available only on browsers that support this HTML5 feature. Only one upload helper is valid per page.

#### Availability

  * Request page (within a [comment form](/api-reference/help_center/help-center-templates/helpers#form-helper))


#### Example


    {{#form "comment"}}  ...  <div class="comment-attachments">    {{upload}}  </div>{{/form}}

### wysiwyg helper

`{{wysiwyg 'identifier'}}`

A textarea that turns into a "wysiwyg" editor when it receives focus, allowing visitors to insert rich content. This helper is an enhanced version of the [textarea](/api-reference/help_center/help-center-templates/helpers#textarea-helper)). It accepts the same `identifier` as a parameter, but unlike the `textarea`, it does not accept attributes.

#### Availability

  * New Post page (within a [post form](/api-reference/help_center/help-center-templates/helpers#form-helper))
  * Post page (within a [comment form](/api-reference/help_center/help-center-templates/helpers#form-helper))
  * Article page (within a [comment form](/api-reference/help_center/help-center-templates/helpers#form-helper))
  * Request page (within a [comment form](/api-reference/help_center/help-center-templates/helpers#form-helper))


#### Parameters

  * `identifier` (required, string) the name of the field. Depends on the page and the form that has the field. See [identifiers](/api-reference/help_center/help-center-templates/helpers#identifiers).


#### Example


    {{#form "post"}}  ...  <div class="form-field">    {{wysiwyg 'details'}}  </div>{{/form}}

### edit helper

`{{edit}}`

Inserts an "edit" button that allows the owner of the profile to edit his or her information.

#### Availability

  * User Profile page


### generative_answers helper

`{{generative_answers}}`

Adds a Quick answers box that displays AI-generated answers to the user's question, alongside buttons that lets the user provide feedback about how helpful the answer is. For more information, see [Using generative search to provide AI-powered answers to search queries](https://support.zendesk.com/hc/en-us/articles/8888178335898) in the Zendesk help center.

#### Availability

  * Search Results page


#### Example


    ...  <section id="main-content" class="search-results-column">    {{generative_answers}}    <h1 class="search-results-subheading">  ...

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)