from typing import Any, Dict

from .client import call_alpha_vantage


def sector_performance() -> Dict[str, Any]:
    return call_alpha_vantage({"function": "SECTOR"})
