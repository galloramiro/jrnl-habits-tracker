import csv
import pytest
import os

from src.data_processor.dto import MonthlyTitleRow, MonthlyHabitsRow
from src.repository.csv_repository import CsvRepository, CsvRepositoryError


def test_save_monthly_habits_rows():
    # Given
    year = 2024
    month = 11
    csv_repository = CsvRepository()
    rows = [
        MonthlyHabitsRow(
            date=f"{year}-{month}-01 12:00:00 PM",
            year=year,
            month=month,
            week_number=1,
            day=5,
            description="SomeDescription",
            value=1,
            tag="SuperTag",
        ),
        MonthlyHabitsRow(
            date=f"{year}-{month}-01 12:00:00 PM",
            year=year,
            month=month,
            week_number=1,
            day=5,
            description="SomeOtherDescription",
            value=0,
            tag="SuperTag",
        ),
    ]

    # When
    file_path = csv_repository.save_monthly_habits_rows(rows=rows)

    # Then
    assert file_path == f"/app/examples/jrnl-dir/{year}/{month}/monthly_habits_data.csv"
    assert os.path.exists(file_path)

    os.remove(file_path)


def test_save_monthly_titles_rows():
    # Given
    year = 2024
    month = 11
    csv_repository = CsvRepository()
    rows = [
        MonthlyTitleRow(
            date=f"{year}-{month}-01 12:00:00 PM",
            year=year,
            month=month,
            week_number=1,
            weekday_number=4,
            time="12:00:00",
            title="title1",
        ),
        MonthlyTitleRow(
            date=f"{year}-{month}-02 12:00:00 PM",
            year=year,
            month=month,
            week_number=1,
            weekday_number=5,
            time="12:00:00",
            title="title1",
        ),
    ]

    # When
    file_path = csv_repository.save_monthly_titles_rows(rows=rows)

    # Then
    assert file_path == f"/app/examples/jrnl-dir/{year}/{month}/monthly_titles_data.csv"
    assert os.path.exists(file_path)

    os.remove(file_path)


def test__save_rows():
    # Given
    year = 2024
    month = 11
    file_path = f"/app/examples/jrnl-dir/{year}/{month}/monthly_titles_data.csv"
    headers = [
        "date",
        "title",
        "year",
        "month",
        "week_number",
        "weekday_number",
        "time",
    ]
    rows = [
        MonthlyTitleRow(
            date=f"{year}-{month}-01 12:00:00 PM",
            year=year,
            month=month,
            week_number=1,
            weekday_number=4,
            time="12:00:00",
            title="title1",
        ),
        MonthlyTitleRow(
            date=f"{year}-{month}-02 12:00:00 PM",
            year=year,
            month=month,
            week_number=1,
            weekday_number=5,
            time="12:00:00",
            title="title1",
        ),
    ]

    # When
    CsvRepository._save_rows(headers=headers, rows=rows, file_path=file_path)

    # Then
    assert os.path.exists(file_path)

    with open(file_path, mode="r") as file:
        reader = csv.DictReader(file)
        header = list(reader.fieldnames)
        header.sort()
        expected_headers = [
            "date",
            "title",
            "year",
            "month",
            "week_number",
            "weekday_number",
            "time",
        ]
        expected_headers.sort()
        assert header == expected_headers

        rows = list(reader)
        assert len(rows) == 2

    os.remove(file_path)


def test__save_rows_with_error():
    # Given
    csv_repository = CsvRepository()
    headers = []
    rows = None

    # THEN
    with pytest.raises(CsvRepositoryError):
        csv_repository._save_rows(headers=None, rows=None, file_path=None)
