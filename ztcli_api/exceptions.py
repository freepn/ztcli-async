"""Exceptions for node API client."""


class ZeroTierError(Exception):
    """General ZeroTierError exception occurred."""

    pass


class ZeroTierConnectionError(ZeroTierError):
    """When a connection error is encountered."""

    pass


class ZeroTierNoDataAvailable(ZeroTierError):
    """When no data is available."""

    pass
