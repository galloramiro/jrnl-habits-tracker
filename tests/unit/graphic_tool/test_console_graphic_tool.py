import pytest
from pandas.tests.dtypes.test_inference import expected

from src.config import JRNL_DIR
from src.graphic_tool.console_graphic_tool import ConsoleGraphicTool


def test__generate_days_line():
    # GIVEN
    graphic_tool = ConsoleGraphicTool()
    month = 3
    year = 2025

    # THEN
    days_line = graphic_tool._generate_days_line(month=month, year=year)
    days_line = days_line.replace("\x1b[35m", "")
    number_days, letter_days = days_line.split("\n")

    assert number_days[:3] == "01 "
    assert number_days[-3:] == "31 "
    assert letter_days[:3] == " S "
    assert letter_days[-3:] == " L "


def test__from_csv_to_list_of_dict():
    # GIVEN
    graphic_tool = ConsoleGraphicTool()
    file_path = f"{JRNL_DIR}/2025/04/monthly_habits_data.csv"

    # THEN
    data = graphic_tool._from_csv_to_list_of_dict(file_path=file_path)
    positive_habits = list(filter(lambda row: row["tag"] == "PositiveHabits", data))
    negative_habits = list(filter(lambda row: row["tag"] == "NegativeHabits", data))

    assert len(data) == 630
    assert len(positive_habits) == 210
    assert len(negative_habits) == 120


def test__generate_month_range():
    # GIVEN
    graphic_tool = ConsoleGraphicTool()
    month = 3
    year = 2025

    # THEN
    month_range = graphic_tool._generate_month_range(month=month, year=year)
    assert month_range[0] == 1
    assert month_range[-1] == 31

    # GIVEN
    month = 2

    # THEN
    month_range = graphic_tool._generate_month_range(month=month, year=year)

    assert month_range[0] == 1
    assert month_range[-1] == 28


def test__get_unique_descriptions():
    # GIVEN
    graphic_tool = ConsoleGraphicTool()
    file_path = f"{JRNL_DIR}/2025/04/monthly_habits_data.csv"
    data = graphic_tool._from_csv_to_list_of_dict(file_path=file_path)
    data = graphic_tool._filter_by_tag(data=data, tag="PositiveHabits")

    # THEN
    descriptions = graphic_tool._get_unique_descriptions(data=data)

    assert len(descriptions) == 7
    assert descriptions[0] == "positive_habit_07"
    assert descriptions[-1] == "positive_habit_01"


def test__filter_by_tag():
    # GIVEN
    graphic_tool = ConsoleGraphicTool()
    file_path = f"{JRNL_DIR}/2025/04/monthly_habits_data.csv"
    data = graphic_tool._from_csv_to_list_of_dict(file_path=file_path)

    # THEN
    positive_habits = graphic_tool._filter_by_tag(data=data, tag="PositiveHabits")
    negative_habits = graphic_tool._filter_by_tag(data=data, tag="NegativeHabits")

    assert len(positive_habits) == 210
    assert len(negative_habits) == 120


