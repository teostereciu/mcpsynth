"""
Stripe Search tools.
Endpoints covered:
  GET    /v1/charges/search
  GET    /v1/customers/search
  GET    /v1/invoices/search
  GET    /v1/payment_intents/search
  GET    /v1/prices/search
  GET    /v1/products/search
  GET    /v1/subscriptions/search
"""

from mcp.server.fastmcp import FastMCP
from .client import stripe_request


def register(mcp: FastMCP):

    @mcp.tool()
    def search_charges(
        query: str,
        limit: int = None,
        page: str = None,
    ) -> dict:
        """
        Search Charges using Stripe's search query syntax.
        Example query: "amount>1000 AND currency:'usd'"
        """
        params = {"query": query}
        if limit is not None:
            params["limit"] = limit
        if page:
            params["page"] = page
        return stripe_request("GET", "/v1/charges/search", params=params)

    @mcp.tool()
    def search_customers(
        query: str,
        limit: int = None,
        page: str = None,
    ) -> dict:
        """
        Search Customers using Stripe's search query syntax.
        Example query: "email:'user@example.com'"
        """
        params = {"query": query}
        if limit is not None:
            params["limit"] = limit
        if page:
            params["page"] = page
        return stripe_request("GET", "/v1/customers/search", params=params)

    @mcp.tool()
    def search_invoices(
        query: str,
        limit: int = None,
        page: str = None,
    ) -> dict:
        """
        Search Invoices using Stripe's search query syntax.
        Example query: "status:'open' AND total>1000"
        """
        params = {"query": query}
        if limit is not None:
            params["limit"] = limit
        if page:
            params["page"] = page
        return stripe_request("GET", "/v1/invoices/search", params=params)

    @mcp.tool()
    def search_payment_intents(
        query: str,
        limit: int = None,
        page: str = None,
    ) -> dict:
        """
        Search PaymentIntents using Stripe's search query syntax.
        Example query: "status:'succeeded' AND amount>5000"
        """
        params = {"query": query}
        if limit is not None:
            params["limit"] = limit
        if page:
            params["page"] = page
        return stripe_request("GET", "/v1/payment_intents/search", params=params)

    @mcp.tool()
    def search_prices(
        query: str,
        limit: int = None,
        page: str = None,
    ) -> dict:
        """
        Search Prices using Stripe's search query syntax.
        Example query: "currency:'usd' AND active:'true'"
        """
        params = {"query": query}
        if limit is not None:
            params["limit"] = limit
        if page:
            params["page"] = page
        return stripe_request("GET", "/v1/prices/search", params=params)

    @mcp.tool()
    def search_products(
        query: str,
        limit: int = None,
        page: str = None,
    ) -> dict:
        """
        Search Products using Stripe's search query syntax.
        Example query: "active:'true' AND name~'widget'"
        """
        params = {"query": query}
        if limit is not None:
            params["limit"] = limit
        if page:
            params["page"] = page
        return stripe_request("GET", "/v1/products/search", params=params)

    @mcp.tool()
    def search_subscriptions(
        query: str,
        limit: int = None,
        page: str = None,
    ) -> dict:
        """
        Search Subscriptions using Stripe's search query syntax.
        Example query: "status:'active' AND customer:'cus_xxx'"
        """
        params = {"query": query}
        if limit is not None:
            params["limit"] = limit
        if page:
            params["page"] = page
        return stripe_request("GET", "/v1/subscriptions/search", params=params)
