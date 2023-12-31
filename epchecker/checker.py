# epchecker/checker.py

import asyncio
from http.client import HTTPConnection
from urllib.parse import urlparse

import aiohttp


def endpoint_is_online(url: str, timeout: int = 3) -> bool:
    """Return True if the target URL is online.
    Raise an exception otherwise."""

    error = Exception("unknown error")
    parser = urlparse(url)
    host = parser.netloc or parser.path.split("/")[0]
    for port in (80, 443):
        connection = HTTPConnection(host=host, port=port, timeout=timeout)
        try:
            connection.request("HEAD", "/")
            return True
        except Exception as err:
            error = err
        finally:
            connection.close()
    raise error


async def endpoint_is_online_async(url: str, timeout: int = 3) -> bool:
    """Return True if the target URL is online.
    Raise an exception otherwise."""

    error = Exception("unknown error")
    parser = urlparse(url)
    host = parser.netloc or parser.path.split("/")[0]
    for scheme in ("http", "https"):
        target_url = f"{scheme}://{host}"
        async with aiohttp.ClientSession() as session:
            try:
                await session.head(target_url, timeout=timeout)
                return True
            except asyncio.exceptions.TimeoutError:
                error = Exception("timed out")
            except Exception as err:
                error = err
    raise error