def test__generate_lines_for_description():
    # GIVEN
    graphic_tool = ConsoleGraphicTool()
    file_path = f"{JRNL_DIR}/2025/04/monthly_habits_data.csv"
    data = graphic_tool._from_csv_to_list_of_dict(file_path=file_path)
    data = graphic_tool._filter_by_tag(data=data, tag="PositiveHabits")
    descriptions = graphic_tool._get_unique_descriptions(data=data)
    days_in_months = graphic_tool._generate_month_range(month=4, year=2025)

    # THEN
    description_line = graphic_tool._generate_lines_for_description(
        data=data, descriptions=descriptions, days_in_month=days_in_months
    )
    expected_description_line = "\x1b[37m \uf444  \uf444  \uf444  \uf444  \uf444  \ue621  \uf444  \uf444  \uf444  \ue621  \uf444  \uf444  \ue621  \uf444  \ue621  \uf444  \ue621  \uf444  \uf444  \uf444  \uf444  \ue621  \uf444  \ue621  \uf444  \uf444  \uf444  \uf444  \uf444  \ue621  \x1b[35mpositive_habit_07\n\x1b[37m \uf444  \uf444  \uf444  \uf444  \uf444  \ue621  \uf444  \ue621  \ue621  \uf444  \uf444  \uf444  \ue621  \uf444  \uf444  \uf444  \ue621  \ue621  \ue621  \uf444  \uf444  \uf444  \ue621  \uf444  \uf444  \ue621  \uf444  \uf444  \uf444  \uf444  \x1b[35mpositive_habit_06\n\x1b[37m \uf444  \ue621  \ue621  \uf444  \uf444  \uf444  \ue621  \ue621  \uf444  \uf444  \uf444  \uf444  \uf444  \uf444  \uf444  \uf444  \uf444  \uf444  \uf444  \ue621  \uf444  \uf444  \uf444  \uf444  \uf444  \uf444  \uf444  \uf444  \uf444  \uf444  \x1b[35mpositive_habit_05\n\x1b[37m \uf444  \uf444  \uf444  \uf444  \uf444  \uf444  \uf444  \uf444  \uf444  \ue621  \uf444  \uf444  \uf444  \uf444  \uf444  \uf444  \ue621  \ue621  \uf444  \uf444  \uf444  \ue621  \uf444  \ue621  \uf444  \uf444  \uf444  \uf444  \ue621  \ue621  \x1b[35mpositive_habit_04\n\x1b[37m \uf444  \uf444  \uf444  \uf444  \uf444  \uf444  \uf444  \uf444  \ue621  \uf444  \uf444  \uf444  \uf444  \uf444  \ue621  \uf444  \uf444  \ue621  \uf444  \uf444  \uf444  \uf444  \uf444  \uf444  \uf444  \ue621  \ue621  \ue621  \ue621  \ue621  \x1b[35mpositive_habit_03\n\x1b[37m \uf444  \uf444  \ue621  \uf444  \uf444  \uf444  \uf444  \uf444  \ue621  \uf444  \uf444  \uf444  \uf444  \uf444  \ue621  \uf444  \uf444  \uf444  \uf444  \ue621  \uf444  \uf444  \uf444  \ue621  \uf444  \uf444  \ue621  \uf444  \uf444  \uf444  \x1b[35mpositive_habit_02\n\x1b[37m \uf444  \uf444  \ue621  \ue621  \uf444  \uf444  \uf444  \uf444  \uf444  \uf444  \uf444  \uf444  \ue621  \uf444  \uf444  \uf444  \uf444  \uf444  \uf444  \uf444  \uf444  \uf444  \uf444  \uf444  \uf444  \uf444  \uf444  \ue621  \uf444  \uf444  \x1b[35mpositive_habit_01\n"

    assert description_line == expected_description_line


