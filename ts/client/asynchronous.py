"""
This module defines the AsyncClient class to make asynchronous HTTP requests using the httpx library.

Classes:
    - AsyncClient: Manages asynchronous HTTP requests.
"""
from typing import Any, Mapping, Optional, AsyncContextManager

import httpx

from .base import BaseClient


class AsyncClient(BaseClient):
    """
    AsyncClient Class for making asynchronous HTTP requests.

    This class inherits from the BaseClient class and implements its abstract methods
    for making HTTP DELETE, GET, POST, and PUT requests.
    """
    #Need this for streaming, for async ands sync, bc otherwise the client is closed by the time it gets returned
    def __post_init__(self):
        super().__post_init__()
        self.client = httpx.AsyncClient()

    async def _delete_request(
        self, url: str, params: Optional[dict] = None, headers: Optional[dict] = None
    ) -> httpx.Response:
        if headers is None:
            headers = {}

        async with httpx.AsyncClient() as client:
            response = await client.delete(url, headers=headers, params=params)

        return response

    async def _get_request(
        self, url: str, params: Optional[dict] = None, headers: Optional[dict] = None, timeout: int = 60
    ) -> httpx.Response:
        if headers is None:
            headers = {}

        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers, params=params, timeout=timeout)

        return response

    async def _post_request(
        self,
        url: str,
        params: Optional[dict] = None,
        headers: Optional[dict] = None,
        data: Optional[Mapping[str, Any]] = None,
    ) -> httpx.Response:
        if headers is None:
            headers = {}

        async with httpx.AsyncClient() as client:
            response = await client.post(url, headers=headers, params=params, data=data)

        return response

    async def _put_request(
        self,
        url: str,
        params: Optional[dict] = None,
        headers: Optional[dict] = None,
        data: Optional[Mapping[str, Any]] = None,
    ) -> httpx.Response:
        if headers is None:
            headers = {}

        async with httpx.AsyncClient() as client:
            response = await client.put(url, headers=headers, params=params, data=data)

        return response

    def _stream_request(self, url: str, params: Optional[dict] = None,
                        headers: Optional[dict] = None, timeout: int = 60) -> AsyncContextManager[httpx.Response]:
        """Submit a stream request to TradeStation."""
        if headers is None:
            headers = {}
        return self.client.stream('GET', url, headers=headers, params=params, timeout=timeout)