# coding: utf-8

"""Exceptions for node API client."""


class ZeroTierError(Exception):
    """General ZeroTierError exception occurred."""


class ZeroTierConnectionError(ZeroTierError):
    """When a connection error is encountered."""


class ZeroTierNoDataAvailable(ZeroTierError):
    """When no data is available."""