def test_generate_positive_habits_graph():
    # GIVEN
    graphic_tool = ConsoleGraphicTool()
    file_path = f"{JRNL_DIR}/2025/04/monthly_habits_data.csv"

    # THEN
    positive_habits_graph = graphic_tool.generate_positive_habits_graph(file_path=file_path)
    expected_positive_habits_graph = "\x1b[37m \uf444  \uf444  \uf444  \uf444  \uf444  \ue621  \uf444  \uf444  \uf444  \ue621  \uf444  \uf444  \ue621  \uf444  \ue621  \uf444  \ue621  \uf444  \uf444  \uf444  \uf444  \ue621  \uf444  \ue621  \uf444  \uf444  \uf444  \uf444  \uf444  \ue621  \x1b[35mpositive_habit_07\n\x1b[37m \uf444  \uf444  \uf444  \uf444  \uf444  \ue621  \uf444  \ue621  \ue621  \uf444  \uf444  \uf444  \ue621  \uf444  \uf444  \uf444  \ue621  \ue621  \ue621  \uf444  \uf444  \uf444  \ue621  \uf444  \uf444  \ue621  \uf444  \uf444  \uf444  \uf444  \x1b[35mpositive_habit_06\n\x1b[37m \uf444  \ue621  \ue621  \uf444  \uf444  \uf444  \ue621  \ue621  \uf444  \uf444  \uf444  \uf444  \uf444  \uf444  \uf444  \uf444  \uf444  \uf444  \uf444  \ue621  \uf444  \uf444  \uf444  \uf444  \uf444  \uf444  \uf444  \uf444  \uf444  \uf444  \x1b[35mpositive_habit_05\n\x1b[37m \uf444  \uf444  \uf444  \uf444  \uf444  \uf444  \uf444  \uf444  \uf444  \ue621  \uf444  \uf444  \uf444  \uf444  \uf444  \uf444  \ue621  \ue621  \uf444  \uf444  \uf444  \ue621  \uf444  \ue621  \uf444  \uf444  \uf444  \uf444  \ue621  \ue621  \x1b[35mpositive_habit_04\n\x1b[37m \uf444  \uf444  \uf444  \uf444  \uf444  \uf444  \uf444  \uf444  \ue621  \uf444  \uf444  \uf444  \uf444  \uf444  \ue621  \uf444  \uf444  \ue621  \uf444  \uf444  \uf444  \uf444  \uf444  \uf444  \uf444  \ue621  \ue621  \ue621  \ue621  \ue621  \x1b[35mpositive_habit_03\n\x1b[37m \uf444  \uf444  \ue621  \uf444  \uf444  \uf444  \uf444  \uf444  \ue621  \uf444  \uf444  \uf444  \uf444  \uf444  \ue621  \uf444  \uf444  \uf444  \uf444  \ue621  \uf444  \uf444  \uf444  \ue621  \uf444  \uf444  \ue621  \uf444  \uf444  \uf444  \x1b[35mpositive_habit_02\n\x1b[37m \uf444  \uf444  \ue621  \ue621  \uf444  \uf444  \uf444  \uf444  \uf444  \uf444  \uf444  \uf444  \ue621  \uf444  \uf444  \uf444  \uf444  \uf444  \uf444  \uf444  \uf444  \uf444  \uf444  \uf444  \uf444  \uf444  \uf444  \ue621  \uf444  \uf444  \x1b[35mpositive_habit_01\n\x1b[35m01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 \n\x1b[35m M  M  J  V  S  D  L  M  M  J  V  S  D  L  M  M  J  V  S  D  L  M  M  J  V  S  D  L  M  M "

    assert positive_habits_graph == expected_positive_habits_graph


def test_generate_negative_habits_graph():
    # GIVEN
    graphic_tool = ConsoleGraphicTool()
    file_path = f"{JRNL_DIR}/2025/04/monthly_habits_data.csv"

    # THEN
    negative_habits_graph = graphic_tool.generate_negative_habits_graph(file_path=file_path)
    expected_negative_habits_graph = "\x1b[37m \ue621  \ue621  \ue621  \ue621  \ue621  \ue621  \ue621  \ue621  \ue621  \ue621  \ue621  \ue621  \ue621  \ue621  \ue621  \ue621  \ue621  \uf444  \ue621  \ue621  \ue621  \ue621  \ue621  \ue621  \ue621  \ue621  \ue621  \ue621  \ue621  \ue621  \x1b[35mnegative_habit_04\n\x1b[37m \uf444  \ue621  \ue621  \ue621  \ue621  \ue621  \ue621  \ue621  \ue621  \ue621  \ue621  \ue621  \ue621  \uf444  \ue621  \ue621  \ue621  \ue621  \ue621  \ue621  \ue621  \ue621  \ue621  \ue621  \ue621  \ue621  \ue621  \ue621  \ue621  \ue621  \x1b[35mnegative_habit_03\n\x1b[37m \ue621  \ue621  \ue621  \ue621  \ue621  \ue621  \ue621  \ue621  \ue621  \ue621  \ue621  \ue621  \ue621  \ue621  \ue621  \ue621  \ue621  \ue621  \ue621  \ue621  \ue621  \ue621  \ue621  \ue621  \ue621  \ue621  \ue621  \ue621  \ue621  \ue621  \x1b[35mnegative_habit_02\n\x1b[37m \ue621  \ue621  \ue621  \ue621  \ue621  \ue621  \ue621  \ue621  \ue621  \uf444  \ue621  \uf444  \ue621  \ue621  \ue621  \ue621  \ue621  \ue621  \ue621  \ue621  \ue621  \ue621  \ue621  \ue621  \uf444  \ue621  \ue621  \ue621  \ue621  \ue621  \x1b[35mnegative_habit_01\n\x1b[35m01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 \n\x1b[35m M  M  J  V  S  D  L  M  M  J  V  S  D  L  M  M  J  V  S  D  L  M  M  J  V  S  D  L  M  M "

    assert negative_habits_graph == expected_negative_habits_graph


