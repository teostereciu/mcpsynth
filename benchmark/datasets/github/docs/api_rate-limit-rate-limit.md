# REST API endpoints for rate limits

*Source: https://docs.github.com/en/rest/rate-limit/rate-limit*

---

# REST API endpoints for rate limits
Use the REST API to check your current rate limit status.

## About rate limits
You can check your current rate limit status at any time. For more information about rate limit rules, seeRate limits for the REST API.
The REST API for searching items has a custom rate limit that is separate from the rate limit governing the other REST API endpoints. For more information, seeREST API endpoints for search. The GraphQL API also has a custom rate limit that is separate from and calculated differently than rate limits in the REST API. For more information, seeRate limits and query limits for the GraphQL API. For these reasons, the API response categorizes your rate limit. Underresources, you'll see objects relating to different categories:
- Thecoreobject provides your rate limit status for all non-search-related resources in the REST API.
- Thesearchobject provides your rate limit status for the REST API for searching (excluding code searches). For more information, seeREST API endpoints for search.
- Thecode_searchobject provides your rate limit status for the REST API for searching code. For more information, seeREST API endpoints for search.
- Thegraphqlobject provides your rate limit status for the GraphQL API.
- Theintegration_manifestobject provides your rate limit status for thePOST /app-manifests/{code}/conversionsoperation. For more information, seeRegistering a GitHub App from a manifest.
- Thedependency_snapshotsobject provides your rate limit status for submitting snapshots to the dependency graph. For more information, seeREST API endpoints for the dependency graph.
- Thecode_scanning_uploadobject provides your rate limit status for uploading SARIF results to code scanning. For more information, seeUploading a SARIF file to GitHub.
- Theactions_runner_registrationobject provides your rate limit status for registering self-hosted runners in GitHub Actions. For more information, seeREST API endpoints for self-hosted runners.
For more information on the headers and values in the rate limit response, seeRate limits for the REST API.

## Get rate limit status for the authenticated user
Note
Accessing this endpoint does not count against your REST API rate limit.
Some categories of endpoints have custom rate limits that are separate from the rate limit governing the other REST API endpoints. For this reason, the API response categorizes your rate limit. Underresources, you'll see objects relating to different categories:
- Thecoreobject provides your rate limit status for all non-search-related resources in the REST API.
- Thesearchobject provides your rate limit status for the REST API for searching (excluding code searches). For more information, see "Search."
- Thecode_searchobject provides your rate limit status for the REST API for searching code. For more information, see "Search code."
- Thegraphqlobject provides your rate limit status for the GraphQL API. For more information, see "Resource limitations."
- Theintegration_manifestobject provides your rate limit status for thePOST /app-manifests/{code}/conversionsoperation. For more information, see "Creating a GitHub App from a manifest."
- Thedependency_snapshotsobject provides your rate limit status for submitting snapshots to the dependency graph. For more information, see "Dependency graph."
- Thedependency_sbomobject provides your rate limit status for requesting SBOMs from the dependency graph. For more information, see "Dependency graph."
- Thecode_scanning_uploadobject provides your rate limit status for uploading SARIF results to code scanning. For more information, see "Uploading a SARIF file to GitHub."
- Theactions_runner_registrationobject provides your rate limit status for registering self-hosted runners in GitHub Actions. For more information, see "Self-hosted runners."
- Thesource_importobject is no longer in use for any API endpoints, and it will be removed in the next API version. For more information about API versions, see "API Versions."
Note
Therateobject is closing down. If you're writing new API client code or updating existing code, you should use thecoreobject instead of therateobject. Thecoreobject contains the same information that is present in therateobject.

### Fine-grained access tokens for "Get rate limit status for the authenticated user"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token does not require any permissions.
This endpoint can be used without authentication if only public resources are requested.

### HTTP response status codes for "Get rate limit status for the authenticated user"

[TABLE]
Status code | Description
200 | OK
304 | Not modified
404 | Resource not found
[/TABLE]
OK
Not modified
Resource not found

### Code samples for "Get rate limit status for the authenticated user"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/rate_limit
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "resources": {
    "core": {
      "limit": 5000,
      "used": 1,
      "remaining": 4999,
      "reset": 1691591363
    },
    "search": {
      "limit": 30,
      "used": 12,
      "remaining": 18,
      "reset": 1691591091
    },
    "graphql": {
      "limit": 5000,
      "used": 7,
      "remaining": 4993,
      "reset": 1691593228
    },
    "integration_manifest": {
      "limit": 5000,
      "used": 1,
      "remaining": 4999,
      "reset": 1691594631
    },
    "source_import": {
      "limit": 100,
      "used": 1,
      "remaining": 99,
      "reset": 1691591091
    },
    "code_scanning_upload": {
      "limit": 500,
      "used": 1,
      "remaining": 499,
      "reset": 1691594631
    },
    "actions_runner_registration": {
      "limit": 10000,
      "used": 0,
      "remaining": 10000,
      "reset": 1691594631
    },
    "scim": {
      "limit": 15000,
      "used": 0,
      "remaining": 15000,
      "reset": 1691594631
    },
    "dependency_snapshots": {
      "limit": 100,
      "used": 0,
      "remaining": 100,
      "reset": 1691591091
    },
    "code_search": {
      "limit": 10,
      "used": 0,
      "remaining": 10,
      "reset": 1691591091
    },
    "code_scanning_autofix": {
      "limit": 10,
      "used": 0,
      "remaining": 10,
      "reset": 1691591091
    }
  },
  "rate": {
    "limit": 5000,
    "used": 1,
    "remaining": 4999,
    "reset": 1372700873
  }
}
```