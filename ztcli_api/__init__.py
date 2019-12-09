"""A Python client wrapper for the zerotier-cli node API."""
import asyncio
import logging

import aiohttp
import async_timeout

from ztcli_api import exceptions

logger = logging.getLogger(__name__)

WRITABLE_NETWORK = [
    'allowManaged',
    'allowGlobal',
    'allowDefault',
]

WRITABLE_MEMBER = []


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
        """Retrieve node data using JSON API ``endpoint``."""
        try:
            with async_timeout.timeout(5, loop=self._loop):
                response = await self._session.get(
                    'http://{}/{}'.format(self.url, endpoint),
                    headers=self.headers)

            logger.debug("Response status: %s", response.status)
            self.data = await response.json()
            logger.debug(self.data)
        except (asyncio.TimeoutError, aiohttp.ClientError):
            logger.error("Can not load data from ZeroTier node")
            raise exceptions.ZeroTierConnectionError()

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
            logger.error("Can not update entry of ZeroTier node")
            raise exceptions.ZeroTierConnectionError()