def test__group_data_by_value():
    # GIVEN
    graphic_tool = ConsoleGraphicTool()
    data = [
        # Single values
        {
            "date": "2025-04-01 08:16:04 PM",
            "year": "2025",
            "month": "4",
            "day": "1",
            "week_number": "14",
            "description": "Sueño",
            "value": "8",
            "tag": "Health",
        },
        {
            "date": "2025-04-01 08:16:04 PM",
            "year": "2025",
            "month": "4",
            "day": "3",
            "week_number": "14",
            "description": "Sueño",
            "value": "9",
            "tag": "Health",
        },
        # Repeated on value 7 and day 1
        {
            "date": "2025-04-01 08:16:04 PM",
            "year": "2025",
            "month": "4",
            "day": "1",
            "week_number": "14",
            "description": "Sueño",
            "value": "7",
            "tag": "Health",
        },
        {
            "date": "2025-04-01 08:16:04 PM",
            "year": "2025",
            "month": "4",
            "day": "1",
            "week_number": "14",
            "description": "Humor",
            "value": "7",
            "tag": "Health",
        },
    ]
    # THEN
    data_by_value = graphic_tool._group_data_by_value(data=data)

    assert len(data_by_value) == 3
    assert len(data_by_value[7]) == 2
    assert len(data_by_value[8]) == 1
    assert len(data_by_value[9]) == 1

    expected_data = {
        7: [
            {
                "date": "2025-04-01 08:16:04 PM",
                "year": "2025",
                "month": "4",
                "day": "1",
                "week_number": "14",
                "description": "Sueño",
                "value": "7",
                "tag": "Health",
            },
            {
                "date": "2025-04-01 08:16:04 PM",
                "year": "2025",
                "month": "4",
                "day": "1",
                "week_number": "14",
                "description": "Humor",
                "value": "7",
                "tag": "Health",
            },
        ],
        8: [
            {
                "date": "2025-04-01 08:16:04 PM",
                "year": "2025",
                "month": "4",
                "day": "1",
                "week_number": "14",
                "description": "Sueño",
                "value": "8",
                "tag": "Health",
            }
        ],
        9: [
            {
                "date": "2025-04-01 08:16:04 PM",
                "year": "2025",
                "month": "4",
                "day": "3",
                "week_number": "14",
                "description": "Sueño",
                "value": "9",
                "tag": "Health",
            }
        ],
    }
    __import__("ipdb").set_trace()
    assert data_by_value == expected_data


def test__generate_humor_value_string():
    # GIVEN
    graphic_tool = ConsoleGraphicTool()
    day_value_data = [
        # Repeated on value 7 and day 1
        {
            "date": "2025-04-01 08:16:04 PM",
            "year": "2025",
            "month": "4",
            "day": "1",
            "week_number": "14",
            "description": "Sueño",
            "value": "7",
            "tag": "Health",
        },
        {
            "date": "2025-04-01 08:16:04 PM",
            "year": "2025",
            "month": "4",
            "day": "1",
            "week_number": "14",
            "description": "Humor",
            "value": "7",
            "tag": "Health",
        },
        {
            "date": "2025-04-01 08:16:04 PM",
            "year": "2025",
            "month": "4",
            "day": "1",
            "week_number": "14",
            "description": "Estres",
            "value": "7",
            "tag": "Health",
        },
    ]
    # THEN
    humor_string = graphic_tool._generate_humor_value_string(day_value_data=day_value_data)

    assert humor_string == "\x1b[32m\uf0de"

    # GIVEN
    day_value_data = [
        {
            "date": "2025-04-01 08:16:04 PM",
            "year": "2025",
            "month": "4",
            "day": "1",
            "week_number": "14",
            "description": "Humor",
            "value": "5",
            "tag": "Health",
        },
    ]

    # THEN
    humor_string = graphic_tool._generate_humor_value_string(day_value_data=day_value_data)

    assert humor_string == "\x1b[33m\uf0de"

    # GIVEN
    day_value_data = [
        {
            "date": "2025-04-01 08:16:04 PM",
            "year": "2025",
            "month": "4",
            "day": "1",
            "week_number": "14",
            "description": "Humor",
            "value": "2",
            "tag": "Health",
        },
    ]

    # THEN
    humor_string = graphic_tool._generate_humor_value_string(day_value_data=day_value_data)

    assert humor_string == "\x1b[31m\uf0de"


