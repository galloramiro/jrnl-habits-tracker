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
            if file.endswith(".txt"):
                files.append(os.path.join(files_path, file))

        number_of_files = len(files)
        self._check_files_exist(files_path, number_of_files)

        LOGGER.info(
            f"We find {number_of_files} files in the following path: {files_path}",
            extra={"month_path": files_path, "number_of_files": number_of_files},
        )
        files.sort()
        return files

    def get_jrnl_files_path_by_month(self, month: int) -> List[str]:
        raise NotImplementedError

    def get_monthly_habits_by_month(self, month: int) -> List[str]:
        raise NotImplementedError

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
    def _check_files_exist(files_path, number_of_files) -> bool:
        if not number_of_files:
            LOGGER.error(
                f"We didn't find files in the following path: {files_path}",
                extra={"files_path": files_path, "number_of_files": number_of_files},
            )
            raise LocalClientError(path=files_path, description="_check_files_exist")
        return True