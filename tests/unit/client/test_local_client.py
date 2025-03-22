import pytest

from src.client.local_client import LocalClient, LocalClientError


def test_get_file_paths_by_month():
    client = LocalClient()

    # GIVEN
    month = 4

    # THEN
    april_2025_files = client.get_file_paths_by_month(month=month)
    assert len(april_2025_files) == 30

    # GIVEN
    month = 12
    year = 2024
    december_2024_files = client.get_file_paths_by_month(month=month, year=year)
    assert len(december_2024_files) == 31


def test_get_file_paths_by_month_error():
    client = LocalClient()

    # GIVEN
    month = 13

    # THEN
    with pytest.raises(LocalClientError):
        client.get_file_paths_by_month(month=month)

    # GIVEN
    month = 11
    year = 2024

    # THEN
    with pytest.raises(LocalClientError):
        client.get_file_paths_by_month(month=month, year=year)

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
    files_path = "./examples/jrnl-dir/2025/04"
    number_of_files = 30

    # THEN
    assert client._check_files_exist(files_path=files_path, number_of_files=number_of_files) == True

    # GIVEN
    files_path = "./examples/jrnl-dir/2024/11"
    number_of_files = 0

    # THEN
    with pytest.raises(LocalClientError):
        client._check_files_exist(files_path=files_path, number_of_files=number_of_files)