def test__generate_stress_value_string():
    # GIVEN
    graphic_tool = ConsoleGraphicTool()
    day_value_data = [
        # Repeated on value 7 and day 1
        {
            "date": "2025-04-01 08:16:04 PM",
            "year": "2025",
            "month": "4",
            "day": "1",
            "week_number": "14",
            "description": "Sueño",
            "value": "7",
            "tag": "Health",
        },
        {
            "date": "2025-04-01 08:16:04 PM",
            "year": "2025",
            "month": "4",
            "day": "1",
            "week_number": "14",
            "description": "Humor",
            "value": "7",
            "tag": "Health",
        },
        {
            "date": "2025-04-01 08:16:04 PM",
            "year": "2025",
            "month": "4",
            "day": "1",
            "week_number": "14",
            "description": "Estres",
            "value": "7",
            "tag": "Health",
        },
    ]
    # THEN
    humor_string = graphic_tool._generate_stress_value_string(day_value_data=day_value_data)

    assert humor_string == "\x1b[31m\uf467"

    # GIVEN
    day_value_data = [
        {
            "date": "2025-04-01 08:16:04 PM",
            "year": "2025",
            "month": "4",
            "day": "1",
            "week_number": "14",
            "description": "Estres",
            "value": "3",
            "tag": "Health",
        },
    ]

    # THEN
    humor_string = graphic_tool._generate_stress_value_string(day_value_data=day_value_data)

    assert humor_string == "\x1b[33m\uf467"

    # GIVEN
    day_value_data = [
        {
            "date": "2025-04-01 08:16:04 PM",
            "year": "2025",
            "month": "4",
            "day": "1",
            "week_number": "14",
            "description": "Estres",
            "value": "2",
            "tag": "Health",
        },
    ]

    # THEN
    humor_string = graphic_tool._generate_stress_value_string(day_value_data=day_value_data)

    assert humor_string == "\x1b[32m\uf467"


def test__generate_sleep_value_string():
    # GIVEN
    graphic_tool = ConsoleGraphicTool()
    day_value_data = [
        # Repeated on value 7 and day 1
        {
            "date": "2025-04-01 08:16:04 PM",
            "year": "2025",
            "month": "4",
            "day": "1",
            "week_number": "14",
            "description": "Sueño",
            "value": "7",
            "tag": "Health",
        },
        {
            "date": "2025-04-01 08:16:04 PM",
            "year": "2025",
            "month": "4",
            "day": "1",
            "week_number": "14",
            "description": "Humor",
            "value": "7",
            "tag": "Health",
        },
        {
            "date": "2025-04-01 08:16:04 PM",
            "year": "2025",
            "month": "4",
            "day": "1",
            "week_number": "14",
            "description": "Estres",
            "value": "7",
            "tag": "Health",
        },
    ]
    # THEN
    sleep_string = graphic_tool._generate_sleep_value_string(day_value_data=day_value_data)

    assert sleep_string == "\x1b[32m\uf444"

    # GIVEN
    day_value_data = [
        {
            "date": "2025-04-01 08:16:04 PM",
            "year": "2025",
            "month": "4",
            "day": "1",
            "week_number": "14",
            "description": "Sueño",
            "value": "5",
            "tag": "Health",
        },
    ]

    # THEN
    sleep_string = graphic_tool._generate_sleep_value_string(day_value_data=day_value_data)

    assert sleep_string == "\x1b[33m\uf444"

    # GIVEN
    day_value_data = [
        {
            "date": "2025-04-01 08:16:04 PM",
            "year": "2025",
            "month": "4",
            "day": "1",
            "week_number": "14",
            "description": "Sueño",
            "value": "2",
            "tag": "Health",
        },
    ]

    # THEN
    sleep_string = graphic_tool._generate_sleep_value_string(day_value_data=day_value_data)

    assert sleep_string == "\x1b[31m\uf444"


