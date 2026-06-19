# User Profile page

*Source: https://developer.zendesk.com/api-reference/help_center/help-center-templates/user_profile_page/*

---

## On this page

  * [User Profile page](/api-reference/help_center/help-center-templates/user_profile_page/#user-profile-page)
  * [Available properties](/api-reference/help_center/help-center-templates/user_profile_page/#available-properties)
  * [Available helpers](/api-reference/help_center/help-center-templates/user_profile_page/#available-helpers)
  * [Filters](/api-reference/help_center/help-center-templates/user_profile_page/#filters)
  * [Sorters](/api-reference/help_center/help-center-templates/user_profile_page/#sorters)
  * [Example](/api-reference/help_center/help-center-templates/user_profile_page/#example)


# User Profile page

## On this page

  * [User Profile page](/api-reference/help_center/help-center-templates/user_profile_page/#user-profile-page)
  * [Available properties](/api-reference/help_center/help-center-templates/user_profile_page/#available-properties)
  * [Available helpers](/api-reference/help_center/help-center-templates/user_profile_page/#available-helpers)
  * [Filters](/api-reference/help_center/help-center-templates/user_profile_page/#filters)
  * [Sorters](/api-reference/help_center/help-center-templates/user_profile_page/#sorters)
  * [Example](/api-reference/help_center/help-center-templates/user_profile_page/#example)


## User Profile page

The User Profile page template is rendered when a user navigates to `https://{yoursubdomain}.zendesk.com/hc/{locale}/profiles/{user_id}`.

### Available properties

Name| Type| Description
---|---|---
description| string| The description of the user
post_count| integer| The number of posts created by the user
comment_count| integer| The number of comments created by the user
vote_count| integer| The number of votes created by the user
article_count| integer| The number of articles created by the user
total_activity| integer| The total number of articles, votes, posts, comments, and subscriptions created by the user
follower_count| integer| The number of followers of the user
following_count| integer| The number of people that this user is following
subscription_count| integer| The number of subscriptions created by the user
member_since| timestamp| The time at which the first contribution has been made by the user
last_activity_at| timestamp| The time of the last activity of the user
sorter_description| string| The description for each sorter
private_profile| boolean| If the help center user profiles setting is private
visible| boolean| Whether the user profiles setting is public. `true` for private user profiles only if the viewer is the owner of the profile or is an agent
activities| array| An array of [activity](/api-reference/help_center/help-center-templates/objects#activity-object) objects
current_sorter| object| The current [sorter](/api-reference/help_center/help-center-templates/objects#filter-object) object
sorters| array| An array of [filter](/api-reference/help_center/help-center-templates/objects#filter-object) objects for the page. See Sorters below
contributions| array| The array of [contribution](/api-reference/help_center/help-center-templates/objects#contribution-object) objects
filters| array| An array of [filter](/api-reference/help_center/help-center-templates/objects#filter-object) objects for the page
current_filter| object| The current [filter](/api-reference/help_center/help-center-templates/objects#filter-object) object
user| object| The [user](/api-reference/help_center/help-center-templates/objects#user-object) object
signed_in| boolean| Whether the user is logged in or not
featured_posts| array| An array of featured [post](/api-reference/help_center/help-center-templates/objects#post-object) objects
brand| object| A [brand](/api-reference/help_center/help-center-templates/objects#brand-object) object representing the current brand
user| object| A [user](/api-reference/help_center/help-center-templates/objects#user-object) object representing the current user

### Available helpers

Name| Description
---|---
subscribe| A link to follow or unfollow new contributions by this user, See [subscribe](/api-reference/help_center/help-center-templates/helpers#subscribe-helper)
actions| A split button menu of possible actions to take on the current user profile, including editing the profile and user badges
edit| A link to edit the current user profile. Similar to `actions` but only supports profile editing
pagination| Pagination links, See [pagination helper](/api-reference/help_center/help-center-templates/helpers#pagination-helper)
change_password| Show the change password modal. See [change_password helper](/api-reference/help_center/help-center-templates/helpers#change_password-helper)

### Filters

Iterating through the `filters` array of [filter](/api-reference/help_center/help-center-templates/objects#filter-object) objects adds the following links in the table below to the page. In the tab names, `n` is the count.

Identifier| Tab Name (en-us)| Remarks
---|---|---
activities| Activity overview|
badges| Badges (`n`)| Included if [User Badges is enabled](https://support.zendesk.com/hc/en-us/articles/360047549154).
articles| Articles (`n`)|
posts Â | Posts (`n`)| Included if [Community is enabled](https://support.zendesk.com/hc/en-us/articles/360035960273)
comments| Comments (`n`)| Included if [Community is enabled](https://support.zendesk.com/hc/en-us/articles/360035960273)

### Sorters

Iterating through the `sorters` array of [filter](/api-reference/help_center/help-center-templates/objects#filter-object) objects adds the following links to the page:

Link text| Action
---|---
Recent activity| Sorts by the most recent activity in descending order. Activity are actions taken on the object, such as creating or updating it
Votes| Sorts by the highest vote sum in descending order

### Example


    <header class="profile-header">  <div class="profile-info">    <div class="profile-avatar {{#if user.agent}}profile-avatar-agent{{/if}}">      <img class="avatar" src="{{user.avatar_url}}" alt="Avatar"/>    </div>    <div class="basic-info">      <h1 class="name">        {{#if user.url}}          <a href="{{user.url}}" target="_zendesk_lotus" title="{{t 'open_user_in_support'}}">{{user.name}}</a>        {{else}}          {{user.name}}        {{/if}}      </h1>    </div>    <div class="options">      {{#if private_profile}}        <span class="profile-private-badge">{{t 'private'}}</span>      {{/if}}      {{actions class='user-profile-actions split-button'}}      {{subscribe}}    </div>
        {{#if description}}      <p class="description">{{description}}</p>    {{/if}}
        <ul class="profile-stats profile-stats-activity">      <li class="stat">        <span class="stat-label">{{t 'total_activity'}}</span>        <span class="stat-value">{{total_activity}}</span>      </li>      <li class="stat">        <span class="stat-label">{{t 'last_activity'}}</span>        <span class="stat-value">          {{#if last_activity_at}}            {{date last_activity_at timeago=true}}          {{else}}            {{t 'no_activity_yet'}}          {{/if}}        </span>      </li>      <li class="stat">        <span class="stat-label">{{t 'member_since'}}</span>        <span class="stat-value">          {{#if member_since}}            {{date member_since timeago=true}}          {{else}}            {{t 'no_activity_yet'}}          {{/if}}        </span>      </li>    </ul>  </div>

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)