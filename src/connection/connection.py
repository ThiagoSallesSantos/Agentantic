import requests

from enum import Enum

class ConnectionType(Enum):
    POST = requests.post
    GET = requests.get

def connection(connection_type: ConnectionType, url: str, **kwargs) -> requests.Response:
    response: requests.Response = connection_type(
        url=url,
        json=kwargs
    )

    return response