def test_generate_health_graph():
    # GIVEN
    graphic_tool = ConsoleGraphicTool()
    file_path = f"{JRNL_DIR}/2025/04/monthly_habits_data.csv"

    # THEN
    health_graph = graphic_tool.generate_health_graph(file_path=file_path)
    expected_health_graph = "\uf0de : Humor \uf444 : Sleep \uf467 : Stress\n        \x1b[32m\uf444                    \x1b[32m\uf444        \x1b[32m\uf444     \x1b[32m\uf444  \x1b[32m\uf444                                           \x1b[35m9\n     \x1b[32m\uf444     \x1b[32m\uf444  \x1b[32m\uf444           \x1b[32m\uf444     \x1b[32m\uf444\x1b[32m\uf0de \x1b[32m\uf444\x1b[32m\uf0de    \x1b[32m\uf444        \x1b[32m\uf444     \x1b[32m\uf444  \x1b[32m\uf444\x1b[32m\uf0de \x1b[32m\uf444\x1b[32m\uf0de       \x1b[32m\uf444  \x1b[32m\uf444                \x1b[35m8\n  \x1b[32m\uf444      \x1b[32m\uf0de           \x1b[32m\uf0de  \x1b[32m\uf0de                       \x1b[32m\uf0de  \x1b[32m\uf0de \x1b[32m\uf444           \x1b[32m\uf444         \x1b[32m\uf0de \x1b[32m\uf444  \x1b[32m\uf444\x1b[32m\uf0de \x1b[32m\uf444\x1b[32m\uf0de \x1b[32m\uf444  \x1b[32m\uf444 \x1b[35m7\n   \x1b[32m\uf0de  \x1b[32m\uf0de     \x1b[32m\uf0de  \x1b[32m\uf0de \x1b[33m\uf444  \x1b[33m\uf444  \x1b[33m\uf444   \x1b[32m\uf0de  \x1b[32m\uf0de        \x1b[32m\uf0de  \x1b[32m\uf0de  \x1b[32m\uf0de        \x1b[32m\uf0de  \x1b[32m\uf0de        \x1b[32m\uf0de \x1b[33m\uf444\x1b[32m\uf0de        \x1b[32m\uf0de        \x1b[32m\uf0de   \x1b[35m6\n\x1b[33m\uf0de                 \x1b[33m\uf0de                                                     \x1b[33m\uf0de                  \x1b[35m5\n       \x1b[33m\uf467                 \x1b[33m\uf467                                      \x1b[33m\uf467                 \x1b[33m\uf467        \x1b[35m4\n \x1b[33m\uf467                                                                          \x1b[33m\uf467  \x1b[33m\uf467           \x1b[35m3\n                   \x1b[32m\uf467                 \x1b[32m\uf467  \x1b[32m\uf467  \x1b[32m\uf467        \x1b[32m\uf467              \x1b[32m\uf467     \x1b[32m\uf467                 \x1b[35m2\n    \x1b[32m\uf467     \x1b[32m\uf467  \x1b[32m\uf467  \x1b[32m\uf467     \x1b[32m\uf467     \x1b[32m\uf467  \x1b[32m\uf467  \x1b[32m\uf467           \x1b[32m\uf467  \x1b[32m\uf467     \x1b[32m\uf467  \x1b[32m\uf467  \x1b[32m\uf467        \x1b[32m\uf467              \x1b[32m\uf467  \x1b[32m\uf467  \x1b[35m1\n\x1b[35m01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 \n\x1b[35m M  M  J  V  S  D  L  M  M  J  V  S  D  L  M  M  J  V  S  D  L  M  M  J  V  S  D  L  M  M "

    assert health_graph == expected_health_graph


@pytest.mark.skip("Debugging purposes")
def test_debug():
    # GIVEN
    graphic_tool = ConsoleGraphicTool()
    file_path = f"{JRNL_DIR}/2025/04/monthly_habits_data.csv"

    # THEN
    dock = graphic_tool.generate_health_graph(file_path=file_path)
    __import__("ipdb").set_trace()
