# Submit data to a form (supporting authentication)

*Source: https://developers.hubspot.com/docs/api-reference/legacy/marketing/forms/v3-legacy/submit-data-authenticated*

---

v3 legacy

# Submit data to a form (supporting authentication)

Send form submission data to a HubSpot form, specified by form ID. This endpoint requires authentication and has higher rate limits.

POST

/

submissions

/

v3

/

integration

/

secure

/

submit

/

{portalId}

/

{formGuid}

Try it

Submit data to a form (supporting authentication)

cURL


    curl --request POST \
      --url https://api.hsforms.com/submissions/v3/integration/secure/submit/{portalId}/{formGuid} \
      --header 'Content-Type: application/json' \
      --data '
    {
      "fields": [
        {
          "objectTypeId": "<string>",
          "name": "<string>",
          "value": "<string>"
        }
      ],
      "submittedAt": "<string>",
      "context": {
        "hutk": "<string>",
        "ipAddress": "<string>",
        "pageName": "<string>",
        "pageUri": "<string>",
        "pageId": "<string>",
        "sfdcCampaignId": "<string>",
        "goToWebinarWebinarKey": "<string>"
      },
      "legalConsentOptions": {},
      "skipValidation": true
    }
    '

200

400

429

default


    {
      "redirectUri": "<string>",
      "inlineMessage": "<string>"
    }

Scope requirements

#### Path Parameters

​

portalId

string

required

The HubSpot portal the form belongs to.

​

formGuid

string

required

The ID of the form you're sending data to.

#### Body

application/json

​

fields

object[]

required

A list of form field names and the values for those fields, up to 1000 fields can be included.

Maximum array length: `1000`

Show child attributes

​

submittedAt

string

A millisecond timestamp representing the time of the form submission. This can be used to backdate the submission, but using a time more than one month old will result in an error.

​

context

object

Show child attributes

​

legalConsentOptions

object

Show child attributes

​

skipValidation

boolean

deprecated

Whether or not to skip validation based on the form settings. Defaults to false. Note: This parameter is deprecated.

#### Response

200

application/json

Form submission successful

​

redirectUri

string

If the submission was accepted, and the form has a redirect URI set in its settings, this will be that redirect URI

​

inlineMessage

string

If the submission was accepted, and the form has an inline thank you message set in its settings, this will be the HTML for that message

Last modified on March 30, 2026

Was this page helpful?

YesNo

⌘I

[facebook](https://www.facebook.com/hubspot)[instagram](https://www.instagram.com/hubspot)[youtube](https://youtube.com/user/HubSpot)[x](https://x.com/HubSpot)[linkedin](https://www.linkedin.com/company/hubspot)[medium](https://medium.com/@HubSpot)