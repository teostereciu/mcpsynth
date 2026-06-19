# REST API endpoints for artifact metadata

*Source: https://docs.github.com/en/rest/orgs/artifact-metadata*

---

# REST API endpoints for artifact metadata
Use these endpoints to retrieve and manage metadata for artifacts in your organization. Artifact metadata provides information about build artifacts, their provenance, and related details.
You can use these endpoints to upload storage and deployment records for software that your organization builds with GitHub Actions. The records are displayed on the organization's linked artifacts page. SeeAbout linked artifacts.

## Create an artifact deployment record
Create or update deployment records for an artifact associated
with an organization.
This endpoint allows you to record information about a specific
artifact, such as its name, digest, environments, cluster, and
deployment.
The deployment name has to be uniqe within a cluster (i.e a
combination of logical, physical environment and cluster) as it
identifies unique deployment.
Multiple requests for the same combination of logical, physical
environment, cluster and deployment name will only create one
record, successive request will update the existing record.
This allows for a stable tracking of a deployment where the actual
deployed artifact can change over time.

### Fine-grained access tokens for "Create an artifact deployment record"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have at least one of the following permission sets:
- "Contents" repository permissions (write)
- "Artifact metadata" repository permissions (write)

### Parameters for "Create an artifact deployment record"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
[/TABLE]
The organization name. The name is not case sensitive.

[TABLE]
Name, Type, Description
namestringRequiredThe name of the artifact.
digeststringRequiredThe hex encoded digest of the artifact.
versionstringThe artifact version.
statusstringRequiredThe status of the artifact. Can be either deployed or decommissioned.Can be one of:deployed,decommissioned
logical_environmentstringRequiredThe stage of the deployment.
physical_environmentstringThe physical region of the deployment.
clusterstringThe deployment cluster.
deployment_namestringRequiredThe unique identifier for the deployment represented by the new record. To accommodate differing
containers and namespaces within a cluster, the following format is recommended:
{namespaceName}-{deploymentName}-{containerName}.
tagsobjectThe tags associated with the deployment.
runtime_risksarray of stringsA list of runtime risks associated with the deployment.
Supported values are:critical-resource,internet-exposed,lateral-movement,sensitive-data
github_repositorystringThe name of the GitHub repository associated with the artifact. This should be used
when there are no provenance attestations available for the artifact. The repository
must belong to the organization specified in the path parameter.If a provenance attestation is available for the artifact, the API will use
the repository information from the attestation instead of this parameter.
[/TABLE]
The name of the artifact.
The hex encoded digest of the artifact.
The artifact version.
The status of the artifact. Can be either deployed or decommissioned.
Can be one of:deployed,decommissioned

```
decommissioned
```

```
logical_environment
```
The stage of the deployment.

```
physical_environment
```
The physical region of the deployment.
The deployment cluster.

```
deployment_name
```
The unique identifier for the deployment represented by the new record. To accommodate differing
containers and namespaces within a cluster, the following format is recommended:
{namespaceName}-{deploymentName}-{containerName}.
The tags associated with the deployment.

```
runtime_risks
```
A list of runtime risks associated with the deployment.
Supported values are:critical-resource,internet-exposed,lateral-movement,sensitive-data

```
github_repository
```
The name of the GitHub repository associated with the artifact. This should be used
when there are no provenance attestations available for the artifact. The repository
must belong to the organization specified in the path parameter.
If a provenance attestation is available for the artifact, the API will use
the repository information from the attestation instead of this parameter.

### HTTP response status codes for "Create an artifact deployment record"

[TABLE]
Status code | Description
200 | Artifact deployment record stored successfully.
[/TABLE]
Artifact deployment record stored successfully.

### Code samples for "Create an artifact deployment record"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/artifacts/metadata/deployment-record \
  -d '{"name":"awesome-image","digest":"sha256:1bb1e949e55dcefc6353e7b36c8897d2a107d8e8dca49d4e3c0ea8493fc0bc72","status":"deployed","logical_environment":"prod","physical_environment":"pacific-east","cluster":"moda-1","deployment_name":"deployment-pod","tags":{"data-access":"sensitive"}}'
