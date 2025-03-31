import pytest

from src.graphic_tool.console_graphic_tool import ConsoleGraphicTool


@pytest.mark.skip(reason="Use this for debugging purposes")
def test_debug():
    graphic_tool = ConsoleGraphicTool()
    __import__("ipdb").set_trace()
