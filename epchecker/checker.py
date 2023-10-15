# epchecker/checker.py

from http.client import HTTPConnection
from urllib.parse import urlparse


def site_is_online(url: str, timeout: int = 3):
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