```

#### Artifact deployment record stored successfully.
- Example response
- Response schema

```
Status: 200
```

```
{
  "total_count": 1,
  "deployment_records": [
    {
      "id": 123,
      "digest": "sha256:1bb1e949e55dcefc6353e7b36c8897d2a107d8e8dca49d4e3c0ea8493fc0bc72",
      "logical_environment": "prod",
      "physical_environment": "pacific-east",
      "cluster": "moda-1",
      "deployment_name": "prod-deployment",
      "tags": {
        "data": "sensitive"
      },
      "created": "2011-01-26T19:14:43Z",
      "updated_at": "2011-01-26T19:14:43Z",
      "attestation_id": 456
    }
  ]
}
```

## Set cluster deployment records
Set deployment records for a given cluster.
If proposed records in the 'deployments' field have identical 'cluster', 'logical_environment',
'physical_environment', and 'deployment_name' values as existing records, the existing records will be updated.
If no existing records match, new records will be created.

### Fine-grained access tokens for "Set cluster deployment records"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have at least one of the following permission sets:
- "Contents" repository permissions (write)
- "Artifact metadata" repository permissions (write)

### Parameters for "Set cluster deployment records"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
clusterstringRequiredThe cluster name.
[/TABLE]
The organization name. The name is not case sensitive.
The cluster name.

[TABLE]
Name, Type, Description
logical_environmentstringRequiredThe stage of the deployment.
physical_environmentstringThe physical region of the deployment.
deploymentsarray of objectsRequiredThe list of deployments to record.
Properties ofdeploymentsName, Type, DescriptionnamestringRequiredThe name of the artifact. Note that if multiple deployments have identical 'digest' parameter values,
the name parameter must also be identical across all entries.digeststringRequiredThe hex encoded digest of the artifact. Note that if multiple deployments have identical 'digest' parameter values,
the name and version parameters must also be identical across all entries.versionstringThe artifact version. Note that if multiple deployments have identical 'digest' parameter values,
the version parameter must also be identical across all entries.statusstringThe deployment status of the artifact.Default:deployedCan be one of:deployed,decommissioneddeployment_namestringRequiredThe unique identifier for the deployment represented by the new record. To accommodate differing
containers and namespaces within a record set, the following format is recommended:
{namespaceName}-{deploymentName}-{containerName}.
The deployment_name must be unique across all entries in the deployments array.github_repositorystringThe name of the GitHub repository associated with the artifact. This should be used
when there are no provenance attestations available for the artifact. The repository
must belong to the organization specified in the path parameter.If a provenance attestation is available for the artifact, the API will use
the repository information from the attestation instead of this parameter.tagsobjectKey-value pairs to tag the deployment record.runtime_risksarray of stringsA list of runtime risks associated with the deployment.
Supported values are:critical-resource,internet-exposed,lateral-movement,sensitive-data | Name, Type, Description | namestringRequiredThe name of the artifact. Note that if multiple deployments have identical 'digest' parameter values,
the name parameter must also be identical across all entries. | digeststringRequiredThe hex encoded digest of the artifact. Note that if multiple deployments have identical 'digest' parameter values,
the name and version parameters must also be identical across all entries. | versionstringThe artifact version. Note that if multiple deployments have identical 'digest' parameter values,
the version parameter must also be identical across all entries. | statusstringThe deployment status of the artifact.Default:deployedCan be one of:deployed,decommissioned | deployment_namestringRequiredThe unique identifier for the deployment represented by the new record. To accommodate differing
containers and namespaces within a record set, the following format is recommended:
{namespaceName}-{deploymentName}-{containerName}.
The deployment_name must be unique across all entries in the deployments array. | github_repositorystringThe name of the GitHub repository associated with the artifact. This should be used
when there are no provenance attestations available for the artifact. The repository
must belong to the organization specified in the path parameter.If a provenance attestation is available for the artifact, the API will use
the repository information from the attestation instead of this parameter. | tagsobjectKey-value pairs to tag the deployment record. | runtime_risksarray of stringsA list of runtime risks associated with the deployment.
Supported values are:critical-resource,internet-exposed,lateral-movement,sensitive-data
Name, Type, Description
namestringRequiredThe name of the artifact. Note that if multiple deployments have identical 'digest' parameter values,
the name parameter must also be identical across all entries.
digeststringRequiredThe hex encoded digest of the artifact. Note that if multiple deployments have identical 'digest' parameter values,
the name and version parameters must also be identical across all entries.
versionstringThe artifact version. Note that if multiple deployments have identical 'digest' parameter values,
the version parameter must also be identical across all entries.
statusstringThe deployment status of the artifact.Default:deployedCan be one of:deployed,decommissioned
deployment_namestringRequiredThe unique identifier for the deployment represented by the new record. To accommodate differing
containers and namespaces within a record set, the following format is recommended:
{namespaceName}-{deploymentName}-{containerName}.
The deployment_name must be unique across all entries in the deployments array.
github_repositorystringThe name of the GitHub repository associated with the artifact. This should be used
when there are no provenance attestations available for the artifact. The repository
must belong to the organization specified in the path parameter.If a provenance attestation is available for the artifact, the API will use
the repository information from the attestation instead of this parameter.
tagsobjectKey-value pairs to tag the deployment record.
runtime_risksarray of stringsA list of runtime risks associated with the deployment.
Supported values are:critical-resource,internet-exposed,lateral-movement,sensitive-data
[/TABLE]

```
logical_environment
```
The stage of the deployment.

```
physical_environment
```
The physical region of the deployment.

```
deployments
```
The list of deployments to record.

```
deployments
```

[TABLE]
Name, Type, Description
namestringRequiredThe name of the artifact. Note that if multiple deployments have identical 'digest' parameter values,
the name parameter must also be identical across all entries.
digeststringRequiredThe hex encoded digest of the artifact. Note that if multiple deployments have identical 'digest' parameter values,
the name and version parameters must also be identical across all entries.
versionstringThe artifact version. Note that if multiple deployments have identical 'digest' parameter values,
the version parameter must also be identical across all entries.
statusstringThe deployment status of the artifact.Default:deployedCan be one of:deployed,decommissioned
deployment_namestringRequiredThe unique identifier for the deployment represented by the new record. To accommodate differing
containers and namespaces within a record set, the following format is recommended:
{namespaceName}-{deploymentName}-{containerName}.
The deployment_name must be unique across all entries in the deployments array.
github_repositorystringThe name of the GitHub repository associated with the artifact. This should be used
when there are no provenance attestations available for the artifact. The repository
must belong to the organization specified in the path parameter.If a provenance attestation is available for the artifact, the API will use
the repository information from the attestation instead of this parameter.
tagsobjectKey-value pairs to tag the deployment record.
runtime_risksarray of stringsA list of runtime risks associated with the deployment.
Supported values are:critical-resource,internet-exposed,lateral-movement,sensitive-data
[/TABLE]
The name of the artifact. Note that if multiple deployments have identical 'digest' parameter values,
the name parameter must also be identical across all entries.
The hex encoded digest of the artifact. Note that if multiple deployments have identical 'digest' parameter values,
the name and version parameters must also be identical across all entries.
The artifact version. Note that if multiple deployments have identical 'digest' parameter values,
the version parameter must also be identical across all entries.
The deployment status of the artifact.
Default:deployed
Can be one of:deployed,decommissioned

```
decommissioned
```

```
deployment_name
```
The unique identifier for the deployment represented by the new record. To accommodate differing
containers and namespaces within a record set, the following format is recommended:
{namespaceName}-{deploymentName}-{containerName}.
The deployment_name must be unique across all entries in the deployments array.

```
github_repository
```
The name of the GitHub repository associated with the artifact. This should be used
when there are no provenance attestations available for the artifact. The repository
must belong to the organization specified in the path parameter.
If a provenance attestation is available for the artifact, the API will use
the repository information from the attestation instead of this parameter.
Key-value pairs to tag the deployment record.

```
runtime_risks
```
A list of runtime risks associated with the deployment.
Supported values are:critical-resource,internet-exposed,lateral-movement,sensitive-data

### HTTP response status codes for "Set cluster deployment records"

[TABLE]
Status code | Description
200 | Deployment records created or updated successfully.
[/TABLE]
Deployment records created or updated successfully.

### Code samples for "Set cluster deployment records"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/artifacts/metadata/deployment-record/cluster/CLUSTER \
  -d '{"logical_environment":"prod","physical_environment":"pacific-east","deployments":[{"name":"awesome-image","digest":"sha256:1bb1e949e55dcefc6353e7b36c8897d2a107d8e8dca49d4e3c0ea8493fc0bc72","version":"2.1.0","status":"deployed","deployment_name":"deployment-pod","tags":{"runtime-risk":"sensitive-data"}}]}'
```

