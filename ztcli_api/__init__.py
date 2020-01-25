# coding: utf-8
"""A Python async client wrapper for the zerotier-cli node API."""
import logging
import asyncio

import aiohttp
import async_timeout

from .exceptions import ZeroTierConnectionError as ZeroTierConnectionError


__all__ = [
    'WRITABLE_NETWORK',
    'WRITABLE_NODE',
    'ZeroTier',
    'ZeroTierConnectionError',
]


logger = logging.getLogger(__name__)


WRITABLE_NETWORK = [
    'name',
    'private',
    'enableBroadcast',
    'v4AssignMode',
    'v6AssignMode',
    'mtu',
    'multicastLimit'
    'routes',
    'ipAssignmentPools',
    'rules',
    'capabilities',
    'tags',
    'remoteTraceTarget',
    'remoteTraceLevel',
]

WRITABLE_NODE = [
    'allowManaged',
    'allowGlobal',
    'allowDefault',
]


class ZeroTier(object):
    """A class for handling the data retrieval."""

    def __init__(self, api_token, loop, session, host='localhost', port=9993):
        """Initialize the connection."""
        self._loop = loop
        self._session = session
        self.headers = {'X-ZT1-Auth': api_token}
        self.data = None
        self.url = '{}:{}'.format(host, port)

    async def get_data(self, endpoint):
        """Send a GET request to  JSON API ``endpoint``."""
        try:
            with async_timeout.timeout(5, loop=self._loop):
                response = await self._session.get(
                    'http://{}/{}'.format(self.url, endpoint),
                    headers=self.headers)

            logger.debug("Response status: %s", response.status)
            self.data = await response.json()
            logger.debug(self.data)
        except (asyncio.TimeoutError, aiohttp.ClientError):
            logger.debug("Cannot load data from ZeroTier node")
            raise ZeroTierConnectionError('Cannot connect to ZeroTier API')

    async def set_value(self, key, variable, endpoint):
        """Send a POST request to JSON API ``endpoint``."""
        payload = {key: variable}
        print(payload)
        try:
            with async_timeout.timeout(5, loop=self._loop):
                response = await self._session.post(
                    'http://{}/{}'.format(self.url, endpoint),
                    headers=self.headers, data=payload)

            logger.debug("Response status: %s", response.status)
        except (asyncio.TimeoutError, aiohttp.ClientError):
            logger.debug("Cannot update entry of ZeroTier node")
            raise ZeroTierConnectionError('Cannot connect to ZeroTier API')
