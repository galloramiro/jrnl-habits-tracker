import pytest

from src.client.local_client import LocalClient


@pytest.mark.skip(reason="Use this for debugging purposes")
def test_debug():
    client = LocalClient()
    import ipdb; ipdb.set_trace()