#### Deployment records created or updated successfully.
- Example response
- Response schema

```
Status: 200
```

```
{
  "total_count": 1,
  "deployment_records": [
    {
      "id": 123,
      "digest": "sha256:1bb1e949e55dcefc6353e7b36c8897d2a107d8e8dca49d4e3c0ea8493fc0bc72",
      "logical_environment": "prod",
      "physical_environment": "pacific-east",
      "cluster": "moda-1",
      "deployment_name": "prod-deployment",
      "tags": {
        "data": "sensitive"
      },
      "created": "2011-01-26T19:14:43Z",
      "updated_at": "2011-01-26T19:14:43Z",
      "attestation_id": 456
    }
  ]
}
```

## Create artifact metadata storage record
Create metadata storage records for artifacts associated with an organization.
This endpoint will create a new artifact storage record on behalf of any artifact matching the provided digest and
associated with a repository owned by the organization.

### Fine-grained access tokens for "Create artifact metadata storage record"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have at least one of the following permission sets:
- "Contents" repository permissions (write)
- "Artifact metadata" repository permissions (write)

### Parameters for "Create artifact metadata storage record"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
[/TABLE]
The organization name. The name is not case sensitive.

[TABLE]
Name, Type, Description
namestringRequiredThe name of the artifact.
digeststringRequiredThe digest of the artifact (algorithm:hex-encoded-digest).
versionstringThe artifact version.
artifact_urlstringThe URL where the artifact is stored.
pathstringThe path of the artifact.
registry_urlstringRequiredThe base URL of the artifact registry.
repositorystringThe repository name within the registry.
statusstringThe status of the artifact (e.g., active, inactive).Default:activeCan be one of:active,eol,deleted
github_repositorystringThe name of the GitHub repository associated with the artifact. This should be used
when there are no provenance attestations available for the artifact. The repository
must belong to the organization specified in the path parameter.If a provenance attestation is available for the artifact, the API will use
the repository information from the attestation instead of this parameter.
[/TABLE]
The name of the artifact.
The digest of the artifact (algorithm:hex-encoded-digest).
The artifact version.

