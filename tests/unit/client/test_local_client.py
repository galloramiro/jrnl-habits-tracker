import pytest

from src.client.local_client import LocalClient, LocalClientError


def test_get_file_paths_by_month():
    client = LocalClient()

    # GIVEN
    month = 4

    # THEN
    april_2025_files = client.get_file_paths_by_month(month=month)
    assert len(april_2025_files) == 32

    # GIVEN
    month = 12
    year = 2024
    december_2024_files = client.get_file_paths_by_month(month=month, year=year)
    assert len(december_2024_files) == 31

    # GIVEN
    month = 11
    year = 2024

    # THEN
    november_2024_files = client.get_file_paths_by_month(month=month, year=year)
    assert len(november_2024_files) == 1


def test_get_file_paths_by_month_error():
    client = LocalClient()

    # GIVEN
    month = 13

    # THEN
    with pytest.raises(LocalClientError):
        client.get_file_paths_by_month(month=month)


def test_get_jrnl_files_path_by_month():
    client = LocalClient()

    # GIVEN
    month = 4

    # THEN
    april_2025_files = client.get_jrnl_files_path_by_month(month=month)
    assert len(april_2025_files) == 30


def test_get_jrnl_files_path_by_month_not_file_found():
    client = LocalClient()

    # GIVEN
    month = 11
    year = 2024

    # THEN
    with pytest.raises(LocalClientError):
        client.get_jrnl_files_path_by_month(month=month, year=year)

def test_get_monthly_habits_by_month():
    client = LocalClient()

    # GIVEN
    month = 4

    # THEN
    april_2025_files = client.get_monthly_habits_by_month(month=month)
    assert april_2025_files == "/app/examples/jrnl-dir/2025/04/monthly_habits_data.csv"


def test_get_monthly_habits_by_month_not_file_found():
    client = LocalClient()

    # GIVEN
    month = 11
    year = 2024

    # THEN
    with pytest.raises(LocalClientError):
        client.get_monthly_habits_by_month(month=month, year=year)


def test__check_path_exist():
    client = LocalClient()

    # GIVEN
    path = "./examples/jrnl-dir/2025/04"

    # THEN
    assert client._check_path_exist(path=path) == True

    # GIVEN
    path = "./examples/jrnl-dir/2025/13"

    # THEN
    with pytest.raises(LocalClientError):
        client._check_path_exist(path=path)

def test__check_files_exist():
    client = LocalClient()

    # GIVEN
    paths_list = ["./examples/jrnl-dir/2025/04/01.txt", "./examples/jrnl-dir/2025/04/02.txt"]

    # THEN
    assert client._check_files_exist(paths_list=paths_list)

    # GIVEN
    paths_list = []

    # THEN
    with pytest.raises(LocalClientError):
        client._check_files_exist(paths_list=paths_list)