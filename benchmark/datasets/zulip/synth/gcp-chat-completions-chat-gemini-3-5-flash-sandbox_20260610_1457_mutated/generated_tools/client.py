import os
import requests
from typing import Any, Dict, Optional

class ZulipClient:
    def __init__(self):
        self.email = os.environ.get("ZULIP_EMAIL")
        self.api_key = os.environ.get("ZULIP_API_KEY")
        self.site = os.environ.get("ZULIP_SITE")
        
        if self.site:
            self.site = self.site.rstrip("/")
            self.base_url = f"{self.site}/api/v1"
        else:
            self.base_url = None

    def is_configured(self) -> bool:
        return bool(self.email and self.api_key and self.site)

    def request(
        self,
        method: str,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
        files: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        if not self.is_configured():
            return {
                "error": "Zulip client is not fully configured. Please set ZULIP_EMAIL, ZULIP_API_KEY, and ZULIP_SITE environment variables."
            }
        
        url = f"{self.base_url}/{path.lstrip('/')}"
        auth = (self.email, self.api_key)
        
        try:
            response = requests.request(
                method=method,
                url=url,
                auth=auth,
                params=params,
                data=data,
                files=files,
                timeout=30,
            )
            
            try:
                result = response.json()
            except ValueError:
                return {
                    "error": f"Invalid JSON response from server (HTTP {response.status_code})",
                    "raw_response": response.text[:1000]
                }
                
            if not response.ok:
                msg = result.get("msg", response.reason)
                return {
                    "error": f"HTTP {response.status_code}: {msg}",
                    "details": result
                }
                
            return result
        except Exception as e:
            return {"error": f"Request failed: {str(e)}"}

client = ZulipClient()
