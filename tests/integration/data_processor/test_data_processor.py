import pytest

from src.data_processor.data_processor import DataProcessor


@pytest.mark.skip(reason="Use this for debugging purposes")
def test_debug():
    data_processor = DataProcessor()
    __import__("ipdb").set_trace()
