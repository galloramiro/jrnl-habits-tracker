import pytest

from src.service.service import JrnlHabitTrackerService


@pytest.mark.skip(reason="Use this for debugging purposes")
def test_debug():
    service = JrnlHabitTrackerService.build_local_console_service()
    __import__("ipdb").set_trace()
