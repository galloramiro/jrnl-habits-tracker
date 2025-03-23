import pytest

from src.graphic_tool.console_graphic_tool import ConsoleGraphicTool


def test__generate_days_line():
    # GIVEN
    graphic_tool = ConsoleGraphicTool()
    month = 3
    year = 2025

    # THEN
    days_line = graphic_tool._generate_days_line(month=month, year=year)
    days_line.replace("\x1b[35m", "")
    number_days, letter_days = days_line.split("\n")

    assert number_days[:3] == "01 "
    assert number_days[-3:] == "31 "
    assert letter_days[:3] == "S  "
    assert letter_days[-3:] == "L  "
