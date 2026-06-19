"""Mastodon reports API tools."""
import os
import requests
from typing import Optional
from mcp.server.fastmcp import FastMCP

BASE_URL = os.environ.get("MASTODON_BASE_URL", "").rstrip("/")
ACCESS_TOKEN = os.environ.get("MASTODON_ACCESS_TOKEN", "")


def _headers():
    return {"Authorization": f"Bearer {ACCESS_TOKEN}"}


def _api(path: str) -> str:
    return f"{BASE_URL}{path}"


def register(mcp: FastMCP):

    @mcp.tool()
    def file_report(
        account_id: str,
        status_ids: Optional[list] = None,
        comment: Optional[str] = None,
        forward: Optional[bool] = None,
        category: Optional[str] = None,
        rule_ids: Optional[list] = None,
    ) -> dict:
        """File a report against an account for moderation review.

        Args:
            account_id: The ID of the account to report.
            status_ids: List of status IDs to attach as evidence.
            comment: Reason for the report (max 1000 characters).
            forward: Forward report to remote admin if account is remote.
            category: Report category: 'spam', 'legal', 'violation', or 'other'.
            rule_ids: List of rule IDs broken (for 'violation' category).
        """
        try:
            data = [("account_id", account_id)]
            if status_ids:
                for sid in status_ids:
                    data.append(("status_ids[]", sid))
            if comment:
                data.append(("comment", comment))
            if forward is not None:
                data.append(("forward", str(forward).lower()))
            if category:
                data.append(("category", category))
            if rule_ids:
                for rid in rule_ids:
                    data.append(("rule_ids[]", rid))
            resp = requests.post(_api("/api/v1/reports"), headers=_headers(), data=data)
            return resp.json()
        except Exception as e:
            return {"error": str(e)}
