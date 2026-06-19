import os
import time
import base64
import threading
from dataclasses import dataclass
from typing import Dict, Optional, Tuple

import requests


EBAY_OAUTH_BASE = {
    "SANDBOX": "https://api.sandbox.ebay.com",
    "PRODUCTION": "https://api.ebay.com",
}


def _env(name: str, default: Optional[str] = None) -> str:
    v = os.getenv(name, default)
    if v is None or v == "":
        raise RuntimeError(f"Missing required environment variable: {name}")
    return v


def get_environment() -> str:
    env = os.getenv("EBAY_ENVIRONMENT", "SANDBOX").upper()
    if env not in ("SANDBOX", "PRODUCTION"):
        env = "SANDBOX"
    return env


def get_base_url(media: bool = False) -> str:
    env = get_environment()
    if media:
        return "https://apim.sandbox.ebay.com" if env == "SANDBOX" else "https://apim.ebay.com"
    return EBAY_OAUTH_BASE[env]


@dataclass
class Token:
    access_token: str
    expires_at: float
    token_type: str = "Bearer"

    def is_expired(self, skew_s: int = 60) -> bool:
        return time.time() >= (self.expires_at - skew_s)


class EbayTokenManager:
    def __init__(self):
        self._lock = threading.Lock()
        self._app_token: Optional[Token] = None
        self._user_token: Optional[Token] = None

    def _basic_auth_header(self) -> str:
        client_id = _env("EBAY_APP_ID")
        client_secret = _env("EBAY_CERT_ID")
        b64 = base64.b64encode(f"{client_id}:{client_secret}".encode("utf-8")).decode("ascii")
        return f"Basic {b64}"

    def _token_endpoint(self) -> str:
        return f"{get_base_url(media=False)}/identity/v1/oauth2/token"

    def get_app_token(self, scope: Optional[str] = None) -> Token:
        with self._lock:
            if self._app_token and not self._app_token.is_expired():
                return self._app_token

            data = {
                "grant_type": "client_credentials",
            }
            if scope:
                data["scope"] = scope

            headers = {
                "Authorization": self._basic_auth_header(),
                "Content-Type": "application/x-www-form-urlencoded",
            }
            r = requests.post(self._token_endpoint(), data=data, headers=headers, timeout=30)
            if r.status_code >= 400:
                raise RuntimeError(f"OAuth app token error {r.status_code}: {r.text}")
            j = r.json()
            tok = Token(
                access_token=j["access_token"],
                token_type=j.get("token_type", "Bearer"),
                expires_at=time.time() + float(j.get("expires_in", 7200)),
            )
            self._app_token = tok
            return tok

    def get_user_token(self, scope: Optional[str] = None) -> Token:
        with self._lock:
            if self._user_token and not self._user_token.is_expired():
                return self._user_token

            refresh_token = _env("EBAY_REFRESH_TOKEN")
            data = {
                "grant_type": "refresh_token",
                "refresh_token": refresh_token,
            }
            if scope:
                data["scope"] = scope

            headers = {
                "Authorization": self._basic_auth_header(),
                "Content-Type": "application/x-www-form-urlencoded",
            }
            r = requests.post(self._token_endpoint(), data=data, headers=headers, timeout=30)
            if r.status_code >= 400:
                raise RuntimeError(f"OAuth user token error {r.status_code}: {r.text}")
            j = r.json()
            tok = Token(
                access_token=j["access_token"],
                token_type=j.get("token_type", "Bearer"),
                expires_at=time.time() + float(j.get("expires_in", 7200)),
            )
            self._user_token = tok
            return tok


TOKEN_MANAGER = EbayTokenManager()


def auth_headers(user: bool = False, scope: Optional[str] = None) -> Dict[str, str]:
    tok = TOKEN_MANAGER.get_user_token(scope=scope) if user else TOKEN_MANAGER.get_app_token(scope=scope)
    return {
        "Authorization": f"{tok.token_type} {tok.access_token}",
        "Accept": "application/json",
    }


def request_json(
    method: str,
    path: str,
    *,
    params: Optional[Dict] = None,
    json: Optional[Dict] = None,
    headers: Optional[Dict[str, str]] = None,
    user: bool = False,
    scope: Optional[str] = None,
    media: bool = False,
) -> Tuple[int, Dict]:
    base = get_base_url(media=media)
    url = base + path
    h = {}
    h.update(auth_headers(user=user, scope=scope))
    if headers:
        h.update({k: v for k, v in headers.items() if v is not None})
    try:
        r = requests.request(method, url, params=params, json=json, headers=h, timeout=60)
    except requests.RequestException as e:
        return 0, {"error": str(e), "url": url}

    if r.status_code == 204:
        return r.status_code, {"ok": True}

    ct = r.headers.get("content-type", "")
    if "application/json" in ct:
        body = r.json()
    else:
        body = {"raw": r.text}

    if r.status_code >= 400:
        return r.status_code, {"error": body, "status": r.status_code, "url": url}
    return r.status_code, body