```
artifact_url
```
The URL where the artifact is stored.
The path of the artifact.

```
registry_url
```
The base URL of the artifact registry.
The repository name within the registry.
The status of the artifact (e.g., active, inactive).
Default:active
Can be one of:active,eol,deleted

```
github_repository
```
The name of the GitHub repository associated with the artifact. This should be used
when there are no provenance attestations available for the artifact. The repository
must belong to the organization specified in the path parameter.
If a provenance attestation is available for the artifact, the API will use
the repository information from the attestation instead of this parameter.

### HTTP response status codes for "Create artifact metadata storage record"

[TABLE]
Status code | Description
200 | Artifact metadata storage record stored successfully.
[/TABLE]
Artifact metadata storage record stored successfully.

### Code samples for "Create artifact metadata storage record"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/artifacts/metadata/storage-record \
  -d '{"name":"libfoo","version":"1.2.3","digest":"sha256:1bb1e949e55dcefc6353e7b36c8897d2a107d8e8dca49d4e3c0ea8493fc0bc72","artifact_url":"https://reg.example.com/artifactory/bar/libfoo-1.2.3","registry_url":"https://reg.example.com/artifactory/","repository":"bar","status":"active"}'
```

#### Artifact metadata storage record stored successfully.
- Example response
- Response schema

```
Status: 200
```

```
{
  "total_count": 1,
  "storage_records": [
    {
      "name": "libfoo",
      "digest": "sha256:1bb1e949e55dcefc6353e7b36c8897d2a107d8e8dca49d4e3c0ea8493fc0bc72",
      "artifact_url": "https://reg.example.com/artifactory/bar/libfoo-1.2.3",
      "registry_url": "https://reg.example.com/artifactory/",
      "repository": "bar",
      "status": "active",
      "created_at": "2023-10-01T12:00:00Z",
      "updated_at": "2023-10-01T12:00:00Z"
    }
  ]
}
```

## List artifact deployment records
List deployment records for an artifact metadata associated with an organization.

### Fine-grained access tokens for "List artifact deployment records"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have at least one of the following permission sets:
- "Contents" repository permissions (read)
- "Artifact metadata" repository permissions (read)

### Parameters for "List artifact deployment records"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
subject_digeststringRequiredThe SHA256 digest of the artifact, in the formsha256:HEX_DIGEST.
[/TABLE]
The organization name. The name is not case sensitive.

```
subject_digest
```
The SHA256 digest of the artifact, in the formsha256:HEX_DIGEST.

### HTTP response status codes for "List artifact deployment records"

[TABLE]
Status code | Description
200 | Successful response
[/TABLE]
Successful response

### Code samples for "List artifact deployment records"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/artifacts/SUBJECT_DIGEST/metadata/deployment-records
```

