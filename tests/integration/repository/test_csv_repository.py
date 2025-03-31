import pytest

from src.repository.csv_repository import CsvRepository


@pytest.mark.skip(reason="Use this for debugging purposes")
def test_debug():
    repository = CsvRepository()
    __import__("ipdb").set_trace()
