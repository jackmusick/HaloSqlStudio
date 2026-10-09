"""modules.halopsa_split._common — DotDict, SDKError, base client (helpers only)."""

from __future__ import annotations

import time

from dataclasses import dataclass

from typing import Any, Dict, List, Optional

import requests

class DotDict(dict):
    """Dict subclass that allows dot notation access to keys."""

    def __getattr__(self, key):
        try:
            value = self[key]
            if isinstance(value, dict) and (not isinstance(value, DotDict)):
                return DotDict(value)
            elif isinstance(value, list):
                return [DotDict(item) if isinstance(item, dict) else item for item in value]
            return value
        except KeyError:
            raise AttributeError(f'No attribute {key}')

    def __setattr__(self, key, value):
        self[key] = value

    def __delattr__(self, key):
        try:
            del self[key]
        except KeyError:
            raise AttributeError(f'No attribute {key}')

class SDKError(Exception):
    """SDK operation failed with details about the HTTP response."""

    def __init__(self, message: str, status_code: int=None, response_body: str=None):
        self.status_code = status_code
        self.response_body = response_body
        super().__init__(message)

    def __str__(self):
        return self.args[0] if self.args else 'SDK Error'

class _HaloAPIClient:
    """Internal client implementation for HaloAPI."""
    RETRYABLE_STATUS_CODES = {429, 500, 502, 503, 504}

    def __init__(self, base_url: str, session: requests.Session, timeout: float=30.0, max_retries: int=3, base_backoff: float=1.0, max_backoff: float=60.0):
        self.base_url = base_url.rstrip('/')
        self.session = session
        self.timeout = timeout
        self.max_retries = max_retries
        self.base_backoff = base_backoff
        self.max_backoff = max_backoff

    def _request_with_retry(self, method: str, url: str, **kwargs) -> requests.Response:
        """Execute HTTP request with exponential backoff retry for transient failures."""
        kwargs.setdefault('timeout', self.timeout)
        last_response = None
        for attempt in range(self.max_retries + 1):
            response = self.session.request(method, url, **kwargs)
            last_response = response
            if response.status_code not in self.RETRYABLE_STATUS_CODES:
                return response
            if attempt >= self.max_retries:
                break
            if response.status_code == 429:
                retry_after = response.headers.get('Retry-After')
                if retry_after:
                    try:
                        wait = float(retry_after)
                    except ValueError:
                        wait = self.base_backoff * 2 ** attempt
                else:
                    wait = self.base_backoff * 2 ** attempt
            else:
                wait = self.base_backoff * 2 ** attempt
            wait = min(wait, self.max_backoff)
            time.sleep(wait)
        return last_response

    def _auto_convert(self, data):
        """Automatically convert dicts to DotDict for dot notation access."""
        if data is None:
            return None
        if isinstance(data, list):
            return [self._auto_convert(item) for item in data]
        if isinstance(data, dict):
            return DotDict(data)
        return data
