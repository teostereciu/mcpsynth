# REST API endpoints for software bill of materials (SBOM)

*Source: https://docs.github.com/en/rest/dependency-graph/sboms*

---

# REST API endpoints for software bill of materials (SBOM)
Use the REST API to export the software bill of materials (SBOM) for a repository.
If you have at least read access to the repository, you can export the dependency graph for the repository as an SPDX-compatible, Software Bill of Materials (SBOM), via the GitHub UI or GitHub REST API. For more information, seeExporting a software bill of materials for your repository.
This article gives details about the REST API endpoint.

## Export a software bill of materials (SBOM) for a repository.
Exports the software bill of materials (SBOM) for a repository in SPDX JSON format.

### Fine-grained access tokens for "Export a software bill of materials (SBOM) for a repository."
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Contents" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "Export a software bill of materials (SBOM) for a repository."

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

### HTTP response status codes for "Export a software bill of materials (SBOM) for a repository."

[TABLE]
Status code | Description
200 | OK
403 | Forbidden
404 | Resource not found
[/TABLE]
OK
Forbidden
Resource not found

### Code samples for "Export a software bill of materials (SBOM) for a repository."

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/dependency-graph/sbom
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "sbom": {
    "SPDXID": "SPDXRef-DOCUMENT",
    "spdxVersion": "SPDX-2.3",
    "creationInfo": {
      "created": "2021-09-01T00:00:00Z",
      "creators": [
        "Tool: GitHub.com-Dependency-Graph"
      ]
    },
    "name": "github/example",
    "dataLicense": "CC0-1.0",
    "documentNamespace": "https://spdx.org/spdxdocs/protobom/15e41dd2-f961-4f4d-b8dc-f8f57ad70d57",
    "packages": [
      {
        "name": "rails",
        "SPDXID": "SPDXRef-Package",
        "versionInfo": "1.0.0",
        "downloadLocation": "NOASSERTION",
        "filesAnalyzed": false,
        "licenseConcluded": "MIT",
        "licenseDeclared": "MIT",
        "copyrightText": "Copyright (c) 1985 GitHub.com",
        "externalRefs": [
          {
            "referenceCategory": "PACKAGE-MANAGER",
            "referenceType": "purl",
            "referenceLocator": "pkg:gem/rails@1.0.0"
          }
        ]
      },
      {
        "name": "github/example",
        "SPDXID": "SPDXRef-Repository",
        "versionInfo": "main",
        "downloadLocation": "NOASSERTION",
        "filesAnalyzed": false,
        "externalRefs": [
          {
            "referenceCategory": "PACKAGE-MANAGER",
            "referenceType": "purl",
            "referenceLocator": "pkg:github/example@main"
          }
        ]
      }
    ],
    "relationships": [
      {
        "relationshipType": "DEPENDS_ON",
        "spdxElementId": "SPDXRef-Repository",
        "relatedSpdxElement": "SPDXRef-Package"
      },
      {
        "relationshipType": "DESCRIBES",
        "spdxElementId": "SPDXRef-DOCUMENT",
        "relatedSpdxElement": "SPDXRef-Repository"
      }
    ]
  }
}
```