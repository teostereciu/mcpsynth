from generated_tools.utils import make_request

def register(mcp):
    @mcp.tool()
    def get_price_rules():
        """Retrieve a list of price rules."""
        return make_request("GET", "/price_rules.json")

    @mcp.tool()
    def get_price_rule(price_rule_id: int):
        """Retrieve a single price rule by ID."""
        return make_request("GET", f"/price_rules/{price_rule_id}.json")

    @mcp.tool()
    def create_price_rule(price_rule: dict):
        """Create a new price rule."""
        return make_request("POST", "/price_rules.json", json_data={"price_rule": price_rule})

    @mcp.tool()
    def update_price_rule(price_rule_id: int, price_rule: dict):
        """Update an existing price rule."""
        return make_request("PUT", f"/price_rules/{price_rule_id}.json", json_data={"price_rule": price_rule})

    @mcp.tool()
    def delete_price_rule(price_rule_id: int):
        """Delete a price rule."""
        return make_request("DELETE", f"/price_rules/{price_rule_id}.json")

    @mcp.tool()
    def get_discount_codes(price_rule_id: int):
        """Retrieve a list of discount codes for a price rule."""
        return make_request("GET", f"/price_rules/{price_rule_id}/discount_codes.json")

    @mcp.tool()
    def create_discount_code(price_rule_id: int, discount_code: dict):
        """Create a discount code for a price rule."""
        return make_request("POST", f"/price_rules/{price_rule_id}/discount_codes.json", json_data={"discount_code": discount_code})

    @mcp.tool()
    def update_discount_code(price_rule_id: int, discount_code_id: int, discount_code: dict):
        """Update an existing discount code."""
        return make_request("PUT", f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json", json_data={"discount_code": discount_code})

    @mcp.tool()
    def delete_discount_code(price_rule_id: int, discount_code_id: int):
        """Delete a discount code."""
        return make_request("DELETE", f"/price_rules/{price_rule_id}/discount_codes/{discount_code_id}.json")
