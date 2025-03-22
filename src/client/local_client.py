import os
from datetime import datetime
from typing import List

from src.config import JRNL_DIR, LOGGER


class LocalClientError(Exception):
    """Raised when we find errors"""

    def __init__(self, path: str, description: str):
        self.description = description
        self.path = path
        self.message = f"Error when {description} in path: {path}"
        super().__init__(self.message)


class LocalClient:
    _JRNL_DIR = JRNL_DIR

    def get_file_paths_by_month(self, month: int, year: int = datetime.now().year) -> List[str]:
        """
        Get all the files in a month and year.

        :param month: month number
        :param year: year number
        :return: List of paths to the files
        :raise LocalClientError
        """
        month = str(month).zfill(2)
        files_path = os.path.abspath(f"{self._JRNL_DIR}/{year}/{month}")
        self._check_path_exist(path=files_path)

        files = []
        for file in os.listdir(files_path):
            files.append(os.path.join(files_path, file))

        number_of_files = len(files)
        LOGGER.info(
            f"We find {number_of_files} files in the following path: {files_path}",
            extra={"month_path": files_path, "number_of_files": number_of_files},
        )
        files.sort()
        return files

    def get_jrnl_files_path_by_month(self, month: int, year: int = datetime.now().year) -> List[str]:
        all_files = self.get_file_paths_by_month(month=month, year=year)
        jrnl_files = list(filter(lambda file: file.endswith(".txt"), all_files))
        self._check_files_exist(paths_list=jrnl_files)
        number_of_files = len(jrnl_files)
        LOGGER.info(
            f"We find {number_of_files} jrnl files for year: {year} month: {month}",
            extra={"month": month, "year": year, "number_of_files": number_of_files},
        )
        return jrnl_files

    def get_monthly_habits_by_month(self, month: int, year: int = datetime.now().year) -> str:
        file_name = "monthly_habits_data"
        all_files = self.get_file_paths_by_month(month=month, year=year)
        monthly_habit_files = list(filter(lambda file: file_name in file, all_files))
        self._check_files_exist(paths_list=monthly_habit_files)
        file_path = monthly_habit_files[0]
        LOGGER.info(
            f"We find {file_path} file for year: {year} month: {month}",
            extra={"month": month, "year": year},
        )
        return file_path

    def get_monthly_habits_files_paths_by_year(self, month: int) -> List[str]:
        raise NotImplementedError

    def get_monthly_titles_by_month(self, month: int) -> List[str]:
        raise NotImplementedError

    def get_monthly_titles_files_paths_by_year(self, month: int) -> List[str]:
        raise NotImplementedError

    @staticmethod
    def _check_path_exist(path: str) -> bool:
        if not os.path.exists(path):
            LOGGER.error(
                f"The path does not exist: {path}",
                extra={"path": path},
            )
            raise LocalClientError(path=path, description="_check_path_exist")
        return True

    @staticmethod
    def _check_files_exist(paths_list: List[str]) -> bool:
        number_of_files = len(paths_list)
        if not number_of_files:
            LOGGER.error(
                f"We didn't find files",
                extra={"paths_list": paths_list},
            )
            raise LocalClientError(path="", description="_check_files_exist")
        return True
