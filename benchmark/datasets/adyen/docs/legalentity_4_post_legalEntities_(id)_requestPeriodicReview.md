# legalentity/4/post/legalEntities/(id)/requestPeriodicReview

*Source: https://docs.adyen.com/api-explorer/legalentity/4/post/legalEntities/(id)/requestPeriodicReview*

---

# Request periodic data review
Requests a periodic data review for the legal entity of the user specified in the path.
The unique identifier of the legal entity.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 204 - No ContentThe request has been successfully processed, but there is no additional content.

#### 204 - No Content