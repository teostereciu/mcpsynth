import os
import requests
from mcp.server.fastmcp import FastMCP

class StripeClient:
    BASE_URL = "https://api.stripe.com/v1"

    def __init__(self):
        self.api_key = os.environ.get("STRIPE_API_KEY")
        if not self.api_key:
            raise ValueError("STRIPE_API_KEY environment variable not set.")
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/x-www-form-urlencoded",
        }

    def _request(self, method, path, data=None):
        url = f"{self.BASE_URL}{path}"
        try:
            response = requests.request(method, url, headers=self.headers, data=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            return {"error": str(e), "status_code": e.response.status_code, "response": e.response.json()}
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

    # --- Customer Tools ---
    def create_customer(self, email: str, description: str = None):
        """Creates a new customer.
        Args:
            email: Customer's email address.
            description: An arbitrary string that you can attach to a customer.
        """
        data = {"email": email}
        if description:
            data["description"] = description
        return self._request("POST", "/customers", data=data)

    def get_customer(self, customer_id: str):
        """Retrieves a customer by ID.
        Args:
            customer_id: The ID of the customer to retrieve.
        """
        return self._request("GET", f"/customers/{customer_id}")

    def update_customer(self, customer_id: str, email: str = None, description: str = None):
        """Updates an existing customer.
        Args:
            customer_id: The ID of the customer to update.
            email: Customer's email address.
            description: An arbitrary string that you can attach to a customer.
        """
        data = {}
        if email:
            data["email"] = email
        if description:
            data["description"] = description
        if not data:
            return {"error": "No update parameters provided."}
        return self._request("POST", f"/customers/{customer_id}", data=data)

    def delete_customer(self, customer_id: str):
        """Deletes a customer.
        Args:
            customer_id: The ID of the customer to delete.
        """
        return self._request("DELETE", f"/customers/{customer_id}")

    def list_customers(self, limit: int = 10, starting_after: str = None, ending_before: str = None):
        """Lists all customers.
        Args:
            limit: A limit on the number of objects to be returned.
            starting_after: A cursor for use in pagination.
            ending_before: A cursor for use in pagination.
        """
        params = {"limit": limit}
        if starting_after:
            params["starting_after"] = starting_after
        if ending_before:
            params["ending_before"] = ending_before
        return self._request("GET", "/customers", data=params) # GET with data is unusual, but requests handles it as params

    # --- Payment Intent Tools ---
    def create_payment_intent(self, amount: int, currency: str, customer_id: str = None, description: str = None):
        """Creates a PaymentIntent.
        Args:
            amount: Amount in cents to be collected.
            currency: Three-letter ISO currency code.
            customer_id: ID of the customer this PaymentIntent belongs to.
            description: An arbitrary string attached to the object.
        """
        data = {"amount": amount, "currency": currency}
        if customer_id:
            data["customer"] = customer_id
        if description:
            data["description"] = description
        return self._request("POST", "/payment_intents", data=data)

    def get_payment_intent(self, pi_id: str):
        """Retrieves a PaymentIntent.
        Args:
            pi_id: The ID of the PaymentIntent to retrieve.
        """
        return self._request("GET", f"/payment_intents/{pi_id}")

    def confirm_payment_intent(self, pi_id: str, payment_method: str = None):
        """Confirms a PaymentIntent.
        Args:
            pi_id: The ID of the PaymentIntent to confirm.
            payment_method: ID of the payment method to confirm with.
        """
        data = {}
        if payment_method:
            data["payment_method"] = payment_method
        return self._request("POST", f"/payment_intents/{pi_id}/confirm", data=data)

    def cancel_payment_intent(self, pi_id: str):
        """Cancels a PaymentIntent.
        Args:
            pi_id: The ID of the PaymentIntent to cancel.
        """
        return self._request("POST", f"/payment_intents/{pi_id}/cancel")

    def list_payment_intents(self, limit: int = 10, customer_id: str = None):
        """Lists all PaymentIntents.
        Args:
            limit: A limit on the number of objects to be returned.
            customer_id: Only return PaymentIntents for this customer.
        """
        params = {"limit": limit}
        if customer_id:
            params["customer"] = customer_id
        return self._request("GET", "/payment_intents", data=params)

    # --- Charge Tools ---
    def create_charge(self, amount: int, currency: str, source: str, customer_id: str = None, description: str = None):
        """Creates a new charge.
        Args:
            amount: Amount in cents to be charged.
            currency: Three-letter ISO currency code.
            source: A payment source to be charged, such as a credit card, a bank account, or a token.
            customer_id: The ID of an existing customer that will be charged.
            description: An arbitrary string attached to the object.
        """
        data = {"amount": amount, "currency": currency, "source": source}
        if customer_id:
            data["customer"] = customer_id
        if description:
            data["description"] = description
        return self._request("POST", "/charges", data=data)

    def get_charge(self, charge_id: str):
        """Retrieves a charge by ID.
        Args:
            charge_id: The ID of the charge to retrieve.
        """
        return self._request("GET", f"/charges/{charge_id}")

    def refund_charge(self, charge_id: str, amount: int = None):
        """Refunds a charge.
        Args:
            charge_id: The ID of the charge to refund.
            amount: A positive integer in cents representing how much of the charge to refund.
        """
        data = {}
        if amount:
            data["amount"] = amount
        return self._request("POST", f"/charges/{charge_id}/refund", data=data)

    def list_charges(self, limit: int = 10, customer_id: str = None):
        """Lists all charges.
        Args:
            limit: A limit on the number of objects to be returned.
            customer_id: Only return charges for this customer.
        """
        params = {"limit": limit}
        if customer_id:
            params["customer"] = customer_id
        return self._request("GET", "/charges", data=params)

    # --- Refund Tools ---
    def get_refund(self, refund_id: str):
        """Retrieves a refund by ID.
        Args:
            refund_id: The ID of the refund to retrieve.
        """
        return self._request("GET", f"/refunds/{refund_id}")

    def list_refunds(self, limit: int = 10, charge_id: str = None):
        """Lists all refunds.
        Args:
            limit: A limit on the number of objects to be returned.
            charge_id: Only return refunds for this charge.
        """
        params = {"limit": limit}
        if charge_id:
            params["charge"] = charge_id
        return self._request("GET", "/refunds", data=params)

    # --- Product Tools ---
    def create_product(self, name: str, description: str = None, active: bool = True):
        """Creates a new product.
        Args:
            name: The product's name, displayable to customers.
            description: The product's description, displayable to customers.
            active: Whether the product is available for purchase.
        """
        data = {"name": name, "active": active}
        if description:
            data["description"] = description
        return self._request("POST", "/products", data=data)

    def get_product(self, product_id: str):
        """Retrieves a product by ID.
        Args:
            product_id: The ID of the product to retrieve.
        """
        return self._request("GET", f"/products/{product_id}")

    def update_product(self, product_id: str, name: str = None, description: str = None, active: bool = None):
        """Updates an existing product.
        Args:
            product_id: The ID of the product to update.
            name: The product's name, displayable to customers.
            description: The product's description, displayable to customers.
            active: Whether the product is available for purchase.
        """
        data = {}
        if name:
            data["name"] = name
        if description:
            data["description"] = description
        if active is not None:
            data["active"] = active
        if not data:
            return {"error": "No update parameters provided."}
        return self._request("POST", f"/products/{product_id}", data=data)

    def list_products(self, limit: int = 10, active: bool = None):
        """Lists all products.
        Args:
            limit: A limit on the number of objects to be returned.
            active: Only return products that are active or inactive.
        """
        params = {"limit": limit}
        if active is not None:
            params["active"] = active
        return self._request("GET", "/products", data=params)

    # --- Price Tools ---
    def create_price(self, product_id: str, unit_amount: int, currency: str, recurring_interval: str = None, recurring_interval_count: int = None):
        """Creates a new price.
        Args:
            product_id: The ID of the product that this price belongs to.
            unit_amount: The unit amount in cents to be charged, represented as a positive integer.
            currency: Three-letter ISO currency code.
            recurring_interval: The frequency at which a subscription is billed. Can be `day`, `week`, `month` or `year`.
            recurring_interval_count: The number of intervals between subscription billings. For example, `interval=month` and `interval_count=3` bills every three months.
        """
        data = {"product": product_id, "unit_amount": unit_amount, "currency": currency}
        if recurring_interval:
            data["recurring"] = {"interval": recurring_interval}
            if recurring_interval_count:
                data["recurring"]["interval_count"] = recurring_interval_count
        return self._request("POST", "/prices", data=data)

    def get_price(self, price_id: str):
        """Retrieves a price by ID.
        Args:
            price_id: The ID of the price to retrieve.
        """
        return self._request("GET", f"/prices/{price_id}")

    def list_prices(self, limit: int = 10, product_id: str = None, active: bool = None):
        """Lists all prices.
        Args:
            limit: A limit on the number of objects to be returned.
            product_id: Only return prices for this product.
            active: Only return prices that are active or inactive.
        """
        params = {"limit": limit}
        if product_id:
            params["product"] = product_id
        if active is not None:
            params["active"] = active
        return self._request("GET", "/prices", data=params)

    # --- Subscription Tools ---
    def create_subscription(self, customer_id: str, price_id: str, collection_method: str = "charge_automatically"):
        """Creates a new subscription.
        Args:
            customer_id: The ID of the customer to subscribe.
            price_id: The ID of the price to subscribe the customer to.
            collection_method: Either `charge_automatically` or `send_invoice`.
        """
        data = {"customer": customer_id, "items": [{"price": price_id}], "collection_method": collection_method}
        return self._request("POST", "/subscriptions", data=data)

    def get_subscription(self, subscription_id: str):
        """Retrieves a subscription by ID.
        Args:
            subscription_id: The ID of the subscription to retrieve.
        """
        return self._request("GET", f"/subscriptions/{subscription_id}")

    def update_subscription(self, subscription_id: str, price_id: str = None, cancel_at_period_end: bool = None):
        """Updates an existing subscription.
        Args:
            subscription_id: The ID of the subscription to update.
            price_id: The ID of the new price to subscribe the customer to.
            cancel_at_period_end: A flag that indicates whether the subscription should be canceled at the end of the current period.
        """
        data = {}
        if price_id:
            data["items"] = [{
                "id": "{{subscription_item_id}}", # This needs to be dynamic, but for now, a placeholder
                "price": price_id
            }]
        if cancel_at_period_end is not None:
            data["cancel_at_period_end"] = cancel_at_period_end
        if not data:
            return {"error": "No update parameters provided."}
        return self._request("POST", f"/subscriptions/{subscription_id}", data=data)

    def cancel_subscription(self, subscription_id: str):
        """Cancels a subscription immediately.
        Args:
            subscription_id: The ID of the subscription to cancel.
        """
        return self._request("DELETE", f"/subscriptions/{subscription_id}")

    def list_subscriptions(self, limit: int = 10, customer_id: str = None):
        """Lists all subscriptions.
        Args:
            limit: A limit on the number of objects to be returned.
            customer_id: Only return subscriptions for this customer.
        """
        params = {"limit": limit}
        if customer_id:
            params["customer"] = customer_id
        return self._request("GET", "/subscriptions", data=params)

    # --- Invoice Tools ---
    def get_invoice(self, invoice_id: str):
        """Retrieves an invoice by ID.
        Args:
            invoice_id: The ID of the invoice to retrieve.
        """
        return self._request("GET", f"/invoices/{invoice_id}")

    def list_invoices(self, limit: int = 10, customer_id: str = None):
        """Lists all invoices.
        Args:
            limit: A limit on the number of objects to be returned.
            customer_id: Only return invoices for this customer.
        """
        params = {"limit": limit}
        if customer_id:
            params["customer"] = customer_id
        return self._request("GET", "/invoices", data=params)

    # --- Checkout Session Tools ---
    def create_checkout_session(self, line_items: list, mode: str, success_url: str, cancel_url: str, customer_id: str = None):
        """Creates a new Checkout Session.
        Args:
            line_items: A list of items the customer is purchasing.
                        Each item should be a dictionary with 'price' (Price ID) and 'quantity'.
                        Example: [{'price': 'price_123', 'quantity': 1}]
            mode: The mode of the Checkout Session. Can be `payment`, `setup`, or `subscription`.
            success_url: The URL to which Stripe redirects your customer after a successful payment.
            cancel_url: The URL to which Stripe redirects your customer when they cancel payment.
            customer_id: The ID of an existing customer to use for this Checkout Session.
        """
        data = {
            "line_items": line_items,
            "mode": mode,
            "success_url": success_url,
            "cancel_url": cancel_url,
        }
        if customer_id:
            data["customer"] = customer_id
        return self._request("POST", "/checkout/sessions", data=data)

    def get_checkout_session(self, session_id: str):
        """Retrieves a Checkout Session by ID.
        Args:
            session_id: The ID of the Checkout Session to retrieve.
        """
        return self._request("GET", f"/checkout/sessions/{session_id}")

    # --- Payment Link Tools ---
    def create_payment_link(self, line_items: list, allow_promotion_codes: bool = False, active: bool = True):
        """Creates a new Payment Link.
        Args:
            line_items: A list of items the customer is purchasing.
                        Each item should be a dictionary with 'price' (Price ID) and 'quantity'.
                        Example: [{'price': 'price_123', 'quantity': 1}]
            allow_promotion_codes: Whether to allow customers to enter promotion codes.
            active: Whether the payment link is active.
        """
        data = {
            "line_items": line_items,
            "allow_promotion_codes": allow_promotion_codes,
            "active": active,
        }
        return self._request("POST", "/payment_links", data=data)

    def get_payment_link(self, payment_link_id: str):
        """Retrieves a Payment Link by ID.
        Args:
            payment_link_id: The ID of the Payment Link to retrieve.
        """
        return self._request("GET", f"/payment_links/{payment_link_id}")

    def list_payment_links(self, limit: int = 10, active: bool = None):
        """Lists all Payment Links.
        Args:
            limit: A limit on the number of objects to be returned.
            active: Only return payment links that are active or inactive.
        """
        params = {"limit": limit}
        if active is not None:
            params["active"] = active
        return self._request("GET", "/payment_links", data=params)

    # --- Connect Account Tools ---
    def create_connect_account(self, type: str, country: str, email: str = None):
        """Creates a new Connect account.
        Args:
            type: The type of business entity. Can be `standard`, `express`, or `custom`.
            country: The country in which the business is located.
            email: The email address of the account holder.
        """
        data = {"type": type, "country": country}
        if email:
            data["email"] = email
        return self._request("POST", "/accounts", data=data)

    def get_connect_account(self, account_id: str):
        """Retrieves a Connect account by ID.
        Args:
            account_id: The ID of the Connect account to retrieve.
        """
        return self._request("GET", f"/accounts/{account_id}")

    def list_connect_accounts(self, limit: int = 10):
        """Lists all Connect accounts.
        Args:
            limit: A limit on the number of objects to be returned.
        """
        params = {"limit": limit}
        return self._request("GET", "/accounts", data=params)

    # --- Transfer Tools ---
    def create_transfer(self, amount: int, currency: str, destination_account_id: str):
        """Creates a new transfer.
        Args:
            amount: A positive integer in cents representing how much to transfer.
            currency: Three-letter ISO currency code.
            destination_account_id: The ID of a connected Stripe account to transfer funds to.
        """
        data = {"amount": amount, "currency": currency, "destination": destination_account_id}
        return self._request("POST", "/transfers", data=data)

    def get_transfer(self, transfer_id: str):
        """Retrieves a transfer by ID.
        Args:
            transfer_id: The ID of the transfer to retrieve.
        """
        return self._request("GET", f"/transfers/{transfer_id}")

    def list_transfers(self, limit: int = 10, destination_account_id: str = None):
        """Lists all transfers.
        Args:
            limit: A limit on the number of objects to be returned.
            destination_account_id: Only return transfers for this destination account.
        """
        params = {"limit": limit}
        if destination_account_id:
            params["destination"] = destination_account_id
        return self._request("GET", "/transfers", data=params)

    # --- Payout Tools ---
    def create_payout(self, amount: int, currency: str, destination_bank_account_or_card_id: str = None):
        """Creates a new payout.
        Args:
            amount: A positive integer in cents representing how much to payout.
            currency: Three-letter ISO currency code.
            destination_bank_account_or_card_id: The ID of a bank account or card to send the payout to.
        """
        data = {"amount": amount, "currency": currency}
        if destination_bank_account_or_card_id:
            data["destination"] = destination_bank_account_or_card_id
        return self._request("POST", "/payouts", data=data)

    def get_payout(self, payout_id: str):
        """Retrieves a payout by ID.
        Args:
            payout_id: The ID of the payout to retrieve.
        """
        return self._request("GET", f"/payouts/{payout_id}")

    def list_payouts(self, limit: int = 10, status: str = None):
        """Lists all payouts.
        Args:
            limit: A limit on the number of objects to be returned.
            status: Only return payouts with this status (e.g., `paid`, `pending`, `failed`).
        """
        params = {"limit": limit}
        if status:
            params["status"] = status
        return self._request("GET", "/payouts", data=params)

    # --- Setup Intent Tools ---
    def create_setup_intent(self, customer_id: str = None, usage: str = "off_session"):
        """Creates a SetupIntent.
        Args:
            customer_id: The ID of the customer this SetupIntent belongs to.
            usage: Indicates how the payment method is intended to be used. Can be `on_session` or `off_session`.
        """
        data = {"usage": usage}
        if customer_id:
            data["customer"] = customer_id
        return self._request("POST", "/setup_intents", data=data)

    def get_setup_intent(self, si_id: str):
        """Retrieves a SetupIntent.
        Args:
            si_id: The ID of the SetupIntent to retrieve.
        """
        return self._request("GET", f"/setup_intents/{si_id}")

    def confirm_setup_intent(self, si_id: str, payment_method: str = None):
        """Confirms a SetupIntent.
        Args:
            si_id: The ID of the SetupIntent to confirm.
            payment_method: ID of the payment method to confirm with.
        """
        data = {}
        if payment_method:
            data["payment_method"] = payment_method
        return self._request("POST", f"/setup_intents/{si_id}/confirm", data=data)

    def cancel_setup_intent(self, si_id: str):
        """Cancels a SetupIntent.
        Args:
            si_id: The ID of the SetupIntent to cancel.
        """
        return self._request("POST", f"/setup_intents/{si_id}/cancel")

    # --- Coupon Tools ---
    def create_coupon(self, percent_off: float = None, amount_off: int = None, currency: str = None, duration: str = "once", duration_in_months: int = None, id: str = None):
        """Creates a new coupon.
        Args:
            percent_off: A positive float representing the percentage of the discount.
            amount_off: A positive integer in cents representing the amount to subtract from the price of an item.
            currency: Three-letter ISO currency code if `amount_off` is specified.
            duration: Specifies how long the discount will be in effect. Can be `forever`, `once`, or `repeating`.
            duration_in_months: If `duration` is `repeating`, the number of months the coupon applies.
            id: Unique string that identifies this coupon.
        """
        data = {"duration": duration}
        if percent_off:
            data["percent_off"] = percent_off
        if amount_off:
            data["amount_off"] = amount_off
            data["currency"] = currency
        if duration == "repeating" and duration_in_months:
            data["duration_in_months"] = duration_in_months
        if id:
            data["id"] = id
        return self._request("POST", "/coupons", data=data)

    def get_coupon(self, coupon_id: str):
        """Retrieves a coupon by ID.
        Args:
            coupon_id: The ID of the coupon to retrieve.
        """
        return self._request("GET", f"/coupons/{coupon_id}")

    def delete_coupon(self, coupon_id: str):
        """Deletes a coupon.
        Args:
            coupon_id: The ID of the coupon to delete.
        """
        return self._request("DELETE", f"/coupons/{coupon_id}")

    def list_coupons(self, limit: int = 10):
        """Lists all coupons.
        Args:
            limit: A limit on the number of objects to be returned.
        """
        params = {"limit": limit}
        return self._request("GET", "/coupons", data=params)

    # --- Promotion Code Tools ---
    def create_promotion_code(self, coupon_id: str, code: str = None, active: bool = True):
        """Creates a new promotion code.
        Args:
            coupon_id: The ID of the coupon to attach to the promotion code.
            code: The customer-facing code that will be entered at checkout.
            active: Whether the promotion code is active.
        """
        data = {"coupon": coupon_id, "active": active}
        if code:
            data["code"] = code
        return self._request("POST", "/promotion_codes", data=data)

    def get_promotion_code(self, promo_code_id: str):
        """Retrieves a promotion code by ID.
        Args:
            promo_code_id: The ID of the promotion code to retrieve.
        """
        return self._request("GET", f"/promotion_codes/{promo_code_id}")

    def list_promotion_codes(self, limit: int = 10, coupon_id: str = None):
        """Lists all promotion codes.
        Args:
            limit: A limit on the number of objects to be returned.
            coupon_id: Only return promotion codes for this coupon.
        """
        params = {"limit": limit}
        if coupon_id:
            params["coupon"] = coupon_id
        return self._request("GET", "/promotion_codes", data=params)


# Initialize the MCP server
mcp_server = FastMCP()
stripe_client = StripeClient()

# Register tools
mcp_server.register_tool(stripe_client.create_customer)
mcp_server.register_tool(stripe_client.get_customer)
mcp_server.register_tool(stripe_client.update_customer)
mcp_server.register_tool(stripe_client.delete_customer)
mcp_server.register_tool(stripe_client.list_customers)

mcp_server.register_tool(stripe_client.create_payment_intent)
mcp_server.register_tool(stripe_client.get_payment_intent)
mcp_server.register_tool(stripe_client.confirm_payment_intent)
mcp_server.register_tool(stripe_client.cancel_payment_intent)
mcp_server.register_tool(stripe_client.list_payment_intents)

mcp_server.register_tool(stripe_client.create_charge)
mcp_server.register_tool(stripe_client.get_charge)
mcp_server.register_tool(stripe_client.refund_charge)
mcp_server.register_tool(stripe_client.list_charges)
mcp_server.register_tool(stripe_client.get_refund)
mcp_server.register_tool(stripe_client.list_refunds)

mcp_server.register_tool(stripe_client.create_product)
mcp_server.register_tool(stripe_client.get_product)
mcp_server.register_tool(stripe_client.update_product)
mcp_server.register_tool(stripe_client.list_products)
mcp_server.register_tool(stripe_client.create_price)
mcp_server.register_tool(stripe_client.get_price)
mcp_server.register_tool(stripe_client.list_prices)

mcp_server.register_tool(stripe_client.create_subscription)
mcp_server.register_tool(stripe_client.get_subscription)
mcp_server.register_tool(stripe_client.update_subscription)
mcp_server.register_tool(stripe_client.cancel_subscription)
mcp_server.register_tool(stripe_client.list_subscriptions)
mcp_server.register_tool(stripe_client.get_invoice)
mcp_server.register_tool(stripe_client.list_invoices)

mcp_server.register_tool(stripe_client.create_checkout_session)
mcp_server.register_tool(stripe_client.get_checkout_session)
mcp_server.register_tool(stripe_client.create_payment_link)
mcp_server.register_tool(stripe_client.get_payment_link)
mcp_server.register_tool(stripe_client.list_payment_links)

mcp_server.register_tool(stripe_client.create_connect_account)
mcp_server.register_tool(stripe_client.get_connect_account)
mcp_server.register_tool(stripe_client.list_connect_accounts)
mcp_server.register_tool(stripe_client.create_transfer)
mcp_server.register_tool(stripe_client.get_transfer)
mcp_server.register_tool(stripe_client.list_transfers)
mcp_server.register_tool(stripe_client.create_payout)
mcp_server.register_tool(stripe_client.get_payout)
mcp_server.register_tool(stripe_client.list_payouts)
mcp_server.register_tool(stripe_client.create_setup_intent)
mcp_server.register_tool(stripe_client.get_setup_intent)
mcp_server.register_tool(stripe_client.confirm_setup_intent)
mcp_server.register_tool(stripe_client.cancel_setup_intent)
mcp_server.register_tool(stripe_client.create_coupon)
mcp_server.register_tool(stripe_client.get_coupon)
mcp_server.register_tool(stripe_client.delete_coupon)
mcp_server.register_tool(stripe_client.list_coupons)
mcp_server.register_tool(stripe_client.create_promotion_code)
mcp_server.register_tool(stripe_client.get_promotion_code)
mcp_server.register_tool(stripe_client.list_promotion_codes)

if __name__ == "__main__":
    mcp_server.run()
