from typing import Any, Dict, List, Optional
from generated_tools.utils import stripe_request

def register_tools(mcp):
    @mcp.tool()
    def create_payment_intent(
        amount: int,
        currency: str,
        payment_method_types: Optional[List[str]] = None,
        metadata: Optional[Dict[str, str]] = None,
        description: Optional[str] = None,
        receipt_email: Optional[str] = None,
        customer: Optional[str] = None,
        setup_future_usage: Optional[str] = None,
        statement_descriptor: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Create a PaymentIntent to track and guide a customer through the payment flow.
        
        Args:
            amount: Amount intended to be collected in the smallest currency unit (e.g., 1000 for $10.00).
            currency: Three-letter ISO currency code, in lowercase (e.g., usd, eur).
            payment_method_types: List of payment method types (e.g., ['card']).
            metadata: Set of key-value pairs for storing custom data.
            description: An arbitrary string attached to the object.
            receipt_email: Email address that the receipt for this charge will be sent to.
            customer: ID of the Customer this PaymentIntent is for, if one exists.
            setup_future_usage: Indicates how you intend to use the payment method (e.g., 'off_session', 'on_session').
            statement_descriptor: Text that appears on the customer's statement.
        """
        params = {
            "amount": amount,
            "currency": currency,
        }
        if payment_method_types is not None:
            params["payment_method_types"] = payment_method_types
        if metadata is not None:
            params["metadata"] = metadata
        if description is not None:
            params["description"] = description
        if receipt_email is not None:
            params["receipt_email"] = receipt_email
        if customer is not None:
            params["customer"] = customer
        if setup_future_usage is not None:
            params["setup_future_usage"] = setup_future_usage
        if statement_descriptor is not None:
            params["statement_descriptor"] = statement_descriptor

        return stripe_request("POST", "/v1/payment_intents", params)

    @mcp.tool()
    def retrieve_payment_intent(id: str) -> Dict[str, Any]:
        """
        Retrieve the details of an existing PaymentIntent.
        
        Args:
            id: The identifier of the PaymentIntent to retrieve.
        """
        return stripe_request("GET", f"/v1/payment_intents/{id}")

    @mcp.tool()
    def update_payment_intent(
        id: str,
        amount: Optional[int] = None,
        currency: Optional[str] = None,
        metadata: Optional[Dict[str, str]] = None,
        description: Optional[str] = None,
        receipt_email: Optional[str] = None,
        customer: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Update properties on a PaymentIntent.
        
        Args:
            id: The identifier of the PaymentIntent to update.
            amount: Amount intended to be collected.
            currency: Three-letter ISO currency code.
            metadata: Set of key-value pairs for storing custom data.
            description: An arbitrary string attached to the object.
            receipt_email: Email address that the receipt for this charge will be sent to.
            customer: ID of the Customer this PaymentIntent is for.
        """
        params = {}
        if amount is not None:
            params["amount"] = amount
        if currency is not None:
            params["currency"] = currency
        if metadata is not None:
            params["metadata"] = metadata
        if description is not None:
            params["description"] = description
        if receipt_email is not None:
            params["receipt_email"] = receipt_email
        if customer is not None:
            params["customer"] = customer

        return stripe_request("POST", f"/v1/payment_intents/{id}", params)

    @mcp.tool()
    def confirm_payment_intent(
        id: str,
        payment_method: Optional[str] = None,
        receipt_email: Optional[str] = None,
        return_url: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Confirm that the customer intends to pay with the presented payment method.
        
        Args:
            id: The identifier of the PaymentIntent to confirm.
            payment_method: ID of the payment method to associate with this PaymentIntent.
            receipt_email: Email address that the receipt for this charge will be sent to.
            return_url: The URL to redirect your customer back to after they authenticate or complete the payment.
        """
        params = {}
        if payment_method is not None:
            params["payment_method"] = payment_method
        if receipt_email is not None:
            params["receipt_email"] = receipt_email
        if return_url is not None:
            params["return_url"] = return_url

        return stripe_request("POST", f"/v1/payment_intents/{id}/confirm", params)

    @mcp.tool()
    def cancel_payment_intent(
        id: str,
        cancellation_reason: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Cancel a PaymentIntent.
        
        Args:
            id: The identifier of the PaymentIntent to cancel.
            cancellation_reason: Reason for canceling this PaymentIntent (e.g., 'duplicate', 'fraudulent', 'requested_by_customer').
        """
        params = {}
        if cancellation_reason is not None:
            params["cancellation_reason"] = cancellation_reason

        return stripe_request("POST", f"/v1/payment_intents/{id}/cancel", params)

    @mcp.tool()
    def list_payment_intents(
        limit: Optional[int] = 10,
        starting_after: Optional[str] = None,
        customer: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        List all PaymentIntents.
        
        Args:
            limit: A limit on the number of objects to be returned, between 1 and 100.
            starting_after: A cursor for pagination (an object ID).
            customer: Only return PaymentIntents for the customer specified by this customer ID.
        """
        params = {}
        if limit is not None:
            params["limit"] = limit
        if starting_after is not None:
            params["starting_after"] = starting_after
        if customer is not None:
            params["customer"] = customer

        return stripe_request("GET", "/v1/payment_intents", params)
