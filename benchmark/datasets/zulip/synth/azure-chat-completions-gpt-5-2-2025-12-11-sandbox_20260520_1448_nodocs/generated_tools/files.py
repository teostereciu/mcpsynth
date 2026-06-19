from __future__ import annotations

from pathlib import Path

from zulip_client import ZulipClient


def upload_file(client: ZulipClient, *, file_path: str) -> dict:
    p = Path(file_path)
    if not p.exists() or not p.is_file():
        return {"error": f"File not found: {file_path}"}
    with p.open("rb") as f:
        files = {"file": (p.name, f)}
        return client.request("POST", "/user_uploads", files=files)
