"""Get data from a given node."""
import platform

import asyncio
import aiohttp

from ztcli_api import ZeroTier


def get_filepath():
    """Get filepath according to OS"""
    if platform.system() == "Linux":
        return "/var/lib/zerotier-one"
    elif platform.system() == "Darwin":
        return "/Library/Application Support/ZeroTier/One"
    elif platform.system() == "FreeBSD" or platform.system() == "OpenBSD":
        return "/var/db/zerotier-one"
    elif platform.system() == "Windows":
        return "C:\ProgramData\ZeroTier\One"


def get_token():
    """Get authentication token (requires root or user acl)"""
    with open(get_filepath()+"/authtoken.secret") as file:
        auth_token = file.read()
    return auth_token


ZT_HOST = 'localhost'
ZT_API = get_token()


async def main():
    """Example code to retrieve data from a ZeroTier node."""
    async with aiohttp.ClientSession() as session:
        client = ZeroTier(ZT_API, loop, session)

        # Print details of the controller
        await client.get_data('status')
        print(client.data)
        print(client.data.get('online'))

        # Display all available nets
        await client.get_data('network')
        for network in client.data:
            print(network.get('id'))

        # Get details about a network
        await client.get_data('network/{}'.format('b6079f73c63cea29'))
        print(client.data)

        # Set a toggle for an existing network
        await client.set_value(
            'allowGlobal', 'True', 'network/{}'.format('b6079f73c63cea29'))
        await client.get_data('network/{}'.format('b6079f73c63cea29'))
        print(network.get('allowGlobal'))

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
