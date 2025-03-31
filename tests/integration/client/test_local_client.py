import pytest

from src.client.local_client import LocalClient


@pytest.mark.skip(reason="Use this for debugging purposes")
def test_debug():
    client = LocalClient()
    __import__("ipdb").set_trace()
