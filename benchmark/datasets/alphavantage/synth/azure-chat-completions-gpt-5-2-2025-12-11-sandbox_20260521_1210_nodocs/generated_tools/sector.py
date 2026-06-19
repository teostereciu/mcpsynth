from typing import Any, Dict

from .client import av_get


def sector_performance() -> Dict[str, Any]:
    return av_get({"function": "SECTOR"})
