"""Get data from local ZT node API."""
import json
import platform

import asyncio
import aiohttp

from ztcli_api import ZeroTier
from ztcli_api import exceptions


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


def pprint(obj):
    print(json.dumps(obj, indent=2, separators=(',', ': ')))


async def main():
    """Example code to retrieve data from a ZeroTier node."""
    async with aiohttp.ClientSession() as session:
        ZT_API = get_token()
        client = ZeroTier(ZT_API, loop, session)

        try:
            # get status details of the local node
            await client.get_data('status')
            print('Node status:')
            pprint(client.data)
            # print(client.data.get('online'))

            # get status details of the node peers
            await client.get_data('peer')
            print('Peers found:')
            pprint(client.data)

            # get/display all available network data
            await client.get_data('network')
            print('Networks found:')
            pprint(client.data)
            # for network in client.data:
                # my_id = network.get('id')
                # print(my_id)
                # # Get details about each network
                # await client.get_data('network/{}'.format(my_id))
                # pprint(client.data)

                # Set a toggle for an existing network
                # await client.set_value(
                    # 'allowGlobal', 'True', 'network/{}'.format(my_id))
                # await client.get_data('network/{}'.format(my_id))
                # print(network.get('allowGlobal'))
        except exceptions.ZeroTierConnectionError:
            pass

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
