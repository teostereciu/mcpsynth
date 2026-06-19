# Using the REST API to interact with checks

*Source: https://docs.github.com/en/rest/guides/using-the-rest-api-to-interact-with-checks*

---

# Using the REST API to interact with checks
You can use the REST API to build GitHub Apps that run powerful checks against code changes in a repository. You can create apps that perform continuous integration, code linting, or code scanning services and provide detailed feedback on commits.

## In this article

## Overview
Rather than binary pass/fail build statuses, GitHub Apps can report rich statuses, annotate lines of code with detailed information, and re-run tests. REST API to manage checks is available exclusively to your GitHub Apps.
For an example of how to use the REST API with a GitHub App, seeBuilding CI checks with a GitHub App.
You can use statuses withprotected branchesto prevent people from merging pull requests prematurely. For more information, seeAbout protected branches.

## About check suites
When someone pushes code to a repository, GitHub creates a check suite for the last commit. A check suite is a collection of thecheck runscreated by a single GitHub App for a specific commit. Check suites summarize the status and conclusion of the check runs that a suite includes.
Thestatuscan bequeued,in_progress,requested,waiting,pending, orcompleted. Only GitHub Actions can set a status ofrequested,waiting, orpending.
If the status iscompleted, the conclusion can be any of the following:
- action_required
- cancelled
- timed_out
- failure
- neutral
- skipped
- stale
- startup_failure
- success
The check suite reports the highest priority check runconclusionin the check suite'sconclusion. For example, if three check runs have conclusions oftimed_out,success, andneutralthe check suite conclusion will betimed_out.
By default, GitHub creates a check suite automatically when code is pushed to the repository. This default flow sends thecheck_suiteevent (withrequestedaction) to all GitHub Apps that have thechecks:writepermission. When your GitHub App receives thecheck_suiteevent, it can create new check runs for the latest commit. GitHub automatically adds new check runs to the correctcheck suitebased on the check run's repository and SHA.
If you don't want to use the default automatic flow, you can control when you create check suites. To change the default settings for the creation of check suites, use theUpdate repository preferences for check suitesendpoint. All changes to the automatic flow settings are recorded in the audit log for the repository. If you have disabled the automatic flow, you can create a check suite using theCreate a check suiteendpoint. You should continue to use theCreate a check runendpoint to provide feedback on a commit.
Write permission for the REST API to interact with checks is only available to GitHub Apps. OAuth apps and authenticated users can view check runs and check suites, but they are not able to create them. If you aren't building a GitHub App, you might be interested in using the REST API to interact withcommit statuses.
To use the endpoints to manage check suites, the GitHub App must have thechecks:writepermission and can also subscribe to thecheck_suitewebhook.
For information on how to authenticate as a GitHub App, seeAbout authentication with a GitHub App.

## About check runs
A check run is an individual test that is part of a check suite. Each run includes a status and conclusion.
Thestatuscan bequeued,in_progress,requested,waiting,pending, orcompleted. Only GitHub Actions can set a status ofrequested,waiting, orpending.
If the status iscompleted, the conclusion can be any of the following:
- action_required
- cancelled
- timed_out
- failure
- neutral
- skipped
- success
If a check run is in an incomplete issue_state for more than 14 days, then the check run'sconclusionbecomesstaleand appears on GitHub as stale with. Only GitHub can mark check runs asstale. For more information about possible conclusions of a check run, see theconclusionparameter.
As soon as you receive thecheck_suitewebhook, you can create the check run, even if the check is not complete. You can update thestatusof the check run as it completes with the valuesqueued,in_progress, orcompleted, and you can update theoutputas more details become available. A check run can contain timestamps, a link to more details on your external site, detailed annotations for specific lines of code, and information about the analysis performed.

```
check_suite
```
Annotations add information from your check run to specific lines of code. Each annotation includes anannotation_levelproperty, which can benotice,warning, orfailure. The annotation also includespath,start_line, andend_lineto specify what location the annotation refers to. The annotation includes amessageto describe the result. For more information, seeREST API endpoints for check runs.
A check can also be manually re-run in the GitHub UI. SeeAbout status checksfor more details. When this occurs, the GitHub App that created the check run will receive thecheck_runwebhook requesting a new check run. If you create a check run without creating a check suite, GitHub creates the check suite for you automatically.
Write permission for the REST API to interact with checks is only available to GitHub Apps. OAuth apps and authenticated users can view check runs and check suites, but they are not able to create them. If you aren't building a GitHub App, you might be interested in using the REST API to interact withcommit statuses.
To use the endpoints to manage check runs, the GitHub App must have thechecks:writepermission and can also subscribe to thecheck_runwebhook.

## Check runs and requested actions
When you set up a check run with requested actions (not to be confused with GitHub Actions), you can display a button in the pull request view on GitHub that allows people to request your GitHub App to perform additional tasks.
For example, a code linting app could use requested actions to display a button in a pull request to automatically fix detected syntax errors.
To create a button that can request additional actions from your app, use theactionsobjectwhen youCreate a check run. For example, theactionsobject below displays a button in theCheckstab of a pull request with the label "Fix this." The button appears after the check run completes.

```
"actions":[{"label":"Fix this","description":"Let us fix that for you","identifier":"fix_errors"}]
```

```
"actions":[{"label":"Fix this","description":"Let us fix that for you","identifier":"fix_errors"}]
```
When a user clicks the button, GitHub sends thecheck_run.requested_actionwebhookto your app. When your app receives acheck_run.requested_actionwebhook event, it can look for therequested_action.identifierkey in the webhook payload to determine which button was clicked and perform the requested task.

```
check_run.requested_action
```
For a detailed example of how to set up requested actions with the REST API, seeBuilding CI checks with a GitHub App.

## Retention of checks data
GitHub retains checks data for 400 days. After 400 days, the data is archived. 10 days after archival, the data is permanently deleted.
To merge a pull request with checks that are both required and archived, you must rerun the checks.