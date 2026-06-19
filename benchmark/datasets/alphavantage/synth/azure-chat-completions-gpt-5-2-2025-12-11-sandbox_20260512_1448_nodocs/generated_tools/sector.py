from typing import Any, Dict, Optional

from .client import AlphaVantageClient


def sector_performance(client: Optional[AlphaVantageClient] = None) -> Dict[str, Any]:
    c = client or AlphaVantageClient()
    return c.request("SECTOR")
