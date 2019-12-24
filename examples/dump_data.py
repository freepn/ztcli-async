# coding: utf-8

"""Get data from local ZT node API."""
import json
import platform

import asyncio
import aiohttp

from ztcli_api import ZeroTier
from ztcli_api import ZeroTierConnectionError as ZeroTierConnectionError


verbose = True


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


def dump_json(endpoint, data):
    with open(endpoint + '.json', 'w') as fp:
        json.dump(data, fp)
    print('{} data in {}.json'.format(endpoint, endpoint))


def load_json(endpoint):
    with open(endpoint + '.json', 'r') as fp:
        data = json.load(fp)
    print('{} data read from {}.json'.format(endpoint, endpoint))
    return data


async def main():
    """Example code to retrieve data from a ZeroTier node."""
    async with aiohttp.ClientSession() as session:
        ZT_API = get_token()
        client = ZeroTier(ZT_API, loop, session)

        try:
            # get status details of the local node
            await client.get_data('status')
            dump_json('status', client.data)
            status_data = load_json('status')
            if verbose:
                pprint(status_data)

            # get status details of the node peers
            await client.get_data('peer')
            dump_json('peer', client.data)
            peer_data = load_json('peer')
            if verbose:
                pprint(peer_data)

            # get/display all available network data
            await client.get_data('network')
            dump_json('network', client.data)
            net_data = load_json('network')
            if verbose:
                pprint(net_data)

        except ZeroTierConnectionError as exc:
            print(str(exc))
            pass

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