#### Successful response
- Example response
- Response schema

```
Status: 200
```

```
{
  "total_count": 1,
  "deployment_records": [
    {
      "id": 123,
      "digest": "sha256:1bb1e949e55dcefc6353e7b36c8897d2a107d8e8dca49d4e3c0ea8493fc0bc72",
      "logical_environment": "prod",
      "physical_environment": "pacific-east",
      "cluster": "moda-1",
      "deployment_name": "prod-deployment",
      "tags": {
        "data": "sensitive"
      },
      "created": "2011-01-26T19:14:43Z",
      "updated_at": "2011-01-26T19:14:43Z",
      "attestation_id": 456
    }
  ]
}
```

## List artifact storage records
List a collection of artifact storage records with a given subject digest that are associated with repositories owned by an organization.
The collection of storage records returned by this endpoint is filtered according to the authenticated user's permissions; if the authenticated user cannot read a repository, the attestations associated with that repository will not be included in the response. In addition, when using a fine-grained access token thecontent:readpermission is required.

### Fine-grained access tokens for "List artifact storage records"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have at least one of the following permission sets:
- "Contents" repository permissions (read)
- "Artifact metadata" repository permissions (read)

### Parameters for "List artifact storage records"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
subject_digeststringRequiredThe parameter should be set to the attestation's subject's SHA256 digest, in the formsha256:HEX_DIGEST.
[/TABLE]
The organization name. The name is not case sensitive.

```
subject_digest
```
The parameter should be set to the attestation's subject's SHA256 digest, in the formsha256:HEX_DIGEST.

### HTTP response status codes for "List artifact storage records"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "List artifact storage records"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/artifacts/SUBJECT_DIGEST/metadata/storage-records
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "storage_records": [
    {
      "name": "libfoo-1.2.3",
      "digest": "sha256:1bb1e949e55dcefc6353e7b36c8897d2a107d8e8dca49d4e3c0ea8493fc0bc72",
      "artifact_url": "https://reg.example.com/artifactory/bar/libfoo-1.2.3",
      "registry_url": "https://reg.example.com/artifactory/",
      "repository": "bar",
      "status": "active",
      "created_at": "2023-10-01T12:00:00Z",
      "updated_at": "2023-10-01T12:00:00Z"
    }
  ]
}
```